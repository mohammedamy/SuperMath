"""Rich Bilingual Study Lessons for Kangaroo Math Competition — Ecolier Division (Grades 3–4)."""

from kangaroo_common import (
    dm,
    kang_concept,
    kang_worked_example,
    m,
    make_kangaroo_lesson,
    svg_analog_clock,
    svg_balance_scales,
    svg_bar_chart,
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digital_clock,
    svg_digit_slots,
    svg_fenceposts,
    svg_fraction_grid,
    svg_function_machine,
    svg_kang_cube_faces,
    svg_kang_folded_ribbon,
    svg_kang_grid_walk,
    svg_kang_magic_cross,
    svg_kang_matchstick_digits,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_overlapping_rects,
    svg_kang_polyomino_board,
    svg_kang_staircase_perimeter,
    svg_kang_stamp_grid,
    svg_magic_square_3x3,
    svg_matchstick_squares,
    svg_matchstick_triangles,
    svg_number_line_jumps,
    svg_number_strip,
    svg_pie_chart,
)

LEVEL = "Ecolier"


def _lesson_1_1() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-01",
        level=LEVEL,
        unit_num="Lesson 1.1",
        topic="Number Theory",
        title_en="Skip-Counting Jumps, Place-Value Digits & Brick Number Pyramids",
        title_ar="قفزات العدّ النمطي، والقيمة المنزلية للأرقام، وأهرامات الطوب العددية",
        summary_en=(
            "Welcome to Kangaroo Ecolier! Learn how numbers climb inside brick pyramids, "
            "how Kangy hops along a number line without falling for the 'last jump' trick, "
            "how to arrange digit cards using place value, and why 9 trees make only 8 gaps."
        ),
        summary_ar=(
            "مرحباً بك في مستوى إيكولير لمسابقة الكنغر! تعلّم كيف تتصاعد الأعداد داخل أهرامات الطوب، "
            "وكيف يقفز الكنغر على خط الأعداد دون الوقوع في فخ القفزة الأخيرة، "
            "وكيف ترتّب بطاقات الأرقام بالقيمة المنزلية، ولماذا تصنع 9 أشجار 8 مسافات فقط."
        ),
        goals_en=[
            "Solve **3-row and 4-row brick number pyramids** forward and backward by spotting which bricks are added twice.",
            "Track **skip-counting and forward-backward kangaroo hops**, checking when the target is reached before sliding back.",
            "Build the **largest and smallest multi-digit numbers** from digit cards without placing **0** at the front.",
            "Apply the **Fencepost Rule**: the number of gaps between items in a straight line is always **1 less** than the number of items.",
        ],
        goals_ar=[
            "حل **أهرامات الطوب العددية من 3 و4 صفوف** صعوداً ونزولاً مع ملاحظة الطوبة الوسطى التي تُجمع مرتين.",
            "تتبّع **قفزات العدّ النمطي والقفز للأمام والخلف** والانتباه لحظة الوصول إلى الهدف قبل التراجع.",
            "تكوين **أكبر وأصغر عدد** من بطاقات الأرقام مع تذكّر أن الصفر **0** لا يوضع في المنزلة اليسرى الكبرى.",
            "تطبيق **قاعدة الأعمدة والمسافات**: عدد المسافات في صف مستقيم يساوي دائماً **عدد الأشياء ناقص 1**.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Brick Number Pyramids & the Double-Middle Secret",
                title_ar="١. أهرامات الطوب العددية وسرّ الطوبة الوسطى المضاعفة",
                body_en=(
                    f"In a Kangaroo number pyramid, each brick holds the **sum of the two bricks right below it**. "
                    f"If the bottom row has {m('a')}, {m('b')}, and {m('c')}, then the middle row has {m('a + b')} and {m('b + c')}. "
                    f"Notice that the middle brick {m('b')} climbs into **both** upper neighbors, so the top brick equals {m('a + 2b + c')}! "
                    f"Whenever a brick is missing, work step-by-step from any pair of known bricks or subtract backward."
                ),
                body_ar=(
                    f"في هرم الكنغر العددي، كل طوبة تساوي **مجموع الطوبتين الموجودتين أسفلها مباشرة**. "
                    f"إذا كان الصف السفلي يضم {m('a')} و{m('b')} و{m('c')}، فإن الصف الأوسط يضم {m('a + b')} و{m('b + c')}. "
                    f"لاحظ أن الطوبة الوسطى {m('b')} تدخل في الطوبتين معاً، لذلك تساوي طوبة القمة {m('a + 2b + c')}! "
                    f"عند البحث عن طوبة مفقودة، ابدأ من أي طوبتين معلوشتين بالجمع صعوداً أو بالطرح نزولاً."
                ),
                formula_en=dm("\\text{Left Mid} = a + b, \\qquad \\text{Right Mid} = b + c, \\qquad \\text{Top} = a + 2b + c"),
                caption_ar="قاعدة هرم الطوب ذي الثلاثة صفوف:",
                formula_math_ar=dm("\\text{Top} = (a + b) + (b + c) = a + 2b + c"),
                diagram_en=svg_kang_number_pyramid([["33"], ["14", "19"], ["6", "8", "11"]]),
            ),
            kang_concept(
                title_en="2. Kangaroo Hops & the Fencepost Gap Rule",
                title_ar="٢. قفزات الكنغر وقاعدة الأعمدة والمسافات",
                body_en=(
                    f"Hold up {m(5)} fingers on your hand and count the spaces between them—there are only {m(4)} spaces! "
                    f"In a straight row, **Gaps = Posts − 1** and **Posts = Gaps + 1**. "
                    f"Also, when Kangy jumps {m('+5')} forward during the day and slides {m('-2')} back at night, his net gain per full day-and-night is {m('5 - 2 = 3')}, "
                    f"but as soon as a daytime jump reaches the finish stone, **he stops right there** without sliding back!"
                ),
                body_ar=(
                    f"ارفع {m(5)} أصابع في يدك وعدّ الفراغات بينها: ستجد {m(4)} فراغات فقط! "
                    f"في أي صف مستقيم، **عدد المسافات = عدد العلامات − 1** و**عدد العلامات = عدد المسافات + 1**. "
                    f"كذلك عندما يقفز الكنغر {m('+5')} خطوات نهاراً ويتراجع {m('-2')} ليلاً، فإن تقدّمه الصافي في اليوم الكامل هو {m('5 - 2 = 3')}، "
                    f"لكن بمجرد وصوله إلى حجر النهاية في قفزة النهار **يتوقف فوراً** ولا يتراجع بعدها!"
                ),
                formula_en=dm("\\text{Gaps} = \\text{Posts} - 1, \\qquad \\text{Total Distance} = (\\text{Posts} - 1) \\times \\text{Gap}"),
                caption_ar="العلاقة الذهبية بين عدد العلامات وعدد المسافات:",
                formula_math_ar=dm("\\text{Distance} = (N - 1) \\times d"),
                diagram_en=svg_fenceposts("6 m", "48 m"),
            ),
            kang_concept(
                title_en="3. Place-Value Digit Cards & Zero Watch",
                title_ar="٣. بطاقات القيمة المنزلية والانتباه لبطاقة الصفر",
                body_en=(
                    f"In a 4-digit number, the **thousands place** carries the biggest weight ({m(1000)}), followed by hundreds ({m(100)}), tens ({m(10)}), and ones ({m(1)}). "
                    f"To build the **largest** number, put your biggest digits on the left from greatest to least. "
                    f"To build the **smallest** number, put your smallest **non-zero** digit first on the left, then place {m(0)} right after it in the hundreds spot!"
                ),
                body_ar=(
                    f"في العدد المكوّن من 4 أرقام، تحمل **منزلة الآلاف** أكبر قيمة ({m(1000)})، تليها المئات ({m(100)}) ثم العشرات ({m(10)}) فالآحاد ({m(1)}). "
                    f"لتكوين **أكبر عدد** نرتّب الأرقام تنازلياً من اليسار إلى اليمين. "
                    f"أما لتكوين **أصغر عدد** فنضع أصغر رقم **غير صفري** في أقصى اليسار أولاً، ثم نضع الصفر {m(0)} بعده مباشرة في منزلة المئات!"
                ),
                formula_en=dm("\\overline{abcd} = 1000a + 100b + 10c + d \\quad (a \\neq 0)"),
                caption_ar="تفكيك العدد الرباعي حسب القيمة المنزلية:",
                formula_math_ar=dm("\\overline{abcd} = 1000a + 100b + 10c + d \\quad (a \\neq 0)"),
                diagram_en=svg_digit_slots(["1", "0", "4", "8"], "Smallest 4-digit = 1048"),
                diagram_ar=svg_digit_slots(["1", "0", "4", "8"], "أصغر عدد رباعي = 1048"),
            ),
        ],
        traps_en=[
            "Trap: Multiplying the total number of trees by the gap! For 9 trees spaced 6 m apart, there are 8 gaps (48 m), NOT 9 × 6 = 54 m.",
            "Trap: Putting 0 in the leftmost spot of a 4-digit number! Using cards 0, 2, 3, 7, writing 0237 gives a 3-digit number; the smallest 4-digit number is 2037.",
            "Trap: Dividing total distance by net jump without checking the final forward hop! Kangy reaches the goal during his forward leap before sliding back.",
        ],
        traps_ar=[
            "فخ شائع: ضرب عدد الأشجار الكلي في طول المسافة! بين 9 أشجار توجد 8 مسافات فقط (8 × 6 = 48 م) وليس 9 × 6 = 54 م.",
            "فخ شائع: وضع الصفر 0 في المنزلة اليسرى! بالبطاقات 0 و2 و3 و7، كتابة 0237 تعطي عدداً من 3 أرقام؛ أصغر عدد من 4 أرقام هو 2037.",
            "فخ شائع: قسمة المسافة الكلية على التقدم الصافي مباشرة! الكنغر يصل إلى الهدف أثناء قفزته الأمامية قبل أن يتراجع.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-01-EX1",
                title_en="Worked Example 1 — Mystery Middle Brick in a Pyramid",
                title_ar="مثال محلول ١ — الطوبة الوسطى المفقودة في الهرم",
                q_en=f"In Kangy's 3-row number pyramid, each brick is the sum of the two bricks directly below it. The bottom row has {m(5)}, {m('?')}, and {m(9)}, and the top brick is {m(26)}. What number belongs in the {m('?')} brick?",
                q_ar=f"في هرم الكنغر العددي ذي الصفوف الثلاثة، كل طوبة تساوي مجموع الطوبتين أسفلها مباشرة. الصف السفلي هو {m(5)} و{m('?')} و{m(9)}، وطوبة القمة هي {m(26)}. ما العدد في طوبة {m('?')}؟",
                correct_val=6,
                distractors=[5, 7, 12, 14],
                idea_en="Call the mystery middle brick \\( b \\). It gets added into both middle-row bricks, so the top brick equals \\( 5 + 2b + 9 \\).",
                steps_en=[
                    f"The two bricks in the middle row are {m('5 + b')} and {m('b + 9')}.",
                    f"Adding those two middle bricks gives the top brick: {m('(5 + b) + (b + 9) = 14 + 2b')}.",
                    f"Since the top brick is {m(26)}, we have {m('14 + 2b = 26')}, so {m('2b = 12')} and {m('b = 6')}.",
                ],
                check_en=f"Check bottom-up: {m('5 + 6 = 11')}, {m('6 + 9 = 15')}, and {m('11 + 15 = 26')}. Exact match!",
                idea_ar="نسمّي الطوبة الوسطى \\( b \\)؛ وهي تدخل في طوبتي الصف الأوسط معاً، فتكون القمة مساوية \\( 5 + 2b + 9 \\).",
                steps_ar=[
                    f"طوبتا الصف الأوسط هما {m('5 + b')} و{m('b + 9')}.",
                    f"مجموعهما يعطي طوبة القمة: {m('(5 + b) + (b + 9) = 14 + 2b')}.",
                    f"بما أن القمة تساوي {m(26)} فإن {m('14 + 2b = 26')}، أي {m('2b = 12')} ومنها {m('b = 6')}.",
                ],
                check_ar=f"تحقق من الأسفل للأعلى: {m('5 + 6 = 11')}، و{m('6 + 9 = 15')}، ومجموعهما {m('11 + 15 = 26')}!",
                diagram_en=svg_kang_number_pyramid([["26"], ["", ""], ["5", "?", "9"]]),
            ),
            kang_worked_example(
                ex_id="KANG-L1-01-EX2",
                title_en="Worked Example 2 — Forward-and-Back Kangaroo Hops",
                title_ar="مثال محلول ٢ — قفزات الكنغر للأمام والخلف",
                q_en=f"Little Kangy starts at {m(0)} on a number line. Each sunny hop moves him {m(5)} units forward, and each windy gust pushes him {m(2)} units back. On which sunny hop does Kangy first land on {m(17)}?",
                q_ar=f"يبدأ الكنغر الصغير عند {m(0)} على خط الأعداد. في كل قفزة نهارية يتقدم {m(5)} وحدات للأمام، وبعدها تدفعه الريح {m(2)} وحدتين للخلف. في أي قفزة نهارية يصل الكنغر لأول مرة إلى العدد {m(17)}؟",
                correct_val=5,
                distractors=[4, 6, 7, 8],
                idea_en="Each full cycle (hop + push) gains \\( 5 - 2 = 3 \\) units, so stop one hop before \\( 17 \\) and test the next \\( +5 \\) jump!",
                steps_en=[
                    f"After each full hop-and-push cycle, Kangy advances by {m('5 - 2 = 3')} units.",
                    f"After {m(4)} full cycles, Kangy stands at {m('4 \\times 3 = 12')}.",
                    f"On his **5th** sunny hop, he jumps {m('12 + 5 = 17')} and lands right on {m(17)}!",
                ],
                check_en=f"Positions after sunny hops: 1st {m('\\to 5')}, 2nd {m('\\to 8')}, 3rd {m('\\to 11')}, 4th {m('\\to 14')}, 5th {m('\\to 17')}.",
                idea_ar="في كل دورة كاملة (قفزة ثم تراجع) يتقدم الكنغر \\( 5 - 2 = 3 \\) وحدات، فنتوقف عند \\( 17 - 5 = 12 \\) ثم نقفز القفزة الأخيرة!",
                steps_ar=[
                    f"التقدم الصافي في كل دورة كاملة يساوي {m('5 - 2 = 3')} وحدات.",
                    f"بعد {m(4)} دورات كاملة يقف الكنغر عند العدد {m('4 \\times 3 = 12')}.",
                    f"في القفزة النهارية **الخامسة** يقفز {m('12 + 5 = 17')} فيصل مباشرة إلى الهدف!",
                ],
                check_ar=f"مواقع القفزات النهارية: الأولى {m(5)}، الثانية {m(8)}، الثالثة {m(11)}، الرابعة {m(14)}، الخامسة {m(17)}.",
                diagram_en=svg_number_line_jumps(5, 2, 17),
            ),
            kang_worked_example(
                ex_id="KANG-L1-01-EX3",
                title_en="Worked Example 3 — Largest Minus Smallest 4-Digit Number",
                title_ar="مثال محلول ٣ — الفرق بين أكبر وأصغر عدد من 4 أرقام",
                q_en=f"Lina holds four digit cards: {m(3)}, {m(0)}, {m(7)}, and {m(2)}. Using all four cards once each time, what is the difference between the **largest** 4-digit number and the **smallest** 4-digit number she can form?",
                q_ar=f"مع لينا أربع بطاقات أرقام: {m(3)} و{m(0)} و{m(7)} و{m(2)}. باستعمال البطاقات الأربع معاً في كل مرة، ما الفرق بين **أكبر** عدد من 4 أرقام و**أصغر** عدد من 4 أرقام يمكنها تكوينه؟",
                correct_val=5283,
                distractors=[7083, 5043, 5317, 4983],
                idea_en="Sort digits high-to-low for the largest number, and put the smallest non-zero digit first (then \\( 0 \\)) for the smallest 4-digit number.",
                steps_en=[
                    f"Arranging {m('7, 3, 2, 0')} from greatest to least gives the largest number: {m(7320)}.",
                    f"For the smallest 4-digit number, {m(0)} cannot go first, so put {m(2)} in the thousands place and {m(0)} next: {m(2037)}.",
                    f"Subtract: {m('7320 - 2037 = 5283')}.",
                ],
                check_en=f"Add back to check: {m('2037 + 5283 = 7320')}, and {m(2037)} has {m(4)} digits without a leading zero.",
                idea_ar="نرتب الأرقام تنازلياً لأكبر عدد، ونضع أصغر رقم غير صفري في الآلاف يليه الصفر لأصغر عدد رباعي.",
                steps_ar=[
                    f"ترتيب الأرقام {m('7, 3, 2, 0')} تنازلياً يعطي أكبر عدد: {m(7320)}.",
                    f"لأصغر عدد من 4 أرقام لا نضع {m(0)} في اليسار، فنضع {m(2)} في الآلاف ثم {m(0)} في المئات: {m(2037)}.",
                    f"نحسب الفرق: {m('7320 - 2037 = 5283')}.",
                ],
                check_ar=f"بالجمع العكسي: {m('2037 + 5283 = 7320')}، وهو فرق دقيق!",
                diagram_en=svg_digit_slots(["2", "0", "3", "7"], "7320 − 2037 = ?"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-01-EX4",
                title_en="Worked Example 4 — Palm Trees Along a Straight Path",
                title_ar="مثال محلول ٤ — أشجار النخيل على ممر مستقيم",
                q_en=f"Gardeners plant {m(9)} palm trees in a straight row along the school walkway. The distance between any two neighboring trees is {m(6)} meters. How many meters is it from the **1st** tree to the **9th** tree?",
                q_ar=f"زرع البستانيون {m(9)} نخلات في صف مستقيم على ممر المدرسة، والمسافة بين كل نخلتين متجاورتين {m(6)} أمتار. كم متراً تبلغ المسافة من النخلة **الأولى** إلى النخلة **التاسعة**؟",
                correct_val=48,
                distractors=[54, 42, 60, 45],
                idea_en="Count the **gaps** between the \\( 9 \\) trees: \\( 9 - 1 = 8 \\) equal spaces!",
                steps_en=[
                    f"Between {m(9)} trees in a straight line, there are {m('9 - 1 = 8')} gaps.",
                    f"Each gap measures {m(6)} meters.",
                    f"Total distance = {m('8 \\times 6 = 48')} meters.",
                ],
                check_en=f"With {m(2)} trees the distance is {m('1 \\times 6 = 6')}; with {m(9)} trees it is {m('8 \\times 6 = 48')} m (not {m(54)}).",
                idea_ar="نحسب **عدد المسافات** بين النخلات التسع: \\( 9 - 1 = 8 \\) مسافات متساوية!",
                steps_ar=[
                    f"بين {m(9)} نخلات في صف مستقيم توجد {m('9 - 1 = 8')} مسافات.",
                    f"طول كل مسافة يساوي {m(6)} أمتار.",
                    f"المسافة الكلية = {m('8 \\times 6 = 48')} متراً.",
                ],
                check_ar=f"مع نخلتين فقط المسافة {m('1 \\times 6 = 6')} م، ومع {m(9)} نخلات تكون {m('8 \\times 6 = 48')} م!",
                diagram_en=svg_fenceposts("6 m", "? m"),
            ),
        ],
        blueprints=[
            "kang_eco_brick_pyramid",
            "kang_eco_kangaroo_jumps",
            "kang_eco_place_value_digits",
            "kang_eco_fencepost_spacing",
        ],
    )



def _lesson_1_2() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-02",
        level=LEVEL,
        unit_num="Lesson 1.2",
        topic="Algebra",
        title_en="Toy Balance Scales, Magic Number Crosses & Repeating Patterns",
        title_ar="موازين الألعاب، والتقاطعات العددية السحرية، والأنماط المتكررة",
        summary_en=(
            "Discover Grade 3–4 visual algebra without scary letters! Trade equal toys on balance scales, "
            "unlock Kangaroo magic crosses by spotting the shared center cell, group repeating bead necklaces, "
            "and rewind two-step number machines backward."
        ),
        summary_ar=(
            "اكتشف الجبر البصري الممتع للصفين الثالث والرابع! بادل الألعاب المتساوية على كفتي الميزان، "
            "وحلّ التقاطعات السحرية بملاحظة المربع الأوسط المشترك، وجمّع عقود الخرز المتكررة في مجموعات، "
            "وأعِد تشغيل آلات الأعداد خطوة بخطوة بالعكس."
        ),
        goals_en=[
            "Swap equal groups of toys on **balance scales** and remove identical items from both sides safely.",
            "Use the **shared center square** in a 5-cell magic cross to make row and column sums match.",
            "Count colors or find the **nth item** in a repeating necklace or sticker pattern using equal groups and leftovers.",
            "Work **backward** through a 2-step mystery number machine by undoing the last step first.",
        ],
        goals_ar=[
            "استبدال الألعاب المتكافئة على **كفتي الميزان** وحذف القطع المتماثلة من الطرفين بأمان.",
            "توظيف **المربع الأوسط المشترك** في التقاطع السحري ذي المربعات الخمسة لمساواة مجموع الصف والعمود.",
            "حساب عدد الخرزات من لون معين أو تحديد **العنصر رقم n** في نمط متكرر بتقسيمه إلى مجموعات متساوية وباقٍ.",
            "السير **عكسياً** في آلة الأعداد ذات الخطوتين بإلغاء العملية الأخيرة أولاً.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Toy Balance Scales & Fair Trading",
                title_ar="١. موازين الألعاب والمقايضة العادلة",
                body_en=(
                    f"A level balance scale means **both sides weigh the exact same**. "
                    f"You have two superpowers: **(1) Take away identical toys** from both pans, and **(2) Trade any toy** for what it balances on another scale! "
                    f"In the diagram, {m(2)} orange balls balance {m(1)} green cube, and {m(1)} green cube balances {m(3)} purple pyramids—so {m(2)} orange balls balance {m(3)} purple pyramids!"
                ),
                body_ar=(
                    f"عندما تتساوى كفتا الميزان فهذا يعني أن **الطرفين لهما الوزن نفسه تماماً**. "
                    f"لديك مهارتان ذهبيتان: **(١) احذف الألعاب المتطابقة** من الكفتين معاً، و**(٢) استبدل أي لعبة** بما يعادلها في ميزان آخر! "
                    f"في الرسم، كرتان برتقاليتان تعادلان مكعباً أخضر واحداً، والمكعب الأخضر يعادل {m(3)} أهرامات بنفسجية؛ إذن كرتان برتقاليتان تعادلان {m(3)} أهرامات!"
                ),
                formula_en=dm("2\\text{ Balls} = 1\\text{ Cube}, \\quad 1\\text{ Cube} = 3\\text{ Pyramids} \\implies 2\\text{ Balls} = 3\\text{ Pyramids}"),
                caption_ar="قاعدة الاستبدال المتكافئ على الميزان:",
                formula_math_ar=dm("2\\text{ Balls} = 1\\text{ Cube} = 3\\text{ Pyramids}"),
                diagram_en=svg_balance_scales(2, 1, 1, 3),
            ),
            kang_concept(
                title_en="2. Magic Number Crosses & the Shared Center",
                title_ar="٢. التقاطع العددي السحري والمربع الأوسط المشترك",
                body_en=(
                    f"In a 5-square Kangaroo cross, the **center square is counted twice**—once in the horizontal row and once in the vertical column! "
                    f"When the row sum and column sum are equal, removing the center square leaves two pairs of outer arms that must also have the **exact same sum**. "
                    f"Adding the row sum and column sum together always equals **(sum of all 5 numbers) + (center)**."
                ),
                body_ar=(
                    f"في تقاطع الكنغر المكوّن من 5 مربعات، **يُحسب المربع الأوسط مرتين**: مرة ضمن الصف الأفقي ومرة ضمن العمود الرأسي! "
                    f"عندما يتساوى مجموع الصف ومجموع العمود، فإن حذف المربع الأوسط يترك زوجين متقابلين لهما **المجموع نفسه تماماً**. "
                    f"كما أن مجموع الصف زائد مجموع العمود يساوي دائماً **(مجموع الأعداد الخمسة كلها) + (عدد الوسط)**."
                ),
                formula_en=dm("(\\text{Row Sum}) + (\\text{Col Sum}) = (\\text{Total of all } 5\\text{ cells}) + \\text{Center}"),
                caption_ar="علاقة مجموع الصف والعمود بالمربع الأوسط:",
                formula_math_ar=dm("S_{\\text{row}} + S_{\\text{col}} = \\text{Total} + C"),
                diagram_en=svg_kang_magic_cross("5", "2", "7", "8", "3", "Row = 15, Col = 15"),
            ),
            kang_concept(
                title_en="3. Repeating Patterns & Rewinding Mystery Machines",
                title_ar="٣. الأنماط المتكررة وإعادة تشغيل آلة الأعداد عكسياً",
                body_en=(
                    f"When a bead necklace repeats a block of {m(k := 4)} colors, divide the total position by {m(4)}: "
                    f"the **quotient** tells how many full blocks occur, and the **leftover** tells where to stop inside the next block! "
                    f"For a 2-step mystery machine, walk **backward from the exit** using opposite operations: undo {m('\\times 3')} with {m('\\div 3')}, and undo {m('+ 4')} with {m('- 4')}."
                ),
                body_ar=(
                    f"عندما يتكرر عقد الخرز في مجموعة طولها {m(4)} خرزات، اقسم رقم الخرزة على {m(4)}: "
                    f"**خارج القسمة** يخبرك بعدد المجموعات الكاملة، و**الباقي** يحدد موقع الخرزة في المجموعة التالية! "
                    f"وفي آلة الأعداد ذات الخطوتين، ارجع **عكسياً من المخرج** بالعمليات المعاكسة: ألغِ {m('\\times 3')} بالقسمة {m('\\div 3')}، وألغِ {m('+ 4')} بالطرح {m('- 4')}."
                ),
                formula_en=dm("\\text{In} \\xrightarrow{+4} \\square \\xrightarrow{\\times 3} 27 \\quad \\Longrightarrow \\quad 27 \\xrightarrow{\\div 3} 9 \\xrightarrow{-4} 5"),
                caption_ar="الرجوع العكسي خطوة بخطوة من المخرج إلى المدخل:",
                formula_math_ar=dm("27 \\div 3 = 9 \\implies 9 - 4 = 5"),
                diagram_en=svg_function_machine("?", "+ 4", "× 3", "27"),
            ),
        ],
        traps_en=[
            "Trap: Undoing a 2-step machine in the wrong order! If a machine adds 6 then multiplies by 3 to get 39, divide by 3 FIRST (39 ÷ 3 = 13), then subtract 6 to get 7—do NOT subtract 6 from 39 first!",
            "Trap: Forgetting the center square is counted twice in a cross! Two lines of sum 15 do NOT sum to 30 across 5 cells—if the center is 5, the 5 cells sum to 30 − 5 = 25.",
            "Trap: When the remainder of a repeating pattern is 0, picking the 1st bead instead of the LAST bead of the repeating block!",
        ],
        traps_ar=[
            "فخ شائع: عكس ترتيب العمليات عند الرجوع في آلة الأعداد! إذا جمعت الآلة 6 ثم ضربت في 3 فأعطت 39، اقسم على 3 أولاً (13) ثم اطرح 6 لتحصل على 7.",
            "فخ شائع: نسيان أن مربع الوسط يُجمع مرتين! إذا كان مجموع الصف 15 ومجموع العمود 15 والوسط 5 فإن مجموع الأعداد الخمسة هو 30 − 5 = 25 وليس 30.",
            "فخ شائع: عندما يكون باقي القسمة في النمط المتكرر صفراً (0)، اختيار الخرزة الأولى بدلاً من الخرزة الأخيرة في المجموعة!",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-02-EX1",
                title_en="Worked Example 1 — Trading Toys Across Two Scales",
                title_ar="مثال محلول ١ — تبديل الألعاب عبر ميزانين",
                q_en=f"On Kangy's first balance scale, {m(2)} orange balls balance {m(1)} green cube. On his second scale, {m(1)} green cube balances {m(3)} purple pyramids. How many purple pyramids balance {m(4)} orange balls?",
                q_ar=f"في الميزان الأول لدى الكنغر تتعادل كرتان برتقاليتان ({m(2)}) مع مكعب أخضر واحد ({m(1)}). وفي الميزان الثاني يتعادل مكعب أخضر واحد ({m(1)}) مع {m(3)} أهرامات بنفسجية. كم هرماً بنفسجياً يعادل {m(4)} كرات برتقالية؟",
                correct_val=6,
                distractors=[3, 4, 5, 8],
                idea_en="First trade the \\( 4 \\) orange balls for green cubes, then trade each green cube for \\( 3 \\) purple pyramids!",
                steps_en=[
                    f"Since {m(2)} orange balls equal {m(1)} green cube, {m(4)} orange balls equal {m('2 \\times 1 = 2')} green cubes.",
                    f"Each green cube equals {m(3)} purple pyramids.",
                    f"So {m(2)} green cubes equal {m('2 \\times 3 = 6')} purple pyramids.",
                ],
                check_en=f"Double both sides of {m('2\\text{ balls} = 3\\text{ pyramids}')}: {m('4\\text{ balls} = 6\\text{ pyramids}')}!",
                idea_ar="نستبدل الكرات الأربع بمكعبات خضراء أولاً، ثم نستبدل كل مكعب أخضر بثلاثة أهرامات بنفسجية!",
                steps_ar=[
                    f"بما أن كرتين برتقاليتين تعادلان مكعباً أخضر واحداً، فإن {m(4)} كرات تعادل مكعبين أخضرين ({m(2)}).",
                    f"كل مكعب أخضر يعادل {m(3)} أهرامات بنفسجية.",
                    f"إذن المكعبان الأخضران يعادلان {m('2 \\times 3 = 6')} أهرامات بنفسجية.",
                ],
                check_ar=f"بمضاعفة المعادلة {m('2\\text{ كرات} = 3\\text{ أهرامات}')} نحصل على {m('4\\text{ كرات} = 6\\text{ أهرامات}')}!",
                diagram_en=svg_balance_scales(2, 1, 1, 3),
            ),
            kang_worked_example(
                ex_id="KANG-L1-02-EX2",
                title_en="Worked Example 2 — Finding the Center of a Magic Cross",
                title_ar="مثال محلول ٢ — إيجاد مركز التقاطع السحري",
                q_en=f"Tariq places each of the five numbers {m(2)}, {m(4)}, {m(5)}, {m(6)}, and {m(8)} into one square of a 5-cell cross so the 3-cell horizontal sum equals the 3-cell vertical sum. Which number **must** go in the center square?",
                q_ar=f"يضع طارق الأعداد الخمسة {m(2)} و{m(4)} و{m(5)} و{m(6)} و{m(8)} في مربعات تقاطع مكوّن من 5 خلايا بحيث يتساوى مجموع خلايا الصف الثلاث مع مجموع خلايا العمود الثلاث. أي عدد **يجب** وضعه في المربع الأوسط؟",
                correct_val=5,
                distractors=[2, 4, 6, 8],
                idea_en="Once you pick the center number, the remaining four numbers must split into two pairs with the **exact same sum**!",
                steps_en=[
                    f"Add all five numbers: {m('2 + 4 + 5 + 6 + 8 = 25')}.",
                    f"To split the remaining {m(4)} numbers into two equal pairs, their sum {m('25 - \\text{center}')} must be **even**.",
                    f"Only subtracting the odd number {m(5)} gives an even total ({m('25 - 5 = 20')}), splitting into {m('2 + 8 = 10')} and {m('4 + 6 = 10')}!",
                ],
                check_en=f"Row {m('2 + 5 + 8 = 15')} and Column {m('4 + 5 + 6 = 15')}—both equal {m(15)}!",
                idea_ar="بعد اختيار عدد الوسط يجب أن تنقسم الأعداد الأربعة الباقية إلى زوجين لهما **المجموع نفسه تماماً**!",
                steps_ar=[
                    f"مجموع الأعداد الخمسة كلها يساوي {m('2 + 4 + 5 + 6 + 8 = 25')}.",
                    f"كي تنقسم الأعداد الأربعة المتبقية إلى زوجين متساويين يجب أن يكون مجموعها {m('25 - \\text{الوسط}')} عدداً **زوجياً**.",
                    f"العدد الفردي الوحيد هو {m(5)}، فيتبقى {m('25 - 5 = 20')} وتنقسم إلى {m('2 + 8 = 10')} و{m('4 + 6 = 10')}!",
                ],
                check_ar=f"مجموع الصف {m('2 + 5 + 8 = 15')} ومجموع العمود {m('4 + 5 + 6 = 15')} متساويان تماماً!",
                diagram_en=svg_kang_magic_cross("?", "4", "8", "6", "2", "Place 2, 4, 5, 6, 8"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-02-EX3",
                title_en="Worked Example 3 — Counting Blue Beads on a Bracelet",
                title_ar="مثال محلول ٣ — عدّ الخرزات الزرقاء في السوار",
                q_en=f"Sara threads {m(23)} beads onto a string by repeating the 4-bead pattern **Red, Blue, Blue, Yellow** over and over from the start. How many **Blue** beads are on her finished string?",
                q_ar=f"تنظِم سارة {m(23)} خرزة في خيط بتكرار النمط الرباعي **أحمر، أزرق، أزرق، أصفر** بالترتيب نفسه من البداية. كم خرزة **زرقاء** في الخيط المكتمل؟",
                correct_val=12,
                distractors=[10, 11, 13, 6],
                idea_en="Group the \\( 23 \\) beads into complete blocks of \\( 4 \\), then check the leftover beads at the end!",
                steps_en=[
                    f"Divide {m(23)} by {m(4)}: {m('23 = 5 \\times 4 + 3')}, so there are {m(5)} full blocks and {m(3)} extra beads.",
                    f"Each full block (**R, B, B, Y**) has {m(2)} Blue beads, giving {m('5 \\times 2 = 10')} Blue beads.",
                    f"The {m(3)} leftover beads at the end are **Red, Blue, Blue**, adding {m(2)} more Blue beads for {m('10 + 2 = 12')} in all.",
                ],
                check_en=f"Count all {m(23)} beads: {m(6)} Red + {m(12)} Blue + {m(5)} Yellow = {m(23)} beads!",
                idea_ar="نجمّع الـ \\( 23 \\) خرزة في مجموعات رباعية مكتملة ثم نفحص الخرزات المتبقية في النهاية!",
                steps_ar=[
                    f"بقسمة {m(23)} على {m(4)} نجد {m('23 = 5 \\times 4 + 3')}، أي {m(5)} مجموعات كاملة و{m(3)} خرزات إضافية.",
                    f"في كل مجموعة كاملة خرزتان زرقاوان، ما يعطي {m('5 \\times 2 = 10')} خرزات زرقاء.",
                    f"أول {m(3)} خرزات إضافية هي (**أحمر، أزرق، أزرق**) فتضيف خرزتين زرقاوين ليصبح المجموع {m('10 + 2 = 12')}.",
                ],
                check_ar=f"تحقق من المجموع الكلي: {m(6)} حمراء + {m(12)} زرقاء + {m(5)} صفراء = {m(23)} خرزة!",
                diagram_en=svg_kang_necklace_beads(["R", "B", "B", "Y", "R", "B", "B", "Y", "?"]),
            ),
            kang_worked_example(
                ex_id="KANG-L1-02-EX4",
                title_en="Worked Example 4 — Rewinding Kangy's Number Machine",
                title_ar="مثال محلول ٤ — تشغيل آلة الكنغر العددية بالعكس",
                q_en=f"Omar feeds a mystery number into Kangy's 2-step machine. First the machine **adds {m(6)}**, and next it **multiplies by {m(3)}**. The final number that comes out is {m(39)}. What number did Omar put in?",
                q_ar=f"أدخل عمر عدداً سرياً في آلة الكنغر ذات الخطوتين: أولاً **تجمع {m(6)}**، ثم **تضرب الناتج في {m(3)}**. إذا خرج العدد {m(39)} في النهاية، فما العدد الذي أدخله عمر؟",
                correct_val=7,
                distractors=[5, 11, 13, 19],
                idea_en="Walk backward from \\( 39 \\): undo the multiplication by \\( 3 \\) first, then undo adding \\( 6 \\)!",
                steps_en=[
                    f"Before multiplying by {m(3)}, the number inside the machine was {m('39 \\div 3 = 13')}.",
                    f"Before adding {m(6)}, Omar's starting number was {m('13 - 6 = 7')}.",
                ],
                check_en=f"Test forward: {m('7 + 6 = 13')}, and {m('13 \\times 3 = 39')}. Spot on!",
                idea_ar="نرجع عكسياً من العدد \\( 39 \\): نلغي الضرب في \\( 3 \\) بالقسمة أولاً، ثم نلغي جمع \\( 6 \\) بالطرح!",
                steps_ar=[
                    f"قبل الضرب في {m(3)} كان العدد في وسط الآلة يساوي {m('39 \\div 3 = 13')}.",
                    f"وقبل جمع {m(6)} كان العدد الأصلي الذي أدخله عمر يساوي {m('13 - 6 = 7')}.",
                ],
                check_ar=f"اختبر للأمام: {m('7 + 6 = 13')} ثم {m('13 \\times 3 = 39')}. إجابة صحيحة!",
                diagram_en=svg_function_machine("?", "+ 6", "× 3", "39"),
            ),
        ],
        blueprints=[
            "kang_eco_toy_balance",
            "kang_eco_magic_cross",
            "kang_eco_repeating_beads",
            "kang_eco_mystery_machine",
        ],
    )



def _lesson_1_3() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-03",
        level=LEVEL,
        unit_num="Lesson 1.3",
        topic="Geometry",
        title_en="Staircase Perimeters, Grid Tile Counting & Overlapping Cards",
        title_ar="محيطات الأشكال المتدرجة، وعدّ بلاطات الشبكة، والبطاقات المتداخلة",
        summary_en=(
            "See shapes like a Kangaroo geometry champion! Slide staircase edges outward to find perimeters in seconds, "
            "count visible and hidden floor tiles on a grid, subtract double-counted overlaps between cards, "
            "and build rows of matchstick polygons without counting shared sides twice."
        ),
        summary_ar=(
            "انظر إلى الأشكال بعين بطل الكنغر الهندسي! ادفع حواف السلالم للخارج لحساب المحيط في ثوانٍ، "
            "وعدّ البلاطات الظاهرة والمخفية على الشبكة، واطرح منطقة التداخل المكررة بين البطاقات، "
            "وابنِ صفوف المضلعات بأعواد الثقاب دون تكرار عدّ الأضلاع المشتركة."
        ),
        goals_en=[
            "Find the **perimeter of a staircase polygon** by sliding horizontal steps up and vertical steps sideways: **P = 2(W + H)**.",
            "Calculate **grid areas**, pair two half-square triangles into **1 whole tile**, and count hidden tiles under a rug.",
            "Solve **overlapping card and ribbon length/area puzzles** using **Total = First + Second − Overlap**.",
            "Count matchsticks in connected chains of squares (**3n + 1**) and triangles (**2n + 1**).",
        ],
        goals_ar=[
            "إيجاد **محيط المضلع المتدرج (السّلّمي)** بدفع الدرجات الأفقية للأعلى والرأسية للجانب: **P = 2(W + H)**.",
            "حساب **مساحات الشبكة** ودمج كل مثلثين نصفيين في **بلاطة كاملة** وعدّ البلاطات المخفية تحت السجادة.",
            "حل مسائل **البطاقات والشرائط المتداخلة** بالقاعدة الذهبية: **المجموع المغطى = الأول + الثاني − التداخل**.",
            "عدّ أعواد الثقاب في صفوف المربعات المتصلة (**3n + 1**) والمثلثات المتصلة (**2n + 1**).",
        ],
        concepts=[
            kang_concept(
                title_en="1. The Staircase Edge-Pushing Trick",
                title_ar="١. خدعة دفع حواف الشكل المتدرج (السّلّم)",
                body_en=(
                    f"Even if you don't know the length of each tiny step on a staircase shape, you can still find its **exact perimeter**! "
                    f"Push every horizontal step straight up—together they match the bottom width {m('W')}. "
                    f"Push every vertical step straight right—together they match the left height {m('H')}. "
                    f"As long as the steps never dip inward into a U-pocket, the perimeter is simply {m('2 \\times (W + H)')}!"
                ),
                body_ar=(
                    f"حتى لو لم تعرف طول كل درجة صغيرة في الشكل السّلّمي، يمكنك إيجاد **محيطه الدقيق فوراً**! "
                    f"ادفع جميع القطع الأفقية للدرجات إلى الأعلى فتكوّن معاً عرض القاعدة {m('W')}. "
                    f"وادفع جميع القطع الرأسية إلى اليمين فتكوّن معاً الارتفاع الأيسر {m('H')}. "
                    f"ما دامت الدرجات لا تنثني للداخل لتصنع جيباً، فإن المحيط يساوي ببساطة {m('2 \\times (W + H)')}!"
                ),
                formula_en=dm("\\text{Staircase Perimeter} = W + H + W + H = 2(W + H)"),
                caption_ar="محيط المضلع المتدرج يساوي محيط المستطيل المحيط به:",
                formula_math_ar=dm("P = 2(W + H)"),
                diagram_en=svg_kang_staircase_perimeter("12 cm", "9 cm", 4),
            ),
            kang_concept(
                title_en="2. Grid Tile Counting & Rugs on Tiled Floors",
                title_ar="٢. عدّ بلاطات الشبكة والسجاد فوق الأرضيات المبلطة",
                body_en=(
                    f"To count tiles in a rectangular floor quickly, multiply **rows × columns** along two outer borders. "
                    f"If a rug covers a middle section, inspect the uncovered border columns and rows to see how many rows and columns lie underneath the rug! "
                    f"And on a square grid, **two half-square triangles** always combine to make **1 whole unit square**."
                ),
                body_ar=(
                    f"لعدّ البلاطات في أرضية مستطيلة بسرعة، اضرب **عدد الصفوف × عدد الأعمدة** من الحافتين الخارجيتين. "
                    f"وإذا غطت سجادة جزءاً في المنتصف، تتبّع الصفوف والأعمدة المحيطة بها لتعرف كم صفاً وكم عموداً يختبئ تحتها! "
                    f"وعلى شبكة المربعات، يتحد كل **مثلثين نصفيين** دائماً ليشكّلا **مربعاً كاملاً واحداً**."
                ),
                formula_en=dm("\\text{Total Tiles} = \\text{Rows} \\times \\text{Cols}, \\qquad 2\\text{ Half-Squares} = 1\\text{ Whole Tile}"),
                caption_ar="حساب البلاطات الكلية ودمج أنصاف المربعات:",
                formula_math_ar=dm("\\text{Area} = R \\times C"),
                diagram_en=svg_kang_polyomino_board([
                    [1, 1, 1, 1, 1, 1],
                    [1, -1, -1, -1, 1, 1],
                    [1, -1, -1, -1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                ]),
            ),
            kang_concept(
                title_en="3. Overlapping Cards & Shared Matchstick Sides",
                title_ar="٣. البطاقات المتداخلة والأضلاع المشتركة بأعواد الثقاب",
                body_en=(
                    f"When two cards overlap on a table, adding their two areas counts the middle overlap **twice**, so subtract it once: "
                    f"{m('\\text{Covered} = A_1 + A_2 - \\text{Overlap}')}. "
                    f"The same idea powers matchstick chains! One square uses {m(4)} sticks, and every extra square glued to the right needs only {m(3)} new sticks because it shares {m(1)} wall: {m('4 + 3(n - 1) = 3n + 1')}."
                ),
                body_ar=(
                    f"عندما تتداخل بطاقتان فوق الطاولة، فإن جمع مساحتيهما يحسب منطقة التداخل **مرتين**؛ لذلك نطرحها مرة واحدة: "
                    f"{m('\\text{المغطى} = A_1 + A_2 - \\text{التداخل}')}. "
                    f"والفكرة نفسها تنطبق على سلاسل أعواد الثقاب! المربع الأول يحتاج {m(4)} أعواد، وكل مربع جديد ملتصق به يحتاج {m(3)} أعواد فقط لمشاركته ضلعاً: {m('3n + 1')}."
                ),
                formula_en=dm("\\text{Covered Area} = A_1 + A_2 - A_{\\text{overlap}}, \\qquad \\text{Sticks for } n\\text{ Squares} = 3n + 1"),
                caption_ar="قانون المساحة المغطاة وقانون صف المربعات المتصلة:",
                formula_math_ar=dm("A_{\\text{total}} = A_1 + A_2 - A_{\\text{ov}}, \\qquad S_n = 3n + 1"),
                diagram_en=svg_kang_overlapping_rects("30 cm²", "24 cm²", "8 cm²"),
            ),
        ],
        traps_en=[
            "Trap: Thinking a 5-step staircase has a larger perimeter than a 2-step staircase with the same width W and height H! Both have perimeter 2(W + H).",
            "Trap: Subtracting the overlap TWICE when finding covered area! It was counted twice in A₁ + A₂, so subtract the overlap only ONCE to leave one layer.",
            "Trap: Multiplying 4 × n for n connected matchstick squares! That double-counts every shared inner wall—use 3n + 1 instead.",
        ],
        traps_ar=[
            "فخ شائع: الظن بأن السّلّم ذا 5 درجات محيطه أكبر من سُلّم ذي درجتين له نفس العرض W والارتفاع H! كلاهما محيطه 2(W + H).",
            "فخ شائع: طرح منطقة التداخل مرتين عند حساب المساحة المغطاة! نطرح التداخل مرة واحدة فقط ليبقى محسوباً مرة واحدة.",
            "فخ شائع: ضرب 4 × n لصف من المربعات المتصلة بأعواد الثقاب! الصواب 3n + 1 لأن الأضلاع الداخلية مشتركة.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-03-EX1",
                title_en="Worked Example 1 — Perimeter of a 5-Step Garden Staircase",
                title_ar="مثال محلول ١ — محيط حديقة متدرجة من 5 درجات",
                q_en=f"A right-angled staircase shape has a flat bottom edge of {m(14)} cm, a flat left edge of {m(10)} cm, and {m(5)} steps climbing neatly from bottom-right to top-left. What is the perimeter of the shape in cm?",
                q_ar=f"شكل متدرج قائم الزوايا طول قاعدته السفلية {m(14)} سم وطول حافته اليسرى {m(10)} سم، وله {m(5)} درجات تصعد بانتظام من أسفل اليمين إلى أعلى اليسار. ما محيط الشكل بالسنتمتر؟",
                correct_val=48,
                distractors=[24, 38, 53, 58],
                idea_en="Push all horizontal step treads up to equal \\( 14 \\) cm and all vertical step risers right to equal \\( 10 \\) cm!",
                steps_en=[
                    f"All horizontal treads at the top add up to the bottom width: {m(14)} cm.",
                    f"All vertical risers on the right add up to the left height: {m(10)} cm.",
                    f"Total perimeter = {m('14 + 10 + 14 + 10 = 48')} cm.",
                ],
                check_en=f"Notice {m('2 \\times (14 + 10) = 2 \\times 24 = 48')} cm regardless of the {m(5)} steps!",
                idea_ar="ندفع القطع الأفقية للدرجات للأعلى فتساوي \\( 14 \\) سم، والقطع الرأسية لليمين فتساوي \\( 10 \\) سم!",
                steps_ar=[
                    f"مجموع الأجزاء الأفقية للدرجات يساوي عرض القاعدة {m(14)} سم.",
                    f"مجموع الأجزاء الرأسية للدرجات يساوي الارتفاع الأيسر {m(10)} سم.",
                    f"المحيط الكلي = {m('14 + 10 + 14 + 10 = 48')} سم.",
                ],
                check_ar=f"المحيط يساوي {m('2 \\times (14 + 10) = 48')} سم مهما كان عدد الدرجات المنتظمة!",
                diagram_en=svg_kang_staircase_perimeter("14 cm", "10 cm", 5),
            ),
            kang_worked_example(
                ex_id="KANG-L1-03-EX2",
                title_en="Worked Example 2 — Visible Floor Tiles Around a Rug",
                title_ar="مثال محلول ٢ — البلاطات الظاهرة حول سجادة",
                q_en=f"A rectangular room floor has {m(6)} rows and {m(8)} columns of square tiles. A rug covers a neat {m(3)}-row by {m(5)}-column rectangle of tiles in the middle. How many tiles are still **visible**?",
                q_ar=f"أرضية غرفة مستطيلة مبلّطة بـ {m(6)} صفوف و{m(8)} أعمدة من البلاطات المربعة. غطّت سجادة منطقة مستطيلة أبعادها {m(3)} صفوف في {m(5)} أعمدة في الوسط. كم بلاطة بقيت **ظاهرة**؟",
                correct_val=33,
                distractors=[15, 32, 35, 48],
                idea_en="Subtract the number of hidden tiles under the rug from the total number of floor tiles!",
                steps_en=[
                    f"Total floor tiles = {m('6 \\times 8 = 48')} tiles.",
                    f"Hidden tiles under the rug = {m('3 \\times 5 = 15')} tiles.",
                    f"Visible tiles = {m('48 - 15 = 33')} tiles.",
                ],
                check_en=f"Add visible and hidden tiles back: {m('33 + 15 = 48')} total tiles!",
                idea_ar="نطرح عدد البلاطات المخفية تحت السجادة من العدد الكلي لبلاطات الغرفة!",
                steps_ar=[
                    f"إجمالي بلاطات الغرفة = {m('6 \\times 8 = 48')} بلاطة.",
                    f"البلاطات المخفية تحت السجادة = {m('3 \\times 5 = 15')} بلاطة.",
                    f"البلاطات الظاهرة = {m('48 - 15 = 33')} بلاطة.",
                ],
                check_ar=f"بجمع الظاهرة والمخفية: {m('33 + 15 = 48')} بلاطة!",
                diagram_en=svg_fraction_grid(8, 6, 33, 15),
            ),
            kang_worked_example(
                ex_id="KANG-L1-03-EX3",
                title_en="Worked Example 3 — Two Overlapping Postcards on a Desk",
                title_ar="مثال محلول ٣ — بطاقتان بريديتان متداخلتان على المكتب",
                q_en=f"Amal places two postcards of areas {m(30)} cm² and {m(24)} cm² on her desk so they overlap in a rectangle of area {m(8)} cm². What total area of the desk (in cm²) is covered?",
                q_ar=f"وضعت أمل بطاقتين بريديتين مساحتاهما {m(30)} سم² و{m(24)} سم² فوق مكتبها بحيث تداخلتا في مستطيل مساحته {m(8)} سم². ما المساحة الكلية المغطاة من المكتب بالسنتمتر المربع؟",
                correct_val=46,
                distractors=[38, 42, 54, 62],
                idea_en="Add the two postcard areas and subtract the \\( 8 \\) cm² overlap once so it isn't counted twice!",
                steps_en=[
                    f"Adding both postcards gives {m('30 + 24 = 54')} cm², which counts the overlap twice.",
                    f"Subtract one copy of the overlap: {m('54 - 8 = 46')} cm².",
                ],
                check_en=f"Only-first ({m('30 - 8 = 22')}) + overlap ({m(8)}) + only-second ({m('24 - 8 = 16')}) = {m('22 + 8 + 16 = 46')} cm²!",
                idea_ar="نجمع مساحتي البطاقتين ثم نطرح مساحة التداخل \\( 8 \\) سم² مرة واحدة حتى لا نحسبها مرتين!",
                steps_ar=[
                    f"مجموع مساحتي البطاقتين يساوي {m('30 + 24 = 54')} سم² وفيه التداخل مكرر مرتين.",
                    f"نطرح التداخل مرة واحدة: {m('54 - 8 = 46')} سم².",
                ],
                check_ar=f"الأولى فقط ({m(22)}) + التداخل ({m(8)}) + الثانية فقط ({m(16)}) = {m(46)} سم²!",
                diagram_en=svg_kang_overlapping_rects("30 cm²", "24 cm²", "8 cm²"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-03-EX4",
                title_en="Worked Example 4 — A Train of 7 Matchstick Squares",
                title_ar="مثال محلول ٤ — قطار من 7 مربعات بأعواد الثقاب",
                q_en=f"Yousef uses identical matchsticks to build a straight row of {m(7)} connected squares side by side, sharing inner sides as shown. How many matchsticks does he use altogether?",
                q_ar=f"يستعمل يوسف أعواد ثقاب متطابقة لبناء صف مستقيم من {m(7)} مربعات متلاصقة تتشارك الأضلاع الداخلية كما في الشكل. كم عود ثقاب يستعمل إجمالاً؟",
                correct_val=22,
                distractors=[21, 24, 25, 28],
                idea_en="Start with \\( 4 \\) matchsticks for the 1st square, then add \\( 3 \\) matchsticks for each of the remaining \\( 6 \\) squares!",
                steps_en=[
                    f"The 1st square uses {m(4)} matchsticks.",
                    f"Each of the next {m('7 - 1 = 6')} squares adds {m(3)} new matchsticks: {m('6 \\times 3 = 18')}.",
                    f"Total matchsticks = {m('4 + 18 = 22')}.",
                ],
                check_en=f"Formula check: {m('3 \\times 7 + 1 = 21 + 1 = 22')} matchsticks!",
                idea_ar="نبدأ بـ \\( 4 \\) أعواد للمربع الأول، ثم نضيف \\( 3 \\) أعواد لكل مربع من المربعات الـ \\( 6 \\) التالية!",
                steps_ar=[
                    f"يحتاج المربع الأول إلى {m(4)} أعواد ثقاب.",
                    f"كل مربع من المربعات الـ {m(6)} التالية يضيف {m(3)} أعواد جديدة: {m('6 \\times 3 = 18')}.",
                    f"المجموع الكلي للأعواد = {m('4 + 18 = 22')} عوداً.",
                ],
                check_ar=f"بالقانون المباشر: {m('3 \\times 7 + 1 = 22')} عوداً!",
                diagram_en=svg_matchstick_squares((1, 2, 3)),
            ),
        ],
        blueprints=[
            "kang_eco_staircase_perimeter",
            "kang_eco_grid_tile_area",
            "kang_eco_overlapping_cards",
            "kang_eco_matchstick_shapes",
        ],
    )



def _lesson_1_4() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-04",
        level=LEVEL,
        unit_num="Lesson 1.4",
        topic="Geometry",
        title_en="3D Toy Cube Stacks, Opposite Die Faces & Transparent Stamp Turns",
        title_ar="أبراج المكعبات ثلاثية الأبعاد، والأوجه المتقابلة للنرد، ودوران الأختام الشفافة",
        summary_en=(
            "Train your 3D Kangaroo X-ray vision! Count hidden support blocks inside toy cube towers, "
            "fold flat paper nets into numbered dice using the 'sum to 7' rule, spin transparent stamp grids by quarter-turns, "
            "and tile game boards with polyomino pieces."
        ),
        summary_ar=(
            "درّب خيالك البصري ثلاثي الأبعاد لأبطال الكنغر! عدّ المكعبات الداعمة المخفية في الأبراج، "
            "واطوِ الشبكات المسطحة لتكوين مكعبات النرد بقاعدة مجموع الوجهين المتقابلين = 7، "
            "وأدِر الأختام الشفافة ربع دورة، وبلّط اللوحات بقطع البوليومينو."
        ),
        goals_en=[
            "Count **all unit cubes in a 3D stack** column-by-column so hidden cubes underneath are never missed.",
            "Use the **Standard Die Rule (opposite faces sum to 7)** and the **skip-one-square rule** on flat cube nets.",
            "Track a corner landmark under **90° clockwise, 90° counterclockwise, and 180° turns** (and mirror flips of rubber stamps).",
            "Count how many **domino, tromino, or tetromino tiles** fit onto a grid board without overlapping.",
        ],
        goals_ar=[
            "عدّ **جميع المكعبات الصغيرة في المجسم** عموداً بعمود لعدم إغفال المكعبات المخفية في الأسفل.",
            "استخدام **قاعدة النرد القياسي (مجموع كل وجهين متقابلين = 7)** وقاعدة **تخطي مربع واحد** في الشبكات المسطحة.",
            "تتبّع ركن مميز عند **الدوران 90° مع عقارب الساعة أو عكسها أو 180°** (وانعكاس الأختام المطاطية).",
            "حساب عدد قطع **الدومينو أو الترومينو أو التترومينو** التي تغطي لوحة شبكية دون تداخل.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Counting 3D Cube Stacks Column-by-Column",
                title_ar="١. عدّ أبراج المكعبات عموداً بعمود",
                body_en=(
                    f"Cubes don't float in mid-air! If you see the top of a column {m(3)} levels high, there **must** be {m(2)} supporting cubes standing underneath it—even if front blocks hide them. "
                    f"The safest Kangaroo method is to write the **height number** on top of each floor column and add those heights together. "
                    f"To complete a full {m('n \\times n \\times n')} cube, subtract your current count from {m('n^3')} ({m(8)} for {m('2\\times2\\times2')}, {m(27)} for {m('3\\times3\\times3')}, {m(64)} for {m('4\\times4\\times4')})."
                ),
                body_ar=(
                    f"المكعبات لا تطير في الهواء! إذا رأيت قمة عمود ارتفاعه {m(3)} طوابق، فلا بد من وجود مكعبين داعمين أسفله حتى لو حجبتهما المكعبات الأمامية. "
                    f"أضمن طريقة في الكنغر هي كتابة **ارتفاع كل عمود** ثم جمع الارتفاعات معاً. "
                    f"ولإكمال مكعب كبير أبعاده {m('n \\times n \\times n')}، اطرح عدد المكعبات الموجودة من {m('n^3')} ({m(8)} أو {m(27)} أو {m(64)})."
                ),
                formula_en=dm("\\text{Total Cubes} = \\sum (\\text{Column Heights}), \\qquad \\text{Missing for } 3\\times3\\times3 = 27 - \\text{Current}"),
                caption_ar="مجموع المكعبات يساوي مجموع ارتفاعات الأعمدة:",
                formula_math_ar=dm("2^3 = 8, \\qquad 3^3 = 27, \\qquad 4^3 = 64"),
                diagram_en=svg_cube_stack_3d((3, 2, 1)),
            ),
            kang_concept(
                title_en="2. Standard Dice (Sum = 7) & Folding Cube Nets",
                title_ar="٢. النرد القياسي (المجموع = 7) وطيّ شبكات المكعب",
                body_en=(
                    f"On every standard game die, **opposite faces always add up to {m(7)}**: {m(1)} is opposite {m(6)}, {m(2)} is opposite {m(5)}, and {m(3)} is opposite {m(4)}. "
                    f"When a cube is unfolded into a flat 6-square net, any two squares in the **same row or column with exactly 1 square between them** fold up to become **opposite faces**!"
                ),
                body_ar=(
                    f"في أي حجر نرد قياسي، **مجموع كل وجهين متقابلين يساوي {m(7)} دائماً**: الوجه {m(1)} يقابل {m(6)}، والوجه {m(2)} يقابل {m(5)}، والوجه {m(3)} يقابل {m(4)}. "
                    f"وعند فرد المكعب إلى شبكة من 6 مربعات، فإن أي مربعين يقعان في **نفس الصف أو العمود ويفصل بينهما مربع واحد بالضبط** يصبحان **وجهين متقابلين** عند الطي!"
                ),
                formula_en=dm("\\text{Opposite Face} = 7 - \\text{Visible Face} \\qquad (1\\leftrightarrow 6,\\; 2\\leftrightarrow 5,\\; 3\\leftrightarrow 4)"),
                caption_ar="قاعدة الوجه المقابل على حجر النرد القياسي:",
                formula_math_ar=dm("F_{\\text{opp}} = 7 - F"),
                diagram_en=svg_cube_net([(1, 0, "1"), (0, 1, "2"), (1, 1, "3"), (2, 1, "5"), (3, 1, "4"), (1, 2, "6")]),
            ),
            kang_concept(
                title_en="3. Transparent Card Turns & Polyomino Tiling",
                title_ar="٣. تدوير البطاقات الشفافة وتبليط قطع البوليومينو",
                body_en=(
                    f"Don't try to rotate an entire pattern in your head at once! Pick **one special corner** (like a dot in the **top-left**): "
                    f"a {m('90^\\circ')} **clockwise** ({m('\\circlearrowright')}) turn moves **top-left → top-right → bottom-right → bottom-left**. "
                    f"When tiling a board with polyominoes of size {m('k')} squares, divide the total available squares by {m('k')} and check corners so no single square gets trapped alone!"
                ),
                body_ar=(
                    f"لا تحاول تدوير الشكل كله دفعة واحدة في ذهنك! اختر **ركناً مميزاً واحداً** (مثل النقطة في **أعلى اليسار**): "
                    f"الدوران {m('90^\\circ')} **مع عقارب الساعة** ينقل الركن من **أعلى اليسار ← أعلى اليمين ← أسفل اليمين ← أسفل اليسار**. "
                    f"وعند تبليط لوحة بقطع حجم كل منها {m('k')} مربعات، اقسم المساحة الفارغة على {m('k')} وتأكد من عدم محاصرة مربع منفرد!"
                ),
                formula_en=dm("\\text{Top-Left} \\xrightarrow{90^\\circ \\text{ CW}} \\text{Top-Right} \\xrightarrow{90^\\circ \\text{ CW}} \\text{Bottom-Right} \\xrightarrow{90^\\circ \\text{ CW}} \\text{Bottom-Left}"),
                caption_ar="مسار انتقال الركن عند الدوران ربع دورة مع عقارب الساعة:",
                formula_math_ar=dm("\\text{Max Tiles} \\le \\frac{\\text{Empty Squares}}{\\text{Squares per Tile}}"),
                diagram_en=svg_kang_stamp_grid([[2, 1, 0], [0, 1, 0], [0, 0, 1]], "Pick 1 corner & rotate ↻"),
            ),
        ],
        traps_en=[
            "Trap: Counting only cube faces or cube tops visible in a drawing and forgetting the hidden cubes underneath tall back columns!",
            "Trap: Thinking two squares that touch at an edge on a cube net can be opposite! Neighboring squares fold to 90° edges—opposite faces NEVER share an edge.",
            "Trap: Confusing a 90° clockwise turn with a horizontal mirror flip! Pressing an inked rubber stamp onto paper flips left-and-right like a mirror.",
        ],
        traps_ar=[
            "فخ شائع: عدّ الأوجه الظاهرة فقط ونسيان المكعبات المخفية تحت الأعمدة الخلفية العالية!",
            "فخ شائع: الظن بأن مربعين متجاورين بحافة في الشبكة يمكن أن يتقابلا! المربعان المتجاوران يلتقيان بحافة قائمة ولا يتقابلان أبداً.",
            "فخ شائع: الخلط بين الدوران 90° والانعكاس المرآوي! طبع ختم مطاطي محبّر على الورق يعكس اليمين واليسار كالمرآة.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-04-EX1",
                title_en="Worked Example 1 — Finishing a 3 × 3 × 3 Toy Cube",
                title_ar="مثال محلول ١ — إكمال مكعب ألعاب أبعاده 3 × 3 × 3",
                q_en=f"Nora wants to build a solid {m('3 \\times 3 \\times 3')} big cube out of small unit cubes. So far she has glued three columns of heights {m(3)}, {m(2)}, and {m(1)} as shown. How many **more** unit cubes does she need?",
                q_ar=f"تريد نورة بناء مكعب مصمت كبير أبعاده {m('3 \\times 3 \\times 3')} من مكعبات صغيرة. وضعت حتى الآن ثلاثة أعمدة ارتفاعاتها {m(3)} و{m(2)} و{m(1)} كما في الشكل. كم مكعباً صغيراً **إضافياً** تحتاج؟",
                correct_val=21,
                distractors=[18, 20, 22, 24],
                idea_en="A full \\( 3 \\times 3 \\times 3 \\) cube holds \\( 27 \\) unit cubes; subtract the \\( 3 + 2 + 1 \\) cubes already placed!",
                steps_en=[
                    f"Full {m('3 \\times 3 \\times 3')} cube = {m('3 \\times 3 \\times 3 = 27')} unit cubes.",
                    f"Cubes already in Nora's three columns = {m('3 + 2 + 1 = 6')} unit cubes.",
                    f"More cubes needed = {m('27 - 6 = 21')}.",
                ],
                check_en=f"Add back: {m('6 + 21 = 27 = 3^3')} unit cubes!",
                idea_ar="المكعب الكامل \\( 3 \\times 3 \\times 3 \\) يضم \\( 27 \\) مكعباً صغيراً؛ نطرح منه مجموع الأعمدة الموجودة!",
                steps_ar=[
                    f"عدد مكعبات المجسم الكامل = {m('3 \\times 3 \\times 3 = 27')} مكعباً.",
                    f"المكعبات الموضوعة حالياً = {m('3 + 2 + 1 = 6')} مكعبات.",
                    f"المكعبات الإضافية المطلوبة = {m('27 - 6 = 21')} مكعباً.",
                ],
                check_ar=f"تحقق بالجمع: {m('6 + 21 = 27')} مكعباً!",
                diagram_en=svg_cube_stack_3d((3, 2, 1)),
            ),
            kang_worked_example(
                ex_id="KANG-L1-04-EX2",
                title_en="Worked Example 2 — Hidden Faces of Two Stacked Dice",
                title_ar="مثال محلول ٢ — الأوجه الأفقية المخفية لنردين متراصين",
                q_en=f"Zaid stacks {m(2)} standard dice one on top of the other on a table. Opposite faces on each die sum to {m(7)}. If the very top face shows {m(2)}, what is the sum of the **three hidden horizontal faces** (between the dice and against the table)?",
                q_ar=f"وضع زيد حجري نرد قياسيين أحدهما فوق الآخر على الطاولة، ومجموع كل وجهين متقابلين يساوي {m(7)}. إذا كان الوجه العلوي الظاهر يحمل {m(2)}، فما مجموع **الأوجه الأفقية الثلاثة المخفية**؟",
                correct_val=12,
                distractors=[9, 10, 11, 14],
                idea_en="Both dice have (top + bottom = \\( 7 \\)), so all \\( 4 \\) horizontal faces sum to \\( 14 \\)—just subtract the visible top face!",
                steps_en=[
                    f"On the upper die, top + bottom = {m(7)}; since top = {m(2)}, its hidden bottom face is {m('7 - 2 = 5')}.",
                    f"On the lower die, its hidden top face and hidden bottom face are opposite, so they automatically add up to {m(7)}!",
                    f"Sum of all three hidden horizontal faces = {m('5 + 7 = 12')}.",
                ],
                check_en=f"Four horizontal faces sum to {m('2 \\times 7 = 14')}; subtracting the visible {m(2)} leaves {m('14 - 2 = 12')}!",
                idea_ar="مجموع الوجه العلوي والسفلي لكل نرد يساوي \\( 7 \\)، إذن مجموع الأوجه الأفقية الأربعة \\( 14 \\)؛ نطرح الوجه العلوي الظاهر!",
                steps_ar=[
                    f"في النرد العلوي: الوجه السفلي المخفي يساوي {m('7 - 2 = 5')}.",
                    f"في النرد السفلي: الوجهان العلوي والسفلي متقابلان فمجموعهما دائماً {m(7)}.",
                    f"إذن مجموع الأوجه الأفقية الثلاثة المخفية = {m('5 + 7 = 12')}.",
                ],
                check_ar=f"بطريقة أسرع: {m('14 - 2 = 12')}!",
                diagram_en=svg_kang_cube_faces("2", "3", "4"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-04-EX3",
                title_en="Worked Example 3 — Quarter-Turn of a Transparent Grid",
                title_ar="مثال محلول ٣ — ربع دورة لبطاقة شبكية شفافة",
                q_en=f"Jude holds a {m('3 \\times 3')} transparent card with {m(8)} written in the **top-left** corner, {m(5)} in the **top-right**, and {m(3)} in the **bottom-left**. She turns the card {m('90^\\circ')} **clockwise** without flipping it. Which number is now in the **top-right** corner?",
                q_ar=f"تمسك جود بطاقة شفافة {m('3 \\times 3')} مكتوب في ركنها **العلوي الأيسر** {m(8)}، وفي **العلوي الأيمن** {m(5)}، وفي **السفلي الأيسر** {m(3)}. أدارت البطاقة {m('90^\\circ')} **مع عقارب الساعة** دون قلبها. ما العدد الذي أصبح في الركن **العلوي الأيمن**؟",
                correct_val=8,
                distractors=[3, 5, 6, 9],
                idea_en="Under a \\( 90^\\circ \\) clockwise turn, whatever started in the **top-left** corner travels into the **top-right** corner!",
                steps_en=[
                    f"Watch how the corners move {m('90^\\circ')} clockwise: **top-left → top-right**.",
                    f"Since {m(8)} started in the top-left corner, {m(8)} lands in the top-right corner!",
                ],
                check_en=f"Meanwhile {m(5)} (old top-right) moves to bottom-right, and {m(3)} (old bottom-left) moves to top-left.",
                idea_ar="عند الدوران \\( 90^\\circ \\) مع عقارب الساعة ينتقل محتوى الركن **العلوي الأيسر** إلى الركن **العلوي الأيمن**!",
                steps_ar=[
                    f"تتبّع حركة الأركان مع عقارب الساعة: **أعلى اليسار ← أعلى اليمين**.",
                    f"بما أن العدد {m(8)} كان في أعلى اليسار، فإنه يستقر في أعلى اليمين!",
                ],
                check_ar=f"وفي الوقت نفسه ينتقل {m(5)} إلى أسفل اليمين وينتقل {m(3)} إلى أعلى اليسار.",
                diagram_en=svg_kang_stamp_grid([[2, 0, 1], [0, 0, 0], [1, 0, 0]], "Turn 90° CW ↻"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-04-EX4",
                title_en="Worked Example 4 — Tiling a 4 × 6 Board with L-Trominoes",
                title_ar="مثال محلول ٤ — تبليط لوحة 4 × 6 بقطع ثلاثية على شكل L",
                q_en=f"Salman completely covers a {m('4 \\times 6')} grid board using identical 3-square L-shaped tiles with no gaps and no overlaps. How many L-tiles does he use?",
                q_ar=f"غطّى سلمان لوحة شبكية أبعادها {m('4 \\times 6')} بالكامل باستعمال قطع متطابقة على شكل حرف L مكوّنة من {m(3)} مربعات دون فراغات أو تداخل. كم قطعة استعمل؟",
                correct_val=8,
                distractors=[6, 7, 9, 12],
                idea_en="Divide the total number of board squares by \\( 3 \\), and verify that pairs of L-tiles form neat \\( 2 \\times 3 \\) rectangles!",
                steps_en=[
                    f"The {m('4 \\times 6')} board has {m('4 \\times 6 = 24')} unit squares.",
                    f"Each L-tile covers {m(3)} unit squares, so {m('24 \\div 3 = 8')} tiles are needed.",
                    f"Two L-tiles fit together into a {m('2 \\times 3')} block, and four {m('2 \\times 3')} blocks tile the {m('4 \\times 6')} board cleanly!",
                ],
                check_en=f"Check area: {m('8 \\times 3 = 24')} squares, matching {m('4 \\times 6 = 24')}!",
                idea_ar="نقسم إجمالي مربعات اللوحة على \\( 3 \\) ونتحقق من إمكانية رصّ كل قطعتين في مستطيل \\( 2 \\times 3 \\)!",
                steps_ar=[
                    f"تحتوي اللوحة {m('4 \\times 6')} على {m('4 \\times 6 = 24')} مربعاً صغيراً.",
                    f"تغطي كل قطعة {m(3)} مربعات، فيكون العدد {m('24 \\div 3 = 8')} قطع.",
                    f"كل قطعتين تشكلان مستطيلاً {m('2 \\times 3')}، وأربعة مستطيلات منها تغطي اللوحة بانتظام!",
                ],
                check_ar=f"تحقق من المساحة: {m('8 \\times 3 = 24')} مربعاً!",
                diagram_en=svg_kang_polyomino_board([
                    [1, 1, 2, 3, 3, 4],
                    [1, 2, 2, 3, 4, 4],
                    [5, 5, 6, 1, 1, 2],
                    [5, 6, 6, 1, 2, 2],
                ]),
            ),
        ],
        blueprints=[
            "kang_eco_cube_stack_count",
            "kang_eco_die_opposite_faces",
            "kang_eco_stamp_rotation",
            "kang_eco_polyomino_fit",
        ],
    )



def _lesson_1_5() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-05",
        level=LEVEL,
        unit_num="Lesson 1.5",
        topic="Combinatorics & Logic",
        title_en="Queue Positions, Folded Ribbons, Outfit Choices & Mini-Sudoku Logic",
        title_ar="مواقع الطوابير، والشرائط المطوية، وخيارات الملابس، ومنطق السودوكو المصغّر",
        summary_en=(
            "Think like a Kangaroo puzzle detective! Count lines of students without counting yourself twice, "
            "predict how many pieces fall when scissors snip a folded ribbon, multiply outfit choices, "
            "and crack mini-Sudoku and ordering riddles step by step."
        ),
        summary_ar=(
            "فكّر كمحقق ذكي في ألغاز الكنغر! احسب عدد الطلاب في الطابور دون تكرار عدّ نفسك، "
            "وتوقّع عدد القطع الناتجة عند قص شريط مطوي بالمقص، واضرب خيارات الملابس، "
            "وفكّك شبكات السودوكو المصغّر وألغاز الترتيب خطوة بخطوة."
        ),
        goals_en=[
            "Solve **queue and line-order puzzles** using **Total = Front Rank + Back Rank − 1**.",
            "Count pieces after cutting a **folded ribbon** using **Pieces = (Strands × Cuts) + 1**.",
            "Multiply choices across independent stages (**Hats × Shirts × Shoes**) instead of adding them.",
            "Eliminate impossible values in **3 × 3 and 4 × 4 mini-Sudoku grids** and clue-based orderings.",
        ],
        goals_ar=[
            "حل **مسائل الطوابير والترتيب** بالقاعدة: **العدد الكلي = الترتيب من الأمام + الترتيب من الخلف − 1**.",
            "حساب عدد القطع بعد قص **شريط مطوي** بالقاعدة: **عدد القطع = (عدد الطبقات × عدد القصّات) + 1**.",
            "ضرب عدد الخيارات المستقلة (**قبعات × قمصان × أحذية**) بدلاً من جمعها.",
            "استبعاد القيم المستحيلة في **شبكات السودوكو المصغّر** وألغاز الترتيب المنطقية.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Queue Ranks: Don't Count Yourself Twice!",
                title_ar="١. الترتيب في الطابور: لا تحسب نفسك مرتين!",
                body_en=(
                    f"Suppose Hala is **{m(6)}th from the front** and **{m(9)}th from the back** of a ticket line. "
                    f"If you add {m('6 + 9 = 15')}, Hala was included in the front group **and** in the back group! "
                    f"Subtract {m(1)} to count her once: {m('6 + 9 - 1 = 14')} people. "
                    f"Conversely, if a problem says '{m(5)} ahead of her and {m(8)} behind her,' Hala wasn't counted yet, so **add 1**: {m('5 + 8 + 1 = 14')}!"
                ),
                body_ar=(
                    f"لنفترض أن هلا هي **السادسة من الأمام** و**التاسعة من الخلف** في طابور التذاكر. "
                    f"عندما تجمع {m('6 + 9 = 15')} تكون قد حسبت هلا مرتين (مرة مع الأمام ومرة مع الخلف)! "
                    f"اطرح {m(1)} لتحسبها مرة واحدة: {m('6 + 9 - 1 = 14')} شخصاً. "
                    f"أما إذا قيل «أمامها {m(5)} وخلفها {m(8)}» فلم تُحسب هلا بعد، لذا **نضيف 1**: {m('5 + 8 + 1 = 14')}!"
                ),
                formula_en=dm("\\text{Total} = (\\text{Rank from Front}) + (\\text{Rank from Back}) - 1 = (\\text{Ahead}) + (\\text{Behind}) + 1"),
                caption_ar="قانونا حساب عدد الواقفين في الطابور:",
                formula_math_ar=dm("N = R_{\\text{front}} + R_{\\text{back}} - 1 = A + B + 1"),
                diagram_en=svg_number_strip(["1st", "...", "6th / 9th", "...", "14th"]),
            ),
            kang_concept(
                title_en="2. Cutting a Folded Ribbon with Scissors",
                title_ar="٢. قصّ شريط مطوي بالمقص",
                body_en=(
                    f"Before folding, a straight ribbon has {m(2)} loose ends and is {m(1)} whole piece. "
                    f"Every snip along an open ribbon adds **1 extra piece** ({m('k')} snips make {m('k + 1')} pieces). "
                    f"When a ribbon is folded into {m('S')} parallel layers and scissors cut straight across all layers {m('C')} times (away from the folded bends), "
                    f"that makes {m('S \\times C')} snips along the ribbon—creating **{m('S \\times C + 1')} pieces**!"
                ),
                body_ar=(
                    f"الشريط المستقيم المفتوح يبدأ كقطعة واحدة، وكل قصّة في وسطه تضيف **قطعة جديدة واحدة** ({m('k')} قصّات تصنع {m('k + 1')} قطعة). "
                    f"عندما نطوي الشريط ليصبح {m('S')} طبقات متوازية ونقصّ عبر الطبقات كلها {m('C')} مرات (بعيداً عن ثنيات الطي)، "
                    f"فإن المقص يصنع {m('S \\times C')} نقاط قص على الشريط المفتوح، فينتج **{m('S \\times C + 1')} قطعة**!"
                ),
                formula_en=dm("\\text{Pieces} = (\\text{Strands} \\times \\text{Cuts}) + 1"),
                caption_ar="عدد القطع الناتجة عند قص شريط مفتوح مطوي:",
                formula_math_ar=dm("\\text{Pieces} = S \\times C + 1"),
                diagram_en=svg_kang_folded_ribbon(4, 1),
            ),
            kang_concept(
                title_en="3. Multiplying Choices & Mini-Sudoku Grids",
                title_ar="٣. قاعدة ضرب الخيارات وشبكات السودوكو المصغّر",
                body_en=(
                    f"When choosing **one** item from {m('A')} hats **and** **one** item from {m('B')} shirts, each hat pairs with every shirt, giving {m('A \\times B')} outfits! "
                    f"In a mini-Sudoku grid where each row and column holds {m('1, 2, 3')} once, start at the row or column that already has **two** numbers filled in—the third is forced immediately!"
                ),
                body_ar=(
                    f"عند اختيار عنصر واحد من {m('A')} قبعات **و**عنصر واحد من {m('B')} قمصان، تقترن كل قبعة بجميع القمصان فيكون عدد الأطقم {m('A \\times B')}! "
                    f"وفي شبكة السودوكو المصغّر حيث يظهر كل من {m('1, 2, 3')} مرة واحدة في كل صف وعمود، ابدأ دائماً بالصف أو العمود الذي يضم **رقمين معلومين** لأن الرقم الثالث يتحدد فوراً!"
                ),
                formula_en=dm("\\text{Total Outfits} = (\\text{Hats}) \\times (\\text{Shirts}) \\times (\\text{Shoes})"),
                caption_ar="قاعدة الضرب لاختيار عنصر من كل مجموعة:",
                formula_math_ar=dm("\\text{Choices} = A \\times B \\times C"),
                diagram_en=svg_magic_square_3x3([["1", "2", "3"], ["3", "?", "2"], ["2", "3", "1"]]),
            ),
        ],
        traps_en=[
            "Trap: Adding Front Rank + Back Rank without subtracting 1! Being 7th from front and 11th from back means 7 + 11 − 1 = 17 children, NOT 18.",
            "Trap: Multiplying Strands × Cuts and forgetting the +1 on a folded ribbon! Cutting 4 strands once makes 4 × 1 + 1 = 5 pieces, NOT 4 pieces (the folded bends hold middle loops together!).",
            "Trap: Adding 3 + 4 + 2 = 9 instead of multiplying 3 × 4 × 2 = 24 when picking 1 hat AND 1 shirt AND 1 pair of shoes!",
        ],
        traps_ar=[
            "فخ شائع: جمع الترتيب من الأمام والترتيب من الخلف دون طرح 1! السابع من الأمام والحادي عشر من الخلف يعني 7 + 11 − 1 = 17 طفلاً وليس 18.",
            "فخ شائع: نسيان (+ 1) في الشريط المطوي! قص 4 طبقات مرة واحدة يعطي 4 × 1 + 1 = 5 قطع وليس 4 قطع.",
            "فخ شائع: جمع الخيارات 3 + 4 + 2 = 9 بدلاً من ضربها 3 × 4 × 2 = 24 عند اختيار قبعة وقميص وحذاء معاً!",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-05-EX1",
                title_en="Worked Example 1 — Standing in the Ice-Cream Line",
                title_ar="مثال محلول ١ — الوقوف في طابور المثلجات",
                q_en=f"Children stand in a single straight queue for Kangaroo ice cream. Hala is **{m(7)}th from the front** and **{m(11)}th from the back**. How many children are in the queue?",
                q_ar=f"يقف الأطفال في طابور واحد مستقيم لشراء المثلجات. ترتيب هلا هو **السابع من الأمام** و**الحادي عشر من الخلف**. كم طفلاً في الطابور؟",
                correct_val=17,
                distractors=[15, 16, 18, 19],
                idea_en="Add both ranks and subtract \\( 1 \\) because Hala is counted in both numbers!",
                steps_en=[
                    f"There are {m('7 - 1 = 6')} children ahead of Hala and {m('11 - 1 = 10')} children behind her.",
                    f"Counting everyone including Hala gives {m('6 + 1 + 10 = 17')} children (or {m('7 + 11 - 1 = 17')}).",
                ],
                check_en=f"In a line of {m(17)}, position {m(7)} from front has {m('17 - 7 = 10')} behind, making her {m(11)}th from back!",
                idea_ar="نجمع الترتيبين ونطرح \\( 1 \\) لأن هلا حُسبت مرتين!",
                steps_ar=[
                    f"يوجد أمام هلا {m('7 - 1 = 6')} أطفال، وخلفها {m('11 - 1 = 10')} أطفال.",
                    f"العدد الكلي = {m('6 + 1 + 10 = 17')} طفلاً (أو {m('7 + 11 - 1 = 17')}).",
                ],
                check_ar=f"في طابور من {m(17)} طفلاً، السابع من الأمام خلفه {m(10)} أطفال فهو الحادي عشر من الخلف!",
                diagram_en=svg_number_strip(["1st", "...", "Hala (7th)", "...", "Last"]),
            ),
            kang_worked_example(
                ex_id="KANG-L1-05-EX2",
                title_en="Worked Example 2 — Two Scissors Cuts Across 4 Ribbon Layers",
                title_ar="مثال محلول ٢ — قصّتان بالمقص عبر 4 طبقات من الشريط",
                q_en=f"Kangy folds one long ribbon in half twice so it makes {m(4)} parallel strands, then cuts straight across all {m(4)} strands in {m(2)} places as shown (without cutting the folded bends). How many pieces of ribbon does he get when unfolded?",
                q_ar=f"طوى الكنغر شريطاً طويلاً من المنتصف مرتين فشكّل {m(4)} طبقات متوازية، ثم قصّ بالمقص عبر الطبقات الأربع كلها في موضعين ({m(2)}) بعيداً عن الثنيات. كم قطعة شريط يحصل عليها عند فتحها؟",
                correct_val=9,
                distractors=[6, 8, 10, 12],
                idea_en="Count total snips across the unfolded ribbon (\\( 4 \\times 2 = 8 \\)), then add \\( 1 \\)!",
                steps_en=[
                    f"Each of the {m(2)} cuts slices through {m(4)} strands, making {m('4 \\times 2 = 8')} snips along the ribbon.",
                    f"Making {m(8)} snips along a single open ribbon divides it into {m('8 + 1 = 9')} separate pieces.",
                ],
                check_en=f"With {m(1)} cut across {m(4)} strands we get {m('4 + 1 = 5')} pieces; the 2nd cut adds {m(4)} more pieces: {m('5 + 4 = 9')}!",
                idea_ar="نحسب إجمالي نقاط القص على الشريط المفتوح (\\( 4 \\times 2 = 8 \\)) ثم نضيف \\( 1 \\)!",
                steps_ar=[
                    f"كل قصّة من القصّتين تقطع {m(4)} طبقات، فتصنع {m('4 \\times 2 = 8')} نقاط قص على الشريط.",
                    f"وجود {m(8)} نقاط قص يقسم الشريط الواحد المفتوح إلى {m('8 + 1 = 9')} قطع منفصلة.",
                ],
                check_ar=f"قصّة واحدة تعطي {m(5)} قطع، والقصّة الثانية تضيف {m(4)} قطع فيصبح المجموع {m(9)} قطع!",
                diagram_en=svg_kang_folded_ribbon(4, 2),
            ),
            kang_worked_example(
                ex_id="KANG-L1-05-EX3",
                title_en="Worked Example 3 — Dressing Kangy's Toy Bear",
                title_ar="مثال محلول ٣ — تنسيق ملابس الدب الصغير",
                q_en=f"Leo dresses his toy bear by choosing {m(1)} cap out of {m(3)} caps, {m(1)} shirt out of {m(4)} shirts, and {m(1)} pair of shoes out of {m(2)} pairs. How many different complete outfits can Leo make?",
                q_ar=f"يُلبس ليو دبه الصغير باختيار قبعة واحدة من {m(3)} قبعات، وقميص واحد من {m(4)} قمصان، وحذاء واحد من زوجين ({m(2)}). كم طقماً كاملاً مختلفاً يمكنه تكوينه؟",
                correct_val=24,
                distractors=[9, 14, 18, 20],
                idea_en="Multiply the number of choices at each step: \\( 3 \\times 4 \\times 2 \\)!",
                steps_en=[
                    f"Pairing {m(3)} caps with {m(4)} shirts gives {m('3 \\times 4 = 12')} cap-and-shirt combinations.",
                    f"Each of those {m(12)} combinations can wear either of the {m(2)} pairs of shoes: {m('12 \\times 2 = 24')} outfits.",
                ],
                check_en=f"Trap check: we pick a cap **and** a shirt **and** shoes, so we multiply ({m(24)}), never add ({m(9)}).",
                idea_ar="نضرب عدد الخيارات المتاحة في كل خطوة: \\( 3 \\times 4 \\times 2 \\)!",
                steps_ar=[
                    f"تنسيق {m(3)} قبعات مع {m(4)} قمصان يعطي {m('3 \\times 4 = 12')} خياراً.",
                    f"كل خيار منها يقترن بأي من الزوجين ({m(2)}) فيكون الإجمالي {m('12 \\times 2 = 24')} طقماً.",
                ],
                check_ar=f"تأكد من الضرب ({m(24)}) لا الجمع ({m(9)}) لأننا نختار من المجموعات الثلاث معاً!",
                diagram_en=svg_digit_slots(["3 caps", "4 shirts", "2 shoes"], "3 × 4 × 2 outfits"),
            ),
            kang_worked_example(
                ex_id="KANG-L1-05-EX4",
                title_en="Worked Example 4 — Cracking a 3 × 3 Mini-Sudoku Corner",
                title_ar="مثال محلول ٤ — حل ركن شبكة سودوكو مصغّرة 3 × 3",
                q_en=f"In this {m('3 \\times 3')} puzzle grid, every row and every column contains {m(1)}, {m(2)}, and {m(3)} once each. The top row reads {m('2, 1, 3')} and the left column reads {m('2, 3, 1')} from top to bottom. What number goes in the bottom-right {m('?')} square?",
                q_ar=f"في هذه الشبكة {m('3 \\times 3')} يحتوي كل صف وكل عمود على الأرقام {m(1)} و{m(2)} و{m(3)} مرة واحدة. الصف العلوي هو {m('2, 1, 3')} والعمود الأيسر من الأعلى للأسفل هو {m('2, 3, 1')}. ما الرقم في مربع {m('?')} أسفل اليمين؟",
                correct_val=2,
                distractors=[1, 3, 4, 5],
                idea_en="Fill the center cell first by checking Row 2 and Column 2 together!",
                steps_en=[
                    f"Row 2 already starts with {m(3)}, so its middle and right cells must be {m(1)} and {m(2)} in some order.",
                    f"Column 2 already has {m(1)} at the top, so the center cell cannot be {m(1)}—it must be {m(2)}, forcing Row 2's right cell to be {m(1)}.",
                    f"Now Column 3 has {m(3)} at the top and {m(1)} in the middle, so the bottom-right {m('?')} square must be {m(2)}!",
                ],
                check_en=f"Completed rows: {m('(2,1,3)')}, {m('(3,2,1)')}, {m('(1,3,2)')}—every row and column has {m('1, 2, 3')}!",
                idea_ar="نحدد خلية المركز أولاً بمقاطعة الصف الثاني مع العمود الثاني!",
                steps_ar=[
                    f"الصف الثاني يبدأ بالرقم {m(3)}، إذن خليتاه الوسطى واليمنى هما {m(1)} و{m(2)}.",
                    f"العمود الثاني فيه {m(1)} في الأعلى، لذا لا يمكن أن تكون خلية المركز {m(1)} بل هي {m(2)}، وتصبح يمين الصف الثاني {m(1)}.",
                    f"الآن العمود الثالث يضم {m(3)} و{m(1)}، فيتبقى للركن السفلي الأيمن {m('?')} الرقم {m(2)}!",
                ],
                check_ar=f"الصفوف المكتملة {m('(2,1,3)')} و{m('(3,2,1)')} و{m('(1,3,2)')} تحقق الشرط في كل صف وعمود!",
                diagram_en=svg_magic_square_3x3([["2", "1", "3"], ["3", "", ""], ["1", "", "?"]]),
            ),
        ],
        blueprints=[
            "kang_eco_queue_position",
            "kang_eco_folded_ribbon_cuts",
            "kang_eco_outfit_counting",
            "kang_eco_truth_order_puzzle",
        ],
    )



def _lesson_1_6() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L1-06",
        level=LEVEL,
        unit_num="Lesson 1.6",
        topic="Data & Probability",
        title_en="Clocks & Elapsed Time, Bar Pictographs & Guaranteed-Draw Bags",
        title_ar="الساعات والزمن المنقضي، والأعمدة البيانية، وسحب الكرات المضمون",
        summary_en=(
            "Master everyday Kangaroo data and certainty puzzles! Hop across 60-minute clock bridges without falling into the base-100 trap, "
            "decode bar charts with missing columns, outsmart the 'unluckiest draw' in a dark marble bag, "
            "and guide robots along arrow paths on a grid."
        ),
        summary_ar=(
            "أتقن ألغاز البيانات واليقين في مسابقة الكنغر! انتقل عبر جسور الساعة ذات الـ 60 دقيقة دون الوقوع في فخ المئة، "
            "واقرأ الأعمدة البيانية ذات القيم المفقودة، وتغلّب على أسوأ الحظوظ عند السحب من كيس مظلم، "
            "ووجّه الروبوتات عبر أسهم الحركة على الشبكة."
        ),
        goals_en=[
            "Calculate **elapsed time and clock hands** using **1 hour = 60 minutes** by bridging to the nearest whole hour.",
            "Read **bar charts and pictographs**, compare categories, and uncover missing bars from a known total.",
            "Find the **minimum draw to guarantee a match** by counting the worst-case non-matching draw plus **1**.",
            "Trace **arrow command sequences** (**↑, ↓, ←, →**) on a grid to find the exact finish square or path length.",
        ],
        goals_ar=[
            "حساب **الزمن المنقضي وقراءة الساعات** بقاعدة **1 ساعة = 60 دقيقة** عبر الوصول إلى الساعة الكاملة الأقرب أولاً.",
            "قراءة **الأعمدة البيانية والتمثيلات المصورة** والمقارنة بين الفئات وإيجاد العمود المفقود من المجموع الكلي.",
            "إيجاد **أقل عدد سحبات يضمن النتيجة** بحساب أسوأ حالة ممكنة ثم إضافة **1**.",
            "تتبّع **سلاسل أوامر الأسهم** (**↑، ↓، ←، →**) على الشبكة لتحديد مربع النهاية أو طول المسار.",
        ],
        concepts=[
            kang_concept(
                title_en="1. The Whole-Hour Bridge for Clocks (60 Minutes!)",
                title_ar="١. جسر الساعة الكاملة لحساب الوقت (60 دقيقة!)",
                body_en=(
                    f"Clocks count to **{m(60)} minutes**, never {m(100)}! Instead of subtracting times in columns, hop to the **next whole hour** like a stepping stone. "
                    f"For example, from `3:45` to `4:20`: hop {m('+15')} minutes to reach `4:00`, then hop {m('+20')} minutes to reach `4:20`—that is {m('15 + 20 = 35')} minutes in total!"
                ),
                body_ar=(
                    f"الساعة تتكوّن من **{m(60)} دقيقة** وليس {m(100)}! بدلاً من الطرح العمودي المربك، اقفز إلى **الساعة الكاملة التالية** كجسر مساعد. "
                    f"مثلاً من `3:45` إلى `4:20`: اقفز {m('+15')} دقيقة للوصول إلى `4:00`، ثم {m('+20')} دقيقة للوصول إلى `4:20`، فيكون الزمن {m('15 + 20 = 35')} دقيقة!"
                ),
                formula_en=dm("1\\text{ hour} = 60\\text{ minutes}, \\qquad 3\\text{:}45 \\xrightarrow{+15\\text{ min}} 4\\text{:}00 \\xrightarrow{+20\\text{ min}} 4\\text{:}20"),
                caption_ar="قاعدة الجسر الزمني عبر الساعة الكاملة:",
                formula_math_ar=dm("15 + 20 = 35\\text{ min}"),
                diagram_en=svg_analog_clock(3, 45, angle_lbl=""),
            ),
            kang_concept(
                title_en="2. Decoding Bar Charts & Missing Columns",
                title_ar="٢. قراءة الأعمدة البيانية وإيجاد العمود المفقود",
                body_en=(
                    f"Always check the **vertical scale** on the left side of a bar chart first—grid lines might jump by {m(1)}, {m(2)}, {m(4)}, or {m(5)}! "
                    f"When one bar is labeled {m('?')} and you know the grand total of all bars, add the known bars together and subtract from the grand total."
                ),
                body_ar=(
                    f"افحص دائماً **تدريج المحور الرأسي** على يسار الرسم البياني أولاً؛ فقد تقفز الخطوط بمقدار {m(1)} أو {m(2)} أو {m(4)} أو {m(5)}! "
                    f"وعندما يحمل أحد الأعمدة علامة {m('?')} مع معرفة المجموع الكلي، اجمع الأعمدة المعلومة واطرح مجموعها من الإجمالي."
                ),
                formula_en=dm("\\text{Missing Bar } (?) = \\text{Grand Total} - (\\text{Sum of Known Bars})"),
                caption_ar="إيجاد قيمة العمود المفقود من المجموع الكلي:",
                formula_math_ar=dm("\\text{Missing} = \\text{Total} - \\sum \\text{Known}"),
                diagram_en=svg_bar_chart([("Art", 14, "14"), ("Music", 11, "11"), ("Sci", 15, "?"), ("Sport", 12, "12")], y_max=20),
            ),
            kang_concept(
                title_en="3. Worst-Case Marble Draws & Grid Arrow Walks",
                title_ar="٣. أسوأ حالة سحب ومسارات الأسهم على الشبكة",
                body_en=(
                    f"To be **100% certain** of getting what you want without looking, ask: *'What is the largest number of items I could pull while STILL failing?'* "
                    f"Then add **{m('+ 1')}**! And on a grid arrow walk, pair up opposite arrows: each {m('\\rightarrow')} adds {m('+1')} column while {m('\\leftarrow')} subtracts {m('1')}, and {m('\\uparrow')} / {m('\\downarrow')} change the row!"
                ),
                body_ar=(
                    f"كي تكون **متأكداً بنسبة 100%** عند السحب دون النظر، اسأل نفسك: *«ما أكبر عدد من القطع يمكن أن أسحبه دون تحقيق الشرط بعد؟»* "
                    f"ثم أضف **{m('+ 1')}**! وفي مسارات الأسهم على الشبكة، اجمع الأسهم المتعاكسة: كل سهم {m('\\rightarrow')} يزيد العمود {m('+1')} والسهم {m('\\leftarrow')} ينقصه {m('1')}!"
                ),
                formula_en=dm("\\text{Guaranteed Draw} = (\\text{Maximum Unlucky Draws}) + 1"),
                caption_ar="قاعدة السحب المضمون (أسوأ حالة + 1):",
                formula_math_ar=dm("\\text{Sure Count} = \\text{Worst Case} + 1"),
                diagram_en=svg_kang_grid_walk(5, 4, [(0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (3, 1)]),
            ),
        ],
        traps_en=[
            "Trap: Subtracting clock times as regular base-10 numbers (like 420 − 345 = 75 instead of 4:20 − 3:45 = 35 minutes)!",
            "Trap: Answering a 'guaranteed draw' question with the lucky best case (like 2 draws for a pair)! 'To be sure' ALWAYS requires beating the worst case (+1).",
            "Trap: Counting the starting square as Step 1 on a grid walk! Each arrow moves to the NEXT square—count arrows (steps), not squares, when finding distance.",
        ],
        traps_ar=[
            "فخ شائع: طرح الأوقات كأعداد عشرية عادية (مثل 420 − 345 = 75 بدلاً من 35 دقيقة بين 3:45 و4:20)!",
            "فخ شائع: الإجابة بأفضل حظ ممكن (مثل سحبتين للحصول على زوج متماثل)! عبارة «ليضمن بالتأكيد» تتطلب دائماً التغلب على أسوأ حالة (+ 1).",
            "فخ شائع: عدّ مربع البداية كخطوة أولى على الشبكة! كل سهم يمثّل خطوة انتقال واحدة إلى المربع المجاور.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L1-06-EX1",
                title_en="Worked Example 1 — Crossing the 3:00 Hour Bridge",
                title_ar="مثال محلول ١ — عبور جسر الساعة الثالثة",
                q_en=f"Kangy's favorite nature movie begins at `2:40` PM and runs for {m(55)} minutes without breaks. How many minutes **after `3:00` PM** does the movie end?",
                q_ar=f"يبدأ الفيلم الوثائقي المفضل لدى الكنغر الساعة `2:40` مساءً ويستمر لمدة {m(55)} دقيقة متواصلة. بعد كم دقيقة من الساعة `3:00` مساءً ينتهي الفيلم؟",
                correct_val=35,
                distractors=[15, 20, 25, 45],
                idea_en="Use the minutes needed to reach `3:00` PM first, then see how many minutes of the movie remain!",
                steps_en=[
                    f"From `2:40` PM to `3:00` PM takes {m('60 - 40 = 20')} minutes.",
                    f"Out of the {m(55)}-minute movie, {m('55 - 20 = 35')} minutes remain after `3:00` PM.",
                ],
                check_en=f"The movie finishes at `3:35` PM, and {m('20 + 35 = 55')} minutes!",
                idea_ar="نحسب الدقائق اللازمة للوصول إلى `3:00` أولاً ثم نطرحها من مدة الفيلم الكلية!",
                steps_ar=[
                    f"من الساعة `2:40` حتى `3:00` تمضي {m('60 - 40 = 20')} دقيقة.",
                    f"يتبقى من مدة الفيلم بعد الساعة `3:00` مقدار {m('55 - 20 = 35')} دقيقة.",
                ],
                check_ar=f"ينتهي الفيلم الساعة `3:35` مساءً، ومجموع الجزأين {m('20 + 35 = 55')} دقيقة!",
                diagram_en=svg_analog_clock(2, 40, angle_lbl=""),
            ),
            kang_worked_example(
                ex_id="KANG-L1-06-EX2",
                title_en="Worked Example 2 — Finding the Missing Club Bar",
                title_ar="مثال محلول ٢ — إيجاد عمود النادي المفقود",
                q_en=f"Four Grade 4 clubs collected {m(52)} storybooks altogether. On the bar chart, Art collected {m(14)}, Music collected {m(11)}, Science is marked {m('?')}, and Sports collected {m(12)}. How many storybooks did the **Science** club collect?",
                q_ar=f"جمعت أربعة أندية في الصف الرابع {m(52)} قصة معاً. يظهر في الرسم البياني أن نادي الفن جمع {m(14)}، والموسيقى {m(11)}، والعلوم {m('?')}، والرياضة {m(12)}. كم قصة جمع نادي **العلوم**؟",
                correct_val=15,
                distractors=[13, 14, 16, 17],
                idea_en="Add the three known clubs and subtract their sum from \\( 52 \\)!",
                steps_en=[
                    f"Known clubs total = {m('14 + 11 + 12 = 37')} storybooks.",
                    f"Science club = {m('52 - 37 = 15')} storybooks.",
                ],
                check_en=f"Check all four bars: {m('14 + 11 + 15 + 12 = 52')} storybooks!",
                idea_ar="نجمع قصص الأندية الثلاثة المعلومة ثم نطرح المجموع من \\( 52 \\)!",
                steps_ar=[
                    f"مجموع الأندية الثلاثة المعلومة = {m('14 + 11 + 12 = 37')} قصة.",
                    f"ما جمعه نادي العلوم = {m('52 - 37 = 15')} قصة.",
                ],
                check_ar=f"مجموع الأعمدة الأربعة: {m('14 + 11 + 15 + 12 = 52')} قصة!",
                diagram_en=svg_bar_chart([("Art", 14, "14"), ("Music", 11, "11"), ("Sci", 15, "?"), ("Sport", 12, "12")], y_max=20),
            ),
            kang_worked_example(
                ex_id="KANG-L1-06-EX3",
                title_en="Worked Example 3 — Guaranteed Pair of Marbles in the Dark",
                title_ar="مثال محلول ٣ — ضمان سحب كرتين من اللون نفسه في الظلام",
                q_en=f"A velvet bag holds {m(6)} red marbles, {m(5)} blue marbles, and {m(4)} yellow marbles. Without looking, what is the **smallest** number of marbles Pippa must draw to be **100% sure** she gets at least {m(2)} marbles of the **same color**?",
                q_ar=f"يحتوي كيس مخملي على {m(6)} كرات حمراء و{m(5)} زرقاء و{m(4)} صفراء. دون النظر، ما **أصغر** عدد من الكرات يجب أن تسحبه بيبا لتكون **متأكدة تماماً** من حصولها على كرتين ({m(2)}) على الأقل من **اللون نفسه**؟",
                correct_val=4,
                distractors=[2, 3, 5, 7],
                idea_en="With \\( 3 \\) colors, the worst luck gives \\( 1 \\) marble of each color on the first \\( 3 \\) draws—then the 4th draw forces a pair!",
                steps_en=[
                    f"In the worst case, Pippa's first {m(3)} marbles are {m(1)} red, {m(1)} blue, and {m(1)} yellow—still no matching pair!",
                    f"When she draws the **4th** marble, it must be red, blue, or yellow, matching one she already holds!",
                ],
                check_en=f"With {m(3)} draws she might have R-B-Y (no pair), so {m(3)} is not enough; {m(4)} guarantees a pair!",
                idea_ar="مع وجود \\( 3 \\) ألوان، أسوأ حظ يعطي كرة واحدة من كل لون في أول \\( 3 \\) سحبات، ثم تضمن السحبة الرابعة التطابق!",
                steps_ar=[
                    f"في أسوأ حالة تكون أول {m(3)} كرات هي: حمراء واحدة وزرقاء واحدة وصفراء واحدة دون أي زوج متطابق.",
                    f"عند سحب الكرة **الرابعة** لا بد أن تطابق أحد الألوان الثلاثة الموجودة بيدها!",
                ],
                check_ar=f"ثلاث سحبات قد تعطي ثلاثة ألوان مختلفة، أما {m(4)} سحبات فتضمن زوجاً متماثلاً دائماً!",
                diagram_en=svg_pie_chart([(6 / 15, "6 Red"), (5 / 15, "5 Blue"), (4 / 15, "4 Yellow")]),
            ),
            kang_worked_example(
                ex_id="KANG-L1-06-EX4",
                title_en="Worked Example 4 — Guiding a Toy Robot Along Grid Arrows",
                title_ar="مثال محلول ٤ — توجيه روبوت صغير عبر أسهم الشبكة",
                q_en=f"On a {m('6 \\times 5')} grid, columns are numbered {m(1)} to {m(6)} from left to right and rows {m(1)} to {m(5)} from bottom to top. A robot starts on square {m('(1, 2)')} and follows `→, →, ↑, ↑, →, ↓, →`. What is the **sum** of its final column number and final row number?",
                q_ar=f"على شبكة أبعادها {m('6 \\times 5')}، تُرقّم الأعمدة من {m(1)} إلى {m(6)} من اليسار لليمين، والصفوف من {m(1)} إلى {m(5)} من الأسفل للأعلى. يبدأ روبوت عند المربع {m('(1, 2)')} ويتبع الأسهم `→, →, ↑, ↑, →, ↓, →`. ما **مجموع** رقم عموده النهائي ورقم صفه النهائي؟",
                correct_val=8,
                distractors=[6, 7, 9, 10],
                idea_en="Count total right/left arrows to update the column, and total up/down arrows to update the row!",
                steps_en=[
                    f"There are {m(4)} right arrows (`→`) and {m(0)} left arrows, so final column = {m('1 + 4 = 5')}.",
                    f"There are {m(2)} up arrows (`↑`) and {m(1)} down arrow (`↓`), so final row = {m('2 + 2 - 1 = 3')}.",
                    f"The robot lands on {m('(5, 3)')}, and the sum is {m('5 + 3 = 8')}.",
                ],
                check_en=f"Step-by-step: {m('(1,2)\\to(2,2)\\to(3,2)\\to(3,3)\\to(3,4)\\to(4,4)\\to(4,3)\\to(5,3)')}, sum = {m(8)}!",
                idea_ar="نحسب صافي حركة اليمين واليسار لتحديد العمود، وصافي حركة الأعلى والأسفل لتحديد الصف!",
                steps_ar=[
                    f"يوجد {m(4)} أسهم لليمين، فيكون رقم العمود النهائي {m('1 + 4 = 5')}.",
                    f"يوجد سهمان للأعلى وسهم للأسفل، فيكون رقم الصف النهائي {m('2 + 2 - 1 = 3')}.",
                    f"يصل الروبوت إلى {m('(5, 3)')}، ومجموع الإحداثيين يساوي {m('5 + 3 = 8')}.",
                ],
                check_ar=f"بالتتبع المباشر خطوة بخطوة نصل إلى {m('(5, 3)')} والمجموع {m(8)}!",
                diagram_en=svg_kang_grid_walk(6, 5, [(0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (3, 1), (3, 2), (4, 2)]),
            ),
        ],
        blueprints=[
            "kang_eco_clock_elapsed",
            "kang_eco_bar_chart_read",
            "kang_eco_worst_case_draw",
            "kang_eco_grid_arrow_walk",
        ],
    )


def get_ecolier_lessons() -> list[dict]:
    """Return all 6 Kangaroo Ecolier (Grades 3–4) bilingual study lessons."""
    return [
        _lesson_1_1(),
        _lesson_1_2(),
        _lesson_1_3(),
        _lesson_1_4(),
        _lesson_1_5(),
        _lesson_1_6(),
    ]
