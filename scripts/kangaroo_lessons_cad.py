"""Bilingual Study Lessons for Kangaroo Math Competition — Cadet Division (Grades 7–8)."""
from fractions import Fraction

from kangaroo_common import (
    dm,
    kang_concept,
    kang_worked_example,
    m,
    make_kangaroo_lesson,
    svg_balance_scales,
    svg_bar_chart,
    svg_binary_bulbs,
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digit_slots,
    svg_factor_tree,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_kang_cube_faces,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_polyomino_board,
    svg_midpoint_square_shaded,
    svg_motion_timeline,
    svg_number_strip,
    svg_painted_cube_3d,
    svg_parallel_zigzag,
    svg_spinner,
    svg_square_circle_shaded,
    svg_street_grid,
    svg_subdivided_rect_2x2,
    svg_two_jars,
    svg_venn_3,
)

LEVEL = "Cadet"


def _lesson_3_1() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-01",
        level=LEVEL,
        unit_num="Lesson 3.1",
        topic="Number Theory",
        title_en="Prime Factorizations, GCD/LCM Puzzles, Digit Sums & Power Last Digits",
        title_ar="التحليل إلى عوامل أولية وألغاز القاسم والمضاعف ومجموع الأرقام وآحاد القوى",
        summary_en=(
            "Unlock Grade 7–8 Kangaroo number puzzles without brute-force arithmetic: pair up prime "
            "exponents to build squares and cubes, link GCD and LCM through coprime ratios, decode "
            "reversed multi-digit numbers with place-value algebra, and spot 4-step cycles in giant powers."
        ),
        summary_ar=(
            "حلّ ألغاز الأعداد لمستوى كاديت (الصفين 7–8) في مسابقة الكانجارو بذكاء ودون حسابات مطوّلة: "
            "زاوج أسس العوامل الأولية لتكوين المربعات والمكعبات الكاملة، واربط القاسم المشترك الأكبر بالمضاعف "
            "المشترك الأصغر، وفكّ شفرة الأعداد المعكوسة بالقيمة المكانية، واكتشف دورة الآحاد الرباعية للقوى الكبيرة."
        ),
        goals_en=[
            "Use prime factorizations to build **perfect squares and cubes** and count positive divisors rapidly.",
            "Solve **GCD and LCM pair puzzles** using \\( a = g x,\\; b = g y \\) with \\( \\gcd(x, y) = 1 \\).",
            "Translate reversed 2-digit and 3-digit numbers into clean multiples of **9, 11, and 99**.",
            "Find the **units digit** of large exponential sums and products via 4-step remainder cycles.",
        ],
        goals_ar=[
            "توظيف التحليل إلى العوامل الأولية لتكوين **المربعات والمكعبات الكاملة** وحساب عدد القواسم بسرعة.",
            "حلّ ألغاز **القاسم المشترك الأكبر والمضاعف المشترك الأصغر** بكتابة \\( a = g x,\\; b = g y \\) مع \\( \\gcd(x, y) = 1 \\).",
            "تحويل الأعداد المعكوسة المكوّنة من رقمين أو ثلاثة أرقام إلى مضاعفات أنيقة للأعداد **9 و11 و99**.",
            "إيجاد **رقم الآحاد** لمجاميع وجداءات القوى الكبيرة باستخدام دورات البواقي الرباعية.",
        ],
        concepts=[
            kang_concept(
                "1. Prime Exponents, Perfect Squares & Coprime GCD–LCM Pairs",
                "١. أسس العوامل الأولية والمربعات الكاملة وثنائيات القاسم والمضاعف",
                f"Every integer greater than {m(1)} factors uniquely into primes: {m('N = p_1^{e_1} p_2^{e_2} \\cdots')}. "
                f"In a **perfect square**, every prime exponent {m('e_i')} is **even**; in a **perfect cube**, every exponent "
                f"is a multiple of {m(3)}. For two integers {m('a')} and {m('b')} with {m('g = \\gcd(a,b)')}, write "
                f"{m('a = g x')} and {m('b = g y')} where {m('\\gcd(x,y) = 1')}; then {m('\\operatorname{lcm}(a,b) = g x y')} "
                f"and {m('a \\cdot b = g \\cdot \\operatorname{lcm}(a,b)')}.",
                f"كل عدد صحيح أكبر من {m(1)} يتحلل بطريقة وحيدة إلى عوامله الأولية: {m('N = p_1^{e_1} p_2^{e_2} \\cdots')}. "
                f"في **المربع الكامل** يكون كل أسّ أولي {m('e_i')} **زوجياً**، وفي **المكعب الكامل** يكون من مضاعفات {m(3)}. "
                f"ولأي عددين {m('a')} و{m('b')} قاسمهما المشترك الأكبر {m('g = \\gcd(a,b)')}، اكتب {m('a = g x')} و{m('b = g y')} "
                f"بحيث {m('\\gcd(x,y) = 1')}؛ فيكون {m('\\operatorname{lcm}(a,b) = g x y')} وكذلك {m('a \\cdot b = g \\cdot \\operatorname{lcm}(a,b)')}.",
                dm("N = p_1^{e_1} p_2^{e_2} \\text{ square} \\iff 2 \\mid e_i, \\qquad a = gx,\\; b = gy \\implies \\operatorname{lcm}(a,b) = gxy"),
                "شرط المربع الكامل وعلاقة القاسم والمضاعف:",
                dm("2 \\mid e_i, \\qquad \\gcd(a,b)\\cdot\\operatorname{lcm}(a,b) = a\\cdot b"),
                diagram_en=svg_factor_tree("504", "8", "63", "9", "7"),
            ),
            kang_concept(
                "2. Place-Value Algebra & Digit-Reversal Shortcuts",
                "٢. جبر القيمة المكانية واختصارات عكس الأرقام",
                f"Kangaroo loves hiding algebra inside digits! Write a 2-digit number {m('\\overline{ab}')} as {m('10a + b')} "
                f"and a 3-digit number {m('\\overline{abc}')} as {m('100a + 10b + c')}. Subtracting its reversal cancels the "
                f"middle digit completely: {m('\\overline{ab} - \\overline{ba} = 9(a - b)')} and "
                f"{m('\\overline{abc} - \\overline{cba} = 99(a - c)')}! Also remember that any integer leaves the **same remainder "
                f"modulo 9** as the sum of its digits.",
                f"تعشق مسابقة الكانجارو إخفاء الجبر داخل خانات الأرقام! اكتب العدد الثنائي {m('\\overline{ab}')} على الصورة {m('10a + b')} "
                f"والعدد الثلاثي {m('\\overline{abc}')} على الصورة {m('100a + 10b + c')}. عند طرح مقلوب العدد تختفي الخانة الوسطى تماماً: "
                f"{m('\\overline{ab} - \\overline{ba} = 9(a - b)')} وكذلك {m('\\overline{abc} - \\overline{cba} = 99(a - c)')}! "
                f"وتذكّر دائماً أن باقي قسمة أي عدد على {m(9)} يساوي باقي قسمة **مجموع أرقامه** على {m(9)}.",
                dm("\\overline{ab} + \\overline{ba} = 11(a+b), \\qquad \\overline{abc} - \\overline{cba} = 99(a-c)"),
                "متطابقات جمع وطرح الأعداد المعكوسة:",
                dm("\\overline{ab} + \\overline{ba} = 11(a+b), \\qquad \\overline{abc} - \\overline{cba} = 99(a-c)"),
                diagram_en=svg_digit_slots(["a", "b", "c"], "abc − cba = 99(a − c)"),
                diagram_ar=svg_digit_slots(["a", "b", "c"], "abc − cba = 99(a − c)"),
            ),
            kang_concept(
                "3. Units-Digit Cycles of Giant Powers",
                "٣. دورة رقم الآحاد للقوى العملاقة",
                f"Only the **units digit of the base** affects the units digit of {m('A^n')}. Digits {m('0, 1, 5, 6')} stay "
                f"fixed forever; {m('4')} and {m('9')} alternate every {m(2)} powers; and {m('2, 3, 7, 8')} repeat in clean "
                f"**cycles of length 4** (for example, {m('7^n')} cycles through {m('7, 9, 3, 1')}). Divide the exponent {m('n')} "
                f"by {m(4)}: remainders {m('1, 2, 3')} pick the 1st, 2nd, or 3rd cycle entry, while remainder {m(0)} picks the **4th** entry!",
                f"وحدها **خانة الآحاد في الأساس** تحدّد رقم آحاد القوة {m('A^n')}. الأرقام {m('0, 1, 5, 6')} تبقى ثابتة دائماً، "
                f"والرقمان {m('4, 9')} يتناوبان في دورة طولها {m(2)}، بينما الأرقام {m('2, 3, 7, 8')} تتكرر في **دورة رباعية** منتظمة "
                f"(مثلاً قوى {m(7)} تدور عبر {m('7, 9, 3, 1')}). اقسم الأس {m('n')} على {m(4)}: البواقي {m('1, 2, 3')} تعطي الحد الأول أو "
                f"الثاني أو الثالث، أما الباقي {m(0)} فيعطي الحد **الرابع** في الدورة!",
                dm("2^n \\bmod 10:\\;(2,4,8,6), \\quad 3^n:\\;(3,9,7,1), \\quad 7^n:\\;(7,9,3,1), \\quad 8^n:\\;(8,4,2,6)"),
                "الدورات الرباعية لأرقام الآحاد:",
                dm("2^n:(2,4,8,6), \\quad 3^n:(3,9,7,1), \\quad 7^n:(7,9,3,1), \\quad 8^n:(8,4,2,6)"),
                diagram_en=svg_function_machine("Base^n", "n mod 4", "Cycle[r]", "Last Digit"),
                diagram_ar=svg_function_machine("Base^n", "باقي n÷4", "الحد بالدورة", "رقم الآحاد"),
            ),
        ],
        traps_en=[
            "Trap: Picking non-coprime factor pairs in GCD/LCM problems! If \\( \\gcd(a,b)=12 \\) and \\( xy = 15 \\) looks clean, remember that for \\( xy = 12 \\), the pair \\( (2,6) \\) is **invalid** because \\( \\gcd(2,6) = 2 \\neq 1 \\).",
            "Trap: Treating remainder \\( 0 \\) modulo \\( 4 \\) as power \\( 0 \\) (giving \\( 1 \\) for even bases)! Actually \\( 2^{40} \\) ends in the 4th term of \\( (2, 4, 8, 6) \\), which is **6**, never \\( 1 \\).",
            "Trap: Forgetting that the leading digit of an \\( n \\)-digit number cannot be zero! When reversing \\( \\overline{abc} \\) into another 3-digit number \\( \\overline{cba} \\), both \\( a \\ge 1 \\) and \\( c \\ge 1 \\) must hold.",
        ],
        traps_ar=[
            "فخ شائع: اختيار عوامل غير أولية نسبياً في مسائل القاسم والمضاعف! إذا كان \\( x y = 12 \\)، فالزوج \\( (2,6) \\) **مرفوض** لأن \\( \\gcd(2,6) = 2 \\neq 1 \\) فيغيّر القاسم المشترك الأكبر.",
            "فخ شائع: اعتبار باقي القسمة \\( 0 \\) على \\( 4 \\) كأنه أسّ صفري يعطي \\( 1 \\) للأساسات الزوجية! في الحقيقة \\( 2^{40} \\) ينتهي بالحد الرابع من \\( (2, 4, 8, 6) \\) وهو **6** وليس \\( 1 \\).",
            "فخ شائع: نسيان أن الخانة اليسرى لأي عدد مكوّن من \\( n \\) أرقام لا تساوي صفراً! إذا كان مقلوب \\( \\overline{abc} \\) عدداً من 3 أرقام أيضاً فيجب أن يتحقق \\( a \\ge 1 \\) و\\( c \\ge 1 \\).",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-01-EX1",
                "Worked Example 1 — Completing a Perfect Square",
                "مثال محلول ١ — إكمال المربع الكامل بالعوامل الأولية",
                f"What is the smallest positive integer {m('k')} such that {m('504 \\times k')} is a perfect square?",
                f"ما أصغر عدد صحيح موجب {m('k')} يجعل حاصل الضرب {m('504 \\times k')} مربعاً كاملاً؟",
                14,
                [7, 12, 21, 42],
                "Factor \\( 504 \\) into primes and multiply one copy of each prime whose exponent is odd.",
                [
                    f"Break {m(504)} into primes: {m('504 = 8 \\times 63 = 2^3 \\times 3^2 \\times 7^1')}.",
                    f"For {m('504 \\times k')} to be a perfect square, every prime exponent must become **even**.",
                    f"Here {m('3^2')} already has an even exponent, while {m('2^3')} and {m('7^1')} have odd exponents.",
                    f"Supply one factor of {m(2)} and one factor of {m(7)}: {m('k = 2 \\times 7 = 14')}.",
                ],
                f"{m('504 \\times 14 = 7056 = (2^2 \\times 3 \\times 7)^2 = 84^2')}, a perfect square!",
                "حلّل \\( 504 \\) إلى عوامله الأولية واضرب في نسخة واحدة من كل عامل أولي أسّه فردي.",
                [
                    f"نحلّل العدد {m(504)} إلى عوامله الأولية: {m('504 = 8 \\times 63 = 2^3 \\times 3^2 \\times 7^1')}.",
                    f"لكي يصبح {m('504 \\times k')} مربعاً كاملاً يجب أن تصبح جميع أسس العوامل الأولية **زوجية**.",
                    f"العامل {m('3^2')} أسّه زوجي جاهز، بينما {m('2^3')} و{m('7^1')} أسّاهما فرديان.",
                    f"نضرب في عامل واحد من {m(2)} وعامل واحد من {m(7)} فنحصل على أصغر قيمة: {m('k = 2 \\times 7 = 14')}.",
                ],
                f"تحقق: {m('504 \\times 14 = 7056 = 84^2')} وهو مربع كامل فعلاً!",
                diagram_en=svg_factor_tree("504", "8", "63", "9", "7"),
            ),
            kang_worked_example(
                "KANG-L3-01-EX2",
                "Worked Example 2 — GCD & LCM Coprime Pair",
                "مثال محلول ٢ — ثنائية القاسم المشترك الأكبر والمضاعف المشترك الأصغر",
                f"Two positive integers {m('a < b')} satisfy {m('\\gcd(a, b) = 12')} and {m('\\operatorname{lcm}(a, b) = 180')}. If neither integer divides the other, what is {m('a + b')}?",
                f"عددان صحيحان موجبان {m('a < b')} يحققان {m('\\gcd(a, b) = 12')} و{m('\\operatorname{lcm}(a, b) = 180')}. إذا لم يكن أيٌّ منهما قاسماً للآخر، فما قيمة {m('a + b')}؟",
                96,
                [72, 84, 108, 192],
                "Set \\( a = 12x \\) and \\( b = 12y \\) with \\( \\gcd(x, y) = 1 \\), then solve \\( 12xy = 180 \\).",
                [
                    f"Write {m('a = 12x')} and {m('b = 12y')} where {m('x < y')} and {m('\\gcd(x, y) = 1')}.",
                    f"Then {m('\\operatorname{lcm}(a, b) = 12xy = 180')}, which gives {m('xy = 15')}.",
                    f"The coprime factor pairs of {m(15)} with {m('x < y')} are {m('(1, 15)')} and {m('(3, 5)')}.",
                    f"Pair {m('(1, 15)')} gives {m('(12, 180)')}, where {m(12)} divides {m(180)}. So we must pick {m('(3, 5)')}, giving {m('a = 36')}, {m('b = 60')}, and {m('a + b = 96')}.",
                ],
                f"{m('\\gcd(36, 60) = 12')}, {m('\\operatorname{lcm}(36, 60) = 180')}, and {m('36 \\nmid 60')}. Sum = {m(96)}!",
                "ضع \\( a = 12x \\) و\\( b = 12y \\) مع \\( \\gcd(x, y) = 1 \\)، ثم حلّ المعادلة \\( 12xy = 180 \\).",
                [
                    f"نكتب {m('a = 12x')} و{m('b = 12y')} حيث {m('x < y')} و{m('\\gcd(x, y) = 1')}.",
                    f"إذن {m('\\operatorname{lcm}(a, b) = 12xy = 180')} ومنها {m('xy = 15')}.",
                    f"أزواج العوامل الأولية نسبياً للعدد {m(15)} مع {m('x < y')} هي {m('(1, 15)')} و{m('(3, 5)')}.",
                    f"الزوج {m('(1, 15)')} يعطي {m('(12, 180)')} حيث يقسم أحدهما الآخر، لذا نختار {m('(3, 5)')} فنحصل على {m('a = 36')} و{m('b = 60')} ومجموعهما {m('a + b = 96')}.",
                ],
                f"تحقق: {m('\\gcd(36, 60) = 12')} و{m('\\operatorname{lcm}(36, 60) = 180')} ومجموعهما {m(96)}!",
                diagram_en=svg_number_strip(["gcd=12", "a=12x", "b=12y", "lcm=180"]),
            ),
            kang_worked_example(
                "KANG-L3-01-EX3",
                "Worked Example 3 — Reversed 3-Digit Kangaroo Code",
                "مثال محلول ٣ — شفرة الكانجارو الثلاثية المعكوسة",
                f"A 3-digit ticket number {m('\\overline{abc}')} satisfies {m('\\overline{abc} - \\overline{cba} = 594')}, its middle digit is {m('b = 4')}, and the sum of its digits is {m('a + b + c = 16')}. What is {m('\\overline{abc}')}?",
                f"رقم تذكرة ثلاثي الخانات {m('\\overline{abc}')} يحقق {m('\\overline{abc} - \\overline{cba} = 594')}، ورقمه الأوسط {m('b = 4')}، ومجموع أرقامه {m('a + b + c = 16')}. ما قيمة العدد {m('\\overline{abc}')}؟",
                943,
                [842, 741, 934, 844],
                "Use \\( \\overline{abc} - \\overline{cba} = 99(a - c) \\) to find \\( a - c \\), then combine with \\( a + c \\).",
                [
                    f"By place value, {m('(100a + 10b + c) - (100c + 10b + a) = 99(a - c) = 594')}.",
                    f"Divide both sides by {m(99)}: {m('a - c = 6')}.",
                    f"Since {m('b = 4')} and {m('a + b + c = 16')}, we also have {m('a + c = 12')}.",
                    f"Adding {m('a - c = 6')} and {m('a + c = 12')} gives {m('2a = 18 \\implies a = 9')} and {m('c = 3')}, so {m('\\overline{abc} = 943')}.",
                ],
                f"{m('943 - 349 = 594')} and {m('9 + 4 + 3 = 16')}. Exact match!",
                "استخدم المتطابقة \\( \\overline{abc} - \\overline{cba} = 99(a - c) \\) لإيجاد \\( a - c \\) ثم اجمعها مع \\( a + c \\).",
                [
                    f"من القيمة المكانية نجد {m('(100a + 10b + c) - (100c + 10b + a) = 99(a - c) = 594')}.",
                    f"بقسمة الطرفين على {m(99)} نحصل على {m('a - c = 6')}.",
                    f"وبما أن {m('b = 4')} و{m('a + b + c = 16')}، فإن {m('a + c = 12')}.",
                    f"بجمع المعادلتين نجد {m('2a = 18 \\implies a = 9')} ومنها {m('c = 3')}، فيكون العدد {m('943')}.",
                ],
                f"تحقق: {m('943 - 349 = 594')} ومجموع الأرقام {m('9 + 4 + 3 = 16')}!",
                diagram_en=svg_digit_slots(["a", "4", "c"], "abc − cba = 594"),
                diagram_ar=svg_digit_slots(["a", "4", "c"], "abc − cba = 594"),
            ),
            kang_worked_example(
                "KANG-L3-01-EX4",
                "Worked Example 4 — Units Digit of a Power Sum",
                "مثال محلول ٤ — رقم الآحاد لمجموع قوتين كبيرتين",
                f"What is the units digit of {m('2027^{55} + 2028^{42}')}?",
                f"ما رقم الآحاد للمقدار {m('2027^{55} + 2028^{42}')}؟",
                7,
                [1, 3, 5, 9],
                "Keep only the units digits \\( 7^{55} \\) and \\( 8^{42} \\), then reduce both exponents modulo \\( 4 \\).",
                [
                    f"The units digit of {m('2027^{55}')} equals the units digit of {m('7^{55}')}. Powers of {m(7)} end in the 4-cycle {m('(7, 9, 3, 1)')}.",
                    f"Since {m('55 = 4 \\times 13 + 3')} leaves remainder {m(3)}, {m('7^{55}')} ends in the 3rd term: {m(3)}.",
                    f"The units digit of {m('2028^{42}')} equals the units digit of {m('8^{42}')}. Powers of {m(8)} end in {m('(8, 4, 2, 6)')}.",
                    f"Since {m('42 = 4 \\times 10 + 2')} leaves remainder {m(2)}, {m('8^{42}')} ends in the 2nd term: {m(4)}. Adding gives {m('3 + 4 = 7')}.",
                ],
                f"{m('3 + 4 = 7 < 10')}, so the final units digit is {m(7)}.",
                "احتفظ برقم الآحاد فقط لكل أساس (\\( 7^{55} \\) و\\( 8^{42} \\))، ثم احسب باقي قسمة كل أسّ على \\( 4 \\).",
                [
                    f"آحاد {m('2027^{55}')} هو نفسه آحاد {m('7^{55}')}، ودورة آحاد قوى {m(7)} هي {m('(7, 9, 3, 1)')}.",
                    f"بما أن {m('55 = 4 \\times 13 + 3')} باقيها {m(3)}، فإن آحاد {m('7^{55}')} هو الحد الثالث أي {m(3)}.",
                    f"وآحاد {m('2028^{42}')} هو آحاد {m('8^{42}')}، ودورة آحاد قوى {m(8)} هي {m('(8, 4, 2, 6)')}.",
                    f"بما أن {m('42 = 4 \\times 10 + 2')} باقيها {m(2)}، فإن آحاد {m('8^{42}')} هو الحد الثاني أي {m(4)}، والمجموع {m('3 + 4 = 7')}.",
                ],
                f"تحقق: {m('3 + 4 = 7')}، إذن رقم الآحاد هو {m(7)}.",
                diagram_en=svg_function_machine("7^55 + 8^42", "rem 3 & 2", "3 + 4", "7"),
            ),
        ],
        blueprints=[
            "kang_cad_prime_factor_squares",
            "kang_cad_gcd_lcm_product",
            "kang_cad_digit_sum_reversal",
            "kang_cad_power_units_cycle",
        ],
    )


def _lesson_3_2() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-02",
        level=LEVEL,
        unit_num="Lesson 3.2",
        topic="Algebra",
        title_en="Smart Ratios & Mixtures, Round-Trip Average Speed, Age Shifts & Telescoping Sums",
        title_ar="النسب والخلطات الذكية والسرعة المتوسطة ذهاباً وإياباً وفروق الأعمار والمجاميع المتداخلة",
        summary_en=(
            "Master Cadet-level algebraic thinking through invariants: keep total units constant when pouring "
            "between jars, compute round-trip speeds with the harmonic mean, solve symmetric balance and age "
            "systems by adding and subtracting equations, and collapse long fraction chains via telescoping."
        ),
        summary_ar=(
            "أتقن التفكير الجبري لمستوى كاديت عبر الثوابت الذكية: وحّد مجموع الأجزاء عند نقل السوائل بين الوعاءين، "
            "واحسب السرعة المتوسطة ذهاباً وإياباً بالمتوسط التوافقي، وحلّ أنظمة الموازين والأعمار بجمع وطرح المعادلات، "
            "واختصر سلاسل الكسور الطويلة بالحذف المتداخل."
        ),
        goals_en=[
            "Track **invariants** (constant total volume or constant age difference) to turn ratio shifts into 1-step arithmetic.",
            "Apply the **harmonic mean** \\( \\frac{2 v_1 v_2}{v_1 + v_2} \\) for equal-distance round trips instead of averaging speeds.",
            "Solve **symmetric linear systems** of weights, coins, and ages by adding and subtracting whole equations.",
            "Collapse long **telescoping sums and products** such as \\( \\sum \\frac{1}{k(k+1)} \\) and \\( \\prod (1 \\pm \\frac{1}{k}) \\).",
        ],
        goals_ar=[
            "تتبّع **الثوابت الرياضية** (ثبات الحجم الكلي أو ثبات فرق العمر) لتحويل تغيّر النسب إلى خطوة حسابية واحدة.",
            "تطبيق **المتوسط التوافقي** \\( \\frac{2 v_1 v_2}{v_1 + v_2} \\) لرحلات الذهاب والإياب المتساوية المسافة بدلاً من المتوسط الحسابي.",
            "حلّ **الأنظمة الخطية المتماثلة** للأوزان والعملات والأعمار بجمع المعادلات وطرحها مباشرة.",
            "اختصار **المجاميع والجداءات المتداخلة** الطويلة مثل \\( \\sum \\frac{1}{k(k+1)} \\) و\\( \\prod (1 \\pm \\frac{1}{k}) \\).",
        ],
        concepts=[
            kang_concept(
                "1. Ratio Transfers & Mixture Invariants",
                "١. نقل النسب وثابت المجموع في الخلطات",
                f"When liquid is poured from Jar A to Jar B without spilling, the **total volume stays constant**! "
                f"Scale the before-ratio and after-ratio so both have the **same total number of parts** (using their LCM). "
                f"Similarly, when water evaporates from fruit or salt water, the **dry/pure solute mass** never changes—anchor "
                f"your calculation on the unchanged quantity!",
                f"عند صبّ سائل من الوعاء (أ) إلى الوعاء (ب) دون انسكاب، يبقى **الحجم الكلي ثابتاً**! وحّد مجموع أجزاء النسبة قبل الصبّ "
                f"وبعده باستخدام المضاعف المشترك الأصغر لمجموعَي الأجزاء. وبالمثل، عند تبخّر الماء من الفاكهة أو المحلول الملحي تبقى "
                f"**كتلة المادة الجافة أو الملح النقي ثابتة** تماماً، فاجعلها دائماً نقطة ارتكازك!",
                dm("A:B = 5:3 = 10:6 \\;(\\text{sum }16) \\xrightarrow{-3\\text{ parts}} 7:9 \\;(\\text{sum }16)"),
                "توحيد مجموع الأجزاء قبل النقل وبعده:",
                dm("5:3 = 10:6 \\;(\\text{مجموع }16) \\longrightarrow 7:9 \\;(\\text{مجموع }16)"),
                diagram_en=svg_two_jars("A (5:3)", 0.68, "B", 0.42, "pour k mL"),
                diagram_ar=svg_two_jars("أ (5:3)", 0.68, "ب", 0.42, "نقل k مل"),
            ),
            kang_concept(
                "2. Equal-Distance Average Speed (Harmonic Mean) & Age Shifts",
                "٢. السرعة المتوسطة ذهاباً وإياباً وفروق الأعمار الثابتة",
                f"Average speed is ALWAYS **total distance divided by total time**, never the average of the two speeds "
                f"(because you spend MORE time moving at the slower speed!). Pick a smart distance {m('D = \\operatorname{lcm}(v_1, v_2)')} "
                f"or use {m('v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}')}. In age puzzles, the **age difference** between two "
                f"people is constant every year, while a group of {m('n')} people gains {m('n \\cdot t')} total years after {m('t')} years.",
                f"السرعة المتوسطة تساوي دائماً **المسافة الكلية مقسومةً على الزمن الكلي**، وليست المتوسط الحسابي للسرعتين "
                f"(لأنك تقضي زمناً أطول أثناء السير بالسرعة الأبطأ!). افترض مسافة ذكية {m('D = \\operatorname{lcm}(v_1, v_2)')} "
                f"أو طبّق القانون {m('v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}')}. وفي ألغاز الأعمار يبقى **فرق العمر** بين أي شخصين ثابتاً دائماً.",
                dm("v_{\\text{avg}} = \\frac{2D}{\\frac{D}{v_1} + \\frac{D}{v_2}} = \\frac{2 v_1 v_2}{v_1 + v_2}"),
                "قانون السرعة المتوسطة لرحلة الذهاب والإياب:",
                dm("v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}"),
                diagram_en=svg_motion_timeline("Start", "Summit", "Distance D", "v₁ up", "v₂ down", meet=True),
                diagram_ar=svg_motion_timeline("البداية", "القمة", "المسافة D", "ذهاب v₁", "إياب v₂", meet=True),
            ),
            kang_concept(
                "3. Symmetric Balance Systems & Telescoping Chains",
                "٣. أنظمة الموازين المتماثلة والسلاسل الكسرية المتداخلة",
                f"Given symmetric equations like {m('3x + 2y = A')} and {m('2x + 3y = B')}, don't isolate a variable right away! "
                f"**Add** them to get {m('5(x+y) = A+B')} and **subtract** them to get {m('x - y = A - B')}. And when facing a long "
                f"sum {m('\\sum \\frac{1}{k(k+1)}')} or product {m('\\prod \\frac{k+1}{k}')}, split or factor each term so interior "
                f"pieces cancel like falling dominoes, leaving only the first and last boundary terms!",
                f"عند مواجهة معادلتين متماثلتين مثل {m('3x + 2y = A')} و{m('2x + 3y = B')}، لا تعزل متغيراً بالكسور! **اجمعهما** لتحصل "
                f"على {m('5(x+y) = A+B')} و**اطرحهما** لتحصل على {m('x - y = A - B')}. وفي المجاميع الطويلة مثل {m('\\sum \\frac{1}{k(k+1)}')} "
                f"أو الجداءات {m('\\prod \\frac{k+1}{k}')}، فكّك كل حد لتتلاشى الحدود الداخلية تباعاً ولا يبقى سوى الطرفين الأول والأخير!",
                dm("\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}, \\qquad \\prod_{k=a}^{b} \\frac{k+1}{k} = \\frac{b+1}{a}"),
                "تفكيك الكسور المتداخلة واختصار الجداءات:",
                dm("\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}, \\qquad \\prod_{k=a}^{b} \\frac{k+1}{k} = \\frac{b+1}{a}"),
                diagram_en=svg_balance_scales(3, 2, 2, 3),
            ),
        ],
        traps_en=[
            "Trap: Averaging \\( 12\\text{ km/h} \\) and \\( 20\\text{ km/h} \\) to get \\( 16\\text{ km/h} \\)! On a round trip, the harmonic mean \\( \\frac{2(12)(20)}{32} = 15\\text{ km/h} \\) is **always strictly less** than the arithmetic mean.",
            "Trap: Subtracting transferred liters from one jar's ratio without adding them to the other jar! When \\( k \\) liters move from A to B, \\( A \\) decreases by \\( k \\) **and** \\( B \\) increases by \\( k \\), changing their difference by \\( 2k \\).",
            "Trap: Dropping the factor \\( \\frac{1}{d} \\) when telescoping a step-\\( d \\) denominator! Remember \\( \\frac{1}{k(k+d)} = \\frac{1}{d}\\left(\\frac{1}{k} - \\frac{1}{k+d}\\right) \\).",
        ],
        traps_ar=[
            "فخ شائع: حساب متوسط السرعتين \\( 12 \\) و\\( 20 \\) كأنه \\( 16\\text{ كم/س} \\)! في الذهاب والإياب يكون المتوسط التوافقي \\( 15\\text{ كم/س} \\) **أصغر دائماً** من المتوسط الحسابي.",
            "فخ شائع: طرح الكمية المنقولة من الوعاء الأول ونسيان إضافتها للثاني! عند نقل \\( k \\) لتر من (أ) إلى (ب) ينقص الأول بمقدار \\( k \\) ويزيد الثاني بمقدار \\( k \\) فيتغير الفرق بمقدار \\( 2k \\).",
            "فخ شائع: نسيان المعامل \\( \\frac{1}{d} \\) في الكسور المتداخلة ذات القفزة \\( d \\)! تذكّر دائماً أن \\( \\frac{1}{k(k+d)} = \\frac{1}{d}\\left(\\frac{1}{k} - \\frac{1}{k+d}\\right) \\).",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-02-EX1",
                "Worked Example 1 — Pouring Between Two Pitchers",
                "مثال محلول ١ — نقل العصير بين إبريقين مع ثبات المجموع",
                f"Pitcher A and Pitcher B hold berry punch in the ratio {m('5 : 3')}. After {m('18\\text{ mL}')} of punch is poured from Pitcher A into Pitcher B, the ratio becomes {m('7 : 9')}. How many milliliters of punch are in both pitchers altogether?",
                f"يحتوي الإبريق (أ) والإبريق (ب) على عصير التوت بنسبة {m('5 : 3')}. بعد صبّ {m('18\\text{ مل}')} من الإبريق (أ) في الإبريق (ب) أصبحت النسبة {m('7 : 9')}. كم ملليلتراً من العصير يوجد في الإبريقين معاً؟",
                96,
                [64, 72, 80, 112],
                "Match the total number of ratio parts before and after pouring since no punch leaves the two-pitcher system.",
                [
                    f"Before pouring, total parts = {m('5 + 3 = 8')}. After pouring, total parts = {m('7 + 9 = 16')}.",
                    f"Scale the initial ratio by {m(2)} so total parts match {m(16)}: {m('5 : 3 = 10 : 6')}.",
                    f"Pitcher A drops from {m(10)} parts to {m(7)} parts, so {m('3\\text{ parts} = 18\\text{ mL}')}, giving {m('1\\text{ part} = 6\\text{ mL}')}.",
                    f"Total punch across all {m(16)} parts is {m('16 \\times 6 = 96\\text{ mL}')}.",
                ],
                f"Initially {m('60\\text{ mL}')} and {m('36\\text{ mL}')}; after pouring {m(18)}, we get {m('42 : 54 = 7 : 9')}. Total = {m(96)}!",
                "وحّد مجموع أجزاء النسبة قبل الصبّ وبعده لأن الحجم الكلي للعصير لم يتغير.",
                [
                    f"قبل الصبّ مجموع الأجزاء {m('5 + 3 = 8')}، وبعد الصبّ مجموع الأجزاء {m('7 + 9 = 16')}.",
                    f"نضرب النسبة الأولى في {m(2)} لتوحيد المجموع على {m(16)} جزءاً: {m('5 : 3 = 10 : 6')}.",
                    f"نقص الإبريق (أ) من {m(10)} أجزاء إلى {m(7)} أجزاء، أي أن {m('3\\text{ أجزاء} = 18\\text{ مل}')} ومنه الجزء الواحد = {m('6\\text{ مل}')}.",
                    f"إذن الحجم الكلي للـ {m(16)} جزءاً يساوي {m('16 \\times 6 = 96\\text{ مل}')}.",
                ],
                f"تحقق: البداية {m(60)} و{m(36)}، وبعد نقل {m(18)} تصبح {m('42 : 54 = 7 : 9')} والمجموع {m(96)}!",
                diagram_en=svg_two_jars("A (10→7)", 0.65, "B (6→9)", 0.45, "18 mL"),
                diagram_ar=svg_two_jars("أ (10←7)", 0.65, "ب (6←9)", 0.45, "18 مل"),
            ),
            kang_worked_example(
                "KANG-L3-02-EX2",
                "Worked Example 2 — Mountain Trail Round-Trip Speed",
                "مثال محلول ٢ — السرعة المتوسطة صعوداً وهبوطاً",
                f"A cyclist climbs a hill trail at {m('12\\text{ km/h}')} and returns along the exact same trail at {m('20\\text{ km/h}')}. What is her average speed for the whole round trip in {m('\\text{km/h}')}?",
                f"تصعد درّاجة مساراً جبلياً بسرعة {m('12\\text{ كم/س}')} وتعود على نفس المسار تماماً بسرعة {m('20\\text{ كم/س}')}. ما سرعتها المتوسطة لرحلة الذهاب والإياب كاملةً بوحدة {m('\\text{كم/س}')}؟",
                15,
                [14, 16, 17, 18],
                "Pick a convenient trail length \\( D = \\operatorname{lcm}(12, 20) = 60\\text{ km} \\) and divide \\( 2D \\) by total time.",
                [
                    f"Choose one-way trail distance {m('D = \\operatorname{lcm}(12, 20) = 60\\text{ km}')} (any positive {m('D')} gives the same answer!).",
                    f"Time going uphill is {m('60 \\div 12 = 5\\text{ hours}')}; time coming downhill is {m('60 \\div 20 = 3\\text{ hours}')}.",
                    f"Total round-trip distance is {m('60 + 60 = 120\\text{ km}')} and total time is {m('5 + 3 = 8\\text{ hours}')}.",
                    f"Average speed = {m('120 \\div 8 = 15\\text{ km/h}')}.",
                ],
                f"Harmonic formula check: {m('\\frac{2 \\times 12 \\times 20}{12 + 20} = \\frac{480}{32} = 15\\text{ km/h}')}.",
                "اختر طول مسار مريحاً \\( D = \\operatorname{lcm}(12, 20) = 60\\text{ كم} \\) واقسم المسافة الكلية \\( 2D \\) على الزمن الكلي.",
                [
                    f"نفرض طول المسار ذهاباً {m('D = \\operatorname{lcm}(12, 20) = 60\\text{ كم}')}.",
                    f"زمن الصعود {m('60 \\div 12 = 5')} ساعات، وزمن الهبوط {m('60 \\div 20 = 3')} ساعات.",
                    f"المسافة الكلية ذهاباً وإياباً {m('60 + 60 = 120\\text{ كم}')} والزمن الكلي {m('5 + 3 = 8')} ساعات.",
                    f"السرعة المتوسطة = {m('120 \\div 8 = 15\\text{ كم/س}')}.",
                ],
                f"تحقق بالقانون التوافقي: {m('\\frac{2 \\times 12 \\times 20}{12 + 20} = \\frac{480}{32} = 15\\text{ كم/س}')}.",
                diagram_en=svg_motion_timeline("Base", "Peak", "60 km", "12 km/h", "20 km/h", meet=True),
                diagram_ar=svg_motion_timeline("القاعدة", "القمة", "60 كم", "12 كم/س", "20 كم/س", meet=True),
            ),
            kang_worked_example(
                "KANG-L3-02-EX3",
                "Worked Example 3 — Symmetric Scale Weights",
                "مثال محلول ٣ — أوزان الميزان المتماثلة",
                f"Three bronze spheres and two silver cubes together weigh {m('310\\text{ g}')}, while two bronze spheres and three silver cubes together weigh {m('290\\text{ g}')}. What is the mass of one bronze sphere in grams?",
                f"تزن ثلاث كرات برونزية ومكعبان فضيان معاً {m('310\\text{ جم}')}، بينما تزن كرتان برونزيتان وثلاثة مكعبات فضية معاً {m('290\\text{ جم}')}. ما كتلة الكرة البرونزية الواحدة بالجرام؟",
                70,
                [50, 60, 65, 80],
                "Add the two weighings to find \\( B + S \\), and subtract them to find \\( B - S \\).",
                [
                    f"Let {m('B')} and {m('S')} be the masses of a bronze sphere and a silver cube: {m('3B + 2S = 310')} and {m('2B + 3S = 290')}.",
                    f"Adding both equations gives {m('5B + 5S = 600')}, so {m('B + S = 120')}.",
                    f"Subtracting the second equation from the first gives {m('B - S = 20')}.",
                    f"Adding {m('B + S = 120')} and {m('B - S = 20')} yields {m('2B = 140 \\implies B = 70\\text{ g}')}.",
                ],
                f"With {m('B = 70')} and {m('S = 50')}: {m('3(70)+2(50) = 310')} and {m('2(70)+3(50) = 290')}.",
                "اجمع الوزنين لإيجاد \\( B + S \\) واطرحهما لإيجاد \\( B - S \\).",
                [
                    f"نفرض كتلة الكرة البرونزية {m('B')} والمكعب الفضي {m('S')}: لدينا {m('3B + 2S = 310')} و{m('2B + 3S = 290')}.",
                    f"بجمع المعادلتين نحصل على {m('5B + 5S = 600')} ومنها {m('B + S = 120')}.",
                    f"بطرح المعادلة الثانية من الأولى نحصل على {m('B - S = 20')}.",
                    f"بجمع {m('B + S = 120')} و{m('B - S = 20')} نجد {m('2B = 140 \\implies B = 70\\text{ جم}')}.",
                ],
                f"تحقق عند {m('B = 70, S = 50')}: {m('3(70)+2(50) = 310')} و{m('2(70)+3(50) = 290')}.",
                diagram_en=svg_balance_scales(3, 2, 2, 3),
            ),
            kang_worked_example(
                "KANG-L3-02-EX4",
                "Worked Example 4 — Telescoping Fraction Product",
                "مثال محلول ٤ — جداء الكسور المتداخلة",
                f"What is the exact value of the product {m('\\left(1 + \\frac{1}{3}\\right)\\left(1 + \\frac{1}{4}\\right)\\left(1 + \\frac{1}{5}\\right)\\cdots\\left(1 + \\frac{1}{29}\\right)')}?",
                f"ما القيمة الدقيقة لحاصل الضرب {m('\\left(1 + \\frac{1}{3}\\right)\\left(1 + \\frac{1}{4}\\right)\\left(1 + \\frac{1}{5}\\right)\\cdots\\left(1 + \\frac{1}{29}\\right)')}؟",
                10,
                [9, Fraction(29, 3), Fraction(31, 3), 11],
                "Convert every parenthesis into an improper fraction \\( \\frac{k+1}{k} \\) and watch adjacent numerators and denominators cancel!",
                [
                    f"Rewrite each factor as a single fraction: {m('\\frac{4}{3} \\times \\frac{5}{4} \\times \\frac{6}{5} \\times \\cdots \\times \\frac{30}{29}')}.",
                    f"Every numerator from {m(4)} through {m(29)} cancels with the denominator of the very next fraction!",
                    f"Only the very first denominator {m(3)} and the very last numerator {m(30)} survive.",
                    f"Thus the entire product simplifies to {m('\\frac{30}{3} = 10')}.",
                ],
                f"Testing the first 3 terms: {m('\\frac{4}{3}\\cdot\\frac{5}{4}\\cdot\\frac{6}{5} = \\frac{6}{3} = 2')}; extending to {m('k=29')} gives {m('30/3 = 10')}.",
                "حوّل كل قوس إلى كسر غير فعلي \\( \\frac{k+1}{k} \\) وراقب اختصار كل بسط مع مقام الكسر الذي يليه!",
                [
                    f"نكتب كل عامل على صورة كسر واحد: {m('\\frac{4}{3} \\times \\frac{5}{4} \\times \\frac{6}{5} \\times \\cdots \\times \\frac{30}{29}')}.",
                    f"يُختصر كل بسط من {m(4)} حتى {m(29)} مع مقام الكسر التالي مباشرة.",
                    f"لا يتبقى سوى أول مقام وهو {m(3)} وآخر بسط وهو {m(30)}.",
                    f"إذن قيمة الجداء بالكامل هي {m('\\frac{30}{3} = 10')}.",
                ],
                f"تحقق على أول 3 حدود: {m('\\frac{4}{3}\\cdot\\frac{5}{4}\\cdot\\frac{6}{5} = \\frac{6}{3} = 2')}، وعند الوصول إلى {m(29)} يصبح الناتج {m('30/3 = 10')}.",
                diagram_en=svg_number_strip(["4/3", "× 5/4", "× … ×", "30/29", "= 10"]),
            ),
        ],
        blueprints=[
            "kang_cad_ratio_jar_transfer",
            "kang_cad_harmonic_roundtrip",
            "kang_cad_linear_system_weights",
            "kang_cad_telescoping_fractions",
        ],
    )


def _lesson_3_3() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-03",
        level=LEVEL,
        unit_num="Lesson 3.3",
        topic="Geometry",
        title_en="Parallel Zigzag Angles, Subdivided Rectangle Areas, Midpoint Squares & Semicircle Sectors",
        title_ar="زوايا الخط المتعرج بين متوازيين ومساحات المستطيلات المقسمة ومربعات المنتصفات والقطاعات الدائرية",
        summary_en=(
            "Conquer signature Kangaroo Cadet flat-geometry puzzles: split zigzag bends with auxiliary parallel "
            "lines, unlock missing sub-rectangle areas and perimeters without solving for individual sides, "
            "halve areas repeatedly with midpoint squares, and reassemble circular sectors cleanly."
        ),
        summary_ar=(
            "أتقن أشهر ألغاز الهندسة المستوية في مستوى كاديت: قسّم زوايا الخطوط المتعرجة بمستقيمات مساعدة موازية، "
            "واستنتج مساحات ومحيطات المستطيلات الفرعية دون إيجاد كل ضلع منفرداً، ونصّف المساحات بمربعات المنتصفات، "
            "وأعد تجميع أنصاف الدوائر والقطاعات بذكاء."
        ),
        goals_en=[
            "Draw **auxiliary parallel lines** through every bend vertex to solve multi-turn zigzag angle puzzles.",
            "Apply the **cross-product area rule** \\( A_1 A_4 = A_2 A_3 \\) and **cross-sum perimeter rule** \\( P_1 + P_4 = P_2 + P_3 \\) in subdivided rectangles.",
            "Use **area halving** when joining midpoints of squares and cutting squares into 8 congruent triangles.",
            "Combine **inscribed circles, semicircles, and quarter-circles** inside squares by reassembling matching regions.",
        ],
        goals_ar=[
            "رسم **مستقيمات مساعدة موازية** عند كل رأس منكسر لحلّ ألغاز الزوايا المتعرجة.",
            "تطبيق **قاعدة الضرب التبادلي للمساحات** \\( A_1 A_4 = A_2 A_3 \\) و**قاعدة الجمع التبادلي للمحيطات** \\( P_1 + P_4 = P_2 + P_3 \\) في المستطيلات المقسمة.",
            "استخدام **تنصيف المساحة المتتالي** عند توصيل منتصفات أضلاع المربع وتقسيمه إلى 8 مثلثات متطابقة.",
            "تجميع **الدوائر وأنصاف وأرباع الدوائر** داخل المربعات لحساب المساحات المظللة بسرعة.",
        ],
        concepts=[
            kang_concept(
                "1. Auxiliary Parallel Lines in Zigzag Paths",
                "١. المستقيمات المساعدة الموازية في الخطوط المتعرجة",
                f"Whenever a broken line zigzags between parallel lines {m('L_1 \\parallel L_2')}, draw a **helper line "
                f"parallel to {m('L_1')} through each bend vertex**! Alternate interior angles (Z-angles) transfer each outer "
                f"acute angle directly to the bend. For a single bend, the middle turn angle equals the sum of the two acute "
                f"angles; for multiple alternating bends, **sum of right-pointing angles = sum of left-pointing angles**!",
                f"عندما يتعرج خط منكسر بين مستقيمين متوازيين {m('L_1 \\parallel L_2')}، ارسم **مستقيماً مساعداً موازياً لـ {m('L_1')} "
                f"يمر بكل رأس منكسر**! تنقل الزوايا المتبادلة داخلياً كل زاوية حادة مباشرة إلى الرأس الأوسط. وفي التعرجات المتعددة "
                f"المتناوبة يتحقق دائماً: **مجموع الزوايا المتجهة يميناً = مجموع الزوايا المتجهة يساراً**!",
                dm("L_1 \\parallel L_2 \\implies x = \\alpha + \\beta, \\qquad \\sum \\theta_{\\text{right}} = \\sum \\theta_{\\text{left}}"),
                "قاعدة زاوية الانكسار وموازنة الزوايا المتناوبة:",
                dm("x = \\alpha + \\beta, \\qquad \\sum \\theta_{\\text{يمين}} = \\sum \\theta_{\\text{يسار}}"),
                diagram_en=svg_parallel_zigzag("α", "α + β", "β"),
            ),
            kang_concept(
                "2. Subdivided 2×2 Rectangles: Cross-Product & Cross-Sum",
                "٢. المستطيل المقسم 2×2: الضرب التبادلي للمساحات والجمع التبادلي للمحيطات",
                f"Cutting a rectangle with one horizontal line and one vertical line creates widths {m('w_1, w_2')} and heights "
                f"{m('h_1, h_2')}. Notice that opposite **areas** multiply to the exact same quantity "
                f"{m('(w_1 h_1)(w_2 h_2) = (w_2 h_1)(w_1 h_2)')}, while opposite **perimeters** add to the exact same sum "
                f"{m('P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}} = 2(w_1+w_2+h_1+h_2)')}!",
                f"تقسيم مستطيل بخط أفقي وخط رأسي يُنتج عرضين {m('w_1, w_2')} وارتفاعين {m('h_1, h_2')}. لاحظ أن حاصل ضرب **مساحتَي** "
                f"أي مستطيلين متقابلين قُطرياً متساوٍ تماماً {m('A_{\\text{TL}}\\cdot A_{\\text{BR}} = A_{\\text{TR}}\\cdot A_{\\text{BL}}')}، "
                f"بينما مجموع **محيطَي** أي مستطيلين متقابلين قُطرياً متساوٍ {m('P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}}')}!",
                dm("A_{\\text{TL}} \\cdot A_{\\text{BR}} = A_{\\text{TR}} \\cdot A_{\\text{BL}}, \\qquad P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}}"),
                "قاعدتا المساحات والمحيطات المتقابلة قطرياً:",
                dm("A_{\\text{TL}} \\cdot A_{\\text{BR}} = A_{\\text{TR}} \\cdot A_{\\text{BL}}, \\qquad P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}}"),
                diagram_en=svg_subdivided_rect_2x2("w₁·h₁", "w₂·h₁", "w₁·h₂", "w₂·h₂"),
            ),
            kang_concept(
                "3. Midpoint Squares & Circular Cutouts in Squares",
                "٣. مربعات المنتصفات والقطاعات الدائرية داخل المربع",
                f"Connecting the midpoints of the four sides of a square of side {m('s')} forms a tilted square whose side is "
                f"{m('\\frac{s}{\\sqrt{2}}')} and whose **area is exactly half** ({m('\\frac{1}{2}s^2')}) because each of the four "
                f"corner triangles matches an inner quarter! Likewise, two inward semicircles on opposite sides of a square of side "
                f"{m('s')} have radius {m('r = \\frac{s}{2}')}, so together they form **one complete circle** of area {m('\\pi (s/2)^2')}.",
                f"توصيل منتصفات أضلاع مربع طول ضلعه {m('s')} يصنع مربعاً مائلاً طول ضلعه {m('\\frac{s}{\\sqrt{2}}')} و**مساحته نصف مساحة "
                f"المربع الأصلي تماماً** ({m('\\frac{1}{2}s^2')})! وبالمثل، نصفا دائرتين مرسومان للداخل على ضلعين متقابلين من مربع طول ضلعه "
                f"{m('s')} لهما نصف قطر {m('r = \\frac{s}{2}')}، فيجتمعان معاً لتكوين **دائرة كاملة واحدة** مساحتها {m('\\pi (s/2)^2')}.",
                dm("A_{\\text{midpoint sq}} = \\frac{1}{2}s^2, \\qquad A_{\\text{corners}} = s^2 - \\pi\\left(\\frac{s}{2}\\right)^2"),
                "تنصيف المساحة بالمنتصفات ومساحة زوايا المربع خارج الدائرة:",
                dm("A_{\\text{المنتصفات}} = \\frac{1}{2}s^2, \\qquad A_{\\text{الزوايا}} = s^2 - \\pi\\left(\\frac{s}{2}\\right)^2"),
                diagram_en=svg_square_circle_shaded("s", "inscribed_outside"),
            ),
        ],
        traps_en=[
            "Trap: Confusing an **obtuse** supplement \\( 180^\\circ - \\alpha \\) on a parallel line with the acute alternate angle \\( \\alpha \\)! Always trace which side of the transversal opens toward the bend.",
            "Trap: Adding areas instead of multiplying in a \\( 2\\times 2 \\) subdivided rectangle! Remember: **perimeters add** (\\( P_1 + P_4 = P_2 + P_3 \\)), whereas **areas multiply** (\\( A_1 A_4 = A_2 A_3 \\)).",
            "Trap: Using diameter \\( s \\) instead of radius \\( r = s/2 \\) in \\( \\pi r^2 \\)! A circle inscribed in a square of side \\( 14 \\) has radius \\( 7 \\), not \\( 14 \\).",
        ],
        traps_ar=[
            "فخ شائع: الخلط بين الزاوية **المنفرجة** المكملة \\( 180^\\circ - \\alpha \\) والزاوية الحادة المتبادلة \\( \\alpha \\)! تتبّع دائماً الفتحة المتجهة نحو رأس الانكسار.",
            "فخ شائع: جمع المساحات بدلاً من ضربها في المستطيل المقسم \\( 2\\times 2 \\)! تذكّر: **المحيطات تُجمع** (\\( P_1 + P_4 = P_2 + P_3 \\)) بينما **المساحات تُضرب** (\\( A_1 A_4 = A_2 A_3 \\)).",
            "فخ شائع: التعويض بالقطر الكامل \\( s \\) بدلاً من نصف القطر \\( r = s/2 \\) في قانون المساحة \\( \\pi r^2 \\)! الدائرة المرسومة داخل مربع ضلعه \\( 14 \\) نصف قطرها \\( 7 \\) وليس \\( 14 \\).",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-03-EX1",
                "Worked Example 1 — Zigzag Bend Between Parallel Lines",
                "مثال محلول ١ — زاوية الانكسار بين مستقيمين متوازيين",
                f"In the diagram, {m('L_1 \\parallel L_2')}. A two-segment path leaves {m('L_1')} at {m('42^\\circ')} and meets {m('L_2')} at {m('53^\\circ')}. What is the measure of the middle bend angle {m('x')} in degrees?",
                f"في الشكل الموضح {m('L_1 \\parallel L_2')}. ينطلق مسار منكسر من {m('L_1')} بزاوية {m('42^\\circ')} ويلتقي بـ {m('L_2')} بزاوية {m('53^\\circ')}. ما قياس زاوية الرأس الأوسط {m('x')} بالدرجات؟",
                95,
                [85, 90, 105, 138],
                "Draw an auxiliary line through the middle vertex parallel to \\( L_1 \\) and \\( L_2 \\).",
                [
                    f"Draw a helper line {m('L_m')} through the middle vertex parallel to both {m('L_1')} and {m('L_2')}.",
                    f"By alternate interior angles with {m('L_1')}, the upper portion of angle {m('x')} equals {m('42^\\circ')}.",
                    f"By alternate interior angles with {m('L_2')}, the lower portion of angle {m('x')} equals {m('53^\\circ')}.",
                    f"Therefore {m('x = 42^\\circ + 53^\\circ = 95^\\circ')}.",
                ],
                f"{m('42 + 53 = 95')}, slightly larger than a right angle as drawn.",
                "ارسم مستقيماً مساعداً يمر بالرأس الأوسط ويوازي كلاً من \\( L_1 \\) و\\( L_2 \\).",
                [
                    f"نرسم مستقيماً مساعداً {m('L_m')} يمر بالرأس الأوسط ويوازي {m('L_1')} و{m('L_2')}.",
                    f"بالتبادل الداخلي مع {m('L_1')} يكون الجزء العلوي من الزاوية {m('x')} مساوياً {m('42^\\circ')}.",
                    f"وبالتبادل الداخلي مع {m('L_2')} يكون الجزء السفلي من الزاوية {m('x')} مساوياً {m('53^\\circ')}.",
                    f"إذن قياس الزاوية {m('x = 42^\\circ + 53^\\circ = 95^\\circ')}.",
                ],
                f"تحقق: {m('42 + 53 = 95')} درجة.",
                diagram_en=svg_parallel_zigzag("42°", "x°", "53°"),
            ),
            kang_worked_example(
                "KANG-L3-03-EX2",
                "Worked Example 2 — Missing Area in a Subdivided Rectangle",
                "مثال محلول ٢ — المساحة المفقودة في مستطيل مقسم إلى أربعة أجزاء",
                f"A rectangle is split by one horizontal line and one vertical line into four smaller rectangles. The top-left, top-right, and bottom-left areas are {m('18\\text{ cm}^2')}, {m('24\\text{ cm}^2')}, and {m('27\\text{ cm}^2')}. What is the bottom-right area in {m('\\text{cm}^2')}?",
                f"قُسّم مستطيل بخط أفقي وخط رأسي إلى أربعة مستطيلات صغيرة. إذا كانت مساحات المستطيلات (أعلى اليسار، أعلى اليمين، أسفل اليسار) هي {m('18\\text{ سم}^2')} و{m('24\\text{ سم}^2')} و{m('27\\text{ سم}^2')}، فما مساحة المستطيل أسفل اليمين بوحدة {m('\\text{سم}^2')}؟",
                36,
                [30, 32, 33, 42],
                "Use the cross-product property \\( A_{\\text{TL}} \\cdot A_{\\text{BR}} = A_{\\text{TR}} \\cdot A_{\\text{BL}} \\).",
                [
                    f"In any {m('2 \\times 2')} grid of rectangles, the top-left to top-right width ratio is {m('18 : 24 = 3 : 4')}.",
                    f"The bottom row shares the exact same widths, so {m('27 : A_{\\text{BR}} = 3 : 4')}.",
                    f"Equivalently, {m('18 \\cdot A_{\\text{BR}} = 24 \\times 27 = 648')}.",
                    f"Dividing by {m(18)} gives {m('A_{\\text{BR}} = 648 \\div 18 = 36\\text{ cm}^2')}.",
                ],
                f"Ratios check: {m('18/24 = 3/4')} and {m('27/36 = 3/4')}. Verified!",
                "استخدم خاصية الضرب التبادلي للمساحات \\( A_{\\text{TL}} \\cdot A_{\\text{BR}} = A_{\\text{TR}} \\cdot A_{\\text{BL}} \\).",
                [
                    f"نسبة العرضين في الصف العلوي تساوي نسبة المساحتين: {m('18 : 24 = 3 : 4')}.",
                    f"الصف السفلي له نفس العرضين تماماً، لذا {m('27 : A_{\\text{BR}} = 3 : 4')}.",
                    f"وبالضرب التبادلي: {m('18 \\cdot A_{\\text{BR}} = 24 \\times 27 = 648')}.",
                    f"بقسمة {m(648)} على {m(18)} نجد المساحة المطلوبة {m('36\\text{ سم}^2')}.",
                ],
                f"تحقق: {m('18 \\times 36 = 648')} و{m('24 \\times 27 = 648')}!",
                diagram_en=svg_subdivided_rect_2x2("18", "24", "27", "?"),
            ),
            kang_worked_example(
                "KANG-L3-03-EX3",
                "Worked Example 3 — Nested Midpoint Squares",
                "مثال محلول ٣ — مربعات المنتصفات المتداخلة",
                f"An outer square has side length {m('16\\text{ cm}')}. Connecting the midpoints of its sides forms a 2nd square, and connecting the midpoints of that 2nd square forms a 3rd innermost square. What is the area of the 3rd square in {m('\\text{cm}^2')}?",
                f"مربع خارجي طول ضلعه {m('16\\text{ سم}')}. بتوصيل منتصفات أضلاعه يتكون مربع ثانٍ، وبتوصيل منتصفات أضلاع المربع الثاني يتكون مربع ثالث داخلي. ما مساحة المربع الثالث بوحدة {m('\\text{سم}^2')}؟",
                64,
                [32, 48, 96, 128],
                "Each midpoint square has exactly half the area of the square immediately outside it.",
                [
                    f"The outer (1st) square has area {m('16^2 = 256\\text{ cm}^2')}.",
                    f"Joining its midpoints cuts the area in half: the 2nd square has area {m('256 \\div 2 = 128\\text{ cm}^2')}.",
                    f"Joining the midpoints once more halves the area again: the 3rd square has area {m('128 \\div 2 = 64\\text{ cm}^2')}.",
                ],
                f"Side check: 2nd side = {m('8\\sqrt{2}')}, 3rd side = {m('8\\text{ cm}')}, and {m('8^2 = 64\\text{ cm}^2')}!",
                "كل مربع منتصفات تساوي مساحته نصف مساحة المربع الذي يحيط به مباشرة.",
                [
                    f"مساحة المربع الخارجي الأول تساوي {m('16^2 = 256\\text{ سم}^2')}.",
                    f"بتوصيل منتصفاته تنقسم المساحة إلى النصف، فتكون مساحة المربع الثاني {m('256 \\div 2 = 128\\text{ سم}^2')}.",
                    f"وبتوصيل المنتصفات مرة ثانية تنقسم المساحة إلى النصف مجدداً، فتصبح مساحة المربع الثالث {m('128 \\div 2 = 64\\text{ سم}^2')}.",
                ],
                f"تحقق بطول الضلع: ضلع الثاني {m('8\\sqrt{2}')} وضلع الثالث {m('8\\text{ سم}')} ومساحته {m('8^2 = 64')}!",
                diagram_en=svg_midpoint_square_shaded("16 cm", shade_inner=True),
            ),
            kang_worked_example(
                "KANG-L3-03-EX4",
                "Worked Example 4 — Two Semicircles Cut from a Square",
                "مثال محلول ٤ — نصفا دائرتين مقطوعان من داخل مربع",
                f"Inside a square of side length {m('14\\text{ cm}')}, two inward semicircles are drawn using the left and right vertical sides as diameters. Using {m('\\pi = \\frac{22}{7}')}, what is the shaded area outside both semicircles in {m('\\text{cm}^2')}?",
                f"داخل مربع طول ضلعه {m('14\\text{ سم}')}، رُسم نصفا دائرتين باتجاه الداخل بحيث يكون الضلعان الرأسيان الأيمن والأيسر قطرين لهما. باعتبار {m('\\pi = \\frac{22}{7}')}، ما المساحة المظللة خارج نصفي الدائرتين بوحدة {m('\\text{سم}^2')}؟",
                42,
                [38, 49, 77, 119],
                "Combine the two non-overlapping semicircles of radius \\( 7\\text{ cm} \\) into one full circle, then subtract from the square's area.",
                [
                    f"The square has area {m('14^2 = 196\\text{ cm}^2')}.",
                    f"Each semicircle has diameter {m('14\\text{ cm}')}, so its radius is {m('r = 7\\text{ cm}')}. Since {m('7 + 7 = 14')}, the two semicircles just touch at the center without overlapping.",
                    f"Together they have the exact area of one full circle: {m('\\pi r^2 = \\frac{22}{7} \\times 7^2 = 154\\text{ cm}^2')}.",
                    f"Subtracting from the square gives {m('196 - 154 = 42\\text{ cm}^2')}.",
                ],
                f"{m('154 + 42 = 196 = 14^2')}, and {m('42')} is roughly {m('21.4\\%')} of the square (matching {m('1 - \\pi/4')}).",
                "اجمع نصفي الدائرتين غير المتداخلين (نصف قطر كلٍّ منهما \\( 7\\text{ سم} \\)) لتكوين دائرة كاملة ثم اطرح مساحتها من المربع.",
                [
                    f"مساحة المربع تساوي {m('14^2 = 196\\text{ سم}^2')}.",
                    f"قطر كل نصف دائرة {m('14\\text{ سم}')} أي أن نصف القطر {m('r = 7\\text{ سم}')}، وبما أن {m('7 + 7 = 14')} فهما يتماسان في المركز دون تداخل.",
                    f"مجموع مساحتَي نصفي الدائرتين يساوي مساحة دائرة كاملة: {m('\\pi r^2 = \\frac{22}{7} \\times 49 = 154\\text{ سم}^2')}.",
                    f"إذن المساحة المظللة تساوي {m('196 - 154 = 42\\text{ سم}^2')}.",
                ],
                f"تحقق: {m('154 + 42 = 196 = 14^2')}!",
                diagram_en=svg_square_circle_shaded("14 cm", "two_semis_outside"),
            ),
        ],
        blueprints=[
            "kang_cad_parallel_zigzag_angle",
            "kang_cad_four_rect_areas",
            "kang_cad_midpoint_shaded_square",
            "kang_cad_circle_in_square_area",
        ],
    )


def _lesson_3_4() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-04",
        level=LEVEL,
        unit_num="Lesson 3.4",
        topic="Geometry",
        title_en="3D Painted Solids, Rolling Dice on Grids, Unfolded Box Shortest Paths & Sliced Cubes",
        title_ar="المجسمات المطلية ثلاثية الأبعاد ودحرجة النرد وأقصر المسارات على الشبكات والمكعبات المكدسة",
        summary_en=(
            "Build sharp 3D spatial intuition for Kangaroo's favorite Cadet geometry problems: classify painted "
            "unit cubes by corners, edges, faces, and interior cores, track opposite faces on rolling dice, "
            "unfold boxes into flat nets for shortest paths, and count exposed faces by orthogonal projections."
        ),
        summary_ar=(
            "طوّر خيالك الفراغي ثلاثي الأبعاد لأشهر مسائل الكانجارو في مستوى كاديت: صنّف المكعبات الصغيرة المطلية "
            "حسب الرؤوس والحواف والأوجه والقلب الداخلي، وتتبّع الأوجه المتقابلة عند دحرجة النرد، وافرد الصناديق "
            "لإيجاد أقصر المسارات، واحسب المساحة الظاهرة بالمساقط المتعامدة."
        ),
        goals_en=[
            "Count **0-, 1-, 2-, and 3-painted-face unit cubes** in an \\( a \\times b \\times c \\) rectangular prism.",
            "Track all six faces of a **standard die** (opposite faces sum to \\( 7 \\)) across grid rolls and glued towers.",
            "Unfold 3D boxes into flat 2D rectangles to find **shortest surface paths** via the Pythagorean theorem.",
            "Compute **exposed surface areas** of glued cube stacks and sliced solids using 6-direction views or glued-face subtraction.",
        ],
        goals_ar=[
            "حساب أعداد المكعبات الوحدوية المطلية على **0 أو 1 أو 2 أو 3 أوجه** في متوازي مستطيلات \\( a \\times b \\times c \\).",
            "تتبّع الأوجه الستة **لحجر النرد القياسي** (مجموع كل وجهين متقابلين \\( 7 \\)) أثناء الدحرجة على الشبكات.",
            "فرد الصناديق ثلاثية الأبعاد إلى مستطيلات مستوية لإيجاد **أقصر مسار سطحي** بنظرية فيثاغورس.",
            "حساب **المساحة السطحية الظاهرة** لمجموعات المكعبات الملتصقة والمقطوعة عبر المساقط الستة أو طرح الأوجه الملتصقة.",
        ],
        concepts=[
            kang_concept(
                "1. Anatomy of a Painted a × b × c Rectangular Block",
                "١. تشريح متوازي المستطيلات المطلي a × b × c",
                f"When an {m('a \\times b \\times c')} block (with {m('a,b,c \\ge 2')}) is painted on all 6 faces and cut into "
                f"{m('abc')} unit cubes: **3 painted faces** sit at the {m(8)} **corners**; **2 painted faces** sit along the "
                f"12 **edges** ({m('4[(a-2)+(b-2)+(c-2)]')}); **1 painted face** sits on the 6 **face interiors**; and **0 painted "
                f"faces** form the hidden inner box {m('(a-2)(b-2)(c-2)')}!",
                f"عند طلاء متوازي مستطيلات أبعاده {m('a \\times b \\times c')} (حيث {m('a,b,c \\ge 2')}) من جميع أوجهه الستة وتقطيعه "
                f"إلى {m('abc')} مكعباً صغيراً: مكعبات **3 أوجه مطلية** تقع في **الرؤوس** الثمانية ({m(8)})؛ ومكعبات **وجهين مطليين** "
                f"تقع على **الحواف** الـ 12 ({m('4[(a-2)+(b-2)+(c-2)]')})؛ ومكعبات **الوجه الواحد** في قلب الأوجه؛ ومكعبات **0 أوجه** "
                f"تشكّل الصندوق الداخلي المخفي {m('(a-2)(b-2)(c-2)')}!",
                dm("N_3 = 8, \\quad N_2 = 4(a+b+c-6), \\quad N_0 = (a-2)(b-2)(c-2)"),
                "قوانين المكعبات المطلية في متوازي المستطيلات:",
                dm("N_3 = 8, \\quad N_2 = 4(a+b+c-6), \\quad N_0 = (a-2)(b-2)(c-2)"),
                diagram_en=svg_painted_cube_3d(4),
            ),
            kang_concept(
                "2. Rolling Dice & Opposite-Face Invariants",
                "٢. دحرجة النرد وثابت الأوجه المتقابلة",
                f"On a standard die, **opposite faces always add to 7**: {m('(1,6)')}, {m('(2,5)')}, and {m('(3,4)')}. "
                f"When a die rolls one step **East**, its North and South faces **do not change**, while "
                f"{m('\\text{West} \\to \\text{Top} \\to \\text{East} \\to \\text{Bottom} \\to \\text{West}')}. "
                f"Notice that rolling **2 steps in a straight line** swaps Top and Bottom, and rolling **4 steps** restores the exact starting state!",
                f"في حجر النرد القياسي يكون **مجموع كل وجهين متقابلين مساوياً لـ 7 دائماً**: {m('(1,6)')} و{m('(2,5)')} و{m('(3,4)')}. "
                f"عند دحرجة النرد خطوة واحدة **شرقاً** يبقى الوجهان الشمالي والجنوبي **ثابتين**، بينما ينتقل الغربي للأعلى والعلوي للشرق. "
                f"لاحظ أن الدحرجة **خطوتين على استقامة واحدة** تبدّل الأعلى بالأسفل، و**أربع خطوات** تعيد النرد لوضعه الأصلي!",
                dm("\\text{Top} + \\text{Bottom} = 7, \\qquad 2\\text{ straight rolls}: \\text{Top} \\leftrightarrow \\text{Bottom}"),
                "قاعدة الأوجه المتقابلة والدحرجة المستقيمة:",
                dm("\\text{الأعلى} + \\text{الأسفل} = 7, \\qquad \\text{خطوتان مستقيمتان}: \\text{الأعلى} \\leftrightarrow \\text{الأسفل}"),
                diagram_en=svg_kang_cube_faces("1", "2", "3"),
            ),
            kang_concept(
                "3. Unfolding Nets for Shortest Paths & Projection Counting",
                "٣. فرد الشبكات لأقصر المسارات وحساب المساحة بالمساقط",
                f"An ant crawling across faces of a box {m('a \\times b \\times c')} from one corner to the opposite corner travels "
                f"in a **straight line on the unfolded net**! To minimize {m('\\sqrt{(x+y)^2 + z^2}')}, always pair the **two "
                f"smallest dimensions** as {m('x + y')} and keep the **largest dimension** alone as {m('z')}. For glued cube stacks, "
                f"each glue seam hides **2 unit faces**, and slicing a solid with one flat cut **adds 2 cross-section faces**!",
                f"النملة التي تزحف على سطح صندوق أبعاده {m('a \\times b \\times c')} للوصول إلى الركن المقابل تسلك **خطاً مستقيماً على "
                f"الشبكة المفرودة**! لتصغير {m('\\sqrt{(x+y)^2 + z^2}')} اجمع دائماً **أصغر بُعدين معاً** {m('(x+y)')} واترك **البُعد الأكبر** "
                f"منفرداً {m('z')}. وفي المكعبات الملتصقة تُخفي كل وصلة التصاق **وجهين**، بينما تضيف كل عملية قطع مستوٍ **وجهين جديدين**!",
                dm("d_{\\min} = \\sqrt{(a+b)^2 + c^2} \\quad (a \\le b \\le c), \\qquad S_{\\text{glued}} = 6n - 2g"),
                "أقصر مسار على سطح الصندوق ومساحة المكعبات الملتصقة:",
                dm("d_{\\min} = \\sqrt{(a+b)^2 + c^2} \\quad (a \\le b \\le c), \\qquad S = 6n - 2g"),
                diagram_en=svg_cube_net([(1, 0, "Top"), (0, 1, "a"), (1, 1, "b"), (2, 1, "c"), (1, 2, "Base"), (3, 1, "Back")]),
            ),
        ],
        traps_en=[
            "Trap: Using the painted-prism formula when one dimension equals \\( 1 \\)! In a \\( 1 \\times 4 \\times 5 \\) flat slab, corner cubes have **4** painted faces (not 3!) and interior cubes have **2** painted faces (top and bottom).",
            "Trap: Pairing the two largest box edges when unfolding for an ant's shortest path! Since \\( (x+y)^2 + z^2 = x^2+y^2+z^2 + 2xy \\), minimizing \\( 2xy \\) requires pairing the **two smallest** edges.",
            "Trap: Counting bottom faces resting on the floor when a problem specifies **exposed faces painted after placing on a table**! Always check whether the base is included.",
        ],
        traps_ar=[
            "فخ شائع: تطبيق قوانين متوازي المستطيلات المعتادة عندما يكون أحد الأبعاد \\( 1 \\)! في لوح \\( 1 \\times 4 \\times 5 \\) مكعبات الزوايا لها **4** أوجه مطلية وليس 3!",
            "فخ شائع: جمع البُعدين الأكبرين عند فرد الصندوق لإيجاد أقصر مسار! بما أن \\( (x+y)^2 + z^2 = x^2+y^2+z^2 + 2xy \\) يجب جمع **أصغر بُعدين** لتصغير الحد \\( 2xy \\).",
            "فخ شائع: احتساب أوجه القاعدة الملامسة للطاولة عندما ينص السؤال على **طلاء المجسم وهو موضوع على الطاولة**! اقرأ شرط القاعدة بعناية.",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-04-EX1",
                "Worked Example 1 — Two-Face Painted Cubes in a Block",
                "مثال محلول ١ — المكعبات المطلية على وجهين في متوازي مستطيلات",
                f"A wooden {m('5 \\times 4 \\times 3')} block is painted blue on all six faces and cut into {m(60)} unit cubes. How many unit cubes have **exactly 2** blue faces?",
                f"طُلي متوازي مستطيلات خشبي أبعاده {m('5 \\times 4 \\times 3')} باللون الأزرق من جميع أوجهه الستة ثم قُطّع إلى {m(60)} مكعباً صغيراً. كم مكعباً صغيراً يحمل **وجهين أزرقين بالضبط**؟",
                24,
                [18, 20, 22, 32],
                "Cubes with exactly 2 painted faces lie on the 12 edges excluding the 8 corners: \\( 4[(a-2)+(b-2)+(c-2)] \\).",
                [
                    f"Along each of the {m(4)} edges of length {m(5)}, removing the {m(2)} corners leaves {m('5 - 2 = 3')} two-face cubes.",
                    f"Along each of the {m(4)} edges of length {m(4)}, there are {m('4 - 2 = 2')} two-face cubes.",
                    f"Along each of the {m(4)} edges of length {m(3)}, there is {m('3 - 2 = 1')} two-face cube.",
                    f"Total cubes with 2 blue faces = {m('4 \\times (3 + 2 + 1) = 24')}.",
                ],
                f"Full partition check: {m('8\\text{ (3-face)} + 24\\text{ (2-face)} + 22\\text{ (1-face)} + 6\\text{ (0-face)} = 60')}.",
                "المكعبات ذات الوجهين المطليين تقع على الحواف الـ 12 باستثناء الرؤوس الثمانية: \\( 4[(a-2)+(b-2)+(c-2)] \\).",
                [
                    f"على كل حافة من الحواف الـ {m(4)} ذات الطول {m(5)} يوجد {m('5 - 2 = 3')} مكعبات بوجهين مطليين.",
                    f"على كل حافة من الحواف الـ {m(4)} ذات الطول {m(4)} يوجد {m('4 - 2 = 2')} مكعبان بوجهين مطليين.",
                    f"على كل حافة من الحواف الـ {m(4)} ذات الطول {m(3)} يوجد {m('3 - 2 = 1')} مكعب واحد بوجهين مطليين.",
                    f"المجموع الكلي = {m('4 \\times (3 + 2 + 1) = 24')} مكعباً.",
                ],
                f"تحقق شامل: {m('8 + 24 + 22 + 6 = 60')} مكعباً بالضبط!",
                diagram_en=svg_painted_cube_3d(4),
            ),
            kang_worked_example(
                "KANG-L3-04-EX2",
                "Worked Example 2 — Rolling a Standard Die on a Grid",
                "مثال محلول ٢ — دحرجة حجر نرد قياسي على شبكة",
                f"A standard die (opposite faces sum to {m(7)}) starts with **1 on top**, **2 facing South**, and **3 facing East**. It rolls **2 steps East** and then **1 step South**. Which number lands on **top**?",
                f"يبدأ حجر نرد قياسي (مجموع كل وجهين متقابلين {m(7)}) والرقم **1 في الأعلى** و**2 باتجاه الجنوب** و**3 باتجاه الشرق**. تدحرج النرد **خطوتين شرقاً** ثم **خطوة واحدة جنوباً**. ما الرقم الذي سيظهر في **الأعلى**؟",
                5,
                [1, 2, 4, 6],
                "Rolling 2 steps East flips Top and Bottom while keeping North and South untouched; then rolling South brings North to the Top!",
                [
                    f"From opposite pairs summing to {m(7)}: Bottom = {m(6)}, North = {m(5)}, and West = {m(4)}.",
                    f"Rolling **2 steps East** flips the die {m('180^\\circ')} east-west: Top becomes {m(6)}, Bottom becomes {m(1)}, while South stays {m(2)} and North stays {m(5)}.",
                    f"Rolling **1 step South** rotates the North face up onto the Top!",
                    f"Therefore the final number on top is {m(5)}.",
                ],
                f"Step-by-step East rolls: Top {m('1 \\to 4 \\to 6')}, then South roll: North ({m(5)}) {m('\\to')} Top ({m(5)}).",
                "الدحرجة خطوتين شرقاً تقلب الأعلى والأسفل مع بقاء الشمال والجنوب ثابتين، ثم الدحرجة جنوباً ترفع الوجه الشمالي إلى الأعلى!",
                [
                    f"من مجموع المتقابلين {m(7)}: الأسفل = {m(6)}، الشمال = {m(5)}، الغرب = {m(4)}.",
                    f"عند الدحرجة **خطوتين شرقاً** ينقلب الأعلى والأسفل فيصبح الأعلى {m(6)} والأسفل {m(1)} ويبقى الجنوب {m(2)} والشمال {m(5)}.",
                    f"عند الدحرجة **خطوة جنوباً** ينتقل الوجه الشمالي ليصبح في الأعلى.",
                    f"إذن الرقم الظاهر في الأعلى في النهاية هو {m(5)}.",
                ],
                f"تحقق خطوة بخطوة: الأعلى {m('1 \\to 4 \\to 6')} شرقاً، ثم {m('6 \\to')} الجنوب ويحل محله الشمال ({m(5)}).",
                diagram_en=svg_kang_cube_faces("1", "2", "3"),
            ),
            kang_worked_example(
                "KANG-L3-04-EX3",
                "Worked Example 3 — Shortest Ant Path Across a Box",
                "مثال محلول ٣ — أقصر مسار لنملة على سطح صندوق",
                f"An ant crawls along the outside surface of a closed {m('3\\text{ cm} \\times 5\\text{ cm} \\times 15\\text{ cm}')} rectangular box from one corner to the diagonally opposite corner in space. What is the length of the **shortest** possible path in {m('\\text{cm}')}?",
                f"تزحف نملة على السطح الخارجي لصندوق مغلق أبعاده {m('3\\text{ سم} \\times 5\\text{ سم} \\times 15\\text{ سم}')} من أحد أركانه إلى الركن المقابل له قطرياً في الفراغ. ما طول **أقصر** مسار ممكن بوحدة {m('\\text{سم}')}؟",
                17,
                [16, 18, 19, 23],
                "Unfold two adjacent faces into a flat rectangle, pairing the two smallest edges \\( 3 + 5 = 8 \\) against \\( 15 \\).",
                [
                    f"On an unfolded two-face rectangle, the straight-line path has length {m('\\sqrt{(x+y)^2 + z^2}')}.",
                    f"To make {m('(x+y)^2 + z^2')} as small as possible, combine the **two smallest** dimensions: {m('3 + 5 = 8\\text{ cm}')}, with {m('z = 15\\text{ cm}')}.",
                    f"Apply the Pythagorean theorem: {m('d = \\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = \\sqrt{289} = 17\\text{ cm}')}.",
                ],
                f"Other unfoldings give {m('\\sqrt{18^2+5^2}=\\sqrt{349} > 17')} and {m('\\sqrt{20^2+3^2}=\\sqrt{409} > 17')}.",
                "افرد وجهين متجاورين في مستطيل مستوٍ بجمع أصغر بُعدين \\( 3 + 5 = 8 \\) مع البُعد الثالث \\( 15 \\).",
                [
                    f"على الشبكة المفرودة لوجهين متجاورين يكون طول الخط المستقيم {m('\\sqrt{(x+y)^2 + z^2}')}.",
                    f"لتصغير المسافة نجمع **أصغر بُعدين** معاً: {m('3 + 5 = 8\\text{ سم}')} مع بقاء البُعد الأكبر {m('15\\text{ سم}')}.",
                    f"بنظرية فيثاغورس: {m('d = \\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = \\sqrt{289} = 17\\text{ سم}')}.",
                ],
                f"تحقق: المسارات الأخرى تعطي {m('\\sqrt{349}')} و{m('\\sqrt{409}')} وكلاهما أكبر من {m(17)}.",
                diagram_en=svg_cube_net([(1, 0, "Top"), (0, 1, "3"), (1, 1, "5"), (2, 1, "15"), (1, 2, "Base"), (3, 1, "Back")]),
            ),
            kang_worked_example(
                "KANG-L3-04-EX4",
                "Worked Example 4 — Exposed Surface of a Staircase Stack",
                "مثال محلول ٤ — المساحة الظاهرة لدرج من المكعبات على طاولة",
                f"Six unit cubes ({m('1\\text{ cm} \\times 1\\text{ cm} \\times 1\\text{ cm}')}) are glued into three adjacent columns of heights {m('3, 2, 1')} resting flat on a wooden table. All exposed faces **not touching the table** are painted gold. What area is painted gold in {m('\\text{cm}^2')}?",
                f"أُلصقت ستة مكعبات وحدوية ({m('1\\text{ سم} \\times 1\\text{ سم} \\times 1\\text{ سم}')}) لتكوين ثلاثة أعمدة متجاورة ارتفاعاتها {m('3, 2, 1')} موضوعة على طاولة خشبية. طُليت جميع الأوجه المكشوفة **غير الملامسة للطاولة** باللون الذهبي. ما المساحة المطلية بالذهب بوحدة {m('\\text{سم}^2')}؟",
                21,
                [18, 20, 24, 27],
                "Count visible unit squares from Top, Front, Back, Left, and Right projections!",
                [
                    f"**Top view:** looking straight down shows {m(3)} unit squares (one atop each column).",
                    f"**Front and Back views:** each shows {m('3 + 2 + 1 = 6')} squares, contributing {m('2 \\times 6 = 12')} squares.",
                    f"**Left and Right views:** Left shows {m(3)} squares and Right shows {m('1 + 1 + 1 = 3')} step risers, contributing {m('3 + 3 = 6')} squares.",
                    f"Total painted area (excluding the {m(3)} bottom squares on the table) is {m('3 + 12 + 6 = 21\\text{ cm}^2')}.",
                ],
                f"Glue-seam check: {m('6 \\times 6 = 36')} total faces minus {m('2 \\times 6 = 12')} glued faces minus {m(3)} table faces = {m(21)}.",
                "احسب عدد المربعات الوحدوية المرئية من الأعلى والأمام والخلف واليسار واليمين!",
                [
                    f"**من الأعلى:** نرى {m(3)} مربعات وحدوية (مربع فوق كل عمود).",
                    f"**من الأمام والخلف:** يظهر في كل جهة {m('3 + 2 + 1 = 6')} مربعات، أي {m('2 \\times 6 = 12')} مربعاً.",
                    f"**من اليسار واليمين:** يظهر {m(3)} مربعات يساراً و{m(3)} مربعات على درجات اليمين، أي {m('3 + 3 = 6')} مربعات.",
                    f"إجمالي المساحة المطلية (دون المربعات الـ {m(3)} الملامسة للطاولة) هو {m('3 + 12 + 6 = 21\\text{ سم}^2')}.",
                ],
                f"تحقق بطرح الأوجه المخفية: {m('36 - 12\\text{ (ملتصقة)} - 3\\text{ (طاولة)} = 21')}.",
                diagram_en=svg_cube_stack_3d((3, 2, 1)),
            ),
        ],
        blueprints=[
            "kang_cad_painted_prism_cubes",
            "kang_cad_rolling_die_top",
            "kang_cad_ant_on_box_net",
            "kang_cad_hidden_stack_surface",
        ],
    )


def _lesson_3_5() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-05",
        level=LEVEL,
        unit_num="Lesson 3.5",
        topic="Combinatorics & Logic",
        title_en="Knights & Liars Circles, Checkerboard Parity, Blocked Street Grids & Tournament Scores",
        title_ar="دوائر الفرسان والكاذبين وتكافؤ رقعة الشطرنج ومسارات الشبكات المغلقة ونقاط البطولات",
        summary_en=(
            "Think like a Kangaroo Cadet medalist on logic and counting puzzles: chain implications around "
            "Knight–Liar circles, prove tiling limits with black-white checkerboard coloring, count grid "
            "detours by complementary subtraction or corner-by-corner DP, and decode tournament point totals."
        ),
        summary_ar=(
            "فكّر كأبطال الكانجارو في مسائل المنطق والعدّ لمستوى كاديت: اربط الاستنتاجات حول دوائر الصادقين "
            "والكاذبين، وأثبت حدود التبليط بتلوين رقعة الشطرنج، واحسب المسارات بقاعدة الطرح التكميلي أو جمع "
            "التقاطعات، وحلّل مجاميع نقاط البطولات الدورية."
        ),
        goals_en=[
            "Analyze **Knight (truth-teller) and Liar** statements around a circle to bound the minimum and maximum Knights.",
            "Use **2-coloring (checkerboard parity)** to bound domino tilings and alternating grid walks.",
            "Count **shortest lattice paths** around blocked intersections via \\( \\binom{m+n}{n} \\) subtraction or dynamic addition.",
            "Relate **total matches** \\( \\binom{n}{2} \\) to **total points** in \\( (3, 1, 0) \\) football/chess round-robin leagues.",
        ],
        goals_ar=[
            "تحليل عبارات **الفرسان (الصادقين) والكاذبين** حول طاولة دائرية لإيجاد أكبر وأصغر عدد ممكن للصادقين.",
            "استخدام **التلوين الثنائي (تكافؤ رقعة الشطرنج)** لتحديد أقصى عدد من قطع الدومينو ومسارات الشبكة.",
            "عدّ **أقصر المسارات الشبكية** مع وجود تقاطعات مغلقة عبر الطرح التكميلي للتوافيق أو الجمع المتدرج.",
            "ربط **إجمالي المباريات** \\( \\binom{n}{2} \\) **بمجموع النقاط الكلي** في بطولات الدوري ذات نظام \\( (3, 1, 0) \\).",
        ],
        concepts=[
            kang_concept(
                "1. Knights & Liars Around a Circle",
                "١. الفرسان الصادقون والكاذبون حول دائرة",
                f"Always test **both cases** for a speaker {m('X')}: (1) If {m('X')} is a **Knight**, the statement is **100% "
                f"true**; (2) If {m('X')} is a **Liar**, the statement is **false** (be careful: the negation of *'Both neighbors "
                f"are Liars'* is *'At least one neighbor is a Knight'*, NOT *'Both are Knights'*!). Lock in a small repeating "
                f"block (such as {m('K-L')} of length {m(2)} or {m('K-L-L')} of length {m(3)}) that tiles the circle!",
                f"اختبر دائماً **الحالتين** لأي متحدث {m('X')}: (١) إذا كان **فارساً صادقاً** فعبارته **صحيحة تماماً**؛ (٢) إذا كان "
                f"**كاذباً** فعبارته **خاطئة** (انتبه: نفي عبارة «جاراي كلاهما كاذبان» هو «أحد جاريّ على الأقل صادق» وليس كلاهما!). "
                f"استخرج نمطاً دورياً قصيراً مثل {m('K-L')} أو {m('K-L-L')} يغطي الدائرة بانتظام!",
                dm("\\neg(\\text{Both } L) \\iff \\text{At least one } K \\quad (\\text{blocks } K\\text{-}L \\text{ or } K\\text{-}L\\text{-}L)"),
                "نفي العبارة المزدوجة والأنماط الدورية على الدائرة:",
                dm("\\neg(\\text{كلاهما كاذب}) \\iff \\text{أحدهما صادق على الأقل}"),
                diagram_en=svg_kang_necklace_beads(["K", "L", "K", "L", "K", "L", "K", "L"]),
            ),
            kang_concept(
                "2. Checkerboard Parity & Domino Tilings",
                "٢. تلوين رقعة الشطرنج وتبليط الدومينو",
                f"Color grid cells alternately black and white like a chessboard. Every {m('1 \\times 2')} domino covers **exactly "
                f"1 black cell and 1 white cell**! Therefore, {m('k')} non-overlapping dominoes ALWAYS cover {m('k')} black and "
                f"{m('k')} white cells. If a mutilated board has {m('B')} black and {m('W')} white cells left, you can NEVER place "
                f"more than {m('\\min(B, W)')} dominoes—even if {m('B + W')} is even!",
                f"لوّن خلايا الشبكة بالتناوب بالأسود والأبيض كرقعة الشطرنج. كل قطعة دومينو {m('1 \\times 2')} تغطي **مربعاً أسود واحداً "
                f"ومربعاً أبيض واحداً بالضبط**! لذا فإن {m('k')} قطعة دومينو تغطي حتماً {m('k')} مربعاً أسود و{m('k')} مربعاً أبيض. "
                f"وإذا بقي في اللوحة {m('B')} أسود و{m('W')} أبيض، فلا يمكن أبداً وضع أكثر من {m('\\min(B, W)')} قطعة دومينو!",
                dm("1 \\text{ domino} = 1\\text{ Black} + 1\\text{ White} \\implies N_{\\text{dominoes}} \\le \\min(B, W)"),
                "شرط التكافؤ اللوني لتبليط الدومينو:",
                dm("N_{\\text{دومينو}} \\le \\min(B, W)"),
                diagram_en=svg_kang_polyomino_board([[-1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, -1]]),
            ),
            kang_concept(
                "3. Blocked Grid Paths & Round-Robin Point Invariants",
                "٣. مسارات الشبكة المغلقة وثوابت نقاط البطولات الدورية",
                f"Going {m('m')} steps East and {m('n')} steps North takes {m('\\binom{m+n}{n}')} shortest paths. If node "
                f"{m('P(a,b)')} is blocked, subtract the paths **through P**: {m('\\binom{m+n}{n} - \\binom{a+b}{b}\\binom{(m-a)+(n-b)}{n-b}')}. "
                f"In an {m('n')}-team round-robin league, there are {m('M = \\binom{n}{2}')} matches. Under **3-1-0** scoring, "
                f"every decisive game adds {m(3)} points to the league sum while every draw adds {m('1+1=2')} points, so "
                f"{m('\\text{Draws} = 3M - \\text{Total Points}')}!",
                f"الانتقال {m('m')} خطوة شرقاً و{m('n')} شمالاً له {m('\\binom{m+n}{n}')} مساراً قصيراً. عند إغلاق التقاطع {m('P(a,b)')} "
                f"اطرح المسارات المارة به: {m('\\binom{m+n}{n} - \\binom{a+b}{b}\\binom{(m-a)+(n-b)}{n-b}')}. وفي بطولة دوري من "
                f"{m('n')} فرق تُلعب {m('M = \\binom{n}{2}')} مباراة؛ في نظام **(3-1-0)** يضيف الفوز {m(3)} نقاط للمجموع الكلي بينما يضيف "
                f"التعادل نقطتين ({m('1+1')})، لذا فإن **عدد التعادلات** {m('= 3M - \\text{مجموع النقاط}')}!",
                dm("\\text{Paths}_{\\neg P} = \\binom{m+n}{n} - \\binom{a+b}{b}\\binom{m-a+n-b}{n-b}, \\qquad D = 3\\binom{n}{2} - S"),
                "طرح المسارات المحظورة وحساب عدد التعادلات:",
                dm("\\text{المسارات} = \\binom{m+n}{n} - \\binom{a+b}{b}\\binom{m-a+n-b}{n-b}, \\qquad D = 3\\binom{n}{2} - S"),
                diagram_en=svg_street_grid(4, 3, blocked=(2, 1)),
            ),
        ],
        traps_en=[
            "Trap: Negating *'All my neighbors are Liars'* into *'All my neighbors are Knights'*! The true logical negation of **all** is **not all** (at least one neighbor is a Knight).",
            "Trap: Dividing remaining squares by \\( 2 \\) without checking colors! A \\( 6 \\times 6 \\) board missing two opposite corners has \\( 34 \\) squares, yet \\( 17 \\) dominoes is **impossible** because opposite corners have the **same color**.",
            "Trap: Forgetting to divide by \\( 2 \\) in \\( \\binom{n}{2} = \\frac{n(n-1)}{2} \\)! Six teams play \\( 15 \\) matches in a single round-robin, not \\( 30 \\).",
        ],
        traps_ar=[
            "فخ شائع: نفي عبارة «كلا جاريّ كاذبان» إلى «كلا جاريّ صادقان»! النفي المنطقي الصحيح لـ (الكل) هو (ليس الكل)، أي أحد الجارين على الأقل صادق.",
            "فخ شائع: قسمة عدد المربعات المتبقية على \\( 2 \\) دون فحص الألوان! لوحة \\( 6 \\times 6 \\) حُذف منها ركنان متقابلان يتبقى فيها \\( 34 \\) مربعاً، لكن وضع \\( 17 \\) قطعة دومينو **مستحيل** لأن الركنين المتقابلين من **نفس اللون**.",
            "فخ شائع: نسيان القسمة على \\( 2 \\) في عدد المباريات \\( \\binom{n}{2} = \\frac{n(n-1)}{2} \\)! ستة فرق تلعب \\( 15 \\) مباراة في الدوري من دور واحد وليس \\( 30 \\).",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-05-EX1",
                "Worked Example 1 — Campfire Circle of Knights & Liars",
                "مثال محلول ١ — دائرة الفرسان والكاذبين حول النار",
                f"Twelve islanders (each a truth-telling **Knight** or an always-lying **Liar**) sit around a circular campfire. Every single person says: *\"Both of my immediate neighbors are Liars.\"* What is the **largest** possible number of Knights at the campfire?",
                f"يجلس اثنا عشر شخصاً من سكان الجزيرة (كلٌّ منهم إما **فارس صادق** دائماً أو **كاذب** دائماً) حول نار مخيم دائرية. قال كل شخص منهم: *«جاراي المجاوران لي كلاهما كاذبان»*. ما **أكبر** عدد ممكن للفرسان الصادقين حول النار؟",
                6,
                [3, 4, 5, 8],
                "No two Knights can sit adjacent; test whether alternating \\( K, L, K, L, \\dots \\) satisfies both Knights and Liars!",
                [
                    f"If a person is a **Knight**, their statement is true, so **both** of their neighbors must be Liars—meaning two Knights can never sit next to each other.",
                    f"Around a circle of {m(12)} seats, at most half the seats ({m('12 \\div 2 = 6')}) can be non-adjacent.",
                    f"Test the alternating pattern {m('K, L, K, L, \\dots')} repeated {m(6)} times: every Knight sits between two Liars (true!), and every Liar sits between two Knights, making *'both neighbors are Liars'* false (a valid lie!).",
                    f"Hence {m(6)} Knights is achievable and maximum.",
                ],
                f"Note: the **minimum** number of Knights would use {m('K, L, L')} repeated 4 times = {m(4)} Knights.",
                "لا يمكن أن يتجاور فارسان صادقان أبداً؛ اختبر النمط المتناوب \\( K, L, K, L, \\dots \\) حول الدائرة!",
                [
                    f"إذا كان المتحدث **فارساً صادقاً** فيجب أن يكون جاراه كاذبين معاً، مما يعني استحالة جلوس صادقين متجاورين.",
                    f"حول دائرة من {m(12)} مقعداً، أقصى عدد لمقاعد غير متجاورة هو النصف أي {m('12 \\div 2 = 6')}.",
                    f"نختبر التناوب {m('K, L, K, L, \\dots')}: كل صادق بين كاذبين (عبارته صحيحة)، وكل كاذب بين صادقين فعبارته «كلاهما كاذبان» خاطئة فعلاً!",
                    f"إذن أكبر عدد ممكن للفرسان الصادقين هو {m(6)}.",
                ],
                f"تحقق: النمط المتناوب يحقق شروط الصادقين الـ {m(6)} والكاذبين الـ {m(6)} دون أي تناقض.",
                diagram_en=svg_kang_necklace_beads(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]),
            ),
            kang_worked_example(
                "KANG-L3-05-EX2",
                "Worked Example 2 — Mutilated 6×6 Board Domino Cap",
                "مثال محلول ٢ — أقصى عدد لقطع الدومينو على لوحة 6×6 مقطوعة الركنين",
                f"From a standard {m('6 \\times 6')} checkerboard, two **diagonally opposite corner squares** are cut off, leaving {m(34)} unit squares. What is the **maximum** number of non-overlapping {m('1 \\times 2')} dominoes that can be placed on the remaining board?",
                f"من رقعة شطرنج قياسية أبعادها {m('6 \\times 6')} قُطع **مربعان في ركنين متقابلين قطرياً**، فبقي {m(34)} مربعاً صغيراً. ما **أكبر** عدد من قطع الدومينو {m('1 \\times 2')} غير المتداخلة التي يمكن وضعها على الرقعة المتبقية؟",
                16,
                [14, 15, 17, 18],
                "Opposite corners of an even-by-even board share the **same color**, leaving 16 cells of one color and 18 of the other!",
                [
                    f"A full {m('6 \\times 6')} checkerboard has {m(18)} black and {m(18)} white squares.",
                    f"Corners {m('(1,1)')} and {m('(6,6)')} both have even coordinate sums ({m('1+1=2')} and {m('6+6=12')}), so **both removed squares are the same color** (say black), leaving {m(16)} black and {m(18)} white squares.",
                    f"Each {m('1 \\times 2')} domino covers {m(1)} black and {m(1)} white square, so at most {m(16)} dominoes can ever be placed.",
                    f"Placing {m(2)} horizontal dominoes in Row 1, {m(3)} in each of Rows 2–5 ({m(12)} dominoes), and {m(2)} in Row 6 achieves {m('2 + 12 + 2 = 16')} dominoes!",
                ],
                f"{m(16)} dominoes cover {m(32)} squares (all {m(16)} black + {m(16)} white), leaving {m(2)} white squares uncovered.",
                "الركنان المتقابلان قطرياً في لوحة زوجية يحملان **اللون نفسه**، فيتبقى 16 مربعاً من لون و18 من اللون الآخر!",
                [
                    f"تحتوي لوحة {m('6 \\times 6')} الكاملة على {m(18)} مربعاً أسود و{m(18)} مربعاً أبيض.",
                    f"الركنان المتقابلان {m('(1,1)')} و{m('(6,6)')} لهما مجموع إحداثيات زوجي، أي أنهما من **نفس اللون** (أسود مثلاً)، فيبقى {m(16)} مربعاً أسود و{m(18)} أبيض.",
                    f"كل قطعة دومينو تغطي مربعاً أسود واحداً ومربعاً أبيض واحداً، لذا يستحيل وضع أكثر من {m(16)} قطعة.",
                    f"بوضع قطعتين في الصف الأول، و{m(3)} قطع في كلٍّ من الصفوف 2 إلى 5 ({m(12)} قطعة)، وقطعتين في الصف السادس نضع {m('2+12+2=16')} قطعة فعلاً!",
                ],
                f"تحقق: {m(16)} قطعة تغطي {m(32)} مربعاً ويتبقى مربعان أبيضان فقط.",
                diagram_en=svg_kang_polyomino_board([
                    [-1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, -1],
                ]),
            ),
            kang_worked_example(
                "KANG-L3-05-EX3",
                "Worked Example 3 — Detouring Around Roadwork on a Grid",
                "مثال محلول ٣ — المسارات القصيرة مع تقاطع مغلق",
                f"On the {m('4 \\times 3')} street grid shown, a courier walks from {m('A(0,0)')} to {m('B(4,3)')} moving only **East** or **North**. Intersection {m('P(2,1)')} is closed for roadwork. How many shortest paths from {m('A')} to {m('B')} avoid {m('P')}?",
                f"على شبكة الشوارع {m('4 \\times 3')} الموضحة، يسير مندوب من {m('A(0,0)')} إلى {m('B(4,3)')} متجهاً **شرقاً** أو **شمالاً** فقط. التقاطع {m('P(2,1)')} مغلق للصيانة. كم مساراً قصيراً من {m('A')} إلى {m('B')} يتجنب المرور بالتقاطع {m('P')}؟",
                17,
                [15, 18, 19, 23],
                "Subtract the shortest paths that pass through \\( P(2,1) \\) from all \\( \\binom{7}{3} \\) unrestricted shortest paths.",
                [
                    f"Without roadwork, every shortest path uses {m(4)} East and {m(3)} North steps: {m('\\binom{7}{3} = 35')} total paths.",
                    f"Paths from {m('A(0,0)')} to {m('P(2,1)')} use {m(2)} East and {m(1)} North step: {m('\\binom{3}{1} = 3')} paths.",
                    f"Paths from {m('P(2,1)')} to {m('B(4,3)')} use {m(2)} East and {m(2)} North steps: {m('\\binom{4}{2} = 6')} paths.",
                    f"By the multiplication rule, {m('3 \\times 6 = 18')} paths hit {m('P')}, leaving {m('35 - 18 = 17')} valid paths!",
                ],
                f"{m('17 + 18 = 35 = \\binom{7}{3}')}. Confirmed!",
                "اطرح عدد المسارات المارة بالتقاطع \\( P(2,1) \\) من إجمالي المسارات الكلية \\( \\binom{7}{3} \\).",
                [
                    f"دون إغلاق، يحتاج أي مسار قصير إلى {m(4)} خطوات شرقاً و{m(3)} شمالاً: الإجمالي {m('\\binom{7}{3} = 35')} مساراً.",
                    f"من {m('A(0,0)')} إلى {m('P(2,1)')} يوجد {m('\\binom{2+1}{1} = 3')} مسارات.",
                    f"ومن {m('P(2,1)')} إلى {m('B(4,3)')} يوجد {m('\\binom{2+2}{2} = 6')} مسارات.",
                    f"إذن يمر بالتقاطع المغلق {m('3 \\times 6 = 18')} مساراً، ويبقى {m('35 - 18 = 17')} مساراً متاحاً!",
                ],
                f"تحقق: {m('17 + 18 = 35 = \\binom{7}{3}')}.",
                diagram_en=svg_street_grid(4, 3, blocked=(2, 1)),
            ),
            kang_worked_example(
                "KANG-L3-05-EX4",
                "Worked Example 4 — Counting Draws in a 6-Club League",
                "مثال محلول ٤ — حساب عدد التعادلات في بطولة من 6 أندية",
                f"Six football clubs play a single round-robin tournament (each pair plays once). A win awards **3 points** to the winner and **0** to the loser; a draw gives **1 point** to each club. After all matches finish, the sum of all six clubs' points is {m(39)}. How many matches ended in a **draw**?",
                f"تتنافس ستة أندية في بطولة دوري من دور واحد (يلعب كل ناديين معاً مباراة واحدة). يمنح الفوز **3 نقاط** للفائز و**0** للخاسر، ويمنح التعادل **نقطة واحدة** لكل نادٍ. بعد انتهاء جميع المباريات بلغ مجموع نقاط الأندية الستة معاً {m(39)} نقطة. كم مباراة انتهت **بالتعادل**؟",
                6,
                [3, 4, 5, 9],
                "Find total matches \\( \\binom{6}{2} = 15 \\); each draw reduces the maximum possible league sum \\( 3 \\times 15 = 45 \\) by exactly \\( 1 \\) point!",
                [
                    f"Total matches played among {m(6)} clubs is {m('\\binom{6}{2} = \\frac{6 \\times 5}{2} = 15')}.",
                    f"Every decisive match adds {m('3 + 0 = 3')} points to the league total, while every draw adds {m('1 + 1 = 2')} points.",
                    f"If all {m(15)} matches had a winner, total points would be {m('15 \\times 3 = 45')}.",
                    f"Each draw drops the total by {m('3 - 2 = 1')} point, so the number of draws is {m('45 - 39 = 6')}.",
                ],
                f"{m(9)} wins ({m('9 \\times 3 = 27')} pts) + {m(6)} draws ({m('6 \\times 2 = 12')} pts) = {m(15)} games and {m('27 + 12 = 39')} pts!",
                "احسب عدد المباريات \\( \\binom{6}{2} = 15 \\)؛ كل تعادل يُنقص المجموع الأقصى للنقاط \\( 45 \\) بمقدار نقطة واحدة بالضبط!",
                [
                    f"إجمالي عدد المباريات بين {m(6)} أندية يساوي {m('\\binom{6}{2} = \\frac{6 \\times 5}{2} = 15')} مباراة.",
                    f"كل مباراة تحسم بالفوز تضيف {m(3)} نقاط للمجموع الكلي، بينما يضيف التعادل {m('1 + 1 = 2')} نقطتين فقط.",
                    f"لو انتهت جميع الـ {m(15)} مباراة بالفوز لكان المجموع {m('15 \\times 3 = 45')} نقطة.",
                    f"كل تعادل يُنقص المجموع نقطة واحدة ({m('3 - 2 = 1')})، لذا فعدد التعادلات هو {m('45 - 39 = 6')} مباريات.",
                ],
                f"تحقق: {m(9)} انتصارات ({m(27)} نقطة) + {m(6)} تعادلات ({m(12)} نقطة) = {m(39)} نقطة!",
                diagram_en=svg_graph_cycle_chords(6, full_kn=True),
            ),
        ],
        blueprints=[
            "kang_cad_knights_liars_circle",
            "kang_cad_domino_parity_hole",
            "kang_cad_blocked_grid_paths",
            "kang_cad_round_robin_points",
        ],
    )


def _lesson_3_6() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L3-06",
        level=LEVEL,
        unit_num="Lesson 3.6",
        topic="Data & Probability",
        title_en="Weighted Group Means, Two-Step Bag Draws, 3-Set Venn Counts & Binary Bulb Codes",
        title_ar="المتوسطات المرجحة والسحب دون إرجاع ومخططات فن الثلاثية وشفرات المصابيح الثنائية",
        summary_en=(
            "Finish the Cadet curriculum by mastering Kangaroo data, set, probability, and binary puzzles: "
            "convert group averages into total sums, adjust denominators on without-replacement draws, peel "
            "3-set Venn diagrams from the center outward, and decode binary switchboards using powers of two."
        ),
        summary_ar=(
            "اختتم منهج كاديت بإتقان ألغاز البيانات والمجموعات والاحتمالات والشفرات الثنائية: حوّل متوسطات "
            "المجموعات إلى مجاميع كلية، وعدّل المقامات عند السحب دون إرجاع، واملأ مخططات فن الثلاثية من المركز "
            "نحو الخارج، وفكّ شفرات لوحات المصابيح الثنائية بقوى العدد 2."
        ),
        goals_en=[
            "Compute **weighted group means** and outlier shifts by always tracking **Total Sum = Count × Mean**.",
            "Calculate **two-step probabilities without replacement** by updating both numerator and denominator after Draw 1.",
            "Solve **3-set Venn puzzles** from the triple intersection outward or via Inclusion–Exclusion.",
            "Decode **binary light-bulb panels** and toggle-switch parity using powers of two \\( (16, 8, 4, 2, 1) \\).",
        ],
        goals_ar=[
            "حساب **المتوسطات المرجحة للمجموعات** وتأثير القيم المضافة أو المحذوفة عبر قانون **المجموع الكلي = العدد × المتوسط**.",
            "حساب **احتمالات السحب على خطوتين دون إرجاع** بتحديث البسط والمقام بعد السحبة الأولى.",
            "حلّ **مخططات فن ذات المجموعات الثلاث** انطلاقاً من التقاطع الثلاثي الأوسط نحو الخارج أو بمبدأ التضمين والإقصاء.",
            "فكّ شفرات **لوحات المصابيح الثنائية** وتبديل المفاتيح باستخدام قوى العدد اثنين \\( (16, 8, 4, 2, 1) \\).",
        ],
        concepts=[
            kang_concept(
                "1. Weighted Group Means & Balancing Deviations",
                "١. المتوسطات المرجحة للمجموعات وموازنة الفروق",
                f"Never average two group means directly when the group sizes differ! Convert every average into a **total sum** "
                f"first: if {m('n_1')} items have mean {m('\\mu_1')} and {m('n_2')} items have mean {m('\\mu_2')}, the combined "
                f"mean is {m('\\frac{n_1 \\mu_1 + n_2 \\mu_2}{n_1 + n_2}')}.Notice the combined mean always sits **closer to the "
                f"larger group's mean**, splitting the gap in inverse proportion {m('n_2 : n_1')}!",
                f"لا تجمع متوسطَي مجموعتين وتقسمهما على 2 أبداً عندما يختلف عدد عناصرهما! حوّل كل متوسط إلى **مجموع كلي** أولاً: "
                f"المتوسط المشترك هو {m('\\frac{n_1 \\mu_1 + n_2 \\mu_2}{n_1 + n_2}')}. لاحظ أن المتوسط المشترك ينجذب دائماً **نحو "
                f"المجموعة الأكبر عدداً** ويقسم المسافة بين المتوسطين بنسبة عكسية {m('n_2 : n_1')}!",
                dm("\\mu_{\\text{all}} = \\frac{n_1 \\mu_1 + n_2 \\mu_2}{n_1 + n_2}, \\qquad S = n \\cdot \\mu"),
                "قانون المتوسط المرجح للمجموعات:",
                dm("\\mu_{\\text{الكل}} = \\frac{n_1 \\mu_1 + n_2 \\mu_2}{n_1 + n_2}"),
                diagram_en=svg_bar_chart([("G₁ (n₁)", 85, "μ₁"), ("G₂ (n₂)", 65, "μ₂"), ("All", 77, "μ")], y_max=100),
            ),
            kang_concept(
                "2. Two-Step Draws Without Replacement & 3-Set Venn Peeling",
                "٢. السحب دون إرجاع وتقشير مخططات فن الثلاثية",
                f"When drawing 2 items **without replacement** from {m('N')} items, the second draw has denominator {m('N - 1')}! "
                f"For same-color pairs with {m('r')} red and {m('b')} blue ({m('N = r+b')}), add the disjoint branches: "
                f"{m('\\frac{r(r-1) + b(b-1)}{N(N-1)}')}. In **3-set Venn puzzles**, ALWAYS write the **center triple overlap "
                f"{m('|A\\cap B\\cap C|')} first**, subtract it from each pairwise overlap, and work outward!",
                f"عند سحب عنصرين **دون إرجاع** من أصل {m('N')} عنصراً، يصبح مقام السحبة الثانية {m('N - 1')}! للحصول على لون متماثل "
                f"اجمع الفرعين المانعين لبعضهما: {m('\\frac{r(r-1) + b(b-1)}{N(N-1)}')}. وفي **مخططات فن الثلاثية** ابدأ دائماً بكتابة "
                f"**التقاطع الثلاثي الأوسط {m('|A\\cap B\\cap C|')} أولاً** ثم اطرحه من كل تقاطع ثنائي متجهاً للخارج!",
                dm("|A \\cup B \\cup C| = |A|+|B|+|C| - |A\\cap B| - |B\\cap C| - |A\\cap C| + |A\\cap B\\cap C|"),
                "مبدأ التضمين والإقصاء لثلاث مجموعات:",
                dm("|A \\cup B \\cup C| = |A|+|B|+|C| - |A\\cap B| - |B\\cap C| - |A\\cap C| + |A\\cap B\\cap C|"),
                diagram_en=svg_venn_3("A", "B", "C", {"a": "a", "b": "b", "c": "c", "ab": "ab", "bc": "bc", "ac": "ac", "abc": "x"}),
            ),
            kang_concept(
                "3. Binary Powers of Two & Switch-Toggle Parity",
                "٣. الأعداد الثنائية بقوى العدد 2 وتكافؤ تبديل المفاتيح",
                f"Because {m('1, 2, 4, 8, 16, \\dots')} double each step, **every integer from {m(0)} to {m('2^k - 1')} has a "
                f"unique subset of ON bulbs**! Also remember switch parity: toggling any bulb an **even** number of times leaves it "
                f"**unchanged**, whereas toggling it an **odd** number of times **reverses** its state ({m('\\text{ON} \\leftrightarrow \\text{OFF}')}).",
                f"لأن الأوزان {m('1, 2, 4, 8, 16, \\dots')} تتضاعف في كل خطوة، فإن **كل عدد صحيح من {m(0)} إلى {m('2^k - 1')} يُمثَّل "
                f"بتشكيلة وحيدة من المصابيح المضاءة**! وتذكّر تكافؤ المفاتيح: تبديل حالة أي مصباح عدداً **زوجياً** من المرات يبقيه **كما كان**، "
                f"بينما تبديله عدداً **فردياً** من المرات **يعكس** حالته ({m('\\text{مضاء} \\leftrightarrow \\text{مطفأ}')}).",
                dm("N = \\sum_{i=0}^{k-1} b_i 2^i \\quad (b_i \\in \\{0,1\\}), \\qquad \\text{odd toggles} \\implies 1 - b_i"),
                "التمثيل الثنائي الوحيد وتكافؤ عدد التبديلات:",
                dm("N = \\sum_{i=0}^{k-1} b_i 2^i, \\qquad \\text{تبديل فردي} \\implies 1 - b_i"),
                diagram_en=svg_binary_bulbs((1, 0, 1, 1, 0), (16, 8, 4, 2, 1)),
            ),
        ],
        traps_en=[
            "Trap: Computing \\( \\left(\\frac{5}{8}\\right)^2 + \\left(\\frac{3}{8}\\right)^2 \\) when balls are drawn **without replacement**! Once the first ball stays out, only \\( 7 \\) balls remain in the bag.",
            "Trap: Subtracting \\( |A\\cap B| + |B\\cap C| + |A\\cap C| \\) in a 3-set Venn diagram and forgetting to **add back** \\( +|A\\cap B\\cap C| \\), which got subtracted three times after being added three times!",
            "Trap: Confusing the **number of switches** with the **highest weight**! Five binary bulbs have weights \\( 1, 2, 4, 8, 16 \\) (highest is \\( 2^4 = 16 \\), maximum sum is \\( 2^5 - 1 = 31 \\)).",
        ],
        traps_ar=[
            "فخ شائع: حساب \\( \\left(\\frac{5}{8}\\right)^2 + \\left(\\frac{3}{8}\\right)^2 \\) في مسائل السحب **دون إرجاع**! بعد إخراج الكرة الأولى يتبقى في الكيس \\( 7 \\) كرات فقط.",
            "فخ شائع: طرح التقاطعات الثنائية الثلاثة ونسيان **إعادة جمع** التقاطع الثلاثي الأوسط \\( +|A\\cap B\\cap C| \\) الذي أُضيف 3 مرات وطُرح 3 مرات!",
            "فخ شائع: الخلط بين **عدد المصابيح** و**أكبر وزن ثنائي**! خمسة مصابيح أوزانها \\( 1, 2, 4, 8, 16 \\) (أكبرها \\( 2^4 = 16 \\) وأقصى مجموع لها \\( 2^5 - 1 = 31 \\)).",
        ],
        examples=[
            kang_worked_example(
                "KANG-L3-06-EX1",
                "Worked Example 1 — Combining Two Robotics Squads",
                "مثال محلول ١ — دمج متوسطَي فريقين للروبوتات",
                f"In a school robotics club, {m(12)} students in Squad Alpha scored a mean of {m(85)} points, and {m(8)} students in Squad Beta scored a mean of {m(75)} points. What is the mean score of all {m(20)} students combined?",
                f"في نادي الروبوتات المدرسي، حقق {m(12)} طالباً في الفريق (ألفا) متوسطاً قدره {m(85)} نقطة، وحقق {m(8)} طلاب في الفريق (بيتا) متوسطاً قدره {m(75)} نقطة. ما المتوسط الحسابي لجميع الطلاب الـ {m(20)} معاً؟",
                81,
                [79, 80, 82, 83],
                "Multiply each squad's count by its mean to find the grand total of points, then divide by \\( 20 \\).",
                [
                    f"Squad Alpha's total points = {m('12 \\times 85 = 1020')}.",
                    f"Squad Beta's total points = {m('8 \\times 75 = 600')}.",
                    f"Grand total across all {m('12 + 8 = 20')} students is {m('1020 + 600 = 1620')} points.",
                    f"Combined mean = {m('1620 \\div 20 = 81')} points.",
                ],
                f"{m(81)} sits closer to {m(85)} than {m(75)}, splitting the {m(10)}-point gap in ratio {m('4 : 6 = 8 : 12')}!",
                "اضرب عدد طلاب كل فريق في متوسطه لإيجاد مجموع النقاط الكلي، ثم اقسم على \\( 20 \\).",
                [
                    f"مجموع نقاط الفريق (ألفا) = {m('12 \\times 85 = 1020')} نقطة.",
                    f"مجموع نقاط الفريق (بيتا) = {m('8 \\times 75 = 600')} نقطة.",
                    f"المجموع الكلي لجميع الـ {m(20)} طالباً هو {m('1020 + 600 = 1620')} نقطة.",
                    f"المتوسط المشترك = {m('1620 \\div 20 = 81')} نقطة.",
                ],
                f"تحقق: العدد {m(81)} أقرب إلى {m(85)} منه إلى {m(75)} بنسبة {m('8 : 12')} تماماً!",
                diagram_en=svg_bar_chart([("Alpha (12)", 85, "85"), ("Beta (8)", 75, "75"), ("All (20)", 81, "?")], y_max=100),
            ),
            kang_worked_example(
                "KANG-L3-06-EX2",
                "Worked Example 2 — Matching Gem Tokens Without Replacement",
                "مثال محلول ٢ — سحب قطعتين متماثلتي اللون دون إرجاع",
                f"A velvet pouch contains {m(5)} ruby tokens and {m(3)} emerald tokens. Two tokens are drawn at random one after another **without replacement**. What is the probability that **both** tokens have the **same color**?",
                f"يحتوي كيس مخملي على {m(5)} قطع ياقوتية حمراء و{m(3)} قطع زمردية خضراء. سُحبت قطعتان عشوائياً الواحدة تلو الأخرى **دون إرجاع**. ما احتمال أن تكون القطعتان من **اللون نفسه**؟",
                Fraction(13, 28),
                [Fraction(5, 14), Fraction(15, 32), Fraction(17, 32), Fraction(15, 28)],
                "Add the probability of two rubies \\( \\frac{5}{8}\\cdot\\frac{4}{7} \\) and the probability of two emeralds \\( \\frac{3}{8}\\cdot\\frac{2}{7} \\).",
                [
                    f"There are {m('5 + 3 = 8')} tokens initially, and {m(7)} remain for the second draw.",
                    f"Probability both are ruby: {m('\\frac{5}{8} \\times \\frac{4}{7} = \\frac{20}{56}')}.",
                    f"Probability both are emerald: {m('\\frac{3}{8} \\times \\frac{2}{7} = \\frac{6}{56}')}.",
                    f"Adding the two disjoint cases gives {m('\\frac{20 + 6}{56} = \\frac{26}{56} = \\frac{13}{28}')}.",
                ],
                f"Complement check: mixed colors occur with probability {m('2 \\times \\frac{5 \\times 3}{8 \\times 7} = \\frac{30}{56} = \\frac{15}{28}')}, and {m('\\frac{13}{28} + \\frac{15}{28} = 1')}.",
                "اجمع احتمال سحب قطعتين حمراوين \\( \\frac{5}{8}\\cdot\\frac{4}{7} \\) مع احتمال سحب قطعتين خضراوين \\( \\frac{3}{8}\\cdot\\frac{2}{7} \\).",
                [
                    f"يوجد في البداية {m('5 + 3 = 8')} قطع، ويتبقى {m(7)} قطع عند السحبة الثانية.",
                    f"احتمال أن تكونا حمراوين معاً: {m('\\frac{5}{8} \\times \\frac{4}{7} = \\frac{20}{56}')}.",
                    f"احتمال أن تكونا خضراوين معاً: {m('\\frac{3}{8} \\times \\frac{2}{7} = \\frac{6}{56}')}.",
                    f"بجمع الحالتين نحصل على {m('\\frac{20 + 6}{56} = \\frac{26}{56} = \\frac{13}{28}')}.",
                ],
                f"تحقق بالمتمم: احتمال اختلاف اللونين {m('\\frac{30}{56} = \\frac{15}{28}')}، ومجموعهما {m('\\frac{13+15}{28} = 1')}.",
                diagram_en=svg_spinner([(5 / 8, "5 R"), (3 / 8, "3 E")]),
            ),
            kang_worked_example(
                "KANG-L3-06-EX3",
                "Worked Example 3 — Three-Club Kangaroo Camp Survey",
                "مثال محلول ٣ — استبيان الأندية الثلاثة بمخطط فن",
                f"Among {m(50)} Kangaroo campers, {m(26)} play Chess, {m(24)} do Logic puzzles, and {m(22)} practice Origami. Exactly {m(11)} do both Chess and Logic, {m(10)} do both Logic and Origami, {m(9)} do both Chess and Origami, and {m(5)} do **all three**. How many campers do **none** of the three activities?",
                f"من بين {m(50)} مشاركاً في معسكر الكانجارو، يمارس {m(26)} الشطرنج، و{m(24)} ألغاز المنطق، و{m(22)} فن الأوريغامي. إذا كان {m(11)} يمارسون الشطرنج والمنطق معاً، و{m(10)} المنطق والأوريغامي معاً، و{m(9)} الشطرنج والأوريغامي معاً، و{m(5)} يمارسون **الأنشطة الثلاثة جميعاً**، فكم مشاركاً **لا يمارس أياً** من هذه الأنشطة الثلاثة؟",
                3,
                [0, 5, 8, 13],
                "Apply 3-set Inclusion–Exclusion to find \\( |C \\cup L \\cup O| \\), then subtract from \\( 50 \\).",
                [
                    f"Sum the single-activity totals: {m('26 + 24 + 22 = 72')}.",
                    f"Subtract the pairwise overlaps: {m('72 - (11 + 10 + 9) = 72 - 30 = 42')}.",
                    f"Add back the triple overlap: {m('|C \\cup L \\cup O| = 42 + 5 = 47')} campers in at least one activity.",
                    f"Campers in **none** of the three = {m('50 - 47 = 3')}.",
                ],
                f"Region-by-region check: {m('11 + 8 + 8 + 6 + 5 + 4 + 5 = 47')}, plus {m(3)} outside = {m(50)}!",
                "طبّق مبدأ التضمين والإقصاء لإيجاد \\( |C \\cup L \\cup O| \\) ثم اطرح الناتج من \\( 50 \\).",
                [
                    f"نجمع أعداد المجموعات الثلاث: {m('26 + 24 + 22 = 72')}.",
                    f"نطرح التقاطعات الثنائية: {m('72 - (11 + 10 + 9) = 72 - 30 = 42')}.",
                    f"نضيف التقاطع الثلاثي الأوسط: {m('|C \\cup L \\cup O| = 42 + 5 = 47')} مشاركاً في نشاط واحد على الأقل.",
                    f"إذن عدد الذين لا يمارسون أي نشاط هو {m('50 - 47 = 3')} مشاركين.",
                ],
                f"تحقق بالمناطق السبع: {m('11 + 8 + 8 + 6 + 5 + 4 + 5 = 47')}، والباقي خارج الدوائر {m(3)}!",
                diagram_en=svg_venn_3("C (26)", "L (24)", "O (22)", {"a": "?", "b": "?", "c": "?", "ab": "6", "bc": "5", "ac": "4", "abc": "5"}),
            ),
            kang_worked_example(
                "KANG-L3-06-EX4",
                "Worked Example 4 — Toggling a Binary Bulb Panel",
                "مثال محلول ٤ — تبديل لوحة المصابيح الثنائية",
                f"Five bulbs carry weights {m('16, 8, 4, 2, 1')} from left to right and currently show **(ON, OFF, ON, ON, OFF)** as illustrated. Pressing Button X flips the state of the **three rightmost** bulbs ({m('4, 2, 1')}). What is the sum of the weights of all **ON** bulbs after pressing Button X once?",
                f"تحمل خمسة مصابيح الأوزان {m('16, 8, 4, 2, 1')} من اليسار إلى اليمين وتظهر حالياً بالحالة **(مضاء، مطفأ، مضاء، مضاء، مطفأ)** كما في الشكل. الضغط على الزر X يعكس حالة **المصابيح الثلاثة اليمنى** ({m('4, 2, 1')}). ما مجموع أوزان المصابيح **المضاءة** بعد الضغط على الزر X مرة واحدة؟",
                17,
                [9, 15, 19, 22],
                "Keep the two leftmost bits unchanged and invert each of the three rightmost bits!",
                [
                    f"Initial bit pattern for weights {m('(16, 8, 4, 2, 1)')} is {m('(1, 0, 1, 1, 0)')} (currently summing to {m('16+4+2=22')}).",
                    f"The two leftmost bulbs stay {m('(1, 0)')}, while the three rightmost bulbs {m('(1, 1, 0)')} flip to {m('(0, 0, 1)')}.",
                    f"The new pattern is {m('(1, 0, 0, 0, 1)')}, so only weights {m(16)} and {m(1)} are ON.",
                    f"New lit weight sum = {m('16 + 1 = 17')}.",
                ],
                f"Flipping {m('(4,2,1)')} replaces {m('4+2=6')} with {m('7 - 6 = 1')}, so {m('22 - 6 + 1 = 17')}!",
                "أبقِ المصباحين الأيسرين كما هما واعكس حالة كل مصباح من المصابيح الثلاثة اليمنى!",
                [
                    f"الحالة الابتدائية للأوزان {m('(16, 8, 4, 2, 1)')} هي {m('(1, 0, 1, 1, 0)')} (مجموعها الابتدائي {m(22)}).",
                    f"المصباحان الأيسران يبقيان {m('(1, 0)')}، وتنعكس الثلاثة اليمنى من {m('(1, 1, 0)')} إلى {m('(0, 0, 1)')}.",
                    f"تصبح الحالة الجديدة {m('(1, 0, 0, 0, 1)')}، أي أن المضاءين هما الوزنان {m(16)} و{m(1)} فقط.",
                    f"مجموع الأوزان المضاءة الجديد = {m('16 + 1 = 17')}.",
                ],
                f"تحقق سريع: عكس الأوزان {m('(4,2,1)')} التي مجموعها {m(7)} يستبدل {m(6)} بـ {m('7-6=1')}، فيصبح المجموع {m('16 + 1 = 17')}!",
                diagram_en=svg_binary_bulbs((1, 0, 1, 1, 0), (16, 8, 4, 2, 1)),
            ),
        ],
        blueprints=[
            "kang_cad_weighted_group_mean",
            "kang_cad_without_replacement_prob",
            "kang_cad_three_set_venn",
            "kang_cad_binary_bulb_switches",
        ],
    )


def get_cadet_lessons() -> list[dict]:
    """Return all 6 Cadet (Grades 7–8) Kangaroo study lessons."""
    return [
        _lesson_3_1(),
        _lesson_3_2(),
        _lesson_3_3(),
        _lesson_3_4(),
        _lesson_3_5(),
        _lesson_3_6(),
    ]
