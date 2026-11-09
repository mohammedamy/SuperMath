"""Comprehensive Pedagogical & Visual Enhancements for All 18 KAUST (KMC) Study Academy Lessons (KMC-L1-01..KMC-L3-06).

Adds to every lesson:
- A 4th Illustrated Core Concept Card (54 -> 72 concept cards, 100% bilingual EN/AR SVGs) covering the expanded KMC blueprints
- A 5th Learning Goal (72 -> 90 goals)
- Expanded Common KMC Exam Traps (38 -> 72 traps, 4 per lesson)
- A 4-Card Quick Formula & Strategy Cheat-Sheet (72 cheat-sheet cards across 18 lessons)
- +31 New Bespoke Core Worked Examples with 100% bilingual EN/AR SVGs (77 -> 108 bespoke worked examples, 6 per lesson)
"""
from fractions import Fraction
from kmc_common import m, _format_prose_html
import kmc_diagrams_extra as D
from kmc_lesson_helpers import dm, concept, worked_math_example


def cheat_item(title_en: str, title_ar: str, formula: str, note_en: str, note_ar: str) -> dict:
    return {
        "en": {
            "title": _format_prose_html(title_en),
            "formula": _format_prose_html(formula),
            "note": _format_prose_html(note_en),
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "formula": _format_prose_html(formula),
            "note": _format_prose_html(note_ar),
        },
    }


LESSON_ENHANCEMENTS: dict[str, dict] = {
    # =========================================================================
    # TRACK 1: GRADES 6–7 (KMC-L1-01 .. KMC-L1-06)
    # =========================================================================
    "KMC-L1-01": {
        "extra_goals": [
            (
                "Evaluate **Buy-M-Get-K** bundle promotions and equal-capacity two-jar transfers using common-denominator units.",
                "حساب عروض **«اشترِ M واحصل على K مجاناً»** ومسائل نقل السوائل بين وعاءين متساويي السعة بتوحيد المقامات.",
            ),
        ],
        "extra_concept": concept(
            "4. Visual Fraction Grids, Bundle Promotions & Two-Jar Transfers",
            "٤. شبكات الكسور، عروض الحزم المجانية، والنقل بين الوعاءين",
            f"In a grid of {m('R \\times C')} equal cells, shading {m('a')} cells and then {m('b')} more gives {m('\\frac{a+b}{RC}')}. "
            f"For a **'Buy {m('M')}, Get {m('K')} Free'** promotion, you receive {m('M + K')} items while paying for {m('M')}, so the effective discount rate is {m('\\frac{K}{M + K}')} (not {m('\\frac{K}{M}')}!). "
            f"When transferring between two equal-capacity jars filled to fractions {m('\\frac{a}{b}')} and {m('\\frac{c}{d}')}, set each jar's capacity to {m('\\operatorname{lcm}(b, d)')} units.",
            f"في شبكة مكوّنة من {m('R \\times C')} مربعات متطابقة، تظليل {m('a')} ثم {m('b')} مربعاً يعطي الكسر {m('\\frac{a+b}{RC}')}. "
            f"وفي عرض **«اشترِ {m('M')} واحصل على {m('K')} مجاناً»** تستلم {m('M + K')} قطع وتدفع ثمن {m('M')} فقط، فتكون نسبة الخصم الفعلية {m('\\frac{K}{M + K}')} وليست {m('\\frac{K}{M}')}! "
            f"وعند نقل السوائل بين وعاءين متماثلين مملوءين بالكسرين {m('\\frac{a}{b}')} و{m('\\frac{c}{d}')}، افرض سعة كل وعاء {m('\\operatorname{lcm}(b, d)')} وحدة.",
            dm("\\text{Effective Discount} = \\frac{K}{M + K} \\times 100\\%, \\qquad C_{\\text{jar}} = \\operatorname{lcm}(b, d)"),
            f'<div class="eg-f-caption" dir="rtl">نسبة الخصم الفعلي في العروض وسعة الوعاء المشتركة:</div>{dm("D_{\\text{eff}} = \\frac{K}{M + K} \\times 100\\%, \\qquad C = \\operatorname{lcm}(b, d)")}',
            diagram_en=D.svg_fraction_grid(5, 4, 9, 3),
            diagram_ar=D.svg_fraction_grid(5, 4, 9, 3),
        ),
        "extra_traps": [
            (
                "Trap: Thinking 'Buy 3, Get 1 Free' is a \\( 33.3\\% \\) discount — you get \\( 4 \\) items and get \\( 1 \\) free, so the true discount is \\( \\frac{1}{4} = 25\\% \\)!",
                "فخ شائع: الاعتقاد بأن عرض «اشترِ 3 واحصل على 1 مجاناً» يمثّل خصماً قدره \\( 33.3\\% \\) — الصحيح أنك تستلم \\( 4 \\) قطع منها \\( 1 \\) مجانية، فالخصم \\( \\frac{1}{4} = 25\\% \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Remainder Chain", "سلسلة البواقي", r"\(F_{\text{left}} = (1 - f_1)(1 - f_2)\)", "Multiply what stays after each step.", "اضرب الكسور المتبقية بعد كل خطوة."),
            cheat_item("Unchanged Ratio Anchor", "تثبيت المقدار الثابت", r"\(1\text{ unit} = \frac{\Delta Q}{\Delta n}\)", "Match the ratio part of the unchanged ingredient.", "وحّد حصة المكون الذي لم يتغير."),
            cheat_item("Successive % Change", "التغير المئوي المتتالي", r"\(M = \left(1 \pm \frac{p_1}{100}\right)\!\left(1 \pm \frac{p_2}{100}\right)\)", "Never add consecutive percentage changes.", "لا تجمع النسب المئوية المتتالية أبداً."),
            cheat_item("Buy M Get K Free", "اشترِ M واحصل على K مجاناً", r"\(\text{Discount} = \frac{K}{M + K}\)", "Divide free items by total items received.", "اقسم القطع المجانية على إجمالي القطع المستلمة."),
        ],
        "extra_examples": [
            worked_math_example(
                "L11-E5",
                "Solved Example 5 — Buy-M-Get-K Bundle Promotion",
                "مثال محلول ٥ — عرض الحزم المجانية (اشترِ M واحصل على K)",
                f"A bookstore offers a **'Buy {m(3)} notebooks, get {m(2)} free'** promotion, where each notebook normally costs {m(15)} riyals. If Omar needs {m(20)} notebooks, what is the **effective percentage discount** he receives compared to the regular price?",
                f"يقدّم متجر قرطاسية عرض **«اشترِ {m(3)} دفاتر واحصل على {m(2)} مجاناً»**، علماً أن سعر الدفتر العادي {m(15)} ريالاً. إذا اشترى عمر {m(20)} دفتراً ضمن العرض، فما **النسبة المئوية للخصم الفعلي** الذي حصل عليه؟",
                40, [25, 30, 50, 60],
                "In every bundle of \\( 3 + 2 = 5 \\) notebooks, exactly \\( 2 \\) are free!",
                [
                    f"Each bundle gives {m('3 + 2 = 5')} notebooks for the price of {m(3)} notebooks.",
                    f"The fraction of free notebooks in every bundle (and in {m(20)} notebooks = {m(4)} bundles) is {m('\\frac{2}{3 + 2} = \\frac{2}{5}')}.",
                    f"Convert to a percentage: {m('\\frac{2}{5} \\times 100\\% = 40\\%')}.",
                ],
                f"Regular cost of {m(20)} notebooks: {m('20 \\times 15 = 300')}. Promo cost: {m('4 \\times 3 \\times 15 = 180')}, saving {m('120 / 300 = 40\\%')}.",
                "في كل حزمة من \\( 3 + 2 = 5 \\) دفاتر، يحصل المشتري على دفترين مجاناً من أصل \\( 5 \\)!",
                [
                    f"تضم الحزمة الواحدة {m('3 + 2 = 5')} دفاتر يدفع منها ثمن {m(3)} فقط.",
                    f"نسبة التوفير في كل حزمة هي {m('\\frac{2}{5} = 40\\%')}.",
                ],
                f"السعر الأصلي {m('20 \\times 15 = 300')} ريال، وسعر العرض {m('12 \\times 15 = 180')} ريالاً، والتوفير {m('120/300 = 40\\%')}.",
                suffix="%",
                diagram_en=D.svg_tape_bar_split([(0.60, "Pay 3"), (0.40, "Free 2")], "Bundle = 5"),
                diagram_ar=D.svg_tape_bar_split([(0.60, "يدفع 3"), (0.40, "مجاناً 2")], "الحزمة = 5"),
            ),
            worked_math_example(
                "L11-E6",
                "Solved Example 6 — Equal-Capacity Two-Jar Transfer",
                "مثال محلول ٦ — نقل الماء بين وعاءين متساويي السعة",
                f"Jar A and Jar B have the **same total capacity**. Jar A is {m('\\frac{3}{8}')} full of water and Jar B is {m('\\frac{5}{6}')} full of water. Enough water is poured from Jar B into Jar A to fill Jar A **completely to the brim**. What fraction of Jar B remains filled?",
                f"الوعاء A والوعاء B لهما **السعة الكلية نفسها**. الوعاء A مملوء بالماء حتى {m('\\frac{3}{8}')} سعته، والوعاء B مملوء حتى {m('\\frac{5}{6}')} سعته. سُكب ماء من B إلى A حتى امتلأ الوعاء A **تماماً**. ما الكسر الذي يمثّل الجزء المتبقي في الوعاء B؟",
                Fraction(5, 24), [Fraction(1, 6), Fraction(7, 24), Fraction(1, 4), Fraction(3, 8)],
                "Let each jar have capacity \\( \\operatorname{lcm}(8, 6) = 24 \\) units so every fraction becomes an integer!",
                [
                    f"Choose a common capacity of {m('\\operatorname{lcm}(8, 6) = 24')} units for each jar.",
                    f"Initially, Jar A has {m('\\frac{3}{8} \\times 24 = 9')} units and Jar B has {m('\\frac{5}{6} \\times 24 = 20')} units.",
                    f"To fill Jar A to {m(24)} units, we pour {m('24 - 9 = 15')} units from Jar B, leaving {m('20 - 15 = 5')} units in Jar B, or {m('\\frac{5}{24}')}.",
                ],
                f"Total water conserved: {m('\\frac{3}{8} + \\frac{5}{6} = \\frac{29}{24} = 1 + \\frac{5}{24}')}.",
                "افرض سعة كل وعاء \\( \\operatorname{lcm}(8, 6) = 24 \\) وحدة لتحويل الكسور إلى أعداد صحيحة!",
                [
                    f"بسعة {m(24)} وحدة لكل وعاء، يحوي A في البداية {m('9')} وحدات ويحوي B {m('20')} وحدة.",
                    f"يحتاج الوعاء A إلى {m('24 - 9 = 15')} وحدة ليمتلئ، فيبقى في B {m('20 - 15 = 5')} وحدات من {m(24)} أي {m('\\frac{5}{24}')}.",
                ],
                f"مجموع الماء ثابت: {m('\\frac{9}{24} + \\frac{20}{24} = 1 + \\frac{5}{24}')}.",
                diagram_en=D.svg_two_jars("A (3/8)", 0.38, "B (5/6)", 0.83, "Fill A → B=?"),
                diagram_ar=D.svg_two_jars("A (3/8)", 0.38, "B (5/6)", 0.83, "ملء A ← باقي B=؟"),
            ),
        ],
    },

    "KMC-L1-02": {
        "extra_goals": [
            (
                "Count **24-hour digital clock palindromes** and apply composite divisibility tests for **3, 4, and 6** simultaneously.",
                "عدّ **الأوقات المتناظرة على الساعة الرقمية (24 ساعة)** وتطبيق شروط قابلية القسمة المركّبة على **3 و4 و6** معاً.",
            ),
        ],
        "extra_concept": concept(
            "4. Digital Clock Palindromes & Composite Divisibility (÷3, ÷4, ÷6)",
            "٤. تناظر الساعة الرقمية وقابلية القسمة المركّبة (3، 4، 6)",
            f"A 24-hour digital display {m('AB:BA')} is a palindrome when the hour {m('AB \\in \\{00, 01, \\dots, 23\\}')} has reversed minutes {m('BA < 60')}, requiring units digit {m('B \\in \\{0,1,2,3,4,5\\}')}. "
            f"For missing-digit divisibility by {m(6)}, enforce **both** even last digit ({m('\\div 2')}) and digit sum divisible by {m(3)} ({m('\\div 3')}); for {m('\\div 4')}, check only the **last two digits**.",
            f"تكون قراءة الساعة الرقمية بنظام 24 ساعة {m('AB:BA')} متناظرة عندما تكون الساعة {m('AB \\in \\{00, \\dots, 23\\}')} والدقائق المعكوسة {m('BA < 60')}، أي يجب أن يكون رقم الآحاد {m('B \\in \\{0,1,2,3,4,5\\}')}. "
            f"ولقابلية القسمة على {m(6)}، طبّق شرطَي الزوجية ({m('\\div 2')}) ومجموع الأرقام ({m('\\div 3')}) معاً؛ وللقسمة على {m(4)} افحص **آخر رقمين فقط**.",
            dm("6 \\mid N \\iff (2 \\mid N)\\;\\wedge\\;(3 \\mid S_{\\text{digits}}), \\qquad 4 \\mid N \\iff 4 \\mid (10d_{\\text{tens}} + d_{\\text{units}})"),
            f'<div class="eg-f-caption" dir="rtl">شرطا قابلية القسمة على 6 وعلى 4:</div>{dm("6 \\mid N \\iff (2 \\mid N) \\wedge (3 \\mid S), \\qquad 4 \\mid N \\iff 4 \\mid \\overline{d_1 d_0}")}',
            diagram_en=D.svg_digital_clock("15:51", "B ∈ {0..5} ⇒ BA < 60"),
            diagram_ar=D.svg_digital_clock("15:51", "شرط الدقائق: B ∈ {0..5}"),
        ),
        "extra_traps": [
            (
                "Trap: Counting `06:60` or `16:61` as valid digital-clock palindromes — minutes can never be \\( 60 \\) or more!",
                "فخ شائع: احتساب `06:60` أو `16:61` كأوقات متناظرة صحيحة — خانة الدقائق يجب أن تكون أقل من \\( 60 \\) دائماً!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Cycle Synchronization", "التقاء الدورات", r"\(T = \operatorname{lcm}(t_1, t_2, t_3)\)", "Use LCM when periodic events repeat together.", "استخدم م.م.أ عند تلاقي أحداث دورية."),
            cheat_item("Inclusion–Exclusion (2 Sets)", "التضمين والإقصاء", r"\(|A \cup B| = |A| + |B| - |A \cap B|\)", "Subtract the overlap counted twice.", "اطرح التقاطع المكرر مرتين."),
            cheat_item("Divisibility by 4 & 6", "القسمة على 4 و6", r"\(4 \mid \overline{d_1 d_0}, \quad 6 \mid N \iff 2\mid N \;\wedge\; 3\mid S\)", "Last 2 digits for 4; even + digit-sum for 6.", "آخر خانتين للعدد 4؛ زوجي + مجموع الأرقام للعدد 6."),
            cheat_item("24-Hour Clock Palindromes", "تناظر الساعة AB:BA", r"\(A \in \{0,1,2\},\; B \in \{0..5\}\)", "Minutes BA < 60 requires B ≤ 5.", "شرط الدقائق أقل من 60 يتطلب B ≤ 5."),
        ],
        "extra_examples": [
            worked_math_example(
                "L12-E5",
                "Solved Example 5 — 24-Hour Digital Clock Palindromes",
                "مثال محلول ٥ — الأوقات المتناظرة على ساعة 24 ساعة",
                f"A 24-hour digital clock displays time in the four-digit format {m('HH:MM')} from {m('00:00')} to {m('23:59')}. How many times during one full day (24 hours) is the four-digit display a **palindrome** (reading the same forwards and backwards, such as {m('13:31')})?",
                f"تعرض ساعة رقمية بنظام 24 ساعة الوقت بالصيغة {m('HH:MM')} من {m('00:00')} إلى {m('23:59')}. كم مرة خلال يوم كامل (24 ساعة) تكون القراءة المكونة من أربعة أرقام **متناظرة** (تُقرأ من اليمين كقراءتها من اليسار مثل {m('13:31')})؟",
                16, [12, 14, 15, 24],
                "For \\( AB:BA \\) to be a valid time, the reversed minute \\( BA \\) must be less than \\( 60 \\), so \\( B \\in \\{0, 1, 2, 3, 4, 5\\} \\)!",
                [
                    f"When the first digit is {m('A = 0')} or {m('A = 1')}, the second digit {m('B')} can be any of {m('\\{0, 1, 2, 3, 4, 5\\}')} so that {m('BA < 60')}: that gives {m('6 + 6 = 12')} palindromes.",
                    f"When {m('A = 2')}, the hour {m('2B')} is at most {m(23)}, so {m('B \\in \\{0, 1, 2, 3\\}')} ({m('20:02, 21:12, 22:22, 23:32')}), giving {m(4)} more.",
                    f"Total valid palindromic times: {m('12 + 4 = 16')}.",
                ],
                f"List check: {m('00:00..05:50')} ({m(6)}), {m('10:01..15:51')} ({m(6)}), {m('20:02..23:32')} ({m(4)}) -> {m('6 + 6 + 4 = 16')}.",
                "لكي يكون الوقت \\( AB:BA \\) صحيحاً يجب أن تكون الدقائق \\( BA < 60 \\)، أي \\( B \\in \\{0, 1, 2, 3, 4, 5\\} \\)!",
                [
                    f"عندما {m('A = 0')} أو {m('A = 1')}، يأخذ {m('B')} أي قيمة من {m('\\{0,1,2,3,4,5\\}')} فيعطي {m('6 + 6 = 12')} وقتاً.",
                    f"وعندما {m('A = 2')}، يجب أن تكون الساعة {m('2B \\le 23')} أي {m('B \\in \\{0,1,2,3\\}')} فيعطي {m(4)} أوقات إضافية.",
                    f"المجموع الكلي = {m('12 + 4 = 16')} مرة.",
                ],
                f"التحقق: {m('6 + 6 + 4 = 16')} وقتاً متناظراً.",
                diagram_en=D.svg_digital_clock("23:32", "A=0,1 (6 each) + A=2 (4) = ?"),
                diagram_ar=D.svg_digital_clock("23:32", "A=0,1 (6 لكلٍّ) + A=2 (4) = ؟"),
            ),
            worked_math_example(
                "L12-E6",
                "Solved Example 6 — Missing Digits for Simultaneous Divisibility by 3 and 4",
                "مثال محلول ٦ — إيجاد الأرقام المفقودة لقابلية القسمة على 3 و4",
                f"The four-digit number {m('\\overline{5A2B}')} is divisible by **both** {m(3)} and {m(4)}. What is the **maximum** possible value of the digit sum {m('A + B')}?",
                f"العدد المكون من أربعة أرقام {m('\\overline{5A2B}')} يقبل القسمة على **كلٍّ من** {m(3)} و{m(4)}. ما **أكبر** قيمة ممكنة لمجموع الرقمين {m('A + B')}؟",
                17, [13, 14, 15, 16],
                "Use divisibility by \\( 4 \\) on the last two digits \\( \\overline{2B} \\) first to maximize \\( B \\), then maximize \\( A \\) using divisibility by \\( 3 \\)!",
                [
                    f"For {m('\\overline{5A2B}')} to be divisible by {m(4)}, the two-digit ending {m('\\overline{2B}')} must be divisible by {m(4)}, so {m('B \\in \\{0, 4, 8\\}')}.",
                    f"To maximize {m('A + B')}, test the largest valid units digit {m('B = 8')}. Then the digit sum is {m('5 + A + 2 + 8 = 15 + A')}.",
                    f"For {m('15 + A')} to be divisible by {m(3)}, the largest single digit for {m('A')} is {m('A = 9')}, giving {m('A + B = 9 + 8 = 17')}.",
                ],
                f"Check {m('5928')}: {m('5928 \\div 4 = 1482')} and {m('5 + 9 + 2 + 8 = 24 = 3 \\times 8')}. Valid!",
                "ابدأ بقابلية القسمة على \\( 4 \\) في آخر رقمين \\( \\overline{2B} \\) لتعظيم \\( B \\)، ثم عظّم \\( A \\) بشرط القسمة على \\( 3 \\)!",
                [
                    f"يقبل {m('\\overline{2B}')} القسمة على {m(4)} عندما {m('B \\in \\{0, 4, 8\\}')}، ونختار أكبرها {m('B = 8')}.",
                    f"يصبح مجموع الأرقام {m('5 + A + 2 + 8 = 15 + A')}، وأكبر رقم {m('A')} يجعله مضاعفاً للعدد {m(3)} هو {m('A = 9')}.",
                    f"إذن أكبر قيمة للمجموع {m('A + B = 9 + 8 = 17')}.",
                ],
                f"التحقق: العدد {m(5928)} يقبل القسمة على {m(4)} ومجموع أرقامه {m(24)} يقبل القسمة على {m(3)}.",
                diagram_en=D.svg_digit_cards(["5", "A", "2", "B"], "÷3 and ÷4", "max(A + B) = ?"),
                diagram_ar=D.svg_digit_cards(["5", "A", "2", "B"], "يقبل على 3 و4", "أكبر A + B = ؟"),
            ),
        ],
    },

    "KMC-L1-03": {
        "extra_goals": [
            (
                "Invert **two-step function machines** and express the apex of a **3-row or 4-row additive number pyramid** in terms of the base row.",
                "عكس **آلات الدوال ذات الخطوتين** والتعبير عن قمة **هرم الأعداد الجمعي** بدلالة أعداد الصف السفلي.",
            ),
        ],
        "extra_concept": concept(
            "4. Figurate Dot Arrays, Inverse Function Machines & Additive Pyramids",
            "٤. أنماط النقاط، عكس آلات الدوال، وأهرامات الأعداد الجمعية",
            f"To invert a two-step function machine {m('x \\xrightarrow{\\times a} ax \\xrightarrow{+ b} y')}, reverse **both** the order and the operations: {m('x = (y - b) \\div a')}. "
            f"In a 3-row additive pyramid with base {m('(A, B, C)')}, the middle row is {m('(A+B,\\; B+C)')} and the top cell is {m('A + 2B + C')} (the middle base number is counted **twice**!).",
            f"لإيجاد المدخل في آلة دالة ذات خطوتين {m('x \\xrightarrow{\\times a} ax \\xrightarrow{+ b} y')}، اعكس **ترتيب العمليات ونوعها**: {m('x = (y - b) \\div a')}. "
            f"وفي هرم جمعي من 3 صفوف قاعدته {m('(A, B, C)')}، يكون الصف الأوسط {m('(A+B,\\; B+C)')} وقمة الهرم {m('A + 2B + C')} (العدد الأوسط في القاعدة يُجمع **مرتين**!).",
            dm("x = \\frac{y - b}{a}, \\qquad \\text{Top}_{3\\text{-row}} = A + 2B + C, \\qquad \\text{Top}_{4\\text{-row}} = A + 3B + 3C + D"),
            f'<div class="eg-f-caption" dir="rtl">عكس آلة الدالة وقمة الهرم الجمعي (معاملات باسكال):</div>{dm("x = \\frac{y - b}{a}, \\qquad T_3 = A + 2B + C, \\qquad T_4 = A + 3B + 3C + D")}',
            diagram_en=D.svg_number_pyramid("A + 2B + C", "A + B", "B + C", "A", "B", "C"),
            diagram_ar=D.svg_number_pyramid("A + 2B + C", "A + B", "B + C", "A", "B", "C"),
        ),
        "extra_traps": [
            (
                "Trap: Writing Top \\( = A + B + C \\) in a 3-row additive pyramid — the center base cell \\( B \\) feeds into **both** middle cells, so Top \\( = A + 2B + C \\)!",
                "فخ شائع: كتابة قمة الهرم الثلاثي \\( A + B + C \\) — الخلية الوسطى \\( B \\) تدخل في **كلا** مربعي الصف الأوسط، لذا القمة \\( = A + 2B + C \\)!",
            ),
            (
                "Trap: Reversing the operations of a function machine without reversing their **order** (undo the **last** operation first!).",
                "فخ شائع: عكس العمليات في آلة الدالة دون عكس **ترتيبها** (ابدأ دائماً بإلغاء **العملية الأخيرة** أولاً!).",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Adjacent Shapes", "الأشكال المتجاورة", r"\(S(n) = S_1 + (n - 1)\Delta S\)", "First shape + (n−1) × shared-edge increment.", "الشكل الأول + (n−1) × الزيادة الثابتة."),
            cheat_item("Inverse Function Machine", "عكس آلة الدالة", r"\(x \xrightarrow{\times a} \xrightarrow{+b} y \implies x = \frac{y - b}{a}\)", "Undo the last operation first.", "اعكس العملية الأخيرة أولاً."),
            cheat_item("3-Row Additive Pyramid", "قمة الهرم الثلاثي", r"\(\text{Top} = A + 2B + C\)", "The middle base cell B is counted twice.", "الخلية الوسطى B تُحسب مرتين."),
            cheat_item("Balance Substitution", "تعويض الموازين", r"\(a\bigcirc = b\square,\; c\square = d\triangle\)", "Express all shapes in terms of the lightest unit.", "عبّر عن جميع الأشكال بدلالة الأخف وزناً."),
        ],
        "extra_examples": [
            worked_math_example(
                "L13-E5",
                "Solved Example 5 — Solving for the Middle Base Cell of a Number Pyramid",
                "مثال محلول ٥ — إيجاد الخلية الوسطى في قاعدة هرم الأعداد",
                f"In a 3-row additive number pyramid, each cell above the bottom row equals the sum of the two cells directly below it. If the three bottom-row numbers are {m('14')}, {m('x')}, and {m('21')}, and the top cell is {m('83')}, what is the value of {m('x')}?",
                f"في هرم أعداد جمعي مكوّن من 3 صفوف، يساوي كل مربع فوق الصف السفلي مجموع المربعين اللذين تحته مباشرةً. إذا كانت أعداد الصف السفلي هي {m('14')} و{m('x')} و{m('21')}، وكان العدد في قمة الهرم {m('83')}، فما قيمة {m('x')}؟",
                24, [20, 22, 26, 48],
                "Use the 3-row pyramid identity \\( \\text{Top} = A + 2B + C \\) so you solve for \\( x \\) in one line!",
                [
                    f"The middle row has left cell {m('14 + x')} and right cell {m('x + 21')}.",
                    f"Adding them gives the top cell: {m('(14 + x) + (x + 21) = 35 + 2x = 83')}.",
                    f"Subtract {m(35)}: {m('2x = 48 \\implies x = 24')}.",
                ],
                f"Check: base {m('(14, 24, 21)')} -> middle {m('(38, 45)')} -> top {m('38 + 45 = 83')}. Exact!",
                "استخدم متطابقة قمة الهرم الثلاثي \\( \\text{Top} = A + 2B + C \\) لإيجاد \\( x \\) مباشرة!",
                [
                    f"الصف الأوسط يحتوي على {m('14 + x')} و{m('x + 21')}.",
                    f"مجموعهما في القمة: {m('35 + 2x = 83 \\implies 2x = 48 \\implies x = 24')}.",
                ],
                f"التحقق: القاعدة {m('(14, 24, 21)')} ← الوسط {m('(38, 45)')} ← القمة {m('38 + 45 = 83')}.",
                diagram_en=D.svg_number_pyramid("83", "14 + x", "x + 21", "14", "x = ?", "21"),
                diagram_ar=D.svg_number_pyramid("83", "14 + x", "x + 21", "14", "x = ؟", "21"),
            ),
            worked_math_example(
                "L13-E6",
                "Solved Example 6 — Working Backwards Through a Two-Step Function Machine",
                "مثال محلول ٦ — الرجوع العكسي في آلة دالة ذات خطوتين",
                f"A number {m('N')} enters a two-step function machine that first **multiplies by {m(4)}** and then **subtracts {m(9)}**. If the output is {m('3N + 11')}, what is the input number {m('N')}?",
                f"يدخل العدد {m('N')} في آلة دالة ذات خطوتين تقوم أولاً **بالضرب في {m(4)}** ثم **طرح {m(9)}**. إذا كان المخرج يساوي {m('3N + 11')}، فما قيمة العدد المدخل {m('N')}؟",
                20, [16, 18, 22, 24],
                "Write the machine's output algebraically as \\( 4N - 9 \\) and equate it to \\( 3N + 11 \\)!",
                [
                    f"Following the two steps on input {m('N')} produces output {m('4N - 9')}.",
                    f"Set this equal to the given expression: {m('4N - 9 = 3N + 11')}.",
                    f"Subtract {m('3N')} and add {m(9)}: {m('N = 20')}.",
                ],
                f"Check {m('N = 20')}: machine gives {m('4(20) - 9 = 71')}, and {m('3(20) + 11 = 71')}.",
                "اكتب مخرج الآلة جبرياً \\( 4N - 9 \\) وساوِه بالمقدار المعطى \\( 3N + 11 \\)!",
                [
                    f"مخرج الآلة عند إدخال {m('N')} هو {m('4N - 9')}.",
                    f"بمساواته بالمخرج المعطى: {m('4N - 9 = 3N + 11 \\implies N = 20')}.",
                ],
                f"التحقق عند {m('N = 20')}: {m('4(20) - 9 = 71')} و{m('3(20) + 11 = 71')}.",
                diagram_en=D.svg_function_machine("N = ?", "× 4", "− 9", "3N + 11"),
                diagram_ar=D.svg_function_machine("N = ؟", "× 4", "− 9", "3N + 11"),
            ),
        ],
    },

    "KMC-L1-04": {
        "extra_goals": [
            (
                "Avoid off-by-one errors in **fencepost tree-spacing** problems and solve **heads-and-legs (two-value)** systems by extreme-case replacement.",
                "تجنّب خطأ الزيادة أو النقصان بواحد في مسائل **الأعمدة والأشجار والمسافات البينية**، وحل مسائل **الرؤوس والأرجل** بطريقة الافتراض والتعويض.",
            ),
        ],
        "extra_concept": concept(
            "4. Fencepost Intervals (N − 1 Gaps) & Two-Value Replacement (Heads & Legs)",
            "٤. المسافات البينية (N − 1 فجوة) وطريقة الافتراض (الرؤوس والأرجل)",
            f"Along a straight road with {m('N')} trees planted at equal spacing {m('d')}, there are {m('N - 1')} **gaps**, so total length is {m('L = (N - 1)d')} (whereas around a **closed loop**, {m('N_{\\text{gaps}} = N')}). "
            f"For a two-value system (e.g. bicycles with {m(2)} wheels and cars with {m(4)} wheels totaling {m('H')} vehicles and {m('W')} wheels), assume **all {m('H')} are bicycles** ({m('2H')} wheels); each upgrade to a car adds {m('4 - 2 = 2')} wheels!",
            f"على طريق مستقيم زُرعت فيه {m('N')} شجرة بمسافات متساوية {m('d')}، يوجد {m('N - 1')} **مسافة بينية** فقط، فيكون الطول الكلي {m('L = (N - 1)d')} (أما في **مسار دائري مغلق** فعدد المسافات يساوي {m('N')}). "
            f"وفي مسائل القيمتين (مثل دراجات بعجلتين وسيارات بـ {m(4)} عجلات بمجموع {m('H')} مركبة و{m('W')} عجلة)، افرض أن **جميع المركبات دراجات** ({m('2H')} عجلة)، ثم اقسم فرق العجلات على {m('4 - 2 = 2')}!",
            dm("L_{\\text{line}} = (N - 1)d, \\qquad N_{\\text{large}} = \\frac{\\text{Total Value} - H \\cdot v_{\\text{small}}}{v_{\\text{large}} - v_{\\text{small}}}"),
            f'<div class="eg-f-caption" dir="rtl">قانون المسافات البينية وقانون الافتراض والتعويض:</div>{dm("L = (N - 1)d, \\qquad N_{\\text{large}} = \\frac{V_{\\text{total}} - H \\cdot v_{\\text{small}}}{v_{\\text{large}} - v_{\\text{small}}}")}',
            diagram_en=D.svg_fenceposts("d", "L = (N − 1)·d"),
            diagram_ar=D.svg_fenceposts("d", "الطول = (N − 1)·d"),
        ),
        "extra_traps": [
            (
                "Trap: Dividing road length \\( L \\) by spacing \\( d \\) and forgetting to **add 1** for the starting post (\\( N = L/d + 1 \\))!",
                "فخ شائع: قسمة طول الطريق \\( L \\) على المسافة \\( d \\) ونسيان **إضافة 1** لعمود البداية (\\( N = L/d + 1 \\))!",
            ),
            (
                "Trap: Subtracting speeds when two trains move **toward each other** — opposite-direction closing speed is the **sum** \\( v_1 + v_2 \\)!",
                "فخ شائع: طرح السرعتين عندما يتحرك قطاران **باتجاهين متعاكسين** — سرعة التقارب هي **مجموع السرعتين** \\( v_1 + v_2 \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Age Difference Invariant", "ثبات فرق العمر", r"\(A_1 - A_2 = \text{const}\)", "The age gap between two people never changes.", "فرق العمر بين شخصين ثابت لا يتغير أبداً."),
            cheat_item("Symmetric Pair Sums", "مجموع الأزواج المتناظرة", r"\(A + B + C = \frac{(A+B)+(B+C)+(C+A)}{2}\)", "Add all pairwise equations and divide by 2.", "اجمع المعادلات الزوجية واقسم على 2."),
            cheat_item("Fencepost Rule", "قانون الأشجار والأعمدة", r"\(N_{\text{posts}} = \frac{L}{d} + 1\)", "Posts on a straight segment = gaps + 1.", "عدد الأعمدة على خط مستقيم = الفجوات + 1."),
            cheat_item("Meet vs Chase Time", "زمن الالتقاء واللحاق", r"\(t_{\text{meet}} = \frac{D}{v_1+v_2}, \quad t_{\text{chase}} = \frac{G}{v_1-v_2}\)", "Add speeds when meeting; subtract when chasing.", "اجمع السرعتين عند التلاقي؛ واطرحهما عند المطاردة."),
        ],
        "extra_examples": [
            worked_math_example(
                "L14-E5",
                "Solved Example 5 — Fencepost Tree Spacing Along an Avenue",
                "مثال محلول ٥ — المسافات البينية بين الأشجار على طريق مستقيم",
                f"Palm trees are planted at equal intervals along a straight avenue, including one at each end. The distance from the **1st** tree to the **6th** tree is {m(60)} meters. What is the distance (in meters) from the **1st** tree to the **16th** tree?",
                f"زُرعت أشجار نخيل على مسافات متساوية على طول طريق مستقيم بما في ذلك شجرة عند كل طرف. إذا كانت المسافة من الشجرة **الأولى** إلى الشجرة **السادسة** تساوي {m(60)} متراً، فما المسافة (بالأمتار) من الشجرة **الأولى** إلى الشجرة **السادسة عشرة**؟",
                180, [150, 160, 168, 192],
                "Between tree 1 and tree 6 there are \\( 6 - 1 = 5 \\) gaps (not 6!), and between tree 1 and tree 16 there are \\( 16 - 1 = 15 \\) gaps!",
                [
                    f"The number of intervals between the 1st and 6th tree is {m('6 - 1 = 5')} gaps.",
                    f"Each gap has length {m('60 \\div 5 = 12')} meters.",
                    f"From the 1st to the 16th tree there are {m('16 - 1 = 15')} gaps, giving {m('15 \\times 12 = 180')} meters.",
                ],
                f"Ratio shortcut: {m('15')} gaps is {m('3 \\times 5')} gaps, so {m('3 \\times 60 = 180')} m!",
                "بين الشجرة الأولى والسادسة توجد \\( 6 - 1 = 5 \\) فجوات (وليس 6!)، وبين الأولى والسادسة عشرة توجد \\( 16 - 1 = 15 \\) فجوة!",
                [
                    f"عدد المسافات البينية من الشجرة 1 إلى 6 هو {m('6 - 1 = 5')} مسافات، فطول المسافة الواحدة {m('60 \\div 5 = 12')} متراً.",
                    f"من الشجرة 1 إلى 16 توجد {m('16 - 1 = 15')} مسافة، فتكون المسافة الكلية {m('15 \\times 12 = 180')} متراً.",
                ],
                f"باختصار التناسب: {m('15')} فجوة تساوي {m(3)} أضعاف {m(5)} فجوات، أي {m('3 \\times 60 = 180')} م.",
                diagram_en=D.svg_fenceposts("d = 12 m", "15 gaps = ?"),
                diagram_ar=D.svg_fenceposts("d = 12 م", "15 فجوة = ؟"),
            ),
            worked_math_example(
                "L14-E6",
                "Solved Example 6 — Two-Value Replacement (5-Riyal & 10-Riyal Notes)",
                "مثال محلول ٦ — فئات الأوراق النقدية بطريقة الافتراض",
                f"A wallet contains {m(24)} banknotes consisting only of {m(5)}-riyal notes and {m(10)}-riyal notes. If the total value of the notes is {m(185)} riyals, how many **{m(10)}-riyal notes** are in the wallet?",
                f"تحتوي محفظة على {m(24)} ورقة نقدية من فئتي {m(5)} ريالات و{m(10)} ريالات فقط. إذا كانت القيمة الكلية للأوراق {m(185)} ريالاً، فكم ورقة من فئة **{m(10)} ريالات** في المحفظة؟",
                13, [10, 11, 12, 14],
                "Assume all \\( 24 \\) notes are \\( 5 \\)-riyal notes (\\( 120 \\) riyals); every swap of a \\( 5 \\)-riyal note for a \\( 10 \\)-riyal note adds \\( 5 \\) riyals!",
                [
                    f"If all {m(24)} notes were {m(5)}-riyal notes, their total value would be {m('24 \\times 5 = 120')} riyals.",
                    f"The actual total is {m('185 - 120 = 65')} riyals higher.",
                    f"Replacing one {m(5)}-riyal note with a {m(10)}-riyal note adds {m('10 - 5 = 5')} riyals, so there are {m('65 \\div 5 = 13')} notes of {m(10)} riyals.",
                ],
                f"Check: {m('13 \\times 10 + 11 \\times 5 = 130 + 55 = 185')} riyals with {m('13 + 11 = 24')} notes.",
                "افترض أن جميع الأوراق الـ \\( 24 \\) من فئة \\( 5 \\) ريالات (بقيمة \\( 120 \\) ريالاً)، وكل استبدال بورقة فئة \\( 10 \\) ريالات يزيد المجموع بمقدار \\( 5 \\) ريالات!",
                [
                    f"لو كانت الأوراق الـ {m(24)} كلها من فئة {m(5)} ريالات لكانت قيمتها {m('24 \\times 5 = 120')} ريالاً.",
                    f"الفرق عن المبلغ الفعلي هو {m('185 - 120 = 65')} ريالاً.",
                    f"بما أن كل ورقة فئة {m(10)} ريالات تزيد {m('10 - 5 = 5')} ريالات، فإن عددها {m('65 \\div 5 = 13')} ورقة.",
                ],
                f"التحقق: {m('13 \\times 10 + 11 \\times 5 = 185')} ريالاً.",
                diagram_en=D.svg_pigeonhole_bins([("5 SAR", "24 − x"), ("10 SAR", "x = ?")], "Total = 185 SAR"),
                diagram_ar=D.svg_pigeonhole_bins([("5 ريالات", "24 − x"), ("10 ريالات", "x = ؟")], "المجموع = 185 ريالاً"),
            ),
        ],
    },

    "KMC-L1-05": {
        "extra_goals": [
            (
                "Calculate **clock-hand angles** using the \\( 5.5^\\circ/\\text{min} \\) relative rate, **paper-folding reflection angles**, and **exposed faces** of glued 3D cube stacks.",
                "حساب **الزاوية بين عقربي الساعة** بمعدل \\( 5.5^\\circ \\) لكل دقيقة، وزوايا **طي الورق بالانعكاس**، وعدد **الأوجه الظاهرة** لمجسمات المكعبات المتلاصقة.",
            ),
        ],
        "extra_concept": concept(
            "4. Paper-Folding Reflections, Clock-Hand Angles & Glued Cube Stacks",
            "٤. انعكاس طي الورق، زاوية عقربي الساعة، ومجسمات المكعبات",
            f"When a paper strip is folded along a crease, the folded angle equals the original angle by reflection ({m('\\angle_{\\text{folded}} = \\alpha')}), so a straight {m('180^\\circ')} edge loses **twice** the crease angle: {m('x = 180^\\circ - 2\\alpha')}. "
            f"On an analog clock at {m('H:M')}, the hour hand moves {m('0.5^\\circ/\\text{min}')} and the minute hand moves {m('6^\\circ/\\text{min}')}, giving angle {m('|30H - 5.5M|')}. "
            f"For a 3D stack of unit cubes resting on a table, count exposed faces by **projection** (top view + 2×front view + 2×side view if no concavities).",
            f"عند طي شريط ورقي حول خط طي بزاوية {m('\\alpha')}، تنعكس الزاوية بالتطابق، فتكون الزاوية المتبقية من الخط المستقيم {m('x = 180^\\circ - 2\\alpha')}. "
            f"وعلى الساعة ذات العقارب عند الوقت {m('H:M')}، يتحرك عقرب الساعات {m('0.5^\\circ')} لكل دقيقة وعقرب الدقائق {m('6^\\circ')}، فتكون الزاوية بينهما {m('|30H - 5.5M|')}. "
            f"ولحساب الأوجه الظاهرة لمجسم مكعبات موضوع على طاولة، اجمع المساقط (العلوي + 2×الأمامي + 2×الجانبي).",
            dm("x_{\\text{fold}} = 180^\\circ - 2\\alpha, \\qquad \\theta_{\\text{clock}} = |30H - 5.5M|"),
            f'<div class="eg-f-caption" dir="rtl">زاوية طي الورق وزاوية عقربي الساعة عند الوقت H:M:</div>{dm("x_{\\text{fold}} = 180^\\circ - 2\\alpha, \\qquad \\theta_{\\text{clock}} = |30H - 5.5M|")}',
            diagram_en=D.svg_analog_clock(4, 20, "|30H − 5.5M|"),
            diagram_ar=D.svg_analog_clock(4, 20, "|30H − 5.5M|"),
        ),
        "extra_traps": [
            (
                "Trap: Assuming the hour hand stands still at \\( 30H^\\circ \\) when minutes \\( M > 0 \\) — it advances by \\( 0.5^\\circ \\) every minute!",
                "فخ شائع: افتراض أن عقرب الساعات يبقى ثابتاً عند الرقم \\( H \\) أثناء تحرك عقرب الدقائق — عقرب الساعات يتحرك بمقدار \\( 0.5^\\circ \\) في كل دقيقة!",
            ),
            (
                "Trap: Counting the bottom faces resting on the table when a problem asks for the **painted** or **exposed** surface area of a cube stack!",
                "فخ شائع: احتساب الأوجه السفلية الملاصقة للطاولة عندما يطلب السؤال المساحة **المطلية** أو **المكشوفة** لمجسم المكعبات!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Inscribed Triangle in Rectangle", "مثلث داخل مستطيل", r"\(A_{\triangle} = \frac{1}{2} L W\)", "Any apex on the opposite side gives half the rectangle.", "أي رأس على الضلع المقابل يعطي نصف مساحة المستطيل."),
            cheat_item("Staircase Perimeter", "محيط الشكل المدرّج", r"\(P = 2(W + H)\)", "Push concave steps outward to form a bounding box.", "ادفع الدرجات للخارج لتكوين مستطيل محيط."),
            cheat_item("Paper-Fold Reflection", "زاوية طي الورق", r"\(x = 180^\circ - 2\alpha\)", "Folding doubles the subtracted crease angle.", "الطي يطابق الزاوية فتُطرح مرتين من 180°."),
            cheat_item("Clock-Hands Formula", "زاوية عقربي الساعة", r"\(\theta = |30H - 5.5M|\)", "Hour hand = 30°/hr + 0.5°/min; Minute = 6°/min.", "عقرب الساعات يتحرك 0.5°/د والدقائق 6°/د."),
        ],
        "extra_examples": [
            worked_math_example(
                "L15-E6",
                "Solved Example 6 — Exact Angle Between Clock Hands",
                "مثال محلول ٦ — الزاوية الدقيقة بين عقربي الساعة",
                f"What is the smaller angle (in degrees) between the hour hand and the minute hand of a standard analog clock at **{m('4:20')}**?",
                f"ما قياس الزاوية الصغرى (بالدرجات) بين عقرب الساعات وعقرب الدقائق في ساعة حائط عادية عند الساعة **{m('4:20')}** تماماً؟",
                10, [0, 5, 15, 20],
                "At 4:20 the minute hand points exactly at the 4 (\\( 120^\\circ \\)), while the hour hand has moved \\( \\frac{20}{60} = \\frac{1}{3} \\) of the way from 4 toward 5!",
                [
                    f"At {m('4:20')}, the minute hand is at {m('20 \\times 6^\\circ = 120^\\circ')} past {m(12)}.",
                    f"The hour hand is at {m('4 \\times 30^\\circ + 20 \\times 0.5^\\circ = 120^\\circ + 10^\\circ = 130^\\circ')}.",
                    f"The angle between them is {m('|130^\\circ - 120^\\circ| = 10^\\circ')}.",
                ],
                f"Direct formula check: {m('|30(4) - 5.5(20)| = |120 - 110| = 10^\\circ')}.",
                "عند الساعة 4:20 يشير عقرب الدقائق إلى الرقم 4 تماماً (\\( 120^\\circ \\))، بينما تحرّك عقرب الساعات بمقدار \\( 20 \\times 0.5^\\circ = 10^\\circ \\) بعد الرقم 4!",
                [
                    f"زاوية عقرب الدقائق من الرقم 12 هي {m('20 \\times 6^\\circ = 120^\\circ')}.",
                    f"وزاوية عقرب الساعات هي {m('4 \\times 30^\\circ + 20 \\times 0.5^\\circ = 130^\\circ')}.",
                    f"الفرق بينهما = {m('130^\\circ - 120^\\circ = 10^\\circ')}.",
                ],
                f"بالقانون المباشر: {m('|30(4) - 5.5(20)| = 10^\\circ')}.",
                suffix="°",
                diagram_en=D.svg_analog_clock(4, 20, "θ = ?"),
                diagram_ar=D.svg_analog_clock(4, 20, "الزاوية = ؟"),
            ),
        ],
    },

    "KMC-L1-06": {
        "extra_goals": [
            (
                "Use the **3×3 magic-square center rule** (\\( S = 3c \\)), count **shortest street-grid paths** via Pascal's triangle, and relate **pie-chart central angles** to totals.",
                "استخدام **قاعدة المركز في المربع السحري 3×3** (\\( S = 3c \\))، وعدّ **أقصر المسارات الشبكية**، والربط بين **الزوايا المركزية في القطاعات الدائرية** والمجموع الكلي.",
            ),
        ],
        "extra_concept": concept(
            "4. 3×3 Magic Squares (S = 3c), Street-Grid Paths & Pie-Chart Sectors",
            "٤. المربعات السحرية (S = 3c)، مسارات الشبكة، والقطاعات الدائرية",
            f"In every {m('3 \\times 3')} magic square, the magic sum {m('S')} of any row, column, or main diagonal equals **three times the center cell** ({m('S = 3c')}). "
            f"On an {m('m \\times n')} street grid moving only Right and Up, the number of shortest paths is {m('\\binom{m+n}{m}')}. "
            f"In a pie chart, a sector of central angle {m('\\theta^\\circ')} represents the fraction {m('\\frac{\\theta}{360}')} of the total data set.",
            f"في أي مربع سحري {m('3 \\times 3')}، يساوي المجموع السحري {m('S')} لأي صف أو عمود أو قطر رئيسي **ثلاثة أضعاف الخلية الوسطى** ({m('S = 3c')}). "
            f"وفي شبكة طرق أبعادها {m('m \\times n')} بالتحرك يميناً وأعلى فقط، عدد أقصر المسارات هو {m('\\binom{m+n}{m}')}. "
            f"وفي التمثيل بالقطاعات الدائرية، القطاع ذو الزاوية المركزية {m('\\theta^\\circ')} يمثّل الكسر {m('\\frac{\\theta}{360}')} من المجموع الكلي.",
            dm("S_{\\text{magic}} = 3c, \\qquad N_{\\text{paths}}(m, n) = \\binom{m + n}{m}, \\qquad \\text{Sector Value} = \\frac{\\theta^\\circ}{360^\\circ} \\times N_{\\text{total}}"),
            f'<div class="eg-f-caption" dir="rtl">قانون مركز المربع السحري ومسارات الشبكة والقطاع الدائري:</div>{dm("S = 3c, \\qquad N_{\\text{paths}} = \\binom{m + n}{m}, \\qquad V = \\frac{\\theta}{360} N")}',
            diagram_en=D.svg_magic_square_3x3([["8", "1", "6"], ["3", "c = 5", "7"], ["4", "9", "2"]]),
            diagram_ar=D.svg_magic_square_3x3([["8", "1", "6"], ["3", "c = 5", "7"], ["4", "9", "2"]]),
        ),
        "extra_traps": [
            (
                "Trap: Counting grid **street intersections** instead of **city blocks (steps)** when computing shortest paths \\( \\binom{m+n}{m} \\)!",
                "فخ شائع: عدّ **نقاط التقاطع** بدلاً من **خطوات المربعات** عند حساب عدد المسارات الشبكية \\( \\binom{m+n}{m} \\)!",
            ),
            (
                "Trap: Confusing a pie-chart sector's **angle in degrees** (out of \\( 360^\\circ \\)) with its **percentage** (out of \\( 100\\% \\))!",
                "فخ شائع: الخلط بين **زاوية القطاع بالدرجات** (من أصل \\( 360^\\circ \\)) و**نسبته المئوية** (من أصل \\( 100\\% \\))!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Handshakes & Pairs", "المصافحات والأزواج", r"\(\binom{n}{2} = \frac{n(n - 1)}{2}\)", "Divide n(n−1) by 2 so pairs aren't double-counted.", "اقسم n(n−1) على 2 لعدم تكرار الزوج."),
            cheat_item("3×3 Magic Square Center", "مركز المربع السحري", r"\(S = 3c\)", "Row/column/diagonal sum = 3 × center cell.", "المجموع السحري = 3 × خلية المركز."),
            cheat_item("Monotone Grid Paths", "مسارات الشبكة", r"\(\binom{m + n}{m}\)", "Choose which m of the (m+n) steps go Right.", "اختر m خطوة أفقية من أصل (m+n) خطوة."),
            cheat_item("Weighted Group Mean", "المتوسط المرجّح", r"\(\bar{x} = \frac{N_1\bar{x}_1 + N_2\bar{x}_2}{N_1 + N_2}\)", "Always sum total points before dividing.", "اجمع المجاميع الكلية أولاً قبل القسمة."),
        ],
        "extra_examples": [
            worked_math_example(
                "L16-E5",
                "Solved Example 5 — 3×3 Magic Square Center & Missing Corner",
                "مثال محلول ٥ — مركز المربع السحري 3×3 والركن المفقود",
                f"In a {m('3 \\times 3')} magic square, the sum of the three numbers in every row, column, and main diagonal is the same. If the center square contains {m(14)} and two numbers in the top row are {m(9)} and {m(16)}, what is the third number in the top row?",
                f"في مربع سحري {m('3 \\times 3')}، يتساوى مجموع الأعداد الثلاثة في كل صف وكل عمود وكل قطر رئيسي. إذا كان العدد في الخلية الوسطى {m(14)}، وكان عددان في الصف العلوي هما {m(9)} و{m(16)}، فما العدد الثالث في الصف العلوي؟",
                17, [13, 15, 18, 19],
                "By the 3×3 magic-square theorem, the magic sum of every row is \\( S = 3 \\times \\text{center} = 3 \\times 14 = 42 \\)!",
                [
                    f"In any {m('3 \\times 3')} magic square, the magic sum equals {m('3 \\times c = 3 \\times 14 = 42')}.",
                    f"The three numbers in the top row must also sum to {m(42)}.",
                    f"Thus the missing top-row number is {m('42 - (9 + 16) = 42 - 25 = 17')}.",
                ],
                f"Check: {m('9 + 16 + 17 = 42 = 3 \\times 14')}.",
                "في أي مربع سحري 3×3 يساوي المجموع السحري لكل صف ثلاثة أضعاف الخلية الوسطى: \\( S = 3 \\times 14 = 42 \\)!",
                [
                    f"المجموع السحري للمربع هو {m('S = 3 \\times 14 = 42')}.",
                    f"العدد الثالث في الصف العلوي = {m('42 - (9 + 16) = 17')}.",
                ],
                f"التحقق: {m('9 + 16 + 17 = 42 = 3 \\times 14')}.",
                diagram_en=D.svg_magic_square_3x3([["9", "16", "?"], ["·", "14", "·"], ["·", "·", "·"]]),
                diagram_ar=D.svg_magic_square_3x3([["9", "16", "؟"], ["·", "14", "·"], ["·", "·", "·"]]),
            ),
            worked_math_example(
                "L16-E6",
                "Solved Example 6 — Pie Chart Sector Angle to Student Count",
                "مثال محلول ٦ — تحويل زاوية القطاع الدائري إلى عدد الطلاب",
                f"A school surveyed {m(180)} students about their favorite competition subject and displayed the results in a pie chart. If the **Mathematics** sector has a central angle of {m('108^\\circ')} and the **Physics** sector has {m('72^\\circ')}, how many **more** students chose Mathematics than Physics?",
                f"أجرت مدرسة استبياناً شمل {m(180)} طالباً حول مادة المسابقات المفضلة لديهم ومثّلت النتائج بقطاعات دائرية. إذا كانت الزاوية المركزية لقطاع **الرياضيات** {m('108^\\circ')} ولقطاع **الفيزياء** {m('72^\\circ')}، فبكم يزيد عدد الطلاب الذين اختاروا الرياضيات على الذين اختاروا الفيزياء؟",
                18, [12, 15, 24, 36],
                "Take the angle difference \\( 108^\\circ - 72^\\circ = 36^\\circ \\) directly as a fraction of \\( 360^\\circ \\)!",
                [
                    f"The difference in central angles between Mathematics and Physics is {m('108^\\circ - 72^\\circ = 36^\\circ')}.",
                    f"Since {m('36^\\circ')} is exactly {m('\\frac{36}{360} = \\frac{1}{10}')} of the full circle, the difference in students is {m('\\frac{1}{10} \\times 180 = 18')}.",
                ],
                f"Check: Math = {m('\\frac{108}{360}\\times 180 = 54')}, Physics = {m('\\frac{72}{360}\\times 180 = 36')}, and {m('54 - 36 = 18')}.",
                "احسب فرق الزاويتين المركزيتين \\( 108^\\circ - 72^\\circ = 36^\\circ \\) مباشرةً كنسبة من \\( 360^\\circ \\)!",
                [
                    f"الفرق بين زاويتي القطاعين هو {m('108^\\circ - 72^\\circ = 36^\\circ')}.",
                    f"بما أن {m('\\frac{36^\\circ}{360^\\circ} = \\frac{1}{10}')} من الدائرة، فإن الفرق في عدد الطلاب = {m('\\frac{1}{10} \\times 180 = 18')} طالباً.",
                ],
                f"التحقق: الرياضيات {m(54)} طالباً والفيزياء {m(36)} طالباً، والفرق {m('54 - 36 = 18')}.",
                diagram_en=D.svg_pie_chart([(0.30, "Math 108°"), (0.20, "Phys 72°"), (0.50, "Other")]),
                diagram_ar=D.svg_pie_chart([(0.30, "رياضيات 108°"), (0.20, "فيزياء 72°"), (0.50, "أخرى")]),
            ),
        ],
    },

    # =========================================================================
    # TRACK 2: GRADES 8–9 (KMC-L2-01 .. KMC-L2-06)
    # =========================================================================
    "KMC-L2-01": {
        "extra_goals": [
            (
                "Find minimal multipliers to create **perfect squares or cubes**, apply **3-set Venn inclusion–exclusion**, and solve **simultaneous remainder** problems via common offsets.",
                "إيجاد أصغر مضاعف لتكوين **مربع كامل أو مكعب كامل**، وتطبيق **مخطط فن لثلاث مجموعات**، وحل مسائل **البواقي المشتركة** بإزاحة المضاعف المشترك الأصغر.",
            ),
        ],
        "extra_concept": concept(
            "4. Perfect-Power Multipliers, 3-Set Venn Diagrams & Simultaneous Remainders",
            "٤. مضاعفات القوى الكاملة، مخططات فن الثلاثية، والبواقي المتزامنة",
            f"Given prime factorization {m('N = \\prod p_i^{e_i}')}, the smallest positive integer {m('k')} making {m('Nk')} a **perfect square** (or **perfect cube**) raises each exponent {m('e_i')} to the next multiple of {m(2)} (or {m(3)}). "
            f"If {m('N')} leaves remainder {m('r')} when divided by {m('a, b, c')}, then {m('N - r')} is a multiple of {m('\\operatorname{lcm}(a,b,c)')}; if it leaves remainders {m('a-d, b-d, c-d')} (constant deficit {m('d')}), then {m('N + d')} is a multiple of {m('\\operatorname{lcm}(a,b,c)')}!",
            f"إذا كان التحليل الأولي {m('N = \\prod p_i^{e_i}')}، فإن أصغر عدد موجب {m('k')} يجعل {m('Nk')} **مربعاً كاملاً** (أو **مكعباً كاملاً**) يكمّل كل أس {m('e_i')} إلى أقرب مضاعف للعدد {m(2)} (أو {m(3)}). "
            f"وإذا ترك العدد {m('N')} الباقي نفسه {m('r')} عند قسمته على {m('a, b, c')} فإن {m('N - r')} مضاعف لـ {m('\\operatorname{lcm}(a,b,c)')}؛ أما إذا كان النقص ثابتاً {m('d')} عن كل مقسوم عليه فإن {m('N + d')} مضاعف لـ {m('\\operatorname{lcm}(a,b,c)')}!",
            dm("N \\equiv -d \\pmod{a,b,c} \\implies N = k\\cdot\\operatorname{lcm}(a, b, c) - d"),
            f'<div class="eg-f-caption" dir="rtl">قاعدة النقص الثابت في البواقي المتزامنة:</div>{dm("N \\equiv -d \\pmod{a,b,c} \\implies N = k\\cdot\\operatorname{lcm}(a, b, c) - d")}',
            diagram_en=D.svg_venn_3("A", "B", "C", {"a": "A", "b": "B", "c": "C", "ab": "∩", "bc": "∩", "ac": "∩", "abc": "A∩B∩C"}),
            diagram_ar=D.svg_venn_3("A", "B", "C", {"a": "A", "b": "B", "c": "C", "ab": "∩", "bc": "∩", "ac": "∩", "abc": "A∩B∩C"}),
        ),
        "extra_traps": [
            (
                "Trap: Forgetting the inequality \\( d > r \\) when \\( A \\) divided by \\( d \\) leaves remainder \\( r \\) — divisors of \\( A - r \\) that are \\( \\le r \\) are invalid!",
                "فخ شائع: نسيان الشرط الأساسي \\( d > r \\) عندما يترك \\( A \\) الباقي \\( r \\) عند قسمته على \\( d \\) — يجب استبعاد جميع قواسم \\( A - r \\) التي لا تزيد على \\( r \\)!",
            ),
            (
                "Trap: Subtracting pairwise overlaps in a 3-set Venn diagram without **adding back** the triple intersection \\( |A \\cap B \\cap C| \\)!",
                "فخ شائع: طرح التقاطعات الثنائية في مخطط فن لثلاث مجموعات دون **إعادة جمع** التقاطع الثلاثي \\( |A \\cap B \\cap C| \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Divisor Count Formula", "عدد القواسم الموجبة", r"\(\tau(N) = (e_1 + 1)(e_2 + 1)\cdots\)", "Add 1 to each prime exponent and multiply.", "أضف 1 لكل أس أولي ثم اضرب."),
            cheat_item("Remainder Division Rule", "شرط الباقي والمقسوم عليه", r"\(A = qd + r \iff d \mid (A - r),\; d > r\)", "The divisor d must strictly exceed r.", "المقسوم عليه d يجب أن يكون أكبر تماماً من الباقي r."),
            cheat_item("Constant-Deficit LCM", "البواقي ذات النقص الثابت", r"\(N = k\cdot\operatorname{lcm}(a,b,c) - d\)", "Add the common deficit d to reach a multiple.", "أضف النقص الثابت d للوصول إلى المضاعف المشترك."),
            cheat_item("3-Set Inclusion–Exclusion", "التضمين والإقصاء الثلاثي", r"\(|A\cup B\cup C| = \sum|A| - \sum|A\cap B| + |A\cap B\cap C|\)", "Add singles, subtract pairs, add back triple.", "اجمع المفردات، اطرح الثنائيات، وأعد جمع الثلاثي."),
        ],
        "extra_examples": [
            worked_math_example(
                "L21-E5",
                "Solved Example 5 — Smallest Multiplier for a Perfect Cube",
                "مثال محلول ٥ — أصغر مضاعف لتكوين مكعب كامل",
                f"What is the smallest positive integer {m('k')} such that the product {m('360 \\times k')} is a **perfect cube**?",
                f"ما أصغر عدد صحيح موجب {m('k')} يجعل حاصل الضرب {m('360 \\times k')} **مكعباً كاملاً**؟",
                75, [15, 25, 45, 90],
                "Factor \\( 360 = 2^3 \\times 3^2 \\times 5^1 \\) and raise every prime exponent to the nearest multiple of \\( 3 \\)!",
                [
                    f"Prime factorize {m('360 = 8 \\times 9 \\times 5 = 2^3 \\times 3^2 \\times 5^1')}.",
                    f"For a perfect cube, each prime exponent must be a multiple of {m(3)}.",
                    f"The exponent of {m(2)} is already {m(3)}; we need {m('3^{3-2} = 3^1')} and {m('5^{3-1} = 5^2')}, so {m('k = 3 \\times 25 = 75')}.",
                ],
                f"Check: {m('360 \\times 75 = 27000 = 30^3')}.",
                "حلّل \\( 360 = 2^3 \\times 3^2 \\times 5^1 \\) وكمّل كل أس أولي ليصبح من مضاعفات \\( 3 \\)!",
                [
                    f"التحليل الأولي: {m('360 = 2^3 \\times 3^2 \\times 5^1')}.",
                    f"لتكوين مكعب كامل نحتاج إلى {m('3^1')} و{m('5^2')}، فيكون أصغر مضاعف {m('k = 3 \\times 25 = 75')}.",
                ],
                f"التحقق: {m('360 \\times 75 = 27000 = 30^3')}.",
                diagram_en=D.svg_factor_tree("360·k = □³", "2³", "3²·5¹", "×3¹", "×5² = 75"),
                diagram_ar=D.svg_factor_tree("360·k = □³", "2³", "3²·5¹", "×3¹", "×5² = 75"),
            ),
            worked_math_example(
                "L21-E6",
                "Solved Example 6 — Simultaneous Remainders with Constant Deficit",
                "مثال محلول ٦ — البواقي المتزامنة ذات النقص الثابت",
                f"Find the smallest positive integer {m('N > 10')} that leaves a remainder of {m(3)} when divided by {m(4)}, a remainder of {m(5)} when divided by {m(6)}, and a remainder of {m(8)} when divided by {m(9)}.",
                f"ما أصغر عدد صحيح موجب {m('N > 10')} يترك الباقي {m(3)} عند قسمته على {m(4)}، والباقي {m(5)} عند قسمته على {m(6)}، والباقي {m(8)} عند قسمته على {m(9)}؟",
                35, [23, 31, 37, 71],
                "Notice that every remainder is exactly \\( 1 \\) less than its divisor (\\( 4-3 = 6-5 = 9-8 = 1 \\)), so \\( N + 1 \\) is a common multiple of \\( 4, 6, 9 \\)!",
                [
                    f"Since {m('N \\equiv -1')} modulo {m(4)}, {m(6)}, and {m(9)}, the integer {m('N + 1')} is divisible by {m('\\operatorname{lcm}(4, 6, 9)')}.",
                    f"Compute {m('\\operatorname{lcm}(4, 6, 9) = 36')}.",
                    f"Thus the smallest positive solution is {m('N = 36 - 1 = 35')}.",
                ],
                f"Check {m(35)}: {m('35 = 4(8)+3 = 6(5)+5 = 9(3)+8')}. All three remainders match!",
                "لاحظ أن كل باقٍ يقل بمقدار \\( 1 \\) عن المقسوم عليه، مما يعني أن \\( N + 1 \\) مضاعف مشترك للأعداد \\( 4, 6, 9 \\)!",
                [
                    f"بما أن النقص ثابت ويساوي {m(1)}، فإن {m('N + 1')} يقبل القسمة على {m('\\operatorname{lcm}(4, 6, 9) = 36')}.",
                    f"إذن أصغر قيمة هي {m('N = 36 - 1 = 35')}.",
                ],
                f"التحقق: {m('35 = 4(8)+3 = 6(5)+5 = 9(3)+8')}.",
                diagram_en=D.svg_algebra_flow([("N ≡ −1", "mod 4, 6, 9"), ("LCM", "lcm(4,6,9) = 36"), ("Target", "N = 36 − 1 = ?")], ["+1", "−1"]),
                diagram_ar=D.svg_algebra_flow([("N ≡ −1", "للمقسومات 4، 6، 9"), ("م.م.أ", "lcm(4,6,9) = 36"), ("المطلوب", "N = 36 − 1 = ؟")], ["+1", "−1"]),
            ),
        ],
    },

    "KMC-L2-02": {
        "extra_goals": [
            (
                "Track **binary switch toggle parity**, apply the **alternating digit-sum test for 11** on palindromes, and use the **digital root (mod 9) invariant**.",
                "تتبّع **زوجية ضغطات المفاتيح الثنائية**، وتطبيق **قاعدة المجموع المتناوب للقسمة على 11** في الأعداد المتناظرة، واستخدام **ثابت الجذر الرقمي (باقي القسمة على 9)**.",
            ),
        ],
        "extra_concept": concept(
            "4. Binary Switch Parity, Divisibility by 11 & Digital Root (mod 9) Invariants",
            "٤. زوجية المفاتيح الثنائية، قابلية القسمة على 11، وثابت बाقي 9",
            f"A bulb starting OFF ends ON if and only if it is toggled an **odd** number of times. "
            f"A number is divisible by {m(11)} iff the alternating sum of its digits {m('(d_0 - d_1 + d_2 - \\cdots)')} is a multiple of {m(11)} (so every **even-length palindrome** {m('\\overline{abccba}')} is automatically divisible by {m(11)}!). "
            f"Because {m('10^k \\equiv 1 \\pmod{9}')}, any rearrangement or digit-sum replacement preserves {m('N \\bmod 9')}.",
            f"المصباح الذي يبدأ مطفأً ينتهي مضاءً إذا وفقط إذا تم تغيير حالته عدداً **فردياً** من المرات. "
            f"ويقبل العدد القسمة على {m(11)} إذا وفقط إذا كان المجموع المتناوب لأرقامه مضاعفاً للعدد {m(11)} (لذلك فإن كل **عدد متناظر ذي عدد زوجي من الخانات** مثل {m('\\overline{abba}')} يقبل القسمة على {m(11)} دائماً!). "
            f"وبما أن {m('10^k \\equiv 1 \\pmod{9}')} فإن جمع الأرقام المتكرر يحفظ باقي القسمة على {m(9)} دائماً.",
            dm("11 \\mid N \\iff 11 \\mid \\sum (-1)^k d_k, \\qquad S_{\\text{digits}}(N) \\equiv N \\pmod{9}"),
            f'<div class="eg-f-caption" dir="rtl">قابلية القسمة على 11 وثابت باقي القسمة على 9:</div>{dm("11 \\mid N \\iff 11 \\mid \\sum (-1)^k d_k, \\qquad S(N) \\equiv N \\pmod{9}")}',
            diagram_en=D.svg_digit_cards(["a", "b", "b", "a"], "a − b + b − a = 0", "Always ÷ 11"),
            diagram_ar=D.svg_digit_cards(["a", "b", "b", "a"], "a − b + b − a = 0", "يقبل القسمة على 11 دائماً"),
        ),
        "extra_traps": [
            (
                "Trap: Counting factor \\( 2 \\)s instead of factor \\( 5 \\)s when finding trailing zeros of a factorial or product (and forgetting that \\( 25 = 5^2 \\) contributes **two** \\( 5 \\)s)!",
                "فخ شائع: إغفال أن العدد \\( 25 = 5^2 \\) (ومضاعفاته كـ \\( 50, 75 \\)) يمنح **عاملَين** من \\( 5 \\) عند حساب الأصفار الطرفية!",
            ),
            (
                "Trap: Thinking \\( 4^k \\) has a units-digit cycle of length \\( 4 \\) instead of \\( 2 \\) (\\( 4, 6, 4, 6, \\dots \\)), or forgetting that remainder \\( 0 \\pmod{4} \\) corresponds to the **4th** term in the cycle!",
                "فخ شائع: عند قسمة الأس على \\( 4 \\) والحصول على الباقي \\( 0 \\)، يجب أخذ **العنصر الرابع** في دورة الآحاد وليس الأول!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Units-Digit Period", "دورة رقم الآحاد", r"\(r = n \bmod 4\;\;(r=0 \Rightarrow 4)\)", "Bases 2, 3, 7, 8 repeat every 4 powers.", "الأعداد 2، 3، 7، 8 تتكرر آحادها كل 4 قوى."),
            cheat_item("Trailing Zeros", "الأصفار الطرفية", r"\(Z = \min(v_2(N),\, v_5(N))\)", "Each 10 = 2 × 5; count powers of 5 carefully.", "كل صفر طرفي ينتج عن زوج (2 × 5)."),
            cheat_item("10ⁿ − k Digit Sum", "مجموع أرقام 10ⁿ − k", r"\(\underbrace{99\dots9}_{n-2}\,(d_1)(d_0)\)", "First (n−2) digits are 9s.", "أول (n−2) خانة تتحول كلها إلى تسعات."),
            cheat_item("Divisibility by 9 & 11", "القسمة على 9 و11", r"\(9 \mid \sum d_k, \quad 11 \mid \sum (-1)^k d_k\)", "Sum digits for 9; alternate + and − for 11.", "مجموع الأرقام لـ 9؛ والمجموع المتناوب لـ 11."),
        ],
        "extra_examples": [
            worked_math_example(
                "L22-E5",
                "Solved Example 5 — Five-Digit Palindrome Divisible by 11",
                "مثال محلول ٥ — عدد متناظر من 5 خانات يقبل القسمة على 11",
                f"The five-digit palindrome {m('\\overline{4B7B4}')} is divisible by {m(11)}. What is the value of the digit {m('B')}?",
                f"العدد المتناظر المكون من خمسة أرقام {m('\\overline{4B7B4}')} يقبل القسمة على {m(11)}. ما قيمة الرقم {m('B')}؟",
                2, [1, 3, 5, 7],
                "Compute the alternating digit sum \\( 4 - B + 7 - B + 4 = 15 - 2B \\) and set it equal to a multiple of \\( 11 \\)!",
                [
                    f"By the divisibility rule for {m(11)}, the alternating sum of digits is {m('4 - B + 7 - B + 4 = 15 - 2B')}.",
                    f"Since {m('0 \\le B \\le 9')}, {m('15 - 2B')} lies between {m('-3')} and {m(15)}.",
                    f"The only multiple of {m(11)} in this range with matching parity is {m(11)}: {m('15 - 2B = 11 \\implies 2B = 4 \\implies B = 2')}.",
                ],
                f"Check {m(42724)}: {m('42724 \\div 11 = 3884')}. Exact!",
                "احسب المجموع المتناوب للأرقام \\( 4 - B + 7 - B + 4 = 15 - 2B \\) واجعله من مضاعفات \\( 11 \\)!",
                [
                    f"المجموع المتناوب لأرقام العدد هو {m('4 - B + 7 - B + 4 = 15 - 2B')}.",
                    f"لكي يقبل القسمة على {m(11)} نضع {m('15 - 2B = 11 \\implies 2B = 4 \\implies B = 2')}.",
                ],
                f"التحقق: {m('42724 \\div 11 = 3884')}.",
                diagram_en=D.svg_digit_cards(["4", "B", "7", "B", "4"], "15 − 2B = 11", "B = ?"),
                diagram_ar=D.svg_digit_cards(["4", "B", "7", "B", "4"], "15 − 2B = 11", "B = ؟"),
            ),
            worked_math_example(
                "L22-E6",
                "Solved Example 6 — Digital Root Invariant After Repeated Digit Summing",
                "مثال محلول ٦ — الجذر الرقمي وثابت باقي القسمة على 9",
                f"We start with the number {m('N = 2025^{2025}')} and repeatedly replace the number on the board with the **sum of its base-10 digits** until only a single digit remains. What is that final single digit?",
                f"بدأنا بالعدد {m('N = 2025^{2025}')}، وفي كل خطوة نستبدل بالعدد المكتوب **مجموع أرقامه** في النظام العشري، ونكرر ذلك حتى يتبقى رقم واحد فقط. ما هذا الرقم النهائي؟",
                9, [0, 1, 5, 7],
                "Summing digits preserves the remainder modulo \\( 9 \\), and any positive multiple of \\( 9 \\) reduces to final single digit \\( 9 \\)!",
                [
                    f"Notice that the digit sum of {m(2025)} is {m('2 + 0 + 2 + 5 = 9')}, so {m('2025')} is a multiple of {m(9)}.",
                    f"Therefore {m('N = 2025^{2025}')} is a positive multiple of {m(9)}.",
                    f"Every digit-sum step preserves divisibility by {m(9)} and stays positive, so the final single digit must be {m(9)}.",
                ],
                f"Any positive multiple of {m(9)} has digital root {m(9)} (never {m(0)} since {m('N > 0')}).",
                "عملية جمع الأرقام تحفظ باقي القسمة على \\( 9 \\)، وأي مضاعف موجب للعدد \\( 9 \\) ينتهي حتماً بالرقم المفرد \\( 9 \\)!",
                [
                    f"مجموع أرقام الأساس {m(2025)} هو {m('2 + 0 + 2 + 5 = 9')}، فهو يقبل القسمة على {m(9)}.",
                    f"لذلك فإن {m('2025^{2025}')} مضاعف موجب للعدد {m(9)}، وعند تكرار جمع الأرقام يستقر على الرقم {m(9)}.",
                ],
                f"التحقق: الجذر الرقمي لأي مضاعف موجب للعدد {m(9)} هو {m(9)}.",
                diagram_en=D.svg_function_machine("2025²⁰²⁵", "∑ digits", "mod 9 = 0", "Digit = ?"),
                diagram_ar=D.svg_function_machine("2025²⁰²⁵", "مجموع الأرقام", "مضاعف لـ 9", "الرقم = ؟"),
            ),
        ],
    },

    "KMC-L2-03": {
        "extra_goals": [
            (
                "Collapse **telescoping fraction products** by factoring \\( 1 - \\frac{1}{k^2} = \\frac{k-1}{k}\\cdot\\frac{k+1}{k} \\) and solve **linear floor equations** by bounding.",
                "تبسيط **الجداءات الكسرية التلسكوبية** بتحليل \\( 1 - \\frac{1}{k^2} = \\frac{k-1}{k}\\cdot\\frac{k+1}{k} \\)، وحل **معادلات دالة الصحيح الخطية** بالحصر.",
            ),
        ],
        "extra_concept": concept(
            "4. Telescoping Fraction Products & Linear Floor Equations",
            "٤. الجداءات الكسرية التلسكوبية ومعادلات دالة الصحيح",
            f"In long products such as {m('\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k}\\right)')} or {m('\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k^2}\\right)')}, rewrite each factor over a common denominator so adjacent numerators and denominators cancel! "
            f"For an equation mixing {m('x')} and {m('\\lfloor x \\rfloor')}, set {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} and use {m('n \\le x < n + 1')} to pin down the integer {m('n')} first.",
            f"في الجداءات الطويلة مثل {m('\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k}\\right)')} أو {m('\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k^2}\\right)')}، وحّد المقام داخل كل قوس وحلّل البسط لتختصر العوامل المتجاورة تلسكوبياً! "
            f"ولحل معادلة تجمع بين {m('x')} و{m('\\lfloor x \\rfloor')}، افرض {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} واستخدم المتباينة {m('n \\le x < n + 1')} لتحديد {m('n')} أولاً.",
            dm("\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k^2}\\right) = \\prod_{k=2}^{n}\\frac{(k-1)(k+1)}{k^2} = \\frac{n + 1}{2n}"),
            f'<div class="eg-f-caption" dir="rtl">الجداء التلسكوبي لفرق المربعين الكسري:</div>{dm("\\prod_{k=2}^{n}\\left(1 - \\frac{1}{k^2}\\right) = \\frac{n + 1}{2n}")}',
            diagram_en=D.svg_telescoping_chain(["1/2 · 3/2", "2/3 · 4/3", "···", "(n−1)/n · (n+1)/n"], "×", "Telescoping Product"),
            diagram_ar=D.svg_telescoping_chain(["1/2 · 3/2", "2/3 · 4/3", "···", "(n−1)/n · (n+1)/n"], "×", "جداء تلسكوبي"),
        ),
        "extra_traps": [
            (
                "Trap: Writing \\( \\left(x + \\frac{1}{x}\\right)^2 = x^2 + \\frac{1}{x^2} \\) and forgetting the middle term \\( +2 \\)!",
                "فخ شائع: كتابة \\( \\left(x + \\frac{1}{x}\\right)^2 = x^2 + \\frac{1}{x^2} \\) ونسيان الحد الأوسط الثابت \\( +2 \\)!",
            ),
            (
                "Trap: Rounding a negative number toward zero when computing \\( \\lfloor x \\rfloor \\) — remember \\( \\lfloor -2.3 \\rfloor = -3 \\), not \\( -2 \\)!",
                "فخ شائع: تقريب العدد السالب نحو الصفر في دالة الصحيح — تذكّر أن \\( \\lfloor -2.3 \\rfloor = -3 \\) وليس \\( -2 \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Reciprocal Square", "مربع المقلوب", r"\(x^2 + \frac{1}{x^2} = \left(x + \frac{1}{x}\right)^2 - 2\)", "Subtract 2 from the squared sum.", "اطرح 2 من مربع المجموع."),
            cheat_item("Simon's Favorite Trick", "إتمام المستطيل الجبري", r"\(xy + ax + by + ab = (x + b)(y + a)\)", "Add ab to both sides to factor.", "أضف ab للطرفين لتحليل المقدار."),
            cheat_item("Telescoping Product", "الجداء التلسكوبي", r"\(\prod_{k=2}^{n}\left(1 - \frac{1}{k^2}\right) = \frac{n + 1}{2n}\)", "Factor 1 − 1/k² = (k−1)(k+1)/k².", "حلّل 1 − 1/k² لتختصر الحدود الوسطى."),
            cheat_item("Floor Bounding", "حصر دالة الصحيح", r"\(n = \lfloor x \rfloor \iff n \le x < n + 1\)", "Replace ⌊x⌋ by an integer n first.", "استبدل ⌊x⌋ بعدد صحيح n أولاً."),
        ],
        "extra_examples": [
            worked_math_example(
                "L23-E5",
                "Solved Example 5 — Telescoping Product of (1 − 1/k²)",
                "مثال محلول ٥ — الجداء التلسكوبي للمقدار (1 − 1/k²)",
                f"What is the exact value of the product {m('P = 20 \\times \\left(1 - \\frac{1}{2^2}\\right)\\left(1 - \\frac{1}{3^2}\\right)\\left(1 - \\frac{1}{4^2}\\right)\\cdots\\left(1 - \\frac{1}{10^2}\\right)')}?",
                f"ما القيمة الدقيقة لحاصل الضرب {m('P = 20 \\times \\left(1 - \\frac{1}{2^2}\\right)\\left(1 - \\frac{1}{3^2}\\right)\\left(1 - \\frac{1}{4^2}\\right)\\cdots\\left(1 - \\frac{1}{10^2}\\right)')}؟",
                11, [9, 10, 12, 15],
                "Factor each bracket as \\( \\frac{k-1}{k}\\cdot\\frac{k+1}{k} \\) so all interior terms cancel!",
                [
                    f"Rewrite {m('1 - \\frac{1}{k^2} = \\frac{k-1}{k}\\cdot\\frac{k+1}{k}')} for {m('k = 2, 3, \\dots, 10')}.",
                    f"The product of the first fractions is {m('\\frac{1}{2}\\cdot\\frac{2}{3}\\cdots\\frac{9}{10} = \\frac{1}{10}')}, and the product of the second fractions is {m('\\frac{3}{2}\\cdot\\frac{4}{3}\\cdots\\frac{11}{10} = \\frac{11}{2}')}.",
                    f"Multiply by {m(20)}: {m('P = 20 \\times \\frac{1}{10} \\times \\frac{11}{2} = 11')}.",
                ],
                f"Formula check for {m('n = 10')}: {m('20 \\times \\frac{10 + 1}{2 \\times 10} = 11')}.",
                "حلّل كل قوس إلى \\( \\frac{k-1}{k}\\cdot\\frac{k+1}{k} \\) لتختصر جميع الحدود الوسطى!",
                [
                    f"نكتب كل عامل بالصورة {m('\\frac{k-1}{k}\\cdot\\frac{k+1}{k}')} من {m('k = 2')} إلى {m('k = 10')}.",
                    f"يتبقى بعد الاختصار التلسكوبي {m('\\frac{1}{2} \\times \\frac{11}{10} = \\frac{11}{20}')}، وبالضرب في {m(20)} يكون الناتج {m(11)}.",
                ],
                f"التحقق بالصيغة: {m('20 \\times \\frac{10+1}{2(10)} = 11')}.",
                diagram_en=D.svg_telescoping_chain(["1/2·3/2", "2/3·4/3", "···", "9/10·11/10"], "×", "20 × (11/20) = ?"),
                diagram_ar=D.svg_telescoping_chain(["1/2·3/2", "2/3·4/3", "···", "9/10·11/10"], "×", "20 × (11/20) = ؟"),
            ),
            worked_math_example(
                "L23-E6",
                "Solved Example 6 — Solving a Linear Equation with Floor Function",
                "مثال محلول ٦ — حل معادلة خطية تحتوي على دالة الصحيح",
                f"A positive real number {m('x')} satisfies {m('2x + 3\\lfloor x \\rfloor = 21')}, where {m('\\lfloor x \\rfloor')} denotes the greatest integer less than or equal to {m('x')}. What is the value of {m('2x')}?",
                f"عدد حقيقي موجب {m('x')} يحقق المعادلة {m('2x + 3\\lfloor x \\rfloor = 21')}، حيث يرمز {m('\\lfloor x \\rfloor')} إلى أكبر عدد صحيح أصغر من أو يساوي {m('x')}. ما قيمة {m('2x')}؟",
                9, [8, 10, 11, 12],
                "Let \\( n = \\lfloor x \\rfloor \\). Since \\( n \\le x < n + 1 \\), bound \\( 5n \\le 21 < 5n + 2 \\) to find \\( n = 4 \\) immediately!",
                [
                    f"Set {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')}. Since {m('n \\le x < n + 1')}, we have {m('5n \\le 2x + 3n < 5n + 2')}.",
                    f"Because {m('2x + 3n = 21')}, the integer {m('n')} must satisfy {m('5n \\le 21 < 5n + 2')}, which forces {m('n = 4')}.",
                    f"Substitute {m('\\lfloor x \\rfloor = 4')}: {m('2x = 21 - 3(4) = 9')} (so {m('x = 4.5')}, which indeed has {m('\\lfloor 4.5 \\rfloor = 4')}).",
                ],
                f"Check {m('x = 4.5')}: {m('\\lfloor 4.5 \\rfloor = 4')} and {m('2(4.5) + 3(4) = 9 + 12 = 21')}.",
                "افرض \\( n = \\lfloor x \\rfloor \\) واحصر \\( 5n \\le 2x + 3n < 5n + 2 \\) لتحديد الجزء الصحيح \\( n = 4 \\) فوراً!",
                [
                    f"بفرض {m('n = \\lfloor x \\rfloor')} فإن {m('5n \\le 2x + 3n < 5n + 2')}.",
                    f"عند {m('2x + 3\\lfloor x \\rfloor = 21')} نجد {m('5n \\le 21 < 5n + 2 \\implies n = 4')}.",
                    f"نعوّض {m('\\lfloor x \\rfloor = 4')} فنجد {m('2x = 21 - 12 = 9')}.",
                ],
                f"التحقق عند {m('x = 4.5')}: {m('2(4.5) + 3(4) = 9 + 12 = 21')}.",
                diagram_en=D.svg_number_line_sign_chart([("4", True), ("x=4.5", True), ("5", False)], ["", "⌊x⌋ = 4", ""], "2x + 3⌊x⌋ = 21"),
                diagram_ar=D.svg_number_line_sign_chart([("4", True), ("x=4.5", True), ("5", False)], ["", "⌊x⌋ = 4", ""], "2x + 3⌊x⌋ = 21"),
            ),
        ],
    },

    "KMC-L2-04": {
        "extra_goals": [
            (
                "Compute **round-trip average speed** via the harmonic mean, combine **inlet (+) and leak (−) tank rates**, and analyze **round-robin league points**.",
                "حساب **السرعة المتوسطة لرحلة الذهاب والإياب** بالوسط التوافقي، ودمج **معدلات الملء (+) والتسريب (−) في الخزانات**، وتحليل **مجموع نقاط الدوريات الرياضية**.",
            ),
        ],
        "extra_concept": concept(
            "4. Harmonic Round-Trip Speed, Inlet–Leak Tanks & League Table Invariants",
            "٤. السرعة المتوسطة ذهاباً وإياباً، خزانات الملء والتسريب، ونقاط الدوريات",
            f"Traveling equal distances at speeds {m('v_1')} and {m('v_2')} gives average speed {m('v_{\\text{avg}} = \\frac{2v_1 v_2}{v_1 + v_2}')} (the **harmonic mean**, always strictly less than {m('\\frac{v_1+v_2}{2}')}!). "
            f"When an inlet fills a tank in {m('t_1')} hours and a leak empties it in {m('t_2')} hours, the net rate is {m('\\frac{1}{t_1} - \\frac{1}{t_2}')}. "
            f"In a round-robin league of {m('n')} teams ({m('3')} pts win, {m('1')} pt each draw), every decisive match adds {m(3)} total points and every draw adds {m(2)} total points!",
            f"عند قطع المسافة نفسها ذهاباً بسرعة {m('v_1')} وإياباً بسرعة {m('v_2')}، تكون السرعة المتوسطة {m('v_{\\text{avg}} = \\frac{2v_1 v_2}{v_1 + v_2}')} (**الوسط التوافقي**، وهو أصغر دائماً من الوسط الحسابي!). "
            f"وعند عمل صنبور يملأ الخزان في {m('t_1')} ساعة مع تسريب يفرغه في {m('t_2')} ساعة، يكون المعدل الصافي {m('\\frac{1}{t_1} - \\frac{1}{t_2}')}. "
            f"وفي دوري من {m('n')} فرق ({m(3)} نقاط للفوز ونقطة للتعادل لكل فريق)، تضيف كل مباراة حاسمة {m(3)} نقاط للمجموع الكلي بينما يضيف كل تعادل نقطتين فقط!",
            dm("v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}, \\qquad R_{\\text{net}} = \\frac{1}{t_{\\text{in}}} - \\frac{1}{t_{\\text{out}}}, \\qquad S_{\\text{league}} = 3M - D"),
            f'<div class="eg-f-caption" dir="rtl">الوسط التوافقي للسرعة، معدل الخزان الصافي، ومجموع نقاط الدوري:</div>{dm("v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}, \\qquad R_{\\text{net}} = \\frac{1}{t_{\\text{in}}} - \\frac{1}{t_{\\text{out}}}, \\qquad S = 3M - D")}',
            diagram_en=D.svg_pipe_tank("+1 / t_in", "−1 / t_out"),
            diagram_ar=D.svg_pipe_tank("+1 / t_in", "−1 / t_out"),
        ),
        "extra_traps": [
            (
                "Trap: Averaging \\( 60\\text{ km/h} \\) and \\( 40\\text{ km/h} \\) on a round trip as \\( 50\\text{ km/h} \\) — you spend **more time** at the slower speed, so \\( v_{\\text{avg}} = \\frac{2(60)(40)}{100} = 48\\text{ km/h} \\)!",
                "فخ شائع: حساب متوسط سرعة الذهاب \\( 60 \\) والإياب \\( 40 \\) على أنه \\( 50\\text{ كم/س} \\) — الصحيح استخدام الوسط التوافقي \\( \\frac{2(60)(40)}{60+40} = 48\\text{ كم/س} \\)!",
            ),
            (
                "Trap: Adding an outlet leak rate \\( +\\frac{1}{t_2} \\) instead of **subtracting** \\( -\\frac{1}{t_2} \\) from the inlet filling rate!",
                "فخ شائع: جمع معدل التسريب مع معدل الملء بدلاً من **طرحه** \\( \\frac{1}{t_1} - \\frac{1}{t_2} \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Arithmetic Progression", "المتتابعة الحسابية", r"\(a_m - a_n = (m - n)d\)", "Difference of terms = step gap × d.", "فرق الحدين = فرق الرتبتين × الأساس d."),
            cheat_item("Harmonic Round-Trip Speed", "السرعة المتوسطة ذهاباً وإياباً", r"\(v_{\text{avg}} = \frac{2v_1 v_2}{v_1 + v_2}\)", "Equal distances use the harmonic mean.", "تساوي المسافتين يتطلب الوسط التوافقي."),
            cheat_item("Inlet & Leak Tank", "صنبور الملء والتسريب", r"\(t_{\text{fill}} = \frac{t_1 t_2}{t_2 - t_1}\)", "Subtract leak rate 1/t₂ from inlet rate 1/t₁.", "اطرح معدل التسريب من معدل الملء."),
            cheat_item("League Draw Count", "عدد التعادلات في الدوري", r"\(D = 3\binom{n}{2} - \sum \text{Pts}\)", "Each draw reduces the 3M max point pool by 1.", "كل تعادل ينقص المجموع الأقصى 3M بمقدار 1."),
        ],
        "extra_examples": [
            worked_math_example(
                "L24-E5",
                "Solved Example 5 — Harmonic Mean Round-Trip Speed",
                "مثال محلول ٥ — السرعة المتوسطة لرحلة ذهاب وإياب",
                f"A driver travels from Thuwal to Jeddah at a constant speed of {m('60\\text{ km/h}')} and returns along the exact same route at {m('90\\text{ km/h}')}. What is the driver's **average speed** (in km/h) for the entire round trip?",
                f"قاد سائق سيارته من ثول إلى جدة بسرعة ثابتة قدرها {m('60\\text{ كم/س}')}، ثم عاد على الطريق نفسه تماماً بسرعة {m('90\\text{ كم/س}')}. ما **السرعة المتوسطة** للسائق (بـ كم/س) في رحلة الذهاب والإياب كاملةً؟",
                72, [70, 74, 75, 80],
                "Pick a convenient one-way distance divisible by both \\( 60 \\) and \\( 90 \\) (such as \\( 180\\text{ km} \\)), or apply \\( \\frac{2v_1 v_2}{v_1 + v_2} \\)!",
                [
                    f"Let the one-way distance be {m('\\operatorname{lcm}(60, 90) = 180\\text{ km}')}.",
                    f"The outbound trip takes {m('180 \\div 60 = 3')} hours and the return trip takes {m('180 \\div 90 = 2')} hours.",
                    f"Total distance divided by total time is {m('\\frac{180 + 180}{3 + 2} = \\frac{360}{5} = 72\\text{ km/h}')}.",
                ],
                f"Harmonic mean formula: {m('\\frac{2 \\times 60 \\times 90}{60 + 90} = \\frac{10800}{150} = 72\\text{ km/h}')}.",
                "افرض مسافة ذهاب تقبل القسمة على \\( 60 \\) و\\( 90 \\) معاً (مثل \\( 180\\text{ كم} \\))، أو طبّق قانون الوسط التوافقي \\( \\frac{2v_1 v_2}{v_1 + v_2} \\)!",
                [
                    f"بفرض مسافة الذهاب {m(180)} كم: زمن الذهاب {m('180 \\div 60 = 3')} ساعات وزمن الإياب {m('180 \\div 90 = 2')} ساعتان.",
                    f"السرعة المتوسطة = المسافة الكلية على الزمن الكلي = {m('\\frac{360}{3 + 2} = 72')} كم/س.",
                ],
                f"بالقانون المباشر: {m('\\frac{2(60)(90)}{60+90} = 72')} كم/س.",
                diagram_en=D.svg_motion_timeline("Thuwal", "Jeddah", "d = 180 km", "60 km/h →", "← 90 km/h", meet=True),
                diagram_ar=D.svg_motion_timeline("ثول", "جدة", "المسافة 180 كم", "60 كم/س ←", "→ 90 كم/س", meet=True),
            ),
            worked_math_example(
                "L24-E6",
                "Solved Example 6 — Counting Drawn Matches in a Round-Robin League",
                "مثال محلول ٦ — حساب عدد مباريات التعادل في دوري رياضي",
                f"Six football teams play a single round-robin tournament where every team plays every other team once. A win awards {m(3)} points to the winner and {m(0)} to the loser, while a draw awards {m(1)} point to each team. At the end of the tournament, the sum of all six teams' points is {m(41)}. How many matches ended in a **draw**?",
                f"تتنافس {m(6)} فرق في بطولة دوري من دور واحد بحيث يلعب كل فريق مع بقية الفرق مرة واحدة. يمنح الفوز {m(3)} نقاط للفائز و{m(0)} للخاسر، بينما يمنح التعادل نقطة واحدة لكل فريق. إذا كان مجموع نقاط الفرق الستة في نهاية البطولة {m(41)} نقطة، فكم مباراة انتهت **بالتعادل**؟",
                4, [2, 3, 5, 6],
                "There are \\( \\binom{6}{2} = 15 \\) matches in total; each decisive match contributes \\( 3 \\) points to the sum, and each draw reduces that maximum of \\( 45 \\) by \\( 1 \\) point!",
                [
                    f"The total number of matches played among {m(6)} teams is {m('\\binom{6}{2} = \\frac{6 \\times 5}{2} = 15')}.",
                    f"If all {m(15)} matches had a winner, the total points awarded would be {m('15 \\times 3 = 45')}.",
                    f"Each draw awards {m('1 + 1 = 2')} points instead of {m(3)} (losing {m(1)} point from the pool), so the number of draws is {m('45 - 41 = 4')}.",
                ],
                f"Check: {m(11)} wins + {m(4)} draws gives {m('11(3) + 4(2) = 33 + 8 = 41')} points.",
                "عدد المباريات الكلي \\( \\binom{6}{2} = 15 \\) مباراة؛ كل فوز يضيف \\( 3 \\) نقاط للمجموع الكلي وكل تعادل ينقص المجموع الأقصى (\\( 45 \\)) بمقدار نقطة واحدة!",
                [
                    f"إجمالي عدد المباريات هو {m('\\binom{6}{2} = 15')} مباراة.",
                    f"أقصى مجموع نقاط ممكن (دون أي تعادل) هو {m('15 \\times 3 = 45')} نقطة.",
                    f"كل تعادل ينقص المجموع الكلي بمقدار {m('3 - 2 = 1')} نقطة، فيكون عدد التعادلات {m('45 - 41 = 4')} مباريات.",
                ],
                f"التحقق: {m(11)} فوزاً و{m(4)} تعادلات تعطي {m('11(3) + 4(2) = 41')} نقطة.",
                diagram_en=D.svg_score_table(["Outcome", "Matches", "Pool Pts"], [["Win/Loss", "15 − D", "3 pts"], ["Draw", "D = ?", "2 pts"]], "Total Pool = 41"),
                diagram_ar=D.svg_score_table(["النتيجة", "المباريات", "النقاط الموزعة"], [["فوز/خسارة", "15 − D", "3 نقاط"], ["تعادل", "D = ؟", "نقطتان"]], "المجموع = 41"),
            ),
        ],
    },

    "KMC-L2-05": {
        "extra_goals": [
            (
                "Use **Thales's semicircle theorem** (\\( \\angle ACB = 90^\\circ \\)), drop **two altitudes in an isosceles trapezoid**, and compute **circular sector and annulus areas**.",
                "توظيف **مبرهنة طاليس في نصف الدائرة** (\\( \\angle ACB = 90^\\circ \\))، وإسقاط **عمودين في شبه المنحرف المتطابق الساقين**، وحساب **مساحات القطاعات والحلقات الدائرية**.",
            ),
        ],
        "extra_concept": concept(
            "4. Thales's Semicircle Theorem, Isosceles Trapezoids & Annulus Areas",
            "٤. مبرهنة طاليس، شبه المنحرف المتطابق الساقين، ومساحة الحلقة الدائرية",
            f"Any point {m('C')} on a circle with diameter {m('AB')} forms a right angle {m('\\angle ACB = 90^\\circ')}, and the circumradius of any right triangle is half its hypotenuse ({m('R = c/2')}). "
            f"In an isosceles trapezoid with parallel bases {m('a < b')} and legs {m('\\ell')}, dropping both altitudes splits {m('b')} into {m('\\frac{b-a}{2} + a + \\frac{b-a}{2}')}, giving height {m('h = \\sqrt{\\ell^2 - ((b-a)/2)^2}')}. "
            f"An annulus between concentric circles of radii {m('R > r')} has area {m('\\pi(R^2 - r^2) = \\pi(L_{\\text{tangent}}/2)^2')}.",
            f"أي زاوية محيطية {m('\\angle ACB')} مرسومة في نصف دائرة قطرها {m('AB')} هي زاوية قائمة {m('90^\\circ')}. "
            f"وفي شبه المنحرف المتطابق الساقين ذي القاعدتين {m('a < b')} والساق {m('\\ell')}، إسقاط العمودين من الرأسين العلويين يقتطع مستطيلاً في الوسط ومثلثين قائمين متطابقين قاعدتهما {m('\\frac{b - a}{2}')}. "
            f"ومساحة الحلقة الدائرية بين دائرتين متحدتي المركز تساوي {m('\\pi(R^2 - r^2)')}.",
            dm("\\angle ACB = 90^\\circ \\;(\\text{diameter } AB), \\qquad h_{\\text{trap}} = \\sqrt{\\ell^2 - \\left(\\frac{b - a}{2}\\right)^2}"),
            f'<div class="eg-f-caption" dir="rtl">مبرهنة طاليس وارتفاع شبه المنحرف المتطابق الساقين:</div>{dm("\\angle ACB = 90^\\circ, \\qquad h = \\sqrt{\\ell^2 - \\left(\\frac{b - a}{2}\\right)^2}")}',
            diagram_en=D.svg_isosceles_trapezoid("a", "b", "ℓ", "h"),
            diagram_ar=D.svg_isosceles_trapezoid("a", "b", "ℓ", "h"),
        ),
        "extra_traps": [
            (
                "Trap: Using the full base difference \\( b - a \\) instead of **half** the difference \\( \\frac{b - a}{2} \\) as the horizontal leg in an isosceles trapezoid!",
                "فخ شائع: استعمال فرق القاعدتين كاملاً \\( b - a \\) بدلاً من **نصف الفرق** \\( \\frac{b - a}{2} \\) كقاعدة للمثلث القائم الطرفي في شبه المنحرف المتطابق الساقين!",
            ),
            (
                "Trap: Forgetting that the radius \\( OA = OB = OC \\) in a semicircle creates **isosceles** triangles \\( \\triangle OAC \\) and \\( \\triangle OBC \\)!",
                "فخ شائع: إغفال أن أنصاف الأقطار \\( OA = OB = OC \\) في نصف الدائرة تصنع مثلثين **متطابقي الضلعين** \\( \\triangle OAC \\) و\\( \\triangle OBC \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Isosceles Vertex Angle", "زوايا المثلث المتطابق الضلعين", r"\(\text{Base Angle} = \frac{180^\circ - V}{2}\)", "Equal sides subtend equal opposite angles.", "الضلعان المتساويان يقابلان زاويتين متساويتين."),
            cheat_item("Overlap Subtraction", "طرح المنطقة المشتركة", r"\((A_1 - A_0) - (A_2 - A_0) = A_1 - A_2\)", "The unknown overlap A₀ cancels out.", "المنطقة المتداخلة المجهولة A₀ تختصر بالطرح."),
            cheat_item("Thales's Semicircle", "مبرهنة طاليس", r"\(AB\text{ diameter} \implies \angle ACB = 90^\circ\)", "Angle inscribed in a semicircle is 90°.", "الزاوية المحيطية المرسومة في نصف دائرة قائمة."),
            cheat_item("Isosceles Trapezoid Height", "ارتفاع شبه المنحرف", r"\(h = \sqrt{\ell^2 - \left(\frac{b - a}{2}\right)^2}\)", "Drop two altitudes to form right triangles.", "أسقط عمودين لتكوين مثلثين قائمين متطابقين."),
        ],
        "extra_examples": [
            worked_math_example(
                "L25-E6",
                "Solved Example 6 — Area of an Isosceles Trapezoid via Pythagorean Altitude",
                "مثال محلول ٦ — مساحة شبه منحرف متطابق الساقين بإسقاط الارتفاع",
                f"An isosceles trapezoid has parallel bases of lengths {m(10)} and {m(22)}, and each of its two non-parallel legs has length {m(10)}. What is the **area** of the trapezoid?",
                f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(10)} و{m(22)}، وطول كل ساق من ساقيه غير المتوازيتين {m(10)}. ما **مساحة** شبه المنحرف؟",
                128, [112, 120, 144, 160],
                "Drop perpendiculars from both ends of the top base \\( 10 \\) to split the bottom base \\( 22 \\) into \\( 6 + 10 + 6 \\)!",
                [
                    f"Dropping both altitudes divides the bottom base {m(22)} into a middle segment of {m(10)} and two symmetric outer segments of {m('\\frac{22 - 10}{2} = 6')} each.",
                    f"By the Pythagorean theorem on the {m('6\\text{-}h\\text{-}10')} right triangle, the height is {m('h = \\sqrt{10^2 - 6^2} = 8')}.",
                    f"The area of the trapezoid is {m('\\frac{10 + 22}{2} \\times 8 = 16 \\times 8 = 128')}.",
                ],
                f"Check: central rectangle {m('10 \\times 8 = 80')} plus two right triangles {m('2 \\times \\frac{1}{2}(6)(8) = 48')} gives {m('80 + 48 = 128')}.",
                "أسقط عمودين من طرفي القاعدة الصغرى \\( 10 \\) لتنقسم القاعدة الكبرى \\( 22 \\) إلى \\( 6 + 10 + 6 \\)!",
                [
                    f"الجزء الأفقي لكل مثلث قائم طرفي هو {m('\\frac{22 - 10}{2} = 6')}.",
                    f"من فيثاغورس للوتر {m(10)} والقاعدة {m(6)}: الارتفاع {m('h = \\sqrt{10^2 - 6^2} = 8')}.",
                    f"مساحة شبه المنحرف = {m('\\frac{10 + 22}{2} \\times 8 = 16 \\times 8 = 128')}.",
                ],
                f"التحقق: المستطيل الأوسط {m(80)} + المثلثان الطرفيان {m(48)} = {m(128)}.",
                diagram_en=D.svg_isosceles_trapezoid("10", "22", "10", "h = ?"),
                diagram_ar=D.svg_isosceles_trapezoid("10", "22", "10", "ع = ؟"),
            ),
        ],
    },

    "KMC-L2-06": {
        "extra_goals": [
            (
                "Count **grid paths avoiding a blocked intersection**, find minimum **3-way pan-balance weighings** for a counterfeit coin, and compute **two-box sequential transfer probabilities**.",
                "عدّ **مسارات الشبكة مع وجود تقاطع مغلق**، وتحديد أقل عدد من **وزنات الميزان ذي الكفتين** لاكتشاف العملة المزيفة، وحساب **احتمالات النقل المتتابع بين صندوقين**.",
            ),
        ],
        "extra_concept": concept(
            "4. Blocked-Grid Subtraction, Ternary Pan-Balance Weighings & Two-Box Transfers",
            "٤. مسارات الشبكة المغلقة، وزنات العملة المزيفة (3ᵏ)، والنقل بين صندوقين",
            f"To count shortest paths from {m('A(0,0)')} to {m('B(m,n)')} avoiding a blocked node {m('P(a,b)')}, subtract paths passing through {m('P')}: {m('\\binom{m+n}{m} - \\binom{a+b}{a}\\binom{(m-a)+(n-b)}{m-a}')}. "
            f"Each weighing on a two-pan balance has **3 outcomes** (Left heavy, Right heavy, Balanced), so {m('k')} weighings can distinguish one lighter/heavier counterfeit coin among up to {m('3^k')} coins! "
            f"For sequential transfer from Box A to Box B, condition on the color transferred in Step 1.",
            f"لعدّ أقصر المسارات من {m('A(0,0)')} إلى {m('B(m,n)')} مع تجنّب النقطة المغلقة {m('P(a,b)')}، اطرح المسارات المارة بـ {m('P')}: {m('\\binom{m+n}{m} - \\binom{a+b}{a}\\binom{(m-a)+(n-b)}{m-a}')}. "
            f"ولكل وزنة على ميزان ذي كفتين **3 نتائج ممكنة** (الكفة اليسرى أثقل، اليمنى أثقل، تعادل)، لذا تكفي {m('k')} وزنات لتحديد عملة واحدة أخف (أو أثقل) بين ما يصل إلى {m('3^k')} عملة! "
            f"وفي مسائل نقل كرة من صندوق أول إلى ثانٍ، فرّع الحل حسب لون الكرة المنقولة في الخطوة الأولى.",
            dm("N_{\\text{avoid }P} = \\binom{m+n}{m} - \\binom{a+b}{a}\\binom{m+n-a-b}{m-a}, \\qquad N_{\\text{coins}}(k) \\le 3^k"),
            f'<div class="eg-f-caption" dir="rtl">طرح المسارات المارة بنقطة مغلقة والحد الأقصى لوزنات الميزان:</div>{dm("N_{\\text{avoid }P} = \\binom{m+n}{m} - \\binom{a+b}{a}\\binom{m+n-a-b}{m-a}, \\qquad N_{\\text{coins}} \\le 3^k")}',
            diagram_en=D.svg_pan_balance_coins("3^k Rule", "3^{k-1}", "3^{k-1}", "3^{k-1} aside"),
            diagram_ar=D.svg_pan_balance_coins("قاعدة 3^k", "3^{k-1}", "3^{k-1}", "3^{k-1} خارج الميزان"),
        ),
        "extra_traps": [
            (
                "Trap: Dividing coins into **2 halves** instead of **3 equal groups** on a two-pan balance — the unweighed third group gives just as much information when the pans balance!",
                "فخ شائع: تقسيم العملات إلى **نصفين** بدلاً من **3 مجموعات متساوية** في مسائل الميزان ذي الكفتين — المجموعة الثالثة خارج الميزان تحسم النتيجة عند تعادل الكفتين!",
            ),
            (
                "Trap: Forgetting to increase the denominator of Box B by \\( +1 \\) after transferring a ball from Box A into Box B!",
                "فخ شائع: نسيان زيادة العدد الكلي للكرات في الصندوق الثاني بمقدار \\( +1 \\) بعد نقل كرة إليه من الصندوق الأول!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Sub-Rectangles in Grid", "عدد المستطيلات في شبكة", r"\(\binom{m + 1}{2}\binom{n + 1}{2}\)", "Choose 2 vertical lines and 2 horizontal lines.", "اختر خطين عموديين وخطين أفقيين."),
            cheat_item("Blocked Grid Node", "نقطة تقاطع مغلقة", r"\(\binom{m+n}{m} - \binom{a+b}{a}\binom{m-a+n-b}{m-a}\)", "Total paths minus paths through P(a,b).", "المسارات الكلية ناقص المسارات المارة بـ P."),
            cheat_item("3-Way Coin Weighings", "وزنات العملة المزيفة", r"\(3^{k-1} < N \le 3^k \implies k\text{ weighings}\)", "Split into 3 groups (left, right, table).", "قسّم العملات إلى 3 مجموعات متقاربة."),
            cheat_item("Worst-Case Pigeonhole", "مبدأ برج الحمام", r"\(\sum \min(c_i,\, k - 1) + 1\)", "Take (k−1) from every color, then +1.", "خذ (k−1) من كل نوع متاح ثم أضف 1."),
        ],
        "extra_examples": [
            worked_math_example(
                "L26-E5",
                "Solved Example 5 — Shortest Grid Paths Avoiding a Blocked Intersection",
                "مثال محلول ٥ — أقصر المسارات الشبكية مع وجود تقاطع مغلق",
                f"On a {m('4 \\times 3')} city grid (4 blocks East, 3 blocks North), a walker travels from corner {m('A(0,0)')} to corner {m('B(4,3)')} moving only East and North. If intersection {m('P(2, 1)')} is closed for construction, how many valid shortest paths are there?",
                f"في شبكة طرق أبعادها {m('4 \\times 3')} (4 مربعات شرقاً و3 شمالاً)، يتحرك شخص من الركن {m('A(0,0)')} إلى الركن {m('B(4,3)')} باتجاهي الشرق والشمال فقط. إذا كان التقاطع {m('P(2, 1)')} مغلقاً، فكم مساراً قصيراً صالحاً يوجد؟",
                17, [15, 18, 20, 23],
                "Subtract the paths that pass through \\( P(2,1) \\) from the total unrestricted paths \\( \\binom{7}{3} \\)!",
                [
                    f"Without restrictions, the total number of shortest paths is {m('\\binom{4+3}{3} = \\binom{7}{3} = 35')}.",
                    f"Paths from {m('A(0,0)')} to {m('P(2,1)')} equal {m('\\binom{2+1}{1} = 3')}, and paths from {m('P(2,1)')} to {m('B(4,3)')} equal {m('\\binom{2+2}{2} = 6')}.",
                    f"Multiply to find paths through {m('P(2,1)')}: {m('3 \\times 6 = 18')}. Subtracting gives {m('35 - 18 = 17')} valid paths.",
                ],
                f"Check: {m('\\binom{7}{3} - \\binom{3}{1}\\binom{4}{2} = 35 - 18 = 17')}.",
                "اطرح عدد المسارات المارة بالنقطة المغلقة \\( P(2,1) \\) من إجمالي عدد المسارات \\( \\binom{7}{3} \\)!",
                [
                    f"عدد المسارات الكلي بدون إغلاق هو {m('\\binom{4+3}{3} = 35')} مساراً.",
                    f"عدد المسارات من {m('A(0,0)')} إلى {m('P(2,1)')} هو {m('\\binom{3}{1} = 3')}، ومن {m('P(2,1)')} إلى {m('B(4,3)')} هو {m('\\binom{4}{2} = 6')}.",
                    f"إذن عدد المسارات الصالحة = {m('35 - (3 \\times 6) = 35 - 18 = 17')} مساراً.",
                ],
                f"التحقق: {m('35 - 18 = 17')}.",
                diagram_en=D.svg_street_grid(4, 3, (2, 1)),
                diagram_ar=D.svg_street_grid(4, 3, (2, 1)),
            ),
            worked_math_example(
                "L26-E6",
                "Solved Example 6 — Minimum Pan-Balance Weighings for a Lighter Coin",
                "مثال محلول ٦ — أقل عدد من الوزنات لاكتشاف العملة المزيفة الأخف",
                f"Among {m(25)} identical-looking gold coins, exactly **one** coin is counterfeit and slightly **lighter** than the others. Using a two-pan balance scale without weights, what is the **minimum** number of weighings needed to **guarantee** finding the counterfeit coin?",
                f"من بين {m(25)} عملة ذهبية متماثلة الشكل، توجد عملة **واحدة** فقط مزيفة وهي **أخف** قليلاً من البقية. باستخدام ميزان ذي كفتين (دون أثقال خارجية)، ما **أقل** عدد من الوزنات يكفي **لضمان** تحديد العملة المزيفة في جميع الحالات؟",
                3, [2, 4, 5, 6],
                "Since each weighing has 3 outcomes, \\( k \\) weighings can test up to \\( 3^k \\) coins, and \\( 3^2 = 9 < 25 \\le 27 = 3^3 \\)!",
                [
                    f"In Weighing 1, place {m(9)} coins on the left pan, {m(9)} on the right pan, and leave {m(7)} on the table: the lighter group of at most {m(9)} coins is identified.",
                    f"In Weighing 2, split that group (at most {m(9)}) into {m('3 + 3 + 3')} (or {m('3 + 3 + 1')}): this narrows the counterfeit coin to at most {m(3)} coins.",
                    f"In Weighing 3, weigh {m(1)} against {m(1)} from those {m(3)} coins to pinpoint the lighter coin. Thus {m(3)} weighings suffice (and {m(2)} weighings can distinguish at most {m('3^2 = 9 < 25')} coins).",
                ],
                f"Check information bound: {m('3^2 = 9 < 25 \\le 27 = 3^3 \\implies k = 3')}.",
                "بما أن لكل وزنة 3 نتائج ممكنة، فإن \\( k \\) وزنات تميّز حتى \\( 3^k \\) عملة، ولدينا \\( 3^2 = 9 < 25 \\le 27 = 3^3 \\)!",
                [
                    f"في الوزنة الأولى نضع {m(9)} عملات في كل كفة ونترك {m(7)} خارج الميزان، فنحصر العملة الأخف في مجموعة من {m(9)} عملات على الأكثر.",
                    f"في الوزنة الثانية نقسّم الـ {m(9)} إلى {m('3 + 3 + 3')} فنحصرها في {m(3)} عملات على الأكثر.",
                    f"في الوزنة الثالثة نزن عملة مقابل عملة فنحدد العملة المزيفة يقيناً في {m(3)} وزنات.",
                ],
                f"التحقق: {m('3^2 = 9 < 25 \\le 27 = 3^3')} إذن أقل عدد هو {m(3)}.",
                diagram_en=D.svg_pan_balance_coins("25 Coins → k = ?", "9 coins", "9 coins", "7 on table (≤ 3³ = 27)"),
                diagram_ar=D.svg_pan_balance_coins("25 عملة ← k = ؟", "9 عملات", "9 عملات", "7 خارج الميزان (≤ 27)"),
            ),
        ],
    },

    # =========================================================================
    # TRACK 3: GRADES 10–11 (KMC-L3-01 .. KMC-L3-06)
    # =========================================================================
    "KMC-L3-01": {
        "extra_goals": [
            (
                "Compute **Legendre's prime exponent** \\( v_p(n!) \\), count divisors of \\( n^2 \\) from \\( (2e_i + 1) \\), and apply the **Chicken McNugget (Frobenius) coin theorem** \\( ab - a - b \\).",
                "حساب **أس العامل الأولي في المضروب (صيغة ليجندر)** \\( v_p(n!) \\)، وعدّ قواسم \\( n^2 \\) عبر \\( (2e_i + 1) \\)، وتطبيق **مبرهنة فروبينيوس (الطوابع والعملات)** \\( ab - a - b \\).",
            ),
        ],
        "extra_concept": concept(
            "4. Legendre's v_p(n!) Formula, Divisors of n² & Frobenius Coin Theorem",
            "٤. صيغة ليجندر للمضروب، قواسم المربع الكامل، ومبرهنة فروبينيوس",
            f"For any prime {m('p')}, the exact exponent of {m('p')} dividing {m('n!')} is {m('v_p(n!) = \\sum_{k \\ge 1} \\lfloor n / p^k \\rfloor')}. "
            f"If {m('n = \\prod p_i^{e_i}')}, then {m('n^2 = \\prod p_i^{2e_i}')} has {m('\\tau(n^2) = \\prod (2e_i + 1)')} divisors (always odd!). "
            f"For two coprime coin/stamp denominations {m('a, b')} with {m('\\gcd(a,b)=1')}, the **largest unattainable amount** is {m('ab - a - b')}, and the number of unattainable non-negative amounts is {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"لأي عدد أولي {m('p')}، يُعطى أس {m('p')} في تحليل المضروب {m('n!')} بصيغة ليجندر {m('v_p(n!) = \\sum_{k \\ge 1} \\lfloor n / p^k \\rfloor')}. "
            f"وإذا كان {m('n = \\prod p_i^{e_i}')} فإن عدد قواسم مربعه هو {m('\\tau(n^2) = \\prod (2e_i + 1)')}. "
            f"ولفئتين أوليتين نسبياً {m('\\gcd(a,b)=1')}، فإن **أكبر مبلغ لا يمكن تكوينه** هو {m('ab - a - b')}، وعدد المبالغ غير الممكنة يساوي {m('\\frac{(a-1)(b-1)}{2}')}!",
            dm("v_p(n!) = \\sum_{k \\ge 1}\\left\\lfloor\\frac{n}{p^k}\\right\\rfloor, \\qquad g(a, b) = ab - a - b, \\qquad N_{\\text{unattainable}} = \\frac{(a-1)(b-1)}{2}"),
            f'<div class="eg-f-caption" dir="rtl">صيغة ليجندر وأكبر قيمة غير قابلة للتمثيل (فروبينيوس):</div>{dm("v_p(n!) = \\sum_{k \\ge 1}\\left\\lfloor\\frac{n}{p^k}\\right\\rfloor, \\qquad g(a, b) = ab - a - b")}',
            diagram_en=D.svg_factorial_padic_bars("v_p(n!) & Frobenius", [("⌊n/p⌋", 1.0, "p¹"), ("⌊n/p²⌋", 0.55, "p²"), ("ab−a−b", 0.85, "Max Gap")]),
            diagram_ar=D.svg_factorial_padic_bars("صيغة ليجندر وفروبينيوس", [("⌊n/p⌋", 1.0, "p¹"), ("⌊n/p²⌋", 0.55, "p²"), ("ab−a−b", 0.85, "أكبر عجز")]),
        ),
        "extra_traps": [
            (
                "Trap: Using the Frobenius formula \\( ab - a - b \\) when \\( \\gcd(a, b) > 1 \\) — if \\( \\gcd(a, b) > 1 \\), infinitely many numbers are unattainable!",
                "فخ شائع: تطبيق قانون فروبينيوس \\( ab - a - b \\) عندما يكون \\( \\gcd(a, b) > 1 \\) — إذا لم تكن الفئتان أوليتين نسبياً فيوجد عدد لا نهائي من القيم المستحيلة!",
            ),
            (
                "Trap: Computing \\( v_p(n!) \\) as \\( \\lfloor n/p \\rfloor \\) only and forgetting higher powers \\( \\lfloor n/p^2 \\rfloor + \\lfloor n/p^3 \\rfloor + \\cdots \\)!",
                "فخ شائع: الاكتفاء بالحد الأول \\( \\lfloor n/p \\rfloor \\) في صيغة ليجندر وإهمال القوى الأعلى \\( \\lfloor n/p^2 \\rfloor + \\lfloor n/p^3 \\rfloor \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Lone Even Prime", "الأولي الزوجي الوحيد", r"\(p + q \equiv 1 \pmod 2 \implies 2 \in \{p, q\}\)", "An odd sum/difference of primes forces 2.", "المجموع أو الفرق الفردي لأوليين يفرض وجود 2."),
            cheat_item("Legendre's Formula", "صيغة ليجندر", r"\(v_p(n!) = \sum_{k\ge 1}\lfloor n/p^k\rfloor\)", "Sum floor quotients across all powers of p.", "اجمع نواتج القسمة الصحيحة لجميع قوى p."),
            cheat_item("Squares Modulo 4", "بواقي المربعات على 4", r"\(n^2 \equiv 0 \text{ or } 1 \pmod 4\)", "A sum of two squares is never ≡ 3 (mod 4).", "مجموع مربعين لا يترك الباقي 3 على 4 أبداً."),
            cheat_item("Chicken McNugget Theorem", "مبرهنة فروبينيوس", r"\(\max_{\text{impossible}} = ab - a - b\)", "Requires gcd(a, b) = 1.", "يشترط أن يكون gcd(a, b) = 1."),
        ],
        "extra_examples": [
            worked_math_example(
                "L31-E6",
                "Solved Example 6 — Largest Unattainable Postage via Frobenius Theorem",
                "مثال محلول ٦ — أكبر قيمة طوابع غير ممكنة بمبرهنة فروبينيوس",
                f"A post office sells stamps only in denominations of {m(7)} riyals and {m(11)} riyals. What is the **largest** whole-riyal postage amount that **cannot** be formed using a non-negative combination of these two stamp values?",
                f"يبيع مكتب بريد طوابع من فئتي {m(7)} ريالات و{m(11)} ريالاً فقط. ما **أكبر** مبلغ صحيح بالريالات **لا يمكن** تكوينه أبداً باستخدام هاتين الفئتين؟",
                59, [55, 58, 60, 66],
                "Since \\( \\gcd(7, 11) = 1 \\), apply the Frobenius (Chicken McNugget) formula \\( g(a, b) = ab - a - b \\)!",
                [
                    f"Check coprimality: {m('\\gcd(7, 11) = 1')}, so every sufficiently large integer can be formed.",
                    f"By the Frobenius Coin Theorem, the largest unattainable integer is {m('ab - a - b = 7 \\times 11 - 7 - 11')}.",
                    f"Evaluate: {m('77 - 18 = 59')}.",
                ],
                f"Check {m(60)}: {m('60 = 5(11) + 5')} no, {m('60 = 7(7) + 11 = 49 + 11 = 60')}! And {m('61 = 4(7) + 3(11) = 28 + 33')}.",
                "بما أن \\( \\gcd(7, 11) = 1 \\)، طبّق صيغة فروبينيوس \\( ab - a - b \\) مباشرة!",
                [
                    f"العددان {m(7)} و{m(11)} أوليان نسبياً لأن {m('\\gcd(7, 11) = 1')}.",
                    f"أكبر مبلغ لا يمكن تكوينه هو {m('7 \\times 11 - 7 - 11 = 77 - 18 = 59')} ريالاً.",
                ],
                f"التحقق: المبلغ التالي {m('60 = 7(7) + 1(11)')} قابل للتكوين.",
                diagram_en=D.svg_algebra_flow([("Stamps", "a = 7, b = 11"), ("Coprime", "gcd(7,11) = 1"), ("Max Gap", "ab − a − b = ?")], ["→", "="]),
                diagram_ar=D.svg_algebra_flow([("الفئتان", "a = 7, b = 11"), ("أوليان نسبياً", "gcd(7,11) = 1"), ("أكبر عجز", "ab − a − b = ؟")], ["←", "="]),
            ),
        ],
    },

    "KMC-L3-02": {
        "extra_goals": [
            (
                "Evaluate **symmetric floor sums** by pairing \\( k \\) with \\( n - k \\), convert numbers across **non-decimal bases \\( b \\)**, and find **constrained sum/product extrema**.",
                "حساب **مجاميع دالة الصحيح المتناظرة** بالمزاوجة بين \\( k \\) و\\( n - k \\)، والتحويل بين **أنظمة العد للأساس \\( b \\)**، وإيجاد **القيم القصوى للمجموع والجداء**.",
            ),
        ],
        "extra_concept": concept(
            "4. Symmetric Floor Pairing, Base-b Conversions & Sum–Product Extrema",
            "٤. المزاوجة المتناظرة لدالة الصحيح، أنظمة العد للأساس b، والقيم القصوى",
            f"For any non-integer real number {m('x \\notin \\mathbb{Z}')}, {m('\\lfloor x \\rfloor + \\lfloor 1 - x \\rfloor = 0')} and {m('\\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1')}. "
            f"In base {m('b')}, the numeral {m('\\overline{d_2 d_1 d_0}_{(b)}')} represents the polynomial {m('d_2 b^2 + d_1 b + d_0')} with digits {m('0 \\le d_i < b')}. "
            f"For positive numbers with fixed sum {m('S')}, their product is maximized when the numbers are as **close together** as possible (AM–GM).",
            f"لأي عدد حقيقي غير صحيح {m('x \\notin \\mathbb{Z}')}، يتحقق دائماً {m('\\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1')}. "
            f"وفي نظام العد ذي الأساس {m('b')}، يمثّل العدد {m('\\overline{d_2 d_1 d_0}_{(b)}')} كثيرة الحدود {m('d_2 b^2 + d_1 b + d_0')} بشرط {m('0 \\le d_i < b')}. "
            f"ولأعداد موجبة مجموعها ثابت {m('S')}، يتحقق أكبر جداء ممكن عندما تكون الأعداد **متساوية أو متقاربة لأقصى حد**.",
            dm("x \\notin \\mathbb{Z} \\implies \\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1, \\qquad \\overline{d_2 d_1 d_0}_{(b)} = d_2 b^2 + d_1 b + d_0"),
            f'<div class="eg-f-caption" dir="rtl">المزاوجة المتناظرة لدالة الصحيح والتمثيل في الأساس b:</div>{dm("\\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1 \\;(x \\notin \\mathbb{Z}), \\qquad \\overline{d_2 d_1 d_0}_{(b)} = d_2 b^2 + d_1 b + d_0")}',
            diagram_en=D.svg_digit_cards(["d₂·b²", "d₁·b¹", "d₀·b⁰"], "Base b", "0 ≤ dᵢ < b"),
            diagram_ar=D.svg_digit_cards(["d₂·b²", "d₁·b¹", "d₀·b⁰"], "الأساس b", "0 ≤ dᵢ < b"),
        ),
        "extra_traps": [
            (
                "Trap: Using \\( \\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1 \\) when \\( x \\) is an **integer** — for integers, \\( \\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m \\)!",
                "فخ شائع: تطبيق \\( \\lfloor x \\rfloor + \\lfloor m - x \\rfloor = m - 1 \\) عندما يكون \\( x \\) **عدداً صحيحاً** — للأعداد الصحيحة يساوي المجموع \\( m \\) تماماً!",
            ),
            (
                "Trap: Accepting a base \\( b \\) that is smaller than or equal to one of the digits appearing in the numeral (every digit \\( d \\) in base \\( b \\) must satisfy \\( d < b \\))!",
                "فخ شائع: قبول أساس عدّ \\( b \\) أصغر من أو يساوي أحد الأرقام الظاهرة في العدد (يجب دائماً أن يكون كل رقم \\( d < b \\))!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("⌊√n⌋ Block Length", "طول فترة ثبات ⌊√n⌋", r"\(\#\{n : \lfloor\sqrt{n}\rfloor = m\} = 2m + 1\)", "Runs from m² to (m+1)² − 1.", "يمتد من m² إلى (m+1)² − 1."),
            cheat_item("Triangular Block Index", "رتبة المتتالية المثلثية", r"\(T_k = \frac{k(k+1)}{2} \ge N\)", "Find smallest k whose triangular number ≥ N.", "أوجد أصغر عدد مثلثي أكبر من أو يساوي N."),
            cheat_item("Symmetric Floor Pair", "مزاوجة دالة الصحيح", r"\(\left\lfloor\frac{k}{p}\right\rfloor + \left\lfloor\frac{m\cdot p - k}{p}\right\rfloor = m - 1\)", "Holds whenever p does not divide k.", "يتحقق كلما كان k لا يقبل القسمة على p."),
            cheat_item("Base-b Expansion", "التحويل من الأساس b", r"\(\overline{abc}_{(b)} = ab^2 + bb + c\)", "Recognize algebraic squares like 121_b = (b+1)².", "لاحظ المربعات الجبرية مثل 121_b = (b+1)²."),
        ],
        "extra_examples": [
            worked_math_example(
                "L32-E5",
                "Solved Example 5 — Symmetric Floor Sum Pairing",
                "مثال محلول ٥ — جمع دالة الصحيح بالمزاوجة المتناظرة",
                f"What is the exact value of the sum {m('S = \\left\\lfloor\\frac{1}{7}\\right\\rfloor + \\left\\lfloor\\frac{2}{7}\\right\\rfloor + \\left\\lfloor\\frac{3}{7}\\right\\rfloor + \\cdots + \\left\\lfloor\\frac{27}{7}\\right\\rfloor')}?",
                f"ما القيمة الدقيقة للمجموع {m('S = \\left\\lfloor\\frac{1}{7}\\right\\rfloor + \\left\\lfloor\\frac{2}{7}\\right\\rfloor + \\left\\lfloor\\frac{3}{7}\\right\\rfloor + \\cdots + \\left\\lfloor\\frac{27}{7}\\right\\rfloor')}؟",
                42, [36, 39, 45, 49],
                "Pair \\( \\frac{k}{7} \\) with \\( \\frac{28 - k}{7} = 4 - \\frac{k}{7} \\), or group the terms into blocks of length \\( 7 \\)!",
                [
                    f"Group {m('k = 1, \\dots, 27')} by quotient mod {m(7)}: for {m('k = 1..6')} ({m(6)} terms) the floor is {m(0)}; for {m('k = 7..13')} ({m(7)} terms) it is {m(1)}; for {m('k = 14..20')} ({m(7)} terms) it is {m(2)}; for {m('k = 21..27')} ({m(7)} terms) it is {m(3)}.",
                    f"Sum the blocks: {m('6(0) + 7(1) + 7(2) + 7(3) = 7(1 + 2 + 3) = 42')}.",
                ],
                f"Pairing check: {m(3)} integer terms ({m('7/7+14/7+21/7 = 6')}) plus {m(12)} non-integer pairs each summing to {m('4 - 1 = 3')} gives {m('6 + 36 = 42')}.",
                "قسّم الحدود إلى فترات طول كلٍّ منها \\( 7 \\) أو زاوج بين \\( \\frac{k}{7} \\) و\\( \\frac{28-k}{7} \\)!",
                [
                    f"الحدود من {m('1..6')} قيمتها {m(0)}، ومن {m('7..13')} ({m(7)} حدود) قيمتها {m(1)}، ومن {m('14..20')} ({m(7)} حدود) قيمتها {m(2)}، ومن {m('21..27')} ({m(7)} حدود) قيمتها {m(3)}.",
                    f"المجموع الكلي = {m('7(1 + 2 + 3) = 42')}.",
                ],
                f"التحقق بالمزاوجة: {m('6 + 12 \\times 3 = 42')}.",
                diagram_en=D.svg_telescoping_chain(["1..6 → 0", "7..13 → 1", "14..20 → 2", "21..27 → 3"], "+", "7(1+2+3) = ?", slash_middle=False),
                diagram_ar=D.svg_telescoping_chain(["1..6 ← 0", "7..13 ← 1", "14..20 ← 2", "21..27 ← 3"], "+", "7(1+2+3) = ؟", slash_middle=False),
            ),
            worked_math_example(
                "L32-E6",
                "Solved Example 6 — Solving for an Unknown Base b",
                "مثال محلول ٦ — إيجاد أساس العد المجهول b",
                f"In a certain base {m('b > 4')}, the three-digit number {m('144_{(b)}')} is equal to the base-10 number {m('81')}. What is the value of the base {m('b')}?",
                f"في نظام عدّ أساسه {m('b > 4')}، يساوي العدد المكون من ثلاث خانات {m('144_{(b)}')} العدد {m('81')} في النظام العشري. ما قيمة الأساس {m('b')}؟",
                7, [5, 6, 8, 9],
                "Expand \\( 144_{(b)} = b^2 + 4b + 4 = (b + 2)^2 \\) and take the square root!",
                [
                    f"Convert {m('144_{(b)}')} to base 10 using place values: {m('1\\cdot b^2 + 4\\cdot b + 4 = b^2 + 4b + 4')}.",
                    f"Recognize the perfect square trinomial: {m('(b + 2)^2 = 81')}.",
                    f"Since {m('b > 0')}, {m('b + 2 = 9 \\implies b = 7')}.",
                ],
                f"Check in base {m(7)}: {m('1\\times 49 + 4\\times 7 + 4 = 49 + 28 + 4 = 81')}.",
                "فكّ التمثيل الموضعي \\( 144_{(b)} = b^2 + 4b + 4 = (b + 2)^2 \\) ثم خذ الجذر التربيعي!",
                [
                    f"نحوّل العدد إلى النظام العشري: {m('144_{(b)} = b^2 + 4b + 4 = (b + 2)^2')}.",
                    f"بمساواته بالعدد {m(81)}: {m('(b + 2)^2 = 81 \\implies b + 2 = 9 \\implies b = 7')}.",
                ],
                f"التحقق في الأساس {m(7)}: {m('49 + 28 + 4 = 81')}.",
                diagram_en=D.svg_algebra_flow([("144_(b)", "b² + 4b + 4"), ("Square", "(b + 2)² = 81"), ("Base", "b = ?")], ["=", "√"]),
                diagram_ar=D.svg_algebra_flow([("144_(b)", "b² + 4b + 4"), ("مربع كامل", "(b + 2)² = 81"), ("الأساس", "b = ؟")], ["=", "√"]),
            ),
        ],
    },

    "KMC-L3-03": {
        "extra_goals": [
            (
                "Solve **exponential equations quadratic in \\( a^x \\)** via Vieta's product of roots and evaluate **reciprocal cube sums** \\( x^3 + x^{-3} \\).",
                "حل **المعادلات الأسية التربيعية في \\( a^x \\)** باستخدام جداء الجذور لفييت، وحساب **مجموع مكعبي العدد ومقلوبه** \\( x^3 + x^{-3} \\).",
            ),
        ],
        "extra_concept": concept(
            "4. Exponential Quadratics (t = aˣ) & Reciprocal Cube Powers",
            "٤. المعادلات الأسية التربيعية ومجموع المكعب والمقلوب",
            f"An equation of the form {m('a^{2x} - S a^x + P = 0')} becomes a quadratic {m('t^2 - St + P = 0')} under {m('t = a^x > 0')}. "
            f"If its two positive roots are {m('t_1 = a^{x_1}')} and {m('t_2 = a^{x_2}')}, then Vieta's product {m('t_1 t_2 = a^{x_1 + x_2} = P')} gives the **sum of exponents** {m('x_1 + x_2 = \\log_a(P)')} without even finding {m('t_1, t_2')}! "
            f"For reciprocal cubes, {m('x^3 + \\frac{1}{x^3} = \\left(x + \\frac{1}{x}\\right)^3 - 3\\left(x + \\frac{1}{x}\\right)')}.",
            f"تتحول المعادلة الأسية {m('a^{2x} - S a^x + P = 0')} بالتعويض {m('t = a^x > 0')} إلى المعادلة التربيعية {m('t^2 - St + P = 0')}. "
            f"وبضرب الجذرين الموجبين نجد {m('t_1 t_2 = a^{x_1 + x_2} = P')}، مما يعطي **مجموع الجذرين** {m('x_1 + x_2 = \\log_a(P)')} فوراً! "
            f"ولمجموع المكعب ومقلوبه استخدم المتطابقة {m('x^3 + \\frac{1}{x^3} = k^3 - 3k')} حيث {m('k = x + \\frac{1}{x}')}.",
            dm("t = a^x \\implies a^{x_1 + x_2} = t_1 t_2 = P, \\qquad x^3 + \\frac{1}{x^3} = \\left(x + \\frac{1}{x}\\right)^3 - 3\\left(x + \\frac{1}{x}\\right)"),
            f'<div class="eg-f-caption" dir="rtl">مجموع جذور المعادلة الأسية التربيعية ومتطابقة المكعب والمقلوب:</div>{dm("a^{x_1 + x_2} = t_1 t_2 = P, \\qquad x^3 + \\frac{1}{x^3} = k^3 - 3k")}',
            diagram_en=D.svg_algebra_flow([("k = x + 1/x", "Square: k² − 2"), ("Cube", "x³ + 1/x³"), ("Formula", "k³ − 3k")], ["x²", "x³"]),
            diagram_ar=D.svg_algebra_flow([("k = x + 1/x", "التربيع: k² − 2"), ("التكعيب", "x³ + 1/x³"), ("القانون", "k³ − 3k")], ["x²", "x³"]),
        ),
        "extra_traps": [
            (
                "Trap: Taking the **sum** \\( t_1 + t_2 = S \\) instead of the **product** \\( t_1 t_2 = P \\) when asked for \\( x_1 + x_2 \\) in \\( a^{2x} - S a^x + P = 0 \\) — adding exponents corresponds to **multiplying** powers \\( a^{x_1} a^{x_2} = a^{x_1+x_2} \\)!",
                "فخ شائع: استخدام مجموع الجذرين \\( t_1 + t_2 \\) بدلاً من **ضربهما** \\( t_1 t_2 = a^{x_1+x_2} \\) عند طلب مجموع الحلول \\( x_1 + x_2 \\) في المعادلة الأسية!",
            ),
            (
                "Trap: Writing \\( x^3 + \\frac{1}{x^3} = k^3 - 3 \\) instead of \\( k^3 - 3k \\) where \\( k = x + \\frac{1}{x} \\)!",
                "فخ شائع: كتابة \\( x^3 + \\frac{1}{x^3} = k^3 - 3 \\) بدلاً من الصيغة الصحيحة \\( k^3 - 3k \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Root-Distance Squared", "مربع المسافة بين الجذرين", r"\((r_1 - r_2)^2 = (r_1 + r_2)^2 - 4r_1 r_2\)", "Equals Δ / a² for ax² + bx + c = 0.", "يساوي المميز مقسوماً على a²."),
            cheat_item("Sum of Cubes Identity", "مجموع المكعبين", r"\(a^3 + b^3 = (a + b)^3 - 3ab(a + b)\)", "Express directly in terms of s = a+b and p = ab.", "بدلالة المجموع والجداء مباشرة."),
            cheat_item("Reciprocal Cube Sum", "مجموع المكعب ومقلوبه", r"\(x^3 + x^{-3} = k^3 - 3k\;\;(k = x + x^{-1})\)", "Here ab = x · (1/x) = 1.", "حالة خاصة حيث حاصل الضرب يساوي 1."),
            cheat_item("Exponential Vieta Product", "جداء فييت للمعادلة الأسية", r"\(a^{2x} - Sa^x + P = 0 \implies a^{x_1+x_2} = P\)", "Multiply t₁t₂ to add the exponents x₁ + x₂.", "اضرب الجذرين t₁t₂ لجمع الأسين x₁ + x₂."),
        ],
        "extra_examples": [
            worked_math_example(
                "L33-E5",
                "Solved Example 5 — Sum of Roots of an Exponential Quadratic",
                "مثال محلول ٥ — مجموع جذور معادلة أسية تربيعية",
                f"What is the sum of all real solutions {m('x')} to the exponential equation {m('9^x - 12 \\cdot 3^x + 27 = 0')}?",
                f"ما مجموع جميع الحلول الحقيقية {m('x')} للمعادلة الأسية {m('9^x - 12 \\cdot 3^x + 27 = 0')}؟",
                3, [2, 4, 9, 12],
                "Substitute \\( t = 3^x \\) to get \\( t^2 - 12t + 27 = 0 \\), then use Vieta's product \\( t_1 t_2 = 3^{x_1 + x_2} = 27 \\)!",
                [
                    f"Since {m('9^x = (3^x)^2')}, setting {m('t = 3^x')} transforms the equation into {m('t^2 - 12t + 27 = 0')}.",
                    f"This factors as {m('(t - 3)(t - 9) = 0')}, giving two positive roots {m('t_1 = 3')} and {m('t_2 = 9')}.",
                    f"Thus {m('3^{x_1 + x_2} = t_1 t_2 = 27 = 3^3')}, which yields {m('x_1 + x_2 = 3')}.",
                ],
                f"Individual roots are {m('x_1 = 1')} ({m('3^1 = 3')}) and {m('x_2 = 2')} ({m('3^2 = 9')}), summing to {m('1 + 2 = 3')}.",
                "عوّض \\( t = 3^x \\) لتحصل على \\( t^2 - 12t + 27 = 0 \\)، ثم استخدم جداء الجذرين \\( t_1 t_2 = 3^{x_1 + x_2} = 27 \\)!",
                [
                    f"بوضع {m('t = 3^x')} تصبح المعادلة {m('t^2 - 12t + 27 = 0')} وجذراها الموجبان {m('t_1 = 3')} و{m('t_2 = 9')}.",
                    f"حاصل ضرب الجذرين {m('3^{x_1 + x_2} = 27 = 3^3')}، ومنه {m('x_1 + x_2 = 3')}.",
                ],
                f"التحقق: الحلان هما {m('x = 1')} و{m('x = 2')} ومجموعهما {m(3)}.",
                diagram_en=D.svg_parabola_roots("t₁ = 3", "t₂ = 9", "3^(x₁+x₂) = 27"),
                diagram_ar=D.svg_parabola_roots("t₁ = 3", "t₂ = 9", "3^(x₁+x₂) = 27"),
            ),
            worked_math_example(
                "L33-E6",
                "Solved Example 6 — Reciprocal Cube Power Identity",
                "مثال محلول ٦ — حساب مجموع المكعب ومقلوبه",
                f"If {m('x')} is a positive real number such that {m('x + \\frac{1}{x} = 4')}, what is the exact value of {m('x^3 + \\frac{1}{x^3}')}?",
                f"إذا كان {m('x')} عدداً حقيقياً موجباً يحقق {m('x + \\frac{1}{x} = 4')}، فما القيمة الدقيقة للمقدار {m('x^3 + \\frac{1}{x^3}')}؟",
                52, [48, 56, 60, 64],
                "Apply the reciprocal cube identity \\( x^3 + \\frac{1}{x^3} = \\left(x + \\frac{1}{x}\\right)^3 - 3\\left(x + \\frac{1}{x}\\right) \\)!",
                [
                    f"Cube both sides of {m('x + \\frac{1}{x} = 4')}: {m('x^3 + 3x + \\frac{3}{x} + \\frac{1}{x^3} = 64')}.",
                    f"Factor the middle terms as {m('3\\left(x + \\frac{1}{x}\\right) = 3(4) = 12')}.",
                    f"Subtract {m(12)}: {m('x^3 + \\frac{1}{x^3} = 64 - 12 = 52')}.",
                ],
                f"Also {m('x^2 + x^{-2} = 4^2 - 2 = 14')}, and {m('(x + x^{-1})(x^2 - 1 + x^{-2}) = 4(14 - 1) = 52')}.",
                "طبّق متطابقة المكعب والمقلوب \\( k^3 - 3k \\) عند \\( k = 4 \\)!",
                [
                    f"بتكعيب الطرفين: {m('x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right) = 4^3 = 64')}.",
                    f"نعوّض {m('x + \\frac{1}{x} = 4')}: {m('x^3 + \\frac{1}{x^3} = 64 - 3(4) = 52')}.",
                ],
                f"التحقق: {m('4 \\times (14 - 1) = 52')}.",
                diagram_en=D.svg_algebra_flow([("k = x + 1/x = 4", "k³ = 64"), ("Subtract 3k", "64 − 3(4)"), ("Result", "x³ + 1/x³ = ?")], ["( )³", "−12"]),
                diagram_ar=D.svg_algebra_flow([("k = x + 1/x = 4", "k³ = 64"), ("اطرح 3k", "64 − 3(4)"), ("الناتج", "x³ + 1/x³ = ؟")], ["( )³", "−12"]),
            ),
        ],
    },

    "KMC-L3-04": {
        "extra_goals": [
            (
                "Solve **functional involution systems** by substituting \\( g(x) \\), compute the **area of a Manhattan diamond** \\( |x| + |y| \\le R \\), and **denest compound radicals** \\( \\sqrt{a \\pm 2\\sqrt{b}} \\).",
                "حل **أنظمة المعادلات الدالية الالتفافية** بالتعويض المزدوج، وحساب **مساحة معين القيمة المطلقة** \\( |x| + |y| \\le R \\)، و**تبسيط الجذور المتداخلة** \\( \\sqrt{a \\pm 2\\sqrt{b}} \\).",
            ),
        ],
        "extra_concept": concept(
            "4. Functional Involution Systems, Manhattan Diamonds & Denesting Radicals",
            "٤. الأنظمة الدالية الالتفافية، معين القيمة المطلقة، وتبسيط الجذور المركّبة",
            f"To solve {m('a f(x) + b f(g(x)) = h(x)')} where {m('g(g(x)) = x')} (such as {m('g(x) = 1 - x')} or {m('1/x')}), plug in {m('x')} and {m('g(x)')} to get a {m('2 \\times 2')} linear system for {m('f(x)')}. "
            f"The region {m('|x| + |y| \\le R')} is a tilted square (Manhattan diamond) with diagonals {m('2R')} and area {m('\\frac{1}{2}(2R)(2R) = 2R^2')}. "
            f"To denest {m('\\sqrt{a \\pm 2\\sqrt{b}}')}, find {m('u \\ge v > 0')} with {m('u + v = a')} and {m('uv = b')}, giving {m('\\sqrt{u} \\pm \\sqrt{v}')}!",
            f"لحل المعادلة الدالية {m('a f(x) + b f(g(x)) = h(x)')} حيث {m('g(g(x)) = x')} (مثل {m('1 - x')} أو {m('1/x')})، عوّض مرّة بـ {m('x')} ومرّة بـ {m('g(x)')} لتحصل على معادلتين خطيتين في {m('f(x)')}. "
            f"والمنطقة {m('|x| + |y| \\le R')} تمثّل مربعاً مائلاً (معيناً) طول كل من قطريه {m('2R')} ومساحته {m('2R^2')}. "
            f"ولتبسيط الجذر المركّب {m('\\sqrt{a \\pm 2\\sqrt{b}}')}، ابحث عن عددين {m('u \\ge v > 0')} مجموعهما {m('a')} وحاصل ضربهما {m('b')}، فيكون الناتج {m('\\sqrt{u} \\pm \\sqrt{v}')}!",
            dm("A_{\\{|x|+|y|\\le R\\}} = 2R^2, \\qquad \\sqrt{(u + v) \\pm 2\\sqrt{uv}} = \\sqrt{u} \\pm \\sqrt{v}\\;\\;(u \\ge v > 0)"),
            f'<div class="eg-f-caption" dir="rtl">مساحة معين القيمة المطلقة وقاعدة فك الجذر المزدوج:</div>{dm("A_{\\{|x|+|y|\\le R\\}} = 2R^2, \\qquad \\sqrt{(u + v) \\pm 2\\sqrt{uv}} = \\sqrt{u} \\pm \\sqrt{v}")}',
            diagram_en=D.svg_coord_diamond("R"),
            diagram_ar=D.svg_coord_diamond("R"),
        ),
        "extra_traps": [
            (
                "Trap: Writing \\( \\sqrt{a - 2\\sqrt{b}} = \\sqrt{v} - \\sqrt{u} < 0 \\) when \\( v < u \\) — the principal square root \\( \\sqrt{\\cdot} \\) is **always non-negative**, so put the larger radical first: \\( \\sqrt{u} - \\sqrt{v} \\)!",
                "فخ شائع: كتابة \\( \\sqrt{a - 2\\sqrt{b}} = \\sqrt{v} - \\sqrt{u} \\) بقيمة سالبة — الجذر التربيعي الرئيسي **غير سالب دائماً**، لذا ضع الأكبر أولاً \\( \\sqrt{u} - \\sqrt{v} \\)!",
            ),
            (
                "Trap: Computing the area of \\( |x| + |y| \\le R \\) as \\( 4R^2 \\) (the bounding square) instead of \\( 2R^2 \\) (half the bounding square)!",
                "فخ شائع: حساب مساحة المنطقة \\( |x| + |y| \\le R \\) على أنها \\( 4R^2 \\) بدلاً من \\( 2R^2 \\) (مساحة المعين المتعامد القطرين \\( \\frac{1}{2}(2R)(2R) = 2R^2 \\))!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Telescoping Surds", "مجموع الجذور التلسكوبي", r"\(\sum_{k=1}^{n-1}\frac{1}{\sqrt{k}+\sqrt{k+1}} = \sqrt{n} - 1\)", "Multiply numerator & denominator by √(k+1) − √k.", "اضرب في المرافق التربيعي."),
            cheat_item("Shifted Odd Symmetry", "تماثل الدالة الفردية المزاحة", r"\(f(x) = g_{\text{odd}}(x) + c \implies f(a)+f(-a) = 2c\)", "The odd part cancels out at x = ±a.", "الجزء الفردي يختصر عند جمع ±a."),
            cheat_item("Denesting Radicals", "فك الجذر المركّب", r"\(\sqrt{(u+v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v}\)", "Find u ≥ v > 0 with sum a and product b.", "ابحث عن عددين مجموعهما a وضربهما b."),
            cheat_item("Manhattan Diamond Area", "مساحة معين القيمة المطلقة", r"\(|x - h| + |y - k| \le R \implies \text{Area} = 2R^2\)", "Diagonals have length 2R each.", "طول كل قطر 2R والمساحة 2R²."),
        ],
        "extra_examples": [
            worked_math_example(
                "L34-E5",
                "Solved Example 5 — Solving a 2×2 Involution Functional Equation",
                "مثال محلول ٥ — حل معادلة دالية التفافية بالتعويض المزدوج",
                f"A function {m('f: \\mathbb{R} \\to \\mathbb{R}')} satisfies {m('2f(x) + f(1 - x) = 6x + 3')} for all real numbers {m('x')}. What is the value of {m('f(4)')}?",
                f"تحقق الدالة {m('f: \\mathbb{R} \\to \\mathbb{R}')} العلاقة {m('2f(x) + f(1 - x) = 6x + 3')} لجميع الأعداد الحقيقية {m('x')}. ما قيمة {m('f(4)')}؟",
                23, [15, 19, 21, 27],
                "Substitute \\( x = 4 \\) and \\( x = 1 - 4 = -3 \\) to get two linear equations in the two unknowns \\( f(4) \\) and \\( f(-3) \\)!",
                [
                    f"Plug in {m('x = 4')}: {m('2f(4) + f(-3) = 6(4) + 3 = 27')}.",
                    f"Plug in {m('x = -3')}: {m('2f(-3) + f(4) = 6(-3) + 3 = -15')}.",
                    f"Multiply the first equation by {m(2)} and subtract the second: {m('3f(4) = 2(27) - (-15) = 54 + 15 = 69 \\implies f(4) = 23')}.",
                ],
                f"Check with {m('f(x) = 6x - 1')}: {m('f(4) = 23')}, {m('f(-3) = -19')}, and {m('2(23) + (-19) = 27')}.",
                "عوّض \\( x = 4 \\) ثم \\( x = -3 \\) لتحصل على نظام معادلتين خطيتين في المجهولين \\( f(4) \\) و\\( f(-3) \\)!",
                [
                    f"عند {m('x = 4')}: {m('2f(4) + f(-3) = 27')}.",
                    f"وعند {m('x = -3')}: {m('2f(-3) + f(4) = -15')}.",
                    f"بضرب المعادلة الأولى في {m(2)} وطرح الثانية: {m('3f(4) = 54 - (-15) = 69 \\implies f(4) = 23')}.",
                ],
                f"التحقق: {m('f(4) = 23')} و{m('f(-3) = -19')} ويحققان {m('2(23) - 19 = 27')}.",
                diagram_en=D.svg_algebra_flow([("x = 4", "2f(4) + f(−3) = 27"), ("x = −3", "f(4) + 2f(−3) = −15"), ("Eliminate", "3f(4) = 69 → ?")], ["⇄", "÷3"]),
                diagram_ar=D.svg_algebra_flow([("x = 4", "2f(4) + f(−3) = 27"), ("x = −3", "f(4) + 2f(−3) = −15"), ("حذف", "3f(4) = 69 ← ؟")], ["⇄", "÷3"]),
            ),
            worked_math_example(
                "L34-E6",
                "Solved Example 6 — Denesting Paired Nested Square Roots",
                "مثال محلول ٦ — تبسيط الجذور التربيعية المتداخلة",
                f"What is the exact value of {m('\\left(\\sqrt{9 + 2\\sqrt{14}} - \\sqrt{9 - 2\\sqrt{14}}\\right)^2')}?",
                f"ما القيمة الدقيقة للمقدار {m('\\left(\\sqrt{9 + 2\\sqrt{14}} - \\sqrt{9 - 2\\sqrt{14}}\\right)^2')}؟",
                8, [4, 6, 10, 14],
                "Find two numbers with sum \\( 9 \\) and product \\( 14 \\) (namely \\( 7 \\) and \\( 2 \\)) to denest each radical into \\( \\sqrt{7} \\pm \\sqrt{2} \\)!",
                [
                    f"Since {m('7 + 2 = 9')} and {m('7 \\times 2 = 14')}, we have {m('\\sqrt{9 + 2\\sqrt{14}} = \\sqrt{7} + \\sqrt{2}')} and {m('\\sqrt{9 - 2\\sqrt{14}} = \\sqrt{7} - \\sqrt{2}')}.",
                    f"Subtracting gives {m('(\\sqrt{7} + \\sqrt{2}) - (\\sqrt{7} - \\sqrt{2}) = 2\\sqrt{2}')}.",
                    f"Squaring the result gives {m('(2\\sqrt{2})^2 = 8')}.",
                ],
                f"Direct squaring check: {m('(9+2\\sqrt{14}) + (9-2\\sqrt{14}) - 2\\sqrt{81 - 56} = 18 - 2(5) = 8')}.",
                "ابحث عن عددين مجموعهما \\( 9 \\) وحاصل ضربهما \\( 14 \\) (وهما \\( 7 \\) و\\( 2 \\)) لفك كل جذر إلى \\( \\sqrt{7} \\pm \\sqrt{2} \\)!",
                [
                    f"بما أن {m('7 + 2 = 9')} و{m('7 \\times 2 = 14')}، فإن {m('\\sqrt{9 \\pm 2\\sqrt{14}} = \\sqrt{7} \\pm \\sqrt{2}')}.",
                    f"الفرق بينهما يساوي {m('(\\sqrt{7} + \\sqrt{2}) - (\\sqrt{7} - \\sqrt{2}) = 2\\sqrt{2}')}.",
                    f"بتربيع الناتج نحصل على {m('(2\\sqrt{2})^2 = 8')}.",
                ],
                f"التحقق بالتربيع المباشر: {m('18 - 2\\sqrt{81 - 56} = 18 - 10 = 8')}.",
                diagram_en=D.svg_algebra_flow([("u+v=9, uv=14", "u = 7, v = 2"), ("Difference", "(√7+√2)−(√7−√2) = 2√2"), ("Square", "(2√2)² = ?")], ["√", "( )²"]),
                diagram_ar=D.svg_algebra_flow([("u+v=9, uv=14", "u = 7, v = 2"), ("الفرق", "(√7+√2)−(√7−√2) = 2√2"), ("التربيع", "(2√2)² = ؟")], ["√", "( )²"]),
            ),
        ],
    },

    "KMC-L3-05": {
        "extra_goals": [
            (
                "Apply **Power of a Point** (\\( PT^2 = PA \\cdot PB \\)), the **Angle Bisector Ratio Theorem**, and the **right-triangle inradius formula** \\( r = \\frac{a + b - c}{2} \\).",
                "تطبيق **قوة النقطة للمماس والقاطع** (\\( PT^2 = PA \\cdot PB \\))، و**مبرهنة منصف الزاوية**، وقانون **نصف قطر الدائرة الداخلية للمثلث القائم** \\( r = \\frac{a + b - c}{2} \\).",
            ),
        ],
        "extra_concept": concept(
            "4. Secant–Tangent Power of a Point, Angle Bisectors & Right-Triangle Inradius",
            "٤. قوة النقطة للمماس والقاطع، منصف الزاوية، والدائرة الداخلية للمثلث القائم",
            f"From an exterior point {m('P')}, a tangent {m('PT')} and secant {m('PAB')} to a circle satisfy {m('PT^2 = PA \\cdot PB')} (where {m('PB = PA + AB')} is the **entire** secant length!). "
            f"In {m('\\triangle ABC')}, the internal bisector {m('AD')} of {m('\\angle A')} divides {m('BC')} in the ratio of the adjacent sides: {m('\\frac{BD}{DC} = \\frac{AB}{AC}')}. "
            f"In a right triangle with legs {m('a, b')} and hypotenuse {m('c')}, the incircle has radius {m('r = \\frac{a + b - c}{2}')}.",
            f"من نقطة خارجية {m('P')}، يحقق المماس {m('PT')} والقاطع {m('PAB')} للدائرة العلاقة {m('PT^2 = PA \\cdot PB')} (حيث {m('PB = PA + AB')} هو طول القاطع **كاملاً**!). "
            f"وفي المثلث {m('\\triangle ABC')}، يقسم منصف الزاوية الداخلي {m('AD')} الضلع المقابل {m('BC')} بنسبة الضلعين المجاورين {m('\\frac{BD}{DC} = \\frac{AB}{AC}')}. "
            f"وفي المثلث القائم ذي الساقين {m('a, b')} والوتر {m('c')}، يُعطى نصف قطر الدائرة الداخلية بالقانون السريع {m('r = \\frac{a + b - c}{2}')}.",
            dm("PT^2 = PA \\cdot PB, \\qquad \\frac{BD}{DC} = \\frac{AB}{AC}, \\qquad r_{\\perp} = \\frac{a + b - c}{2}"),
            f'<div class="eg-f-caption" dir="rtl">قوة النقطة، مبرهنة منصف الزاوية، ونصف قطر الدائرة الداخلية للمثلث القائم:</div>{dm("PT^2 = PA \\cdot PB, \\qquad \\frac{BD}{DC} = \\frac{AB}{AC}, \\qquad r_{\\perp} = \\frac{a + b - c}{2}")}',
            diagram_en=D.svg_power_of_point("PT", "PA", "AB"),
            diagram_ar=D.svg_power_of_point("PT", "PA", "AB"),
        ),
        "extra_traps": [
            (
                "Trap: Multiplying the external part \\( PA \\) by the chord \\( AB \\) instead of the **whole secant** \\( PB = PA + AB \\) in \\( PT^2 = PA \\cdot PB \\)!",
                "فخ شائع: ضرب الجزء الخارجي \\( PA \\) في طول الوتر الداخلي \\( AB \\) بدلاً من **طول القاطع الكلي** \\( PB = PA + AB \\) في قانون قوة النقطة!",
            ),
            (
                "Trap: Scaling volume by \\( k^2 \\) instead of \\( k^3 \\) when all linear dimensions of a 3D solid are multiplied by \\( k \\)!",
                "فخ شائع: ضرب الحجم في \\( k^2 \\) بدلاً من \\( k^3 \\) عند مضاعفة الأبعاد الخطية لمجسم ثلاثي الأبعاد بمعامل \\( k \\)!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Power of a Point", "قوة النقطة", r"\(PT^2 = PA \cdot (PA + AB)\)", "Tangent² = External × Whole Secant.", "مربع المماس = الجزء الخارجي × القاطع الكلي."),
            cheat_item("Angle Bisector Theorem", "مبرهنة منصف الزاوية", r"\(\frac{BD}{DC} = \frac{AB}{AC}\)", "Base segments are proportional to adjacent sides.", "جزأا القاعدة متناسبان مع الضلعين المجاورين."),
            cheat_item("Right-Triangle Inradius", "نصف قطر الدائرة الداخلية للقائم", r"\(r = \frac{a + b - c}{2},\;\; R = \frac{c}{2}\)", "Thus r + R = (a + b)/2.", "وبالتالي فإن r + R = (a + b)/2."),
            cheat_item("Polygon Diagonal Crossings", "تقاطعات أقطار المضلع", r"\(I_{\max} = \binom{n}{4}\)", "Every 4 vertices determine 1 interior crossing.", "كل 4 رؤوس تحدد نقطة تقاطع داخلية وحيدة."),
        ],
        "extra_examples": [
            worked_math_example(
                "L35-E6",
                "Solved Example 6 — Right-Triangle Inradius & Circumradius Sum",
                "مثال محلول ٦ — نصفا قطري الدائرة الداخلية والمحيطة لمثلث قائم",
                f"A right triangle has legs of lengths {m(16)} and {m(30)}. What is the radius {m('r')} of the circle inscribed in this triangle?",
                f"مثلث قائم الزاوية طولا ضلعيه القائمين {m(16)} و{m(30)}. ما طول نصف قطر الدائرة المرسومة داخل هذا المثلث {m('r')} (الماسة لأضلاعه الثلاثة)؟",
                6, [4, 5, 7, 8],
                "Find the hypotenuse \\( c \\) using the \\( 8\\text{-}15\\text{-}17 \\) Pythagorean triple scaled by \\( 2 \\), then apply \\( r = \\frac{a + b - c}{2} \\)!",
                [
                    f"Since {m('(16, 30) = 2 \\times (8, 15)')}, the hypotenuse is {m('c = 2 \\times 17 = 34')}.",
                    f"For any right triangle, the inradius is {m('r = \\frac{a + b - c}{2}')}.",
                    f"Substitute {m('a = 16, b = 30, c = 34')}: {m('r = \\frac{16 + 30 - 34}{2} = \\frac{12}{2} = 6')}.",
                ],
                f"Area check: {m('[ABC] = \\frac{1}{2}(16)(30) = 240')} and semiperimeter {m('s = \\frac{16+30+34}{2} = 40')}, giving {m('r = \\frac{240}{40} = 6')}.",
                "أوجد طول الوتر \\( c \\) من ثلاثية فيثاغورس \\( (8, 15, 17) \\) مضروبةً في \\( 2 \\)، ثم طبّق القانون \\( r = \\frac{a + b - c}{2} \\)!",
                [
                    f"من ثلاثية فيثاغورس {m('2 \\times (8, 15, 17)')} نجد طول الوتر {m('c = 34')}.",
                    f"نصف قطر الدائرة الداخلية للمثلث القائم هو {m('r = \\frac{a + b - c}{2} = \\frac{16 + 30 - 34}{2} = 6')}.",
                ],
                f"التحقق بالمساحة: {m('r = \\frac{\\Delta}{s} = \\frac{240}{40} = 6')}.",
                diagram_en=D.svg_right_tri_incircle("16", "30", "34", "r = ?"),
                diagram_ar=D.svg_right_tri_incircle("16", "30", "34", "نق = ؟"),
            ),
        ],
    },

    "KMC-L3-06": {
        "extra_goals": [
            (
                "Count integer solutions via **Stars and Bars**, handle **circular seating & derangements \\( D_n \\)**, and evaluate **geometric interval/region probabilities**.",
                "عدّ الحلول الصحيحة بطريقة **النجوم والفواصل**، وحساب **التباديل الدائرية والتباديل الخالية من النقاط الثابتة \\( D_n \\)**، وإيجاد **الاحتمال الهندسي للمساحات والفترات**.",
            ),
        ],
        "extra_concept": concept(
            "4. Stars & Bars Partitions, Circular Seating & Derangements (D_n)",
            "٤. النجوم والفواصل، الجلوس الدائري، والتباديل بلا نقاط ثابتة",
            f"The equation {m('x_1 + x_2 + \\cdots + x_k = n')} has {m('\\binom{n - 1}{k - 1}')} solutions in **positive** integers ({m('x_i \\ge 1')}) and {m('\\binom{n + k - 1}{k - 1}')} solutions in **non-negative** integers ({m('x_i \\ge 0')}). "
            f"Around a circular table, {m('n')} people can sit in {m('(n - 1)!')} ways. "
            f"The number of **derangements** {m('D_n')} (permutations where no item stays in its original spot) satisfies {m('D_1 = 0,\\; D_2 = 1,\\; D_3 = 2,\\; D_4 = 9,\\; D_5 = 44')}.",
            f"عدد الحلول الصحيحة **الموجبة** ({m('x_i \\ge 1')}) للمعادلة {m('x_1 + \\cdots + x_k = n')} هو {m('\\binom{n - 1}{k - 1}')}، وعدد الحلول **غير السالبة** ({m('x_i \\ge 0')}) هو {m('\\binom{n + k - 1}{k - 1}')}. "
            f"وعلى طاولة دائرية يجلس {m('n')} أشخاص بـ {m('(n - 1)!')} طريقة. "
            f"وعدد **التباديل الخالية من النقاط الثابتة** {m('D_n')} يساوي {m('D_1 = 0,\\; D_2 = 1,\\; D_3 = 2,\\; D_4 = 9,\\; D_5 = 44')}.",
            dm("\\#\\{x_i \\ge 1\\} = \\binom{n - 1}{k - 1}, \\qquad \\#\\{x_i \\ge 0\\} = \\binom{n + k - 1}{k - 1}, \\qquad (D_3, D_4, D_5) = (2, 9, 44)"),
            f'<div class="eg-f-caption" dir="rtl">قانونا النجوم والفواصل وأعداد التباديل الخالية من النقاط الثابتة:</div>{dm("\\#\\{x_i \\ge 1\\} = \\binom{n - 1}{k - 1}, \\qquad \\#\\{x_i \\ge 0\\} = \\binom{n + k - 1}{k - 1}, \\qquad (D_3, D_4, D_5) = (2, 9, 44)")}',
            diagram_en=D.svg_round_table(6, highlight_adj=True),
            diagram_ar=D.svg_round_table(6, highlight_adj=True),
        ),
        "extra_traps": [
            (
                "Trap: Using \\( \\binom{n+k-1}{k-1} \\) when the problem asks for **positive** integers \\( x_i \\ge 1 \\) (or vice versa when \\( x_i \\ge 0 \\) is allowed)!",
                "فخ شائع: الخلط بين صيغة الأعداد الصحيحة **الموجبة** \\( \\binom{n-1}{k-1} \\) وصيغة الأعداد **غير السالبة** \\( \\binom{n+k-1}{k-1} \\) التي تسمح بالصفر!",
            ),
            (
                "Trap: Using \\( n! \\) instead of \\( (n - 1)! \\) for circular table arrangements where rotations are considered identical!",
                "فخ شائع: استعمال \\( n! \\) بدلاً من \\( (n - 1)! \\) عند ترتيب \\( n \\) أشخاص حول طاولة دائرية!",
            ),
        ],
        "cheat_sheet": [
            cheat_item("Complementary Counting", "العدّ بالمتمم", r"\(N_{\text{valid}} = N_{\text{total}} - N_{\text{forbidden}}\)", "Subtract forbidden committees/triangles from total.", "اطرح الحالات الممنوعة من العدد الكلي."),
            cheat_item("Stars & Bars", "النجوم والفواصل", r"\(x_i \ge 1:\;\binom{n-1}{k-1}, \quad x_i \ge 0:\;\binom{n+k-1}{k-1}\)", "Place (k−1) dividers among stars.", "ضع (k−1) فاصلاً بين النجوم."),
            cheat_item("Circular Seating", "الترتيب الدائري", r"\((n - 1)!\text{ total}, \quad 2!\cdot(n - 2)!\text{ pair together}\)", "Bundle an adjacent pair as 1 unit first.", "اربط الزوج المتجاور ككتلة واحدة أولاً."),
            cheat_item("Derangements D_n", "التباديل بلا نقاط ثابتة", r"\(D_3 = 2,\;\; D_4 = 9,\;\; D_5 = 44\)", "Memorize D₁..D₅ for instant KMC speed.", "احفظ قيم D₁..D₅ للحل الفوري."),
        ],
        "extra_examples": [
            worked_math_example(
                "L36-E6",
                "Solved Example 6 — Stars and Bars with Positive Integer Constraints",
                "مثال محلول ٦ — توزيع العناصر بطريقة النجوم والفواصل",
                f"How many ordered quadruples of **positive integers** {m('(a, b, c, d)')} satisfy {m('a + b + c + d = 11')}?",
                f"كم رباعية مرتبة من **الأعداد الصحيحة الموجبة** {m('(a, b, c, d)')} تحقق المعادلة {m('a + b + c + d = 11')}؟",
                120, [84, 110, 165, 330],
                "For \\( k = 4 \\) positive integers summing to \\( n = 11 \\), place \\( 4 - 1 = 3 \\) dividers among \\( 11 - 1 = 10 \\) internal gaps!",
                [
                    f"Since {m('a, b, c, d \\ge 1')} are positive integers, apply the Stars and Bars formula {m('\\binom{n - 1}{k - 1}')} with {m('n = 11')} and {m('k = 4')}.",
                    f"This gives {m('\\binom{11 - 1}{4 - 1} = \\binom{10}{3}')}.",
                    f"Evaluate {m('\\binom{10}{3} = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120')}.",
                ],
                f"Check: {m('10 \\times 3 \\times 4 = 120')}.",
                "لأربعة أعداد صحيحة موجبة مجموعها \\( 11 \\)، ضع \\( 4 - 1 = 3 \\) فواصل في \\( 11 - 1 = 10 \\) فجوات داخلية!",
                [
                    f"بما أن المتغيرات الأربعة أعداد صحيحة موجبة ({m('\\ge 1')})، نطبق القانون {m('\\binom{n - 1}{k - 1}')} عند {m('n = 11')} و{m('k = 4')}.",
                    f"عدد الرباعيات = {m('\\binom{10}{3} = \\frac{10 \\times 9 \\times 8}{6} = 120')}.",
                ],
                f"التحقق: {m('\\binom{10}{3} = 120')}.",
                diagram_en=D.svg_digit_cards(["a ≥ 1", "b ≥ 1", "c ≥ 1", "d ≥ 1"], "a+b+c+d = 11", "C(10, 3) = ?"),
                diagram_ar=D.svg_digit_cards(["a ≥ 1", "b ≥ 1", "c ≥ 1", "d ≥ 1"], "a+b+c+d = 11", "C(10, 3) = ؟"),
            ),
        ],
    },
}
