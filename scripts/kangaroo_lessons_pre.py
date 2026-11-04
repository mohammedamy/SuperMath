"""Rich Bilingual Study Lessons for Kangaroo Math Competition — PreEcolier Division (Grades 1–2)."""

from kangaroo_common import (
    dm,
    kang_concept,
    kang_worked_example,
    m,
    make_kangaroo_lesson,
    svg_analog_clock,
    svg_balance_scales,
    svg_bar_chart,
    svg_cube_stack_3d,
    svg_digit_slots,
    svg_fenceposts,
    svg_function_machine,
    svg_kang_folded_ribbon,
    svg_kang_grid_walk,
    svg_kang_magic_cross,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_polyomino_board,
    svg_kang_stamp_grid,
    svg_number_strip,
    svg_pre_coin_purse,
    svg_pre_die_dots,
    svg_pre_icon_addition,
    svg_pre_marble_bag,
    svg_pre_paired_items,
    svg_pre_queue_line,
    svg_pre_shape_collage,
    svg_pre_tens_ones_blocks,
    svg_spinner,
)

LEVEL = "PreEcolier"


def _lesson_p_1() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-01",
        level=LEVEL,
        unit_num="P.1",
        topic="Number Theory",
        title_en="Skip-Counting Hops, Place-Value Cards, Mini Pyramids & Pairing Socks",
        title_ar="قفزات العدّ النمطي، وبطاقات العشرات والآحاد، والأهرامات الصغيرة، وتكوين الأزواج",
        summary_en=(
            "Welcome to Kangaroo PreEcolier! Join Little Kangy to hop by equal steps along river stones, "
            "build two-digit numbers with tens rods and ones cubes, climb mini 3-row brick pyramids, "
            "and pair up colourful socks and mittens to spot even and odd numbers."
        ),
        summary_ar=(
            "مرحباً بك في مستوى بري-إيكولير (الصف الأول والثاني) لمسابقة الكنغر! رافق الكنغر الصغير "
            "في قفزاته المتساوية على الحجارة، وكوّن الأعداد من رقمين بعمود العشرات ومكعبات الآحاد، "
            "وتسلّق أهرامات الطوب الصغيرة، وجمّع الجوارب والقفازات في أزواج لتمييز الزوجي والفردي."
        ),
        goals_en=[
            "Hop forward and backward by **2s, 3s, 4s, 5s, and 10s**, counting the **jumps** carefully from the starting stone.",
            "Read **tens rods and ones cubes** and arrange digit cards to build the **largest** and **smallest** 2-digit numbers without putting **0** in the tens spot.",
            "Solve **mini 3-row brick pyramids** where each upper brick holds the sum of the two bricks right below it.",
            "Group **socks, shoes, and gloves** into pairs of **2** to tell **even** numbers (0 left over) from **odd** numbers (1 lonely item left).",
        ],
        goals_ar=[
            "القفز للأمام والخلف بمقدار **2 أو 3 أو 4 أو 5 أو 10** مع عدّ **القفزات** بدقة انطلاقاً من حجر البداية.",
            "قراءة **أعمدة العشرات ومكعبات الآحاد** وترتيب بطاقات الأرقام لتكوين **أكبر وأصغر عدد من رقمين** دون وضع **0** في منزلة العشرات.",
            "حل **أهرامات الطوب الصغيرة من 3 صفوف** حيث تساوي كل طوبة علوية مجموع الطوبتين أسفلها مباشرة.",
            "تجميع **الجوارب والأحذية والقفازات** في أزواج من **2** للتمييز بين العدد **الزوجي** (بلا باقٍ) والعدد **الفردي** (يبقى عنصر واحد منفرد).",
        ],
        concepts=[
            kang_concept(
                title_en="1. Skip-Counting Hops & Two-Digit Place Cards",
                title_ar="١. قفزات العدّ النمطي وبطاقات العشرات والآحاد",
                body_en=(
                    f"When Little Kangy starts on a stone and makes equal hops, add the hop size once for **each jump**! "
                    f"In any two-digit number up to {m(99)}, the **left digit** counts stacks of **tens** ({m(10)}) and the **right digit** counts single **ones** ({m(1)}): "
                    f"{m(3)} tens and {m(4)} ones make {m('30 + 4 = 34')}. "
                    f"To make the **biggest** 2-digit number from cards, put your largest digit in the tens spot; for the **smallest** 2-digit number, put the smallest **non-zero** digit in the tens spot!"
                ),
                body_ar=(
                    f"عندما يقفز الكنغر الصغير قفزات متساوية، نضيف مقدار القفزة مرة واحدة عن **كل قفزة**! "
                    f"وفي أي عدد مكوّن من رقمين حتى {m(99)}، يدل الرقم الأيسر على **العشرات** ({m(10)}) والرقم الأيمن على **الآحاد** ({m(1)}): "
                    f"فمثلاً {m(3)} عشرات و{m(4)} آحاد تكوّن العدد {m('30 + 4 = 34')}. "
                    f"لتكوين **أكبر** عدد من رقمين نضع أكبر رقم في العشرات، ولتكوين **أصغر** عدد من رقمين نضع أصغر رقم **غير الصفر** في العشرات!"
                ),
                formula_en=dm("3 \\text{ Tens} + 4 \\text{ Ones} = 30 + 4 = 34"),
                caption_ar="تكوين العدد المكوّن من رقمين من العشرات والآحاد:",
                formula_math_ar=dm("3 \\times 10 + 4 = 34"),
                diagram_en=svg_pre_tens_ones_blocks(3, 4, "34"),
            ),
            kang_concept(
                title_en="2. Mini 3-Row Brick Number Pyramids",
                title_ar="٢. أهرامات الطوب العددية الصغيرة ذات الصفوف الثلاثة",
                body_en=(
                    f"In Kangy's brick pyramid, every brick sits on **two** bricks right below it and holds their **sum**! "
                    f"Look at the bottom row {m(4)}, {m(5)}, and {m(3)}: on the left {m('4 + 5 = 9')}, on the right {m('5 + 3 = 8')}, and at the very top {m('9 + 8 = 17')}. "
                    f"Notice a fun Kangaroo secret: the middle bottom brick ({m(5)}) climbs into **both** middle bricks, so it gets counted **twice** in the top brick! "
                    f"If an upper brick and one brick under it are known, **subtract** to find its partner."
                ),
                body_ar=(
                    f"في هرم الطوب العددي، تجلس كل طوبة فوق **طوبتين** أسفلها مباشرة وتساوي **مجموعهما**! "
                    f"انظر إلى الصف السفلي {m(4)} و{m(5)} و{m(3)}: على اليسار {m('4 + 5 = 9')}، وعلى اليمين {m('5 + 3 = 8')}، وفي القمة {m('9 + 8 = 17')}. "
                    f"لاحظ سرّ الكنغر الجميل: الطوبة الوسطى ({m(5)}) تدخل في طوبتي الوسط معاً، لذلك تُحسب **مرتين** في طوبة القمة! "
                    f"وإذا علمتَ طوبة علوية وإحدى الطوبتين تحتها، استعمل **الطرح** لإيجاد جارتها."
                ),
                formula_en=dm("4 + 5 = 9, \\qquad 5 + 3 = 8, \\qquad 9 + 8 = 17"),
                caption_ar="قاعدة الجمع خطوة بخطوة في هرم الطوب الصغير:",
                formula_math_ar=dm("4 + 5 = 9, \\qquad 5 + 3 = 8, \\qquad 9 + 8 = 17"),
                diagram_en=svg_kang_number_pyramid([["17"], ["9", "8"], ["4", "5", "3"]]),
            ),
            kang_concept(
                title_en="3. Pairing Socks & Gloves: Even vs. Odd",
                title_ar="٣. تجميع الجوارب والقفازات: الزوجي والفردي",
                body_en=(
                    f"Line up socks or mittens and bundle them into **pairs of {m(2)}**! "
                    f"If every item finds a partner with **{m(0)} left over**, the total is **even** ({m('2, 4, 6, 8, 10, \\dots')}). "
                    f"If **{m(1)} lonely item** is left without a partner—like {m(9)} items making {m(4)} pairs plus {m(1)} extra—the total is **odd** ({m('1, 3, 5, 7, 9, \\dots')}). "
                    f"When you put **two odd groups** together, their two lonely leftovers join hands to make one brand-new pair, so **Odd + Odd = Even**!"
                ),
                body_ar=(
                    f"رتّب الجوارب أو القفازات وجمّع كل **اثنين معاً في زوج واحد**! "
                    f"إذا وجد كل عنصر شريكاً ولم يبقَ شيء (**الباقي {m(0)}**)، فالعدد **زوجي** ({m('2, 4, 6, 8, 10, \\dots')}). "
                    f"وإذا بقيت **قطعة واحدة منفردة** بلا شريك — مثل {m(9)} قطع تصنع {m(4)} أزواج وتبقى {m(1)} — فالعدد **فردي** ({m('1, 3, 5, 7, 9, \\dots')}). "
                    f"وعند جمع **مجموعتين فرديتين** تتحد القطعتان المنفردتان لتصنعا زوجاً جديداً، ولذلك **فردي + فردي = زوجي**!"
                ),
                formula_en=dm("9 = 4 \\times 2 + 1 \\quad (\\text{4 full pairs and 1 left over})"),
                caption_ar="تجميع العناصر اثنين اثنين لمعرفة الأزواج والباقي:",
                formula_math_ar=dm("9 = 4 \\times 2 + 1"),
                diagram_en=svg_pre_paired_items(9, "4 Pairs"),
            ),
        ],
        traps_en=[
            "Trap: Counting the starting stone as Hop 1! Starting on 6 and making 5 hops of +4 adds 20 to reach 26, NOT 22.",
            "Trap: Putting 0 in the tens place for a 2-digit number! With cards 0, 3, 8, writing 03 is a 1-digit number; the smallest 2-digit number is 30.",
            "Trap: Mixing up single socks with pairs of socks! 10 single socks make 5 pairs, whereas 10 pairs equal 20 single socks.",
        ],
        traps_ar=[
            "فخ شائع: عدّ حجر البداية كأنه القفزة الأولى! البدء عند 6 والقفز 5 قفزات بمقدار +4 يوصلك إلى 26 وليس 22.",
            "فخ شائع: وضع الصفر 0 في منزلة العشرات! بالبطاقات 0 و3 و8، الكتابة 03 تعطي عدداً من رقم واحد، أما أصغر عدد من رقمين فهو 30.",
            "فخ شائع: الخلط بين عدد الفردات وعدد الأزواج! 10 جوارب مفردة تصنع 5 أزواج فقط، بينما 10 أزواج تعني 20 فردة.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-01-EX1",
                title_en="Kangy's Equal Stepping-Stone Hops",
                title_ar="قفزات الكنغر المتساوية على حجارة النهر",
                q_en=f"Little Kangy stands on stone {m(6)} and makes {m(5)} equal hops forward. Each hop adds {m(4)} to his stone number (`6, 10, 14, ...`). Which stone number {m('?')} does Kangy land on after his **5th** hop?",
                q_ar=f"يقف الكنغر الصغير على الحجر رقم {m(6)} ويقفز {m(5)} قفزات متساوية للأمام، وتضيف كل قفزة {m(4)} إلى رقم الحجر (`6, 10, 14, ...`). على أي حجر {m('?')} يهبط الكنغر بعد قفزته **الخامسة**؟",
                correct_val=26,
                distractors=[20, 22, 24, 30],
                idea_en="Start at \\( 6 \\) and add \\( 4 \\) five times—one \\( +4 \\) for each hop!",
                steps_en=[
                    f"After Hop 1: {m('6 + 4 = 10')}; after Hop 2: {m('10 + 4 = 14')}.",
                    f"After Hop 3: {m('14 + 4 = 18')}; after Hop 4: {m('18 + 4 = 22')}.",
                    f"After Hop 5: {m('22 + 4 = 26')}.",
                ],
                check_en=f"Five hops of {m(4)} cover {m('5 \\times 4 = 20')}, and {m('6 + 20 = 26')}!",
                idea_ar="نبدأ من العدد \\( 6 \\) ونضيف \\( 4 \\) خمس مرات — أي مرة واحدة لكل قفزة!",
                steps_ar=[
                    f"بعد القفزة ١: {m('6 + 4 = 10')}، وبعد القفزة ٢: {m('10 + 4 = 14')}.",
                    f"بعد القفزة ٣: {m('14 + 4 = 18')}، وبعد القفزة ٤: {m('18 + 4 = 22')}.",
                    f"بعد القفزة ٥: {m('22 + 4 = 26')}.",
                ],
                check_ar=f"خمس قفزات طول كل منها {m(4)} تساوي {m('5 \\times 4 = 20')}، وبإضافة نقطة البداية {m('6 + 20 = 26')}!",
                diagram_en=svg_number_strip(["6", "10", "14", "...", "?"]),
            ),
            kang_worked_example(
                ex_id="KANG-L0-01-EX2",
                title_en="Biggest Minus Smallest Two-Digit Card Number",
                title_ar="الفرق بين أكبر وأصغر عدد من رقمين",
                q_en=f"Sara holds three digit cards: {m(0)}, {m(3)}, and {m(8)}. Picking two cards at a time, she forms the **largest** possible 2-digit number and the **smallest** possible 2-digit number. What is the difference between her two numbers?",
                q_ar=f"مع سارة ثلاث بطاقات أرقام: {m(0)} و{m(3)} و{m(8)}. تختار بطاقتين في كل مرة لتكوّن **أكبر** عدد ممكن من رقمين و**أصغر** عدد ممكن من رقمين. ما الفرق بين العددين؟",
                correct_val=53,
                distractors=[45, 50, 55, 80],
                idea_en="Put the biggest digits on the left for the largest 2-digit number, and remember \\( 0 \\) cannot sit in the tens place!",
                steps_en=[
                    f"For the **largest** 2-digit number, put {m(8)} in the tens spot and {m(3)} in the ones spot to get {m(83)}.",
                    f"For the **smallest** 2-digit number, {m(0)} cannot go in the tens spot, so put {m(3)} in the tens spot and {m(0)} in the ones spot to get {m(30)}.",
                    f"Subtract the two numbers: {m('83 - 30 = 53')}.",
                ],
                check_en=f"Add back to check: {m('30 + 53 = 83')}, and both {m(83)} and {m(30)} are valid 2-digit numbers!",
                idea_ar="نضع أكبر رقم في العشرات لأكبر عدد، ونتذكر أن الصفر \\( 0 \\) لا يوضع في منزلة العشرات!",
                steps_ar=[
                    f"لتكوين **أكبر** عدد من رقمين نضع {m(8)} في العشرات و{m(3)} في الآحاد فنحصل على {m(83)}.",
                    f"لتكوين **أصغر** عدد من رقمين لا نضع {m(0)} في العشرات، بل نضع {m(3)} في العشرات و{m(0)} في الآحاد فنحصل على {m(30)}.",
                    f"نحسب الفرق بالطرح: {m('83 - 30 = 53')}.",
                ],
                check_ar=f"بالجمع العكسي: {m('30 + 53 = 83')}، وكلا العددين مكوّن من رقمين!",
                diagram_en=svg_digit_slots(["0", "3", "8"], "2-Digit?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-01-EX3",
                title_en="Top Brick of a Mini Number Pyramid",
                title_ar="طوبة القمة في هرم الأعداد الصغير",
                q_en=f"In Kangy's mini pyramid, each brick holds the sum of the two bricks directly underneath it. The bottom row has {m(7)}, {m(5)}, and {m(8)}. What number belongs in the top {m('?')} brick?",
                q_ar=f"في هرم الكنغر الصغير، كل طوبة تساوي مجموع الطوبتين أسفلها مباشرة. الصف السفلي يحوي الأعداد {m(7)} و{m(5)} و{m(8)}. ما العدد الذي يوضع في طوبة القمة {m('?')}؟",
                correct_val=25,
                distractors=[20, 22, 27, 30],
                idea_en="Fill in the two middle-row bricks first by adding neighboring pairs from the bottom row!",
                steps_en=[
                    f"Left middle brick = {m('7 + 5 = 12')}.",
                    f"Right middle brick = {m('5 + 8 = 13')}.",
                    f"Top brick = {m('12 + 13 = 25')}.",
                ],
                check_en=f"Notice the middle bottom brick {m(5)} is counted twice: {m('7 + 5 + 5 + 8 = 25')}!",
                idea_ar="نملأ طوبتي الصف الأوسط أولاً بجمع كل طوبتين متجاورتين في الصف السفلي!",
                steps_ar=[
                    f"الطوبة الوسطى اليسرى = {m('7 + 5 = 12')}.",
                    f"الطوبة الوسطى اليمنى = {m('5 + 8 = 13')}.",
                    f"طوبة القمة = {m('12 + 13 = 25')}.",
                ],
                check_ar=f"الطوبة السفلية الوسطى {m(5)} جُمعت مرتين: {m('7 + 5 + 5 + 8 = 25')}!",
                diagram_en=svg_kang_number_pyramid([["?"], ["", ""], ["7", "5", "8"]]),
            ),
            kang_worked_example(
                ex_id="KANG-L0-01-EX4",
                title_en="Matching Pairs of Mittens on Laundry Day",
                title_ar="تجميع القفازات المتطابقة في أزواج",
                q_en=f"Omar takes {m(15)} single red mittens and {m(4)} single blue mittens out of the basket. Two mittens make a matching pair only when they have the **same colour**. How many **complete matching pairs** can Omar make altogether?",
                q_ar=f"أخرج عمر {m(15)} فردة قفاز حمراء و{m(4)} فردات قفاز زرقاء من السلة. لا يتكوّن زوج متطابق إلا من فردتين لهما **اللون نفسه**. كم **زوجاً متطابقاً كاملاً** يمكن لعمر تكوينه إجمالاً؟",
                correct_val=9,
                distractors=[8, 10, 11, 19],
                idea_en="Bundle the red mittens into pairs of \\( 2 \\) and the blue mittens into pairs of \\( 2 \\) separately!",
                steps_en=[
                    f"From {m(15)} red mittens, Omar makes {m(7)} red pairs ({m('7 \\times 2 = 14')}) with {m(1)} lonely red mitten left over.",
                    f"From {m(4)} blue mittens, Omar makes {m(2)} blue pairs ({m('2 \\times 2 = 4')}) with {m(0)} blue mittens left over.",
                    f"Total matching pairs = {m('7 + 2 = 9')}.",
                ],
                check_en=f"Used mittens = {m('9 \\times 2 = 18')}, plus {m(1)} leftover red mitten gives all {m('18 + 1 = 19')} mittens!",
                idea_ar="نجمّع القفازات الحمراء اثنين اثنين على حدة، والزرقاء اثنين اثنين على حدة!",
                steps_ar=[
                    f"من {m(15)} فردة حمراء يصنع عمر {m(7)} أزواج حمراء ({m('7 \\times 2 = 14')}) وتبقى فردة حمراء واحدة.",
                    f"من {m(4)} فردات زرقاء يصنع عمر زوجين أزرقين ({m('2 \\times 2 = 4')}) دون باقٍ.",
                    f"مجموع الأزواج المتطابقة = {m('7 + 2 = 9')} أزواج.",
                ],
                check_ar=f"عدد الفردات المستعملة {m('9 \\times 2 = 18')} + فردة حمراء باقية = {m(19)} فردة!",
                diagram_en=svg_pre_paired_items(15, "Pairs ?"),
            ),
        ],
        blueprints=[
            "kang_pre_skip_counting_hops",
            "kang_pre_two_digit_place_cards",
            "kang_pre_mini_brick_pyramids",
            "kang_pre_even_odd_sock_gloves",
        ],
    )


def _lesson_p_2() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-02",
        level=LEVEL,
        unit_num="P.2",
        topic="Algebra",
        title_en="Toy Pan Balances, Picture Sums, Repeating Bead Trains & Secret Rule Boxes",
        title_ar="ميزان الألعاب ذو الكفتين، وجمع الرموز المصوّرة، وقطار الخرز المتكرر، وصناديق الأعداد",
        summary_en=(
            "Step into Kangaroo puzzle-algebra without any scary letters! Trade equal toys on pan balances, "
            "crack secret numbers hidden behind stars and hearts, spot repeating groups on colourful bead necklaces, "
            "and walk forward and backward through magic number boxes."
        ),
        summary_ar=(
            "اكتشف جبر الألغاز الممتع في الكنغر بالصور والألعاب دون أي رموز معقدة! استبدل الألعاب المتساوية "
            "على الميزان ذي الكفتين، واكشف الأعداد المخبأة خلف النجوم والقلوب، وتتبّع النمط المتكرر في قطار الخرز، "
            "وتحرّك للأمام والخلف داخل صناديق الأعداد السرية."
        ),
        goals_en=[
            "Keep a **toy pan balance** level by removing matching toys from both pans or swapping equal weights.",
            "Solve **picture and fruit addition puzzles** where identical icons always stand for the same number.",
            "Find the **repeating core group** of a bead train or necklace to count colours or predict later beads.",
            "Follow **In-and-Out number boxes** forward and undo each step in reverse to uncover a mystery input.",
        ],
        goals_ar=[
            "الحفاظ على توازن **ميزان الكفتين** بحذف الألعاب المتماثلة من الجانبين أو استبدال الأوزان المتساوية.",
            "حل **ألغاز جمع الصور والفواكه** حيث يدل الشكل نفسه دائماً على العدد نفسه.",
            "اكتشاف **المجموعة الأساسية المتكررة** في قطار الخرز أو العقد لعدّ الألوان أو معرفة الخرزات التالية.",
            "تتبّع **صناديق المدخلات والمخرجات** للأمام وعكس العمليات بالترتيب العكسي لإيجاد العدد السري.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Toy Pan Balances & Trading Equal Weights",
                title_ar="١. ميزان الألعاب واستبدال الأوزان المتساوية",
                body_en=(
                    f"When a balance beam sits flat and level, both pans have the **exact same weight**! "
                    f"You can take the **same toy** off both sides and the beam stays level. "
                    f"You can also **swap** equal weights: on the two scales below, {m(1)} green block balances {m(2)} orange balls on the left, "
                    f"and {m(1)} green block also balances {m(3)} purple cones on the right—so {m(2)} orange balls weigh the exact same as {m(3)} purple cones!"
                ),
                body_ar=(
                    f"عندما تكون ذراع الميزان أفقية تماماً، فإن الكفتين لهما **الوزن نفسه بالضبط**! "
                    f"يمكنك رفع **اللعبة نفسها** من الكفتين معاً وسيبقى الميزان متوازناً. "
                    f"ويمكنك أيضاً **استبدال** الأوزان المتساوية: في الشكل أدناه، مكعب أخضر واحد يوازن كرتين برتقاليتين في الميزان الأول، "
                    f"ويوازن {m(3)} مخاريط بنفسجية في الميزان الثاني، إذن كرتان برتقاليتان توازنان {m(3)} مخاريط بنفسجية!"
                ),
                formula_en=dm("1\\;\\text{Block} = 2\\;\\text{Balls}, \\quad 1\\;\\text{Block} = 3\\;\\text{Cones} \\implies 2\\;\\text{Balls} = 3\\;\\text{Cones}"),
                caption_ar="قاعدة استبدال الأوزان المتساوية على الميزان:",
                formula_math_ar=dm("2\\;\\text{Balls} = 1\\;\\text{Block} = 3\\;\\text{Cones}"),
                diagram_en=svg_balance_scales(2, 1, 1, 3),
            ),
            kang_concept(
                title_en="2. Picture & Fruit Sums: Same Icon, Same Number",
                title_ar="٢. جمع الصور والرموز: الشكل نفسه يعني العدد نفسه",
                body_en=(
                    f"In Kangaroo picture sums, every copy of the same icon hides the **same secret number**. "
                    f"Always start with the row that has **only one kind of shape**! "
                    f"In the top row below, two identical gold stars make {m(10)}, so each star must be half of {m(10)}, which is {m(5)}. "
                    f"Now write {m(5)} on top of the star in the second row: {m('5 + \\heartsuit = 13')}, so the pink heart equals {m('13 - 5 = 8')}!"
                ),
                body_ar=(
                    f"في ألغاز الجمع المصوّرة، كل شكل مكرر يخفي وراءه **العدد السري نفسه**. "
                    f"ابدأ دائماً بالسطر الذي يحتوي على **نوع واحد فقط من الأشكال**! "
                    f"في السطر العلوي أدناه، نجمتان ذهبيتان مجموعهما {m(10)}، إذن كل نجمة تساوي نصف {m(10)} أي {m(5)}. "
                    f"نكتب الآن {m(5)} مكان النجمة في السطر الثاني: {m('5 + \\heartsuit = 13')}، فنجد أن القلب الوردي يساوي {m('13 - 5 = 8')}!"
                ),
                formula_en=dm("\\bigstar + \\bigstar = 10 \\implies \\bigstar = 5, \\qquad 5 + \\heartsuit = 13 \\implies \\heartsuit = 8"),
                caption_ar="البدء بالسطر ذي الرمز الواحد ثم التعويض في السطر الثاني:",
                formula_math_ar=dm("\\bigstar = 5, \\qquad \\heartsuit = 13 - 5 = 8"),
                diagram_en=svg_pre_icon_addition(["star", "star"], "10", ["star", "heart"], "13"),
            ),
            kang_concept(
                title_en="3. Repeating Bead Trains & In-Out Rule Boxes",
                title_ar="٣. قطار الخرز المتكرر وصناديق الأعداد السرية",
                body_en=(
                    f"A **repeating bead train** copies one short **core group** over and over—for example, `Red, Blue, Blue` has length {m(3)}, so every group of {m(3)} beads holds {m(1)} Red and {m(2)} Blue beads! "
                    f"In an **In-and-Out number machine**, follow the arrows left-to-right when you know the start number. "
                    f"When you only know the **end** number, walk **backward from right to left** and do the **opposite** step (`+` becomes `-`, and doubling becomes halving)!"
                ),
                body_ar=(
                    f"ينسخ **قطار الخرز المتكرر** مجموعة أساسية قصيرة مراراً وتكراراً — مثل `أحمر، أزرق، أزرق` وطولها {m(3)} خرزات، فكل مجموعة من {m(3)} خرزات تضم خرزة حمراء وخرزتين زرقاوين! "
                    f"وفي **صندوق الأعداد**، اتبع الأسهم من اليسار لليمين إذا علمتَ عدد البداية. "
                    f"أما إذا علمتَ **عدد النهاية** فقط، فارجع **عكسياً من اليمين لليسار** واعكس كل عملية (الجمع يصبح طرحاً، والمضاعفة تصبح أخذ النصف)!"
                ),
                formula_en=dm("7 \\xrightarrow{+4} 11 \\xrightarrow{\\times 2} 22 \\quad \\Longleftrightarrow \\quad 22 \\xrightarrow{\\div 2} 11 \\xrightarrow{-4} 7"),
                caption_ar="التقدم للأمام والرجوع بالعكس في آلة الأعداد:",
                formula_math_ar=dm("7 \\xrightarrow{+4} 11 \\xrightarrow{\\times 2} 22 \\quad \\Longleftrightarrow \\quad 22 \\xrightarrow{\\div 2} 11 \\xrightarrow{-4} 7"),
                diagram_en=svg_function_machine("7", "+ 4", "× 2", "22"),
            ),
        ],
        traps_en=[
            "Trap: Stopping as soon as you find the first shape! Always check whether the question asks for one shape or the sum of two shapes.",
            "Trap: Counting all beads in the picture instead of just ONE repeating block! In R, B, B, R, B, B, the core block has 3 beads, not 6.",
            "Trap: Reversing a 2-step number box in the wrong order! Undo the LAST box first, then undo the FIRST box.",
        ],
        traps_ar=[
            "فخ شائع: التوقف بمجرد إيجاد قيمة الشكل الأول! تأكد دائماً هل يطلب السؤال قيمة شكل واحد أم مجموع شكلين معاً.",
            "فخ شائع: عدّ جميع الخرزات المرسومة بدلاً من طول المجموعة المتكررة الواحدة! في (أحمر، أزرق، أزرق، أحمر، أزرق، أزرق) طول النمط 3 وليس 6.",
            "فخ شائع: عكس صندوقي الأعداد بترتيب خاطئ! عند الرجوع للخلف اعكس الصندوق الأخير أولاً ثم الصندوق الأول.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-02-EX1",
                title_en="Trading Toy Balls, Blocks, and Cones",
                title_ar="استبدال الكرات والمكعبات والمخاريط على الميزان",
                q_en=f"On the left balance scale, {m(3)} orange balls weigh the same as {m(1)} green block. On the right balance scale, {m(2)} green blocks weigh the same as {m(4)} purple cones. How many **orange balls** weigh the same as {m(4)} purple cones?",
                q_ar=f"في الميزان الأيسر، توازن {m(3)} كرات برتقالية مكعباً أخضر واحداً. وفي الميزان الأيمن، يوازن مكعبان أخضران {m(4)} مخاريط بنفسجية. كم **كرة برتقالية** توازن {m(4)} مخاريط بنفسجية؟",
                correct_val=6,
                distractors=[3, 4, 5, 8],
                idea_en="Replace each of the \\( 2 \\) green blocks on the right scale with \\( 3 \\) orange balls!",
                steps_en=[
                    f"From the right scale, {m(4)} purple cones equal {m(2)} green blocks.",
                    f"From the left scale, each green block equals {m(3)} orange balls.",
                    f"Replacing both green blocks gives {m('3 + 3 = 6')} orange balls!",
                ],
                check_en=f"Notice {m(1)} green block = {m(2)} cones = {m(3)} balls, so {m(4)} cones = {m(6)} balls!",
                idea_ar="نستبدل كل مكعب من المكعبين الأخضرين في الميزان الأيمن بـ \\( 3 \\) كرات برتقالية!",
                steps_ar=[
                    f"من الميزان الأيمن نعلم أن {m(4)} مخاريط بنفسجية توازن مكعبين أخضرين.",
                    f"ومن الميزان الأيسر نعلم أن كل مكعب أخضر يوازن {m(3)} كرات برتقالية.",
                    f"باستبدال المكعبين معاً نحصل على {m('3 + 3 = 6')} كرات برتقالية!",
                ],
                check_ar=f"مكعب واحد يوازن مخروطين ويساوي {m(3)} كرات، إذن {m(4)} مخاريط تساوي {m(6)} كرات!",
                diagram_en=svg_balance_scales(3, 1, 2, 4),
            ),
            kang_worked_example(
                ex_id="KANG-L0-02-EX2",
                title_en="Gold Stars and Pink Hearts Picture Puzzle",
                title_ar="لغز النجوم الذهبية والقلوب الوردية",
                q_en=f"In Kangy's picture puzzle, two identical gold stars add up to {m(14)} in the top row. A pink heart is worth {m(4)} **more** than one gold star. What number belongs in the {m('?')} box in the bottom row?",
                q_ar=f"في لغز الكنغر المصوّر، مجموع نجمتين ذهبيتين متطابقتين في السطر العلوي يساوي {m(14)}. وقيمة القلب الوردي تزيد بمقدار {m(4)} على النجمة الذهبية الواحدة. ما العدد الذي يوضع في مربع {m('?')} في السطر السفلي؟",
                correct_val=18,
                distractors=[11, 14, 15, 22],
                idea_en="Split \\( 14 \\) into two equal halves to find one star, add \\( 4 \\) to find one heart, then add star + heart!",
                steps_en=[
                    f"Since {m('\\bigstar + \\bigstar = 14')}, one gold star equals {m('14 \\div 2 = 7')}.",
                    f"A pink heart is {m(4)} more than a star, so {m('\\heartsuit = 7 + 4 = 11')}.",
                    f"Bottom row total: {m('\\bigstar + \\heartsuit = 7 + 11 = 18')}.",
                ],
                check_en=f"Check both clues: {m('7 + 7 = 14')}, {m('11 - 7 = 4')}, and {m('7 + 11 = 18')}!",
                idea_ar="نقسم \\( 14 \\) بالتساوي لمعرفة قيمة النجمة الواحدة، ثم نضيف \\( 4 \\) لمعرفة القلب، ثم نجمعهما!",
                steps_ar=[
                    f"بما أن {m('\\bigstar + \\bigstar = 14')}، فإن النجمة الواحدة تساوي {m(7)}.",
                    f"القلب الوردي يزيد بـ {m(4)} على النجمة، إذن {m('\\heartsuit = 7 + 4 = 11')}.",
                    f"مجموع السطر السفلي: {m('\\bigstar + \\heartsuit = 7 + 11 = 18')}.",
                ],
                check_ar=f"نتحقق: {m('7 + 7 = 14')}، والفرق {m('11 - 7 = 4')}، والمجموع {m('7 + 11 = 18')}!",
                diagram_en=svg_pre_icon_addition(["star", "star"], "14", ["star", "heart"], "?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-02-EX3",
                title_en="Counting Blue Beads on a Repeating Train",
                title_ar="عدّ الخرزات الزرقاء في قطار النمط المتكرر",
                q_en=f"Maya threads {m(14)} beads in order by repeating the {m(3)}-bead pattern **Red, Blue, Blue** (`R, B, B, R, B, B, ...`), starting with Red. How many **Blue** beads are on her {m(14)}-bead string altogether?",
                q_ar=f"تنظُم مايا {m(14)} خرزة بالترتيب بتكرار النمط الثلاثي **أحمر، أزرق، أزرق** (`R, B, B, R, B, B, ...`) بدءاً باللون الأحمر. كم خرزة **زرقاء** توجد في خيطها المكوّن من {m(14)} خرزة؟",
                correct_val=9,
                distractors=[7, 8, 10, 11],
                idea_en="Group the \\( 14 \\) beads into full sets of \\( 3 \\) (`R, B, B`), then check the leftover beads at the end!",
                steps_en=[
                    f"Four full groups of {m(3)} use {m('4 \\times 3 = 12')} beads, and each group holds {m(2)} Blue beads: {m('4 \\times 2 = 8')} Blue beads.",
                    f"There are {m('14 - 12 = 2')} beads left at the end (the 13th and 14th beads), which start a new pattern: `R, B`.",
                    f"That adds {m(1)} more Blue bead, giving {m('8 + 1 = 9')} Blue beads in total!",
                ],
                check_en=f"Write all {m(14)}: `R B B | R B B | R B B | R B B | R B` — {m(5)} Red + {m(9)} Blue = {m(14)} beads!",
                idea_ar="نجمّع الـ \\( 14 \\) خرزة في مجموعات كاملة من \\( 3 \\) خرزات (`R, B, B`)، ثم نفحص الخرزات المتبقية في النهاية!",
                steps_ar=[
                    f"أربع مجموعات كاملة من {m(3)} خرزات تستهلك {m('4 \\times 3 = 12')} خرزة، وفيها {m('4 \\times 2 = 8')} خرزات زرقاء.",
                    f"يتبقى في النهاية {m('14 - 12 = 2')} خرزتان (الثالثة عشرة والرابعة عشرة) وهما بداية نمط جديد: `R, B`.",
                    f"نحصل منهما على خرزة زرقاء إضافية، فيكون المجموع {m('8 + 1 = 9')} خرزات زرقاء!",
                ],
                check_ar=f"بكتابة الخرزات الأربع عشرة: {m(5)} حمراء + {m(9)} زرقاء = {m(14)} خرزة بالضبط!",
                diagram_en=svg_kang_necklace_beads(["R", "B", "B", "R", "B", "B", "?"]),
            ),
            kang_worked_example(
                ex_id="KANG-L0-02-EX4",
                title_en="Uncovering Rami's Secret Starting Number",
                title_ar="اكتشاف عدد البداية السري في صندوق رامي",
                q_en=f"Rami drops a secret number {m('?')} into the machine. The first box **adds {m(6)}**, the second box **subtracts {m(2)}**, and the number {m(19)} comes out at the end. What secret number {m('?')} did Rami put in?",
                q_ar=f"أدخل رامي عدداً سرياً {m('?')} في الآلة. الصندوق الأول **يجمع {m(6)}**، والصندوق الثاني **يطرح {m(2)}**، فخرج العدد {m(19)} في النهاية. ما العدد السري {m('?')} الذي أدخله رامي في البداية؟",
                correct_val=15,
                distractors=[11, 13, 17, 23],
                idea_en="Start from \\( 19 \\) at the exit and walk **backward**, reversing `- 2` to `+ 2` and `+ 6` to `- 6`!",
                steps_en=[
                    f"Undo the second box (`- 2`) by adding {m(2)}: {m('19 + 2 = 21')}.",
                    f"Undo the first box (`+ 6`) by subtracting {m(6)}: {m('21 - 6 = 15')}.",
                ],
                check_en=f"Test {m(15)} going forward: {m('15 + 6 = 21')}, then {m('21 - 2 = 19')}. Spot on!",
                idea_ar="نبدأ من العدد \\( 19 \\) عند المخرج ونرجع **عكسياً**، فنحوّل `- 2` إلى `+ 2` ونحوّل `+ 6` إلى `- 6`!",
                steps_ar=[
                    f"نعكس الصندوق الثاني (`- 2`) بجمع {m(2)}: {m('19 + 2 = 21')}.",
                    f"نعكس الصندوق الأول (`+ 6`) بطرح {m(6)}: {m('21 - 6 = 15')}.",
                ],
                check_ar=f"نجرّب {m(15)} للأمام: {m('15 + 6 = 21')} ثم {m('21 - 2 = 19')}. إجابة صحيحة!",
                diagram_en=svg_function_machine("?", "+ 6", "- 2", "19"),
            ),
        ],
        blueprints=[
            "kang_pre_toy_pan_balance",
            "kang_pre_fruit_icon_sums",
            "kang_pre_repeating_bead_train",
            "kang_pre_in_out_number_box",
        ],
    )


def _lesson_p_3() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-03",
        level=LEVEL,
        unit_num="P.3",
        topic="Geometry",
        title_en="Counting Shapes & Corners, Missing Wall Tiles, Stamp Turns & Toy Cube Stacks",
        title_ar="عدّ الأشكال والرؤوس، وإكمال البلاط المفقود، وتدوير الأختام، وأبراج المكعبات",
        summary_en=(
            "Sharpen your Kangaroo geometry eyes! Sort triangles, squares, and circles to count sides and corners, "
            "patch missing holes in tiled walls, spin transparent stamp cards by a quarter-turn, "
            "and use X-ray vision to count hidden blocks inside 3D toy towers."
        ),
        summary_ar=(
            "درّب عينيْ بطل الكنغر على الهندسة البصرية! صنّف المثلثات والمربعات والدوائر لعدّ الأضلاع والرؤوس، "
            "واحسب البلاطات المفقودة في الجدار، وأدِر البطاقات الشفافة ربع دورة، "
            "واستعمل خيالك ثلاثي الأبعاد لعدّ المكعبات المخفية تحت الأبراج."
        ),
        goals_en=[
            "Count **triangles, squares, and circles** systematically and total their straight sides or corners.",
            "Find **missing square tiles** in a rectangular grid by multiplying rows by columns or counting hole cells.",
            "Track one special corner or dot when a **transparent card turns** a quarter-turn or flips in a mirror.",
            "Count **all unit cubes** in a 3D toy block stack—including hidden cubes supporting taller columns.",
        ],
        goals_ar=[
            "عدّ **المثلثات والمربعات والدوائر** بانتظام وحساب مجموع أضلاعها المستقيمة أو رؤوسها.",
            "إيجاد **البلاطات المربعة المفقودة** في شبكة مستطيلة بضرب الصفوف في الأعمدة أو عدّ الفراغات.",
            "تتبّع ركن مميز أو نقطة عند **دوران بطاقة شفافة** ربع دورة أو انعكاسها في المرآة.",
            "عدّ **جميع المكعبات الصغيرة** في الأبراج ثلاثية الأبعاد بما فيها المكعبات المخفية الداعمة بالأسفل.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Shapes, Straight Sides & Corners Safari",
                title_ar="١. رحلة الأشكال الهندسية وعدّ الأضلاع والرؤوس",
                body_en=(
                    f"Every polygon has the **same number of corners as straight sides**: "
                    f"a **triangle** has {m(3)} sides and {m(3)} corners, a **square** or **rectangle** has {m(4)} sides and {m(4)} corners, "
                    f"and a smooth round **circle** has **{m(0)} straight sides and {m(0)} corners**! "
                    f"On the card below with {m(3)} triangles, {m(2)} squares, and {m(2)} circles, group by shape first: {m('3 \\times 3 + 2 \\times 4 + 0 = 17')} corners!"
                ),
                body_ar=(
                    f"في كل مضلع يتساوى **عدد الرؤوس وعدد الأضلاع المستقيمة**: "
                    f"فالمثلث له {m(3)} أضلاع و{m(3)} رؤوس، والمربع أو المستطيل له {m(4)} أضلاع و{m(4)} رؤوس، "
                    f"أما **الدائرة** المنحنية فليس لها أي ضلع مستقيم ولها **{m(0)} من الرؤوس**! "
                    f"في البطاقة أدناه ({m(3)} مثلثات ومربعان ودائرتان) نصنّف أولاً ثم نجمع: {m('3 \\times 3 + 2 \\times 4 + 0 = 17')} رأساً!"
                ),
                formula_en=dm("3 \\times 3 + 2 \\times 4 + 2 \\times 0 = 9 + 8 + 0 = 17 \\;\\text{corners}"),
                caption_ar="مجموع الرؤوس بتصنيف الأشكال أولاً:",
                formula_math_ar=dm("3 \\times 3 + 2 \\times 4 + 0 = 17"),
                diagram_en=svg_pre_shape_collage(3, 2, 2),
            ),
            kang_concept(
                title_en="2. Tiled Grids, Missing Holes & Quarter-Turns",
                title_ar="٢. شبكات البلاط، والفراغات المفقودة، والدوران ربع دورة",
                body_en=(
                    f"A full rectangular grid with {m(4)} rows and {m(5)} columns holds {m('4 \\times 5 = 20')} square tiles. "
                    f"To find how many tiles are missing in a dark hole, either count the dark grid squares row-by-row or subtract the light tiles from {m(20)}! "
                    f"When turning a **transparent stamp card** a **quarter-turn clockwise** (`↻`), follow **one landmark**: "
                    f"**Top** moves to **Right**, **Right** moves to **Bottom**, **Bottom** moves to **Left**, and **Left** moves to **Top**!"
                ),
                body_ar=(
                    f"الشبكة المستطيلة الكاملة المكوّنة من {m(4)} صفوف و{m(5)} أعمدة تتسع لـ {m('4 \\times 5 = 20')} بلاطة مربعة. "
                    f"لمعرفة عدد البلاطات المفقودة في الفجوة الداكنة، عُدّ المربعات الداكنة صفاً بصف أو اطرح البلاطات الفاتحة من {m(20)}! "
                    f"وعند تدوير **بطاقة شفافة ربع دورة مع عقارب الساعة** (`↻`)، راقب علامة مميزة واحدة فقط: "
                    f"**الأعلى** ينتقل إلى **اليمين**، و**اليمين** إلى **الأسفل**، و**الأسفل** إلى **اليسار**، و**اليسار** إلى **الأعلى**!"
                ),
                formula_en=dm("4 \\times 5 = 20 \\;\\text{total tiles}, \\qquad 20 - 16 = 4 \\;\\text{missing tiles}"),
                caption_ar="حساب البلاطات المفقودة في جدار 4 في 5:",
                formula_math_ar=dm("4 \\times 5 - 16 = 4"),
                diagram_en=svg_kang_polyomino_board([[1, 1, 1, 1, 1], [1, -1, -1, 1, 1], [1, 1, -1, -1, 1], [1, 1, 1, 1, 1]]),
            ),
            kang_concept(
                title_en="3. Counting 3D Toy Cube Stacks Column-by-Column",
                title_ar="٣. عدّ أبراج المكعبات عموداً بعمود",
                body_en=(
                    f"Wooden blocks never float in mid-air! If the tallest column rises {m(3)} blocks high, there are **{m(2)} blocks underneath** holding up the top block—even if front blocks hide part of them. "
                    f"Count **column-by-column** from tallest to shortest: here the three columns have heights {m(3)}, {m(2)}, and {m(1)}, giving {m('3 + 2 + 1 = 6')} blocks altogether!"
                ),
                body_ar=(
                    f"مكعبات الخشب لا تطير في الهواء! إذا ارتفع العمود الأعلى {m(3)} طوابق، فلا بد من وجود **مكعبين تحته** يحملان المكعب العلوي حتى لو حجبت الرؤية بعض أجزائهما. "
                    f"عُدّ **عموداً بعمود** من الأطول إلى الأقصر: ارتفاعات الأعمدة الثلاثة هنا هي {m(3)} و{m(2)} و{m(1)}، فيكون المجموع {m('3 + 2 + 1 = 6')} مكعبات!"
                ),
                formula_en=dm("\\text{Total Cubes} = 3 + 2 + 1 = 6"),
                caption_ar="جمع ارتفاعات الأعمدة شاملاً المكعبات الداعمة بالأسفل:",
                formula_math_ar=dm("3 + 2 + 1 = 6"),
                diagram_en=svg_cube_stack_3d((3, 2, 1)),
            ),
        ],
        traps_en=[
            "Trap: Giving a circle 1 corner! A circle is smooth all the way around, so it has 0 corners and 0 straight sides.",
            "Trap: Confusing a quarter-turn clockwise with a mirror flip! In a mirror across a vertical line, Top stays on Top while Left and Right swap.",
            "Trap: Counting visible square faces instead of whole 3D cubes, or forgetting hidden bottom cubes under a tall column!",
        ],
        traps_ar=[
            "فخ شائع: احتساب رأس واحد للدائرة! الدائرة منحنية بالكامل، لذا عدد رؤوسها 0 وعدد أضلاعها المستقيمة 0.",
            "فخ شائع: الخلط بين الدوران ربع دورة والانعكاس في المرآة! في المرآة الرأسية يبقى الأعلى في الأعلى ويتبادل اليمين واليسار فقط.",
            "فخ شائع: عدّ الأوجه المربعة الظاهرة بدلاً من المكعبات الكاملة، أو نسيان المكعبات السفلية المخفية تحت العمود الطويل!",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-03-EX1",
                title_en="Counting All Corners on Noor's Shape Card",
                title_ar="عدّ جميع الرؤوس في بطاقة أشكال نور",
                q_en=f"Noor glues {m(4)} triangles, {m(3)} squares, and {m(2)} circles onto her poster without any shapes touching or overlapping. How many **corners** do all the shapes on her poster have altogether?",
                q_ar=f"ألصقت نور {m(4)} مثلثات و{m(3)} مربعات ودائرتين على لوحتها دون تلامس أو تداخل بين الأشكال. كم **رأساً (زاوية)** لجميع الأشكال على لوحتها إجمالاً؟",
                correct_val=24,
                distractors=[20, 22, 26, 28],
                idea_en="Count \\( 3 \\) corners for each triangle, \\( 4 \\) corners for each square, and \\( 0 \\) corners for each circle!",
                steps_en=[
                    f"Corners on {m(4)} triangles = {m('4 \\times 3 = 12')}.",
                    f"Corners on {m(3)} squares = {m('3 \\times 4 = 12')}.",
                    f"Corners on {m(2)} circles = {m(0)}, so total corners = {m('12 + 12 + 0 = 24')}.",
                ],
                check_en=f"Add step-by-step: {m('3+3+3+3 = 12')} and {m('4+4+4 = 12')}, giving {m('12 + 12 = 24')}!",
                idea_ar="نحسب \\( 3 \\) رؤوس لكل مثلث، و\\( 4 \\) رؤوس لكل مربع، و\\( 0 \\) من الرؤوس لكل دائرة!",
                steps_ar=[
                    f"رؤوس المثلثات الأربعة = {m('4 \\times 3 = 12')} رأساً.",
                    f"رؤوس المربعات الثلاثة = {m('3 \\times 4 = 12')} رأساً.",
                    f"رؤوس الدائرتين = {m(0)}، فيكون المجموع الكلي = {m('12 + 12 + 0 = 24')} رأساً.",
                ],
                check_ar=f"بالجمع المباشر: {m('12 + 12 = 24')} رأساً!",
                diagram_en=svg_pre_shape_collage(4, 3, 2),
            ),
            kang_worked_example(
                ex_id="KANG-L0-03-EX2",
                title_en="Missing Square Tiles in the Kitchen Wall",
                title_ar="البلاطات المربعة المفقودة في جدار المطبخ",
                q_en=f"A rectangular kitchen wall grid has {m(4)} rows and {m(6)} columns of square tiles. Several tiles fell out of the dark middle hole, leaving {m(18)} light tiles on the wall. How many square tiles are **missing**?",
                q_ar=f"شبكة جدار مطبخ مستطيلة تتكوّن من {m(4)} صفوف و{m(6)} أعمدة من البلاطات المربعة. سقطت عدة بلاطات من الفجوة الداكنة في الوسط فبقيت {m(18)} بلاطة فاتحة. كم بلاطة مربعة **مفقودة**؟",
                correct_val=6,
                distractors=[4, 5, 7, 8],
                idea_en="Multiply rows by columns to get the full wall count, then subtract the \\( 18 \\) remaining tiles (or count the dark squares directly)!",
                steps_en=[
                    f"Full {m(4)}-by-{m(6)} grid holds {m('4 \\times 6 = 24')} square tiles.",
                    f"Subtract the {m(18)} remaining light tiles: {m('24 - 18 = 6')} missing tiles.",
                ],
                check_en=f"Count the dark hole squares directly in the drawing: {m(3)} in row 2 + {m(3)} in row 3 = {m(6)} tiles!",
                idea_ar="نضرب عدد الصفوف في عدد الأعمدة لإيجاد سعة الجدار الكامل، ثم نطرح \\( 18 \\) بلاطة متبقية!",
                steps_ar=[
                    f"الجدار الكامل ({m(4)} صفوف في {m(6)} أعمدة) يتسع لـ {m('4 \\times 6 = 24')} بلاطة.",
                    f"نطرح البلاطات الفاتحة المتبقية: {m('24 - 18 = 6')} بلاطات مفقودة.",
                ],
                check_ar=f"بعدّ المربعات الداكنة مباشرة في الشكل: {m(3)} في الصف الثاني + {m(3)} في الصف الثالث = {m(6)} بلاطات!",
                diagram_en=svg_kang_polyomino_board([
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, -1, -1, -1, 1],
                    [1, -1, -1, -1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                ]),
            ),
            kang_worked_example(
                ex_id="KANG-L0-03-EX3",
                title_en="Quarter-Turn of a Transparent Stamp Card",
                title_ar="تدوير بطاقة شفافة ربع دورة",
                q_en=f"A {m('3 \\times 3')} transparent card has its {m(9)} squares numbered row-by-row: `1, 2, 3` across the top, `4, 5, 6` across the middle, and `7, 8, 9` across the bottom. Right now the special dot sits in the **top-middle** square (position {m(2)}). After **one quarter-turn clockwise** (`↻`), which position number (`1` to `9`) will the special dot sit in?",
                q_ar=f"بطاقة شفافة أبعادها {m('3 \\times 3')} مُرقّمة مربعاتها التسعة صفاً بصف: `1, 2, 3` في الصف العلوي، و`4, 5, 6` في الأوسط، و`7, 8, 9` في السفلي. تقع النقطة المميزة الآن في مربع **منتصف الأعلى** (الموقع {m(2)}). بعد **دورانها ربع دورة مع عقارب الساعة** (`↻`)، في أي موقع (`1` إلى `9`) ستصبح النقطة المميزة؟",
                correct_val=6,
                distractors=[3, 4, 8, 9],
                idea_en="A quarter-turn clockwise (`↻`) moves the **top edge** onto the **right edge**, so **top-middle** lands on **middle-right**!",
                steps_en=[
                    f"Before turning, the special dot sits in the middle of the **top** row (position {m(2)}).",
                    f"Turning one quarter-turn clockwise (`↻`) rotates the top row onto the **right** column.",
                    f"The middle square of the right column (`3, 6, 9`) is position {m(6)}!",
                ],
                check_en=f"Trace all four quarter-turns of {m(2)}: {m('2 \\to 6 \\to 8 \\to 4 \\to 2')}!",
                idea_ar="الدوران ربع دورة مع عقارب الساعة (`↻`) ينقل **الحافة العلوية** إلى **الحافة اليمنى**، فينتقل منتصف الأعلى إلى **منتصف اليمين**!",
                steps_ar=[
                    f"قبل الدوران تقع النقطة المميزة في منتصف الصف **العلوي** (الموقع {m(2)}).",
                    f"عند الدوران ربع دورة مع عقارب الساعة (`↻`) يصبح الصف العلوي هو العمود **الأيمن**.",
                    f"مربع المنتصف في العمود الأيمن (`3, 6, 9`) هو الموقع رقم {m(6)}!",
                ],
                check_ar=f"بتتبع الأرباع الأربعة للدورة: {m('2 \\to 6 \\to 8 \\to 4 \\to 2')}!",
                diagram_en=svg_kang_stamp_grid([[0, 2, 0], [0, 1, 0], [1, 1, 0]], "Turn ↻ ?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-03-EX4",
                title_en="Wooden Cubes Left Inside Jad's Toy Bucket",
                title_ar="المكعبات المتبقية في سلة ألعاب جاد",
                q_en=f"Jad starts with {m(19)} wooden unit cubes in his bucket. He glues three columns of heights {m(3)}, {m(3)}, and {m(2)} side by side as shown. How many unit cubes are **still left** in his bucket?",
                q_ar=f"بدأ جاد وبحوزته {m(19)} مكعباً خشبياً صغيراً في سلته، ثم ألصق ثلاثة أعمدة متجاورة ارتفاعاتها {m(3)} و{m(3)} و{m(2)} كما في الشكل. كم مكعباً صغيراً **بقي** في سلته؟",
                correct_val=11,
                distractors=[8, 10, 12, 13],
                idea_en="Add the heights of all three columns to count the cubes in Jad's tower, then subtract from \\( 19 \\)!",
                steps_en=[
                    f"Cubes used in the three columns = {m('3 + 3 + 2 = 8')} unit cubes.",
                    f"Subtract from the {m(19)} cubes in his bucket: {m('19 - 8 = 11')} cubes left.",
                ],
                check_en=f"Used ({m(8)}) + left in bucket ({m(11)}) = {m('8 + 11 = 19')} total cubes!",
                idea_ar="نجمع ارتفاعات الأعمدة الثلاثة لمعرفة عدد المكعبات المستعملة، ثم نطرحه من \\( 19 \\)!",
                steps_ar=[
                    f"عدد المكعبات المستعملة في الأعمدة الثلاثة = {m('3 + 3 + 2 = 8')} مكعبات.",
                    f"نطرحها من {m(19)} مكعباً في السلة: {m('19 - 8 = 11')} مكعباً متبقياً.",
                ],
                check_ar=f"المستعمل ({m(8)}) + المتبقي ({m(11)}) = {m('8 + 11 = 19')} مكعباً!",
                diagram_en=svg_cube_stack_3d((3, 3, 2)),
            ),
        ],
        blueprints=[
            "kang_pre_shape_polygon_counting",
            "kang_pre_grid_tile_completion",
            "kang_pre_stamp_mirror_turns",
            "kang_pre_toy_cube_stacks",
        ],
    )


def _lesson_p_4() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-04",
        level=LEVEL,
        unit_num="P.4",
        topic="Geometry",
        title_en="Grid Step Paths, Tree & Lamp Gaps, Folded Ribbon Cuts & Opposite Die Dots",
        title_ar="مسارات خطوات الشبكة، والمسافات بين الأشجار، وقصّ الأشرطة المطوية، ونقاط النرد المتقابلة",
        summary_en=(
            "Explore four classic Kangaroo spatial puzzles! Walk step-by-step from Start to Star on park grids, "
            "count gaps between rows of trees and lamps, snip folded ribbons with scissors, "
            "and use the magic 'sum to 7' rule to see hidden dots on the back and bottom of a die."
        ),
        summary_ar=(
            "استكشف أربعة من أشهر ألغاز الكنغر المكانية! امشِ خطوة بخطوة من البداية إلى النجمة على الشبكة، "
            "واحسب المسافات بين الأشجار وأعمدة الإنارة، وقصّ الأشرطة المطوية بالمقص، "
            "واستعمل قاعدة (المجموع = 7) لمعرفة النقاط المخفية خلف وأسفل حجر النرد."
        ),
        goals_en=[
            "Count **steps along a grid path** from `S` to `★`, remembering to count **moves** rather than squares.",
            "Apply the **Finger-and-Gap Secret** (`Gaps = Trees − 1`) along straight rows of trees, flags, or lamps.",
            "Predict how many **ribbon pieces** appear when scissors cut across a **folded strip** (`1 + Strands Cut`).",
            "Find **hidden dots on a standard die** using the rule that opposite faces always add up to **7**.",
        ],
        goals_ar=[
            "عدّ **الخطوات على مسار الشبكة** من `S` إلى `★` مع تذكّر عدّ **الانتقالات** لا عدد المربعات.",
            "تطبيق **سرّ الأصابع والمسافات** (`عدد المسافات = عدد الأشجار − 1`) في الصفوف المستقيمة.",
            "معرفة **عدد قطع الشريط** الناتجة عند قص شريط مطوي بالمقص (`1 + عدد الطبقات المقصوصة`).",
            "إيجاد **النقاط المخفية في حجر النرد القياسي** بقاعدة مجموع كل وجهين متقابلين يساوي **7** دائماً.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Grid Step Paths & the Tree-Lamp Gap Secret",
                title_ar="١. مسارات الشبكة وسرّ المسافات بين الأشجار والأعمدة",
                body_en=(
                    f"Hold up {m(5)} fingers on one hand and count the spaces between them—there are {m(4)} spaces, **1 less** than {m(5)}! "
                    f"In a straight row of trees or lamps, **Gaps = Items − 1**. "
                    f"The exact same idea works on a **grid path**: on the {m('5 \\times 4')} grid below, Kangy's red trail touches {m(6)} squares from `S` to `★`, "
                    f"which means he makes {m('6 - 1 = 5')} steps (`3` steps right + `2` steps up = {m(5)} steps)!"
                ),
                body_ar=(
                    f"ارفع {m(5)} أصابع في يدك وعدّ الفراغات بينها: ستجد {m(4)} فراغات فقط، أي **أقل بواحد** من {m(5)}! "
                    f"في أي صف مستقيم من الأشجار أو الأعمدة يكون **عدد المسافات = عدد الأشجار − 1**. "
                    f"والفكرة نفسها تنطبق على **مسار الشبكة**: في الشبكة أدناه يمر المسار الأحمر بـ {m(6)} مربعات من `S` إلى `★`، "
                    f"أي أن الكنغر يخطو {m('6 - 1 = 5')} خطوات فقط ({m(3)} خطوات لليمين + خطوتان للأعلى = {m(5)} خطوات)!"
                ),
                formula_en=dm("\\text{Gaps} = \\text{Trees} - 1, \\qquad \\text{Steps} = \\text{Visited Squares} - 1"),
                caption_ar="قاعدة المسافات على الممر والخطوات على الشبكة:",
                formula_math_ar=dm("6 - 1 = 5 \\;\\text{steps}"),
                diagram_en=svg_kang_grid_walk(5, 4, [(0, 3), (1, 3), (1, 2), (2, 2), (2, 1), (3, 1)]),
            ),
            kang_concept(
                title_en="2. Cutting Folded Paper Strips & Ribbons",
                title_ar="٢. قصّ الأشرطة الورقية والحبال المطوية بالمقص",
                body_en=(
                    f"Start with **1 whole ribbon**. Every time scissors snip cleanly through **one layer**, the number of pieces goes up by **{m(1)}**! "
                    f"In the diagram below, the blue ribbon is folded into **{m(3)} horizontal layers** and cut once down the middle (`✂`). "
                    f"The scissors slice through {m(3)} layers, so you get {m('1 + 3 = 4')} pieces—because the two curved fold loops keep pairs of cut strands joined together!"
                ),
                body_ar=(
                    f"نبدأ بـ **شريط واحد متصل**. في كل مرة يقصّ المقص **طبقة واحدة** يزيد عدد القطع بمقدار **{m(1)}**! "
                    f"في الشكل أدناه طُوي الشريط الأزرق إلى **{m(3)} طبقات أفقية** وقُصّ مرة واحدة في المنتصف (`✂`). "
                    f"يمر المقص عبر {m(3)} طبقات، فينتج {m('1 + 3 = 4')} قطع لأن الثنيتين الجانبيتين تُبقيان الأطراف المطوية متصلة!"
                ),
                formula_en=dm("\\text{Pieces} = 1 + (\\text{Layers Cut}) = 1 + 3 = 4"),
                caption_ar="عدد القطع يساوي 1 زائد عدد الطبقات التي قطعها المقص:",
                formula_math_ar=dm("1 + 3 = 4 \\;\\text{pieces}"),
                diagram_en=svg_kang_folded_ribbon(3, 1),
            ),
            kang_concept(
                title_en="3. Opposite Die Dots Always Add Up to 7",
                title_ar="٣. النقاط المتقابلة على حجر النرد مجموعها 7 دائماً",
                body_en=(
                    f"On every standard Kangaroo die, the dots on **opposite faces always add up to {m(7)}**: "
                    f"{m(1)} dot is opposite {m(6)} dots, {m(2)} dots are opposite {m(5)} dots, and {m(3)} dots are opposite {m(4)} dots! "
                    f"In the die below, **Top = {m(1)}** (so **Bottom = {m('7 - 1 = 6')}**), **Front-Left = {m(2)}** (so **Back-Right = {m(5)}**), "
                    f"and **Front-Right = {m(3)}** (so **Back-Left = {m(4)}**). All {m(6)} faces together always hold {m('7 + 7 + 7 = 21')} dots!"
                ),
                body_ar=(
                    f"في كل حجر نرد قياسي في مسابقات الكنغر، **مجموع النقاط على أي وجهين متقابلين يساوي {m(7)} دائماً**: "
                    f"نقطة {m(1)} تقابل {m(6)} نقاط، ونقطتان {m(2)} تقابلان {m(5)} نقاط، و{m(3)} نقاط تقابل {m(4)} نقاط! "
                    f"في النرد أدناه: **الأعلى = {m(1)}** (إذن **الأسفل = {m(6)}**)، والأمامي الأيسر = {m(2)} (يقابله {m(5)})، "
                    f"والأمامي الأيمن = {m(3)} (يقابله {m(4)}). ومجموع نقاط الأوجه الستة معاً يساوي دائماً {m('7 + 7 + 7 = 21')} نقطة!"
                ),
                formula_en=dm("\\text{Opposite Dots} = 7 - \\text{Visible Dots}, \\qquad \\text{All 6 Faces} = 21 \\;\\text{dots}"),
                caption_ar="أزواج النقاط المتقابلة على حجر النرد القياسي:",
                formula_math_ar=dm("1 + 6 = 7, \\qquad 2 + 5 = 7, \\qquad 3 + 4 = 7"),
                diagram_en=svg_pre_die_dots(1, 2, 3),
            ),
        ],
        traps_en=[
            "Trap: Counting the green start square S as Step 1! Standing at S is 0 steps; count the red line segments between squares.",
            "Trap: Multiplying all 8 lamps by 4 m to get 32 m! Between 8 lamps there are only 8 − 1 = 7 spaces (28 m).",
            "Trap: Doubling the 4 folded ribbon layers to get 8 pieces! Folded loops hold pieces together, so 1 cut across 4 layers makes 1 + 4 = 5 pieces.",
        ],
        traps_ar=[
            "فخ شائع: عدّ مربع البداية الأخضر S كأنه الخطوة الأولى! الوقوف عند S هو 0 خطوة؛ عُدّ القطع الحمراء الواصلة بين المربعات.",
            "فخ شائع: ضرب 8 أعمدة في 4 أمتار للحصول على 32 متراً! بين 8 أعمدة توجد 7 مسافات فقط (7 × 4 = 28 متراً).",
            "فخ شائع: مضاعفة 4 طبقات مطوية للحصول على 8 قطع! الثنيات تُبقي الأطراف متصلة، لذا قص 4 طبقات مرة واحدة يعطي 1 + 4 = 5 قطع.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-04-EX1",
                title_en="Kangy's Walk From Start to Star on the Grid",
                title_ar="رحلة الكنغر من البداية إلى النجمة على الشبكة",
                q_en=f"Little Kangy follows the red path on the {m('5 \\times 4')} grid from the green start square `S` to the yellow star square `★`. Each single step from one square's center to the next square's center is {m(2)} meters long. How many **meters** does Kangy walk in total?",
                q_ar=f"يتبع الكنغر الصغير المسار الأحمر على الشبكة {m('5 \\times 4')} من مربع البداية الأخضر `S` إلى مربع النجمة الأصفر `★`. طول كل خطوة واحدة من مركز مربع إلى مركز المربع المجاور هو {m(2)} متران. كم **متراً** يمشي الكنغر إجمالاً؟",
                correct_val=14,
                distractors=[7, 12, 16, 18],
                idea_en="Count the **steps** (red segments) from `S` to `★`, then multiply the number of steps by \\( 2 \\) meters!",
                steps_en=[
                    f"Follow the red path: {m(2)} steps right, {m(2)} steps up, {m(2)} steps right, and {m(1)} step up = {m('2 + 2 + 2 + 1 = 7')} steps.",
                    f"Each step is {m(2)} meters long, so total distance = {m('7 \\times 2 = 14')} meters.",
                ],
                check_en=f"The path visits {m(8)} colored squares, so there are {m('8 - 1 = 7')} steps and {m('7 \\times 2 = 14')} m (not {m(16)})!",
                idea_ar="نعدّ **الخطوات** (القطع الحمراء) من `S` إلى `★`، ثم نضرب عدد الخطوات في \\( 2 \\) متر!",
                steps_ar=[
                    f"نتتبع المسار الأحمر: خطوتان لليمين + خطوتان للأعلى + خطوتان لليمين + خطوة للأعلى = {m('2 + 2 + 2 + 1 = 7')} خطوات.",
                    f"طول كل خطوة {m(2)} متران، إذن المسافة الكلية = {m('7 \\times 2 = 14')} متراً.",
                ],
                check_ar=f"يمر المسار بـ {m(8)} مربعات ملوّنة، أي {m('8 - 1 = 7')} خطوات، والمسافة {m('7 \\times 2 = 14')} متراً!",
                diagram_en=svg_kang_grid_walk(5, 4, [(0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 0)]),
            ),
            kang_worked_example(
                ex_id="KANG-L0-04-EX2",
                title_en="Garden Lamps Along a Straight Walkway",
                title_ar="أعمدة الإنارة على ممر الحديقة المستقيم",
                q_en=f"There are {m(8)} garden lamps standing in a straight row with equal spaces between neighbors. The distance between the **1st** lamp and the **2nd** lamp is {m(4)} meters. How many meters is it from the **1st** lamp to the **8th** lamp?",
                q_ar=f"تقف {m(8)} أعمدة إنارة في صف مستقيم بمسافات متساوية بين كل عمودين متجاورين. إذا كانت المسافة بين العمود **الأول** والعمود **الثاني** {m(4)} أمتار، فكم متراً تبلغ المسافة من العمود **الأول** إلى العمود **الثامن**؟",
                correct_val=28,
                distractors=[24, 30, 32, 36],
                idea_en="Between \\( 8 \\) lamps in a straight row, there are \\( 8 - 1 = 7 \\) equal gaps!",
                steps_en=[
                    f"Number of gaps = {m('8 - 1 = 7')} gaps.",
                    f"Each gap is {m(4)} meters long, so total distance = {m('7 \\times 4 = 28')} meters.",
                ],
                check_en=f"Count by {m(4)}s from Lamp 1 (`0 m`): `4, 8, 12, 16, 20, 24, 28` at Lamp 8!",
                idea_ar="بين \\( 8 \\) أعمدة في صف مستقيم توجد \\( 8 - 1 = 7 \\) مسافات متساوية!",
                steps_ar=[
                    f"عدد المسافات = {m('8 - 1 = 7')} مسافات.",
                    f"طول كل مسافة {m(4)} أمتار، فتكون المسافة الكلية = {m('7 \\times 4 = 28')} متراً.",
                ],
                check_ar=f"بالعدّ النمطي أربعات من العمود الأول (`0 م`): نصل عند العمود الثامن إلى {m(28)} متراً!",
                diagram_en=svg_fenceposts("4 m", "? m"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-04-EX3",
                title_en="Snipping a Four-Layer Folded Ribbon",
                title_ar="قصّ شريط مطوي من أربع طبقات",
                q_en=f"Salma folds a long blue ribbon back and forth into {m(4)} horizontal layers as shown, then makes {m(1)} straight vertical scissor cut (`✂`) all the way through all {m(4)} layers. How many separate pieces of ribbon does she get?",
                q_ar=f"طوت سلمى شريطاً أزرق طويلاً ذهاباً وإياباً في {m(4)} طبقات أفقية كما في الشكل، ثم قصّته بالمقص (`✂`) قصّة رأسية واحدة تمر عبر الطبقات الـ {m(4)} كلها. كم قطعة منفصلة من الشريط تحصل عليها؟",
                correct_val=5,
                distractors=[4, 6, 7, 8],
                idea_en="Each strand sliced by the scissors adds \\( 1 \\) piece to the original \\( 1 \\) ribbon!",
                steps_en=[
                    f"The scissors cut cleanly across {m(4)} horizontal layers.",
                    f"Starting from {m(1)} whole ribbon, {m(4)} strand cuts make {m('1 + 4 = 5')} pieces.",
                ],
                check_en=f"Trace them directly: {m(2)} loose end pieces + {m(3)} U-shaped loop pieces = {m('2 + 3 = 5')} pieces!",
                idea_ar="كل طبقة يقطعها المقص تضيف قطعة واحدة إلى الشريط الأصلي الواحد!",
                steps_ar=[
                    f"يقطع المقص {m(4)} طبقات أفقية دفعة واحدة.",
                    f"ابتداءً من شريط واحد متصل نحصل على {m('1 + 4 = 5')} قطع منفصلة.",
                ],
                check_ar=f"بتتبع القطع مباشرة: طرفان حرّان ({m(2)}) + {m(3)} ثنيات على شكل حرف U = {m('2 + 3 = 5')} قطع!",
                diagram_en=svg_kang_folded_ribbon(4, 1),
            ),
            kang_worked_example(
                ex_id="KANG-L0-04-EX4",
                title_en="Total Hidden Dots on a Standard Die",
                title_ar="مجموع النقاط المخفية على حجر النرد",
                q_en=f"Amir places a standard die on the table. As shown, you can see {m(2)} dots on **top**, {m(4)} dots on the **front-left** face, and {m(1)} dot on the **front-right** face. What is the **total number of dots** hidden on the **other three** faces?",
                q_ar=f"وضع أمير حجر نرد قياسياً على الطاولة. كما في الشكل، تظهر نقطتان ({m(2)}) في **الأعلى**، و{m(4)} نقاط على الوجه **الأمامي الأيسر**، ونقطة واحدة ({m(1)}) على الوجه **الأمامي الأيمن**. ما **مجموع النقاط المخفية** على **الأوجه الثلاثة الأخرى**؟",
                correct_val=14,
                distractors=[7, 12, 13, 15],
                idea_en="Subtract each visible face from \\( 7 \\) to find its opposite hidden face, then add the three hidden faces!",
                steps_en=[
                    f"Opposite the top ({m(2)}) is the bottom with {m('7 - 2 = 5')} dots.",
                    f"Opposite front-left ({m(4)}) is {m('7 - 4 = 3')} dots, and opposite front-right ({m(1)}) is {m('7 - 1 = 6')} dots.",
                    f"Total hidden dots = {m('5 + 3 + 6 = 14')}.",
                ],
                check_en=f"Fast check: all {m(6)} faces hold {m(21)} dots, minus {m('2 + 4 + 1 = 7')} visible dots = {m('21 - 7 = 14')}!",
                idea_ar="نطرح كل وجه ظاهر من \\( 7 \\) لإيجاد الوجه الخفي المقابل له، ثم نجمع الأوجه الثلاثة المخفية!",
                steps_ar=[
                    f"مقابل الوجه العلوي ({m(2)}) يوجد في الأسفل {m('7 - 2 = 5')} نقاط.",
                    f"مقابل الأمامي الأيسر ({m(4)}) يوجد {m('7 - 4 = 3')} نقاط، ومقابل الأمامي الأيمن ({m(1)}) يوجد {m('7 - 1 = 6')} نقاط.",
                    f"مجموع النقاط المخفية = {m('5 + 3 + 6 = 14')} نقطة.",
                ],
                check_ar=f"طريقة سريعة: مجموع أوجه النرد الستة {m(21)} نقطة، نطرح منها الظاهر ({m('2 + 4 + 1 = 7')}) فنحصل على {m('21 - 7 = 14')}!",
                diagram_en=svg_pre_die_dots(2, 4, 1),
            ),
        ],
        blueprints=[
            "kang_pre_grid_step_paths",
            "kang_pre_tree_lamp_gaps",
            "kang_pre_folded_strip_cuts",
            "kang_pre_opposite_die_dots",
        ],
    )


def _lesson_p_5() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-05",
        level=LEVEL,
        unit_num="P.5",
        topic="Combinatorics & Logic",
        title_en="Queue Line Positions, Coin Totals, Ice-Cream Pairs & Magic Five-Cell Crosses",
        title_ar="الترتيب في الطابور، ومجموع النقود، وأزواج الآيس كريم، والصليب السحري الخماسي",
        summary_en=(
            "Think like a young Kangaroo logician! Count children standing in a queue without counting Kangy twice, "
            "add riyal coins and compute change at the toy shop, pair every ice-cream cone with every scoop flavour, "
            "and balance row and column sums inside a Magic 5-Cell Cross."
        ),
        summary_ar=(
            "فكّر بذكاء أبطال الكنغر في العدّ والمنطق! احسب عدد الأطفال في الطابور دون عدّ الكنغر مرتين، "
            "واجمع القطع النقدية واحسب الباقي في متجر الألعاب، وكوّن جميع أزواج بسكويت ونكهات الآيس كريم، "
            "ووازن مجموع الصف والعمود داخل الصليب السحري الخماسي."
        ),
        goals_en=[
            "Relate **position from the Front**, **position from the Back**, and **total queue length** (`Front + Back − 1`).",
            "Add **1, 2, 5, and 10-riyal coins**, calculate shopping change, or make a price with the fewest coins.",
            "Count **all outfit or ice-cream pairs** systematically by matching every item in Group 1 with every item in Group 2.",
            "Fill a **5-cell Magic Cross** by spotting that the center cell is shared by both row and column.",
        ],
        goals_ar=[
            "الربط بين **الترتيب من الأمام** و**الترتيب من الخلف** و**العدد الكلي في الطابور** (`الأمام + الخلف − 1`).",
            "جمع **القطع النقدية من فئات 1 و2 و5 و10 ريالات** وحساب الباقي أو تكوين مبلغ بأقل عدد من القطع.",
            "عدّ **جميع أزواج الملابس أو الآيس كريم** بانتظام عبر ربط كل خيار من المجموعة الأولى بكل خيار من الثانية.",
            "إكمال **الصليب السحري الخماسي** بملاحظة أن الخانة الوسطى مشتركة بين الصف الأفقي والعمود الرأسي.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Standing in a Queue Line (Don't Count ★ Twice!)",
                title_ar="١. الترتيب في الطابور (لا تعدّ النجمة ★ مرتين!)",
                body_en=(
                    f"Look at the starred child (`★`) in the line below: counting from the **Front**, she is **4th** ({m(3)} ahead + her), "
                    f"and counting from the **Back**, she is **3rd** ({m(2)} behind + her). "
                    f"If you add {m('4 + 3 = 7')}, you counted `★` **two times**! Subtract {m(1)} so she is counted once: {m('4 + 3 - 1 = 6')} children in line!"
                ),
                body_ar=(
                    f"انظر إلى الطفلة المميزة بنجمة (`★`) في الطابور أدناه: ترتيبها من **الأمام** هو **الرابع** ({m(3)} أمامها + هي)، "
                    f"وترتيبها من **الخلف** هو **الثالث** ({m(2)} خلفها + هي). "
                    f"إذا جمعت {m('4 + 3 = 7')} تكون قد عددت `★` **مرتين**! اطرح {m(1)} لتُحسب مرة واحدة فقط: {m('4 + 3 - 1 = 6')} أطفال في الطابور!"
                ),
                formula_en=dm("\\text{Total in Queue} = (\\text{From Front}) + (\\text{From Back}) - 1 = 4 + 3 - 1 = 6"),
                caption_ar="قانون الطابور الذهبي دون تكرار العدّ:",
                formula_math_ar=dm("4 + 3 - 1 = 6"),
                diagram_en=svg_pre_queue_line(6, 3, "Front", "Back"),
            ),
            kang_concept(
                title_en="2. Coin Purse Totals & Matching Choice Pairs",
                title_ar="٢. جمع القطع النقدية وتكوين أزواج الاختيارات",
                body_en=(
                    f"When counting coins, **start from the biggest value** so addition stays easy: {m('10 + 5 + 2 + 1 = 18')} riyals! "
                    f"To pay a price using the **fewest coins**, always grab the largest coin that fits first. "
                    f"And when choosing **1 item from Group A** (say {m(2)} shirts) **and 1 item from Group B** (say {m(3)} caps), "
                    f"each shirt pairs with all {m(3)} caps, making {m('3 + 3 = 2 \\times 3 = 6')} different outfits!"
                ),
                body_ar=(
                    f"عند عدّ النقود، **ابدأ بالقطعة الأكبر قيمة** ليكون الجمع سهلاً وسريعاً: {m('10 + 5 + 2 + 1 = 18')} ريالاً! "
                    f"ولدفع ثمن لعبة **بأقل عدد من القطع**، اختر دائماً أكبر فئة نقدية مناسبة أولاً. "
                    f"وعند اختيار **عنصر من المجموعة الأولى** (مثلاً قميصين {m(2)}) **وعنصر من المجموعة الثانية** (مثلاً {m(3)} قبعات)، "
                    f"يقترن كل قميص بالقبعات الثلاث جميعاً، فنحصل على {m('3 + 3 = 2 \\times 3 = 6')} إطلالات مختلفة!"
                ),
                formula_en=dm("10 + 5 + 2 + 1 = 18, \\qquad 2 \\text{ shirts} \\times 3 \\text{ caps} = 6 \\text{ outfits}"),
                caption_ar="جمع النقود من الأكبر للأصغر وحساب عدد الأزواج:",
                formula_math_ar=dm("10 + 5 + 2 + 1 = 18, \\qquad 2 \\times 3 = 6"),
                diagram_en=svg_pre_coin_purse(["10", "5", "2", "1"], "18 SAR"),
            ),
            kang_concept(
                title_en="3. The Magic 5-Cell Number Cross",
                title_ar="٣. الصليب السحري الخماسي للأعداد",
                body_en=(
                    f"In a Magic 5-Cell Cross, the **3 vertical cells** and the **3 horizontal cells** add up to the **exact same sum**. "
                    f"Because the yellow **center cell** sits in **both** lines, the two outer vertical cells (**Top + Bottom**) must have the **same sum** as the two outer horizontal cells (**Left + Right**)! "
                    f"Below, {m('1 + 5 = 6')} and {m('2 + 4 = 6')}, and with {m(3)} in the center both lines add up to {m('6 + 3 = 9')}!"
                ),
                body_ar=(
                    f"في الصليب السحري الخماسي، يتساوى مجموع **الخانات الثلاث الرأسية** ومجموع **الخانات الثلاث الأفقية**. "
                    f"ولأن **الخانة الوسطى الصفراء** مشتركة في الخطين معاً، فلا بد أن يتساوى مجموع الطرفين الرأسيين (**الأعلى + الأسفل**) مع مجموع الطرفين الأفقيين (**اليسار + اليمين**)! "
                    f"في الشكل أدناه: {m('1 + 5 = 6')} و{m('2 + 4 = 6')}، ومع وجود {m(3)} في الوسط يصبح مجموع كل خط {m('6 + 3 = 9')}!"
                ),
                formula_en=dm("\\text{Top} + \\text{Bottom} = \\text{Left} + \\text{Right} \\quad (1 + 5 = 2 + 4 = 6)"),
                caption_ar="تساوي مجموع الطرفين المتقابلين في الصليب السحري:",
                formula_math_ar=dm("1 + 3 + 5 = 2 + 3 + 4 = 9"),
                diagram_en=svg_kang_magic_cross("3", "1", "4", "5", "2", "Sum = 9"),
            ),
        ],
        traps_en=[
            "Trap: Adding Front position + Back position and forgetting to subtract 1! Without − 1, the starred child gets counted twice.",
            "Trap: Adding 3 cones + 4 flavours = 7 instead of pairing each cone with all 4 flavours (4 + 4 + 4 = 12)!",
            "Trap: Forgetting the shared center cell in a Magic Cross and adding all 5 numbers together instead of matching one line of 3!",
        ],
        traps_ar=[
            "فخ شائع: جمع الترتيب من الأمام + الترتيب من الخلف ونسيان طرح 1! بدون طرح 1 يُحسب الشخص المميز مرتين.",
            "فخ شائع: جمع 3 أنواع بسكويت + 4 نكهات = 7 بدلاً من ربط كل بسكويت بالنكهات الأربع جميعاً (4 + 4 + 4 = 12)!",
            "فخ شائع: نسيان اشتراك الخانة الوسطى في الصليب السحري وجمع الخانات الخمس معاً بدلاً من مساواة خط أفقي بخط رأسي!",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-05-EX1",
                title_en="Huda's New Place After Friends Join the Queue",
                title_ar="ترتيب هدى الجديد بعد انضمام أصدقائها للطابور",
                q_en=f"In the photo, Huda (`★`) stands **4th** from the **Front** and **4th** from the **Back** of the zoo line. Right after the photo, {m(5)} more children join at the very **Back** of the line. What is Huda's new position counting from the **Back**?",
                q_ar=f"في الصورة، تقف هدى (`★`) في الترتيب **الرابع** من **الأمام** و**الرابع** من **الخلف** في طابور حديقة الحيوان. وبعد التقاط الصورة مباشرة انضم {m(5)} أطفال جدد في **نهاية الطابور (الخلف)**. ما ترتيب هدى الجديد عند العدّ من **الخلف**؟",
                correct_val=9,
                distractors=[7, 8, 10, 12],
                idea_en="First see how many children stand behind Huda, add the \\( 5 \\) new children behind her, and include Huda herself!",
                steps_en=[
                    f"Being **4th** from the Back means {m('4 - 1 = 3')} children stood behind Huda.",
                    f"After {m(5)} new children join the Back, there are {m('3 + 5 = 8')} children behind Huda.",
                    f"Counting from the Back up to Huda herself gives {m('8 + 1 = 9')} (**9th** from the Back)!",
                ],
                check_en=f"Original queue had {m('4 + 4 - 1 = 7')} children; new queue has {m('7 + 5 = 12')}, and {m('4 + 9 - 1 = 12')}!",
                idea_ar="نحسب عدد الواقفين خلف هدى أولاً، ثم نضيف إليهم الـ \\( 5 \\) الجدد في الخلف، ثم نحسب هدى معهم!",
                steps_ar=[
                    f"بما أن ترتيب هدى كان **الرابع** من الخلف، فقد كان خلفها {m('4 - 1 = 3')} أطفال.",
                    f"بعد انضمام {m(5)} أطفال في الخلف أصبح خلف هدى {m('3 + 5 = 8')} أطفال.",
                    f"عند العدّ من الخلف شاملاً هدى نفسها يكون ترتيبها {m('8 + 1 = 9')} (**التاسعة** من الخلف)!",
                ],
                check_ar=f"كان في الطابور {m('4 + 4 - 1 = 7')} أطفال فأصبحوا {m('7 + 5 = 12')} طفلاً، وبالقانون {m('4 + 9 - 1 = 12')}!",
                diagram_en=svg_pre_queue_line(7, 3, "Front", "Back +5"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-05-EX2",
                title_en="Riyals Left in Tariq's Coin Purse",
                title_ar="الريالات المتبقية في محفظة طارق",
                q_en=f"Tariq has the {m(5)} coins shown in his purse: one {m(10)}-riyal coin, two {m(5)}-riyal coins, and two {m(2)}-riyal coins. He buys a puzzle book for {m(17)} riyals. How many riyals does Tariq have **left**?",
                q_ar=f"مع طارق {m(5)} قطع نقدية في محفظته كما في الشكل: قطعة من فئة {m(10)} ريالات، وقطعتان من فئة {m(5)} ريالات، وقطعتان من فئة ريالين ({m(2)}). اشترى كتاب ألغاز بسعر {m(17)} ريالاً. كم ريالاً **بقي** مع طارق؟",
                correct_val=7,
                distractors=[5, 6, 8, 9],
                idea_en="Add all five coins from largest to smallest first, then subtract the \\( 17 \\)-riyal book price!",
                steps_en=[
                    f"Total money in Tariq's purse = {m('10 + 5 + 5 + 2 + 2 = 24')} riyals.",
                    f"Money left after spending {m(17)} riyals = {m('24 - 17 = 7')} riyals.",
                ],
                check_en=f"Add back: {m('17 + 7 = 24')} riyals!",
                idea_ar="نجمع القطع النقدية الخمس من الأكبر إلى الأصغر أولاً، ثم نطرح ثمن الكتاب \\( 17 \\) ريالاً!",
                steps_ar=[
                    f"مجموع النقود في محفظة طارق = {m('10 + 5 + 5 + 2 + 2 = 24')} ريالاً.",
                    f"المبلغ المتبقي بعد دفع {m(17)} ريالاً = {m('24 - 17 = 7')} ريالات.",
                ],
                check_ar=f"بالجمع العكسي: {m('17 + 7 = 24')} ريالاً!",
                diagram_en=svg_pre_coin_purse(["10", "5", "5", "2", "2"], "Left: ?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-05-EX3",
                title_en="Ice-Cream Cone and Scoop Treats",
                title_ar="تشكيلات بسكويت ونكهات الآيس كريم",
                q_en=f"Kangy's ice-cream stand has {m(3)} kinds of cones (Waffle, Sugar, Cup) and {m(4)} scoop flavours (Vanilla, Mango, Berry, Cocoa). Lina chooses **1 cone** and **1 scoop flavour**. How many different ice-cream treats can she make?",
                q_ar=f"يقدّم كشك الآيس كريم {m(3)} أنواع من البسكويت أو الأكواب و{m(4)} نكهات مختلفة. تختار لينا **نوعاً واحداً** من البسكويت مع **نكهة واحدة**. كم تشكيلة مختلفة من الآيس كريم يمكنها اختيارها؟",
                correct_val=12,
                distractors=[7, 9, 10, 16],
                idea_en="Each of the \\( 3 \\) cones can hold any of the \\( 4 \\) scoop flavours, so add \\( 4 \\) three times!",
                steps_en=[
                    f"Waffle cone gives {m(4)} treats, Sugar cone gives {m(4)} treats, and Cup gives {m(4)} treats.",
                    f"Total treats = {m('4 + 4 + 4 = 3 \\times 4 = 12')}.",
                ],
                check_en=f"Count by flavour instead: {m(4)} flavours {m('\\times\\; 3')} cones = {m('3 + 3 + 3 + 3 = 12')} treats!",
                idea_ar="كل نوع من الأنواع الـ \\( 3 \\) يمكن ملؤه بأي نكهة من النكهات الـ \\( 4 \\)، فنجمع \\( 4 \\) ثلاث مرات!",
                steps_ar=[
                    f"النوع الأول يعطي {m(4)} تشكيلات، والثاني {m(4)} تشكيلات، والثالث {m(4)} تشكيلات.",
                    f"مجموع التشكيلات الممكنة = {m('4 + 4 + 4 = 3 \\times 4 = 12')} تشكيلة.",
                ],
                check_ar=f"بالعدّ حسب النكهات: {m(4)} نكهات في {m(3)} أنواع = {m('3 + 3 + 3 + 3 = 12')} تشكيلة!",
                diagram_en=svg_digit_slots(["3", "4"], "Pairs ?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-05-EX4",
                title_en="Missing Right Cell in a Magic Cross",
                title_ar="العدد المفقود في الخانة اليمنى للصليب السحري",
                q_en=f"In this Magic Cross, the {m(3)} vertical cells have the **same sum** as the {m(3)} horizontal cells. The top cell is {m(8)}, the center cell is {m(6)}, the bottom cell is {m(5)}, and the left cell is {m(4)}. What number belongs in the right cell {m('?')}?",
                q_ar=f"في هذا الصليب السحري، مجموع الخانات الثلاث الرأسية **يساوي** مجموع الخانات الثلاث الأفقية. الخانة العلوية {m(8)}، والوسطى {m(6)}، والسفلية {m(5)}، واليسرى {m(4)}. ما العدد الذي يوضع في الخانة اليمنى {m('?')}؟",
                correct_val=9,
                distractors=[7, 8, 10, 13],
                idea_en="Add the vertical column (`8 + 6 + 5`) to find the magic line sum, then make the horizontal row match it!",
                steps_en=[
                    f"Vertical column sum = {m('8 + 6 + 5 = 19')}.",
                    f"Known horizontal cells add up to {m('4 + 6 = 10')}.",
                    f"Right cell {m('?')} = {m('19 - 10 = 9')}.",
                ],
                check_en=f"Outer-pair shortcut: Top + Bottom = {m('8 + 5 = 13')}, and Left + Right = {m('4 + 9 = 13')}!",
                idea_ar="نجمع العمود الرأسي (`8 + 6 + 5`) لمعرفة المجموع السحري، ثم نكمل الصف الأفقي ليحقق المجموع نفسه!",
                steps_ar=[
                    f"مجموع العمود الرأسي = {m('8 + 6 + 5 = 19')}.",
                    f"مجموع الخانتين المعلومتين في الصف الأفقي = {m('4 + 6 = 10')}.",
                    f"الخانة اليمنى {m('?')} = {m('19 - 10 = 9')}.",
                ],
                check_ar=f"بطريقة الأطراف السريعة: الأعلى + الأسفل = {m('8 + 5 = 13')}، واليسار + اليمين = {m('4 + 9 = 13')}!",
                diagram_en=svg_kang_magic_cross("6", "8", "?", "5", "4", "Same Sum"),
            ),
        ],
        blueprints=[
            "kang_pre_queue_line_positions",
            "kang_pre_coin_bill_totals",
            "kang_pre_outfit_icecream_pairs",
            "kang_pre_magic_cross_five",
        ],
    )


def _lesson_p_6() -> dict:
    return make_kangaroo_lesson(
        lesson_id="KANG-L0-06",
        level=LEVEL,
        unit_num="P.6",
        topic="Data & Probability",
        title_en="Clocks on the Hour & Half-Hour, Bar Charts, Blindfold Marbles & Spinners",
        title_ar="قراءة الساعة والنصف، والتمثيل بالأعمدة، وسحب الكرات دون نظر، والقرص الدوّار",
        summary_en=(
            "Finish your PreEcolier journey as a Kangaroo data & chance champion! Read whole hours and half-hours "
            "on analog clocks, compare colourful bar charts, outsmart dark-room marble bags with 'unluckiest pick' logic, "
            "and spot which prize number is most likely to win on a spinner."
        ),
        summary_ar=(
            "اختتم رحلتك في مستوى بري-إيكولير كبطل في البيانات والاحتمالات! اقرأ الساعات الكاملة وأنصاف الساعات "
            "على ساعة العقارب، وقارن التمثيلات بالأعمدة، واكشف سرّ سحب الكرات دون نظر بقاعدة أسوأ حالة، "
            "وحدّد الرقم الأكثر احتمالاً للفوز على القرص الدوّار."
        ),
        goals_en=[
            "Read **o'clock (`:00`) and half-past (`:30`)** times on an analog clock and add hours or half-hours.",
            "Read **bar charts and picture tallies** to find totals, missing bars, and *'how many more'* differences.",
            "Use **Worst-Case ('Unluckiest Streak') logic** when picking marbles in the dark to be completely sure of winning.",
            "Compare slices on a **game spinner** to decide which number or colour is **most likely** or **least likely**.",
        ],
        goals_ar=[
            "قراءة **الساعة الكاملة (`:00`) والنصف ساعة (`:30`)** على ساعة العقارب وإضافة ساعات أو أنصاف ساعات.",
            "قراءة **التمثيل بالأعمدة والصور** لإيجاد المجموع والعمود المفقود والفرق في أسئلة (بكم يزيد؟).",
            "استخدام **منطق أسوأ حالة ممكنة** عند سحب الكرات دون نظر لضمان النتيجة بشكل أكيد.",
            "مقارنة أجزاء **القرص الدوّار** لتحديد النتيجة **الأكثر احتمالاً** أو **الأقل احتمالاً**.",
        ],
        concepts=[
            kang_concept(
                title_en="1. Analog Clocks: Whole Hours & Half-Hours",
                title_ar="١. ساعة العقارب: الساعة الكاملة والنصف ساعة",
                body_en=(
                    f"An analog clock has **two hands**: the **short red hand** tells the **hour**, and the **long blue hand** tells the **minutes**. "
                    f"When the long blue hand points straight up to {m(12)}, it is an exact **o'clock** (`:00`). "
                    f"When the long blue hand points straight down to {m(6)}, **{m(30)} minutes** (half an hour) have passed—like **half-past {m(4)}** (`4:30`) below! "
                    f"Remember: **two half-hours** ({m('30 + 30 = 60')} minutes) make **{m(1)} full hour**!"
                ),
                body_ar=(
                    f"لساعة العقارب **عقربان**: **العقرب الأحمر القصير** يدل على **الساعات**، و**العقرب الأزرق الطويل** يدل على **الدقائق**. "
                    f"عندما يشير العقرب الطويل للأعلى نحو {m(12)} تكون الساعة **تماماً** (`:00`). "
                    f"وعندما يشير العقرب الطويل للأسفل نحو {m(6)} تكون قد مضت **{m(30)} دقيقة** (نصف ساعة) — مثل **الرابعة والنصف** (`4:30`) في الشكل أدناه! "
                    f"وتذكّر أن **نصفي ساعة** ({m('30 + 30 = 60')} دقيقة) يكوّنان **ساعة كاملة** ({m(1)})!"
                ),
                formula_en=dm("1 \\text{ hour} = 60 \\text{ min}, \\qquad \\text{Half-hour} = 30 \\text{ min} \\;(\\text{minute hand on } 6)"),
                caption_ar="العلاقة بين الساعة الكاملة والنصف ساعة:",
                formula_math_ar=dm("30 + 30 = 60 \\;\\text{min} = 1 \\;\\text{hour}"),
                diagram_en=svg_analog_clock(4, 30, ""),
            ),
            kang_concept(
                title_en="2. Reading Bar Charts & 'How Many More?'",
                title_ar="٢. قراءة التمثيل بالأعمدة وأسئلة (بكم يزيد؟)",
                body_en=(
                    f"In a bar chart, the **top of each bar** lines up with its count! "
                    f"Below, class pets are **Cats = {m(5)}**, **Birds = {m(8)}**, **Fish = {m(3)}**, and **Rabbits = {m(6)}**. "
                    f"To answer *'How many **more** Birds than Fish?'*, **subtract** the shorter bar from the taller bar: {m('8 - 3 = 5')}. "
                    f"To find a **missing bar** when you know the grand total ({m(22)}), add the known bars first and subtract from {m(22)}!"
                ),
                body_ar=(
                    f"في التمثيل بالأعمدة يدل **ارتفاع كل عمود** على العدد المقابل له! "
                    f"في الشكل أدناه: **القطط = {m(5)}**، و**الطيور = {m(8)}**، و**الأسماك = {m(3)}**، و**الأرانب = {m(6)}**. "
                    f"للإجابة عن سؤال *(بكم تزيد الطيور على الأسماك؟)* **نطرح** العمود الأقصر من الأطول: {m('8 - 3 = 5')}. "
                    f"ولإيجاد **عمود مفقود** عند معرفة المجموع الكلي ({m(22)})، نجمع الأعمدة المعلومة أولاً ثم نطرحها من {m(22)}!"
                ),
                formula_en=dm("\\text{How Many More} = 8 - 3 = 5, \\qquad \\text{Total} = 5 + 8 + 3 + 6 = 22"),
                caption_ar="حساب الفرق والمجموع الكلي من التمثيل بالأعمدة:",
                formula_math_ar=dm("8 - 3 = 5, \\qquad 5 + 8 + 3 + 6 = 22"),
                diagram_en=svg_bar_chart([("Cats", 5, "5"), ("Birds", 8, "8"), ("Fish", 3, "3"), ("Rabbits", 6, "6")], y_max=8),
            ),
            kang_concept(
                title_en="3. Blindfold Marbles & Most-Likely Spinners",
                title_ar="٣. سحب الكرات دون نظر والقرص الدوّار الأكثر احتمالاً",
                body_en=(
                    f"When picking marbles in the dark to be **completely sure** of your goal, imagine the **unluckiest streak** first, then add **{m(1)} more pick**! "
                    f"In the bag below (`4` Red, `3` Blue, `2` Green), to be certain of getting **a matching pair** of any colour, the unluckiest start is `1` Red + `1` Blue + `1` Green ({m(3)} picks)—so pick **{m('3 + 1 = 4')}** guarantees a pair! "
                    f"On a **game spinner** cut into equal slices, whichever number appears on the **most slices** is **most likely** to win!"
                ),
                body_ar=(
                    f"عند سحب الكرات دون نظر لضمان هدفك **بشكل أكيد**، تخيّل أولاً **أطول سلسلة غير محظوظة** لا تحقق الهدف، ثم أضف **سحبة واحدة فقط ({m('+ 1')})**! "
                    f"في الكيس أدناه (`4` حمراء و`3` زرقاء و`2` خضراء)، لضمان **زوج من اللون نفسه**، أسوأ بداية هي سحب واحدة من كل لون ({m(3)} كرات)، لذا **{m('3 + 1 = 4')} سحبات** تضمن زوجاً متطابقاً! "
                    f"وعلى **القرص الدوّار** المقسم إلى أجزاء متساوية، الرقم الموجود في **أكبر عدد من الأجزاء** هو **الأكثر احتمالاً** للفوز!"
                ),
                formula_en=dm("\\text{Sure Picks} = (\\text{Unluckiest Streak}) + 1"),
                caption_ar="قاعدة السحب الأكيد في الغرفة المظلمة:",
                formula_math_ar=dm("3 \\text{ colours} \\implies 3 + 1 = 4 \\text{ picks}"),
                diagram_en=svg_pre_marble_bag([("R", 4), ("B", 3), ("G", 2)], "Blind"),
            ),
        ],
        traps_en=[
            "Trap: Reading the long minute hand on 6 as '6 minutes' or '6 o'clock'! On an analog clock, the minute hand on 6 means 30 minutes (half-past).",
            "Trap: Adding two bars when asked 'How many more?'! 'How many more' always asks for the difference (Taller − Shorter).",
            "Trap: Confusing 'any matching pair' with 'at least 1 Red marble'! For at least 1 Red, the unluckiest streak pulls ALL Blue and Green marbles first.",
        ],
        traps_ar=[
            "فخ شائع: قراءة العقرب الطويل عند 6 على أنها 6 دقائق أو الساعة السادسة! العقرب الطويل على 6 يعني 30 دقيقة (النصف).",
            "فخ شائع: جمع العمودين عند سؤال (بكم يزيد؟)! هذا السؤال يطلب دائماً الفرق بالطرح (الأكبر − الأصغر).",
            "فخ شائع: الخلط بين (زوج من أي لون) و(كرة حمراء واحدة على الأقل)! لضمان كرة حمراء قد تسحب جميع الكرات الزرقاء والخضراء أولاً.",
        ],
        examples=[
            kang_worked_example(
                ex_id="KANG-L0-06-EX1",
                title_en="Finish Time of Sami's Science Show",
                title_ar="وقت انتهاء البرنامج العلمي لسامي",
                q_en=f"Sami's science show starts at **half-past {m(2)}** (`2:30`) as shown on the clock. The show lasts **{m(1)} hour and {m(30)} minutes**. At what exact **o'clock** hour does the show finish?",
                q_ar=f"يبدأ البرنامج العلمي لسامي عند الساعة **الثانية والنصف** (`2:30`) كما يظهر على الساعة، ويستمر مدة **ساعة واحدة و{m(30)} دقيقة**. عند أي ساعة **تماماً** ينتهي البرنامج؟",
                correct_val=4,
                distractors=[3, 5, 6, 8],
                idea_en="Add \\( 1 \\) whole hour first (`2:30` to `3:30`), then add the remaining \\( 30 \\) minutes to complete the next hour!",
                steps_en=[
                    f"Starting at `2:30`, adding {m(1)} hour brings the clock to `3:30`.",
                    f"Adding {m(30)} more minutes moves from `3:30` to `4:00` (**{m(4)} o'clock**).",
                ],
                check_en=f"Notice `2:30` + `0:30` = `3:00`, plus `1:00` = `4:00` (**{m(4)} o'clock**)!",
                idea_ar="نضيف ساعة كاملة أولاً (`2:30` تصبح `3:30`)، ثم نضيف الـ \\( 30 \\) دقيقة المتبقية فتكتمل الساعة التالية!",
                steps_ar=[
                    f"من الساعة `2:30` نضيف ساعة واحدة فنصل إلى `3:30`.",
                    f"نضيف {m(30)} دقيقة أخرى فتنتقل الساعة من `3:30` إلى `4:00` (**الساعة {m(4)} تماماً**).",
                ],
                check_ar=f"بطريقة أخرى: `2:30` + نصف ساعة = `3:00`، زائد ساعة كاملة = الساعة **{m(4)}** تماماً!",
                diagram_en=svg_analog_clock(2, 30, ""),
            ),
            kang_worked_example(
                ex_id="KANG-L0-06-EX2",
                title_en="Lama's Missing Bar on the Sticker Chart",
                title_ar="عمود لمى المفقود في لوحة الملصقات",
                q_en=f"Four classmates earned {m(24)} star stickers altogether this week. On the bar chart, **Ali** has {m(6)}, **Mona** has {m(9)}, **Ziad** has {m(4)}, and **Lama's** count is marked {m('?')}. How many star stickers did **Lama** earn?",
                q_ar=f"حصل أربعة زملاء معاً على {m(24)} ملصق نجمة هذا الأسبوع. يبيّن التمثيل بالأعمدة أن لدى **علي** {m(6)}، ولدى **منى** {m(9)}، ولدى **زياد** {m(4)}، بينما عُلم عمود **لمى** بالرمز {m('?')}. كم ملصقاً حصلت عليه **لمى**؟",
                correct_val=5,
                distractors=[4, 6, 7, 8],
                idea_en="Add the three known sticker bars first, then subtract their sum from \\( 24 \\)!",
                steps_en=[
                    f"Known stickers = {m('6 + 9 + 4 = 19')}.",
                    f"Lama's stickers = {m('24 - 19 = 5')}.",
                ],
                check_en=f"Add all four bars: {m('6 + 9 + 4 + 5 = 24')} stickers!",
                idea_ar="نجمع الأعمدة الثلاثة المعلومة أولاً، ثم نطرح مجموعها من العدد الكلي \\( 24 \\)!",
                steps_ar=[
                    f"مجموع الملصقات المعلومة = {m('6 + 9 + 4 = 19')} ملصقاً.",
                    f"ملصقات لمى = {m('24 - 19 = 5')} ملصقات.",
                ],
                check_ar=f"بجمع الأعمدة الأربعة: {m('6 + 9 + 4 + 5 = 24')} ملصقاً!",
                diagram_en=svg_bar_chart([("Ali", 6, "6"), ("Mona", 9, "9"), ("Ziad", 4, "4"), ("Lama", 5, "?")], y_max=10),
            ),
            kang_worked_example(
                ex_id="KANG-L0-06-EX3",
                title_en="Guaranteeing a Red Marble in the Dark",
                title_ar="ضمان سحب كرة حمراء دون نظر",
                q_en=f"A cloth pouch contains {m(5)} **Red** marbles, {m(4)} **Blue** marbles, and {m(3)} **Green** marbles. Without looking inside, what is the **smallest** number of marbles Dana must pull out to be **completely sure** she gets **at least {m(1)} Red** marble?",
                q_ar=f"يحتوي كيس قماشي على {m(5)} كرات **حمراء** و{m(4)} كرات **زرقاء** و{m(3)} كرات **خضراء**. دون النظر داخل الكيس، ما **أصغر** عدد من الكرات يجب أن تسحبه دانة لتكون **متأكدة تماماً** من الحصول على **كرة حمراء واحدة على الأقل**؟",
                correct_val=8,
                distractors=[2, 4, 6, 9],
                idea_en="Imagine the unluckiest picks where Dana pulls **every Blue and Green marble first**, then add \\( 1 \\) more pick!",
                steps_en=[
                    f"In the unluckiest streak without any Red marble, Dana pulls all {m(4)} Blue marbles and all {m(3)} Green marbles = {m('4 + 3 = 7')} marbles.",
                    f"Only Red marbles remain in the pouch now, so her **8th** pick ({m('7 + 1 = 8')}) is guaranteed to be Red!",
                ],
                check_en=f"With {m(7)} picks she might have {m(4)} Blue + {m(3)} Green ({m(0)} Red), so {m(8)} is the smallest sure number!",
                idea_ar="نتخيّل أسوأ حالة تسحب فيها دانة **جميع الكرات الزرقاء والخضراء أولاً**، ثم نضيف سحبة واحدة!",
                steps_ar=[
                    f"في أسوأ سلسلة دون أي كرة حمراء، تسحب دانة كل الكرات الزرقاء ({m(4)}) وكل الخضراء ({m(3)}) = {m('4 + 3 = 7')} كرات.",
                    f"لم يبقَ في الكيس بعدها إلا الكرات الحمراء، لذا السحبة **الثامنة** ({m('7 + 1 = 8')}) تكون حمراء حتماً!",
                ],
                check_ar=f"بسبع سحبات قد تخرج {m(4)} زرقاء و{m(3)} خضراء دون حمراء، لذا {m(8)} هو أصغر عدد مضمون!",
                diagram_en=svg_pre_marble_bag([("R", 5), ("B", 4), ("G", 3)], "Sure R?"),
            ),
            kang_worked_example(
                ex_id="KANG-L0-06-EX4",
                title_en="Most Likely Prize Number on Kangy's Spinner",
                title_ar="الرقم الأكثر احتمالاً للفوز على قرص الكنغر",
                q_en=f"Kangy's game wheel is divided into {m(8)} **equal** slices labelled around the circle as shown: `2, 5, 3, 5, 1, 4, 5, 2`. When Kangy spins the arrow, which prize number is it **most likely** to land on?",
                q_ar=f"قُسّم قرص اللعب لدى الكنغر إلى {m(8)} أجزاء **متساوية** كُتبت عليها الأرقام بالترتيب كما في الشكل: `2, 5, 3, 5, 1, 4, 5, 2`. عند تدوير المؤشر، ما رقم الجائزة **الأكثر احتمالاً** لأن يقف عنده المؤشر؟",
                correct_val=5,
                distractors=[1, 2, 3, 4],
                idea_en="Since all \\( 8 \\) slices have the exact same size, count how many slices carry each prize number!",
                steps_en=[
                    f"Count each number on the wheel: {m(5)} appears on **{m(3)}** slices, {m(2)} appears on **{m(2)}** slices, and {m(1)}, {m(3)}, {m(4)} appear on **{m(1)}** slice each.",
                    f"Because {m(5)} covers the most slices ({m(3)} out of {m(8)}), prize number {m(5)} is most likely to win!",
                ],
                check_en=f"Total slices = {m('3 + 2 + 1 + 1 + 1 = 8')} slices, and {m(3)} slices is the largest count!",
                idea_ar="بما أن الأجزاء الـ \\( 8 \\) متساوية تماماً في المساحة، نعدّ كم جزءاً يحمل كل رقم!",
                steps_ar=[
                    f"نعدّ تكرار كل رقم: الرقم {m(5)} يتكرر في **{m(3)}** أجزاء، والرقم {m(2)} في **جزأين** ({m(2)})، أما {m(1)} و{m(3)} و{m(4)} ففي **جزء واحد** لكل منها.",
                    f"بما أن الرقم {m(5)} يغطي أكبر عدد من الأجزاء ({m(3)} من أصل {m(8)})، فهو الأكثر احتمالاً للفوز!",
                ],
                check_ar=f"مجموع الأجزاء = {m('3 + 2 + 1 + 1 + 1 = 8')} أجزاء، وأكبر تكرار هو {m(3)} للرقم {m(5)}!",
                diagram_en=svg_spinner([
                    (0.125, "2"),
                    (0.125, "5"),
                    (0.125, "3"),
                    (0.125, "5"),
                    (0.125, "1"),
                    (0.125, "4"),
                    (0.125, "5"),
                    (0.125, "2"),
                ]),
            ),
        ],
        blueprints=[
            "kang_pre_clock_hour_halfhour",
            "kang_pre_bar_pictograph_read",
            "kang_pre_dark_room_marbles",
            "kang_pre_spinner_most_likely",
        ],
    )


def get_preecolier_lessons() -> list[dict]:
    """Return all 6 Kangaroo PreEcolier (Grades 1–2) bilingual study lessons."""
    return [
        _lesson_p_1(),
        _lesson_p_2(),
        _lesson_p_3(),
        _lesson_p_4(),
        _lesson_p_5(),
        _lesson_p_6(),
    ]
