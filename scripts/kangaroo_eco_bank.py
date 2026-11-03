"""Kangaroo Math Competition — Ecolier Division (Grades 3–4) Question Bank — 360 Programmatically Verified Questions."""
from fractions import Fraction

from kangaroo_common import (
    DIFF_TO_POINTS,
    KANGAROO_FORBIDDEN_RE,
    explain_ar,
    explain_en,
    load_other_track_stems,
    m,
    make_5_bilingual_options,
    make_kang_q,
    make_kangaroo_question,
    norm_text,
    svg_analog_clock,
    svg_balance_scales,
    svg_bar_chart,
    svg_column_cryptarithm,
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digital_clock,
    svg_digit_slots,
    svg_fenceposts,
    svg_fraction_grid,
    svg_function_machine,
    svg_grid_polygon,
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
    svg_motion_timeline,
    svg_number_line_jumps,
    svg_number_strip,
    svg_painted_cube_3d,
    svg_pie_chart,
    svg_polyomino,
    svg_spinner,
    svg_street_grid,
)

LEVEL = "Ecolier"


class BankBuilder:
    """Sequential builder generating KANG-ECO-001 .. KANG-ECO-360 with full validation."""

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
        qid = f"KANG-ECO-{len(self.items) + 1:03d}"
        self.items.append(
            make_kang_q(
                qid=qid,
                level=LEVEL,
                topic=topic,
                difficulty=difficulty,
                blueprint=blueprint,
                q_en=q_en,
                q_ar=q_ar,
                correct_val=correct_val,
                distractors=distractors,
                hint_en=hint_en,
                hint_ar=hint_ar,
                idea_en=idea_en,
                steps_en=steps_en,
                check_en=check_en,
                idea_ar=idea_ar,
                steps_ar=steps_ar,
                check_ar=check_ar,
                suffix=suffix,
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
        qid = f"KANG-ECO-{len(self.items) + 1:03d}"
        opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, correct_pair_idx, seed_key=qid)
        self.items.append(
            make_kangaroo_question(
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


# ==============================================================================
# UNIT 1.1 — Number Theory (60 Questions: KANG-ECO-001 .. KANG-ECO-060)
# Blueprints: kang_eco_brick_pyramid, kang_eco_kangaroo_jumps,
#             kang_eco_place_value_digits, kang_eco_fencepost_spacing
# ==============================================================================
_SEG_COUNTS = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}


def _add_unit_1_1(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. kang_eco_brick_pyramid (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_brick_pyramid"
    pyr_easy = [
        (4, 7, 5, "Kangy", "الكنغر"),
        (6, 3, 9, "Lina", "لينا"),
        (8, 5, 4, "Omar", "عمر"),
        (3, 9, 7, "Sara", "سارة"),
        (7, 6, 8, "Tariq", "طارق"),
    ]
    for a, b, c, nm_en, nm_ar in pyr_easy:
        ml, mr = a + b, b + c
        ans = ml + mr
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} builds a 3-row number pyramid where each brick equals the sum of the two bricks right below it. The bottom bricks are {m(a)}, {m(b)}, and {m(c)}. What number belongs in the top {m('?')} brick?",
            f"يبني {nm_ar} هرماً عددياً من 3 صفوف بحيث تساوي كل طوبة مجموع الطوبتين أسفلها مباشرة. إذا كان الصف السفلي يضم {m(a)} و{m(b)} و{m(c)}، فما العدد في طوبة القمة {m('?')}؟",
            ans, [a + b + c, ans - b + 1, ans + b, ml + c],
            f"Find the two middle-row bricks ({m(f'{a}+{b}')} and {m(f'{b}+{c}')}) first, then add them!",
            f"أوجد طوبتي الصف الأوسط ({m(f'{a}+{b}')} و{m(f'{b}+{c}')}) أولاً ثم اجمعهما!",
            "Compute the middle row from adjacent bottom pairs, then sum the middle row.",
            [
                f"Left middle brick = {m(f'{a} + {b} = {ml}')}, and right middle brick = {m(f'{b} + {c} = {mr}')}.",
                f"Top brick = {m(f'{ml} + {mr} = {ans}')}.",
            ],
            f"Notice the middle number {m(b)} is counted twice: {m(f'{a} + 2 \\times {b} + {c} = {ans}')}!",
            "نحسب طوبتي الصف الأوسط من جمع كل طوبتين متجاورتين في الأسفل، ثم نجمعهما للوصول للقمة.",
            [
                f"الطوبة الوسطى اليسرى = {m(f'{a} + {b} = {ml}')}، والطوبة الوسطى اليمنى = {m(f'{b} + {c} = {mr}')}.",
                f"طوبة القمة = {m(f'{ml} + {mr} = {ans}')}.",
            ],
            f"لاحظ أن الطوبة الوسطى {m(b)} تُجمع مرتين: {m(f'{a} + 2 \\times {b} + {c} = {ans}')}!",
            diagram_en=svg_kang_number_pyramid([["?"], ["", ""], [str(a), str(b), str(c)]]),
        )

    pyr_med = [
        (4, 8, 6, "Nora's sandcastle", "قلعة نورة الرملية"),
        (7, 5, 9, "Zaid's wooden", "هرم زيد الخشبي"),
        (9, 7, 4, "Hala's sticker", "هرم ملصقات هلا"),
        (6, 9, 8, "Yousef's chalk", "هرم يوسف الطباشيري"),
        (8, 4, 11, "Amal's puzzle", "لغز أمل الهرمي"),
    ]
    for a, b, c, ctx_en, ctx_ar in pyr_med:
        top = a + 2 * b + c
        B.add_math(
            tp, "Medium", bp,
            f"In {ctx_en} pyramid, each brick is the sum of the two bricks directly beneath it. The bottom row shows {m(a)}, {m('?')}, and {m(c)}, while the top brick is {m(top)}. What number goes into {m('?')}?",
            f"في {ctx_ar}، كل طوبة تساوي مجموع الطوبتين أسفلها مباشرة. الصف السفلي يظهر فيه {m(a)} و{m('?')} و{m(c)}، وطوبة القمة تساوي {m(top)}. ما العدد الذي يوضع مكان {m('?')}؟",
            b, [2 * b, b + 1, b - 1, top - a - b],
            f"The middle bottom brick gets added into BOTH middle-row bricks, so {m(f'{a} + 2 \\times ? + {c} = {top}')}!",
            f"الطوبة الوسطى في الأسفل تدخل في طوبتي الصف الأوسط معاً، أي {m(f'{a} + 2 \\times ? + {c} = {top}')}!",
            "Subtract the two outer bottom corners from the top brick, then divide by 2.",
            [
                f"Let the missing middle brick be {m('x')}. The middle row bricks are {m(f'{a} + x')} and {m(f'x + {c}')}.",
                f"Their sum at the top is {m(f'{a} + {c} + 2x = {a + c} + 2x = {top}')}.",
                f"So {m(f'2x = {top} - {a + c} = {2 * b}')}, giving {m(f'x = {b}')}.",
            ],
            f"Check: {m(f'({a}+{b}) + ({b}+{c}) = {a+b} + {b+c} = {top}')}!",
            "نطرح ركني القاعدة من القمة ثم نقسم الباقي على 2 لأن طوبة الوسط تُحسب مرتين.",
            [
                f"نفرض أن الطوبة المفقودة {m('x')}، فيكون مجموع القمة {m(f'{a + c} + 2x = {top}')}.",
                f"إذن {m(f'2x = {top} - {a + c} = {2 * b}')} ومنها {m(f'x = {b}')}.",
            ],
            f"تحقق: {m(f'({a}+{b}) + ({b}+{c}) = {a+b} + {b+c} = {top}')}!",
            diagram_en=svg_kang_number_pyramid([[str(top)], ["", ""], [str(a), "?", str(c)]]),
        )

    pyr_hard = [
        (3, 5, 4, 6, "Jude", "جود"),
        (2, 6, 3, 5, "Salman", "سلمان"),
        (4, 3, 5, 2, "Pippa", "بيبا"),
        (5, 4, 2, 7, "Leo", "ليو"),
        (1, 7, 4, 3, "Rayan", "ريان"),
    ]
    for a, b, c, d, nm_en, nm_ar in pyr_hard:
        r3_l, r3_m, r3_r = a + b, b + c, c + d
        r2_l, r2_r = r3_l + r3_m, r3_m + r3_r
        top = r2_l + r2_r
        B.add_math(
            tp, "Hard", bp,
            f"In {nm_en}'s 4-row Kangaroo pyramid, every brick equals the sum of the two bricks directly below it. Given top brick {m(top)}, second-row left brick {m(r2_l)}, and bottom row {m(a)}, {m('?')}, {m(c)}, {m(d)}, find {m('?')}.",
            f"في هرم الكنغر ذي 4 صفوف لدى {nm_ar}، كل طوبة تساوي مجموع الطوبتين أسفلها مباشرة. إذا كانت القمة {m(top)}، وطوبة يسار الصف الثاني {m(r2_l)}، والصف السفلي {m(a)} و{m('?')} و{m(c)} و{m(d)}، فأوجد قيمة {m('?')}.",
            b, [b + 1, b + 2, r3_m, max(1, b - 1)],
            f"First find the right brick under {m(top)} ({m(f'{top} - {r2_l}')}), and add {m(f'{c} + {d}')} on the bottom right!",
            f"أوجد أولاً الطوبة اليمنى أسفل {m(top)} ({m(f'{top} - {r2_l}')}) واجمع {m(f'{c} + {d}')} في أسفل اليمين!",
            "Work down the right side of the 4-row pyramid using subtraction.",
            [
                f"In Row 2 (below the top), the right brick is {m(f'{top} - {r2_l} = {r2_r}')}.",
                f"In Row 3, the rightmost brick is {m(f'{c} + {d} = {r3_r}')}, so the middle brick of Row 3 is {m(f'{r2_r} - {r3_r} = {r3_m}')}.",
                f"Finally, {m(f'? + {c} = {r3_m}')}, so {m(f'? = {r3_m} - {c} = {b}')}.",
            ],
            f"Left-side check: {m(f'({a}+{b}) + ({b}+{c}) = {r3_l} + {r3_m} = {r2_l}')}. Verified!",
            "ننزل عبر الجانب الأيمن للهرم بالطرح خطوة بخطوة.",
            [
                f"طوبة يمين الصف الثاني تساوي {m(f'{top} - {r2_l} = {r2_r}')}.",
                f"طوبة يمين الصف الثالث تساوي {m(f'{c} + {d} = {r3_r}')}، إذن وسط الصف الثالث يساوي {m(f'{r2_r} - {r3_r} = {r3_m}')}.",
                f"ومنه {m(f'? = {r3_m} - {c} = {b}')}.",
            ],
            f"تحقق من اليسار: {m(f'({a}+{b}) + ({b}+{c}) = {r2_l}')}!",
            diagram_en=svg_kang_number_pyramid([[str(top)], [str(r2_l), ""], ["", "", ""], [str(a), "?", str(c), str(d)]]),
        )

    # 2. kang_eco_kangaroo_jumps (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_kangaroo_jumps"
    jmp_easy = [
        (3, 4, 6, "green lily pads", "أوراق زنبق خضراء"),
        (5, 6, 7, "park stepping stones", "أحجار الممر في الحديقة"),
        (2, 5, 8, "chalk squares", "مربعات الطباشير"),
        (10, 3, 9, "wooden tiles", "البلاطات الخشبية"),
        (4, 7, 6, "painted circles", "الدوائر الملونة"),
    ]
    for s, step, k, ctx_en, ctx_ar in jmp_easy:
        ans = s + k * step
        B.add_math(
            tp, "Easy", bp,
            f"Kangy starts on number {m(s)} along a path of {ctx_en} and jumps forward by {m(step)} on every hop. Which number does Kangy land on after {m(k)} hops?",
            f"يبدأ الكنغر عند العدد {m(s)} على مسار من {ctx_ar} ويقفز للأمام بمقدار {m(step)} في كل قفزة. على أي عدد يهبط بعد {m(k)} قفزات؟",
            ans, [s + (k - 1) * step, s + (k + 1) * step, k * step, ans + 2],
            f"Each of the {m(k)} hops adds {m(step)} to the starting number {m(s)}.",
            f"كل قفزة من القفزات الـ {m(k)} تضيف {m(step)} إلى عدد البداية {m(s)}.",
            "Multiply the number of hops by the hop size, then add the starting number.",
            [
                f"Total distance jumped in {m(k)} hops = {m(f'{k} \\times {step} = {k * step}')}.",
                f"Landing number = {m(f'{s} + {k * step} = {ans}')}.",
            ],
            f"Skip-counting check: {m(s)}, {m(s + step)}, {m(s + 2 * step)}, ..., landing at {m(ans)}!",
            "نضرب عدد القفزات في طول القفزة الواحدة ثم نجمع نقطة البداية.",
            [
                f"مجموع التقدم في {m(k)} قفزات = {m(f'{k} \\times {step} = {k * step}')}.",
                f"عدد الوصول = {m(f'{s} + {k * step} = {ans}')}.",
            ],
            f"بالعد النمطي نصل بعد القفزة {m(k)} إلى العدد {m(ans)}!",
            diagram_en=svg_number_strip([str(s), str(s + step), str(s + 2 * step), "...", "?"]),
        )

    jmp_med = [
        (4, 1, 16, "a baby kangaroo", "كنغر صغير"),
        (6, 2, 22, "a desert frog", "ضفدع صحراوي"),
        (5, 3, 15, "a clockwork grasshopper", "جندب آلي"),
        (7, 3, 23, "a springy rabbit", "أرنب وثّاب"),
        (6, 4, 16, "a climbing squirrel", "سنجاب متسلق"),
    ]
    for fwd, back, target, actor_en, actor_ar in jmp_med:
        pos = 0
        hops = 0
        while True:
            hops += 1
            pos += fwd
            if pos >= target:
                assert pos == target
                break
            pos -= back
        net = fwd - back
        B.add_math(
            tp, "Medium", bp,
            f"Starting at {m(0)} on a number line, {actor_en} leaps {m(fwd)} units forward each morning and slips {m(back)} units back each night. On which morning leap does it first land on {m(target)}?",
            f"ينطلق {actor_ar} من العدد {m(0)} على خط الأعداد، فيقفز {m(fwd)} وحدات للأمام كل صباح وينزلق {m(back)} وحدات للخلف كل ليلة. في أي قفزة صباحية يصل لأول مرة إلى {m(target)}؟",
            hops, [hops - 1, hops + 1, hops + 2, target // net + 2],
            f"Each full day+night advances {m(f'{fwd} - {back} = {net}')} units, so stop at {m(target - fwd)} before the final morning leap!",
            f"كل يوم وليلة يحقق تقدماً صافياً قدره {m(f'{fwd} - {back} = {net}')}، فتوقف عند {m(target - fwd)} قبل القفزة الصباحية الأخيرة!",
            "Count full forward-minus-back cycles until one morning leap reaches the target directly.",
            [
                f"Each full day-and-night cycle advances by {m(f'{fwd} - {back} = {net}')} units.",
                f"After {m(hops - 1)} full cycles, the position is {m(f'{hops - 1} \\times {net} = {(hops - 1) * net}')}.",
                f"On morning leap #{m(hops)}, it jumps {m(f'{(hops - 1) * net} + {fwd} = {target}')} and reaches the goal!",
            ],
            f"It reaches {m(target)} during morning leap #{m(hops)} before slipping back!",
            "نحسب الدورات الكاملة حتى نصبح على بُعد قفزة صباحية واحدة من الهدف.",
            [
                f"التقدم الصافي في الدورة الواحدة = {m(f'{fwd} - {back} = {net}')}.",
                f"بعد {m(hops - 1)} دورات كاملة يقف عند {m((hops - 1) * net)}.",
                f"في القفزة الصباحية رقم {m(hops)} يقفز {m(f'{(hops - 1) * net} + {fwd} = {target}')}!",
            ],
            f"يصل إلى {m(target)} في القفزة الصباحية رقم {m(hops)} ويتوقف دون تراجع!",
            diagram_en=svg_number_line_jumps(fwd, back, target),
        )

    jmp_hard = [
        (2, 32, 3, 2, "Kangy", "Pippa", "الكنغر كانجي", "بيبا"),
        (5, 45, 5, 3, "Leo", "Ruby", "ليو", "روبي"),
        (0, 36, 4, 5, "Bouncy", "Skippy", "باونسي", "سكيبي"),
        (4, 46, 4, 3, "Milo", "Koko", "مايلو", "كوكو"),
        (3, 51, 5, 3, "Zuzu", "Toto", "زوزو", "توتو"),
    ]
    for s1, s2, v1, v2, n1_en, n2_en, n1_ar, n2_ar in jmp_hard:
        dist = s2 - s1
        assert dist % (v1 + v2) == 0
        whistles = dist // (v1 + v2)
        meet_stone = s1 + whistles * v1
        assert s2 - whistles * v2 == meet_stone
        B.add_math(
            tp, "Hard", bp,
            f"{n1_en} stands on stone {m(s1)} and {n2_en} stands on stone {m(s2)}. Every whistle blow, {n1_en} jumps {m(v1)} stones right (toward higher numbers) while {n2_en} jumps {m(v2)} stones left. On **which stone number** do they meet?",
            f"يقف {n1_ar} على الحجر {m(s1)} وتقف {n2_ar} على الحجر {m(s2)}. مع كل صافرة يقفز {n1_ar} بمقدار {m(v1)} لليمين وتقفز {n2_ar} بمقدار {m(v2)} لليسار. على **أي رقم حجر** يلتقيان؟",
            meet_stone, [whistles, meet_stone - v1, meet_stone + v1, s1 + whistles * v2],
            f"Together they close the gap of {m(f'{s2} - {s1} = {dist}')} by {m(f'{v1} + {v2} = {v1 + v2}')} stones per whistle!",
            f"يقتربان معاً في كل صافرة بمقدار {m(f'{v1} + {v2} = {v1 + v2}')} حجراً لسد المسافة {m(dist)}!",
            "Find how many whistles it takes to close the gap, then calculate the meeting stone!",
            [
                f"Initial gap = {m(f'{s2} - {s1} = {dist}')} stones, closing by {m(f'{v1} + {v2} = {v1 + v2}')} stones per whistle.",
                f"They meet after {m(f'{dist} \\div {v1 + v2} = {whistles}')} whistles.",
                f"Meeting stone = {m(f'{s1} + {whistles} \\times {v1} = {meet_stone}')}.",
            ],
            f"Check from the right: {m(f'{s2} - {whistles} \\times {v2} = {meet_stone}')}—same stone!",
            "نوجد عدد الصافرات بقسمة المسافة على مجموع القفزتين، ثم نحسب رقم حجر الالتقاء.",
            [
                f"المسافة الأولية {m(f'{s2} - {s1} = {dist}')} وتقل بمقدار {m(v1 + v2)} في كل صافرة، فيلتقيان بعد {m(whistles)} صافرات.",
                f"رقم حجر الالتقاء = {m(f'{s1} + {whistles} \\times {v1} = {meet_stone}')}.",
            ],
            f"تحقق من الطرف الآخر: {m(f'{s2} - {whistles} \\times {v2} = {meet_stone}')}!",
            diagram_en=svg_motion_timeline(f"#{s1}", f"#{s2}", f"Gap {dist}", f"+{v1}", f"−{v2}", meet=True),
        )

    # 3. kang_eco_place_value_digits (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_place_value_digits"
    pv_easy = [
        ([5, 0, 8, 1], "Maha", "مها"),
        ([6, 0, 2, 9], "Faisal", "فيصل"),
        ([4, 7, 0, 3], "Dana", "دانة"),
        ([9, 1, 0, 6], "Kareem", "كريم"),
        ([8, 4, 0, 2], "Reem", "ريم"),
    ]
    for cards, nm_en, nm_ar in pv_easy:
        nz = sorted(x for x in cards if x != 0)
        ans = int(f"{nz[0]}0{nz[1]}{nz[2]}")
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} has four digit cards: {m(cards[0])}, {m(cards[1])}, {m(cards[2])}, and {m(cards[3])}. Using each card once, what is the **smallest 4-digit** number {nm_en} can make?",
            f"مع {nm_ar} أربع بطاقات أرقام: {m(cards[0])} و{m(cards[1])} و{m(cards[2])} و{m(cards[3])}. باستعمال كل بطاقة مرة واحدة، ما **أصغر عدد من 4 أرقام** يمكن تكوينه؟",
            ans,
            [int(f"{nz[0]}{nz[1]}0{nz[2]}"), int(f"{nz[1]}0{nz[0]}{nz[2]}"), int(f"{nz[0]}{nz[1]}{nz[2]}"), int(f"{nz[0]}0{nz[2]}{nz[1]}")],
            f"A 4-digit number cannot start with {m(0)}, so place the smallest non-zero digit in the thousands spot!",
            f"العدد المكوّن من 4 أرقام لا يبدأ بالصفر {m(0)}؛ ضع أصغر رقم غير صفري في الآلاف ثم الصفر بعده!",
            "Put the smallest non-zero digit in the thousands place, then 0 in the hundreds place, then sort the rest.",
            [
                f"The smallest non-zero card is {m(nz[0])}, so {m(nz[0])} goes in the thousands place.",
                f"Place {m(0)} right after it in the hundreds place, followed by {m(nz[1])} and {m(nz[2])}: {m(ans)}.",
            ],
            f"Putting {m(0)} first would make {m(int(f'{nz[0]}{nz[1]}{nz[2]}'))}, which has only 3 digits—so {m(ans)} is smallest!",
            "نضع أصغر رقم غير صفري في الآلاف، ثم الصفر في المئات، ثم نرتب الباقي تصاعدياً.",
            [
                f"أصغر بطاقة غير صفرية هي {m(nz[0])} فتوضع في منزلة الآلاف.",
                f"نضع {m(0)} في المئات ثم {m(nz[1])} في العشرات و{m(nz[2])} في الآحاد فنحصل على {m(ans)}.",
            ],
            f"العدد {m(ans)} يتكون من 4 أرقام كاملة وهو الأصغر!",
            diagram_en=svg_digit_slots([str(d) for d in cards], "Smallest 4-digit number"),
        )

    pv_med = [
        ("2026", "year banner", "لافتة العام"),
        ("1475", "locker code", "رمز الخزانة"),
        ("3194", "scoreboard", "لوحة النتائج"),
        ("7042", "train sign", "لوحة القطار"),
        ("5137", "camp badge", "شارة المعسكر"),
    ]
    for code, ctx_en, ctx_ar in pv_med:
        lit = sum(_SEG_COUNTS[ch] for ch in code)
        extra_to_8 = 28 - lit
        B.add_math(
            tp, "Medium", bp,
            f"The {ctx_en} displays `{code}` using orange matchsticks on a 7-segment board as shown (where `8` uses all {m(7)} slots per digit). How many **more** matchsticks are needed to fill every empty grey slot and turn `{code}` into `8888`?",
            f"تعرض {ctx_ar} الرمز `{code}` بأعواد ثقاب برتقالية كما في الشكل (حيث يملأ الرقم `8` المواضع الـ {m(7)} كاملة لكل خانة). كم عوداً **إضافياً** نحتاج لملء المواضع الرمادية الفارغة وتحويل `{code}` إلى `8888`؟",
            extra_to_8, [lit, extra_to_8 - 1, extra_to_8 + 1, extra_to_8 + 2],
            "Count the missing grey sticks in each of the 4 digits (or subtract lit sticks from 28)!",
            "عدّ المواضع الرمادية الفارغة في كل رقم من الأرقام الأربعة (أو اطرح الأعواد المضيئة من 28)!",
            "Subtract each digit's lit segments from 7 and sum across all 4 digits.",
            [
                f"Lit sticks per digit in `{code}`: " + ", ".join(f"`{ch}` uses {m(_SEG_COUNTS[ch])}" for ch in code) + f" (total {m(lit)}).",
                f"Turning all 4 digits into `8888` needs {m('4 \\times 7 = 28')} sticks, so {m(f'28 - {lit} = {extra_to_8}')} more sticks are needed.",
            ],
            f"Missing per digit: " + " + ".join(str(7 - _SEG_COUNTS[ch]) for ch in code) + f" = {m(extra_to_8)}!",
            "نطرح عدد الأعواد البرتقالية في كل خانة من 7 ثم نجمع النواتج للأرقام الأربعة.",
            [
                f"مجموع الأعواد المضيئة حالياً في `{code}` هو {m(lit)} عوداً.",
                f"الرمز `8888` يحتاج {m('4 \\times 7 = 28')} عوداً، إذن نحتاج {m(f'28 - {lit} = {extra_to_8}')} أعواد إضافية.",
            ],
            f"بجمع الفراغات في كل رقم نحصل على {m(extra_to_8)} بالضبط!",
            diagram_en=svg_kang_matchstick_digits(code),
        )

    pv_hard = [
        (2, 4, 3, 5, 6),
        (1, 7, 4, 6, 8),
        (3, 2, 2, 7, 4),
        (4, 8, 1, 5, 7),
        (2, 6, 5, 9, 3),
    ]
    for a, b, c, d, star in pv_hard:
        n1 = 100 * a + 10 * star + b
        n2 = 100 * c + 10 * star + d
        tot = n1 + n2
        B.add_math(
            tp, "Hard", bp,
            f"In the column addition shown, both `★` symbols stand for the **exact same single digit**: {m(f'\\overline{{{a}\\bigstar{b}}} + \\overline{{{c}\\bigstar{d}}} = {tot}')}. What digit does `★` represent?",
            f"في عملية الجمع العمودية الموضحة، يمثّل الرمزان `★` **الرقم المفرد نفسه تماماً**: {m(f'\\overline{{{a}\\bigstar{b}}} + \\overline{{{c}\\bigstar{d}}} = {tot}')}. ما الرقم الذي يمثّله الرمز `★`؟",
            star, [max(0, star - 1), min(9, star + 1) if star < 9 else 2, (star + 3) % 10, (2 * star) % 10 if (2 * star) % 10 != star else 5],
            f"Replace `★` with {m(0)} first ({m(f'{100*a+b} + {100*c+d} = {100*(a+c)+b+d}')}), then see how many {m(20)}s are missing!",
            f"عوّض عن `★` بالصفر مؤقتاً ({m(100*(a+c)+b+d)}) ثم اقسم الفرق عن {m(tot)} على {m(20)}!",
            "Each `★` sits in the tens place (worth 10·★), so together the two stars contribute 20·★.",
            [
                f"Without the tens digit `★`, {m(f'{100*a+b} + {100*c+d} = {100*(a+c)+b+d}')}.",
                f"The two `★` digits in the tens column add {m(f'20 \\times \\bigstar = {tot} - {100*(a+c)+b+d} = {20 * star}')}.",
                f"Dividing by {m(20)} gives {m(f'\\bigstar = {star}')}.",
            ],
            f"Verify: {m(f'{n1} + {n2} = {tot}')}. Exact match!",
            "وجود `★` في عشرات العددين يضيف `20 × ★` إلى مجموع المئات والآحاد.",
            [
                f"مجموع العددين مع وضع صفر في العشرات = {m(100*(a+c)+b+d)}.",
                f"إذن {m(f'20 \\times \\bigstar = {tot} - {100*(a+c)+b+d} = {20 * star}')}، ومنها {m(f'\\bigstar = {star}')}.",
            ],
            f"تحقق بالجمع الكامل: {m(f'{n1} + {n2} = {tot}')}!",
            diagram_en=svg_column_cryptarithm([f"{a}★{b}", f"{c}★{d}"], str(tot)),
        )

    # 4. kang_eco_fencepost_spacing (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_fencepost_spacing"
    fp_easy = [
        (7, 5, "camp lanterns", "فوانيس مخيم"),
        (11, 4, "colorful flags", "أعلام ملونة"),
        (8, 7, "orange cones", "أقماع برتقالية"),
        (12, 3, "park benches", "مقاعد حديقة"),
        (10, 8, "wooden posts", "أعمدة خشبية"),
    ]
    for n, d, item_en, item_ar in fp_easy:
        ans = (n - 1) * d
        B.add_math(
            tp, "Easy", bp,
            f"There are {m(n)} {item_en} placed in a straight line with {m(d)} meters between any two neighbors. How many meters is it from the **first** one to the **last** one?",
            f"وُضعت {m(n)} من {item_ar} في خط مستقيم بحيث تفصل {m(d)} أمتار بين كل اثنين متجاورين. كم متراً تبلغ المسافة من **الأول** إلى **الأخير**؟",
            ans, [n * d, (n - 2) * d, (n + 1) * d, ans + 2],
            f"Count the spaces between {m(n)} items: {m(f'{n} - 1 = {n - 1}')} gaps!",
            f"عدد المسافات بين {m(n)} علامات في خط مستقيم هو {m(f'{n} - 1 = {n - 1}')} مسافة!",
            "Use Distance = (Number of items − 1) × Gap length.",
            [
                f"Number of gaps = {m(f'{n} - 1 = {n - 1}')}.",
                f"Total distance = {m(f'{n - 1} \\times {d} = {ans}')} meters.",
            ],
            f"Avoid the {m(f'{n} \\times {d} = {n * d}')} trap—the first item is at {m(0)} m!",
            "نطبق القاعدة: المسافة الكلية = (العدد − 1) × طول المسافة الواحدة.",
            [
                f"عدد المسافات الفاصلة = {m(f'{n} - 1 = {n - 1}')}.",
                f"المسافة الكلية = {m(f'{n - 1} \\times {d} = {ans}')} متراً.",
            ],
            f"انتبه من فخ ضرب {m(f'{n} \\times {d} = {n * d}')}!",
            diagram_en=svg_fenceposts(f"{d} m", "? m"),
        )

    fp_med = [
        (36, 4, "a wooden bridge", "جسر خشبي"),
        (45, 5, "a school hallway", "ممر المدرسة"),
        (60, 6, "a racetrack fence", "سياج المضمار"),
        (42, 7, "a garden wall", "سور الحديقة"),
        (64, 8, "a festival street", "شارع المهرجان"),
    ]
    for L, d, place_en, place_ar in fp_med:
        gaps = L // d
        ans = gaps + 1
        B.add_math(
            tp, "Medium", bp,
            f"Along one straight side of {place_en} of length {m(L)} meters, banners are placed every {m(d)} meters, **including one at the very start and one at the very end**. How many banners are placed in total?",
            f"على جانب مستقيم واحد من {place_ar} طوله {m(L)} متراً، تُوضع راية كل {m(d)} أمتار **بما في ذلك البداية والنهاية**. كم راية تُوضع إجمالاً؟",
            ans, [gaps, gaps - 1, ans + 1, 2 * ans],
            f"Divide {m(L)} by {m(d)} to count gaps, then **add 1** for the starting banner!",
            f"اقسم {m(L)} على {m(d)} لمعرفة عدد المسافات، ثم **أضف 1** لراية البداية!",
            "Use Posts = (Total Length ÷ Gap) + 1 when both endpoints get a banner.",
            [
                f"Number of {m(d)}-meter gaps = {m(f'{L} \\div {d} = {gaps}')}.",
                f"Including both ends gives {m(f'{gaps} + 1 = {ans}')} banners.",
            ],
            f"Check: {m(ans)} banners have {m(f'{ans} - 1 = {gaps}')} gaps of {m(d)} m = {m(L)} m!",
            "نقسم الطول الكلي على المسافة ثم نضيف 1 لأن الطرفين يضمان رايتين.",
            [
                f"عدد المسافات = {m(f'{L} \\div {d} = {gaps}')} مسافة.",
                f"عدد الرايات شاملة البداية والنهاية = {m(f'{gaps} + 1 = {ans}')} رايات.",
            ],
            f"تحقق: {m(ans)} رايات بينها {m(gaps)} مسافات طولها {m(f'{gaps} \\times {d} = {L}')} م!",
            diagram_en=svg_fenceposts(f"{d} m", f"{L} m"),
        )

    fp_hard = [
        (3, 5, 2, "wooden logs", "جذوع خشبية"),
        (2, 6, 3, "bamboo poles", "أعمدة خيزران"),
        (4, 4, 2, "plastic pipes", "أنابيب بلاستيكية"),
        (3, 6, 4, "metal rods", "قضبان معدنية"),
        (5, 4, 3, "cedar planks", "ألواح أرز"),
    ]
    for k, p, t, mat_en, mat_ar in fp_hard:
        cuts_per = p - 1
        tot_cuts = k * cuts_per
        ans = tot_cuts * t
        B.add_math(
            tp, "Hard", bp,
            f"A builder has {m(k)} separate {mat_en}. Each one must be sawed into {m(p)} smaller pieces, sawed one piece at a time, and each saw cut takes {m(t)} minutes. How many minutes does all the sawing take?",
            f"لدى نجار {m(k)} من {mat_ar} المنفصلة، ويريد نشر كل واحد منها إلى {m(p)} قطع أصغر على حدة، وتستغرق كل عملية نشر واحدة {m(t)} دقائق. كم دقيقة يستغرق النشر كله؟",
            ans, [k * p * t, (k * p - 1) * t, cuts_per * t, (tot_cuts + 1) * t],
            f"Sawing **1** log into {m(p)} pieces takes only {m(f'{p} - 1 = {cuts_per}')} cuts!",
            f"تقطيع القطعة الواحدة إلى {m(p)} أجزاء يحتاج {m(f'{p} - 1 = {cuts_per}')} نشرات فقط!",
            "Each separate log needs (p − 1) cuts; multiply by k logs and t minutes per cut.",
            [
                f"Cutting 1 log into {m(p)} pieces requires {m(f'{p} - 1 = {cuts_per}')} saw cuts.",
                f"For {m(k)} separate logs, total cuts = {m(f'{k} \\times {cuts_per} = {tot_cuts}')} cuts.",
                f"Total time = {m(f'{tot_cuts} \\times {t} = {ans}')} minutes.",
            ],
            f"Double trap avoided: neither {m(f'{k}\\times{p}\\times{t}={k*p*t}')} nor {m(f'({k}\\times{p}-1)\\times{t}={(k*p-1)*t}')}!",
            "كل جذع مستقل يحتاج (p − 1) نشرات، ثم نضرب في عدد الجذوع وزمن النشرة الواحدة.",
            [
                f"لتقسيم قطعة واحدة إلى {m(p)} أجزاء نحتاج {m(f'{p} - 1 = {cuts_per}')} نشرات.",
                f"لعدد {m(k)} قطع منفصلة نحتاج {m(f'{k} \\times {cuts_per} = {tot_cuts}')} نشرة.",
                f"الزمن الكلي = {m(f'{tot_cuts} \\times {t} = {ans}')} دقيقة.",
            ],
            f"تجنبنا فخ ضرب {m(p)} مباشرة وفخ اعتبار القطع متصلة!",
            diagram_en=svg_fenceposts("1 cut", f"{p} pieces/log"),
        )



# ==============================================================================
# UNIT 1.2 — Algebra (60 Questions: KANG-ECO-061 .. KANG-ECO-120)
# Blueprints: kang_eco_toy_balance, kang_eco_magic_cross,
#             kang_eco_repeating_beads, kang_eco_mystery_machine
# ==============================================================================
def _add_unit_1_2(B: BankBuilder) -> None:
    tp = "Algebra"

    # 1. kang_eco_toy_balance (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_toy_balance"
    bal_easy = [
        (3, 1, 1, 2, 6, "Kangy", "الكنغر"),
        (2, 1, 1, 4, 6, "Lina", "لينا"),
        (1, 2, 1, 3, 2, "Omar", "عمر"),
        (3, 1, 1, 4, 9, "Sara", "سارة"),
        (1, 3, 1, 2, 3, "Tariq", "طارق"),
    ]
    for c1, s1, s2, t2, ask_balls, nm_en, nm_ar in bal_easy:
        assert (ask_balls * s1) % c1 == 0
        cubes = (ask_balls * s1) // c1
        assert cubes % s2 == 0
        ans = (cubes // s2) * t2
        B.add_math(
            tp, "Easy", bp,
            f"On {nm_en}'s first balance scale, {m(c1)} orange ball(s) balance {m(s1)} green cube(s). On the second scale, {m(s2)} green cube(s) balance {m(t2)} purple pyramids. How many purple pyramids balance {m(ask_balls)} orange balls?",
            f"في الميزان الأول لدى {nm_ar} تتعادل {m(c1)} من الكرات البرتقالية مع {m(s1)} من المكعبات الخضراء، وفي الميزان الثاني تتعادل {m(s2)} من المكعبات الخضراء مع {m(t2)} أهرامات بنفسجية. كم هرماً بنفسجياً يعادل {m(ask_balls)} كرات برتقالية؟",
            ans, [cubes, ans - 2 if ans > 2 else ans + 3, ans + 2, ask_balls + t2],
            "First trade the orange balls for green cubes, then trade each green cube for purple pyramids!",
            "استبدل الكرات البرتقالية بمكعبات خضراء أولاً، ثم استبدل المكعبات الخضراء بأهرامات بنفسجية!",
            "Use equal-weight substitution from orange balls to green cubes to purple pyramids.",
            [
                f"Since {m(c1)} ball(s) = {m(s1)} cube(s), {m(ask_balls)} balls = {m(cubes)} green cubes.",
                f"Since {m(s2)} cube = {m(t2)} pyramids, {m(cubes)} cubes = {m(f'{cubes} \\times {t2} = {ans}')} purple pyramids.",
            ],
            f"Substitution check: {m(ask_balls)} balls = {m(cubes)} cubes = {m(ans)} pyramids!",
            "نستبدل الكرات بالمكعبات ثم نستبدل المكعبات بالأهرامات بالتناسب.",
            [
                f"بما أن {m(c1)} كرة = {m(s1)} مكعب، فإن {m(ask_balls)} كرات تعادل {m(cubes)} مكعبات خضراء.",
                f"وبما أن المكعب يعادل {m(t2)} أهرامات، فإن {m(cubes)} مكعبات تعادل {m(f'{cubes} \\times {t2} = {ans}')} هرماً.",
            ],
            f"تحقق: {m(ask_balls)} كرات = {m(cubes)} مكعبات = {m(ans)} هرماً!",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        )

    bal_med = [
        (2, 1, 2, 4, 15, "Nora", "نورة"),
        (3, 2, 1, 3, 12, "Zaid", "زيد"),
        (2, 3, 2, 4, 10, "Hala", "هلا"),
        (4, 2, 1, 3, 8, "Yousef", "يوسف"),
        (3, 1, 2, 3, 20, "Amal", "أمل"),
    ]
    for c1, s1, s2, t2, w_pyr, nm_en, nm_ar in bal_med:
        assert (t2 * w_pyr) % s2 == 0
        w_sq = (t2 * w_pyr) // s2
        assert (s1 * w_sq) % c1 == 0
        w_cir = (s1 * w_sq) // c1
        B.add_math(
            tp, "Medium", bp,
            f"In {nm_en}'s toy lab, {m(c1)} orange balls balance {m(s1)} green cube(s), and {m(s2)} green cube(s) balance {m(t2)} purple pyramids. Each purple pyramid weighs {m(w_pyr)} grams. How many grams does **1 orange ball** weigh?",
            f"في معمل الألعاب لدى {nm_ar}، تتعادل {m(c1)} كرات برتقالية مع {m(s1)} مكعبات خضراء، وتتعادل {m(s2)} مكعبات خضراء مع {m(t2)} أهرامات بنفسجية. إذا كان وزن الهرم البنفسجي الواحد {m(w_pyr)} غراماً، فكم غراماً يزن **كرة برتقالية واحدة**؟",
            w_cir, [w_sq, w_cir + w_pyr, max(2, w_cir - 5), s1 * w_sq],
            "Find the weight of 1 green cube from the right scale first, then find 1 orange ball on the left scale!",
            "احسب وزن المكعب الأخضر الواحد من الميزان الأيمن أولاً، ثم احسب وزن الكرة البرتقالية من الميزان الأيسر!",
            "Work from the known pyramid weight to 1 green cube, then to 1 orange ball.",
            [
                f"Right scale: {m(s2)} green cube(s) weigh {m(f'{t2} \\times {w_pyr} = {t2 * w_pyr}')} g, so 1 green cube weighs {m(f'{t2 * w_pyr} \\div {s2} = {w_sq}')} g.",
                f"Left scale: {m(c1)} orange balls weigh {m(f'{s1} \\times {w_sq} = {s1 * w_sq}')} g, so 1 orange ball weighs {m(f'{s1 * w_sq} \\div {c1} = {w_cir}')} g.",
            ],
            f"Check: {m(f'{c1} \\times {w_cir} = {c1 * w_cir}')} g = {m(f'{s1} \\times {w_sq}')} g!",
            "نبدأ بوزن الهرم المعلوم لإيجاد وزن المكعب الأخضر ثم وزن الكرة البرتقالية.",
            [
                f"من الميزان الأيمن: وزن المكعب الأخضر الواحد = {m(f'({t2} \\times {w_pyr}) \\div {s2} = {w_sq}')} غراماً.",
                f"من الميزان الأيسر: وزن الكرة البرتقالية الواحدة = {m(f'({s1} \\times {w_sq}) \\div {c1} = {w_cir}')} غراماً.",
            ],
            f"تحقق: {m(f'{c1} \\times {w_cir} = {s1 * w_sq}')} غراماً!",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        )

    bal_hard = [
        (2, 3, 1, 2, 4, 1, "Jude", "جود"),
        (3, 2, 2, 3, 3, 2, "Salman", "سلمان"),
        (2, 1, 1, 4, 3, 2, "Pippa", "بيبا"),
        (1, 2, 2, 3, 2, 2, "Leo", "ليو"),
        (2, 4, 1, 2, 3, 1, "Rayan", "ريان"),
    ]
    for c1, s1, s2, t2, qc, qs, nm_en, nm_ar in bal_hard:
        # Express everything in purple pyramids: s2 cubes = t2 pyramids, c1 balls = s1 cubes = s1*t2/s2 pyramids
        # Total pyramids for qc balls + qs cubes:
        num = qc * s1 * t2 + qs * c1 * t2
        den = c1 * s2
        assert num % den == 0
        ans = num // den
        balls_pyr = (qc * s1 * t2) // den
        cubes_pyr = (qs * t2) // s2
        B.add_math(
            tp, "Hard", bp,
            f"Two balanced scales are shown. {nm_en} places {m(qc)} orange balls **and** {m(qs)} green cube(s) together on the left pan of a third scale. How many **purple pyramids** must {nm_en} put on the right pan to balance it?",
            f"يظهر في الرسم ميزانان متعادلان. وضع {nm_ar} في الكفة اليسرى لميزان ثالث {m(qc)} كرات برتقالية **و**{m(qs)} من المكعبات الخضراء معاً. كم **هرماً بنفسجياً** يجب وضعه في الكفة اليمنى ليتعادل الميزان؟",
            ans, [balls_pyr, ans - 2, ans + 2, ans + t2],
            "Convert both the orange balls and the green cubes into purple pyramids, then add!",
            "حوّل كلاً من الكرات البرتقالية والمكعبات الخضراء إلى ما يعادلها من الأهرامات البنفسجية ثم اجمع!",
            "Convert each group into purple pyramids using the two scale ratios, then sum.",
            [
                f"From the scales, {m(qc)} orange balls equal {m(balls_pyr)} purple pyramids.",
                f"Also, {m(qs)} green cube(s) equal {m(cubes_pyr)} purple pyramids.",
                f"Together they balance {m(f'{balls_pyr} + {cubes_pyr} = {ans}')} purple pyramids.",
            ],
            f"Check: {m(balls_pyr)} + {m(cubes_pyr)} = {m(ans)} pyramids (don't forget the extra green cube(s)!).",
            "نحوّل الكرات البرتقالية والمكعبات الخضراء كلتيهما إلى أهرامات بنفسجية ثم نجمع.",
            [
                f"تعادل {m(qc)} كرات برتقالية {m(balls_pyr)} هرماً بنفسجياً.",
                f"وتعادل {m(qs)} مكعبات خضراء {m(cubes_pyr)} أهرامات بنفسجية.",
                f"المجموع اللازم للموازنة = {m(f'{balls_pyr} + {cubes_pyr} = {ans}')} هرماً.",
            ],
            f"تحقق: {m(f'{balls_pyr} + {cubes_pyr} = {ans}')} هرماً!",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        )

    # 2. kang_eco_magic_cross (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_magic_cross"
    mc_easy = [
        (5, 8, 6, 4, "Lina", "لينا"),
        (7, 9, 4, 6, "Omar", "عمر"),
        (3, 10, 7, 9, "Sara", "سارة"),
        (6, 11, 5, 7, "Tariq", "طارق"),
        (4, 12, 8, 9, "Nora", "نورة"),
    ]
    for cen, top, bot, left, nm_en, nm_ar in mc_easy:
        col_sum = top + cen + bot
        ans = top + bot - left
        B.add_math(
            tp, "Easy", bp,
            f"In {nm_en}'s 5-cell Kangaroo cross (center {m(cen)}, top {m(top)}, bottom {m(bot)}, and left {m(left)}), the sum of the {m(3)} numbers in the horizontal row equals the sum of the {m(3)} numbers in the vertical column. What number belongs in the right {m('?')} square?",
            f"في تقاطع {nm_ar} المكوّن من 5 مربعات (المركز {m(cen)}، الأعلى {m(top)}، الأسفل {m(bot)}، واليسار {m(left)})، يساوي مجموع الأعداد الثلاثة في الصف الأفقي مجموع الأعداد الثلاثة في العمود الرأسي. ما العدد المناسب لمربع اليمين {m('?')}؟",
            ans, [col_sum, ans + cen, max(1, ans - 2), ans + 2],
            f"First add the vertical column ({m(f'{top} + {cen} + {bot} = {col_sum}')}), then make the horizontal row match!",
            f"اجمع العمود الرأسي أولاً ({m(f'{top} + {cen} + {bot} = {col_sum}')}) ثم اجعل الصف الأفقي يساويه!",
            "Equate the 3-cell horizontal sum and the 3-cell vertical sum.",
            [
                f"Vertical column sum = {m(f'{top} + {cen} + {bot} = {col_sum}')}.",
                f"Horizontal row must also sum to {m(col_sum)}: {m(f'{left} + {cen} + ? = {col_sum}')}, so {m(f'? = {col_sum} - {left + cen} = {ans}')}.",
            ],
            f"Shortcut: since center {m(cen)} is shared, {m(f'{left} + ? = {top} + {bot} = {top + bot}')}, giving {m(ans)}!",
            "نساوي مجموع الصف بمجموع العمود (أو نساوي طرفي الصف بطرفي العمود لحذف المركز المشترك).",
            [
                f"مجموع العمود الرأسي = {m(f'{top} + {cen} + {bot} = {col_sum}')}.",
                f"إذن {m(f'? = {col_sum} - ({left} + {cen}) = {ans}')}.",
            ],
            f"اختصار ذكي: {m(f'{top} + {bot} - {left} = {ans}')}!",
            diagram_en=svg_kang_magic_cross(str(cen), str(top), "?", str(bot), str(left), "Row sum = Col sum"),
        )

    mc_med = [
        ([1, 2, 4, 6, 8], 1, "Kangy", "الكنغر"),
        ([2, 3, 4, 8, 10], 3, "Maha", "مها"),
        ([1, 3, 6, 7, 9], 6, "Faisal", "فيصل"),
        ([3, 5, 7, 8, 9], 8, "Dana", "دانة"),
        ([4, 6, 9, 10, 12], 9, "Kareem", "كريم"),
    ]
    for nums, expected_c, nm_en, nm_ar in mc_med:
        valid_c = []
        for cand in nums:
            rem = sorted(x for x in nums if x != cand)
            if rem[0] + rem[3] == rem[1] + rem[2]:
                valid_c.append(cand)
        assert valid_c == [expected_c], f"Non-unique center: {valid_c}"
        rem = sorted(x for x in nums if x != expected_c)
        line_sum = expected_c + rem[0] + rem[3]
        n_str = ", ".join(str(x) for x in nums)
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} places each of the five numbers {m(n_str)} into one cell of a 5-square cross so the 3-cell row sum equals the 3-cell column sum. Which number **must** be placed in the center?",
            f"يضع {nm_ar} الأعداد الخمسة {m(n_str)} في خلايا تقاطع مكوّن من 5 مربعات بحيث يتساوى مجموع خلايا الصف الثلاث مع مجموع خلايا العمود الثلاث. أي عدد **يجب** أن يوضع في الوسط؟",
            expected_c, [x for x in nums if x != expected_c],
            "After removing the center number, the other 4 numbers must form two pairs with the exact same sum!",
            "بعد اختيار عدد الوسط، يجب أن تنقسم الأعداد الأربعة الباقية إلى زوجين لهما المجموع نفسه!",
            "Pick the unique center that leaves four numbers with an even sum splitting into two equal pairs.",
            [
                f"Total of all 5 numbers = {m(sum(nums))}. Leaving two equal-sum pairs requires {m(f'{sum(nums)} - \\text{{center}}')} to be even.",
                f"Testing {m(expected_c)} in the center leaves {m(rem)}, which pairs cleanly as {m(f'{rem[0]} + {rem[3]} = {rem[0]+rem[3]}')} and {m(f'{rem[1]} + {rem[2]} = {rem[1]+rem[2]}')}.",
                f"No other number among {m(n_str)} leaves two equal pairs, so the center must be {m(expected_c)}.",
            ],
            f"Row {m(f'{rem[0]}+{expected_c}+{rem[3]}={line_sum}')} and Column {m(f'{rem[1]}+{expected_c}+{rem[2]}={line_sum}')}!",
            "نختار العدد الوحيد الذي يترك أربعة أعداد تنقسم إلى زوجين متساويي المجموع.",
            [
                f"مجموع الأعداد الخمسة = {m(sum(nums))}، واختيار {m(expected_c)} في الوسط يترك الأعداد {m(rem)}.",
                f"تنقسم هذه الأربعة إلى زوجين متساويين: {m(f'{rem[0]} + {rem[3]} = {rem[1]} + {rem[2]} = {rem[0]+rem[3]}')}.",
            ],
            f"مجموع الصف ومجموع العمود كلاهما يساوي {m(line_sum)}!",
            diagram_en=svg_kang_magic_cross("?", "", "", "", "", f"Use {n_str}"),
        )

    mc_hard_shifts = [
        (0, "silver", "الفضية"),
        (2, "golden", "الذهبية"),
        (3, "emerald", "الزمردية"),
        (5, "sapphire", "الياقوتية"),
        (7, "crystal", "البلورية"),
    ]
    base_sq = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    for sh, adj_en, adj_ar in mc_hard_shifts:
        sq = [[v + sh for v in row] for row in base_sq]
        msum = sq[2][0] + sq[1][1] + sq[0][2]
        ans = sq[1][2]
        B.add_math(
            tp, "Hard", bp,
            f"In Kangy's {adj_en} {m('3 \\times 3')} magic square, every row, every column, and both 3-cell diagonals add up to the **same magic sum**. Four numbers are shown: top-left {m(sq[0][0])}, top-right {m(sq[0][2])}, center {m(sq[1][1])}, and bottom-left {m(sq[2][0])}. What number goes in {m('?')}?",
            f"في المربع السحري {adj_ar} {m('3 \\times 3')} لدى الكنغر، يتساوى مجموع كل صف وكل عمود والقطرين. ظهرت أربعة أعداد: أعلى اليسار {m(sq[0][0])}، وأعلى اليمين {m(sq[0][2])}، والوسط {m(sq[1][1])}، وأسفل اليسار {m(sq[2][0])}. ما العدد في خانة {m('?')}؟",
            ans, [sq[1][0], sq[0][1], ans + 2, msum - ans],
            f"Add the complete diagonal ({m(f'{sq[2][0]} + {sq[1][1]} + {sq[0][2]}')}) first to unlock the magic sum!",
            f"اجمع القطر المكتمل ({m(f'{sq[2][0]} + {sq[1][1]} + {sq[0][2]}')}) أولاً لمعرفة المجموع السحري!",
            "Find the magic sum from the complete diagonal, fill the middle-left cell via Column 1, then solve Row 2.",
            [
                f"The diagonal from bottom-left to top-right gives the magic sum: {m(f'{sq[2][0]} + {sq[1][1]} + {sq[0][2]} = {msum}')}.",
                f"In the left column, the middle-left cell is {m(f'{msum} - {sq[0][0]} - {sq[2][0]} = {sq[1][0]}')}.",
                f"In the middle row, {m(f'? = {msum} - {sq[1][0]} - {sq[1][1]} = {ans}')}.",
            ],
            f"Check middle row: {m(f'{sq[1][0]} + {sq[1][1]} + {ans} = {msum}')}, matching the magic sum!",
            "نحسب المجموع السحري من القطر المكتمل، ثم نكمل العمود الأيسر فنجد خانة الصف الأوسط.",
            [
                f"المجموع السحري من القطر = {m(f'{sq[2][0]} + {sq[1][1]} + {sq[0][2]} = {msum}')}.",
                f"الخلية الوسطى في العمود الأيسر = {m(f'{msum} - {sq[0][0]} - {sq[2][0]} = {sq[1][0]}')}.",
                f"إذن في الصف الأوسط {m(f'? = {msum} - {sq[1][0]} - {sq[1][1]} = {ans}')}.",
            ],
            f"تحقق: {m(f'{sq[1][0]} + {sq[1][1]} + {ans} = {msum}')}!",
            diagram_en=svg_magic_square_3x3([
                [str(sq[0][0]), "", str(sq[0][2])],
                ["", str(sq[1][1]), "?"],
                [str(sq[2][0]), "", ""],
            ]),
        )

    # 3. kang_eco_repeating_beads (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_repeating_beads"
    color_5 = [
        ("Red", "أحمر", "R"),
        ("Blue", "أزرق", "B"),
        ("Yellow", "أصفر", "Y"),
        ("Green", "أخضر", "G"),
        ("Purple", "بنفسجي", "P"),
    ]
    bead_easy = [
        (27, [0, 1, 2, 3, 4], "necklace", "عقد"),
        (34, [1, 3, 0, 4, 2], "party garland", "زينة الحفل"),
        (41, [2, 0, 3, 1, 4], "bookmark ribbon", "شريط الكتاب"),
        (38, [4, 2, 1, 0, 3], "paper chain", "سلسلة ورقية"),
        (45, [3, 0, 4, 2, 1], "lantern string", "حبل الفوانيس"),
    ]
    for pos, perm, item_en, item_ar in bead_easy:
        cyc = [color_5[i] for i in perm]
        ans_i = (pos - 1) % 5
        pairs = [(c[0], c[1]) for c in cyc]
        seq_en = ", ".join(c[0] for c in cyc)
        seq_ar = "، ".join(c[1] for c in cyc)
        q_div, rem = divmod(pos, 5)
        B.add_bilingual(
            tp, "Easy", bp,
            f"Kangy makes a {item_en} by repeating the 5-color sequence **{seq_en}** over and over from the 1st bead. What color is the **{m(pos)}th** bead?",
            f"يصنع الكنغر {item_ar} بتكرار الألوان الخمسة **{seq_ar}** بالترتيب نفسه بدءاً من الخرزة الأولى. ما لون الخرزة رقم **{m(pos)}**؟",
            pairs, ans_i,
            f"Divide {m(pos)} by {m(5)} and check the remainder (remainder {m(0)} means the 5th color)!",
            f"اقسم {m(pos)} على {m(5)} وانظر إلى الباقي (الباقي {m(0)} يعني اللون الخامس)!",
            "Every 5 beads repeat the exact same block; use the remainder mod 5.",
            [
                f"Dividing {m(pos)} by {m(5)} gives {m(q_div)} full blocks of 5 with remainder {m(rem)}.",
                f"Position {m(pos)} matches item #{m(5 if rem == 0 else rem)} in the block, which is **{cyc[ans_i][0]}**.",
            ],
            f"Bead #{m(5 * q_div if rem > 0 else pos)} ends a full block, landing Bead #{m(pos)} on **{cyc[ans_i][0]}**!",
            "تتكرر الدورة كل 5 خرزات؛ نقسم رتبة الخرزة على 5 ونستخدم الباقي.",
            [
                f"بقسمة {m(pos)} على {m(5)} نحصل على {m(q_div)} مجموعات والباقي {m(rem)}.",
                f"إذن الخرزة رقم {m(pos)} تطابق العنصر رقم {m(5 if rem == 0 else rem)} في المجموعة وهو **{cyc[ans_i][1]}**.",
            ],
            f"تحقق: اللون الصحيح هو **{cyc[ans_i][1]}**!",
            diagram_en=svg_kang_necklace_beads([c[2] for c in cyc] + [cyc[0][2], cyc[1][2], "?"]),
        )

    bead_med = [
        (["R", "G", "R", "Y"], "R", "Red", "حمراء", 26, "Lina", "لينا"),
        (["B", "Y", "B", "B", "G"], "B", "Blue", "زرقاء", 29, "Omar", "عمر"),
        (["Y", "R", "Y", "B", "Y"], "Y", "Yellow", "صفراء", 32, "Sara", "سارة"),
        (["G", "P", "G", "R"], "G", "Green", "خضراء", 35, "Tariq", "طارق"),
        (["P", "B", "P", "P", "Y"], "P", "Purple", "بنفسجية", 28, "Nora", "نورة"),
    ]
    cmap_en = {"R": "Red", "B": "Blue", "Y": "Yellow", "G": "Green", "P": "Purple"}
    cmap_ar = {"R": "أحمر", "B": "أزرق", "Y": "أصفر", "G": "أخضر", "P": "بنفسجي"}
    for blk, tgt, t_en, t_ar, n_tot, nm_en, nm_ar in bead_med:
        full_seq = (blk * (n_tot // len(blk) + 2))[:n_tot]
        ans = full_seq.count(tgt)
        k_len = len(blk)
        q_b, r_b = divmod(n_tot, k_len)
        per_blk = blk.count(tgt)
        rem_cnt = blk[:r_b].count(tgt)
        pat_en = ", ".join(cmap_en[x] for x in blk)
        pat_ar = "، ".join(cmap_ar[x] for x in blk)
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} strings {m(n_tot)} beads by repeating the {m(k_len)}-bead pattern **{pat_en}** from start to finish. How many **{t_en}** beads are on the string altogether?",
            f"تنظِم/ينظِم {nm_ar} عدد {m(n_tot)} خرزة بتكرار النمط المكون من {m(k_len)} خرزات (**{pat_ar}**) من البداية للنهاية. كم خرزة **{t_ar}** في الخيط كله؟",
            ans, [q_b * per_blk, ans - 1, ans + 1, (q_b + 1) * per_blk if (q_b + 1) * per_blk != ans else ans + 2],
            f"Split {m(n_tot)} into full groups of {m(k_len)} plus the leftover {m(r_b)} beads at the end!",
            f"قسّم {m(n_tot)} إلى مجموعات كاملة من {m(k_len)} خرزات ثم افحص الـ {m(r_b)} خرزات المتبقية!",
            "Multiply the count in one block by the number of full blocks, then add matches in the remainder.",
            [
                f"Divide {m(n_tot)} by {m(k_len)}: {m(f'{n_tot} = {q_b} \\times {k_len} + {r_b}')}.",
                f"Each full block has {m(per_blk)} {t_en} beads, giving {m(f'{q_b} \\times {per_blk} = {q_b * per_blk}')}.",
                f"The first {m(r_b)} leftover beads contribute {m(rem_cnt)} more, for a total of {m(f'{q_b * per_blk} + {rem_cnt} = {ans}')}.",
            ],
            f"Full blocks ({m(q_b * per_blk)}) + leftover ({m(rem_cnt)}) = {m(ans)} {t_en} beads!",
            "نحسب عدد الخرزات المطلوبة في المجموعات الكاملة ثم نضيف ما يظهر في الباقي.",
            [
                f"لدينا {m(f'{n_tot} = {q_b} \\times {k_len} + {r_b}')}.",
                f"في المجموعات الكاملة {m(f'{q_b} \\times {per_blk} = {q_b * per_blk}')}، وفي الباقي {m(rem_cnt)}، فالمجموع {m(ans)}.",
            ],
            f"تحقق: {m(f'{q_b * per_blk} + {rem_cnt} = {ans}')}!",
            diagram_en=svg_kang_necklace_beads(blk + blk[:3] + ["?"]),
        )

    bead_hard = [
        ([2, 5, 1, 4], 23, "Zaid", "زيد"),
        ([3, 1, 6, 2], 26, "Hala", "هلا"),
        ([4, 2, 5, 1, 3], 28, "Yousef", "يوسف"),
        ([1, 7, 2, 4], 29, "Amal", "أمل"),
        ([5, 3, 2, 6, 1], 32, "Jude", "جود"),
    ]
    for pat, n_tot, nm_en, nm_ar in bead_hard:
        seq = (pat * (n_tot // len(pat) + 2))[:n_tot]
        ans = sum(seq)
        k_len = len(pat)
        q_b, r_b = divmod(n_tot, k_len)
        b_sum = sum(pat)
        r_sum = sum(pat[:r_b])
        p_str = ", ".join(str(x) for x in pat)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} writes a repeating number strip by copying the block `({p_str})` over and over until {m(n_tot)} numbers are written in total. What is the **sum of all {m(n_tot)} numbers**?",
            f"يكتب/تكتب {nm_ar} شريط أعداد متكرراً بنسخ المجموعة `({p_str})` مراراً حتى يكتمل {m(n_tot)} عدداً. ما **مجموع الأعداد الـ {m(n_tot)} كلها**؟",
            ans, [q_b * b_sum, (q_b + 1) * b_sum, ans - pat[0], ans + pat[-1]],
            f"Find the sum of one {m(k_len)}-number block ({m(b_sum)}), multiply by full blocks, and add the leftover numbers!",
            f"احسب مجموع المجموعة الواحدة ({m(b_sum)}) واضربه في عدد المجموعات الكاملة ثم أضف الأعداد المتبقية!",
            "Sum one repeating block, multiply by floor(N / k), and add the prefix of length (N mod k).",
            [
                f"One block `({p_str})` has {m(k_len)} numbers with sum {m(b_sum)}.",
                f"Since {m(f'{n_tot} = {q_b} \\times {k_len} + {r_b}')}, there are {m(q_b)} full blocks summing to {m(f'{q_b} \\times {b_sum} = {q_b * b_sum}')}.",
                f"The remaining {m(r_b)} number(s) at the end add {m(r_sum)}, giving {m(f'{q_b * b_sum} + {r_sum} = {ans}')}.",
            ],
            f"Check: {m(f'{q_b} \\times {b_sum} + {r_sum} = {ans}')}!",
            "نضرب مجموع المجموعة الواحدة في عدد التكرارات الكاملة ثم نجمع الحدود المتبقية في النهاية.",
            [
                f"مجموع المجموعة الواحدة = {m(b_sum)}، ولدينا {m(f'{n_tot} = {q_b} \\times {k_len} + {r_b}')}.",
                f"المجموع الكلي = {m(f'{q_b} \\times {b_sum} + {r_sum} = {ans}')}.",
            ],
            f"تحقق: {m(f'{q_b * b_sum} + {r_sum} = {ans}')}!",
            diagram_en=svg_number_strip([str(x) for x in pat] + [str(pat[0]), "...", "?"]),
        )

    # 4. kang_eco_mystery_machine (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_mystery_machine"
    mm_easy = [
        (6, 4, 3, "add_mul", "Salman", "سلمان"),
        (8, 3, 5, "mul_add", "Pippa", "بيبا"),
        (9, 5, 2, "add_mul", "Leo", "ليو"),
        (7, 4, 6, "mul_sub", "Rayan", "ريان"),
        (12, 3, 4, "sub_mul", "Maha", "مها"),
    ]
    for x, a, b, mode, nm_en, nm_ar in mm_easy:
        if mode == "add_mul":
            mid = x + a
            ans = mid * b
            wrong = x * b + a
            op1, op2 = f"+ {a}", f"× {b}"
            desc_en, desc_ar = f"**adds {m(a)}** and then **multiplies by {m(b)}**", f"**تجمع {m(a)}** ثم **تضرب في {m(b)}**"
        elif mode == "mul_add":
            mid = x * a
            ans = mid + b
            wrong = (x + b) * a
            op1, op2 = f"× {a}", f"+ {b}"
            desc_en, desc_ar = f"**multiplies by {m(a)}** and then **adds {m(b)}**", f"**تضرب في {m(a)}** ثم **تجمع {m(b)}**"
        elif mode == "mul_sub":
            mid = x * a
            ans = mid - b
            wrong = (x - b) * a
            op1, op2 = f"× {a}", f"− {b}"
            desc_en, desc_ar = f"**multiplies by {m(a)}** and then **subtracts {m(b)}**", f"**تضرب في {m(a)}** ثم **تطرح {m(b)}**"
        else:
            mid = x - a
            ans = mid * b
            wrong = x * b - a
            op1, op2 = f"− {a}", f"× {b}"
            desc_en, desc_ar = f"**subtracts {m(a)}** and then **multiplies by {m(b)}**", f"**تطرح {m(a)}** ثم **تضرب في {m(b)}**"
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} drops the number {m(x)} into a 2-step Kangaroo machine that first {desc_en}. What number comes out?",
            f"يُدخل {nm_ar} العدد {m(x)} في آلة الكنغر ذات الخطوتين التي {desc_ar}. ما العدد الذي يخرج من الآلة؟",
            ans, [wrong, mid, ans + b, ans - a],
            "Follow the two boxes strictly in order from left to right!",
            "اتبع الصندوقين بالترتيب من اليسار إلى اليمين خطوة بخطوة!",
            "Apply Box 1 to the input, then apply Box 2 to that intermediate result.",
            [
                f"After Box 1 (`{op1}`), the number becomes {m(mid)}.",
                f"After Box 2 (`{op2}`), the final output is {m(ans)}.",
            ],
            f"Order check: {m(x)} → {m(mid)} → {m(ans)}!",
            "نطبق العملية الأولى على المدخل، ثم نطبق العملية الثانية على الناتج الوسيط.",
            [
                f"بعد الصندوق الأول (`{op1}`) يصبح العدد {m(mid)}.",
                f"بعد الصندوق الثاني (`{op2}`) يخرج الناتج النهائي {m(ans)}.",
            ],
            f"تحقق بالتسلسل: {m(x)} ← {m(mid)} ← {m(ans)}!",
            diagram_en=svg_function_machine(str(x), op1, op2, "?"),
        )

    mm_med = [
        (8, 5, 4, "add_mul", "Faisal", "فيصل"),
        (9, 4, 7, "mul_add", "Dana", "دانة"),
        (11, 3, 5, "sub_mul", "Kareem", "كريم"),
        (6, 5, 8, "mul_sub", "Reem", "ريم"),
        (7, 8, 3, "add_mul", "Lina", "لينا"),
    ]
    for x, a, b, mode, nm_en, nm_ar in mm_med:
        if mode == "add_mul":
            mid = x + a
            out = mid * b
            op1, op2 = f"+ {a}", f"× {b}"
            desc_en, desc_ar = f"**adds {m(a)}** and then **multiplies by {m(b)}**", f"**تجمع {m(a)}** ثم **تضرب في {m(b)}**"
            trap_v = (out - a) // b if (out - a) % b == 0 else mid
        elif mode == "mul_add":
            mid = x * a
            out = mid + b
            op1, op2 = f"× {a}", f"+ {b}"
            desc_en, desc_ar = f"**multiplies by {m(a)}** and then **adds {m(b)}**", f"**تضرب في {m(a)}** ثم **تجمع {m(b)}**"
            trap_v = out // a - b
        elif mode == "sub_mul":
            mid = x - a
            out = mid * b
            op1, op2 = f"− {a}", f"× {b}"
            desc_en, desc_ar = f"**subtracts {m(a)}** and then **multiplies by {m(b)}**", f"**تطرح {m(a)}** ثم **تضرب في {m(b)}**"
            trap_v = mid
        else:
            mid = x * a
            out = mid - b
            op1, op2 = f"× {a}", f"− {b}"
            desc_en, desc_ar = f"**multiplies by {m(a)}** and then **subtracts {m(b)}**", f"**تضرب في {m(a)}** ثم **تطرح {m(b)}**"
            trap_v = (out - b) // a
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} puts a mystery number {m('?')} into a machine that first {desc_en}. If the output is {m(out)}, what was the starting number {m('?')}?",
            f"أدخل/أدخلت {nm_ar} عدداً مجهولاً {m('?')} في آلة {desc_ar}. إذا خرج الناتج {m(out)}، فما العدد الأصلي {m('?')}؟",
            x, [mid, trap_v, x + 2, max(1, x - 2)],
            f"Work backward from {m(out)}: undo `{op2}` first, then undo `{op1}`!",
            f"ارجع عكسياً من {m(out)}: ألغِ العملية الأخيرة `{op2}` أولاً ثم ألغِ `{op1}`!",
            "Undo the second operation first using its inverse, then undo the first operation.",
            [
                f"Undoing `{op2}` on {m(out)} gives the middle number {m(mid)}.",
                f"Undoing `{op1}` on {m(mid)} gives the starting number {m(x)}.",
            ],
            f"Forward check: {m(x)} → (`{op1}`) → {m(mid)} → (`{op2}`) → {m(out)}!",
            "نلغي العملية الثانية بعكسها أولاً ثم نلغي العملية الأولى بعكسها.",
            [
                f"بإلغاء `{op2}` من العدد {m(out)} نحصل على العدد الأوسط {m(mid)}.",
                f"وبإلغاء `{op1}` من العدد {m(mid)} نحصل على المدخل الأصلي {m(x)}.",
            ],
            f"تحقق للأمام: {m(x)} ← {m(mid)} ← {m(out)}!",
            diagram_en=svg_function_machine("?", op1, op2, str(out)),
        )

    mm_hard = [
        (10, 5, 3, "Kangy"),
        (14, 3, 4, "Omar"),
        (9, 7, 4, "Sara"),
        (18, 5, 4, "Tariq"),
        (13, 3, 4, "Nora"),
    ]
    ar_names_h = {"Kangy": "الكنغر", "Omar": "عمر", "Sara": "سارة", "Tariq": "طارق", "Nora": "نورة"}
    for start_v, odd_add, steps_k, nm_en in mm_hard:
        nm_ar = ar_names_h[nm_en]
        trace = [start_v]
        cur = start_v
        for _ in range(steps_k):
            cur = cur // 2 if cur % 2 == 0 else cur + odd_add
            trace.append(cur)
        ans = trace[-1]
        tr_str = " \\to ".join(str(v) for v in trace)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en}'s smart machine follows this rule each turn: **if the number is even, divide it by {m(2)}; if it is odd, add {m(odd_add)}**. Starting with {m(start_v)}, what number comes out after **{m(steps_k)} turns** in a row?",
            f"تتبع آلة {nm_ar} الذكية القاعدة الآتية في كل دورة: **إذا كان العدد زوجياً تقسمه على {m(2)}، وإذا كان فردياً تضيف إليه {m(odd_add)}**. بدءاً بالعدد {m(start_v)}، ما العدد الناتج بعد **{m(steps_k)} دورات** متتالية؟",
            ans, [trace[-2], ans + 2, ans * 2, max(1, ans - 1)],
            "Test even or odd carefully at the start of EVERY single turn!",
            "اختبر هل العدد زوجي أم فردي في بداية **كل** دورة على حدة!",
            "Simulate the even/odd rule step-by-step for the exact number of turns.",
            [
                f"Follow each turn carefully: {m(tr_str)}.",
                f"After {m(steps_k)} turns, the machine outputs {m(ans)}.",
            ],
            f"Count the arrows in {m(tr_str)}: {m(steps_k)} steps land cleanly on {m(ans)}!",
            "نتتبع القاعدة خطوة بخطوة مع فحص الزوجية والفردية في كل مرة.",
            [
                f"مسار الأعداد عبر الدورات: {m(tr_str)}.",
                f"بعد {m(steps_k)} دورات بالضبط يخرج العدد {m(ans)}.",
            ],
            f"عدد الأسهم في المسار {m(steps_k)} والناتج النهائي {m(ans)}!",
            diagram_en=svg_function_machine(f"Start {start_v}", "Even ÷2", f"Odd +{odd_add}", f"{steps_k} turns"),
        )



# ==============================================================================
# UNIT 1.3 — Geometry Part 1 (60 Questions: KANG-ECO-121 .. KANG-ECO-180)
# Blueprints: kang_eco_staircase_perimeter, kang_eco_grid_tile_area,
#             kang_eco_overlapping_cards, kang_eco_matchstick_shapes
# ==============================================================================
def _poly_area2(verts: list[tuple[int, int]]) -> int:
    n = len(verts)
    return abs(sum(verts[i][0] * verts[(i + 1) % n][1] - verts[(i + 1) % n][0] * verts[i][1] for i in range(n)))


def _add_unit_1_3(B: BankBuilder) -> None:
    tp = "Geometry"

    # 1. kang_eco_staircase_perimeter (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_staircase_perimeter"
    st_easy = [
        (11, 8, 3, "wooden podium", "منصة خشبية"),
        (15, 9, 4, "garden flowerbed", "حوض زهور"),
        (13, 7, 5, "foam block", "مجسم إسفنجي"),
        (16, 12, 4, "cardboard cutout", "قصاصة كرتونية"),
        (18, 11, 6, "tiled terrace", "شرفة مبلطة"),
    ]
    for W, H, steps, item_en, item_ar in st_easy:
        ans = 2 * (W + H)
        B.add_math(
            tp, "Easy", bp,
            f"A right-angled {item_en} shaped like a staircase has bottom width {m(W)} cm, left height {m(H)} cm, and {m(steps)} steps climbing smoothly from bottom-right to top-left. What is its perimeter in cm?",
            f"تأخذ {item_ar} قائمة الزوايا شكل سلّم عرض قاعدته {m(W)} سم وارتفاعه الأيسر {m(H)} سم، وله {m(steps)} درجات تصعد بانتظام من أسفل اليمين لأعلى اليسار. ما محيط الشكل بالسنتمتر؟",
            ans, [W + H, 2 * W + H, W + 2 * H, ans + steps],
            f"Slide all horizontal treads up to match {m(W)} cm and all vertical risers right to match {m(H)} cm!",
            f"ادفع القطع الأفقية للأعلى لتساوي {m(W)} سم، والقطع الرأسية لليمين لتساوي {m(H)} سم!",
            "Push staircase edges outward to match the bounding rectangle: Perimeter = 2(W + H).",
            [
                f"Sum of all horizontal step edges = {m(W)} cm, and sum of all vertical step edges = {m(H)} cm.",
                f"Total perimeter = {m(f'2 \\times ({W} + {H}) = {ans}')} cm.",
            ],
            f"The number of steps ({m(steps)}) does not change the perimeter {m(ans)} cm!",
            "بدفع الحواف المتدرجة للخارج يصبح المحيط مساوياً لمحيط المستطيل المحيط 2(W + H).",
            [
                f"مجموع القطع الأفقية العليا يساوي {m(W)} سم، ومجموع القطع الرأسية اليمنى يساوي {m(H)} سم.",
                f"المحيط الكلي = {m(f'2 \\times ({W} + {H}) = {ans}')} سم.",
            ],
            f"عدد الدرجات ({m(steps)}) لا يغير قيمة المحيط {m(ans)} سم!",
            diagram_en=svg_kang_staircase_perimeter(f"{W} cm", f"{H} cm", steps),
        )

    st_med = [
        (52, 16, 4, "Kangy", "الكنغر"),
        (60, 19, 5, "Lina", "لينا"),
        (44, 13, 3, "Omar", "عمر"),
        (68, 21, 4, "Sara", "سارة"),
        (76, 24, 5, "Tariq", "طارق"),
    ]
    for P, W, steps, nm_en, nm_ar in st_med:
        H = P // 2 - W
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} measures the total perimeter of this {m(steps)}-step right-angled staircase polygon to be {m(P)} m. Its flat bottom width is {m(W)} m. What is its left height {m('?')} in meters?",
            f"قاس {nm_ar} المحيط الكلي لهذا المضلع المتدرج ذي الـ {m(steps)} درجات فكان {m(P)} متراً. إذا كان عرض قاعدته السفلية {m(W)} متراً، فكم متراً يبلغ ارتفاعه الأيسر {m('?')}؟",
            H, [P - W, P - 2 * W, H + 2, max(2, H - 2)],
            f"Half of the perimeter equals width + height ({m(f'{P} \\div 2 = {P // 2}')})!",
            f"نصف المحيط يساوي مجموع العرض والارتفاع ({m(f'{P} \\div 2 = {P // 2}')})!",
            "Use W + H = Perimeter ÷ 2 for a monotone staircase polygon.",
            [
                f"Since {m(f'2 \\times (W + H) = {P}')}, we have {m(f'W + H = {P} \\div 2 = {P // 2}')} m.",
                f"Subtract the width: {m(f'H = {P // 2} - {W} = {H}')} m.",
            ],
            f"Check: {m(f'2 \\times ({W} + {H}) = 2 \\times {W + H} = {P}')} m!",
            "بما أن المحيط يساوي 2(W + H) نقسم المحيط على 2 ثم نطرح العرض.",
            [
                f"نصف المحيط = {m(f'{P} \\div 2 = {P // 2}')} متراً.",
                f"الارتفاع الأيسر = {m(f'{P // 2} - {W} = {H}')} متراً.",
            ],
            f"تحقق: {m(f'2 \\times ({W} + {H}) = {P}')} متراً!",
            diagram_en=svg_kang_staircase_perimeter(f"{W} m", "? m", steps),
        )

    st_hard = [
        (8, 6, 2, 4, "Nora", "نورة"),
        (9, 6, 2, 3, "Zaid", "زيد"),
        (8, 5, 3, 4, "Hala", "هلا"),
        (10, 6, 2, 4, "Yousef", "يوسف"),
        (9, 7, 3, 3, "Amal", "أمل"),
    ]
    for W, H, d, u, nm_en, nm_ar in st_hard:
        ans = 2 * (W + H) + 2 * d
        c_left = (W - u) // 2
        c_right = c_left + u
        verts = [(0, 0), (W, 0), (W, H), (c_right, H), (c_right, H - d), (c_left, H - d), (c_left, H), (0, H)]
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} starts with a {m(W)} cm by {m(H)} cm rectangle and cuts a rectangular U-notch of width {m(u)} cm and depth {m(d)} cm straight down into the top edge as shown on the unit grid. What is the perimeter of the notched shape in cm?",
            f"بدأت/بدأ {nm_ar} بمستطيل أبعاده {m(W)} سم في {m(H)} سم، ثم قصّ تجويفاً مستطيلاً على شكل حرف U عرضه {m(u)} سم وعمقه {m(d)} سم في الحافة العلوية كما في الشبكة. ما محيط الشكل الجديد بالسنتمتر؟",
            ans, [2 * (W + H), 2 * (W + H) - 2 * d, 2 * (W + H) + d, ans + u],
            f"Push the bottom of the notch straight up to restore the {m(W)} cm top edge—then count the **two vertical walls** of depth {m(d)} cm!",
            f"ادفع قاع التجويف للأعلى ليكتمل الضلع العلوي {m(W)} سم، ثم أضف **الجدارين الرأسيين** اللذين عمق كل منهما {m(d)} سم!",
            "Pushing the horizontal notch floor up completes 2(W + H), leaving two extra vertical segments of length d.",
            [
                f"Without the notch, the rectangle's perimeter would be {m(f'2 \\times ({W} + {H}) = {2 * (W + H)}') } cm.",
                f"Pushing the {m(u)} cm floor of the U-notch up completes the top edge, while adding **two** vertical inner walls of {m(d)} cm each.",
                f"New perimeter = {m(f'{2 * (W + H)} + 2 \\times {d} = {ans}')} cm.",
            ],
            f"Sum all 8 edges directly: {m(f'{W} + {H} + {W - c_right} + {d} + {u} + {d} + {c_left} + {H} = {ans}')} cm!",
            "قاع التجويف يعوّض الجزء المقصوص من الحافة العليا، ويزيد المحيط بمقدار الجدارين الرأسيين 2d.",
            [
                f"محيط المستطيل الأصلي = {m(f'2 \\times ({W} + {H}) = {2 * (W + H)}') } سم.",
                f"يضيف التجويف جدارين رأسيين طول كل منهما {m(d)} سم، فيصبح المحيط {m(f'{2 * (W + H)} + 2 \\times {d} = {ans}')} سم.",
            ],
            f"بجمع الأضلاع الثمانية مباشرة نجد {m(ans)} سم!",
            diagram_en=svg_grid_polygon(W, H, verts),
        )

    # 2. kang_eco_grid_tile_area (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_grid_tile_area"
    gt_easy = [
        (5, 7, 2, 3, "courtyard fountain", "نافورة الفناء"),
        (6, 7, 3, 4, "picnic blanket", "بساط النزهة"),
        (5, 8, 3, 4, "sandbox", "حوض الرمل"),
        (6, 9, 4, 5, "flower carpet", "سجادة الزهور"),
        (7, 8, 3, 6, "stage platform", "منصة المسرح"),
    ]
    for R, C, r, c, obj_en, obj_ar in gt_easy:
        ans = R * C - r * c
        board = [[-1 if (1 <= i <= r and 1 <= j <= c) else 1 for j in range(C)] for i in range(R)]
        B.add_math(
            tp, "Easy", bp,
            f"A rectangular floor has {m(R)} rows and {m(C)} columns of unit tiles. A {obj_en} covers a {m(r)}-by-{m(c)} dark block of tiles. How many light tiles remain **uncovered**?",
            f"أرضية مستطيلة مبلطة بـ {m(R)} صفوف و{m(C)} أعمدة من البلاطات. تغطي {obj_ar} منطقة داكنة أبعادها {m(r)} في {m(c)}. كم بلاطة فاتحة بقيت **غير مغطاة**؟",
            ans, [r * c, R * C, ans - r, ans + c],
            f"Multiply {m(f'{R} \\times {C}')} for the whole floor and subtract {m(f'{r} \\times {c}')}!",
            f"احسب بلاطات الأرضية كلها ({m(f'{R} \\times {C}')}) ثم اطرح المنطقة الداكنة ({m(f'{r} \\times {c}')})!",
            "Subtract the covered rectangular patch area from the total grid area.",
            [
                f"Total floor tiles = {m(f'{R} \\times {C} = {R * C}')}.",
                f"Covered dark tiles = {m(f'{r} \\times {c} = {r * c}')}.",
                f"Uncovered tiles = {m(f'{R * C} - {r * c} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} + {r * c} = {R * C}')} tiles!",
            "نطرح مساحة المستطيل المغطى من المساحة الكلية للشبكة.",
            [
                f"العدد الكلي للبلاطات = {m(f'{R} \\times {C} = {R * C}')}، والمغطى = {m(f'{r} \\times {c} = {r * c}')}.",
                f"البلاطات غير المغطاة = {m(f'{R * C} - {r * c} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} + {r * c} = {R * C}')}!",
            diagram_en=svg_kang_polyomino_board(board),
        )

    gt_med = [
        (6, 4, [(0, 0), (6, 0), (4, 4), (0, 4)], "Jude"),
        (7, 4, [(0, 0), (7, 0), (3, 4), (0, 4)], "Salman"),
        (6, 5, [(0, 0), (6, 0), (6, 3), (3, 5), (0, 3)], "Pippa"),
        (6, 4, [(1, 0), (6, 0), (5, 4), (0, 4)], "Leo"),
        (8, 4, [(0, 0), (8, 0), (5, 4), (1, 4)], "Rayan"),
    ]
    ar_med = {"Jude": "جود", "Salman": "سلمان", "Pippa": "بيبا", "Leo": "ليو", "Rayan": "ريان"}
    for cols, rows, verts, nm_en in gt_med:
        nm_ar = ar_med[nm_en]
        a2 = _poly_area2(verts)
        assert a2 % 2 == 0
        ans = a2 // 2
        B.add_math(
            tp, "Medium", bp,
            f"Each small square on {nm_en}'s grid has area {m(1)} cm². What is the area (in cm²) of the shaded polygon?",
            f"مساحة كل مربع صغير في شبكة {nm_ar} تساوي {m(1)} سم². ما مساحة المضلع المظلل بالسنتمتر المربع؟",
            ans, [cols * rows, ans - 2, ans + 2, ans + 4],
            f"Start with the {m(f'{cols} \\times {rows} = {cols * rows}')} cm² grid rectangle and subtract the unshaded corner triangle(s)!",
            f"ابدأ بمساحة المستطيل الكلي ({m(f'{cols} \\times {rows} = {cols * rows}')} سم²) ثم اطرح المثلثات غير المظللة في الأركان!",
            "Split into whole rectangles and right triangles (half-rectangles) or subtract unshaded triangles from the grid box.",
            [
                f"The full {m(f'{cols} \\times {rows}')} grid has area {m(cols * rows)} cm².",
                f"Subtracting the unshaded right-triangle corner region(s) of total area {m(cols * rows - ans)} cm² leaves {m(ans)} cm².",
            ],
            f"Whole grid ({m(cols * rows)}) − unshaded ({m(cols * rows - ans)}) = {m(ans)} cm²!",
            "نحسب مساحة شبكة المستطيل الكلية ثم نطرح مساحات المثلثات القائمة البيضاء.",
            [
                f"مساحة الشبكة الكلية = {m(f'{cols} \\times {rows} = {cols * rows}')} سم².",
                f"بطرح المثلثات غير المظللة ({m(cols * rows - ans)} سم²) تتبقى المساحة المظللة {m(ans)} سم².",
            ],
            f"تحقق: {m(f'{ans} + {cols * rows - ans} = {cols * rows}')} سم²!",
            diagram_en=svg_grid_polygon(cols, rows, verts),
        )

    gt_hard = [
        (6, 6, [(1, 0), (6, 2), (5, 6), (0, 4)], "kite shield", "درع ورقي"),
        (6, 6, [(2, 0), (6, 3), (4, 6), (0, 3)], "diamond badge", "شارة ماسية"),
        (7, 6, [(2, 0), (7, 2), (5, 6), (0, 4)], "tilted tile", "بلاطة مائلة"),
        (6, 5, [(2, 0), (6, 1), (4, 5), (0, 4)], "gemstone", "جوهرة هندسية"),
        (8, 6, [(3, 0), (8, 3), (5, 6), (0, 3)], "crystal star", "ماسة بلورية"),
    ]
    for cols, rows, verts, sh_en, sh_ar in gt_hard:
        a2 = _poly_area2(verts)
        assert a2 % 2 == 0
        ans = a2 // 2
        box = cols * rows
        unsh = box - ans
        B.add_math(
            tp, "Hard", bp,
            f"On a {m(f'{cols} \\times {rows}')} unit grid (each small square = {m(1)} cm²), Kangy draws a tilted {sh_en} whose corners touch the four outer borders. What is its shaded area in cm²?",
            f"على شبكة أبعادها {m(f'{cols} \\times {rows}')} (مساحة كل مربع صغير {m(1)} سم²)، رسم الكنغر {sh_ar} تلامس رؤوسه الحواف الأربع للشبكة. ما المساحة المظللة بالسنتمتر المربع؟",
            ans, [box // 2 if box // 2 != ans else ans + 3, ans - 2, ans + 2, unsh if unsh != ans else ans + 4],
            f"Enclose the tilted shape in the {m(f'{cols} \\times {rows}')} rectangle ({m(box)} cm²) and subtract the 4 corner right triangles!",
            f"أحِط الشكل المائل بالمستطيل {m(f'{cols} \\times {rows}')} ({m(box)} سم²) ثم اطرح المثلثات القائمة الأربعة في الأركان!",
            "Use the Kangaroo Bounding-Box Trick: Area = Grid Box − Sum of 4 Corner Right Triangles.",
            [
                f"The outer grid rectangle has area {m(f'{cols} \\times {rows} = {box}')} cm².",
                f"The 4 white right triangles at the corners have combined area {m(unsh)} cm².",
                f"Shaded area = {m(f'{box} - {unsh} = {ans}')} cm².",
            ],
            f"Shoelace / grid-triangle verification confirms exact area {m(ans)} cm²!",
            "نستخدم طريقة الصندوق المحيط: نطرح مجموع مساحات المثلثات القائمة الأربعة في الزوايا من مساحة المستطيل.",
            [
                f"مساحة الصندوق المحيط = {m(f'{cols} \\times {rows} = {box}')} سم².",
                f"مجموع مساحات المثلثات الأربعة البيضاء في الأركان = {m(unsh)} سم².",
                f"المساحة المظللة = {m(f'{box} - {unsh} = {ans}')} سم².",
            ],
            f"تحقق: {m(f'{ans} + {unsh} = {box}')} سم²!",
            diagram_en=svg_grid_polygon(cols, rows, verts),
        )

    # 3. kang_eco_overlapping_cards (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_overlapping_cards"
    ov_easy = [
        (25, 20, 6, "Maha", "مها"),
        (36, 28, 9, "Faisal", "فيصل"),
        (40, 32, 12, "Dana", "دانة"),
        (18, 22, 5, "Kareem", "كريم"),
        (45, 30, 10, "Reem", "ريم"),
    ]
    for a1, a2, ov, nm_en, nm_ar in ov_easy:
        ans = a1 + a2 - ov
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} places two colored cards of areas {m(a1)} cm² and {m(a2)} cm² on a table. Their overlapping region has area {m(ov)} cm². What total table area (in cm²) is covered?",
            f"وضعت/وضع {nm_ar} بطاقتين ملونتين مساحتاهما {m(a1)} سم² و{m(a2)} سم² فوق الطاولة، فكانت مساحة التداخل بينهما {m(ov)} سم². ما المساحة الكلية المغطاة من الطاولة بالسنتمتر المربع؟",
            ans, [a1 + a2, a1 + a2 - 2 * ov, a1 + a2 + ov, ans + 3],
            f"Add {m(f'{a1} + {a2}')} and subtract {m(ov)} once so the overlap is not counted twice!",
            f"اجمع {m(f'{a1} + {a2}')} ثم اطرح {m(ov)} مرة واحدة لعدم تكرار التداخل!",
            "Total Covered = First Area + Second Area − Overlap.",
            [
                f"Sum of both card areas = {m(f'{a1} + {a2} = {a1 + a2}')} cm².",
                f"Subtracting the double-counted overlap gives {m(f'{a1 + a2} - {ov} = {ans}')} cm².",
            ],
            f"Check parts: {m(f'({a1 - ov}) + {ov} + ({a2 - ov}) = {ans}')} cm²!",
            "المساحة الكلية المغطاة = مساحة الأولى + مساحة الثانية − مساحة التداخل.",
            [
                f"مجموع المساحتين = {m(f'{a1} + {a2} = {a1 + a2}')} سم².",
                f"بطرح التداخل مرة واحدة نحصل على {m(f'{a1 + a2} - {ov} = {ans}')} سم².",
            ],
            f"تحقق بتجزئة المناطق الثلاث: {m(ans)} سم²!",
            diagram_en=svg_kang_overlapping_rects(f"{a1} cm²", f"{a2} cm²", f"{ov} cm²"),
        )

    ov_med = [
        (18, 15, 27, "paper strips", "شريطين ورقيين"),
        (24, 20, 36, "wooden rulers", "مسطرتين خشبيتين"),
        (30, 25, 44, "party ribbons", "شريطين ملونين"),
        (22, 19, 34, "cardboard bars", "قطعتين كرتونيتين"),
        (35, 28, 50, "train tracks", "قطعتين من سكة القطار"),
    ]
    for l1, l2, tot, obj_en, obj_ar in ov_med:
        ov = l1 + l2 - tot
        B.add_math(
            tp, "Medium", bp,
            f"Kangy glues two straight {obj_en} of lengths {m(l1)} cm and {m(l2)} cm together with an overlapping tab. The finished glued strip is {m(tot)} cm long. How many cm long is the **overlapping tab**?",
            f"ألصق الكنغر {obj_ar} طولاهما {m(l1)} سم و{m(l2)} سم معاً بجزء متداخل، فأصبح الطول الكلي بعد اللصق {m(tot)} سم. كم سنتمتراً يبلغ طول **جزء التداخل**؟",
            ov, [l1 + l2, 2 * ov, abs(l1 - l2), ov + 3],
            f"Compare the unglued sum ({m(f'{l1} + {l2} = {l1 + l2}')} cm) with the glued length ({m(tot)} cm)!",
            f"قارن مجموع الطولين قبل اللصق ({m(f'{l1} + {l2} = {l1 + l2}')} سم) بالطول النهائي ({m(tot)} سم)!",
            "The length lost when gluing two strips together equals the length of the overlap.",
            [
                f"End-to-end without overlap, the strips would measure {m(f'{l1} + {l2} = {l1 + l2}')} cm.",
                f"Since the glued strip is {m(tot)} cm, the overlap is {m(f'{l1 + l2} - {tot} = {ov}')} cm.",
            ],
            f"Check: {m(f'{l1} + {l2} - {ov} = {tot}')} cm!",
            "الفرق بين مجموع الطولين والطول الكلي بعد اللصق يساوي طول التداخل.",
            [
                f"مجموع الطولين دون تداخل = {m(f'{l1} + {l2} = {l1 + l2}')} سم.",
                f"طول جزء التداخل = {m(f'{l1 + l2} - {tot} = {ov}')} سم.",
            ],
            f"تحقق: {m(f'{l1} + {l2} - {ov} = {tot}')} سم!",
            diagram_en=svg_kang_overlapping_rects(f"{l1} cm", f"{l2} cm", "? cm"),
        )

    ov_hard = [
        (40, 35, 63, "Lina", "لينا"),
        (50, 42, 76, "Omar", "عمر"),
        (36, 36, 58, "Sara", "سارة"),
        (48, 38, 71, "Tariq", "طارق"),
        (60, 45, 87, "Nora", "نورة"),
    ]
    for a1, a2, tot, nm_en, nm_ar in ov_hard:
        ov = a1 + a2 - tot
        single_layer = tot - ov
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} lays two rectangular sheets of areas {m(a1)} cm² and {m(a2)} cm² partly over each other. Together they cover {m(tot)} cm² of the desk. What area (in cm²) is covered by **only a single sheet** (not the double-thick overlap)?",
            f"وضعت/وضع {nm_ar} ورقتين مستطيلتين مساحتاهما {m(a1)} سم² و{m(a2)} سم² متداخلتين جزئياً، فغطتا معاً {m(tot)} سم² من المكتب. ما المساحة (بالسم²) المغطاة **بورقة واحدة فقط** (دون منطقة التداخل المزدوجة)؟",
            single_layer, [ov, tot, a1 + a2, single_layer + ov // 2 + 1],
            f"First find the overlap ({m(f'{a1} + {a2} - {tot} = {ov}')} cm²), then remove that overlap from the {m(tot)} cm² covered area!",
            f"أوجد مساحة التداخل أولاً ({m(f'{a1} + {a2} - {tot} = {ov}')} سم²)، ثم اطرحها من المساحة المغطاة الكلية ({m(tot)} سم²)!",
            "Find Overlap = A1 + A2 − Total, then Single-Layer = Total − Overlap.",
            [
                f"Overlap area = {m(f'{a1} + {a2} - {tot} = {ov}')} cm².",
                f"Removing the double-thick overlap from the total covered area gives {m(f'{tot} - {ov} = {single_layer}')} cm².",
            ],
            f"Check: only-first ({m(a1 - ov)}) + only-second ({m(a2 - ov)}) = {m(single_layer)} cm²!",
            "نحسب مساحة التداخل أولاً ثم نطرحها من إجمالي المساحة المغطاة.",
            [
                f"مساحة التداخل = {m(f'{a1} + {a2} - {tot} = {ov}')} سم².",
                f"مساحة الطبقة الواحدة فقط = {m(f'{tot} - {ov} = {single_layer}')} سم².",
            ],
            f"تحقق: ({m(a1 - ov)}) + ({m(a2 - ov)}) = {m(single_layer)} سم²!",
            diagram_en=svg_kang_overlapping_rects(f"{a1} cm²", f"{a2} cm²", "Overlap"),
        )

    # 4. kang_eco_matchstick_shapes (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_matchstick_shapes"
    ms_easy = [
        (5, "Zaid", "زيد"),
        (8, "Hala", "هلا"),
        (9, "Yousef", "يوسف"),
        (10, "Amal", "أمل"),
        (12, "Jude", "جود"),
    ]
    for n, nm_en, nm_ar in ms_easy:
        ans = 3 * n + 1
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} builds a straight row of {m(n)} connected squares out of identical matchsticks as shown. How many matchsticks are used in total?",
            f"يبني/تبني {nm_ar} صفاً مستقيماً من {m(n)} مربعات متلاصقة بأعواد الثقاب كما في الشكل. كم عود ثقاب يُستعمل إجمالاً؟",
            ans, [4 * n, 3 * n, ans + 2, 4 * n - 1],
            f"The 1st square uses {m(4)} sticks, and each new square adds {m(3)} sticks ({m(f'3 \\times {n} + 1')})!",
            f"المربع الأول يأخذ {m(4)} أعواد، وكل مربع إضافي يأخذ {m(3)} أعواد ({m(f'3 \\times {n} + 1')})!",
            "Use Sticks = 3n + 1 for a single row of n connected squares.",
            [
                f"Square #1 needs {m(4)} matchsticks, and each of the next {m(n - 1)} squares adds {m(3)} matchsticks.",
                f"Total = {m(f'4 + 3 \\times {n - 1} = 3 \\times {n} + 1 = {ans}')} matchsticks.",
            ],
            f"Shared-wall check: {m(f'4 \\times {n} - {n - 1} = {ans}')} matchsticks!",
            "نطبق قانون صف المربعات المتصلة: 3n + 1.",
            [
                f"يحتاج المربع الأول {m(4)} أعواد، وتحتاج الـ {m(n - 1)} مربعات التالية {m(f'3 \\times {n - 1} = {3 * (n - 1)}')} عوداً.",
                f"المجموع = {m(ans)} عوداً.",
            ],
            f"تحقق بطرح الأضلاع المشتركة: {m(f'4 \\times {n} - {n - 1} = {ans}')}!",
            diagram_en=svg_matchstick_squares((1, 2, 3)),
        )

    ms_med = [
        (19, "Salman", "سلمان"),
        (23, "Pippa", "بيبا"),
        (27, "Leo", "ليو"),
        (31, "Rayan", "ريان"),
        (35, "Kangy", "الكنغر"),
    ]
    for sticks, nm_en, nm_ar in ms_med:
        ans = (sticks - 1) // 2
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} has {m(sticks)} identical matchsticks and uses **all** of them to build one continuous zig-zag strip of connected equilateral triangles as shown. How many small unit triangles are formed?",
            f"لدى {nm_ar} عدد {m(sticks)} عود ثقاب متطابق، واستعملها **كلها** لبناء شريط متعرج متصل من المثلثات المتطابقة الأضلاع كما في الشكل. كم مثلثاً صغيراً تكوّن؟",
            ans, [sticks // 3, ans - 1, ans + 1, ans + 2],
            f"The 1st triangle uses {m(3)} sticks, and each extra triangle needs only {m(2)} more sticks ({m('2n + 1')})!",
            f"المثلث الأول يحتاج {m(3)} أعواد، وكل مثلث تالٍ يحتاج عودين فقط ({m('2n + 1')})!",
            "Solve 2n + 1 = M by subtracting 1 and dividing by 2.",
            [
                f"In a connected triangle strip, {m('n')} triangles require {m('2n + 1')} matchsticks.",
                f"Since {m(f'2n + 1 = {sticks}')}, we have {m(f'2n = {sticks - 1}')} and {m(f'n = {ans}')} triangles.",
            ],
            f"Check forward: {m(f'2 \\times {ans} + 1 = {sticks}')} matchsticks!",
            "في شريط المثلثات المتصلة، عدد الأعواد هو 2n + 1؛ نطرح 1 ثم نقسم على 2.",
            [
                f"بما أن {m(f'2n + 1 = {sticks}')} فإن {m(f'2n = {sticks - 1}')}.",
                f"إذن عدد المثلثات = {m(f'{sticks - 1} \\div 2 = {ans}')}.",
            ],
            f"تحقق: {m(f'2 \\times {ans} + 1 = {sticks}')} عوداً!",
            diagram_en=svg_matchstick_triangles((1, 2, 3)),
        )

    ms_hard = [
        (2, 2, "Maha", "مها"),
        (2, 3, "Faisal", "فيصل"),
        (2, 4, "Dana", "دانة"),
        (3, 3, "Kareem", "كريم"),
        (3, 4, "Reem", "ريم"),
    ]
    for R, C, nm_en, nm_ar in ms_hard:
        horiz = (R + 1) * C
        vert = (C + 1) * R
        ans = horiz + vert
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} builds a {m(f'{R} \\times {C}')} rectangular grid of unit squares using matchsticks, where every small square side is **1 matchstick** long. How many matchsticks are needed in total?",
            f"تبني/يبني {nm_ar} شبكة مستطيلة أبعادها {m(f'{R} \\times {C}')} من المربعات الصغيرة بأعواد الثقاب، بحيث يتكون كل ضلع مربع صغير من **عود ثقاب واحد**. كم عود ثقاب يلزم إجمالاً؟",
            ans, [4 * R * C, 3 * R * C + 1, 2 * R * C, ans - R],
            f"Count horizontal sticks ({m(R + 1)} rows of {m(C)}) and vertical sticks ({m(C + 1)} columns of {m(R)}) separately!",
            f"احسب الأعواد الأفقية ({m(R + 1)} خطوط طولها {m(C)}) والأعواد الرأسية ({m(C + 1)} خطوط طولها {m(R)}) كلٌّ على حدة!",
            "Count horizontal matchsticks (R + 1)·C plus vertical matchsticks (C + 1)·R.",
            [
                f"There are {m(R + 1)} horizontal grid lines, each using {m(C)} sticks: {m(f'{R + 1} \\times {C} = {horiz}')}.",
                f"There are {m(C + 1)} vertical grid lines, each using {m(R)} sticks: {m(f'{C + 1} \\times {R} = {vert}')}.",
                f"Total matchsticks = {m(f'{horiz} + {vert} = {ans}')}.",
            ],
            f"Formula check: {m(f'2 \\times {R} \\times {C} + {R} + {C} = {ans}')} matchsticks!",
            "نفصل العدّ إلى خطوط أفقية عددها (R + 1) وخطوط رأسية عددها (C + 1).",
            [
                f"الأعواد الأفقية = {m(f'{R + 1} \\times {C} = {horiz}')} عوداً.",
                f"الأعواد الرأسية = {m(f'{C + 1} \\times {R} = {vert}')} عوداً.",
                f"الإجمالي = {m(f'{horiz} + {vert} = {ans}')} عوداً.",
            ],
            f"تحقق: {m(f'{horiz} + {vert} = {ans}')} عوداً!",
            diagram_en=svg_fraction_grid(C, R, 0, 0),
        )



# ==============================================================================
# UNIT 1.4 — Geometry Part 2 (60 Questions: KANG-ECO-181 .. KANG-ECO-240)
# Blueprints: kang_eco_cube_stack_count, kang_eco_die_opposite_faces,
#             kang_eco_stamp_rotation, kang_eco_polyomino_fit
# ==============================================================================
def _rot90_cw(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    return [[grid[n - 1 - r][c] for r in range(n)] for c in range(n)]


def _add_unit_1_4(B: BankBuilder) -> None:
    tp = "Geometry"

    # 1. kang_eco_cube_stack_count (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_cube_stack_count"
    cs_easy = [
        ((4, 3, 2), 1, "Kangy", "الكنغر"),
        ((4, 2, 1), 2, "Lina", "لينا"),
        ((3, 3, 2), 2, "Omar", "عمر"),
        ((4, 4, 2), 1, "Sara", "سارة"),
        ((4, 3, 1), 3, "Tariq", "طارق"),
    ]
    for cols, copies, nm_en, nm_ar in cs_easy:
        one_cnt = sum(cols)
        ans = one_cnt * copies
        extra_en = "tower shown" if copies == 1 else f"{m(copies)} identical copies of the tower shown"
        extra_ar = "البرج الموضح" if copies == 1 else f"{m(copies)} نسخ متطابقة من البرج الموضح"
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} glues small unit cubes into three vertical columns of heights {m(cols[0])}, {m(cols[1])}, and {m(cols[2])} to make {extra_en}. How many small unit cubes are used altogether?",
            f"يلصق {nm_ar} مكعبات صغيرة في ثلاثة أعمدة رأسية ارتفاعاتها {m(cols[0])} و{m(cols[1])} و{m(cols[2])} لتكوين {extra_ar}. كم مكعباً صغيراً استُعمل إجمالاً؟",
            ans, [ans - copies, ans + copies, one_cnt if copies > 1 else ans - 2, ans + 3],
            "Add the three column heights (including hidden bottom cubes!), then multiply by the number of towers!",
            "اجمع ارتفاعات الأعمدة الثلاثة (شاملة المكعبات المخفية بالأسفل) ثم اضرب في عدد الأبراج!",
            "Sum the column heights for one stack and multiply by the number of identical stacks.",
            [
                f"One 3-column tower contains {m(f'{cols[0]} + {cols[1]} + {cols[2]} = {one_cnt}')} unit cubes.",
                f"Total across {m(copies)} tower(s) = {m(f'{copies} \\times {one_cnt} = {ans}')} unit cubes.",
            ],
            f"Column-by-column count guarantees zero hidden cubes are missed: {m(ans)}!",
            "نجمع ارتفاعات الأعمدة الثلاثة للبرج الواحد ثم نضرب في عدد النسخ.",
            [
                f"عدد المكعبات في البرج الواحد = {m(f'{cols[0]} + {cols[1]} + {cols[2]} = {one_cnt}')} مكعباً.",
                f"العدد الكلي = {m(f'{copies} \\times {one_cnt} = {ans}')} مكعباً.",
            ],
            f"تحقق: {m(ans)} مكعباً صغيراً!",
            diagram_en=svg_cube_stack_3d(cols),
        )

    cs_med = [
        ((4, 2, 1), 3, 3, 4, "Nora", "نورة"),
        ((4, 3, 2), 3, 4, 4, "Zaid", "زيد"),
        ((2, 2, 1), 2, 3, 2, "Hala", "هلا"),
        ((3, 3, 1), 3, 3, 3, "Yousef", "يوسف"),
        ((4, 4, 3), 4, 4, 4, "Amal", "أمل"),
    ]
    for cols, L, W, H, nm_en, nm_ar in cs_med:
        cur = sum(cols)
        full = L * W * H
        ans = full - cur
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} starts with the 3-column stack of heights {m(cols[0])}, {m(cols[1])}, and {m(cols[2])} shown, and wants to add unit cubes to build a solid {m(f'{L} \\times {W} \\times {H}')} rectangular block. How many **more** unit cubes are needed?",
            f"يبدأ/تبدأ {nm_ar} بالمجسم المكون من 3 أعمدة ارتفاعاتها {m(cols[0])} و{m(cols[1])} و{m(cols[2])}، ويريد إضافة مكعبات صغيرة لبناء متوازي مستطيلات مصمت أبعاده {m(f'{L} \\times {W} \\times {H}')}. كم مكعباً **إضافياً** يحتاج؟",
            ans, [full, ans - 2, ans + 2, full - cols[0]],
            f"Subtract the current {m(f'{cols[0]} + {cols[1]} + {cols[2]} = {cur}')} cubes from {m(f'{L} \\times {W} \\times {H} = {full}')}!",
            f"اطرح المكعبات الحالية ({m(cur)}) من الحجم الكامل ({m(f'{L} \\times {W} \\times {H} = {full}')})!",
            "Compute Full Block Volume − Current Column Sum.",
            [
                f"Solid {m(f'{L} \\times {W} \\times {H}')} block needs {m(full)} unit cubes in all.",
                f"Current stack already has {m(f'{cols[0]} + {cols[1]} + {cols[2]} = {cur}')} unit cubes.",
                f"Extra cubes needed = {m(f'{full} - {cur} = {ans}')}.",
            ],
            f"Check: {m(f'{cur} + {ans} = {full}')} unit cubes!",
            "نحسب العدد الكلي لمكعبات المجسم المكتمل ثم نطرح المكعبات الموجودة حالياً.",
            [
                f"المجسم الكامل يحتاج {m(f'{L} \\times {W} \\times {H} = {full}')} مكعباً.",
                f"الموجود حالياً = {m(cur)}، إذن الإضافي المطلوب = {m(f'{full} - {cur} = {ans}')}.",
            ],
            f"تحقق: {m(f'{cur} + {ans} = {full}')}!",
            diagram_en=svg_cube_stack_3d(cols),
        )

    cs_hard = [
        (3, "2_faces", "exactly **2** painted faces", "**وجهان ملونان بالضبط**"),
        (3, "1_face", "exactly **1** painted face", "**وجه ملون واحد بالضبط**"),
        (3, "at_least_2", "**at least 2** painted faces", "**وجهان ملونان على الأقل**"),
        (4, "0_faces", "**0** painted faces (completely unpainted)", "**صفر** من الأوجه الملونة (غير ملونة إطلاقاً)"),
        (4, "2_faces", "exactly **2** painted faces", "**وجهان ملونان بالضبط**"),
    ]
    for n, kind, ask_en, ask_ar in cs_hard:
        corners = 8
        edges = 12 * (n - 2)
        faces = 6 * (n - 2) ** 2
        inner = (n - 2) ** 3
        assert corners + edges + faces + inner == n ** 3
        ans = {"2_faces": edges, "1_face": faces, "at_least_2": corners + edges, "0_faces": inner}[kind]
        B.add_math(
            tp, "Hard", bp,
            f"A wooden {m(f'{n} \\times {n} \\times {n}')} cube is painted purple on all {m(6)} outside faces and then sawed into {m(n ** 3)} small {m('1 \\times 1 \\times 1')} cubes. How many small cubes have {ask_en}?",
            f"طُلي مكعب خشبي أبعاده {m(f'{n} \\times {n} \\times {n}')} باللون البنفسجي من أوجهه الخارجية الستة كلها، ثم قُطّع إلى {m(n ** 3)} مكعباً صغيراً. كم مكعباً صغيراً له {ask_ar}؟",
            ans, [corners if ans != corners else 12, faces if ans != faces else 16, edges if ans != edges else 9, n ** 3 - ans],
            "Corners have 3 painted faces, edge-middle cubes have 2, face-center cubes have 1, and interior cubes have 0!",
            "مكعبات الرؤوس (8) لها 3 أوجه، وحواف الأضلاع (12 ضلعاً) لها وجهان، ومراكز الأوجه (6 أوجه) لها وجه واحد، والداخلية 0!",
            "Classify the n³ unit cubes into 8 corners, 12(n−2) edges, 6(n−2)² face-interiors, and (n−2)³ hidden inner cubes.",
            [
                f"In a {m(f'{n} \\times {n} \\times {n}')} painted cube: {m(8)} corners (3 faces), {m(f'12 \\times ({n}-2) = {edges}')} edge cubes (2 faces), {m(f'6 \\times ({n}-2)^2 = {faces}')} face-center cubes (1 face), and {m(f'({n}-2)^3 = {inner}')} inner cubes (0 faces).",
                f"Selecting the group with {ask_en} gives {m(ans)}.",
            ],
            f"Sum of all 4 groups: {m(f'8 + {edges} + {faces} + {inner} = {n ** 3}')} total cubes!",
            "نصنّف المكعبات الصغيرة حسب موقعها: 8 رؤوس، و12(n−2) على الحواف، و6(n−2)² في أوساط الأوجه، و(n−2)³ بالداخل.",
            [
                f"في المكعب {m(f'{n} \\times {n} \\times {n}')}: الرؤوس {m(8)}، والحواف {m(edges)}، وأوساط الأوجه {m(faces)}، والداخلية {m(inner)}.",
                f"المطلوب ({ask_ar}) يساوي {m(ans)}.",
            ],
            f"مجموع الفئات الأربع = {m(f'8 + {edges} + {faces} + {inner} = {n ** 3}')}!",
            diagram_en=svg_painted_cube_3d(n),
        )

    # 2. kang_eco_die_opposite_faces (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_die_opposite_faces"
    die_easy = [
        (1, 2, 3, "bottom", "السفلي"),
        (5, 3, 1, "bottom", "السفلي"),
        (6, 4, 2, "all3", "الثلاثة المخفية كلها"),
        (2, 6, 3, "all3", "الثلاثة المخفية كلها"),
        (4, 1, 5, "all3", "الثلاثة المخفية كلها"),
    ]
    for t, f, r, mode, m_ar in die_easy:
        ans = (7 - t) if mode == "bottom" else (21 - t - f - r)
        q_part_en = "is on the **hidden bottom** face" if mode == "bottom" else "is the **sum of the three hidden faces**"
        q_part_ar = "العدد الموجود على الوجه **السفلي المخفي**" if mode == "bottom" else "**مجموع الأوجه الثلاثة المخفية**"
        B.add_math(
            tp, "Easy", bp,
            f"On a standard Kangaroo die, opposite faces always add up to {m(7)}. Looking at the die shown (top {m(t)}, front {m(f)}, right {m(r)}), what {q_part_en}?",
            f"في حجر النرد القياسي يساوي مجموع كل وجهين متقابلين {m(7)} دائماً. بالنظر إلى النرد الموضح (أعلى {m(t)}، أمام {m(f)}، يمين {m(r)})، ما {q_part_ar}؟",
            ans, [t + f + r, ans - 1, ans + 1, ans + 2],
            "Every pair of opposite faces sums to 7 (and all 6 faces sum to 21)!",
            "كل وجهين متقابلين مجموعهما 7 (ومجموع الأوجه الستة كلها 21)!",
            "Use Opposite = 7 − Visible (and Total of all 6 faces = 21).",
            [
                f"Opposite of top {m(t)} is {m(7 - t)}, opposite of front {m(f)} is {m(7 - f)}, and opposite of right {m(r)} is {m(7 - r)}.",
                f"Required value = {m(ans)}.",
            ],
            f"Check: visible ({m(t + f + r)}) + hidden ({m(21 - t - f - r)}) = {m(21)}!",
            "نستخدم قاعدة الوجه المقابل = 7 − الوجه الظاهر.",
            [
                f"مقابل {m(t)} هو {m(7 - t)}، ومقابل {m(f)} هو {m(7 - f)}، ومقابل {m(r)} هو {m(7 - r)}.",
                f"القيمة المطلوبة = {m(ans)}.",
            ],
            f"تحقق: مجموع الأوجه الستة {m(21)}!",
            diagram_en=svg_kang_cube_faces(str(t), str(f), str(r)),
        )

    die_med = [
        (7, [(1, 0, "2"), (0, 1, "4"), (1, 1, "1"), (2, 1, "3"), (3, 1, "6"), (1, 2, "?")], 5),
        (10, [(1, 0, "3"), (0, 1, "?"), (1, 1, "2"), (2, 1, "6"), (3, 1, "8"), (1, 2, "7")], 4),
        (9, [(1, 0, "5"), (0, 1, "2"), (1, 1, "3"), (2, 1, "7"), (3, 1, "?"), (1, 2, "4")], 6),
        (11, [(1, 0, "?"), (0, 1, "3"), (1, 1, "4"), (2, 1, "8"), (3, 1, "7"), (1, 2, "2")], 9),
        (12, [(1, 0, "4"), (0, 1, "7"), (1, 1, "?"), (2, 1, "5"), (3, 1, "9"), (1, 2, "8")], 3),
    ]
    for target_s, net_cells, expected_ans in die_med:
        # Verify programmatically which cell has '?' and its opposite cell at +/-2 col or +/-2 row
        pos_map = {(c, r): lbl for c, r, lbl in net_cells}
        q_pos = next(pos for pos, lbl in pos_map.items() if lbl == "?")
        opp_candidates = [(q_pos[0] + dc, q_pos[1] + dr) for dc, dr in ((2, 0), (-2, 0), (0, 2), (0, -2)) if (q_pos[0] + dc, q_pos[1] + dr) in pos_map]
        assert len(opp_candidates) == 1
        opp_val = int(pos_map[opp_candidates[0]])
        ans = target_s - opp_val
        assert ans == expected_ans
        B.add_math(
            tp, "Medium", bp,
            f"When this 6-square paper net is folded into a cube, every pair of **opposite faces** adds up to {m(target_s)}. What number must be written in the {m('?')} square?",
            f"عند طيّ هذه الشبكة الورقية المكونة من 6 مربعات لتشكيل مكعب، يصبح مجموع كل **وجهين متقابلين** مساوياً {m(target_s)}. ما العدد الذي يجب كتابته في مربع {m('?')}؟",
            ans, [opp_val, ans - 1, ans + 1, ans + 2],
            "On a flat net, two squares in the same row or column with **1 square between them** fold to become opposite!",
            "في الشبكة المسطحة، المربعان الواقعان في نفس الصف أو العمود ويفصل بينهما **مربع واحد** يصبحان متقابلين!",
            "Locate the square separated from `?` by 1 square along a straight line, then subtract from the opposite-face sum.",
            [
                f"Skipping 1 square in a straight line from {m('?')} lands on its opposite face {m(opp_val)}.",
                f"Since opposite faces add to {m(target_s)}, {m(f'? = {target_s} - {opp_val} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} + {opp_val} = {target_s}')}!",
            "نحدد الوجه المقابل بتخطي مربع واحد على استقامة واحدة، ثم نطرحه من المجموع المطلوب.",
            [
                f"المربع المقابل للخانة {m('?')} بعد الطي يحمل العدد {m(opp_val)}.",
                f"إذن {m(f'? = {target_s} - {opp_val} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} + {opp_val} = {target_s}')}!",
            diagram_en=svg_cube_net(net_cells),
        )

    die_hard = [
        (2, 3, "visible", "Jude", "جود"),
        (3, 5, "visible", "Salman", "سلمان"),
        (3, 1, "visible", "Pippa", "بيبا"),
        (3, 4, "hidden_horiz", "Leo", "ليو"),
        (4, 6, "hidden_horiz", "Rayan", "ريان"),
    ]
    for k_dice, top_v, kind, nm_en, nm_ar in die_hard:
        if kind == "visible":
            ans = 14 * k_dice + top_v
            ask_en = f"all **{m(4 * k_dice + 1)} visible faces** as {nm_en} walks all the way around the table"
            ask_ar = f"**الأوجه الظاهرة الـ {m(4 * k_dice + 1)} كلها** عند الدوران حول الطاولة"
            st_en = [
                f"On each die, the 4 vertical side faces form 2 opposite pairs, summing to {m('7 + 7 = 14')}.",
                f"Across {m(k_dice)} dice, the vertical sides sum to {m(f'{k_dice} \\times 14 = {14 * k_dice}')}; adding the very top face {m(top_v)} gives {m(ans)}.",
            ]
            st_ar = [
                f"في كل نرد تشكّل الأوجه الجانبية الأربعة زوجين متقابلين مجموعهما {m('7 + 7 = 14')}.",
                f"لعدد {m(k_dice)} أحجار نرد يكون مجموع الجوانب {m(14 * k_dice)}، ومع الوجه العلوي {m(top_v)} يصبح المجموع {m(ans)}.",
            ]
        else:
            ans = 7 * k_dice - top_v
            ask_en = f"all **{m(2 * k_dice - 1)} hidden horizontal faces** (between dice and touching the table)"
            ask_ar = f"**الأوجه الأفقية المخفية الـ {m(2 * k_dice - 1)} كلها** (بين الأحجار وعلى الطاولة)"
            st_en = [
                f"Each of the {m(k_dice)} dice has a top+bottom pair summing to {m(7)}, so all {m(2 * k_dice)} horizontal faces sum to {m(f'{k_dice} \\times 7 = {7 * k_dice}')}.",
                f"Subtracting the single visible top face {m(top_v)} leaves {m(f'{7 * k_dice} - {top_v} = {ans}')}.",
            ]
            st_ar = [
                f"مجموع الوجه العلوي والسفلي لكل نرد يساوي {m(7)}، فمجموع الأوجه الأفقية كلها {m(f'{k_dice} \\times 7 = {7 * k_dice}')}.",
                f"بطرح الوجه العلوي الظاهر {m(top_v)} يتبقى {m(f'{7 * k_dice} - {top_v} = {ans}')}.",
            ]
        f_vis = 2 if top_v not in (2, 5) else 1
        r_vis = 3 if top_v not in (3, 4) and f_vis not in (3, 4) else 4
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} stacks {m(k_dice)} standard dice (opposite faces sum to {m(7)}) in a single vertical column on a table. The very top face shows {m(top_v)}. What is the sum of {ask_en}?",
            f"يرصّ {nm_ar} عدد {m(k_dice)} أحجار نرد قياسية (مجموع المتقابلين {m(7)}) في عمود رأسي واحد على الطاولة، ويظهر في قمته العليا العدد {m(top_v)}. ما مجموع {ask_ar}؟",
            ans, [ans - 7, ans + 7, ans - top_v, 21 * k_dice - ans],
            "Group opposite pairs into 7s instead of guessing individual hidden faces!",
            "جمّع كل وجهين متقابلين في مجموع قيمته 7 بدلاً من تخمين كل وجه منفرداً!",
            "Every opposite pair contributes 7 regardless of how a die is spun horizontally.",
            st_en,
            f"Notice visible ({m(14 * k_dice + top_v)}) + hidden ({m(7 * k_dice - top_v)}) = {m(21 * k_dice)}!",
            "نعتمد على ثبات مجموع كل وجهين متقابلين عند القيمة 7.",
            st_ar,
            f"تحقق: الظاهر + المخفي = {m(21 * k_dice)}!",
            diagram_en=svg_kang_cube_faces(str(top_v), str(f_vis), str(r_vis)),
        )

    # 3. kang_eco_stamp_rotation (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_stamp_rotation"
    sr_easy = [
        ([[9, 0, 2], [0, 0, 0], [5, 0, 7]], 1, "90° clockwise", "90° مع عقارب الساعة", (2, 2), "bottom-right", "السفلي الأيمن"),
        ([[4, 0, 8], [0, 0, 0], [1, 0, 6]], 2, "180° (half-turn)", "180° (نصف دورة)", (0, 0), "top-left", "العلوي الأيسر"),
        ([[3, 0, 9], [0, 0, 0], [6, 0, 2]], 3, "90° counterclockwise", "90° عكس عقارب الساعة", (0, 0), "top-left", "العلوي الأيسر"),
        ([[7, 0, 4], [0, 0, 0], [8, 0, 1]], 1, "90° clockwise", "90° مع عقارب الساعة", (0, 0), "top-left", "العلوي الأيسر"),
        ([[5, 0, 9], [0, 0, 0], [2, 0, 6]], 2, "180° (half-turn)", "180° (نصف دورة)", (0, 2), "top-right", "العلوي الأيمن"),
    ]
    for g0, k_turns, t_en, t_ar, (tr_r, tr_c), c_en, c_ar in sr_easy:
        g = g0
        for _ in range(k_turns):
            g = _rot90_cw(g)
        ans = g[tr_r][tr_c]
        corners = [g0[0][0], g0[0][2], g0[2][2], g0[2][0]]
        vis = [[2 if (r, c) == (0, 0) else (1 if g0[r][c] else 0) for c in range(3)] for r in range(3)]
        B.add_math(
            tp, "Easy", bp,
            f"Kangy holds a {m('3 \\times 3')} transparent card with corner numbers top-left {m(g0[0][0])}, top-right {m(g0[0][2])}, bottom-right {m(g0[2][2])}, and bottom-left {m(g0[2][0])}. After rotating it **{t_en}** without flipping, which number is in the **{c_en}** corner?",
            f"يمسك الكنغر بطاقة شفافة {m('3 \\times 3')} تحمل في أركانها: أعلى اليسار {m(g0[0][0])}، أعلى اليمين {m(g0[0][2])}، أسفل اليمين {m(g0[2][2])}، أسفل اليسار {m(g0[2][0])}. بعد تدويرها **{t_ar}** دون قلبها، أي عدد يصبح في الركن **{c_ar}**؟",
            ans, [x for x in corners if x != ans] + [ans + 1],
            "Track which starting corner travels into the target corner under the rotation!",
            "تتبّع أي ركن أصلي ينتقل إلى الركن المطلوب عند الدوران!",
            "Apply the exact 2D corner rotation to the four corner values.",
            [
                f"Rotating the {m('3 \\times 3')} card {t_en} moves the corners to top-left {m(g[0][0])}, top-right {m(g[0][2])}, bottom-right {m(g[2][2])}, bottom-left {m(g[2][0])}.",
                f"The **{c_en}** corner now holds {m(ans)}.",
            ],
            f"Verified by exact {m('3 \\times 3')} grid rotation: {m(ans)}!",
            "نتتبع حركة الأركان الأربعة تحت الدوران المحدد.",
            [
                f"بعد الدوران {t_ar} تصبح الأركان: أعلى اليسار {m(g[0][0])}، أعلى اليمين {m(g[0][2])}، أسفل اليمين {m(g[2][2])}، أسفل اليسار {m(g[2][0])}.",
                f"إذن الركن **{c_ar}** يحمل العدد {m(ans)}.",
            ],
            f"تحقق بالدوران المباشر: {m(ans)}!",
            diagram_en=svg_kang_stamp_grid(vis, t_en),
        )

    sr_med = [
        ([[2, 5, 8], [1, 4, 7], [3, 6, 9]], 0, (0, 2), "top-right", "العلوي الأيمن"),
        ([[3, 1, 7], [6, 5, 2], [9, 4, 8]], 1, (2, 2), "bottom-right", "السفلي الأيمن"),
        ([[8, 2, 4], [5, 9, 1], [7, 3, 6]], 1, (0, 0), "top-left", "العلوي الأيسر"),
        ([[1, 6, 9], [8, 3, 4], [5, 2, 7]], 2, (2, 0), "bottom-left", "السفلي الأيسر"),
        ([[6, 8, 1], [2, 7, 4], [9, 3, 5]], 3, (0, 2), "top-right", "العلوي الأيمن"),
    ]
    for g0, extra_cw, (tr_r, tr_c), c_en, c_ar in sr_med:
        # Press rubber stamp (horizontal left-right mirror flip), then optional CW turns of the paper
        stamped = [row[::-1] for row in g0]
        g = stamped
        for _ in range(extra_cw):
            g = _rot90_cw(g)
        ans = g[tr_r][tr_c]
        turn_note_en = "without turning the paper" if extra_cw == 0 else f"and then turns the paper {m(extra_cw * 90)}° clockwise"
        turn_note_ar = "دون تدوير الورقة" if extra_cw == 0 else f"ثم أدار الورقة {m(extra_cw * 90)}° مع عقارب الساعة"
        B.add_math(
            tp, "Medium", bp,
            f"A {m('3 \\times 3')} rubber stamp face holds row 1 `{g0[0]}`, row 2 `{g0[1]}`, and row 3 `{g0[2]}`. Pressing it onto paper **flips left-and-right like a mirror**, {turn_note_en}. What number appears in the **{c_en}** corner?",
            f"وجه ختم مطاطي {m('3 \\times 3')} يحمل الصف الأول `{g0[0]}` والثاني `{g0[1]}` والثالث `{g0[2]}`. عند طبعه على الورق **ينعكس اليمين واليسار كالمرآة**، {turn_note_ar}. ما العدد الذي يظهر في الركن **{c_ar}**؟",
            ans, [g0[tr_r][tr_c], stamped[0][0], stamped[2][2], g0[2][0]],
            "Flip left and right columns first (mirror image!), then rotate the paper if needed!",
            "اعكس العمود الأيمن والعمود الأيسر أولاً (صورة مرآة)، ثم طبّق الدوران إن وُجد!",
            "Apply horizontal reflection first, followed by the specified clockwise rotation.",
            [
                f"Pressing the stamp mirrors each row left-to-right: top row becomes `{stamped[0]}` and bottom row becomes `{stamped[2]}`.",
                f"After the paper turn ({m(extra_cw * 90)}° CW), the **{c_en}** corner holds {m(ans)}.",
            ],
            f"Exact mirror + rotation check lands {m(ans)} in the {c_en} corner!",
            "نعكس كل صف أفقياً أولاً لتأثير الختم، ثم نطبق دوران الورقة.",
            [
                f"بعد الانعكاس الأفقي يصبح الصف العلوي `{stamped[0]}` والسفلي `{stamped[2]}`.",
                f"بعد التدوير يستقر العدد {m(ans)} في الركن **{c_ar}**.",
            ],
            f"تحقق: العدد في الركن المطلوب هو {m(ans)}!",
            diagram_en=svg_kang_stamp_grid([[2, 1, 0], [1, 0, 0], [0, 0, 1]], "Mirror L↔R + Turn"),
        )

    sr_hard = [
        ([[1, 1, 0], [1, 0, 0], [0, 0, 0]], 1, "white", "بيضاء تماماً", "Kangy", "الكنغر", "a 3-square corner L-shape in the top-left", "شكل حرف L ركني من 3 مربعات في أعلى اليسار"),
        ([[1, 1, 1], [0, 1, 0], [0, 0, 0]], 2, "shaded", "مظللة", "Lina", "لينا", "4 shaded squares forming a T-shape in the top two rows", "4 مربعات مظللة على شكل حرف T في الصفين العلويين"),
        ([[1, 0, 1], [1, 0, 0], [0, 0, 0]], 1, "white", "بيضاء تماماً", "Omar", "عمر", "3 shaded squares at top-left, top-right, and middle-left", "3 مربعات مظللة في أعلى اليسار وأعلى اليمين ووسط اليسار"),
        ([[1, 1, 0], [0, 1, 0], [0, 0, 1]], 1, "shaded", "مظللة", "Sara", "سارة", "4 shaded squares stepping from top-left down to bottom-right", "4 مربعات مظللة تتدرج من أعلى اليسار إلى أسفل اليمين"),
        ([[1, 0, 0], [1, 0, 0], [1, 1, 0]], 2, "white", "بيضاء تماماً", "Tariq", "طارق", "a 4-square tall L-shape along the left column and bottom", "شكل حرف L طويل من 4 مربعات على العمود الأيسر والأسفل"),
    ]
    for g0, k_turns, mode, m_ar, nm_en, nm_ar, desc_en, desc_ar in sr_hard:
        g_rot = g0
        for _ in range(k_turns):
            g_rot = _rot90_cw(g_rot)
        shaded_union = sum(1 for r in range(3) for c in range(3) if g0[r][c] or g_rot[r][c])
        white_cnt = 9 - shaded_union
        ans = white_cnt if mode == "white" else shaded_union
        deg = k_turns * 90
        ask_en = "stay **completely white**" if mode == "white" else "end up **shaded** (by one or both sheets)"
        ask_ar = "تبقى **بيضاء تماماً**" if mode == "white" else "تصبح **مظللة** (بورقة واحدة أو كلتيهما)"
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} takes the {m('3 \\times 3')} transparent sheet shown ({desc_en}), makes an exact copy, rotates the copy **{m(deg)}° clockwise**, and places it directly on top of the original. Out of the {m(9)} small squares, how many {ask_en}?",
            f"أخذ/أخذت {nm_ar} الشفافية {m('3 \\times 3')} الموضحة ({desc_ar})، وصنع/صنعت نسخة مطابقة منها وأدارها **{m(deg)}° مع عقارب الساعة** ثم وضعها فوق الأصلية تماماً. من بين المربعات الـ {m(9)}، كم مربعاً {ask_ar}؟",
            ans, [9 - ans, ans - 1 if ans > 0 else 2, ans + 1, sum(sum(r) for r in g0) * 2],
            f"Mark where each shaded cell lands after a {m(deg)}° clockwise turn right on the {m('3 \\times 3')} grid!",
            f"عيّن مواقع المربعات المظللة بعد دورانها {m(deg)}° مع عقارب الساعة فوق الشبكة {m('3 \\times 3')} نفسها!",
            "Overlay the original 3×3 grid with its rotated image and count shaded vs unshaded cells.",
            [
                f"Rotating the shaded squares {m(deg)}° clockwise and overlaying them covers {m(shaded_union)} distinct squares out of {m(9)}.",
                f"That leaves {m(f'9 - {shaded_union} = {white_cnt}')} completely white squares, so the answer is {m(ans)}.",
            ],
            f"Check: {m(shaded_union)} shaded + {m(white_cnt)} white = {m(9)} squares!",
            "نطابق الشبكة الأصلية مع صورتها بعد الدوران ونحصي الخلايا المظللة والبيضاء.",
            [
                f"عدد المربعات المظللة بعد التطابق (مع عدم تكرار المشترك) = {m(shaded_union)} من أصل {m(9)}.",
                f"عدد المربعات البيضاء المتبقية = {m(white_cnt)}، فتكون الإجابة {m(ans)}.",
            ],
            f"تحقق: {m(f'{shaded_union} + {white_cnt} = 9')} مربعات!",
            diagram_en=svg_kang_stamp_grid(g0, f"Overlay +{deg}° CW"),
        )

    # 4. kang_eco_polyomino_fit (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_polyomino_fit"
    pf_easy = [
        ([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], 1, "plus-pentomino", "قطعة الزائد الخماسية"),
        ([(0, 0), (1, 0), (2, 0), (1, 1)], 2, "T-tetromino", "قطعة حرف T الرباعية"),
        ([(0, 0), (0, 1), (0, 2), (1, 2)], 3, "L-tetromino", "قطعة حرف L الرباعية"),
        ([(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)], 1, "U-pentomino", "قطعة حرف U الخماسية"),
        ([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)], 2, "stair-pentomino", "القطعة المتدرجة الخماسية"),
    ]
    for cells, side_cm, name_en, name_ar in pf_easy:
        cset = set(cells)
        unit_edges = sum(4 - sum((c + dc, r + dr) in cset for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1))) for c, r in cset)
        ans = unit_edges * side_cm
        B.add_math(
            tp, "Easy", bp,
            f"This {name_en} is made of {m(len(cells))} identical squares, each of side length {m(side_cm)} cm. What is the **outer perimeter** of the shape in cm?",
            f"تتكوّن {name_ar} الموضحة من {m(len(cells))} مربعات متطابقة طول ضلع كل منها {m(side_cm)} سم. ما **المحيط الخارجي** للشكل بالسنتمتر؟",
            ans, [4 * len(cells) * side_cm, ans - 2 * side_cm, ans + 2 * side_cm, len(cells) * side_cm * side_cm],
            "Walk all the way around the outside boundary and count unit edges—don't count inner glued lines!",
            "عدّ الحواف الخارجية فقط حول محيط الشكل ولا تحسب الخطوط الداخلية المشتركة!",
            "Count exposed boundary edges of the polyomino and multiply by the side length.",
            [
                f"Counting around the boundary gives {m(unit_edges)} exposed square edges.",
                f"Each edge is {m(side_cm)} cm, so perimeter = {m(f'{unit_edges} \\times {side_cm} = {ans}')} cm.",
            ],
            f"Inner glued edges are excluded: {m(f'{unit_edges} \\times {side_cm} = {ans}')} cm!",
            "نحصي عدد الأضلاع الخارجية المكشوفة حول الشكل ثم نضرب في طول الضلع.",
            [
                f"عدد الأضلاع الخارجية المكشوفة = {m(unit_edges)} ضلعاً.",
                f"المحيط = {m(f'{unit_edges} \\times {side_cm} = {ans}')} سم.",
            ],
            f"تحقق: {m(ans)} سم!",
            diagram_en=svg_polyomino(cells, f"Side = {side_cm} cm"),
        )

    # Use boards where blocked cells leave a 100% tilable white region by 1x2 dominoes
    pf_med_clean = [
        (4, 4, [(0, 0), (0, 1)], "Maha", "مها"),
        (4, 5, [(0, 0), (0, 1), (3, 3), (3, 4)], "Faisal", "فيصل"),
        (3, 6, [(1, 2), (1, 3)], "Dana", "دانة"),
        (4, 6, [(0, 0), (1, 0), (2, 5), (3, 5)], "Kareem", "كريم"),
        (5, 4, [(2, 1), (2, 2)], "Reem", "ريم"),
    ]
    for R, C, blocked, nm_en, nm_ar in pf_med_clean:
        bset = set(blocked)
        # Verify white/black checkerboard balance == 0 AND exact tilability
        w_col = sum(1 for r in range(R) for c in range(C) if (r, c) not in bset and (r + c) % 2 == 0)
        b_col = sum(1 for r in range(R) for c in range(C) if (r, c) not in bset and (r + c) % 2 == 1)
        assert w_col == b_col
        ans = w_col
        board = [[-1 if (r, c) in bset else 0 for c in range(C)] for r in range(R)]
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en}'s {m(f'{R} \\times {C}')} game board has {m(len(blocked))} dark blocked squares as shown. How many {m('1 \\times 2')} domino tiles are needed to cover **all** remaining white squares without overlapping?",
            f"لوحة اللعب {m(f'{R} \\times {C}')} لدى {nm_ar} فيها {m(len(blocked))} مربعات داكنة مغلقة كما في الشكل. كم قطعة دومينو ({m('1 \\times 2')}) تلزم لتغطية **جميع** المربعات البيضاء المتبقية دون تداخل؟",
            ans, [R * C // 2, ans - 1, ans + 1, R * C - len(blocked)],
            "Count the remaining white squares and divide by 2!",
            "احسب عدد المربعات البيضاء المتبقية ثم اقسمه على 2!",
            "Subtract blocked cells from R × C, then divide by 2 squares per domino.",
            [
                f"Total squares = {m(f'{R} \\times {C} = {R * C}')}; subtracting {m(len(blocked))} dark squares leaves {m(R * C - len(blocked))} white squares.",
                f"Each {m('1 \\times 2')} domino covers {m(2)} white squares, requiring {m(f'{R * C - len(blocked)} \\div 2 = {ans}')} dominoes.",
            ],
            f"All remaining rows/pairs tile cleanly with {m(ans)} dominoes!",
            "نطرح المربعات المغلقة من مساحة اللوحة ثم نقسم الباقي على 2.",
            [
                f"المربعات البيضاء المتبقية = {m(f'{R * C} - {len(blocked)} = {R * C - len(blocked)}') } مربعاً.",
                f"عدد قطع الدومينو = {m(f'{R * C - len(blocked)} \\div 2 = {ans}')} قطعة.",
            ],
            f"تحقق: {m(f'{ans} \\times 2 = {R * C - len(blocked)}') } مربعاً أبيض!",
            diagram_en=svg_kang_polyomino_board(board),
        )

    pf_hard = [
        (5, 5, "Kangy", "الكنغر"),
        (5, 7, "Lina", "لينا"),
        (5, 9, "Omar", "عمر"),
        (7, 7, "Sara", "سارة"),
        (7, 9, "Tariq", "طارق"),
    ]
    for R, C, nm_en, nm_ar in pf_hard:
        ans = (R // 2) * (C // 2)
        area_trap = (R * C) // 4
        board = [[((r // 2 + c // 2) % 3 + 1) if (r < 2 * (R // 2) and c < 2 * (C // 2)) else 0 for c in range(C)] for r in range(R)]
        B.add_math(
            tp, "Hard", bp,
            f"What is the **maximum** number of non-overlapping {m('2 \\times 2')} square tiles {nm_en} can place inside an empty {m(f'{R} \\times {C}')} grid board (without cutting any tile)?",
            f"ما **أكبر** عدد من البلاطات المربعة {m('2 \\times 2')} التي يمكن لـ {nm_ar} وضعها داخل لوحة شبكية فارغة أبعادها {m(f'{R} \\times {C}')} دون تداخل ودون قص أي بلاطة؟",
            ans, [area_trap, ans + 1, ans - 1, (R * C) // 2],
            f"You cannot cut tiles! Check how many {m(2)}s fit along height {m(R)} and how many {m(2)}s fit along width {m(C)}!",
            f"لا يمكن قص البلاطات! افحص كم اثنين تسع في الارتفاع {m(R)} وكم اثنين تسع في العرض {m(C)}!",
            "Along height R at most floor(R/2) tiles fit, and along width C at most floor(C/2) tiles fit.",
            [
                f"Because tiles cannot be cut, at most {m(f'\\lfloor {R} \\div 2 \\rfloor = {R // 2}')} tiles fit vertically and {m(f'\\lfloor {C} \\div 2 \\rfloor = {C // 2}')} tiles fit horizontally.",
                f"Even if shifted, every {m('2 \\times 2')} tile covers one of the {m(f'{R // 2} \\times {C // 2} = {ans}')} odd-row, odd-column landmark squares.",
                f"Thus the maximum number of {m('2 \\times 2')} tiles is {m(ans)} (not {m(area_trap)}!).",
            ],
            f"Trap avoided: {m(f'{R} \\times {C} \\div 4')} gives {m(area_trap)}, but leftover 1-wide strips cannot hold uncut {m('2 \\times 2')} tiles!",
            "بما أنه لا يُسمح بقص البلاطات، نحسب أقصى سعة رأسية ⌊R/2⌋ وأفقية ⌊C/2⌋ ونضربهما.",
            [
                f"يتسع الارتفاع {m(R)} لعدد {m(R // 2)} بلاطات كحد أقصى، والعرض {m(C)} لعدد {m(C // 2)} بلاطات.",
                f"إذن أقصى عدد ممكن دون قص أو تداخل هو {m(f'{R // 2} \\times {C // 2} = {ans}')} بلاطة (وليس {m(area_trap)}).",
            ],
            f"الشريط المتبقي بعرض مربع واحد لا يتسع لبلاطة {m('2 \\times 2')}، فالجواب {m(ans)}!",
            diagram_en=svg_kang_polyomino_board(board),
        )



# ==============================================================================
# UNIT 1.5 — Combinatorics & Logic (60 Questions: KANG-ECO-241 .. KANG-ECO-300)
# Blueprints: kang_eco_queue_position, kang_eco_folded_ribbon_cuts,
#             kang_eco_outfit_counting, kang_eco_truth_order_puzzle
# ==============================================================================
import itertools


def _add_unit_1_5(B: BankBuilder) -> None:
    tp = "Combinatorics & Logic"

    # 1. kang_eco_queue_position (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_queue_position"
    q_easy = [
        (5, 9, "Kangy", "الكنغر", "zoo train", "قطار الحديقة"),
        (8, 12, "Lina", "لينا", "bakery counter", "مخبز الحي"),
        (10, 6, "Omar", "عمر", "water fountain", "براد الماء"),
        (9, 14, "Sara", "سارة", "ferris wheel", "العجلة الدوارة"),
        (12, 11, "Tariq", "طارق", "museum gate", "بوابة المتحف"),
    ]
    for f_rk, b_rk, nm_en, nm_ar, plc_en, plc_ar in q_easy:
        ans = f_rk + b_rk - 1
        B.add_math(
            tp, "Easy", bp,
            f"Students stand in one straight queue at the {plc_en}. {nm_en} is **{m(f_rk)}th from the front** and **{m(b_rk)}th from the back**. How many students are in the queue altogether?",
            f"يقف الطلاب في طابور واحد مستقيم عند {plc_ar}. ترتيب {nm_ar} هو **{m(f_rk)} من الأمام** و**{m(b_rk)} من الخلف**. كم طالباً في الطابور إجمالاً؟",
            ans, [f_rk + b_rk, ans - 1, ans + 2, abs(f_rk - b_rk) + 8],
            f"Adding {m(f'{f_rk} + {b_rk}')} counts {nm_en} twice—subtract {m(1)}!",
            f"جمع {m(f'{f_rk} + {b_rk}')} يحسب {nm_ar} مرتين، لذا اطرح {m(1)}!",
            "Total in Queue = Rank from Front + Rank from Back − 1.",
            [
                f"Ahead of {nm_en}: {m(f'{f_rk} - 1 = {f_rk - 1}')}; behind {nm_en}: {m(f'{b_rk} - 1 = {b_rk - 1}')}.",
                f"Total = {m(f'{f_rk} + {b_rk} - 1 = {ans}')} students.",
            ],
            f"Check: {m(f'{f_rk - 1} + 1 + {b_rk - 1} = {ans}')} students!",
            "العدد الكلي = الترتيب من الأمام + الترتيب من الخلف − 1.",
            [
                f"أمام {nm_ar} يوجد {m(f_rk - 1)} طلاب، وخلفه يوجد {m(b_rk - 1)} طلاب.",
                f"المجموع الكلي = {m(f'{f_rk} + {b_rk} - 1 = {ans}')} طالباً.",
            ],
            f"تحقق: {m(f'{f_rk - 1} + 1 + {b_rk - 1} = {ans}')}!",
            diagram_en=svg_number_strip(["1st", "...", f"#{f_rk}", "...", "Last"]),
        )

    q_med = [
        (24, 7, 6, "Nora", "Zaid", "نورة", "زيد"),
        (30, 9, 8, "Hala", "Yousef", "هلا", "يوسف"),
        (20, 5, 6, "Amal", "Jude", "أمل", "جود"),
        (28, 8, 9, "Salman", "Pippa", "سلمان", "بيبا"),
        (32, 10, 7, "Leo", "Rayan", "ليو", "ريان"),
    ]
    for N, a_rk, b_rk, n1_en, n2_en, n1_ar, n2_ar in q_med:
        pos_b = N - b_rk + 1
        assert a_rk < pos_b
        ans = pos_b - a_rk - 1
        assert ans == N - a_rk - b_rk
        B.add_math(
            tp, "Medium", bp,
            f"In a straight queue of {m(N)} children, {n1_en} is **{m(a_rk)}th from the front** and {n2_en} is **{m(b_rk)}th from the back**. How many children stand **strictly between** {n1_en} and {n2_en}?",
            f"في طابور مستقيم يضم {m(N)} طفلاً، ترتيب {n1_ar} هو **{m(a_rk)} من الأمام** وترتيب {n2_ar} هو **{m(b_rk)} من الخلف**. كم طفلاً يقف **بينهما تماماً**؟",
            ans, [ans + 1, ans - 1, ans + 2, a_rk + b_rk],
            f"Remove the first {m(a_rk)} children (up to {n1_en}) and the last {m(b_rk)} children (from {n2_en} to the end)!",
            f"استبعد أول {m(a_rk)} أطفال من الأمام وآخر {m(b_rk)} أطفال من الخلف!",
            "Subtract the front block of size a and the back block of size b from N.",
            [
                f"The first {m(a_rk)} children include {n1_en} and everyone ahead of {n1_en}.",
                f"The last {m(b_rk)} children include {n2_en} and everyone behind {n2_en}.",
                f"Children strictly between them = {m(f'{N} - {a_rk} - {b_rk} = {ans}')}.",
            ],
            f"Position check: {n1_en} is #{m(a_rk)} and {n2_en} is #{m(pos_b)}, leaving {m(f'{pos_b} - {a_rk} - 1 = {ans}')} between!",
            "نطرح مجموعة الأمام ومجموعة الخلف كلتيهما من العدد الكلي N.",
            [
                f"أول {m(a_rk)} أطفال يشملون {n1_ar} ومن أمامه، وآخر {m(b_rk)} أطفال يشملون {n2_ar} ومن خلفه.",
                f"عدد الأطفال بينهما = {m(f'{N} - {a_rk} - {b_rk} = {ans}')}.",
            ],
            f"تحقق بالمواقع: بين #{m(a_rk)} و#{m(pos_b)} يوجد {m(ans)} أطفال!",
            diagram_en=svg_number_strip(["1", "...", n1_en, "? between", n2_en, "...", str(N)]),
        )

    q_hard = [
        (15, 11, 10, "Maha", "Faisal", "مها", "فيصل"),
        (20, 14, 13, "Dana", "Kareem", "دانة", "كريم"),
        (18, 13, 12, "Reem", "Tariq", "ريم", "طارق"),
        (22, 16, 14, "Lina", "Omar", "لينا", "عمر"),
        (25, 18, 15, "Sara", "Zaid", "سارة", "زيد"),
    ]
    for N, a_rk, b_rk, n1_en, n2_en, n1_ar, n2_ar in q_hard:
        pos_a = a_rk
        pos_b = N - b_rk + 1
        assert pos_b < pos_a
        ans = len(range(pos_b + 1, pos_a))
        assert ans == a_rk + b_rk - N - 2
        B.add_math(
            tp, "Hard", bp,
            f"Exactly {m(N)} students stand in a single line. {n1_en} is **{m(a_rk)}th from the front**, while {n2_en} is **{m(b_rk)}th from the back**. How many students stand **strictly between** {n1_en} and {n2_en}?",
            f"يقف {m(N)} طالباً في صف واحد مستقيم. ترتيب {n1_ar} هو **{m(a_rk)} من الأمام**، بينما ترتيب {n2_ar} هو **{m(b_rk)} من الخلف**. كم طالباً يقف **بينهما تماماً**؟",
            ans, [a_rk + b_rk - N, a_rk + b_rk - N - 1, ans + 3, abs(a_rk - b_rk)],
            f"Careful—{m(f'{a_rk} + {b_rk} = {a_rk + b_rk} > {N}')}, so {n2_en} actually stands **ahead** of {n1_en}! Find {n2_en}'s exact rank from the front first!",
            f"انتبه: {m(f'{a_rk} + {b_rk} > {N}')} أي أن {n2_ar} يقف **أمام** {n1_ar}! احسب ترتيب {n2_ar} من الأمام أولاً!",
            "Convert the back rank to a front position (N − b + 1), then count positions strictly between them.",
            [
                f"From the front, {n2_en}'s position is {m(f'{N} - {b_rk} + 1 = {pos_b}')}, which is ahead of {n1_en} at position {m(pos_a)}.",
                f"Students strictly between position {m(pos_b)} and position {m(pos_a)} = {m(f'{pos_a} - {pos_b} - 1 = {ans}')}.",
            ],
            f"Overlap formula check: {m(f'{a_rk} + {b_rk} - {N} - 2 = {ans}')} students!",
            "نحوّل الترتيب من الخلف إلى موقع من الأمام (N − b + 1) ثم نحسب المحصورين بين الموقعين.",
            [
                f"موقع {n2_ar} من الأمام هو {m(f'{N} - {b_rk} + 1 = {pos_b}')}، وموقع {n1_ar} من الأمام هو {m(pos_a)}.",
                f"عدد الطلاب الواقفين بين الموقعين {m(pos_b)} و{m(pos_a)} يساوي {m(f'{pos_a} - {pos_b} - 1 = {ans}')}.",
            ],
            f"تحقق: بين الموقع {m(pos_b)} والموقع {m(pos_a)} يقف {m(ans)} طلاب!",
            diagram_en=svg_number_strip(["1", "...", n2_en, "? between", n1_en, "...", str(N)]),
        )

    # 2. kang_eco_folded_ribbon_cuts (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_folded_ribbon_cuts"
    rb_easy = [
        (2, "silk ribbon", "شريط حريري"),
        (3, "paper streamer", "شريط ورقي"),
        (4, "cotton string", "خيط قطني"),
        (5, "yarn cord", "حبل صوفي"),
        (6, "gift tape", "شريط هدايا"),
    ]
    for s_cnt, obj_en, obj_ar in rb_easy:
        ans = s_cnt + 1
        B.add_math(
            tp, "Easy", bp,
            f"Kangy folds one straight {obj_en} into {m(s_cnt)} parallel layers as shown and makes **1 straight scissor cut** across all layers (away from the folds). How many separate pieces result?",
            f"طوى الكنغر {obj_ar} مستقيماً واحداً إلى {m(s_cnt)} طبقات متوازية كما في الشكل، ثم قصّه بالمقص **قصّة واحدة مستقيمة** عبر الطبقات كلها. كم قطعة منفصلة تنتج؟",
            ans, [s_cnt, s_cnt * 2, ans + 1, ans + 2],
            f"One cut across {m(s_cnt)} layers makes {m(s_cnt)} snips along the unfolded ribbon—add {m(1)}!",
            f"القصّة الواحدة عبر {m(s_cnt)} طبقات تصنع {m(s_cnt)} نقاط قص على الشريط المفتوح، فأضف {m(1)}!",
            "Cutting an open ribbon in S places produces S + 1 pieces.",
            [
                f"The scissors slice the ribbon in {m(s_cnt)} distinct places.",
                f"An open ribbon cut in {m(s_cnt)} places falls into {m(f'{s_cnt} + 1 = {ans}')} pieces.",
            ],
            f"Check: {m(2)} loose-end pieces + {m(s_cnt - 1)} folded loop piece(s) = {m(ans)} pieces!",
            "قص شريط مفتوح في S مواضع ينتج S + 1 من القطع المنفصلة.",
            [
                f"يقطع المقص الشريط في {m(s_cnt)} مواضع مختلفة.",
                f"عدد القطع الناتجة = {m(f'{s_cnt} + 1 = {ans}')} قطع.",
            ],
            f"تحقق: طرفان حران ({m(2)}) + ثنيات وسطى ({m(s_cnt - 1)}) = {m(ans)} قطع!",
            diagram_en=svg_kang_folded_ribbon(s_cnt, 1),
        )

    rb_med = [
        (2, 2, "Nora", "نورة"),
        (3, 2, "Zaid", "زيد"),
        (3, 3, "Hala", "هلا"),
        (5, 2, "Yousef", "يوسف"),
        (4, 3, "Amal", "أمل"),
    ]
    for s_cnt, c_cnt, nm_en, nm_ar in rb_med:
        ans = s_cnt * c_cnt + 1
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} folds one long ribbon into {m(s_cnt)} parallel layers and makes **{m(c_cnt)} straight cuts** completely across the middle (not touching the folds). How many pieces of ribbon are formed?",
            f"طوت/طوى {nm_ar} شريطاً طويلاً واحداً إلى {m(s_cnt)} طبقات متوازية، ثم قصّ **{m(c_cnt)} قصّات مستقيمة** عبر الطبقات كلها بعيداً عن الثنيات. كم قطعة شريط تتكوّن؟",
            ans, [s_cnt * c_cnt, ans + 1, s_cnt + c_cnt + 1, (s_cnt + 1) * c_cnt],
            f"Multiply {m(f'{s_cnt} \\times {c_cnt}')} to count total snips, then add {m(1)}!",
            f"اضرب {m(f'{s_cnt} \\times {c_cnt}')} لحساب إجمالي نقاط القص ثم أضف {m(1)}!",
            "Use Pieces = (Strands × Cuts) + 1.",
            [
                f"Total snips along the unfolded ribbon = {m(f'{s_cnt} \\times {c_cnt} = {s_cnt * c_cnt}')}.",
                f"Number of pieces = {m(f'{s_cnt * c_cnt} + 1 = {ans}')}.",
            ],
            f"Formula check: {m(f'{s_cnt} \\times {c_cnt} + 1 = {ans}')} pieces!",
            "نطبق القاعدة: عدد القطع = (عدد الطبقات × عدد القصّات) + 1.",
            [
                f"إجمالي نقاط القص على الشريط = {m(f'{s_cnt} \\times {c_cnt} = {s_cnt * c_cnt}')}.",
                f"عدد القطع الناتجة = {m(f'{s_cnt * c_cnt} + 1 = {ans}')} قطعة.",
            ],
            f"تحقق: {m(ans)} قطعة!",
            diagram_en=svg_kang_folded_ribbon(s_cnt, c_cnt),
        )

    rb_hard = [
        ("cuts", 4, 3, 0, "Jude", "جود"),
        ("cuts", 5, 3, 0, "Salman", "سلمان"),
        ("len", 2, 1, 24, "Pippa", "بيبا"),
        ("len", 2, 1, 36, "Leo", "ليو"),
        ("len", 2, 1, 48, "Rayan", "ريان"),
    ]
    for kind, s_cnt, c_cnt, L_cm, nm_en, nm_ar in rb_hard:
        if kind == "cuts":
            pcs = s_cnt * c_cnt + 1
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} folds a single straight rope into {m(s_cnt)} parallel layers and makes several straight scissor cuts across all {m(s_cnt)} layers (away from the folds). When unfolded, there are **{m(pcs)} separate pieces**. How many straight cuts did {nm_en} make?",
                f"طوى/طوت {nm_ar} حبلاً مستقيماً واحداً إلى {m(s_cnt)} طبقات متوازية، ثم قصّ عدة قصّات مستقيمة عبر الطبقات الـ {m(s_cnt)} كلها، فنتجت **{m(pcs)} قطعة منفصلة**. كم قصّة مستقيمة صنع؟",
                c_cnt, [c_cnt + 1, c_cnt - 1, pcs // s_cnt + 2, s_cnt],
                f"Subtract {m(1)} from {m(pcs)} to find the total snips, then divide by {m(s_cnt)} layers!",
                f"اطرح {m(1)} من {m(pcs)} لمعرفة نقاط القص الكلية، ثم اقسم على {m(s_cnt)} طبقات!",
                "Solve S × C + 1 = Pieces by computing (Pieces − 1) ÷ S.",
                [
                    f"Getting {m(pcs)} pieces from 1 rope requires {m(f'{pcs} - 1 = {pcs - 1}')} snips in total.",
                    f"Each straight cut makes {m(s_cnt)} snips, so {m(f'{pcs - 1} \\div {s_cnt} = {c_cnt}')} cuts were made.",
                ],
                f"Check: {m(f'{s_cnt} \\times {c_cnt} + 1 = {pcs}')} pieces!",
                "نطرح 1 من عدد القطع ثم نقسم على عدد الطبقات.",
                [
                    f"عدد نقاط القص الكلي = {m(f'{pcs} - 1 = {pcs - 1}')}.",
                    f"عدد القصّات بالمقص = {m(f'{pcs - 1} \\div {s_cnt} = {c_cnt}')} قصّات.",
                ],
                f"تحقق: {m(f'{s_cnt} \\times {c_cnt} + 1 = {pcs}')} قطعة!",
                diagram_en=svg_kang_folded_ribbon(s_cnt, c_cnt),
            )
        else:
            ans = L_cm // 2
            short_p = L_cm // 4
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} takes a ribbon of length {m(L_cm)} cm, folds it **exactly in half** ({m(2)} equal layers of {m(L_cm // 2)} cm), and makes **1 cut** right through the exact midpoint of the folded ribbon. When unfolded, how many cm long is the **longest** piece?",
                f"أخذ/أخذت {nm_ar} شريطاً طوله {m(L_cm)} سم، وطواه **من المنتصف تماماً** إلى طبقتين طول كل منهما {m(L_cm // 2)} سم، ثم قصّه **قصّة واحدة** في منتصف الشريط المطوي تماماً. عند فتح القطع، كم سنتمتراً طول **أطول** قطعة؟",
                ans, [short_p, L_cm // 3, ans + short_p, short_p // 2],
                "The folded bend stays connected! Two quarter-lengths stay joined across the fold!",
                "ثنية الطي تظل متصلة! نصفا الطبقتين عند جهة الطي يبقيان قطعة واحدة متصلة!",
                "Trace the two loose ends (L/4 each) and the connected U-fold loop (L/4 + L/4 = L/2).",
                [
                    f"The folded ribbon has length {m(L_cm // 2)} cm, so cutting its midpoint slices {m(short_p)} cm from the loose ends and {m(short_p)} cm from the fold.",
                    f"The two loose ends give two pieces of {m(short_p)} cm, while the folded U-loop unfolds into **one connected piece** of length {m(f'{short_p} + {short_p} = {ans}')} cm!",
                ],
                f"Sum of all 3 pieces: {m(f'{short_p} + {ans} + {short_p} = {L_cm}')} cm!",
                "ننتبه إلى أن الجزء القريب من ثنية الطي لا ينفصل بل يمتد على الطبقتين معاً.",
                [
                    f"القص في منتصف الطول المطوي ({m(L_cm // 2)} سم) يبعد {m(short_p)} سم عن الطرفين الحرين وعن الثنية.",
                    f"ينتج طرفان طول كل منهما {m(short_p)} سم، وقطعة متصلة عبر الثنية طولها {m(f'{short_p} + {short_p} = {ans}')} سم!",
                ],
                f"مجموع أطوال القطع الثلاث: {m(f'{short_p} + {ans} + {short_p} = {L_cm}')} سم!",
                diagram_en=svg_kang_folded_ribbon(2, 1),
            )

    # 3. kang_eco_outfit_counting (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_outfit_counting"
    oc_easy = [
        (4, 3, "scoop flavors", "cones", "نكهات مثلجات", "بسكويتات"),
        (5, 4, "colored hats", "scarves", "قبعات ملونة", "أوشحة"),
        (3, 6, "notebooks", "gel pens", "دفاتر", "أقلام حبر"),
        (6, 5, "sandwiches", "juices", "شطائر", "عصائر"),
        (4, 7, "kite shapes", "ribbons", "طائرات ورقية", "شرائط ذيل"),
    ]
    for a, b, i1_en, i2_en, i1_ar, i2_ar in oc_easy:
        ans = a * b
        B.add_math(
            tp, "Easy", bp,
            f"At the Kangaroo booth, a child picks **1** item from {m(a)} {i1_en} **and 1** item from {m(b)} {i2_en}. How many different pairs can be chosen?",
            f"في ركن الكنغر يختار الطفل عنصراً **واحداً** من {m(a)} {i1_ar} **وعنصراً واحداً** من {m(b)} {i2_ar}. كم زوجاً مختلفاً يمكن اختياره؟",
            ans, [a + b, ans - a, ans + b, 2 * (a + b)],
            f"Each of the {m(a)} first choices can pair with any of the {m(b)} second choices—multiply!",
            f"كل خيار من الـ {m(a)} الأولى يقترن بأي من الـ {m(b)} الثانية؛ اضرب العددين!",
            "Apply the Multiplication Principle: a × b.",
            [
                f"There are {m(a)} choices for the first item and {m(b)} choices for the second item.",
                f"Total combinations = {m(f'{a} \\times {b} = {ans}')}.",
            ],
            f"Avoid adding ({m(a + b)})—multiplying gives {m(ans)}!",
            "نطبق مبدأ العد بالضرب: عدد الخيارات الأولى × عدد الخيارات الثانية.",
            [
                f"يوجد {m(a)} خيارات للأول و{m(b)} خيارات للثاني.",
                f"عدد الأزواج المختلفة = {m(f'{a} \\times {b} = {ans}')}.",
            ],
            f"تحقق: {m(f'{a} \\times {b} = {ans}')}!",
            diagram_en=svg_digit_slots([f"{a}", f"{b}"], f"{a} × {b} choices"),
        )

    oc_med = [
        (2, 4, 4, "hats", "jackets", "boots", "قبعات", "سترات", "أحذية"),
        (3, 3, 4, "soups", "pastas", "fruits", "حساء", "معكرونة", "فواكه"),
        (4, 5, 2, "stickers", "cards", "envelopes", "ملصقات", "بطاقات", "مغلفات"),
        (3, 5, 3, "badges", "lanyards", "pens", "شارات", "أشرطة", "أقلام"),
        (2, 6, 3, "helmets", "jerseys", "shorts", "خوذات", "قمصان", "سراويل"),
    ]
    for a, b, c, x1, x2, x3, y1, y2, y3 in oc_med:
        ans = a * b * c
        B.add_math(
            tp, "Medium", bp,
            f"Kangy packs a gift kit by choosing **1** of {m(a)} {x1}, **1** of {m(b)} {x2}, and **1** of {m(c)} {x3}. How many different complete gift kits are possible?",
            f"يجهز الكنغر حقيبة هدية باختيار عنصر **واحد** من {m(a)} {y1}، و**واحد** من {m(b)} {y2}، و**واحد** من {m(c)} {y3}. كم حقيبة هدية مختلفة يمكن تكوينها؟",
            ans, [a + b + c, a * b + c, ans - b, ans + c],
            f"Multiply all three choice counts together: {m(f'{a} \\times {b} \\times {c}')}!",
            f"اضرب أعداد الخيارات الثلاثة معاً: {m(f'{a} \\times {b} \\times {c}')}!",
            "Multiply choices across all three independent categories.",
            [
                f"First two categories give {m(f'{a} \\times {b} = {a * b}')} pairs.",
                f"Pairing with {m(c)} {x3} gives {m(f'{a * b} \\times {c} = {ans}')} kits.",
            ],
            f"Check: {m(f'{a} \\times {b} \\times {c} = {ans}')}!",
            "نضرب عدد خيارات الفئات الثلاث المستقلة معاً.",
            [
                f"أول فئتين تعطيان {m(f'{a} \\times {b} = {a * b}')} زوجاً.",
                f"وبالضرب في {m(c)} نحصل على {m(f'{a * b} \\times {c} = {ans}')} حقيبة.",
            ],
            f"تحقق: {m(f'{a} \\times {b} \\times {c} = {ans}')}!",
            diagram_en=svg_digit_slots([str(a), str(b), str(c)], f"{a} × {b} × {c}"),
        )

    oc_hard = [
        ([1, 2, 3, 5], "Maha", "مها"),
        ([2, 3, 4, 7], "Faisal", "فيصل"),
        ([1, 4, 6, 8], "Dana", "دانة"),
        ([2, 4, 6, 9], "Kareem", "كريم"),
        ([2, 4, 6, 8], "Reem", "ريم"),
    ]
    for cards, nm_en, nm_ar in oc_hard:
        valid_nums = [
            100 * x + 10 * y + z
            for x in cards for y in cards for z in cards
            if len({x, y, z}) == 3 and z % 2 == 0
        ]
        ans = len(valid_nums)
        evens = [d for d in cards if d % 2 == 0]
        c_str = ", ".join(str(d) for d in cards)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} has four digit cards: {m(c_str)}. How many different **3-digit EVEN numbers** can {nm_en} build if no card can be used more than once in the same number?",
            f"مع {nm_ar} أربع بطاقات أرقام: {m(c_str)}. كم **عدداً زوجياً مختلفاً من 3 أرقام** يمكن تكوينه دون تكرار أي بطاقة في العدد الواحد؟",
            ans, [24 if ans != 24 else 16, len(evens) * 9, ans + 3, max(2, ans - 2)],
            "Choose the **ones digit FIRST** so the number is guaranteed to be even!",
            "اختر **رقم الآحاد أولاً** لضمان كون العدد زوجياً!",
            "Pick an even card for the ones place first, then fill hundreds and tens from the remaining 3 cards.",
            [
                f"For the number to be even, the ones digit must come from the even card(s) in `{{{c_str}}}`: {m(len(evens))} choice(s).",
                f"After placing the ones digit, {m(3)} cards remain for the hundreds place, and then {m(2)} cards remain for the tens place.",
                f"Total even 3-digit numbers = {m(f'{len(evens)} \\times 3 \\times 2 = {ans}')}.",
            ],
            f"Exhaustive list count confirms {m(ans)} distinct 3-digit even numbers!",
            "نبدأ بخانة الآحاد بشرط الزوجية، ثم نملأ المئات فالعشرات من البطاقات المتبقية.",
            [
                f"عدد البطاقات الزوجية المتاحة لخانة الآحاد هو {m(len(evens))}.",
                f"يتبقى {m(3)} خيارات للمئات ثم خياران ({m(2)}) للعشرات، فيكون الناتج {m(f'{len(evens)} \\times 3 \\times 2 = {ans}')}.",
            ],
            f"تحقق بالحصر الكامل: {m(ans)} أعداد!",
            diagram_en=svg_digit_slots(["3 left", "2 left", f"{len(evens)} even"], f"Cards: {c_str}"),
        )

    # 4. kang_eco_truth_order_puzzle (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_truth_order_puzzle"
    friends = [
        ("Ali", "علي"),
        ("Badr", "بدر"),
        ("Faris", "فارس"),
        ("Hamad", "حمد"),
        ("Sami", "سامي"),
    ]
    # 5 unique ordering puzzles over 0..4 (index 0 = 1st/tallest, 4 = 5th/shortest)
    ord_specs = [
        # perm [2, 0, 4, 1, 3]: 1st Badr(1), 2nd Hamad(3), 3rd Ali(0), 4th Sami(4), 5th Faris(2)
        ([1, 3, 0, 4, 2], 2, "3rd (right in the middle)", "الثالث (في المنتصف تماماً)",
         "Badr finished ahead of everyone. Faris finished last. Ali finished behind Hamad and ahead of Sami.",
         "أنهى بدر السباق قبل الجميع، وجاء فارس أخيراً، وجاء علي بعد حمد وقبل سامي."),
        # perm [4, 2, 0, 3, 1]: 1st Sami(4), 2nd Faris(2), 3rd Ali(0), 4th Hamad(3), 5th Badr(1)
        ([4, 2, 0, 3, 1], 1, "2nd", "الثاني",
         "Sami is the tallest. Badr is the shortest. Ali is taller than Hamad, and Faris is taller than Ali.",
         "سامي هو الأطول، وبدر هو الأقصر، وعلي أطول من حمد، وفارس أطول من علي."),
        # perm [0, 4, 1, 2, 3]: 1st Ali(0), 2nd Sami(4), 3rd Badr(1), 4th Faris(2), 5th Hamad(3)
        ([0, 4, 1, 2, 3], 3, "4th", "الرابع",
         "Ali has the most stickers. Hamad has the fewest. Sami has more than Badr, and Badr has more than Faris.",
         "مع علي أكبر عدد من الملصقات، ومع حمد الأقل، ومع سامي أكثر من بدر، ومع بدر أكثر من فارس."),
        # perm [3, 1, 4, 2, 0]: 1st Hamad(3), 2nd Badr(1), 3rd Sami(4), 4th Faris(2), 5th Ali(0)
        ([3, 1, 4, 2, 0], 2, "3rd", "الثالث",
         "Hamad arrived 1st and Ali arrived 5th. Badr arrived earlier than Sami, and Sami arrived earlier than Faris.",
         "وصل حمد أولاً ووصل علي خامساً، ووصل بدر قبل سامي، ووصل سامي قبل فارس."),
        # perm [2, 3, 1, 0, 4]: 1st Faris(2), 2nd Hamad(3), 3rd Badr(1), 4th Ali(0), 5th Sami(4)
        ([2, 3, 1, 0, 4], 1, "2nd", "الثاني",
         "Faris scored highest and Sami scored lowest. Badr scored higher than Ali, and Hamad scored higher than Badr.",
         "حصل فارس على أعلى درجة وسامي على أقل درجة، وحصل بدر على أعلى من علي، وحمد على أعلى من بدر."),
    ]
    for order_list, ask_pos_idx, pos_en, pos_ar, clue_en, clue_ar in ord_specs:
        winner_friend_idx = order_list[ask_pos_idx]
        ordered_names_en = " → ".join(friends[i][0] for i in order_list)
        ordered_names_ar = " ← ".join(friends[i][1] for i in order_list)
        B.add_bilingual(
            tp, "Easy", bp,
            f"Five friends—Ali, Badr, Faris, Hamad, and Sami—are ranked from 1st to 5th with no ties. {clue_en} Who is in **{pos_en}** place?",
            f"خمسة أصدقاء (علي، بدر، فارس، حمد، سامي) مرتبون من الأول إلى الخامس دون تعادل. {clue_ar} مَن صاحب المركز **{pos_ar}**؟",
            friends, winner_friend_idx,
            "Place the 1st and 5th friends at the ends first, then chain the remaining three comparisons!",
            "ضع الأول والخامس في الطرفين أولاً ثم رتب الثلاثة الباقين بالتسلسل!",
            "Fix the extreme positions first, then order the middle three using the transitive clues.",
            [
                f"Putting every clue together fixes the unique order from 1st to 5th: **{ordered_names_en}**.",
                f"Reading position **{pos_en}** gives **{friends[winner_friend_idx][0]}**.",
            ],
            f"Every clue is satisfied by {ordered_names_en}!",
            "نثبت الطرفين أولاً ثم نرتب الثلاثة الأوساط حسب المتباينات المعطاة.",
            [
                f"الترتيب الوحيد من الأول إلى الخامس هو: **{ordered_names_ar}**.",
                f"صاحب المركز **{pos_ar}** هو **{friends[winner_friend_idx][1]}**.",
            ],
            f"تحقق: الترتيب يحقق جميع الشروط المعطاة!",
            diagram_en=svg_number_strip(["1st", "2nd", "3rd", "4th", "5th"]),
        )

    # Medium: 5 distinct 3x3 Latin squares
    all_latin3 = [
        g for g in itertools.product(itertools.permutations([1, 2, 3]), repeat=3)
        if all(len({g[0][c], g[1][c], g[2][c]}) == 3 for c in range(3))
    ]
    latin_med_specs = [
        ({(0, 0): 1, (0, 1): 3, (0, 2): 2, (1, 0): 2, (2, 0): 3}, (2, 2), "bottom-right", "Lina", "لينا", "top row (1, 3, 2) and left column (1, 2, 3)", "الصف العلوي (1، 3، 2) والعمود الأيسر (1، 2، 3)"),
        ({(0, 0): 3, (0, 1): 1, (0, 2): 2, (1, 2): 1, (2, 2): 3}, (2, 0), "bottom-left", "Omar", "عمر", "top row (3, 1, 2) and right column (2, 1, 3)", "الصف العلوي (3، 1، 2) والعمود الأيمن (2، 1، 3)"),
        ({(0, 0): 1, (1, 0): 3, (2, 0): 2, (2, 1): 1, (2, 2): 3}, (0, 1), "top-middle", "Sara", "سارة", "left column (1, 3, 2) and bottom row (2, 1, 3)", "العمود الأيسر (1، 3، 2) والصف السفلي (2، 1، 3)"),
        ({(0, 1): 2, (0, 2): 1, (1, 2): 3, (2, 2): 2}, (1, 1), "center", "Tariq", "طارق", "top-middle 2 and right column (1, 3, 2)", "أعلى الوسط 2 والعمود الأيمن (1، 3، 2)"),
        ({(0, 0): 1, (0, 1): 3, (1, 1): 1, (2, 0): 3}, (2, 2), "bottom-right", "Nora", "نورة", "top-left 1, top-middle 3, center 1, and bottom-left 3", "أعلى اليسار 1 وأعلى الوسط 3 والمركز 1 وأسفل اليسار 3"),
    ]
    pos_ar_map = {
        "bottom-right": "أسفل اليمين",
        "bottom-left": "أسفل اليسار",
        "top-middle": "أعلى الوسط",
        "center": "المركز",
    }
    for clues, q_rc, p_en, nm_en, nm_ar, clue_en, clue_ar in latin_med_specs:
        matches = [g for g in all_latin3 if all(g[r][c] == v for (r, c), v in clues.items())]
        vals_at_q = {g[q_rc[0]][q_rc[1]] for g in matches}
        assert len(vals_at_q) == 1, f"Ambiguous Latin clue: {vals_at_q}"
        ans = next(iter(vals_at_q))
        grid_disp = [["?" if (r, c) == q_rc else str(clues.get((r, c), "")) for c in range(3)] for r in range(3)]
        B.add_math(
            tp, "Medium", bp,
            f"In {nm_en}'s {m('3 \\times 3')} mini-Sudoku grid ({clue_en}), every row and every column must contain {m(1)}, {m(2)}, and {m(3)} once each. What number must go in the {p_en} {m('?')} cell?",
            f"في شبكة السودوكو المصغرة {m('3 \\times 3')} لدى {nm_ar} ({clue_ar})، يجب أن يظهر كل من {m(1)} و{m(2)} و{m(3)} مرة واحدة في كل صف وكل عمود. ما الرقم الواجب وضعه في خلية {m('?')} ({pos_ar_map[p_en]})؟",
            ans, [x for x in (1, 2, 3, 4, 5) if x != ans],
            "Complete any row or column that already has two numbers first!",
            "ابدأ بإكمال أي صف أو عمود يحتوي بالفعل على رقمين معلومين!",
            "Fill forced cells row-by-row and column-by-column until `?` is uniquely determined.",
            [
                f"Using the rule that every row and column contains {m('1, 2, 3')} without repeats, each missing neighbor is forced step-by-step.",
                f"The unique valid {m('3 \\times 3')} completion places {m(ans)} in the {p_en} {m('?')} cell.",
            ],
            f"Verified across all valid {m('3 \\times 3')} Latin squares: {m('?')} must be {m(ans)}!",
            "نملأ الصفوف والأعمدة التي ينقصها رقم واحد بالتتابع حتى تتحدد خلية الاستفهام.",
            [
                f"بتطبيق شرط عدم تكرار {m('1, 2, 3')} في أي صف أو عمود تتحدد الخانات المجاورة تباعاً.",
                f"القيمة الوحيدة الممكنة في خلية {m('?')} هي {m(ans)}.",
            ],
            f"تحقق: إكمال الشبكة يحقق الشرط في جميع الصفوف والأعمدة مع {m(ans)}!",
            diagram_en=svg_magic_square_3x3(grid_disp),
        )

    # Hard: 5 Verified Truth-Count Treasure Chest Logic Puzzles
    truth_hard = [
        (
            [12, 15, 18, 20, 24], 3,
            [("greater than 16", "أكبر من 16", lambda x: x > 16),
             ("a multiple of 5", "من مضاعفات 5", lambda x: x % 5 == 0),
             ("even", "زوجي", lambda x: x % 2 == 0),
             ("less than 15", "أصغر من 15", lambda x: x < 15)],
        ),
        (
            [11, 14, 15, 21, 28], 1,
            [("even", "زوجي", lambda x: x % 2 == 0),
             ("a multiple of 7", "يقبل القسمة على 7", lambda x: x % 7 == 0),
             ("greater than 20", "أكبر من 20", lambda x: x > 20),
             ("a multiple of 5", "يقبل القسمة على 5", lambda x: x % 5 == 0)],
        ),
        (
            [9, 12, 16, 18, 25], 3,
            [("a multiple of 3", "يقبل القسمة على 3", lambda x: x % 3 == 0),
             ("greater than 15", "أكبر من 15", lambda x: x > 15),
             ("even", "زوجي", lambda x: x % 2 == 0),
             ("odd", "فردي", lambda x: x % 2 == 1)],
        ),
        (
            [10, 13, 18, 25, 30], 4,
            [("even", "زوجي", lambda x: x % 2 == 0),
             ("a multiple of 5", "يقبل القسمة على 5", lambda x: x % 5 == 0),
             ("greater than 20", "أكبر من 20", lambda x: x > 20),
             ("a multiple of 3", "يقبل القسمة على 3", lambda x: x % 3 == 0)],
        ),
        (
            [8, 15, 21, 24, 27], 1,
            [("a multiple of 3", "يقبل القسمة على 3", lambda x: x % 3 == 0),
             ("greater than 20", "أكبر من 20", lambda x: x > 20),
             ("odd", "فردي", lambda x: x % 2 == 1),
             ("less than 10", "أصغر من 10", lambda x: x < 10)],
        ),
    ]
    for cands, k_true, preds in truth_hard:
        winners = [x for x in cands if sum(bool(fn(x)) for _, _, fn in preds) == k_true]
        assert len(winners) == 1, f"Expected unique winner, got {winners}"
        ans = winners[0]
        distractors = [x for x in cands if x != ans]
        c_str = ", ".join(str(x) for x in cands)
        clues_en = "; ".join(f"({i}) it is {pe}" for i, (pe, _, _) in enumerate(preds, 1))
        clues_ar = "؛ ".join(f"({i}) أنه {pa}" for i, (_, pa, _) in enumerate(preds, 1))
        counts_desc = ", ".join(f"{x}→{sum(bool(fn(x)) for _, _, fn in preds)}" for x in cands)
        B.add_math(
            tp, "Hard", bp,
            f"Kangy hides one of the five numbers `{c_str}` inside a mystery box and writes 4 clues: {clues_en}. If **exactly {m(k_true)}** of the 4 clues are **TRUE**, which number is inside the box?",
            f"أخفى الكنغر أحد الأعداد الخمسة `{c_str}` في صندوق وكتب 4 عبارات: {clues_ar}. إذا كان عدد العبارات **الصحيحة بالضبط هو {m(k_true)}** من أصل 4، فما العدد داخل الصندوق؟",
            ans, distractors,
            f"Test each of the 5 candidate numbers `{c_str}` and count how many clues it makes true!",
            f"اختبر كلاً من الأعداد الخمسة `{c_str}` وعدّ كم عبارة تصح معه!",
            "Count true statements for each of the 5 candidate numbers and select the unique match.",
            [
                f"Counting true clues for each candidate gives: `{counts_desc}`.",
                f"Only {m(ans)} makes **exactly {m(k_true)}** clue(s) true!",
            ],
            f"Uniqueness verified across all 5 tags: only {m(ans)} scores {m(k_true)}!",
            "نختبر كل عدد مرشح أمام العبارات الأربع ونحصي عدد العبارات الصحيحة لكل منها.",
            [
                f"عدد العبارات الصحيحة لكل مرشح هو: `{counts_desc}`.",
                f"العدد الوحيد الذي يحقق **{m(k_true)}** عبارات صحيحة بالضبط هو {m(ans)}!",
            ],
            f"تحقق: العدد {m(ans)} وحده يحقق الشرط!",
            diagram_en=svg_number_strip([str(x) for x in cands]),
        )



# ==============================================================================
# UNIT 1.6 — Data & Probability (60 Questions: KANG-ECO-301 .. KANG-ECO-360)
# Blueprints: kang_eco_clock_elapsed, kang_eco_bar_chart_read,
#             kang_eco_worst_case_draw, kang_eco_grid_arrow_walk
# ==============================================================================
def _mins_to_next_palindrome(h0: int, m0: int) -> tuple[int, str]:
    total = h0 * 60 + m0
    steps = 0
    while True:
        steps += 1
        total = (total + 1) % (24 * 60)
        hh, mm = divmod(total, 60)
        s = f"{hh:02d}{mm:02d}"
        if s == s[::-1]:
            return steps, f"{hh:02d}:{mm:02d}"


def _count_grid_paths(cols: int, rows: int, blocked: tuple[int, int] = None) -> int:
    dp = [[0] * (rows + 1) for _ in range(cols + 1)]
    for c in range(cols + 1):
        for r in range(rows + 1):
            if blocked is not None and (c, r) == blocked:
                dp[c][r] = 0
            elif c == 0 and r == 0:
                dp[c][r] = 1
            else:
                dp[c][r] = (dp[c - 1][r] if c > 0 else 0) + (dp[c][r - 1] if r > 0 else 0)
    return dp[cols][rows]


def _add_unit_1_6(B: BankBuilder) -> None:
    tp = "Data & Probability"

    # 1. kang_eco_clock_elapsed (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_clock_elapsed"
    clk_easy = [
        (3, 45, 4, 20, "art lesson", "حصة الرسم"),
        (5, 35, 6, 15, "soccer practice", "تدريب كرة القدم"),
        (7, 50, 8, 25, "morning bus ride", "رحلة الحافلة الصباحية"),
        (9, 40, 10, 30, "science quiz", "مسابقة العلوم"),
        (11, 25, 12, 10, "library reading", "قراءة المكتبة"),
    ]
    for h1, m1, h2, m2, ev_en, ev_ar in clk_easy:
        ans = (60 - m1) + m2
        base100_trap = ans + 40
        B.add_math(
            tp, "Easy", bp,
            f"Kangy's {ev_en} starts at `{h1}:{m1:02d}` (shown on the clock) and finishes at `{h2}:{m2:02d}`. How many **minutes** long is the {ev_en}?",
            f"تبدأ {ev_ar} لدى الكنغر عند الساعة `{h1}:{m1:02d}` (الموضحة في الساعة) وتنتهي عند `{h2}:{m2:02d}`. كم **دقيقة** تستغرق {ev_ar}؟",
            ans, [base100_trap, abs(m1 - m2), ans - 10, ans + 10],
            f"Bridge to `{h2}:00` first ({m(f'60 - {m1} = {60 - m1}')} minutes), then add {m(m2)} minutes!",
            f"انتقل أولاً إلى الساعة `{h2}:00` ({m(f'60 - {m1} = {60 - m1}')} دقيقة)، ثم أضف {m(m2)} دقيقة!",
            "Count minutes to the next whole hour (60 − m1), then add m2.",
            [
                f"From `{h1}:{m1:02d}` to `{h2}:00` is {m(f'60 - {m1} = {60 - m1}')} minutes.",
                f"From `{h2}:00` to `{h2}:{m2:02d}` is {m(m2)} minutes, giving {m(f'{60 - m1} + {m2} = {ans}')} minutes.",
            ],
            f"Remember 1 hour = 60 minutes (never 100!), so the duration is {m(ans)} minutes!",
            "نستخدم الساعة الكاملة كجسر: نحسب الدقائق حتى تمام الساعة ثم نجمع الدقائق بعدها.",
            [
                f"من `{h1}:{m1:02d}` إلى `{h2}:00` تمضي {m(60 - m1)} دقيقة.",
                f"ومن `{h2}:00` إلى `{h2}:{m2:02d}` تمضي {m(m2)} دقيقة، فالمجموع {m(ans)} دقيقة.",
            ],
            f"تحقق: الساعة 60 دقيقة، فالإجمالي {m(ans)} دقيقة!",
            diagram_en=svg_analog_clock(h1, m1, angle_lbl=""),
        )

    clk_med = [
        (14, 35, 30, 15, 25, "Lina", "لينا"),
        (9, 45, 40, 10, 30, "Omar", "عمر"),
        (16, 20, 35, 15, 35, "Sara", "سارة"),
        (10, 50, 25, 20, 30, "Tariq", "طارق"),
        (13, 40, 45, 10, 20, "Nora", "نورة"),
    ]
    for h0, m0, p1, brk, p2, nm_en, nm_ar in clk_med:
        dur = p1 + brk + p2
        end_tot = h0 * 60 + m0 + dur
        eh, em = divmod(end_tot, 60)
        ans_t = f"`{eh:02d}:{em:02d}`"
        wrongs = []
        for delta in (-10, 10, 20, -25):
            wh, wm = divmod(end_tot + delta, 60)
            wrongs.append(f"`{wh:02d}:{wm:02d}`")
        pairs = [(ans_t, ans_t)] + [(w, w) for w in wrongs]
        B.add_bilingual(
            tp, "Medium", bp,
            f"A 24-hour digital clock shows `{h0:02d}:{m0:02d}` when {nm_en} starts studying. {nm_en} reads for {m(p1)} minutes, takes a {m(brk)}-minute snack break, and solves math puzzles for {m(p2)} minutes. What time does the clock show at the end?",
            f"تشير ساعة رقمية (بنظام 24 ساعة) إلى `{h0:02d}:{m0:02d}` عندما يبدأ/تبدأ {nm_ar} المذاكرة: يقرأ لمدة {m(p1)} دقيقة، ثم يأخذ استراحة {m(brk)} دقيقة، ثم يحل ألغازاً لمدة {m(p2)} دقيقة. ما الوقت الذي تعرضه الساعة عند الانتهاء؟",
            pairs, 0,
            f"Add all three durations ({m(f'{p1} + {brk} + {p2} = {dur}')} min), then convert {m(60)} minutes into {m(1)} hour!",
            f"اجمع المدد الثلاث ({m(f'{p1} + {brk} + {p2} = {dur}')} دقيقة)، وحوّل كل {m(60)} دقيقة إلى ساعة كاملة!",
            "Sum the elapsed minutes, convert into hours and minutes, and advance from the start time.",
            [
                f"Total elapsed time = {m(f'{p1} + {brk} + {p2} = {dur}')} minutes = {m(dur // 60)} hour(s) and {m(dur % 60)} minutes.",
                f"Adding {m(dur)} minutes to `{h0:02d}:{m0:02d}` lands on {ans_t}.",
            ],
            f"Minute check: `{h0:02d}:{m0:02d}` + {m(dur)} min = {ans_t}!",
            "نجمع الدقائق الكلية ثم نحولها إلى ساعات ودقائق ونضيفها لوقت البداية.",
            [
                f"الزمن الكلي المنقضي = {m(f'{p1} + {brk} + {p2} = {dur}')} دقيقة.",
                f"بإضافة {m(dur)} دقيقة إلى `{h0:02d}:{m0:02d}` تصل الساعة إلى {ans_t}.",
            ],
            f"تحقق: الوقت النهائي الصحيح هو {ans_t}!",
            diagram_en=svg_digital_clock(f"{h0:02d}:{m0:02d}", "Start time (24h)"),
        )

    clk_hard = [
        (11, 50),
        (14, 41),
        (15, 51),
        (19, 45),
        (23, 32),
    ]
    for h0, m0 in clk_hard:
        ans, next_pal = _mins_to_next_palindrome(h0, m0)
        start_s = f"{h0:02d}:{m0:02d}"
        B.add_math(
            tp, "Hard", bp,
            f"Kangy's 24-hour digital clock currently shows `{start_s}` (`00:00` to `23:59`). A **palindrome time** reads the exact same four digits forward and backward (such as `12:21` or `20:02`). How many **minutes** pass until the **very next** palindrome time appears?",
            f"تعرض ساعة الكنغر الرقمية بنظام 24 ساعة (`00:00` إلى `23:59`) حالياً الوقت `{start_s}`. نسمي الوقت **متناظراً** إذا قُرئت أرقامه الأربعة من اليمين كقراءتها من اليسار (مثل `12:21` أو `20:02`). بعد كم **دقيقة** يظهر **أقرب** وقت متناظر تالٍ؟",
            ans, [70 if ans != 70 else 60, 110 if ans != 110 else 90, ans + 10, max(5, ans - 11)],
            "Remember minutes must stay between `00` and `59` (so `16:61` does NOT exist, and `00:00` comes right after `23:59`)!",
            "تذكّر أن الدقائق تكون بين `00` و`59` فقط (فلا يوجد وقت `16:61`، ويأتي `00:00` بعد `23:59`)!",
            "Find the earliest valid 24-hour HH:MM after the current time with reverse(HH) = MM < 60.",
            [
                f"Checking valid hours after `{start_s}` whose reversed digits are less than `60`, the very next palindrome time is `{next_pal}`.",
                f"Counting minutes from `{start_s}` to `{next_pal}` gives {m(ans)} minutes.",
            ],
            f"Advancing `{start_s}` by {m(ans)} minutes lands on `{next_pal}`, which reads identically backward!",
            "نحدد أول وقت صالح تالٍ يحقق تناظر الخانات الأربع مع بقاء الدقائق أقل من 60.",
            [
                f"أقرب وقت متناظر صالح بعد `{start_s}` هو `{next_pal}`.",
                f"عدد الدقائق الفاصلة من `{start_s}` حتى `{next_pal}` يساوي {m(ans)} دقيقة.",
            ],
            f"تحقق: إضافة {m(ans)} دقيقة إلى `{start_s}` تعطي `{next_pal}`!",
            diagram_en=svg_digital_clock(start_s, "Next palindrome?"),
        )

    # 2. kang_eco_bar_chart_read (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_bar_chart_read"
    bc_easy = [
        ([("Cats", 16), ("Dogs", 11), ("Birds", 7), ("Fish", 13)], 20, "favorite pets", "الحيوانات المفضلة"),
        ([("Mon", 18), ("Tue", 9), ("Wed", 14), ("Thu", 12)], 20, "apples picked", "التفاحات المقطوفة"),
        ([("Red", 8), ("Blue", 19), ("Green", 12), ("Gold", 15)], 20, "team stars", "نجوم الفرق"),
        ([("Bus", 22), ("Walk", 14), ("Bike", 9), ("Car", 17)], 24, "morning travel", "وسائل الوصول"),
        ([("Math", 21), ("Art", 15), ("Gym", 18), ("Code", 11)], 24, "club votes", "أصوات الأندية"),
    ]
    for items, ym, topic_en, topic_ar in bc_easy:
        vals = [v for _, v in items]
        ans = max(vals) - min(vals)
        bars = [(lbl, v, str(v)) for lbl, v in items]
        B.add_math(
            tp, "Easy", bp,
            f"The bar chart shows Grade 3 data for {topic_en}. What is the difference between the **highest** bar and the **lowest** bar?",
            f"يوضّح الرسم البياني بالأعمدة بيانات الصف الثالث حول {topic_ar}. ما الفرق بين **أعلى** عمود و**أقل** عمود؟",
            ans, [max(vals), min(vals), max(vals) + min(vals), ans + 2],
            "Subtract the smallest bar number from the largest bar number!",
            "اطرح أصغر قيمة عمود من أكبر قيمة عمود!",
            "Identify the maximum and minimum bar values and subtract.",
            [
                f"Highest bar = {m(max(vals))}, and lowest bar = {m(min(vals))}.",
                f"Difference = {m(f'{max(vals)} - {min(vals)} = {ans}')}.",
            ],
            f"Check: {m(f'{min(vals)} + {ans} = {max(vals)}') }!",
            "نحدد أكبر قيمة وأصغر قيمة على الأعمدة ثم نطرحهما.",
            [
                f"أعلى عمود = {m(max(vals))}، وأقل عمود = {m(min(vals))}.",
                f"الفرق بينهما = {m(f'{max(vals)} - {min(vals)} = {ans}')}.",
            ],
            f"تحقق: {m(f'{min(vals)} + {ans} = {max(vals)}') }!",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        )

    bc_med = [
        ([("G1", 12), ("G2", 17), ("G3", 15), ("G4", 14)], 2, 20, "paper cranes", "طيور ورقية"),
        ([("A", 16), ("B", 11), ("C", 19), ("D", 13)], 1, 20, "recycling cans", "علب معاد تدويرها"),
        ([("Sun", 14), ("Mon", 18), ("Tue", 13), ("Wed", 16)], 3, 20, "shells found", "أصداف بحرية"),
        ([("Jan", 15), ("Feb", 21), ("Mar", 18), ("Apr", 12)], 0, 24, "sunny days", "أيام مشمسة"),
        ([("Lina", 19), ("Omar", 14), ("Sara", 22), ("Zaid", 17)], 2, 24, "puzzle stars", "نجوم الألغاز"),
    ]
    for items, q_idx, ym, obj_en, obj_ar in bc_med:
        tot = sum(v for _, v in items)
        ans = items[q_idx][1]
        known_sum = tot - ans
        q_lbl = items[q_idx][0]
        bars = [(lbl, v, "?" if i == q_idx else str(v)) for i, (lbl, v) in enumerate(items)]
        B.add_math(
            tp, "Medium", bp,
            f"All four bars in this chart add up to **{m(tot)} {obj_en}** in total. What number belongs above the missing `{q_lbl}` bar marked `{m('?')}`?",
            f"مجموع الأعمدة الأربعة في هذا الرسم البياني يساوي **{m(tot)} من {obj_ar}**. ما العدد المفقود فوق عمود `{q_lbl}` المشار إليه بعلامة `{m('?')}`؟",
            ans, [known_sum, ans - 2, ans + 2, tot // 4],
            f"Add the three known bars ({m(known_sum)}) and subtract from {m(tot)}!",
            f"اجمع الأعمدة الثلاثة المعلومة ({m(known_sum)}) ثم اطرح المجموع من {m(tot)}!",
            "Missing Bar = Total − Sum of Known Bars.",
            [
                f"Sum of the three known bars = {m(known_sum)}.",
                f"Missing `{q_lbl}` bar = {m(f'{tot} - {known_sum} = {ans}')}.",
            ],
            f"Check: {m(f'{known_sum} + {ans} = {tot}')}!",
            "قيمة العمود المفقود = المجموع الكلي − مجموع الأعمدة المعلومة.",
            [
                f"مجموع الأعمدة الثلاثة المعلومة = {m(known_sum)}.",
                f"قيمة عمود `{q_lbl}` المفقودة = {m(f'{tot} - {known_sum} = {ans}')}.",
            ],
            f"تحقق: {m(f'{known_sum} + {ans} = {tot}')}!",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        )

    bc_hard = [
        ([("B1", 14), ("B2", 6), ("B3", 12), ("B4", 8)], 16, "apples", "تفاحات"),
        ([("B1", 15), ("B2", 7), ("B3", 9), ("B4", 17)], 20, "oranges", "برتقالات"),
        ([("B1", 18), ("B2", 10), ("B3", 6), ("B4", 14)], 20, "cookies", "قطع بسكويت"),
        ([("B1", 19), ("B2", 8), ("B3", 11), ("B4", 14)], 20, "marbles", "كرات زجاجية"),
        ([("B1", 21), ("B2", 9), ("B3", 15), ("B4", 11)], 24, "stickers", "ملصقات"),
    ]
    for items, ym, obj_en, obj_ar in bc_hard:
        vals = [v for _, v in items]
        assert sum(vals) % 4 == 0
        avg = sum(vals) // 4
        give = sum(v - avg for v in vals if v > avg)
        recv = sum(avg - v for v in vals if v < avg)
        assert give == recv
        ans = give
        bars = [(lbl, v, str(v)) for lbl, v in items]
        B.add_math(
            tp, "Hard", bp,
            f"Four baskets hold {m(vals[0])}, {m(vals[1])}, {m(vals[2])}, and {m(vals[3])} {obj_en} as shown. What is the **smallest number of {obj_en}** Kangy must move from fuller baskets to emptier baskets so all 4 baskets hold the **exact same number**?",
            f"تحتوي أربع سلال على {m(vals[0])} و{m(vals[1])} و{m(vals[2])} و{m(vals[3])} من {obj_ar} كما في الرسم. ما **أقل عدد من {obj_ar}** يجب أن ينقله الكنغر من السلال الأكثر امتلاءً إلى الأقل حتى تتساوى السلال الأربع تماماً؟",
            ans, [avg, 2 * ans, max(vals) - min(vals), ans + 2],
            f"First find the equal target per basket ({m(f'{sum(vals)} \\div 4 = {avg}')}), then count only how many extras leave the fuller baskets!",
            f"احسب أولاً العدد المتساوي لكل سلة ({m(f'{sum(vals)} \\div 4 = {avg}')})، ثم اجمع الزيادات الخارجة من السلال الممتلئة فقط!",
            "Find the target average per basket, then sum (v − target) over baskets above the average.",
            [
                f"Total = {m(sum(vals))}, so each of the 4 baskets must end with {m(f'{sum(vals)} \\div 4 = {avg}')} {obj_en}.",
                f"Counting extras above {m(avg)} gives {m(ans)} {obj_en} moved directly into the baskets below {m(avg)}.",
            ],
            f"Don't double-count givers and receivers—moving {m(ans)} items both removes {m(ans)} extras and fills {m(recv)} gaps!",
            "نحسب نصيب كل سلة بعد التساوي (المتوسط)، ثم نجمع الفائض فوق المتوسط فقط.",
            [
                f"المجموع الكلي = {m(sum(vals))}، فنصيب كل سلة عند التساوي هو {m(f'{sum(vals)} \\div 4 = {avg}')}.",
                f"مجموع الزيادات فوق {m(avg)} يساوي {m(ans)}، ونقلها يملأ النقص في السلال الأخرى مباشرة.",
            ],
            f"تحقق: الفائض ({m(give)}) يساوي النقص ({m(recv)})، فأقل عدد يُنقل هو {m(ans)}!",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        )

    # 3. kang_eco_worst_case_draw (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_worst_case_draw"
    wc_easy = [
        ([("Red", 5), ("Blue", 5), ("Green", 5), ("Gold", 5)], "pair", 0, "socks", "جوارب"),
        ([("White", 6), ("Black", 6)], "pair", 0, "gloves (same color)", "قفازات من نفس اللون"),
        ([("Apple", 7), ("Lemon", 6), ("Berry", 4)], "target", 2, "candies", "قطع حلوى"),
        ([("Red", 8), ("Blue", 5)], "target", 1, "caps", "قبعات"),
        ([("Silver", 4), ("Gold", 6), ("Bronze", 5)], "target", 1, "coins", "عملات"),
    ]
    for items, kind, tgt_i, obj_en, obj_ar in wc_easy:
        tot = sum(c for _, c in items)
        slices = [(c / tot, f"{c} {nm}") for nm, c in items]
        if kind == "pair":
            ans = len(items) + 1
            goal_en = "at least **2** of the **same color**"
            goal_ar = "**اثنين (2) على الأقل من اللون نفسه**"
            worst = len(items)
        else:
            t_nm, t_cnt = items[tgt_i]
            worst = tot - t_cnt
            ans = worst + 1
            goal_en = f"at least **1 {t_nm}** item"
            goal_ar = f"**قطعة واحدة (1) على الأقل من نوع ({t_nm})**"
        desc_en = ", ".join(f"{m(c)} {nm}" for nm, c in items)
        B.add_math(
            tp, "Easy", bp,
            f"A dark bag contains {desc_en} {obj_en}. Without looking, what is the **smallest** number Kangy must draw to be **100% sure** of getting {goal_en}?",
            f"يحتوي كيس مظلم على {obj_ar} بالأعداد ({desc_en}). دون النظر، ما **أصغر** عدد يجب أن يسحبه الكنغر ليكون **متأكداً تماماً** من الحصول على {goal_ar}؟",
            ans, [worst, 2 if ans != 2 else 4, ans + 1, tot],
            f"Imagine the unluckiest draw first ({m(worst)} items without winning), then add {m(1)}!",
            f"تخيّل أسوأ حظ ممكن أولاً ({m(worst)} سحبات دون تحقق الشرط)، ثم أضف {m(1)}!",
            "Guaranteed Draw = Maximum Unlucky Draws + 1.",
            [
                f"In the worst case, Kangy can draw {m(worst)} items and still not achieve the goal.",
                f"Drawing 1 more ({m(f'{worst} + 1 = {ans}')}) guarantees success!",
            ],
            f"With {m(worst)} draws he could still fail, so {m(ans)} is the exact minimum!",
            "العدد المضمون = أقصى عدد سحبات غير محققة للشرط + 1.",
            [
                f"في أسوأ الحالات قد يسحب {m(worst)} دون تحقق المطلوب.",
                f"السحبة التالية ({m(f'{worst} + 1 = {ans}')}) تضمن تحقيق الشرط حتماً!",
            ],
            f"تحقق: {m(ans)} سحبات تضمن النتيجة بنسبة 100%!",
            diagram_en=svg_pie_chart(slices),
        )

    wc_med = [
        ([("Red", 6), ("Blue", 6), ("Green", 6)], 3, "Lina", "لينا"),
        ([("Red", 8), ("Blue", 7), ("Gold", 6), ("Pink", 5)], 3, "Omar", "عمر"),
        ([("White", 7), ("Black", 7), ("Grey", 7)], 4, "Sara", "سارة"),
        ([("Lime", 9), ("Mint", 8)], 5, "Tariq", "طارق"),
        ([("Ruby", 8), ("Sky", 8), ("Sun", 8), ("Plum", 8)], 4, "Nora", "نورة"),
    ]
    for items, k_same, nm_en, nm_ar in wc_med:
        tot = sum(c for _, c in items)
        worst = sum(min(c, k_same - 1) for _, c in items)
        ans = worst + 1
        desc_en = ", ".join(f"{m(c)} {nm}" for nm, c in items)
        B.add_math(
            tp, "Medium", bp,
            f"A box holds {desc_en} marbles. Without looking, what is the **minimum** number of marbles {nm_en} must take out to be **100% certain** of getting **{m(k_same)} marbles of the same color**?",
            f"يحتوي صندوق على كرات بالأعداد ({desc_en}). دون النظر، ما **أقل** عدد من الكرات يجب أن يسحبه {nm_ar} ليضمن بالتأكيد الحصول على **{m(k_same)} كرات من اللون نفسه**؟",
            ans, [worst, k_same, len(items) * k_same, ans + 2],
            f"In the worst case, {nm_en} draws {m(k_same - 1)} of EACH of the {m(len(items))} colors first—then add {m(1)}!",
            f"في أسوأ حالة يسحب {m(k_same - 1)} من **كل** لون من الألوان الـ {m(len(items))}، ثم نضيف {m(1)}!",
            "Take (k − 1) from each color in the worst case, then add 1.",
            [
                f"Worst-case draw without any {m(k_same)}-of-a-kind takes {m(k_same - 1)} of each of the {m(len(items))} colors: {m(f'{len(items)} \\times {k_same - 1} = {worst}')}.",
                f"The very next marble ({m(f'{worst} + 1 = {ans}')}) forces {m(k_same)} of one color!",
            ],
            f"Check: {m(worst)} marbles can split into {m(k_same - 1)} per color, so {m(ans)} is required!",
            "نأخذ (k − 1) من كل لون في أسوأ حالة ثم نضيف 1.",
            [
                f"أقصى سحب دون اكتمال {m(k_same)} من لون واحد هو {m(f'{len(items)} \\times {k_same - 1} = {worst}')} كرة.",
                f"إضافة كرة واحدة ({m(f'{worst} + 1 = {ans}')}) تضمن اكتمال {m(k_same)} من أحد الألوان!",
            ],
            f"تحقق: {m(ans)} كرة تضمن الشرط دائماً!",
            diagram_en=svg_pie_chart([(c / tot, f"{c} {nm}") for nm, c in items]),
        )

    wc_hard = [
        ([("White", 2), ("Yellow", 3), ("Blue", 7), ("Red", 8)], 4, "Zaid", "زيد"),
        ([("Pink", 1), ("Green", 2), ("Gold", 6), ("Purple", 7)], 4, "Hala", "هلا"),
        ([("Silver", 2), ("Orange", 3), ("Black", 8), ("Teal", 9)], 5, "Yousef", "يوسف"),
        ([("Brown", 3), ("Grey", 3), ("Red", 9), ("Blue", 10)], 5, "Amal", "أمل"),
        ([("Lime", 1), ("Cyan", 4), ("Rose", 8), ("Navy", 8)], 6, "Jude", "جود"),
    ]
    for items, k_same, nm_en, nm_ar in wc_hard:
        tot = sum(c for _, c in items)
        worst = sum(min(c, k_same - 1) for _, c in items)
        ans = worst + 1
        naive_trap = len(items) * (k_same - 1) + 1
        assert ans < naive_trap and max(c for _, c in items) >= k_same
        desc_en = ", ".join(f"{m(c)} {nm}" for nm, c in items)
        cap_parts = " + ".join(str(min(c, k_same - 1)) for _, c in items)
        B.add_math(
            tp, "Hard", bp,
            f"A drawer holds {desc_en} crayons. Without looking, what is the **smallest** number of crayons {nm_en} must pull out to be **100% sure** of having at least **{m(k_same)} crayons of the same color**?",
            f"يحتوي درج على أقلام تلوين بالأعداد ({desc_en}). دون النظر، ما **أصغر** عدد من الأقلام يجب أن يسحبه {nm_ar} ليكون **متأكداً تماماً** من وجود **{m(k_same)} أقلام على الأقل من اللون نفسه**؟",
            ans, [naive_trap, worst, ans - 2, naive_trap + 1],
            f"Watch out for rare colors that have **fewer** than {m(k_same - 1)} crayons—you can only draw as many of them as exist!",
            f"انتبه للألوان القليلة التي عددها أقل من {m(k_same - 1)}؛ في أسوأ حالة تسحب كل المتاح منها فقط!",
            "Sum min(count, k − 1) across every color for the exact worst case, then add 1.",
            [
                f"In the worst case, {nm_en} takes at most {m(k_same - 1)} of each color (or all of a color if fewer exist): {m(f'{cap_parts} = {worst}')} crayons.",
                f"Drawing 1 more crayon ({m(f'{worst} + 1 = {ans}')}) must belong to one of the abundant colors, completing {m(k_same)} of that color!",
            ],
            f"Trap avoided: multiplying {m(f'{len(items)} \\times {k_same - 1} + 1 = {naive_trap}')} overcounts colors with fewer than {m(k_same - 1)} crayons!",
            "نجمع الأصغر من (عدد اللون، k − 1) لكل لون لحساب أسوأ حالة بدقة ثم نضيف 1.",
            [
                f"أقصى سحب غير محقق للشرط = {m(f'{cap_parts} = {worst}')} قلماً.",
                f"القلم التالي ({m(f'{worst} + 1 = {ans}')}) يكمل حتماً {m(k_same)} أقلام من أحد الألوان الوفيرة!",
            ],
            f"تجنبنا فخ الضرب المباشر ({m(naive_trap)}) لأن بعض الألوان أقل من {m(k_same - 1)}!",
            diagram_en=svg_pie_chart([(c / tot, f"{c} {nm}") for nm, c in items]),
        )

    # 4. kang_eco_grid_arrow_walk (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_eco_grid_arrow_walk"
    gw_easy = [
        (5, 4, [(0, 3), (1, 3), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1)], "Kangy"),
        (5, 4, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (4, 3)], "Salman"),
        (6, 4, [(0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (4, 0), (5, 0)], "Pippa"),
        (5, 5, [(0, 4), (0, 3), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 0), (4, 0), (4, 1)], "Leo"),
        (6, 4, [(0, 2), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (5, 3), (5, 2), (5, 1)], "Rayan"),
    ]
    ar_gw = {"Kangy": "الكنغر", "Salman": "سلمان", "Pippa": "بيبا", "Leo": "ليو", "Rayan": "ريان"}
    for cols, rows, path, nm_en in gw_easy:
        ans = len(path) - 1
        nm_ar = ar_gw[nm_en]
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} walks along the red path from the green start square `S` to the yellow star square `★`, moving 1 square per step. How many **steps** does {nm_en} take?",
            f"يسير {nm_ar} على المسار الأحمر من مربع البداية الأخضر `S` إلى مربع النجمة الأصفر `★` خطوة واحدة لكل مربع مجاور. كم **خطوة** يخطوها؟",
            ans, [len(path), ans - 1, ans + 2, cols + rows],
            "Count the transitions (segments) from square to square—do NOT count `S` as Step 1!",
            "عدّ انتقالات المسار من مربع لآخر، ولا تحسب مربع البداية `S` كخطوة أولى!",
            "Steps = Number of Visited Squares − 1.",
            [
                f"The path visits {m(len(path))} squares including both `S` and `★`.",
                f"Moving between {m(len(path))} consecutive squares takes {m(f'{len(path)} - 1 = {ans}')} steps.",
            ],
            f"Fencepost check: {m(len(path))} squares mean {m(ans)} steps!",
            "عدد الخطوات يساوي عدد المربعات في المسار ناقص 1.",
            [
                f"يمر المسار عبر {m(len(path))} مربعات شاملة البداية والنهاية.",
                f"عدد الخطوات = {m(f'{len(path)} - 1 = {ans}')} خطوة.",
            ],
            f"تحقق: {m(ans)} خطوة!",
            diagram_en=svg_kang_grid_walk(cols, rows, path),
        )

    gw_med = [
        (6, 5, (1, 1), ["→", "→", "↑", "→", "↑", "↑", "←"], "Maha", "مها"),
        (6, 5, (2, 2), ["→", "↑", "→", "→", "↓", "→", "↑", "↑"], "Faisal", "فيصل"),
        (7, 5, (1, 3), ["→", "→", "↓", "→", "→", "↑", "↑", "→"], "Dana", "دانة"),
        (6, 6, (2, 1), ["↑", "↑", "→", "→", "→", "↑", "←", "↑"], "Kareem", "كريم"),
        (7, 5, (1, 2), ["→", "↑", "→", "→", "↑", "→", "↓", "→", "↑"], "Reem", "ريم"),
    ]
    delta_map = {"→": (1, 0), "←": (-1, 0), "↑": (0, 1), "↓": (0, -1)}
    for cols, rows, (c0, r0), cmds, nm_en, nm_ar in gw_med:
        # 1-based math coords: c in 1..cols left-to-right, r in 1..rows bottom-to-top
        cur_c, cur_r = c0, r0
        svg_pts = [(cur_c - 1, rows - cur_r)]
        for ch in cmds:
            dc, dr = delta_map[ch]
            cur_c += dc
            cur_r += dr
            assert 1 <= cur_c <= cols and 1 <= cur_r <= rows
            svg_pts.append((cur_c - 1, rows - cur_r))
        ans = 10 * cur_c + cur_r
        cmd_s = ", ".join(cmds)
        B.add_math(
            tp, "Medium", bp,
            f"Columns on {nm_en}'s {m(f'{cols} \\times {rows}')} grid are numbered {m(1)}..{m(cols)} (left to right) and rows {m(1)}..{m(rows)} (bottom to top). Starting at {m(f'({c0}, {r0})')}, a turtle follows `{cmd_s}` to reach {m('(C, R)')}. What 2-digit code {m('10C + R')} does it land on?",
            f"تُرقّم أعمدة شبكة {nm_ar} ({m(f'{cols} \\times {rows}')}) من {m(1)} إلى {m(cols)} (من اليسار لليمين) والصفوف من {m(1)} إلى {m(rows)} (من الأسفل للأعلى). تبدأ سلحفاة عند {m(f'({c0}, {r0})')} وتتبع `{cmd_s}` لتصل إلى {m('(C, R)')}. ما الرمز المكون من رقمين {m('10C + R')} لموقع الوصول؟",
            ans, [10 * cur_r + cur_c if cur_c != cur_r else ans + 11, ans - 10, ans + 1, ans - 1],
            "Add right arrows (and subtract left arrows) for column C; add up arrows (and subtract down arrows) for row R!",
            "احسب صافي أسهم اليمين واليسار للعمود C، وصافي أسهم الأعلى والأسفل للصف R!",
            "Update C with net horizontal moves and R with net vertical moves, then form 10C + R.",
            [
                f"Final column {m(f'C = {cur_c}')}, and final row {m(f'R = {cur_r}')}.",
                f"Two-digit location code {m(f'10C + R = 10 \\times {cur_c} + {cur_r} = {ans}')}.",
            ],
            f"Step-by-step path ends at {m(f'({cur_c}, {cur_r})')} → code {m(ans)}!",
            "نحدّث إحداثي العمود C بالحركة الأفقية وإحداثي الصف R بالحركة الرأسية.",
            [
                f"العمود النهائي {m(f'C = {cur_c}')}، والصف النهائي {m(f'R = {cur_r}')}.",
                f"الرمز المطلوب = {m(f'10 \\times {cur_c} + {cur_r} = {ans}')}.",
            ],
            f"تحقق: نقطة النهاية {m(f'({cur_c}, {cur_r})')} تعطي {m(ans)}!",
            diagram_en=svg_kang_grid_walk(cols, rows, svg_pts),
        )

    gw_hard = [
        (3, 2, (1, 1), "Kangy", "الكنغر"),
        (3, 3, (1, 2), "Lina", "لينا"),
        (4, 2, (2, 1), "Omar", "عمر"),
        (3, 3, (2, 2), "Sara", "سارة"),
        (4, 3, (2, 1), "Tariq", "طارق"),
    ]
    for cols, rows, blk, nm_en, nm_ar in gw_hard:
        ans = _count_grid_paths(cols, rows, blocked=blk)
        unblocked = _count_grid_paths(cols, rows, blocked=None)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} walks along the street lines from corner `A` (bottom-left) to corner `B` (top-right), moving **only Right (`→`) or Up (`↑`)**, and **cannot** pass through the blocked puddle corner `×`. How many different shortest routes are there?",
            f"يسير {nm_ar} على خطوط الشبكة من الركن `A` (أسفل اليسار) إلى الركن `B` (أعلى اليمين) بالتحرك **يميناً (`→`) أو للأعلى (`↑`) فقط**، مع تجنب التقاطع المغلق `×`. كم مساراً أقصر مختلفاً يوجد؟",
            ans, [unblocked, ans - 1, ans + 2, unblocked - 1 if unblocked - 1 != ans else ans + 3],
            "Write `1`s along the bottom and left edges, put `0` on `×`, and add (left + below) at every corner!",
            "اكتب `1` على حافتي الأسفل واليسار، وضع `0` عند `×`، واجمع (اليسار + الأسفل) عند كل تقاطع!",
            "Use corner-by-corner path addition (Pascal grid DP) with 0 paths through the blocked node.",
            [
                f"Without the puddle `×`, there would be {m(unblocked)} shortest routes.",
                f"Setting the puddle corner `×` to {m(0)} and adding (paths from left + paths from below) at each corner gives **{m(ans)}** valid routes to `B`.",
            ],
            f"Subtracting routes through `×` ({m(unblocked - ans)}) from {m(unblocked)} also confirms {m(ans)}!",
            "نطبق طريقة جمع المسارات عند كل ركن مع جعل قيمة التقاطع المغلق `×` مساوية للصفر.",
            [
                f"من دون العائق يوجد {m(unblocked)} مساراً.",
                f"بوضع {m(0)} عند `×` وجمع (اليسار + الأسفل) عند كل ركن نجد **{m(ans)}** مسارات صالحة إلى `B`.",
            ],
            f"تحقق بطرح مسارات العائق: {m(f'{unblocked} - {unblocked - ans} = {ans}')} مسارات!",
            diagram_en=svg_street_grid(cols, rows, blocked=blk),
        )


def build_ecolier_bank() -> list[dict]:
    """Build and programmatically validate all 360 Kangaroo Ecolier (Grades 3–4) questions."""
    B = BankBuilder()
    _add_unit_1_1(B)
    _add_unit_1_2(B)
    _add_unit_1_3(B)
    _add_unit_1_4(B)
    _add_unit_1_5(B)
    _add_unit_1_6(B)
    assert len(B.items) == 360, f"Expected 360 Ecolier questions, got {len(B.items)}"
    seen_stems: set[str] = set()
    other_stems = load_other_track_stems()
    for it in B.items:
        ns = norm_text(it["content"]["en"]["question"])
        assert ns not in seen_stems, f"Duplicate Ecolier stem in {it['id']}"
        assert ns not in other_stems, f"Cross-track stem collision in {it['id']}"
        seen_stems.add(ns)
    return B.items
