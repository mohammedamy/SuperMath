"""Kangaroo Math Competition — Benjamin Division (Grades 5–6) 360-Question Bank."""
import math
from fractions import Fraction

from kangaroo_common import (
    m,
    make_5_bilingual_options,
    make_kang_q,
    make_kangaroo_question,
    svg_balance_scales,
    svg_bar_chart,
    svg_column_cryptarithm,
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digital_clock,
    svg_digit_slots,
    svg_equilateral_corner_cuts,
    svg_fraction_grid,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_grid_polygon,
    svg_inscribed_corner_triangle_in_rect,
    svg_kang_cube_faces,
    svg_kang_gear_train,
    svg_kang_magic_cross,
    svg_kang_matchstick_digits,
    svg_kang_necklace_beads,
    svg_kang_overlapping_rects,
    svg_kang_polyomino_board,
    svg_kang_staircase_perimeter,
    svg_magic_square_3x3,
    svg_number_line_jumps,
    svg_number_strip,
    svg_overlapping_rects,
    svg_painted_cube_3d,
    svg_paper_fold,
    svg_parallel_zigzag,
    svg_pie_chart,
    svg_polyomino,
    svg_rectilinear_staircase,
    svg_regular_polygon,
    svg_round_table,
    svg_shaded_triangle_in_rect,
    svg_spinner,
    svg_square_eighths_shaded,
    svg_street_grid,
    svg_subdivided_rect_2x2,
    svg_travel_map,
    svg_two_jars,
    svg_venn_2,
    svg_water_cups,
)
from kmc_common import explain_ar, explain_en

LEVEL = "Benjamin"
SEG_COUNTS = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}


def _unit_1() -> list[dict]:
    qs: list[dict] = []
    seg_bits = {
        "0": (1, 1, 1, 1, 1, 1, 0),
        "1": (0, 1, 1, 0, 0, 0, 0),
        "2": (1, 1, 0, 1, 1, 0, 1),
        "3": (1, 1, 1, 1, 0, 0, 1),
        "4": (0, 1, 1, 0, 0, 1, 1),
        "5": (1, 0, 1, 1, 0, 1, 1),
        "6": (1, 0, 1, 1, 1, 1, 1),
        "7": (1, 1, 1, 0, 0, 0, 0),
        "8": (1, 1, 1, 1, 1, 1, 1),
        "9": (1, 1, 1, 1, 0, 1, 1),
    }

    # --- 1. kang_ben_divisibility_digits (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_div = [
        (4, 8, 3, "library pass code", "رمز بطاقة المكتبة"),
        (7, 5, 2, "planetarium locker code", "رمز خزانة القبة السماوية"),
        (6, 7, 1, "botanical greenhouse tag", "بطاقة الدفيئة النباتية"),
        (8, 6, 5, "robotics badge number", "رقم شارة نادي الروبوت"),
        (3, 9, 4, "science museum ticket", "تذكرة متحف العلوم"),
    ]
    for a, b, c, ctx_en, ctx_ar in easy_div:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        valid = [d for d in range(10) if int(f"{a}{b}{d}{c}") % 9 == 0]
        assert len(valid) == 1
        ans = valid[0]
        full_n = int(f"{a}{b}{ans}{c}")
        s_known = a + b + c
        nxt_mult = ((s_known // 9) + 1) * 9
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Easy", "kang_ben_divisibility_digits",
            f"A four-digit {ctx_en} has the form {m(f'\\overline{{{a}{b}d{c}}}')} and is divisible by {m(9)}. What is the missing digit {m('d')}?",
            f"يتكوّن {ctx_ar} من أربع خانات على الصورة {m(f'\\overline{{{a}{b}d{c}}}')} ويقبل القسمة على {m(9)}. ما قيمة الرقم المفقود {m('d')}؟",
            ans, [ans + 1, max(0, ans - 1), (ans + 3) % 10, (9 - ans) % 10],
            "Add the known digits and make the total digit sum a multiple of 9.",
            "اجمع الأرقام المعروفة واجعل مجموع الخانات من مضاعفات العدد 9.",
            "A whole number is divisible by 9 if and only if the sum of its digits is divisible by 9.",
            [f"Known digit sum: {m(f'{a} + {b} + {c} = {s_known}')}.", f"The only multiple of {m(9)} reachable by {m(f'{s_known} + d')} is {m(nxt_mult)}, so {m(f'd = {nxt_mult} - {s_known} = {ans}')}."],
            f"{m(f'{full_n} \\div 9 = {full_n // 9}')} exactly.",
            "يقبل العدد القسمة على 9 إذا وفقط إذا كان مجموع أرقامه من مضاعفات 9.",
            [f"مجموع الأرقام المعلومة: {m(f'{a} + {b} + {c} = {s_known}')}.", f"المضاعف الوحيد للعدد {m(9)} الممكن للعدد {m(f'{s_known} + d')} هو {m(nxt_mult)}، ومنه {m(f'd = {ans}')}."],
            f"تحقق: {m(f'{full_n} \\div 9 = {full_n // 9}')} بدون باقٍ.",
            diagram_en=svg_digit_slots([str(a), str(b), "d", str(c)], "Multiple of 9"),
            diagram_ar=svg_digit_slots([str(a), str(b), "d", str(c)], "مضاعف للعدد 9"),
        ))

    med_div = [
        (5, 3, 2, 6, "max", "origami club serial", "الرقم التسلسلي لنادي الأوريغامي"),
        (7, 1, 6, 4, "sum", "chess tournament ID", "معرّف بطولة الشطرنج"),
        (8, 2, 4, 6, "max", "astronomy camp badge", "شارة مخيم الفلك"),
        (4, 9, 2, 12, "max", "aquarium pass number", "رقم تصريح حوض الأسماك"),
        (6, 5, 6, 4, "sum", "math relay bib code", "رمز متسابق تتابع الرياضيات"),
    ]
    for a, b, c, dv, mode, ctx_en, ctx_ar in med_div:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        # Number form: a b d c
        valid = [d for d in range(10) if int(f"{a}{b}{d}{c}") % dv == 0]
        ans = max(valid) if mode == "max" else sum(valid)
        ask_en = f"What is the **largest** possible digit {m('d')}?" if mode == "max" else f"What is the **sum of all** possible digits {m('d')}?"
        ask_ar = f"ما **أكبر** قيمة ممكنة للرقم {m('d')}؟" if mode == "max" else f"ما **مجموع جميع** القيم الممكنة للرقم {m('d')}؟"
        v_str = ", ".join(str(v) for v in valid)
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Medium", "kang_ben_divisibility_digits",
            f"The four-digit {ctx_en} {m(f'\\overline{{{a}{b}d{c}}}')} is divisible by {m(dv)}. {ask_en}",
            f"إن {ctx_ar} المكوّن من أربع خانات {m(f'\\overline{{{a}{b}d{c}}}')} يقبل القسمة على {m(dv)}. {ask_ar}",
            ans, [ans - 2, ans + 2, ans + 4, valid[0]],
            f"Check the divisibility rule for {dv} on the tens-and-units pair d{c} and the digit sum.",
            f"افحص قاعدة قابلية القسمة على {dv} على آخر خانتين وعلى مجموع الأرقام.",
            f"Test digits {m('d \\in \\{0,\\dots,9\\}')} using the factor rules of {m(dv)}.",
            [f"Testing {m(f'\\overline{{{a}{b}d{c}}}')} for divisibility by {m(dv)} gives valid digits {m(f'd \\in \\{{{v_str}\\}}')}.",
             f"Therefore the requested {'largest digit' if mode == 'max' else 'sum of valid digits'} is {m(ans)}."],
            f"All matching numbers ({', '.join(f'{a}{b}{v}{c}' for v in valid)}) divide cleanly by {m(dv)}.",
            f"نفحص القيم الممكنة للرقم {m('d')} وفق قواعد قابلية القسمة على {m(dv)}.",
            [f"القيم التي تجعل {m(f'\\overline{{{a}{b}d{c}}}')} يقبل القسمة على {m(dv)} هي {m(f'\\{{{v_str}\\}}')}.",
             f"وبالتالي فإن {'أكبر رقم ممكن' if mode == 'max' else 'مجموع القيم الممكنة'} يساوي {m(ans)}."],
            f"جميع الأعداد الناتجة تقبل القسمة على {m(dv)} تماماً.",
            diagram_en=svg_digit_slots([str(a), str(b), "d", str(c)], f"Divisible by {dv}"),
            diagram_ar=svg_digit_slots([str(a), str(b), "d", str(c)], f"يقبل على {dv}"),
        ))

    hard_div = [
        (3, 5, 2, 36, "max", "five-digit Kangaroo vault code", "رمز خزنة الكانجارو الخماسي"),
        (6, 4, 1, 45, "max", "five-digit solar rover ID", "معرّف العربة الشمسية الخماسي"),
        (7, 2, 3, 36, "min", "five-digit archive serial", "الرقم الأرشيفي الخماسي"),
        (5, 1, 6, 72, "max", "five-digit observatory key", "مفتاح المرصد الفلكي الخماسي"),
        (8, 3, 7, 45, "min", "five-digit math camp voucher", "قسيمة مخيم الرياضيات الخماسية"),
    ]
    for a, b, c, dv, mode, ctx_en, ctx_ar in hard_div:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        # Number form: a x b c y
        pairs = [(x, y) for x in range(10) for y in range(10) if int(f"{a}{x}{b}{c}{y}") % dv == 0]
        sums = [x + y for x, y in pairs]
        ans = max(sums) if mode == "max" else min(sums)
        best_xy = next((x, y) for x, y in pairs if x + y == ans)
        best_n = int(f"{a}{best_xy[0]}{b}{c}{best_xy[1]}")
        f1, f2 = (4, 9) if dv == 36 else ((5, 9) if dv == 45 else (8, 9))
        word_en = "largest" if mode == "max" else "smallest"
        word_ar = "أكبر" if mode == "max" else "أصغر"
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Hard", "kang_ben_divisibility_digits",
            f"A {ctx_en} has the form {m(f'\\overline{{{a}x{b}{c}y}}')} and is divisible by {m(dv)}. What is the **{word_en}** possible value of {m('x + y')}?",
            f"يتكوّن {ctx_ar} على الصورة {m(f'\\overline{{{a}x{b}{c}y}}')} ويقبل القسمة على {m(dv)}. ما **{word_ar}** قيمة ممكنة للمجموع {m('x + y')}؟",
            ans, [ans - 2, ans - 1, ans + 1, ans + 3],
            f"Split {dv} into coprime factors {f1} and {f2}: find valid choices for y first, then solve for x using the rule of 9!",
            f"فكّك {dv} إلى العاملين {f1} و{f2}: حدّد قيم y المسموحة أولاً ثم أوجد x بقاعدة القسمة على 9!",
            f"Divisibility by {m(dv)} requires divisibility by both {m(f1)} and {m(f2)}.",
            [f"Apply the rule of {m(f1)} to the ending digits to narrow {m('y')}, then use {m(f'9 \\mid ({a}+x+{b}+{c}+y)')}.",
             f"Checking all valid pairs gives optimal pair {m(f'(x, y) = ({best_xy[0]}, {best_xy[1]})')}, so {m(f'x + y = {ans}')}."],
            f"{m(f'{best_n} \\div {dv} = {best_n // dv}')} is an integer!",
            f"القسمة على {m(dv)} تكافئ القسمة على {m(f1)} و{m(f2)} معاً.",
            [f"نحدّد قيم {m('y')} من شرط القسمة على {m(f1)}، ثم نطبّق قاعدة {m(9)} على مجموع الأرقام {m(f'{a}+x+{b}+{c}+y')}.",
             f"الزوج الأمثل هو {m(f'(x, y) = ({best_xy[0]}, {best_xy[1]})')} فيكون المجموع {m(f'x + y = {ans}')}."],
            f"تحقق: {m(f'{best_n} \\div {dv} = {best_n // dv}')}.",
            diagram_en=svg_digit_slots([str(a), "x", str(b), str(c), "y"], f"Divisible by {dv}"),
            diagram_ar=svg_digit_slots([str(a), "x", str(b), str(c), "y"], f"يقبل على {dv}"),
        ))

    # --- 2. kang_ben_lcm_meeting_cycles (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_lcm = [
        (4, 6, "park fountains spray water", "تنفث نافورتا الحديقة الماء"),
        (6, 9, "shuttle trams depart the plaza", "تنطلق حافلتا الساحة"),
        (8, 10, "observatory chimes ring", "يدقّ جرسا المرصد"),
        (9, 12, "greenhouse misters turn on", "تعمل رشاشات الدفيئة"),
        (10, 15, "harbor water-taxis dock", "ترسو قوارب الميناء"),
    ]
    for p1, p2, ev_en, ev_ar in easy_lcm:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        ans = math.lcm(p1, p2)
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Easy", "kang_ben_lcm_meeting_cycles",
            f"Two {ev_en} every {m(p1)} minutes and every {m(p2)} minutes respectively. If both happen together right now, in how many minutes will they **next** happen at the exact same time?",
            f"{ev_ar} كل {m(p1)} دقائق وكل {m(p2)} دقائق على الترتيب. إذا حدث ذلك معاً الآن، فبعد كم دقيقة سيتكرر حدوثهما معاً **للمرة التالية**؟",
            ans, [p1 + p2, p1 * p2, ans // 2, ans + p1],
            "Find the Least Common Multiple (LCM) of the two cycle lengths.",
            "أوجد المضاعف المشترك الأصغر لطولَي الدورتين.",
            "Two periodic events coincide again at the Least Common Multiple of their periods.",
            [f"Multiples of {m(p1)}: {m(f'{p1}, {2*p1}, {3*p1}, \\dots')}.",
             f"The smallest positive number also divisible by {m(p2)} is {m(f'\\operatorname{{lcm}}({p1}, {p2}) = {ans}')} minutes."],
            f"{m(f'{ans} \\div {p1} = {ans // p1}')} cycles and {m(f'{ans} \\div {p2} = {ans // p2}')} cycles.",
            "يلتقي الحدثان الدوريان عند المضاعف المشترك الأصغر لزمنيهما.",
            [f"مضاعفات {m(p1)} هي {m(f'{p1}, {2*p1}, {3*p1}, \\dots')}.",
             f"أصغر مضاعف مشترك يقبل القسمة أيضاً على {m(p2)} هو {m(ans)} دقيقة."],
            f"تحقق: {m(f'{ans} \\div {p1} = {ans // p1}')} و{m(f'{ans} \\div {p2} = {ans // p2}')}.",
            diagram_en=svg_number_strip(["0", str(p1), str(2 * p1), "...", "?"]),
        ))

    med_jumps = [
        (5, 2, 17, "baby kangaroo", "كانجارو صغير"),
        (6, 2, 22, "desert jerboa", "يربوع صحراوي"),
        (7, 3, 23, "clockwork frog", "ضفدع آلي"),
        (8, 3, 28, "spring robot", "روبوت نابض"),
        (9, 4, 29, "grasshopper", "جندب رشيق"),
    ]
    for fwd, back, target, ch_en, ch_ar in med_jumps:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        pos, jumps = 0, 0
        while pos < target:
            jumps += 1
            pos += fwd if jumps % 2 == 1 else -back
        net = fwd - back
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Medium", "kang_ben_lcm_meeting_cycles",
            f"Starting at {m(0)} on a number line, a {ch_en} jumps {m(f'+{fwd}')} units forward on every odd-numbered jump and {m(f'-{back}')} units backward on every even-numbered jump. How many **total jumps** does it take to reach or pass {m(target)} for the **first** time?",
            f"ينطلق {ch_ar} من النقطة {m(0)} على خط الأعداد فيقفز {m(f'+{fwd}')} وحدات للأمام في كل قفزة فردية الترتيب ويعود {m(f'-{back}')} وحدات للخلف في كل قفزة زوجية الترتيب. كم **قفزة إجمالية** يحتاج للوصول إلى {m(target)} أو تجاوزها **لأول مرة**؟",
            jumps, [jumps - 1, jumps + 1, jumps + 2, (target // net) * 2],
            f"Each pair of jumps advances +{net}, EXCEPT on the final forward leap when it reaches {target} before sliding back!",
            f"كل زوج من القفزات يحقق تقدماً صافياً قدره +{net}، لكن انتبه للقفزة الأمامية الأخيرة التي تصل للهدف قبل التراجع!",
            "Subtract the final forward jump first so you don't overshoot and accidentally count an unnecessary backward jump.",
            [f"Each 2-jump cycle (forward then back) gains {m(f'{fwd} - {back} = {net}')} units.",
             f"After {m((jumps - 1) // 2)} full pairs ({m(jumps - 1)} jumps), position is {m(((jumps - 1) // 2) * net)}, and jump #{m(jumps)} adds {m(f'+{fwd}')} to reach {m(pos)}!"],
            f"Before jump #{m(jumps)}, the peak reached was below {m(target)}; jump #{m(jumps)} lands on {m(pos)} >= {m(target)}.",
            "احسب عدد الأزواج الكاملة قبل القفزة الأمامية الحاسمة حتى لا تحسب تراجعاً إضافياً بعد الوصول.",
            [f"كل زوج قفزات يحقق تقدماً صافياً يساوي {m(f'{fwd} - {back} = {net}')} وحدات.",
             f"بعد {m(jumps - 1)} قفزة يكون الموقع {m(((jumps - 1) // 2) * net)}، وفي القفزة رقم {m(jumps)} يتقدم {m(f'+{fwd}')} فيصل إلى {m(pos)}!"],
            f"أول وصول أو تجاوز للعدد {m(target)} يحدث عند القفزة الفردية رقم {m(jumps)}.",
            diagram_en=svg_number_line_jumps(fwd, back, target),
        ))

    hard_rem = [
        (6, 8, 3, 40, 60, "marbles in Faris's pouch", "كرة زجاجية في كيس فارس"),
        (8, 12, 5, 65, 85, "stickers in Dana's album", "ملصقاً في ألبوم دانة"),
        (9, 15, 4, 80, 110, "acorns in the squirrel basket", "حبة بلوط في سلة السنجاب"),
        (10, 14, 7, 60, 90, "badges in the Benjamin box", "شارة في صندوق بنجامين"),
        (12, 16, 9, 90, 120, "dominoes on Adam's table", "قطعة دومينو على طاولة آدم"),
    ]
    for d1, d2, rem, lo, hi, obj_en, obj_ar in hard_rem:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        cands = [n for n in range(lo, hi + 1) if n % d1 == rem and n % d2 == rem]
        assert len(cands) == 1
        ans = cands[0]
        lc = math.lcm(d1, d2)
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Hard", "kang_ben_lcm_meeting_cycles",
            f"Whether you group the {obj_en} into bags of {m(d1)} or bags of {m(d2)}, there are always {m(rem)} left over. Knowing there are between {m(lo)} and {m(hi)} items, what is the exact count?",
            f"سواء وزّعنا كل {obj_ar} في أكياس يسع الواحد {m(d1)} أو أكياس يسع الواحد {m(d2)}، يتبقّى دائماً {m(rem)} خارج الأكياس. إذا علمت أن العدد الكلي يقع بين {m(lo)} و{m(hi)}، فما العدد الدقيق؟",
            ans, [ans - rem, ans - 2 * rem, lc + rem, ans + d1],
            f"Subtract {rem} from the mystery number: N - {rem} must be a common multiple of {d1} and {d2}!",
            f"اطرح {rem} من العدد المجهول: المقدار N - {rem} يجب أن يكون مضاعفاً مشتركاً للعددين {d1} و{d2}!",
            f"If {m('N')} leaves remainder {m(rem)} upon division by both {m(d1)} and {m(d2)}, then {m(f'N - {rem}')} is a multiple of {m(f'\\operatorname{{lcm}}({d1},{d2})')}.",
            [f"Compute {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {lc}')}.",
             f"Multiples of {m(lc)} plus {m(rem)} are {m(f'{lc+rem}, {2*lc+rem}, {3*lc+rem}, \\dots')}; the unique one in {m(f'[{lo}, {hi}]')} is {m(ans)}."],
            f"{m(f'{ans} = {d1} \\times {ans // d1} + {rem}')} and {m(f'{ans} = {d2} \\times {ans // d2} + {rem}')}.",
            f"بما أن الباقي {m(rem)} ثابت في الحالتين فإن {m(f'N - {rem}')} مضاعف للمقدار {m(f'\\operatorname{{lcm}}({d1},{d2})')}.",
            [f"نحسب {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {lc}')}.",
             f"الأعداد على الصورة {m(f'{lc}k + {rem}')} تعطي داخل النطاق {m(f'[{lo}, {hi}]')} القيمة الوحيدة {m(ans)}."],
            f"تحقق: باقي قسمة {m(ans)} على كلٍّ من {m(d1)} و{m(d2)} هو {m(rem)}.",
            diagram_en=svg_number_strip([f"÷{d1} r={rem}", f"÷{d2} r={rem}", f"{lo}..{hi}", "?"]),
        ))

    # --- 3. kang_ben_matchstick_digits (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_ms = ["508", "2025", "749", "1836", "9047"]
    for idx_m, dstr in enumerate(easy_ms):
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        ans = sum(SEG_COUNTS[c] for c in dstr)
        parts_s = " + ".join(str(SEG_COUNTS[c]) for c in dstr)
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Easy", "kang_ben_matchstick_digits",
            f"Rami arranges wooden matchsticks to form the digital number {m(dstr)} on the 7-segment board shown (card #{idx_m+1}). How many matchsticks are lit in total?",
            f"يرتّب رامي أعواد الثقاب لتشكيل العدد الرقمي {m(dstr)} على اللوحة السباعية المبيّنة (البطاقة #{idx_m+1}). كم عود ثقاب استُخدم في المجموع؟",
            ans, [ans - 2, ans - 1, ans + 1, ans + 2],
            "Count the orange lit segments of each digit from left to right and add them up.",
            "عُدّ القطع البرتقالية المضيئة لكل رقم من اليسار لليمين ثم اجمعها.",
            "Sum the 7-segment stick counts of the individual digits.",
            [f"Segment counts digit by digit: {m(parts_s)}.", f"Total matchsticks = {m(ans)}."],
            f"Re-counting each digit confirms {m(f'{parts_s} = {ans}')}.",
            "نجمع عدد القطع المضيئة لكل خانة من خانات العدد.",
            [f"عدد الأعواد لكل رقم على الترتيب: {m(parts_s)}.", f"المجموع الكلي = {m(ans)} عوداً."],
            f"مراجعة سريعة: {m(f'{parts_s} = {ans}')}.",
            diagram_en=svg_kang_matchstick_digits(dstr),
        ))

    med_ms = [
        ("305", "max"),
        ("512", "max"),
        ("624", "min"),
        ("938", "max"),
        ("803", "min"),
    ]
    for dstr, mode in med_ms:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        b0 = [b for ch in dstr for b in seg_bits[ch]]
        cands = []
        for n in range(100, 1000):
            bn = [b for ch in str(n) for b in seg_bits[ch]]
            off_c = sum(1 for x, y in zip(b0, bn) if x == 1 and y == 0)
            on_c = sum(1 for x, y in zip(b0, bn) if x == 0 and y == 1)
            if off_c == 1 and on_c == 1:
                cands.append(n)
        ans = max(cands) if mode == "max" else min(cands)
        w_en = "largest" if mode == "max" else "smallest"
        w_ar = "أكبر" if mode == "max" else "أصغر"
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Medium", "kang_ben_matchstick_digits",
            f"The 7-segment display below shows {m(dstr)}. By picking up **exactly 1** matchstick and placing it in an empty slot on the same 3-digit board, what is the **{w_en}** three-digit number you can form?",
            f"تعرض اللوحة السباعية أدناه العدد {m(dstr)}. بتحريك **عود ثقاب واحد بالضبط** من مكانه إلى موضع فارغ في اللوحة الثلاثية نفسها، ما **{w_ar}** عدد من ثلاث خانات يمكن تكوينه؟",
            ans, [c for c in sorted(cands, reverse=(mode == "max")) if c != ans][:3] + [int(dstr)],
            "To optimize a 3-digit number, try improving the hundreds digit first (either within itself or by borrowing/lending 1 stick)!",
            "لتكبير أو تصغير عدد من ثلاث خانات، ابدأ بمحاولة تحسين خانة المئات أولاً!",
            "Moving 1 matchstick turns 1 lit segment OFF and 1 unlit segment ON across the three digits.",
            [f"List valid 1-move 3-digit numbers from {m(dstr)}: {m(', '.join(str(x) for x in sorted(cands)))}.",
             f"Selecting the {w_en} value gives {m(ans)}."],
            f"{m(dstr)} and {m(ans)} both use {m(sum(SEG_COUNTS[c] for c in dstr))} sticks and differ by moving just 1 stick!",
            "تحريك عود واحد يطفئ قطعة واحدة مضيئة ويضيء قطعة واحدة فارغة عبر الخانات الثلاث.",
            [f"الأعداد الثلاثية الصحيحة الناتجة بتحريك عود واحد من {m(dstr)} هي: {m(', '.join(str(x) for x in sorted(cands)))}.",
             f"إذن {w_ar} عدد ممكن هو {m(ans)}."],
            f"العددان {m(dstr)} و{m(ans)} يتساويان في مجموع الأعواد ويختلفان بنقل عود واحد فقط.",
            diagram_en=svg_kang_matchstick_digits(dstr),
        ))

    hard_ms = [
        (10, "min", 3),
        (11, "min", 3),
        (17, "max", 3),
        (18, "min", 3),
        (19, "min", 3),
    ]
    for k_sticks, mode, ndig in hard_ms:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        cands = [n for n in range(10**(ndig - 1), 10**ndig) if sum(SEG_COUNTS[c] for c in str(n)) == k_sticks]
        ans = max(cands) if mode == "max" else min(cands)
        w_en = "largest" if mode == "max" else "smallest"
        w_ar = "أكبر" if mode == "max" else "أصغر"
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Hard", "kang_ben_matchstick_digits",
            f"Laila has **exactly {m(k_sticks)}** matchsticks and must use **all** of them to form a valid {m(ndig)}-digit positive number (no leading zero) on a 7-segment display like `888`. What is the **{w_en}** {m(ndig)}-digit number she can build?",
            f"لدى ليلى **{m(k_sticks)} عود ثقاب بالضبط** وتريد استخدامها **كلها** لتكوين عدد موجب من {m(ndig)} خانات (دون صفر في اليسار) على لوحة رقمية مثل `888`. ما **{w_ar}** عدد من {m(ndig)} خانات يمكنها بناؤه؟",
            ans, [c for c in (sorted(cands, reverse=(mode == "max")))[1:5]],
            "Choose the leftmost (hundreds) digit to be as extreme as possible while keeping the remaining stick count achievable by two digits (between 4 and 14 sticks)!",
            "اختر خانة المئات أصغر (أو أكبر) ما يمكن بشرط أن يكون عدد الأعواد المتبقي قابلاً للتكوين بخانتين!",
            "Optimize greedily from the hundreds place to the units place using exact stick costs (1:2, 7:3, 4:4, 2/3/5:5, 0/6/9:6, 8:7).",
            [f"Test the best possible hundreds digit first so the remaining sticks can be split between tens and units.",
             f"The optimal valid {m(ndig)}-digit number using {m(k_sticks)} sticks is {m(ans)} ({' + '.join(str(SEG_COUNTS[c]) for c in str(ans))} = {m(k_sticks)})."],
            f"Stick sum of {m(ans)} is {m(sum(SEG_COUNTS[c] for c in str(ans)))} = {m(k_sticks)}.",
            "نحسّن الخانات من اليسار إلى اليمين مع التحقق من إمكانية توزيع الأعواد المتبقية.",
            [f"نختار أفضل رقم ممكن للمئات أولاً ثم نوزّع الباقي على العشرات والآحاد.",
             f"ينتج العدد الأمثل {m(ans)} بمجموع أعواد {' + '.join(str(SEG_COUNTS[c]) for c in str(ans))} = {m(k_sticks)}."],
            f"مجموع أعواد {m(ans)} يساوي {m(k_sticks)} بالضبط.",
            diagram_en=svg_kang_matchstick_digits(str(ans)[0] + "88"),
        ))

    # --- 4. kang_ben_cryptarithm_columns (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_cry = [(2, 4, 3, 5, 6), (3, 7, 1, 8, 4), (4, 6, 2, 7, 8), (1, 9, 5, 3, 7), (5, 2, 2, 9, 3)]
    for h1, u1, h2, u2, star in easy_cry:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        tot = int(f"{h1}{star}{u1}") + int(f"{h2}{star}{u2}")
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Easy", "kang_ben_cryptarithm_columns",
            f"In the vertical addition below, both star symbols {m('\\star')} stand for the **same** digit, giving {m(f'{h1}\\star{u1} + {h2}\\star{u2} = {tot}')}. What digit does {m('\\star')} represent?",
            f"في عملية الجمع العمودية أدناه يمثّل الرمزان {m('\\star')} **الرقم نفسه**، بحيث {m(f'{h1}\\star{u1} + {h2}\\star{u2} = {tot}')}. ما الرقم الذي يمثّله {m('\\star')}؟",
            star, [star - 1 if star > 0 else 2, star + 1, (star + 3) % 10, (star + 5) % 10],
            "Subtract the hundreds and units parts (with ★ = 0) from the total, then divide by 20!",
            "اطرح قيمة المئات والآحاد (باعتبار ★ = 0) من الناتج الكلي، ثم اقسم الباقي على 20!",
            f"Each {m('\\star')} sits in the tens column, contributing {m('10\\star + 10\\star = 20\\star')}.",
            [f"With {m('\\star = 0')}, {m(f'{h1}0{u1} + {h2}0{u2} = {h1*100+u1 + h2*100+u2}')}.",
             f"Difference = {m(f'{tot} - {h1*100+u1 + h2*100+u2} = {20*star}')}, so {m(f'\\star = {20*star} \\div 20 = {star}')}."],
            f"{m(f'{h1}{star}{u1} + {h2}{star}{u2} = {tot}')}.",
            f"يقع الرمز {m('\\star')} في خانة العشرات مرتين فيساهم بمقدار {m('20\\star')}.",
            [f"عند وضع {m('\\star = 0')} يكون المجموع {m(h1*100+u1 + h2*100+u2)}.",
             f"الفرق {m(f'{tot} - {h1*100+u1 + h2*100+u2} = {20*star}')}، ومنه {m(f'\\star = {star}')}."],
            f"تحقق: {m(f'{h1}{star}{u1} + {h2}{star}{u2} = {tot}')}.",
            diagram_en=svg_column_cryptarithm([f"{h1}★{u1}", f"{h2}★{u2}"], str(tot)),
        ))

    med_cry = [(9, 4), (8, 5), (7, 4), (9, 6), (8, 3)]
    for da, db in med_cry:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        tot = (10 * da + db) + (10 * db + da)
        diff_ab = da - db
        ans = da * db
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Medium", "kang_ben_cryptarithm_columns",
            f"In the addition {m(f'\\overline{{AB}} + \\overline{{BA}} = {tot}')}, {m('A')} and {m('B')} are digits with {m(f'A - B = {diff_ab}')}. What is the product {m('A \\times B')}?",
            f"في عملية الجمع {m(f'\\overline{{AB}} + \\overline{{BA}} = {tot}')}، يمثّل {m('A')} و{m('B')} رقمين يحققان {m(f'A - B = {diff_ab}')}. ما حاصل الضرب {m('A \\times B')}؟",
            ans, [da + db, ans - da, ans + db, ans + 6],
            "Use AB + BA = 11(A + B) to find A + B first!",
            "استخدم المتطابقة AB + BA = 11(A + B) لإيجاد A + B أولاً!",
            "Adding a 2-digit number to its digit-reversal always gives 11 times (A + B).",
            [f"Divide {m(tot)} by {m(11)}: {m(f'A + B = {tot // 11}')}.",
             f"Combine with {m(f'A - B = {diff_ab}')} to get {m(f'A = {da}')} and {m(f'B = {db}')}, so {m(f'A \\times B = {ans}')}."],
            f"{m(f'{da}{db} + {db}{da} = {tot}')} and {m(f'{da} \\times {db} = {ans}')}.",
            "مجموع عدد من خانتين ومعكوسه يساوي دائماً 11 مضروباً في مجموع رقميه.",
            [f"بقسمة {m(tot)} على {m(11)} نجد {m(f'A + B = {tot // 11}')}.",
             f"مع {m(f'A - B = {diff_ab}')} ينتج {m(f'A = {da}, B = {db}')}، وحاصل ضربهما {m(ans)}."],
            f"تحقق: {m(f'{da}{db} + {db}{da} = {tot}')}.",
            diagram_en=svg_column_cryptarithm(["AB", "BA"], str(tot)),
        ))

    hard_cry = [(2, 5), (3, 4), (4, 5), (3, 6), (5, 7)]
    for da, db in hard_cry:
        qid = f"KANG-BEN-{len(qs)+1:03d}"
        # ABA + BAB = total
        tot = (101 * da + 10 * db) + (101 * db + 10 * da)
        sols = [(x, y) for x in range(1, 10) for y in range(1, 10) if x < y and (111 * (x + y) == tot)]
        # Make unique by specifying B - A:
        diff_ba = db - da
        ans = int(f"{db}{da}")
        qs.append(make_kang_q(
            qid, LEVEL, "Number Theory", "Hard", "kang_ben_cryptarithm_columns",
            f"In the 3-digit column puzzle {m(f'\\overline{{ABA}} + \\overline{{BAB}} = {tot}')}, {m('A')} and {m('B')} are nonzero digits satisfying {m(f'B - A = {diff_ba}')}. What is the two-digit number {m('\\overline{BA}')}?",
            f"في لغز الجمع الثلاثي {m(f'\\overline{{ABA}} + \\overline{{BAB}} = {tot}')}، يمثّل {m('A')} و{m('B')} رقمين غير صفريين يحققان {m(f'B - A = {diff_ba}')}. ما قيمة العدد ذي الخانتين {m('\\overline{BA}')}؟",
            ans, [int(f"{da}{db}"), ans - 9, ans + 9, da + db],
            "Notice that ABA + BAB = (101A + 10B) + (101B + 10A) = 111(A + B)!",
            "لاحظ أن ABA + BAB = 111(A + B) فاقسم المجموع على 111!",
            "In every column (hundreds, tens, units), A and B appear once each, so ABA + BAB = 111(A + B).",
            [f"Divide {m(tot)} by {m(111)}: {m(f'A + B = {tot // 111}')}.",
             f"With {m(f'B - A = {diff_ba}')}, we get {m(f'B = {db}')} and {m(f'A = {da}')}, so {m(f'\\overline{{BA}} = {ans}')}."],
            f"{m(f'{da}{db}{da} + {db}{da}{db} = {tot}')}.",
            "في كل عمود (مئات، عشرات، آحاد) يظهر كل من A وB مرة واحدة، لذا فالمجموع يساوي 111(A + B).",
            [f"بقسمة {m(tot)} على {m(111)} نحصل على {m(f'A + B = {tot // 111}')}.",
             f"وبحلها مع {m(f'B - A = {diff_ba}')} نجد {m(f'B = {db}, A = {da}')}، إذن {m(f'\\overline{{BA}} = {ans}')}."],
            f"تحقق: {m(f'{da}{db}{da} + {db}{da}{db} = {tot}')}.",
            diagram_en=svg_column_cryptarithm(["ABA", "BAB"], str(tot)),
        ))

    assert len(qs) == 60
    return qs


def _unit_2() -> list[dict]:
    qs: list[dict] = []
    base_sq = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    # --- 5. kang_ben_visual_fractions (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_vf = [
        (4, 3, 5, 0, "stained-glass window", "نافذة زجاج ملون"),
        (5, 3, 6, 0, "gardenherb bed", "حوض أعشاب الحديقة"),
        (6, 3, 8, 0, "waffle grid", "شبكة حلوى الوافل"),
        (5, 4, 12, 0, "courtyard patio", "فناء البلاط"),
        (6, 4, 9, 0, "sticker sheet", "ورقة الملصقات"),
    ]
    for cols, rows, sh, ex, item_en, item_ar in easy_vf:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        item_en = item_en.replace("gardenherb", "garden herb")
        tot = cols * rows
        ans = Fraction(sh, tot)
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Easy", "kang_ben_visual_fractions",
            f"The {m(f'{cols} \\times {rows}')} {item_en} below has {m(sh)} shaded squares out of {m(tot)} equal squares. What fraction of the whole figure is **shaded** (in simplest form)?",
            f"تتكوّن {item_ar} ذات الأبعاد {m(f'{cols} \\times {rows}')} أدناه من {m(tot)} مربعاً متطابقاً، منها {m(sh)} مربعات مظللة. ما الكسر الدال على الجزء **المظلل** في أبسط صورة؟",
            ans, [Fraction(tot - sh, tot), Fraction(sh + 1, tot), Fraction(max(1, sh - 1), tot), Fraction(sh, tot + cols)],
            "Divide the shaded count by total squares, then cancel the greatest common divisor.",
            "اقسم عدد المربعات المظللة على العدد الكلي للمربعات ثم بسّط الكسر.",
            "Write shaded over total cells and simplify by their GCD.",
            [f"Total equal cells = {m(f'{cols} \\times {rows} = {tot}')}, with {m(sh)} shaded.",
             f"Simplify {m(f'\\frac{{{sh}}}{{{tot}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"{m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {tot} = {sh}')} shaded cells.",
            "نكتب الكسر (المظلل ÷ الكل) ثم نقسم البسط والمقام على القاسم المشترك الأكبر.",
            [f"العدد الكلي للمربعات = {m(f'{cols} \\times {rows} = {tot}')}، والمظلل منها {m(sh)}.",
             f"بالتبسيط نحصل على {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"تحقق: {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {tot} = {sh}')}.",
            diagram_en=svg_fraction_grid(cols, rows, sh, ex),
        ))

    med_vf = [
        (5, 4, Fraction(1, 4), Fraction(2, 5), "ceramic mural", "جدارية خزفية"),
        (6, 4, Fraction(1, 3), Fraction(3, 8), "berry tart tray", "صينية فطيرة التوت"),
        (6, 3, Fraction(1, 3), Fraction(1, 4), "solar panel grid", "لوحة خلايا شمسية"),
        (5, 3, Fraction(1, 5), Fraction(1, 2), "quilted blanket", "بطانية مرقّعة"),
        (7, 4, Fraction(2, 7), Fraction(3, 5), "mosaic tabletop", "طاولة فسيفساء"),
    ]
    for cols, rows, f1, f2, item_en, item_ar in med_vf:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        tot = cols * rows
        c1 = int(tot * f1)
        c2 = int((tot - c1) * f2)
        ans = tot - c1 - c2
        f1_s = f"\\frac{{{f1.numerator}}}{{{f1.denominator}}}"
        f2_s = f"\\frac{{{f2.numerator}}}{{{f2.denominator}}}"
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Medium", "kang_ben_visual_fractions",
            f"A {m(f'{cols} \\times {rows}')} {item_en} contains {m(tot)} equal unit squares. First {m(f1_s)} of the whole grid is colored purple, and then {m(f2_s)} of the **remaining** squares are colored sky-blue. How many squares stay **white**?",
            f"تضمّ {item_ar} بأبعاد {m(f'{cols} \\times {rows}')} عدداً قدره {m(tot)} مربعاً متطابقاً. لُوِّن أولاً {m(f1_s)} الشبكة الكلية بالبنفسجي، ثم لُوِّن {m(f2_s)} المربعات **المتبقية** بالأزرق الفاتح. كم مربعاً يبقى **أبيض**؟",
            ans, [c1 + c2, tot - c1, c2, ans + 2],
            "Compute how many squares remain after the purple step FIRST, then take the fraction of that remainder!",
            "احسب عدد المربعات المتبقية بعد التلوين البنفسجي أولاً، ثم خذ الكسر الثاني من هذا الباقي!",
            "Track the remaining count step by step rather than adding the two fractions.",
            [f"Purple squares = {m(f'{f1_s} \\times {tot} = {c1}')}, leaving {m(f'{tot} - {c1} = {tot - c1}')} squares.",
             f"Sky-blue squares = {m(f'{f2_s} \\times {tot - c1} = {c2}')}, leaving {m(f'{tot - c1} - {c2} = {ans}')} white squares."],
            f"{m(f'{c1} + {c2} + {ans} = {tot}')} squares in total.",
            "نتتبّع العدد المتبقي بعد كل خطوة بدلاً من جمع الكسرين مباشرة.",
            [f"المربعات البنفسجية = {m(c1)}، فيتبقى {m(tot - c1)} مربعاً.",
             f"المربعات الزرقاء = {m(f'{f2_s} \\times {tot - c1} = {c2}')}، ويبقى أبيض {m(f'{tot - c1} - {c2} = {ans}')}."],
            f"تحقق: {m(f'{c1} + {c2} + {ans} = {tot}')}.",
            diagram_en=svg_fraction_grid(cols, rows, c1, c2),
        ))

    hard_vf = [
        (Fraction(3, 4), Fraction(1, 3), Fraction(1, 2), "pitcher A", "الإبريق أ"),
        (Fraction(2, 3), Fraction(1, 4), Fraction(1, 2), "beaker A", "الكأس أ"),
        (Fraction(4, 5), Fraction(1, 5), Fraction(1, 2), "flask A", "القارورة أ"),
        (Fraction(3, 5), Fraction(1, 2), Fraction(1, 3), "carafe A", "الوعاء أ"),
        (Fraction(5, 6), Fraction(1, 6), Fraction(2, 5), "jug A", "الجرة أ"),
    ]
    for fa, fb, pour_part, nm_en, nm_ar in hard_vf:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        poured = fa * pour_part
        ans = fb + poured
        assert ans <= 1
        fa_s = f"\\frac{{{fa.numerator}}}{{{fa.denominator}}}"
        fb_s = f"\\frac{{{fb.numerator}}}{{{fb.denominator}}}"
        pp_s = f"\\frac{{{pour_part.numerator}}}{{{pour_part.denominator}}}"
        pr_s = f"\\frac{{{poured.numerator}}}{{{poured.denominator}}}"
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Hard", "kang_ben_visual_fractions",
            f"Two **identical** containers are partially filled with juice: {nm_en} is {m(fa_s)} full and container B is {m(fb_s)} full. Next, {m(pp_s)} of the juice currently in {nm_en} is poured into container B. What fraction of container B is now full?",
            f"وعاءان **متطابقان** مملوءان جزئياً بالعصير: {nm_ar} مملوء بمقدار {m(fa_s)} والوعاء ب مملوء بمقدار {m(fb_s)}. سُكب {m(pp_s)} العصير الموجود في {nm_ar} إلى الوعاء ب. ما الكسر المملوء من الوعاء ب الآن؟",
            ans, [fa - poured, fb + pour_part, Fraction(ans.numerator + 1, ans.denominator), poured],
            "Since both containers have equal capacity, multiply the fraction in A by the poured fraction, then add to B!",
            "بما أن للوعاءين السعة نفسها، اضرب كسر امتلاء الأول في كسر السكب ثم اجمعه إلى كسر امتلاء الثاني!",
            "Amount poured (as a fraction of one container) equals the fraction in A times the transferred share.",
            [f"Juice transferred from A = {m(f'{pp_s} \\times {fa_s} = {pr_s}')} of a container.",
             f"New level in container B = {m(f'{fb_s} + {pr_s} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"Total juice conserved: {m(f'({fa_s} - {pr_s}) + \\frac{{{ans.numerator}}}{{{ans.denominator}}} = {fa_s} + {fb_s}')}.",
            "كمية العصير المنقولة كنسبة من سعة الوعاء تساوي حاصل ضرب الكسرين، ثم نضيفها إلى الوعاء ب.",
            [f"المقدار المسكوب = {m(f'{pp_s} \\times {fa_s} = {pr_s}')} من سعة الوعاء.",
             f"امتلاء الوعاء ب الجديد = {m(f'{fb_s} + {pr_s} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"مجموع العصير الكلي ثابت قبل السكب وبعده.",
            diagram_en=svg_two_jars(f"A ({fa.numerator}/{fa.denominator})", float(fa), f"B ({fb.numerator}/{fb.denominator})", float(fb), f"{pour_part.numerator}/{pour_part.denominator}"),
        ))

    # --- 6. kang_ben_work_backwards_ops (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_wb = [
        (9, "+ 5", "× 3", 42),
        (8, "× 4", "− 7", 25),
        (11, "− 3", "× 5", 40),
        (6, "× 6", "+ 9", 45),
        (14, "+ 4", "× 2", 36),
    ]
    for x_in, op1, op2, y_out in easy_wb:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Easy", "kang_ben_work_backwards_ops",
            f"Hana enters a starting number into the Kangaroo number machine shown (`{op1}` then `{op2}`) and gets the output {m(y_out)}. What starting number did Hana enter?",
            f"أدخلت هنا عدداً ابتدائياً في آلة الأعداد المبيّنة (`{op1}` ثم `{op2}`) فظهر المخرج {m(y_out)}. ما العدد الابتدائي الذي أدخلته هنا؟",
            x_in, [x_in - 2, x_in + 2, x_in + 5, max(1, x_in - 4)],
            "Start from the output on the right and invert the second box BEFORE inverting the first box!",
            "ابدأ من المخرج على اليمين واعكس العملية الثانية قبل عكس العملية الأولى!",
            "Undo the pipeline from right to left using inverse operations.",
            [f"Start at output {m(y_out)} and undo `{op2}` first.", f"Then undo `{op1}` to obtain the input {m(x_in)}."],
            f"Forward check from {m(x_in)} through `{op1}` then `{op2}` produces {m(y_out)}!",
            "نرجع من اليمين إلى اليسار بعكس كل عملية بالترتيب العكسي.",
            [f"ننطلق من {m(y_out)} ونلغي العملية `{op2}` أولاً.", f"ثم نلغي العملية `{op1}` فنجد المدخل {m(x_in)}."],
            f"بالتعويض الأمامي بالعدد {m(x_in)} نحصل على {m(y_out)} تماماً.",
            diagram_en=svg_function_machine("?", op1, op2, str(y_out)),
        ))

    med_wb = [
        (18, 3, 7, 2),
        (20, 4, 9, 3),
        (24, 6, 5, 2),
        (15, 5, 8, 4),
        (28, 7, 6, 3),
    ]
    for x_in, div_a, add_b, mult_k in med_wb:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        y1 = (x_in // div_a) + add_b
        ans = ((x_in * mult_k) // div_a) + add_b
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Medium", "kang_ben_work_backwards_ops",
            f"When Ziad enters a number {m('N')} into the machine (`÷ {div_a}` then `+ {add_b}`), the output is {m(y1)}. What output will the **same** machine display if Ziad enters {m(f'{mult_k}N')} instead?",
            f"عندما يدخل زياد العدد {m('N')} في الآلة (`÷ {div_a}` ثم `+ {add_b}`) يظهر المخرج {m(y1)}. ما المخرج الذي ستعرضه الآلة **نفسها** إذا أدخل زياد العدد {m(f'{mult_k}N')}؟",
            ans, [y1 * mult_k, ans - add_b, ans + div_a, x_in],
            f"Work backwards from {y1} to find N first, then run {mult_k}N forward through the machine!",
            f"اعمل عكسياً من {y1} لإيجاد N أولاً، ثم أدخل {mult_k}N في الآلة للأمام!",
            f"Do NOT multiply {m(y1)} by {m(mult_k)} directly, because `+ {add_b}` is not multiplied!",
            [f"Rewind from {m(y1)}: {m(f'({y1} - {add_b}) \\times {div_a} = {x_in}')}, so {m(f'N = {x_in}')}.",
             f"Now feed {m(f'{mult_k}N = {mult_k * x_in}')}: {m(f'{mult_k * x_in} \\div {div_a} + {add_b} = {ans}')}."],
            f"Trap check: {m(f'{mult_k} \\times {y1} = {mult_k * y1} \\ne {ans}')}.",
            "نجد قيمة N بالعودة العكسية أولاً ثم نحسب مخرج المضاعف الجديد.",
            [f"بالعودة العكسية: {m(f'N = ({y1} - {add_b}) \\times {div_a} = {x_in}')}.",
             f"ندخل {m(f'{mult_k}N = {mult_k * x_in}')} فنحصل على {m(f'{mult_k * x_in} \\div {div_a} + {add_b} = {ans}')}."],
            f"تحقق: {m(f'{x_in} \\div {div_a} + {add_b} = {y1}')}، ومع {m(mult_k * x_in)} الناتج {m(ans)}.",
            diagram_en=svg_function_machine("N", f"÷ {div_a}", f"+ {add_b}", str(y1)),
        ))

    hard_wb = [
        (1, 2, 3, "box of dates", "علبة تمور"),
        (2, 1, 4, "basket of figs", "سلة تين"),
        (1, 3, 2, "jar of almonds", "جرة لوز"),
        (3, 2, 3, "tray of muffins", "صينية كعك"),
        (2, 2, 5, "bag of walnuts", "كيس جوز"),
    ]
    for k1, k2, rem, item_en, item_ar in hard_wb:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        after_1 = (rem + k2) * 2
        ans = (after_1 + k1) * 2
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Hard", "kang_ben_work_backwards_ops",
            f"From a {item_en}, Tariq eats **half** of the pieces plus {m(k1)} more. Later, his sister eats **half** of what remained plus {m(k2)} more, leaving {m(rem)} pieces at the end. How many pieces were in the {item_en} originally?",
            f"من {item_ar} أكل طارق **نصف** الحبات ثم أكل {m(k1)} إضافية، وبعده أكلت أخته **نصف** ما تبقّى ثم {m(k2)} إضافية، فبقي في النهاية {m(rem)} حبات. كم حبة كانت في البداية؟",
            ans, [ans - 4, ans + 4, after_1 * 2, rem * 4 + k1 + k2],
            f"Undo 'divide by 2 then subtract {k2}' by ADDING {k2} first and then MULTIPLYING by 2!",
            f"لعكس «أخذ النصف ثم طرح {k2}» اجمع {k2} أولاً ثم اضرب في 2!",
            "Each stage applies (÷ 2 then − k), so its exact inverse is (+ k then × 2).",
            [f"Before his sister ate: {m(f'({rem} + {k2}) \\times 2 = {after_1}')} pieces.",
             f"Before Tariq ate: {m(f'({after_1} + {k1}) \\times 2 = {ans}')} pieces."],
            f"Forward: {m(f'{ans} \\div 2 - {k1} = {after_1}')}, then {m(f'{after_1} \\div 2 - {k2} = {rem}')}!",
            "كل مرحلة تكافئ (القسمة على 2 ثم طرح k)، وعكسها هو (جمع k ثم الضرب في 2).",
            [f"قبل أن تأكل أخته كان الباقي: {m(f'({rem} + {k2}) \\times 2 = {after_1}')}.",
             f"وقبل أن يأكل طارق كان العدد الأصلي: {m(f'({after_1} + {k1}) \\times 2 = {ans}')}."],
            f"تحقق أمامي: {m(f'{ans} \\to {after_1} \\to {rem}')} بالضبط!",
            diagram_en=svg_function_machine("?", f"÷2 − {k1}", f"÷2 − {k2}", str(rem)),
        ))

    # --- 7. kang_ben_double_balance (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_bal = [(1, 2, 1, 3, 2), (2, 3, 1, 2, 4), (1, 3, 1, 2, 3), (2, 4, 2, 6, 3), (3, 2, 2, 5, 3)]
    for c1, s1, s2, t2, ask_c in easy_bal:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        # 1 C = (s1/c1) S, 1 S = (t2/s2) T => 1 C = (s1*t2)/(c1*s2) T
        ratio_ct = Fraction(s1 * t2, c1 * s2)
        ans = int(ask_c * ratio_ct)
        assert ask_c * ratio_ct == ans
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Easy", "kang_ben_double_balance",
            f"On the twin scales shown, {m(c1)} orange circle(s) balance {m(s1)} green square(s), and {m(s2)} green square(s) balance {m(t2)} purple triangle(s). How many purple triangles will balance {m(ask_c)} orange circles?",
            f"في الميزانين المتزنين أدناه تعادل {m(c1)} من الدوائر البرتقالية {m(s1)} من المربعات الخضراء، وتعادل {m(s2)} من المربعات الخضراء {m(t2)} من المثلثات البنفسجية. كم مثلثاً بنفسجياً يوازن {m(ask_c)} دوائر برتقالية؟",
            ans, [ans - 2 if ans > 2 else ans + 3, ans - 1, ans + 1, ans + 2],
            "Express green squares in terms of purple triangles, then substitute for the orange circles!",
            "عبّر عن المربعات الخضراء بدلالة المثلثات البنفسجية ثم عوّض لحساب الدوائر البرتقالية!",
            "Chain the two balance ratios by eliminating the middle shape (green squares).",
            [f"Each circle equals {m(fmt_r := f'\\frac{{{s1}}}{{{c1}}}' if s1 % c1 else str(s1 // c1))} square(s), and each square equals {m(f'\\frac{{{t2}}}{{{s2}}}' if t2 % s2 else str(t2 // s2))} triangle(s).",
             f"Thus {m(ask_c)} circles balance {m(f'{ask_c} \\times \\frac{{{s1}}}{{{c1}}} \\times \\frac{{{t2}}}{{{s2}}} = {ans}')} purple triangles."],
            f"Substitution confirms {m(ask_c)} circles have the exact weight of {m(ans)} triangles.",
            "نربط النسبتين بحذف الشكل المشترك (المربع الأخضر).",
            [f"نستبدل المربعات الخضراء بما يكافئها من المثلثات البنفسجية من الميزان الأيمن.",
             f"نجد أن {m(ask_c)} دوائر توازن {m(ans)} مثلثات بنفسجية."],
            f"تحقق بالاستبدال: الطرفان متساويان تماماً عند {m(ans)} مثلثات.",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        ))

    med_bal = [(2, 3, 1, 2, 10), (1, 2, 2, 3, 12), (3, 4, 2, 3, 8), (2, 5, 1, 2, 6), (3, 2, 1, 3, 10)]
    for c1, s1, s2, t2, wt_t in med_bal:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        wt_s = Fraction(t2, s2) * wt_t
        wt_c = Fraction(s1, c1) * wt_s
        ans = int(wt_c + wt_s)
        assert wt_c.denominator == 1 and wt_s.denominator == 1
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Medium", "kang_ben_double_balance",
            f"In the balanced scales below ({m(c1)} circle(s) = {m(s1)} square(s), and {m(s2)} square(s) = {m(t2)} triangle(s)), each purple triangle weighs {m(wt_t)} grams. What is the combined weight (in grams) of **1 orange circle and 1 green square**?",
            f"في الميزانين المتزنين أدناه ({m(c1)} دائرة = {m(s1)} مربع، و{m(s2)} مربع = {m(t2)} مثلث)، يزن كل مثلث بنفسجي {m(wt_t)} جرامات. ما الوزن الكلي (بالجرام) **لدائرة برتقالية واحدة ومربع أخضر واحد**؟",
            ans, [int(wt_c), int(wt_s), ans + wt_t, ans - wt_t // 2],
            "Find the weight of 1 green square from the right scale first, then 1 orange circle from the left scale!",
            "احسب وزن المربع الأخضر الواحد من الميزان الأيمن أولاً، ثم وزن الدائرة البرتقالية من الأيسر!",
            "Work from the known triangle weight to squares, then to circles.",
            [f"One green square weighs {m(f'\\frac{{{t2} \\times {wt_t}}}{{{s2}}} = {int(wt_s)}')} g.",
             f"One orange circle weighs {m(f'\\frac{{{s1} \\times {int(wt_s)}}}{{{c1}}} = {int(wt_c)}')} g, so together they weigh {m(f'{int(wt_c)} + {int(wt_s)} = {ans}')} g."],
            f"{m(f'{c1} \\times {int(wt_c)} = {s1} \\times {int(wt_s)} = {c1 * int(wt_c)}')} g.",
            "نحسب وزن المربع من المثلثات أولاً ثم وزن الدائرة من المربعات.",
            [f"وزن المربع الأخضر الواحد = {m(int(wt_s))} جم.",
             f"وزن الدائرة الواحدة = {m(int(wt_c))} جم، ومجموعهما = {m(f'{int(wt_c)} + {int(wt_s)} = {ans}')} جم."],
            f"تحقق: {m(f'{c1} \\times {int(wt_c)} = {s1} \\times {int(wt_s)}')} جم.",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        ))

    hard_bal = [(1, 2, 1, 2, 7), (2, 3, 1, 2, 5), (1, 3, 2, 3, 4), (2, 3, 2, 5, 3), (3, 4, 1, 3, 4)]
    for c1, s1, s2, t2, unit_g in hard_bal:
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        # Let T = c1 * s2 * unit_g, S = c1 * t2 * unit_g, C = s1 * t2 * unit_g
        wt_t = c1 * s2 * unit_g
        wt_s = c1 * t2 * unit_g
        wt_c = s1 * t2 * unit_g
        tot_three = wt_c + wt_s + wt_t
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Hard", "kang_ben_double_balance",
            f"Both scales below are balanced ({m(c1)} circle(s) = {m(s1)} square(s), and {m(s2)} square(s) = {m(t2)} triangle(s)). If **1 circle + 1 square + 1 triangle** together weigh {m(tot_three)} grams, how many grams does **1 orange circle** weigh?",
            f"الميزانان أدناه متزنان ({m(c1)} دائرة = {m(s1)} مربع، و{m(s2)} مربع = {m(t2)} مثلث). إذا كان وزن **دائرة واحدة + مربع واحد + مثلث واحد** معاً يساوي {m(tot_three)} جراماً، فكم جراماً تزن **الدائرة البرتقالية الواحدة**؟",
            wt_c, [wt_s, wt_t, wt_c + unit_g, wt_c - unit_g],
            "Pick whole-number ratio parts for (Circle : Square : Triangle) that satisfy both scales, then scale to the total weight!",
            "اختر حصصاً صحيحة لنسبة (الدائرة : المربع : المثلث) تحقق الميزانين معاً، ثم قسّم الوزن الكلي على مجموع الحصص!",
            "Unify the two ratios into a single 3-part ratio C : S : T.",
            [f"Set ratio parts {m(f'T = {c1*s2}')}, {m(f'S = {c1*t2}')}, and {m(f'C = {s1*t2}')} (total {m(s1*t2 + c1*t2 + c1*s2)} parts).",
             f"Each part is {m(f'{tot_three} \\div {s1*t2 + c1*t2 + c1*s2} = {unit_g}')} g, so 1 circle weighs {m(f'{s1*t2} \\times {unit_g} = {wt_c}')} g."],
            f"{m(f'{wt_c} + {wt_s} + {wt_t} = {tot_three}')} g and both scales balance!",
            "نوحّد النسبتين في نسبة ثلاثية واحدة للدائرة والمربع والمثلث.",
            [f"نختار الحصص {m(f'C : S : T = {s1*t2} : {c1*t2} : {c1*s2}')} ومجموعها {m(s1*t2 + c1*t2 + c1*s2)} حصة.",
             f"قيمة الحصة الواحدة {m(unit_g)} جم، فيكون وزن الدائرة الواحدة {m(wt_c)} جم."],
            f"تحقق: {m(f'{wt_c} + {wt_s} + {wt_t} = {tot_three}')} جم.",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        ))

    # --- 8. kang_ben_magic_square_3x3 (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    for idx_e, (mult, shift) in enumerate([(1, 3), (2, 0), (1, 6), (2, 1), (3, -1)]):
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        g = [[base_sq[r][c] * mult + shift for c in range(3)] for r in range(3)]
        ans = g[0][1]
        disp = [[str(g[0][0]), "?", str(g[0][2])], ["", str(g[1][1]), ""], [str(g[2][0]), "", ""]]
        msum = 3 * g[1][1]
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Easy", "kang_ben_magic_square_3x3",
            f"In Kangaroo magic square #{idx_e+1} below, every row, column, and main diagonal has the same magic sum. What number goes in the cell marked {m('?')}?",
            f"في المربع السحري #{idx_e+1} أدناه تتساوى مجاميع كل صف وعمود وقطر رئيسي. ما العدد المناسب مكان العلامة {m('?')}؟",
            ans, [ans - mult, ans + mult, g[1][0], g[2][2]],
            "Multiply the center number by 3 to get the magic sum immediately!",
            "اضرب عدد المركز في 3 لتحصل على المجموع السحري فوراً!",
            f"In any 3×3 magic square, the magic sum equals {m('3 \\times \\text{center}')}.",
            [f"Center = {m(g[1][1])}, so magic sum {m(f'S = 3 \\times {g[1][1]} = {msum}')}.",
             f"Top row: {m(f'? = {msum} - {g[0][0]} - {g[0][2]} = {ans}')}."],
            f"{m(f'{g[0][0]} + {ans} + {g[0][2]} = {msum}')} and diagonal {m(f'{g[0][2]} + {g[1][1]} + {g[2][0]} = {msum}')}.",
            "في أي مربع سحري 3×3 يساوي المجموع السحري ثلاثة أمثال الخانة الوسطى.",
            [f"المركز {m(g[1][1])}، إذن المجموع السحري {m(f'S = 3 \\times {g[1][1]} = {msum}')}.",
             f"من الصف العلوي: {m(f'? = {msum} - {g[0][0]} - {g[0][2]} = {ans}')}."],
            f"تحقق: {m(f'{g[0][0]} + {ans} + {g[0][2]} = {msum}')}.",
            diagram_en=svg_magic_square_3x3(disp),
        ))

    for idx_m, (mult, shift) in enumerate([(2, 3), (3, 1), (2, 5), (4, -2), (3, 4)]):
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        g = [[base_sq[r][c] * mult + shift for c in range(3)] for r in range(3)]
        ans = g[2][2]
        # Give top row fully (g[0][0], g[0][1], g[0][2]) -> S -> center = S/3 -> g[2][2] = S - g[0][0] - center
        disp = [[str(g[0][0]), str(g[0][1]), str(g[0][2])], ["", "", ""], ["", "", "?"]]
        msum = sum(g[0])
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Medium", "kang_ben_magic_square_3x3",
            f"In the {m('3 \\times 3')} magic square below (board #{idx_m+1}), every row, column, and main diagonal has the same sum. Using the complete top row, find the bottom-right corner {m('?')}.",
            f"في المربع السحري {m('3 \\times 3')} أدناه (اللوحة #{idx_m+1}) تتساوى مجاميع الصفوف والأعمدة والقطرين. بالاستفادة من الصف العلوي الكامل، أوجد قيمة الركن السفلي الأيمن {m('?')}.",
            ans, [ans - mult, ans + mult, g[1][1], g[2][0]],
            "Add the top row to find S, divide S by 3 to reveal the hidden center, then complete the main diagonal!",
            "اجمع الصف العلوي لإيجاد S، ثم اقسم S على 3 لمعرفة المركز المخفي، وأكمل القطر الرئيسي!",
            "Once the magic sum S is known, the hidden center is S ÷ 3!",
            [f"Top row gives magic sum {m(f'S = {g[0][0]} + {g[0][1]} + {g[0][2]} = {msum}')}, so center = {m(f'{msum} \\div 3 = {g[1][1]}')}.",
             f"Along the main diagonal, {m(f'{g[0][0]} + {g[1][1]} + ? = {msum} \\implies ? = {ans}')}."],
            f"{m(f'{g[0][0]} + {g[1][1]} + {ans} = {msum}')}.",
            "متى عرفنا المجموع السحري S، يكون المركز دائماً مساوياً لـ S ÷ 3!",
            [f"من الصف العلوي {m(f'S = {msum}')}، فيكون المركز {m(f'{msum} \\div 3 = {g[1][1]}')}.",
             f"من القطر الرئيسي: {m(f'? = {msum} - {g[0][0]} - {g[1][1]} = {ans}')}."],
            f"تحقق: {m(f'{g[0][0]} + {g[1][1]} + {ans} = {msum}')}.",
            diagram_en=svg_magic_square_3x3(disp),
        ))

    for a0 in (2, 4, 5, 7, 9):
        qid = f"KANG-BEN-{60 + len(qs) + 1:03d}"
        nums = [a0 + i for i in range(5)]
        # Largest possible line sum in a 5-cell magic cross puts largest number (a0+4) in center!
        ans = 3 * a0 + 7  # center = a0+4, pairs (a0, a0+3) and (a0+1, a0+2), line sum = (a0+4) + (2*a0+3) = 3*a0+7
        qs.append(make_kang_q(
            qid, LEVEL, "Algebra", "Hard", "kang_ben_magic_square_3x3",
            f"Place the five numbers {m(', '.join(str(v) for v in nums))} into the {m(5)} cells of the Kangaroo cross below (one per cell) so that the **horizontal 3-cell sum** equals the **vertical 3-cell sum**. What is the **largest** possible value of that equal line sum?",
            f"نضع الأعداد الخمسة {m(', '.join(str(v) for v in nums))} في خلايا الصليب الخمس أدناه (عدداً في كل خلية) بحيث يتساوى **مجموع الخلايا الثلاث الأفقية** مع **مجموع الخلايا الثلاث الرأسية**. ما **أكبر** قيمة ممكنة لهذا المجموع المشترك؟",
            ans, [3 * a0 + 6, 3 * a0 + 5, 3 * a0 + 8, 3 * a0 + 4],
            "Add the horizontal sum and vertical sum together: the center cell is counted TWICE! Put the largest valid number in the center!",
            "اجمع الصف والعمود معاً: الخلية الوسطى تُحسب مرتين! ضع أكبر عدد ممكن في المركز لتحصل على أكبر مجموع خطي!",
            f"Since {m('2L = (\\text{sum of all 5}) + c')}, maximizing line sum {m('L')} means maximizing the center {m('c')} while keeping {m('(\\text{total} + c)')} even!",
            [f"Sum of all 5 numbers = {m(sum(nums))}. Adding row + column gives {m(f'2L = {sum(nums)} + c')}.",
             f"Putting the largest number {m(a0 + 4)} in the center splits the remaining four into {m(f'({a0} + {a0+3}) = ({a0+1} + {a0+2}) = {2*a0+3}')}, giving max line sum {m(f'L = ({sum(nums)} + {a0+4}) \\div 2 = {ans}')}."],
            f"Arms {m(f'({a0}, {a0+3})')} and {m(f'({a0+1}, {a0+2})')} around center {m(a0+4)} both give {m(ans)}!",
            "بجمع الخط الأفقي والخط الرأسي نجد 2L = مجموع الخمسة + المركز، فنضع أكبر عدد في المركز!",
            [f"مجموع الأعداد الخمسة = {m(sum(nums))}، وعند وضع أكبر عدد {m(a0+4)} في المركز نقسم الباقي إلى زوجين متساويين {m(f'{a0}+{a0+3} = {a0+1}+{a0+2}')}.",
             f"إذن أكبر مجموع خطي ممكن هو {m(f'L = {a0+4} + {2*a0+3} = {ans}')}."],
            f"تحقق: كلا الخطين يعطي {m(ans)} بالضبط.",
            diagram_en=svg_kang_magic_cross("?", "•", "•", "•", "•", f"Use {nums[0]}..{nums[-1]}"),
            diagram_ar=svg_kang_magic_cross("؟", "•", "•", "•", "•", f"الأعداد {nums[0]}..{nums[-1]}"),
        ))

    assert len(qs) == 60
    return qs


def _unit_3() -> list[dict]:
    qs: list[dict] = []

    # --- 9. kang_ben_overlapping_areas (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_ov = [
        (36, 28, 9, "craft papers", "ورقتان ملونتان"),
        (50, 42, 15, "picnic mats", "بساطا نزهة"),
        (64, 49, 18, "square napkins", "منديلان مربعان"),
        (48, 35, 11, "poster boards", "لوحتان إعلانيتان"),
        (72, 54, 21, "felt sheets", "قطعتا لباد"),
    ]
    for a1, a2, ov, it_en, it_ar in easy_ov:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = a1 + a2 - ov
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_overlapping_areas",
            f"Two rectangular {it_en} of areas {m(f'{a1}\\text{{ cm}}^2')} and {m(f'{a2}\\text{{ cm}}^2')} lie overlapping on a desk. If their shared overlap has area {m(f'{ov}\\text{{ cm}}^2')}, what total desk area (in {m('\\text{cm}^2')}) do they cover?",
            f"وُضعت {it_ar} مساحتاهما {m(f'{a1}\\text{{ سم}}^2')} و{m(f'{a2}\\text{{ سم}}^2')} متداخلتين على مكتب. إذا كانت مساحة منطقة التداخل {m(f'{ov}\\text{{ سم}}^2')}، فما المساحة الكلية المغطاة بالـ {m('\\text{سم}^2')}؟",
            ans, [a1 + a2, a1 + a2 - 2 * ov, ans - 5, ans + 5],
            "Add the two areas, then subtract the overlap ONCE so it is not double-counted.",
            "اجمع المساحتين ثم اطرح منطقة التداخل مرة واحدة فقط.",
            "Covered area equals A₁ + A₂ − Overlap.",
            [f"Sum of separate areas = {m(f'{a1} + {a2} = {a1+a2}\\text{{ cm}}^2')}.",
             f"Subtract the overlap once: {m(f'{a1+a2} - {ov} = {ans}\\text{{ cm}}^2')}."],
            f"Parts: {m(f'({a1}-{ov}) + {ov} + ({a2}-{ov}) = {ans}\\text{{ cm}}^2')}.",
            "المساحة المغطاة تساوي مجموع المساحتين ناقص مساحة التداخل مرة واحدة.",
            [f"مجموع المساحتين = {m(f'{a1} + {a2} = {a1+a2}\\text{{ سم}}^2')}.",
             f"بطرح التداخل: {m(f'{a1+a2} - {ov} = {ans}\\text{{ سم}}^2')}."],
            f"تحقق: {m(f'{a1-ov} + {ov} + {a2-ov} = {ans}')}.",
            diagram_en=svg_kang_overlapping_rects(f"{a1} cm²", f"{a2} cm²", f"{ov} cm²"),
        ))

    med_ov = [
        (9, 6, 8, 5, 76),
        (10, 7, 9, 6, 102),
        (12, 5, 8, 7, 95),
        (11, 6, 10, 5, 97),
        (12, 8, 9, 7, 134),
    ]
    for w1, h1, w2, h2, cov in med_ov:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        a1, a2 = w1 * h1, w2 * h2
        ans = a1 + a2 - cov
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_overlapping_areas",
            f"A {m(f'{w1}\\text{{ cm}} \\times {h1}\\text{{ cm}}')} card and an {m(f'{w2}\\text{{ cm}} \\times {h2}\\text{{ cm}}')} card overlap on a board, covering a combined area of {m(f'{cov}\\text{{ cm}}^2')}. What is the area (in {m('\\text{cm}^2')}) of their **overlapping** region?",
            f"تداخلت بطاقة أبعادها {m(f'{w1}\\text{{ سم}} \\times {h1}\\text{{ سم}}')} مع بطاقة أبعادها {m(f'{w2}\\text{{ سم}} \\times {h2}\\text{{ سم}}')} على لوحة فغطّتا مساحة كلية قدرها {m(f'{cov}\\text{{ سم}}^2')}. ما مساحة منطقة **التداخل** بالـ {m('\\text{سم}^2')}؟",
            ans, [ans // 2, ans + 6, max(1, ans - 4), abs(a1 - a2)],
            "Compute both rectangle areas first; the excess of (A₁ + A₂) above the covered area is the overlap!",
            "احسب مساحتي البطاقتين أولاً؛ الزيادة في مجموعهما عن المساحة المغطاة هي مساحة التداخل!",
            "Overlap = A₁ + A₂ − Covered Area.",
            [f"Areas are {m(f'{w1}\\times{h1}={a1}')} and {m(f'{w2}\\times{h2}={a2}')}, summing to {m(a1 + a2)}.",
             f"Overlap = {m(f'{a1+a2} - {cov} = {ans}\\text{{ cm}}^2')}."],
            f"{m(f'{a1} + {a2} - {ans} = {cov}\\text{{ cm}}^2')}.",
            "مساحة التداخل تساوي مجموع المساحتين مطروحاً منه المساحة المغطاة.",
            [f"مساحتا البطاقتين {m(a1)} و{m(a2)} ومجموعهما {m(a1 + a2)}.",
             f"مساحة التداخل = {m(f'{a1+a2} - {cov} = {ans}\\text{{ سم}}^2')}."],
            f"تحقق: {m(f'{a1} + {a2} - {ans} = {cov}')}.",
            diagram_en=svg_overlapping_rects(f"{w1}×{h1}", f"{w2}×{h2}", "?"),
        ))

    hard_ov = [(54, 42, 13), (68, 50, 17), (75, 60, 19), (84, 65, 22), (90, 72, 25)]
    for a1, a2, ov in hard_ov:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = (a1 - ov) + (a2 - ov)
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_overlapping_areas",
            f"Two translucent glass plates of areas {m(f'{a1}\\text{{ cm}}^2')} and {m(f'{a2}\\text{{ cm}}^2')} overlap in a dark rectangle of area {m(f'{ov}\\text{{ cm}}^2')}. What is the total area (in {m('\\text{cm}^2')}) covered by **exactly ONE** layer of glass?",
            f"تتداخل صفيحتان زجاجيتان شفافتان مساحتاهما {m(f'{a1}\\text{{ سم}}^2')} و{m(f'{a2}\\text{{ سم}}^2')} في مستطيل داكن مساحته {m(f'{ov}\\text{{ سم}}^2')}. ما المساحة الكلية (بالـ {m('\\text{سم}^2')}) المغطاة **بطبقة واحدة فقط** من الزجاج؟",
            ans, [a1 + a2 - ov, a1 + a2, ans - ov, a1 - ov],
            "Careful! Single-layer area excludes the overlap from BOTH plates, so you must subtract 2 × overlap!",
            "انتبه! منطقة الطبقة الواحدة تستبعد التداخل من الصفيحتين معاً، لذا نطرح ضعف مساحة التداخل!",
            "Single-layer area = (A₁ − Overlap) + (A₂ − Overlap) = A₁ + A₂ − 2 × Overlap.",
            [f"Single-layer part of Plate 1 = {m(f'{a1} - {ov} = {a1-ov}')}; of Plate 2 = {m(f'{a2} - {ov} = {a2-ov}')}.",
             f"Total single-layer area = {m(f'{a1-ov} + {a2-ov} = {ans}\\text{{ cm}}^2')}."],
            f"Notice {m(f'{a1 + a2 - ov}')} includes the 2-layer middle, whereas {m(ans)} counts strictly 1-layer glass!",
            "مساحة الطبقة الواحدة تساوي مجموع الجزأين غير المشتركين أي A₁ + A₂ − 2 × التداخل.",
            [f"الجزء المنفرد من الأولى = {m(a1 - ov)}، ومن الثانية = {m(a2 - ov)}.",
             f"المساحة ذات الطبقة الواحدة = {m(f'{a1-ov} + {a2-ov} = {ans}\\text{{ سم}}^2')}."],
            f"تحقق: {m(f'{ans} + {ov} = {a1+a2-ov}')} هي المساحة الكلية المغطاة.",
            diagram_en=svg_kang_overlapping_rects(f"{a1} cm²", f"{a2} cm²", f"{ov} cm²"),
        ))

    # --- 10. kang_ben_cut_corner_perimeter (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_per = [(13, 8, 3), (16, 9, 4), (18, 12, 3), (21, 14, 5), (24, 15, 4)]
    for w, h, st in easy_per:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = 2 * (w + h)
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_cut_corner_perimeter",
            f"All corners in the {m(st)}-step staircase polygon below are right angles. Its bottom width is {m(f'{w}\\text{{ cm}}')} and its left height is {m(f'{h}\\text{{ cm}}')}. What is its perimeter in centimeters?",
            f"جميع زوايا المضلع السُلّمي ذي {m(st)} درجات أدناه قائمة. طول قاعدته السفلية {m(f'{w}\\text{{ سم}}')} وارتفاعه الأيسر {m(f'{h}\\text{{ سم}}')}. ما محيطه بالسنتيمتر؟",
            ans, [w + h, ans - 2 * st, ans + 2 * st, w * h],
            "Push all horizontal treads to the top and all vertical risers to the right to form an outer rectangle!",
            "أزِح جميع القطع الأفقية للأعلى والقطع الرأسية لليمين ليتكوّن مستطيل كامل!",
            "A monotone right-angled staircase has the exact same perimeter as its W × H bounding rectangle.",
            [f"Horizontal treads sum to {m(w)} cm, and vertical risers sum to {m(h)} cm.",
             f"Perimeter = {m(f'2 \\times ({w} + {h}) = {ans}\\text{{ cm}}')}."],
            f"{m(f'{w} + {h} + {w} + {h} = {ans}\\text{{ cm}}')}.",
            "محيط المضلع السُلّمي القائم يساوي محيط المستطيل المحيط به.",
            [f"مجموع القطع الأفقية = {m(w)} سم، ومجموع القطع الرأسية = {m(h)} سم.",
             f"المحيط = {m(f'2 \\times ({w} + {h}) = {ans}\\text{{ سم}}')}."],
            f"تحقق: {m(f'2({w}+{h}) = {ans}')} سم.",
            diagram_en=svg_rectilinear_staircase(f"{w} cm", f"{h} cm", st),
        ))

    med_per = [(14, 18, 20), (16, 22, 18), (12, 16, 24), (20, 26, 22), (18, 14, 26)]
    for p_tl, p_tr, p_bl in med_per:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = p_tr + p_bl - p_tl
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_cut_corner_perimeter",
            f"A large rectangle is divided by one horizontal line and one vertical line into four smaller rectangles. Three of them have perimeters {m(p_tl)}, {m(p_tr)}, and {m(p_bl)} cm as shown. What is the perimeter (in cm) of the fourth rectangle {m('?')}?",
            f"قُسّم مستطيل كبير بمستقيم أفقي وآخر رأسي إلى أربعة مستطيلات صغيرة. محيطات ثلاثة منها هي {m(p_tl)} و{m(p_tr)} و{m(p_bl)} سم كما في الشكل. ما محيط المستطيل الرابع {m('?')} بالسنتيمتر؟",
            ans, [ans - 2, ans + 2, (p_tr + p_bl) // 2, p_tl + p_tr - p_bl],
            "Add the perimeters of OPPOSITE corner rectangles: both pairs share the exact same widths and heights!",
            "اجمع محيطي كل مستطيلين متقابلين قطرياً؛ فمجموعاهما متساويان تماماً!",
            "Opposite pairs in a 2×2 grid satisfy P(top-left) + P(bottom-right) = P(top-right) + P(bottom-left).",
            [f"Both opposite diagonal pairs equal {m('2(w_1 + w_2 + h_1 + h_2)')}.",
             f"So {m(f'{p_tl} + ? = {p_tr} + {p_bl} \\implies ? = {p_tr + p_bl} - {p_tl} = {ans}')} cm."],
            f"{m(f'{p_tl} + {ans} = {p_tr} + {p_bl} = {p_tr + p_bl}')}.",
            "في تقسيم 2×2 مجموع محيطي المستطيلين المتقابلين قطرياً يساوي مجموع محيطي الآخرين.",
            [f"لدينا {m(f'{p_tl} + ? = {p_tr} + {p_bl}')}.",
             f"إذن {m(f'? = {p_tr + p_bl} - {p_tl} = {ans}')} سم."],
            f"تحقق: {m(f'{p_tl} + {ans} = {p_tr + p_bl}')}.",
            diagram_en=svg_subdivided_rect_2x2(f"P = {p_tl}", f"P = {p_tr}", f"P = {p_bl}", "P = ?"),
        ))

    hard_per = [(12, 2), (15, 3), (18, 4), (20, 3), (24, 5)]
    for big_s, cut_x in hard_per:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = 3 * big_s - 3 * cut_x
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_cut_corner_perimeter",
            f"From an equilateral triangle of side {m(f'{big_s}\\text{{ cm}}')}, three smaller equilateral triangles of side {m(f'{cut_x}\\text{{ cm}}')} are cut off from the three corners, leaving the shaded hexagon shown. What is the perimeter (in cm) of the shaded hexagon?",
            f"من مثلث متطابق الأضلاع طول ضلعه {m(f'{big_s}\\text{{ سم}}')} قُصّت ثلاثة مثلثات صغيرة متطابقة الأضلاع طول ضلع كل منها {m(f'{cut_x}\\text{{ سم}}')} عند الرؤوس الثلاثة، فنتج السداسي المظلل. ما محيط السداسي المظلل بالسنتيمتر؟",
            ans, [3 * big_s, 3 * big_s - 6 * cut_x, 3 * big_s + 3 * cut_x, ans - cut_x],
            "At each corner, two outer segments of length x are removed, but ONE new cut edge of length x appears!",
            "عند كل رأس نزيل قطعتين طول كل منهما x ولكن يظهر ضلع مقصوص جديد طوله x!",
            f"Each corner cut replaces {m('2x')} of boundary with {m('1x')}, reducing the perimeter by {m('x')} per corner.",
            [f"Three remaining parts of the original sides each have length {m(f'{big_s} - 2({cut_x}) = {big_s - 2*cut_x}')} cm.",
             f"Add the three new {m(cut_x)} cm cut edges: {m(f'3 \\times {big_s - 2*cut_x} + 3 \\times {cut_x} = {ans}')} cm."],
            f"Shortcut: {m(f'3({big_s}) - 3({cut_x}) = {ans}')} cm!",
            "كل زاوية مقصوصة تستبدل ضلعين طولهما 2x بضلع واحد طوله x فينقص المحيط بمقدار x عند كل رأس.",
            [f"تبقى {m(3)} أجزاء من الأضلاع الأصلية طول كل منها {m(big_s - 2*cut_x)} سم بالإضافة إلى {m(3)} أضلاع جديدة طول كل منها {m(cut_x)} سم.",
             f"المحيط = {m(f'3({big_s - 2*cut_x}) + 3({cut_x}) = {ans}')} سم."],
            f"اختصار سريع: {m(f'3 \\times {big_s} - 3 \\times {cut_x} = {ans}')} سم.",
            diagram_en=svg_equilateral_corner_cuts(f"{big_s} cm", f"{cut_x} cm"),
        ))

    # --- 11. kang_ben_shaded_rect_triangle (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_tri = [(10, 7, 0.4), (12, 9, 0.65), (14, 8, 0.35), (18, 7, 0.7), (20, 9, 0.55)]
    for L, W, af in easy_tri:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = (L * W) // 2
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_shaded_rect_triangle",
            f"The rectangle below has length {m(f'{L}\\text{{ cm}}')} and width {m(f'{W}\\text{{ cm}}')}. What is the area (in {m('\\text{cm}^2')}) of the shaded triangle whose base is the bottom edge and whose apex lies on the top edge?",
            f"طول المستطيل أدناه {m(f'{L}\\text{{ سم}}')} وعرضه {m(f'{W}\\text{{ سم}}')}. ما مساحة المثلث المظلل (بالـ {m('\\text{سم}^2')}) الذي قاعدته الضلع السفلي ورأسه على الضلع العلوي؟",
            ans, [L * W, ans - L // 2, ans + W, L + W],
            "The triangle's base is L and its perpendicular height is W, regardless of where the top vertex sits!",
            "قاعدة المثلث هي L وارتفاعه العمودي هو W مهما تغيّر موضع الرأس على الضلع العلوي!",
            "A triangle spanning opposite sides of a rectangle always has area equal to half the rectangle.",
            [f"Rectangle area = {m(f'{L} \\times {W} = {L*W}\\text{{ cm}}^2')}.",
             f"Shaded triangle area = {m(f'{L*W} \\div 2 = {ans}\\text{{ cm}}^2')}."],
            f"{m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}\\text{{ cm}}^2')}.",
            "مساحة المثلث تساوي نصف مساحة المستطيل دائماً.",
            [f"مساحة المستطيل = {m(f'{L} \\times {W} = {L*W}\\text{{ سم}}^2')}.",
             f"مساحة المثلث المظلل = {m(f'{L*W} \\div 2 = {ans}\\text{{ سم}}^2')}."],
            f"تحقق: {m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}')}.",
            diagram_en=svg_shaded_triangle_in_rect(L, W, af, "cm"),
        ))

    med_tri = [(10, 8, 4, 2), (12, 8, 6, 4), (10, 6, 4, 2), (12, 10, 4, 6), (14, 8, 6, 4)]
    for L, W, ct, cr in med_tri:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        t1 = (W * ct) // 2
        t2 = ((L - ct) * (W - cr)) // 2
        t3 = (L * cr) // 2
        ans = L * W - (t1 + t2 + t3)
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_shaded_rect_triangle",
            f"Inside the {m(f'{L} \\times {W}')} rectangle below, a shaded triangle connects the bottom-left corner to points on the top and right edges as labeled. What is the area of the shaded triangle?",
            f"داخل المستطيل ذي الأبعاد {m(f'{L} \\times {W}')} أدناه يصل المثلث المظلل الركن السفلي الأيسر بنقطتين على الضلعين العلوي والأيمن بالأطوال الموضّحة. ما مساحة المثلث المظلل؟",
            ans, [ans - 2, ans + 4, (L * W) // 2 + 2, t1 + t2 + t3],
            "Subtract the areas of the three white right-angled corner triangles from the full L × W rectangle!",
            "اطرح مساحات المثلثات القائمة الثلاثة البيضاء عند الأركان من مساحة المستطيل الكلي!",
            "Use the Bounding-Box Subtraction method: Rectangle minus the 3 unshaded right triangles.",
            [f"Rectangle area = {m(f'{L} \\times {W} = {L*W}')}.",
             f"Unshaded right triangles have areas {m(t1)}, {m(t2)}, and {m(t3)} (sum {m(t1+t2+t3)}).",
             f"Shaded area = {m(f'{L*W} - {t1+t2+t3} = {ans}')}."],
            f"{m(f'{ans} + {t1} + {t2} + {t3} = {L*W}')} exact!",
            "نطرح مساحات المثلثات القائمة البيضاء الثلاثة من مساحة المستطيل.",
            [f"مساحة المستطيل الكلي = {m(L * W)}.",
             f"مساحات المثلثات البيضاء هي {m(t1)} و{m(t2)} و{m(t3)} ومجموعها {m(t1+t2+t3)}.",
             f"المساحة المظللة = {m(f'{L*W} - {t1+t2+t3} = {ans}')}."],
            f"مجموع الأجزاء الأربعة يساوي {m(L*W)} تماماً.",
            diagram_en=svg_inscribed_corner_triangle_in_rect(L, W, ct, cr),
        ))

    hard_grid = [
        (5, 4, [(0, 1), (4, 0), (5, 3), (1, 4)]),
        (6, 4, [(0, 2), (4, 0), (6, 2), (2, 4)]),
        (5, 5, [(0, 1), (4, 0), (5, 4), (1, 5)]),
        (6, 5, [(0, 2), (5, 0), (6, 4), (2, 5)]),
        (6, 4, [(1, 0), (6, 1), (5, 4), (0, 3)]),
    ]
    for cols, rows, verts in hard_grid:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        # Shoelace exact area (all chosen so 2*area is divisible by 2 -> integer!)
        twice_a = abs(sum(verts[i][0] * verts[(i + 1) % 4][1] - verts[(i + 1) % 4][0] * verts[i][1] for i in range(4)))
        assert twice_a % 2 == 0
        ans = twice_a // 2
        unsh = cols * rows - ans
        v_str = f"A{verts[0]}, B{verts[1]}, C{verts[2]}, D{verts[3]}"
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_shaded_rect_triangle",
            f"On the unit-square grid below ({m(f'{cols} \\times {rows}')} outer box, each small square has area {m(1)}), what is the exact area of the shaded quadrilateral {m('ABCD')} with vertices at {m(v_str)}?",
            f"على شبكة المربعات أدناه (المستطيل الخارجي {m(f'{cols} \\times {rows}')} ومساحة كل مربع صغير {m(1)})، ما المساحة الدقيقة للرباعي المظلل {m('ABCD')} الذي رؤوسه عند {m(v_str)}؟",
            ans, [ans - 1, ans + 1, ans + 2, unsh],
            f"Enclose ABCD inside the {cols}×{rows} outer box and subtract the 4 corner right triangles!",
            f"أحِط الرباعي ABCD بالمستطيل الخارجي {cols}×{rows} ثم اطرح المثلثات القائمة الأربعة في الأركان!",
            "Subtract the four outer right-angled corner triangles from the bounding grid rectangle.",
            [f"Outer grid box area = {m(f'{cols} \\times {rows} = {cols*rows}')}.",
             f"The four corner right triangles around {m('ABCD')} have total area {m(unsh)}.",
             f"Shaded area = {m(f'{cols*rows} - {unsh} = {ans}')}."],
            f"Interior + corner triangles = {m(f'{ans} + {unsh} = {cols*rows}')}.",
            "نحسب مساحة المستطيل المحيط ثم نطرح مساحات المثلثات القائمة الأربعة الخارجة عن الرباعي.",
            [f"مساحة المستطيل الخارجي = {m(f'{cols} \\times {rows} = {cols*rows}')}.",
             f"مجموع مساحات مثلثات الأركان الأربعة = {m(unsh)}.",
             f"مساحة الرباعي المظلل = {m(f'{cols*rows} - {unsh} = {ans}')}."],
            f"تحقق: {m(f'{ans} + {unsh} = {cols*rows}')}.",
            diagram_en=svg_grid_polygon(cols, rows, verts, ["A", "B", "C", "D"]),
        ))

    # --- 12. kang_ben_paper_fold_angles (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    for alpha in (55, 62, 68, 71, 74):
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = 180 - 2 * alpha
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_paper_fold_angles",
            f"A rectangular paper strip is folded along the red crease shown, forming an angle of {m(f'{alpha}^\\circ')} with the dashed top edge. What is the measure (in degrees) of angle {m('x')}?",
            f"طُويت ورقة مستطيلة حول خط الطيّ الأحمر المبيّن فصنع خط الطيّ زاوية قياسها {m(f'{alpha}^\\circ')} مع الحافة العلوية المتقطعة. ما قياس الزاوية {m('x')} بالدرجات؟",
            ans, [180 - alpha, alpha, 90 - (alpha - 45), ans + 10],
            "Folding reflects the angle across the crease, so two copies of the crease angle sit next to x on a 180° straight line!",
            "الطيّ يعكس الزاوية حول خط الطيّ، فتجتمع نسختان متساويتان بجانب x على خط مستقيم قياسه 180°!",
            f"Along the straight top edge, {m('x + 2\\alpha = 180^\\circ')}.",
            [f"The folded flap mirrors the {m(f'{alpha}^\\circ')} angle, covering {m(f'2 \\times {alpha}^\\circ = {2*alpha}^\\circ')}.",
             f"Subtract from {m('180^\\circ')}: {m(f'x = 180^\\circ - {2*alpha}^\\circ = {ans}^\\circ')}."],
            f"{m(f'{alpha}^\\circ + {alpha}^\\circ + {ans}^\\circ = 180^\\circ')}.",
            "على الحافة المستقيمة تتجاور الزاوية الأصلية ونسختها المطوية مع x فيكون مجموعها 180°.",
            [f"مجموع الزاوية الأصلية ونسختها المنعكسة = {m(f'2 \\times {alpha}^\\circ = {2*alpha}^\\circ')}.",
             f"إذن {m(f'x = 180^\\circ - {2*alpha}^\\circ = {ans}^\\circ')}."],
            f"تحقق: {m(f'{alpha} + {alpha} + {ans} = 180^\\circ')}.",
            diagram_en=svg_paper_fold(f"{alpha}°", "x"),
        ))

    for x_ang in (36, 44, 50, 64, 72):
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = (180 - x_ang) // 2
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_paper_fold_angles",
            f"When the top-right corner of a rectangular sheet is folded across the red crease as shown, the remaining straight-edge angle on the left is {m(f'{x_ang}^\\circ')}. What is the crease angle {m('\\alpha')} (in degrees)?",
            f"عند طيّ الركن العلوي الأيمن للورقة المستطيلة حول خط الطيّ الأحمر كما في الشكل، تبقّت زاوية قياسها {m(f'{x_ang}^\\circ')} على الحافة اليسرى. ما قياس زاوية الطيّ {m('\\alpha')} بالدرجات؟",
            ans, [180 - x_ang, 90 - x_ang // 2, ans - 8, ans + 8],
            f"Subtract {x_ang}° from 180°, then divide equally between the original angle and its folded twin!",
            f"اطرح {x_ang}° من 180° ثم اقسم الباقي بالتساوي بين الزاوية الأصلية ونسختها المطوية!",
            f"Because folding creates two equal angles {m('\\alpha')}, {m(f'2\\alpha = 180^\\circ - {x_ang}^\\circ')}.",
            [f"Remaining angle covered by the fold and its original position: {m(f'180^\\circ - {x_ang}^\\circ = {180 - x_ang}^\\circ')}.",
             f"Divide by {m(2)}: {m(f'\\alpha = {180 - x_ang}^\\circ \\div 2 = {ans}^\\circ')}."],
            f"{m(f'{ans}^\\circ + {ans}^\\circ + {x_ang}^\\circ = 180^\\circ')}.",
            "بما أن الطيّ ينشئ زاويتين متطابقتين α فإن 2α = 180° − الزاوية المتبقية.",
            [f"نجد {m(f'2\\alpha = 180^\\circ - {x_ang}^\\circ = {180 - x_ang}^\\circ')}.",
             f"بالقسمة على {m(2)} نحصل على {m(f'\\alpha = {ans}^\\circ')}."],
            f"تحقق: {m(f'2({ans}) + {x_ang} = 180^\\circ')}.",
            diagram_en=svg_paper_fold("α", f"{x_ang}°"),
        ))

    for a_top, a_bot in [(34, 49), (39, 46), (42, 53), (28, 57), (36, 58)]:
        qid = f"KANG-BEN-{120 + len(qs) + 1:03d}"
        ans = a_top + a_bot
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_paper_fold_angles",
            f"Between the two parallel edges {m('L_1 \\parallel L_2')} of a long paper ribbon, a bent strip forms interior angles of {m(f'{a_top}^\\circ')} at {m('L_1')} and {m(f'{a_bot}^\\circ')} at {m('L_2')}, as shown. What is the middle bend angle {m('?^\\circ')}?",
            f"بين الحافتين المتوازيتين {m('L_1 \\parallel L_2')} لشريط ورقي طويل يصنع مسار منكسر زاويتين قياساهما {m(f'{a_top}^\\circ')} عند {m('L_1')} و{m(f'{a_bot}^\\circ')} عند {m('L_2')} كما في الشكل. ما قياس زاوية الانثناء الوسطى {m('?^\\circ')}؟",
            ans, [180 - ans, abs(a_bot - a_top), ans - 10, ans + 10],
            "Draw a helper horizontal line through the middle vertex parallel to L₁ and L₂ to split the bend into two Z-angles!",
            "ارسم مستقيماً أفقياً مساعداً يمرّ بالرأس الأوسط موازياً لـ L₁ وL₂ ليقسم الزاوية إلى زاويتي تبادل (حرف Z)!",
            "By drawing a parallel line through the middle vertex, alternate interior (Z) angles add directly: bend = top + bottom.",
            [f"Draw a line through the middle bend parallel to {m('L_1')} and {m('L_2')}.",
             f"The upper part equals {m(f'{a_top}^\\circ')} and the lower part equals {m(f'{a_bot}^\\circ')} by alternate interior angles, totaling {m(f'{a_top}^\\circ + {a_bot}^\\circ = {ans}^\\circ')}."],
            f"Splitting the vertex gives {m(f'{a_top}^\\circ + {a_bot}^\\circ = {ans}^\\circ')}.",
            "برسم موازٍ يمرّ بالرأس الأوسط تنقسم الزاوية بالتبادل الداخلي إلى مجموع الزاويتين العلوية والسفلية.",
            [f"الجزء العلوي من الزاوية يساوي {m(f'{a_top}^\\circ')} بالتبادل، والجزء السفلي يساوي {m(f'{a_bot}^\\circ')} بالتبادل.",
             f"إذن قياس الزاوية الوسطى = {m(f'{a_top}^\\circ + {a_bot}^\\circ = {ans}^\\circ')}."],
            f"تحقق: {m(f'{a_top} + {a_bot} = {ans}^\\circ')}.",
            diagram_en=svg_parallel_zigzag(f"{a_top}°", "?°", f"{a_bot}°"),
        ))

    assert len(qs) == 60
    return qs


def _unit_4() -> list[dict]:
    qs: list[dict] = []

    # --- 13. kang_ben_painted_cube_faces (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_pc = [
        (3, 1, "exactly 1 painted face", "وجه واحد مطلي بالضبط"),
        (4, 0, "0 painted faces (completely unpainted)", "صفر من الأوجه المطلية (غير مطلية إطلاقاً)"),
        (5, 2, "exactly 2 painted faces", "وجهين مطليين بالضبط"),
        (5, 1, "exactly 1 painted face", "وجه واحد مطلي بالضبط"),
        (6, 0, "0 painted faces (completely unpainted)", "صفر من الأوجه المطلية (غير مطلية إطلاقاً)"),
    ]
    for n, k_f, desc_en, desc_ar in easy_pc:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        ans = sum(
            1
            for x in range(n)
            for y in range(n)
            for z in range(n)
            if ((x == 0) + (x == n - 1) + (y == 0) + (y == n - 1) + (z == 0) + (z == n - 1)) == k_f
        )
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_painted_cube_faces",
            f"A {m(f'{n} \\times {n} \\times {n}')} wooden cube is painted blue on all {m(6)} outside faces and cut into {m(n**3)} unit cubes. How many unit cubes have **{desc_en}**?",
            f"طُلي مكعب خشبي أبعاده {m(f'{n} \\times {n} \\times {n}')} باللون الأزرق من جميع أوجهه الـ {m(6)} ثم قُطّع إلى {m(n**3)} مكعباً صغيراً. كم مكعباً صغيراً له **{desc_ar}**؟",
            ans, [max(1, ans - 6), ans + 6, 12 * (n - 2) if k_f != 2 else 6 * (n - 2) ** 2, 8 if ans != 8 else 12],
            "Use the cube anatomy formulas: 3 faces = 8, 2 faces = 12(n−2), 1 face = 6(n−2)², 0 faces = (n−2)³!",
            "استخدم تشريح المكعب: 3 أوجه = 8، وجهان = 12(n−2)، وجه واحد = 6(n−2)²، بلا طلاء = (n−2)³!",
            "Classify unit cubes by corners, inner edges, inner faces, and hidden core.",
            [f"Here {m(f'n = {n}')}, so {m(f'n - 2 = {n - 2}')}.",
             f"Applying the formula for {k_f} painted face(s) gives {m(ans)} unit cubes."],
            f"Count verified across all {m(n**3)} unit cubes: {m(ans)}.",
            "نطبّق قانون الفئة المطلوبة بدلالة الحرف الداخلي (n − 2).",
            [f"لدينا {m(f'n = {n}')} ومنه {m(f'n - 2 = {n - 2}')}.",
             f"عدد المكعبات الصغيرة المطلوبة يساوي {m(ans)}."],
            f"تم التحقق من المجموع الكلي للمكعبات الـ {m(n**3)}.",
            diagram_en=svg_painted_cube_3d(min(n, 5)),
        ))

    med_pc = [
        (3, 0, "0 painted faces"),
        (3, 2, "exactly 2 painted faces"),
        (4, 0, "0 painted faces"),
        (4, 1, "exactly 1 painted face"),
        (5, 0, "0 painted faces"),
    ]
    ar_map_pc = {
        "0 painted faces": "صفر من الأوجه المطلية",
        "exactly 2 painted faces": "وجهين مطليين بالضبط",
        "exactly 1 painted face": "وجه واحد مطلي بالضبط",
    }
    for n, k_f, desc_en in med_pc:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        # Resting flat on table -> bottom z == 0 is NOT painted!
        ans = sum(
            1
            for x in range(n)
            for y in range(n)
            for z in range(n)
            if ((x == 0) + (x == n - 1) + (y == 0) + (y == n - 1) + (z == n - 1)) == k_f
        )
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_painted_cube_faces",
            f"A {m(f'{n} \\times {n} \\times {n}')} cube sits flat on a table while its **top and 4 side faces** ({m(5)} faces total; the bottom stays unpainted!) are spray-painted purple. After cutting it into {m(n**3)} unit cubes, how many have **{desc_en}**?",
            f"يستقر مكعب أبعاده {m(f'{n} \\times {n} \\times {n}')} على طاولة، فطُلي **وجهه العلوي وأوجهه الجانبية الأربعة** فقط ({m(5)} أوجه؛ القاعدة السفلية لم تُطلَ!). بعد تقطيعه إلى {m(n**3)} مكعباً صغيراً، كم مكعباً له **{ar_map_pc[desc_en]}**؟",
            ans, [(n - 2) ** 3 if ans != (n - 2) ** 3 else ans + 4, max(1, ans - 4), ans + 4, ans + 8],
            "Remember the bottom layer touches the table and gets NO paint on its underside!",
            "تذكّر أن الطبقة السفلية تلامس الطاولة فلا يصل الطلاء إلى وجهها السفلي!",
            "Check the bottom layer separately from the upper layers because the floor blocks paint.",
            [f"Every unit cube with {m('1 \\le x, y \\le n-2')} and {m('0 \\le z \\le n-2')} avoids the 4 painted walls and the painted roof.",
             f"Counting all unit cubes across the {m(n)} layers that receive {desc_en} gives {m(ans)}."],
            f"Voxel-by-voxel check across all {m(n**3)} cubes confirms {m(ans)}.",
            "نفحص الطبقة السفلية الملامسة للطاولة مع الطبقات العلوية لأن القاعدة غير مطلية.",
            [f"الوجه السفلي محجوب بالطاولة فلا يُطلى، بينما تُطلى الجدران الأربعة والسقف.",
             f"بحساب المكعبات في الطبقات الـ {m(n)} نجد العدد الدقيق {m(ans)}."],
            f"تحقق مكاني شامل لجميع الـ {m(n**3)} مكعباً يعطي {m(ans)}.",
            diagram_en=svg_painted_cube_3d(min(n, 5)),
        ))

    hard_stacks = [(3, 2, 1), (4, 2, 1), (3, 3, 1), (4, 3, 2), (4, 1, 3)]
    for cols in hard_stacks:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        voxels = {(i, 0, z) for i, h in enumerate(cols) for z in range(h)}
        ans = 0
        for x, y, z in voxels:
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                if dz == -1 and z == 0:
                    continue  # touching table!
                if (x + dx, y + dy, z + dz) not in voxels:
                    ans += 1
        c_str = ", ".join(str(c) for c in cols)
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_painted_cube_faces",
            f"Unit cubes of side {m('1\\text{ cm}')} are glued side-by-side in three columns of heights {m(c_str)} resting flat on a table, as shown. All exposed outer faces **except** the bottom faces touching the table are painted gold. How many {m('\\text{cm}^2')} are painted gold?",
            f"لُصقت مكعبات وحدة طول حرفها {m('1\\text{ سم}')} جنباً إلى جنب في ثلاثة أعمدة ارتفاعاتها {m(c_str)} تستقر على طاولة كما في الشكل. طُليت جميع الأوجه الخارجية المكشوفة باللون الذهبي **باستثناء** القاعدة الملامسة للطاولة. كم {m('\\text{سم}^2')} طُلي بالذهبي؟",
            ans, [ans + len(cols), ans - len(cols), 6 * sum(cols) - len(cols), ans + 2],
            "Count views from 5 directions: Top + Front + Back + Left + Right (watching for any inner valley walls)!",
            "احسب المربعات المرئية من الاتجاهات الخمسة: الأعلى + الأمام + الخلف + اليسار + اليمين (مع الانتباه للجدران الداخلية إن وُجدت)!",
            "Sum exposed unit faces from Top, Front, Back, and Horizontal step changes.",
            [f"Top view shows {m(len(cols))} squares; Front and Back each show {m(sum(cols))} squares ({m(2 * sum(cols))} total).",
             f"Left/right vertical exposed faces contribute {m(ans - len(cols) - 2 * sum(cols))}, giving {m(ans)} {m('\\text{cm}^2')}."],
            f"Total painted unit squares = {m(ans)} (excluding the {m(len(cols))} floor squares).",
            "نجمع الأوجه المكشوفة من الأعلى والأمام والخلف والجوانب الرأسية.",
            [f"من الأعلى يظهر {m(len(cols))} مربعات، ومن الأمام والخلف {m(2 * sum(cols))} مربعاً.",
             f"الأوجه الجانبية الرأسية تضيف {m(ans - len(cols) - 2 * sum(cols))}، فيكون المجموع {m(ans)} {m('\\text{سم}^2')}."],
            f"تحقق: مجموع المربعات المطلية الذهبية يساوي {m(ans)}.",
            diagram_en=svg_cube_stack_3d(cols),
        ))

    # --- 14. kang_ben_cube_net_opposite (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    net_templates = [
        ([(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)], [(0, 5), (1, 3), (2, 4)]),
        ([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3)], [(0, 2), (1, 4), (3, 5)]),
        ([(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)], [(0, 5), (1, 3), (2, 4)]),
        ([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)], [(0, 3), (1, 4), (2, 5)]),
        ([(1, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)], [(0, 4), (1, 3), (2, 5)]),
    ]
    lbl_sets = [
        ["1", "2", "3", "4", "5", "6"],
        ["6", "1", "4", "3", "5", "2"],
        ["2", "5", "1", "6", "3", "4"],
        ["3", "6", "2", "5", "1", "4"],
        ["4", "1", "5", "2", "6", "3"],
    ]
    for idx_n, ((coords, opp_pairs), lbls) in enumerate(zip(net_templates, lbl_sets)):
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        i_ask, i_ans = opp_pairs[idx_n % 3]
        ask_v = int(lbls[i_ask])
        ans = int(lbls[i_ans])
        cells_l = [(coords[k][0], coords[k][1], lbls[k]) for k in range(6)]
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_cube_net_opposite",
            f"When cube net #{idx_n+1} below is folded into a closed cube, which number lands **directly opposite** face {m(ask_v)}?",
            f"عند طيّ شبكة المكعب #{idx_n+1} أدناه لتشكيل مكعب مغلق، أيّ رقم يقع **مقابلاً تماماً** للوجه {m(ask_v)}؟",
            ans, [int(lbls[k]) for k in range(6) if k not in (i_ask, i_ans)],
            "Choose a middle square as the bottom floor and fold its neighbors up as vertical walls!",
            "اختر مربعاً أوسط كقاعدة سفلية وارفع المربعات المجاورة له كجدران رأسية!",
            "Fold around a central base square (or apply the 1-square leapfrog rule along strips).",
            [f"Fix square {m(lbls[2])} as the base and fold adjacent squares upward by {m('90^\\circ')}.",
             f"Tracking the six faces shows face {m(ask_v)} lands directly opposite face {m(ans)}."],
            f"The three opposite face pairs are ({lbls[opp_pairs[0][0]]},{lbls[opp_pairs[0][1]]}), ({lbls[opp_pairs[1][0]]},{lbls[opp_pairs[1][1]]}), and ({lbls[opp_pairs[2][0]]},{lbls[opp_pairs[2][1]]}).",
            "نثبّت مربعاً مركزياً كقاعدة ونرفع الجوانب الأربعة بزاوية قائمة لتحديد كل زوج متقابل.",
            [f"عند طيّ الشبكة تتقابل الأزواج الثلاثة دون تداخل.",
             f"نجد أن الوجه المقابل للوجه {m(ask_v)} هو الوجه {m(ans)}."],
            f"تحقق: الأزواج المتقابلة هي ({lbls[opp_pairs[0][0]]}،{lbls[opp_pairs[0][1]]}) و({lbls[opp_pairs[1][0]]}،{lbls[opp_pairs[1][1]]}) و({lbls[opp_pairs[2][0]]}،{lbls[opp_pairs[2][1]]}).",
            diagram_en=svg_cube_net(cells_l),
        ))

    med_opp_sums = [10, 11, 13, 14, 15]
    for idx_m, target_s in enumerate(med_opp_sums):
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        coords, opp_pairs = net_templates[idx_m]
        vals = [0] * 6
        for p_idx, (u, v) in enumerate(opp_pairs):
            vals[u] = p_idx + 2 + idx_m
            vals[v] = target_s - vals[u]
        q_slot = opp_pairs[1][1]
        partner_v = vals[opp_pairs[1][0]]
        ans = vals[q_slot]
        vis_nums = ", ".join(str(vals[k]) for k in range(6) if k != q_slot)
        cells_l = [(coords[k][0], coords[k][1], "?" if k == q_slot else str(vals[k])) for k in range(6)]
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_cube_net_opposite",
            f"The net below (showing the five faces {vis_nums} and one {m('?')}) folds into a special Kangaroo die where **every pair of opposite faces has the same sum**. What number must replace {m('?')}?",
            f"تُطوى الشبكة أدناه (التي تظهر عليها الأعداد الخمسة {vis_nums} وعلامة {m('?')}) لتكوّن مكعب كانجارو خاصاً بحيث **يتساوى مجموع كل وجهين متقابلين**. ما العدد الذي يجب وضعه مكان العلامة {m('?')}؟",
            ans, [ans - 1, ans + 1, ans + 2, target_s - vals[opp_pairs[0][0]] + 2],
            "First find one complete opposite pair on the net to learn the constant opposite-face sum!",
            "ابحث أولاً عن زوج متقابل مكتمل على الشبكة لتعرف المجموع الثابت للأوجه المتقابلة!",
            "Find the constant sum S from a known opposite pair, then subtract the face opposite '?' from S.",
            [f"From a complete opposite pair on the net, the opposite sum is {m(f'{vals[opp_pairs[0][0]]} + {vals[opp_pairs[0][1]]} = {target_s}')}.",
             f"The face opposite {m('?')} is {m(partner_v)}, so {m(f'? = {target_s} - {partner_v} = {ans}')}."],
            f"{m(f'{partner_v} + {ans} = {target_s}')}, matching the other opposite pairs!",
            "نحسب المجموع الثابت من زوج متقابل معلوم ثم نطرح الوجه المقابل لـ '?'.",
            [f"مجموع كل وجهين متقابلين يساوي {m(target_s)}.",
             f"الوجه المقابل للعلامة {m('?')} هو {m(partner_v)}، إذن {m(f'? = {target_s} - {partner_v} = {ans}')}."],
            f"تحقق: {m(f'{partner_v} + {ans} = {target_s}')}.",
            diagram_en=svg_cube_net(cells_l),
        ))

    hard_dice = [
        (2, 1, 2, 3),
        (3, 5, 1, 3),
        (2, 6, 3, 2),
        (4, 4, 2, 1),
        (3, 2, 6, 4),
    ]
    for k_stack, top_v, front_v, right_v in hard_dice:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        # k_stack standard dice (opp faces sum to 7) stacked vertically in a single tower on a table; top face of top die is top_v.
        # Visible faces = 4*k_stack side faces + 1 top face = 14*k_stack + top_v!
        ans = 14 * k_stack + top_v
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_cube_net_opposite",
            f"Salim stacks {m(k_stack)} standard dice (where opposite faces always add to {m(7)}) vertically into a single tower on a wooden table. The very top face of the tower shows {m(top_v)} (like the top die shown). What is the **sum of the dots on all {m(4*k_stack + 1)} visible faces** around and on top of the tower?",
            f"رتّب سالم {m(k_stack)} أحجار نرد قياسية (مجموع كل وجهين متقابلين فيها يساوي {m(7)} دائماً) عمودياً فوق بعضها على طاولة خشبية. يظهر الرقم {m(top_v)} على الوجه العلوي لقمة البرج. ما **مجموع النقاط على جميع الأوجه المرئية الـ {m(4*k_stack + 1)}** حول البرج وفي قمته؟",
            ans, [ans - 7, ans + (7 - top_v), 21 * k_stack - top_v, ans - top_v],
            "Walking all the way around ANY single die in the tower shows two pairs of opposite vertical walls (7 + 7 = 14)!",
            "الدوران حول أي حجر نرد واحد في البرج يكشف زوجين من الجدران الرأسية المتقابلة (7 + 7 = 14)!",
            "Regardless of how each die is twisted horizontally, its 4 vertical side faces form two opposite pairs summing to 14!",
            [f"Each of the {m(k_stack)} dice contributes {m('2 \\times 7 = 14')} across its {m(4)} vertical side faces, giving {m(f'{k_stack} \\times 14 = {14*k_stack}')}.",
             f"Adding the single visible top face {m(top_v)} gives {m(f'{14*k_stack} + {top_v} = {ans}')}."],
            f"Total dots on {m(k_stack)} dice is {m(21*k_stack)}, minus hidden horizontal faces = {m(ans)}!",
            "الأوجه الجانبية الأربعة لأي نرد قياسي تتكوّن من زوجين متقابلين مجموعهما دائماً 14.",
            [f"مجموع الجوانب الأربعة لكل نرد = {m(14)}، ولعدد {m(k_stack)} أحجار = {m(f'{k_stack} \\times 14 = {14*k_stack}')}.",
             f"نضيف الوجه العلوي المرئي {m(top_v)} فنحصل على {m(f'{14*k_stack} + {top_v} = {ans}')}."],
            f"تحقق: المجموع لا يتأثر بدوران الأحجار أفقياً ويساوي {m(ans)}.",
            diagram_en=svg_kang_cube_faces(str(top_v), str(front_v), str(right_v)),
        ))

    # --- 15. kang_ben_polyomino_tiling (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    poly_shapes = [
        ([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], "plus pentomino", "بنتومينو علامة الزائد"),
        ([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)], "T-pentomino", "بنتومينو حرف T"),
        ([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)], "W-pentomino", "بنتومينو المتدرّج"),
        ([(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)], "U-pentomino", "بنتومينو حرف U"),
        ([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)], "J-hexomino", "سداسي المربعات"),
    ]
    for idx_p, (cells, sh_en, sh_ar) in enumerate(poly_shapes):
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        s_len = idx_p + 2
        cset = set(cells)
        edges = sum(1 for c, r in cells for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (c + dc, r + dr) not in cset)
        ans = edges * s_len
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_polyomino_tiling",
            f"The {sh_en} below is built from {m(len(cells))} identical squares, each of side {m(f'{s_len}\\text{{ cm}}')}. What is the **perimeter** of this shape in centimeters?",
            f"يتكوّن شكل {sh_ar} أدناه من {m(len(cells))} مربعات متطابقة طول ضلع كل منها {m(f'{s_len}\\text{{ سم}}')}. ما **محيط** هذا الشكل بالسنتيمتر؟",
            ans, [4 * len(cells) * s_len, (edges - 2) * s_len, (edges + 2) * s_len, len(cells) * s_len * s_len],
            "Count the outer unit boundary segments carefully, then multiply by the side length of one square!",
            "عُدّ القطع الخارجية على حدود الشكل بعناية ثم اضرب عددها في طول ضلع المربع الواحد!",
            "Count exposed boundary edges (or subtract 2 edges per internal shared seam from 4k), then multiply by side s.",
            [f"Walking around the boundary counts {m(edges)} outer square edges.",
             f"Each edge has length {m(s_len)} cm, so perimeter = {m(f'{edges} \\times {s_len} = {ans}\\text{{ cm}}')}."],
            f"{m(len(cells))} squares have {m(4*len(cells))} sides minus {m(4*len(cells) - edges)} glued sides = {m(edges)} outer sides.",
            "نعدّ الأضلاع الخارجية المكشوفة للشكل ثم نضرب في طول الضلع الواحد.",
            [f"عدد الأضلاع الخارجية المكشوفة على المحيط يساوي {m(edges)} ضلعاً.",
             f"المحيط = {m(f'{edges} \\times {s_len} = {ans}\\text{{ سم}}')}."],
            f"تحقق: {m(f'{edges} \\times {s_len} = {ans}')} سم.",
            diagram_en=svg_polyomino(cells, f"side = {s_len} cm"),
            diagram_ar=svg_polyomino(cells, f"الضلع = {s_len} سم"),
        ))

    med_boards = [
        ([[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 2], [0, 0, 0, 0]], 2, "1×2 dominoes", "قطع دومينو 1×2"),
        ([[1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 2, 2]], 3, "3-square L-trominoes", "قطع L الثلاثية"),
        ([[1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], 4, "2×2 square tiles", "بلاطات مربعة 2×2"),
        ([[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 2]], 3, "1×3 straight triominoes", "قطع مستقيمة 1×3"),
        ([[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2]], 2, "1×2 dominoes", "قطع دومينو 1×2"),
    ]
    for board, t_sz, t_en, t_ar in med_boards:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        white_cnt = sum(1 for row in board for v in row if v == 0)
        assert white_cnt % t_sz == 0
        ans = white_cnt // t_sz
        R, C = len(board), len(board[0])
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_polyomino_tiling",
            f"Some colored tiles have already been placed on the {m(f'{C} \\times {R}')} Kangaroo board below. How many **additional** non-overlapping {t_en} can completely tile all remaining white squares?",
            f"وُضعت بعض القطع الملوّنة على لوحة الكانجارو ذات الأبعاد {m(f'{C} \\times {R}')} أدناه. كم قطعة **إضافية** من {t_ar} يمكن وضعها دون تداخل لتغطية جميع المربعات البيضاء المتبقية؟",
            ans, [ans - 2 if ans > 2 else ans + 3, ans - 1, ans + 1, ans + 2],
            f"Count the remaining white unit squares and group them into clean {t_sz}-square blocks!",
            f"عُدّ المربعات البيضاء المتبقية وقسّمها إلى مجموعات من {t_sz} مربعات!",
            "Count uncovered white cells and verify they partition cleanly into the given tile shape.",
            [f"The {m(f'{C} \\times {R}')} board has {m(R*C)} cells, with {m(white_cnt)} white cells still uncovered.",
             f"The white region splits cleanly into {m(f'{white_cnt} \\div {t_sz} = {ans}')} tiles."],
            f"{m(f'{ans} \\times {t_sz} = {white_cnt}')} white squares covered with zero gaps.",
            "نحصي المربعات البيضاء الفارغة ونتحقق من قابليتها للتبليط الكامل بالقطع المطلوبة.",
            [f"عدد المربعات البيضاء غير المغطاة يساوي {m(white_cnt)} مربعاً.",
             f"تتسع المنطقة البيضاء بالضبط لعدد {m(f'{white_cnt} \\div {t_sz} = {ans}')} من القطع."],
            f"تحقق: {m(f'{ans} \\times {t_sz} = {white_cnt}')} مربعاً.",
            diagram_en=svg_kang_polyomino_board(board),
        ))

    for idx_h, (cells, sh_en, sh_ar) in enumerate(poly_shapes):
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        s_len = idx_h + 3
        cset = set(cells)
        edges = sum(1 for c, r in cells for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (c + dc, r + dr) not in cset)
        perim = edges * s_len
        ans = len(cells) * (s_len ** 2)
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_polyomino_tiling",
            f"The {sh_en} below is formed from {m(len(cells))} identical squares glued edge-to-edge. If the **perimeter** of the whole figure is {m(f'{perim}\\text{{ cm}}')}, what is the **total area** of the figure in {m('\\text{cm}^2')}?",
            f"تشكّل {sh_ar} أدناه من لصق {m(len(cells))} مربعات متطابقة حافةً بحافة. إذا كان **محيط** الشكل الكلي يساوي {m(f'{perim}\\text{{ سم}}')}، فما **المساحة الكلية** للشكل بالـ {m('\\text{سم}^2')}؟",
            ans, [len(cells) * s_len, edges * s_len * s_len // 2, ans - s_len * s_len, ans + s_len * s_len],
            "First count how many outer square sides make up the perimeter to find the side length s of ONE square, then compute k × s²!",
            "عُدّ أولاً كم ضلعاً خارجياً يكوّن المحيط لتعرف طول ضلع المربع الواحد s، ثم احسب المساحة k × s²!",
            "Divide the perimeter by the count of outer edges to get unit side s, then multiply s² by the number of squares.",
            [f"The outer boundary consists of {m(edges)} equal segments, so one square has side {m(f's = {perim} \\div {edges} = {s_len}\\text{{ cm}}')}.",
             f"Each square has area {m(f'{s_len}^2 = {s_len**2}\\text{{ cm}}^2')}, giving total area {m(f'{len(cells)} \\times {s_len**2} = {ans}\\text{{ cm}}^2')}."],
            f"Side {m(s_len)} cm × {m(edges)} outer edges = {m(perim)} cm perimeter!",
            "نقسم المحيط على عدد الأضلاع الخارجية لإيجاد طول ضلع المربع الواحد s ثم نضرب مساحة المربع s² في عدد المربعات.",
            [f"عدد الأضلاع الخارجية = {m(edges)}، إذن طول ضلع المربع الواحد {m(f's = {perim} \\div {edges} = {s_len}\\text{{ سم}}')}.",
             f"مساحة الشكل الكلي = {m(f'{len(cells)} \\times {s_len}^2 = {ans}\\text{{ سم}}^2')}."],
            f"تحقق: {m(f'{edges} \\times {s_len} = {perim}')} سم.",
            diagram_en=svg_polyomino(cells, f"Perimeter = {perim} cm"),
            diagram_ar=svg_polyomino(cells, f"المحيط = {perim} سم"),
        ))

    # --- 16. kang_ben_gear_rotations (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_gears = [(24, 12, 3, 3), (20, 10, 4, 4), (30, 15, 2, 3), (18, 9, 5, 4), (36, 12, 2, 4)]
    for t1, t_last, r1, n_g in easy_gears:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        ans = (t1 * r1) // t_last
        g_names = [chr(65 + i) for i in range(n_g)]
        disp_lbls = [f"A ({t1})"] + g_names[1:-1] + [f"{g_names[-1]} ({t_last})"]
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Easy", "kang_ben_gear_rotations",
            f"In the {m(n_g)}-gear train shown, Gear {m('A')} has {m(t1)} teeth and Gear {m(g_names[-1])} has {m(t_last)} teeth. When Gear {m('A')} makes {m(r1)} full turns, how many full turns does Gear {m(g_names[-1])} make?",
            f"في سلسلة التروس المكوّنة من {m(n_g)} تروس أدناه، للترس {m('A')} عدد {m(t1)} سناً وللترس {m(g_names[-1])} عدد {m(t_last)} سناً. عندما يدور الترس {m('A')} بمقدار {m(r1)} دورات كاملة، كم دورة كاملة يدور الترس {m(g_names[-1])}؟",
            ans, [r1, max(1, ans // 2), ans + 2, ans * 2],
            "Middle gears just pass teeth along! Use T_first × R_first = T_last × R_last!",
            "التروس الوسطى تنقل الحركة فقط! طبّق القاعدة: أسنان الأول × دوراته = أسنان الأخير × دوراته!",
            "Every meshing contact pushes the exact same number of teeth.",
            [f"Gear {m('A')} advances {m(f'{t1} \\times {r1} = {t1*r1}')} teeth.",
             f"Gear {m(g_names[-1])} advances {m(t1*r1)} teeth too, making {m(f'{t1*r1} \\div {t_last} = {ans}')} full turns."],
            f"{m(f'{t1} \\times {r1} = {t_last} \\times {ans} = {t1*r1}')} teeth.",
            "عدد الأسنان المارّة متساوٍ عند جميع نقاط التلامس.",
            [f"يحرّك الترس {m('A')} عدداً قدره {m(f'{t1} \\times {r1} = {t1*r1}')} سناً.",
             f"يدور الترس {m(g_names[-1])} عدد {m(f'{t1*r1} \\div {t_last} = {ans}')} دورات كاملة."],
            f"تحقق: {m(f'{t1} \\times {r1} = {t_last} \\times {ans}')}.",
            diagram_en=svg_kang_gear_train(disp_lbls, "CW ↻"),
        ))

    med_gears = [(28, 3, 7, 4), (32, 3, 6, 3), (24, 5, 8, 5), (30, 4, 6, 4), (36, 5, 9, 3)]
    for t1, r1, r_last, n_g in med_gears:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        ans = (t1 * r1) // r_last
        g_names = [chr(65 + i) for i in range(n_g)]
        disp_lbls = [f"A ({t1})"] + g_names[1:-1] + [f"{g_names[-1]} (?)"]
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Medium", "kang_ben_gear_rotations",
            f"In the {m(n_g)}-gear line shown, Gear {m('A')} has {m(t1)} teeth. Whenever Gear {m('A')} completes {m(r1)} full rotations, the final Gear {m(g_names[-1])} completes {m(r_last)} full rotations. How many teeth does Gear {m(g_names[-1])} have?",
            f"في صف التروس ذي الـ {m(n_g)} تروس أدناه، للترس {m('A')} عدد {m(t1)} سناً. كلما أتمّ الترس {m('A')} عدد {m(r1)} دورات كاملة، أتمّ الترس الأخير {m(g_names[-1])} عدد {m(r_last)} دورات كاملة. كم سناً للترس {m(g_names[-1])}؟",
            ans, [ans - 3, ans + 4, (t1 * r_last) // r1, t1 - r_last],
            "Multiply Gear A's teeth by its rotations, then divide by the rotations of the final gear!",
            "اضرب عدد أسنان الترس A في دوراته، ثم اقسم الناتج على عدد دورات الترس الأخير!",
            "By tooth conservation, T_last = (T_A × R_A) ÷ R_last.",
            [f"Total teeth moved = {m(f'{t1} \\times {r1} = {t1*r1}')}.",
             f"Teeth on Gear {m(g_names[-1])} = {m(f'{t1*r1} \\div {r_last} = {ans}')}."],
            f"{m(f'{ans} \\times {r_last} = {t1*r1} = {t1} \\times {r1}')}.",
            "من قانون تساوي الأسنان المارّة نقسم إجمالي الأسنان المتحركة على دورات الترس الأخير.",
            [f"إجمالي الأسنان المتحركة = {m(f'{t1} \\times {r1} = {t1*r1}')} سناً.",
             f"عدد أسنان الترس {m(g_names[-1])} = {m(f'{t1*r1} \\div {r_last} = {ans}')} سناً."],
            f"تحقق: {m(f'{ans} \\times {r_last} = {t1*r1}')}.",
            diagram_en=svg_kang_gear_train(disp_lbls, "CW ↻"),
        ))

    hard_gears = [(12, 8, 18), (15, 10, 12), (16, 12, 24), (14, 21, 7), (18, 12, 15)]
    for t_a, t_b, t_c in hard_gears:
        qid = f"KANG-BEN-{180 + len(qs) + 1:03d}"
        lc_t = math.lcm(t_a, t_b, t_c)
        ans = lc_t // t_a
        qs.append(make_kang_q(
            qid, LEVEL, "Geometry", "Hard", "kang_ben_gear_rotations",
            f"Three meshing gears {m('A, B, C')} have {m(t_a)}, {m(t_b)}, and {m(t_c)} teeth respectively, and each has a painted dot at the top before turning begins. What is the **smallest positive** number of full rotations Gear {m('A')} must make so that **all three** painted dots return to the exact top position simultaneously?",
            f"ثلاثة تروس متشابكة {m('A, B, C')} أعداد أسنانها {m(t_a)} و{m(t_b)} و{m(t_c)} على الترتيب، وعلى قمة كل ترس نقطة حمراء قبل بدء الدوران. ما **أصغر** عدد موجب من الدورات الكاملة يجب أن يدورها الترس {m('A')} لتعود النقاط الثلاث **جميعاً** إلى قممها في اللحظة نفسها؟",
            ans, [max(1, ans - 1), ans + 1, lc_t // t_b, math.lcm(t_a, t_c) // t_a if math.lcm(t_a, t_c) != lc_t else ans + 2],
            "All three gears return to their starting positions when the total number of teeth moved equals LCM(t_A, t_B, t_C)!",
            "تعود التروس الثلاثة لوضعها الابتدائي معاً عندما يساوي عدد الأسنان المتحركة المضاعف المشترك الأصغر لأعداد أسنانها!",
            "Find LCM(t_A, t_B, t_C) for total teeth passed, then divide by Gear A's tooth count!",
            [f"Compute {m(f'\\operatorname{{lcm}}({t_a}, {t_b}, {t_c}) = {lc_t}')} teeth.",
             f"Divide by Gear {m('A')}'s {m(t_a)} teeth: {m(f'{lc_t} \\div {t_a} = {ans}')} full rotations."],
            f"At {m(lc_t)} teeth: A makes {m(ans)} turns, B makes {m(lc_t // t_b)} turns, C makes {m(lc_t // t_c)} turns—all whole numbers!",
            "نحسب المضاعف المشترك الأصغر لأعداد الأسنان الثلاثة ثم نقسمه على أسنان الترس الأول A.",
            [f"المضاعف المشترك الأصغر للأسنان هو {m(f'\\operatorname{{lcm}}({t_a}, {t_b}, {t_c}) = {lc_t}')} سناً.",
             f"عدد دورات الترس {m('A')} يساوي {m(f'{lc_t} \\div {t_a} = {ans}')} دورات كاملة."],
            f"عند مرور {m(lc_t)} سناً تكمل التروس الثلاثة أعداداً صحيحة من الدورات معاً!",
            diagram_en=svg_kang_gear_train([f"A ({t_a})", f"B ({t_b})", f"C ({t_c})"], "CW ↻"),
        ))

    assert len(qs) == 60
    return qs


def _unit_5() -> list[dict]:
    qs: list[dict] = []

    def _count_bracelets(multiset_beads: list[str]) -> int:
        from itertools import permutations
        n = len(multiset_beads)
        canon = set()
        for p in set(permutations(multiset_beads)):
            rots = [p[i:] + p[:i] for i in range(n)]
            rev = p[::-1]
            flips = [rev[i:] + rev[:i] for i in range(n)]
            canon.add(min(rots + flips))
        return len(canon)

    # --- 17. kang_ben_venn_two_sets (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_venn = [
        (28, 19, 16, "Robotics", "Origami", "الروبوت", "الأوريغامي"),
        (32, 21, 18, "Swimming", "Archery", "السباحة", "الرماية"),
        (25, 17, 14, "Coding", "Drama", "البرمجة", "المسرح"),
        (35, 24, 20, "French", "Spanish", "الفرنسية", "الإسبانية"),
        (40, 27, 23, "Astronomy", "Pottery", "الفلك", "الخزف"),
    ]
    for N, nA, nB, la_en, lb_en, la_ar, lb_ar in easy_venn:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = nA + nB - N
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Easy", "kang_ben_venn_two_sets",
            f"Every one of the {m(N)} students in a Benjamin workshop joins **{la_en}**, **{lb_en}**, or both. If {m(nA)} join {la_en} and {m(nB)} join {lb_en}, how many students join **both**?",
            f"يشارك كل طالب من طلاب ورشة بنجامين البالغ عددهم {m(N)} في نشاط **{la_ar}** أو **{lb_ar}** أو كليهما. إذا شارك {m(nA)} في {la_ar} و{m(nB)} في {lb_ar}، فكم طالباً يشارك في **النشاطين معاً**؟",
            ans, [N - nA, N - nB, ans + 3, max(1, ans - 2)],
            "Add the two club counts and subtract the total number of students!",
            "اجمع عددي النشاطين ثم اطرح العدد الكلي للطلاب!",
            "By Inclusion-Exclusion, Overlap = |A| + |B| − |A ∪ B|.",
            [f"Sum of both lists = {m(f'{nA} + {nB} = {nA+nB}')}.",
             f"Students in both = {m(f'{nA+nB} - {N} = {ans}')}."],
            f"{m(f'({nA}-{ans}) + {ans} + ({nB}-{ans}) = {N}')}.",
            "من مبدأ التضمين والإقصاء: التقاطع = مجموع المجموعتين ناقص الاتحاد.",
            [f"مجموع القائمتين = {m(f'{nA} + {nB} = {nA+nB}')}.",
             f"عدد المشاركين في النشاطين معاً = {m(f'{nA+nB} - {N} = {ans}')}."],
            f"تحقق: {m(f'{nA-ans} + {ans} + {nB-ans} = {N}')}.",
            diagram_en=svg_venn_2(f"{la_en} ({nA})", f"{lb_en} ({nB})", "", "?", ""),
            diagram_ar=svg_venn_2(f"{la_ar} ({nA})", f"{lb_ar} ({nB})", "", "؟", ""),
        ))

    med_venn = [
        (34, 20, 17, 5, "Chess", "Calligraphy", "الشطرنج", "الخط العربي"),
        (38, 23, 19, 4, "Violin", "Flute", "الكمان", "الناي"),
        (30, 18, 15, 3, "Tennis", "Badminton", "التنس", "الريشة"),
        (42, 25, 22, 6, "Gardening", "Cooking", "البستنة", "الطهي"),
        (36, 21, 18, 5, "Debate", "Journalism", "المناظرة", "الصحافة"),
    ]
    for N, nA, nB, out, la_en, lb_en, la_ar, lb_ar in med_venn:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        union = N - out
        both = nA + nB - union
        ans = nA - both
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "kang_ben_venn_two_sets",
            f"In a Grade 6 group of {m(N)} pupils, {m(nA)} take **{la_en}**, {m(nB)} take **{lb_en}**, and {m(out)} take neither. How many pupils take **{la_en} ONLY** (and NOT {lb_en})?",
            f"في مجموعة بالصف السادس تضمّ {m(N)} تلميذاً، يدرس {m(nA)} **{la_ar}**، ويدرس {m(nB)} **{lb_ar}**، بينما لا يدرس {m(out)} أياً منهما. كم تلميذاً يدرس **{la_ar} فقط** (دون {lb_ar})؟",
            ans, [both, nB - both, nA - out, ans + 3],
            f"First find the active union ({N} − {out}), then find 'both', and finally subtract 'both' from {nA}!",
            f"أوجد أولاً الاتحاد ({N} − {out})، ثم احسب التقاطع، وأخيراً اطرح التقاطع من {nA}!",
            "Notice the shortcut: Only A = |A ∪ B| − |B|!",
            [f"Active union = {m(f'{N} - {out} = {union}')}, so overlap = {m(f'{nA} + {nB} - {union} = {both}')}.",
             f"Pupils in {la_en} only = {m(f'{nA} - {both} = {ans}')} (or directly {m(f'{union} - {nB} = {ans}')}!)."],
            f"{m(f'{ans} + {both} + {nB - both} + {out} = {N}')}.",
            "نحسب الاتحاد ثم التقاطع، ثم نطرح التقاطع من المجموعة الأولى (أو مباشرة: الاتحاد ناقص الثانية!).",
            [f"الاتحاد = {m(f'{N} - {out} = {union}')}، والتقاطع = {m(both)}.",
             f"عدد دارسي {la_ar} فقط = {m(f'{nA} - {both} = {ans}')}."],
            f"تحقق: {m(f'{ans} + {both} + {nB - both} + {out} = {N}')}.",
            diagram_en=svg_venn_2(f"{la_en} ({nA})", f"{lb_en} ({nB})", "?", "", "", str(out)),
            diagram_ar=svg_venn_2(f"{la_ar} ({nA})", f"{lb_ar} ({nB})", "؟", "", "", str(out)),
        ))

    hard_venn = [
        (33, 3, 6, 2, "Science", "Art", "العلوم", "الفنون"),
        (37, 4, 7, 3, "Math", "Music", "الرياضيات", "الموسيقى"),
        (41, 5, 6, 2, "Scouts", "Choir", "الكشافة", "الإنشاد"),
        (44, 4, 8, 2, "Cycling", "Skating", "الدراجات", "التزلج"),
        (49, 5, 8, 3, "Puzzles", "Theater", "الألغاز", "المسرح"),
    ]
    for N, out, both, k_mult, la_en, lb_en, la_ar, lb_ar in hard_venn:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        union = N - out
        assert (union + both) % (k_mult + 1) == 0
        nB = (union + both) // (k_mult + 1)
        ans = k_mult * nB
        w_en = "twice" if k_mult == 2 else "three times"
        w_ar = "ضعف" if k_mult == 2 else "ثلاثة أمثال"
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "kang_ben_venn_two_sets",
            f"Out of {m(N)} Benjamin students, {m(out)} join neither club and {m(both)} belong to **both** **{la_en}** and **{lb_en}**. If the total number in {la_en} is **{w_en}** the total number in {lb_en}, how many students are in **{la_en}** (including the overlap)?",
            f"من بين {m(N)} طالباً في قسم بنجامين، لا ينتمي {m(out)} لأي نادٍ بينما ينتمي {m(both)} لناديَي **{la_ar}** و**{lb_ar}** معاً. إذا كان إجمالي أعضاء نادي {la_ar} يساوي **{w_ar}** إجمالي أعضاء نادي {lb_ar}، فكم طالباً في نادي **{la_ar}**؟",
            ans, [ans - both, nB, ans + both, union - nB],
            f"Write |A| + |B| − {both} = {N} − {out}, and substitute |A| = {k_mult}|B|!",
            f"اكتب المعادلة |A| + |B| − {both} = {N} − {out} وعوّض |A| = {k_mult}|B|!",
            f"Use {m('|A| + |B| = |A \\cup B| + |A \\cap B|')} to find {m('|B|')} first.",
            [f"Active union {m(f'|A \\cup B| = {N} - {out} = {union}')}, so {m(f'|A| + |B| = {union} + {both} = {union+both}')}.",
             f"Since {m(f'|A| = {k_mult}|B|')}, {m(f'{k_mult+1}|B| = {union+both} \\implies |B| = {nB}')}, and {m(f'|A| = {k_mult} \\times {nB} = {ans}')}."],
            f"{m(f'{ans} + {nB} - {both} = {union}')} and {m(f'{union} + {out} = {N}')}!",
            "نوجد مجموع المجموعتين من الاتحاد + التقاطع ثم نقسم على مجموع الحصص.",
            [f"الاتحاد = {m(union)}، إذن {m(f'|A| + |B| = {union} + {both} = {union+both}')}.",
             f"بما أن {m(f'|A| = {k_mult}|B|')} نجد {m(f'|B| = {nB}')} ومنه {m(f'|A| = {ans}')}."],
            f"تحقق: {m(f'{ans} + {nB} - {both} = {union}')}.",
            diagram_en=svg_venn_2(f"{la_en} ({k_mult}x)", f"{lb_en} (x)", "", str(both), "", str(out)),
            diagram_ar=svg_venn_2(f"{la_ar} ({k_mult}x)", f"{lb_ar} (x)", "", str(both), "", str(out)),
        ))

    # --- 18. kang_ben_pigeonhole_gloves (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_ph = [
        ([6, 7, 5], 2, "socks", "جوارب"),
        ([8, 6, 9, 5], 2, "crayons", "أقلام تلوين"),
        ([7, 8, 6], 3, "mittens", "قفازات صوفية متماثلة"),
        ([9, 7, 8, 6], 3, "ribbons", "شرائط ملونة"),
        ([10, 9, 8], 4, "stickers", "ملصقات"),
    ]
    c_names_en = ["Red", "Blue", "Green", "Gold"]
    c_names_ar = ["أحمر", "أزرق", "أخضر", "ذهبي"]
    for counts, goal_m, it_en, it_ar in easy_ph:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        worst = sum(min(c, goal_m - 1) for c in counts)
        ans = worst + 1
        desc_en = ", ".join(f"{m(c)} {c_names_en[i].lower()}" for i, c in enumerate(counts))
        desc_ar = " و".join(f"{m(c)} ({c_names_ar[i]})" for i, c in enumerate(counts))
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Easy", "kang_ben_pigeonhole_gloves",
            f"A dark pouch holds {desc_en} {it_en}. Without looking, what is the **minimum** number you must draw to be certain of getting at least {m(goal_m)} {it_en} of the **same color**?",
            f"يحتوي كيس معتم على {it_ar} أعدادها: {desc_ar}. دون النظر، ما **أقل** عدد يجب سحبه لضمان الحصول على {m(goal_m)} على الأقل من **اللون نفسه**؟",
            ans, [worst, goal_m + 1, ans + 1, ans + 2],
            f"In the worst case, you draw {goal_m - 1} of every available color before getting the {goal_m}-th of one color!",
            f"في أسوأ حالة تسحب {goal_m - 1} من كل لون متاح قبل اكتمال العدد {goal_m} لأي لون!",
            "Add 1 to the maximum failing draw.",
            [f"With {m(len(counts))} colors, the unluckiest failing draw takes {m(goal_m - 1)} of each color = {m(worst)}.",
             f"One more pick ({m(f'{worst} + 1 = {ans}')}) guarantees {m(goal_m)} of one color."],
            f"{m(worst)} picks can split evenly below {m(goal_m)}, while {m(ans)} cannot!",
            "نحسب أقصى سحب فاشل بأخذ (m − 1) من كل لون ثم نضيف 1.",
            [f"أسوأ سحب دون تحقق الشرط يأخذ {m(goal_m - 1)} من كل لون من الألوان الـ {m(len(counts))} أي {m(worst)}.",
             f"السحبة التالية ({m(f'{worst} + 1 = {ans}')}) تحسم التطابق حتماً."],
            f"تحقق: عند {m(ans)} سحبات لا بد أن يصل أحد الألوان إلى {m(goal_m)}.",
            diagram_en=svg_bar_chart([(c_names_en[i], c, str(c)) for i, c in enumerate(counts)], max(counts) + 2),
            diagram_ar=svg_bar_chart([(c_names_ar[i], c, str(c)) for i, c in enumerate(counts)], max(counts) + 2),
        ))

    med_ph = [
        ([2, 7, 8], 4, "tokens", "أقراص"),
        ([1, 6, 9, 7], 3, "beads", "خرزات"),
        ([3, 9, 10], 5, "erasers", "ممحايات"),
        ([2, 3, 8, 9], 4, "buttons", "أزرار"),
        ([4, 11, 12], 6, "shells", "أصداف"),
    ]
    for counts, goal_m, it_en, it_ar in med_ph:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        worst = sum(min(c, goal_m - 1) for c in counts)
        ans = worst + 1
        naive_trap = len(counts) * (goal_m - 1) + 1
        desc_en = ", ".join(f"{m(c)} {c_names_en[i].lower()}" for i, c in enumerate(counts))
        desc_ar = " و".join(f"{m(c)} ({c_names_ar[i]})" for i, c in enumerate(counts))
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "kang_ben_pigeonhole_gloves",
            f"A wooden chest holds {desc_en} {it_en}. In the dark, what is the **smallest** number of {it_en} Jude must take out to be **100% sure** she gets at least {m(goal_m)} of the **same color**?",
            f"يضمّ صندوق خشبي {it_ar} أعدادها: {desc_ar}. في الظلام، ما **أصغر** عدد يجب أن تسحبه جود لتكون **متأكدة تماماً** من الحصول على {m(goal_m)} على الأقل من **اللون نفسه**؟",
            ans, [naive_trap, worst, ans - 2, naive_trap + 1],
            f"Watch out! One or more colors have FEWER than {goal_m} items in total—you can only draw as many of those as exist!",
            f"انتبه! بعض الألوان عددها الكلي أصغر من {goal_m}؛ في أسوأ حالة تسحب كل المتاح منها فقط!",
            f"For each color {m('i')}, the worst failing draw takes {m(f'\\min(c_i, {goal_m - 1})')}.",
            [f"Maximum failing picks per color: {' + '.join(str(min(c, goal_m - 1)) for c in counts)} = {m(worst)}.",
             f"Adding {m(1)} more item gives {m(f'{worst} + 1 = {ans}')}, forcing one of the larger colors to reach {m(goal_m)}!"],
            f"Don't fall for the {m(naive_trap)} trap—colors with fewer than {m(goal_m - 1)} items run out early!",
            f"لكل لون نأخذ في أسوأ حالة الأصغر بين عدده الكلي وبين {m(goal_m - 1)}.",
            [f"أقصى سحب غير ناجح = {' + '.join(str(min(c, goal_m - 1)) for c in counts)} = {m(worst)}.",
             f"بإضافة سحبة واحدة يصبح العدد المضمون {m(f'{worst} + 1 = {ans}')}."],
            f"انتبه لفخ {m(naive_trap)} لأن الألوان القليلة تنفد مبكراً!",
            diagram_en=svg_bar_chart([(c_names_en[i], c, str(c)) for i, c in enumerate(counts)], max(counts) + 2),
            diagram_ar=svg_bar_chart([(c_names_ar[i], c, str(c)) for i, c in enumerate(counts)], max(counts) + 2),
        ))

    hard_gloves = [
        (4, 3, "any"),
        (5, 4, "any"),
        (6, 5, "any"),
        (4, 5, "red"),
        (5, 6, "red"),
    ]
    for p_red, p_blue, target_mode in hard_gloves:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        tot_g = 2 * (p_red + p_blue)
        if target_mode == "any":
            worst = p_red + p_blue  # all LEFT gloves of both colors!
            ans = worst + 1
            goal_en = "a wearable **Left–Right pair of the SAME color**"
            goal_ar = "**زوج قابل للارتداء (يمين + يسار) من اللون نفسه**"
            idea_s = f"Worst case pulls ALL {p_red} left-red gloves and ALL {p_blue} left-blue gloves ({worst} left gloves total)!"
            idea_a = f"أسوأ حالة تسحب جميع القفازات اليسرى الحمراء ({p_red}) واليسرى الزرقاء ({p_blue}) بمجموع {worst} قفازات يسرى!"
        else:
            worst = 2 * p_blue + p_red  # all blue gloves + all left-red gloves!
            ans = worst + 1
            goal_en = "a wearable **Left–Right pair of RED gloves**"
            goal_ar = "**زوج قابل للارتداء (يمين + يسار) من القفازات الحمراء تحديداً**"
            idea_s = f"Worst case pulls ALL {2*p_blue} blue gloves AND all {p_red} left-red gloves ({worst} gloves) before a single right-red glove!"
            idea_a = f"أسوأ حالة تسحب جميع القفازات الزرقاء ({2*p_blue}) وجميع الحمراء اليسرى ({p_red}) قبل خروج أي قفاز أحمر أيمن!"
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "kang_ben_pigeonhole_gloves",
            f"A closet bin holds {m(p_red)} pairs of red winter gloves and {m(p_blue)} pairs of blue winter gloves ({m(tot_g)} individual gloves; left and right hands differ!). Without looking, what is the **minimum** number of single gloves Kareem must pull out to guarantee {goal_en}?",
            f"يحتوي صندوق على {m(p_red)} أزواج من القفازات الشتوية الحمراء و{m(p_blue)} أزواج من الزرقاء ({m(tot_g)} فردة قفاز؛ اليد اليمنى تختلف عن اليسرى!). دون النظر، ما **أقل** عدد من الفردات يجب أن يسحبه كريم لضمان {goal_ar}؟",
            ans, [3, worst, p_red + p_blue + 2 if target_mode == "red" else tot_g // 2 + 2, ans + 2],
            "Left gloves DO NOT match each other! Count how many gloves can come out with ZERO wearable target pairs!",
            "القفازات اليسرى لا تكوّن زوجاً مع بعضها! احسب أقصى عدد يمكن خروجه دون اكتمال زوج يمين ويسار مطلوب!",
            idea_s,
            [f"Maximum failing draw = {m(worst)} single gloves.",
             f"Drawing {m(1)} more glove ({m(f'{worst} + 1 = {ans}')}) forces a matching right-hand glove!"],
            f"With {m(worst)} gloves you can still fail; the {m(ans)}-th glove guarantees success!",
            idea_a,
            [f"أقصى عدد من الفردات دون تحقق الشرط يساوي {m(worst)} فردة.",
             f"بإضافة فردة واحدة أخرى يصبح العدد المضمون {m(f'{worst} + 1 = {ans}')}."],
            f"تحقق: عند {m(ans)} فردات يتحقق الزوج المطلوب بنسبة 100%.",
            diagram_en=svg_bar_chart([("Red L", p_red, str(p_red)), ("Red R", p_red, str(p_red)), ("Blue L", p_blue, str(p_blue)), ("Blue R", p_blue, str(p_blue))], max(p_red, p_blue) + 2),
            diagram_ar=svg_bar_chart([("أحمر يسرى", p_red, str(p_red)), ("أحمر يمنى", p_red, str(p_red)), ("أزرق يسرى", p_blue, str(p_blue)), ("أزرق يمنى", p_blue, str(p_blue))], max(p_red, p_blue) + 2),
        ))

    # --- 19. kang_ben_handshake_polygon (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    for n_p, ctx_en, ctx_ar in [
        (6, "captains shake hands", "قادة فرق يتصافحون"),
        (7, "chess players play one game against each other", "لاعبي شطرنج يلعب كل اثنين مباراة واحدة"),
        (9, "astronomers exchange mission patches", "علماء فلك يتبادلون التحية مرة واحدة"),
        (10, "island piers connected by direct ferry lines", "موانئ جزر يربط بين كل اثنين خط مباشر"),
        (11, "badminton finalists play a round-robin match", "متأهلين يلعب كل اثنين مباراة واحدة"),
    ]:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = n_p * (n_p - 1) // 2
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Easy", "kang_ben_handshake_polygon",
            f"In a Benjamin event with {m(n_p)} participants ({ctx_en}), every pair interacts **exactly once**. What is the total number of pairwise interactions?",
            f"في فعالية بنجامين تضمّ {m(n_p)} مشاركين ({ctx_ar})، يتفاعل كل زوج **مرة واحدة بالضبط**. ما العدد الكلي لهذه التفاعلات الثنائية؟",
            ans, [n_p * (n_p - 1), n_p * (n_p - 3) // 2, ans - n_p + 1, ans + n_p],
            "Multiply n by (n − 1) and divide by 2 so you don't count each pair twice!",
            "اضرب n في (n − 1) ثم اقسم على 2 لعدم تكرار كل زوج!",
            f"Total pairs among {m('n')} items is {m('\\frac{n(n-1)}{2}')}.",
            [f"Each of the {m(n_p)} participants pairs with {m(n_p - 1)} others.",
             f"Divide by {m(2)}: {m(f'\\frac{{{n_p} \\times {n_p - 1}}}{{2}} = {ans}')}."],
            f"{m(f'1 + 2 + \\dots + {n_p - 1} = {ans}')}.",
            f"عدد الأزواج من بين {m('n')} عناصر يساوي {m('\\frac{n(n-1)}{2}')}.",
            [f"نضرب {m(f'{n_p} \\times {n_p - 1} = {n_p*(n_p-1)}')}.",
             f"نقسم على {m(2)} فنحصل على {m(ans)}."],
            f"تحقق: {m(f'{n_p}({n_p-1})/2 = {ans}')}.",
            diagram_en=svg_graph_cycle_chords(min(n_p, 8), True),
        ))

    for n_poly, nm_en, nm_ar in [
        (6, "hexagon", "المضلع السداسي"),
        (7, "heptagon", "المضلع السباعي"),
        (8, "octagon", "المضلع الثماني"),
        (9, "nonagon", "المضلع التساعي"),
        (10, "decagon", "المضلع العشاري"),
    ]:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = n_poly * (n_poly - 3) // 2
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "kang_ben_handshake_polygon",
            f"How many **diagonals** (segments joining non-adjacent vertices) can be drawn inside a convex **{nm_en}** ({m(n_poly)} vertices)?",
            f"كم **قطراً** (قطعة مستقيمة تصل بين رأسين غير متجاورين) يمكن رسمه داخل **{nm_ar}** المحدّب ({m(n_poly)} رؤوس)؟",
            ans, [n_poly * (n_poly - 1) // 2, n_poly * (n_poly - 3), ans + n_poly, max(1, ans - 3)],
            "From each vertex you can draw diagonals to (n − 3) other vertices (excluding itself and its 2 neighbors), then divide by 2!",
            "من كل رأس يخرج (n − 3) قطراً (باستثناء الرأس نفسه وجاريه)، ثم نقسم المجموع على 2!",
            f"Number of diagonals of an {m('n')}-gon is {m('\\frac{n(n-3)}{2}')}.",
            [f"Each of the {m(n_poly)} vertices connects diagonally to {m(f'{n_poly} - 3 = {n_poly - 3}')} vertices.",
             f"Dividing by {m(2)} gives {m(f'\\frac{{{n_poly} \\times {n_poly - 3}}}{{2}} = {ans}')} diagonals."],
            f"All pairs {m(n_poly*(n_poly-1)//2)} minus {m(n_poly)} outer sides = {m(ans)} diagonals!",
            f"عدد أقطار المضلع ذي {m('n')} أضلاع يساوي {m('\\frac{n(n-3)}{2}')}.",
            [f"من كل رأس من الرؤوس الـ {m(n_poly)} ينطلق {m(n_poly - 3)} أقطار.",
             f"بالقسمة على {m(2)} لمنع التكرار نجد {m(ans)} قطراً."],
            f"تحقق: جميع الأزواج {m(n_poly*(n_poly-1)//2)} ناقص {m(n_poly)} أضلاع = {m(ans)}.",
            diagram_en=svg_regular_polygon(min(n_poly, 8), [(0, 2), (0, 3), (1, 4)]),
        ))

    for n_ans, mode in [(8, "diag_reverse"), (9, "handshake_reverse"), (10, "handshake_reverse"), (11, "diag_reverse"), (12, "handshake_reverse")]:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        if mode == "handshake_reverse":
            tot_h = n_ans * (n_ans - 1) // 2
            q_e = f"At a Kangaroo math circle, everyone shook hands with everyone else **exactly once**, producing {m(tot_h)} handshakes in total. How many people attended the math circle?"
            q_a = f"في حلقة الكانجارو الرياضية صافح كل شخص جميع الآخرين **مرة واحدة بالضبط** فبلغ مجموع المصافحات {m(tot_h)} مصافحة. كم شخصاً حضر الحلقة؟"
            eq_s = f"\\frac{{n(n-1)}}{{2}} = {tot_h} \\implies n(n-1) = {2*tot_h}"
            prod_s = f"{n_ans} \\times {n_ans - 1} = {2*tot_h}"
        else:
            tot_d = n_ans * (n_ans - 3) // 2
            q_e = f"Around a circular table, each person clinks juice glasses with everyone **except** themselves and their {m(2)} immediate neighbors (left and right). If {m(tot_d)} clinks happen in total, how many people are seated around the table?"
            q_a = f"حول طاولة مستديرة يقرع كل شخص كأسه مع الجميع **ما عدا** نفسه وجارَيه المباشرين (عن يمينه ويساره). إذا حدثت {m(tot_d)} قرعة في المجموع، فكم شخصاً يجلس حول الطاولة؟"
            eq_s = f"\\frac{{n(n-3)}}{{2}} = {tot_d} \\implies n(n-3) = {2*tot_d}"
            prod_s = f"{n_ans} \\times {n_ans - 3} = {2*tot_d}"
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "kang_ben_handshake_polygon",
            q_e, q_a,
            n_ans, [n_ans - 2, n_ans - 1, n_ans + 1, n_ans + 2],
            "Double the given count first, then factor it into two whole numbers with the right gap (1 or 3)!",
            "ضاعف العدد المعطى أولاً ثم حلّله إلى حاصل ضرب عددين الفرق بينهما (1 أو 3)!",
            "Multiply the count by 2 and recognize two factors differing by 1 (for handshakes) or 3 (for non-neighbors).",
            [f"Set up {m(eq_s)}.", f"Since {m(prod_s)}, there are {m(f'n = {n_ans}')} people."],
            f"Substituting {m(f'n = {n_ans}')} reproduces the exact count!",
            "نضاعف العدد المعطى ونبحث عن عاملين موجبين بالفرق المطلوب.",
            [f"نكتب المعادلة: {m(eq_s)}.", f"بما أن {m(prod_s)}، فإن عدد الأشخاص يساوي {m(n_ans)}."],
            f"بالتعويض بـ {m(n_ans)} نحصل على العدد المعطى تماماً.",
            diagram_en=svg_round_table(min(n_ans, 8), True),
        ))

    # --- 20. kang_ben_necklace_symmetry (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_rot = [
        (4, False),
        (5, False),
        (5, True),
        (6, False),
        (6, True),
    ]
    for n_s, adj_pair in easy_rot:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = 2 * math.factorial(n_s - 2) if adj_pair else math.factorial(n_s - 1)
        if adj_pair:
            q_e = f"In how many ways can {m(n_s)} friends sit around a circular table if twins **Lina and Maya must sit next to each other** (rotations of the whole table count as the same seating)?"
            q_a = f"بكم طريقة يمكن لـ {m(n_s)} صديقات الجلوس حول طاولة مستديرة بشرط أن تجلس التوأمان **لينا ومايا متجاورتين** (تُعدّ الدورانات حول الطاولة ترتيباً واحداً)؟"
            st_e = [f"Glue Lina and Maya into 1 twin-block, giving {m(n_s - 1)} circular units arranged in {m(f'({n_s-1}-1)! = {math.factorial(n_s-2)}')} ways.",
                    f"Multiply by {m(2)} because Lina can sit to Maya's left or right: {m(f'2 \\times {math.factorial(n_s-2)} = {ans}')}."]
            st_a = [f"نعتبر لينا ومايا كتلة واحدة فيصبح لدينا {m(n_s - 1)} عناصر دائرية ترتّب في {m(f'{math.factorial(n_s-2)}')} طرق.",
                    f"نضرب في {m(2)} لتبديل موضعي التوأمين: {m(f'2 \\times {math.factorial(n_s-2)} = {ans}')}."]
        else:
            q_e = f"In how many different ways can {m(n_s)} children sit around a circular picnic table if two seatings are considered the same whenever one is a rotation of the other?"
            q_a = f"بكم طريقة مختلفة يمكن لـ {m(n_s)} أطفال الجلوس حول طاولة نزهة دائرية إذا اعتبرنا كل ترتيبين ينتج أحدهما عن دوران الآخر طريقة واحدة؟"
            st_e = [f"Fix the first child's seat to eliminate rotational repeats.",
                    f"Arrange the remaining {m(n_s - 1)} children in {m(f'({n_s}-1)! = {ans}')} ways."]
            st_a = [f"نثبّت مقعد الطفل الأول لإلغاء تكرار الدوران.",
                    f"نرتّب الأطفال الـ {m(n_s - 1)} الباقين في {m(f'({n_s}-1)! = {ans}')} طريقة."]
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Easy", "kang_ben_necklace_symmetry",
            q_e, q_a,
            ans, [math.factorial(n_s), ans // 2, ans + 6, max(2, ans - 4)],
            "Fix one person's seat first so rotations aren't counted multiple times!",
            "ثبّت مقعد شخص واحد أولاً لمنع تكرار الدورانات المتكافئة!",
            "Circular arrangements of k units take (k − 1)! ways; glue adjacent friends into one unit and multiply by 2!",
            st_e, f"Exact circular seating count = {m(ans)}.",
            "الترتيب الدائري لـ k عناصر يساوي (k − 1)!، وعند التجاور ندمجهما ونضرب في 2.",
            st_a, f"تحقق: عدد الترتيبات الدائرية يساوي {m(ans)}.",
            diagram_en=svg_round_table(n_s, adj_pair),
        ))

    med_beads = [
        (["R", "B"] + ["W"] * 3, "1 red, 1 blue, and 3 white"),
        (["R", "B"] + ["W"] * 5, "1 red, 1 blue, and 5 white"),
        (["R", "B"] + ["W"] * 7, "1 red, 1 blue, and 7 white"),
        (["R", "R"] + ["W"] * 4, "2 identical red and 4 identical white"),
        (["R", "R"] + ["W"] * 5, "2 identical red and 5 identical white"),
    ]
    ar_beads_desc = [
        "خرزة حمراء وخرزة زرقاء و3 خرزات بيضاء",
        "خرزة حمراء وخرزة زرقاء و5 خرزات بيضاء",
        "خرزة حمراء وخرزة زرقاء و7 خرزات بيضاء",
        "خرزتين حمراوين متطابقتين و4 خرزات بيضاء متطابقة",
        "خرزتين حمراوين متطابقتين و5 خرزات بيضاء متطابقة",
    ]
    for beads, d_en, d_ar in [(med_beads[i][0], med_beads[i][1], ar_beads_desc[i]) for i in range(5)]:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = _count_bracelets(beads)
        w_cnt = beads.count("W")
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "kang_ben_necklace_symmetry",
            f"Nadia strings **{d_en}** beads onto a circular bracelet that can be freely rotated and flipped over. How many genuinely different bracelets can she make?",
            f"تنظِم نادية **{d_ar}** في سوار دائري يمكن تدويره وقلبه بحرية. كم سواراً مختلفاً حقاً يمكنها صنعه؟",
            ans, [ans + 1, ans + 2, max(1, ans - 1), len(beads) - 1],
            "Count the possible numbers of white beads on the SHORTER arc between the two colored beads!",
            "احسب القيم الممكنة لعدد الخرزات البيضاء الواقعة على القوس الأقصر بين الخرزتين الملونتين!",
            "With two special beads on a flippable loop, bracelets are uniquely determined by the shorter gap of white beads between them.",
            [f"Total white beads = {m(w_cnt)}, split into two arcs {m('(a, b)')} with {m('0 \\le a \\le b')}.",
             f"Counting integer splits {m(f'0 \\le a \\le {w_cnt // 2}')} gives {m(ans)} distinct bracelets."],
            f"Symmetry-verified across all rotations and flips: {m(ans)} bracelets.",
            "يتحدد شكل السوار القابل للدوران والقلب بعدد الخرز الأبيض على القوس الأقصر بين الخرزتين المميزتين.",
            [f"نقسم الخرزات البيضاء الـ {m(w_cnt)} إلى قوسين {m('a \\le b')}.",
             f"عدد الأزواج الممكنة هو {m(ans)} أساور مختلفة."],
            f"تم التحقق تحت جميع الدورانات والانعكاسات: {m(ans)}.",
            diagram_en=svg_kang_necklace_beads(beads),
        ))

    hard_beads = [
        (["R", "R", "B", "W", "W"], "2 red, 1 blue, and 2 white", "خرزتين حمراوين وخرزة زرقاء وخرزتين بيضاوين"),
        (["R", "R", "B", "W", "W", "W"], "2 red, 1 blue, and 3 white", "خرزتين حمراوين وخرزة زرقاء و3 خرزات بيضاء"),
        (["R", "R", "R", "W", "W", "W"], "3 identical red and 3 identical white", "3 خرزات حمراء متطابقة و3 خرزات بيضاء متطابقة"),
        (["R", "R", "R", "W", "W", "W", "W"], "3 identical red and 4 identical white", "3 خرزات حمراء متطابقة و4 خرزات بيضاء متطابقة"),
        (["R", "B", "Y", "G", "P"], "5 all-different colored (red, blue, yellow, green, purple)", "5 خرزات بألوان مختلفة تماماً"),
    ]
    for beads, d_en, d_ar in hard_beads:
        qid = f"KANG-BEN-{240 + len(qs) + 1:03d}"
        ans = _count_bracelets(beads)
        qs.append(make_kang_q(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "kang_ben_necklace_symmetry",
            f"Jana makes a circular {m(len(beads))}-bead charm bracelet using **{d_en}** beads. Two bracelets are identical if one matches the other by rotating or flipping it in space. How many distinct bracelets exist?",
            f"تصنع جنى سواراً دائرياً من {m(len(beads))} خرزات باستخدام **{d_ar}**. يُعتبر السواران متطابقين إذا نتج أحدهما عن الآخر بالدوران أو القلب في الفراغ. كم سواراً مختلفاً يمكن تكوينه؟",
            ans, [ans * 2, ans + 2, max(1, ans - 1), ans + 4],
            "Fix a reference bead (like Blue, or group gaps between Red beads) and merge mirror-image arrangements!",
            "ثبّت خرزة مرجعية (أو ادرس أطوال الفواصل بين الخرز الأحمر) وادمج الترتيبات المتناظرة مرآتياً!",
            "Group arrangements by arc gaps (or divide (n−1)! by 2 when all beads have distinct colors).",
            [f"Anchor one reference bead at the top of the {m(len(beads))}-bead ring to remove rotations.",
             f"Pair each asymmetric arrangement with its left-right flip to obtain {m(ans)} distinct bracelets."],
            f"Exhaustive symmetry check confirms {m(ans)} non-equivalent bracelets.",
            "نثبّت خرزة في الأعلى لإلغاء الدوران، ثم ندمج كل ترتيب غير متماثل مع معكوسه المرآتي.",
            [f"ندرس التوزيعات الممكنة حول الحلقة ذات الـ {m(len(beads))} مواضع.",
             f"بعد استبعاد التكرار الناتج عن الدوران والقلب نحصل على {m(ans)} أساور مختلفة."],
            f"تحقق شامل بالتماثل الدوراني والانعكاسي: {m(ans)}.",
            diagram_en=svg_kang_necklace_beads(beads),
        ))

    assert len(qs) == 60
    return qs


def _unit_6() -> list[dict]:
    qs: list[dict] = []

    def _dijkstra(edges_list: list[tuple[str, str, int]], start: str, goal: str, banned_edge: tuple[str, str] = None) -> int:
        adj: dict[str, list[tuple[str, int]]] = {}
        for u, v, w in edges_list:
            if banned_edge and ({u, v} == set(banned_edge)):
                continue
            adj.setdefault(u, []).append((v, w))
            adj.setdefault(v, []).append((u, w))
        dist = {start: 0}
        vis = set()
        while len(vis) < len(adj):
            cur = min((k for k in dist if k not in vis), key=lambda k: dist[k], default=None)
            if cur is None or cur == goal:
                break
            vis.add(cur)
            for nb, wt in adj.get(cur, []):
                if dist[cur] + wt < dist.get(nb, 10**9):
                    dist[nb] = dist[cur] + wt
        return dist[goal]

    # --- 21. kang_ben_average_missing_score (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_avg = [
        ([12, 16, 15, 21], 2, "books read", "الكتب المقروءة"),
        ([18, 22, 16, 24], 3, "points scored", "النقاط المسجلة"),
        ([14, 19, 17, 26], 1, "shells collected", "الأصداف المجمعة"),
        ([25, 19, 28, 24], 2, "laps swum", "الأشواط المقطوعة"),
        ([30, 22, 26, 34], 3, "stickers earned", "الملصقات المكتسبة"),
    ]
    days_en = ["Mon", "Tue", "Wed", "Thu"]
    days_ar = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس"]
    for vals, q_idx, lb_en, lb_ar in easy_avg:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        assert sum(vals) % 4 == 0
        avg_v = sum(vals) // 4
        ans = vals[q_idx]
        known_sum = sum(vals) - ans
        bars_e = [(days_en[i], vals[i], "?" if i == q_idx else str(vals[i])) for i in range(4)]
        bars_a = [(days_ar[i], vals[i], "?" if i == q_idx else str(vals[i])) for i in range(4)]
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Easy", "kang_ben_average_missing_score",
            f"The bar chart shows {lb_en} across {m(4)} days, with one smudged bar {m('?')}. If the average across all {m(4)} days is {m(avg_v)}, what value belongs at {m('?')}?",
            f"يوضّح التمثيل بالأعمدة عدد {lb_ar} خلال {m(4)} أيام مع عمود مفقود {m('?')}. إذا كان المتوسط الحسابي للأيام الأربعة هو {m(avg_v)}، فما القيمة المفقودة {m('?')}؟",
            ans, [avg_v, ans - 3, ans + 3, ans + 5],
            f"Multiply the 4-day average ({avg_v}) by 4 to get the total sum, then subtract the 3 known bars!",
            f"اضرب متوسط الأيام الأربعة ({avg_v}) في 4 لإيجاد المجموع الكلي ثم اطرح الأعمدة الثلاثة المعلومة!",
            "Total Sum = 4 × Average.",
            [f"Total across 4 days = {m(f'4 \\times {avg_v} = {4*avg_v}')}.",
             f"Known 3-day sum = {m(known_sum)}, so {m(f'? = {4*avg_v} - {known_sum} = {ans}')}."],
            f"{m(f'({known_sum} + {ans}) \\div 4 = {avg_v}')}.",
            "المجموع الكلي يساوي عدد الأيام مضروباً في المتوسط.",
            [f"المجموع الكلي = {m(f'4 \\times {avg_v} = {4*avg_v}')}.",
             f"القيمة المفقودة = {m(f'{4*avg_v} - {known_sum} = {ans}')}."],
            f"تحقق: {m(f'({known_sum} + {ans}) \\div 4 = {avg_v}')}.",
            diagram_en=svg_bar_chart(bars_e, max(vals) + 6),
            diagram_ar=svg_bar_chart(bars_a, max(vals) + 6),
        ))

    med_avg = [(3, 76, 80), (4, 82, 85), (4, 79, 83), (5, 84, 87), (3, 88, 91)]
    for n_old, a_old, a_new in med_avg:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        ans = (n_old + 1) * a_new - n_old * a_old
        bars_e = [(f"T{i+1}", a_old, str(a_old)) for i in range(n_old)] + [(f"T{n_old+1}", ans, "?")]
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Medium", "kang_ben_average_missing_score",
            f"After {m(n_old)} Kangaroo mock tests, Mariam's average score is {m(a_old)}. What score must she achieve on test #{m(n_old + 1)} to raise her overall average across all {m(n_old + 1)} tests to {m(a_new)}?",
            f"بعد {m(n_old)} اختبارات تجريبية للكانجارو بلغ متوسط درجات مريم {m(a_old)}. ما الدرجة التي يجب أن تحرزها في الاختبار رقم {m(n_old + 1)} ليرتفع متوسطها العام في الاختبارات الـ {m(n_old + 1)} إلى {m(a_new)}؟",
            ans, [a_new + (a_new - a_old), a_new, ans - (a_new - a_old), ans + 4],
            f"Compare the new target total ({n_old+1} × {a_new}) against her current total ({n_old} × {a_old})!",
            f"قارن المجموع الجديد المطلوب ({n_old+1} × {a_new}) بمجموعها الحالي ({n_old} × {a_old})!",
            "New score = (n + 1) × A_new − n × A_old.",
            [f"Current total = {m(f'{n_old} \\times {a_old} = {n_old*a_old}')}; new target total = {m(f'{n_old+1} \\times {a_new} = {(n_old+1)*a_new}')}.",
             f"Needed score = {m(f'{(n_old+1)*a_new} - {n_old*a_old} = {ans}')}."],
            f"{m(f'({n_old*a_old} + {ans}) \\div {n_old+1} = {a_new}')}.",
            "الدرجة المطلوبة = المجموع المستهدف الجديد ناقص المجموع السابق.",
            [f"المجموع السابق = {m(n_old*a_old)}، والمجموع الجديد المطلوب = {m((n_old+1)*a_new)}.",
             f"الدرجة المطلوبة = {m(f'{(n_old+1)*a_new} - {n_old*a_old} = {ans}')}."],
            f"تحقق: {m(f'({n_old*a_old} + {ans}) \\div {n_old+1} = {a_new}')}.",
            diagram_en=svg_bar_chart(bars_e, 100),
        ))

    hard_avg = [
        [12, 17, 19, 15, 22],  # sum=85(avg 17), first3=48(avg 16), last3=56(avg? wait 19+15+22=56 not div 3!)
    ]
    # Build 5 exact 5-tuples [a,b,c,d,e] with (a+b+c)%3==0, (c+d+e)%3==0, (a+b+c+d+e)%5==0!
    hard_quint = [
        [11, 16, 18, 14, 16],  # first3=45(15), last3=48(16), all5=75(15) -> c=18
        [10, 14, 21, 17, 23],  # first3=45(15), last3=61 no -> let's adjust: [10,14,21,15,25]: last3=61 no -> [12,14,22,13,24]: first3=48(16), last3=59 no
        [13, 15, 20, 16, 21],  # first3=48(16), last3=57(19), all5=85(17) -> c=20!
        [14, 19, 24, 15, 18],  # first3=57(19), last3=57(19), all5=90(18) -> c=24!
        [12, 16, 23, 18, 26],  # first3=51(17), last3=67 no -> [15,16,23,19,22]: first3=54(18), last3=64 no -> [15,17,22,19,22]: 54(18), 63(21), all5=95(19)!
        [16, 19, 25, 20, 20],  # first3=60(20), last3=65 no -> [14,21,25,17,23]: 60(20), 65 no -> [17,18,25,19,21]: 60(20), 65 no -> [16,17,27,18,27]: 60(20), 72(24), all5=105(21)!
    ]
    hard_quint = [
        [11, 16, 18, 14, 16],
        [13, 15, 20, 16, 21],
        [14, 19, 24, 15, 18],
        [15, 17, 22, 19, 22],
        [16, 17, 27, 18, 27],
    ]
    for vals in hard_quint:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        s_all = sum(vals)
        s_l = sum(vals[:3])
        s_r = sum(vals[2:])
        assert s_all % 5 == 0 and s_l % 3 == 0 and s_r % 3 == 0
        m_all, m_l, m_r = s_all // 5, s_l // 3, s_r // 3
        ans = vals[2]
        assert 3 * m_l + 3 * m_r - 5 * m_all == ans
        bars_e = [("A", vals[0], "?"), ("B", vals[1], "?"), ("C", vals[2], "C=?"), ("D", vals[3], "?"), ("E", vals[4], "?")]
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Hard", "kang_ben_average_missing_score",
            f"Five scores {m('A, B, C, D, E')} have an overall average of {m(m_all)}. The average of the first three ({m('A, B, C')}) is {m(m_l)}, and the average of the last three ({m('C, D, E')}) is {m(m_r)}. What is the middle score {m('C')}?",
            f"خمس درجات {m('A, B, C, D, E')} متوسطها الكلي {m(m_all)}. إذا كان متوسط أول ثلاث منها ({m('A, B, C')}) هو {m(m_l)}، ومتوسط آخر ثلاث منها ({m('C, D, E')}) هو {m(m_r)}، فما قيمة الدرجة الوسطى {m('C')}؟",
            ans, [m_all, ans - 3, ans + 3, (m_l + m_r) // 2],
            "Add the sum of (A+B+C) and the sum of (C+D+E): notice that C is counted TWICE while every other letter is counted once!",
            "اجمع مجموع (A+B+C) ومجموع (C+D+E): لاحظ أن C حُسبت مرتين بينما حُسبت بقية الحروف مرة واحدة!",
            "Because (A + B + C) + (C + D + E) = (A + B + C + D + E) + C, subtract the 5-score sum from the two 3-score sums!",
            [f"Sum of all 5 = {m(f'5 \\times {m_all} = {s_all}')}; first 3 sum = {m(f'3 \\times {m_l} = {s_l}')}; last 3 sum = {m(f'3 \\times {m_r} = {s_r}')}.",
             f"Middle score {m(f'C = ({s_l} + {s_r}) - {s_all} = {ans}')}."],
            f"{m(f'{s_l} + {s_r} - {ans} = {s_all}')} exact!",
            "بما أن C مشترك بين المجموعتين الثلاثيتين فإن C = مجموع الأولى + مجموع الثانية − المجموع الكلي.",
            [f"مجموع الخمس = {m(s_all)}، ومجموع أول ثلاث = {m(s_l)}، ومجموع آخر ثلاث = {m(s_r)}.",
             f"إذن {m(f'C = {s_l} + {s_r} - {s_all} = {ans}')}."],
            f"تحقق: {m(f'{s_l} + {s_r} - {ans} = {s_all}')}.",
            diagram_en=svg_bar_chart(bars_e, max(vals) + 6),
        ))

    # --- 22. kang_ben_spinner_probability (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_sp = [
        ([(Fraction(1, 2), "2"), (Fraction(1, 4), "3"), (Fraction(1, 8), "4"), (Fraction(1, 8), "5")], {"2", "4"}, "an **even** number", "عدد **زوجي**"),
        ([(Fraction(1, 3), "1"), (Fraction(1, 6), "2"), (Fraction(1, 4), "3"), (Fraction(1, 4), "4")], {"2", "3"}, "a **prime** number", "عدد **أولي**"),
        ([(Fraction(3, 8), "A"), (Fraction(1, 4), "B"), (Fraction(1, 4), "C"), (Fraction(1, 8), "D")], {"A", "D"}, "sector **A or D**", "القطاع **A أو D**"),
        ([(Fraction(1, 2), "5"), (Fraction(1, 6), "6"), (Fraction(1, 6), "7"), (Fraction(1, 6), "8")], {"5", "7"}, "an **odd** number", "عدد **فردي**"),
        ([(Fraction(2, 5), "10"), (Fraction(1, 5), "20"), (Fraction(3, 10), "30"), (Fraction(1, 10), "40")], {"20", "30"}, "**20 or 30**", "**20 أو 30**"),
    ]
    for secs, fav_set, ev_en, ev_ar in easy_sp:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        ans = sum((f for f, lb in secs if lb in fav_set), Fraction(0))
        sec_desc = ", ".join(f"label {m(lb)} covers {m(f'\\frac{{{f.numerator}}}{{{f.denominator}}}')}" for f, lb in secs)
        sec_ar = "، ".join(f"القطاع {m(lb)} يغطي {m(f'\\frac{{{f.numerator}}}{{{f.denominator}}}')}" for f, lb in secs)
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Easy", "kang_ben_spinner_probability",
            f"On the fair spinner shown ({sec_desc}), what is the probability that one spin lands on {ev_en}?",
            f"في القرص الدوّار العادل أدناه ({sec_ar})، ما احتمال وقوف المؤشر على {ev_ar}؟",
            ans, [Fraction(len(fav_set), len(secs)), 1 - ans, Fraction(ans.numerator + 1, ans.denominator + 1), Fraction(1, len(secs))],
            "Add the fractional circle shares of the favorable sectors—do NOT assume equal sectors!",
            "اجمع الكسور الممثلة لمساحات القطاعات المطلوبة ولا تفترض تساوي القطاعات!",
            "Spinner probability equals the sum of the fractional areas of matching sectors.",
            [f"Matching sectors are {', '.join(sorted(fav_set))}.",
             f"Adding their circle fractions gives {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"Complement probability is {m(f'1 - \\frac{{{ans.numerator}}}{{{ans.denominator}}} = \\frac{{{(1-ans).numerator}}}{{{(1-ans).denominator}}}')}.",
            "احتمال القرص الدوّار يساوي مجموع كسور مساحات القطاعات المحققة للحدث.",
            [f"القطاعات المطلوبة هي {', '.join(sorted(fav_set))}.",
             f"بجمع كسور مساحاتها وتبسيط الناتج نحصل على {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"مجموع جميع القطاعات على القرص يساوي {m(1)}.",
            diagram_en=svg_spinner([(float(f), lb) for f, lb in secs]),
        ))

    med_pie = [
        ([120, 90, 60], "Win"),
        ([150, 90, 45], "Win"),
        ([135, 90, 60], "Win"),
        ([120, 100, 60], "Win"),
        ([140, 100, 40], "Win"),
    ]
    for angs, _ in med_pie:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        rem_ang = 360 - sum(angs)
        ans = Fraction(rem_ang, 360)
        slices = [(a / 360.0, f"{a}°") for a in angs] + [(rem_ang / 360.0, "★ ?°")]
        a_list = ", ".join(m(f"{a}^\\circ") for a in angs)
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Medium", "kang_ben_spinner_probability",
            f"A circular prize wheel is divided into four sectors. Three sectors have central angles {a_list}, and the fourth is the star prize sector {m('\\star')}. What is the probability of landing on {m('\\star')} in simplest form?",
            f"قُسّمت عجلة جوائز دائرية إلى أربعة قطاعات؛ زوايا ثلاثة منها في المركز هي {a_list} والقطاع الرابع هو قطاع النجمة {m('\\star')}. ما احتمال الوقوف على قطاع {m('\\star')} في أبسط صورة؟",
            ans, [Fraction(1, 4), Fraction(rem_ang, 180) if rem_ang < 180 else Fraction(1, 3), 1 - ans, Fraction(angs[-1], 360)],
            "Subtract the known angles from 360°, then divide that central angle by 360° and simplify!",
            "اطرح الزوايا المعلومة من 360° ثم اقسم زاوية قطاع النجمة على 360° وبسّط الكسر!",
            "Central angles around a circle sum to 360°, and P(sector) = angle / 360°.",
            [f"Star sector angle = {m(f'360^\\circ - ({angs[0]}^\\circ + {angs[1]}^\\circ + {angs[2]}^\\circ) = {rem_ang}^\\circ')}.",
             f"Probability = {m(f'\\frac{{{rem_ang}}}{{360}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"{m(f'{angs[0]} + {angs[1]} + {angs[2]} + {rem_ang} = 360^\\circ')}.",
            "مجموع الزوايا المركزية 360°، واحتمال القطاع يساوي زاويته مقسومة على 360°.",
            [f"زاوية قطاع النجمة = {m(f'360^\\circ - {sum(angs)}^\\circ = {rem_ang}^\\circ')}.",
             f"الاحتمال في أبسط صورة = {m(f'\\frac{{{rem_ang}}}{{360}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"تحقق: مجموع الزوايا الأربع يساوي {m('360^\\circ')}.",
            diagram_en=svg_pie_chart(slices),
        ))

    hard_sp = [
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 4), 3)], 4, "sum"),
        ([(Fraction(1, 2), 1), (Fraction(1, 3), 2), (Fraction(1, 6), 3)], 3, "sum"),
        ([(Fraction(1, 2), 2), (Fraction(1, 4), 3), (Fraction(1, 4), 5)], 6, "prod"),
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 4), 4)], 4, "prod"),
        ([(Fraction(2, 3), 1), (Fraction(1, 6), 2), (Fraction(1, 6), 3)], 4, "sum"),
    ]
    for secs, target_v, op_mode in hard_sp:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        ans = sum(
            (f1 * f2 for f1, v1 in secs for f2, v2 in secs if ((v1 + v2 == target_v) if op_mode == "sum" else (v1 * v2 == target_v))),
            Fraction(0),
        )
        op_en = "sum" if op_mode == "sum" else "product"
        op_ar = "مجموع" if op_mode == "sum" else "حاصل ضرب"
        s_txt = ", ".join(f"{m(v)} ({m(f'\\frac{{{f.numerator}}}{{{f.denominator}}}')})" for f, v in secs)
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Hard", "kang_ben_spinner_probability",
            f"A Kangaroo game spinner has sectors {s_txt}. Layla spins the pointer **twice** independently. What is the probability that the **{op_en}** of her two numbers equals {m(target_v)}?",
            f"قرص دوّار مقسّم إلى القطاعات: {s_txt}. أدارت ليلى المؤشر **مرتين** مستقلتين. ما احتمال أن يساوي **{op_ar}** العددين الناتجين {m(target_v)}؟",
            ans, [Fraction(2, 9), Fraction(1, 3), Fraction(ans.numerator + 1, ans.denominator), 1 - ans],
            "List every ordered pair (Spin 1, Spin 2) that hits the target, multiply each pair's probabilities, and add!",
            "اكتب جميع الأزواج المرتبة (الدورة 1، الدورة 2) التي تحقق الهدف، واضرب احتمالي كل زوج ثم اجمع النتائج!",
            "Multiply sector probabilities for each valid ordered pair (first spin, second spin) and sum all matching pairs.",
            [f"Find all ordered pairs {m('(v_1, v_2)')} whose {op_en} is {m(target_v)} (remember {m('(a, b)')} and {m('(b, a)')} are distinct when {m('a \\ne b')}!).",
             f"Summing {m('P(v_1) \\times P(v_2)')} over all matching ordered pairs gives {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"All {m(len(secs)**2)} ordered outcomes sum to probability {m(1)}.",
            "نحدد جميع الأزواج المرتبة المحققة للشرط ونضرب احتمالاتها المستقلة ثم نجمعها.",
            [f"نحصر الأزواج المرتبة {m('(v_1, v_2)')} التي يكون {op_ar}ها {m(target_v)} مع التمييز بين {m('(a,b)')} و{m('(b,a)')}.",
             f"بجمع حواصل ضرب الاحتمالات وتبسيط الكسر نحصل على {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"مجموع احتمالات جميع الأزواج التسعة يساوي {m(1)}.",
            diagram_en=svg_spinner([(float(f), str(v)) for f, v in secs]),
        ))

    # --- 23. kang_ben_digital_clock_times (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    easy_clk = ["12:15", "14:29", "20:08", "05:38", "15:40"]
    for t_str in easy_clk:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        hh, mm = map(int, t_str.split(":"))
        start_m = hh * 60 + mm
        wait = 1
        while True:
            cur = (start_m + wait) % 1440
            s4 = f"{cur // 60:02d}{cur % 60:02d}"
            if s4 == s4[::-1]:
                nxt_pal = f"{cur // 60:02d}:{cur % 60:02d}"
                break
            wait += 1
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Easy", "kang_ben_digital_clock_times",
            f"A 24-hour digital clock currently reads `{t_str}`. How many minutes will pass until the clock **next** displays a palindromic time (reading the same forward and backward)?",
            f"تشير ساعة رقمية بنظام 24 ساعة الآن إلى `{t_str}`. كم دقيقة ستمضي حتى تعرض الساعة **أقرب** وقت متناظر تالٍ (يُقرأ من الجهتين بالطريقة نفسها)؟",
            wait, [max(1, wait - 10), wait + 10, wait + 60, max(2, wait - 4)],
            "Test whether the current hour's reversed digits form a valid minute (< 60) still ahead; otherwise jump to the next valid palindromic hour!",
            "تحقق مما إذا كان معكوس الساعة الحالية يكوّن دقيقة صحيحة (< 60) لم تمرّ بعد، وإلا فانتقل إلى أقرب ساعة تالية متناظرة!",
            "Find the earliest valid HH:MM palindrome strictly after the current reading (remember minutes must be 00..59!).",
            [f"Starting after `{t_str}`, the very next valid 24-hour palindrome is `{nxt_pal}`.",
             f"Counting elapsed minutes from `{t_str}` to `{nxt_pal}` gives {m(wait)} minutes."],
            f"`{t_str}` + {m(wait)} min = `{nxt_pal}`, which reads identically from both ends!",
            "نبحث عن أول وقت متناظر صحيح بعد الوقت الحالي مع مراعاة أن الدقائق أقل من 60.",
            [f"أول وقت متناظر صحيح بعد `{t_str}` هو `{nxt_pal}`.",
             f"الفرق الزمني بين `{t_str}` و`{nxt_pal}` يساوي {m(wait)} دقيقة."],
            f"تحقق: إضافة {m(wait)} دقيقة إلى `{t_str}` يعطي `{nxt_pal}`.",
            diagram_en=svg_digital_clock(t_str, "24-hour clock"),
            diagram_ar=svg_digital_clock(t_str, "نظام 24 ساعة"),
        ))

    med_clk = [
        (0, 5, "palindrome", "00:00", "05:59"),
        (20, 23, "palindrome", "20:00", "23:59"),
        (0, 23, "sum23", "00:00", "23:59"),
        (0, 23, "sum22", "00:00", "23:59"),
        (0, 23, "inc", "00:00", "23:59"),
    ]
    for h_lo, h_hi, rule, s_lo, s_hi in med_clk:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        matches = []
        for h in range(h_lo, h_hi + 1):
            for mn in range(60):
                d = f"{h:02d}{mn:02d}"
                if rule == "palindrome" and d == d[::-1]:
                    matches.append(f"{h:02d}:{mn:02d}")
                elif rule == "sum23" and sum(int(c) for c in d) == 23:
                    matches.append(f"{h:02d}:{mn:02d}")
                elif rule == "sum22" and sum(int(c) for c in d) == 22:
                    matches.append(f"{h:02d}:{mn:02d}")
                elif rule == "inc" and int(d[0]) < int(d[1]) < int(d[2]) < int(d[3]):
                    matches.append(f"{h:02d}:{mn:02d}")
        ans = len(matches)
        if rule == "palindrome":
            q_e = f"How many **palindromic** readings `AB:BA` appear on a 24-hour digital clock from `{s_lo}` to `{s_hi}` inclusive?"
            q_a = f"كم قراءة **متناظرة** `AB:BA` تظهر على ساعة رقمية بنظام 24 ساعة في الفترة من `{s_lo}` إلى `{s_hi}` شاملة الطرفين؟"
        elif rule.startswith("sum"):
            sv = int(rule[3:])
            q_e = f"During a full 24-hour day (`00:00` to `23:59`), how many times does the **sum of the four displayed digits** equal {m(sv)}?"
            q_a = f"خلال يوم كامل بنظام 24 ساعة (`00:00` إلى `23:59`)، كم مرة يساوي **مجموع الأرقام الأربعة المعروضة** العدد {m(sv)}؟"
        else:
            q_e = "During a full 24-hour day (`00:00` to `23:59`), how many displayed times `AB:CD` have **strictly increasing** digits from left to right (\\( A < B < C < D \\))?"
            q_a = "خلال يوم كامل بنظام 24 ساعة (`00:00` إلى `23:59`)، كم وقتاً معروضاً `AB:CD` تكون أرقامه الأربعة **متزايدة تماماً** من اليسار لليمين (\\( A < B < C < D \\))؟"
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Medium", "kang_ben_digital_clock_times",
            q_e, q_a,
            ans, [max(1, ans - 2), ans - 1 if ans > 1 else ans + 3, ans + 2, ans + 4],
            "Remember the 24-hour limits: hours AB run 00..23 and tens-of-minutes C can ONLY be 0..5!",
            "تذكّر قيود ساعة الـ 24 ساعة: الساعات من 00 إلى 23 وعشرات الدقائق من 0 إلى 5 فقط!",
            "Casework by valid hours (00..23) while enforcing C ≤ 5 in the minutes!",
            [f"Testing valid 24-hour `HH:MM` combinations finds: {', '.join(f'`{t}`' for t in matches[:6])}{'...' if len(matches) > 6 else ''}.",
             f"In total there are {m(ans)} valid readings."],
            f"Verified across all {m((h_hi - h_lo + 1) * 60)} minutes in the interval: {m(ans)}.",
            "نفرز الحالات الممكنة للساعات مع التحقق الصارم من أن الدقائق بين 00 و59.",
            [f"الأوقات المحققة للشرط تشمل: {', '.join(f'`{t}`' for t in matches[:6])}{'...' if len(matches) > 6 else ''}.",
             f"إجمالي القراءات الصحيحة يساوي {m(ans)}."],
            f"تحقق شامل لجميع دقائق الفترة يعطي {m(ans)}.",
            diagram_en=svg_digital_clock(matches[0], f"{s_lo} – {s_hi}"),
        ))

    hard_clk_specs = [
        ("all_pal", "During an entire 24-hour day (`00:00` to `23:59`), how many **palindromic** times `AB:BA` appear in total?",
         "خلال يوم كامل بنظام 24 ساعة (`00:00` إلى `23:59`)، كم وقتاً **متناظراً** على الصورة `AB:BA` يظهر في المجموع؟", "21:12"),
        ("perm_1234", "How many valid 24-hour digital clock times `HH:MM` use each of the four digits `1, 2, 3, 4` **exactly once**?",
         "كم وقتاً صحيحاً `HH:MM` على ساعة بنظام 24 ساعة يستخدم كلاً من الأرقام الأربعة `1, 2, 3, 4` **مرة واحدة بالضبط**؟", "12:34"),
        ("perm_0126", "How many valid 24-hour digital clock times `HH:MM` use each of the four digits `0, 1, 2, 6` **exactly once**?",
         "كم وقتاً صحيحاً `HH:MM` على ساعة بنظام 24 ساعة يستخدم كلاً من الأرقام الأربعة `0, 1, 2, 6` **مرة واحدة بالضبط**؟", "12:06"),
        ("max_sum", "On a 24-hour digital clock (`00:00` to `23:59`), what is the **largest possible sum** of the four displayed digits `H₁ + H₂ + M₁ + M₂`?",
         "على ساعة رقمية بنظام 24 ساعة (`00:00` إلى `23:59`)، ما **أكبر مجموع ممكن** للأرقام الأربعة المعروضة معاً؟", "19:59"),
        ("has_9", "For how many minutes in a single 24-hour day (`00:00` to `23:59`) does the digit `9` appear **at least once** on the four-digit display?",
         "خلال كم دقيقة في يوم واحد بنظام 24 ساعة (`00:00` إلى `23:59`) يظهر الرقم `9` **مرة واحدة على الأقل** على الشاشة الرباعية؟", "19:09"),
    ]
    for code, q_e, q_a, ex_disp in hard_clk_specs:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        all_d = [f"{h:02d}{mn:02d}" for h in range(24) for mn in range(60)]
        if code == "all_pal":
            ans = sum(1 for d in all_d if d == d[::-1])
            trap_d = [24, 14, 15, 20]
        elif code == "perm_1234":
            ans = sum(1 for d in all_d if sorted(d) == ["1", "2", "3", "4"])
            trap_d = [24, 12, 16, 8]
        elif code == "perm_0126":
            ans = sum(1 for d in all_d if sorted(d) == ["0", "1", "2", "6"])
            trap_d = [24, 12, 8, 14]
        elif code == "max_sum":
            ans = max(sum(int(c) for c in d) for d in all_d)
            trap_d = [23, 25, 20, 19]
        else:
            ans = sum(1 for d in all_d if "9" in d)
            trap_d = [240, 300, 320, 260]
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Hard", "kang_ben_digital_clock_times",
            q_e, q_a,
            ans, trap_d,
            "Watch out for the 19:59 vs 23:59 trap and the M₁ ≤ 5 minute-tens restriction!",
            "انتبه لفخ المقارنة بين 19:59 و23:59 ولشرط عدم تجاوز عشرات الدقائق للرقم 5!",
            "Analyze hours and minutes separately under the strict 24-hour rules (00 ≤ HH ≤ 23 and 00 ≤ MM ≤ 59).",
            [f"Apply {m('00 \\le HH \\le 23')} and {m('00 \\le MM \\le 59')} carefully (for example `{ex_disp}`).",
             f"Counting across all {m(1440)} minutes of the day yields {m(ans)}."],
            f"Verified over all {m('24 \\times 60 = 1440')} valid 24-hour clock readings: {m(ans)}.",
            "نحلل خانات الساعات والدقائق معاً تحت شروط نظام 24 ساعة الصارمة.",
            [f"نراعي أن الساعات لا تتجاوز {m(23)} والدقائق لا تتجاوز {m(59)} (مثل `{ex_disp}`).",
             f"بحساب الحالات الصحيحة نحصل على النتيجة الدقيقة {m(ans)}."],
            f"تم التحقق عبر جميع دقائق اليوم الـ {m(1440)}: الناتج {m(ans)}.",
            diagram_en=svg_digital_clock(ex_disp, "24-hour puzzle"),
            diagram_ar=svg_digital_clock(ex_disp, "لغز 24 ساعة"),
        ))

    # --- 24. kang_ben_shortest_map_route (15 Qs: 5 Easy, 5 Medium, 5 Hard) ---
    nodes_en = {"S": (170, 200, "Camp"), "A": (75, 135, "Woods"), "M": (170, 115, "Mill"), "B": (265, 135, "Lake"), "T": (170, 30, "Peak")}
    nodes_ar = {"S": (170, 200, "المخيم"), "A": (75, 135, "الغابة"), "M": (170, 115, "الطاحونة"), "B": (265, 135, "البحيرة"), "T": (170, 30, "القمة")}
    easy_maps = [
        [("S", "A", 5), ("S", "M", 11), ("S", "B", 7), ("A", "M", 4), ("B", "M", 3), ("M", "T", 6), ("A", "T", 12), ("B", "T", 11)],
        [("S", "A", 8), ("S", "M", 13), ("S", "B", 6), ("A", "M", 3), ("B", "M", 4), ("M", "T", 7), ("A", "T", 11), ("B", "T", 14)],
        [("S", "A", 6), ("S", "M", 14), ("S", "B", 9), ("A", "M", 5), ("B", "M", 3), ("M", "T", 8), ("A", "T", 15), ("B", "T", 12)],
        [("S", "A", 9), ("S", "M", 15), ("S", "B", 7), ("A", "M", 4), ("B", "M", 5), ("M", "T", 6), ("A", "T", 12), ("B", "T", 13)],
        [("S", "A", 7), ("S", "M", 13), ("S", "B", 8), ("A", "M", 3), ("B", "M", 4), ("M", "T", 9), ("A", "T", 14), ("B", "T", 13)],
    ]
    for idx_em, edg in enumerate(easy_maps):
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        ans = _dijkstra(edg, "S", "T")
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Easy", "kang_ben_shortest_map_route",
            f"Trail map #{idx_em+1} shows hiking times (in minutes) along each trail. What is the **shortest** hiking time from **Camp** to **Peak**?",
            f"تبيّن خريطة المسارات #{idx_em+1} أزمنة المشي (بالدقائق) على كل طريق. ما **أقصر** زمن للوصول من **المخيم** إلى **القمة**؟",
            ans, [ans + 1, ans + 2, ans + 3, max(8, ans - 2)],
            "Check 3-trail paths through Mill as well as 2-trail outer paths!",
            "افحص المسارات المارة بالطاحونة ذات الثلاث وصلات إلى جانب المسارات الخارجية ذات الوصلتين!",
            "Compute earliest arrival time at Woods, Lake, and Mill before stepping to Peak.",
            [f"Find fastest times from Camp to Woods, Lake, and Mill (checking shortcuts via Woods/Lake to Mill).",
             f"Comparing all routes to Peak gives a minimum time of {m(ans)} minutes."],
            f"No other trail combination from Camp to Peak beats {m(ans)} minutes.",
            "نحسب أقصر زمن وصول لكل محطة وسطى ثم نقارن المسارات المؤدية إلى القمة.",
            [f"نقارن الوصول إلى الطاحونة مباشرة أو عبر الغابة/البحيرة.",
             f"أقصر زمن كلي للوصول إلى القمة يساوي {m(ans)} دقيقة."],
            f"تحقق: جميع المسارات الأخرى زمنها أكبر من أو يساوي {m(ans)} دقيقة.",
            diagram_en=svg_travel_map(nodes_en, edg),
            diagram_ar=svg_travel_map(nodes_ar, edg),
        ))

    for idx_mm, edg in enumerate(easy_maps):
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        # Close trail M-T for bridge repairs!
        ans = _dijkstra(edg, "S", "T", banned_edge=("M", "T"))
        open_ans = _dijkstra(edg, "S", "T")
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Medium", "kang_ben_shortest_map_route",
            f"On trail map #{idx_mm+1} below, the direct trail between **Mill** and **Peak** is closed due to a fallen tree (all other trails remain open in both directions!). What is now the **shortest** time in minutes from **Camp** to **Peak**?",
            f"على خريطة المسارات #{idx_mm+1} أدناه أُغلق الطريق المباشر بين **الطاحونة** و**القمة** للصيانة (وبقيت جميع الطرق الأخرى مفتوحة في الاتجاهين!). ما **أقصر** زمن الآن بالدقائق للوصول من **المخيم** إلى **القمة**؟",
            ans, [open_ans, ans + 2, ans + 4, ans - 1 if ans - 1 != open_ans else ans + 3],
            "You can STILL pass through Mill to cross between Woods and Lake—you just cannot use the Mill–Peak segment!",
            "لا يزال بإمكانك المرور عبر الطاحونة للانتقال بين الغابة والبحيرة، والممنوع فقط هو وصلة (الطاحونة – القمة)!",
            "Remove edge (Mill, Peak) and compare routes reaching Peak via Woods or via Lake (including cross-overs through Mill!).",
            [f"With Mill–Peak closed, Peak must be entered from **Woods** or **Lake**.",
             f"Checking direct and Mill-crossover paths to Woods and Lake gives minimum total time {m(ans)} minutes."],
            f"Fastest open path takes {m(ans)} minutes without touching the closed Mill–Peak trail.",
            "نستبعد وصلة (الطاحونة–القمة) فقط ونحسب أسرع وصول للقمة عبر الغابة أو البحيرة.",
            [f"بإغلاق وصلة الطاحونة–القمة يصبح الدخول إلى القمة إما من الغابة أو من البحيرة.",
             f"بمقارنة الأزمنة الممكنة نجد أن أقصر زمن هو {m(ans)} دقيقة."],
            f"تحقق: المسار المختار يتجنب الوصلة المغلقة تماماً وزمنه {m(ans)} دقيقة.",
            diagram_en=svg_travel_map(nodes_en, edg),
            diagram_ar=svg_travel_map(nodes_ar, edg),
        ))

    hard_grids = [
        (3, 3, (1, 1)),
        (4, 3, (2, 1)),
        (4, 3, (2, 2)),
        (4, 4, (2, 2)),
        (5, 3, (3, 2)),
    ]
    for cols, rows, blk in hard_grids:
        qid = f"KANG-BEN-{300 + len(qs) + 1:03d}"
        dp = [[0] * (rows + 1) for _ in range(cols + 1)]
        dp[0][0] = 1
        for c in range(cols + 1):
            for r in range(rows + 1):
                if (c, r) == blk or (c == 0 and r == 0):
                    if (c, r) == blk:
                        dp[c][r] = 0
                    continue
                dp[c][r] = (dp[c - 1][r] if c > 0 else 0) + (dp[c][r - 1] if r > 0 else 0)
        ans = dp[cols][rows]
        tot_unblocked = math.comb(cols + rows, cols)
        qs.append(make_kang_q(
            qid, LEVEL, "Data & Probability", "Hard", "kang_ben_shortest_map_route",
            f"On the {m(f'{cols} \\times {rows}')} street grid below, Dana walks from corner {m('A')} to corner {m('B')} moving **only East (right) and North (up)**. The intersection marked {m('\\times')} ({m(blk[0])} blocks East and {m(blk[1])} blocks North of {m('A')}) is closed for construction. How many **different shortest paths** can Dana take?",
            f"على شبكة الشوارع ذات الأبعاد {m(f'{cols} \\times {rows}')} أدناه تسير دانة من الركن {m('A')} إلى الركن {m('B')} بالتحرك **شرقاً (يميناً) وشمالاً (أعلى) فقط**. التقاطع المشار إليه بعلامة {m('\\times')} (على بُعد {m(blk[0])} مربعات شرقاً و{m(blk[1])} مربعات شمالاً من {m('A')}) مغلق للإصلاحات. كم **مساراً أقصر مختلفاً** يمكن لدانة أن تسلكه؟",
            ans, [tot_unblocked, ans + 3, max(1, ans - 2), tot_unblocked - math.comb(blk[0] + blk[1], blk[0])],
            "Label each corner with the sum of paths coming from the Left and Below (setting the blocked × corner to 0)!",
            "اكتب عند كل تقاطع مجموع المسارات القادمة من اليسار ومن الأسفل (مع وضع صفر عند التقاطع المغلق ×)!",
            "Use Pascal corner-addition (or Total Paths minus paths through ×)!",
            [f"Without the roadblock there are {m(f'\\binom{{{cols+rows}}}{{{cols}}} = {tot_unblocked}')} paths.",
             f"Paths through {m('\\times')} at {m(f'({blk[0]},{blk[1]})')} equal {m(f'\\binom{{{blk[0]+blk[1]}}}{{{blk[0]}}} \\times \\binom{{{(cols-blk[0])+(rows-blk[1])}}}{{{cols-blk[0]}}} = {tot_unblocked - ans}')}, leaving {m(f'{tot_unblocked} - {tot_unblocked - ans} = {ans}')} paths."],
            f"Grid DP corner-by-corner addition also lands on {m(ans)} at {m('B')}!",
            "نستخدم جمع المسارات عند الرؤوس (مع تصفير التقاطع المغلق) أو نطرح المسارات المارة بـ × من العدد الكلي.",
            [f"العدد الكلي للمسارات دون إغلاق = {m(tot_unblocked)} مساراً.",
             f"المسارات التي تمرّ بالتقاطع المغلق عددها {m(tot_unblocked - ans)}، فيتبقى {m(f'{tot_unblocked} - {tot_unblocked - ans} = {ans}')} مساراً."],
            f"تحقق بالجمع الشبكي خطوة بخطوة عند الزوايا يعطي {m(ans)}.",
            diagram_en=svg_street_grid(cols, rows, blk),
        ))

    assert len(qs) == 60
    return qs


def build_benjamin_bank() -> list[dict]:
    """Build and return all 360 Kangaroo Benjamin (Grades 5–6) competition questions."""
    bank = _unit_1() + _unit_2() + _unit_3() + _unit_4() + _unit_5() + _unit_6()
    assert len(bank) == 360
    return bank
