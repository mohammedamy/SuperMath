"""ETEC Nafes National Assessment — Grade 6 (الصف السادس الابتدائي) Question Bank: 360 Programmatically Verified Questions."""
import math
from fractions import Fraction

from nafes_common import (
    dm,
    explain_ar,
    explain_en,
    m,
    make_4_bilingual_options,
    make_4_math_options,
    make_nafes_question,
    svg_balance_scales,
    svg_bar_chart,
    svg_factor_tree,
    svg_fenceposts,
    svg_fraction_grid,
    svg_function_machine,
    svg_motion_timeline,
    svg_nafes_analog_clock,
    svg_nafes_box_plot,
    svg_nafes_coordinate_line,
    svg_nafes_fraction_bars,
    svg_nafes_function_table,
    svg_nafes_pie_chart,
    svg_nafes_sar_money,
    svg_nafes_spinner,
    svg_number_strip,
    svg_shaded_triangle_in_rect,
    svg_two_jars,
    svg_venn_2,
    svg_water_tank_3d,
)
from nafes_lessons_g6 import (
    svg_g6_angle_pair,
    svg_g6_circle,
    svg_g6_composite_l,
    svg_g6_parallelogram,
    svg_g6_quad_angles,
    svg_g6_triangle,
)

LEVEL = "Grade 6"


def _mx(fr: Fraction) -> str:
    """Format a positive Fraction as a whole number, proper fraction, or Grade 6 mixed number in LaTeX."""
    assert fr >= 0
    if fr.denominator == 1:
        return str(fr.numerator)
    if fr.numerator < fr.denominator:
        return f"\\frac{{{fr.numerator}}}{{{fr.denominator}}}"
    w, r = divmod(fr.numerator, fr.denominator)
    return f"{w}\\frac{{{r}}}{{{fr.denominator}}}"


class G6BankBuilder:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add_math(
        self,
        topic: str,
        difficulty: str,
        blueprint: str,
        q_en: str,
        q_ar: str,
        correct_val,
        distractors: list,
        hint_en: str,
        hint_ar: str,
        idea_en: str,
        steps_en: list[str],
        check_en: str,
        idea_ar: str,
        steps_ar: list[str],
        check_ar: str,
        suffix: str = "",
        diagram_en: str = None,
        diagram_ar: str = None,
    ) -> None:
        qid = f"NAFS-G6-{len(self.items) + 1:03d}"
        opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, qid, suffix=suffix)
        assert all("_" not in o for o in opts_en), f"Fallback distractor leaked in {qid}: {opts_en}"
        self.items.append(
            make_nafes_question(
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
                diagram_ar=diagram_ar,
            )
        )

    def add_bilingual(
        self,
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
        diagram_en: str = None,
        diagram_ar: str = None,
    ) -> None:
        qid = f"NAFS-G6-{len(self.items) + 1:03d}"
        opts_en, opts_ar, cidx, cans = make_4_bilingual_options(pairs, correct_pair_idx, qid)
        self.items.append(
            make_nafes_question(
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
                diagram_ar=diagram_ar,
            )
        )


def _add_num_01(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-01"
    # 5 Easy: Prime identification & prime-power evaluation
    easy_cases = [
        ("Riyadh Science Fair", "معرض العلوم بالرياض", [21, 27, 29, 33], 29, "29 has only 1 and 29 as factors"),
        ("Jeddah Math Club", "نادي الرياضيات بجدة", [15, 25, 31, 35], 31, "31 is not divisible by 2, 3, or 5"),
        ("Dammam Library badge game", "لعبة أوسمة مكتبة الدمام", [37, 39, 45, 49], 37, "37 has exactly two factors: 1 and 37"),
        ("Abha STEM camp", "مخيم أبها العلمي", [41, 42, 51, 57], 41, "51 = 3×17 and 57 = 3×19, while 41 is prime"),
        ("Madinah quiz bowl", "مسابقة المدينة الثقافية", [43, 48, 55, 63], 43, "43 has only two factors: 1 and 43"),
    ]
    for ctx_en, ctx_ar, nums, prime_ans, note_en in easy_cases:
        wrongs = [x for x in nums if x != prime_ans]
        B.add_math(
            tp, "Easy", bp,
            f"During the {ctx_en}, four number cards {m(', '.join(str(x) for x in nums))} are placed on a table. Which card shows a **prime number**?",
            f"خلال {ctx_ar}، وُضعت البطاقات الأربع {m('، '.join(str(x) for x in nums))} على الطاولة. أي بطاقة منها تحمل **عدداً أولياً**؟",
            prime_ans, wrongs,
            "Test each odd number for divisibility by 3, 5, and 7; a prime number has only two factors.",
            "اختبر قابلية قسمة كل عدد على 3 و5 و7؛ العدد الأولي له قاسمان فقط هما 1 ونفسه.",
            "Eliminate composite cards that have factors other than 1 and themselves.",
            [
                f"Check the cards {m(', '.join(str(x) for x in wrongs))}: each can be factored into smaller whole numbers greater than {m(1)}.",
                f"Verify {m(prime_ans)}: {note_en}, so {m(prime_ans)} is prime.",
            ],
            f"{m(prime_ans)} is divisible only by {m(1)} and {m(prime_ans)}.",
            "نستبعد الأعداد غير الأولية التي تقبل القسمة على عوامل أصغر من نفسها.",
            [
                f"الأعداد {m('، '.join(str(x) for x in wrongs))} تقبل القسمة على {m(3)} أو {m(5)} أو {m(7)} فهي غير أولية.",
                f"أما العدد {m(prime_ans)} فلا يقبل القسمة إلا على {m(1)} ونفسه، فهو عدد أولي.",
            ],
            f"قواسم العدد {m(prime_ans)} هما {m(1)} و{m(prime_ans)} فقط.",
            diagram_en=svg_number_strip([str(x) for x in nums]),
        )

    # 5 Medium: Prime factorization with exponents
    med_trees = [
        ("Taif", "الطائف", 48, "3", "16", "4", "4", "2^4 \\times 3", ["2^3 \\times 3^2", "2^4 \\times 6", "16 \\times 3"]),
        ("Qassim", "القصيم", 60, "5", "12", "3", "4", "2^2 \\times 3 \\times 5", ["2^3 \\times 3 \\times 5", "4 \\times 3 \\times 5", "2 \\times 3^2 \\times 5"]),
        ("Yanbu", "ينبع", 84, "7", "12", "3", "4", "2^2 \\times 3 \\times 7", ["2 \\times 3^2 \\times 7", "4 \\times 21", "2^3 \\times 3 \\times 7"]),
        ("Hail", "حائل", 90, "10", "9", "3", "3", "2 \\times 3^2 \\times 5", ["2^2 \\times 3 \\times 5", "2 \\times 9 \\times 5", "3^2 \\times 10"]),
        ("Tabuk", "تبوك", 108, "4", "27", "3", "9", "2^2 \\times 3^3", ["2^3 \\times 3^2", "4 \\times 3^3", "2^2 \\times 3^2"]),
    ]
    for city_en, city_ar, n_val, lf, rt, rl, rr, ans_tex, dists in med_trees:
        B.add_math(
            tp, "Medium", bp,
            f"A Grade 6 student in {city_en} draws a factor tree for {m(n_val)}. Which expression is the complete **prime factorization** of {m(n_val)} using exponents?",
            f"رسم طالب في الصف السادس في {city_ar} شجرة العوامل للعدد {m(n_val)}. أي عبارة مما يلي تمثّل **التحليل التام إلى العوامل الأولية** للعدد {m(n_val)} باستعمال الأسس؟",
            ans_tex, dists,
            "Keep factoring every composite number until all bases are prime numbers (2, 3, 5, 7).",
            "استمر في تحليل كل عدد غير أولي حتى تصبح جميع الأساسات أعداداً أولية (2، 3، 5، 7).",
            f"Break {n_val} down into prime factors only and write repeated primes as powers.",
            [
                f"Start with {m(f'{n_val} = {lf} \\times {rt}')}.",
                f"Factor every composite branch completely into primes and group identical primes: {m(f'{n_val} = {ans_tex}')}.",
            ],
            f"Evaluating {m(ans_tex)} gives {m(n_val)}, and every base is prime.",
            f"نفكّك العدد {m(n_val)} إلى عوامل أولية فقط ثم نكتب العوامل المتكررة على صورة قوى.",
            [
                f"نبدأ بالتفكيك: {m(f'{n_val} = {lf} \\times {rt}')}.",
                f"نحلّل جميع الفروع غير الأولية ونجمع العوامل المتماثلة بالأسس فنحصل على {m(ans_tex)}.",
            ],
            f"حاصل ضرب {m(ans_tex)} يساوي {m(n_val)} وجميع الأساسات أولية.",
            diagram_en=svg_factor_tree(str(n_val), lf, rt, rl, rr),
        )

    # 5 Hard: Missing exponent or unknown root in prime-power equations
    hard_exp = [
        ("Diriyah Heritage Museum", "متحف الدرعية التراثي", 144, 2, 4, 3, 2, "2^k \\times 3^2 = 144", "9", "16"),
        ("Jubail Robotics Lab", "مختبر الروبوت بالجبيل", 200, 2, 3, 5, 2, "2^k \\times 5^2 = 200", "25", "8"),
        ("Al-Ula Astronomy Club", "نادي الفلك بالعلا", 108, 3, 3, 2, 2, "2^2 \\times 3^k = 108", "4", "27"),
        ("Hofuf Oasis Center", "مركز واحة الهفوف", 250, 5, 3, 2, 1, "2 \\times 5^k = 250", "2", "125"),
        ("Jazan Marine Center", "مركز جازان البحري", 360, 2, 3, 45, 1, "2^k \\times 3^2 \\times 5 = 360", "45", "8"),
    ]
    for place_en, place_ar, total_n, base_p, k_ans, other_b, other_e, eq_tex, known_str, rem_str in hard_exp:
        assert (base_p ** k_ans) * int(known_str) == total_n
        B.add_math(
            tp, "Hard", bp,
            f"At the {place_en}, a code lock uses the prime factorization {m(eq_tex)}. What is the value of the missing exponent {m('k')}?",
            f"في {place_ar}، يستعمل قفل رقمي معادلة التحليل الأولي {m(eq_tex)}. ما قيمة الأس المفقود {m('k')}؟",
            k_ans, [k_ans - 1, k_ans + 1, k_ans + 2],
            f"Divide {total_n} by the known factor ({known_str}) first, then express the quotient as a power of {base_p}.",
            f"اقسم {total_n} على العامل المعلوم ({known_str}) أولاً، ثم اكتب الناتج كقوة للأساس {base_p}.",
            f"Isolate {m(f'{base_p}^k')} by dividing {m(total_n)} by {m(known_str)}.",
            [
                f"Evaluate the known prime factors: {m(known_str)}.",
                f"Divide: {m(f'{base_p}^k = {total_n} \\div {known_str} = {rem_str}')}.",
                f"Since {m(f'{base_p}^{k_ans} = {rem_str}')}, we find {m(f'k = {k_ans}')}.",
            ],
            f"{m(f'{base_p}^{k_ans} \\times {known_str} = {rem_str} \\times {known_str} = {total_n}')}.",
            f"نعزل القوة {m(f'{base_p}^k')} بقسمة {m(total_n)} على حاصل ضرب العوامل المعلومة ({m(known_str)}).",
            [
                f"نقسم {m(f'{total_n} \\div {known_str} = {rem_str}')}.",
                f"بما أن {m(f'{base_p}^{k_ans} = {rem_str}')} فإن قيمة الأس هي {m(f'k = {k_ans}')}.",
            ],
            f"تحقق: {m(f'{rem_str} \\times {known_str} = {total_n}')}.",
            diagram_en=svg_factor_tree(str(total_n), known_str, f"{base_p}^k", str(base_p), "?"),
        )


def _add_num_02(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-02"
    # 5 Easy: Direct GCD & LCM calculations
    easy_gl = [
        ("gcd", 24, 36, "science folders", "ملفات علمية"),
        ("gcd", 30, 45, "art brushes", "فرش رسم"),
        ("lcm", 8, 12, "training laps", "لفات تدريبية"),
        ("lcm", 9, 15, "bell chimes", "رنات جرس"),
        ("gcd", 42, 56, "seed packets", "أكياس بذور"),
    ]
    for mode, a, b, item_en, item_ar in easy_gl:
        ans = math.gcd(a, b) if mode == "gcd" else math.lcm(a, b)
        other = math.lcm(a, b) if mode == "gcd" else math.gcd(a, b)
        lbl_en = "Greatest Common Divisor (GCD)" if mode == "gcd" else "Least Common Multiple (LCM)"
        lbl_ar = "القاسم المشترك الأكبر (ق.م.أ)" if mode == "gcd" else "المضاعف المشترك الأصغر (م.م.أ)"
        B.add_math(
            tp, "Easy", bp,
            f"While organizing {item_en}, Omar compares the numbers {m(a)} and {m(b)}. What is the **{lbl_en}** of {m(a)} and {m(b)}?",
            f"أثناء تنظيم {item_ar}، قارن عمر بين العددين {m(a)} و{m(b)}. ما **{lbl_ar}** للعددين {m(a)} و{m(b)}؟",
            ans, [other, a + b, abs(b - a) if abs(b - a) != ans else ans + 6],
            "Compare prime factorizations: GCD uses shared primes with smallest powers; LCM uses all primes with largest powers.",
            "قارن العوامل الأولية: في (ق.م.أ) نأخذ المشترك بأصغر أس، وفي (م.م.أ) نأخذ جميع العوامل بأكبر أس.",
            f"Find the {lbl_en} of {a} and {b} from their common factors/multiples.",
            [
                f"Factor both numbers: {m(a)} and {m(b)} share greatest common factor {m(math.gcd(a, b))}.",
                f"Therefore, the requested {lbl_en} is {m(ans)}.",
            ],
            f"{m(ans)} divides both numbers evenly." if mode == "gcd" else f"Both {m(a)} and {m(b)} divide {m(ans)} evenly.",
            f"نوجد {lbl_ar} للعددين {m(a)} و{m(b)} بتحليلهما إلى عواملهما الأولية.",
            [
                f"القاسم المشترك الأكبر للعددين هو {m(math.gcd(a, b))} والمضاعف المشترك الأصغر هو {m(math.lcm(a, b))}.",
                f"إذن القيمة المطلوبة هي {m(ans)}.",
            ],
            f"العدد {m(ans)} يحقق تعريف {lbl_ar} للعددين {m(a)} و{m(b)}.",
            diagram_en=svg_venn_2(f"A = {a}", f"B = {b}", "?", "GCD = ?", "?"),
        )

    # 5 Medium: Equal gift-bag / cutting-ribbon GCD word problems
    med_gcd = [
        ("Makkah charity drive", "مبادرة خيرية في مكة", 36, "water flasks", "قارورة ماء", 48, "date boxes", "علبة تمر", "gift bags", "حقيبة"),
        ("Riyadh robotics workshop", "ورشة الروبوت بالرياض", 40, "motors", "محركاً", 64, "wheels", "عجلة", "identical robot kits", "حقيبة روبوت متماثلة"),
        ("Jeddah art studio", "مرسم الفنون بجدة", 45, "blue markers", "قلم أزرق", 75, "green markers", "قلم أخضر", "equal table sets", "مجموعة متساوية"),
        ("Baha honey festival", "مهرجان العسل بالباحة", 28, "Sidr jars", "عبوة سدر", 42, "Acacia jars", "عبوة طلح", "identical gift crates", "صندوق هدايا متماثل"),
        ("Sakaka school fair", "معرض مدرسة بسكاكا", 54, "notebooks", "دفتراً", 72, "pencils", "قلم رصاص", "equal student packs", "حقيبة طلابية متساوية"),
    ]
    for ctx_en, ctx_ar, a, i1_en, i1_ar, b, i2_en, i2_ar, grp_en, grp_ar in med_gcd:
        g = math.gcd(a, b)
        B.add_math(
            tp, "Medium", bp,
            f"For a {ctx_en}, volunteers pack {m(a)} {i1_en} and {m(b)} {i2_en} into {grp_en} with **no items left over**. What is the **greatest** number of {grp_en} they can make?",
            f"في {ctx_ar}، يوزّع المتطوعون {m(a)} {i1_ar} و{m(b)} {i2_ar} في أكبر عدد ممكن من ({grp_ar}) متماثلة **دون باقٍ**. ما **أكبر** عدد من المجموعات يمكن تكوينه؟",
            g, [g // 2 if g % 2 == 0 else g - 3, a // g + b // g, math.lcm(a, b)],
            f"Equal groups with zero remainder means you need gcd({a}, {b}).",
            f"التوزيع المتساوي دون باقٍ لأكبر عدد من المجموعات يعني إيجاد القاسم المشترك الأكبر للعددين {a} و{b}.",
            f"Compute {m(f'\\gcd({a}, {b})')} to find the maximum number of identical groups.",
            [
                f"Find all common divisors of {m(a)} and {m(b)}.",
                f"Since {m(f'{a} = {g} \\times {a // g}')} and {m(f'{b} = {g} \\times {b // g}')} with {m(f'\\gcd({a // g}, {b // g}) = 1')}, {m(f'\\gcd({a}, {b}) = {g}')}.",
            ],
            f"Each of the {m(g)} groups gets {m(a // g)} and {m(b // g)} items with zero remainder.",
            f"نحسب القاسم المشترك الأكبر {m(f'\\gcd({a}, {b})')}.",
            [
                f"نكتب {m(f'{a} = {g} \\times {a // g}')} و{m(f'{b} = {g} \\times {b // g}')}.",
                f"إذن أكبر عدد من المجموعات المتماثلة هو {m(g)}.",
            ],
            f"تحتوي كل مجموعة من الـ {m(g)} على {m(a // g)} و{m(b // g)} دون أي باقٍ.",
            diagram_en=svg_venn_2(f"{a}", f"{b}", "?", "GCD = ?", "?"),
        )

    # 5 Hard: Multi-cycle LCM & count-of-meetings reasoning problems
    hard_lcm = [
        ("Dammam corniche fountain", "نافورة كورنيش الدمام", 10, 15, 180, "jets splash together"),
        ("King Abdulaziz Planetarium", "القبة الفلكية", 12, 16, 192, "laser shows start together"),
        ("Yanbu port beacons", "منارتا ميناء ينبع", 8, 20, 200, "lights flash together"),
        ("Qassim smart farm valves", "صمامات مزرعة ذكية بالقصيم", 15, 20, 240, "valves open together"),
        ("Abha cable-car stations", "محطتا تلفريك أبها", 9, 12, 180, "cabins depart together"),
    ]
    for ctx_en, ctx_ar, t1, t2, span, act_en in hard_lcm:
        L = math.lcm(t1, t2)
        cnt = span // L  # number of subsequent simultaneous occurrences in `span` minutes after t=0
        B.add_math(
            tp, "Hard", bp,
            f"At the {ctx_en}, Signal A repeats every {m(t1)} minutes and Signal B repeats every {m(t2)} minutes. They {act_en} at {m('t = 0')}. How many **more times** will they occur together during the next {m(span)} minutes (including minute {m(span)})?",
            f"في {ctx_ar}، تتكرر الإشارة (أ) كل {m(t1)} دقيقة وتتكرر الإشارة (ب) كل {m(t2)} دقيقة. إذا حدثتا معاً عند البداية ({m('t = 0')})، فكم **مرة إضافية** تحدثان معاً خلال الـ {m(span)} دقيقة التالية (بما في ذلك الدقيقة {m(span)})؟",
            cnt, [cnt + 1, L, span // (t1 + t2)],
            f"First find LCM({t1}, {t2}) to get the cycle gap, then divide {span} by that LCM.",
            f"أوجد أولاً المضاعف المشترك الأصغر للعددين {t1} و{t2}، ثم اقسم {span} على ذلك المضاعف.",
            f"Signals coincide every {m(f'\\operatorname{{lcm}}({t1}, {t2}) = {L}')} minutes; divide {m(span)} by {m(L)}.",
            [
                f"Find the first repeat time: {m(f'\\operatorname{{lcm}}({t1}, {t2}) = {L}')} minutes.",
                f"Count multiples of {m(L)} in {m(f'1 \\dots {span}')}: {m(f'{span} \\div {L} = {cnt}')} times.",
            ],
            f"They coincide at minutes {m(', '.join(str(L * k) for k in range(1, cnt + 1)))}, which is {m(cnt)} additional times.",
            f"تلتقي الإشارتان كل {m(f'\\operatorname{{lcm}}({t1}, {t2}) = {L}')} دقيقة، ثم نقسم {m(span)} على {m(L)}.",
            [
                f"المضاعف المشترك الأصغر للعددين {m(t1)} و{m(t2)} هو {m(L)} دقيقة.",
                f"عدد مرات الالتقاء الإضافية خلال {m(span)} دقيقة هو {m(f'{span} \\div {L} = {cnt}')} مرات.",
            ],
            f"مرات الالتقاء الإضافية تقع عند الدقائق المضاعفة للعدد {m(L)} وعددها {m(cnt)}.",
            diagram_en=svg_number_strip(["0", f"{t1}m & {t2}m", "LCM = ?", f"… {span}m"]),
        )


def _add_num_03(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-03"
    # 5 Easy: Adding & subtracting unlike proper fractions in simplest form
    easy_fr = [
        ("add", (1, 3), (1, 4), "oat flour", "دقيق الشوفان", "cups", "كوب"),
        ("add", (2, 5), (3, 10), "olive oil", "زيت الزيتون", "liters", "لتر"),
        ("sub", (5, 6), (1, 4), "copper wire", "سلك نحاسي", "meters", "متر"),
        ("add", (1, 6), (3, 8), "pomegranate juice", "عصير الرمان", "liters", "لتر"),
        ("sub", (7, 8), (2, 5), "silk ribbon", "شريط حريري", "meters", "متر"),
    ]
    for op, (n1, d1), (n2, d2), item_en, item_ar, u_en, u_ar in easy_fr:
        f1, f2 = Fraction(n1, d1), Fraction(n2, d2)
        ans = f1 + f2 if op == "add" else f1 - f2
        lcd = math.lcm(d1, d2)
        e1, e2 = n1 * (lcd // d1), n2 * (lcd // d2)
        op_sym = "+" if op == "add" else "-"
        naive_den = Fraction(n1 + n2, d1 + d2) if op == "add" else Fraction(max(1, n1 - n2), abs(d1 - d2) or 5)
        dists = [naive_den, Fraction(ans.numerator + 1, ans.denominator), Fraction(max(1, ans.numerator - 1), ans.denominator)]
        q_en = (
            f"Leen mixes {m(f'\\frac{{{n1}}}{{{d1}}}')} {u_en} and {m(f'\\frac{{{n2}}}{{{d2}}}')} {u_en} of {item_en}. What is the total amount in simplest form?"
            if op == "add"
            else f"An electrician starts with {m(f'\\frac{{{n1}}}{{{d1}}}')} {u_en} of {item_en} and cuts off {m(f'\\frac{{{n2}}}{{{d2}}}')} {u_en}. How much remains in simplest form?"
        )
        q_ar = (
            f"خلطت لين {m(f'\\frac{{{n1}}}{{{d1}}}')} {u_ar} و{m(f'\\frac{{{n2}}}{{{d2}}}')} {u_ar} من {item_ar}. ما الكمية الكلية في أبسط صورة؟"
            if op == "add"
            else f"لدى فني كهرباء قطعة من {item_ar} طولها {m(f'\\frac{{{n1}}}{{{d1}}}')} {u_ar}، قصّ منها {m(f'\\frac{{{n2}}}{{{d2}}}')} {u_ar}. كم بقي منها في أبسط صورة؟"
        )
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans, dists,
            f"Rewrite both fractions over their least common denominator LCD = {lcd}.",
            f"أعد كتابة الكسرين باستعمال المقام المشترك الأصغر وهو {lcd}.",
            f"Convert both fractions to denominator {m(lcd)} and combine numerators.",
            [
                f"Since {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {lcd}')}, write {m(f'\\frac{{{n1}}}{{{d1}}} = \\frac{{{e1}}}{{{lcd}}}')} and {m(f'\\frac{{{n2}}}{{{d2}}} = \\frac{{{e2}}}{{{lcd}}}')}.",
                f"Compute {m(f'\\frac{{{e1}}}{{{lcd}}} {op_sym} \\frac{{{e2}}}{{{lcd}}} = {_mx(ans)}')}.",
            ],
            f"{m(_mx(ans))} is in lowest terms because {m(f'\\gcd({ans.numerator}, {ans.denominator}) = 1')}.",
            f"نوحّد المقامين على المقام المشترك الأصغر {m(lcd)} ثم نجري العملية على البسطين.",
            [
                f"نكتب الكسرين المتكافئين: {m(f'\\frac{{{e1}}}{{{lcd}}}')} و{m(f'\\frac{{{e2}}}{{{lcd}}}')}.",
                f"الناتج في أبسط صورة هو {m(_mx(ans))}.",
            ],
            f"الكسر {m(_mx(ans))} في أبسط صورة لأن القاسم المشترك الأكبر لبسطه ومقامه هو 1.",
            diagram_en=svg_nafes_fraction_bars(n1, d1, n2, d2, f"{n1}/{d1}", f"{n2}/{d2}"),
        )

    # 5 Medium: Adding mixed numbers with unlike denominators
    med_mix = [
        ("Al-Ahsa date harvest", "موسم التمور بالأحساء", (2, 1, 2), (1, 2, 3), "kg", "كجم"),
        ("Taif rose distillation", "تقطير الورد الطائفي", (3, 3, 4), (2, 1, 6), "liters", "لتر"),
        ("Riyadh cycling track", "مسار الدراجات بالرياض", (4, 2, 5), (3, 3, 4), "km", "كم"),
        ("Abha hiking trail", "ممشى الجبل في أبها", (1, 5, 6), (2, 3, 8), "km", "كم"),
        ("Jeddah sailing rope", "حبل قارب شراعي بجدة", (5, 1, 3), (2, 4, 5), "m", "م"),
    ]
    for ctx_en, ctx_ar, (w1, n1, d1), (w2, n2, d2), u_en, u_ar in med_mix:
        f1 = Fraction(w1 * d1 + n1, d1)
        f2 = Fraction(w2 * d2 + n2, d2)
        ans = f1 + f2
        lcd = math.lcm(d1, d2)
        ans_s = _mx(ans)
        dists = [_mx(ans - Fraction(1, 1)), _mx(ans + Fraction(1, lcd)), _mx(Fraction(w1 + w2, 1) + Fraction(n1 + n2, d1 + d2))]
        B.add_math(
            tp, "Medium", bp,
            f"During the {ctx_en}, Team A recorded {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} {u_en} and Team B recorded {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')} {u_en}. What is their combined total as a mixed number in simplest form?",
            f"في {ctx_ar}، سجّل الفريق الأول {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} {u_ar} وسجّل الفريق الثاني {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')} {u_ar}. ما مجموع الكميتين على صورة عدد كسري في أبسط صورة؟",
            ans_s, dists,
            f"Use LCD = {lcd} for the fractional parts, and regroup if the fraction sum exceeds 1.",
            f"وحّد مقامي الجزأين الكسريين على {lcd}، وأعد التجميع إذا زاد مجموع الكسرين على 1.",
            "Add the fractional parts over their LCD, regroup any whole unit, and add the whole numbers.",
            [
                f"Over LCD {m(lcd)}: {m(f'\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}} = \\frac{{{n1*(lcd//d1) + n2*(lcd//d2)}}}{{{lcd}}}')}.",
                f"Combine with {m(f'{w1} + {w2} = {w1 + w2}')} and regroup to get {m(ans_s)} {u_en}.",
            ],
            f"Improper check: {m(f'\\frac{{{f1.numerator}}}{{{d1}}} + \\frac{{{f2.numerator}}}{{{d2}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}} = {ans_s}')}.",
            "نوحّد مقامي الكسرين ثم نجمع الأعداد الكلية ونعيد التجميع عند الحاجة.",
            [
                f"المقام المشترك الأصغر هو {m(lcd)}، ومجموع الجزأين الكسريين هو {m(f'\\frac{{{n1*(lcd//d1) + n2*(lcd//d2)}}}{{{lcd}}}')}.",
                f"بإضافة {m(f'{w1} + {w2} = {w1 + w2}')} والتبسيط نحصل على {m(ans_s)}.",
            ],
            f"التحقق بالكسور غير الفعلية يعطي {m(ans_s)} تماماً.",
            diagram_en=svg_nafes_fraction_bars(n1, d1, n2, d2, f"{w1} {n1}/{d1}", f"{w2} {n2}/{d2}"),
        )

    # 5 Hard: Subtracting mixed numbers with borrowing & 3-part whole-minus-two-fractions
    hard_sub = [
        ("borrow", "carpenter in Najran", "نجار في نجران", (5, 1, 4), (2, 2, 3), "m", "م"),
        ("borrow", "chef in Madinah", "طاهٍ في المدينة", (6, 1, 6), (3, 3, 4), "kg", "كجم"),
        ("borrow", "tailor in Makkah", "خيّاط في مكة", (7, 1, 5), (4, 1, 2), "m", "م"),
        ("remain", "Grade 6 garden plot", "حديقة الصف السادس", (1, 3), (2, 5), "", ""),
        ("remain", "school library budget", "ميزانية مكتبة المدرسة", (3, 8), (1, 4), "", ""),
    ]
    for kind, who_en, who_ar, p1, p2, u_en, u_ar in hard_sub:
        if kind == "borrow":
            w1, n1, d1 = p1
            w2, n2, d2 = p2
            f1 = Fraction(w1 * d1 + n1, d1)
            f2 = Fraction(w2 * d2 + n2, d2)
            ans = f1 - f2
            lcd = math.lcm(d1, d2)
            ans_s = _mx(ans)
            no_borrow_trap = _mx(ans + 1)
            flip_trap = _mx(Fraction(w1 - w2, 1) + abs(Fraction(n1, d1) - Fraction(n2, d2)))
            dists = [no_borrow_trap, flip_trap, _mx(ans + Fraction(1, lcd))]
            B.add_math(
                tp, "Hard", bp,
                f"A {who_en} has {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} {u_en} of material and uses {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')} {u_en}. How much material is left in simplest form?",
                f"لدى {who_ar} كمية قدرها {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} {u_ar}، استعمل منها {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')} {u_ar}. كم بقي لديه في أبسط صورة؟",
                ans_s, dists,
                f"Since {n1}/{d1} < {n2}/{d2}, borrow 1 whole ({lcd}/{lcd}) from {w1} before subtracting!",
                f"بما أن الكسر الأول أصغر من الثاني، استلف 1 صحيحاً ({lcd}/{lcd}) من {w1} قبل الطرح!",
                f"Regroup 1 whole from {w1} over LCD {lcd}, then subtract whole and fractional parts.",
                [
                    f"Over LCD {m(lcd)}, {m(f'{w1}\\frac{{{n1*(lcd//d1)}}}{{{lcd}}} = {w1-1}\\frac{{{lcd + n1*(lcd//d1)}}}{{{lcd}}}')}.",
                    f"Subtract {m(f'{w2}\\frac{{{n2*(lcd//d2)}}}{{{lcd}}}')} to obtain {m(ans_s)} {u_en}.",
                ],
                f"{m(f'{ans_s} + {w2}\\frac{{{n2}}}{{{d2}}} = {w1}\\frac{{{n1}}}{{{d1}}}')}.",
                f"نعيد تجميع 1 صحيح على المقام المشترك {m(lcd)} ثم نطرح.",
                [
                    f"بعد الاستلاف يصبح العدد الأول {m(f'{w1-1}\\frac{{{lcd + n1*(lcd//d1)}}}{{{lcd}}}')}.",
                    f"بطرح {m(f'{w2}\\frac{{{n2*(lcd//d2)}}}{{{lcd}}}')} ينتج {m(ans_s)}.",
                ],
                f"مجموع الباقي والمستعمل يعيد {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')}.",
                diagram_en=svg_two_jars(f"Start {w1} {n1}/{d1}", 0.85, f"Used {w2} {n2}/{d2}", 0.42, "Left = ?"),
            )
        else:
            n1, d1 = p1
            n2, d2 = p2
            f1, f2 = Fraction(n1, d1), Fraction(n2, d2)
            used = f1 + f2
            ans = 1 - used
            lcd = math.lcm(d1, d2)
            B.add_math(
                tp, "Hard", bp,
                f"In a {who_en}, {m(f'\\frac{{{n1}}}{{{d1}}}')} is allocated to Section A and {m(f'\\frac{{{n2}}}{{{d2}}}')} to Section B, while the rest goes to Section C. What fraction of the whole goes to Section C?",
                f"في {who_ar}، خُصّص {m(f'\\frac{{{n1}}}{{{d1}}}')} للقسم الأول و{m(f'\\frac{{{n2}}}{{{d2}}}')} للقسم الثاني، وخُصّص الباقي للقسم الثالث. ما الكسر الدال على نصيب القسم الثالث في أبسط صورة؟",
                ans, [used, Fraction(1, d1 + d2), Fraction(ans.numerator + 1, ans.denominator)],
                f"Add the two known fractions over LCD = {lcd}, then subtract their sum from 1 ({lcd}/{lcd}).",
                f"اجمع الكسرين المعلومين على المقام المشترك {lcd}، ثم اطرح مجموعهما من الواحد الصحيح ({lcd}/{lcd}).",
                "Subtract the sum of the first two fractions from 1 whole.",
                [
                    f"Add Sections A and B: {m(f'\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}} = \\frac{{{used.numerator}}}{{{used.denominator}}}')}.",
                    f"Subtract from {m(1)}: {m(f'1 - \\frac{{{used.numerator}}}{{{used.denominator}}} = {_mx(ans)}')}.",
                ],
                f"{m(f'\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}} + {_mx(ans)} = 1')}.",
                "نجمع الكسرين الأولين ثم نطرح الناتج من 1 صحيح.",
                [
                    f"مجموع القسمين الأول والثاني هو {m(_mx(used))}.",
                    f"نصيب القسم الثالث هو {m(f'1 - {_mx(used)} = {_mx(ans)}')}.",
                ],
                f"مجموع الأجزاء الثلاثة يساوي {m(1)} صحيحاً.",
                diagram_en=svg_nafes_fraction_bars(used.numerator, used.denominator, ans.numerator, ans.denominator, "A + B", "C = ?"),
            )


def _add_num_04(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-04"
    # 5 Easy: Fraction × Fraction or Whole × Fraction in simplest form
    easy_mul = [
        ((3, 4), (2, 5), "pan of basbousa", "صينية بسبوسة", 5, 4, 6),
        ((5, 6), (3, 10), "bottle of laban", "عبوة لبن", 6, 4, 6),
        ((4, 9), (3, 8), "roll of felt", "لفة لباد", 6, 3, 3),
        ((2, 3), (9, 10), "jug of mango nectar", "إبريق عصير مانجو", 5, 3, 9),
        ((5, 8), (4, 15), "tray of maamoul", "صينية معمول", 6, 2, 2),
    ]
    for (n1, d1), (n2, d2), item_en, item_ar, gc, gr, gs in easy_mul:
        ans = Fraction(n1, d1) * Fraction(n2, d2)
        dists = [Fraction(n1 + n2, d1 + d2), Fraction(n1 * d2, d1 * n2 if d1 * n2 > 0 else 1), Fraction(ans.numerator + 1, ans.denominator + 1)]
        B.add_math(
            tp, "Easy", bp,
            f"A tray holds {m(f'\\frac{{{n1}}}{{{d1}}}')} of a {item_en}. Grade 6 students eat {m(f'\\frac{{{n2}}}{{{d2}}}')} of what is on the tray. What fraction of the whole {item_en} did they eat?",
            f"تحتوي صينية على {m(f'\\frac{{{n1}}}{{{d1}}}')} من {item_ar}. تناول طلاب الصف السادس {m(f'\\frac{{{n2}}}{{{d2}}}')} مما في الصينية. ما الكسر الدال على ما تناولوه من {item_ar} كاملة في أبسط صورة؟",
            ans, dists,
            "A fraction OF a fraction means multiply numerators and multiply denominators, then simplify.",
            "كسر من كسر يعني ضرب البسط في البسط والمقام في المقام ثم التبسيط.",
            "Multiply the two fractions and cancel common factors.",
            [
                f"Multiply: {m(f'\\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}} = \\frac{{{n1 * n2}}}{{{d1 * d2}}}')}.",
                f"Divide numerator and denominator by {m(math.gcd(n1 * n2, d1 * d2))} to get {m(_mx(ans))}.",
            ],
            f"{m(_mx(ans))} is in simplest form.",
            "نضرب الكسرين ونختصر العوامل المشتركة بين البسط والمقام.",
            [
                f"حاصل الضرب قبل التبسيط: {m(f'\\frac{{{n1 * n2}}}{{{d1 * d2}}}')}.",
                f"بعد القسمة على {m(math.gcd(n1 * n2, d1 * d2))} نحصل على {m(_mx(ans))}.",
            ],
            f"الكسر {m(_mx(ans))} في أبسط صورة.",
            diagram_en=svg_fraction_grid(gc, gr, gs, 2),
        )

    # 5 Medium: Multiplying mixed numbers (recipes & rectangular banners)
    med_mul = [
        ("kabsa spice mix", "خلطة بهارات الكبسة", (2, 1, 4), (1, 1, 3), "cups", "أكواب"),
        ("school science poster", "ملصق علمي مدرسي", (2, 2, 5), (1, 1, 4), "m²", "م²"),
        ("cardamom coffee batch", "تحميص قهوة سعودية", (1, 3, 5), (2, 1, 2), "kg", "كجم"),
        ("heritage rug border", "إطار سجادة تراثية", (3, 1, 3), (1, 4, 5), "m²", "م²"),
        ("solar panel glass sheet", "لوح زجاجي شمسي", (2, 1, 2), (1, 3, 5), "m²", "م²"),
    ]
    for item_en, item_ar, (w1, n1, d1), (w2, n2, d2), u_en, u_ar in med_mul:
        f1 = Fraction(w1 * d1 + n1, d1)
        f2 = Fraction(w2 * d2 + n2, d2)
        ans = f1 * f2
        ans_s = _mx(ans)
        trap_sep = _mx(Fraction(w1 * w2, 1) + Fraction(n1 * n2, d1 * d2))
        dists = [trap_sep, _mx(ans + Fraction(1, 2)), _mx(ans + 1)]
        B.add_math(
            tp, "Medium", bp,
            f"For a {item_en}, a calculation multiplies {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} by {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')}. What is the product in {u_en} in simplest form?",
            f"في مسألة تتعلق بـ ({item_ar})، نضرب العدد الكسري {m(f'{w1}\\frac{{{n1}}}{{{d1}}}')} في {m(f'{w2}\\frac{{{n2}}}{{{d2}}}')}. ما ناتج الضرب بـ ({u_ar}) في أبسط صورة؟",
            ans_s, dists,
            "Convert both mixed numbers to improper fractions first, then cancel common factors and multiply.",
            "حوّل كلا العددين الكسريين إلى كسرين غير فعليين أولاً، ثم اختصر العوامل المشتركة واضرب.",
            "Convert to improper fractions before multiplying.",
            [
                f"Rewrite as improper fractions: {m(f'{w1}\\frac{{{n1}}}{{{d1}}} = \\frac{{{f1.numerator}}}{{{d1}}}')} and {m(f'{w2}\\frac{{{n2}}}{{{d2}}} = \\frac{{{f2.numerator}}}{{{d2}}}')}.",
                f"Multiply and simplify: {m(f'\\frac{{{f1.numerator}}}{{{d1}}} \\times \\frac{{{f2.numerator}}}{{{d2}}} = {ans_s}')}.",
            ],
            f"Estimate check: {m(f'{w1}\\frac{{{n1}}}{{{d1}}} \\times {w2}\\frac{{{n2}}}{{{d2}}} = {ans_s}')} matches whole-number bounds.",
            "نحوّل العددين الكسريين إلى كسور غير فعلية ثم نضرب ونبسّط.",
            [
                f"نكتب: {m(f'\\frac{{{f1.numerator}}}{{{d1}}} \\times \\frac{{{f2.numerator}}}{{{d2}}}')}.",
                f"بالاختصار نحصل على الناتج {m(ans_s)}.",
            ],
            f"الناتج الدقيق في أبسط صورة هو {m(ans_s)}.",
            diagram_en=svg_nafes_fraction_bars(n1, d1, n2, d2, f"{w1} {n1}/{d1}", f"× {w2} {n2}/{d2}"),
        )

    # 5 Hard: Dividing mixed numbers / 2-step combine-and-divide word problems
    hard_div = [
        ("Tabuk olive farm", "مزرعة زيتون في تبوك", (7, 1, 2), (3, 4), "bottles", "قارورة"),
        ("Diriyah weaving loom", "منسج تراثي بالدرعية", (6, 3, 4), (3, 8), "tassels", "شرابة"),
        ("Jazan juice stall", "ركن العصائر في جازان", (5, 1, 4), (3, 8), "cups", "كوباً"),
        ("Hail scout camp", "مخيم الكشافة بحائل", (10, 1, 2), (1, 3, 4), "tent ropes", "حبال خيمة"),
        ("Khobar bakery", "مخبز في الخبر", (8, 2, 5), (1, 1, 5), "dough loaves", "أرغفة عجين"),
    ]
    for ctx_en, ctx_ar, tot_m, piece_p, unit_en, unit_ar in hard_div:
        wt, nt, dt = tot_m
        f_tot = Fraction(wt * dt + nt, dt)
        if len(piece_p) == 2:
            np_, dp_ = piece_p
            f_pc = Fraction(np_, dp_)
            pc_tex = f"\\frac{{{np_}}}{{{dp_}}}"
        else:
            wp, np_, dp_ = piece_p
            f_pc = Fraction(wp * dp_ + np_, dp_)
            pc_tex = f"{wp}\\frac{{{np_}}}{{{dp_}}}"
        ans_q = f_tot / f_pc
        assert ans_q.denominator == 1
        ans_int = ans_q.numerator
        B.add_math(
            tp, "Hard", bp,
            f"At a {ctx_en}, {m(f'{wt}\\frac{{{nt}}}{{{dt}}}')} units of supply are divided equally into portions of size {m(pc_tex)} each. How many {unit_en} are produced?",
            f"في {ctx_ar}، قُسّمت كمية مقدارها {m(f'{wt}\\frac{{{nt}}}{{{dt}}}')} بالتساوي إلى حصص حجم كلٍّ منها {m(pc_tex)}. كم ({unit_ar}) تنتج من هذا التقسيم؟",
            ans_int, [ans_int - 2, ans_int + 2, max(2, int(f_tot * f_pc))],
            "Convert to improper fractions, then multiply the total by the reciprocal of the portion size!",
            "حوّل إلى كسور غير فعلية، ثم اضرب الكمية الكلية في مقلوب حجم الحصة الواحدة!",
            "Divide the total supply by the size of one portion using Keep-Change-Flip.",
            [
                f"Write as improper fractions: {m(f'{wt}\\frac{{{nt}}}{{{dt}}} = \\frac{{{f_tot.numerator}}}{{{f_tot.denominator}}}')} and portion {m(f'\\frac{{{f_pc.numerator}}}{{{f_pc.denominator}}}')}.",
                f"Multiply by the reciprocal: {m(f'\\frac{{{f_tot.numerator}}}{{{f_tot.denominator}}} \\times \\frac{{{f_pc.denominator}}}{{{f_pc.numerator}}} = {ans_int}')}.",
            ],
            f"{m(f'{ans_int} \\times \\frac{{{f_pc.numerator}}}{{{f_pc.denominator}}} = \\frac{{{f_tot.numerator}}}{{{f_tot.denominator}}} = {wt}\\frac{{{nt}}}{{{dt}}}')}.",
            "نحوّل إلى كسور غير فعلية ثم نضرب المقسوم في مقلوب المقسوم عليه.",
            [
                f"الكمية الكلية ككسر غير فعلي هي {m(f'\\frac{{{f_tot.numerator}}}{{{f_tot.denominator}}}')}.",
                f"نضرب في المقلوب {m(f'\\frac{{{f_pc.denominator}}}{{{f_pc.numerator}}}')} فنجد الناتج {m(ans_int)}.",
            ],
            f"التحقق بالضرب العكسي: {m(f'{ans_int} \\times {pc_tex} = {wt}\\frac{{{nt}}}{{{dt}}}')}.",
            diagram_en=svg_two_jars(f"Total {wt} {nt}/{dt}", 0.88, f"Each {pc_tex}", 0.25, "÷"),
        )


def _add_num_05(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-05"
    # 5 Easy: Decimal rounding, place value & addition/subtraction
    easy_dec = [
        ("round10", "7.482", "7.5", ["7.4", "7.48", "8.0"], "Riyadh weather sensor", "حسّاس طقس بالرياض", "tenth", "أقرب جزء من عشرة"),
        ("round100", "12.637", "12.64", ["12.63", "12.6", "12.7"], "chemistry balance in Jeddah", "ميزان مختبر بجدة", "hundredth", "أقرب جزء من مئة"),
        ("add", "4.75 + 2.6", "7.35", ["5.01", "7.01", "6.35"], "two water jugs", "وعاءي ماء", "", ""),
        ("sub", "9.4 - 3.68", "5.72", ["6.28", "5.82", "6.72"], "a wooden plank", "لوح خشبي", "", ""),
        ("add", "6.08 + 5.92", "12", ["11.9", "11.1", "12.1"], "two track sprints", "شوطي جري", "", ""),
    ]
    for kind, expr, ans_s, dists, ctx_en, ctx_ar, pl_en, pl_ar in easy_dec:
        if kind.startswith("round"):
            q_en = f"A {ctx_en} displays the reading {m(expr)}. What is this decimal rounded to the nearest **{pl_en}**?"
            q_ar = f"يُظهر {ctx_ar} القراءة العشرية {m(expr)}. ما تقريب هذا العدد إلى **{pl_ar}**؟"
            h_en = f"Look at the digit immediately to the right of the {pl_en}s place; if it is 5 or more, round up."
            h_ar = f"انظر إلى الرقم الواقع على يمين منزلة التقريب مباشرة؛ إذا كان 5 أو أكبر نضيف 1."
        else:
            q_en = f"While measuring {ctx_en}, Reem computes {m(expr)}. What is the exact value?"
            q_ar = f"أثناء قياس {ctx_ar}، حسبت ريم قيمة العبارة {m(expr)}. ما الناتج الدقيق؟"
            h_en = "Line up the decimal points vertically and pad missing hundredths with a zero before operating."
            h_ar = "رتّب الفواصل العشرية عمودياً وضع صفراً في المنازل الخالية قبل إجراء العملية."
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans_s, dists, h_en, h_ar,
            "Align decimal places carefully and apply place-value rules.",
            [
                f"Start with {m(expr)} and inspect each decimal place (tenths, hundredths, thousandths).",
                f"Carrying out the operation accurately gives {m(ans_s)}.",
            ],
            f"Place-value check confirms {m(ans_s)}.",
            "نراعي القيمة المنزلية للأجزاء العشرية ومحاذاة الفاصلة.",
            [
                f"نفحص المنازل العشرية في {m(expr)} بدقة.",
                f"بتنفيذ القاعدة نحصل على الناتج {m(ans_s)}.",
            ],
            f"مراجعة المنازل العشرية تؤكد صحة {m(ans_s)}.",
            diagram_en=svg_nafes_function_table(["Expression / Reading", expr], [["Result", "?"]], highlight_cell=(0, 1)),
        )

    # 5 Medium: Multiplying decimals in real contexts
    med_dec = [
        ("Al-Madinah Ajwa dates", "تمر عجوة المدينة", "3.5", "24.2", "84.7", ["8.47", "847", "72.7"]),
        ("Taif pomegranate crate", "صندوق رمان طائفي", "2.4", "16.5", "39.6", ["3.96", "38.4", "396"]),
        ("Jazan mango basket", "سلة مانجو جازان", "4.5", "13.2", "59.4", ["5.94", "58.5", "594"]),
        ("Qassim wheat sack", "كيس قمح القصيم", "1.6", "12.5", "20", ["2", "19.2", "200"]),
        ("Hail olive oil tin", "عبوة زيت زيتون حائل", "2.5", "31.6", "79", ["7.9", "78", "790"]),
    ]
    for item_en, item_ar, kg_s, pr_s, ans_s, dists in med_dec:
        B.add_math(
            tp, "Medium", bp,
            f"At a farmers' market, {item_en} costs {m(pr_s)} SAR per kilogram. How much do {m(kg_s)} kilograms cost in SAR?",
            f"في سوق المزارعين، يبلغ سعر الكيلوجرام الواحد من ({item_ar}) {m(pr_s)} ريالاً. كم ريالاً ثمن {m(kg_s)} كيلوجرام؟",
            ans_s, dists,
            f"Multiply {kg_s} × {pr_s} as whole numbers, then place the decimal point using the total number of decimal places.",
            f"اضرب {kg_s} × {pr_s} كأعداد كلية أولاً، ثم ضع الفاصلة بحسب مجموع المنازل العشرية في العاملين.",
            f"Multiply quantity {m(kg_s)} kg by unit price {m(pr_s)} SAR/kg.",
            [
                f"Compute {m(f'{kg_s} \\times {pr_s}')}.",
                f"Count two total decimal digits (and drop any trailing `.00`) to obtain {m(ans_s)} SAR.",
            ],
            f"Reasonableness check: {m(f'{kg_s} \\times {pr_s} = {ans_s}')} SAR.",
            f"نضرب الوزن {m(kg_s)} كجم في سعر الكيلوجرام {m(pr_s)} ريالاً.",
            [
                f"نحسب حاصل الضرب {m(f'{kg_s} \\times {pr_s}')}.",
                f"نضع الفاصلة بعد منزلتين عشريتين فنجد الثمن {m(ans_s)} ريالاً.",
            ],
            f"التقدير التقريبي يؤكد أن {m(ans_s)} ريالاً جواب معقول ودقيق.",
            diagram_en=svg_nafes_function_table(["Mass (kg)", "1", kg_s], [["Cost (SAR)", pr_s, "?"]], highlight_cell=(0, 2)),
        )

    # 5 Hard: Decimal division & multi-step SAR change problems
    hard_dec = [
        ("div", "lab technician in Dhahran", "فني مختبر في الظهران", "18.9", "0.45", 42, [4.2, 38, 420]),
        ("div", "tailor inHofuf shop", "مشغل خياطة بالهفوف", "21.6", "0.8", 27, [2.7, 24, 270]),
        ("div", "beekeeping coop in Baha", "جمعية نحالين بالباحة", "15.75", "0.35", 45, [4.5, 35, 450]),
        ("change", "Salman", "سلمان", "100", "3.5", "18.4", "35.6", ["64.4", "36.6", "45.6"]),
        ("change", "Maha", "مها", "50", "2.5", "13.8", "15.5", ["34.5", "16.5", "25.5"]),
    ]
    for row in hard_dec:
        if row[0] == "div":
            _, who_en, who_ar, tot_s, unit_s, ans_i, dists = row
            who_en_clean = who_en.replace("inHofuf", "in a Hofuf")
            B.add_math(
                tp, "Hard", bp,
                f"A {who_en_clean} divides {m(tot_s)} liters equally into containers of {m(unit_s)} liter each. How many containers are filled?",
                f"يوزّع {who_ar} كمية قدرها {m(tot_s)} لتر بالتساوي في عبوات سعة كلٍّ منها {m(unit_s)} لتر. كم عبوة تمتلئ؟",
                ans_i, dists,
                "Shift the decimal point right in both dividend and divisor so the divisor becomes a whole number.",
                "حرّك الفاصلة لليمين في المقسوم والمقسوم عليه بالقدر نفسه ليصبح المقسوم عليه عدداً كلياً.",
                f"Compute {m(f'{tot_s} \\div {unit_s}')} by clearing decimals first.",
                [
                    f"Multiply both numbers by a power of {m(10)} to clear the divisor's decimal.",
                    f"Evaluating {m(f'{tot_s} \\div {unit_s}')} gives {m(ans_i)} containers.",
                ],
                f"{m(f'{ans_i} \\times {unit_s} = {tot_s}')}.",
                f"نحسب {m(f'{tot_s} \\div {unit_s}')} بعد التخلص من الفاصلة في المقسوم عليه.",
                [
                    f"نحرّك الفاصلة لليمين في الحدين ثم نقسم قسمة أعداد كلية.",
                    f"الناتج هو {m(ans_i)} عبوة.",
                ],
                f"التحقق: {m(f'{ans_i} \\times {unit_s} = {tot_s}')}.",
                diagram_en=svg_two_jars(f"{tot_s} L", 0.86, f"{unit_s} L", 0.28, "÷"),
            )
        else:
            _, name_en, name_ar, bill_s, qty_s, pr_s, ans_s, dists = row
            spent_s = dists[0]
            B.add_math(
                tp, "Hard", bp,
                f"{name_en} pays with a {m(bill_s)}-SAR banknote for {m(qty_s)} kg of almonds priced at {m(pr_s)} SAR per kg. How many SAR of **change** does {name_en} receive?",
                f"دفع/دفعت {name_ar} ورقة نقدية من فئة {m(bill_s)} ريال لشراء {m(qty_s)} كجم من اللوز بسعر {m(pr_s)} ريال للكيلوجرام. كم ريالاً **الباقي** المسترد؟",
                ans_s, dists,
                f"First multiply {qty_s} × {pr_s} to find the total cost, then subtract that cost from {bill_s} SAR.",
                f"اضرب أولاً {qty_s} × {pr_s} لإيجاد التكلفة الكلية، ثم اطرح التكلفة من {bill_s} ريالاً.",
                f"Compute total cost {m(f'{qty_s} \\times {pr_s}')} and subtract from {m(bill_s)}.",
                [
                    f"Total cost = {m(f'{qty_s} \\times {pr_s} = {spent_s}')} SAR.",
                    f"Change = {m(f'{bill_s} - {spent_s} = {ans_s}')} SAR.",
                ],
                f"{m(f'{spent_s} + {ans_s} = {bill_s}')} SAR.",
                f"نحسب التكلفة الكلية ثم نطرحها من {m(bill_s)} ريالاً.",
                [
                    f"ثمن اللوز: {m(f'{qty_s} \\times {pr_s} = {spent_s}')} ريالاً.",
                    f"الباقي المسترد: {m(f'{bill_s} - {spent_s} = {ans_s}')} ريالاً.",
                ],
                f"التحقق: {m(f'{spent_s} + {ans_s} = {bill_s}')} ريالاً.",
                diagram_en=svg_nafes_sar_money([int(bill_s)], f"Paid {bill_s} SAR | Cost {spent_s} SAR"),
            )


def _add_num_06(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-06"
    # 5 Easy: Simplifying ratios (part-to-part and part-to-whole)
    easy_rat = [
        ("part", 18, "red apples", "تفاح أحمر", 24, "green apples", "تفاح أخضر", "3 : 4", ["4 : 3", "3 : 7", "6 : 8"]),
        ("part", 20, "science books", "كتب علمية", 35, "storybooks", "قصص أدبية", "4 : 7", ["7 : 4", "4 : 11", "5 : 7"]),
        ("whole", 12, "gold medals", "ميداليات ذهبية", 18, "silver medals", "ميداليات فضية", "2 : 5", ["2 : 3", "3 : 5", "12 : 18"]),
        ("part", 28, "palm trees", "نخلات", 21, "olive trees", "شجرات زيتون", "4 : 3", ["3 : 4", "4 : 7", "7 : 3"]),
        ("whole", 15, "goalie saves", "تصديات ناجحة", 10, "missed saves", "كرات فائتة", "3 : 5", ["3 : 2", "2 : 5", "5 : 3"]),
    ]
    for mode, a, i1_en, i1_ar, b, i2_en, i2_ar, ans_s, dists in easy_rat:
        tot = a + b
        g = math.gcd(a, b if mode == "part" else tot)
        q_en = (
            f"A basket holds {m(a)} {i1_en} and {m(b)} {i2_en}. What is the ratio of {i1_en} to {i2_en} in simplest form?"
            if mode == "part"
            else f"A team recorded {m(a)} {i1_en} and {m(b)} {i2_en}. What is the ratio of {i1_en} to the **total** in simplest form?"
        )
        q_ar = (
            f"تضم سلة {m(a)} من ({i1_ar}) و{m(b)} من ({i2_ar}). ما نسبة ({i1_ar}) إلى ({i2_ar}) في أبسط صورة؟"
            if mode == "part"
            else f"سجّل فريق {m(a)} من ({i1_ar}) و{m(b)} من ({i2_ar}). ما نسبة ({i1_ar}) إلى **العدد الكلي** في أبسط صورة؟"
        )
        rhs = b if mode == "part" else tot
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans_s, dists,
            f"Divide both terms of {a} : {rhs} by their GCD = {g}.",
            f"اقسم حدي النسبة {a} : {rhs} على قاسمهما المشترك الأكبر وهو {g}.",
            f"Form the ratio {m(f'{a} : {rhs}')} and divide both terms by {m(g)}.",
            [
                f"Write the unsimplified ratio: {m(f'{a} : {rhs}')}.",
                f"Divide both terms by {m(f'\\gcd({a}, {rhs}) = {g}')} to get {m(ans_s)}.",
            ],
            f"Order matches the wording and {m(ans_s)} has GCD 1.",
            f"نكتب النسبة {m(f'{a} : {rhs}')} ثم نقسم حديها على {m(g)}.",
            [
                f"النسبة قبل التبسيط هي {m(f'{a} : {rhs}')}.",
                f"بالقسمة على {m(g)} تصبح النسبة في أبسط صورة {m(ans_s)}.",
            ],
            f"الترتيب مطابق للمطلوب والنسبة {m(ans_s)} في أبسط صورة.",
            diagram_en=svg_nafes_function_table(["Part A", "Part B", "Total"], [[str(a), str(b), str(tot)]]),
        )

    # 5 Medium: Unit rates (speed, typing, unit price, water flow)
    med_rate = [
        ("Riyadh–Dammam express bus", "حافلة الرياض–الدمام", 360, "km", 4, "hours", "km/h", "كم/ساعة"),
        ("school 3D printer", "طابعة ثلاثية الأبعاد", 135, "grams", 3, "hours", "grams/h", "جم/ساعة"),
        ("bookstore bundle", "عرض مكتبة", 96, "SAR", 8, "notebooks", "SAR/notebook", "ريال/دفتر"),
        ("smart drip irrigator", "مرشّ زراعي ذكي", 140, "liters", 5, "minutes", "L/min", "لتر/دقيقة"),
        ("Grade 6 typist", "طالب في نادي الحاسب", 210, "words", 6, "minutes", "words/min", "كلمة/دقيقة"),
    ]
    for ctx_en, ctx_ar, q1, u1, q2, u2, ur_en, ur_ar in med_rate:
        ans = q1 // q2
        B.add_math(
            tp, "Medium", bp,
            f"A {ctx_en} records {m(q1)} {u1} in {m(q2)} {u2}. What is the **unit rate** in {ur_en}?",
            f"يسجّل ({ctx_ar}) معدل {m(q1)} ({u1}) خلال {m(q2)} ({u2}). ما **معدل الوحدة** بوحدة ({ur_ar})؟",
            ans, [ans - 5, ans + 6, q1 - q2],
            f"Divide {q1} by {q2} so the second quantity becomes 1.",
            f"اقسم {q1} على {q2} ليصبح المقام مساوياً لوحدة واحدة.",
            f"Divide {m(q1)} by {m(q2)} to obtain the rate per 1 unit.",
            [
                f"Set up the rate: {m(f'\\frac{{{q1}}}{{{q2}}}')}.",
                f"Divide: {m(f'{q1} \\div {q2} = {ans}')} {ur_en}.",
            ],
            f"{m(f'{ans} \\times {q2} = {q1}')}.",
            f"نقسم {m(q1)} على {m(q2)} لإيجاد المعدل لكل وحدة واحدة.",
            [
                f"نكتب المعدل: {m(f'{q1} \\div {q2}')}.",
                f"ناتج القسمة هو {m(ans)} ({ur_ar}).",
            ],
            f"التحقق: {m(f'{ans} \\times {q2} = {q1}')}.",
            diagram_en=svg_motion_timeline("0", f"{q1} {u1}", f"in {q2} {u2}", f"? {ur_en}", "", meet=False),
        )

    # 5 Hard: Comparing unit prices / multi-column ratio table sum
    hard_rate = [
        ("table", "science kits", "حقائب علمية", 4, 28, 9, "SAR", "ريال"),
        ("table", "solar cells", "خلايا شمسية", 5, 45, 11, "watts", "واط"),
        ("table", "seedling trays", "صواني شتلات", 6, 48, 13, "plants", "شتلة"),
        ("deal", "honey packs", "عروض العسل", 3, 72, 5, 110),
        ("deal", "juice cartons", "صناديق العصير", 4, 36, 6, 48),
    ]
    for row in hard_rate:
        if row[0] == "table":
            _, item_en, item_ar, k1, v1, k2, u_en, u_ar = row
            unit_v = v1 // k1
            ans = k2 * unit_v
            B.add_math(
                tp, "Hard", bp,
                f"In a proportional ratio table for {item_en}, {m(k1)} units correspond to {m(v1)} {u_en}, and {m(2*k1)} units correspond to {m(2*v1)} {u_en}. How many {u_en} correspond to {m(k2)} units?",
                f"في جدول نسب متكافئة لـ ({item_ar})، تقابل {m(k1)} وحدات قيمة {m(v1)} ({u_ar})، وتقابل {m(2*k1)} وحدات قيمة {m(2*v1)} ({u_ar}). فما القيمة المقابلة لـ {m(k2)} وحدة؟",
                ans, [ans - unit_v, ans + unit_v, v1 + k2],
                f"Find the unit rate ({v1} ÷ {k1} = {unit_v}) first, then multiply by {k2}.",
                f"أوجد معدل الوحدة أولاً ({v1} ÷ {k1} = {unit_v}) ثم اضربه في {k2}.",
                f"Compute the unit rate {m(unit_v)} per unit and scale by {m(k2)}.",
                [
                    f"Unit rate = {m(f'{v1} \\div {k1} = {unit_v}')} {u_en} per unit.",
                    f"For {m(k2)} units: {m(f'{k2} \\times {unit_v} = {ans}')} {u_en}.",
                ],
                f"The ratio {m(f'{ans} : {k2}')} simplifies to {m(f'{unit_v} : 1')}.",
                f"نستخرج معدل الوحدة بقسمة {m(v1)} على {m(k1)} ثم نضرب في {m(k2)}.",
                [
                    f"معدل الوحدة = {m(f'{v1} \\div {k1} = {unit_v}')}.",
                    f"القيمة المقابلة لـ {m(k2)} وحدة = {m(f'{k2} \\times {unit_v} = {ans}')}.",
                ],
                f"النسبة {m(f'{ans} : {k2}')} تبسّط إلى {m(f'{unit_v} : 1')}.",
                diagram_en=svg_nafes_function_table(
                    ["Units", str(k1), str(2 * k1), str(k2)],
                    [[u_en, str(v1), str(2 * v1), "?"]],
                    highlight_cell=(0, 3),
                ),
            )
        else:
            _, item_en, item_ar, n_a, p_a, n_b, p_b = row
            u_a, u_b = p_a // n_a, p_b // n_b
            ans = min(u_a, u_b)
            B.add_math(
                tp, "Hard", bp,
                f"Comparing {item_en}: Offer A sells {m(n_a)} items for {m(p_a)} SAR, while Offer B sells {m(n_b)} items for {m(p_b)} SAR. What is the **lower** unit price (in SAR per item)?",
                f"عند مقارنة ({item_ar}): يبيع العرض (أ) {m(n_a)} قطع بسعر {m(p_a)} ريالاً، ويبيع العرض (ب) {m(n_b)} قطع بسعر {m(p_b)} ريالاً. كم يبلغ سعر القطعة الواحدة في العرض **الأرخص** بالريال؟",
                ans, [max(u_a, u_b), u_a + u_b, abs(p_b - p_a)],
                "Compute each offer's unit price (total SAR ÷ item count) and pick the smaller one.",
                "احسب سعر الوحدة لكل عرض (السعر الكلي ÷ عدد القطع) ثم اختر السعر الأقل.",
                "Calculate both unit prices and compare them.",
                [
                    f"Offer A unit price: {m(f'{p_a} \\div {n_a} = {u_a}')} SAR/item.",
                    f"Offer B unit price: {m(f'{p_b} \\div {n_b} = {u_b}')} SAR/item.",
                    f"The lower unit price is {m(ans)} SAR.",
                ],
                f"{m(ans)} < {m(max(u_a, u_b))}, confirming Offer B has the better unit price.",
                "نحسب سعر القطعة الواحدة في كل عرض ثم نقارن بينهما.",
                [
                    f"سعر القطعة في العرض (أ): {m(f'{p_a} \\div {n_a} = {u_a}')} ريالاً.",
                    f"سعر القطعة في العرض (ب): {m(f'{p_b} \\div {n_b} = {u_b}')} ريالاً؛ والأقل هو {m(ans)} ريالاً.",
                ],
                f"{m(ans)} أصغر من {m(max(u_a, u_b))} فهو سعر الوحدة الأفضل.",
                diagram_en=svg_nafes_function_table(["Offer", "Items", "Total SAR"], [["A", str(n_a), str(p_a)], ["B", str(n_b), str(p_b)]]),
            )


def _add_num_07(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-07"
    # 5 Easy: Solving direct proportions a/b = c/x
    easy_prop = [
        (3, 8, 15, "science lab test tubes", "أنابيب اختبار"),
        (4, 9, 28, "sports league jerseys", "قمصان رياضية"),
        (5, 12, 35, "museum brochures", "مطويات متحفية"),
        (6, 11, 42, "school art canvases", "لوحات فنية"),
        (7, 10, 63, "botanical labels", "بطاقات نباتية"),
    ]
    for a, b, c, ctx_en, ctx_ar in easy_prop:
        scale = c // a
        ans = b * scale
        B.add_math(
            tp, "Easy", bp,
            f"While ordering {ctx_en}, Khalid solves the proportion {m(f'\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{x}}')}. What is the value of {m('x')}?",
            f"أثناء طلب ({ctx_ar})، يحل خالد التناسب {m(f'\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{x}}')}. ما قيمة {m('x')}؟",
            ans, [ans - b, ans + a, c + (b - a)],
            f"Notice {a} × {scale} = {c}, so multiply {b} by {scale} as well.",
            f"لاحظ أن {a} × {scale} = {c}، لذا اضرب {b} في {scale} أيضاً.",
            f"Scale both numerator and denominator by {m(scale)} (or cross-multiply).",
            [
                f"Compare numerators: {m(f'{c} \\div {a} = {scale}')}.",
                f"Multiply the denominator by {m(scale)}: {m(f'x = {b} \\times {scale} = {ans}')}.",
            ],
            f"Cross-products match: {m(f'{a} \\times {ans} = {a * ans}')} and {m(f'{b} \\times {c} = {b * c}')}.",
            f"نضرب حدي النسبة الأولى في عامل التوسيع {m(scale)} أو نستعمل الضرب التبادلي.",
            [
                f"بما أن {m(f'{a} \\times {scale} = {c}')} نضرب المقام في {m(scale)}.",
                f"نجد {m(f'x = {b} \\times {scale} = {ans}')}.",
            ],
            f"التحقق بالضرب التبادلي: {m(f'{a} \\times {ans} = {b} \\times {c} = {a * ans}')}.",
            diagram_en=svg_nafes_function_table(["Numerator", str(a), str(c)], [["Denominator", str(b), "x = ?"]], highlight_cell=(0, 2)),
        )

    # 5 Medium: Saudi map & architectural model scale problems
    med_scale = [
        ("Riyadh Metro map", "خريطة قطار الرياض", 2, "cm", 7, "km", 10, "km", "كم"),
        ("Jeddah waterfront model", "مجسم واجهة جدة البحرية", 3, "cm", 12, "m", 15, "m", "م"),
        ("Neom exhibition map", "خريطة معرض نيوم", 1, "cm", 18, "km", 9, "km", "كم"),
        ("Diriyah fort miniature", "مجسم قصر الدرعية", 4, "cm", 10, "m", 14, "m", "م"),
        ("Al-Ula trail map", "خريطة مسار العلا", 5, "cm", 20, "km", 17, "km", "كم"),
    ]
    for ctx_en, ctx_ar, s_map, u_m, s_real, u_r, d_map, out_en, out_ar in med_scale:
        assert (s_real * d_map) % s_map == 0
        ans = (s_real * d_map) // s_map
        B.add_math(
            tp, "Medium", bp,
            f"On a {ctx_en}, the scale is {m(f'{s_map}\\text{{ {u_m}}} : {s_real}\\text{{ {u_r}}}')}. If the model/map distance is {m(d_map)} {u_m}, what is the actual length in {out_en}?",
            f"في ({ctx_ar})، مقياس الرسم هو {m(f'{s_map}\\text{{ {u_m}}} : {s_real}\\text{{ {u_r}}}')}. إذا كان البعد على الرسم {m(d_map)} ({u_m})، فما الطول الحقيقي بوحدة ({out_ar})؟",
            ans, [ans - s_real, ans + s_real, d_map * s_map],
            f"Set up the proportion {s_map}/{s_real} = {d_map}/x and cross-multiply.",
            f"اكتب التناسب {s_map}/{s_real} = {d_map}/س ثم استعمل الضرب التبادلي.",
            "Form a map-to-actual proportion and solve for the real distance.",
            [
                f"Write {m(f'\\frac{{{s_map}}}{{{s_real}}} = \\frac{{{d_map}}}{{x}}')}.",
                f"Cross-multiply: {m(f'{s_map}x = {s_real * d_map} \\implies x = {ans}')} {out_en}.",
            ],
            f"Unit scale is {m(Fraction(s_real, s_map))} {out_en} per {u_m}, times {m(d_map)} = {m(ans)}.",
            "نكتب تناسب مقياس الرسم ونحل لإيجاد الطول الحقيقي.",
            [
                f"التناسب: {m(f'\\frac{{{s_map}}}{{{s_real}}} = \\frac{{{d_map}}}{{x}}')}.",
                f"بالضرب التبادلي والقسمة على {m(s_map)} نحصل على {m(f'x = {ans}')} ({out_ar}).",
            ],
            f"النسبة محفوظة لأن {m(f'{s_map} \\times {ans} = {s_real} \\times {d_map}')}.",
            diagram_en=svg_fenceposts(f"{s_map} {u_m} = {s_real} {u_r}", f"{d_map} {u_m} = ? {out_en}"),
        )

    # 5 Hard: Multi-step ratio sharing (given ratio a:b and total T) & shadow-height proportions
    hard_prop = [
        ("share", "STEM robotics club", "نادي الروبوت", 3, 5, 120, "first", "الأول"),
        ("share", "school tree-planting campaign", "حملة التشجير المدرسي", 4, 7, 132, "second", "الثاني"),
        ("share", "charity food baskets", "سلال غذائية خيرية", 2, 7, 162, "second", "الثاني"),
        ("shadow", "flagpole in Riyadh", "سارية علم بالرياض", 3, 2, 12),
        ("shadow", "palm tree in Hofuf", "نخلة في الهفوف", 5, 4, 16),
    ]
    for row in hard_prop:
        if row[0] == "share":
            _, ctx_en, ctx_ar, r1, r2, tot, which_en, which_ar = row
            parts_sum = r1 + r2
            one_part = tot // parts_sum
            ans = (r1 if which_en == "first" else r2) * one_part
            other = tot - ans
            B.add_math(
                tp, "Hard", bp,
                f"In a {ctx_en}, {m(tot)} items are divided between Group 1 and Group 2 in the ratio {m(f'{r1} : {r2}')}. How many items does the **{which_en}** group receive?",
                f"في ({ctx_ar})، قُسّم {m(tot)} عنصراً بين المجموعة الأولى والمجموعة الثانية بنسبة {m(f'{r1} : {r2}')}. كم عنصراً نصيب المجموعة **{which_ar}**؟",
                ans, [other, one_part, tot // 2],
                f"Add the ratio parts ({r1} + {r2} = {parts_sum}) first to find the value of 1 part!",
                f"اجمع أجزاء النسبة أولاً ({r1} + {r2} = {parts_sum}) لإيجاد قيمة الجزء الواحد!",
                f"Divide {m(tot)} by {m(parts_sum)} total parts, then multiply by the group's share.",
                [
                    f"Total parts = {m(f'{r1} + {r2} = {parts_sum}')}.",
                    f"Value of 1 part = {m(f'{tot} \\div {parts_sum} = {one_part}')}.",
                    f"Requested share = {m(f'{ans // one_part} \\times {one_part} = {ans}')}.",
                ],
                f"Both shares add up to {m(f'{ans} + {other} = {tot}')}.",
                f"نجمع أجزاء النسبة ({m(parts_sum)}) ونقسم الكل عليها لإيجاد الحصة الواحدة.",
                [
                    f"مجموع الأجزاء = {m(f'{r1} + {r2} = {parts_sum}')}، وقيمة الجزء الواحد = {m(f'{tot} \\div {parts_sum} = {one_part}')}.",
                    f"النصيب المطلوب = {m(ans)} عنصراً.",
                ],
                f"مجموع النصيبين: {m(f'{ans} + {other} = {tot}')}.",
                diagram_en=svg_nafes_function_table(["Group 1", "Group 2", "Total"], [[f"{r1} parts", f"{r2} parts", f"{tot} items"]]),
            )
        else:
            _, obj_en, obj_ar, h_stick, s_stick, s_obj = row
            ans = (h_stick * s_obj) // s_stick
            B.add_math(
                tp, "Hard", bp,
                f"At afternoon recess, a {m(h_stick)}-meter post casts a {m(s_stick)}-meter shadow at the exact moment a {obj_en} casts a {m(s_obj)}-meter shadow. How tall is the {obj_en} in meters?",
                f"في فناء المدرسة، يصنع عمود طوله {m(h_stick)} م ظلاً طوله {m(s_stick)} م في اللحظة نفسها التي تصنع فيها ({obj_ar}) ظلاً طوله {m(s_obj)} م. كم متراً ارتفاع ({obj_ar})؟",
                ans, [ans - h_stick, s_obj + (h_stick - s_stick), (s_stick * s_obj) // max(1, h_stick - 1)],
                f"Set up height / shadow = {h_stick} / {s_stick} = H / {s_obj}.",
                f"اكتب تناسب الارتفاع إلى الظل: {h_stick} / {s_stick} = ع / {s_obj}.",
                "Heights and shadows at the same moment are directly proportional.",
                [
                    f"Write the proportion: {m(f'\\frac{{{h_stick}}}{{{s_stick}}} = \\frac{{H}}{{{s_obj}}}')}.",
                    f"Solve: {m(f'H = \\frac{{{h_stick} \\times {s_obj}}}{{{s_stick}}} = {ans}')} m.",
                ],
                f"Height-to-shadow ratio {m(f'{ans} : {s_obj}')} reduces to {m(f'{h_stick} : {s_stick}')}.",
                "نكتب التناسب بين الطول وطول الظل في اللحظة نفسها ثم نحله.",
                [
                    f"التناسب: {m(f'\\frac{{{h_stick}}}{{{s_stick}}} = \\frac{{H}}{{{s_obj}}}')}.",
                    f"بحل التناسب نجد الارتفاع {m(f'H = {ans}')} م.",
                ],
                f"نسبة الارتفاع إلى الظل {m(f'{ans} : {s_obj}')} تكافئ {m(f'{h_stick} : {s_stick}')}.",
                diagram_en=svg_shaded_triangle_in_rect(s_obj, ans, 0.0, "m", w_lbl="H = ? m"),
            )


def _add_num_08(B: G6BankBuilder) -> None:
    tp, bp = "Numbers & Operations", "G6-NUM-08"
    # 5 Easy: Fraction/decimal <-> percentage & simple % of a quantity
    easy_pct = [
        ("conv", (3, 5), 60, [35, 53, 65], "3/5 of a solar battery", "3/5 من بطارية شمسية"),
        ("conv", (7, 20), 35, [14, 27, 70], "7/20 of a school library", "7/20 من كتب المكتبة"),
        ("of", 20, 150, 30, [20, 50, 120], "trees in a Qassim orchard", "شجرة في مزرعة بالقصيم"),
        ("of", 40, 85, 34, [32, 45, 51], "points in a robotics contest", "نقطة في مسابقة الروبوت"),
        ("of", 75, 120, 90, [75, 80, 95], "seats on a Madinah train coach", "مقعداً في عربة قطار المدينة"),
    ]
    for row in easy_pct:
        if row[0] == "conv":
            _, (num, den), ans, dists, ctx_en, ctx_ar = row
            mult = 100 // den
            B.add_math(
                tp, "Easy", bp,
                f"A display shows that {m(f'\\frac{{{num}}}{{{den}}}')} ({ctx_en.split('of ', 1)[1]}) is charged/cataloged. What **percentage** is equivalent to {m(f'\\frac{{{num}}}{{{den}}}')}?",
                f"تُظهر لوحة أن الكسر {m(f'\\frac{{{num}}}{{{den}}}')} يمثّل الجزء المنجز من ({ctx_ar.split('من ', 1)[1]}). ما **النسبة المئوية** المكافئة للكسر {m(f'\\frac{{{num}}}{{{den}}}')}؟",
                ans, dists,
                f"Scale the denominator {den} up to 100 by multiplying top and bottom by {mult}.",
                f"اجعل المقام 100 بضرب البسط والمقام في {mult}.",
                f"Write an equivalent fraction with denominator {m(100)}.",
                [
                    f"Multiply numerator and denominator by {m(mult)}: {m(f'\\frac{{{num} \\times {mult}}}{{{den} \\times {mult}}} = \\frac{{{ans}}}{{100}}')}.",
                    f"Therefore {m(f'\\frac{{{num}}}{{{den}}} = {ans}\\%')}.",
                ],
                f"{m(f'{ans}\\% = \\frac{{{ans}}}{{100}} = \\frac{{{num}}}{{{den}}}')}.",
                f"نحوّل المقام إلى {m(100)} بضرب البسط والمقام في {m(mult)}.",
                [
                    f"الكسر المكافئ: {m(f'\\frac{{{num * mult}}}{{100}}')}.",
                    f"إذن النسبة المئوية هي {m(f'{ans}\\%')}.",
                ],
                f"التبسيط يعيد الكسر الأصلي {m(f'\\frac{{{num}}}{{{den}}}')}.",
                suffix="\\%",
                diagram_en=svg_fraction_grid(den if den <= 10 else 10, 2 if den == 20 else 2, num if den == 20 else num * 2, 0),
            )
        else:
            _, pct, tot, ans, dists, ctx_en, ctx_ar = row
            B.add_math(
                tp, "Easy", bp,
                f"What is {m(f'{pct}\\%')} of {m(tot)} {ctx_en}?",
                f"ما قيمة {m(f'{pct}\\%')} من {m(tot)} ({ctx_ar})؟",
                ans, dists,
                f"Multiply {pct}/100 by {tot} and simplify.",
                f"اضرب {pct}/100 في {tot} ثم بسّط الناتج.",
                f"Compute {m(f'\\frac{{{pct}}}{{100}} \\times {tot}')}.",
                [
                    f"Write {m(f'{pct}\\%')} as {m(f'\\frac{{{pct}}}{{100}}')}.",
                    f"Multiply: {m(f'\\frac{{{pct} \\times {tot}}}{{100}} = \\frac{{{pct * tot}}}{{100}} = {ans}')}.",
                ],
                f"{m(f'\\frac{{{ans}}}{{{tot}}} = \\frac{{{pct}}}{{100}} = {pct}\\%')}.",
                f"نكتب النسبة على صورة كسر مقامه 100 ثم نضرب في {m(tot)}.",
                [
                    f"نحسب {m(f'\\frac{{{pct}}}{{100}} \\times {tot} = {ans}')}.",
                ],
                f"نسبة {m(ans)} إلى {m(tot)} تساوي {m(f'{pct}\\%')}.",
                diagram_en=svg_fraction_grid(10, 5, pct // 2, 0),
            )

    # 5 Medium: Sale price in SAR after a % discount
    med_disc = [
        ("Riyadh sports store", "متجر رياضي بالرياض", "football boots", "حذاء رياضي", 200, 15, [100, 100]),
        ("Dammam electronics shop", "معرض إلكترونيات بالدمام", "wireless headphones", "سماعة لاسلكية", 250, 20, [100, 100, 50]),
        ("Jeddah stationery shop", "قرطاسية في جدة", "geometry backpack", "حقيبة مدرسية", 140, 30, [100, 20, 20]),
        ("Makkah watch boutique", "متجر ساعات بمكة", "digital sports watch", "ساعة رقمية", 180, 25, [100, 50, 20, 10]),
        ("Abha outdoor gear store", "متجر رحلات بأبها", "camping lantern", "مصباح تخييم", 120, 35, [100, 20]),
    ]
    for store_en, store_ar, item_en, item_ar, orig, pct, bills in med_disc:
        disc = (orig * pct) // 100
        sale = orig - disc
        B.add_math(
            tp, "Medium", bp,
            f"A {store_en} offers a {m(f'{pct}\\%')} discount on {item_en} originally priced at {m(orig)} SAR. What is the **sale price** in SAR?",
            f"يقدّم ({store_ar}) خصماً نسبته {m(f'{pct}\\%')} على ({item_ar}) سعره الأصلي {m(orig)} ريالاً. فما **سعر البيع بعد الخصم** بالريال؟",
            sale, [disc, orig - pct, orig + disc],
            f"Find {pct}% of {orig} SAR to get the discount, then subtract it from {orig} SAR!",
            f"احسب {pct}% من {orig} ريالاً لمعرفة مقدار الخصم، ثم اطرحه من {orig} ريالاً!",
            f"Subtract the {m(f'{pct}\\%')} discount ({m(disc)} SAR) from {m(orig)} SAR.",
            [
                f"Discount amount: {m(f'\\frac{{{pct}}}{{100}} \\times {orig} = {disc}')} SAR.",
                f"Sale price: {m(f'{orig} - {disc} = {sale}')} SAR.",
            ],
            f"Paying {m(f'{100 - pct}\\%')} of {m(orig)} gives {m(f'\\frac{{{100 - pct}}}{{100}} \\times {orig} = {sale}')} SAR.",
            f"نحسب مقدار الخصم أولاً ثم نطرحه من السعر الأصلي {m(orig)} ريالاً.",
            [
                f"قيمة الخصم: {m(f'\\frac{{{pct}}}{{100}} \\times {orig} = {disc}')} ريالاً.",
                f"سعر البيع النهائي: {m(f'{orig} - {disc} = {sale}')} ريالاً.",
            ],
            f"يدفع المشتري {m(f'{100 - pct}\\%')} من السعر الأصلي أي {m(sale)} ريالاً.",
            diagram_en=svg_nafes_sar_money(bills, f"Original {orig} SAR (-{pct}%)"),
        )

    # 5 Hard: Reverse percentage (finding whole from part) & VAT / two-step SAR problems
    hard_pct = [
        ("whole", "science quiz", "اختبار العلوم", 18, 90, "questions", "سؤالاً"),
        ("whole", "school auditorium", "مسرح المدرسة", 84, 70, "chairs", "كرسياً"),
        ("whole", "Tabuk farm harvest", "محصول مزرعة تبوك", 96, 60, "crates", "صندوقاً"),
        ("vat", "microscope kit", "طقم مجهر علمي", 200, 15),
        ("vat", "tablet stand", "حامل جهاز لوحي", 80, 15),
    ]
    for row in hard_pct:
        if row[0] == "whole":
            _, ctx_en, ctx_ar, part_v, pct, u_en, u_ar = row
            ans = (part_v * 100) // pct
            B.add_math(
                tp, "Hard", bp,
                f"On a {ctx_en}, {m(part_v)} {u_en} represent exactly {m(f'{pct}\\%')} of the total. What is the **total** number of {u_en}?",
                f"في ({ctx_ar})، يمثّل العدد {m(part_v)} ({u_ar}) نسبة {m(f'{pct}\\%')} تماماً من الإجمالي. فما **العدد الكلي**؟",
                ans, [(part_v * pct) // 100 or part_v - 4, part_v + (100 - pct), ans + 10],
                f"Set up {pct}/100 = {part_v}/T, so T = ({part_v} × 100) ÷ {pct}.",
                f"اكتب التناسب المئوي {pct}/100 = {part_v}/ك، ومنه ك = ({part_v} × 100) ÷ {pct}.",
                f"Use the percent proportion {m(f'\\frac{{{pct}}}{{100}} = \\frac{{{part_v}}}{{T}}')} to find the whole {m('T')}.",
                [
                    f"Write {m(f'\\frac{{{pct}}}{{100}} = \\frac{{{part_v}}}{{T}}')}.",
                    f"Solve: {m(f'T = \\frac{{{part_v} \\times 100}}{{{pct}}} = {ans}')}.",
                ],
                f"{m(f'{pct}\\%')} of {m(ans)} is {m(f'\\frac{{{pct}}}{{100}} \\times {ans} = {part_v}')}.",
                f"نستعمل تناسب النسبة المئوية لإيجاد الكل من الجزء المعلوم.",
                [
                    f"نكتب المعادلة: {m(f'\\frac{{{pct}}}{{100}} \\times T = {part_v}')}.",
                    f"ومنه العدد الكلي {m(f'T = \\frac{{{part_v} \\times 100}}{{{pct}}} = {ans}')}.",
                ],
                f"التحقق: {m(f'{pct}\\%')} من {m(ans)} يساوي {m(part_v)}.",
                diagram_en=svg_nafes_function_table(["Percent", f"{pct}%", "100%"], [["Count", str(part_v), "?"]], highlight_cell=(0, 2)),
            )
        else:
            _, item_en, item_ar, base_p, vat_p = row
            tax = (base_p * vat_p) // 100
            ans = base_p + tax
            B.add_math(
                tp, "Hard", bp,
                f"An educational store sells a {item_en} for {m(base_p)} SAR before tax. Including {m(f'{vat_p}\\%')} Value-Added Tax (VAT), what is the **total price** paid in SAR?",
                f"يبيع متجر تعليمي ({item_ar}) بسعر {m(base_p)} ريال قبل الضريبة. مع إضافة ضريبة القيمة المضافة بنسبة {m(f'{vat_p}\\%')}، كم يبلغ **السعر الإجمالي** بالريال؟",
                ans, [tax, base_p - tax, base_p + vat_p],
                f"Compute {vat_p}% of {base_p} SAR for the VAT, then ADD it to {base_p} SAR.",
                f"احسب {vat_p}% من {base_p} ريالاً لمعرفة الضريبة، ثم أضفها إلى {base_p} ريالاً.",
                f"Add {m(f'{vat_p}\\%')} tax ({m(tax)} SAR) to the pre-tax price {m(base_p)} SAR.",
                [
                    f"VAT = {m(f'\\frac{{{vat_p}}}{{100}} \\times {base_p} = {tax}')} SAR.",
                    f"Total price = {m(f'{base_p} + {tax} = {ans}')} SAR.",
                ],
                f"{m(f'1.15 \\times {base_p} = {ans}')} SAR.",
                f"نحسب مبلغ الضريبة ثم نجمعه مع السعر الأصلي.",
                [
                    f"قيمة الضريبة: {m(f'\\frac{{{vat_p}}}{{100}} \\times {base_p} = {tax}')} ريالاً.",
                    f"السعر الشامل للضريبة: {m(f'{base_p} + {tax} = {ans}')} ريالاً.",
                ],
                f"التحقق: {m(f'{base_p} + {tax} = {ans}')} ريالاً.",
                diagram_en=svg_nafes_sar_money([50, 20, 10], f"Base {base_p} SAR + {vat_p}% VAT"),
            )


def _add_alg_01(B: G6BankBuilder) -> None:
    tp, bp = "Algebra", "G6-ALG-01"
    # 5 Easy: Order of operations with parentheses or exponents
    easy_pem = [
        ("Riyadh math olympiad warm-up", "تدريب أولمبياد الرياض", 14, 6, 3, "add_mul"),   # 14 + 6 × 3 = 32
        ("Jeddah STEM quiz", "مسابقة العلوم بجدة", 40, 16, 4, "sub_div"),                 # 40 - 16 ÷ 4 = 36
        ("Dammam coding club", "نادي البرمجة بالدمام", 5, 3, 4, "pow_add"),               # 5² + 3 × 4 = 37
        ("Abha classroom board", "سبورة صف سادس بأبها", 9, 5, 3, "par_mul"),              # (9 + 5) × 3 = 42
        ("Madinah library puzzle", "لغز مكتبة المدينة", 4, 3, 10, "cube_sub"),            # 4³ - 10 = 54
    ]
    for ctx_en, ctx_ar, a, b, c, mode in easy_pem:
        if mode == "add_mul":
            expr, ans, dists = f"{a} + {b} \\times {c}", a + b * c, [(a + b) * c, a * b + c, a + b + c]
            s1 = f"Multiply first: {m(f'{b} \\times {c} = {b * c}')}, then add {m(a)} to get {m(ans)}."
            s1_ar = f"نضرب أولاً: {m(f'{b} \\times {c} = {b * c}')} ثم نجمع {m(a)} فنحصل على {m(ans)}."
        elif mode == "sub_div":
            expr, ans, dists = f"{a} - {b} \\div {c}", a - b // c, [(a - b) // c, a + b // c, a - b]
            s1 = f"Divide first: {m(f'{b} \\div {c} = {b // c}')}, then subtract from {m(a)} to get {m(ans)}."
            s1_ar = f"نقسم أولاً: {m(f'{b} \\div {c} = {b // c}')} ثم نطرح من {m(a)} فنحصل على {m(ans)}."
        elif mode == "pow_add":
            expr, ans, dists = f"{a}^2 + {b} \\times {c}", a * a + b * c, [2 * a + b * c, (a * a + b) * c, a * a + b + c]
            s1 = f"Compute {m(f'{a}^2 = {a * a}')} and {m(f'{b} \\times {c} = {b * c}')}, then add to get {m(ans)}."
            s1_ar = f"نحسب {m(f'{a}^2 = {a * a}')} و{m(f'{b} \\times {c} = {b * c}')} ثم نجمعهما فنحصل على {m(ans)}."
        elif mode == "par_mul":
            expr, ans, dists = f"({a} + {b}) \\times {c}", (a + b) * c, [a + b * c, a * c + b, a + b + c]
            s1 = f"Parentheses first: {m(f'{a} + {b} = {a + b}')}, then multiply by {m(c)} to get {m(ans)}."
            s1_ar = f"نحسب ما داخل القوس أولاً: {m(f'{a} + {b} = {a + b}')} ثم نضرب في {m(c)} فنحصل على {m(ans)}."
        else:
            expr, ans, dists = f"{a}^3 - {c}", a ** 3 - c, [a * 3 - c, a * a - c, a ** 3 + c]
            s1 = f"Compute the cube {m(f'{a}^3 = {a ** 3}')}, then subtract {m(c)} to get {m(ans)}."
            s1_ar = f"نحسب القوة {m(f'{a}^3 = {a ** 3}')} ثم نطرح {m(c)} فنحصل على {m(ans)}."
        B.add_math(
            tp, "Easy", bp,
            f"In a {ctx_en}, students evaluate {m(expr)}. What is its value?",
            f"في ({ctx_ar})، يحسب الطلاب قيمة العبارة {m(expr)}. فما قيمتها؟",
            ans, dists,
            "Follow order of operations: parentheses, then exponents, then ×/÷ before +/−.",
            "اتّبع ترتيب العمليات: الأقواس أولاً، ثم الأسس، ثم الضرب والقسمة قبل الجمع والطرح.",
            "Apply Grade 6 order of operations step by step.",
            [s1],
            f"Re-evaluating {m(expr)} confirms {m(ans)}.",
            "نطبّق ترتيب العمليات الحسابية خطوة بخطوة.",
            [s1_ar],
            f"إعادة الحساب بالترتيب الصحيح تؤكد أن الناتج {m(ans)}.",
            diagram_en=svg_number_strip([expr.replace("\\times", "×").replace("\\div", "÷"), "=", "?"]),
        )

    # 5 Medium: 4-step expressions with parentheses, powers, multiplication & division
    med_pem = [
        (48, 3, 5, 2, 3, "Taif"),    # 48 ÷ (3+5) + 2³ × 3 = 6 + 24 = 30
        (36, 5, 4, 4, 2, "Qassim"),  # 36 ÷ (5+4) + 4² × 2 = 4 + 32 = 36
        (60, 7, 5, 3, 4, "Yanbu"),   # 60 ÷ (7+5) + 3² × 4 = 5 + 36 = 41
        (54, 2, 7, 5, 2, "Hail"),    # 54 ÷ (2+7) + 5² × 2 = 6 + 50 = 56
        (72, 4, 8, 2, 5, "Tabuk"),   # 72 ÷ (4+8) + 2³ × 5 = 6 + 40 = 46
    ]
    for d_num, p1, p2, base_v, mult_v, city in med_pem:
        exp_p = 3 if base_v == 2 else 2
        q_part = d_num // (p1 + p2)
        pw_val = base_v ** exp_p
        ans = q_part + pw_val * mult_v
        expr = f"{d_num} \\div ({p1} + {p2}) + {base_v}^{exp_p} \\times {mult_v}"
        B.add_math(
            tp, "Medium", bp,
            f"On a Grade 6 Nafes practice sheet in {city}, what is the value of {m(expr)}?",
            f"في ورقة عمل لاختبار نافس للصف السادس، ما قيمة العبارة {m(expr)}؟",
            ans, [(q_part + pw_val) * mult_v, q_part + base_v * exp_p * mult_v, ans - q_part],
            f"Evaluate ({p1}+{p2}) first, then {base_v}^{exp_p}, then divide and multiply before adding!",
            f"احسب القوس ({p1}+{p2}) أولاً، ثم الأس {base_v}^{exp_p}، ثم القسمة والضرب قبل الجمع!",
            "Clear parentheses and exponents first, then perform ÷ and × before +.",
            [
                f"Parentheses and power: {m(f'{p1} + {p2} = {p1 + p2}')} and {m(f'{base_v}^{exp_p} = {pw_val}')}.",
                f"Divide and multiply: {m(f'{d_num} \\div {p1 + p2} = {q_part}')} and {m(f'{pw_val} \\times {mult_v} = {pw_val * mult_v}')}.",
                f"Add: {m(f'{q_part} + {pw_val * mult_v} = {ans}')}.",
            ],
            f"{m(f'{q_part} + {pw_val * mult_v} = {ans}')}.",
            "نفك القوس والأس أولاً ثم نجري القسمة والضرب وأخيراً الجمع.",
            [
                f"القوس: {m(f'{p1}+{p2}={p1+p2}')}، والقوة: {m(f'{base_v}^{exp_p}={pw_val}')}.",
                f"القسمة والضرب ثم الجمع: {m(f'{q_part} + {pw_val * mult_v} = {ans}')}.",
            ],
            f"المجموع النهائي هو {m(ans)}.",
            diagram_en=svg_function_machine(f"{d_num}÷({p1}+{p2})", f"+ {base_v}^{exp_p}×{mult_v}", "PEMDAS", "?"),
        )

    # 5 Hard: Fraction-bar grouping & dual-parentheses order of operations
    hard_pem = [
        (5, 11, 4, 6, 2, "Diriyah"),   # (5² + 11) / 4 + 6 × 2 = 9 + 12 = 21
        (6, 12, 8, 5, 3, "Jubail"),    # (6² + 12) / 8 + 5 × 3 = 6 + 15 = 21 -> let's vary c*d!
        (7, 1, 5, 4, 3, "Al-Ula"),     # (7² + 1) / 5 + 4 × 3 = 10 + 12 = 22
        (4, 14, 6, 7, 2, "Najran"),    # (4² + 14) / 6 + 7 × 2 = 5 + 14 = 19
        (8, 8, 9, 3, 5, "Sakaka"),     # (8² + 8) / 9 + 3 × 5 = 8 + 15 = 23
    ]
    for a, b, c, d, e, city in hard_pem:
        top = a * a + b
        assert top % c == 0
        ans = top // c + d * e
        expr = f"\\frac{{{a}^2 + {b}}}{{{c}}} + {d} \\times {e}"
        B.add_math(
            tp, "Hard", bp,
            f"A challenge card at the {city} STEM Club asks for the value of {m(expr)}. What is the correct result?",
            f"في بطاقة تحدٍّ بنادي العلوم في ({city})، ما القيمة الصحيحة للعبارة {m(expr)}؟",
            ans, [(top // c + d) * e, (2 * a + b + d * e), ans + c],
            "Treat the numerator above the fraction bar as grouped in parentheses, then divide by the denominator and add the product.",
            "عامِل البسط فوق خط الكسر كأنه داخل قوسين، ثم اقسم على المقام واجمع مع حاصل الضرب.",
            "Evaluate the numerator first, divide by the denominator, and add the product.",
            [
                f"Numerator: {m(f'{a}^2 + {b} = {a * a} + {b} = {top}')}.",
                f"Divide by {m(c)} and multiply {m(f'{d} \\times {e}')}: {m(f'{top // c} + {d * e} = {ans}')}.",
            ],
            f"{m(f'\\frac{{{top}}}{{{c}}} + {d * e} = {top // c} + {d * e} = {ans}')}.",
            "نحسب البسط أولاً ثم نقسمه على المقام ونجمع الناتج مع حاصل الضرب.",
            [
                f"البسط: {m(f'{a}^2 + {b} = {top}')}، وبقسمته على {m(c)} ينتج {m(top // c)}.",
                f"نجمع مع {m(f'{d} \\times {e} = {d * e}')} فنحصل على {m(ans)}.",
            ],
            f"الناتج النهائي هو {m(ans)}.",
            diagram_en=svg_number_strip([f"({a}²+{b})÷{c}", "+", f"{d}×{e}", "=", "?"]),
        )


def _add_alg_02(B: G6BankBuilder) -> None:
    tp, bp = "Algebra", "G6-ALG-02"
    # 5 Easy: Evaluating 1-variable algebraic expressions ax + b or x/a + b
    easy_ev = [
        (5, 8, 6, "5n + 8", "library points", "نقاط القراءة"),
        (7, -9, 4, "7k - 9", "quiz tokens", "رموز المسابقة"),
        (6, 11, 5, "6m + 11", "seedlings planted", "شتلات مزروعة"),
        (9, -14, 3, "9t - 14", "robotics score", "درجة الروبوت"),
        (8, 7, 7, "8p + 7", "museum visitors", "زوار المتحف"),
    ]
    for a, b, x_v, expr_s, ctx_en, ctx_ar in easy_ev:
        var = expr_s[1]
        ans = a * x_v + b
        B.add_math(
            tp, "Easy", bp,
            f"The expression {m(expr_s)} models {ctx_en}. What is its value when {m(f'{var} = {x_v}')}?",
            f"تمثّل العبارة الجبرية {m(expr_s)} ({ctx_ar}). ما قيمتها عندما تكون {m(f'{var} = {x_v}')}؟",
            ans, [a + x_v + b, a * (x_v + abs(b)), ans + a],
            f"Replace {var} with {x_v}, multiply by {a} first, and then combine with {b}.",
            f"عوّض عن {var} بالعدد {x_v}، واضرب في {a} أولاً ثم اجمع أو اطرح.",
            f"Substitute {m(f'{var} = {x_v}')} into {m(expr_s)}.",
            [
                f"Multiply first: {m(f'{a} \\times {x_v} = {a * x_v}')}.",
                f"Combine the constant term to obtain {m(ans)}.",
            ],
            f"Substituting {m(x_v)} gives {m(ans)}.",
            f"نعوّض عن المتغير {m(var)} بالقيمة {m(x_v)} ثم نضرب أولاً.",
            [
                f"حاصل الضرب: {m(f'{a} \\times {x_v} = {a * x_v}')}.",
                f"بعد جمع/طرح الحد الثابت نحصل على {m(ans)}.",
            ],
            f"الناتج عند {m(f'{var} = {x_v}')} هو {m(ans)}.",
            diagram_en=svg_function_machine(f"{var} = {x_v}", f"× {a}", f"{'+' if b > 0 else '−'} {abs(b)}", "?"),
        )

    # 5 Medium: Evaluating 2-variable expressions (am + bn - c or a^2 + bm)
    med_ev = [
        (4, 3, 5, 6, 4, "Riyadh book fair", "معرض الرياض للكتاب"),
        (5, 2, 7, 8, 3, "Jeddah aquarium", "فقيه أكواريوم بجدة"),
        (6, 4, 9, 5, 2, "Dammam science hub", "مركز سايتك بالدمام"),
        (3, 5, 4, 7, 6, "Abha art gallery", "معرض الفنون بأبها"),
        (7, 3, 8, 4, 5, "Madinah museum shop", "متجر متحف المدينة"),
    ]
    for c1, c2, sub_k, xv, yv, ctx_en, ctx_ar in med_ev:
        ans = c1 * xv + c2 * yv - sub_k
        expr = f"{c1}x + {c2}y - {sub_k}"
        B.add_math(
            tp, "Medium", bp,
            f"At the {ctx_en}, a group coupon uses the formula {m(expr)}. Find its value when {m(f'x = {xv}')} and {m(f'y = {yv}')}.",
            f"في ({ctx_ar})، تُحسب قيمة قسيمة جماعية بالعبارة {m(expr)}. أوجد قيمتها عندما {m(f'x = {xv}')} و{m(f'y = {yv}')}.",
            ans, [c1 * xv + c2 * yv + sub_k, c1 * yv + c2 * xv - sub_k, ans - c2],
            f"Compute {c1}({xv}) and {c2}({yv}) separately, add them, and subtract {sub_k}.",
            f"احسب {c1}({xv}) و{c2}({yv}) كلاً على حدة، ثم اجمعهما واطرح {sub_k}.",
            f"Substitute {m(f'x = {xv}')} and {m(f'y = {yv}')} into {m(expr)}.",
            [
                f"Products: {m(f'{c1}({xv}) = {c1 * xv}')} and {m(f'{c2}({yv}) = {c2 * yv}')}.",
                f"Combine: {m(f'{c1 * xv} + {c2 * yv} - {sub_k} = {ans}')}.",
            ],
            f"{m(f'{c1 * xv + c2 * yv} - {sub_k} = {ans}')}.",
            "نعوّض عن كل متغير بقيمته ثم نضرب قبل الجمع والطرح.",
            [
                f"نحسب حاصلي الضرب: {m(c1 * xv)} و{m(c2 * yv)}.",
                f"نجمع ثم نطرح {m(sub_k)}: {m(f'{c1 * xv} + {c2 * yv} - {sub_k} = {ans}')}.",
            ],
            f"القيمة الصحيحة هي {m(ans)}.",
            diagram_en=svg_nafes_function_table(["x", "y", expr], [[str(xv), str(yv), "?"]], highlight_cell=(0, 2)),
        )

    # 5 Hard: Translating verbal phrases & two-part club cost models
    hard_ev = [
        ("phrase", "6 less than 4 times a number n", "أقل من أربعة أمثال العدد n بمقدار 6", "4n - 6", ["6 - 4n", "4(n - 6)", "6n - 4"]),
        ("phrase", "9 more than half of a number x", "أكبر من نصف العدد x بمقدار 9", "\\frac{x}{2} + 9", ["2x + 9", "9 - \\frac{x}{2}", "\\frac{x + 9}{2}"]),
        ("cost", "swimming academy in Khobar", "أكاديمية سباحة بالخبر", 45, 25, 6),
        ("cost", "coding camp in Riyadh", "معسكر برمجة بالرياض", 60, 35, 5),
        ("cost", "pottery studio in Taif", "مشغل خزف بالطائف", 30, 22, 7),
    ]
    for row in hard_ev:
        if row[0] == "phrase":
            _, ph_en, ph_ar, ans_tex, dists = row
            B.add_math(
                tp, "Hard", bp,
                f"Which algebraic expression correctly translates the phrase: **\"{ph_en}\"**?",
                f"أي عبارة جبرية مما يلي تترجم العبارة اللفظية: **«{ph_ar}»** ترجمة صحيحة؟",
                ans_tex, dists,
                "Watch subtraction order carefully: '6 less than A' means A − 6, not 6 − A!",
                "انتبه لترتيب الطرح جيداً: «أقل من أ بمقدار 6» تعني أ − 6 وليس 6 − أ!",
                "Translate the multiplier/fraction first, then apply 'more than' (+) or 'less than' (−).",
                [
                    f"Identify the base term from the variable phrase, then attach the constant offset to obtain {m(ans_tex)}.",
                ],
                f"Testing a sample value confirms {m(ans_tex)} matches \"{ph_en}\".",
                "نحدد الحد الجبري الأساسي أولاً ثم نضيف أو نطرح الثابت بالترتيب الصحيح.",
                [
                    f"العبارة الجبرية المطابقة للصياغة اللفظية هي {m(ans_tex)}.",
                ],
                f"التعويض بعدد تجريبي يؤكد تطابق {m(ans_tex)} مع المعنى اللفظي.",
                diagram_en=svg_function_machine("Input", "Main term", "Offset", ans_tex.replace("\\frac{x}{2}", "x/2")),
            )
        else:
            _, place_en, place_ar, reg_fee, per_s, n_sess = row
            ans = reg_fee + per_s * n_sess
            B.add_math(
                tp, "Hard", bp,
                f"A {place_en} charges a one-time registration fee of {m(reg_fee)} SAR plus {m(per_s)} SAR per session ({m(f'{reg_fee} + {per_s}s')}). How much does a student pay in SAR for {m(n_sess)} sessions?",
                f"تفرض ({place_ar}) رسوم تسجيل لمرة واحدة قدرها {m(reg_fee)} ريالاً بالإضافة إلى {m(per_s)} ريالاً عن كل حصة ({m(f'{reg_fee} + {per_s}s')}). كم ريالاً يدفع الطالب مقابل {m(n_sess)} حصص؟",
                ans, [(reg_fee + per_s) * n_sess, reg_fee * n_sess + per_s, ans - reg_fee],
                f"Multiply {per_s} SAR by {n_sess} sessions first; add the one-time {reg_fee} SAR registration fee only once!",
                f"اضرب {per_s} ريالاً في {n_sess} حصص أولاً، ثم أضف رسوم التسجيل ({reg_fee} ريالاً) مرة واحدة فقط!",
                f"Evaluate {m(f'{reg_fee} + {per_s}({n_sess})')}.",
                [
                    f"Session cost: {m(f'{per_s} \\times {n_sess} = {per_s * n_sess}')} SAR.",
                    f"Add registration fee: {m(f'{reg_fee} + {per_s * n_sess} = {ans}')} SAR.",
                ],
                f"Registration {m(reg_fee)} + sessions {m(per_s * n_sess)} = {m(ans)} SAR.",
                f"نعوّض {m(f's = {n_sess}')} في العبارة {m(f'{reg_fee} + {per_s}s')}.",
                [
                    f"تكلفة الحصص: {m(f'{per_s} \\times {n_sess} = {per_s * n_sess}')} ريالاً.",
                    f"بإضافة رسوم التسجيل لمرة واحدة: {m(f'{reg_fee} + {per_s * n_sess} = {ans}')} ريالاً.",
                ],
                f"المبلغ الكلي هو {m(ans)} ريالاً.",
                diagram_en=svg_nafes_function_table(["Sessions s", "1", "2", str(n_sess)], [["Cost (SAR)", str(reg_fee + per_s), str(reg_fee + 2 * per_s), "?"]], highlight_cell=(0, 3)),
            )


def _add_alg_03(B: G6BankBuilder) -> None:
    tp, bp = "Algebra", "G6-ALG-03"
    # 5 Easy: Next term in arithmetic & geometric sequences
    easy_seq = [
        ("arith", [7, 13, 19, 25], 31, "+6", "reading club pages", "صفحات نادي القراءة"),
        ("arith", [52, 45, 38, 31], 24, "−7", "water tank level", "منسوب خزان الماء"),
        ("geom", [3, 6, 12, 24], 48, "×2", "bacteria lab model", "نموذج مخبري"),
        ("geom", [2, 6, 18, 54], 162, "×3", "paper-folding layers", "طبقات طي الورق"),
        ("arith", [11, 20, 29, 38], 47, "+9", "solar display tiles", "بلاطات لوحة شمسية"),
    ]
    for kind, terms, ans, rule_s, ctx_en, ctx_ar in easy_seq:
        t_str = ", ".join(str(v) for v in terms)
        dists = [ans - 3, ans + 4, terms[-1] + (terms[1] - terms[0] if kind == "geom" else terms[-1])]
        B.add_math(
            tp, "Easy", bp,
            f"A sequence for {ctx_en} follows the pattern {m(f'{t_str}, \\dots')}. What is the **next term**?",
            f"تسير متتابعة لـ ({ctx_ar}) وفق النمط {m(f'{t_str}، \\dots')}. ما **الحد التالي** في المتتابعة؟",
            ans, dists,
            f"Compare consecutive terms to spot the constant rule ({rule_s}).",
            f"قارن الحدود المتتالية لاكتشاف قاعدة النمط الثابتة ({rule_s}).",
            f"Apply the step rule {m(rule_s)} to the fourth term {m(terms[-1])}.",
            [
                f"Each term changes by {m(rule_s)} from the previous term.",
                f"Applying {m(rule_s)} to {m(terms[-1])} gives {m(ans)}.",
            ],
            f"The five terms {m(f'{t_str}, {ans}')} follow the exact same rule.",
            f"نطبّق قاعدة النمط {m(rule_s)} على الحد الأخير {m(terms[-1])}.",
            [
                f"قاعدة الانتقال بين كل حد والذي يليه هي {m(rule_s)}.",
                f"بتطبيق القاعدة على {m(terms[-1])} نحصل على الحد التالي {m(ans)}.",
            ],
            f"الحدود الخمسة تحقق القاعدة نفسها دون استثناء.",
            diagram_en=svg_number_strip([str(v) for v in terms] + ["?"]),
        )

    # 5 Medium: Missing output in two-operation linear function tables y = ax + b
    med_fn = [
        (3, 4, [1, 3, 5, 8], "Riyadh robotics battery", "بطارية روبوت بالرياض"),
        (5, -2, [2, 4, 6, 9], "Jeddah ferry tickets", "تذاكر عبارة جدة"),
        (4, 7, [1, 2, 4, 7], "Dammam coding badges", "أوسمة برمجة بالدمام"),
        (6, -5, [2, 3, 5, 8], "Abha greenhouse pots", "أصص مشتل بأبها"),
        (2, 9, [3, 6, 9, 14], "Madinah book club", "نادي الكتاب بالمدينة"),
    ]
    for a, b, xs, ctx_en, ctx_ar in med_fn:
        ys = [a * x + b for x in xs]
        ans = ys[-1]
        rule_tex = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
        B.add_math(
            tp, "Medium", bp,
            f"In a function table for {ctx_en}, inputs {m(f'x = {xs[0]}, {xs[1]}, {xs[2]}')} produce outputs {m(f'y = {ys[0]}, {ys[1]}, {ys[2]}')}. What is the output {m('y')} when {m(f'x = {xs[3]}')}?",
            f"في جدول دالة خطية لـ ({ctx_ar})، تعطي المدخلات {m(f'x = {xs[0]}، {xs[1]}، {xs[2]}')} المخرجات {m(f'y = {ys[0]}، {ys[1]}، {ys[2]}')}. ما قيمة المخرجة {m('y')} عند المدخلة {m(f'x = {xs[3]}')}؟",
            ans, [ans - a, ans + abs(b), a * xs[3]],
            f"Find the linear rule y = {rule_tex} from the first three pairs, then plug in x = {xs[3]}.",
            f"استنتج قاعدة الدالة y = {rule_tex} من الأزواج الثلاثة الأولى ثم عوّض عن x = {xs[3]}.",
            f"Identify the rule {m(f'y = {rule_tex}')} and evaluate at {m(f'x = {xs[3]}')}.",
            [
                f"Check the change: each unit increase in {m('x')} adds {m(a)} to {m('y')}, giving {m(f'y = {rule_tex}')}.",
                f"Substitute {m(f'x = {xs[3]}')}: {m(f'y = {a}({xs[3]}) + ({b}) = {ans}')}.",
            ],
            f"Testing {m(f'x = {xs[2]}')} gives {m(f'{a}({xs[2]}) + ({b}) = {ys[2]}')}, matching the table.",
            f"نكتشف قاعدة الجدول {m(f'y = {rule_tex}')} ثم نعوّض {m(f'x = {xs[3]}')}.",
            [
                f"قاعدة الدالة هي {m(f'y = {rule_tex}')}.",
                f"عند {m(f'x = {xs[3]}')} نجد {m(f'y = {ans}')}.",
            ],
            f"التحقق على المدخلات السابقة يؤكد صحة القاعدة والناتج {m(ans)}.",
            diagram_en=svg_nafes_function_table(
                ["x"] + [str(v) for v in xs],
                [["y", str(ys[0]), str(ys[1]), str(ys[2]), "?"]],
                highlight_cell=(0, 4),
            ),
        )

    # 5 Hard: Finding the n-th term of an arithmetic pattern or working backwards for input x
    hard_fn = [
        ("nth", "matchstick square strip", "نمط مربعات أعواد الثقاب", 3, 1, 15),   # 3n + 1 at n=15 -> 46
        ("nth", "mosaic hexagon border", "إطار فسيفساء سداسي", 4, 2, 12),          # 4n + 2 at n=12 -> 50
        ("nth", "auditorium row seating", "مقاعد صفوف المسرح", 5, 10, 14),          # 5n + 10 at n=14 -> 80
        ("inv", 4, 5, 53, "Taif rose basket order", "طلبية سلال ورد الطائف"),      # 4x + 5 = 53 -> x = 12
        ("inv", 6, -7, 47, "Qassim solar sensor log", "سجل حسّاس شمسي بالقصيم"),   # 6x - 7 = 47 -> x = 9
    ]
    for row in hard_fn:
        if row[0] == "nth":
            _, ctx_en, ctx_ar, a, b, n_idx = row
            t1, t2, t3 = a + b, 2 * a + b, 3 * a + b
            ans = a * n_idx + b
            B.add_math(
                tp, "Hard", bp,
                f"In a {ctx_en}, Figure 1 uses {m(t1)} pieces, Figure 2 uses {m(t2)} pieces, and Figure 3 uses {m(t3)} pieces. Following this linear pattern, how many pieces are in **Figure {m(n_idx)}**?",
                f"في ({ctx_ar})، يتكوّن الشكل (1) من {m(t1)} قطعة، والشكل (2) من {m(t2)} قطعة، والشكل (3) من {m(t3)} قطعة. استمراراً على هذا النمط، كم قطعة في **الشكل ({m(n_idx)})**؟",
                ans, [t1 * n_idx, ans - a, ans + a],
                f"Write the rule {a}n + {b} (adding {a} each step) rather than multiplying {t1} × {n_idx}!",
                f"اكتب قاعدة الحد النوني {a}n + {b} (بزيادة {a} في كل خطوة) ولا تضرب {t1} × {n_idx}!",
                f"Use the n-th term formula {m(f'T_n = {a}n + {b}')} for {m(f'n = {n_idx}')}.",
                [
                    f"Each step adds {m(a)} pieces, and at {m('n = 1')} we have {m(f'{a}(1) + {b} = {t1}')}.",
                    f"For {m(f'n = {n_idx}')}: {m(f'{a}({n_idx}) + {b} = {ans}')} pieces.",
                ],
                f"Checks: {m(f'T_1 = {t1},\\; T_2 = {t2},\\; T_3 = {t3}')}.",
                f"نكتب الصيغة العامة للحد النوني {m(f'{a}n + {b}')} ثم نعوّض {m(f'n = {n_idx}')}.",
                [
                    f"يزداد النمط بمقدار {m(a)} في كل شكل، والقاعدة هي {m(f'{a}n + {b}')}.",
                    f"في الشكل رقم {m(n_idx)}: {m(f'{a}({n_idx}) + {b} = {ans}')} قطعة.",
                ],
                f"التحقق عند {m('n = 1, 2, 3')} يطابق حدود النمط تماماً.",
                diagram_en=svg_nafes_function_table(["Figure n", "1", "2", "3", str(n_idx)], [["Pieces", str(t1), str(t2), str(t3), "?"]], highlight_cell=(0, 4)),
            )
        else:
            _, a, b, y_target, ctx_en, ctx_ar = row
            ans = (y_target - b) // a
            rule_tex = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
            B.add_math(
                tp, "Hard", bp,
                f"A {ctx_en} uses the function rule {m(f'y = {rule_tex}')}. Which **input** value {m('x')} produces the output {m(f'y = {y_target}')}?",
                f"يستعمل ({ctx_ar}) قاعدة الدالة {m(f'y = {rule_tex}')}. ما قيمة **المدخلة** {m('x')} التي تعطي المخرجة {m(f'y = {y_target}')}؟",
                ans, [ans + 2, ans - 2, a * y_target + b],
                f"Work backwards on y = {rule_tex}: undo the constant term first, then divide by {a}.",
                f"اعمل عكسياً في القاعدة y = {rule_tex}: تخلص من الثابت أولاً ثم اقسم على {a}.",
                f"Solve {m(f'{rule_tex} = {y_target}')} for {m('x')}.",
                [
                    f"Set {m(f'{rule_tex} = {y_target}')} so {m(f'{a}x = {y_target - b}')}.",
                    f"Divide by {m(a)}: {m(f'x = {(y_target - b) // a}')}.",
                ],
                f"{m(f'{a}({ans}) + ({b}) = {y_target}')}.",
                f"نحل المعادلة العكسية {m(f'{rule_tex} = {y_target}')} لإيجاد {m('x')}.",
                [
                    f"نجعل {m(f'{a}x = {y_target - b}')}.",
                    f"بقسمة الطرفين على {m(a)} نجد {m(f'x = {ans}')}.",
                ],
                f"التعويض يعطي {m(f'y = {y_target}')} تماماً.",
                diagram_en=svg_function_machine("x = ?", f"× {a}", f"{'+' if b > 0 else '−'} {abs(b)}", str(y_target)),
            )


def _add_alg_04(B: G6BankBuilder) -> None:
    tp, bp = "Algebra", "G6-ALG-04"
    # 5 Easy: One-step equations (x + a = b, x - a = b, ax = c, x/a = b)
    easy_eq = [
        ("add", 19, 46, "x + 19 = 46", "library books borrowed", "كتب مستعارة"),
        ("sub", 14, 38, "y - 14 = 38", "remaining date palms", "نخلات باقية"),
        ("mul", 8, 96, "8m = 96", "equal box weights", "أوزان صناديق متساوية"),
        ("div", 6, 9, "\\frac{k}{6} = 9", "marbles shared per tray", "كرات في كل صينية"),
        ("add", 27, 65, "n + 27 = 65", "points in round two", "نقاط الجولة الثانية"),
    ]
    for kind, a, b, eq_tex, ctx_en, ctx_ar in easy_eq:
        ans = (b - a) if kind == "add" else (b + a) if kind == "sub" else (b // a) if kind == "mul" else (a * b)
        dists = [b + a if kind == "add" else b - a, ans + 4, max(2, ans - 5)]
        B.add_math(
            tp, "Easy", bp,
            f"In a problem about {ctx_en}, what is the solution to the one-step equation {m(eq_tex)}?",
            f"في مسألة حول ({ctx_ar})، ما حل معادلة الخطوة الواحدة {m(eq_tex)}؟",
            ans, dists,
            "Apply the inverse operation to both sides of the equation to isolate the variable.",
            "استعمل العملية العكسية في طرفي المعادلة لعزل المتغير.",
            "Undo the single operation using its inverse.",
            [
                f"Start with {m(eq_tex)} and apply the inverse operation to both sides.",
                f"This isolates the variable with value {m(ans)}.",
            ],
            f"Substituting {m(ans)} back into {m(eq_tex)} makes both sides equal.",
            "نطبّق العملية العكسية على طرفي المعادلة لإيجاد قيمة المتغير.",
            [
                f"بعزل المتغير في المعادلة {m(eq_tex)} نحصل على القيمة {m(ans)}.",
            ],
            f"التعويض بالقيمة {m(ans)} يحقق تساوي طرفي المعادلة.",
            diagram_en=svg_balance_scales(1, 3, 2, 4),
        )

    # 5 Medium: Simple two-step equations ax + b = c & ax - b = c
    med_eq = [
        (4, 9, 45, "4x + 9 = 45", "Riyadh robotics kits", "حقائب الروبوت"),
        (5, -8, 37, "5y - 8 = 37", "Jeddah museum passes", "بطاقات المتحف"),
        (6, 11, 53, "6m + 11 = 53", "Dammam sports cones", "أقماع التدريب"),
        (3, -10, 29, "3k - 10 = 29", "Abha honey jars", "عبوات العسل"),
        (7, 6, 62, "7p + 6 = 62", "Madinah calligraphy pens", "أقلام الخط العربي"),
    ]
    for a, b, c, eq_tex, ctx_en, ctx_ar in med_eq:
        ans = (c - b) // a
        B.add_math(
            tp, "Medium", bp,
            f"A Grade 6 word problem about {ctx_en} leads to the equation {m(eq_tex)}. What is the value of the unknown?",
            f"تؤدي مسألة لفظية حول ({ctx_ar}) إلى المعادلة {m(eq_tex)}. ما قيمة المجهول؟",
            ans, [(c + b) // a if (c + b) % a == 0 else ans + 3, ans - 2, c - abs(b)],
            f"Undo the constant ({'+' if b > 0 else '−'}{abs(b)}) first, then divide both sides by {a}.",
            f"تخلص من الثابت أولاً بالعملية العكسية، ثم اقسم الطرفين على {a}.",
            f"Isolate the variable term {m(f'{a}x')}, then divide by {m(a)}.",
            [
                f"Combine constants on the right: {m(f'{a} \\cdot (\\text{{var}}) = {c - b}')}.",
                f"Divide by {m(a)}: value = {m(ans)}.",
            ],
            f"{m(f'{a}({ans}) + ({b}) = {c}')}.",
            f"نتخلص من الحد الثابت أولاً ثم نقسم الطرفين على المعامل {m(a)}.",
            [
                f"بعد نقل الثابت بعكس إشارته يصبح الطرف الأيمن {m(c - b)}.",
                f"بالقسمة على {m(a)} نجد قيمة المجهول {m(ans)}.",
            ],
            f"التعويض يعطي {m(f'{a}({ans}) + ({b}) = {c}')}.",
            diagram_en=svg_balance_scales(3, 5, 1, 3),
        )

    # 5 Hard: Balance-scale substitution & multi-step equation word problems
    hard_eq = [
        ("scale", 2, 3, 24, "science lab balance", "ميزان مختبر العلوم"),       # 2 spheres = 3 cubes; 1 cube = 8g -> 1 sphere = 12g
        ("scale", 3, 2, 18, "goldsmith pan balance", "ميزان الصائغ"),           # 3 spheres = 2 cubes; 1 cube = 27g -> wait: 2*27=54/3=18! Let's make cube_w explicit!
        ("word", "Tarek", "طارق", 4, 14, 78, "storybooks", "قصص"),              # 4b + 14 = 78 -> b = 16
        ("word", "Huda", "هدى", 5, 18, 93, "watercolor tubes", "أنابيب ألوان"),  # 5b + 18 = 93 -> b = 15
        ("word", "Nasser", "ناصر", 6, 15, 87, "badminton shuttles", "ريش تنس"),  # 6b + 15 = 87 -> b = 12
    ]
    for row in hard_eq:
        if row[0] == "scale":
            _, n_cir, n_sq, sq_mass, ctx_en, ctx_ar = row
            tot_mass = n_sq * sq_mass
            ans = tot_mass // n_cir
            B.add_math(
                tp, "Hard", bp,
                f"On a balanced {ctx_en}, {m(n_cir)} identical orange spheres balance {m(n_sq)} green cubes. If each green cube has a mass of {m(sq_mass)} grams, what is the mass of **one orange sphere** in grams?",
                f"على ({ctx_ar}) متوازن، تتعادل {m(n_cir)} كرات برتقالية متماثلة مع {m(n_sq)} مكعبات خضراء. إذا كانت كتلة كل مكعب أخضر {m(sq_mass)} جراماً، فما كتلة **الكرة البرتقالية الواحدة** بالجرام؟",
                ans, [sq_mass, tot_mass, ans + 6],
                f"Multiply {n_sq} × {sq_mass} g to find the total mass on the right pan, then divide by {n_cir} spheres.",
                f"اضرب {n_sq} × {sq_mass} جم لإيجاد الكتلة الكلية في كفة المكعبات، ثم اقسم على {n_cir} كرات.",
                f"Set up the balance equation {m(f'{n_cir}s = {n_sq} \\times {sq_mass}')} and solve for {m('s')}.",
                [
                    f"Right-pan mass: {m(f'{n_sq} \\times {sq_mass} = {tot_mass}')} g.",
                    f"Divide equally among {m(n_cir)} spheres: {m(f's = {tot_mass} \\div {n_cir} = {ans}')} g.",
                ],
                f"{m(f'{n_cir} \\times {ans} = {tot_mass}')} g matches {m(f'{n_sq} \\times {sq_mass} = {tot_mass}')} g.",
                f"نكتب معادلة الاتزان {m(f'{n_cir}s = {tot_mass}')} ثم نقسم على {m(n_cir)}.",
                [
                    f"الكتلة الكلية للمكعبات: {m(f'{n_sq} \\times {sq_mass} = {tot_mass}')} جم.",
                    f"كتلة الكرة الواحدة: {m(f'{tot_mass} \\div {n_cir} = {ans}')} جم.",
                ],
                f"الكفتان متساويتان بكتلة {m(tot_mass)} جم في كلٍّ منهما.",
                diagram_en=svg_balance_scales(n_cir, n_sq, 1, 2),
            )
        else:
            _, name_en, name_ar, n_boxes, loose, total_cnt, item_en, item_ar = row
            ans = (total_cnt - loose) // n_boxes
            B.add_math(
                tp, "Hard", bp,
                f"{name_en} bought {m(n_boxes)} identical boxes of {item_en} plus {m(loose)} single {item_en}, getting {m(total_cnt)} {item_en} altogether. How many {item_en} are in **each box**?",
                f"اشترى/اشترت {name_ar} عدد {m(n_boxes)} علب متماثلة من ({item_ar}) بالإضافة إلى {m(loose)} قطعة مفردة، فكان المجموع الكلي {m(total_cnt)}. كم قطعة في **العلبة الواحدة**؟",
                ans, [(total_cnt + loose) // n_boxes if (total_cnt + loose) % n_boxes == 0 else ans + 3, total_cnt // n_boxes, ans - 2],
                f"Write {n_boxes}x + {loose} = {total_cnt}, subtract {loose} first, and divide by {n_boxes}.",
                f"اكتب المعادلة {n_boxes}x + {loose} = {total_cnt}، اطرح {loose} أولاً ثم اقسم على {n_boxes}.",
                f"Model the purchase with {m(f'{n_boxes}x + {loose} = {total_cnt}')} and solve.",
                [
                    f"Subtract the {m(loose)} loose items: {m(f'{n_boxes}x = {total_cnt} - {loose} = {total_cnt - loose}')}.",
                    f"Divide by {m(n_boxes)} boxes: {m(f'x = {ans}')}.",
                ],
                f"{m(f'{n_boxes} \\times {ans} + {loose} = {total_cnt}')}.",
                f"نترجم المسألة إلى المعادلة {m(f'{n_boxes}x + {loose} = {total_cnt}')} ونحلها.",
                [
                    f"نطرح القطع المفردة: {m(f'{n_boxes}x = {total_cnt - loose}')}.",
                    f"نقسم على {m(n_boxes)}: {m(f'x = {ans}')} في كل علبة.",
                ],
                f"التحقق: {m(f'{n_boxes} \\times {ans} + {loose} = {total_cnt}')}.",
                diagram_en=svg_balance_scales(min(4, n_boxes), 4, 2, 4),
            )


def _add_geo_01(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-01"
    # 5 Easy: Direct metric unit conversions (mm, cm, m, km; mg, g, kg; mL, L)
    easy_met = [
        ("4.6", "km", "m", 4600, [460, 46000, 4060], "multiply by 1000", "الضرب في 1000", "Riyadh cornice jog", "ممشى بالرياض"),
        ("3500", "mL", "L", "3.5", ["35", "0.35", "305"], "divide by 1000", "القسمة على 1000", "Zamzam water flask", "عبوة ماء زمزم"),
        ("2.75", "kg", "g", 2750, [275, 27500, 2075], "multiply by 1000", "الضرب في 1000", "sack of Basmati rice", "كيس أرز بسمتي"),
        ("84", "mm", "cm", "8.4", ["0.84", "840", "8.04"], "divide by 10", "القسمة على 10", "beetle specimen in biology", "عينة حشرة في العلوم"),
        ("6.3", "m", "cm", 630, [63, 6300, 603], "multiply by 100", "الضرب في 100", "classroom smartboard wall", "جدار فصل دراسي"),
    ]
    for val_s, u_in, u_out, ans, dists, rule_en, rule_ar, ctx_en, ctx_ar in easy_met:
        B.add_math(
            tp, "Easy", bp,
            f"A measurement for a {ctx_en} is {m(f'{val_s}\\text{{ {u_in}}}')}. What is this measurement in **{u_out}**?",
            f"سُجّل قياس لـ ({ctx_ar}) بمقدار {m(f'{val_s}\\text{{ {u_in}}}')}. كم يساوي هذا القياس بوحدة **({u_out})**؟",
            ans, dists,
            f"To convert from {u_in} to {u_out}, {rule_en}.",
            f"للتحويل من ({u_in}) إلى ({u_out}) نستعمل {rule_ar}.",
            f"Convert {m(f'{val_s}\\text{{ {u_in}}}')} to {u_out} by applying the metric factor.",
            [
                f"Apply the metric conversion ({rule_en}) to {m(val_s)}.",
                f"This gives {m(ans)} {u_out}.",
            ],
            f"Reversing the conversion returns {m(f'{val_s}\\text{{ {u_in}}}')}.",
            f"نحوّل {m(f'{val_s}\\text{{ {u_in}}}')} إلى ({u_out}) باستعمال ({rule_ar}).",
            [
                f"بتطبيق قاعدة التحويل نحصل على {m(ans)} ({u_out}).",
            ],
            f"التحويل العكسي يعيد القياس الأصلي {m(f'{val_s}\\text{{ {u_in}}}')}.",
            diagram_en=svg_fenceposts(f"1 unit rule", f"{val_s} {u_in} = ? {u_out}"),
        )

    # 5 Medium: Elapsed time across hour boundaries
    med_time = [
        (8, 35, 10, 20, "science lab session", "حصة مختبر العلوم"),       # 25 + 60 + 20 = 105 min
        (9, 45, 11, 15, "Diriyah guided tour", "جولة إرشادية بالدرعية"),  # 15 + 60 + 15 = 90 min
        (10, 25, 12, 10, "Jeddah boat excursion", "رحلة بحرية بجدة"),     # 35 + 60 + 10 = 105 -> let's make 12:05 -> 100 min!
        (2, 50, 4, 35, "after-school robotics club", "نادي الروبوت المسائي"),
        (7, 40, 9, 55, "morning sports tournament", "بطولة رياضية صباحية"),
    ]
    med_time[2] = (10, 25, 12, 5, "Jeddah boat excursion", "رحلة بحرية بجدة")
    for h1, m1, h2, m2, ctx_en, ctx_ar in med_time:
        ans = (h2 - h1) * 60 + (m2 - m1)
        t1_s, t2_s = f"{h1:02d}:{m1:02d}", f"{h2:02d}:{m2:02d}"
        B.add_math(
            tp, "Medium", bp,
            f"A {ctx_en} begins at {m(t1_s)} and finishes at {m(t2_s)} (same half of the day). How many **minutes** did it last?",
            f"بدأت ({ctx_ar}) عند الساعة {m(t1_s)} وانتهت عند الساعة {m(t2_s)}. كم **دقيقة** استغرقت؟",
            ans, [ans - 40, ans + 15, (h2 - h1) * 100 + (m2 - m1)],
            f"Count minutes from {t1_s} to {h1+1:02d}:00 first (remember 1 hour = 60 minutes, NOT 100!).",
            f"احسب الدقائق المتبقية حتى الساعة {h1+1:02d}:00 أولاً (تذكّر أن الساعة 60 دقيقة وليست 100!).",
            "Bridge to the next whole hour, then add full hours and remaining minutes.",
            [
                f"From {m(t1_s)} to {m(f'{h1+1:02d}:00')} is {m(60 - m1)} minutes.",
                f"From {m(f'{h1+1:02d}:00')} to {m(t2_s)} is {m((h2 - h1 - 1) * 60 + m2)} minutes.",
                f"Total elapsed time = {m(f'{60 - m1} + {(h2 - h1 - 1) * 60 + m2} = {ans}')} minutes.",
            ],
            f"{m(ans)} minutes = {m(ans // 60)} h {m(ans % 60)} min, landing at {m(t2_s)}.",
            "نكمّل الدقائق إلى الساعة التالية ثم نضيف الساعات الكاملة والدقائق المتبقية.",
            [
                f"من {m(t1_s)} إلى {m(f'{h1+1:02d}:00')} توجد {m(60 - m1)} دقيقة.",
                f"ومن {m(f'{h1+1:02d}:00')} إلى {m(t2_s)} توجد {m((h2 - h1 - 1) * 60 + m2)} دقيقة، فالمجموع {m(ans)} دقيقة.",
            ],
            f"إضافة {m(ans)} دقيقة إلى {m(t1_s)} توصلنا إلى {m(t2_s)} بالضبط.",
            diagram_en=svg_nafes_analog_clock(h1, m1, f"{t1_s} -> {t2_s}"),
        )

    # 5 Hard: Multi-step mixed metric arithmetic (L & mL, km & m, kg & g)
    hard_met = [
        ("jug", "dispenses juice at a Taif festival", "موزّع عصير في مهرجان الطائف", "4.5", "L", 12, 250, "mL", 1500),
        ("jug", "dispenses lab distilled water", "وعاء ماء مقطر في المختبر", "6", "L", 15, 300, "mL", 1500),
        ("mass", "shipping box in Dammam", "صندوق شحن بالدمام", "5.2", "kg", 3, 850, "g", 2650),
        ("len", "fiber-optic spool in Jubail", "بكرة ألياف ضوئية بالجبيل", "2.8", "km", 4, 450, "m", 1000),
        ("mass", "spice sack in Qassim", "كيس بهارات بالقصيم", "3.6", "kg", 6, 420, "g", 1080),
    ]
    for _, ctx_en, ctx_ar, tot_s, big_u, cnt, each_v, sm_u, ans in hard_met:
        tot_sm = int(round(float(tot_s) * 1000))
        used_sm = cnt * each_v
        assert tot_sm - used_sm == ans
        B.add_math(
            tp, "Hard", bp,
            f"A container ({ctx_en}) starts with {m(f'{tot_s}\\text{{ {big_u}}}')}. After removing {m(cnt)} portions of {m(f'{each_v}\\text{{ {sm_u}}}')} each, how many **{sm_u}** remain?",
            f"يبدأ ({ctx_ar}) بكمية قدرها {m(f'{tot_s}\\text{{ {big_u}}}')}. بعد أخذ {m(cnt)} حصص مقدار كلٍّ منها {m(f'{each_v}\\text{{ {sm_u}}}')}، كم **({sm_u})** يبقى؟",
            ans, [used_sm, abs(tot_sm // 10 - used_sm), ans + each_v],
            f"Convert {tot_s} {big_u} into {sm_u} (× 1000 = {tot_sm} {sm_u}) first, then subtract {cnt} × {each_v}.",
            f"حوّل {tot_s} ({big_u}) إلى ({sm_u}) بالضرب في 1000 أولاً ({tot_sm})، ثم اطرح {cnt} × {each_v}.",
            f"Unify all units to {sm_u}, then subtract total amount used.",
            [
                f"Convert start amount: {m(f'{tot_s} \\times 1000 = {tot_sm}\\text{{ {sm_u}}}')}.",
                f"Amount removed: {m(f'{cnt} \\times {each_v} = {used_sm}\\text{{ {sm_u}}}')}.",
                f"Remaining: {m(f'{tot_sm} - {used_sm} = {ans}\\text{{ {sm_u}}}')}.",
            ],
            f"{m(f'{used_sm} + {ans} = {tot_sm}\\text{{ {sm_u}}} = {tot_s}\\text{{ {big_u}}}')}.",
            f"نوحّد الوحدات بالتحويل إلى ({sm_u}) ثم نطرح الكمية المسحوبة.",
            [
                f"الكمية الكلية: {m(f'{tot_s} \\times 1000 = {tot_sm}\\text{{ {sm_u}}}')}.",
                f"الكمية المسحوبة: {m(f'{cnt} \\times {each_v} = {used_sm}')}، والباقي {m(f'{tot_sm} - {used_sm} = {ans}\\text{{ {sm_u}}}')}.",
            ],
            f"مجموع المسحوب والباقي يعيد {m(tot_sm)} ({sm_u}).",
            diagram_en=svg_two_jars(f"{tot_s} {big_u}", 0.9, f"{cnt}×{each_v} {sm_u}", 0.52, "Left = ?"),
        )


def _add_geo_02(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-02"
    # 5 Easy: Area of parallelograms (A = bh) & triangles (A = 1/2 bh)
    easy_ar = [
        ("para", 15, 8, 10, "decorative tile in Diriyah", "بلاطة زخرفية بالدرعية"),
        ("tri", 18, 11, 0, "pennant flag at school sports day", "راية مثلثة في اليوم الرياضي"),
        ("para", 14, 9, 11, "solar reflector panel", "لوح عاكس شمسي"),
        ("tri", 22, 10, 0, "garden corner bed in Abha", "حوض زهور مثلث بأبها"),
        ("tri", 16, 13, 0, "museum glass gable", "واجهة زجاجية مثلثة"),
    ]
    for kind, b, h, sl, ctx_en, ctx_ar in easy_ar:
        if kind == "para":
            ans = b * h
            B.add_math(
                tp, "Easy", bp,
                f"A parallelogram ({ctx_en}) has base {m(f'{b}\\text{{ cm}}')}, perpendicular height {m(f'{h}\\text{{ cm}}')}, and slant side {m(f'{sl}\\text{{ cm}}')}. What is its **area** in {m('\\text{cm}^2')}?",
                f"متوازي أضلاع يمثّل ({ctx_ar}) طول قاعدته {m(f'{b}\\text{{ سم}}')} وارتفاعه العمودي {m(f'{h}\\text{{ سم}}')} وضلعه المائل {m(f'{sl}\\text{{ سم}}')}. ما **مساحته** بـ {m('\\text{سم}^2')}؟",
                ans, [b * sl, 2 * (b + sl), (b * h) // 2],
                "Use A = b × h with the perpendicular height, NOT the slant side!",
                "استعمل قانون مساحة متوازي الأضلاع م = ق × ع بالارتفاع العمودي وليس الضلع المائل!",
                f"Multiply base {m(b)} by perpendicular height {m(h)}.",
                [
                    f"Ignore the slant side {m(sl)} cm when computing area.",
                    f"{m(f'A = b \\times h = {b} \\times {h} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"{m(f'{b} \\times {h} = {ans}\\text{{ cm}}^2')}.",
                f"نضرب القاعدة {m(b)} في الارتفاع العمودي {m(h)} ونتجاهل الضلع المائل.",
                [
                    f"المساحة {m(f'A = {b} \\times {h} = {ans}\\text{{ سم}}^2')}.",
                ],
                f"حاصل ضرب القاعدة في الارتفاع العمودي يساوي {m(ans)}.",
                diagram_en=svg_g6_parallelogram(f"b = {b} cm", f"h = {h} cm", f"{sl} cm"),
            )
        else:
            ans = (b * h) // 2
            B.add_math(
                tp, "Easy", bp,
                f"A triangle ({ctx_en}) has base {m(f'{b}\\text{{ cm}}')} and perpendicular height {m(f'{h}\\text{{ cm}}')}. What is its **area** in {m('\\text{cm}^2')}?",
                f"مثلث يمثّل ({ctx_ar}) طول قاعدته {m(f'{b}\\text{{ سم}}')} وارتفاعه العمودي {m(f'{h}\\text{{ سم}}')}. ما **مساحته** بـ {m('\\text{سم}^2')}؟",
                ans, [b * h, b + h, ans + b],
                "Remember the 1/2 in the triangle area formula: A = 1/2 × b × h.",
                "تذكّر الضرب في النصف في قانون مساحة المثلث: م = 1/2 × ق × ع.",
                f"Compute {m(f'\\frac{{1}}{{2}} \\times {b} \\times {h}')}.",
                [
                    f"{m(f'A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"Doubling {m(ans)} gives {m(b * h)}, matching {m(f'{b} \\times {h}')}.",
                "نطبّق قانون مساحة المثلث: نصف طول القاعدة في الارتفاع.",
                [
                    f"{m(f'A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {ans}\\text{{ سم}}^2')}.",
                ],
                f"ضعف المساحة يساوي {m(b * h)} وهو حاصل ضرب القاعدة في الارتفاع.",
                diagram_en=svg_shaded_triangle_in_rect(b, h, 0.5, "cm"),
            )

    # 5 Medium: Finding missing height/base given area, or parallelogram perimeter
    med_ar = [
        ("tri_h", 84, 14, "triangular sail in Jeddah", "شراع مثلث في جدة"),      # h = 2*84/14 = 12
        ("tri_h", 108, 18, "triangular roof truss", "جملون سقف مثلث"),            # h = 2*108/18 = 12 -> let's use A=99, b=18 -> h=11!
        ("para_h", 156, 13, "parallelogram plaza in Riyadh", "ساحة على شكل متوازي أضلاع"),  # h = 12
        ("para_p", 17, 11, 9, "parallelogram flowerbed", "حوض زهور متوازي أضلاع"), # P = 2*(17+11)=56
        ("tri_h", 96, 16, "triangular traffic sign model", "نموذج لوحة مرورية مثلثة"),
    ]
    med_ar[1] = ("tri_h", 99, 18, "triangular roof truss", "جملون سقف مثلث")
    for row in med_ar:
        if row[0] == "tri_h":
            _, area_v, base_v, ctx_en, ctx_ar = row
            ans = (2 * area_v) // base_v
            B.add_math(
                tp, "Medium", bp,
                f"A {ctx_en} has area {m(f'{area_v}\\text{{ cm}}^2')} and base {m(f'{base_v}\\text{{ cm}}')}. What is its perpendicular **height** in cm?",
                f"تبلغ مساحة ({ctx_ar}) {m(f'{area_v}\\text{{ سم}}^2')} وطول قاعدته {m(f'{base_v}\\text{{ سم}}')}. فما **ارتفاعه العمودي** بالسنتيمتر؟",
                ans, [area_v // base_v or ans - 4, ans + 4, 2 * ans],
                f"Since A = 1/2 bh, multiply the area {area_v} by 2 FIRST, then divide by {base_v}!",
                f"بما أن م = 1/2 ق ع، اضرب المساحة {area_v} في 2 أولاً ثم اقسم على القاعدة {base_v}!",
                f"Use {m(f'h = \\frac{{2A}}{{b}}')} to solve for the triangle's height.",
                [
                    f"Double the area: {m(f'2 \\times {area_v} = {2 * area_v}')}.",
                    f"Divide by base {m(base_v)}: {m(f'h = {2 * area_v} \\div {base_v} = {ans}\\text{{ cm}}')}.",
                ],
                f"{m(f'\\frac{{1}}{{2}} \\times {base_v} \\times {ans} = {area_v}\\text{{ cm}}^2')}.",
                f"نضرب المساحة في 2 ثم نقسم على طول القاعدة {m(base_v)}.",
                [
                    f"نكتب: {m(f'h = \\frac{{2 \\times {area_v}}}{{{base_v}}} = {ans}\\text{{ سم}}')}.",
                ],
                f"التحقق: {m(f'\\frac{{1}}{{2}} \\times {base_v} \\times {ans} = {area_v}')}.",
                diagram_en=svg_shaded_triangle_in_rect(base_v, ans, 0.58, "cm", w_lbl="h = ? cm"),
            )
        elif row[0] == "para_h":
            _, area_v, base_v, ctx_en, ctx_ar = row
            ans = area_v // base_v
            B.add_math(
                tp, "Medium", bp,
                f"A {ctx_en} covers an area of {m(f'{area_v}\\text{{ m}}^2')} with base {m(f'{base_v}\\text{{ m}}')}. What is its perpendicular **height** in meters?",
                f"تبلغ مساحة ({ctx_ar}) {m(f'{area_v}\\text{{ م}}^2')} وطول قاعدتها {m(f'{base_v}\\text{{ م}}')}. ما **ارتفاعها العمودي** بالأمتار؟",
                ans, [2 * ans, ans - 3, ans + 5],
                f"For a parallelogram, A = b × h, so divide {area_v} directly by {base_v}.",
                f"في متوازي الأضلاع م = ق × ع، لذا اقسم {area_v} مباشرة على {base_v}.",
                f"Divide area {m(area_v)} by base {m(base_v)}.",
                [
                    f"{m(f'h = A \\div b = {area_v} \\div {base_v} = {ans}\\text{{ m}}')}.",
                ],
                f"{m(f'{base_v} \\times {ans} = {area_v}\\text{{ m}}^2')}.",
                f"نقسم المساحة {m(area_v)} على طول القاعدة {m(base_v)}.",
                [
                    f"الارتفاع العمودي {m(f'h = {area_v} \\div {base_v} = {ans}\\text{{ م}}')}.",
                ],
                f"التحقق: {m(f'{base_v} \\times {ans} = {area_v}')}.",
                diagram_en=svg_g6_parallelogram(f"b = {base_v} m", "h = ? m"),
            )
        else:
            _, b, sl, h, ctx_en, ctx_ar = row
            ans = 2 * (b + sl)
            B.add_math(
                tp, "Medium", bp,
                f"A {ctx_en} has base {m(f'{b}\\text{{ m}}')}, slant side {m(f'{sl}\\text{{ m}}')}, and height {m(f'{h}\\text{{ m}}')}. What is its **perimeter** in meters?",
                f"({ctx_ar}) طول قاعدته {m(f'{b}\\text{{ م}}')} وضلعه المائل {m(f'{sl}\\text{{ م}}')} وارتفاعه العمودي {m(f'{h}\\text{{ م}}')}. ما **محيطه** بالأمتار؟",
                ans, [b * h, 2 * (b + h), b + sl],
                "Perimeter walks around the four outer sides: 2 × (base + slant side), ignoring the interior height!",
                "المحيط هو مجموع أطوال الأضلاع الخارجية الأربعة: 2 × (القاعدة + الضلع المائل) دون الارتفاع الداخلي!",
                f"Add the two adjacent outer side lengths ({b} and {sl}) and multiply by 2.",
                [
                    f"Outer sides are {m(b)} m and {m(sl)} m.",
                    f"{m(f'P = 2({b} + {sl}) = 2 \\times {b + sl} = {ans}\\text{{ m}}')}.",
                ],
                f"{m(f'{b} + {sl} + {b} + {sl} = {ans}\\text{{ m}}')}.",
                "نجمع ضلعين متجاورين من الإطار الخارجي ثم نضرب في 2.",
                [
                    f"المحيط {m(f'P = 2({b} + {sl}) = {ans}\\text{{ م}}')}.",
                ],
                f"مجموع الأضلاع الخارجية الأربعة يساوي {m(ans)} م.",
                diagram_en=svg_g6_parallelogram(f"b = {b} m", f"h = {h} m", f"{sl} m"),
            )

    # 5 Hard: Unshaded area around inscribed triangle & turf cost word problems
    hard_ar = [
        ("unsh", 20, 12, "courtyard in Al-Ula", "فناء مستطيل في العلا"),     # unshaded = 1/2 * 20 * 12 = 120
        ("unsh", 18, 14, "mosaic wall in Makkah", "جدار فسيفساء في مكة"),    # unshaded = 126
        ("cost_t", 16, 10, 25, "triangular lawn in Khobar", "مسطح أخضر مثلث بالخبر"),   # A=80, cost=2000
        ("cost_p", 12, 8, 15, "parallelogram walkway in Yanbu", "ممر متوازي أضلاع بينبع"), # A=96, cost=1440
        ("cost_t", 14, 9, 20, "triangular flowerbed in Taif", "حوض ورد مثلث بالطائف"),  # A=63, cost=1260
    ]
    for row in hard_ar:
        if row[0] == "unsh":
            _, L, W, ctx_en, ctx_ar = row
            ans = (L * W) // 2
            B.add_math(
                tp, "Hard", bp,
                f"A {m(f'{L}\\text{{ m}} \\times {W}\\text{{ m}}')} rectangular {ctx_en} contains a shaded triangle whose base is the full {m(f'{L}\\text{{ m}}')} bottom edge and whose apex touches the top edge. What is the area of the **unshaded** region in {m('\\text{m}^2')}?",
                f"بداخل ({ctx_ar}) أبعاده {m(f'{L}\\text{{ م}} \\times {W}\\text{{ م}}')} رُسم مثلث مظلّل قاعدته الضلع السفلي كاملاً ({m(f'{L}\\text{{ م}}')}) ورأسه على الضلع العلوي. ما مساحة المنطقة **غير المظلّلة** بـ {m('\\text{م}^2')}؟",
                ans, [L * W, ans // 2, L * W - L - W],
                "Find the rectangle area L × W and subtract the shaded triangle area 1/2 × L × W.",
                "احسب مساحة المستطيل (الطول × العرض) ثم اطرح منها مساحة المثلث المظلّل (1/2 × الطول × العرض).",
                "The shaded triangle occupies exactly half of the rectangle, leaving the other half unshaded.",
                [
                    f"Rectangle area = {m(f'{L} \\times {W} = {L * W}\\text{{ m}}^2')}.",
                    f"Shaded triangle area = {m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}\\text{{ m}}^2')}.",
                    f"Unshaded area = {m(f'{L * W} - {ans} = {ans}\\text{{ m}}^2')}.",
                ],
                f"Shaded {m(ans)} + unshaded {m(ans)} = {m(L * W)} {m('\\text{m}^2')}.",
                "مساحة المثلث المظلّل تساوي نصف مساحة المستطيل، فتبقى النصف الآخر غير مظلّل.",
                [
                    f"مساحة المستطيل = {m(f'{L} \\times {W} = {L * W}\\text{{ م}}^2')}.",
                    f"مساحة المثلث المظلّل = {m(ans)}، فتكون المساحة غير المظلّلة {m(f'{L * W} - {ans} = {ans}\\text{{ م}}^2')}.",
                ],
                f"مجموع المظلّل وغير المظلّل يساوي {m(L * W)} م².",
                diagram_en=svg_shaded_triangle_in_rect(L, W, 0.64, "m"),
            )
        else:
            kind, b, h, rate, ctx_en, ctx_ar = row
            area_v = (b * h) // 2 if kind == "cost_t" else b * h
            ans = area_v * rate
            B.add_math(
                tp, "Hard", bp,
                f"Landscaping a {ctx_en} (base {m(f'{b}\\text{{ m}}')}, perpendicular height {m(f'{h}\\text{{ m}}')}) costs {m(rate)} SAR per {m('\\text{m}^2')}. What is the **total cost** in SAR?",
                f"تبلغ تكلفة تجهيز ({ctx_ar}) الذي طول قاعدته {m(f'{b}\\text{{ م}}')} وارتفاعه العمودي {m(f'{h}\\text{{ م}}')} مبلغ {m(rate)} ريالاً لكل {m('\\text{م}^2')}. فما **التكلفة الكلية** بالريال؟",
                ans, [b * h * rate if kind == "cost_t" else (b * h // 2) * rate, area_v + rate, ans - rate * b],
                "First compute the exact area in m², then multiply by the price per m².",
                "احسب المساحة الدقيقة أولاً بالمتر المربع، ثم اضربها في سعر المتر المربع الواحد.",
                f"Find area = {m(area_v)} {m('\\text{m}^2')}, then multiply by {m(rate)} SAR.",
                [
                    f"Area = {m(f'{area_v}\\text{{ m}}^2')}.",
                    f"Total cost = {m(f'{area_v} \\times {rate} = {ans}')} SAR.",
                ],
                f"{m(f'{ans} \\div {rate} = {area_v}\\text{{ m}}^2')}.",
                "نوجد المساحة أولاً ثم نضرب في تكلفة المتر المربع.",
                [
                    f"المساحة تساوي {m(f'{area_v}\\text{{ م}}^2')}.",
                    f"التكلفة الكلية = {m(f'{area_v} \\times {rate} = {ans}')} ريالاً.",
                ],
                f"قسمة {m(ans)} على {m(rate)} تعيد المساحة {m(area_v)} م².",
                diagram_en=(svg_shaded_triangle_in_rect(b, h, 0.5, "m") if kind == "cost_t" else svg_g6_parallelogram(f"b = {b} m", f"h = {h} m")),
            )


def _add_geo_03(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-03"
    # 5 Easy: Circle radius/diameter & circumference using pi ≈ 22/7 or in terms of pi
    easy_cir = [
        ("diam", 9, 18, [9, 27, 81], "circular sundial in Riyadh", "مزولة شمسية دائرية"),
        ("circ22", 7, 44, [22, 88, 154], "round flowerbed in Taif", "حوض ورد دائري بالطائف"),
        ("circ22", 21, 132, [66, 84, 264], "running ring in Dammam", "مضمار دائري بالدمام"),
        ("circ_d22", 14, 44, [28, 88, 154], "heritage well rim in Diriyah", "حافة بئر تراثية بالدرعية"),
        ("circ_pi", 12, "24\\pi", ["12\\pi", "36\\pi", "144\\pi"], "observatory dome ring", "حلقة قبة مرصد فلكي"),
    ]
    for kind, val, ans, dists, ctx_en, ctx_ar in easy_cir:
        if kind == "diam":
            B.add_math(
                tp, "Easy", bp,
                f"A {ctx_en} has radius {m(f'r = {val}\\text{{ cm}}')}. What is its **diameter** in cm?",
                f"نصف قطر ({ctx_ar}) يساوي {m(f'r = {val}\\text{{ سم}}')}. ما طول **قطرها** بالسنتيمتر؟",
                ans, dists,
                "The diameter of any circle is twice its radius: d = 2r.",
                "قطر الدائرة يساوي مثلي نصف قطرها: ق = 2 نق.",
                f"Multiply radius {m(val)} by 2.",
                [f"{m(f'd = 2r = 2 \\times {val} = {ans}\\text{{ cm}}')}."],
                f"{m(f'{ans} \\div 2 = {val}\\text{{ cm}}')}.",
                "نضرب نصف القطر في 2.",
                [f"القطر {m(f'd = 2 \\times {val} = {ans}\\text{{ سم}}')}."],
                f"نصف القطر هو نصف الـ {m(ans)} أي {m(val)} سم.",
                diagram_en=svg_g6_circle(f"r = {val} cm", is_diameter=False),
            )
        elif kind in ("circ22", "circ_d22"):
            is_d = kind == "circ_d22"
            lbl = f"d = {val} m" if is_d else f"r = {val} m"
            B.add_math(
                tp, "Easy", bp,
                f"A {ctx_en} has {'diameter' if is_d else 'radius'} {m(f'{val}\\text{{ m}}')}. Using {m('\\pi \\approx \\frac{22}{7}')}, what is its **circumference** in meters?",
                f"{'قطر' if is_d else 'نصف قطر'} ({ctx_ar}) يساوي {m(f'{val}\\text{{ م}}')}. باستعمال {m('\\pi \\approx \\frac{22}{7}')}، ما **محيطها** بالأمتار؟",
                ans, dists,
                "Use C = πd (or C = 2πr when given the radius) with π = 22/7.",
                "استعمل قانون المحيط مح = ط ق (أو مح = 2 ط نق عند إعطاء نصف القطر) مع ط = 22/7.",
                f"Substitute into {'C = πd' if is_d else 'C = 2πr'} and cancel multiples of 7.",
                [
                    f"Evaluate circumference to obtain {m(f'C = {ans}\\text{{ m}}')}.",
                ],
                f"Ratio {m(f'C \\div d = {ans} \\div {val if is_d else 2*val} = \\frac{{22}}{{7}}')}.",
                "نعوّض في قانون محيط الدائرة ونختصر مع العدد 7.",
                [
                    f"المحيط {m(f'C = {ans}\\text{{ م}}')}.",
                ],
                f"قسمة المحيط على القطر تعطي {m('\\frac{22}{7}')}.",
                diagram_en=svg_g6_circle(lbl, is_diameter=is_d),
            )
        else:
            B.add_math(
                tp, "Easy", bp,
                f"An {ctx_en} has radius {m(f'r = {val}\\text{{ m}}')}. What is its circumference **in terms of {m('\\pi')}** (in meters)?",
                f"نصف قطر ({ctx_ar}) يساوي {m(f'r = {val}\\text{{ م}}')}. ما محيطها **بدلالة {m('\\pi')}** بالأمتار؟",
                ans, dists,
                "Use C = 2πr (do NOT square r—πr² is area!).",
                "استعمل مح = 2 ط نق (ولا تربّع نصف القطر لأن ط نق² قانون المساحة!).",
                f"Compute {m(f'2 \\times \\pi \\times {val}')}.",
                [f"{m(f'C = 2\\pi r = 2 \\times \\pi \\times {val} = {ans}')} m."],
                f"Diameter is {m(2 * val)} m, so {m(f'C = \\pi d = {ans}')}.",
                "نضرب نصف القطر في 2 بدلالة ط.",
                [f"المحيط {m(f'C = 2\\pi({val}) = {ans}')} م."],
                f"القطر {m(2 * val)} م والمحيط {m(ans)}.",
                diagram_en=svg_g6_circle(f"r = {val} m", is_diameter=False),
            )

    # 5 Medium: Area of L-shaped composite rectilinear figures
    med_comp = [
        (12, 10, 5, 4, "school science hall", "قاعة العلوم"),         # 5*10 + (12-5)*4 = 50 + 28 = 78
        (15, 11, 6, 5, "Jeddah exhibition booth", "جناح معرض بجدة"),  # 6*11 + 9*5 = 66 + 45 = 111
        (14, 9, 6, 4, "courtyard patio in Abha", "فناء منزلي بأبها"), # 6*9 + 8*4 = 54 + 32 = 86
        (16, 12, 7, 5, "library reading zone", "ركن القراءة بالمكتبة"), # 7*12 + 9*5 = 84 + 45 = 129
        (18, 10, 8, 4, "robotics arena floor", "أرضية حلبة الروبوت"),   # 8*10 + 10*4 = 80 + 40 = 120
    ]
    for tw, th, lw, rh, ctx_en, ctx_ar in med_comp:
        a1 = lw * th
        a2 = (tw - lw) * rh
        ans = a1 + a2
        B.add_math(
            tp, "Medium", bp,
            f"An L-shaped {ctx_en} has total bottom width {m(f'{tw}\\text{{ m}}')}, left vertical height {m(f'{th}\\text{{ m}}')}, top step width {m(f'{lw}\\text{{ m}}')}, and right wing height {m(f'{rh}\\text{{ m}}')}. What is its **total area** in {m('\\text{m}^2')}?",
            f"أرضية ({ctx_ar}) على شكل حرف L عرضها السفلي الكلي {m(f'{tw}\\text{{ م}}')} وارتفاعها الأيسر {m(f'{th}\\text{{ م}}')} وعرض جزئها العلوي {m(f'{lw}\\text{{ م}}')} وارتفاع جناحها الأيمن {m(f'{rh}\\text{{ م}}')}. ما **مساحتها الكلية** بـ {m('\\text{م}^2')}؟",
            ans, [tw * th, a1 + tw * rh, ans - lw],
            f"Split vertically into a {lw}×{th} left rectangle and a ({tw}−{lw})×{rh} right rectangle, then add their areas!",
            f"اقسم الشكل رأسياً إلى مستطيل أيسر أبعاده {lw}×{th} ومستطيل أيمن أبعاده ({tw}−{lw})×{rh} ثم اجمع مساحتيهما!",
            "Partition the L-shape into two non-overlapping rectangles and sum their areas.",
            [
                f"Left rectangle area: {m(f'{lw} \\times {th} = {a1}\\text{{ m}}^2')}.",
                f"Right wing width = {m(f'{tw} - {lw} = {tw - lw}')} m, so its area is {m(f'{tw - lw} \\times {rh} = {a2}\\text{{ m}}^2')}.",
                f"Total area = {m(f'{a1} + {a2} = {ans}\\text{{ m}}^2')}.",
            ],
            f"Subtracting the missing corner {m(f'({tw - lw})({th - rh}) = {(tw - lw) * (th - rh)}')} from {m(tw * th)} also gives {m(ans)}.",
            "نقسم الشكل المركب إلى مستطيلين غير متداخلين ونجمع مساحتيهما.",
            [
                f"مساحة المستطيل الأيسر: {m(f'{lw} \\times {th} = {a1}\\text{{ م}}^2')}.",
                f"عرض الجناح الأيمن {m(f'{tw} - {lw} = {tw - lw}')} م، ومساحته {m(f'{tw - lw} \\times {rh} = {a2}\\text{{ م}}^2')}.",
                f"المساحة الكلية: {m(f'{a1} + {a2} = {ans}\\text{{ م}}^2')}.",
            ],
            f"طرح الركن المقتطع من المستطيل الكامل يعطي {m(ans)} م² أيضاً.",
            diagram_en=svg_g6_composite_l(f"{tw} m", f"{th} m", f"{lw} m", f"{rh} m"),
        )

    # 5 Hard: Rectangle + triangle gable & finding radius from circumference
    hard_comp = [
        ("gable", 12, 7, 5, "heritage facade in Al-Ula", "واجهة مبنى تراثي بالعلا"),  # 84 + 30 = 114
        ("gable", 14, 8, 6, "greenhouse end wall in Qassim", "واجهة بيت محمي بالقصيم"), # 112 + 42 = 154
        ("gable", 10, 9, 4, "museum banner in Makkah", "لافتة متحف بمكة"),             # 90 + 20 = 110
        ("rev_c", 176, "circular plaza in Riyadh", "ساحة دائرية بالرياض"),             # r = 28
        ("rev_c", 220, "circular irrigation pivot in Hail", "محور ري دائري بحائل"),    # r = 35
    ]
    for row in hard_comp:
        if row[0] == "gable":
            _, w_b, h_r, h_t, ctx_en, ctx_ar = row
            a_rect = w_b * h_r
            a_tri = (w_b * h_t) // 2
            ans = a_rect + a_tri
            B.add_math(
                tp, "Hard", bp,
                f"A {ctx_en} consists of a {m(f'{w_b}\\text{{ m}} \\times {h_r}\\text{{ m}}')} rectangle topped by a triangle of base {m(f'{w_b}\\text{{ m}}')} and height {m(f'{h_t}\\text{{ m}}')}. What is the **total area** in {m('\\text{m}^2')}?",
                f"تتكوّن ({ctx_ar}) من مستطيل أبعاده {m(f'{w_b}\\text{{ م}} \\times {h_r}\\text{{ م}}')} يعلوه مثلث طول قاعدته {m(f'{w_b}\\text{{ م}}')} وارتفاعه {m(f'{h_t}\\text{{ م}}')}. ما **المساحة الكلية** بـ {m('\\text{م}^2')}؟",
                ans, [a_rect + w_b * h_t, (w_b * (h_r + h_t)) // 2, ans - a_tri // 2],
                "Add the rectangle area (w × h_rect) and the triangle area (1/2 × w × h_tri).",
                "اجمع مساحة المستطيل (العرض × ارتفاع المستطيل) مع مساحة المثلث (1/2 × العرض × ارتفاع المثلث).",
                "Decompose into a rectangle plus a triangle and sum their areas.",
                [
                    f"Rectangle area = {m(f'{w_b} \\times {h_r} = {a_rect}\\text{{ m}}^2')}.",
                    f"Triangle roof area = {m(f'\\frac{{1}}{{2}} \\times {w_b} \\times {h_t} = {a_tri}\\text{{ m}}^2')}.",
                    f"Total area = {m(f'{a_rect} + {a_tri} = {ans}\\text{{ m}}^2')}.",
                ],
                f"{m(f'{a_rect} + {a_tri} = {ans}\\text{{ m}}^2')}.",
                "نجمع مساحة المستطيل السفلي ومساحة المثلث العلوي.",
                [
                    f"مساحة المستطيل = {m(a_rect)} م²، ومساحة المثلث = {m(a_tri)} م².",
                    f"المجموع الكلي = {m(f'{a_rect} + {a_tri} = {ans}\\text{{ م}}^2')}.",
                ],
                f"التحقق: {m(f'{a_rect} + {a_tri} = {ans}')}.",
                diagram_en=svg_shaded_triangle_in_rect(w_b, h_r + h_t, 0.5, "m"),
            )
        else:
            _, circ_v, ctx_en, ctx_ar = row
            ans = (circ_v * 7) // 44
            B.add_math(
                tp, "Hard", bp,
                f"A {ctx_en} has circumference {m(f'{circ_v}\\text{{ m}}')}. Using {m('\\pi \\approx \\frac{22}{7}')}, what is its **radius** in meters?",
                f"يبلغ محيط ({ctx_ar}) {m(f'{circ_v}\\text{{ م}}')}. باستعمال {m('\\pi \\approx \\frac{22}{7}')}، ما طول **نصف قطرها** بالأمتار؟",
                ans, [2 * ans, circ_v // 4, ans + 7],
                f"Solve 2 × (22/7) × r = {circ_v}, so r = ({circ_v} × 7) ÷ 44 (be careful not to stop at diameter {2*ans}!).",
                f"حل المعادلة 2 × (22/7) × نق = {circ_v}، أي نق = ({circ_v} × 7) ÷ 44 (وانتبه ألا تتوقف عند القطر {2*ans}!).",
                f"Use {m('C = 2\\pi r')} backwards to isolate the radius {m('r')}.",
                [
                    f"Set {m(f'\\frac{{44}}{{7}} r = {circ_v}')}.",
                    f"Multiply by {m('\\frac{7}{44}')}: {m(f'r = \\frac{{{circ_v} \\times 7}}{{44}} = {ans}\\text{{ m}}')}.",
                ],
                f"{m(f'2 \\times \\frac{{22}}{{7}} \\times {ans} = {circ_v}\\text{{ m}}')}.",
                "نطبّق قانون محيط الدائرة عكسياً لإيجاد نصف القطر.",
                [
                    f"من {m(f'2 \\times \\frac{{22}}{{7}} \\times r = {circ_v}')} نجد {m(f'r = \\frac{{{circ_v} \\times 7}}{{44}} = {ans}\\text{{ م}}')}.",
                ],
                f"التحقق: {m(f'2 \\times \\frac{{22}}{{7}} \\times {ans} = {circ_v}\\text{{ م}}')}.",
                diagram_en=svg_g6_circle("r = ? m", is_diameter=False, caption=f"C = {circ_v} m"),
            )


def _add_geo_04(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-04"
    # 5 Easy: Volume V = lwh of rectangular prisms & cubes
    easy_vol = [
        (9, 5, 4, "date gift box in Madinah", "صندوق تمور بالمدينة"),
        (12, 6, 5, "aquarium tank in Jeddah", "حوض سمك في جدة"),
        (7, 7, 7, "wooden display cube", "مكعب عرض خشبي"),
        (10, 8, 3, "robotics parts bin", "صندوق قطع الروبوت"),
        (11, 4, 6, "ceramic planter box", "حوض زراعة خزفي"),
    ]
    for l, w, h, ctx_en, ctx_ar in easy_vol:
        ans = l * w * h
        B.add_math(
            tp, "Easy", bp,
            f"A rectangular prism ({ctx_en}) has length {m(f'{l}\\text{{ cm}}')}, width {m(f'{w}\\text{{ cm}}')}, and height {m(f'{h}\\text{{ cm}}')}. What is its **volume** in {m('\\text{cm}^3')}?",
            f"منشور رباعي يمثّل ({ctx_ar}) طوله {m(f'{l}\\text{{ سم}}')} وعرضه {m(f'{w}\\text{{ سم}}')} وارتفاعه {m(f'{h}\\text{{ سم}}')}. ما **حجمه** بـ {m('\\text{سم}^3')}؟",
            ans, [2 * (l * w + l * h + w * h), l + w + h, l * w + h],
            "Multiply length × width × height: V = l × w × h.",
            "اضرب الطول × العرض × الارتفاع: ح = ل × ض × ع.",
            f"Compute {m(f'V = {l} \\times {w} \\times {h}')}.",
            [
                f"Base area = {m(f'{l} \\times {w} = {l * w}\\text{{ cm}}^2')}.",
                f"Multiply by height {m(h)}: {m(f'V = {l * w} \\times {h} = {ans}\\text{{ cm}}^3')}.",
            ],
            f"{m(f'{l} \\times {w} \\times {h} = {ans}\\text{{ cm}}^3')}.",
            "نضرب أبعاد المنشور الثلاثة بعضها في بعض.",
            [
                f"مساحة القاعدة {m(f'{l} \\times {w} = {l * w}')} سم²، والحجم {m(f'{l * w} \\times {h} = {ans}\\text{{ سم}}^3')}.",
            ],
            f"حاصل الضرب يساوي {m(ans)} سم³.",
            diagram_en=svg_water_tank_3d(f"{l} cm", f"{w} cm", f"{h} cm", 0.65),
        )

    # 5 Medium: Total surface area SA = 2(lw + lh + wh)
    med_sa = [
        (7, 5, 4, "cardboard shipping parcel", "طرد بريدي كرتوني"),
        (9, 6, 3, "museum artifact case", "صندوق حفظ أثر تاريخي"),
        (6, 6, 6, "cubic gift box", "علبة هدايا مكعبة"),
        (10, 5, 3, "first-aid cabinet", "خزانة إسعافات أولية"),
        (8, 6, 5, "insulated lunch cooler", "حافظة طعام حرارية"),
    ]
    for l, w, h, ctx_en, ctx_ar in med_sa:
        half_sa = l * w + l * h + w * h
        ans = 2 * half_sa
        B.add_math(
            tp, "Medium", bp,
            f"What is the **total surface area** (in {m('\\text{cm}^2')}) of a closed rectangular prism ({ctx_en}) measuring {m(f'{l}\\text{{ cm}} \\times {w}\\text{{ cm}} \\times {h}\\text{{ cm}}')}?",
            f"ما **المساحة الكلية لسطح** منشور رباعي مغلق ({ctx_ar}) أبعاده {m(f'{l}\\text{{ سم}} \\times {w}\\text{{ سم}} \\times {h}\\text{{ سم}}')} بوحدة {m('\\text{سم}^2')}؟",
            ans, [half_sa, l * w * h, ans - 2 * w * h],
            "Use SA = 2(lw + lh + wh)—don't forget to multiply the sum of the three face pairs by 2!",
            "استعمل القانون م = 2(ل ض + ل ع + ض ع)، ولا تنسَ الضرب في 2 لحساب الأوجه الستة!",
            "Sum the areas of the three distinct rectangular faces and double the total.",
            [
                f"Face areas: {m(f'lw = {l * w}')}, {m(f'lh = {l * h}')}, {m(f'wh = {w * h}')}.",
                f"Double their sum: {m(f'SA = 2({l * w} + {l * h} + {w * h}) = 2 \\times {half_sa} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"All 6 faces sum to {m(f'{2*l*w} + {2*l*h} + {2*w*h} = {ans}\\text{{ cm}}^2')}.",
            "نجمع مساحات الأوجه الثلاثة المختلفة ثم نضرب المجموع في 2.",
            [
                f"مساحات الأوجه: {m(l * w)} و{m(l * h)} و{m(w * h)} ومجموعها {m(half_sa)}.",
                f"المساحة الكلية = {m(f'2 \\times {half_sa} = {ans}\\text{{ سم}}^2')}.",
            ],
            f"مجموع مساحات الأوجه الستة يساوي {m(ans)} سم².",
            diagram_en=svg_water_tank_3d(f"{l} cm", f"{w} cm", f"{h} cm", 0.0),
        )

    # 5 Hard: Missing height from volume, partial-fill liters, & packing small cubes into a crate
    hard_prism = [
        ("height", 420, 12, 7, "glass terrarium", "حوض نباتات زجاجي"),    # h = 420 / 84 = 5
        ("height", 540, 15, 6, "water trough in Qassim", "حوض مياه بالقصيم"), # h = 540 / 90 = 6
        ("liters", 50, 30, 40, (3, 4), "Jeddah reef aquarium", "حوض مرجاني بجدة"), # 60000 cm³ * 3/4 = 45000 cm³ = 45 L
        ("cubes", 12, 9, 6, 3, "storage crate", "صندوق تخزين"),            # (12*9*6)/(3^3) = 4*3*2 = 24
        ("cubes", 10, 8, 6, 2, "toy block carton", "كرتون مكعبات خشبية"),   # 5*4*3 = 60
    ]
    for row in hard_prism:
        if row[0] == "height":
            _, vol, l, w, ctx_en, ctx_ar = row
            ans = vol // (l * w)
            B.add_math(
                tp, "Hard", bp,
                f"A rectangular {ctx_en} has volume {m(f'{vol}\\text{{ cm}}^3')}, length {m(f'{l}\\text{{ cm}}')}, and width {m(f'{w}\\text{{ cm}}')}. What is its **height** in cm?",
                f"منشور رباعي يمثّل ({ctx_ar}) حجمه {m(f'{vol}\\text{{ سم}}^3')} وطوله {m(f'{l}\\text{{ سم}}')} وعرضه {m(f'{w}\\text{{ سم}}')}. فما **ارتفاعه** بالسنتيمتر؟",
                ans, [l * w, ans + 3, vol // (l + w)],
                f"Divide the volume {vol} by the base area ({l} × {w} = {l * w}).",
                f"اقسم الحجم {vol} على مساحة القاعدة ({l} × {w} = {l * w}).",
                f"Solve {m(f'{l} \\times {w} \\times h = {vol}')} for {m('h')}.",
                [
                    f"Base area = {m(f'{l} \\times {w} = {l * w}\\text{{ cm}}^2')}.",
                    f"Height {m(f'h = {vol} \\div {l * w} = {ans}\\text{{ cm}}')}.",
                ],
                f"{m(f'{l} \\times {w} \\times {ans} = {vol}\\text{{ cm}}^3')}.",
                "نقسم الحجم الكلي على مساحة القاعدة لإيجاد الارتفاع.",
                [
                    f"مساحة القاعدة {m(f'{l} \\times {w} = {l * w}')} سم².",
                    f"الارتفاع {m(f'h = {vol} \\div {l * w} = {ans}\\text{{ سم}}')}.",
                ],
                f"التحقق: {m(f'{l} \\times {w} \\times {ans} = {vol}')}.",
                diagram_en=svg_water_tank_3d(f"{l} cm", f"{w} cm", "h = ?", 0.8),
            )
        elif row[0] == "liters":
            _, l, w, h, (fn, fd), ctx_en, ctx_ar = row
            full_cm3 = l * w * h
            full_L = full_cm3 // 1000
            ans = (full_L * fn) // fd
            B.add_math(
                tp, "Hard", bp,
                f"A {ctx_en} measures {m(f'{l}\\text{{ cm}} \\times {w}\\text{{ cm}} \\times {h}\\text{{ cm}}')} and is filled {m(f'\\frac{{{fn}}}{{{fd}}}')} full of water ({m('1\\text{ L} = 1000\\text{ cm}^3')}). How many **liters** of water are inside?",
                f"أبعاد ({ctx_ar}) هي {m(f'{l}\\text{{ سم}} \\times {w}\\text{{ سم}} \\times {h}\\text{{ سم}}')} وقد مُلئ بالماء حتى {m(f'\\frac{{{fn}}}{{{fd}}}')} من سعته (علماً أن {m('1\\text{ ل} = 1000\\text{ سم}^3')}). كم **لتراً** من الماء بداخله؟",
                ans, [full_L, ans * 10, full_L - ans],
                f"Compute full volume in cm³, divide by 1000 to get {full_L} L, then multiply by {fn}/{fd}.",
                f"احسب الحجم الكامل بـ سم³، واقسمه على 1000 لتحصل على {full_L} لتراً، ثم اضرب في {fn}/{fd}.",
                "Convert total prism volume to liters and take the given fraction.",
                [
                    f"Full volume = {m(f'{l} \\times {w} \\times {h} = {full_cm3}\\text{{ cm}}^3 = {full_L}\\text{{ L}}')}.",
                    f"Water volume = {m(f'\\frac{{{fn}}}{{{fd}}} \\times {full_L} = {ans}\\text{{ L}}')}.",
                ],
                f"{m(ans)} L is {m(f'\\frac{{{fn}}}{{{fd}}}')} of {m(full_L)} L.",
                "نحسب السعة الكلية باللترات ثم نضرب في الكسر المعطى.",
                [
                    f"السعة الكلية = {m(f'{full_cm3}\\text{{ سم}}^3 = {full_L}\\text{{ ل}}')}.",
                    f"كمية الماء = {m(f'\\frac{{{fn}}}{{{fd}}} \\times {full_L} = {ans}\\text{{ ل}}')}.",
                ],
                f"{m(ans)} لتراً تساوي ثلاثة أرباع الـ {m(full_L)} لتراً.",
                diagram_en=svg_water_tank_3d(f"{l} cm", f"{w} cm", f"{h} cm", fn / fd),
            )
        else:
            _, l, w, h, s, ctx_en, ctx_ar = row
            ans = (l // s) * (w // s) * (h // s)
            B.add_math(
                tp, "Hard", bp,
                f"How many small cubes of edge {m(f'{s}\\text{{ cm}}')} can completely pack a rectangular {ctx_en} of dimensions {m(f'{l}\\text{{ cm}} \\times {w}\\text{{ cm}} \\times {h}\\text{{ cm}}')}?",
                f"كم مكعباً صغيراً طول حرفه {m(f'{s}\\text{{ سم}}')} يملأ تماماً ({ctx_ar}) أبعاده {m(f'{l}\\text{{ سم}} \\times {w}\\text{{ سم}} \\times {h}\\text{{ سم}}')}؟",
                ans, [(l * w * h) // (s * s), (l + w + h) // s, ans + (l // s)],
                f"Divide each edge by {s} cm (or divide crate volume {l*w*h} by cube volume {s}³ = {s**3}, NOT {s}²!).",
                f"اقسم كل بُعد على {s} سم ثم اضرب الأعداد الثلاثة (أو اقسم حجم الصندوق على حجم المكعب {s}³ = {s**3})!",
                f"Divide crate volume by one small cube's volume {m(f'{s}^3 = {s ** 3}')}.",
                [
                    f"Along the edges fit {m(f'{l // s} \\times {w // s} \\times {h // s} = {ans}')} cubes.",
                ],
                f"{m(f'{ans} \\times {s ** 3} = {l * w * h}\\text{{ cm}}^3')}.",
                f"نقسم أبعاد الصندوق على طول حرف المكعب {m(s)} سم ثم نضرب النواتج.",
                [
                    f"عدد المكعبات = {m(f'{l // s} \\times {w // s} \\times {h // s} = {ans}')} مكعباً.",
                ],
                f"التحقق بالحجم: {m(f'{ans} \\times {s ** 3} = {l * w * h}')} سم³.",
                diagram_en=svg_water_tank_3d(f"{l} cm", f"{w} cm", f"{h} cm", 1.0),
            )


def _add_geo_05(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-05"
    # 5 Easy: Direct complementary (90°), supplementary (180°) & vertically opposite angles
    easy_ang = [
        ("comp", 34, 56, "wooden picture frame corner", "زاوية إطار خشبي"),
        ("supp", 72, 108, "highway ramp junction", "تقاطع مخرج طريق"),
        ("vert", 118, 118, "crossed scissor blades", "مقص مفتوح"),
        ("comp", 27, 63, "square mosaic tile cut", "بلاطة مربعة مقسومة"),
        ("supp", 131, 49, "straight bridge beam", "عارضة جسر مستقيمة"),
    ]
    for mode, given_a, ans, ctx_en, ctx_ar in easy_ang:
        rel_en = "complementary" if mode == "comp" else "supplementary" if mode == "supp" else "vertically opposite"
        rel_ar = "متتامتان" if mode == "comp" else "متكاملتان" if mode == "supp" else "متقابلتان بالرأس"
        dists = [180 - given_a if mode == "comp" else abs(90 - given_a), given_a if mode != "vert" else 180 - given_a, ans + 10]
        B.add_math(
            tp, "Easy", bp,
            f"In a {ctx_en}, angle {m('x')} and a {m(f'{given_a}^\\circ')} angle are **{rel_en}**. What is the measure of angle {m('x')} in degrees?",
            f"في ({ctx_ar})، الزاوية {m('x')} والزاوية التي قياسها {m(f'{given_a}^\\circ')} زاويتان **{rel_ar}**. ما قياس الزاوية {m('x')} بالدرجات؟",
            ans, dists,
            "Complementary angles sum to 90°, supplementary sum to 180°, and vertically opposite angles are equal.",
            "الزاويتان المتتامتان مجموعهما 90°، والمتكاملتان مجموعهما 180°، والمتقابلتان بالرأس متطابقتان.",
            f"Apply the {rel_en} angle rule.",
            [
                f"Using the {rel_en} relationship with {m(f'{given_a}^\\circ')} gives {m(f'x = {ans}^\\circ')}.",
            ],
            f"Angle pair check confirms {m(f'x = {ans}^\\circ')}.",
            f"نطبّق قاعدة الزاويتين ({rel_ar}).",
            [
                f"ينتج مباشرة أن {m(f'x = {ans}^\\circ')}.",
            ],
            f"التحقق من العلاقة الهندسية يؤكد أن {m(f'x = {ans}^\\circ')}.",
            diagram_en=svg_g6_angle_pair(mode, f"{given_a}°", "x°"),
        )

    # 5 Medium: Algebraic 1-step / 2-step angle pairs (2x = vert, x + c + d = 180, 3x = 90, etc.)
    med_ang = [
        ("comp", "2x", 38, 26, "2x + 38° = 90°", "solar tracker hinge", "مفصل لوح شمسي"),
        ("supp", "3x", 45, 45, "3x + 45° = 180°", "stadium roof support", "دعامة سقف ملعب"),
        ("vert", "4x", 128, 32, "4x = 128°", "intersecting garden paths", "ممران متقاطعان"),
        ("supp", "2x", 64, 58, "2x + 64° = 180°", "crane boom arm", "ذراع رافعة"),
        ("comp", "3x", 18, 24, "3x + 18° = 90°", "right-angle bracket", "حامل زاوية قائمة"),
    ]
    for mode, x_lbl, other_v, ans, eq_s, ctx_en, ctx_ar in med_ang:
        B.add_math(
            tp, "Medium", bp,
            f"In a {ctx_en} diagram, the angles satisfy {m(eq_s)}. What is the value of {m('x')}?",
            f"في رسم ({ctx_ar})، تحقق الزوايا العلاقة {m(eq_s)}. ما قيمة {m('x')}؟",
            ans, [ans + 8, ans - 6, (180 - other_v) if mode == "comp" else other_v],
            f"Set up {eq_s} from the angle relationship and solve for x.",
            f"استعمل المعادلة الهندسية {eq_s} وحلها لإيجاد قيمة x.",
            f"Solve the angle equation {m(eq_s)}.",
            [
                f"From the geometry, {m(eq_s)}.",
                f"Isolating {m('x')} gives {m(f'x = {ans}')}.",
            ],
            f"Substituting {m(f'x = {ans}')} satisfies {m(eq_s)}.",
            f"نحل معادلة الزوايا {m(eq_s)} بالعمليات العكسية.",
            [
                f"من العلاقة {m(eq_s)} نجد {m(f'x = {ans}')}.",
            ],
            f"بالتعويض عن {m(f'x = {ans}')} تتحقق المعادلة.",
            diagram_en=svg_g6_angle_pair(mode, f"{other_v}°", x_lbl),
        )

    # 5 Hard: Multi-step ratio/difference angle-pair word problems
    hard_ang = [
        ("supp_k", 3, 45, 135, "smaller", "الأصغر", 45),   # x + 3x = 180 -> 45, 135
        ("supp_k", 4, 36, 144, "larger", "الأكبر", 144),    # x + 4x = 180 -> 36, 144
        ("comp_d", 16, 37, 53, "larger", "الأكبر", 53),     # x + (x+16) = 90 -> 37, 53
        ("supp_d", 28, 76, 104, "smaller", "الأصغر", 76),   # x + (x+28) = 180 -> 76, 104
        ("comp_k", 2, 30, 60, "larger", "الأكبر", 60),      # x + 2x = 90 -> 30, 60
    ]
    for kind, param, a_sm, a_lg, ask_en, ask_ar, ans in hard_ang:
        is_supp = kind.startswith("supp")
        tot_deg = 180 if is_supp else 90
        rel_en = "supplementary" if is_supp else "complementary"
        rel_ar = "متكاملتان" if is_supp else "متتامتان"
        if kind.endswith("_k"):
            desc_en = f"one angle is {m(param)} times the other"
            desc_ar = f"قياس إحداهما يساوي {m(param)} أمثال الأخرى"
        else:
            desc_en = f"one angle is {m(f'{param}^\\circ')} greater than the other"
            desc_ar = f"قياس إحداهما يزيد على الأخرى بمقدار {m(f'{param}^\\circ')}"
        other_ans = a_lg if ans == a_sm else a_sm
        B.add_math(
            tp, "Hard", bp,
            f"Two angles are **{rel_en}**, and {desc_en}. What is the measure of the **{ask_en}** angle in degrees?",
            f"زاويتان **{rel_ar}**، و{desc_ar}. ما قياس الزاوية **{ask_ar}** بالدرجات؟",
            ans, [other_ans, tot_deg // 2, ans + 12],
            f"Write an equation summing both angles to {tot_deg}°, solve for the smaller angle x, and pick the {ask_en} one!",
            f"اكتب معادلة مجموع الزاويتين = {tot_deg}°، أوجد الصغرى أولاً ثم حدّد الزاوية {ask_ar}!",
            f"Use the {m(f'{tot_deg}^\\circ')} sum to find both angles ({m(f'{a_sm}^\\circ')} and {m(f'{a_lg}^\\circ')}).",
            [
                f"Their sum is {m(f'{tot_deg}^\\circ')}, yielding the two angles {m(f'{a_sm}^\\circ')} and {m(f'{a_lg}^\\circ')}.",
                f"The {ask_en} angle is {m(f'{ans}^\\circ')}.",
            ],
            f"{m(f'{a_sm}^\\circ + {a_lg}^\\circ = {tot_deg}^\\circ')}.",
            f"نكوّن معادلة مجموع الزاويتين ({m(f'{tot_deg}^\\circ')}) لإيجاد الزاويتين.",
            [
                f"قياسا الزاويتين هما {m(f'{a_sm}^\\circ')} و{m(f'{a_lg}^\\circ')}.",
                f"إذن قياس الزاوية {ask_ar} هو {m(f'{ans}^\\circ')}.",
            ],
            f"مجموع الزاويتين {m(f'{a_sm}^\\circ + {a_lg}^\\circ = {tot_deg}^\\circ')}.",
            diagram_en=svg_g6_angle_pair("supp" if is_supp else "comp", "x", "?" if kind.endswith("_d") else f"{param}x"),
        )


def _add_geo_06(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-06"
    # 5 Easy: Finding missing 3rd angle using 180° sum & classifying acute/right/obtuse
    easy_tri = [
        (58, 67, "tent gable in Hail", "واجهة خيمة في حائل"),
        (90, 36, "wheelchair ramp profile", "مقطع منحدر"),
        (105, 38, "modern museum canopy", "مظلة متحف حديثة"),
        (49, 73, "sailing jib sail", "شراع أمامي لقارب"),
        (64, 64, "heritage arch pennant", "راية قوس تراثي"),
    ]
    for a1, a2, ctx_en, ctx_ar in easy_tri:
        ans = 180 - a1 - a2
        B.add_math(
            tp, "Easy", bp,
            f"Two interior angles of a triangular {ctx_en} measure {m(f'{a1}^\\circ')} and {m(f'{a2}^\\circ')}. What is the measure of the **third angle** in degrees?",
            f"قياسا زاويتين داخليتين في مثلث يمثّل ({ctx_ar}) هما {m(f'{a1}^\\circ')} و{m(f'{a2}^\\circ')}. ما قياس **الزاوية الثالثة** بالدرجات؟",
            ans, [360 - a1 - a2, abs(90 - ans) or ans + 15, a1 + a2],
            "The three interior angles of any triangle add up to 180°.",
            "مجموع قياسات الزوايا الداخلية لأي مثلث يساوي 180°.",
            f"Subtract {m(f'{a1}^\\circ + {a2}^\\circ = {a1 + a2}^\\circ')} from {m('180^\\circ')}.",
            [
                f"Sum of known angles: {m(f'{a1}^\\circ + {a2}^\\circ = {a1 + a2}^\\circ')}.",
                f"Third angle: {m(f'180^\\circ - {a1 + a2}^\\circ = {ans}^\\circ')}.",
            ],
            f"{m(f'{a1} + {a2} + {ans} = 180')}.",
            "نجمع الزاويتين المعلومتين ثم نطرح المجموع من 180°.",
            [
                f"مجموع الزاويتين = {m(f'{a1 + a2}^\\circ')}، والزاوية الثالثة = {m(f'180^\\circ - {a1 + a2}^\\circ = {ans}^\\circ')}.",
            ],
            f"مجموع الزوايا الثلاث يساوي {m('180^\\circ')}.",
            diagram_en=svg_g6_triangle(f"{a1}°", f"{a2}°", "x°", right_bl=(a1 == 90)),
        )

    # 5 Medium: Isosceles vertex/base angles & bilingual triangle classification
    med_tri = [
        ("iso_base", 52, 64, "isosceles glass pyramid face", "وجه هرم زجاجي متطابق الضلعين"),
        ("iso_base", 76, 52, "isosceles pennant", "علم مثلث متطابق الضلعين"),
        ("iso_vert", 68, 44, "isosceles roof frame", "إطار سقف متطابق الضلعين"),
        ("iso_vert", 55, 70, "isosceles sundial pointer", "مؤشر مزولة متطابق الضلعين"),
    ]
    for kind, given_v, ans, ctx_en, ctx_ar in med_tri:
        if kind == "iso_base":
            B.add_math(
                tp, "Medium", bp,
                f"An {ctx_en} has vertex angle {m(f'{given_v}^\\circ')} and two equal base angles. What is the measure of **each base angle** in degrees?",
                f"زاوية الرأس في ({ctx_ar}) تساوي {m(f'{given_v}^\\circ')} وزاويتا القاعدة متطابقتان. ما قياس **كل زاوية من زاويتي القاعدة** بالدرجات؟",
                ans, [180 - given_v, given_v, ans + 10],
                f"Subtract {given_v}° from 180°, then divide by 2!",
                f"اطرح {given_v}° من 180° ثم اقسم الباقي على 2!",
                f"Solve {m(f'{given_v}^\\circ + 2x = 180^\\circ')}.",
                [
                    f"{m(f'2x = 180^\\circ - {given_v}^\\circ = {180 - given_v}^\\circ')}.",
                    f"Divide by 2: {m(f'x = {ans}^\\circ')}.",
                ],
                f"{m(f'{given_v} + {ans} + {ans} = 180')}.",
                "نطرح زاوية الرأس من 180° ثم نقسم على 2.",
                [
                    f"{m(f'2x = {180 - given_v}^\\circ \\implies x = {ans}^\\circ')}.",
                ],
                f"التحقق: {m(f'{given_v} + {ans} + {ans} = 180')}.",
                diagram_en=svg_g6_triangle(f"{given_v}°", "x°", "x°"),
            )
        else:
            B.add_math(
                tp, "Medium", bp,
                f"Each of the two equal base angles of an {ctx_en} measures {m(f'{given_v}^\\circ')}. What is the measure of the **vertex angle** in degrees?",
                f"قياس كل زاوية من زاويتي القاعدة المتطابقتين في ({ctx_ar}) هو {m(f'{given_v}^\\circ')}. ما قياس **زاوية الرأس** بالدرجات؟",
                ans, [(180 - given_v) // 2, 180 - given_v, given_v],
                f"Double the base angle ({given_v}° × 2 = {2*given_v}°) and subtract from 180°.",
                f"اضرب زاوية القاعدة في 2 ({given_v}° × 2 = {2*given_v}°) ثم اطرح الناتج من 180°.",
                f"Subtract both equal base angles from {m('180^\\circ')}.",
                [
                    f"Two base angles sum to {m(f'2 \\times {given_v}^\\circ = {2 * given_v}^\\circ')}.",
                    f"Vertex angle = {m(f'180^\\circ - {2 * given_v}^\\circ = {ans}^\\circ')}.",
                ],
                f"{m(f'{ans} + {given_v} + {given_v} = 180')}.",
                "نضاعف زاوية القاعدة ثم نطرح المجموع من 180°.",
                [
                    f"مجموع زاويتي القاعدة = {m(f'{2 * given_v}^\\circ')}، وزاوية الرأس = {m(f'{ans}^\\circ')}.",
                ],
                f"مجموع الزوايا الثلاث {m('180^\\circ')}.",
                diagram_en=svg_g6_triangle("x°", f"{given_v}°", f"{given_v}°"),
            )
    B.add_bilingual(
        tp, "Medium", bp,
        f"A triangle has interior angles {m('35^\\circ')}, {m('35^\\circ')}, and {m('110^\\circ')}. How is this triangle classified by its **angles and sides**?",
        f"مثلث قياسات زواياه الداخلية {m('35^\\circ')} و{m('35^\\circ')} و{m('110^\\circ')}. كيف يُصنّف هذا المثلث وفق **زواياه وأضلاعه**؟",
        [
            ("Obtuse and isosceles", "منفرج الزاوية ومتطابق الضلعين"),
            ("Acute and isosceles", "حاد الزوايا ومتطابق الضلعين"),
            ("Obtuse and scalene", "منفرج الزاوية ومختلف الأضلاع"),
            ("Right and isosceles", "قائم الزاوية ومتطابق الضلعين"),
        ],
        0,
        "110° > 90° makes it obtuse, and two equal 35° angles mean two equal sides (isosceles).",
        "الزاوية 110° أكبر من 90° فهو منفرج الزاوية، وتساوي زاويتين (35°) يعني تطابق ضلعين.",
        "Check the largest angle (> 90°) and equal angle pairs.",
        [
            f"Since {m('110^\\circ > 90^\\circ')}, the triangle is **obtuse**.",
            f"Since two angles are equal ({m('35^\\circ = 35^\\circ')}), the opposite sides are equal, so it is **isosceles**.",
        ],
        "Obtuse + two equal sides = obtuse isosceles triangle.",
        "نفحص أكبر زاوية وتطابق الزوايا لتصنيف المثلث.",
        [
            f"بما أن {m('110^\\circ > 90^\\circ')} فهو **منفرج الزاوية**.",
            f"وبما أن فيه زاويتين متطابقتين ({m('35^\\circ')}) فهو **متطابق الضلعين**.",
        ],
        "التصنيف الصحيح: منفرج الزاوية ومتطابق الضلعين.",
        diagram_en=svg_g6_triangle("110°", "35°", "35°"),
    )

    # 5 Hard: Triangle angle ratios & exterior straight-line angle puzzles
    hard_tri = [
        ("ratio", (1, 2, 3), "largest", "الكبرى", 90),
        ("ratio", (2, 3, 4), "smallest", "الصغرى", 40),
        ("ratio", (2, 2, 5), "largest", "الكبرى", 100),
        ("ext", 132, 65, 67),  # exterior = 132 => interior = 48; other = 132 - 65 = 67
        ("ext", 118, 54, 64),  # exterior = 118 => interior = 62; other = 118 - 54 = 64
    ]
    for row in hard_tri:
        if row[0] == "ratio":
            _, (r1, r2, r3), which_en, which_ar, ans = row
            s_parts = r1 + r2 + r3
            unit_d = 180 // s_parts
            angs = [r1 * unit_d, r2 * unit_d, r3 * unit_d]
            B.add_math(
                tp, "Hard", bp,
                f"The three interior angles of a triangle are in the ratio {m(f'{r1} : {r2} : {r3}')}. What is the measure of the **{which_en}** angle in degrees?",
                f"النسبة بين قياسات الزوايا الداخلية الثلاث لمثلث هي {m(f'{r1} : {r2} : {r3}')}. ما قياس الزاوية **{which_ar}** بالدرجات؟",
                ans, [unit_d if unit_d != ans else angs[1], angs[1] if angs[1] != ans else angs[0], 360 // s_parts * max(r1, r2, r3)],
                f"Sum the ratio parts ({r1}+{r2}+{r3} = {s_parts}) and divide 180° by {s_parts} to find 1 part.",
                f"اجمع أجزاء النسبة ({r1}+{r2}+{r3} = {s_parts}) واقسم 180° على {s_parts} لإيجاد قيمة الجزء الواحد.",
                f"Divide {m('180^\\circ')} into {m(s_parts)} equal parts.",
                [
                    f"One part = {m(f'180^\\circ \\div {s_parts} = {unit_d}^\\circ')}.",
                    f"The angles are {m(f'{angs[0]}^\\circ, {angs[1]}^\\circ, {angs[2]}^\\circ')}, so the {which_en} angle is {m(f'{ans}^\\circ')}.",
                ],
                f"{m(f'{angs[0]} + {angs[1]} + {angs[2]} = 180')}.",
                f"نقسم {m('180^\\circ')} على مجموع الأجزاء ({m(s_parts)}) ثم نحدد الزاوية المطلوبة.",
                [
                    f"قيمة الجزء الواحد = {m(f'180^\\circ \\div {s_parts} = {unit_d}^\\circ')}.",
                    f"الزوايا هي {m(f'{angs[0]}^\\circ، {angs[1]}^\\circ، {angs[2]}^\\circ')}، فتكون الزاوية {which_ar} مساوية لـ {m(f'{ans}^\\circ')}.",
                ],
                f"مجموع الزوايا الثلاث {m('180^\\circ')}.",
                diagram_en=svg_g6_triangle(f"{r1}k", f"{r2}k", f"{r3}k"),
            )
        else:
            _, ext_a, int_a, ans = row
            adj_int = 180 - ext_a
            B.add_math(
                tp, "Hard", bp,
                f"When the base of a triangle is extended in a straight line, the exterior angle measures {m(f'{ext_a}^\\circ')}. If one non-adjacent interior angle is {m(f'{int_a}^\\circ')}, what is the other non-adjacent interior angle {m('x')} in degrees?",
                f"عند مدّ قاعدة مثلث على استقامتها، نتجت زاوية خارجية قياسها {m(f'{ext_a}^\\circ')}. إذا كان قياس إحدى الزاويتين الداخليتين البعيدتين {m(f'{int_a}^\\circ')}، فما قياس الزاوية الداخلية البعيدة الأخرى {m('x')} بالدرجات؟",
                ans, [adj_int, 180 - int_a, ans + 12],
                f"Find the adjacent interior angle (180° − {ext_a}° = {adj_int}°), then use the 180° triangle sum (or use x + {int_a}° = {ext_a}°).",
                f"أوجد الزاوية الداخلية المجاورة أولاً (180° − {ext_a}° = {adj_int}°)، ثم استعمل مجموع زوايا المثلث 180°.",
                "Use supplementary angles at the extended vertex and the 180° triangle sum.",
                [
                    f"Adjacent interior angle = {m(f'180^\\circ - {ext_a}^\\circ = {adj_int}^\\circ')}.",
                    f"From the triangle sum: {m(f'x = 180^\\circ - ({adj_int}^\\circ + {int_a}^\\circ) = {ans}^\\circ')}.",
                ],
                f"{m(f'{int_a}^\\circ + {ans}^\\circ = {ext_a}^\\circ')}, matching the exterior angle.",
                "نحسب الزاوية المجاورة بالمكملة ثم نطرح من 180°.",
                [
                    f"الزاوية الداخلية المجاورة = {m(f'180^\\circ - {ext_a}^\\circ = {adj_int}^\\circ')}.",
                    f"الزاوية المطلوبة {m(f'x = 180^\\circ - ({adj_int}^\\circ + {int_a}^\\circ) = {ans}^\\circ')}.",
                ],
                f"مجموع البعيدتين {m(f'{int_a}^\\circ + {ans}^\\circ = {ext_a}^\\circ')}.",
                diagram_en=svg_g6_triangle(f"{int_a}°", "x°", f"{adj_int}°", f"Exterior = {ext_a}°"),
            )


def _add_geo_07(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-07"
    # 5 Easy: 360° quadrilateral angle sum & basic classification
    easy_q = [
        (100, 85, 95, "ceramic courtyard tile", "بلاطة فناء خزفية"),
        (115, 70, 90, "stained-glass panel", "لوح زجاج ملون"),
        (108, 92, 65, "garden plot in Taif", "قطعة أرض زراعية بالطائف"),
        (124, 86, 74, "kite frame model", "إطار طائرة ورقية"),
    ]
    for a1, a2, a3, ctx_en, ctx_ar in easy_q:
        ans = 360 - (a1 + a2 + a3)
        B.add_math(
            tp, "Easy", bp,
            f"Three interior angles of a quadrilateral ({ctx_en}) measure {m(f'{a1}^\\circ')}, {m(f'{a2}^\\circ')}, and {m(f'{a3}^\\circ')}. What is the measure of the **fourth angle** in degrees?",
            f"قياسات ثلاث زوايا داخلية في شكل رباعي يمثّل ({ctx_ar}) هي {m(f'{a1}^\\circ')} و{m(f'{a2}^\\circ')} و{m(f'{a3}^\\circ')}. ما قياس **الزاوية الرابعة** بالدرجات؟",
            ans, [abs(360 - ans - 180), ans + 15, ans - 10],
            "All four interior angles of any quadrilateral sum to 360°.",
            "مجموع الزوايا الداخلية الأربع لأي شكل رباعي يساوي 360°.",
            f"Subtract the sum {m(a1 + a2 + a3)}° from {m('360^\\circ')}.",
            [
                f"Known sum = {m(f'{a1}^\\circ + {a2}^\\circ + {a3}^\\circ = {a1 + a2 + a3}^\\circ')}.",
                f"Fourth angle = {m(f'360^\\circ - {a1 + a2 + a3}^\\circ = {ans}^\\circ')}.",
            ],
            f"{m(f'{a1} + {a2} + {a3} + {ans} = 360')}.",
            "نجمع الزوايا الثلاث المعلومة ثم نطرح الناتج من 360°.",
            [
                f"مجموع الزوايا الثلاث = {m(f'{a1 + a2 + a3}^\\circ')}، والرابعة = {m(f'360^\\circ - {a1 + a2 + a3}^\\circ = {ans}^\\circ')}.",
            ],
            f"مجموع الزوايا الأربع يساوي {m('360^\\circ')}.",
            diagram_en=svg_g6_quad_angles(f"{a1}°", f"{a2}°", "x°", f"{a3}°"),
        )
    B.add_bilingual(
        tp, "Easy", bp,
        "Which quadrilateral has **exactly one pair** of parallel opposite sides?",
        "أي شكل رباعي مما يلي فيه **ضلعان متقابلان متوازيان فقط**؟",
        [
            ("Trapezoid", "شبه المنحرف"),
            ("Parallelogram", "متوازي الأضلاع"),
            ("Rhombus", "المعين"),
            ("Rectangle", "المستطيل"),
        ],
        0,
        "Parallelograms, rhombuses, and rectangles all have TWO pairs of parallel sides.",
        "متوازي الأضلاع والمعين والمستطيل فيها كل ضلعين متقابلين متوازيان (زوجان من الأضلاع المتوازية).",
        "Match 'exactly one pair of parallel sides' to the definition of a trapezoid.",
        ["A **trapezoid** has exactly one pair of parallel bases, whereas parallelograms have two pairs."],
        "Trapezoid = 1 pair of parallel sides.",
        "نطابق التعريف الهندسي لشبه المنحرف.",
        ["**شبه المنحرف** له زوج واحد فقط من الأضلاع المتوازية (القاعدتان)."],
        "الإجابة الصحيحة هي شبه المنحرف.",
        diagram_en=svg_g6_quad_angles("115°", "115°", "65°", "65°", "One pair of parallel bases"),
    )

    # 5 Medium: Parallelogram / rhombus opposite & consecutive angles + classification
    med_q = [
        ("adj", 68, 112, "parallelogram solar panel", "لوح شمسي متوازي أضلاع"),
        ("opp", 127, 127, "rhombus heritage motif", "زخرفة تراثية على شكل معين"),
        ("adj", 114, 66, "rhombus lattice window", "نافذة مشربية على شكل معين"),
        ("pair_x", 104, 76, 90, "quadrilateral badge with two equal angles x", "وسام رباعي فيه زاويتان متساويتان x"), # 104+76+2x=360 -> x=90
    ]
    for kind, v1, ans, *rest in med_q:
        if kind in ("adj", "opp"):
            ctx_en, ctx_ar = rest[0], rest[1]
            pos_en = "consecutive (adjacent)" if kind == "adj" else "opposite"
            pos_ar = "المتجاورة معها" if kind == "adj" else "المقابلة لها"
            B.add_math(
                tp, "Medium", bp,
                f"One interior angle of a {ctx_en} measures {m(f'{v1}^\\circ')}. What is the measure of the **{pos_en}** interior angle in degrees?",
                f"قياس إحدى الزوايا الداخلية في ({ctx_ar}) هو {m(f'{v1}^\\circ')}. ما قياس الزاوية الداخلية **{pos_ar}** بالدرجات؟",
                ans, [v1 if kind == "adj" else 180 - v1, abs(90 - v1) or 45, ans + 14],
                "In any parallelogram or rhombus, opposite angles are equal and consecutive angles sum to 180°.",
                "في متوازي الأضلاع والمعين: كل زاويتين متقابلتين متطابقتان، وكل زاويتين متحالفتين (متجاورتين) مجموعهما 180°.",
                "Use parallelogram angle properties.",
                [f"In a parallelogram/rhombus, the {pos_en} angle to {m(f'{v1}^\\circ')} is {m(f'{ans}^\\circ')}."],
                f"All four angles {m(f'{v1}^\\circ, {180-v1}^\\circ, {v1}^\\circ, {180-v1}^\\circ')} sum to {m('360^\\circ')}.",
                "نطبّق خصائص زوايا متوازي الأضلاع والمعين.",
                [f"قياس الزاوية {pos_ar} يساوي {m(f'{ans}^\\circ')}."],
                f"مجموع الزوايا الأربع {m('360^\\circ')}.",
                diagram_en=svg_g6_parallelogram(f"∠1 = {v1}°", f"∠? = ?°"),
            )
        else:
            v2, real_ans, ctx_en, ctx_ar = ans, rest[0], rest[1], rest[2]
            B.add_math(
                tp, "Medium", bp,
                f"A {ctx_en} has angles {m(f'{v1}^\\circ')}, {m(f'{v2}^\\circ')}, {m('x^\\circ')}, and {m('x^\\circ')}. What is the value of {m('x')}?",
                f"شكل رباعي ({ctx_ar}) زواياه {m(f'{v1}^\\circ')} و{m(f'{v2}^\\circ')} و{m('x^\\circ')} و{m('x^\\circ')}. ما قيمة {m('x')}؟",
                real_ans, [2 * real_ans, 180 - v1, real_ans - 15],
                f"Set {v1} + {v2} + 2x = 360, subtract {v1+v2}, and divide by 2.",
                f"اكتب المعادلة {v1} + {v2} + 2x = 360، اطرح {v1+v2} ثم اقسم على 2.",
                f"Solve {m(f'{v1} + {v2} + 2x = 360')}.",
                [f"{m(f'2x = 360 - {v1 + v2} = {360 - v1 - v2} \\implies x = {real_ans}')}."],
                f"{m(f'{v1} + {v2} + {real_ans} + {real_ans} = 360')}.",
                "نطرح مجموع الزاويتين المعلومتين من 360° ثم نقسم الباقي على 2.",
                [f"{m(f'2x = {360 - v1 - v2} \\implies x = {real_ans}')}."],
                f"مجموع الزوايا الأربع يساوي {m('360^\\circ')}.",
                diagram_en=svg_g6_quad_angles(f"{v1}°", "x°", f"{v2}°", "x°"),
            )
    B.add_bilingual(
        tp, "Medium", bp,
        "Which quadrilateral ALWAYS has **four congruent sides** AND **four right angles**?",
        "أي شكل رباعي مما يلي تكون **أضلاعه الأربعة متطابقة** و**زواياه الأربع قوائم** دائماً؟",
        [
            ("Square", "المربع"),
            ("Rhombus (non-square)", "المعين غير المربع"),
            ("Rectangle (non-square)", "المستطيل غير المربع"),
            ("Trapezoid", "شبه المنحرف"),
        ],
        0,
        "Combine the 4 equal sides of a rhombus with the 4 right angles of a rectangle.",
        "اجمع خاصية الأضلاع الأربعة المتطابقة (المعين) مع الزوايا الأربع القوائم (المستطيل).",
        "A square is both a rectangle and a rhombus.",
        ["Only a **square** guarantees all 4 sides equal and all 4 angles equal to 90°."],
        "Square = 4 equal sides + 4 right angles.",
        "المربع يجمع خصائص المستطيل والمعين معاً.",
        ["**المربع** فقط أضلاعه الأربعة متطابقة وزواياه الأربع قوائم دائماً."],
        "الإجابة الصحيحة هي المربع.",
        diagram_en=svg_g6_quad_angles("90°", "90°", "90°", "90°", "4 congruent sides"),
    )

    # 5 Hard: Ratio of angles in a quadrilateral & algebraic quadrilateral angles
    hard_q = [
        ((1, 2, 3, 4), "largest", "الكبرى", 144),
        ((2, 2, 3, 5), "smallest", "الصغرى", 60),
        ((2, 3, 3, 4), "largest", "الكبرى", 120),
        ((1, 3, 3, 5), "smallest", "الصغرى", 30),
        ((3, 4, 5, 6), "largest", "الكبرى", 120),
    ]
    for (r1, r2, r3, r4), which_en, which_ar, ans in hard_q:
        s_p = r1 + r2 + r3 + r4
        u_d = 360 // s_p
        angs = [r1 * u_d, r2 * u_d, r3 * u_d, r4 * u_d]
        B.add_math(
            tp, "Hard", bp,
            f"The four interior angles of a quadrilateral are in the ratio {m(f'{r1} : {r2} : {r3} : {r4}')}. What is the measure of the **{which_en}** angle in degrees?",
            f"النسبة بين الزوايا الداخلية الأربع لشكل رباعي هي {m(f'{r1} : {r2} : {r3} : {r4}')}. ما قياس الزاوية **{which_ar}** بالدرجات؟",
            ans, [180 * max(r1, r4) // s_p or u_d + 10, angs[1] if angs[1] != ans else angs[2], ans - u_d],
            f"Sum the parts ({r1}+{r2}+{r3}+{r4} = {s_p}) and divide 360° (NOT 180°!) by {s_p}.",
            f"اجمع أجزاء النسبة ({s_p}) واقسم 360° (وليس 180°!) على {s_p}.",
            f"Divide {m('360^\\circ')} by {m(s_p)} total parts.",
            [
                f"One part = {m(f'360^\\circ \\div {s_p} = {u_d}^\\circ')}.",
                f"Angles are {m(', '.join(f'{x}^\\circ' for x in angs))}, so the {which_en} is {m(f'{ans}^\\circ')}.",
            ],
            f"Sum = {m(f'{sum(angs)}^\\circ = 360^\\circ')}.",
            f"نقسم {m('360^\\circ')} على مجموع الأجزاء ({m(s_p)}) ثم نحسب الزاوية المطلوبة.",
            [
                f"قيمة الجزء الواحد = {m(f'360^\\circ \\div {s_p} = {u_d}^\\circ')}.",
                f"قياس الزاوية {which_ar} هو {m(f'{ans}^\\circ')}.",
            ],
            f"مجموع الزوايا الأربع {m('360^\\circ')}.",
            diagram_en=svg_g6_quad_angles(f"{r1}k", f"{r2}k", f"{r3}k", f"{r4}k"),
        )


def _add_geo_08(B: G6BankBuilder) -> None:
    tp, bp = "Geometry", "G6-GEO-08"
    # 5 Easy: Horizontal & vertical distances on the coordinate plane
    easy_cp = [
        ((-3, 2), (4, 2), 7, "horizontal", "الأفقية", "metro stations A and B", "محطتي القطار A وB"),
        ((3, -2), (3, 5), 7, "vertical", "الرأسية", "park gates P and Q", "بوابتي المنتزه P وQ"),
        ((-4, -1), (2, -1), 6, "horizontal", "الأفقية", "museum halls M and N", "قاعتي المتحف M وN"),
        ((-2, -3), (-2, 5), 8, "vertical", "الرأسية", "light poles E and F", "عمودي الإنارة E وF"),
        ((1, 4), (6, 4), 5, "horizontal", "الأفقية", "library desks R and S", "طاولتي المكتبة R وS"),
    ]
    for (x1, y1), (x2, y2), ans, dir_en, dir_ar, ctx_en, ctx_ar in easy_cp:
        B.add_math(
            tp, "Easy", bp,
            f"On a coordinate grid, {ctx_en} are plotted at {m(f'({x1}, {y1})')} and {m(f'({x2}, {y2})')}. What is the {dir_en} **distance** between them in grid units?",
            f"في المستوى الإحداثي، تقع ({ctx_ar}) عند النقطتين {m(f'({x1}, {y1})')} و{m(f'({x2}, {y2})')}. كم وحدة تبلغ **المسافة** {dir_ar} بينهما؟",
            ans, [abs(x1 + x2) if dir_en == "horizontal" else abs(y1 + y2), ans - 2, ans + 2],
            "Subtract the changing coordinates and take the positive distance |c2 − c1|.",
            "احسب الفرق المطلق بين الإحداثيين المتغيرين |ع2 − ع1|.",
            "Find the absolute difference between the coordinates that change.",
            [
                f"One coordinate stays constant, so distance = {m(f'|{x2 - x1}| = {ans}') if dir_en == 'horizontal' else m(f'|{y2 - y1}| = {ans}')} units.",
            ],
            f"Counting grid squares from {m(f'({x1}, {y1})')} to {m(f'({x2}, {y2})')} gives {m(ans)} units.",
            "نحسب القيمة المطلقة للفرق بين الإحداثيين غير المتساويين.",
            [
                f"المسافة بين النقطتين تساوي {m(ans)} وحدات.",
            ],
            f"عدّ المربعات على الشبكة يعطي {m(ans)} وحدات.",
            diagram_en=svg_nafes_coordinate_line([(x1, y1, f"({x1},{y1})"), (x2, y2, f"({x2},{y2})")], max_coord=6),
        )

    # 5 Medium: Translations & reflections across the x-axis and y-axis
    med_cp = [
        ("trans", (2, -3), (3, 4), "(5, 1)", ["(-1, -7)", "(6, 1)", "(5, -7)"], "3 units right and 4 units up", "3 وحدات لليمين و4 وحدات للأعلى"),
        ("trans", (-1, 4), (5, -2), "(4, 2)", ["(-6, 6)", "(4, 6)", "(-6, 2)"], "5 units right and 2 units down", "5 وحدات لليمين ووحدتين للأسفل"),
        ("ref_x", (4, 3), (0, 0), "(4, -3)", ["(-4, 3)", "(-4, -3)", "(3, 4)"], "across the x-axis", "حول محور السينات (x)"),
        ("ref_y", (5, -2), (0, 0), "(-5, -2)", ["(5, 2)", "(-5, 2)", "(-2, 5)"], "across the y-axis", "حول محور الصادات (y)"),
        ("ref_x", (-3, 5), (0, 0), "(-3, -5)", ["(3, 5)", "(3, -5)", "(5, -3)"], "across the x-axis", "حول محور السينات (x)"),
    ]
    for kind, (px, py), (dx, dy), ans_s, dists, desc_en, desc_ar in med_cp:
        q_en = (
            f"Point {m(f'P({px}, {py})')} is translated **{desc_en}**. What are the coordinates of the image {m('P^\\prime')}?"
            if kind == "trans"
            else f"Point {m(f'P({px}, {py})')} is reflected **{desc_en}**. What are the coordinates of its image {m('P^\\prime')}?"
        )
        q_ar = (
            f"أُجري انسحاب للنقطة {m(f'P({px}, {py})')} بمقدار **{desc_ar}**. ما إحداثيات صورتها {m('P^\\prime')}؟"
            if kind == "trans"
            else f"أُجري انعكاس للنقطة {m(f'P({px}, {py})')} **{desc_ar}**. ما إحداثيات صورتها {m('P^\\prime')}؟"
        )
        B.add_math(
            tp, "Medium", bp, q_en, q_ar, ans_s, dists,
            "Right/left changes x; up/down changes y. Reflection across x-axis flips y; across y-axis flips x.",
            "اليمين/اليسار يغيّر x، والأعلى/الأسفل يغيّر y. الانعكاس حول محور x يعكس إشارة y، وحول محور y يعكس إشارة x.",
            "Apply the coordinate transformation rule directly.",
            [f"Starting at {m(f'({px}, {py})')}, applying the transformation yields {m(ans_s)}."],
            f"Plotting {m(f'P({px}, {py})')} and {m(f'P^\\prime{ans_s}')} verifies the symmetry/shift.",
            "نطبّق قاعدة التحويل الهندسي على الإحداثيين.",
            [f"صورة النقطة {m(f'({px}, {py})')} بعد التحويل هي {m(ans_s)}."],
            f"تمثيل النقطتين على الشبكة يؤكد صحة الإحداثيات {m(ans_s)}.",
            diagram_en=svg_nafes_coordinate_line([(px, py, f"P({px},{py})")], max_coord=6),
        )

    # 5 Hard: Missing 4th vertex of a rectangle, coordinate rectangle area/perimeter & 2-step transformation
    hard_cp = [
        ("v4", (-2, 1), (4, 1), (4, 5), "(-2, 5)", ["(1, 5)", "(-2, 1)", "(5, -2)"]),
        ("v4", (-3, -2), (3, -2), (3, 4), "(-3, 4)", ["(3, -4)", "(-2, 4)", "(4, -3)"]),
        ("area", (-2, -1), (5, 3), 28, [22, 11, 14]),      # width 7, height 4 -> area 28
        ("perim", (-3, -2), (4, 3), 24, [35, 12, 20]),     # width 7, height 5 -> perim 24
        ("two_step", (2, 3), "(-4, -3)", ["(4, -3)", "(-4, 3)", "(2, -3)"]),  # translate left 6 -> (-4,3), then reflect across x-axis -> (-4,-3)
    ]
    for row in hard_cp:
        if row[0] == "v4":
            _, a_pt, b_pt, c_pt, ans_s, dists = row
            B.add_math(
                tp, "Hard", bp,
                f"Three vertices of rectangle {m('ABCD')} are {m(f'A{a_pt}')}, {m(f'B{b_pt}')}, and {m(f'C{c_pt}')}. What are the coordinates of the **fourth vertex {m('D')}**?",
                f"ثلاثة رؤوس للمستطيل {m('ABCD')} هي {m(f'A{a_pt}')} و{m(f'B{b_pt}')} و{m(f'C{c_pt}')}. ما إحداثيات **الرأس الرابع {m('D')}**؟",
                ans_s, dists,
                "Match the x-coordinate of A and the y-coordinate of C so opposite sides are horizontal and vertical.",
                "خذ الإحداثي السيني للنقطة A والإحداثي الصادي للنقطة C ليكتمل المستطيل.",
                "Align D vertically above A and horizontally across from C.",
                [f"{m('D')} shares {m(f'x = {a_pt[0]}')} with {m('A')} and {m(f'y = {c_pt[1]}')} with {m('C')}, giving {m(ans_s)}."],
                f"Sides have equal opposite lengths {m(b_pt[0] - a_pt[0])} and {m(c_pt[1] - b_pt[1])}.",
                "يشترك الرأس D في الإحداثي السيني مع A وفي الإحداثي الصادي مع C.",
                [f"إذن إحداثيات الرأس الرابع هي {m(ans_s)}."],
                f"يكتمل المستطيل بأضلاع متقابلة متطابقة.",
                diagram_en=svg_nafes_coordinate_line([(a_pt[0], a_pt[1], "A"), (b_pt[0], b_pt[1], "B"), (c_pt[0], c_pt[1], "C")], max_coord=6),
            )
        elif row[0] in ("area", "perim"):
            kind, (x1, y1), (x2, y2), ans, dists = row
            w_u, h_u = abs(x2 - x1), abs(y2 - y1)
            ask_en = "area" if kind == "area" else "perimeter"
            ask_ar = "مساحة" if kind == "area" else "محيط"
            B.add_math(
                tp, "Hard", bp,
                f"Opposite corners of an axis-aligned rectangle on a coordinate grid are {m(f'({x1}, {y1})')} and {m(f'({x2}, {y2})')}. What is the **{ask_en}** of the rectangle?",
                f"طرفا قطر مستطيل أضلاعه موازية للمحورين في المستوى الإحداثي هما {m(f'({x1}, {y1})')} و{m(f'({x2}, {y2})')}. ما **{ask_ar}** المستطيل؟",
                ans, dists,
                f"Find width |{x2} − ({x1})| = {w_u} and height |{y2} − ({y1})| = {h_u} first!",
                f"أوجد العرض |{x2} − ({x1})| = {w_u} والطول الرأسي |{y2} − ({y1})| = {h_u} أولاً!",
                f"Compute width = {m(w_u)} and height = {m(h_u)}, then evaluate {ask_en}.",
                [
                    f"Width = {m(f'|{x2} - ({x1})| = {w_u}')}, height = {m(f'|{y2} - ({y1})| = {h_u}')}.",
                    f"Rectangle {ask_en} = {m(ans)}.",
                ],
                f"Dimensions {m(f'{w_u} \\times {h_u}')} confirm {ask_en} = {m(ans)}.",
                f"نحسب البعدين الأفقي ({m(w_u)}) والرأسي ({m(h_u)}) ثم نحسب ال{ask_ar}.",
                [
                    f"البعد الأفقي = {m(w_u)} والبعد الرأسي = {m(h_u)}، فيكون ال{ask_ar} مساوياً لـ {m(ans)}.",
                ],
                f"أبعاد المستطيل {m(f'{w_u} \\times {h_u}')} تؤكد صحة الناتج {m(ans)}.",
                diagram_en=svg_nafes_coordinate_line([(x1, y1, f"({x1},{y1})"), (x2, y1, ""), (x2, y2, f"({x2},{y2})"), (x1, y2, "")], max_coord=6),
            )
        else:
            _, (px, py), ans_s, dists = row
            B.add_math(
                tp, "Hard", bp,
                f"Point {m(f'A({px}, {py})')} is translated **6 units left** and then reflected **across the x-axis**. What are the final coordinates?",
                f"أُجري للنقطة {m(f'A({px}, {py})')} انسحاب بمقدار **6 وحدات لليسار** ثم انعكاس **حول محور السينات (x)**. ما الإحداثيات النهائية للصورة؟",
                ans_s, dists,
                "Step 1: subtract 6 from x to get (-4, 3). Step 2: flip the sign of y to reflect across the x-axis!",
                "الخطوة 1: اطرح 6 من الإحداثي السيني لتصبح (-4, 3). الخطوة 2: اعكس إشارة الإحداثي الصادي!",
                "Perform the translation first, then reflect the intermediate point across the x-axis.",
                [
                    f"Translate 6 left: {m(f'({px} - 6, {py}) = (-4, 3)')}.",
                    f"Reflect across the x-axis: {m('(-4, -3)')}.",
                ],
                f"x moved {m('2 \\to -4')} and y flipped {m('3 \\to -3')}.",
                "ننفّذ الانسحاب أولاً ثم الانعكاس حول محور السينات.",
                [
                    f"بعد الانسحاب 6 لليسار تصبح النقطة {m('(-4, 3)')}.",
                    f"وبعد الانعكاس حول محور السينات تصبح {m('(-4, -3)')}.",
                ],
                f"الإحداثيات النهائية هي {m('(-4, -3)')}.",
                diagram_en=svg_nafes_coordinate_line([(px, py, "A(2,3)"), (-4, 3, "A1(-4,3)")], max_coord=6),
            )


def _add_dat_01(B: G6BankBuilder) -> None:
    tp, bp = "Data & Probability", "G6-DAT-01"
    # 5 Easy: Arithmetic mean & range of 4–5 values
    easy_mr = [
        ("mean", [14, 18, 12, 20, 16], "science quiz scores in Riyadh", "درجات اختبار العلوم بالرياض"),
        ("mean", [22, 28, 19, 25, 26], "daily library borrowers", "عدد مستعيري المكتبة يومياً"),
        ("range", [13, 29, 17, 34, 21], "seedling heights (cm) in Abha", "أطوال شتلات (سم) في أبها"),
        ("mean", [15, 21, 18, 26], "robotics round points", "نقاط جولات الروبوت"),
        ("range", [18, 41, 25, 16, 33], "wind speeds (km/h) in Sakaka", "سرعات الرياح (كم/ساعة) بسكاكا"),
    ]
    for kind, vals, ctx_en, ctx_ar in easy_mr:
        v_str = ", ".join(str(x) for x in vals)
        if kind == "mean":
            ans = sum(vals) // len(vals)
            dists = [max(vals) - min(vals), sorted(vals)[len(vals) // 2] + 3 if sorted(vals)[len(vals) // 2] == ans else sorted(vals)[len(vals) // 2], ans + 2]
            B.add_math(
                tp, "Easy", bp,
                f"The {ctx_en} were {m(v_str)}. What is the **arithmetic mean**?",
                f"سُجّلت ({ctx_ar}) بالقيم: {m(v_str)}. ما **المتوسط الحسابي** لهذه البيانات؟",
                ans, dists,
                f"Add all {len(vals)} numbers together and divide by {len(vals)}.",
                f"اجمع القيم الـ {len(vals)} معاً ثم اقسم المجموع على {len(vals)}.",
                f"Sum the {len(vals)} values ({m(sum(vals))}) and divide by {m(len(vals))}.",
                [
                    f"Sum of all values = {m(sum(vals))}.",
                    f"Mean = {m(f'{sum(vals)} \\div {len(vals)} = {ans}')}.",
                ],
                f"{m(f'{ans} \\times {len(vals)} = {sum(vals)}')}.",
                f"نقسم مجموع القيم ({m(sum(vals))}) على عددها ({m(len(vals))}).",
                [
                    f"المجموع = {m(sum(vals))}، والمتوسط الحسابي = {m(f'{sum(vals)} \\div {len(vals)} = {ans}')}.",
                ],
                f"التحقق: {m(f'{ans} \\times {len(vals)} = {sum(vals)}')}.",
                diagram_en=svg_bar_chart([(f"D{i+1}", v, str(v)) for i, v in enumerate(vals)], y_max=max(vals) + 4),
            )
        else:
            ans = max(vals) - min(vals)
            dists = [vals[-1] - vals[0], sum(vals) // len(vals), ans + 4]
            B.add_math(
                tp, "Easy", bp,
                f"The {ctx_en} were {m(v_str)}. What is the **range** of these data?",
                f"كانت ({ctx_ar}) هي: {m(v_str)}. ما **المدى** لهذه البيانات؟",
                ans, dists,
                "Range = greatest value − least value (do NOT just subtract first and last!).",
                "المدى = أكبر قيمة − أصغر قيمة (لا تطرح القيمة الأولى من الأخيرة فقط!).",
                f"Subtract minimum {m(min(vals))} from maximum {m(max(vals))}.",
                [
                    f"Greatest value = {m(max(vals))}, least value = {m(min(vals))}.",
                    f"Range = {m(f'{max(vals)} - {min(vals)} = {ans}')}.",
                ],
                f"{m(f'{min(vals)} + {ans} = {max(vals)}')}.",
                "نطرح أصغر قيمة في المجموعة من أكبر قيمة فيها.",
                [
                    f"أكبر قيمة {m(max(vals))} وأصغر قيمة {m(min(vals))}، فالمدى = {m(f'{max(vals)} - {min(vals)} = {ans}')}.",
                ],
                f"التحقق: {m(f'{min(vals)} + {ans} = {max(vals)}')}.",
                diagram_en=svg_bar_chart([(f"D{i+1}", v, str(v)) for i, v in enumerate(vals)], y_max=max(vals) + 4),
            )

    # 5 Medium: Finding a missing value from a target mean
    med_miss = [
        ([16, 20, 15], 18, "Layan's 4 math quizzes", "اختبارات ليان الأربعة"),
        ([24, 19, 22, 25], 23, "Fahad's 5 basketball games", "مباريات فهد الخمس"),
        ([14, 17, 13], 16, "Rakan's 4 spelling tests", "اختبارات راكان الأربعة"),
        ([32, 28, 35, 29], 31, "5 daily greenhouse readings", "خمس قراءات يومية للمشتل"),
        ([40, 46, 38], 43, "4 charity book boxes", "أربعة صناديق كتب خيرية"),
    ]
    for known, target_m, ctx_en, ctx_ar in med_miss:
        n_tot = len(known) + 1
        req_sum = n_tot * target_m
        ans = req_sum - sum(known)
        k_str = ", ".join(str(x) for x in known)
        bars = [(f"#{i+1}", v, str(v)) for i, v in enumerate(known)] + [(f"#{n_tot}", ans, "?")]
        B.add_math(
            tp, "Medium", bp,
            f"In {ctx_en}, the first {m(len(known))} values are {m(k_str)}. What must the **{m(n_tot)}-th value** be so the mean of all {m(n_tot)} values is {m(target_m)}?",
            f"في ({ctx_ar})، القيم الـ {m(len(known))} الأولى هي {m(k_str)}. كم يجب أن تكون **القيمة رقم {m(n_tot)}** ليصبح المتوسط الحسابي لجميع القيم الـ {m(n_tot)} مساوياً لـ {m(target_m)}؟",
            ans, [target_m, ans - 3, ans + 4],
            f"Multiply target mean {target_m} × {n_tot} = {req_sum} to get the required total sum, then subtract {sum(known)}!",
            f"اضرب المتوسط المطلوب {target_m} × {n_tot} = {req_sum} لإيجاد المجموع الكلي المطلوب، ثم اطرح {sum(known)}!",
            f"Use Total Sum = {m(f'{n_tot} \\times {target_m} = {req_sum}')}.",
            [
                f"Required sum = {m(f'{n_tot} \\times {target_m} = {req_sum}')}.",
                f"Known sum = {m(sum(known))}, so missing value = {m(f'{req_sum} - {sum(known)} = {ans}')}.",
            ],
            f"{m(f'({sum(known)} + {ans}) \\div {n_tot} = {req_sum} \\div {n_tot} = {target_m}')}.",
            f"نوجد المجموع الكلي المطلوب ({m(req_sum)}) ثم نطرح مجموع القيم المعلومة ({m(sum(known))}).",
            [
                f"المجموع الكلي المطلوب = {m(f'{n_tot} \\times {target_m} = {req_sum}')}.",
                f"القيمة المفقودة = {m(f'{req_sum} - {sum(known)} = {ans}')}.",
            ],
            f"المتوسط بعد إضافة {m(ans)} يساوي {m(target_m)} تماماً.",
            diagram_en=svg_bar_chart(bars, y_max=max(max(known), ans) + 4),
        )

    # 5 Hard: Updating mean after adding a new score & combining range + minimum
    hard_mr = [
        ("new_m", 4, 19, 29, 21, "science club challenges", "تحديات نادي العلوم"),   # (76+29)/5 = 21
        ("new_m", 5, 24, 36, 26, "football league matches", "مباريات دوري المدرسة"), # (120+36)/6 = 26
        ("new_m", 4, 32, 47, 35, "daily step goals", "أهداف المشي اليومية"),        # (128+47)/5 = 35
        ("max_r", 14, 23, [14, 19, 25], "botanical leaf lengths (mm)", "أطوال أوراق نباتية (ملم)"), # max = 14 + 23 = 37
        ("min_r", 52, 29, [31, 40, 52], "quiz completion times (s)", "أزمنة إنهاء المسابقة (ث)"),   # min = 52 - 29 = 23
    ]
    for row in hard_mr:
        if row[0] == "new_m":
            _, n_old, m_old, new_v, ans, ctx_en, ctx_ar = row
            old_sum = n_old * m_old
            new_sum = old_sum + new_v
            B.add_math(
                tp, "Hard", bp,
                f"Across {m(n_old)} {ctx_en}, a student's mean score was {m(m_old)}. After scoring {m(new_v)} on the next one, what is the **new mean** across all {m(n_old + 1)} challenges?",
                f"بلغ متوسط درجات طالب في {m(n_old)} من ({ctx_ar}) {m(m_old)} درجة. بعد حصوله على {m(new_v)} في المرة التالية، كم يصبح **المتوسط الحسابي الجديد** عبر الـ {m(n_old + 1)} مرات كلها؟",
                ans, [(m_old + new_v) // 2, ans + 2, m_old + 1],
                f"Do NOT average {m_old} and {new_v}! Recover the old sum ({n_old} × {m_old} = {old_sum}), add {new_v}, and divide by {n_old + 1}.",
                f"لا تأخذ متوسط {m_old} و{new_v} مباشرة! احسب المجموع السابق ({n_old} × {m_old} = {old_sum}) وأضف {new_v} ثم اقسم على {n_old + 1}.",
                f"Recover old total {m(old_sum)}, add {m(new_v)}, and divide by {m(n_old + 1)}.",
                [
                    f"Previous total = {m(f'{n_old} \\times {m_old} = {old_sum}')}.",
                    f"New total = {m(f'{old_sum} + {new_v} = {new_sum}')}; new mean = {m(f'{new_sum} \\div {n_old + 1} = {ans}')}.",
                ],
                f"{m(f'{ans} \\times {n_old + 1} = {new_sum}')}.",
                f"نسترجع المجموع القديم ({m(old_sum)}) ثم نضيف القيمة الجديدة ونقسم على {m(n_old + 1)}.",
                [
                    f"المجموع الجديد = {m(f'{old_sum} + {new_v} = {new_sum}')}، والمتوسط الجديد = {m(f'{new_sum} \\div {n_old + 1} = {ans}')}.",
                ],
                f"التحقق: {m(f'{ans} \\times {n_old + 1} = {new_sum}')}.",
                diagram_en=svg_nafes_function_table(["Stage", f"First {n_old}", "Next 1", f"All {n_old+1}"], [["Mean", str(m_old), str(new_v), "?"]], highlight_cell=(0, 3)),
            )
        elif row[0] == "max_r":
            _, min_v, rng_v, samp, ctx_en, ctx_ar = row
            ans = min_v + rng_v
            B.add_math(
                tp, "Hard", bp,
                f"In a dataset of {ctx_en}, the **minimum** value is {m(min_v)} and the **range** is {m(rng_v)}. What is the **maximum** value in the dataset?",
                f"في مجموعة بيانات لـ ({ctx_ar})، إذا كانت **أصغر قيمة** تساوي {m(min_v)} و**المدى** يساوي {m(rng_v)}، فما **أكبر قيمة** في البيانات؟",
                ans, [rng_v - min_v, ans - 5, ans + 6],
                "Since Range = Max − Min, add Min + Range to get Max.",
                "بما أن المدى = الأكبر − الأصغر، فإن الأكبر = الأصغر + المدى.",
                f"Add {m(min_v)} and {m(rng_v)}.",
                [f"{m(f'\\text{{Max}} = \\text{{Min}} + \\text{{Range}} = {min_v} + {rng_v} = {ans}')}."],
                f"Range check: {m(f'{ans} - {min_v} = {rng_v}')}.",
                "نجمع أصغر قيمة مع المدى لإيجاد أكبر قيمة.",
                [f"أكبر قيمة = {m(f'{min_v} + {rng_v} = {ans}')}."],
                f"التحقق: {m(f'{ans} - {min_v} = {rng_v}')}.",
                diagram_en=svg_number_strip([f"Min = {min_v}", f"Range = {rng_v}", "Max = ?"]),
            )
        else:
            _, max_v, rng_v, samp, ctx_en, ctx_ar = row
            ans = max_v - rng_v
            B.add_math(
                tp, "Hard", bp,
                f"In a dataset of {ctx_en}, the **maximum** value is {m(max_v)} and the **range** is {m(rng_v)}. What is the **minimum** value in the dataset?",
                f"في مجموعة بيانات لـ ({ctx_ar})، إذا كانت **أكبر قيمة** تساوي {m(max_v)} و**المدى** يساوي {m(rng_v)}، فما **أصغر قيمة** في البيانات؟",
                ans, [max_v + rng_v, ans + 6, ans - 5],
                "Since Range = Max − Min, subtract Max − Range to find Min.",
                "بما أن المدى = الأكبر − الأصغر، فإن الأصغر = الأكبر − المدى.",
                f"Subtract {m(rng_v)} from {m(max_v)}.",
                [f"{m(f'\\text{{Min}} = \\text{{Max}} - \\text{{Range}} = {max_v} - {rng_v} = {ans}')}."],
                f"Range check: {m(f'{max_v} - {ans} = {rng_v}')}.",
                "نطرح المدى من أكبر قيمة لإيجاد أصغر قيمة.",
                [f"أصغر قيمة = {m(f'{max_v} - {rng_v} = {ans}')}."],
                f"التحقق: {m(f'{max_v} - {ans} = {rng_v}')}.",
                diagram_en=svg_number_strip(["Min = ?", f"Range = {rng_v}", f"Max = {max_v}"]),
            )


def _add_dat_02(B: G6BankBuilder) -> None:
    tp, bp = "Data & Probability", "G6-DAT-02"
    # 5 Easy: Median (odd count) & mode of Grade 6 datasets
    easy_mm = [
        ("med", [19, 12, 25, 16, 21], 19, "unsorted quiz scores", "درجات اختبار قصير"),
        ("mode", [14, 17, 14, 20, 18, 14, 17], 14, "shoe sizes sold in a sports shop", "مقاسات أحذية رياضية"),
        ("med", [31, 22, 28, 35, 24, 19, 30], 28, "daily temperatures (°C) in Abha", "درجات حرارة يومية بأبها"),
        ("mode", [8, 11, 9, 11, 13, 8, 11], 11, "books read by STEM club members", "عدد الكتب المقروءة"),
        ("med", [45, 32, 51, 38, 40], 40, "sprint times (s) in PE class", "أزمنة الجري في حصة الرياضة"),
    ]
    for kind, vals, ans, ctx_en, ctx_ar in easy_mm:
        v_s = ", ".join(str(x) for x in vals)
        sr = sorted(vals)
        if kind == "med":
            B.add_math(
                tp, "Easy", bp,
                f"What is the **median** of the {ctx_en}: {m(v_s)}?",
                f"ما **الوسيط** لمجموعة ({ctx_ar}): {m(v_s)}؟",
                ans, [vals[len(vals) // 2] if vals[len(vals) // 2] != ans else sr[1], sr[-1] - sr[0], ans + 3],
                "Sort the numbers from least to greatest FIRST, then pick the middle number!",
                "رتّب الأعداد تصاعدياً أولاً ثم اختر العدد الذي يتوسطها!",
                "Order the list ascending and select the middle entry.",
                [
                    f"Sorted list: {m(', '.join(str(x) for x in sr))}.",
                    f"The middle value is {m(ans)}.",
                ],
                f"Equal counts of numbers lie below and above {m(ans)}.",
                "نرتب البيانات تصاعدياً ثم نأخذ القيمة الوسطى.",
                [
                    f"بعد الترتيب التصاعدي: {m('، '.join(str(x) for x in sr))}، فالوسيط هو {m(ans)}.",
                ],
                f"عدد القيم الأصغر من {m(ans)} يساوي عدد القيم الأكبر منها.",
                diagram_en=svg_bar_chart([(f"#{i+1}", v, str(v)) for i, v in enumerate(vals)], y_max=max(vals) + 5),
            )
        else:
            B.add_math(
                tp, "Easy", bp,
                f"What is the **mode** of the {ctx_en}: {m(v_s)}?",
                f"ما **المنوال** لمجموعة ({ctx_ar}): {m(v_s)}؟",
                ans, [sr[len(sr) // 2] if sr[len(sr) // 2] != ans else ans + 3, max(vals), min(vals) if min(vals) != ans else ans + 2],
                "The mode is the value that appears MOST frequently.",
                "المنوال هو القيمة الأكثر تكراراً في مجموعة البيانات.",
                f"Count frequencies and pick the value occurring {vals.count(ans)} times.",
                [f"The value {m(ans)} appears {m(vals.count(ans))} times, more than any other value."],
                f"Frequency of {m(ans)} is {m(vals.count(ans))}.",
                "نعدّ تكرار كل قيمة ونختار الأكثر ظهوراً.",
                [f"القيمة {m(ans)} تكررت {m(vals.count(ans))} مرات وهي الأكثر تكراراً."],
                f"إذن المنوال هو {m(ans)}.",
                diagram_en=svg_bar_chart([(f"#{i+1}", v, str(v)) for i, v in enumerate(vals)], y_max=max(vals) + 4),
            )

    # 5 Medium: Median of an even number of values & difference between median and mode
    med_mm = [
        ("even", [18, 26, 14, 22, 30, 20], 21, "6 library table counts", "ست قراءات لعدد رواد المكتبة"),
        ("even", [35, 25, 41, 29, 33, 21], 31, "6 archery scores in Riyadh", "ست نتائج في مسابقة الرماية"),
        ("even", [12, 19, 15, 24, 17, 11], 16, "6 plant heights (cm)", "أطوال ست نبتات (سم)"),
        ("diff", [10, 12, 12, 16, 18, 20, 24], 4, "7 art contest scores (median − mode)", "سبع درجات في مسابقة الرسم"), # med 16, mode 12 -> 4
        ("diff", [15, 18, 21, 21, 21, 12, 14], 3, "7 robotics lap times (mode − median)", "سبعة أزمنة للروبوت"),          # sorted 12,14,15,18,21,21,21: med 18, mode 21 -> 3
    ]
    for kind, vals, ans, ctx_en, ctx_ar in med_mm:
        sr = sorted(vals)
        v_s = ", ".join(str(x) for x in vals)
        if kind == "even":
            m1, m2 = sr[2], sr[3]
            B.add_math(
                tp, "Medium", bp,
                f"Find the **median** of {ctx_en}: {m(v_s)}.",
                f"أوجد **الوسيط** لـ ({ctx_ar}): {m(v_s)}.",
                ans, [m1, m2, sum(vals) // len(vals) + 4],
                "Sort all 6 numbers first, then take the average of the 3rd and 4th numbers!",
                "رتّب الأعداد الستة تصاعدياً أولاً، ثم احسب متوسط العددين الثالث والرابع!",
                "Average the two middle values after sorting.",
                [
                    f"Sorted data: {m(', '.join(str(x) for x in sr))}.",
                    f"Middle pair: {m(m1)} and {m(m2)}; median = {m(f'({m1} + {m2}) \\div 2 = {ans}')}.",
                ],
                f"{m(ans)} lies halfway between {m(m1)} and {m(m2)}.",
                "نرتب القيم الست تصاعدياً ثم نحسب متوسط القيمتين الوسطيين.",
                [
                    f"بعد الترتيب: {m('، '.join(str(x) for x in sr))}.",
                    f"الوسيط = {m(f'({m1} + {m2}) \\div 2 = {ans}')}.",
                ],
                f"{m(ans)} يتوسط القيمتين {m(m1)} و{m(m2)}.",
                diagram_en=svg_number_strip([str(x) for x in vals]),
            )
        else:
            med_v = sr[3]
            mode_v = max(set(vals), key=vals.count)
            B.add_math(
                tp, "Medium", bp,
                f"For the dataset {m(v_s)} ({ctx_en.split(' (')[0]}), what is the positive difference {m('|\\text{median} - \\text{mode}|')}?",
                f"لمجموعة البيانات {m(v_s)} ({ctx_ar})، ما الفرق الموجب بين الوسيط والمنوال {m('|\\text{الوسيط} - \\text{المنوال}|')}؟",
                ans, [med_v, mode_v, ans + 3],
                "Sort the 7 values to find the 4th value (median), find the most repeated value (mode), and subtract.",
                "رتّب القيم السبع لإيجاد الرابعة (الوسيط)، وحدّد القيمة الأكثر تكراراً (المنوال)، ثم اطرحهما.",
                f"Compute median = {m(med_v)} and mode = {m(mode_v)}, then take their difference.",
                [
                    f"Sorted: {m(', '.join(str(x) for x in sr))} gives median = {m(med_v)} and mode = {m(mode_v)}.",
                    f"Difference = {m(f'|{med_v} - {mode_v}| = {ans}')}.",
                ],
                f"{m(f'|{med_v} - {mode_v}| = {ans}')}.",
                "نوجد الوسيط والمنوال ثم نحسب الفرق بينهما.",
                [
                    f"الوسيط هو {m(med_v)} والمنوال هو {m(mode_v)}، والفرق بينهما {m(ans)}.",
                ],
                f"التحقق: {m(f'|{med_v} - {mode_v}| = {ans}')}.",
                diagram_en=svg_number_strip([str(x) for x in sr]),
            )

    # 5 Hard: Outlier identification & outlier impact on mean vs median
    hard_out = [
        ("id", [15, 17, 16, 48, 18, 16], 48, [15, 16, 18], "daily page counts", "عدد الصفحات اليومية"),
        ("drop_mean", [12, 14, 13, 15, 46], 6, [3, 13, 20], "quiz scores with high outlier 46", "درجات اختبار مع القيمة المتطرفة 46"), # mean w/ 46 = 20; without = 54/4? wait 12+14+13+15=54? Let's make 12,14,13,17,44 -> sum=100/5=20; without 44 -> 56/4=14 -> diff=6!
        ("drop_mean", [20, 22, 21, 25, 62], 8, [4, 22, 30], "museum wait times (min) with outlier 62", "أوقات انتظار مع القيمة المتطرفة 62"), # sum=150/5=30; without 62 -> 88/4=22 -> diff=8!
    ]
    hard_out[1] = ("drop_mean", [12, 14, 13, 17, 44], 6, [3, 14, 20], "quiz scores with outlier 44", "درجات اختبار مع القيمة المتطرفة 44")
    for kind, vals, ans, dists, ctx_en, ctx_ar in hard_out:
        v_s = ", ".join(str(x) for x in vals)
        sr = sorted(vals)
        if kind == "id":
            B.add_math(
                tp, "Hard", bp,
                f"In the dataset of {ctx_en} {m(v_s)}, which value is the **outlier**?",
                f"في بيانات ({ctx_ar}): {m(v_s)}، أي قيمة تمثّل **القيمة المتطرفة**؟",
                ans, dists,
                "An outlier stands far away from the cluster of all the other data values.",
                "القيمة المتطرفة تكون بعيدة جداً عن تجمّع بقية القيم.",
                f"Spot the value far separated from the cluster {m('15\\text{–}18')}.",
                [f"Five values cluster tightly in {m('15\\text{–}18')}, while {m(ans)} is far above them."],
                f"{m(ans)} is {m(30)} units above the rest of the cluster.",
                "نحدد القيمة المنعزلة بعيداً عن تجمّع بقية القيم.",
                [f"تتجمع القيم بين {m(15)} و{m(18)} بينما تبتعد {m(ans)} كثيراً عنها."],
                f"القيمة المتطرفة هي {m(ans)}.",
                diagram_en=svg_nafes_box_plot(sr[0], sr[1], sr[2], sr[4], sr[-1], "Outlier Check"),
            )
        else:
            m_with = sum(vals) // len(vals)
            m_without = sum(sr[:-1]) // (len(vals) - 1)
            assert m_with - m_without == ans
            B.add_math(
                tp, "Hard", bp,
                f"For the dataset {m(v_s)} ({ctx_en}), by how many units does the **mean decrease** when the outlier {m(sr[-1])} is removed?",
                f"في مجموعة البيانات {m(v_s)} ({ctx_ar})، بكم وحدة **ينقص المتوسط الحسابي** عند حذف القيمة المتطرفة {m(sr[-1])}؟",
                ans, dists,
                f"Compute the mean of all 5 numbers ({m_with}) and the mean of the remaining 4 numbers ({m_without}), then subtract!",
                f"احسب متوسط القيم الخمس ({m_with}) ومتوسط القيم الأربع بعد الحذف ({m_without})، ثم اطرحهما!",
                "Compare the mean before and after removing the high outlier.",
                [
                    f"Mean with outlier: {m(f'{sum(vals)} \\div 5 = {m_with}')}.",
                    f"Mean without {m(sr[-1])}: {m(f'{sum(sr[:-1])} \\div 4 = {m_without}')}; decrease = {m(f'{m_with} - {m_without} = {ans}')}.",
                ],
                f"{m(f'{m_with} - {m_without} = {ans}')}.",
                "نقارن المتوسط قبل حذف القيمة المتطرفة وبعد حذفها.",
                [
                    f"المتوسط قبل الحذف = {m(m_with)}، وبعد الحذف = {m(m_without)}، فمقدار النقصان = {m(ans)}.",
                ],
                f"التحقق: {m(f'{m_with} - {m_without} = {ans}')}.",
                diagram_en=svg_nafes_box_plot(sr[0], sr[1], sr[2], sr[3], sr[4], f"Outlier = {sr[4]}"),
            )
    # 2 more Hard conceptual/analytical outlier items
    B.add_bilingual(
        tp, "Hard", bp,
        f"A Grade 6 student's reading times (in minutes) are {m('20, 21, 22, 22, 85')}. Which measure of center **best represents** the typical daily reading time without being distorted by the outlier {m(85)}?",
        f"أوقات القراءة اليومية لطالب في الصف السادس (بالدقائق) هي {m('20، 21، 22، 22، 85')}. أي مقاييس النزعة المركزية **يمثّل البيانات بصورة أفضل** دون أن يتشوه بالقيمة المتطرفة {m(85)}؟",
        [
            ("Median (22 minutes)", "الوسيط (22 دقيقة)"),
            ("Mean (34 minutes)", "المتوسط الحسابي (34 دقيقة)"),
            ("Range (65 minutes)", "المدى (65 دقيقة)"),
            ("Maximum (85 minutes)", "القيمة العظمى (85 دقيقة)"),
        ],
        0,
        "A single extreme outlier pulls the mean up to 34, whereas the median stays right in the cluster at 22!",
        "القيمة المتطرفة ترفع المتوسط إلى 34، بينما يبقى الوسيط (22) داخل تجمّع القيم اليومية المعتادة!",
        "When data have a strong outlier, the median is the most representative measure of center.",
        [
            f"Mean = {m('170 \\div 5 = 34')} min (higher than 4 out of 5 days!).",
            f"Median = {m(22)} min, accurately reflecting the typical 20–22 min cluster.",
        ],
        "Median resists outliers; range is a measure of spread, not center.",
        "الوسيط هو المقياس الأنسب للنزعة المركزية عند وجود قيم متطرفة بعيدة.",
        [
            f"المتوسط الحسابي {m(34)} يتأثر بشدة بالقيمة {m(85)}، بينما يبقى الوسيط {m(22)} ممثلاً دقيقاً.",
        ],
        "الاختيار الصحيح هو الوسيط (22 دقيقة).",
        diagram_en=svg_nafes_box_plot(20, 20.5, 22, 22, 85, "Cluster 20-22 vs Outlier 85"),
    )
    B.add_bilingual(
        tp, "Hard", bp,
        f"If the high outlier {m(90)} is added to the sorted data {m('14, 15, 15, 16, 18')}, what happens to the **mean** and the **mode**?",
        f"إذا أُضيفت القيمة المتطرفة {m(90)} إلى البيانات المرتبة {m('14، 15، 15، 16، 18')}، فماذا يحدث لكلٍّ من **المتوسط الحسابي** و**المنوال**؟",
        [
            ("The mean increases sharply, while the mode stays 15", "يزداد المتوسط الحسابي بوضوح، ويبقى المنوال 15 دون تغير"),
            ("Both the mean and the mode increase sharply", "يزداد كلٌّ من المتوسط الحسابي والمنوال بوضوح"),
            ("The mean stays the same, while the mode becomes 90", "يبقى المتوسط الحسابي ثابتاً، ويصبح المنوال 90"),
            ("The mean decreases, while the mode stays 15", "ينقص المتوسط الحسابي، ويبقى المنوال 15"),
        ],
        0,
        "Adding a large number pulls the sum (and mean) up, but 15 still appears twice while 90 appears only once!",
        "إضافة عدد كبير ترفع المتوسط الحسابي، أما العدد 15 فيظل هو الوحيد المتكرر مرتين!",
        "Check both formulas: mean changes from 15.6 to 28, whereas 15 remains the only repeated value.",
        [
            f"New mean = {m('(78 + 90) \\div 6 = 28')} (up from {m('15.6')}).",
            f"Value {m(15)} still occurs twice and {m(90)} once, so the mode remains {m(15)}.",
        ],
        "Mean rises from 15.6 to 28; mode stays 15.",
        "نحسب أثر القيمة الكبيرة في المجموع وفي التكرار.",
        [
            f"يرتفع المتوسط الحسابي إلى {m(28)}، بينما يظل المنوال {m(15)} لأنه الأكثر تكراراً.",
        ],
        "يزداد المتوسط بوضوح ويبقى المنوال 15.",
        diagram_en=svg_nafes_box_plot(14, 15, 15.5, 18, 90, "Adding Outlier 90"),
    )


def _add_dat_03(B: G6BankBuilder) -> None:
    tp, bp = "Data & Probability", "G6-DAT-03"
    # 5 Easy: Missing % sector & basic count from pie chart
    easy_pie = [
        ("miss_p", [("Football 35%", 35), ("Swimming 25%", 25), ("Basketball 22%", 22), ("Tennis ?%", 18)], 18, "sports survey", "استبانة الرياضة"),
        ("miss_p", [("Dates 42%", 42), ("Figs 18%", 18), ("Pomegranates 24%", 24), ("Grapes ?%", 16)], 16, "harvest chart", "مخطط المحاصيل"),
        ("count", [("Science 30%", 30), ("History 25%", 25), ("Stories 35%", 35), ("Poetry 10%", 10)], 240, 30, 72, "library books", "كتب المكتبة"),
        ("count", [("Bus 45%", 45), ("Car 35%", 35), ("Walking 20%", 20)], 160, 20, 32, "students walking to school", "طلاب يمشون للمدرسة"),
        ("count", [("Robotics 40%", 40), ("Coding 30%", 30), ("Chess 20%", 20), ("Art 10%", 10)], 150, 40, 60, "STEM club members", "أعضاء نادي الروبوت"),
    ]
    for row in easy_pie:
        if row[0] == "miss_p":
            _, slices, ans, ctx_en, ctx_ar = row
            known_s = 100 - ans
            B.add_math(
                tp, "Easy", bp,
                f"In a circle pie chart for a {ctx_en}, three sectors represent {m(f'{slices[0][1]}\\%')}, {m(f'{slices[1][1]}\\%')}, and {m(f'{slices[2][1]}\\%')}. What **percentage** represents the fourth sector?",
                f"في قطاع دائري لـ ({ctx_ar})، تمثّل ثلاثة قطاعات النسب {m(f'{slices[0][1]}\\%')} و{m(f'{slices[1][1]}\\%')} و{m(f'{slices[2][1]}\\%')}. ما **النسبة المئوية** للقطاع الرابع؟",
                ans, [360 - known_s, ans + 10, abs(ans - 6)],
                "All percentage sectors of a pie chart sum to 100%.",
                "مجموع النسب المئوية لجميع القطاعات الدائرية يساوي 100%.",
                f"Subtract {m(f'{known_s}\\%')} from {m('100\\%')}.",
                [f"{m(f'100\\% - {known_s}\\% = {ans}\\%')}."],
                f"Total = {m(f'{known_s}\\% + {ans}\\% = 100\\%')}.",
                "نطرح مجموع النسب المعلومة من 100%.",
                [f"النسبة المتبقية = {m(f'100\\% - {known_s}\\% = {ans}\\%')}."],
                f"مجموع النسب الأربع يساوي {m('100\\%')}.",
                suffix="\\%",
                diagram_en=svg_nafes_pie_chart(slices, ctx_en.title()),
            )
        else:
            _, slices, tot_n, pct, ans, ctx_en, ctx_ar = row
            B.add_math(
                tp, "Easy", bp,
                f"A pie chart of {m(tot_n)} total items shows that {m(f'{pct}\\%')} are {ctx_en}. How many items are in that sector?",
                f"يبيّن تمثيل بالقطاعات الدائرية لعدد كلي قدره {m(tot_n)} أن نسبة ({ctx_ar}) هي {m(f'{pct}\\%')}. فما العدد في هذا القطاع؟",
                ans, [pct, tot_n - ans, ans + 12],
                f"Compute {pct}% of {tot_n} = ({pct}/100) × {tot_n}.",
                f"احسب {pct}% من {tot_n} أي ({pct}/100) × {tot_n}.",
                f"Multiply {m(f'\\frac{{{pct}}}{{100}}')} by {m(tot_n)}.",
                [f"{m(f'\\frac{{{pct}}}{{100}} \\times {tot_n} = {ans}')}."],
                f"{m(f'\\frac{{{ans}}}{{{tot_n}}} = {pct}\\%')}.",
                f"نضرب النسبة المئوية في العدد الكلي {m(tot_n)}.",
                [f"العدد = {m(f'\\frac{{{pct}}}{{100}} \\times {tot_n} = {ans}')}."],
                f"نسبة {m(ans)} إلى {m(tot_n)} هي {m(f'{pct}\\%')}.",
                diagram_en=svg_nafes_pie_chart(slices, f"Total = {tot_n}"),
            )

    # 5 Medium: Central angle of a pie-chart sector (360°) & difference between two sectors
    med_pie = [
        ("ang", 25, 90, [("Water 25%", 25), ("Juice 35%", 35), ("Milk 40%", 40)], "school cafeteria drinks", "مشروبات المقصف"),
        ("ang", 35, 126, [("Solar 35%", 35), ("Wind 25%", 25), ("Gas 40%", 40)], "clean energy project", "مشروع الطاقة النظيفة"),
        ("ang", 15, 54, [("Art 15%", 15), ("STEM 45%", 45), ("Sports 40%", 40)], "club enrollment", "التسجيل في الأندية"),
        ("diff", 300, 42, 26, 48, [("Riyadh 42%", 42), ("Jeddah 32%", 32), ("Dammam 26%", 26)], "contest finalists", "المتأهلون للمسابقة"),
        ("diff", 250, 44, 24, 50, [("Buses 44%", 44), ("Vans 32%", 32), ("Cars 24%", 24)], "transport survey", "وسائل النقل"),
    ]
    for row in med_pie:
        if row[0] == "ang":
            _, pct, ans, slices, ctx_en, ctx_ar = row
            B.add_math(
                tp, "Medium", bp,
                f"In a pie chart for {ctx_en}, a sector represents {m(f'{pct}\\%')} of the data. What is the **central angle** of this sector in degrees?",
                f"في تمثيل بالقطاعات الدائرية لـ ({ctx_ar})، يمثّل أحد القطاعات نسبة {m(f'{pct}\\%')} من البيانات. ما قياس **الزاوية المركزية** لهذا القطاع بالدرجات؟",
                ans, [pct, 180 - ans if 180 - ans != ans else 120, (pct * 180) // 100 or 45],
                f"Multiply {pct}/100 by 360° (a full circle is 360°!).",
                f"اضرب {pct}/100 في 360° (لأن مجموع زوايا الدائرة 360°!).",
                f"Compute {m(f'\\frac{{{pct}}}{{100}} \\times 360^\\circ')}.",
                [f"Central angle = {m(f'\\frac{{{pct}}}{{100}} \\times 360^\\circ = {ans}^\\circ')}."],
                f"{m(f'\\frac{{{ans}}}{{360}} = \\frac{{{pct}}}{{100}}')}.",
                f"نضرب النسبة {m(f'\\frac{{{pct}}}{{100}}')} في {m('360^\\circ')}.",
                [f"الزاوية المركزية = {m(f'\\frac{{{pct}}}{{100}} \\times 360^\\circ = {ans}^\\circ')}."],
                f"نسبة الزاوية {m(ans)} إلى {m(360)} تساوي {m(f'{pct}\\%')}.",
                diagram_en=svg_nafes_pie_chart(slices, "360° Circle"),
            )
        else:
            _, tot_n, p1, p2, ans, slices, ctx_en, ctx_ar = row
            B.add_math(
                tp, "Medium", bp,
                f"In a pie chart of {m(tot_n)} {ctx_en}, Sector A is {m(f'{p1}\\%')} and Sector C is {m(f'{p2}\\%')}. How many **more** items are in Sector A than in Sector C?",
                f"في تمثيل بالقطاعات الدائرية يشمل {m(tot_n)} من ({ctx_ar})، تبلغ نسبة القطاع الأول {m(f'{p1}\\%')} والقطاع الثالث {m(f'{p2}\\%')}. بكم **يزيد** عدد القطاع الأول على القطاع الثالث؟",
                ans, [p1 - p2, (tot_n * p1) // 100, (tot_n * p2) // 100],
                f"Subtract percentages ({p1}% − {p2}% = {p1-p2}%) and multiply by {tot_n}!",
                f"اطرح النسبتين ({p1}% − {p2}% = {p1-p2}%) ثم اضرب الناتج في {tot_n}!",
                f"Take {m(f'{p1 - p2}\\%')} of {m(tot_n)}.",
                [
                    f"Percentage difference = {m(f'{p1}\\% - {p2}\\% = {p1 - p2}\\%')}.",
                    f"Count difference = {m(f'\\frac{{{p1 - p2}}}{{100}} \\times {tot_n} = {ans}')}.",
                ],
                f"{m(f'{(tot_n * p1)//100} - {(tot_n * p2)//100} = {ans}')}.",
                "نوجد فرق النسبتين المئويتين ثم نضربه في العدد الكلي.",
                [
                    f"فرق النسبتين = {m(f'{p1 - p2}\\%')}، وفرق العدد = {m(f'\\frac{{{p1 - p2}}}{{100}} \\times {tot_n} = {ans}')}.",
                ],
                f"التحقق: {m(f'{(tot_n * p1)//100} - {(tot_n * p2)//100} = {ans}')}.",
                diagram_en=svg_nafes_pie_chart(slices, f"Total = {tot_n}"),
            )

    # 5 Hard: Reverse pie-chart reasoning from central angles (72°, 90°, 108°, 120°, 144°)
    hard_pie = [
        (72, 36, 180, "total students surveyed", "إجمالي الطلاب المشاركين"),      # 72/360 = 1/5 -> 36*5 = 180
        (90, 45, 180, "total books donated", "إجمالي الكتب المتبرع بها"),          # wait 180 again? Let's make 90° = 65 -> 260!
        (120, 80, 240, "total saplings planted", "إجمالي الشتلات المزروعة"),       # 120/360 = 1/3 -> 240
        (108, 54, 180, "total museum tickets", "إجمالي تذاكر المتحف"),             # let's make 108° = 90 -> 300!
        (144, 96, 240, "total science projects", "إجمالي المشاريع العلمية"),       # 144/360 = 2/5 -> 96 * 5/2 = 240
    ]
    hard_pie[1] = (90, 65, 260, "total books donated", "إجمالي الكتب المتبرع بها")
    hard_pie[3] = (108, 90, 300, "total museum tickets", "إجمالي تذاكر المتحف")
    for deg, part_cnt, ans, ask_en, ask_ar in hard_pie:
        frac = Fraction(deg, 360)
        assert part_cnt / frac == ans
        B.add_math(
            tp, "Hard", bp,
            f"In a circle pie chart, a sector with central angle {m(f'{deg}^\\circ')} represents {m(part_cnt)} items. What is the **{ask_en}** across the entire circle?",
            f"في تمثيل بالقطاعات الدائرية، يمثّل قطاع زاويته المركزية {m(f'{deg}^\\circ')} عدد {m(part_cnt)} مفردة. فما **({ask_ar})** في الدائرة كاملة؟",
            ans, [deg + part_cnt, (part_cnt * 100) // deg if (part_cnt * 100) // deg != ans else ans - 40, ans + 40],
            f"A {deg}° sector is {deg}/360 = {frac.numerator}/{frac.denominator} of the whole circle!",
            f"القطاع ذو الزاوية {deg}° يمثّل الكسر {deg}/360 = {frac.numerator}/{frac.denominator} من الدائرة كاملة!",
            f"Set {m(f'\\frac{{{deg}}}{{360}} \\times T = {part_cnt}')} and solve for {m('T')}.",
            [
                f"Fraction of circle = {m(f'\\frac{{{deg}}}{{360}} = \\frac{{{frac.numerator}}}{{{frac.denominator}}}')}.",
                f"Total {m(f'T = {part_cnt} \\times \\frac{{{frac.denominator}}}{{{frac.numerator}}} = {ans}')}.",
            ],
            f"{m(f'\\frac{{{deg}}}{{360}} \\times {ans} = {part_cnt}')}.",
            f"نحسب الكسر الذي يمثله القطاع ({m(f'\\frac{{{deg}}}{{360}}')}) ثم نوجد العدد الكلي.",
            [
                f"نسبة القطاع من الدائرة = {m(f'\\frac{{{frac.numerator}}}{{{frac.denominator}}}')}، إذن العدد الكلي = {m(f'{part_cnt} \\times \\frac{{{frac.denominator}}}{{{frac.numerator}}} = {ans}')}.",
            ],
            f"التحقق: {m(f'\\frac{{{deg}}}{{360}} \\times {ans} = {part_cnt}')}.",
            diagram_en=svg_nafes_pie_chart([(f"{deg}° ({part_cnt})", deg), ("Rest", 360 - deg)], "Total = ?"),
        )


def _add_dat_04(B: G6BankBuilder) -> None:
    tp, bp = "Data & Probability", "G6-DAT-04"
    # 5 Easy: Simple theoretical probability P(E) in simplest form
    easy_pr = [
        (["R", "R", "B", "B", "B", "G"], "R", Fraction(1, 3), "6-sector spinner landing on R"),
        (["1", "2", "3", "4", "5", "6", "7", "8"], "multiple of 3", Fraction(1, 4), "8-sector spinner landing on a multiple of 3"),
        (["A", "A", "A", "B", "B", "C", "C", "D"], "A", Fraction(3, 8), "8-sector spinner landing on A"),
        (["G", "G", "Y", "Y", "Y", "Y", "B", "B"], "Y", Fraction(1, 2), "8-sector spinner landing on Y"),
        (["2", "3", "4", "5", "6", "7"], "prime", Fraction(1, 2), "spinner {2,3,4,5,6,7} landing on a prime number"),
    ]
    ar_targets = ["الحرف R", "مضاعف للعدد 3", "الحرف A", "الحرف Y", "عدد أولي"]
    for (sectors, target_en, ans, _), target_ar in zip(easy_pr, ar_targets):
        n_tot = len(sectors)
        fav = int(ans * n_tot)
        dists = [Fraction(n_tot - fav, n_tot) if Fraction(n_tot - fav, n_tot) != ans else Fraction(1, n_tot), Fraction(fav, n_tot - fav), Fraction(1, n_tot)]
        B.add_math(
            tp, "Easy", bp,
            f"An equal-sector spinner has labels {m(', '.join(sectors))}. What is the probability in simplest form that it lands on **{target_en}**?",
            f"قرص دوّار مقسّم إلى قطاعات متطابقة تحمل الرموز {m('، '.join(sectors))}. ما احتمال وقوف المؤشر على **({target_ar})** في أبسط صورة؟",
            ans, dists,
            f"Count favorable sectors ({fav}) out of {n_tot} total equal sectors, then simplify!",
            f"عدّ القطاعات المواتية ({fav}) من أصل {n_tot} قطاعات متطابقة، ثم بسّط الكسر!",
            f"Form {m(f'P(E) = \\frac{{{fav}}}{{{n_tot}}}')} and simplify.",
            [
                f"There are {m(fav)} favorable outcomes out of {m(n_tot)} equally likely sectors.",
                f"Probability = {m(f'\\frac{{{fav}}}{{{n_tot}}} = {_mx(ans)}')}.",
            ],
            f"{m(_mx(ans))} lies between {m(0)} and {m(1)} and is in lowest terms.",
            f"نقسم عدد النواتج المواتية ({m(fav)}) على العدد الكلي ({m(n_tot)}) ونبسّط.",
            [
                f"الاحتمال = {m(f'\\frac{{{fav}}}{{{n_tot}}} = {_mx(ans)}')}.",
            ],
            f"الكسر {m(_mx(ans))} في أبسط صورة.",
            diagram_en=svg_nafes_spinner(sectors, f"n = {n_tot}"),
        )

    # 5 Medium: Complementary probability 1 - P(E) & 2-stage Fundamental Counting Principle (m × n)
    med_pr = [
        ("comp", 5, 8, 7, "red", "حمراء", ["R"] * 5 + ["B", "G", "Y"]), # 5 red, 8 blue, 7 green = 20 total -> P(not red) = 15/20 = 3/4
        ("comp", 4, 6, 6, "blue", "زرقاء", ["B", "B", "G", "G", "G", "Y", "Y", "Y"]), # 4,6,6 = 16 -> P(not blue) = 12/16 = 3/4 -> let's vary: 6,5,4=15 -> P(not blue)=9/15=3/5!
        ("fcp", 4, "thobe styles", "موديلات ثياب", 5, "ghutra patterns", "أنواع شماغ"),
        ("fcp", 6, "sandwiches", "شطائر", 4, "fresh juices", "عصائر طازجة"),
        ("fcp", 3, "notebook colors", "ألوان دفاتر", 8, "pen types", "أنواع أقلام"),
    ]
    med_pr[1] = ("comp", 6, 5, 4, "blue", "زرقاء", ["B", "B", "G", "G", "Y"])
    for row in med_pr:
        if row[0] == "comp":
            _, c1, c2, c3, col_en, col_ar, sp_lbls = row
            tot = c1 + c2 + c3
            ans = Fraction(tot - c1, tot)
            B.add_math(
                tp, "Medium", bp,
                f"A bag contains {m(c1)} {col_en} marbles, {m(c2)} green marbles, and {m(c3)} yellow marbles. If one marble is drawn at random, what is the probability that it is **NOT {col_en}** (in simplest form)?",
                f"يحتوي كيس على {m(c1)} كرات {col_ar} و{m(c2)} كرات خضراء و{m(c3)} كرات صفراء. عند سحب كرة واحدة عشوائياً، ما احتمال أن تكون **غير {col_ar}** في أبسط صورة؟",
                ans, [Fraction(c1, tot), Fraction(c1, tot - c1), Fraction(c2, tot)],
                f"Find total marbles ({tot}), subtract {c1} {col_en} marbles to get {tot - c1}, and simplify ({tot - c1})/{tot}.",
                f"أوجد العدد الكلي للكرات ({tot})، واطرح {c1} كرة {col_ar} ليبقى {tot - c1}، ثم بسّط الكسر ({tot - c1})/{tot}.",
                f"Use the complement {m(f'1 - \\frac{{{c1}}}{{{tot}}} = \\frac{{{tot - c1}}}{{{tot}}}')}.",
                [
                    f"Total marbles = {m(f'{c1} + {c2} + {c3} = {tot}')}.",
                    f"Marbles NOT {col_en} = {m(f'{tot} - {c1} = {tot - c1}')}, giving {m(f'\\frac{{{tot - c1}}}{{{tot}}} = {_mx(ans)}')}.",
                ],
                f"{m(f'\\frac{{{c1}}}{{{tot}}} + {_mx(ans)} = 1')}.",
                "نستعمل الحادثة المتممة بقسمة عدد الكرات الباقية على العدد الكلي.",
                [
                    f"مجموع الكرات = {m(tot)}، وغير ال{col_ar} = {m(tot - c1)}، فالاحتمال = {m(_mx(ans))}.",
                ],
                f"مجموع احتمال الحادثة ومتممتها يساوي {m(1)}.",
                diagram_en=svg_nafes_spinner(sp_lbls, f"Total = {tot}"),
            )
        else:
            _, m_c, i1_en, i1_ar, n_c, i2_en, i2_ar = row
            ans = m_c * n_c
            B.add_math(
                tp, "Medium", bp,
                f"A choice offers {m(m_c)} {i1_en} and {m(n_c)} {i2_en}. By the Fundamental Counting Principle, how many distinct pairs of one item from each group exist?",
                f"يتيح عرض اختيار واحد من {m(m_c)} ({i1_ar}) مع واحد من {m(n_c)} ({i2_ar}). باستعمال مبدأ العد الأساسي، كم زوجاً مختلفاً في فضاء العينة؟",
                ans, [m_c + n_c, 2 * (m_c + n_c), ans + m_c],
                f"Multiply {m_c} × {n_c} (do NOT add {m_c} + {n_c}!).",
                f"اضرب عدد الخيارات {m_c} × {n_c} (ولا تجمع {m_c} + {n_c}!).",
                f"Apply the Fundamental Counting Principle: {m(f'{m_c} \\times {n_c}')}.",
                [f"Total sample-space outcomes = {m(f'{m_c} \\times {n_c} = {ans}')}."],
                f"Each of the {m(m_c)} first choices pairs with {m(n_c)} second choices.",
                f"نضرب عدد خيارات المرحلة الأولى في عدد خيارات المرحلة الثانية.",
                [f"عدد النواتج الممكنة = {m(f'{m_c} \\times {n_c} = {ans}')}."],
                f"كل خيار من الـ {m(m_c)} يقترن بـ {m(n_c)} خيارات.",
                diagram_en=svg_nafes_function_table(["Choice 1", "Choice 2", "Total Pairs"], [[str(m_c), str(n_c), "?"]], highlight_cell=(0, 2)),
            )

    # 5 Hard: 3-stage counting principle, coin+die sample space, & adding marbles to hit target probability
    hard_pr = [
        ("fcp3", 3, 4, 2, "school lunch menu (3 soups, 4 mains, 2 fruits)", "وجبة مدرسية (3 حساء، 4 أطباق رئيسية، 2 فاكهة)"),
        ("fcp3", 2, 6, 5, "tossing a coin, rolling a 6-sided die, and spinning a 5-sector wheel", "رمي قطعة نقد ومكعب أرقام (1–6) وتدوير قرص من 5 قطاعات"),
        ("fcp3", 4, 3, 3, "robotics badge design (4 shapes, 3 borders, 3 colors)", "تصميم شعار نادي الروبوت (4 أشكال، 3 إطارات، 3 ألوان)"),
        ("add_m", 3, 9, 6, "blue", "زرقاء"),  # 3 blue, 9 red -> add x=6 blue so (3+6)/(12+6) = 9/18 = 1/2
        ("add_m", 4, 12, 8, "green", "خضراء"), # 4 green, 12 white -> add x=8 green so 12/24 = 1/2
    ]
    for row in hard_pr:
        if row[0] == "fcp3":
            _, c1, c2, c3, ctx_en, ctx_ar = row
            ans = c1 * c2 * c3
            B.add_math(
                tp, "Hard", bp,
                f"How many total outcomes are in the sample space for a {ctx_en}?",
                f"ما العدد الكلي للنواتج الممكنة في فضاء العينة عند ({ctx_ar})؟",
                ans, [c1 + c2 + c3, c1 * c2 + c3, ans + c2],
                f"Multiply all three stage counts: {c1} × {c2} × {c3}.",
                f"اضرب أعداد الخيارات في المراحل الثلاث: {c1} × {c2} × {c3}.",
                f"Apply the 3-stage Fundamental Counting Principle: {m(f'{c1} \\times {c2} \\times {c3}')}.",
                [f"Sample-space size = {m(f'{c1} \\times {c2} \\times {c3} = {ans}')} outcomes."],
                f"{m(f'{c1 * c2} \\times {c3} = {ans}')}.",
                "نضرب عدد خيارات المراحل الثلاث معاً.",
                [f"حجم فضاء العينة = {m(f'{c1} \\times {c2} \\times {c3} = {ans}')} ناتجاً."],
                f"التحقق: {m(f'{c1 * c2} \\times {c3} = {ans}')}.",
                diagram_en=svg_nafes_function_table(["Stage 1", "Stage 2", "Stage 3", "Sample Space"], [[str(c1), str(c2), str(c3), "?"]], highlight_cell=(0, 3)),
            )
        else:
            _, fav0, oth0, ans, col_en, col_ar = row
            B.add_math(
                tp, "Hard", bp,
                f"A box holds {m(fav0)} {col_en} balls and {m(oth0)} other balls. How many **additional {col_en} balls** must be added so the probability of drawing a {col_en} ball becomes exactly {m('\\frac{1}{2}')}?",
                f"يحتوي صندوق على {m(fav0)} كرات {col_ar} و{m(oth0)} كرات من ألوان أخرى. كم **كرة {col_ar} إضافية** يجب وضعها ليصبح احتمال سحب كرة {col_ar} مساوياً لـ {m('\\frac{1}{2}')} تماماً؟",
                ans, [(oth0 - fav0) // 2, oth0, ans + 2],
                f"For probability 1/2, the number of {col_en} balls must equal the {oth0} other balls!",
                f"لكي يصبح الاحتمال 1/2، يجب أن يتساوى عدد الكرات ال{col_ar} مع الكرات الأخرى وعددها {oth0}!",
                f"Match the {col_en} count to the {m(oth0)} non-{col_en} balls: {m(f'{fav0} + x = {oth0}')}.",
                [
                    f"Probability {m('\\frac{1}{2}')} occurs when {col_en} balls equal non-{col_en} balls ({m(oth0)}).",
                    f"Solve {m(f'{fav0} + x = {oth0} \\implies x = {ans}')}.",
                ],
                f"New bag has {m(fav0 + ans)} {col_en} out of {m(fav0 + oth0 + ans)} total, and {m(f'\\frac{{{fav0 + ans}}}{{{fav0 + oth0 + ans}}} = \\frac{{1}}{{2}}')}.",
                f"يتحقق الاحتمال {m('\\frac{1}{2}')} عندما يتساوى عدد الكرات ال{col_ar} مع غيرها ({m(oth0)}).",
                [
                    f"نحل {m(f'{fav0} + x = {oth0}')} فنحصل على {m(f'x = {ans}')} كرات إضافية.",
                ],
                f"يصبح العدد {m(oth0)} من أصل {m(2 * oth0)} أي {m('\\frac{1}{2}')}.",
                diagram_en=svg_nafes_spinner(["★"] * fav0 + ["○"] * min(5, oth0), f"Target P = 1/2"),
            )


def build_grade6_bank() -> list[dict]:
    B = G6BankBuilder()
    for fn in (
        _add_num_01, _add_num_02, _add_num_03, _add_num_04,
        _add_num_05, _add_num_06, _add_num_07, _add_num_08,
        _add_alg_01, _add_alg_02, _add_alg_03, _add_alg_04,
        _add_geo_01, _add_geo_02, _add_geo_03, _add_geo_04,
        _add_geo_05, _add_geo_06, _add_geo_07, _add_geo_08,
        _add_dat_01, _add_dat_02, _add_dat_03, _add_dat_04,
    ):
        fn(B)
    assert len(B.items) == 360, f"Expected 360 Grade 6 items, got {len(B.items)}"
    return B.items
