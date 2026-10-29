"""KAUST Mathematics Competition (KMC) — Track 1: Grades 6-7
Pillar 1: Numbers, Fractions, Ratios, Percentages & Introductory Number Theory (120 questions).
Strictly aligned with official KMC Grades 6-7 syllabus (no calculators).
"""
from fractions import Fraction
import math
from kmc_common import m, explain_en, explain_ar, make_5_math_options, make_5_bilingual_options, make_kmc_question
from kmc_diagrams import svg_column_cryptarithm, svg_water_cups

LEVEL = "Track 1: Grades 6-7"


def generate_t1_numbers() -> list[dict]:
    items = []
    idx = 1

    def next_id():
        nonlocal idx
        qid = f"KAUST-G67-N{idx:03d}"
        idx += 1
        return qid

    # 1. Flashing lights / bells / fountains LCM cycles (8 variants) — KMC G6-7 Sample Q1
    lcm_cases = [
        (12, 18, 3, "Two courtyard beacons at KAUST flash together at 8:00:00", "مصباحا إرشاد في ساحة كاوست يومضان معًا عند الساعة 8:00:00 تمامًا", "flashes", "يومض"),
        (10, 15, 4, "Two school bells chime together at 9:00:00", "جرسان مدرسيان يدقان معًا عند الساعة 9:00:00 تمامًا", "chimes", "يدق"),
        (8, 12, 2, "Two garden sprinklers spray water together at 7:00:00", "رشّاشا مياه في حديقة يعملان معًا عند الساعة 7:00:00 تمامًا", "sprays", "يعمل"),
        (15, 20, 5, "Two lighthouse lamps blink together at midnight", "منارتان بحريتان تومضان معًا عند منتصف الليل تمامًا", "blinks", "تومض"),
        (6, 9, 3, "Two digital timers beep together at 10:00:00", "مؤقّتان رقميان يصدران صافرة معًا عند الساعة 10:00:00 تمامًا", "beeps", "يصدر صافرة"),
        (9, 12, 3, "Two decorative fountains jet upward together at 6:00:00", "نافورتان تندفعان معًا عند الساعة 6:00:00 تمامًا", "jets", "تندفع"),
        (14, 21, 7, "Two laboratory sensors pulse together at 11:00:00", "حسّاسان في المختبر ينبضان معًا عند الساعة 11:00:00 تمامًا", "pulses", "ينبض"),
        (16, 24, 4, "Two traffic warning lights flash together at noon", "إشارتان تحذيريتان تومضان معًا عند الظهر تمامًا", "flashes", "تومض"),
    ]
    for a, b, mins, intro_en, intro_ar, verb_en, verb_ar in lcm_cases:
        qid = next_id()
        L = math.lcm(a, b)
        tot_sec = mins * 60
        assert tot_sec % L == 0
        ans = tot_sec // L
        mults_a = ", ".join(str(a * k) for k in range(1, L // a + 1))
        mults_b = ", ".join(str(b * k) for k in range(1, L // b + 1))
        q_en = (
            f"{intro_en}. The first {verb_en} every {m(a)} seconds and the second every {m(b)} seconds. "
            f"How many times do they happen together during the next {m(mins)} minutes (not counting the starting moment)?"
        )
        q_ar = (
            f"{intro_ar}؛ الأول {verb_ar} كل {m(a)} ثانية والثاني كل {m(b)} ثانية. "
            f"كم مرة يحدث ذلك معًا خلال الـ {m(mins)} دقائق التالية (دون احتساب لحظة البداية)؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 1, ans - 1, tot_sec // a, tot_sec // b, ans + 2], qid
        )
        sol_en = explain_en(
            f"Both events happen at the same time whenever the number of seconds is a multiple of both {m(a)} and {m(b)}. The first shared time is their Least Common Multiple (LCM).",
            [
                f"List multiples of each interval to find the first match: multiples of {m(a)} are {m(mults_a)}, and multiples of {m(b)} are {m(mults_b)}. So they coincide every {m(L)} seconds.",
                f"Convert {m(mins)} minutes into seconds using {m('1\\text{ min} = 60\\text{ s}')}: {m(f'{mins} \\times 60 = {tot_sec}')} seconds.",
                f"Divide the total time by the cycle length: {m(f'{tot_sec} \\div {L} = {ans}')}. Because the starting moment is excluded, we do not add {m(1)}.",
            ],
            f"The shared moments occur at {m(L)}, {m(2*L)}, ..., up to {m(tot_sec)} seconds, giving exactly {m(ans)} times.",
        )
        sol_ar = explain_ar(
            f"يتكرر الحدثان معًا عندما يكون عدد الثواني مضاعفًا مشتركًا للعددين {m(a)} و {m(b)} معًا، وأول التقاء بعد البداية هو المضاعف المشترك الأصغر لهما.",
            [
                f"نكتب أول مضاعفات العددين لإيجاد أول عدد مشترك: مضاعفات {m(a)} هي {m(mults_a)}، ومضاعفات {m(b)} هي {m(mults_b)}. إذن يلتقيان كل {m(L)} ثانية.",
                f"نحوّل الدقائق إلى ثوانٍ بضربها في {m(60)}: {m(f'{mins} \\times 60 = {tot_sec}')} ثانية.",
                f"نقسم الزمن الكلي على طول الدورة الواحدة: {m(f'{tot_sec} \\div {L} = {ans}')} مرات (ولا نضيف {m(1)} لأن لحظة البداية غير محتسبة).",
            ],
            f"الأزمنة المشتركة هي مضاعفات {m(L)} حتى {m(tot_sec)} ثانية، وعددها بالضبط {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-lcm-cycles",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"First find the smallest number of seconds divisible by both {a} and {b}, then convert {mins} minutes into seconds.",
            f"أولًا أوجد أصغر عدد من الثواني يقبل القسمة على {a} و {b} معًا، ثم حوّل {mins} دقائق إلى ثوانٍ.",
            sol_en, sol_ar
        ))

    # 2. Mixing juice / paint / trail-mix in ratio a : b (8 variants) — KMC G6-7 Sample Q3
    ratio_cases = [
        (2, 5, 21, "Juice is made by mixing berry concentrate and water", "concentrate", "liters", "يُحضّر عصير بخلط شراب التوت المركّز والماء", "المركّز", "لترًا"),
        (3, 7, 30, "Lemonade is prepared by mixing lemon juice and water", "lemon juice", "liters", "يُحضّر عصير الليمون بخلط عصير الليمون الصافي والماء", "عصير الليمون الصافي", "لترًا"),
        (2, 3, 25, "Green paint is made by mixing blue paint and yellow paint", "blue paint", "liters", "يُحضّر طلاء أخضر بخلط الطلاء الأزرق والطلاء الأصفر", "الطلاء الأزرق", "لترًا"),
        (3, 5, 32, "A smoothie is made by blending mango puree and milk", "mango puree", "cups", "يُحضّر مشروب بخلط مهروس المانجو والحليب", "مهروس المانجو", "كوبًا"),
        (4, 5, 45, "A concrete mix combines cement and sand", "cement", "kilograms", "تُحضّر خلطة إسمنتية بمزج الإسمنت والرمل", "الإسمنت", "كجم"),
        (1, 4, 35, "Rose syrup drink is made by mixing rose syrup and cold water", "rose syrup", "liters", "يُحضّر شراب الورد بخلط مركز الورد والماء البارد", "مركز الورد", "لترًا"),
        (3, 4, 28, "A snack mix combines almonds and raisins", "almonds", "grams (in hundreds)", "تُحضّر خلطة مكسرات بمزج اللوز والزبيب", "اللوز", "علبة"),
        (5, 7, 48, "Orange punch is made by mixing orange juice and sparkling water", "orange juice", "liters", "يُحضّر شراب البرتقال بخلط عصير البرتقال والماء الفوار", "عصير البرتقال", "لترًا"),
    ]
    for a, b, tot, desc_en, part_en, unit_en, desc_ar, part_ar, unit_ar in ratio_cases:
        qid = next_id()
        parts_sum = a + b
        one_part = tot // parts_sum
        ans = a * one_part
        other = b * one_part
        q_en = (
            f"{desc_en} in a ratio of {m(f'{a} : {b}')}, respectively. "
            f"How many {unit_en} of {part_en} are needed to make {m(tot)} {unit_en} of the mixture?"
        )
        q_ar = (
            f"{desc_ar} بنسبة {m(f'{a} : {b}')} على الترتيب. "
            f"كم {unit_ar} من {part_ar} يلزم لتحضير {m(tot)} {unit_ar} من الخليط؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [other, one_part, ans + one_part, max(1, ans - 2), a + b], qid
        )
        sol_en = explain_en(
            f"A ratio of {m(f'{a} : {b}')} means that every batch is split into {m(f'{a} + {b} = {parts_sum}')} equal parts: {m(a)} parts of {part_en} and {m(b)} parts of the second ingredient.",
            [
                f"Add the ratio numbers to find the total number of equal parts: {m(f'{a} + {b} = {parts_sum}')} parts.",
                f"Find how much {m(1)} part represents by dividing the total amount by {m(parts_sum)}: {m(f'{tot} \\div {parts_sum} = {one_part}')}.",
                f"Multiply the size of {m(1)} part by {m(a)} (the share of {part_en}): {m(f'{a} \\times {one_part} = {ans}')}.",
            ],
            f"The second ingredient uses {m(f'{b} \\times {one_part} = {other}')}, and {m(f'{ans} + {other} = {tot}')}, matching the required total!",
        )
        sol_ar = explain_ar(
            f"النسبة {m(f'{a} : {b}')} تعني أن الخليط مقسّم إلى أجزاء متساوية مجموعها {m(f'{a} + {b} = {parts_sum}')} أجزاء، منها {m(a)} لـ{part_ar}.",
            [
                f"نجمع حدود النسبة لمعرفة العدد الكلي للأجزاء المتساوية: {m(f'{a} + {b} = {parts_sum}')} أجزاء.",
                f"نحسب قيمة الجزء الواحد بقسمة الكمية الكلية على مجموع الأجزاء: {m(f'{tot} \\div {parts_sum} = {one_part}')}.",
                f"نضرب قيمة الجزء الواحد في نصيب {part_ar} وهو {m(a)}: {m(f'{a} \\times {one_part} = {ans}')}.",
            ],
            f"المكوّن الثاني يساوي {m(f'{b} \\times {one_part} = {other}')}، والمجموع {m(f'{ans} + {other} = {tot}')} وهو المطلوب تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-ratio-mixture",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Add {a} + {b} to find how many equal parts make up the whole {tot}.",
            f"اجمع {a} + {b} لمعرفة عدد الأجزاء المتساوية التي تكوّن الكمية الكلية {tot}.",
            sol_en, sol_ar
        ))

    # 3. Counting natural numbers from 1 to N divisible by p or q (8 variants) — KMC G6-7 Sample Q7
    ie_cases = [
        (101, 3, 5), (85, 2, 5), (100, 3, 4), (95, 4, 5),
        (121, 3, 7), (73, 2, 3), (110, 4, 6), (91, 2, 7),
    ]
    for N, p, q in ie_cases:
        qid = next_id()
        L = math.lcm(p, q)
        cp, cq, cl = N // p, N // q, N // L
        ans = cp + cq - cl
        assert ans == sum(1 for x in range(1, N + 1) if x % p == 0 or x % q == 0)
        q_en = f"How many natural numbers from {m(1)} to {m(N)} (inclusive) are divisible by {m(p)} or by {m(q)}?"
        q_ar = f"كم عددًا طبيعيًا من {m(1)} إلى {m(N)} (شاملًا الطرفين) يقبل القسمة على {m(p)} أو على {m(q)}؟"
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [cp + cq, ans + cl, ans - cl, cp + cq - 2 * cl, ans + 2], qid
        )
        sol_en = explain_en(
            f"If we count multiples of {m(p)} and add multiples of {m(q)}, any number divisible by BOTH {m(p)} and {m(q)} gets counted twice—so we subtract those shared multiples once!",
            [
                f"Count multiples of {m(p)} up to {m(N)}: divide {m(N)} by {m(p)} and keep the whole-number quotient: {m(f'\\lfloor {N} \\div {p} \\rfloor = {cp}')} (since {m(f'{p} \\times {cp} = {p*cp}')}).",
                f"Count multiples of {m(q)} up to {m(N)}: {m(f'\\lfloor {N} \\div {q} \\rfloor = {cq}')} (since {m(f'{q} \\times {cq} = {q*cq}')}).",
                f"Numbers divisible by both {m(p)} and {m(q)} are multiples of {m(f'\\text{{LCM}}({p},{q}) = {L}')}. Up to {m(N)}, there are {m(f'\\lfloor {N} \\div {L} \\rfloor = {cl}')} such numbers.",
                f"Add the two counts and subtract the overlap once: {m(f'{cp} + {cq} - {cl} = {ans}')}.",
            ],
            f"Common trap: forgetting to subtract {m(cl)} gives {m(cp+cq)}, which double-counts {m(L)}, {m(2*L)}, etc. Subtracting once gives {m(ans)}.",
        )
        sol_ar = explain_ar(
            f"عند جمع عدد مضاعفات {m(p)} مع عدد مضاعفات {m(q)}، فإن الأعداد التي تقبل القسمة عليهما معًا تُحسب مرتين، لذا نطرح عددها مرة واحدة.",
            [
                f"عدد مضاعفات {m(p)} من {m(1)} إلى {m(N)} هو ناتج القسمة الصحيح لـ {m(N)} على {m(p)}: {m(cp)} عددًا (لأن {m(f'{p} \\times {cp} = {p*cp}')}).",
                f"عدد مضاعفات {m(q)} من {m(1)} إلى {m(N)} هو: {m(cq)} عددًا (لأن {m(f'{q} \\times {cq} = {q*cq}')}).",
                f"الأعداد التي تقبل القسمة على {m(p)} و {m(q)} معًا هي مضاعفات المضاعف المشترك الأصغر {m(L)}، وعددها حتى {m(N)} هو {m(cl)}.",
                f"نجمع ثم نطرح المكرر مرة واحدة: {m(f'{cp} + {cq} - {cl} = {ans}')}.",
            ],
            f"انتبه للخطأ الشائع: جمع {m(f'{cp} + {cq} = {cp+cq}')} دون طرح المكرر يحسب مضاعفات {m(L)} مرتين؛ إذن الجواب الصحيح هو {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-divisible-or",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Count multiples of {p}, count multiples of {q}, and subtract multiples of {L} so you don't count them twice.",
            f"احسب عدد مضاعفات {p} وعدد مضاعفات {q}، ثم اطرح عدد مضاعفات {L} حتى لا تحسبها مرتين.",
            sol_en, sol_ar
        ))

    # 4. Greatest number of gift bags / children — GCD word problems (8 variants) — KMC Junior Q8
    gcd_cases = [
        (36, 18, 24, "chocolates", "cupcakes", "candies", "children at a party", "قطعة شوكولاتة", "كعكة", "قطعة حلوى", "الأطفال في حفلة"),
        (48, 32, 40, "pencils", "erasers", "notebooks", "welcome kits", "قلم رصاص", "ممحاة", "دفترًا", "حقائب ترحيبية"),
        (45, 30, 75, "dates", "figs", "walnuts", "Ramadan gift boxes", "تمرة", "حبة تين", "حبة جوز", "علب هدايا رمضانية"),
        (56, 42, 28, "red marbles", "blue marbles", "green marbles", "identical pouches", "كرة حمراء", "كرة زرقاء", "كرة خضراء", "أكياس متماثلة"),
        (60, 36, 48, "tulips", "roses", "lilies", "identical bouquets", "زهرة توليب", "وردة", "زهرة زنبق", "باقات متماثلة"),
        (40, 60, 100, "stickers", "bookmarks", "pens", "student prize packs", "ملصقًا", "فاصل كتب", "قلمًا", "حزم جوائز طلابية"),
        (54, 36, 63, "apples", "oranges", "bananas", "fruit baskets", "تفاحة", "برتقالة", "موزة", "سلال فاكهة"),
        (44, 66, 88, "science badges", "math pins", "ribbons", "competition teams", "شارة علمية", "دبوس رياضيات", "شريطًا", "فرق المسابقة"),
    ]
    for x, y, z, i1_e, i2_e, i3_e, grp_e, i1_a, i2_a, i3_a, grp_a in gcd_cases:
        qid = next_id()
        ans = math.gcd(math.gcd(x, y), z)
        q_en = (
            f"A teacher has {m(x)} {i1_e}, {m(y)} {i2_e}, and {m(z)} {i3_e} to divide equally among {grp_e}, "
            f"using every item with none left over. What is the greatest possible number of {grp_e}?"
        )
        q_ar = (
            f"لدى معلم {m(x)} {i1_a} و {m(y)} {i2_a} و {m(z)} {i3_a}، ويريد توزيعها بالتساوي على {grp_a} "
            f"بحيث تُستخدم جميع الأصناف دون باقٍ. ما أكبر عدد ممكن من {grp_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans // 2 if ans % 2 == 0 else ans - 2, ans * 2, math.gcd(x, y) if math.gcd(x, y) != ans else ans + 3, ans + 4, max(2, ans - 3)], qid
        )
        sol_en = explain_en(
            f"For every group to get the exact same whole number of each item with zero leftovers, the number of groups must divide {m(x)}, {m(y)}, and {m(z)} evenly. So we need their Greatest Common Divisor (GCD).",
            [
                f"List the factors of the smallest count first, or break each number into factors: {m(f'{x} = {ans} \\times {x//ans}')}, {m(f'{y} = {ans} \\times {y//ans}')}, and {m(f'{z} = {ans} \\times {z//ans}')}.",
                f"Check the remaining quotients {m(x//ans)}, {m(y//ans)}, and {m(z//ans)}: they share no common factor greater than {m(1)}.",
                f"Therefore, the greatest common divisor of {m(x)}, {m(y)}, and {m(z)} is {m(ans)}.",
            ],
            f"With {m(ans)} groups, each receives {m(x//ans)} {i1_e}, {m(y//ans)} {i2_e}, and {m(z//ans)} {i3_e}, using every single item!",
        )
        sol_ar = explain_ar(
            f"لكي تحصل كل مجموعة على العدد نفسه دون أي باقٍ، يجب أن يقسم عدد المجموعات كلًا من {m(x)} و {m(y)} و {m(z)} بدون باقٍ؛ أي نبحث عن القاسم المشترك الأكبر (GCD).",
            [
                f"نحلّل الأعداد لإبراز أكبر عامل مشترك بينها: {m(f'{x} = {ans} \\times {x//ans}')}، و {m(f'{y} = {ans} \\times {y//ans}')}، و {m(f'{z} = {ans} \\times {z//ans}')}.",
                f"نلاحظ أن الأعداد المتبقية {m(x//ans)} و {m(y//ans)} و {m(z//ans)} لا تشترك في أي قاسم أكبر من {m(1)}.",
                f"إذن أكبر عدد يقسم الأعداد الثلاثة معًا هو {m(ans)}.",
            ],
            f"عند القسمة على {m(ans)} تحصل كل مجموعة على {m(x//ans)} و {m(y//ans)} و {m(z//ans)} من الأصناف الثلاثة دون أي باقٍ.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-gcd-equal-sharing",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the largest whole number that divides {x}, {y}, and {z} with no remainder.",
            f"أوجد أكبر عدد صحيح يقسم كلًا من {x} و {y} و {z} دون باقٍ.",
            sol_en, sol_ar
        ))

    # 5. Repeating word / bead cycle (KMC G6-7 Practice Set 1 Q1 style: KAUSTKAUST...) (8 variants)
    cycle_cases = [
        ("KAUST", 98, "What is the 98th letter"),
        ("THUWAL", 100, "What is the 100th letter"),
        ("SCIENCE", 150, "What is the 150th letter"),
        ("RIYADH", 89, "What is the 89th letter"),
        ("ACADEMY", 142, "What is the 142nd letter"),
        ("MATHS", 124, "What is the 124th letter"),
        ("OLYMPIAD", 101, "What is the 101st letter"),
        ("DISCOVER", 135, "What is the 135th letter"),
    ]
    for word, pos, ask_en in cycle_cases:
        qid = next_id()
        L = len(word)
        q_quot, rem = divmod(pos, L)
        ans_letter = word[rem - 1] if rem > 0 else word[-1]
        # Pick 5 distinct letters from word
        uniq_letters = []
        for ch in word:
            if ch not in uniq_letters:
                uniq_letters.append(ch)
        while len(uniq_letters) < 5:
            for extra in "KMCXYZ":
                if extra not in uniq_letters:
                    uniq_letters.append(extra)
                    if len(uniq_letters) == 5:
                        break
        if ans_letter not in uniq_letters[:5]:
            uniq_letters[0] = ans_letter
        five = uniq_letters[:5]
        c_orig = five.index(ans_letter)
        pairs = [(ch, ch) for ch in five]
        opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, c_orig, qid)
        repeated = word * 3 + "..."
        q_en = f"A student writes the word **{word}** repeatedly without spaces: `{repeated}` {ask_en} written?"
        q_ar = f"يكتب طالب الكلمة الإنجليزية **{word}** بشكل متكرر دون مسافات هكذا: `{repeated}` ما الحرف ذو الترتيب {m(pos)}؟"
        rem_explain_en = (
            f"The remainder is {m(rem)}, so we move {m(rem)} letter(s) into the next copy of **{word}**, landing on **{ans_letter}**."
            if rem > 0 else
            f"The remainder is {m(0)}, which means position {m(pos)} is the very last letter of copy #{q_quot}, namely **{ans_letter}**."
        )
        rem_explain_ar = (
            f"الباقي هو {m(rem)}، لذا نعدّ {m(rem)} حرفًا من بداية الكلمة الجديدة **{word}** فنصل إلى الحرف **{ans_letter}**."
            if rem > 0 else
            f"الباقي هو {m(0)}، وهذا يعني أن الموقع {m(pos)} يقع عند الحرف الأخير تمامًا من التكرار رقم {m(q_quot)}، وهو **{ans_letter}**."
        )
        sol_en = explain_en(
            f"Because the word **{word}** has {m(L)} letters, the pattern repeats every {m(L)} positions. Dividing {m(pos)} by {m(L)} tells us how many full copies fit and where we land in the next copy!",
            [
                f"Count the letters in **{word}**: there are {m(L)} letters ({', '.join(f'{i+1}={word[i]}' for i in range(L))}).",
                f"Divide {m(pos)} by {m(L)}: {m(f'{pos} = {L} \\times {q_quot} + {rem}')}.",
                rem_explain_en,
            ],
            f"Every {m(L)}th letter is **{word[-1]}**, so position {m(L * q_quot)} is **{word[-1]}**, and counting {m(rem)} step(s) further gives **{ans_letter}**.",
        )
        sol_ar = explain_ar(
            f"بما أن الكلمة **{word}** تتكون من {m(L)} أحرف، فإن النمط يعيد نفسه كل {m(L)} خانات. باقي قسمة {m(pos)} على {m(L)} يحدد موقع الحرف بدقة.",
            [
                f"نعدّ أحرف الكلمة **{word}** فنجدها {m(L)} أحرف بالترتيب ({'، '.join(f'{i+1}={word[i]}' for i in range(L))}).",
                f"نقسم {m(pos)} على {m(L)}: {m(f'{pos} = {L} \\times {q_quot} + {rem}')}.",
                rem_explain_ar,
            ],
            f"الموقع {m(L * q_quot)} ينتهي عند آخر حرف **{word[-1]}**، ومنه نتحرك {m(rem)} خطوة فنحصل على **{ans_letter}**.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-repeating-word-cycle",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Count how many letters are in {word}, then find the remainder when {pos} is divided by {L}.",
            f"احسب عدد أحرف الكلمة {word}، ثم أوجد باقي قسمة {pos} على {L}.",
            sol_en, sol_ar
        ))

    # 6. Column addition with ★ stars (8 variants with KMC cryptarithm SVG!) — KMC G6-7 Sample Q22
    star_cases = [
        (["1★2", "1★3", "1★4"], 0, "sum of all three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث (حيث تخفي كل نجمة الرقم نفسه)"),
        (["1★1", "1★2", "1★5"], 4, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["2★3", "2★4", "2★1"], 5, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["1★4", "2★3", "1★2"], 6, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["2★5", "1★2", "2★1"], 3, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["3★1", "1★3", "2★4"], 7, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["1★6", "2★1", "1★2"], 2, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
        (["2★2", "3★3", "1★4"], 8, "sum of the three digits covered by the three identical stars", "مجموع الأرقام الثلاثة المغطاة بالنجوم الثلاث المتطابقة"),
    ]
    for rows, d, ask_e, ask_a in star_cases:
        qid = next_id()
        tot = sum(int(r.replace("★", str(d))) for r in rows)
        ans_sum = 3 * d
        svg = svg_column_cryptarithm(rows, str(tot))
        u_sum = sum(int(r[-1]) for r in rows)
        h_base = sum(int(r[0]) for r in rows)
        rows_tex = " + ".join(f"\\overline{{{r.replace('★', '\\star')}}}" for r in rows) + f" = {tot}"
        q_en = (
            f"In the column addition {m(rows_tex)} shown, all three stars ({m('\\star')}) hide the **same** digit. "
            f"What is the {ask_e}?"
        )
        q_ar = (
            f"في عملية الجمع العمودية {m(rows_tex)} الموضحة، جميع النجوم الثلاث ({m('\\star')}) تخفي **الرقم نفسه**. "
            f"ما {ask_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans_sum, [d, ans_sum + 3, max(0, ans_sum - 3) if ans_sum >= 3 else 6, d + 3, ans_sum + 6], qid
        )
        sol_en = explain_en(
            "Check the ones (units) column first to see if anything carries over, then use the total difference to find the tens value!",
            [
                f"If every star were {m(0)}, the three numbers would be {', '.join(m(r.replace('★','0')) for r in rows)}, whose sum is {m(h_base * 100 + u_sum)}.",
                f"Compare that with the actual total {m(tot)}: the extra amount comes entirely from the three tens-place stars: {m(f'{tot} - {h_base*100 + u_sum} = {tot - (h_base*100 + u_sum)}')}.",
                f"Since each star is in the tens column (worth {m('10 \\times \\star')}), all three stars together contribute {m('30 \\times \\star')}. Dividing {m(f'{tot - (h_base*100 + u_sum)} \\div 30 = {d}')}, each star hides the digit {m(d)}.",
                f"The question asks for the **sum of all three digits** under the stars: {m(f'{d} + {d} + {d} = {ans_sum}')}.",
            ],
            f"Test {m(f'\\star = {d}')}: {' + '.join(r.replace('★', str(d)) for r in rows)} = {tot}, and {m(f'3 \\times {d} = {ans_sum}')}!",
        )
        sol_ar = explain_ar(
            "نحسب أولًا مجموع الأعداد لو وُضع صفر مكان كل نجمة، فيكون الفرق بين الناتج الفعلي وهذا المجموع ناتجًا عن قيمة النجوم الثلاث في خانة العشرات.",
            [
                f"لو استبدلنا كل نجمة بالرقم {m(0)} نحصل على الأعداد {', '.join(m(r.replace('★','0')) for r in rows)} ومجموعها {m(h_base * 100 + u_sum)}.",
                f"نطرح هذا المجموع من الناتج المعطى {m(tot)}: {m(f'{tot} - {h_base*100 + u_sum} = {tot - (h_base*100 + u_sum)}')}.",
                f"بما أن كل نجمة تقع في منزلة العشرات فإن الثلاث نجوم تضيف {m('30 \\times \\star')}، ومنه قيمة النجمة الواحدة {m(f'\\star = {tot - (h_base*100 + u_sum)} \\div 30 = {d}')}.",
                f"انتبه للمطلوب: مجموع الأرقام الثلاثة التي تغطيها النجوم هو {m(f'{d} + {d} + {d} = {ans_sum}')}.",
            ],
            f"بالتعويض عن كل نجمة بـ {m(d)}: {' + '.join(r.replace('★', str(d)) for r in rows)} = {tot}، ومجموع النجوم الثلاث يساوي {m(ans_sum)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-star-addition",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Replace each star with 0 first to see how much tens-value the three stars must add to reach the total!",
            "ضع صفرًا مكان كل نجمة أولًا لتعرف كم يجب أن تضيف النجوم الثلاث في منزلة العشرات للوصول إلى المجموع!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 7. Percentage of a percentage (sports/clubs/library) (8 variants) — KMC G6-7 Practice Set 1 Q4
    pct_of_pct = [
        (60, 25, "students in a grade like football", "of those also like basketball", "students in the grade like both sports",
         "طلاب الصف يحبون كرة القدم", "من هؤلاء يحبون كرة السلة أيضًا", "طلاب الصف الذين يحبون الرياضتين معًا"),
        (80, 35, "visitors at a science fair visit the robotics booth", "of those also attend the coding workshop", "all visitors do both",
         "زوار المعرض العلمي يزورون ركن الروبوتات", "منهم يحضرون ورشة البرمجة أيضًا", "جميع الزوار الذين شاركوا في النشاطين"),
        (50, 40, "books in a school library are in Arabic", "of those Arabic books are science books", "all library books are Arabic science books",
         "كتب المكتبة المدرسية باللغة العربية", "من هذه الكتب العربية هي كتب علمية", "جميع كتب المكتبة التي هي كتب علمية عربية"),
        (40, 50, "trees on an orchard farm are palm trees", "of those palm trees are Sukkari palms", "all trees on the farm are Sukkari palms",
         "أشجار مزرعة هي أشجار نخيل", "من أشجار النخيل هذه من نوع السكري", "جميع أشجار المزرعة التي هي نخيل سكري"),
        (75, 20, "members of a math club are in middle school", "of those middle-schoolers are in Grade 6", "all club members are in Grade 6",
         "أعضاء نادي الرياضيات في المرحلة المتوسطة والعليا من الابتدائي", "من هؤلاء في الصف السادس", "جميع أعضاء النادي الذين هم في الصف السادس"),
        (60, 45, "cars in a parking lot are white", "of those white cars are electric", "all cars in the lot are white electric cars",
         "السيارات في موقف هي سيارات بيضاء", "من السيارات البيضاء كهربائية", "جميع السيارات التي هي كهربائية بيضاء"),
        (70, 30, "runners in a race wear blue shirts", "of those wear running caps", "all runners wear both a blue shirt and a cap",
         "المشاركين في سباق يرتدون قمصانًا زرقاء", "منهم يرتدون قبعات رياضية", "جميع المشاركين الذين يرتدون قميصًا أزرق وقبعة معًا"),
        (80, 15, "apples in a crate are red", "of those red apples weigh over 200 g", "all apples in the crate are red and over 200 g",
         "التفاح في صندوق أحمر اللون", "من التفاح الأحمر يزيد وزنه على 200 جم", "جميع التفاح في الصندوق الأحمر الذي يتجاوز 200 جم"),
    ]
    for p1, p2, s1_e, s2_e, ask_e, s1_a, s2_a, ask_a in pct_of_pct:
        qid = next_id()
        ans = (p1 * p2) // 100
        q_en = f"Suppose {m(f'{p1}\\%')} of {s1_e}, and {m(f'{p2}\\%')} {s2_e}. What percentage of {ask_e}?"
        q_ar = f"إذا كان {m(f'{p1}\\%')} من {s1_a}، وكان {m(f'{p2}\\%')} {s2_a}، فما النسبة المئوية لـ{ask_a}؟"
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [p1 + p2, abs(p1 - p2), p2, ans + 10], qid, suffix="\\%"
        )
        sol_en = explain_en(
            f"The easiest way to understand percentages without formulas is to **imagine a group of {m(100)} items**!",
            [
                f"Imagine there are exactly {m(100)} items in total. Since {m(f'{p1}\\%')} befit the first group, that gives {m(p1)} items.",
                f"Now find {m(f'{p2}\\%')} **of those {m(p1)} items** (not of {m(100)}!): multiply {m(f'\\frac{{{p2}}}{{100}} \\times {p1} = \\frac{{{p1*p2}}}{{100}} = {ans}')}.",
                f"Out of our {m(100)} total items, {m(ans)} have both properties, which is {m(f'{ans}\\%')}.",
            ],
            f"Common trap: adding {m(f'{p1}\\% + {p2}\\% = {p1+p2}\\%')} is impossible because the second group is a subset inside the first {m(f'{p1}\\%')}!",
        )
        sol_ar = explain_ar(
            f"أسهل طريقة لحساب نسبة مئوية من نسبة مئوية أخرى دون تعقيد هي **افتراض أن العدد الكلي يساوي {m(100)}**!",
            [
                f"لنفترض أن العدد الكلي هو {m(100)}. بما أن النسبة الأولى {m(f'{p1}\\%')}، فهذا يمثّل {m(p1)} عنصرًا.",
                f"الآن نحسب {m(f'{p2}\\%')} **من هذه الـ {m(p1)}** فقط: {m(f'\\frac{{{p2}}}{{100}} \\times {p1} = \\frac{{{p1*p2}}}{{100}} = {ans}')}.",
                f"إذن يوجد {m(ans)} من أصل {m(100)}، أي أن النسبة المئوية من الكل هي {m(f'{ans}\\%')}.",
            ],
            f"انتبه للخطأ الشائع: لا نجمع النسبتين، بل نأخذ جزءًا من المجموعة الأولى {m(f'{p1}\\%')} فيكون الناتج أصغر منها وهو {m(f'{ans}\\%')}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-percent-of-percent",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Imagine there are 100 in total: first take {p1} of them, then find {p2}% of {p1}.",
            f"تخيّل أن العدد الكلي 100: خذ {p1} منهم أولًا، ثم احسب {p2}% من الـ {p1}.",
            sol_en, sol_ar
        ))

    # 8. Mistakenly multiplied instead of dividing by a decimal/fraction (8 variants) — KMC G6-7 Practice Set 2 Q2
    mistake_cases = [
        ("0.25", Fraction(1, 4), 3, "Ahmed", "أحمد"),
        ("0.5", Fraction(1, 2), 9, "Lina", "لينا"),
        ("0.2", Fraction(1, 5), 4, "Tariq", "طارق"),
        ("0.25", Fraction(1, 4), 5, "Noura", "نورة"),
        ("0.1", Fraction(1, 10), 2, "Faisal", "فيصل"),
        ("0.5", Fraction(1, 2), 14, "Reem", "ريم"),
        ("0.2", Fraction(1, 5), 6, "Yasser", "ياسر"),
        ("0.25", Fraction(1, 4), 7, "Dana", "دانة"),
    ]
    for dec_str, frac, got_val, name_e, name_a in mistake_cases:
        qid = next_id()
        denom = frac.denominator  # 4, 2, 5, 10
        orig_num = got_val * denom
        ans = orig_num * denom
        q_en = (
            f"{name_e} wanted to **divide** a mystery number by {m(dec_str)}, "
            f"but by mistake **multiplied** the number by {m(dec_str)} and got {m(got_val)}. "
            f"What should the correct answer have been?"
        )
        q_ar = (
            f"أراد {name_a} أن **يقسم** عددًا ما على {m(dec_str)}، ولكنه بالخطأ **ضرب** العدد في {m(dec_str)} فحصل على {m(got_val)}. "
            f"ما الإجابة الصحيحة التي كان يجب أن يحصل عليها؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [orig_num, got_val, ans * 2, orig_num + denom], qid
        )
        sol_en = explain_en(
            f"Rewrite the decimal {m(dec_str)} as the simple fraction {m(f'\\frac{{1}}{{{denom}}}')}. Multiplying by {m(f'\\frac{{1}}{{{denom}}}')} makes a number {m(denom)} times smaller, whereas dividing by {m(f'\\frac{{1}}{{{denom}}}')} makes it {m(denom)} times larger!",
            [
                f"Convert {m(dec_str)} to a fraction: {m(f'{dec_str} = \\frac{{1}}{{{denom}}}')}.",
                f"Find the mystery number first: since multiplying it by {m(f'\\frac{{1}}{{{denom}}}')} gave {m(got_val)}, undo that step by multiplying by {m(denom)}: mystery number {m(f'= {got_val} \\times {denom} = {orig_num}')}.",
                f"Now perform the intended operation — divide {m(orig_num)} by {m(f'\\frac{{1}}{{{denom}}}')} (which is multiplying by {m(denom)}): {m(f'{orig_num} \\div \\frac{{1}}{{{denom}}} = {orig_num} \\times {denom} = {ans}')}.",
            ],
            f"Don't stop at {m(orig_num)}! {m(orig_num)} is the starting number ({m(f'{orig_num} \\times {dec_str} = {got_val}')}), and dividing {m(orig_num)} by {m(dec_str)} gives {m(ans)}.",
        )
        sol_ar = explain_ar(
            f"نحوّل الكسر العشري {m(dec_str)} إلى كسر اعتيادي بسيط هو {m(f'\\frac{{1}}{{{denom}}}')}. تذكّر أن القسمة على {m(f'\\frac{{1}}{{{denom}}}')} تعني الضرب في مقلوبه أي الضرب في {m(denom)}!",
            [
                f"نكتب {m(f'{dec_str} = \\frac{{1}}{{{denom}}}')}.",
                f"نوجد العدد الأصلي أولًا: بما أن ضربه في {m(f'\\frac{{1}}{{{denom}}}')} أعطى {m(got_val)}، فإن العدد الأصلي يساوي {m(f'{got_val} \\times {denom} = {orig_num}')}.",
                f"الآن ننفذ العملية الصحيحة المطلوبة، وهي قسمة {m(orig_num)} على {m(f'\\frac{{1}}{{{denom}}}')}: {m(f'{orig_num} \\div \\frac{{1}}{{{denom}}} = {orig_num} \\times {denom} = {ans}')}.",
            ],
            f"احذر من التوقف عند {m(orig_num)}؛ فـ {m(orig_num)} هو العدد الأصلي فقط، بينما ناتج القسمة الصحيح هو {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-decimal-divide-mistake",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Write {dec_str} as 1/{denom}: first find the original number, then divide that original number by 1/{denom}.",
            f"اكتب {dec_str} على صورة 1/{denom}: أوجد العدد الأصلي أولًا، ثم اقسمه على 1/{denom}.",
            sol_en, sol_ar
        ))

    # 9. Sequential fractions of remainder (books / pocket money / journey) (8 variants)
    rem_cases = [
        (Fraction(1, 3), Fraction(1, 2), 24, "pages of a storybook on Friday", "of the remaining pages on Saturday", "pages left for Sunday", "total pages in the book",
         "صفحات قصة يوم الجمعة", "من الصفحات المتبقية يوم السبت", "صفحة ليوم الأحد", "إجمالي صفحات القصة"),
        (Fraction(1, 4), Fraction(1, 3), 30, "of her savings on a calculator-free puzzle book", "of what remained on geometry tools", "riyals left", "riyals she had at the start",
         "من مدخراتها لشراء كتاب ألغاز", "مما تبقى لشراء أدوات هندسية", "ريالًا متبقيًا", "المبلغ الذي كان معها في البداية بالريال"),
        (Fraction(2, 5), Fraction(1, 3), 18, "of a basket of dates at breakfast", "of the remaining dates at evening coffee", "dates left in the basket", "dates originally in the basket",
         "من سلة تمر في الفطور", "من التمر المتبقي مع قهوة المساء", "تمرة متبقية في السلة", "عدد التمرات في السلة في البداية"),
        (Fraction(1, 5), Fraction(1, 4), 36, "of a cycling trail in the first hour", "of the remaining distance in the second hour", "kilometers left to finish", "total kilometers of the trail",
         "من مسار دراجات في الساعة الأولى", "من المسافة المتبقية في الساعة الثانية", "كم متبقيًا للنهاية", "طول المسار الكلي بالكيلومتر"),
        (Fraction(1, 3), Fraction(2, 5), 20, "of a roll of ribbon for gift boxes", "of the remaining ribbon for posters", "meters of ribbon left", "original length of the ribbon in meters",
         "من لفة شريط لتغليف الهدايا", "من الشريط المتبقي للوحات", "مترًا متبقيًا", "الطول الأصلي للشريط بالأمتار"),
        (Fraction(3, 8), Fraction(1, 5), 25, "of a tank of water on Monday", "of the remaining water on Tuesday", "liters left in the tank", "liters originally in the tank",
         "من خزان ماء يوم الإثنين", "من الماء المتبقي يوم الثلاثاء", "لترًا في الخزان", "كمية الماء في الخزان في البداية باللتر"),
        (Fraction(1, 6), Fraction(2, 5), 27, "of the muffins sold in the morning", "of the remaining muffins sold at lunch", "muffins left", "muffins baked originally",
         "من الكعكات بيعت صباحًا", "من الكعكات المتبقية بيعت ظهرًا", "كعكة متبقية", "عدد الكعكات التي خُبزت أصلًا"),
        (Fraction(2, 7), Fraction(1, 5), 32, "of the seedlings planted on Day 1", "of the remaining seedlings planted on Day 2", "seedlings left for Day 3", "total seedlings at the beginning",
         "من الشتلات زُرعت في اليوم الأول", "من الشتلات المتبقية زُرعت في اليوم الثاني", "شتلة لليوم الثالث", "إجمالي عدد الشتلات في البداية"),
    ]
    for f1, f2, left_val, p1_e, p2_e, p3_e, ask_e, p1_a, p2_a, p3_a, ask_a in rem_cases:
        qid = next_id()
        rem1 = 1 - f1
        rem2 = rem1 * (1 - f2)
        total = left_val / rem2
        assert total.denominator == 1
        ans = total.numerator
        q_en = (
            f"After using {m(f'\\frac{{{f1.numerator}}}{{{f1.denominator}}}')} {p1_e}, and then {m(f'\\frac{{{f2.numerator}}}{{{f2.denominator}}}')} {p2_e}, "
            f"there are exactly {m(left_val)} {p3_e}. Find the {ask_e}."
        )
        q_ar = (
            f"بعد استهلاك {m(f'\\frac{{{f1.numerator}}}{{{f1.denominator}}}')} {p1_a}، ثم {m(f'\\frac{{{f2.numerator}}}{{{f2.denominator}}}')} {p2_a}، "
            f"بقي بالضبط {m(left_val)} {p3_a}. أوجد {ask_a}."
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans - left_val // 2, ans + left_val // 2, left_val * 2, ans + 12], qid
        )
        sol_en = explain_en(
            "Work step-by-step with **what fraction remains** after each stage rather than adding the two fractions directly (because the second fraction acts only on the remainder!).",
            [
                f"After the first part ({m(f'\\frac{{{f1.numerator}}}{{{f1.denominator}}}')}) is used, the fraction remaining is {m(f'1 - \\frac{{{f1.numerator}}}{{{f1.denominator}}} = \\frac{{{rem1.numerator}}}{{{rem1.denominator}}}')}.",
                f"Next, {m(f'\\frac{{{f2.numerator}}}{{{f2.denominator}}}')} of that remainder is used, so {m(f'1 - \\frac{{{f2.numerator}}}{{{f2.denominator}}} = \\frac{{{(1-f2).numerator}}}{{{(1-f2).denominator}}}')} of that remainder stays.",
                f"Multiply to find the final fraction of the whole that is left: {m(f'\\frac{{{rem1.numerator}}}{{{rem1.denominator}}} \\times \\frac{{{(1-f2).numerator}}}{{{(1-f2).denominator}}} = \\frac{{{rem2.numerator}}}{{{rem2.denominator}}}')}.",
                f"Since {m(f'\\frac{{{rem2.numerator}}}{{{rem2.denominator}}}')} of the total equals {m(left_val)}, one part ({m(f'\\frac{{1}}{{{rem2.denominator}}}')}) is {m(f'{left_val} \\div {rem2.numerator} = {left_val // rem2.numerator}')}, and the whole total is {m(f'{left_val // rem2.numerator} \\times {rem2.denominator} = {ans}')}.",
            ],
            f"Check forward from {m(ans)}: first remove {m(int(ans * f1))}, leaving {m(int(ans * rem1))}; next remove {m(int(ans * rem1 * f2))}, leaving {m(left_val)}!",
        )
        sol_ar = explain_ar(
            "نتتبع **الكسر المتبقي** بعد كل مرحلة؛ لأن الكسر الثاني يُؤخذ من الباقي وليس من الكمية الأصلية كاملة.",
            [
                f"بعد المرحلة الأولى ({m(f'\\frac{{{f1.numerator}}}{{{f1.denominator}}}')}) يبقى من الكل: {m(f'1 - \\frac{{{f1.numerator}}}{{{f1.denominator}}} = \\frac{{{rem1.numerator}}}{{{rem1.denominator}}}')}.",
                f"في المرحلة الثانية يُستهلك {m(f'\\frac{{{f2.numerator}}}{{{f2.denominator}}}')} من الباقي، فيتبقى منه {m(f'1 - \\frac{{{f2.numerator}}}{{{f2.denominator}}} = \\frac{{{(1-f2).numerator}}}{{{(1-f2).denominator}}}')}.",
                f"نضرب الكسرين لمعرفة الجزء المتبقي من الأصل: {m(f'\\frac{{{rem1.numerator}}}{{{rem1.denominator}}} \\times \\frac{{{(1-f2).numerator}}}{{{(1-f2).denominator}}} = \\frac{{{rem2.numerator}}}{{{rem2.denominator}}}')}.",
                f"بما أن {m(f'\\frac{{{rem2.numerator}}}{{{rem2.denominator}}}')} من الكل يساوي {m(left_val)}، فإن الكل يساوي {m(f'{left_val} \\div {rem2.numerator} \\times {rem2.denominator} = {ans}')}.",
            ],
            f"تحقق من البداية بالعدد {m(ans)}: بعد المرحلة الأولى يتبقى {m(int(ans * rem1))}، وبعد الثانية يتبقى {m(left_val)} تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-fraction-of-remainder",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Find what fraction is LEFT after step 1, then find what fraction of that is LEFT after step 2.",
            "احسب الكسر المتبقي بعد الخطوة الأولى، ثم الكسر المتبقي منه بعد الخطوة الثانية.",
            sol_en, sol_ar
        ))

    # 10. Divisibility by 9 / 3 / 4 missing digit puzzles (8 variants)
    div9_cases = [
        ("42□6", 9, 6, "divisible by 9", "يقبل القسمة على 9"),
        ("7□35", 9, 3, "divisible by 9", "يقبل القسمة على 9"),
        ("58□2", 9, 3, "divisible by 9", "يقبل القسمة على 9"),
        ("61□8", 9, 3, "divisible by 9", "يقبل القسمة على 9"),
        ("9□45", 9, 0, "the **smallest** digit □ that makes it divisible by 9", "أصغر رقم □ يجعله يقبل القسمة على 9"),
        ("35□4", 9, 6, "divisible by 9", "يقبل القسمة على 9"),
        ("8□26", 9, 2, "divisible by 9", "يقبل القسمة على 9"),
        ("27□5", 9, 4, "divisible by 9", "يقبل القسمة على 9"),
    ]
    for pat, modv, ans, cond_e, cond_a in div9_cases:
        qid = next_id()
        known_digits = [int(ch) for ch in pat if ch.isdigit()]
        ksum = sum(known_digits)
        filled_num = int(pat.replace("□", str(ans)))
        assert filled_num % modv == 0
        tex_pat = pat.replace("□", "\\square")
        q_en = f"In the four-digit number {m(tex_pat)}, {m('\\square')} represents a single digit from {m(0)} to {m(9)}. Find the digit {m('\\square')} so that the number is {cond_e}."
        q_ar = f"في العدد المكوّن من أربع خانات {m(tex_pat)}، يمثّل الرمز {m('\\square')} رقمًا واحدًا من {m(0)} إلى {m(9)}. أوجد قيمة {m('\\square')} بحيث يكون العدد {cond_a}."
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [(ans + 1) % 10, (ans + 2) % 10, (ans + 3) % 10, (ans + 5) % 10], qid
        )
        next_mult = ksum + ans
        sol_en = explain_en(
            "Divisibility Rule for 9: A whole number is divisible by 9 if and only if the **sum of all its digits** is a multiple of 9 (such as 9, 18, 27, ...).",
            [
                f"Add the three known digits first: {m(' + '.join(map(str, known_digits)) + f' = {ksum}')}.",
                f"Including the missing digit {m('\\square')}, the digit sum is {m(f'{ksum} + \\square')}.",
                f"Look for a multiple of {m(9)} we can reach by adding a single digit ({m('0')} to {m('9')}): the target multiple of {m(9)} is {m(next_mult)}, so {m(f'\\square = {next_mult} - {ksum} = {ans}')}.",
            ],
            f"When {m(f'\\square = {ans}')}, the number is {m(filled_num)} and {m(f'{filled_num} \\div 9 = {filled_num // 9}')} with zero remainder!",
        )
        sol_ar = explain_ar(
            "قاعدة قابلية القسمة على 9: يقبل العدد القسمة على 9 إذا وفقط إذا كان **مجموع أرقامه** من مضاعفات العدد 9 (مثل 9، 18، 27، ...).",
            [
                f"نجمع الأرقام الثلاثة المعلومة أولًا: {m(' + '.join(map(str, known_digits)) + f' = {ksum}')}.",
                f"بإضافة الرقم المجهول يصبح مجموع الأرقام: {m(f'{ksum} + \\square')}.",
                f"نبحث عن مضاعف للعدد {m(9)} يمكن الوصول إليه بإضافة رقم من {m(0)} إلى {m(9)}، وهو {m(next_mult)}، فيكون {m(f'\\square = {next_mult} - {ksum} = {ans}')}.",
            ],
            f"بالتعويض نحصل على العدد {m(filled_num)}، وعند قسمته على {m(9)} يكون الناتج {m(filled_num // 9)} بدون باقٍ.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-divisibility-by-9",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Add the visible digits and find what single digit makes the total sum a multiple of 9.",
            "اجمع الأرقام الظاهرة وابحث عن الرقم الذي يجعل مجموع الأرقام من مضاعفات 9.",
            sol_en, sol_ar
        ))

    # 11. Comparing 5 arithmetic fractions — largest value (8 variants) — KMC G6-7 Sample Q13
    frac_cmp_cases = [
        (3, 5, 8), (2, 5, 7), (3, 4, 9), (2, 7, 9),
        (4, 5, 11), (3, 7, 10), (2, 3, 8), (4, 7, 9),
    ]
    for a, b, c in frac_cmp_cases:
        qid = next_id()
        # 5 expressions built from a < b < c: largest is (b+c)/a!
        exprs = [
            (f"\\frac{{{b}+{c}}}{{{a}}}", Fraction(b + c, a)),
            (f"\\frac{{{a}}}{{{b}+{c}}}", Fraction(a, b + c)),
            (f"\\frac{{{a}+{c}}}{{{b}}}", Fraction(a + c, b)),
            (f"\\frac{{{a}+{b}}}{{{c}}}", Fraction(a + b, c)),
            (f"\\frac{{{c}}}{{{a}+{b}}}", Fraction(c, a + b)),
        ]
        vals = [v for _, v in exprs]
        assert vals[0] > max(vals[1:])
        pairs = [(m(tex), m(tex)) for tex, _ in exprs]
        opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, 0, qid)
        q_en = f"Which of the following five fractions made from the numbers {m(a)}, {m(b)}, and {m(c)} has the **largest** value?"
        q_ar = f"أيٌّ من الكسور الخمسة التالية المكوّنة من الأعداد {m(a)} و {m(b)} و {m(c)} له **أكبر** قيمة؟"
        sol_en = explain_en(
            "A positive fraction becomes **as large as possible** when its **top number (numerator) is as big as possible** and its **bottom number (denominator) is as small as possible**!",
            [
                f"With {m(a)}, {m(b)}, and {m(c)}, the largest sum of two numbers for the top is {m(f'{b} + {c} = {b+c}')}, and the smallest single number for the bottom is {m(a)}.",
                f"Evaluate that candidate: {m(f'\\frac{{{b}+{c}}}{{{a}}} = \\frac{{{b+c}}}{{{a}}}')} (which is greater than {m((b+c)//a)}).",
                f"Compare quickly with the next closest choice {m(f'\\frac{{{a}+{c}}}{{{b}}} = \\frac{{{a+c}}}{{{b}}}')}: since {m(f'{b+c} > {a+c}')} (bigger top) AND {m(f'{a} < {b}')} (smaller bottom), {m(f'\\frac{{{b}+{c}}}{{{a}}}')} is strictly larger than all the others!",
            ],
            f"All other options have smaller numerators or larger denominators, confirming {m(f'\\frac{{{b}+{c}}}{{{a}}}')} is the maximum.",
        )
        sol_ar = explain_ar(
            "يكبر الكسر الموجب كلما كان **بسطه (العدد العلوي) أكبر ما يمكن** وكان **مقامه (العدد السفلي) أصغر ما يمكن**!",
            [
                f"من بين الأعداد {m(a)} و {m(b)} و {m(c)}، أكبر مجموع لعددين في البسط هو {m(f'{b} + {c} = {b+c}')}، وأصغر عدد مفرد في المقام هو {m(a)}.",
                f"نحسب قيمة هذا الكسر: {m(f'\\frac{{{b}+{c}}}{{{a}}} = \\frac{{{b+c}}}{{{a}}}')}.",
                f"نقارنه بأقرب منافس له وهو {m(f'\\frac{{{a}+{c}}}{{{b}}} = \\frac{{{a+c}}}{{{b}}}')}: نلاحظ أن {m(b+c)} أكبر من {m(a+c)} في البسط، و {m(a)} أصغر من {m(b)} في المقام، لذا فإن {m(f'\\frac{{{b}+{c}}}{{{a}}}')} هو الأكبر قطعًا.",
            ],
            f"بقية الخيارات إما أصغر من {m(1)} أو ذات بسط أصغر ومقام أكبر، إذن {m(f'\\frac{{{b}+{c}}}{{{a}}}')} هو الأكبر.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Easy", "g67-largest-fraction-choice",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "To make a fraction as big as possible, make the numerator as large as possible and the denominator as small as possible.",
            "لجعل الكسر أكبر ما يمكن، اجعل البسط أكبر ما يمكن والمقام أصغر ما يمكن.",
            sol_en, sol_ar
        ))

    # 12. Pouring water between 3 identical cups (8 variants with KMC water-cups SVG!) — KMC Junior Q5
    cup_cases = [
        (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), "half", "half", "half", "نصف", "نصف", "نصف"),
        (Fraction(1, 2), Fraction(1, 2), Fraction(1, 4), "half", "half", "one-quarter", "نصف", "نصف", "ربع"),
        (Fraction(1, 4), Fraction(1, 2), Fraction(1, 2), "one-quarter", "half", "half", "ربع", "نصف", "نصف"),
        (Fraction(3, 5), Fraction(1, 2), Fraction(1, 2), "three-fifths", "half", "half", "ثلاثة أخماس", "نصف", "نصف"),
        (Fraction(2, 5), Fraction(1, 2), Fraction(1, 2), "two-fifths", "half", "half", "خُمسَي", "نصف", "نصف"),
        (Fraction(1, 2), Fraction(2, 5), Fraction(1, 2), "half", "two-fifths", "half", "نصف", "خُمسَي", "نصف"),
        (Fraction(4, 5), Fraction(1, 2), Fraction(1, 2), "four-fifths", "half", "half", "أربعة أخماس", "نصف", "نصف"),
        (Fraction(1, 2), Fraction(3, 5), Fraction(1, 2), "half", "three-fifths", "half", "نصف", "ثلاثة أخماس", "نصف"),
    ]
    for p1, p2, p3, w1_e, w2_e, w3_e, w1_a, w2_a, w3_a in cup_cases:
        qid = next_id()
        # Start: c1=100%, c2=0, c3=0
        c1, c2, c3 = Fraction(100), Fraction(0), Fraction(0)
        mv1 = c1 * p1
        c1 -= mv1; c2 += mv1
        s1_tup = (c1, c2, c3)
        mv2 = c2 * p2
        c2 -= mv2; c3 += mv2
        s2_tup = (c1, c2, c3)
        mv3 = c3 * p3
        c3 -= mv3; c1 += mv3
        ans_pct = float(c1) if c1.denominator != 1 else int(c1)
        svg = svg_water_cups((1.0, 0.0, 0.0), ("Cup 1", "Cup 2", "Cup 3"))
        q_en = (
            f"Three identical cups stand on a table: Cup 1 is completely full of water ({m('100\\%')}) and Cups 2 and 3 are empty. "
            f"First, Ali pours **{w1_e}** of the water in Cup 1 into Cup 2. "
            f"Next, he pours **{w2_e}** of the water now in Cup 2 into Cup 3. "
            f"Finally, he pours **{w3_e}** of the water now in Cup 3 back into Cup 1. "
            f"What percentage of Cup 1 is filled with water at the end?"
        )
        q_ar = (
            f"توجد ثلاثة أكواب متطابقة على طاولة: الكوب 1 ممتلئ تمامًا بالماء ({m('100\\%')}) والكوبان 2 و 3 فارغان. "
            f"يسكب علي أولًا **{w1_a}** الماء من الكوب 1 في الكوب 2، ثم يسكب **{w2_a}** الماء الموجود في الكوب 2 في الكوب 3، "
            f"وأخيرًا يسكب **{w3_a}** الماء الموجود في الكوب 3 عائدًا إلى الكوب 1. "
            f"ما النسبة المئوية لامتلاء الكوب 1 بالماء في النهاية؟"
        )
        ans_disp = f"{ans_pct:g}"
        distractors = [f"{ans_pct - 4:g}", f"{ans_pct + 2.5:g}", f"{ans_pct - 2.5:g}", f"{ans_pct + 5:g}"]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_disp, distractors, qid, suffix="\\%")
        sol_en = explain_en(
            "Imagine Cup 1 starts with **100 units** of water so that every cup's amount directly equals its percentage!",
            [
                f"**Start:** Cup 1 = {m(100)}, Cup 2 = {m(0)}, Cup 3 = {m(0)}.",
                f"**First pour ({w1_e} from Cup 1 to Cup 2):** {m(float(mv1) if mv1.denominator!=1 else int(mv1))} units move, so Cup 1 = {m(f'{float(s1_tup[0]):g}')}, Cup 2 = {m(f'{float(s1_tup[1]):g}')}, Cup 3 = {m(0)}.",
                f"**Second pour ({w2_e} from Cup 2 to Cup 3):** {m(f'{float(mv2):g}')} units move, so Cup 1 = {m(f'{float(s2_tup[0]):g}')}, Cup 2 = {m(f'{float(s2_tup[1]):g}')}, Cup 3 = {m(f'{float(s2_tup[2]):g}')}.",
                f"**Third pour ({w3_e} from Cup 3 to Cup 1):** {m(f'{float(mv3):g}')} units return to Cup 1, giving Cup 1 = {m(f'{float(s2_tup[0]):g} + {float(mv3):g} = {ans_disp}\\%')}.",
            ],
            f"Total water check: Cup 1 ({m(f'{ans_disp}')}) + Cup 2 ({m(f'{float(c2):g}')}) + Cup 3 ({m(f'{float(c3):g}')}) = {m(100)} units (no water lost!).",
        )
        sol_ar = explain_ar(
            "لنفترض أن سعة الكوب الواحد هي **100 وحدة** من الماء، وعندها يمثّل عدد الوحدات في كل كوب نسبته المئوية مباشرة!",
            [
                f"**في البداية:** الكوب 1 = {m(100)}، الكوب 2 = {m(0)}، الكوب 3 = {m(0)}.",
                f"**السكبة الأولى ({w1_a} من 1 إلى 2):** ينتقل {m(f'{float(mv1):g}')}، فيصبح الكوب 1 = {m(f'{float(s1_tup[0]):g}')}، والكوب 2 = {m(f'{float(s1_tup[1]):g}')}، والكوب 3 = {m(0)}.",
                f"**السكبة الثانية ({w2_a} من 2 إلى 3):** ينتقل {m(f'{float(mv2):g}')}، فيصبح الكوب 2 = {m(f'{float(s2_tup[1]):g}')}، والكوب 3 = {m(f'{float(s2_tup[2]):g}')}.",
                f"**السكبة الثالثة ({w3_a} من 3 إلى 1):** يعود {m(f'{float(mv3):g}')} إلى الكوب 1، فيصبح فيه {m(f'{float(s2_tup[0]):g} + {float(mv3):g} = {ans_disp}\\%')}.",
            ],
            f"نتحقق بجمع الماء في الأكواب الثلاثة: {m(f'{ans_disp} + {float(c2):g} + {float(c3):g} = 100')} وحدة تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-water-cups-percent",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Start with 100 units of water in Cup 1 and write down the three cup amounts after each pour.",
            "ابدأ بافتراض وجود 100 وحدة ماء في الكوب 1 وسجّل كمية الماء في الأكواب الثلاثة بعد كل خطوة.",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 13. Ratio shift when k items join/leave (boys:girls, red:blue) (8 variants) — KMC G6-7 Sample Q9
    ratio_shift = [
        (3, 5, 4, "boys", "girls", "students in the class", "البنين", "البنات", "طلاب الفصل"),
        (2, 5, 9, "red pens", "blue pens", "pens in the box", "الأقلام الحمراء", "الأقلام الزرقاء", "الأقلام في العلبة"),
        (3, 7, 12, "science books", "storybooks", "books on the shelf", "الكتب العلمية", "القصص", "الكتب على الرف"),
        (4, 7, 6, "green apples", "red apples", "apples in the basket", "التفاح الأخضر", "التفاح الأحمر", "التفاحات في السلة"),
        (2, 3, 5, "gold medals", "silver medals", "medals in the display", "الميداليات الذهبية", "الميداليات الفضية", "الميداليات في الخزانة"),
        (5, 8, 9, "juniors", "seniors", "members in the club", "الناشئين", "الكبار", "أعضاء النادي"),
        (1, 3, 8, "vans", "buses", "vehicles in the yard", "الحافلات الصغيرة", "الحافلات الكبيرة", "المركبات في الساحة"),
        (4, 9, 15, "tulips", "daisies", "flowers in the garden bed", "أزهار التوليب", "أزهار الأقحوان", "الأزهار في الحوض"),
    ]
    for a, b, add_n, g1_e, g2_e, tot_e, g1_a, g2_a, tot_a in ratio_shift:
        qid = next_id()
        diff_parts = b - a
        assert add_n % diff_parts == 0
        k = add_n // diff_parts
        ans = (a + b) * k
        q_en = (
            f"Originally, the ratio of {g1_e} to {g2_e} is {m(f'{a} : {b}')}. "
            f"After {m(add_n)} more {g1_e} are added (with no change in {g2_e}), the numbers of {g1_e} and {g2_e} become **equal**. "
            f"How many {tot_e} were there **originally**?"
        )
        q_ar = (
            f"في البداية كانت النسبة بين عدد {g1_a} إلى عدد {g2_a} هي {m(f'{a} : {b}')}. "
            f"وبعد إضافة {m(add_n)} إلى {g1_a} (دون تغيير عدد {g2_a}) أصبح العددان **متساويين**. "
            f"كم كان إجمالي عدد {tot_a} **في الأصل**؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + add_n, b * k, 2 * b * k, a * k, ans + 4], qid
        )
        sol_en = explain_en(
            f"Think in equal ratio parts! Originally {g1_e} have {m(a)} parts and {g2_e} have {m(b)} parts, so {g1_e} are behind by {m(f'{b} - {a} = {diff_parts}')} parts.",
            [
                f"Write the original counts using a part size {m('k')}: {g1_e} {m(f'= {a}k')} and {g2_e} {m(f'= {b}k')}.",
                f"Adding {m(add_n)} makes them equal, which means those {m(add_n)} new items fill the gap of {m(f'{b}k - {a}k = {diff_parts}k')}: so {m(f'{diff_parts}k = {add_n}')}, giving {m(f'k = {add_n} \\div {diff_parts} = {k}')}.",
                f"The **original** total had {m(f'{a}k + {b}k = {a+b}k')} items: {m(f'{a+b} \\times {k} = {ans}')}.",
            ],
            f"Check: originally {m(a*k)} and {m(b*k)} (ratio {m(f'{a}:{b}')}); after adding {m(add_n)} to {m(a*k)} we get {m(a*k + add_n)}, matching {m(b*k)}! (Watch out: {m(ans + add_n)} is the *new* total, whereas {m(ans)} is the *original* total.)",
        )
        sol_ar = explain_ar(
            f"نعبّر عن النسبة بأجزاء متساوية طول الواحد منها {m('k')}: في البداية {g1_a} {m(f'= {a}k')} و{g2_a} {m(f'= {b}k')}، والفرق بينهما {m(f'{b} - {a} = {diff_parts}')} أجزاء.",
            [
                f"بما أن إضافة {m(add_n)} سدّت الفرق وجعلت العددين متساويين، فإن {m(f'{diff_parts}k = {add_n}')}.",
                f"نقسم الطرفين على {m(diff_parts)} فنجد قيمة الجزء الواحد: {m(f'k = {add_n} \\div {diff_parts} = {k}')}.",
                f"العدد الكلي **في الأصل** يساوي مجموع الأجزاء الأصلية {m(f'({a} + {b})k = {a+b} \\times {k} = {ans}')}.",
            ],
            f"تحقق: في الأصل كان العددان {m(a*k)} و {m(b*k)}، وعند إضافة {m(add_n)} إلى {m(a*k)} يصبح {m(a*k + add_n)} مساويًا لـ {m(b*k)} تمامًا!",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-ratio-equalize",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Represent the original counts as {a}k and {b}k. Adding {add_n} bridges the gap ({b} - {a})k!",
            f"مثّل العددين الأصليين بالصورة {a}k و {b}k؛ إضافة {add_n} تسد الفجوة البالغة ({b} - {a})k!",
            sol_en, sol_ar
        ))

    # 14. Successive percentage increase then decrease (+p% then -p%) (8 variants)
    up_down_cases = [
        (20, 20, 150, "jacket", "سترة"),
        (10, 10, 200, "headphones", "سماعة رأس"),
        (25, 20, 160, "backpack", "حقيبة ظهر"),
        (20, 25, 120, "board game", "لعبة لوحية"),
        (50, 20, 100, "wristwatch", "ساعة يد"),
        (30, 10, 200, "desk lamp", "مصباح مكتب"),
        (40, 25, 200, "telescope", "منظار فلكي"),
        (10, 20, 250, "bicycle helmet", "خوذة دراجة"),
    ]
    for p_up, p_dn, p0, item_e, item_a in up_down_cases:
        qid = next_id()
        after_up = p0 * (100 + p_up) // 100
        ans = after_up * (100 - p_dn) // 100
        assert (p0 * (100 + p_up)) % 100 == 0 and (after_up * (100 - p_dn)) % 100 == 0
        q_en = (
            f"A store originally priced a {item_e} at {m(p0)} riyals. First, its price was increased by {m(f'{p_up}\\%')}. "
            f"Later, during a weekend sale, the **new** price was reduced by {m(f'{p_dn}\\%')}. What is the final price in riyals?"
        )
        q_ar = (
            f"كان السعر الأصلي لـ{item_a} في متجر هو {m(p0)} ريالًا. ارتفع سعرها أولًا بنسبة {m(f'{p_up}\\%')}، "
            f"ثم في تخفيضات نهاية الأسبوع خُفِّض **السعر الجديد** بنسبة {m(f'{p_dn}\\%')}. كم أصبح السعر النهائي بالريال؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [p0, p0 + (p_up - p_dn) * p0 // 100 if p_up != p_dn else ans + 6, after_up, ans - 5, ans + 8], qid
        )
        sol_en = explain_en(
            "Be careful: the second percentage applies to the **updated price**, NOT the original price! Calculate one change at a time.",
            [
                f"**First change (+{p_up}%):** {m(f'{p_up}\\%')} of {m(p0)} is {m(f'\\frac{{{p_up}}}{{100}} \\times {p0} = {after_up - p0}')} riyals. Add this to {m(p0)} to get the new price: {m(f'{p0} + {after_up - p0} = {after_up}')} riyals.",
                f"**Second change (-{p_dn}% of {after_up}):** {m(f'{p_dn}\\%')} of {m(after_up)} is {m(f'\\frac{{{p_dn}}}{{100}} \\times {after_up} = {after_up - ans}')} riyals.",
                f"Subtract that discount from {m(after_up)}: {m(f'{after_up} - {after_up - ans} = {ans}')} riyals.",
            ],
            f"Notice why +{p_up}% followed by -{p_dn}% does NOT simply cancel out when {m(f'{p_up}={p_dn}')}: the discount is taken from the larger number {m(after_up)}!",
        )
        sol_ar = explain_ar(
            "انتبه جيدًا: التخفيض الثاني يُحسب من **السعر الجديد بعد الزيادة** وليس من السعر الأصلي! لذا نحسب كل خطوة على حدة.",
            [
                f"**الخطوة الأولى (زيادة {p_up}%):** مقدار الزيادة هو {m(f'\\frac{{{p_up}}}{{100}} \\times {p0} = {after_up - p0}')} ريالًا، فيصبح السعر الجديد {m(f'{p0} + {after_up - p0} = {after_up}')} ريالًا.",
                f"**الخطوة الثانية (تخفيض {p_dn}% من {after_up}):** مقدار الخصم هو {m(f'\\frac{{{p_dn}}}{{100}} \\times {after_up} = {after_up - ans}')} ريالًا.",
                f"نطرح مقدار الخصم من {m(after_up)}: {m(f'{after_up} - {after_up - ans} = {ans}')} ريالًا.",
            ],
            f"لاحظ أن أخذ خصم من عدد أكبر ({m(after_up)}) يعطي قيمة مختلفة عن العودة المباشرة للسعر الأول؛ فالسعر النهائي هو {m(ans)} ريالًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-successive-percent",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"First compute the new price after adding {p_up}% to {p0}, then take {p_dn}% off that new price.",
            f"احسب أولًا السعر الجديد بعد زيادة {p_up}% على {p0}، ثم اخفض {p_dn}% من ذلك السعر الجديد.",
            sol_en, sol_ar
        ))

    # 15. Smallest / largest N-digit number with given digit product or digit sum (8 variants)
    digit_prod_cases = [
        (2, "product", 24, "smallest", 38, "حاصل ضرب", "أصغر"),
        (2, "product", 36, "smallest", 49, "حاصل ضرب", "أصغر"),
        (3, "product", 18, "smallest", 129, "حاصل ضرب", "أصغر"),
        (3, "product", 24, "smallest", 138, "حاصل ضرب", "أصغر"),
        (3, "product", 36, "smallest", 149, "حاصل ضرب", "أصغر"),
        (3, "sum", 20, "smallest", 299, "مجموع", "أصغر"),
        (3, "sum", 19, "smallest", 199, "مجموع", "أصغر"),
        (3, "product", 45, "smallest", 159, "حاصل ضرب", "أصغر"),
    ]
    for ndig, kind, target_v, extr_e, ans, kind_a, extr_a in digit_prod_cases:
        qid = next_id()
        # Verify by brute force!
        lo, hi = 10 ** (ndig - 1), 10 ** ndig
        valid = []
        for x in range(lo, hi):
            ds = [int(c) for c in str(x)]
            val = math.prod(ds) if kind == "product" else sum(ds)
            if val == target_v:
                valid.append(x)
        assert min(valid) == ans, (ndig, kind, target_v, min(valid), ans)
        word_n_e = "two-digit" if ndig == 2 else "three-digit"
        word_n_a = "مكوّن من خانتين" if ndig == 2 else "مكوّن من ثلاث خانات"
        q_en = f"What is the **{extr_e}** positive {word_n_e} integer whose digits have a {kind} equal to {m(target_v)}?"
        q_ar = f"ما **{extr_a}** عدد صحيح موجب {word_n_a} يكون {kind_a} أرقامه مساويًا لـ {m(target_v)}؟"
        alt_d = sorted(valid)[1] if len(valid) > 1 else ans + 9
        rev_d = int(str(ans)[::-1])
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [alt_d, rev_d if rev_d != ans else ans + 18, ans + 9, ans + 11], qid
        )
        ds_ans = [int(c) for c in str(ans)]
        op_sym = "\\times" if kind == "product" else "+"
        sol_en = explain_en(
            f"To make a multi-digit number as **small** as possible, make its **leftmost digit** (hundreds or tens) as **small** as possible, which means packing as much as possible into the rightmost digit(s) (up to {m(9)})!",
            [
                f"Start from the rightmost (ones) place and put the largest valid single digit (at most {m(9)}) that works cleanly with {m(target_v)}: here the ones digit is {m(ds_ans[-1])}.",
                f"Arrange the remaining digit(s) so the leftmost non-zero digit is as small as possible: the digits in order from left to right are {', '.join(m(d) for d in ds_ans)}.",
                f"Combine them into the {word_n_e} number {m(ans)}.",
            ],
            f"Verify the digit {kind}: {m(f' {op_sym} '.join(map(str, ds_ans)) + f' = {target_v}')}, and no smaller {word_n_e} integer achieves {m(target_v)}!",
        )
        sol_ar = explain_ar(
            f"لجعل العدد **أصغر ما يمكن**، نجعل الرقم في **الخانة اليسرى (الأعلى منزلة)** أصغر ما يمكن، وذلك بوضع أكبر رقم مسموح (حتى {m(9)}) في خانة الآحاد على اليمين!",
            [
                f"نضع أكبر رقم مناسب في خانة الآحاد أولًا وهو {m(ds_ans[-1])} حتى نترك أصغر قيمة ممكنة للخانات اليسرى.",
                f"نرتب الأرقام من اليسار إلى اليمين تصاعديًا: {' ثم '.join(m(d) for d in ds_ans)}.",
                f"نحصل بذلك على العدد {m(ans)}.",
            ],
            f"نتحقق من {kind_a} الأرقام: {m(f' {op_sym} '.join(map(str, ds_ans)) + f' = {target_v}')}، وهو أصغر عدد موجب {word_n_a} يحقق الشرط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Number Theory", "Medium", "g67-smallest-digit-prod-sum",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Make the leftmost digit as small as possible by placing the largest valid digit (at most 9) on the right.",
            "اجعل الخانة اليسرى أصغر ما يمكن بوضع أكبر رقم مناسب (لا يتجاوز 9) في خانة الآحاد يمينًا.",
            sol_en, sol_ar
        ))

    assert len(items) == 120, f"Expected 120 items, got {len(items)}"
    return items


if __name__ == "__main__":
    qs = generate_t1_numbers()
    print(f"Generated {len(qs)} Track 1 Numbers questions cleanly.")
