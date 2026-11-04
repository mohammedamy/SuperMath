"""Kangaroo Math Competition — PreEcolier Division (Grades 1–2) Question Bank — 360 Programmatically Verified Questions."""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from kangaroo_common import (
    DIFF_TO_POINTS,
    KANGAROO_FORBIDDEN_RE,
    ROOT,
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
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digital_clock,
    svg_digit_slots,
    svg_fenceposts,
    svg_fraction_grid,
    svg_function_machine,
    svg_kang_folded_ribbon,
    svg_kang_grid_walk,
    svg_kang_magic_cross,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_polyomino_board,
    svg_kang_stamp_grid,
    svg_number_strip,
    svg_polyomino,
    svg_pre_coin_purse,
    svg_pre_die_dots,
    svg_pre_icon_addition,
    svg_pre_marble_bag,
    svg_pre_paired_items,
    svg_pre_queue_line,
    svg_pre_shape_collage,
    svg_pre_tens_ones_blocks,
    svg_spinner,
    svg_street_grid,
    svg_subdivided_apex_triangle,
)

LEVEL = "PreEcolier"


class BankBuilder:
    """Sequential builder generating KANG-PRE-001 .. KANG-PRE-360 with full validation."""

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
        assert diagram_en and "<svg" in diagram_en, f"Missing SVG diagram for item #{len(self.items) + 1} ({blueprint})"
        qid = f"KANG-PRE-{len(self.items) + 1:03d}"
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
        assert diagram_en and "<svg" in diagram_en, f"Missing SVG diagram for item #{len(self.items) + 1} ({blueprint})"
        qid = f"KANG-PRE-{len(self.items) + 1:03d}"
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
# UNIT 1 — Number Theory (60 Questions: KANG-PRE-001 .. KANG-PRE-060)
# Blueprints: kang_pre_skip_counting_hops, kang_pre_two_digit_place_cards,
#             kang_pre_mini_brick_pyramids, kang_pre_even_odd_sock_gloves
# ==============================================================================
def _add_unit_1_1(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. kang_pre_skip_counting_hops (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_skip_counting_hops"
    hops_easy = [
        (4, 2, "Baby Kangy", "الكنغر الصغير", "garden stones", "حجارة الحديقة"),
        (5, 5, "Little Frog", "الضفدع الصغير", "lily pads", "أوراق الزنبق"),
        (3, 3, "Bunny Mimi", "الأرنبة ميمي", "carrot tiles", "بلاطات الجزر"),
        (6, 4, "Squirrel Nutty", "السنجاب نشيط", "tree stumps", "جذوع الأشجار"),
        (10, 10, "Cricket Pip", "الجندب بيب", "sidewalk squares", "مربعات الرصيف"),
    ]
    for s0, step, who_en, who_ar, item_en, item_ar in hops_easy:
        s1, s2, ans, s4 = s0 + step, s0 + 2 * step, s0 + 3 * step, s0 + 4 * step
        B.add_math(
            tp, "Easy", bp,
            f"{who_en} hops forward by the **same number** each time along five {item_en}: {m(s0)}, {m(s1)}, {m(s2)}, {m('?')}, {m(s4)}. Which number is hidden under {m('?')}?",
            f"يقفز {who_ar} إلى الأمام **بالعدد نفسه** في كل مرة فوق خمس من {item_ar}: {m(s0)}، {m(s1)}، {m(s2)}، {m('?')}، {m(s4)}. ما العدد المخفي مكان {m('?')}؟",
            ans, [ans - 1, ans + 1, ans + step, s2 + 1],
            f"Find how much the numbers grow from {m(s0)} to {m(s1)}, then add that jump to {m(s2)}!",
            f"اعرف مقدار الزيادة من {m(s0)} إلى {m(s1)}، ثم أضف هذه القفزة إلى {m(s2)}!",
            "Find the fixed skip-counting jump between neighbor stones and add it to the third stone.",
            [
                f"From {m(s0)} to {m(s1)}, each hop adds {m(f'{s1} - {s0} = {step}')} (check: {m(f'{s1} + {step} = {s2}')}).",
                f"Hopping {m(f'+{step}')} from {m(s2)} lands on {m(f'{s2} + {step} = {ans}')}.",
            ],
            f"One more hop gives {m(f'{ans} + {step} = {s4}')}, matching the last stone!",
            "نحسب مقدار القفزة الثابتة بين كل حجرين متجاورين ثم نضيفها إلى العدد الثالث.",
            [
                f"الفرق بين {m(s0)} و{m(s1)} هو {m(f'{s1} - {s0} = {step}')} (ومنه {m(f'{s1} + {step} = {s2}')}).",
                f"نضيف {m(step)} إلى {m(s2)} فنحصل على {m(f'{s2} + {step} = {ans}')}.",
            ],
            f"القفزة التالية تعطي {m(f'{ans} + {step} = {s4}')} وهو العدد الأخير تماماً!",
            diagram_en=svg_number_strip([str(s0), str(s1), str(s2), "?", str(s4)]),
        )

    hops_med = [
        (4, 20, "Lina's puppy", "جرو لينا"),
        (10, 30, "Omar's toy train", "قطار عمر اللعبة"),
        (36, 12, "Sara's paper boat", "قارب سارة الورقي"),
        (45, 25, "Tariq's wind-up robot", "روبوت طارق"),
        (7, 23, "Nora's hopping chick", "كتكوت نورة القافز"),
    ]
    for s_start, s_end, who_en, who_ar in hops_med:
        diff = s_end - s_start
        assert diff % 4 == 0
        step = diff // 4
        ans = s_start + 2 * step
        assert ans == (s_start + s_end) // 2
        dir_en = "increases" if step > 0 else "decreases"
        dir_ar = "يزداد" if step > 0 else "ينقص"
        abs_step = abs(step)
        op = "+" if step > 0 else "-"
        B.add_math(
            tp, "Medium", bp,
            f"Along this 5-box number strip, {who_en} makes **4 equal jumps** so the numbers change by the same amount from each box to the next. The first box is {m(s_start)} and the fifth box is {m(s_end)}. What number belongs in the middle box {m('?')}?",
            f"على شريط الأعداد المكوّن من 5 خانات، يتحرك {who_ar} **4 قفزات متساوية** بحيث {dir_ar} العدد بالمقدار نفسه من خانة لأخرى. الخانة الأولى {m(s_start)} والخامسة {m(s_end)}. ما العدد في الخانة الوسطى {m('?')}؟",
            ans, [ans + abs_step, ans - abs_step, ans + 2, s_start + abs_step],
            f"The middle box {m('?')} sits **halfway** between {m(s_start)} and {m(s_end)} (after 2 of the 4 equal jumps)!",
            f"الخانة الوسطى {m('?')} تقع في **منتصف المسافة** تماماً بين {m(s_start)} و{m(s_end)}!",
            "Find the total change across the 4 equal jumps, or take the number halfway between the ends.",
            [
                f"Going from {m(s_start)} to {m(s_end)} in 4 equal jumps covers a total difference of {m(abs(diff))}, so each jump {dir_en} by {m(abs_step)}.",
                f"After 2 jumps: {m(f'{s_start} {op} {abs_step} {op} {abs_step} = {ans}')}.",
            ],
            f"Full strip check: {m(f'{s_start}, {s_start + step}, {ans}, {s_start + 3*step}, {s_end}')}!",
            "نحسب مقدار التغير الكلي عبر 4 قفزات متساوية فنعرف مقدار كل قفزة.",
            [
                f"الفرق بين {m(s_start)} و{m(s_end)} هو {m(abs(diff))} موزعاً على 4 قفزات متساوية، أي {m(abs_step)} لكل قفزة.",
                f"بعد قفزتين نصل إلى الخانة الوسطى: {m(f'{s_start} {op} {abs_step} {op} {abs_step} = {ans}')}.",
            ],
            f"تحقق من الشريط كاملاً: {m(f'{s_start}، {s_start + step}، {ans}، {s_start + 3*step}، {s_end}')}!",
            diagram_en=svg_number_strip([str(s_start), "", "?", "", str(s_end)]),
        )

    hops_hard = [
        (2, 5, 2, 3, False, "Joey", "جوي"),
        (10, 6, 4, 4, False, "Zaid", "زيد"),
        (5, 4, 1, 3, True, "Hala", "هلا"),
        (8, 7, 3, 2, True, "Yousef", "يوسف"),
        (15, 5, 3, 5, False, "Amal", "أمل"),
    ]
    for s0, fwd, back, rounds, extra_fwd, nm_en, nm_ar in hops_hard:
        pos = s0
        trail = [pos]
        for _ in range(rounds):
            pos += fwd
            trail.append(pos)
            pos -= back
            trail.append(pos)
        if extra_fwd:
            pos += fwd
            trail.append(pos)
        ans = pos
        net = fwd - back
        assert ans == s0 + rounds * net + (fwd if extra_fwd else 0)
        if not extra_fwd:
            q_en = (
                f"{nm_en}'s toy kangaroo starts on stone {m(s0)}. In each round, it hops **{m(fwd)} forward** ({m(f'+{fwd}')}) and then slides **{m(back)} back** ({m(f'-{back}')}). "
                f"On which stone number does it land after **{m(rounds)} complete rounds**?"
            )
            q_ar = (
                f"يبدأ كنغر {nm_ar} اللعبة عند الحجر {m(s0)}. في كل جولة يقفز **{m(fwd)} للأمام** ({m(f'+{fwd}')}) ثم يتراجع **{m(back)} للخلف** ({m(f'-{back}')}). "
                f"على أي حجر يقف بعد إتمام **{m(rounds)} جولات كاملة**؟"
            )
        else:
            tot_moves = 2 * rounds + 1
            q_en = (
                f"{nm_en}'s frog starts at {m(s0)} and alternates moves: **1st move {m(f'+{fwd}')}**, **2nd move {m(f'-{back}')}**, **3rd move {m(f'+{fwd}')}**, **4th move {m(f'-{back}')}**, and so on. "
                f"On what number does the frog land right after its **{m(tot_moves)}th move**?"
            )
            q_ar = (
                f"تبدأ ضفدعة {nm_ar} عند العدد {m(s0)} وتتناوب حركاتها: **الحركة 1 هي {m(f'+{fwd}')}**، **الحركة 2 هي {m(f'-{back}')}**، **الحركة 3 هي {m(f'+{fwd}')}**، وهكذا. "
                f"على أي عدد تقف الضفدعة مباشرة بعد **حركتها رقم {m(tot_moves)}**؟"
            )
        B.add_math(
            tp, "Hard", bp, q_en, q_ar,
            ans, [s0 + rounds * fwd, ans + back, ans - net, ans + fwd],
            f"Each pair of moves ({m(f'+{fwd}')} then {m(f'-{back}')}) moves forward by {m(f'{fwd} - {back} = {net}')} in total!",
            f"كل زوج من الحركات ({m(f'+{fwd}')} ثم {m(f'-{back}')}) يقدّم الموقع بمقدار {m(f'{fwd} - {back} = {net}')}!",
            "Group each (+forward, -backward) pair into one net forward step, then add any final jump.",
            [
                f"One pair of moves ({m(f'+{fwd}')} followed by {m(f'-{back}')}) shifts the position by {m(f'{fwd} - {back} = +{net}')}.",
                (
                    f"After {m(rounds)} full rounds from {m(s0)}: {m(f'{s0} + {rounds} \\times {net} = {ans}')}."
                    if not extra_fwd
                    else f"After {m(rounds)} pairs ({m(2 * rounds)} moves) the frog is at {m(f'{s0} + {rounds} \\times {net} = {s0 + rounds * net}')}, and move {m(2 * rounds + 1)} adds {m(f'+{fwd}')} to reach {m(ans)}."
                ),
            ],
            f"Step-by-step positions: {', '.join(m(v) for v in trail)}!",
            "نجمع كل قفزة أمامية مع التراجع الذي يليها كخطوة صافية واحدة.",
            [
                f"كل جولة ({m(f'+{fwd}')} ثم {m(f'-{back}')}) تزيد الموقع بمقدار {m(f'{fwd} - {back} = {net}')}.",
                (
                    f"بعد {m(rounds)} جولات كاملة من {m(s0)} نصل إلى {m(f'{s0} + {rounds} \\times {net} = {ans}')}."
                    if not extra_fwd
                    else f"بعد {m(rounds)} أزواج ({m(2 * rounds)} حركات) نصل إلى {m(s0 + rounds * net)}، ثم تضيف الحركة الأخيرة {m(f'+{fwd}')} فنصل إلى {m(ans)}."
                ),
            ],
            f"تتبع الأعداد خطوة بخطوة: {' ← '.join(m(v) for v in trail)}!",
            diagram_en=svg_number_strip([str(s0), f"+{fwd}", f"-{back}", "...", "?"]),
        )

    # 2. kang_pre_two_digit_place_cards (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_two_digit_place_cards"
    pv_easy = [
        (3, 4, "Jude", "جود"),
        (5, 2, "Salman", "سلمان"),
        (2, 7, "Rayan", "ريان"),
        (6, 5, "Dana", "دانة"),
        (4, 8, "Karam", "كرم"),
    ]
    for tens, ones, nm_en, nm_ar in pv_easy:
        ans = 10 * tens + ones
        swap_v = 10 * ones + tens
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} places **{m(tens)} ten-rods** (towers of {m(10)}) and **{m(ones)} single cubes** on the math mat as shown. What two-digit number goes in the {m('?')} box?",
            f"يضع {nm_ar} على لوحة الحساب **{m(tens)} أعمدة عشرات** (في كل عمود {m(10)}) و**{m(ones)} مكعبات مفردة** كما في الرسم. ما العدد المكوّن من رقمين الذي يوضع في خانة {m('?')}؟",
            ans, [swap_v, tens + ones, ans + 10, ans - 1],
            f"Count by tens {m(tens)} times ({m(10 * tens)}), then count on {m(ones)} more ones!",
            f"عُدّ بالعشرات {m(tens)} مرات ({m(10 * tens)})، ثم أضف {m(ones)} آحاد!",
            "Combine the tens value (10 per rod) with the unit cubes.",
            [
                f"{m(tens)} ten-rods equal {m(10 * tens)}, and {m(ones)} unit cubes equal {m(ones)}.",
                f"Putting tens and ones together gives {m(f'{10 * tens} + {ones} = {ans}')}.",
            ],
            f"In {m(ans)}, the tens digit is {m(tens)} and the ones digit is {m(ones)}!",
            "نجمع قيمة أعمدة العشرات مع المكعبات المفردة للآحاد.",
            [
                f"{m(tens)} أعمدة عشرات تساوي {m(10 * tens)}، ولدينا {m(ones)} آحاد.",
                f"العدد الكلي هو {m(f'{10 * tens} + {ones} = {ans}')}.",
            ],
            f"في العدد {m(ans)} رقم العشرات {m(tens)} ورقم الآحاد {m(ones)}!",
            diagram_en=svg_pre_tens_ones_blocks(tens, ones, badge_lbl="?"),
        )

    pv_med = [
        (2, 7, 1, 5, "add", "Maya", "مايا"),
        (3, 6, 2, 8, "add", "Faris", "فارس"),
        (4, 8, 1, 6, "add", "Layan", "ليان"),
        (2, 6, 0, 0, "swap_diff", "Sami", "سامي"),
        (3, 8, 0, 0, "swap_num", "Tala", "تالا"),
    ]
    for tens, ones, dt, du, mode, nm_en, nm_ar in pv_med:
        base_v = 10 * tens + ones
        if mode == "add":
            ans = base_v + 10 * dt + du
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en} starts with the blocks shown ({m(tens)} ten-rods and {m(ones)} ones), then adds **{m(dt)} more ten-rod(s)** and **{m(du)} more unit cubes**. What number does {nm_en} have now?",
                f"لدى {nm_ar} المكعبات المرسومة ({m(tens)} عشرات و{m(ones)} آحاد)، ثم أضاف إليها **{m(dt)} من أعمدة العشرات** و**{m(du)} مكعبات آحاد**. ما العدد الجديد الآن؟",
                ans, [ans - 10, base_v + dt + du, ans + 1, ans - 1],
                f"Notice {m(f'{ones} + {du} = {ones + du}')} ones makes a new bundle of {m(10)} plus {m((ones + du) % 10)} leftover ones!",
                f"لاحظ أن {m(f'{ones} + {du} = {ones + du}')} آحاد تكوّن عشرة جديدة ويبقى {m((ones + du) % 10)} آحاد!",
                "Add the starting two-digit number and the newly added tens and ones (regrouping 10 ones into 1 ten).",
                [
                    f"The pictured blocks show {m(f'{10 * tens} + {ones} = {base_v}')}.",
                    f"Adding {m(dt)} ten(s) ({m(10 * dt)}) and {m(du)} ones gives {m(f'{base_v} + {10 * dt} + {du} = {ans}')}.",
                ],
                f"Regrouping check: {m(tens + dt)} tens + {m(ones + du)} ones = {m(f'{10 * (tens + dt)} + {ones + du} = {ans}')}!",
                "نحسب العدد المرسوم أولاً ثم نضيف العشرات والآحاد الجديدة مع تجميع كل 10 آحاد في عشرة.",
                [
                    f"المكعبات المرسومة تمثل {m(f'{10 * tens} + {ones} = {base_v}')}.",
                    f"نضيف {m(10 * dt)} و{m(du)} فنحصل على {m(f'{base_v} + {10 * dt} + {du} = {ans}')}.",
                ],
                f"تحقق بالتجميع: {m(tens + dt)} عشرات + {m(ones + du)} آحاد = {m(ans)}!",
                diagram_en=svg_pre_tens_ones_blocks(tens, ones, badge_lbl="New: ?"),
            )
        elif mode == "swap_diff":
            swapped = 10 * ones + tens
            ans = swapped - base_v
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en} builds the number shown ({m(tens)} tens and {m(ones)} ones), then **swaps** the tens and ones to make {m(ones)} tens and {m(tens)} ones. How much **bigger** is the new number than the starting number?",
                f"يبني {nm_ar} العدد المرسوم ({m(tens)} عشرات و{m(ones)} آحاد)، ثم **يبدّل** العشرات والآحاد ليصبح لديه {m(ones)} عشرات و{m(tens)} آحاد. بكم يزيد العدد الجديد عن العدد الأول؟",
                ans, [swapped, base_v, ans - 9, ans + 9],
                f"Write both two-digit numbers ({m(swapped)} and {m(base_v)}) and subtract the smaller from the larger!",
                f"اكتب العددين ({m(swapped)} و{m(base_v)}) ثم اطرح الأصغر من الأكبر!",
                "Find the original number and the digit-swapped number, then subtract.",
                [
                    f"Starting number = {m(base_v)}, and swapped number = {m(swapped)}.",
                    f"Difference = {m(f'{swapped} - {base_v} = {ans}')}.",
                ],
                f"Check by adding back: {m(f'{base_v} + {ans} = {swapped}')}!",
                "نكتب العدد الأصلي والعدد بعد تبديل الرقمين ثم نطرحهما.",
                [
                    f"العدد الأول هو {m(base_v)}، وبعد التبديل يصبح {m(swapped)}.",
                    f"مقدار الزيادة = {m(f'{swapped} - {base_v} = {ans}')}.",
                ],
                f"تحقق بالجمع العكسي: {m(f'{base_v} + {ans} = {swapped}')}!",
                diagram_en=svg_pre_tens_ones_blocks(tens, ones, badge_lbl="Diff: ?"),
            )
        else:
            swapped = 10 * ones + tens
            ans = swapped - 10
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en} sees {m(tens)} ten-rods and {m(ones)} ones on the tray, swaps the tens digit and ones digit, and then takes away **{m(1)} ten-rod**. What number does {nm_en} get?",
                f"ترى {nm_ar} على اللوحة {m(tens)} عشرات و{m(ones)} آحاد، فتبدّل رقمي العشرات والآحاد، ثم تزيل **عمود عشرات واحد ({m(10)})**. ما العدد الناتج؟",
                ans, [swapped, base_v - 10, swapped + 10, ans - 1],
                f"Swapping {m(base_v)} gives {m(swapped)}; now subtract {m(10)}!",
                f"تبديل رقمي {m(base_v)} يعطي {m(swapped)}، ثم اطرح {m(10)}!",
                "Swap the digits of the starting number first, then subtract 10.",
                [
                    f"The blocks show {m(base_v)}. Swapping its digits gives {m(swapped)}.",
                    f"Removing {m(1)} ten-rod subtracts {m(10)}: {m(f'{swapped} - 10 = {ans}')}.",
                ],
                f"Check: {m(swapped)} has {m(ones)} tens; taking {m(1)} ten leaves {m(ones - 1)} tens and {m(tens)} ones = {m(ans)}!",
                "نبدّل رقمي العدد المرسوم أولاً ثم ننقص عشرة واحدة.",
                [
                    f"العدد المرسوم {m(base_v)} يصبح بعد التبديل {m(swapped)}.",
                    f"إزالة عمود عشرات تعني طرح {m(10)}: {m(f'{swapped} - 10 = {ans}')}.",
                ],
                f"تحقق: {m(ones - 1)} عشرات و{m(tens)} آحاد تعطي {m(ans)}!",
                diagram_en=svg_pre_tens_ones_blocks(tens, ones, badge_lbl="Swap-10"),
            )

    pv_hard = [
        ((1, 4, 7), "diff", "Kangy", "الكنغر"),
        ((2, 5, 8), "diff", "Lina", "لينا"),
        ((0, 3, 8), "diff", "Omar", "عمر"),
        ((0, 2, 7), "sum_small", "Sara", "سارة"),
        ((2, 6, 9), "diff", "Tariq", "طارق"),
    ]
    for cards, hmode, nm_en, nm_ar in pv_hard:
        two_digs = sorted({10 * a + b for i, a in enumerate(cards) for j, b in enumerate(cards) if i != j and a != 0})
        smallest, second_smallest, largest = two_digs[0], two_digs[1], two_digs[-1]
        c_lbls = [str(c) for c in cards]
        if hmode == "diff":
            ans = largest - smallest
            zero_trap = 10 * cards[0] + cards[1] if cards[0] == 0 else smallest - 1
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} has three digit cards: {m(cards[0])}, {m(cards[1])}, and {m(cards[2])}. Using **two different cards** at a time (a two-digit number cannot start with {m(0)}!), what is the **difference** between the **largest** and **smallest** two-digit numbers {nm_en} can make?",
                f"لدى {nm_ar} ثلاث بطاقات أرقام: {m(cards[0])} و{m(cards[1])} و{m(cards[2])}. باستعمال **بطاقتين مختلفتين** في كل مرة (العدد المكوّن من رقمين لا يبدأ بـ {m(0)}!)، ما **الفرق** بين **أكبر** عدد و**أصغر** عدد من رقمين يمكن تكوينهما؟",
                ans, [largest - zero_trap if zero_trap != smallest else ans + 9, largest, smallest, ans - 9],
                f"Put the biggest digit in the tens place for the largest number ({m(largest)}), and the smallest non-zero digit in the tens place for the smallest ({m(smallest)})!",
                f"ضع أكبر رقم في العشرات لتحصل على الأكبر ({m(largest)})، وأصغر رقم غير صفري في العشرات لتحصل على الأصغر ({m(smallest)})!",
                "Form the largest and smallest valid 2-digit numbers from the given cards, then subtract.",
                [
                    f"Largest two-digit number uses the two biggest digits in order: {m(largest)}.",
                    f"Smallest valid two-digit number cannot start with {m(0)}, so it is {m(smallest)}.",
                    f"Difference = {m(f'{largest} - {smallest} = {ans}')}.",
                ],
                f"All valid 2-digit numbers here are {', '.join(m(x) for x in two_digs)}; {m(f'{largest} - {smallest} = {ans}')}!",
                "نكوّن أكبر عدد وأصغر عدد صالح من رقمين من البطاقات ثم نطرحهما.",
                [
                    f"أكبر عدد من رقمين هو {m(largest)}.",
                    f"أصغر عدد صالح من رقمين (لا يبدأ بالصفر) هو {m(smallest)}.",
                    f"الفرق بينهما = {m(f'{largest} - {smallest} = {ans}')}.",
                ],
                f"جميع الأعداد الصالحة هي {', '.join(m(x) for x in two_digs)}، وفعلاً {m(f'{largest} - {smallest} = {ans}')}!",
                diagram_en=svg_number_strip(c_lbls),
            )
        else:
            ans = smallest + second_smallest
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} has the three digit cards {m(cards[0])}, {m(cards[1])}, and {m(cards[2])}. What is the **sum** of the **two smallest** valid two-digit numbers {nm_en} can build using two different cards each time (remember a two-digit number never starts with {m(0)})?",
                f"تحمل {nm_ar} ثلاث بطاقات أرقام: {m(cards[0])} و{m(cards[1])} و{m(cards[2])}. ما **مجموع أصغر عددين** صالحين مكوّنين من رقمين مختلفين من هذه البطاقات (تذكّر أن العشرات لا تساوي {m(0)})؟",
                ans, [smallest + (10 * cards[0] + cards[2]), smallest + largest, ans + 10, ans - 7],
                f"Neither number can start with {m(0)}, so start with {m(cards[1])} in the tens place first!",
                f"لا يمكن البدء بـ {m(0)} في العشرات، لذا ابدأ بوضع {m(cards[1])} في خانة العشرات!",
                "List all valid 2-digit numbers in order and add the smallest two.",
                [
                    f"All valid 2-digit numbers from {m(cards[0])}, {m(cards[1])}, {m(cards[2])} are {', '.join(m(x) for x in two_digs)}.",
                    f"The two smallest are {m(smallest)} and {m(second_smallest)}, and their sum is {m(f'{smallest} + {second_smallest} = {ans}')}.",
                ],
                f"Check: {m(f'{smallest} + {second_smallest} = {ans}')}, well under {m(99)}!",
                "نرتب الأعداد الصالحة من الأصغر للأكبر ثم نجمع أول عددين.",
                [
                    f"الأعداد الصالحة المكوّنة من رقمين هي: {', '.join(m(x) for x in two_digs)}.",
                    f"أصغر عددين هما {m(smallest)} و{m(second_smallest)}، ومجموعهما {m(f'{smallest} + {second_smallest} = {ans}')}.",
                ],
                f"تحقق: {m(f'{smallest} + {second_smallest} = {ans}')}!",
                diagram_en=svg_number_strip(c_lbls),
            )

    # 3. kang_pre_mini_brick_pyramids (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_mini_brick_pyramids"
    pyr_easy = [
        (2, 3, 4, "Joey", "جوي"),
        (5, 2, 6, "Mimi", "ميمي"),
        (3, 6, 2, "Koko", "كوكو"),
        (4, 5, 5, "Bibi", "بيبي"),
        (7, 4, 5, "Toto", "توتو"),
    ]
    for a, b, c, nm_en, nm_ar in pyr_easy:
        ml, mr = a + b, b + c
        ans = ml + mr
        B.add_math(
            tp, "Easy", bp,
            f"In Grade 1 block play, {nm_en} stacks foam bricks so every upper brick shows the **sum** of the two bricks touching it underneath. The bottom row has {m(a)}, {m(b)}, and {m(c)}. Which number goes on the top yellow brick {m('?')}?",
            f"في ركن المكعبات بالصف الأول، يرتب {nm_ar} طوبات إسفنجية بحيث يساوي العدد في كل طوبة علوية **مجموع** الطوبتين أسفلها مباشرة. إذا كان الصف السفلي {m(a)} و{m(b)} و{m(c)}، فما العدد في طوبة القمة الصفراء {m('?')}؟",
            ans, [a + b + c, ans - b, ans + 2, ml + c],
            f"Fill the two blank middle bricks first: {m(f'{a} + {b}')} on the left and {m(f'{b} + {c}')} on the right!",
            f"املأ طوبتي الصف الأوسط أولاً: {m(f'{a} + {b}')} يساراً و{m(f'{b} + {c}')} يميناً!",
            "Add neighbor pairs in the bottom row to get the middle row, then add the two middle bricks.",
            [
                f"Middle-left brick = {m(f'{a} + {b} = {ml}')}, and middle-right brick = {m(f'{b} + {c} = {mr}')}.",
                f"Top brick {m('?')} = {m(f'{ml} + {mr} = {ans}')}.",
            ],
            f"Quick check: {m(b)} is added into both sides, so {m(f'{a} + {b} + {b} + {c} = {ans}')}!",
            "نجمع كل طوبتين متجاورتين في القاعدة لإيجاد الصف الأوسط ثم نجمع طوبتي الوسط.",
            [
                f"طوبة الوسط اليسرى = {m(f'{a} + {b} = {ml}')}، واليمنى = {m(f'{b} + {c} = {mr}')}.",
                f"طوبة القمة {m('?')} = {m(f'{ml} + {mr} = {ans}')}.",
            ],
            f"تحقق سريع: {m(f'{a} + {b} + {b} + {c} = {ans}')}!",
            diagram_en=svg_kang_number_pyramid([["?"], ["", ""], [str(a), str(b), str(c)]]),
        )

    pyr_med = [
        (3, 4, 5, "crayon", "الألوان"),
        (2, 6, 4, "seashell", "الأصداف"),
        (5, 3, 7, "acorn", "البلوط"),
        (4, 7, 2, "pebble", "الحصى"),
        (6, 5, 8, "star", "النجوم"),
    ]
    for a, b, c, theme_en, theme_ar in pyr_med:
        top = a + 2 * b + c
        rem = top - a - c
        assert rem == 2 * b
        B.add_math(
            tp, "Medium", bp,
            f"In this 3-row {theme_en} number wall, each brick equals the sum of the two bricks right under it. The top brick is {m(top)}, and the bottom row shows {m(a)}, {m('?')}, and {m(c)}. What number belongs in {m('?')}?",
            f"في جدار {theme_ar} العددي ذي 3 صفوف، كل طوبة تساوي مجموع الطوبتين تحتها مباشرة. إذا كانت القمة {m(top)}، والصف السفلي {m(a)} و{m('?')} و{m(c)}، فما العدد في {m('?')}؟",
            b, [rem, b + 1, max(1, b - 1), top - a - b],
            f"The middle bottom brick {m('?')} gets counted **twice** in the top sum! Take away {m(a)} and {m(c)} from {m(top)}, then take half!",
            f"طوبة الوسط السفلية {m('?')} تُحسب **مرتين** عند القمة! اطرح {m(a)} و{m(c)} من {m(top)} ثم خذ النصف!",
            "Subtract the two bottom corner numbers from the top number, then split the result into two equal halves.",
            [
                f"The top brick equals {m(a)} + {m('?')} + {m('?')} + {m(c)} = {m(top)}.",
                f"Subtracting the corners {m(f'{a} + {c} = {a + c}')} from {m(top)} leaves {m(f'{top} - {a + c} = {rem}')} for the two copies of {m('?')}.",
                f"Half of {m(rem)} is {m(b)}, so {m('?')} = {m(b)}.",
            ],
            f"Check: middle bricks are {m(f'{a}+{b}={a+b}')} and {m(f'{b}+{c}={b+c}')}, and {m(f'{a+b} + {b+c} = {top}')}!",
            "نطرح ركني القاعدة من عدد القمة، ثم نقسم الباقي إلى نصفين متساويين.",
            [
                f"القمة تساوي {m(a)} + {m('?')} + {m('?')} + {m(c)} = {m(top)}.",
                f"نطرح الركنين {m(f'{a} + {c} = {a + c}')} من {m(top)} فيتبقى {m(f'{top} - {a + c} = {rem}')}.",
                f"نصف العدد {m(rem)} هو {m(b)}، إذن {m('?')} = {m(b)}.",
            ],
            f"تحقق: الصف الأوسط {m(a + b)} و{m(b + c)}، ومجموعهما {m(f'{a+b} + {b+c} = {top}')}!",
            diagram_en=svg_kang_number_pyramid([[str(top)], ["", ""], [str(a), "?", str(c)]]),
        )

    pyr_hard = [
        (2, 3, 1, 4, "Dana", "دانة"),
        (1, 4, 2, 3, "Karam", "كرم"),
        (3, 2, 4, 1, "Maya", "مايا"),
        (4, 1, 3, 2, "Faris", "فارس"),
        (2, 5, 2, 1, "Tala", "تالا"),
    ]
    for a, b, c, d, nm_en, nm_ar in pyr_hard:
        r3_l, r3_m, r3_r = a + b, b + c, c + d
        r2_l, r2_r = r3_l + r3_m, r3_m + r3_r
        top = r2_l + r2_r
        B.add_math(
            tp, "Hard", bp,
            f"In {nm_en}'s 4-row mini brick tower, each brick is the sum of the two bricks right below it. The top brick is {m(top)}, the brick below it on the left is {m(r2_l)}, and the bottom row is {m(a)}, {m('?')}, {m(c)}, {m(d)}. What number goes in {m('?')}?",
            f"في برج الطوب الصغير ذي 4 صفوف لدى {nm_ar}، كل طوبة تساوي مجموع الطوبتين أسفلها مباشرة. إذا كانت القمة {m(top)}، والطوبة أسفلها يساراً {m(r2_l)}، والصف السفلي {m(a)} و{m('?')} و{m(c)} و{m(d)}، فما العدد في {m('?')}؟",
            b, [r3_m, b + 1, b + 2, max(1, b - 1)],
            f"First subtract {m(f'{top} - {r2_l}')} to get the right brick in row 2, and add {m(f'{c} + {d}')} on the bottom right!",
            f"اطرح أولاً {m(f'{top} - {r2_l}')} لمعرفة الطوبة اليمنى في الصف الثاني، واجمع {m(f'{c} + {d}')} أسفل اليمين!",
            "Work down the right side of the tower using simple subtraction and addition.",
            [
                f"In the 2nd row from the top, the right brick is {m(f'{top} - {r2_l} = {r2_r}')}.",
                f"In the 3rd row, the rightmost brick is {m(f'{c} + {d} = {r3_r}')}, so the middle brick next to it is {m(f'{r2_r} - {r3_r} = {r3_m}')}.",
                f"Since that middle brick equals {m('?')} + {m(c)} = {m(r3_m)}, we get {m('?')} = {m(f'{r3_m} - {c} = {b}')}.",
            ],
            f"Left-side check: {m(f'{a} + {b} = {r3_l}')}, and {m(f'{r3_l} + {r3_m} = {r2_l}')}!",
            "ننزل خطوة بخطوة على الجهة اليمنى من البرج باستعمال الجمع والطرح.",
            [
                f"الطوبة اليمنى في الصف الثاني من الأعلى = {m(f'{top} - {r2_l} = {r2_r}')}.",
                f"في الصف الثالث طوبة أقصى اليمين = {m(f'{c} + {d} = {r3_r}')}، فتكون طوبة الوسط بجوارها {m(f'{r2_r} - {r3_r} = {r3_m}')}.",
                f"وبما أن {m('?')} + {m(c)} = {m(r3_m)} فإن {m('?')} = {m(f'{r3_m} - {c} = {b}')}.",
            ],
            f"تحقق من اليسار: {m(f'{a} + {b} = {r3_l}')}، و{m(f'{r3_l} + {r3_m} = {r2_l}')}!",
            diagram_en=svg_kang_number_pyramid([[str(top)], [str(r2_l), ""], ["", "", ""], [str(a), "?", str(c), str(d)]]),
        )

    # 4. kang_pre_even_odd_sock_gloves (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_even_odd_sock_gloves"
    sock_easy = [
        (5, 4, "striped socks", "جوارب مخططة", "Lina", "لينا"),
        (7, 6, "blue mittens", "قفازات صوفية زرقاء", "Omar", "عمر"),
        (6, 5, "rain boots", "أحذية مطر", "Sara", "سارة"),
        (9, 4, "fuzzy slippers", "نعال ناعمة", "Tariq", "طارق"),
        (8, 7, "skating shoes", "أحذية تزلج", "Nora", "نورة"),
    ]
    for a, b, item_en, item_ar, nm_en, nm_ar in sock_easy:
        tot = a + b
        ans = tot // 2
        rem = tot % 2
        B.add_math(
            tp, "Easy", bp,
            f"Box A shows **{m(a)}** identical {item_en}, and a closed laundry bag holds **{m(b)}** more of the exact same {item_en}. When {nm_en} puts them all together, how many **complete pairs of {m(2)}** can {nm_en} make?",
            f"يظهر في الصندوق A عدد **{m(a)}** من {item_ar} المتماثلة، وفي كيس الغسيل المغلق **{m(b)}** أخرى مماثلة لها. عندما يجمعها {nm_ar} كلها معاً، كم **زوجاً كاملاً (من {m(2)})** يمكنه تكوينه؟",
            ans, [tot, ans + 1, max(1, ans - 1), a // 2 + b // 2 if (a % 2 and b % 2) else ans + 2],
            f"Add {m(f'{a} + {b} = {tot}')} first, then group {m(tot)} by twos!",
            f"اجمع {m(f'{a} + {b} = {tot}')} أولاً، ثم قسّمها إلى أزواج اثنين اثنين!",
            "Find the total count of items, then count how many groups of 2 fit inside.",
            [
                f"Total items altogether = {m(f'{a} + {b} = {tot}')}.",
                f"Grouping {m(tot)} into twos gives **{m(ans)}** complete pairs" + (f" (with {m(rem)} single item left over)." if rem else " with none left over."),
            ],
            f"Check: {m(f'{ans} \\times 2 + {rem} = {tot}')}!",
            "نجمع العدد الكلي أولاً ثم نحسب عدد الأزواج الكاملة (كل زوج من قطعتين).",
            [
                f"المجموع الكلي = {m(f'{a} + {b} = {tot}')}.",
                f"بتكوين مجموعات من {m(2)} نحصل على **{m(ans)}** أزواج كاملة" + (f" (وتبقى قطعة مفردة واحدة)." if rem else "."),
            ],
            f"تحقق: {m(f'{ans} \\times 2 + {rem} = {tot}')}!",
            diagram_en=svg_pre_paired_items(a, caption="Box A"),
        )

    sock_med = [
        (7, 4, 8, "Kangy", "الكنغر"),
        (5, 6, 9, "Zaid", "زيد"),
        (9, 2, 8, "Hala", "هلا"),
        (6, 5, 10, "Yousef", "يوسف"),
        (8, 3, 9, "Amal", "أمل"),
    ]
    for a, b, target_pairs, nm_en, nm_ar in sock_med:
        goal_tot = 2 * target_pairs
        have = a + b
        ans = goal_tot - have
        assert ans > 0
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} has **{m(a)}** identical mittens on the bench (shown) and **{m(b)}** more in a drawer. How many **more single mittens** does {nm_en} need so there are enough to make **exact {m(target_pairs)} complete pairs**?",
            f"لدى {nm_ar} عدد **{m(a)}** قفازات متماثلة على الطاولة (كما في الرسم) و**{m(b)}** أخرى في الدرج. كم **قفازاً مفرداً إضافياً** يحتاج ليكون لديه ما يكفي لتكوين **{m(target_pairs)} أزواج كاملة بالضبط**؟",
            ans, [target_pairs - have // 2, ans + 2, max(1, ans - 1), goal_tot],
            f"{m(target_pairs)} pairs means {m(f'2 \\times {target_pairs} = {goal_tot}')} single mittens in all!",
            f"{m(target_pairs)} أزواج تعني {m(f'2 \\times {target_pairs} = {goal_tot}')} قفازاً مفرداً في المجموع!",
            "Multiply the target pairs by 2 to get total mittens needed, then subtract the mittens already owned.",
            [
                f"To make {m(target_pairs)} complete pairs, {nm_en} needs {m(f'{target_pairs} + {target_pairs} = {goal_tot}')} mittens.",
                f"Right now {nm_en} has {m(f'{a} + {b} = {have}')} mittens, so {m(f'{goal_tot} - {have} = {ans}')} more single mittens are needed.",
            ],
            f"Check: {m(f'{have} + {ans} = {goal_tot}')} mittens = {m(target_pairs)} pairs!",
            "نحسب عدد القفازات اللازمة للأزواج المطلوبة (ضعف عدد الأزواج) ثم نطرح الموجود.",
            [
                f"لتكوين {m(target_pairs)} أزواج كاملة نحتاج {m(f'{target_pairs} + {target_pairs} = {goal_tot}')} قفازاً.",
                f"الموجود حالياً {m(f'{a} + {b} = {have}')}، فيحتاج {m(f'{goal_tot} - {have} = {ans}')} قفازات مفردة إضافية.",
            ],
            f"تحقق: {m(f'{have} + {ans} = {goal_tot}')} قفازاً تكوّن {m(target_pairs)} أزواج!",
            diagram_en=svg_pre_paired_items(a, caption="Bench"),
        )

    sock_hard = [
        (4, 7, 3, 2, "pairs", "Jude", "جود"),
        (6, 3, 2, 4, "pairs", "Salman", "سلمان"),
        (5, 8, 4, 3, "pairs", "Rayan", "ريان"),
        (7, 4, 5, 2, "leftover", "Dana", "دانة"),
        (3, 6, 2, 5, "leftover", "Karam", "كرم"),
    ]
    for l1, r1, l2, r2, hmode, nm_en, nm_ar in sock_hard:
        L = l1 + l2
        R = r1 + r2
        pairs = min(L, R)
        unmatched = abs(L - R)
        if hmode == "pairs":
            ans = pairs
            B.add_math(
                tp, "Hard", bp,
                f"A wearable pair of winter gloves needs **1 Left glove** and **1 Right glove**. {nm_en} has {m(l1)} Left gloves and {m(r1)} Right gloves on a shelf, then finds {m(l2)} more Left gloves and {m(r2)} more Right gloves in a coat basket. How many **wearable Left–Right pairs** can {nm_en} make?",
                f"يتكوّن زوج القفازات الصحيح من **قفاز أيسر واحد** و**قفاز أيمن واحد**. لدى {nm_ar} على الرف {m(l1)} قفازات يسرى و{m(r1)} قفازات يمنى، ثم وجد في السلة {m(l2)} يسرى و{m(r2)} يمنى إضافية. كم **زوجاً صالحاً للارتداء (يمين + يسار)** يمكنه تكوينه؟",
                ans, [(L + R) // 2, max(L, R), ans + 1, max(1, ans - 1)],
                f"Add all Left gloves together and all Right gloves together — you cannot pair two Right gloves with each other!",
                f"اجمع كل القفازات اليسرى معاً وكل اليمنى معاً — لا يمكن لبس قفازين من الجهة نفسها كزوج!",
                "Count total Left gloves and total Right gloves separately; the smaller count limits the wearable pairs.",
                [
                    f"Total Left gloves = {m(f'{l1} + {l2} = {L}')}, and total Right gloves = {m(f'{r1} + {r2} = {R}')}.",
                    f"Each wearable pair uses 1 Left and 1 Right, so {nm_en} can make **{m(ans)}** pairs (leaving {m(unmatched)} extra single gloves of one hand).",
                ],
                f"Check: {m(ans)} Left + {m(ans)} Right = {m(ans)} proper pairs!",
                "نحسب إجمالي القفازات اليسرى وإجمالي اليمنى على حدة، والعدد الأصغر يحدد عدد الأزواج الصحيحة.",
                [
                    f"مجموع اليسرى = {m(f'{l1} + {l2} = {L}')}، ومجموع اليمنى = {m(f'{r1} + {r2} = {R}')}.",
                    f"كل زوج يحتاج يسرى واحدة ويمنى واحدة، فيتكوّن **{m(ans)}** أزواج صالحة.",
                ],
                f"تحقق: العدد الأقل بين {m(L)} و{m(R)} هو {m(ans)}!",
                diagram_en=svg_number_strip([f"L: {l1}", f"R: {r1}", "+ Basket"]),
            )
        else:
            ans = unmatched
            B.add_math(
                tp, "Hard", bp,
                f"Every proper pair of shoes needs **1 Left shoe** and **1 Right shoe**. {nm_en} counts {m(l1)} Left shoes and {m(r1)} Right shoes by the door, plus {m(l2)} Left shoes and {m(r2)} Right shoes in the closet. After making as many proper Left–Right pairs as possible, how many **single shoes are left without a partner**?",
                f"كل زوج أحذية صحيح يحتاج **فردة يسرى** و**فردة يمنى**. أحصت {nm_ar} عند الباب {m(l1)} فردات يسرى و{m(r1)} يمنى، وفي الخزانة {m(l2)} يسرى و{m(r2)} يمنى. بعد تكوين أكبر عدد ممكن من الأزواج الصحيحة، كم **فردة حذاء تبقى بلا شريك**؟",
                ans, [(L + R) % 2, pairs, ans + 2, max(1, ans - 2)],
                f"Find total Left shoes ({m(f'{l1}+{l2}')}) and total Right shoes ({m(f'{r1}+{r2}')}), then subtract the smaller from the larger!",
                f"احسب مجموع اليسرى ({m(f'{l1}+{l2}')}) ومجموع اليمنى ({m(f'{r1}+{r2}')}) ثم اطرح الأصغر من الأكبر!",
                "Sum Left and Right shoes separately; after pairing min(L, R) pairs, |L - R| single shoes remain.",
                [
                    f"Total Left shoes = {m(f'{l1} + {l2} = {L}')}, and total Right shoes = {m(f'{r1} + {r2} = {R}')}.",
                    f"They form {m(pairs)} Left–Right pairs, leaving {m(f'{max(L, R)} - {min(L, R)} = {ans}')} unmatched single shoes.",
                ],
                f"Check: {m(f'2 \\times {pairs} + {ans} = {L + R}')} total shoes!",
                "نجمع الفردات اليسرى واليمنى كلّاً على حدة، ويكون الباقي بلا شريك هو الفرق بينهما.",
                [
                    f"إجمالي اليسرى = {m(L)}، وإجمالي اليمنى = {m(R)}.",
                    f"يتكوّن {m(pairs)} أزواج صحيحة، ويبقى {m(f'{max(L, R)} - {min(L, R)} = {ans}')} فردات بلا شريك.",
                ],
                f"تحقق: {m(f'2 \\times {pairs} + {ans} = {L + R}')} فردة في المجموع!",
                diagram_en=svg_number_strip([f"L: {l1}", f"R: {r1}", "+ Closet"]),
            )


# ==============================================================================
# UNIT 2 — Algebra (60 Questions: KANG-PRE-061 .. KANG-PRE-120)
# Blueprints: kang_pre_toy_pan_balance, kang_pre_fruit_icon_sums,
#             kang_pre_repeating_bead_train, kang_pre_in_out_number_box
# ==============================================================================
def _add_unit_1_2(B: BankBuilder) -> None:
    tp = "Algebra"

    # 5. kang_pre_toy_pan_balance (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_toy_pan_balance"
    bal_easy = [
        (2, 2, "Kangy", "الكنغر"),
        (2, 3, "Lina", "لينا"),
        (3, 2, "Omar", "عمر"),
        (3, 3, "Sara", "سارة"),
        (4, 2, "Tariq", "طارق"),
    ]
    for a, b, nm_en, nm_ar in bal_easy:
        ans = a * b
        B.add_math(
            tp, "Easy", bp,
            f"Look at {nm_en}'s two level toy scales: on the left scale, **1 orange ball** balances **{m(a)} green cubes**; on the right scale, **1 green cube** balances **{m(b)} purple cones**. How many **purple cones** will balance **1 orange ball**?",
            f"انظر إلى ميزاني الألعاب المتزنين لدى {nm_ar}: في الميزان الأيسر تتزن **كرة برتقالية واحدة** مع **{m(a)} مكعبات خضراء**، وفي الميزان الأيمن يتزن **مكعب أخضر واحد** مع **{m(b)} مخاريط بنفسجية**. كم **مخروطاً بنفسجياً** يتزن مع **كرة برتقالية واحدة**؟",
            ans, [a + b, ans + 1, max(1, ans - 1), ans + b],
            f"Swap each of the {m(a)} green cubes for {m(b)} purple cones!",
            f"استبدل كل مكعب أخضر من المكعبات الـ {m(a)} بـ {m(b)} مخاريط بنفسجية!",
            "Replace every green cube with its matching group of purple cones.",
            [
                f"1 orange ball balances {m(a)} green cubes.",
                f"Since each green cube balances {m(b)} purple cones, {m(a)} green cubes balance {m(' + '.join([str(b)] * a) + f' = {ans}')} purple cones.",
            ],
            f"Check: {m(f'{a} \\times {b} = {ans}')} purple cones!",
            "نستبدل كل مكعب أخضر بما يعادله من المخاريط البنفسجية ثم نجمعها.",
            [
                f"الكرة البرتقالية تتزن مع {m(a)} مكعبات خضراء.",
                f"كل مكعب أخضر يعادل {m(b)} مخاريط، إذن {m(' + '.join([str(b)] * a) + f' = {ans}')} مخاريط بنفسجية.",
            ],
            f"تحقق: {m(f'{a} \\times {b} = {ans}')} مخاريط!",
            diagram_en=svg_balance_scales(1, a, 1, b),
        )

    bal_med = [
        (2, 2, 3, False, "Nora", "نورة"),
        (2, 3, 2, False, "Zaid", "زيد"),
        (3, 2, 4, False, "Hala", "هلا"),
        (2, 2, 5, True, "Yousef", "يوسف"),
        (3, 2, 3, True, "Amal", "أمل"),
    ]
    for a, b, w_cone, ask_both, nm_en, nm_ar in bal_med:
        w_sq = b * w_cone
        w_ball = a * w_sq
        ans = (w_ball + w_sq) if ask_both else w_ball
        if not ask_both:
            q_en = (
                f"On {nm_en}'s toy scales, **1 orange ball** balances **{m(a)} green cubes**, and **1 green cube** balances **{m(b)} purple cones**. "
                f"If each purple cone weighs **{m(w_cone)} grams**, how many grams does **1 orange ball** weigh?"
            )
            q_ar = (
                f"على ميزاني {nm_ar}، تتزن **كرة برتقالية واحدة** مع **{m(a)} مكعبات خضراء**، ويتزن **مكعب أخضر واحد** مع **{m(b)} مخاريط بنفسجية**. "
                f"إذا كان وزن المخروط البنفسجي الواحد **{m(w_cone)} جرامات**، فكم جراماً تزن **الكرة البرتقالية الواحدة**؟"
            )
        else:
            q_en = (
                f"On {nm_en}'s scales, **1 orange ball** balances **{m(a)} green cubes**, and **1 green cube** balances **{m(b)} purple cones**. "
                f"Each purple cone weighs **{m(w_cone)} grams**. What is the total weight in grams of **1 orange ball and 1 green cube together**?"
            )
            q_ar = (
                f"على ميزاني {nm_ar}، تتزن **كرة برتقالية واحدة** مع **{m(a)} مكعبات خضراء**، ويتزن **مكعب أخضر واحد** مع **{m(b)} مخاريط بنفسجية**. "
                f"يزن المخروط البنفسجي الواحد **{m(w_cone)} جرامات**. ما الوزن الكلي بالجرام لـ **كرة برتقالية واحدة ومكعب أخضر واحد معاً**؟"
            )
        B.add_math(
            tp, "Medium", bp, q_en, q_ar,
            ans, [w_sq, w_ball if ask_both else w_ball + w_sq, a + b + w_cone, ans - w_cone],
            f"First find 1 green cube's weight ({m(f'{b} \\times {w_cone}')} g), then find 1 orange ball's weight!",
            f"احسب أولاً وزن المكعب الأخضر الواحد ({m(f'{b} \\times {w_cone}')} جم)، ثم وزن الكرة البرتقالية!",
            "Find the weight of 1 green cube from the right scale, then use the left scale for 1 orange ball.",
            [
                f"1 green cube weighs {m(f'{b} \\times {w_cone} = {w_sq}')} grams.",
                f"1 orange ball weighs {m(f'{a} \\times {w_sq} = {w_ball}')} grams."
                + (f" Adding 1 green cube gives {m(f'{w_ball} + {w_sq} = {ans}')} grams." if ask_both else ""),
            ],
            f"Check in cones: {m(a * b + (b if ask_both else 0))} cones × {m(w_cone)} g = {m(ans)} g!",
            "نوجد وزن المكعب الأخضر من الميزان الأيمن، ثم نستنتج وزن الكرة البرتقالية من الأيسر.",
            [
                f"وزن المكعب الأخضر الواحد = {m(f'{b} \\times {w_cone} = {w_sq}')} جم.",
                f"وزن الكرة البرتقالية الواحدة = {m(f'{a} \\times {w_sq} = {w_ball}')} جم."
                + (f" ومع مكعب أخضر واحد يصبح المجموع {m(f'{w_ball} + {w_sq} = {ans}')} جم." if ask_both else ""),
            ],
            f"تحقق: المجموع المتزن يساوي {m(ans)} جم!",
            diagram_en=svg_balance_scales(1, a, 1, b),
        )

    bal_hard = [
        (1, 2, 2, 3, 3, 0, 9, "Jude", "جود"),
        (1, 3, 3, 4, 2, 0, 8, "Salman", "سلمان"),
        (2, 4, 1, 3, 2, 1, 15, "Rayan", "ريان"),
        (3, 3, 1, 4, 3, 2, 20, "Dana", "دانة"),
        (1, 4, 2, 3, 3, 0, 18, "Karam", "كرم"),
    ]
    for c1, s1, s2, t2, ask_balls, ask_cubes, expected_ans, nm_en, nm_ar in bal_hard:
        # Verify exact integer cone equivalence: 1 cube = (t2 / s2) cones, 1 ball = (s1 / c1) * (t2 / s2) cones
        assert (s1 * t2) % (c1 * s2) == 0
        cones_per_ball = (s1 * t2) // (c1 * s2)
        if ask_cubes > 0:
            assert t2 % s2 == 0
        ans = ask_balls * cones_per_ball + (ask_cubes * (t2 // s2) if ask_cubes else 0)
        assert ans == expected_ans
        target_en = f"**{m(ask_balls)} orange balls**" if ask_cubes == 0 else f"**{m(ask_balls)} orange balls and {m(ask_cubes)} green cube(s)**"
        target_ar = f"**{m(ask_balls)} كرات برتقالية**" if ask_cubes == 0 else f"**{m(ask_balls)} كرات برتقالية و{m(ask_cubes)} من المكعبات الخضراء**"
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} balances two toy scales: the left scale shows **{m(c1)} orange ball(s)** balancing **{m(s1)} green cubes**, and the right scale shows **{m(s2)} green cube(s)** balancing **{m(t2)} purple cones**. How many **purple cones** are needed to balance {target_en}?",
            f"يوازن {nm_ar} ميزانين: في الأيسر تتزن **{m(c1)} من الكرات البرتقالية** مع **{m(s1)} مكعبات خضراء**، وفي الأيمن تتزن **{m(s2)} من المكعبات الخضراء** مع **{m(t2)} مخاريط بنفسجية**. كم **مخروطاً بنفسجياً** يلزم لموازنة {target_ar}؟",
            ans, [cones_per_ball, ans - t2, ans + 2, ans + cones_per_ball],
            f"Find how many purple cones balance **1 orange ball** ({m(cones_per_ball)} cones) by matching groups of green cubes!",
            f"اعرف أولاً كم مخروطاً بنفسجياً يعادل **كرة برتقالية واحدة** ({m(cones_per_ball)} مخاريط) بمطابقة مجموعات المكعبات الخضراء!",
            "Match equal groups of green cubes across both scales to find cones per orange ball.",
            [
                f"From the two scales, 1 orange ball balances {m(cones_per_ball)} purple cones.",
                f"Therefore, {target_en} balances {m(ans)} purple cones.",
            ],
            f"Ratio check: {m(f'{ask_balls} \\times {cones_per_ball}' + (f' + {ask_cubes * (t2 // s2)}' if ask_cubes else '') + f' = {ans}')} cones!",
            "نطابق مجموعات المكعبات الخضراء بين الميزانين لمعرفة عدد المخاريط لكل كرة برتقالية.",
            [
                f"بمقارنة الكفتين نجد أن الكرة البرتقالية الواحدة تعادل {m(cones_per_ball)} مخاريط بنفسجية.",
                f"إذن المجموعة المطلوبة تتزن مع {m(ans)} مخاريط بنفسجية.",
            ],
            f"تحقق: العدد الكلي للمخاريط هو {m(ans)}!",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        )

    # 6. kang_pre_fruit_icon_sums (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_fruit_icon_sums"
    icon_easy = [
        ("star", "heart", 5, 3, "yellow star", "red heart", "النجمة الصفراء", "القلب الأحمر"),
        ("diamond", "square", 4, 7, "blue diamond", "green square", "الماسة الزرقاء", "المربع الأخضر"),
        ("heart", "star", 6, 5, "red heart", "yellow star", "القلب الأحمر", "النجمة الصفراء"),
        ("square", "circle", 8, 4, "green square", "purple circle", "المربع الأخضر", "الدائرة البنفسجية"),
        ("circle", "diamond", 7, 9, "purple circle", "blue diamond", "الدائرة البنفسجية", "الماسة الزرقاء"),
    ]
    for ic1, ic2, v1, v2, n1_en, n2_en, n1_ar, n2_ar in icon_easy:
        rhs1 = 2 * v1
        rhs2 = v1 + v2
        ans = v2
        B.add_math(
            tp, "Easy", bp,
            f"On this picture puzzle card, identical shapes stand for the **same** secret number. The top row shows two `{n1_en}` shapes adding up to {m(rhs1)}, and the bottom row shows one `{n1_en}` plus one `{n2_en}` adding up to {m(rhs2)}. What number does **one `{n2_en}`** stand for?",
            f"في بطاقة الألغاز المصوّرة، الأشكال المتماثلة تمثل **العدد السري نفسه**. الصف العلوي يبيّن أن مجموع قطعتين من «{n1_ar}» يساوي {m(rhs1)}، والصف السفلي يبيّن أن «{n1_ar}» مع «{n2_ar}» يساوي {m(rhs2)}. ما العدد الذي تمثله **«{n2_ar}» الواحدة**؟",
            ans, [v1, rhs2, ans + 2, max(1, ans - 1)],
            f"Take half of {m(rhs1)} to find one `{n1_en}`, then subtract it from {m(rhs2)}!",
            f"خذ نصف العدد {m(rhs1)} لمعرفة قيمة «{n1_ar}»، ثم اطرحها من {m(rhs2)}!",
            "Halve the top sum to find the first icon, then subtract from the bottom sum.",
            [
                f"Two `{n1_en}` icons make {m(rhs1)}, so one `{n1_en}` = {m(v1)} (since {m(f'{v1} + {v1} = {rhs1}')}).",
                f"In the bottom row, {m(v1)} + `{n2_en}` = {m(rhs2)}, so one `{n2_en}` = {m(f'{rhs2} - {v1} = {ans}')}.",
            ],
            f"Check: {m(f'{v1} + {ans} = {rhs2}')}!",
            "نأخذ نصف مجموع الصف العلوي لإيجاد الشكل الأول ثم نطرحه من مجموع الصف السفلي.",
            [
                f"قطعتان من «{n1_ar}» تساويان {m(rhs1)}، إذن الواحدة = {m(v1)}.",
                f"في الصف السفلي: {m(v1)} + «{n2_ar}» = {m(rhs2)}، ومنه «{n2_ar}» = {m(f'{rhs2} - {v1} = {ans}')}.",
            ],
            f"تحقق: {m(f'{v1} + {ans} = {rhs2}')}!",
            diagram_en=svg_pre_icon_addition([ic1, ic1], str(rhs1), [ic1, ic2], str(rhs2)),
        )

    icon_med = [
        ("star", "square", 4, 5, "pair", "yellow star", "green square", "النجمة الصفراء", "المربع الأخضر"),
        ("heart", "diamond", 6, 3, "pair", "red heart", "blue diamond", "القلب الأحمر", "الماسة الزرقاء"),
        ("circle", "star", 5, 7, "pair", "purple circle", "yellow star", "الدائرة البنفسجية", "النجمة الصفراء"),
        ("diamond", "heart", 3, 8, "second", "blue diamond", "red heart", "الماسة الزرقاء", "القلب الأحمر"),
        ("square", "circle", 7, 6, "second", "green square", "purple circle", "المربع الأخضر", "الدائرة البنفسجية"),
    ]
    for ic1, ic2, v1, v2, ask_kind, n1_en, n2_en, n1_ar, n2_ar in icon_med:
        rhs1 = 3 * v1
        rhs2 = v1 + 2 * v2
        ans = (v1 + v2) if ask_kind == "pair" else v2
        ask_en = f"**one `{n1_en}` + one `{n2_en}`**" if ask_kind == "pair" else f"**one `{n2_en}`**"
        ask_ar = f"**«{n1_ar}» واحدة + «{n2_ar}» واحدة**" if ask_kind == "pair" else f"**«{n2_ar}» الواحدة**"
        B.add_math(
            tp, "Medium", bp,
            f"Each matching icon hides the same number: three `{n1_en}` icons add up to {m(rhs1)}, while one `{n1_en}` plus two `{n2_en}` icons add up to {m(rhs2)}. What is the value of {ask_en}?",
            f"كل شكل متماثل يخفي العدد نفسه: ثلاث من «{n1_ar}» مجموعها {m(rhs1)}، وواحدة من «{n1_ar}» مع اثنتين من «{n2_ar}» مجموعها {m(rhs2)}. ما قيمة {ask_ar}؟",
            ans, [v1, v2 if ask_kind == "pair" else v1 + v2, 2 * v2, ans + 2],
            f"Split {m(rhs1)} into 3 equal parts to get one `{n1_en}` = {m(v1)}, then subtract {m(v1)} from {m(rhs2)}!",
            f"قسّم {m(rhs1)} إلى 3 أجزاء متساوية لتجد «{n1_ar}» = {m(v1)}، ثم اطرح {m(v1)} من {m(rhs2)}!",
            "Find the first icon from the 3-of-a-kind top row, then halve the remaining part of the bottom row.",
            [
                f"Three `{n1_en}` icons sum to {m(rhs1)}, so one `{n1_en}` = {m(v1)}.",
                f"Subtracting {m(v1)} from {m(rhs2)} leaves {m(f'{rhs2} - {v1} = {2 * v2}')} for two `{n2_en}` icons, so one `{n2_en}` = {m(v2)}.",
                (f"Adding one of each gives {m(f'{v1} + {v2} = {ans}')}." if ask_kind == "pair" else f"Thus one `{n2_en}` stands for {m(ans)}."),
            ],
            f"Row 2 check: {m(f'{v1} + {v2} + {v2} = {rhs2}')}!",
            "نقسم مجموع الصف الأول على 3 لإيجاد الشكل الأول، ثم نطرحه من الصف الثاني ونأخذ النصف.",
            [
                f"ثلاث من «{n1_ar}» تساوي {m(rhs1)}، أي الواحدة = {m(v1)}.",
                f"نطرح {m(v1)} من {m(rhs2)} فيبقى {m(2 * v2)} لقطعتين من «{n2_ar}»، أي الواحدة = {m(v2)}.",
                (f"المجموع المطلوب = {m(f'{v1} + {v2} = {ans}')}." if ask_kind == "pair" else f"إذن القيمة المطلوبة هي {m(ans)}."),
            ],
            f"تحقق من الصف الثاني: {m(f'{v1} + {v2} + {v2} = {rhs2}')}!",
            diagram_en=svg_pre_icon_addition([ic1, ic1, ic1], str(rhs1), [ic1, ic2, ic2], str(rhs2)),
        )

    icon_hard = [
        ("star", "heart", 5, 4, "pair", "yellow star", "red heart", "النجمة الصفراء", "القلب الأحمر"),
        ("diamond", "square", 7, 2, "pair", "blue diamond", "green square", "الماسة الزرقاء", "المربع الأخضر"),
        ("circle", "heart", 6, 8, "pair", "purple circle", "red heart", "الدائرة البنفسجية", "القلب الأحمر"),
        ("star", "diamond", 8, 5, "first", "yellow star", "blue diamond", "النجمة الصفراء", "الماسة الزرقاء"),
        ("square", "heart", 9, 4, "first", "green square", "red heart", "المربع الأخضر", "القلب الأحمر"),
    ]
    for ic1, ic2, v1, v2, ask_kind, n1_en, n2_en, n1_ar, n2_ar in icon_hard:
        rhs1 = 2 * v1 + v2
        rhs2 = v1 + 2 * v2
        tot_both = rhs1 + rhs2
        assert tot_both % 3 == 0
        pair_sum = tot_both // 3
        assert pair_sum == v1 + v2
        ans = pair_sum if ask_kind == "pair" else (rhs1 - pair_sum)
        if ask_kind == "first":
            assert ans == v1
        ask_en = f"**one `{n1_en}` + one `{n2_en}`**" if ask_kind == "pair" else f"**one `{n1_en}` alone**"
        ask_ar = f"**«{n1_ar}» واحدة + «{n2_ar}» واحدة**" if ask_kind == "pair" else f"**«{n1_ar}» الواحدة بمفردها**"
        B.add_math(
            tp, "Hard", bp,
            f"Look closely at both rows: two `{n1_en}` icons and one `{n2_en}` icon add up to {m(rhs1)}, while one `{n1_en}` icon and two `{n2_en}` icons add up to {m(rhs2)}. What is the value of {ask_en}?",
            f"تأمل الصفين جيداً: قطعتان من «{n1_ar}» مع قطعة من «{n2_ar}» مجموعها {m(rhs1)}، وقطعة من «{n1_ar}» مع قطعتين من «{n2_ar}» مجموعها {m(rhs2)}. ما قيمة {ask_ar}؟",
            ans, [abs(rhs1 - rhs2), pair_sum if ask_kind == "first" else v1, ans + 2, max(1, ans - 2)],
            f"Put BOTH rows together into one big basket: you get **3 of each shape** adding up to {m(f'{rhs1} + {rhs2} = {tot_both}')}!",
            f"اجمع الصفين معاً في سلة واحدة: ستحصل على **3 من كل شكل** بمجموع {m(f'{rhs1} + {rhs2} = {tot_both}')}!",
            "Add both rows together to get 3 pairs of icons, then divide into 3 equal groups.",
            [
                f"Adding both rows together gives 3 `{n1_en}` + 3 `{n2_en}` = {m(f'{rhs1} + {rhs2} = {tot_both}')}.",
                f"Splitting {m(tot_both)} into 3 equal pairs gives 1 `{n1_en}` + 1 `{n2_en}` = {m(pair_sum)}."
                + ("" if ask_kind == "pair" else f" Comparing with Row 1 ({m(rhs1)}), the extra `{n1_en}` equals {m(f'{rhs1} - {pair_sum} = {ans}')}."),
            ],
            f"Check: `{n1_en}` = {m(v1)}, `{n2_en}` = {m(v2)} → {m(f'2\\times{v1}+{v2}={rhs1}')} and {m(f'{v1}+2\\times{v2}={rhs2}')}!",
            "نجمع الصفين معاً فنحصل على 3 أزواج متطابقة من الشكلين، ثم نقسم المجموع على 3.",
            [
                f"بجمع الصفين نحصل على 3 من كل شكل بمجموع {m(f'{rhs1} + {rhs2} = {tot_both}')}.",
                f"إذن قيمة زوج واحد (قطعة من كل نوع) = {m(pair_sum)}."
                + ("" if ask_kind == "pair" else f" وبمقارنة ذلك بالصف الأول ({m(rhs1)}) نجد أن «{n1_ar}» الواحدة = {m(f'{rhs1} - {pair_sum} = {ans}')}."),
            ],
            f"تحقق: {m(v1)} و{m(v2)} يحققان {m(rhs1)} و{m(rhs2)} تماماً!",
            diagram_en=svg_pre_icon_addition([ic1, ic1, ic2], str(rhs1), [ic1, ic2, ic2], str(rhs2)),
        )

    # 7. kang_pre_repeating_bead_train (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_repeating_bead_train"
    color_pairs_5 = [
        ("Red (`R`)", "حمراء (`R`)"),
        ("Blue (`B`)", "زرقاء (`B`)"),
        ("Yellow (`Y`)", "صفراء (`Y`)"),
        ("Green (`G`)", "خضراء (`G`)"),
        ("White (`W`)", "بيضاء (`W`)"),
    ]
    code_to_idx = {"R": 0, "B": 1, "Y": 2, "G": 3, "W": 4}
    bead_easy = [
        (["R", "B"], 8, 5, "Maya", "مايا"),
        (["R", "Y", "B"], 9, 4, "Faris", "فارس"),
        (["G", "W"], 10, 6, "Layan", "ليان"),
        (["R", "G", "Y"], 9, 7, "Sami", "سامي"),
        (["B", "Y", "G", "W"], 8, 6, "Tala", "تالا"),
    ]
    for cyc, n_tot, q_pos, nm_en, nm_ar in bead_easy:
        assert n_tot % len(cyc) == 0
        full = [cyc[i % len(cyc)] for i in range(n_tot)]
        ans_code = full[q_pos]
        shown = list(full)
        shown[q_pos] = "?"
        cidx = code_to_idx[ans_code]
        cyc_str = " → ".join(cyc)
        B.add_bilingual(
            tp, "Easy", bp,
            f"{nm_en} makes a circular bracelet by repeating the bead pattern `{cyc_str}` all the way around clockwise from the top. One bead is covered with `{m('?')}`. What color is the `{m('?')}` bead?",
            f"تصنع {nm_ar} سواراً دائرياً بتكرار نمط الخرزات `{cyc_str}` باتجاه عقارب الساعة بدءاً من الأعلى. خرزة واحدة مغطاة بالعلامة `{m('?')}`. ما لون الخرزة `{m('?')}`؟",
            color_pairs_5, cidx,
            f"Point to the top bead and chant `{cyc_str}` clockwise around the circle until you land on `?`!",
            f"ابدأ من الخرزة العلوية وردد النمط `{cyc_str}` مع عقارب الساعة حتى تصل إلى `?`!",
            "Follow the repeating color unit step-by-step around the bracelet.",
            [
                f"The bracelet repeats `{cyc_str}` in order around all {m(n_tot)} spots.",
                f"Look at the bead right before `?` (`{full[q_pos - 1]}`) and right after `?` (`{full[(q_pos + 1) % n_tot]}`): the missing bead is **{color_pairs_5[cidx][0]}**.",
            ],
            f"Restoring `{ans_code}` keeps every `{cyc_str}` group unbroken all around the circle!",
            "نتتبع وحدة التكرار اللونية بالترتيب حول الدائرة حتى موضع العلامة `?`.",
            [
                f"النمط المتكرر هو `{cyc_str}` على مدار {m(n_tot)} خرزات.",
                f"الخرزة التي تسبق `?` هي `{full[q_pos - 1]}`، فتكون الخرزة المفقودة **{color_pairs_5[cidx][1]}**.",
            ],
            f"وضع `{ans_code}` يحافظ على انتظام النمط `{cyc_str}` حول السوار بالكامل!",
            diagram_en=svg_kang_necklace_beads(shown),
        )

    bead_med = [
        (["R", "B", "B"], 15, "B", "Blue (`B`)", "الزرقاء (`B`)", "Kangy", "الكنغر"),
        (["R", "R", "Y"], 14, "R", "Red (`R`)", "الحمراء (`R`)", "Lina", "لينا"),
        (["G", "Y", "B", "Y"], 16, "Y", "Yellow (`Y`)", "الصفراء (`Y`)", "Omar", "عمر"),
        (["R", "G", "B"], 19, "R", "Red (`R`)", "الحمراء (`R`)", "Sara", "سارة"),
        (["B", "W", "B", "Y"], 18, "B", "Blue (`B`)", "الزرقاء (`B`)", "Tariq", "طارق"),
    ]
    for cyc, total_n, tgt, tgt_en, tgt_ar, nm_en, nm_ar in bead_med:
        p = len(cyc)
        seq = [cyc[i % p] for i in range(total_n)]
        ans = seq.count(tgt)
        groups = total_n // p
        rem = total_n % p
        per_grp = cyc.count(tgt)
        rem_cnt = cyc[:rem].count(tgt)
        assert ans == groups * per_grp + rem_cnt
        preview = (cyc * 3)[:9] if p == 3 else (cyc * 2)
        preview_shown = list(preview)
        preview_shown[-1] = "?"
        cyc_str = "-".join(cyc)
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} strings **{m(total_n)} beads** in a straight line by repeating the group `{cyc_str}` again and again from the start (matching the pattern loop shown). How many **{tgt_en}** beads are on the {m(total_n)}-bead string altogether?",
            f"ينظم {nm_ar} خيطاً مستقيماً فيه **{m(total_n)} خرزة** بتكرار المجموعة `{cyc_str}` مراراً بالترتيب من البداية. كم خرزة من اللون **{tgt_ar}** توجد في الخيط كلّه؟",
            ans, [groups, ans + 1, max(1, ans - 1), total_n - ans],
            f"Each group `{cyc_str}` has {m(p)} beads (including {m(per_grp)} `{tgt}` bead(s)). Count how many full groups of {m(p)} fit in {m(total_n)}!",
            f"كل مجموعة `{cyc_str}` تضم {m(p)} خرزات (منها {m(per_grp)} باللون `{tgt}`). احسب كم مجموعة كاملة من {m(p)} توجد في {m(total_n)}!",
            "Count full repeating groups inside the total length, then check any leftover beads at the end.",
            [
                f"One group `{cyc_str}` has {m(p)} beads and contains {m(per_grp)} `{tgt}` bead(s).",
                f"{m(total_n)} beads make {m(groups)} full groups ({m(groups * p)} beads) plus {m(rem)} leftover bead(s) at the end.",
                f"Total `{tgt}` beads = {m(f'{groups} \\times {per_grp} + {rem_cnt} = {ans}')}.",
            ],
            f"Direct count of all {m(total_n)} beads confirms exact **{m(ans)}** `{tgt}` beads!",
            "نحسب عدد المجموعات الكاملة في الخيط ثم نضيف ما يظهر في الخرزات المتبقية في النهاية.",
            [
                f"المجموعة الواحدة `{cyc_str}` طولها {m(p)} وفيها {m(per_grp)} من `{tgt}`.",
                f"في {m(total_n)} خرزة توجد {m(groups)} مجموعات كاملة ({m(groups * p)} خرزة) ويتبقى {m(rem)} في النهاية.",
                f"إجمالي خرزات `{tgt}` = {m(f'{groups} \\times {per_grp} + {rem_cnt} = {ans}')}.",
            ],
            f"تحقق: العدّ المباشر للخرزات الـ {m(total_n)} يعطي **{m(ans)}** تماماً!",
            diagram_en=svg_kang_necklace_beads(preview_shown),
        )

    bead_hard = [
        (["R", "B", "B"], 12, (4, 5, 6, 7), {"R": 3, "B": 2}, "Nora", "نورة"),
        (["R", "Y", "G"], 12, (3, 4, 5, 6, 7), {"R": 2, "Y": 3, "G": 4}, "Zaid", "زيد"),
        (["B", "Y", "B", "G"], 12, (5, 6, 7, 8), {"B": 2, "Y": 5, "G": 3}, "Hala", "هلا"),
        (["R", "R", "W"], 9, (2, 3, 4, 5), {"R": 4, "W": 1}, "Yousef", "يوسف"),
        (["G", "B", "Y"], 12, (2, 3, 4, 5), {"G": 5, "B": 2, "Y": 3}, "Amal", "أمل"),
    ]
    for cyc, n_tot, hid_idxs, pts_map, nm_en, nm_ar in bead_hard:
        assert n_tot % len(cyc) == 0
        full = [cyc[i % len(cyc)] for i in range(n_tot)]
        shown = ["?" if i in hid_idxs else full[i] for i in range(n_tot)]
        hidden_cols = [full[i] for i in hid_idxs]
        ans = sum(pts_map[c] for c in hidden_cols)
        pts_desc_en = ", ".join(f"`{k}` = {m(v)} pts" for k, v in pts_map.items())
        pts_desc_ar = "، ".join(f"`{k}` = {m(v)} نقاط" for k, v in pts_map.items())
        cyc_str = "-".join(cyc)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en}'s {m(n_tot)}-bead necklace repeats `{cyc_str}` clockwise from the top bead, and **{m(len(hid_idxs))} consecutive beads** are hidden as `{m('?')}`. If bead scores are {pts_desc_en}, what is the **total score of ONLY the hidden `{m('?')}` beads**?",
            f"عقد {nm_ar} المكوّن من {m(n_tot)} خرزة يكرر النمط `{cyc_str}` مع عقارب الساعة من الأعلى، وهناك **{m(len(hid_idxs))} خرزات متتالية** مخفية بالعلامة `{m('?')}`. إذا كانت قيم الخرزات ({pts_desc_ar})، فما **مجموع نقاط الخرزات المخفية `{m('?')}` فقط**؟",
            ans, [ans + 2, max(1, ans - 2), ans + 3, len(hid_idxs) * max(pts_map.values())],
            f"First uncover the {m(len(hid_idxs))} hidden letters by continuing `{cyc_str}` clockwise, then add their point values!",
            f"اكشف أولاً ألوان الخرزات الـ {m(len(hid_idxs))} المخفية بإكمال النمط `{cyc_str}`، ثم اجمع نقاطها!",
            "Restore the hidden bead colors using the repeating cycle, then sum their point values.",
            [
                f"Continuing `{cyc_str}` clockwise around the {m(n_tot)} positions, the hidden `{m('?')}` beads are `{'-'.join(hidden_cols)}`.",
                f"Adding their scores gives {' + '.join(str(pts_map[c]) for c in hidden_cols)} = **{m(ans)}** points.",
            ],
            f"Hidden colors `{'-'.join(hidden_cols)}` reconnect smoothly to `{full[(hid_idxs[-1] + 1) % n_tot]}` right after the gap!",
            "نستعيد ألوان الخرزات المخفية من النمط الدوري ثم نجمع نقاط كل خرزة منها.",
            [
                f"بمتابعة النمط `{cyc_str}` مع عقارب الساعة نجد أن الخرزات المخفية هي `{'-'.join(hidden_cols)}`.",
                f"مجموع نقاطها = {' + '.join(str(pts_map[c]) for c in hidden_cols)} = **{m(ans)}**.",
            ],
            f"تحقق: الخرزة التي تلي الفجوة مباشرة هي `{full[(hid_idxs[-1] + 1) % n_tot]}`، وهو يطابق الرسم!",
            diagram_en=svg_kang_necklace_beads(shown),
        )

    # 8. kang_pre_in_out_number_box (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_in_out_number_box"
    box_easy = [
        (6, "+ 5", "- 3", 8, "Joey", "جوي"),
        (5, "Double", "+ 4", 14, "Mimi", "ميمي"),
        (12, "- 4", "+ 7", 15, "Koko", "كوكو"),
        (8, "+ 6", "Half", 7, "Bibi", "بيبي"),
        (9, "Double", "- 5", 13, "Toto", "توتو"),
    ]
    def _apply_op(val: int, op_s: str) -> int:
        if op_s == "Double":
            return val * 2
        if op_s == "Half":
            assert val % 2 == 0
            return val // 2
        sign, num = op_s.split()
        k = int(num)
        return val + k if sign == "+" else val - k

    for inp, op1, op2, expected, nm_en, nm_ar in box_easy:
        mid = _apply_op(inp, op1)
        ans = _apply_op(mid, op2)
        assert ans == expected
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} drops the number **{m(inp)}** into this two-step toy number machine (`{op1}`, then `{op2}`, where `Double` means adding a number to itself and `Half` means splitting into two equal parts). What number comes out at `{m('?')}`?",
            f"يُدخل {nm_ar} العدد **{m(inp)}** في آلة الأعداد ذات الخطوتين (`{op1}` ثم `{op2}`، حيث `Double` تعني الضعف و`Half` تعني النصف). ما العدد الذي يخرج عند `{m('?')}`؟",
            ans, [mid, ans + 2, max(1, ans - 2), inp + ans],
            f"Do the blue box (`{op1}`) on {m(inp)} first to get {m(mid)}, then do the purple box (`{op2}`)!",
            f"طبّق الصندوق الأول (`{op1}`) على {m(inp)} لتحصل على {m(mid)}، ثم طبّق الصندوق الثاني (`{op2}`)!",
            "Follow the two boxes in order from left to right.",
            [
                f"First box (`{op1}`) turns {m(inp)} into {m(mid)}.",
                f"Second box (`{op2}`) turns {m(mid)} into **{m(ans)}**.",
            ],
            f"Pipeline trace: {m(inp)} → {m(mid)} → {m(ans)}!",
            "ننفذ العملية الأولى ثم نطبّق العملية الثانية على الناتج بالترتيب.",
            [
                f"الصندوق الأول (`{op1}`) يحوّل {m(inp)} إلى {m(mid)}.",
                f"الصندوق الثاني (`{op2}`) يحوّل {m(mid)} إلى **{m(ans)}**.",
            ],
            f"تتبع المسار: {m(inp)} ← {m(mid)} ← {m(ans)}!",
            diagram_en=svg_function_machine(str(inp), op1, op2, "?"),
        )

    box_med = [
        (7, "+ 6", "- 4", 9, "Jude", "جود"),
        (5, "Double", "+ 3", 13, "Salman", "سلمان"),
        (14, "- 5", "Double", 18, "Rayan", "ريان"),
        (9, "+ 7", "Half", 8, "Dana", "دانة"),
        (8, "Double", "- 6", 10, "Karam", "كرم"),
    ]
    for ans_in, op1, op2, out_v, nm_en, nm_ar in box_med:
        mid = _apply_op(ans_in, op1)
        assert _apply_op(mid, op2) == out_v
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} puts a secret number `{m('?')}` into this machine (`{op1}`, then `{op2}`), and the number **{m(out_v)}** pops out at the end! What secret number `{m('?')}` went IN at the start?",
            f"أدخل {nm_ar} عدداً سرياً `{m('?')}` في هذه الآلة (`{op1}` ثم `{op2}`)، فخرج العدد **{m(out_v)}** في النهاية! ما العدد السري `{m('?')}` الذي دخل في البداية؟",
            ans_in, [mid, _apply_op(_apply_op(out_v, op1), op2) if op2 != "Half" or _apply_op(out_v, op1) % 2 == 0 else out_v + 3, ans_in + 2, max(1, ans_in - 2)],
            f"Walk **backward** from {m(out_v)}: undo `{op2}` first (opposite action!), then undo `{op1}`!",
            f"ارجع **بالعكس** من {m(out_v)}: اعكس العملية `{op2}` أولاً، ثم اعكس `{op1}`!",
            "Work backward from the output by reversing the second box first and the first box second.",
            [
                f"Before the second box (`{op2}`) produced {m(out_v)}, the number in the middle had to be {m(mid)}.",
                f"Reversing the first box (`{op1}`) from {m(mid)} gives the starting number **{m(ans_in)}**.",
            ],
            f"Forward check: {m(ans_in)} → (`{op1}`) → {m(mid)} → (`{op2}`) → {m(out_v)}!",
            "نسير عكسياً من المخرج بعكس العملية الثانية أولاً ثم عكس العملية الأولى.",
            [
                f"بعكس الصندوق الثاني (`{op2}`) بدءاً من {m(out_v)} نجد أن العدد الأوسط كان {m(mid)}.",
                f"وبعكس الصندوق الأول (`{op1}`) من {m(mid)} نجد أن العدد الأول هو **{m(ans_in)}**.",
            ],
            f"تحقق للأمام: {m(ans_in)} ← {m(mid)} ← {m(out_v)}!",
            diagram_en=svg_function_machine("?", op1, op2, str(out_v)),
        )

    box_hard = [
        ("twopass", 3, "Double", "+ 1", 15, "Maya", "مايا"),
        ("twopass", 10, "- 4", "Double", 16, "Faris", "فارس"),
        ("twopass", 4, "+ 8", "Half", 7, "Layan", "ليان"),
        ("find_op", 6, "Double", 5, 17, "Sami", "سامي"),
        ("find_op", 15, "- 7", 9, 17, "Tala", "تالا"),
    ]
    for hmode, inp, op1, op2_or_k, target_v, nm_en, nm_ar in box_hard:
        if hmode == "twopass":
            op2 = str(op2_or_k)
            pass1 = _apply_op(_apply_op(inp, op1), op2)
            ans = _apply_op(_apply_op(pass1, op1), op2)
            assert ans == target_v
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} puts **{m(inp)}** into this machine (`{op1}`, then `{op2}`), catches the number that comes out, and feeds **that number right back into the start** of the same machine a **second time**! What number comes out after the second trip?",
                f"تُدخل {nm_ar} العدد **{m(inp)}** في الآلة (`{op1}` ثم `{op2}`)، ثم تأخذ العدد الذي يخرج وتُدخله **مرة ثانية** من بداية الآلة نفسها! ما العدد الذي يخرج بعد الرحلة الثانية؟",
                ans, [pass1, ans + 2, max(1, ans - 2), pass1 * 2],
                f"Find what comes out on Trip 1 ({m(pass1)}), then send {m(pass1)} through `{op1}` and `{op2}` one more time!",
                f"احسب مخرج الرحلة الأولى ({m(pass1)})، ثم مرّر {m(pass1)} عبر `{op1}` و`{op2}` مرة ثانية!",
                "Run the two-step machine once to get the first output, then run that output through both steps again.",
                [
                    f"Trip 1: {m(inp)} → (`{op1}`) → {m(_apply_op(inp, op1))} → (`{op2}`) → {m(pass1)}.",
                    f"Trip 2: {m(pass1)} → (`{op1}`) → {m(_apply_op(pass1, op1))} → (`{op2}`) → **{m(ans)}**.",
                ],
                f"Two-trip trace: {m(inp)} → {m(pass1)} → {m(ans)}!",
                "نشغّل الآلة في المرة الأولى ثم نأخذ الناتج وندخله في الآلة مرة ثانية.",
                [
                    f"الرحلة الأولى: {m(inp)} ← {m(_apply_op(inp, op1))} ← {m(pass1)}.",
                    f"الرحلة الثانية: {m(pass1)} ← {m(_apply_op(pass1, op1))} ← **{m(ans)}**.",
                ],
                f"تحقق من الرحلتين: {m(inp)} ← {m(pass1)} ← {m(ans)}!",
                diagram_en=svg_function_machine(str(inp), op1, op2, "?"),
            )
        else:
            ans = int(op2_or_k)
            mid = _apply_op(inp, op1)
            assert mid + ans == target_v
            B.add_math(
                tp, "Hard", bp,
                f"When {nm_en} puts **{m(inp)}** into this machine, the first box does `{op1}`, the second box **adds a secret number `{m('?')}`** (`+ ?`), and **{m(target_v)}** comes out! What number is `{m('?')}`?",
                f"عندما يُدخل {nm_ar} العدد **{m(inp)}** في الآلة، ينفذ الصندوق الأول `{op1}`، ويضيف الصندوق الثاني **عدداً سرياً `{m('?')}`** (`+ ?`)، فيخرج العدد **{m(target_v)}**! ما قيمة `{m('?')}`؟",
                ans, [mid, target_v - inp, ans + 2, max(1, ans - 2)],
                f"First apply `{op1}` to {m(inp)} to get {m(mid)}, then see how much must be added to reach {m(target_v)}!",
                f"طبّق أولاً `{op1}` على {m(inp)} لتحصل على {m(mid)}، ثم احسب كم نضيف للوصول إلى {m(target_v)}!",
                "Compute the number leaving the first box, then subtract it from the final output.",
                [
                    f"After the first box (`{op1}`), {m(inp)} becomes {m(mid)}.",
                    f"To turn {m(mid)} into {m(target_v)}, the second box must add {m(f'{target_v} - {mid} = {ans}')}.",
                ],
                f"Check: {m(inp)} → {m(mid)} → {m(f'{mid} + {ans} = {target_v}')}!",
                "نحسب العدد الخارج من الصندوق الأول ثم نطرحه من الناتج النهائي.",
                [
                    f"بعد الصندوق الأول (`{op1}`) يصبح العدد {m(mid)}.",
                    f"ولكي يصبح {m(mid)} مساوياً لـ {m(target_v)} نضيف {m(f'{target_v} - {mid} = {ans}')}.",
                ],
                f"تحقق: {m(f'{mid} + {ans} = {target_v}')}!",
                diagram_en=svg_function_machine(str(inp), op1, "+ ?", str(target_v)),
            )


# ==============================================================================
# UNIT 3 — Geometry Part 1 (60 Questions: KANG-PRE-121 .. KANG-PRE-180)
# Blueprints: kang_pre_shape_polygon_counting, kang_pre_grid_tile_completion,
#             kang_pre_stamp_mirror_turns, kang_pre_toy_cube_stacks
# ==============================================================================
def _add_unit_1_3(B: BankBuilder) -> None:
    tp = "Geometry"

    # 9. kang_pre_shape_polygon_counting (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_shape_polygon_counting"
    shp_easy = [
        (2, 1, 2, "Kangy", "الكنغر"),
        (3, 2, 1, "Lina", "لينا"),
        (1, 3, 2, "Omar", "عمر"),
        (4, 1, 3, "Sara", "سارة"),
        (2, 3, 2, "Tariq", "طارق"),
    ]
    for t_cnt, s_cnt, c_cnt, nm_en, nm_ar in shp_easy:
        ans = 3 * t_cnt + 4 * s_cnt
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en}'s art card shows separate triangles, squares, and circles ({m(t_cnt)} triangle(s), {m(s_cnt)} square(s), and {m(c_cnt)} circle(s)). Remembering that circles have **{m(0)} sharp corners**, how many **sharp corners** are on the card altogether?",
            f"تضم بطاقة الرسم لدى {nm_ar} مثلثات ومربعات ودوائر منفصلة ({m(t_cnt)} من المثلثات، و{m(s_cnt)} من المربعات، و{m(c_cnt)} من الدوائر). علماً بأن الدائرة لها **{m(0)} من الرؤوس المدببة**، كم **ركناً (رأساً) مدبباً** في البطاقة إجمالاً؟",
            ans, [ans + c_cnt, t_cnt + s_cnt + c_cnt, 4 * t_cnt + 3 * s_cnt, ans + 3],
            f"Count {m(3)} corners for each yellow triangle and {m(4)} corners for each blue square!",
            f"احسب {m(3)} رؤوس لكل مثلث أصفر و{m(4)} رؤوس لكل مربع أزرق!",
            "Multiply triangles by 3 corners and squares by 4 corners, then add (circles contribute 0).",
            [
                f"Triangles give {m(f'{t_cnt} \\times 3 = {3 * t_cnt}')} corners, and squares give {m(f'{s_cnt} \\times 4 = {4 * s_cnt}')} corners.",
                f"Circles have {m(0)} corners, so total corners = {m(f'{3 * t_cnt} + {4 * s_cnt} = {ans}')}.",
            ],
            f"Check: {m(f'{3 * t_cnt} + {4 * s_cnt} + 0 = {ans}')} corners!",
            "نحسب 3 رؤوس لكل مثلث و4 رؤوس لكل مربع وصفر لكل دائرة ثم نجمع.",
            [
                f"رؤوس المثلثات = {m(f'{t_cnt} \\times 3 = {3 * t_cnt}')}، ورؤوس المربعات = {m(f'{s_cnt} \\times 4 = {4 * s_cnt}')}.",
                f"الدوائر ليس لها رؤوس ({m(0)})، إذن المجموع = {m(f'{3 * t_cnt} + {4 * s_cnt} = {ans}')}.",
            ],
            f"تحقق: {m(f'{3 * t_cnt} + {4 * s_cnt} = {ans}')} رأساً!",
            diagram_en=svg_pre_shape_collage(t_cnt, s_cnt, c_cnt),
        )

    shp_med = [
        (3, 2, 2, "dots", "Nora", "نورة"),
        (2, 3, 3, "dots", "Zaid", "زيد"),
        (4, 2, 1, "score", "Hala", "هلا"),
        (1, 4, 2, "diff_sides", "Yousef", "يوسف"),
        (5, 2, 2, "diff_sides", "Amal", "أمل"),
    ]
    for t_cnt, s_cnt, c_cnt, mmode, nm_en, nm_ar in shp_med:
        if mmode == "dots":
            ans = 3 * t_cnt + 4 * s_cnt + 2 * c_cnt
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en} decorates the shapes on this card ({m(t_cnt)} triangles, {m(s_cnt)} squares, and {m(c_cnt)} circles) by placing **1 glitter dot on every sharp corner** AND **2 glitter dots inside every circle**. How many glitter dots does {nm_en} use in all?",
                f"تزيّن {nm_ar} الأشكال المرسومة ({m(t_cnt)} مثلثات و{m(s_cnt)} مربعات و{m(c_cnt)} دوائر) بوضع **نقطة لامعة على كل ركن مدبب** و**نقطتين لامعتين داخل كل دائرة**. كم نقطة لامعة استعملت في المجموع؟",
                ans, [3 * t_cnt + 4 * s_cnt + c_cnt, 3 * t_cnt + 4 * s_cnt, ans + 2, ans - 3],
                f"Add triangle corners ({m(3 * t_cnt)}), square corners ({m(4 * s_cnt)}), and {m(2)} dots per circle ({m(2 * c_cnt)})!",
                f"اجمع رؤوس المثلثات ({m(3 * t_cnt)}) ورؤوس المربعات ({m(4 * s_cnt)}) ونقاط الدوائر ({m(2 * c_cnt)})!",
                "Count 3 per triangle, 4 per square, and 2 per circle, then add them up.",
                [
                    f"Triangles get {m(f'{t_cnt} \\times 3 = {3 * t_cnt}')} dots, and squares get {m(f'{s_cnt} \\times 4 = {4 * s_cnt}')} dots.",
                    f"Circles get {m(f'{c_cnt} \\times 2 = {2 * c_cnt}')} dots, making {m(f'{3 * t_cnt} + {4 * s_cnt} + {2 * c_cnt} = {ans}')} dots.",
                ],
                f"Total check: {m(f'{3 * t_cnt} + {4 * s_cnt} + {2 * c_cnt} = {ans}')}!",
                "نضرب عدد المثلثات في 3 والمربعات في 4 والدوائر في 2 ثم نجمع النواتج.",
                [
                    f"نقاط المثلثات = {m(3 * t_cnt)}، ونقاط المربعات = {m(4 * s_cnt)}.",
                    f"نقاط الدوائر = {m(2 * c_cnt)}، فيكون المجموع {m(f'{3 * t_cnt} + {4 * s_cnt} + {2 * c_cnt} = {ans}')}.",
                ],
                f"تحقق: المجموع الكلي {m(ans)} نقطة!",
                diagram_en=svg_pre_shape_collage(t_cnt, s_cnt, c_cnt),
            )
        elif mmode == "score":
            ans = 2 * t_cnt + 5 * s_cnt + 3 * c_cnt
            B.add_math(
                tp, "Medium", bp,
                f"In {nm_en}'s card game ({m(t_cnt)} triangles, {m(s_cnt)} squares, and {m(c_cnt)} circle), each triangle is worth **{m(2)} points**, each square is worth **{m(5)} points**, and each circle is worth **{m(3)} points**. What is the total score of this card?",
                f"في لعبة بطاقات {nm_ar} ({m(t_cnt)} مثلثات و{m(s_cnt)} مربعان و{m(c_cnt)} دائرة)، قيمة كل مثلث **{m(2)} نقطة**، وكل مربع **{m(5)} نقاط**، وكل دائرة **{m(3)} نقاط**. ما مجموع نقاط البطاقة؟",
                ans, [t_cnt + s_cnt + c_cnt, ans - 2, ans + 3, 3 * t_cnt + 4 * s_cnt + c_cnt],
                f"Find points for triangles ({m(f'{t_cnt}\\times2')}), squares ({m(f'{s_cnt}\\times5')}), and circles ({m(f'{c_cnt}\\times3')}), then add!",
                f"احسب نقاط المثلثات ({m(f'{t_cnt}\\times2')}) والمربعات ({m(f'{s_cnt}\\times5')}) والدوائر ({m(f'{c_cnt}\\times3')}) ثم اجمع!",
                "Multiply the count of each shape by its point value and sum the three totals.",
                [
                    f"Triangles: {m(f'{t_cnt} \\times 2 = {2 * t_cnt}')}; squares: {m(f'{s_cnt} \\times 5 = {5 * s_cnt}')}; circle: {m(f'{c_cnt} \\times 3 = {3 * c_cnt}')}.",
                    f"Total score = {m(f'{2 * t_cnt} + {5 * s_cnt} + {3 * c_cnt} = {ans}')}.",
                ],
                f"Check: {m(f'{2 * t_cnt} + {5 * s_cnt} + {3 * c_cnt} = {ans}')} points!",
                "نحسب نقاط كل نوع من الأشكال على حدة ثم نجمعها.",
                [
                    f"نقاط المثلثات {m(2 * t_cnt)}، والمربعات {m(5 * s_cnt)}، والدائرة {m(3 * c_cnt)}.",
                    f"المجموع الكلي = {m(f'{2 * t_cnt} + {5 * s_cnt} + {3 * c_cnt} = {ans}')}.",
                ],
                f"تحقق: {m(ans)} نقطة!",
                diagram_en=svg_pre_shape_collage(t_cnt, s_cnt, c_cnt),
            )
        else:
            sq_sides = 4 * s_cnt
            tr_sides = 3 * t_cnt
            ans = abs(sq_sides - tr_sides)
            B.add_math(
                tp, "Medium", bp,
                f"Look at {nm_en}'s shape board ({m(t_cnt)} triangle(s), {m(s_cnt)} squares, and {m(c_cnt)} circles). What is the **difference** between the total number of straight sides on the triangles ({m(3)} each) and the total number of straight sides on the squares ({m(4)} each)?",
                f"انظر إلى لوحة أشكال {nm_ar} ({m(t_cnt)} من المثلثات و{m(s_cnt)} مربعات و{m(c_cnt)} دائرتان). ما **الفرق** بين إجمالي الأضلاع المستقيمة للمثلثات وإجمالي الأضلاع المستقيمة للمربعات؟",
                ans, [sq_sides + tr_sides, abs(s_cnt - t_cnt), ans + 2, max(1, ans - 2)],
                f"Compare {m(f'{t_cnt} \\times 3 = {tr_sides}')} triangle sides with {m(f'{s_cnt} \\times 4 = {sq_sides}')} square sides!",
                f"قارن بين أضلاع المثلثات ({m(tr_sides)}) وأضلاع المربعات ({m(sq_sides)})!",
                "Compute total triangle sides and total square sides, then subtract the smaller from the larger.",
                [
                    f"Triangle straight sides = {m(f'{t_cnt} \\times 3 = {tr_sides}')}; square straight sides = {m(f'{s_cnt} \\times 4 = {sq_sides}')}.",
                    f"Difference = {m(f'{max(sq_sides, tr_sides)} - {min(sq_sides, tr_sides)} = {ans}')}.",
                ],
                f"Circles have {m(0)} straight sides, so {m(ans)} is exact!",
                "نحسب أضلاع المثلثات وأضلاع المربعات ثم نطرح الأصغر من الأكبر.",
                [
                    f"أضلاع المثلثات = {m(tr_sides)}، وأضلاع المربعات = {m(sq_sides)}.",
                    f"الفرق بينهما = {m(f'{max(sq_sides, tr_sides)} - {min(sq_sides, tr_sides)} = {ans}')}.",
                ],
                f"تحقق: الفرق الصحيح هو {m(ans)}!",
                diagram_en=svg_pre_shape_collage(t_cnt, s_cnt, c_cnt),
            )

    shp_hard = [
        (2, 1, 3, "Joey", "جوي"),
        (3, 1, 6, "Mimi", "ميمي"),
        (2, 2, 6, "Koko", "كوكو"),
        (4, 1, 10, "Bibi", "بيبي"),
        (3, 2, 12, "Toto", "توتو"),
    ]
    for b_parts, n_lv, expected_tri, nm_en, nm_ar in shp_hard:
        ans = n_lv * (b_parts * (b_parts + 1) // 2)
        assert ans == expected_tri
        per_lv = b_parts * (b_parts + 1) // 2
        B.add_math(
            tp, "Hard", bp,
            f"How many **triangles of ALL sizes** (counting both small single triangles AND bigger combined triangles!) can {nm_en} find in this figure?",
            f"كم **مثلثاً من جميع الأحجام** (باحتساب المثلثات الصغيرة والمثلثات الأكبر المكوّنة من دمجها معاً!) يمكن أن يجد {nm_ar} في هذا الشكل؟",
            ans, [b_parts * n_lv, per_lv if n_lv > 1 else b_parts, ans - 1, ans + 2],
            f"Don't stop at the smallest pieces — glue neighbor slices together from the top corner to find wider triangles too!",
            f"لا تكتفِ بالمثلثات الصغيرة فقط — ادمج القطع المتجاورة من الرأس العلوي لتجد المثلثات الأعرض أيضاً!",
            "Count single, double, and wider triangles sharing the top corner on each horizontal base line.",
            [
                f"Using one horizontal base line with {m(b_parts)} slices gives {m(' + '.join(str(k) for k in range(b_parts, 0, -1)) + f' = {per_lv}')} triangles.",
                (
                    f"With only {m(1)} base line, there are **{m(ans)}** triangles in all."
                    if n_lv == 1
                    else f"There are {m(n_lv)} horizontal base lines (middle line and bottom line; the lower strips alone have 4 sides, not 3!), giving {m(f'{n_lv} \\times {per_lv} = {ans}')} triangles."
                ),
            ],
            f"Systematic count by size confirms **{m(ans)}** triangles!",
            "نعدّ المثلثات المفردة والمندمجة التي تشترك في الرأس العلوي فوق كل خط قاعدة أفقي.",
            [
                f"على خط القاعدة الواحد المقسّم إلى {m(b_parts)} أجزاء يتكوّن {m(per_lv)} مثلثات (صغيرة ومندمجة).",
                (
                    f"إذن العدد الكلي للمثلثات هو **{m(ans)}**."
                    if n_lv == 1
                    else f"وبما أن هناك خطي قاعدة أفقيين (الأوسط والسفلي)، فإن العدد الكلي = {m(f'{n_lv} \\times {per_lv} = {ans}')} مثلثاً."
                ),
            ],
            f"تحقق: العدد الدقيق لكل المثلثات هو **{m(ans)}**!",
            diagram_en=svg_subdivided_apex_triangle(b_parts, n_lv),
        )

    # 10. kang_pre_grid_tile_completion (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_grid_tile_completion"
    tile_easy = [
        (4, 3, 4, "Jude", "جود"),
        (5, 2, 2, "Salman", "سلمان"),
        (4, 4, 6, "Rayan", "ريان"),
        (5, 4, 8, "Dana", "دانة"),
        (3, 4, 2, "Karam", "كرم"),
    ]
    for cols, rows, shaded, nm_en, nm_ar in tile_easy:
        tot_sq = cols * rows
        white_sq = tot_sq - shaded
        assert white_sq % 2 == 0
        ans = white_sq // 2
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en}'s {m(f'{cols} \\times {rows}')} game board has **{m(shaded)} purple squares** already covered, and the rest are empty white squares. Each wooden **domino** covers **exact {m(2)} white squares**. How many dominoes are needed to cover all the empty white squares?",
            f"لوحة لعب {nm_ar} ذات الأبعاد {m(f'{cols} \\times {rows}')} فيها **{m(shaded)} مربعات بنفسجية** مغطاة، والباقي مربعات بيضاء فارغة. كل قطعة **دومينو** تغطي **مربعين أبيضين بالضبط**. كم قطعة دومينو تلزم لتغطية كل المربعات البيضاء؟",
            ans, [white_sq, tot_sq // 2, ans + 1, max(1, ans - 1)],
            f"First find how many white squares are empty ({m(f'{tot_sq} - {shaded} = {white_sq}')}), then group them in pairs of {m(2)}!",
            f"أوجد أولاً عدد المربعات البيضاء الفارغة ({m(f'{tot_sq} - {shaded} = {white_sq}')})، ثم قسّمها اثنين اثنين!",
            "Subtract shaded squares from total board squares, then divide by 2 squares per domino.",
            [
                f"Total squares on the {m(f'{cols} \\times {rows}')} board = {m(tot_sq)}, leaving {m(f'{tot_sq} - {shaded} = {white_sq}')} white squares.",
                f"Since 1 domino covers 2 squares, {nm_en} needs {m(white_sq)} split into twos = **{m(ans)}** dominoes.",
            ],
            f"Check: {m(f'{ans} \\times 2 + {shaded} = {tot_sq}')} squares!",
            "نحسب عدد المربعات البيضاء الفارغة ثم نقسمها على 2 لأن كل دومينو يغطي مربعين.",
            [
                f"إجمالي المربعات = {m(tot_sq)}، والبيضاء الفارغة = {m(f'{tot_sq} - {shaded} = {white_sq}')}.",
                f"عدد قطع الدومينو اللازمة = نصف {m(white_sq)} = **{m(ans)}**.",
            ],
            f"تحقق: {m(f'{ans} \\times 2 + {shaded} = {tot_sq}')} مربعاً!",
            diagram_en=svg_fraction_grid(cols, rows, shaded),
        )

    tile_med = [
        ([[1, 1, 0, 0], [1, 0, 0, 2], [0, 0, 2, 2]], "tromino", "Maya", "مايا"),
        ([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 2], [0, 0, 2, 2]], "tromino", "Faris", "فارس"),
        ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 2, 2], [0, 0, 0, 2, 2]], "tromino", "Layan", "ليان"),
        ([[1, 1, 0, 0], [1, 0, 0, 2], [0, 0, 0, 2]], "stars2", "Sami", "سامي"),
        ([[1, 1, 2, 2], [1, 0, 0, 2], [0, 0, 0, 0]], "stars2", "Tala", "تالا"),
    ]
    for board, mmode, nm_en, nm_ar in tile_med:
        rows_n, cols_n = len(board), len(board[0])
        white_cnt = sum(1 for r in board for v in r if v == 0)
        colored_cnt = rows_n * cols_n - white_cnt
        if mmode == "tromino":
            assert white_cnt % 3 == 0
            ans = white_cnt // 3
            B.add_math(
                tp, "Medium", bp,
                f"On {nm_en}'s {m(f'{rows_n} \\times {cols_n}')} tile tray, {m(colored_cnt)} squares are already covered by colored pieces, leaving empty white squares. Each **3-square L-tile** covers **exact {m(3)} unit squares**. How many 3-square tiles are needed to cover all the white squares?",
                f"على لوحة {nm_ar} ذات الحجم {m(f'{rows_n} \\times {cols_n}')}، هناك {m(colored_cnt)} مربعات مغطاة بقطع ملونة والباقي مربعات بيضاء فارغة. إذا كانت كل قطعة جديدة تغطي **{m(3)} مربعات بالضبط**، فكم قطعة ثلاثية تلزم لتغطية كل المربعات البيضاء؟",
                ans, [white_cnt, white_cnt // 2, ans + 1, max(1, ans - 1)],
                f"Count the empty white squares ({m(white_cnt)}) and group them by threes!",
                f"عُدّ المربعات البيضاء الفارغة ({m(white_cnt)}) وقسّمها ثلاثات!",
                "Count the uncovered white unit squares and divide into groups of 3.",
                [
                    f"The {m(f'{rows_n} \\times {cols_n}')} tray has {m(rows_n * cols_n)} squares in all, with {m(white_cnt)} white squares uncovered.",
                    f"Grouping {m(white_cnt)} white squares into threes gives **{m(ans)}** tiles.",
                ],
                f"Check: {m(f'{ans} \\times 3 + {colored_cnt} = {rows_n * cols_n}')}!",
                "نحسب عدد المربعات البيضاء غير المغطاة ثم نقسمها إلى مجموعات من 3.",
                [
                    f"اللوحة فيها {m(rows_n * cols_n)} مربعاً، منها {m(white_cnt)} مربعات بيضاء فارغة.",
                    f"بتقسيم {m(white_cnt)} على {m(3)} نجد أننا نحتاج **{m(ans)}** قطع ثلاثية.",
                ],
                f"تحقق: {m(f'{ans} \\times 3 + {colored_cnt} = {rows_n * cols_n}')}!",
                diagram_en=svg_kang_polyomino_board(board),
            )
        else:
            ans = 2 * white_cnt
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en}'s {m(f'{rows_n} \\times {cols_n}')} craft grid has {m(colored_cnt)} colored squares and empty white squares. {nm_en} glues **{m(2)} tiny shells** inside **each empty white square**. How many tiny shells does {nm_en} glue in total?",
                f"في شبكة الأعمال اليدوية ({m(f'{rows_n} \\times {cols_n}')}) لدى {nm_ar} توجد {m(colored_cnt)} مربعات ملونة ومربعات بيضاء فارغة. تلصق {nm_ar} **{m(2)} صدفة صغيرة** داخل **كل مربع أبيض فارغ**. كم صدفة تلصق إجمالاً؟",
                ans, [white_cnt, 2 * colored_cnt, ans + 2, ans - 2],
                f"Count the white squares ({m(white_cnt)}) first, then double that number!",
                f"عُدّ المربعات البيضاء الفارغة ({m(white_cnt)}) أولاً، ثم ضاعف العدد!",
                "Find the number of empty white unit squares and multiply by 2.",
                [
                    f"Out of {m(rows_n * cols_n)} grid squares, {m(f'{rows_n * cols_n} - {colored_cnt} = {white_cnt}')} are white.",
                    f"Putting {m(2)} shells in each gives {m(f'{white_cnt} + {white_cnt} = {ans}')} shells.",
                ],
                f"Check: {m(f'{white_cnt} \\times 2 = {ans}')} shells!",
                "نوجد عدد المربعات البيضاء الفارغة ثم نضاعف العدد (نضرب في 2).",
                [
                    f"عدد المربعات البيضاء = {m(f'{rows_n * cols_n} - {colored_cnt} = {white_cnt}')}.",
                    f"عدد الأصداف الكلي = {m(f'{white_cnt} + {white_cnt} = {ans}')}.",
                ],
                f"تحقق: {m(f'{white_cnt} \\times 2 = {ans}')} صدفة!",
                diagram_en=svg_kang_polyomino_board(board),
            )

    tile_hard = [
        ([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], "square", "Kangy", "الكنغر"),
        ([(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2)], "square", "Lina", "لينا"),
        ([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2)], "square", "Omar", "عمر"),
        ([(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (2, 3), (3, 3)], "square", "Sara", "سارة"),
        ([(0, 0), (2, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], "square", "Tariq", "طارق"),
    ]
    for cells, _, nm_en, nm_ar in tile_hard:
        w_span = max(c for c, _ in cells) - min(c for c, _ in cells) + 1
        h_span = max(r for _, r in cells) - min(r for _, r in cells) + 1
        side = max(w_span, h_span)
        ans = side * side - len(cells)
        rect_trap = w_span * h_span - len(cells)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} glued **{m(len(cells))} identical unit squares** together as shown. Without cutting or overlapping, what is the **smallest** number of extra unit squares (lined up with the grid) {nm_en} must attach to turn this shape into a **complete solid square**?",
            f"ألصق {nm_ar} عدد **{m(len(cells))} مربعات وحدة متطابقة** كما في الشكل. من دون قص أو تداخل، ما **أقل** عدد من مربعات الوحدة الإضافية (على نفس محاذاة الشبكة) يجب إلصاقها لتحويل الشكل إلى **مربع كامل مصمت**؟",
            ans, [rect_trap if rect_trap != ans else ans + 2, side * side, ans + 1, max(1, ans - 2)],
            f"Measure how wide ({m(w_span)}) and how tall ({m(h_span)}) the shape already is — a full **square** must have equal width and height ({m(f'{side} \\times {side}')})!",
            f"قِس عرض الشكل ({m(w_span)}) وارتفاعه ({m(h_span)}) — لكي يصبح **مربعاً** يجب أن يتساوى عرضه وارتفاعه عند {m(f'{side} \\times {side}')}!",
            "Find the smallest bounding square side max(width, height), then subtract the existing unit squares.",
            [
                f"The shape spans {m(w_span)} units wide and {m(h_span)} units tall, so the smallest grid-aligned **square** around it is {m(f'{side} \\times {side} = {side * side}')} unit squares.",
                f"Since {m(len(cells))} unit squares are already there, {nm_en} needs {m(f'{side * side} - {len(cells)} = {ans}')} extra unit squares.",
            ],
            f"Check: {m(f'{len(cells)} + {ans} = {side * side} = {side} \\times {side}')}!",
            "نحدد طول ضلع أصغر مربع يحوي الشكل (الأكبر بين العرض والارتفاع) ثم نطرح المربعات الموجودة.",
            [
                f"يمتد الشكل بعرض {m(w_span)} وارتفاع {m(h_span)}، فأصغر **مربع** كامل يحويه هو {m(f'{side} \\times {side} = {side * side}')} مربع وحدة.",
                f"نطرح المربعات الموجودة ({m(len(cells))}): {m(f'{side * side} - {len(cells)} = {ans}')} مربعاً إضافياً.",
            ],
            f"تحقق: {m(f'{len(cells)} + {ans} = {side * side}')}!",
            diagram_en=svg_polyomino(cells),
        )

    # 11. kang_pre_stamp_mirror_turns (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_stamp_mirror_turns"
    corner_pairs = [
        ("Top-left corner", "الركن العلوي الأيسر"),
        ("Top-right corner", "الركن العلوي الأيمن"),
        ("Bottom-left corner", "الركن السفلي الأيسر"),
        ("Bottom-right corner", "الركن السفلي الأيمن"),
        ("Center square", "المربع الأوسط"),
    ]
    rc_to_corner_idx = {(0, 0): 0, (0, 2): 1, (2, 0): 2, (2, 2): 3, (1, 1): 4}

    stamp_easy = [
        ([[2, 1, 0], [0, 1, 0], [0, 0, 0]], "horiz", (0, 0), "Nora", "نورة"),
        ([[0, 0, 2], [0, 1, 1], [0, 0, 0]], "vert", (0, 2), "Zaid", "زيد"),
        ([[0, 0, 0], [1, 0, 0], [2, 1, 0]], "horiz", (2, 0), "Hala", "هلا"),
        ([[0, 1, 0], [0, 0, 1], [0, 0, 2]], "vert", (2, 2), "Yousef", "يوسف"),
        ([[0, 0, 2], [1, 1, 0], [0, 0, 0]], "horiz", (0, 2), "Amal", "أمل"),
    ]
    for grid, flip_kind, dot_rc, nm_en, nm_ar in stamp_easy:
        r0, c0 = dot_rc
        assert grid[r0][c0] == 2
        new_rc = (r0, 2 - c0) if flip_kind == "horiz" else (2 - r0, c0)
        cidx = rc_to_corner_idx[new_rc]
        flip_en = "left-to-right across a vertical mirror on its right side" if flip_kind == "horiz" else "top-to-bottom across a horizontal mirror under its bottom edge"
        flip_ar = "من اليسار إلى اليمين عبر مرآة رأسية على جانبها الأيمن" if flip_kind == "horiz" else "من الأعلى إلى الأسفل عبر مرآة أفقية تحت حافتها السفلية"
        B.add_bilingual(
            tp, "Easy", bp,
            f"{nm_en} flips this {m('3 \\times 3')} clear card **{flip_en}**. Where does the special blue square with the **dark dot (`•`)** land after the flip?",
            f"يقلب {nm_ar} هذه البطاقة الشفافة ({m('3 \\times 3')}) **{flip_ar}**. أين يستقر المربع الأزرق المميّز **بالنقطة الداكنة (`•`)** بعد القلب؟",
            corner_pairs, cidx,
            "A left-right mirror swaps Left ↔ Right (keeping Top/Bottom the same); a top-bottom mirror swaps Top ↔ Bottom (keeping Left/Right the same)!",
            "القلب الأفقي يبدّل اليسار ↔ اليمين فقط، والقلب الرأسي يبدّل الأعلى ↔ الأسفل فقط!",
            "Reflect the row or column coordinate of the dotted square across the mirror line.",
            [
                f"Before the flip, the dotted blue square sits in the **{corner_pairs[rc_to_corner_idx[dot_rc]][0]}**.",
                f"Flipping {('left ↔ right' if flip_kind == 'horiz' else 'top ↔ bottom')} moves it to the **{corner_pairs[cidx][0]}**.",
            ],
            f"Mirror check: flipping back returns it to `{corner_pairs[rc_to_corner_idx[dot_rc]][0]}`!",
            "نعكس موضع المربع ذي النقطة عبر خط المرآة المحدد.",
            [
                f"قبل القلب يقع المربع ذو النقطة في **{corner_pairs[rc_to_corner_idx[dot_rc]][1]}**.",
                f"وبعد القلب ينتقل إلى **{corner_pairs[cidx][1]}**.",
            ],
            f"تحقق: إعادته بالمرآة يرجعه إلى مكانه الأصلي!",
            diagram_en=svg_kang_stamp_grid(grid),
        )

    edge_pairs = [
        ("Top-middle square", "مربع أعلى الوسط"),
        ("Right-middle square", "مربع يمين الوسط"),
        ("Bottom-middle square", "مربع أسفل الوسط"),
        ("Left-middle square", "مربع يسار الوسط"),
        ("Center square", "المربع الأوسط"),
    ]
    rc_to_edge_idx = {(0, 1): 0, (1, 2): 1, (2, 1): 2, (1, 0): 3, (1, 1): 4}

    stamp_med = [
        ([[2, 1, 0], [0, 1, 0], [0, 0, 1]], "cw90", (0, 0), "corner", "Joey", "جوي"),
        ([[0, 0, 2], [1, 0, 0], [1, 1, 0]], "rot180", (0, 2), "corner", "Mimi", "ميمي"),
        ([[0, 2, 0], [1, 1, 0], [0, 0, 1]], "cw90", (0, 1), "edge", "Koko", "كوكو"),
        ([[1, 0, 0], [2, 1, 0], [0, 1, 0]], "rot180", (1, 0), "edge", "Bibi", "بيبي"),
        ([[0, 0, 1], [0, 1, 2], [1, 0, 0]], "ccw90", (1, 2), "edge", "Toto", "توتو"),
    ]
    for grid, rot_kind, dot_rc, grp, nm_en, nm_ar in stamp_med:
        r0, c0 = dot_rc
        assert grid[r0][c0] == 2
        if rot_kind == "cw90":
            new_rc = (c0, 2 - r0)
            rot_en, rot_ar = "a **quarter-turn clockwise** (like clock hands moving from 12 to 3)", "**ربع دورة مع عقارب الساعة** (من 12 إلى 3)"
        elif rot_kind == "ccw90":
            new_rc = (2 - c0, r0)
            rot_en, rot_ar = "a **quarter-turn counter-clockwise** (from 3 back up to 12)", "**ربع دورة عكس عقارب الساعة** (من 3 صعوداً إلى 12)"
        else:
            new_rc = (2 - r0, 2 - c0)
            rot_en, rot_ar = "a **half-turn upside down**", "**نصف دورة رأساً على عقب**"
        opts_list = corner_pairs if grp == "corner" else edge_pairs
        idx_map = rc_to_corner_idx if grp == "corner" else rc_to_edge_idx
        cidx = idx_map[new_rc]
        B.add_bilingual(
            tp, "Medium", bp,
            f"{nm_en} turns this {m('3 \\times 3')} card by {rot_en} without flipping it over. Where does the blue square with the **dark dot (`•`)** end up?",
            f"يدير {nm_ar} هذه البطاقة ({m('3 \\times 3')}) بمقدار {rot_ar} من دون قلبها على ظهرها. أين يصبح المربع الأزرق ذو **النقطة الداكنة (`•`)**؟",
            opts_list, cidx,
            "Put your finger on the dotted square and turn it around the center square just like the hand of a clock!",
            "ضع إصبعك على المربع ذي النقطة وأدره حول المربع الأوسط كما تدور عقارب الساعة!",
            "Track the dotted square around the center of the 3×3 card under the given rotation.",
            [
                f"The dotted square starts at the **{opts_list[idx_map[dot_rc]][0]}**.",
                f"Turning the card by {rot_en} carries that spot to the **{opts_list[cidx][0]}**.",
            ],
            f"Rotation check: `{opts_list[idx_map[dot_rc]][0]}` → `{opts_list[cidx][0]}`!",
            "نتتبع دوران المربع ذي النقطة حول مركز الشبكة حسب اتجاه ومقدار الدوران.",
            [
                f"يبدأ المربع ذو النقطة في **{opts_list[idx_map[dot_rc]][1]}**.",
                f"وبعد الدوران ينتقل إلى **{opts_list[cidx][1]}**.",
            ],
            f"تحقق: الموقع الجديد الصحيح هو `{opts_list[cidx][1]}`!",
            diagram_en=svg_kang_stamp_grid(grid),
        )

    stamp_hard = [
        ([[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]], "lr", "Jude", "جود"),
        ([[1, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0]], "lr", "Salman", "سلمان"),
        ([[1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]], "lr", "Rayan", "ريان"),
        ([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], "tb", "Dana", "دانة"),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], "tb", "Karam", "كرم"),
    ]
    for grid, fold_dir, nm_en, nm_ar in stamp_hard:
        rows_n, cols_n = len(grid), len(grid[0])
        tot_shaded = sum(sum(r) for r in grid)
        if fold_dir == "lr":
            assert cols_n % 2 == 0
            ans = sum(1 for r in range(rows_n) for c in range(cols_n // 2) if grid[r][c] or grid[r][cols_n - 1 - c])
            overlap_both = sum(1 for r in range(rows_n) for c in range(cols_n // 2) if grid[r][c] and grid[r][cols_n - 1 - c])
            dir_en = f"in half **from left to right** (creating a {m(f'{rows_n} \\times {cols_n // 2}')} folded rectangle)"
            dir_ar = f"من المنتصف **من اليسار إلى اليمين** (لتصبح مستطيلاً مطوياً بحجم {m(f'{rows_n} \\times {cols_n // 2}')})"
        else:
            assert rows_n % 2 == 0
            ans = sum(1 for r in range(rows_n // 2) for c in range(cols_n) if grid[r][c] or grid[rows_n - 1 - r][c])
            overlap_both = sum(1 for r in range(rows_n // 2) for c in range(cols_n) if grid[r][c] and grid[rows_n - 1 - r][c])
            dir_en = f"in half **from top to bottom** (creating a {m(f'{rows_n // 2} \\times {cols_n}')} folded rectangle)"
            dir_ar = f"من المنتصف **من الأعلى إلى الأسفل** (لتصبح مستطيلاً مطوياً بحجم {m(f'{rows_n // 2} \\times {cols_n}')})"
        assert ans == tot_shaded - overlap_both
        B.add_math(
            tp, "Hard", bp,
            f"This clear plastic sheet ({m(f'{rows_n} \\times {cols_n}')}) has **{m(tot_shaded)} shaded purple squares**. {nm_en} folds the sheet {dir_en}. Because the plastic is see-through, a folded square looks shaded if **either** layer is shaded! How many squares look shaded after folding?",
            f"هذه الورقة الشفافة ({m(f'{rows_n} \\times {cols_n}')}) فيها **{m(tot_shaded)} مربعات مظللة**. يطويها {nm_ar} {dir_ar}. ولأن الورقة شفافة يبدو المربع مظللاً إذا كانت **إحدى الطبقتين أو كلتاهما** مظللة! كم مربعاً يبدو مظللاً بعد الطي؟",
            ans, [tot_shaded, overlap_both, ans + 1 if ans + 1 != tot_shaded else ans + 2, max(1, ans - 1)],
            f"Start with all {m(tot_shaded)} shaded squares, and subtract {m(1)} for each pair of shaded squares that land **right on top of each other**!",
            f"ابدأ بجميع المربعات المظللة ({m(tot_shaded)})، واطرح {m(1)} عن كل زوج من المربعات المظللة ينطبقان **فوق بعضهما تماماً**!",
            "Pair mirror-opposite cells across the fold line; subtract overlapping shaded pairs from the total shaded count.",
            [
                f"There are {m(tot_shaded)} shaded squares before folding.",
                f"Exact {m(overlap_both)} pair(s) of shaded squares land right on top of each other when folded, so we see {m(f'{tot_shaded} - {overlap_both} = {ans}')} shaded squares.",
            ],
            f"Cell-by-cell check on the folded half confirms **{m(ans)}** shaded squares!",
            "نطابق كل مربع مع نظيره عبر خط الطي؛ الأزواج المظللة المتطابقة تُعدّ مربعاً واحداً بعد الطي.",
            [
                f"عدد المربعات المظللة قبل الطي = {m(tot_shaded)}.",
                f"ينطبق {m(overlap_both)} زوج/أزواج من المربعات المظللة فوق بعضها، فيظهر لدينا {m(f'{tot_shaded} - {overlap_both} = {ans}')} مربعات مظللة.",
            ],
            f"تحقق مربعاً بمربع بعد الطي يعطي **{m(ans)}** تماماً!",
            diagram_en=svg_kang_stamp_grid(grid),
        )

    # 12. kang_pre_toy_cube_stacks (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_toy_cube_stacks"
    cube_easy = [
        ((3, 2, 1), 15, "left_in_box", "Maya", "مايا"),
        ((2, 4, 2), 18, "left_in_box", "Faris", "فارس"),
        ((3, 1, 3, 2), 20, "left_in_box", "Layan", "ليان"),
        ((2, 3, 2), 0, "two_towers", "Sami", "سامي"),
        ((4, 2, 3, 1), 0, "two_towers", "Tala", "تالا"),
    ]
    for cols_h, box_tot, emode, nm_en, nm_ar in cube_easy:
        used = sum(cols_h)
        cols_desc = ", ".join(str(x) for x in cols_h)
        if emode == "left_in_box":
            ans = box_tot - used
            B.add_math(
                tp, "Easy", bp,
                f"{nm_en} starts with **{m(box_tot)} wooden cubes** in a toy box and uses some to build this tower (with column heights {m(cols_desc)} from back-left to front-right). How many cubes are **still left inside the toy box**?",
                f"لدى {nm_ar} في صندوق الألعاب **{m(box_tot)} مكعباً خشبياً**، واستعمل بعضها لبناء هذا البرج (بارتفاعات الأعمدة {m(cols_desc)}). كم مكعباً **بقي داخل الصندوق**؟",
                ans, [used, ans + 2, max(1, ans - 1), box_tot - len(cols_h)],
                f"Add the heights of the columns ({' + '.join(str(x) for x in cols_h)}) to see how many cubes are in the tower, then subtract from {m(box_tot)}!",
                f"اجمع ارتفاعات الأعمدة ({' + '.join(str(x) for x in cols_h)}) لمعرفة مكعبات البرج، ثم اطرحها من {m(box_tot)}!",
                "Sum the cubes in all columns of the tower and subtract from the starting box count.",
                [
                    f"Cubes used in the tower = {m(' + '.join(str(x) for x in cols_h) + f' = {used}')}.",
                    f"Cubes remaining in the box = {m(f'{box_tot} - {used} = {ans}')}.",
                ],
                f"Check: {m(f'{used} + {ans} = {box_tot}')} cubes!",
                "نجمع عدد المكعبات في أعمدة البرج ثم نطرحه من العدد الأصلي في الصندوق.",
                [
                    f"المكعبات المستعملة في البرج = {m(' + '.join(str(x) for x in cols_h) + f' = {used}')}.",
                    f"المتبقي في الصندوق = {m(f'{box_tot} - {used} = {ans}')}.",
                ],
                f"تحقق: {m(f'{used} + {ans} = {box_tot}')} مكعباً!",
                diagram_en=svg_cube_stack_3d(cols_h),
            )
        else:
            ans = 2 * used
            B.add_math(
                tp, "Easy", bp,
                f"{nm_en} builds the block staircase shown (column heights {m(cols_desc)}), and {nm_en}'s twin builds a **second identical** block staircase right beside it. How many unit cubes do **both staircases use altogether**?",
                f"يبني {nm_ar} درج المكعبات المرسوم (بارتفاعات الأعمدة {m(cols_desc)})، وتبني أخته التوأم **درجاً ثانياً مطابقاً له تماماً**. كم مكعب وحدة في **الدرجين معاً**؟",
                ans, [used, ans - 2, ans + 2, used + len(cols_h)],
                f"Count the cubes in one staircase ({m(used)}), then double that number!",
                f"احسب عدد المكعبات في الدرج الواحد ({m(used)})، ثم ضاعف العدد!",
                "Add the column heights of one tower and double the result.",
                [
                    f"One staircase uses {m(' + '.join(str(x) for x in cols_h) + f' = {used}')} cubes.",
                    f"Two identical staircases use {m(f'{used} + {used} = {ans}')} cubes.",
                ],
                f"Check: {m(f'2 \\times {used} = {ans}')} cubes!",
                "نجمع مكعبات الشكل الواحد ثم نضاعف الناتج للشكلين المتطابقين.",
                [
                    f"عدد مكعبات الشكل الواحد = {m(used)}.",
                    f"للشكلين معاً: {m(f'{used} + {used} = {ans}')} مكعباً.",
                ],
                f"تحقق: {m(f'2 \\times {used} = {ans}')}!",
                diagram_en=svg_cube_stack_3d(cols_h),
            )

    cube_med = [
        ((3, 1, 2), 3, "Kangy", "الكنغر"),
        ((4, 2, 1, 3), 4, "Lina", "لينا"),
        ((2, 4, 1, 2), 4, "Omar", "عمر"),
        ((1, 3, 2, 1, 3), 4, "Sara", "سارة"),
        ((3, 2, 4, 1), 5, "Tariq", "طارق"),
    ]
    for cols_h, target_h, nm_en, nm_ar in cube_med:
        have = sum(cols_h)
        full_wall = len(cols_h) * target_h
        ans = full_wall - have
        assert ans == sum(target_h - h for h in cols_h)
        cols_desc = ", ".join(str(x) for x in cols_h)
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en}'s tower has **{m(len(cols_h))} columns** of heights {m(cols_desc)}. How many **more unit cubes** must {nm_en} stack on top so that **every single column is exact {m(target_h)} cubes tall**?",
            f"يتكوّن برج {nm_ar} من **{m(len(cols_h))} أعمدة** بارتفاعات {m(cols_desc)}. كم **مكعب وحدة إضافياً** يجب وضعه فوق الأعمدة ليصبح ارتفاع **كل عمود {m(target_h)} مكعبات بالضبط**؟",
            ans, [have, full_wall, ans + 1, max(1, ans - 1)],
            f"A flat wall of {m(len(cols_h))} columns each {m(target_h)} tall holds {m(f'{len(cols_h)} \\times {target_h} = {full_wall}')} cubes!",
            f"الجدار المتساوي من {m(len(cols_h))} أعمدة بارتفاع {m(target_h)} يضم {m(f'{len(cols_h)} \\times {target_h} = {full_wall}')} مكعباً!",
            "Subtract existing cubes from the full rectangular wall size (or add what each column is missing).",
            [
                f"Missing cubes per column: {' + '.join(str(target_h - h) for h in cols_h)} = **{m(ans)}**.",
                f"Equivalently, {m(f'{len(cols_h)} \\times {target_h} - {have} = {full_wall} - {have} = {ans}')} cubes.",
            ],
            f"Check: {m(f'{have} + {ans} = {full_wall}')} cubes!",
            "نحسب ما ينقص كل عمود للوصول إلى الارتفاع المطلوب ثم نجمع النواقص.",
            [
                f"النواقص فوق الأعمدة بالترتيب: {' + '.join(str(target_h - h) for h in cols_h)} = **{m(ans)}**.",
                f"أو بطرح الموجود من الجدار الكامل: {m(f'{full_wall} - {have} = {ans}')} مكعبات.",
            ],
            f"تحقق: {m(f'{have} + {ans} = {full_wall}')} مكعباً!",
            diagram_en=svg_cube_stack_3d(cols_h),
        )

    cube_hard = [
        ((2, 1), "Nora", "نورة"),
        ((3, 1), "Zaid", "زيد"),
        ((2, 2), "Hala", "هلا"),
        ((3, 2), "Yousef", "يوسف"),
        ((2, 1, 2), "Amal", "أمل"),
    ]
    for cols_h, nm_en, nm_ar in cube_hard:
        tot_c = sum(cols_h)
        top_f = len(cols_h)
        fb_f = 2 * tot_c
        lr_f = cols_h[0] + cols_h[-1] + sum(abs(cols_h[i] - cols_h[i + 1]) for i in range(len(cols_h) - 1))
        ans = top_f + fb_f + lr_f
        # Independent check via 6*tot_c - table_bottoms - 2*(internal glue joints)
        glue_joints = sum(h - 1 for h in cols_h) + sum(min(cols_h[i], cols_h[i + 1]) for i in range(len(cols_h) - 1))
        assert ans == 6 * tot_c - len(cols_h) - 2 * glue_joints
        cols_desc = ", ".join(str(x) for x in cols_h)
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} glues **{m(tot_c)} unit cubes** into a single row of columns (heights {m(cols_desc)}) standing flat on a table, and paints **every outside square face EXCEPT the bottom touching the table**. How many unit square faces get painted?",
            f"يلصق {nm_ar} عدد **{m(tot_c)} مكعبات وحدة** في صف واحد من الأعمدة (بارتفاعات {m(cols_desc)}) موضوعٍ فوق طاولة، ثم يطلي **جميع الأوجه المربعة الخارجية ما عدا القاعدة الملامسة للطاولة**. كم وجهاً مربعاً صغيراً يُطلى؟",
            ans, [ans + len(cols_h), 6 * tot_c, ans - top_f, ans + 2],
            f"Look from **5 directions** (Top, Front, Back, Left end, Right end — plus any step walls between columns)!",
            f"انظر من **5 جهات** (الأعلى، الأمام، الخلف، اليسار، اليمين — ولا تنسَ الجوانب الرأسية بين الأعمدة)!",
            "Count exposed square faces from above, the two long sides, and the left/right/step vertical faces.",
            [
                f"From above: {m(top_f)} top square(s). From the two long sides (front & back): {m(f'{tot_c} + {tot_c} = {fb_f}')} squares.",
                f"Vertical end & step faces: {m(lr_f)} squares, giving {m(f'{top_f} + {fb_f} + {lr_f} = {ans}')} painted faces.",
            ],
            f"Glue check: {m(f'6 \\times {tot_c} - {len(cols_h)} \\text{{ (table)}} - {2 * glue_joints} \\text{{ (glued)}} = {ans}')}!",
            "نعدّ الأوجه الظاهرة من الأعلى، ومن الجانبين الطويلين، ومن الأطراف والدرجات الرأسية.",
            [
                f"من الأعلى: {m(top_f)} أوجه، ومن الأمام والخلف معاً: {m(f'{tot_c} + {tot_c} = {fb_f}')} وجهاً.",
                f"الأوجه الرأسية على الأطراف والدرجات = {m(lr_f)}، فيكون المجموع {m(f'{top_f} + {fb_f} + {lr_f} = {ans}')} وجهاً مطلياً.",
            ],
            f"تحقق بطرح الأوجه المخفية: {m(f'{6 * tot_c} - {len(cols_h) + 2 * glue_joints} = {ans}')}!",
            diagram_en=svg_cube_stack_3d(cols_h),
        )


# ==============================================================================
# UNIT 4 — Geometry Part 2 (60 Questions: KANG-PRE-181 .. KANG-PRE-240)
# Blueprints: kang_pre_grid_step_paths, kang_pre_tree_lamp_gaps,
#             kang_pre_folded_strip_cuts, kang_pre_opposite_die_dots
# ==============================================================================
def _count_grid_routes(cols: int, rows: int, blocked: tuple[int, int] | None = None) -> int:
    dp = [[0] * (rows + 1) for _ in range(cols + 1)]
    dp[0][0] = 1
    for c in range(cols + 1):
        for r in range(rows + 1):
            if (c, r) == (0, 0) or (blocked is not None and (c, r) == blocked):
                if blocked is not None and (c, r) == blocked:
                    dp[c][r] = 0
                continue
            dp[c][r] = (dp[c - 1][r] if c > 0 else 0) + (dp[c][r - 1] if r > 0 else 0)
    return dp[cols][rows]


def _add_unit_1_4(B: BankBuilder) -> None:
    tp = "Geometry"

    # 13. kang_pre_grid_step_paths (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_grid_step_paths"
    path_easy = [
        (2, 2, "LadybugDot", "الدعسوقة المنقطة"),
        (3, 2, "Ant Pip", "النملة بيب"),
        (4, 2, "Snail Shelly", "الحلزون صدفي"),
        (3, 3, "Turtle Toby", "السلحفاة توبي"),
        (4, 3, "Caterpillar Coco", "اليرقة كوكو"),
    ]
    for cols, rows, who_en, who_ar in path_easy:
        ans = cols + rows
        B.add_math(
            tp, "Easy", bp,
            f"{who_en} crawls along the grid lines from green corner `A` (bottom-left) to blue corner `B` (top-right), moving **only Right (`→`) and Up (`↑`)** across the {m(f'{cols} \\times {rows}')} grid. How many **unit grid steps** long is {who_en}'s walk?",
            f"تزحف {who_ar} على خطوط الشبكة ({m(f'{cols} \\times {rows}')}) من الركن الأخضر `A` (أسفل اليسار) إلى الركن الأزرق `B` (أعلى اليمين) بالتحرك **يميناً (`→`) وللأعلى (`↑`) فقط**. كم **خطوة وحدة** يبلغ طول هذه الرحلة؟",
            ans, [cols * rows, ans - 1, ans + 1, ans + 2],
            f"Every shortest walk goes {m(cols)} steps Right and {m(rows)} steps Up — just add them!",
            f"كل مسار أقصر يتحرك {m(cols)} خطوات يميناً و{m(rows)} خطوات للأعلى — اجمعهما فقط!",
            "Add the horizontal steps right and the vertical steps up.",
            [
                f"To go from `A` to `B`, {who_en} must move {m(cols)} unit steps Right and {m(rows)} unit steps Up.",
                f"Total steps = {m(f'{cols} + {rows} = {ans}')}.",
            ],
            f"No matter what order Right and Up are mixed, {m(f'{cols} + {rows} = {ans}')} steps!",
            "نجمع عدد الخطوات الأفقية لليمين مع عدد الخطوات الرأسية للأعلى.",
            [
                f"للانتقال من `A` إلى `B` يلزم {m(cols)} خطوات يميناً و{m(rows)} خطوات للأعلى.",
                f"إجمالي الخطوات = {m(f'{cols} + {rows} = {ans}')}.",
            ],
            f"تحقق: بأي ترتيب للخطوات يبقى الطول {m(f'{cols} + {rows} = {ans}')}!",
            diagram_en=svg_street_grid(cols, rows),
        )

    path_med = [
        (4, 3, [(0, 2), (1, 2), (1, 1)], "Joey", "جوي"),
        (5, 3, [(0, 2), (0, 1), (1, 1), (2, 1)], "Mimi", "ميمي"),
        (4, 4, [(0, 3), (1, 3), (2, 3), (2, 2)], "Koko", "كوكو"),
        (5, 4, [(0, 3), (0, 2), (1, 2), (1, 1), (2, 1)], "Bibi", "بيبي"),
        (5, 3, [(0, 2), (1, 2), (2, 2), (2, 1)], "Toto", "توتو"),
    ]
    for cols, rows, pcells, nm_en, nm_ar in path_med:
        for i in range(len(pcells) - 1):
            assert abs(pcells[i][0] - pcells[i + 1][0]) + abs(pcells[i][1] - pcells[i + 1][1]) == 1
        leg1 = len(pcells) - 1
        c_star, r_star = pcells[-1]
        leg2 = (cols - 1 - c_star) + r_star
        ans = leg1 + leg2
        B.add_math(
            tp, "Medium", bp,
            f"On this {m(f'{cols} \\times {rows}')} floor grid, {nm_en} has already hopped **{m(leg1)} steps** from the green start square `S` to the yellow star square `★`, and will now hop from `★` to the **top-right corner square** using the fewest square-to-square steps (only Right or Up). How many steps is {nm_en}'s **entire** trip from `S` to the top-right square?",
            f"على شبكة الأرضية ({m(f'{cols} \\times {rows}')})، قفز {nm_ar} بالفعل **{m(leg1)} خطوات** من مربع البداية الأخضر `S` إلى مربع النجمة الأصفر `★`، وسيكمل الآن من `★` إلى **مربع الركن العلوي الأيمن** بأقل عدد من الخطوات (يميناً أو للأعلى). كم خطوة يبلغ طول رحلته **الكاملة** من `S` حتى الركن العلوي الأيمن؟",
            ans, [leg2, ans + 1, ans - 1, cols * rows],
            f"Count how many steps Right ({m(cols - 1 - c_star)}) and Up ({m(r_star)}) are still needed from `★` to the top-right square, then add {m(leg1)}!",
            f"عُدّ الخطوات المتبقية من `★` إلى الركن العلوي الأيمن ({m(cols - 1 - c_star)} يميناً و{m(r_star)} للأعلى)، ثم أضفها إلى {m(leg1)}!",
            "Add the first part of the walk (S to ★) and the remaining Right + Up steps from ★ to the top-right square.",
            [
                f"From `S` to `★` takes {m(leg1)} steps.",
                f"From `★` to the top-right corner needs {m(cols - 1 - c_star)} step(s) Right and {m(r_star)} step(s) Up = {m(leg2)} more steps.",
                f"Total trip = {m(f'{leg1} + {leg2} = {ans}')} steps.",
            ],
            f"Notice `S` is bottom-left and every step went Right or Up: {m(f'({cols}-1) + ({rows}-1) = {ans}')}!",
            "نجمع خطوات الجزء الأول حتى `★` مع الخطوات المتبقية يميناً وللأعلى للوصول للركن العلوي الأيمن.",
            [
                f"من `S` إلى `★` قطع {m(leg1)} خطوات.",
                f"ومن `★` إلى الركن العلوي الأيمن يحتاج {m(cols - 1 - c_star)} يميناً + {m(r_star)} للأعلى = {m(leg2)} خطوات.",
                f"المجموع الكلي = {m(f'{leg1} + {leg2} = {ans}')} خطوات.",
            ],
            f"تحقق: الرحلة كلها تتجه يميناً وللأعلى فقط، فالمجموع {m(ans)} خطوات!",
            diagram_en=svg_kang_grid_walk(cols, rows, pcells),
        )

    path_hard = [
        (2, 1, None, "Duckling Sunny", "البطة الصغيرة"),
        (3, 1, None, "Hedgehog Spike", "القنفذ الصغير"),
        (2, 2, None, "Kitten Whiskers", "القطة الصغيرة"),
        (2, 2, (1, 1), "Puppy Biscuit", "الجرو الصغير"),
        (3, 2, (1, 1), "Hamster Nibbles", "الهامستر الصغير"),
    ]
    for cols, rows, blk, who_en, who_ar in path_hard:
        ans = _count_grid_routes(cols, rows, blocked=blk)
        unblk = _count_grid_routes(cols, rows, blocked=None)
        if blk is None:
            q_en = (
                f"{who_en} walks along the grid lines from green corner `A` to blue corner `B`, taking **only Right (`→`) and Up (`↑`)** steps. "
                f"How many **different shortest paths** can {who_en} choose?"
            )
            q_ar = (
                f"يمشي {who_ar} على خطوط الشبكة من الركن الأخضر `A` إلى الركن الأزرق `B` بالتحرك **يميناً (`→`) أو للأعلى (`↑`) فقط**. "
                f"كم **طريقاً أقصر مختلفاً** يمكنه اختياره؟"
            )
        else:
            q_en = (
                f"{who_en} walks along the grid lines from `A` to `B` moving **only Right (`→`) and Up (`↑`)**, and **must stay off** the muddy puddle corner marked `×`. "
                f"How many **different shortest paths** go from `A` to `B`?"
            )
            q_ar = (
                f"يمشي {who_ar} على خطوط الشبكة من `A` إلى `B` بالتحرك **يميناً (`→`) أو للأعلى (`↑`) فقط**، مع **عدم المرور** بركن البركة الطينية `×`. "
                f"كم **طريقاً أقصر مختلفاً** يوصل من `A` إلى `B`؟"
            )
        B.add_math(
            tp, "Hard", bp, q_en, q_ar,
            ans, [unblk if blk else ans + 1, ans + 2, max(1, ans - 1), cols + rows],
            "Write `1` along the bottom and left edges from `A`, then at each corner add (ways from left + ways from below)!",
            "اكتب `1` على حافتي الأسفل واليسار من `A`، وعند كل ركن اجمع (الطرق من اليسار + الطرق من الأسفل)!",
            "Count paths corner-by-corner by adding incoming ways from the left and from below (with 0 at any puddle ×).",
            [
                (
                    f"Adding ways from the left and from below at each corner of the {m(f'{cols} \\times {rows}')} grid gives **{m(ans)}** shortest paths to `B`."
                    if blk is None
                    else f"Setting the puddle corner `×` to {m(0)} ways and adding (left + below) at every other corner leaves **{m(ans)}** valid paths to `B`."
                ),
            ],
            f"Listing every valid arrow sequence (`→` and `↑`) confirms exact **{m(ans)}** paths!",
            "نحسب عدد الطرق عند كل تقاطع بجمع الطرق القادمة من اليسار ومن الأسفل (مع صفر عند `×`).",
            [
                (
                    f"بجمع الطرق عند تقاطعات الشبكة {m(f'{cols} \\times {rows}')} نحصل على **{m(ans)}** طرق مختلفة إلى `B`."
                    if blk is None
                    else f"بجعل التقاطع `×` يساوي {m(0)} وجمع (اليسار + الأسفل) عند باقي التقاطعات نجد **{m(ans)}** طرق صالحة إلى `B`."
                ),
            ],
            f"تحقق: حصر جميع سلاسل الأسهم الصالحة يعطي **{m(ans)}** طرق بالضبط!",
            diagram_en=svg_street_grid(cols, rows, blocked=blk),
        )

    # 14. kang_pre_tree_lamp_gaps (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_tree_lamp_gaps"
    gap_easy = [
        (5, 3, "apple trees", "أشجار تفاح", "Jude", "جود"),
        (6, 4, "garden lamps", "مصابيح حديقة", "Salman", "سلمان"),
        (4, 5, "wooden posts", "أعمدة خشبية", "Rayan", "ريان"),
        (7, 2, "sunflowers", "زهرات عباد شمس", "Dana", "دانة"),
        (8, 3, "park flags", "أعلام ملونة", "Karam", "كرم"),
    ]
    for n_posts, d_m, obj_en, obj_ar, nm_en, nm_ar in gap_easy:
        gaps = n_posts - 1
        ans = gaps * d_m
        B.add_math(
            tp, "Easy", bp,
            f"Along {nm_en}'s walkway, **{m(n_posts)} {obj_en}** stand in a straight line with **{m(d_m)} meters** between every two neighbors. How many meters is it from the **1st** one to the **{m(n_posts)}th** (last) one?",
            f"على ممر {nm_ar} تقف **{m(n_posts)} {obj_ar}** في صف مستقيم، والمسافة بين كل اثنتين متجاورتين **{m(d_m)} أمتار**. كم متراً تبلغ المسافة من **الأولى** حتى **الأخيرة (رقم {m(n_posts)})**؟",
            ans, [n_posts * d_m, (n_posts + 1) * d_m, ans - d_m + 1, ans + 2],
            f"{m(n_posts)} posts in a row have **{m(gaps)} gaps** between them (one fewer than the posts)!",
            f"{m(n_posts)} أعمدة في صف واحد بينها **{m(gaps)} مسافات** (أقل بواحد من عدد الأعمدة)!",
            "Count (n - 1) gaps between n items, then multiply by the gap length.",
            [
                f"Between {m(n_posts)} items in a line, there are {m(f'{n_posts} - 1 = {gaps}')} equal gaps.",
                f"Total distance = {m(f'{gaps} \\times {d_m} = {ans}')} meters.",
            ],
            f"Check on your fingers: {m(5)} fingers have {m(4)} spaces — here {m(n_posts)} items have {m(gaps)} spaces × {m(d_m)} m = {m(ans)} m!",
            "عدد المسافات بين الأشياء المصطفة يقل بواحد عن عددها، ثم نضرب في طول المسافة الواحدة.",
            [
                f"بين {m(n_posts)} عناصر متتالية توجد {m(f'{n_posts} - 1 = {gaps}')} مسافات متساوية.",
                f"المسافة الكلية = {m(f'{gaps} \\times {d_m} = {ans}')} متراً.",
            ],
            f"تحقق: مثل أصابع اليد الـ {m(5)} بينها {m(4)} فراغات — هنا {m(f'{gaps} \\times {d_m} = {ans}')} متراً!",
            diagram_en=svg_fenceposts(f"{d_m} m", "?"),
        )

    gap_med = [
        (12, 3, "Maya", "مايا"),
        (20, 4, "Faris", "فارس"),
        (15, 5, "Layan", "ليان"),
        (18, 2, "Sami", "سامي"),
        (24, 4, "Tala", "تالا"),
    ]
    for tot_l, d_m, nm_en, nm_ar in gap_med:
        assert tot_l % d_m == 0
        gaps = tot_l // d_m
        ans = gaps + 1
        B.add_math(
            tp, "Medium", bp,
            f"A straight park path is **{m(tot_l)} meters** long. {nm_en} sees lanterns placed every **{m(d_m)} meters**, including a lantern at the **very start** and a lantern at the **very end**. How many lanterns stand along the path?",
            f"طول ممر مستقيم في الحديقة **{m(tot_l)} متراً**. يرى {nm_ar} فوانيس موضوعة كل **{m(d_m)} أمتار**، مع وجود فانوس في **بداية الممر تماماً** وفانوس في **نهايته تماماً**. كم فانوساً على طول الممر؟",
            ans, [gaps, gaps - 1, ans + 1, ans + 2],
            f"Divide {m(tot_l)} by {m(d_m)} to count the **gaps** ({m(gaps)}), then **add {m(1)}** for the starting lantern!",
            f"اقسم {m(tot_l)} على {m(d_m)} لمعرفة عدد **المسافات** ({m(gaps)})، ثم **أضف {m(1)}** لفانوس البداية!",
            "Find the number of gaps along the path, then add 1 because both ends have a lantern.",
            [
                f"Number of {m(d_m)}-meter gaps in {m(tot_l)} meters = {m(gaps)} gaps.",
                f"With a lantern at both ends, there are {m(f'{gaps} + 1 = {ans}')} lanterns.",
            ],
            f"Positions in meters: {', '.join(m(k * d_m) for k in range(ans))} → **{m(ans)}** lanterns!",
            "نقسم الطول الكلي على طول المسافة لإيجاد عدد المسافات ثم نضيف 1 لوجود فانوس عند الطرفين.",
            [
                f"عدد المسافات بطول {m(d_m)} م داخل {m(tot_l)} م هو {m(gaps)} مسافات.",
                f"عدد الفوانيس = {m(f'{gaps} + 1 = {ans}')} فوانيس.",
            ],
            f"مواقع الفوانيس بالأمتار: {', '.join(m(k * d_m) for k in range(ans))} وعددها **{m(ans)}**!",
            diagram_en=svg_fenceposts(f"{d_m} m", f"{tot_l} m"),
        )

    gap_hard = [
        ("tulips", 6, 3, 0, "Kangy", "الكنغر"),
        ("tulips", 8, 2, 0, "Lina", "لينا"),
        ("tulips", 5, 4, 0, "Omar", "عمر"),
        ("both_sides", 0, 5, 15, "Sara", "سارة"),
        ("both_sides", 0, 4, 16, "Tariq", "طارق"),
    ]
    for hmode, n_trees, step_or_flw, road_l, nm_en, nm_ar in gap_hard:
        if hmode == "tulips":
            gaps = n_trees - 1
            ans = gaps * step_or_flw
            B.add_math(
                tp, "Hard", bp,
                f"Along {nm_en}'s garden fence, **{m(n_trees)} oak trees** stand in a straight row. Between every two neighbor oak trees, gardeners plant **{m(step_or_flw)} red tulips**. How many **trees and tulips altogether** are in that row?",
                f"بمحاذاة سور حديقة {nm_ar} تقف **{m(n_trees)} أشجار بلوط** في صف مستقيم. وبين كل شجرتي بلوط متجاورتين يزرع البستاني **{m(step_or_flw)} زهرات توليب حمراء**. كم يبلغ مجموع **الأشجار وزهرات التوليب معاً** في هذا الصف؟",
                n_trees + ans, [ans, n_trees * step_or_flw, n_trees + n_trees * step_or_flw, n_trees + ans - 1],
                f"{m(n_trees)} trees create {m(gaps)} gaps of {m(step_or_flw)} tulips — find the tulips ({m(ans)}), then don't forget to add the {m(n_trees)} oak trees!",
                f"{m(n_trees)} أشجار تصنع {m(gaps)} فراغات في كل منها {m(step_or_flw)} زهرات ({m(ans)}) — ثم لا تنسَ إضافة الـ {m(n_trees)} أشجار!",
                "Count tulips in the (n - 1) gaps, then add the n oak trees.",
                [
                    f"{m(n_trees)} oak trees make {m(f'{n_trees} - 1 = {gaps}')} spaces, holding {m(f'{gaps} \\times {step_or_flw} = {ans}')} tulips.",
                    f"Adding the {m(n_trees)} oak trees gives {m(f'{ans} + {n_trees} = {n_trees + ans}')} plants in all.",
                ],
                f"Check: {m(n_trees)} trees + {m(ans)} tulips = **{m(n_trees + ans)}**!",
                "نحسب زهرات التوليب في الفراغات الـ (n - 1) ثم نضيف إليها عدد الأشجار نفسه.",
                [
                    f"بين {m(n_trees)} أشجار توجد {m(gaps)} فراغات فيها {m(f'{gaps} \\times {step_or_flw} = {ans}')} زهرة توليب.",
                    f"بإضافة {m(n_trees)} أشجار يصبح المجموع الكلي {m(f'{ans} + {n_trees} = {n_trees + ans}')}.",
                ],
                f"تحقق: {m(n_trees)} أشجار + {m(ans)} زهرة = **{m(n_trees + ans)}**!",
                diagram_en=svg_fenceposts(f"{step_or_flw} flw", "?"),
            )
        else:
            d_m = step_or_flw
            assert road_l % d_m == 0
            one_side = road_l // d_m + 1
            ans = 2 * one_side
            B.add_math(
                tp, "Hard", bp,
                f"A straight wooden bridge is **{m(road_l)} meters** long. Workers put lamps every **{m(d_m)} meters** (including both ends!) along **BOTH the left railing AND the right railing** of the bridge. How many lamps are on the bridge in all?",
                f"طول جسر خشبي مستقيم **{m(road_l)} متراً**. يثبت العمال مصابيح كل **{m(d_m)} أمتار** (بما في ذلك البداية والنهاية!) على **كلا جانبي الجسر (الأيمن والأيسر معاً)**. كم مصباحاً على الجسر إجمالاً؟",
                ans, [one_side, 2 * (road_l // d_m), ans - 1, ans + 2],
                f"Find how many lamps stand on **one** side ({m(f'{road_l // d_m} + 1 = {one_side}')}), then double it for **both** sides!",
                f"احسب عدد المصابيح على **جانب واحد** ({m(f'{road_l // d_m} + 1 = {one_side}')})، ثم ضاعف العدد **للجانبين معاً**!",
                "Compute (gaps + 1) lamps on one railing, then double for the two railings.",
                [
                    f"On one side: {m(road_l // d_m)} gaps + {m(1)} = {m(one_side)} lamps.",
                    f"On both sides together: {m(f'{one_side} + {one_side} = {ans}')} lamps.",
                ],
                f"Check: {m(f'2 \\times {one_side} = {ans}')} lamps!",
                "نحسب عدد المصابيح على جهة واحدة (عدد المسافات + 1) ثم نضرب في 2 للجهتين.",
                [
                    f"على الجهة الواحدة: {m(road_l // d_m)} مسافات + {m(1)} = {m(one_side)} مصابيح.",
                    f"على الجهتين معاً: {m(f'{one_side} + {one_side} = {ans}')} مصابيح.",
                ],
                f"تحقق: {m(f'2 \\times {one_side} = {ans}')} مصباحاً!",
                diagram_en=svg_fenceposts(f"{d_m} m", f"{road_l} m"),
            )

    # 15. kang_pre_folded_strip_cuts (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_folded_strip_cuts"
    rib_easy = [
        (2, "Nora", "نورة"),
        (3, "Zaid", "زيد"),
        (4, "Hala", "هلا"),
        (5, "Yousef", "يوسف"),
        (6, "Amal", "أمل"),
    ]
    for strands, nm_en, nm_ar in rib_easy:
        ans = strands + 1
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} folds a single long ribbon back and forth so it has **{m(strands)} horizontal layers**, and makes **1 straight scissor cut** (`✂`) right across the middle as shown. How many separate ribbon pieces fall onto the table?",
            f"يطوي {nm_ar} شريطاً واحداً ذهاباً وإياباً ليصبح مكوّناً من **{m(strands)} طبقات أفقية**، ثم يقصه **قصّة مستقيمة واحدة** (`✂`) عبر المنتصف كما في الرسم. كم قطعة منفصلة تنتج بعد القص؟",
            ans, [strands, 2 * strands, ans + 1, max(2, strands - 1)],
            f"The scissors snip the single ribbon **{m(strands)} times** — snipping a string {m(strands)} times always makes {m(f'{strands} + 1')} pieces!",
            f"المقص يقطع الشريط الواحد في **{m(strands)} مواضع** — وقطع خيط في {m(strands)} مواضع يعطي دائماً {m(f'{strands} + 1')} قطع!",
            "Count total snips along the single continuous ribbon (strands × 1), then add 1.",
            [
                f"One straight cut across {m(strands)} layers snips the ribbon {m(strands)} times.",
                f"Cutting a single unlooped ribbon {m(strands)} times creates {m(f'{strands} + 1 = {ans}')} separate pieces.",
            ],
            f"Count on the diagram: {m(2)} loose ends + {m(strands - 1)} curved fold loops = **{m(ans)}** pieces!",
            "كل طبقة تُقص تمثل موضع قطع على الشريط الواحد، وعدد القطع يساوي (عدد القطوع + 1).",
            [
                f"القصّة الواحدة تقطع {m(strands)} طبقات، أي {m(strands)} قطوع في الشريط.",
                f"إذن ينتج {m(f'{strands} + 1 = {ans}')} قطع منفصلة.",
            ],
            f"تحقق من الرسم: طرفان حرّان + {m(strands - 1)} ثنيات منحنية = **{m(ans)}** قطع!",
            diagram_en=svg_kang_folded_ribbon(strands, 1),
        )

    rib_med = [
        (2, 2, "Joey", "جوي"),
        (3, 2, "Mimi", "ميمي"),
        (4, 2, "Koko", "كوكو"),
        (5, 2, "Bibi", "بيبي"),
        (3, 3, "Toto", "توتو"),
    ]
    for strands, cuts, nm_en, nm_ar in rib_med:
        snips = strands * cuts
        ans = snips + 1
        B.add_math(
            tp, "Medium", bp,
            f"{nm_en} folds one ribbon into **{m(strands)} layers** and makes **{m(cuts)} straight scissor cuts** (`✂`) all the way across as shown. How many separate pieces of ribbon are there after cutting?",
            f"يطوي {nm_ar} شريطاً واحداً إلى **{m(strands)} طبقات**، ثم يقصه **{m(cuts)} قصّات مستقيمة** (`✂`) عبر جميع الطبقات كما في الرسم. كم قطعة منفصلة تصبح لديه بعد القص؟",
            ans, [snips, strands + cuts, ans - 2, ans + 2],
            f"Each of the {m(cuts)} cuts snips {m(strands)} layers ({m(f'{strands} \\times {cuts} = {snips}')} snips in all), then add {m(1)}!",
            f"كل قصّة من الـ {m(cuts)} تقطع {m(strands)} طبقات ({m(f'{strands} \\times {cuts} = {snips}')} قطوع)، ثم أضف {m(1)}!",
            "Multiply layers by cuts to count total snips on the single ribbon, then add 1.",
            [
                f"Total snips along the ribbon = {m(f'{strands} \\times {cuts} = {snips}')}.",
                f"Total pieces = {m(f'{snips} + 1 = {ans}')}.",
            ],
            f"Piece breakdown: {m(2)} loose ends + {m(strands - 1)} curved end-loops + {m(strands * (cuts - 1))} middle strips = **{m(ans)}**!",
            "نضرب عدد الطبقات في عدد القصّات لمعرفة إجمالي القطوع على الشريط، ثم نضيف 1.",
            [
                f"إجمالي مواضع القطع = {m(f'{strands} \\times {cuts} = {snips}')}.",
                f"عدد القطع الناتجة = {m(f'{snips} + 1 = {ans}')}.",
            ],
            f"تحقق بالتفصيل: طرفان + {m(strands - 1)} ثنيات + {m(strands * (cuts - 1))} قطع وسطى = **{m(ans)}**!",
            diagram_en=svg_kang_folded_ribbon(strands, cuts),
        )

    rib_hard = [
        ("flat", 2, 2, "Jude", "جود"),
        ("flat", 3, 2, "Salman", "سلمان"),
        ("flat", 4, 2, "Rayan", "ريان"),
        ("two_ribbons", 2, 1, "Dana", "دانة"),
        ("two_ribbons", 3, 2, "Karam", "كرم"),
    ]
    for hmode, strands, cuts, nm_en, nm_ar in rib_hard:
        tot_one = strands * cuts + 1
        bent_one = strands - 1
        flat_one = tot_one - bent_one
        assert flat_one == strands * (cuts - 1) + 2
        if hmode == "flat":
            ans = flat_one
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} folds one ribbon into **{m(strands)} layers** with **{m(bent_one)} curved U-folds** on the ends, then makes **{m(cuts)} straight cuts** (`✂`) through the middle as shown. Out of all the pieces created, how many pieces are **completely straight (with NO curved fold bend)**?",
                f"يطوي {nm_ar} شريطاً واحداً إلى **{m(strands)} طبقات** (فيها **{m(bent_one)} ثنيات منحنية** عند الأطراف)، ثم يقصه **{m(cuts)} قصّتين مستقيمتين** (`✂`) في المنتصف كما في الرسم. كم قطعة من القطع الناتجة تكون **مستقيمة تماماً (بلا أي ثنية منحنية)**؟",
                ans, [tot_one, bent_one, strands * (cuts - 1), ans + 1],
                f"Find total pieces ({m(tot_one)}), then subtract the **{m(bent_one)} curved U-fold pieces** on the left and right ends!",
                f"احسب إجمالي القطع ({m(tot_one)})، ثم اطرح منها **{m(bent_one)} قطع مثنية** عند الأطراف!",
                "Subtract the (strands - 1) curved fold-bend pieces from the total pieces (or add the 2 loose ends + middle straight strips).",
                [
                    f"Total pieces = {m(f'{strands} \\times {cuts} + 1 = {tot_one}')}.",
                    f"Each of the {m(bent_one)} U-bends stays in {m(1)} curved piece, leaving {m(f'{tot_one} - {bent_one} = {ans}')} completely straight pieces.",
                ],
                f"Direct check: {m(strands * (cuts - 1))} middle strips between the cuts + {m(2)} loose ends = **{m(ans)}**!",
                "نطرح عدد القطع ذات الثنيات المنحنية من العدد الكلي للقطع (أو نجمع القطع الوسطى مع الطرفين الحرين).",
                [
                    f"العدد الكلي للقطع = {m(f'{strands} \\times {cuts} + 1 = {tot_one}')}.",
                    f"عدد القطع ذات الثنية المنحنية = {m(bent_one)}، فيتبقى {m(f'{tot_one} - {bent_one} = {ans}')} قطع مستقيمة تماماً.",
                ],
                f"تحقق مباشر: {m(strands * (cuts - 1))} قطع بين القصّتين + طرفان حرّان = **{m(ans)}**!",
                diagram_en=svg_kang_folded_ribbon(strands, cuts),
            )
        else:
            ans = 2 * tot_one
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} folds a **red ribbon** into {m(strands)} layers just like the picture, AND folds a **blue ribbon** the exact same way ({m(strands)} layers), lays one on top of the other, and makes **{m(cuts)} straight cut(s)** (`✂`) through **both ribbons at once**. How many separate ribbon pieces are made altogether?",
                f"تطوي {nm_ar} **شريطاً أحمر** إلى {m(strands)} طبقات كما في الرسم، وتطوي **شريطاً أزرق** بالطريقة نفسها تماماً ({m(strands)} طبقات)، ثم تضعهما معاً وتقصهما **{m(cuts)} قصّة/قصّات مستقيمة** (`✂`) معاً. كم قطعة منفصلة تنتج من الشريطين إجمالاً؟",
                ans, [tot_one, 2 * strands * cuts + 1, ans - 1, ans + 2],
                f"Watch out: there are **two separate ribbons**! Find how many pieces **1 ribbon** makes ({m(tot_one)}), then double it!",
                f"انتبه: لدينا **شريطان منفصلان**! احسب عدد قطع **الشريط الواحد** ({m(tot_one)}) ثم ضاعف العدد!",
                "Compute (strands × cuts + 1) pieces for one ribbon, then multiply by 2 for the two separate ribbons.",
                [
                    f"The red ribbon alone breaks into {m(f'{strands} \\times {cuts} + 1 = {tot_one}')} pieces.",
                    f"The blue ribbon also breaks into {m(tot_one)} pieces, giving {m(f'{tot_one} + {tot_one} = {ans}')} pieces in all.",
                ],
                f"Trap check: don't add +1 only once — 2 separate starting ribbons + {m(2 * strands * cuts)} snips = {m(ans)} pieces!",
                "نحسب عدد القطع الناتجة من الشريط الواحد ثم نضاعفها لأن الشريطين منفصلان.",
                [
                    f"الشريط الأحمر وحده يعطي {m(f'{strands} \\times {cuts} + 1 = {tot_one}')} قطع.",
                    f"والشريط الأزرق يعطي {m(tot_one)} قطع أيضاً، فالمجموع {m(f'{tot_one} + {tot_one} = {ans}')} قطعة.",
                ],
                f"تحقق: شريطان منفصلان في البداية + {m(2 * strands * cuts)} موضع قطع = {m(ans)} قطعة!",
                diagram_en=svg_kang_folded_ribbon(strands, cuts),
            )

    # 16. kang_pre_opposite_die_dots (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_opposite_die_dots"
    die_easy = [
        (1, 2, 3, "top", "bottom face touching the table", "الوجه السفلي الملامس للطاولة", "Maya", "مايا"),
        (5, 3, 1, "top", "bottom face touching the table", "الوجه السفلي الملامس للطاولة", "Faris", "فارس"),
        (2, 4, 1, "front", f"hidden back face opposite the front-left {m(4)}-dot face", f"الوجه الخلفي المقابل لوجه الـ {m(4)} نقاط", "Layan", "ليان"),
        (6, 2, 4, "top", "bottom face hidden underneath", "الوجه السفلي المخفي بالأسفل", "Sami", "سامي"),
        (3, 1, 5, "right", f"hidden face opposite the {m(5)}-dot face", f"الوجه المخفي المقابل لوجه الـ {m(5)} نقاط", "Tala", "تالا"),
    ]
    for top_d, fr_d, rt_d, which, face_en, face_ar, nm_en, nm_ar in die_easy:
        assert len({top_d, fr_d, rt_d}) == 3 and (top_d + fr_d != 7) and (top_d + rt_d != 7) and (fr_d + rt_d != 7)
        shown_v = {"top": top_d, "front": fr_d, "right": rt_d}[which]
        ans = 7 - shown_v
        B.add_math(
            tp, "Easy", bp,
            f"On a standard game die, **opposite faces always add up to {m(7)}**. {nm_en}'s die shows {m(top_d)} dot(s) on top, {m(fr_d)} on the front-left, and {m(rt_d)} on the front-right. How many dots are on the **{face_en}**?",
            f"في حجر النرد القياسي **مجموع كل وجهين متقابلين يساوي دائماً {m(7)}**. يظهر على نرد {nm_ar} بالأعلى {m(top_d)}، وأمام اليسار {m(fr_d)}، وأمام اليمين {m(rt_d)}. كم نقطة على **{face_ar}**؟",
            ans, [shown_v, 7 - (fr_d if which == "top" else top_d), 7 - (rt_d if which != "right" else fr_d), (ans % 6) + 1],
            f"Subtract the matching visible face ({m(shown_v)}) from {m(7)}!",
            f"اطرح عدد نقاط الوجه المقابل الظاهر ({m(shown_v)}) من {m(7)}!",
            "Subtract the visible face's dot count from 7.",
            [
                f"Opposite faces on a standard die sum to {m(7)}.",
                f"Opposite {m(shown_v)} is {m(f'7 - {shown_v} = {ans}')} dot(s).",
            ],
            f"Check: {m(f'{shown_v} + {ans} = 7')}!",
            "نطرح عدد نقاط الوجه الظاهر المقابل من العدد 7.",
            [
                f"مجموع كل وجهين متقابلين يساوي {m(7)}.",
                f"الوجه المقابل لـ {m(shown_v)} يحمل {m(f'7 - {shown_v} = {ans}')}.",
            ],
            f"تحقق: {m(f'{shown_v} + {ans} = 7')}!",
            diagram_en=svg_pre_die_dots(top_d, fr_d, rt_d),
        )

    die_med = [
        (1, 2, 3, "all3", "Kangy", "الكنغر"),
        (6, 4, 2, "all3", "Lina", "لينا"),
        (5, 1, 3, "all3", "Omar", "عمر"),
        (2, 6, 3, "bot_and_opp_r", "Sara", "سارة"),
        (4, 5, 1, "bot_and_opp_r", "Tariq", "طارق"),
    ]
    for top_d, fr_d, rt_d, mmode, nm_en, nm_ar in die_med:
        assert len({top_d, fr_d, rt_d}) == 3 and (top_d + fr_d != 7) and (top_d + rt_d != 7) and (fr_d + rt_d != 7)
        if mmode == "all3":
            vis = top_d + fr_d + rt_d
            ans = 21 - vis
            assert ans == (7 - top_d) + (7 - fr_d) + (7 - rt_d)
            B.add_math(
                tp, "Medium", bp,
                f"On {nm_en}'s standard die (opposite faces sum to {m(7)}), the three visible faces show {m(top_d)}, {m(fr_d)}, and {m(rt_d)} dots. What is the **total number of dots on ALL THREE hidden faces** combined?",
                f"على نرد {nm_ar} القياسي (مجموع كل وجهين متقابلين {m(7)})، تظهر على الأوجه الثلاثة المرئية الأعداد {m(top_d)} و{m(fr_d)} و{m(rt_d)} من النقاط. ما **مجموع النقاط على الأوجه الثلاثة المخفية كلها معاً**؟",
                ans, [vis, ans - 2, ans + 2, 14 - top_d - fr_d],
                f"All {m(6)} faces of a die have {m('1+2+3+4+5+6 = 21')} dots in all — subtract the {m(vis)} visible dots (or add {m(7 - top_d)} + {m(7 - fr_d)} + {m(7 - rt_d)})!",
                f"جميع أوجه النرد الستة عليها {m(21)} نقطة إجمالاً — اطرح النقاط الظاهرة ({m(vis)}) أو اجمع متممات الـ {m(7)}!",
                "Subtract each visible face from 7 and add the three hidden faces (or subtract visible sum from 21).",
                [
                    f"Hidden faces opposite {m(top_d)}, {m(fr_d)}, {m(rt_d)} have {m(7 - top_d)}, {m(7 - fr_d)}, and {m(7 - rt_d)} dots.",
                    f"Their sum is {m(f'{7 - top_d} + {7 - fr_d} + {7 - rt_d} = {ans}')} dots.",
                ],
                f"21-dot shortcut check: {m(f'21 - ({top_d} + {fr_d} + {rt_d}) = 21 - {vis} = {ans}')}!",
                "نوجد نقاط كل وجه مخفي بطرح مقابله من 7 ثم نجمع الأوجه الثلاثة المخفية.",
                [
                    f"الأوجه المخفية المقابلة لـ {m(top_d)} و{m(fr_d)} و{m(rt_d)} تحمل {m(7 - top_d)} و{m(7 - fr_d)} و{m(7 - rt_d)} نقاط.",
                    f"مجموعها = {m(f'{7 - top_d} + {7 - fr_d} + {7 - rt_d} = {ans}')} نقطة.",
                ],
                f"تحقق سريع من مجموع النرد ({m(21)}): {m(f'21 - {vis} = {ans}')}!",
                diagram_en=svg_pre_die_dots(top_d, fr_d, rt_d),
            )
        else:
            b_face = 7 - top_d
            opp_r = 7 - rt_d
            ans = b_face + opp_r
            B.add_math(
                tp, "Medium", bp,
                f"Look at {nm_en}'s standard die (opposite faces add up to {m(7)}), showing {m(top_d)} on top, {m(fr_d)} on the front-left, and {m(rt_d)} on the front-right. What is the **sum** of the dots on the **bottom face** and the face **opposite the {m(rt_d)}-dot face**?",
                f"انظر إلى نرد {nm_ar} القياسي (مجموع المتقابلين {m(7)}) الذي يظهر عليه {m(top_d)} بالأعلى و{m(fr_d)} أمام اليسار و{m(rt_d)} أمام اليمين. ما **مجموع** نقاط **الوجه السفلي** والوجه **المقابل لوجه الـ {m(rt_d)} نقاط**؟",
                ans, [top_d + rt_d, (7 - top_d) + (7 - fr_d), ans + 1, max(2, ans - 2)],
                f"Bottom face = {m(f'7 - {top_d}')}, and opposite {m(rt_d)} = {m(f'7 - {rt_d}')} — add those two!",
                f"الوجه السفلي = {m(f'7 - {top_d}')}، والمقابل لـ {m(rt_d)} = {m(f'7 - {rt_d}')} — اجمعهما!",
                "Find each requested hidden face using 7 minus its opposite face, then add.",
                [
                    f"Bottom face (opposite top {m(top_d)}) = {m(f'7 - {top_d} = {b_face}')}.",
                    f"Face opposite {m(rt_d)} = {m(f'7 - {rt_d} = {opp_r}')}, so their sum is {m(f'{b_face} + {opp_r} = {ans}')}.",
                ],
                f"Check: {m(f'14 - ({top_d} + {rt_d}) = {ans}')}!",
                "نحسب الوجه السفلي والوجه المقابل لوجه اليمين من مكملات الـ 7 ثم نجمعهما.",
                [
                    f"الوجه السفلي = {m(f'7 - {top_d} = {b_face}')}، والمقابل لـ {m(rt_d)} = {m(f'7 - {rt_d} = {opp_r}')}.",
                    f"المجموع = {m(f'{b_face} + {opp_r} = {ans}')}.",
                ],
                f"تحقق: {m(f'{b_face} + {opp_r} = {ans}')}!",
                diagram_en=svg_pre_die_dots(top_d, fr_d, rt_d),
            )

    # Cross net: [(1,0,T), (0,1,L), (1,1,C), (2,1,R), (3,1,B), (1,2,D)] -> T<->D, L<->R, C<->B
    die_hard = [
        ("opp", ("2", "5", "1", "8", "9", "4"), "1", 9, "Nora", "نورة"),
        ("opp", ("3", "7", "4", "2", "6", "8"), "7", 2, "Zaid", "زيد"),
        ("opp", ("9", "1", "5", "6", "3", "4"), "9", 4, "Hala", "هلا"),
        ("sum10", ("3", "6", "2", "4", "?", "7"), "2", 8, "Yousef", "يوسف"),
        ("sum10", ("?", "1", "4", "9", "6", "2"), "2", 8, "Amal", "أمل"),
    ]
    for hmode, vals6, ref_lbl, expected_ans, nm_en, nm_ar in die_hard:
        T_v, L_v, C_v, R_v, B_v, D_v = vals6
        net_cells = [(1, 0, T_v), (0, 1, L_v), (1, 1, C_v), (2, 1, R_v), (3, 1, B_v), (1, 2, D_v)]
        opp_pairs = [(T_v, D_v), (L_v, R_v), (C_v, B_v)]
        if hmode == "opp":
            partner = next(y if x == ref_lbl else x for x, y in opp_pairs if ref_lbl in (x, y))
            ans = int(partner)
            assert ans == expected_ans
            other_nums = [int(v) for v in vals6 if v not in (ref_lbl, partner)]
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} cuts out this 6-square paper cross and folds it along the lines to make a closed cube. Which number ends up on the face **directly opposite** the face with **{m(ref_lbl)}**?",
                f"تقص {nm_ar} هذه الشبكة الورقية المكوّنة من 6 مربعات وتطويها على الخطوط لتصنع مكعباً مغلقاً. ما العدد الذي يصبح على الوجه **المقابل تماماً** للوجه الذي يحمل **{m(ref_lbl)}**؟",
                ans, other_nums[:4],
                f"Keep the middle square `{C_v}` flat on the table and fold its 4 neighbors straight up into walls — faces separated by **1 square in a straight line** become opposite!",
                f"ثبّت المربع الأوسط `{C_v}` على الطاولة واطوِ جيرانه الأربعة كجدران — المربعان اللذان يفصل بينهما **مربع واحد في خط مستقيم** يصبحان متقابلين!",
                "On a straight strip of squares in a cube net, two squares separated by one middle square fold to opposite faces.",
                [
                    f"Folding around `{C_v}` puts `{T_v}` opposite `{D_v}`, `{L_v}` opposite `{R_v}`, and `{C_v}` opposite `{B_v}`.",
                    f"Therefore, the face opposite {m(ref_lbl)} is **{m(ans)}**.",
                ],
                f"Opposite pairs check: ({T_v}, {D_v}), ({L_v}, {R_v}), ({C_v}, {B_v})!",
                "عند طي الشبكة، كل مربعين يفصل بينهما مربع واحد على استقامة واحدة يصبحان وجهين متقابلين.",
                [
                    f"بطي المربعات حول `{C_v}` يتقابل `{T_v}` مع `{D_v}`، ويتقابل `{L_v}` مع `{R_v}`، ويتقابل `{C_v}` مع `{B_v}`.",
                    f"إذن الوجه المقابل للعدد {m(ref_lbl)} يحمل العدد **{m(ans)}**.",
                ],
                f"تحقق من الأزواج المتقابلة: ({T_v}، {D_v}) و({L_v}، {R_v}) و({C_v}، {B_v})!",
                diagram_en=svg_cube_net(net_cells),
            )
        else:
            q_partner = next(y if x == "?" else x for x, y in opp_pairs if "?" in (x, y))
            assert q_partner == ref_lbl
            ans = 10 - int(q_partner)
            assert ans == expected_ans
            B.add_math(
                tp, "Hard", bp,
                f"When {nm_en} folds this 6-square net into a cube, **every pair of opposite faces adds up to {m(10)}**! What number belongs in the `{m('?')}` square?",
                f"عندما يطوي {nm_ar} هذه الشبكة ذات 6 مربعات لتكوين مكعب، يكون **مجموع كل وجهين متقابلين مساوياً لـ {m(10)}**! ما العدد الذي يجب وضعه في المربع `{m('?')}`؟",
                ans, [10 - int(C_v) if q_partner != C_v else 10 - int(T_v), 7 - int(q_partner) if int(q_partner) < 7 else ans + 1, ans - 2, ans + 2],
                f"First find which square folds **opposite** `{m('?')}` (skip 1 square in a straight line → {m(q_partner)}), then subtract from {m(10)}!",
                f"اعرف أولاً أي مربع يقابل `{m('?')}` بعد الطي (تخطَّ مربعاً واحداً على استقامة واحدة ← {m(q_partner)})، ثم اطرحه من {m(10)}!",
                "Identify the face opposite '?' on the net, then subtract that number from 10.",
                [
                    f"Folding the net places `{m('?')}` directly opposite the square showing {m(q_partner)}.",
                    f"Since opposite faces add up to {m(10)}, `{m('?')}` = {m(f'10 - {q_partner} = {ans}')}.",
                ],
                f"Check: every opposite pair ({L_v}+{R_v}, etc.) sums to {m(10)}, and {m(f'{q_partner} + {ans} = 10')}!",
                "نحدد الوجه المقابل للمربع `?` عند الطي ثم نطرح عدده من 10.",
                [
                    f"عند طي الشبكة يقابل المربع `{m('?')}` المربعَ الذي يحمل العدد {m(q_partner)}.",
                    f"وبما أن مجموع المتقابلين {m(10)} فإن `{m('?')}` = {m(f'10 - {q_partner} = {ans}')}.",
                ],
                f"تحقق: جميع الأزواج المتقابلة مجموعها {m(10)}، وفعلاً {m(f'{q_partner} + {ans} = 10')}!",
                diagram_en=svg_cube_net(net_cells),
            )


# ==============================================================================
# UNIT 5 — Combinatorics & Logic (60 Questions: KANG-PRE-241 .. KANG-PRE-300)
# Blueprints: kang_pre_queue_line_positions, kang_pre_coin_bill_totals,
#             kang_pre_outfit_icecream_pairs, kang_pre_magic_cross_five
# ==============================================================================
def _add_unit_1_5(B: BankBuilder) -> None:
    tp = "Combinatorics & Logic"

    # 17. kang_pre_queue_line_positions (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_queue_line_positions"
    q_easy = [
        (4, 3, "Joey", "جوي", "ice-cream cart", "عربة المثلجات"),
        (5, 6, "Mimi", "ميمي", "zoo gate", "بوابة الحديقة"),
        (7, 4, "Koko", "كوكو", "slide ladder", "سلم الزحليقة"),
        (6, 8, "Bibi", "بيبي", "puppet show", "مسرح العرائس"),
        (9, 5, "Toto", "توتو", "school bus", "حافلة المدرسة"),
    ]
    for pos_f, pos_b, nm_en, nm_ar, place_en, place_ar in q_easy:
        ans = pos_f + pos_b - 1
        B.add_math(
            tp, "Easy", bp,
            f"Children stand in one straight line at the {place_en}. {nm_en} (`★`) is **{m(pos_f)}th from the Front** and **{m(pos_b)}th from the Back**. How many children are standing in the line altogether?",
            f"يصطف الأطفال في طابور واحد عند {place_ar}. يقف {nm_ar} (`★`) في الترتيب **{m(pos_f)} من الأمام** وفي الترتيب **{m(pos_b)} من الخلف**. كم طفلاً يقف في الطابور إجمالاً؟",
            ans, [pos_f + pos_b, ans - 1, ans + 2, abs(pos_f - pos_b) + 1],
            f"Adding {m(f'{pos_f} + {pos_b}')} counts {nm_en} (`★`) **twice** — subtract {m(1)} so {nm_en} is counted once!",
            f"جمع {m(f'{pos_f} + {pos_b}')} يحسب {nm_ar} (`★`) **مرتين** — اطرح {m(1)} ليُحسب مرة واحدة!",
            "Add front rank and back rank, then subtract 1 because the starred child was counted in both.",
            [
                f"There are {m(pos_f - 1)} children ahead of {nm_en} and {m(pos_b - 1)} children behind {nm_en}.",
                f"Including {nm_en} (`+ 1`), total children = {m(f'{pos_f - 1} + 1 + {pos_b - 1} = {ans}')} (same as {m(f'{pos_f} + {pos_b} - 1 = {ans}')}).",
            ],
            f"Check: {m(pos_f - 1)} in front + {nm_en} + {m(pos_b - 1)} behind = **{m(ans)}**!",
            "نجمع الترتيب من الأمام والترتيب من الخلف ثم نطرح 1 لعدم تكرار عدّ صاحب النجمة.",
            [
                f"أمام {nm_ar} يوجد {m(pos_f - 1)} أطفال، وخلفه يوجد {m(pos_b - 1)} أطفال.",
                f"مع حساب {nm_ar} نفسه يصبح المجموع {m(f'{pos_f} + {pos_b} - 1 = {ans}')} طفلاً.",
            ],
            f"تحقق: {m(pos_f - 1)} أمامه + {m(1)} + {m(pos_b - 1)} خلفه = **{m(ans)}**!",
            diagram_en=svg_number_strip(["Front", "...", "★", "...", "Back"]),
        )

    q_med = [
        ("from_back", 15, 6, 0, "Jude", "جود"),
        ("from_back", 18, 7, 0, "Salman", "سلمان"),
        ("from_back", 20, 12, 0, "Rayan", "ريان"),
        ("turn_join", 7, 2, 3, "Dana", "دانة"),
        ("turn_join", 9, 3, 4, "Karam", "كرم"),
    ]
    for mmode, tot_n, a_val, k_join, nm_en, nm_ar in q_med:
        if mmode == "from_back":
            ans = tot_n - a_val + 1
            B.add_math(
                tp, "Medium", bp,
                f"Exact **{m(tot_n)} children** stand in a single line. {nm_en} (`★`) is **{m(a_val)}th from the Front**. What position is {nm_en} counting **from the Back**?",
                f"يقف **{m(tot_n)} طفلاً** بالضبط في طابور واحد. ترتيب {nm_ar} (`★`) هو **{m(a_val)} من الأمام**. ما ترتيب {nm_ar} عند العدّ **من الخلف**؟",
                ans, [tot_n - a_val, tot_n - a_val - 1, ans + 1, a_val + 1],
                f"There are {m(f'{tot_n} - {a_val} = {tot_n - a_val}')} children **behind** {nm_en}, so {nm_en} comes right after them from the back (`+ 1`)!",
                f"يوجد خلف {nm_ar} عدد {m(f'{tot_n} - {a_val} = {tot_n - a_val}')} أطفال، إذن ترتيبه من الخلف يزيد عليهم بـ {m(1)}!",
                "Count how many children stand behind the starred child (N - a), then add 1.",
                [
                    f"Out of {m(tot_n)} children, the first {m(a_val)} include {nm_en}, leaving {m(f'{tot_n} - {a_val} = {tot_n - a_val}')} children behind {nm_en}.",
                    f"Counting from the Back, {nm_en} is in position {m(f'{tot_n - a_val} + 1 = {ans}')}.",
                ],
                f"Formula check: {m(f'{a_val} + {ans} - 1 = {tot_n}')}!",
                "نحسب عدد الواقفين خلفه (العدد الكلي - ترتيبه من الأمام) ثم نضيف 1.",
                [
                    f"عدد الأطفال خلف {nm_ar} هو {m(f'{tot_n} - {a_val} = {tot_n - a_val}')}.",
                    f"وعند العدّ من الخلف يكون ترتيبه {m(f'{tot_n - a_val} + 1 = {ans}')}.",
                ],
                f"تحقق: {m(f'{a_val} + {ans} - 1 = {tot_n}')}!",
                diagram_en=svg_number_strip(["1st", "...", "★", "...", f"#{tot_n}"]),
            )
        else:
            # star_idx = a_val (0-based), so rank from front = a_val + 1
            rank_f = a_val + 1
            behind_orig = tot_n - rank_f
            ans = behind_orig + k_join + 1
            B.add_math(
                tp, "Medium", bp,
                f"At first, **{m(tot_n)} children** stand in line as shown, with {nm_en} (`★`) at **{m(rank_f)}th from the Front**. Next, **{m(k_join)} more children join at the Back**, and then **everybody turns around** so the old Back becomes the **new Front**! What is {nm_en}'s position from the **new Front**?",
                f"في البداية يقف **{m(tot_n)} أطفال** في الطابور كما في الرسم، وترتيب {nm_ar} (`★`) هو **{m(rank_f)} من الأمام**. بعد ذلك انضم **{m(k_join)} أطفال جدد في آخر الطابور**، ثم **استدار الجميع** فأصبح الخلف القديم هو **الأمام الجديد**! ما ترتيب {nm_ar} من **الأمام الجديد**؟",
                ans, [ans - 1, rank_f + k_join, tot_n + k_join - rank_f, ans + 1],
                f"Count everyone standing on the `Back` side of `★` ({m(behind_orig)} shown + {m(k_join)} new arrivals), then add {m(1)} for `★`!",
                f"احسب كل من يقف جهة الخلف من `★` ({m(behind_orig)} في الرسم + {m(k_join)} جدد)، ثم أضف {m(1)} لترتيب `★`!",
                "Count all children on the Back side of ★ after the newcomers join; turning around puts them all ahead of ★.",
                [
                    f"Initially {m(f'{tot_n} - {rank_f} = {behind_orig}')} children stand behind {nm_en}, and {m(k_join)} more join there, making {m(f'{behind_orig} + {k_join} = {behind_orig + k_join}')} children on that side.",
                    f"After turning around, all {m(behind_orig + k_join)} of them are in front of {nm_en}, so {nm_en} is **{m(ans)}th** from the new Front.",
                ],
                f"New total is {m(tot_n + k_join)}, and {nm_en} has {m(rank_f - 1)} behind now: {m(f'{ans} + {rank_f - 1} = {tot_n + k_join}')}!",
                "نحسب جميع الواقفين خلف `★` بعد انضمام الجدد، فعند الاستدارة يصبحون جميعاً أمامه.",
                [
                    f"خلف {nm_ar} في البداية {m(behind_orig)} أطفال، ومع انضمام {m(k_join)} يصبحون {m(behind_orig + k_join)} أطفال.",
                    f"بعد الاستدارة يصبح هؤلاء جميعاً أمامه، فيكون ترتيبه **{m(ans)}** من الأمام الجديد.",
                ],
                f"تحقق: العدد الجديد {m(tot_n + k_join)}، وترتيبه {m(ans)} من الأمام!",
                diagram_en=svg_pre_queue_line(shown_slots=tot_n, star_idx=a_val, front_lbl="Front", back_lbl="Back"),
            )

    q_hard = [
        (16, 4, 5, "Maya", "مايا", "Faris", "فارس"),
        (20, 6, 7, "Layan", "ليان", "Sami", "سامي"),
        (18, 5, 4, "Tala", "تالا", "Kangy", "الكنغر"),
        (15, 11, 9, "Lina", "لينا", "Omar", "عمر"),
        (14, 10, 8, "Sara", "سارة", "Tariq", "طارق"),
    ]
    for tot_n, rf_a, rb_b, a_en, a_ar, b_en, b_ar in q_hard:
        pos_a = rf_a
        pos_b = tot_n - rb_b + 1
        assert pos_a != pos_b
        ans = abs(pos_a - pos_b) - 1
        assert ans >= 1
        line_Arr = list(range(1, tot_n + 1))
        lo_p, hi_p = min(pos_a, pos_b), max(pos_a, pos_b)
        assert len([p for p in line_Arr if lo_p < p < hi_p]) == ans
        B.add_math(
            tp, "Hard", bp,
            f"In a straight line of **{m(tot_n)} children**, {a_en} is **{m(rf_a)}th from the Front** and {b_en} is **{m(rb_b)}th from the Back**. How many children are standing **strictly between** {a_en} and {b_en}?",
            f"في طابور مستقيم يضم **{m(tot_n)} طفلاً**، تقف {a_ar} في الترتيب **{m(rf_a)} من الأمام** ويقف {b_ar} في الترتيب **{m(rb_b)} من الخلف**. كم طفلاً يقف **بينهما تماماً**؟",
            ans, [ans + 1, ans + 2, max(0, ans - 1), abs(rf_a - rb_b)],
            f"Find {b_en}'s spot counting from the **Front** ({m(f'{tot_n} - {rb_b} + 1 = {pos_b}')}), then count spots strictly between #{m(lo_p)} and #{m(hi_p)}!",
            f"حدد موقع {b_ar} بالعدّ من **الأمام** ({m(f'{tot_n} - {rb_b} + 1 = {pos_b}')})، ثم احسب كم طفلاً يقع بين #{m(lo_p)} و#{m(hi_p)}!",
            "Convert both positions to numbers from the Front (1 to N), then compute |pos_A - pos_B| - 1.",
            [
                f"Counting from the Front (`1` to `{tot_n}`), {a_en} is at spot #{m(pos_a)} and {b_en} is at spot #{m(f'{tot_n} - {rb_b} + 1 = {pos_b}')}.",
                f"Children strictly between spot #{m(lo_p)} and spot #{m(hi_p)}: {m(f'{hi_p} - {lo_p} - 1 = {ans}')}.",
            ],
            f"Spots between #{m(lo_p)} and #{m(hi_p)} are {', '.join('#' + str(k) for k in range(lo_p + 1, hi_p))} → **{m(ans)}** children!",
            "نحوّل موقعي الصديقين إلى الترتيب من الأمام ثم نطرح الصغير من الكبير وننقص 1.",
            [
                f"من الأمام تقف {a_ar} في الموقع #{m(pos_a)}، ويقف {b_ar} في الموقع #{m(f'{tot_n} - {rb_b} + 1 = {pos_b}')}.",
                f"عدد الواقفين بين #{m(lo_p)} و#{m(hi_p)} يساوي {m(f'{hi_p} - {lo_p} - 1 = {ans}')}.",
            ],
            f"المواقع المحصورة بينهما عددها **{m(ans)}** بالضبط!",
            diagram_en=svg_number_strip(["Front", "...", "?", "...", "Back"]),
        )

    # 18. kang_pre_coin_bill_totals (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_coin_bill_totals"
    coin_easy = [
        (["10", "5", "2", "1"], "Nora", "نورة"),
        (["10", "5", "5", "2", "1"], "Zaid", "زيد"),
        (["10", "10", "2", "2", "1"], "Hala", "هلا"),
        (["5", "5", "2", "2", "2"], "Yousef", "يوسف"),
        (["10", "10", "5", "2", "2", "1"], "Amal", "أمل"),
    ]
    for coins, nm_en, nm_ar in coin_easy:
        ans = sum(int(c) for c in coins)
        c_list_str = ", ".join(m(c) for c in coins)
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} opens a coin purse and sees these **{m(len(coins))} riyal coins**: {c_list_str}. How many riyals does {nm_en} have in total (`Sum: ?`)?",
            f"يفتح {nm_ar} محفظة النقود فيجد هذه **العملات الـ {m(len(coins))} بالريال**: {c_list_str}. كم ريالاً مع {nm_ar} في المجموع (`Sum: ?`)؟",
            ans, [len(coins), ans - 1, ans + 2, ans + 5],
            "Add the biggest coins (`10`s and `5`s) first, then count on the `2`s and `1`s!",
            "اجمع العملات الكبيرة (`10` و`5`) أولاً، ثم أضف عملات `2` و`1`!",
            "Add the values of all coins starting from the largest denominations.",
            [
                f"Adding the coins in order: {' + '.join(coins)} = **{m(ans)}** riyals.",
            ],
            f"Re-adding from smallest to largest also gives {m(ans)} riyals!",
            "نجمع قيم جميع العملات النقدية بدءاً من الفئات الأكبر.",
            [
                f"مجموع العملات = {' + '.join(coins)} = **{m(ans)}** ريالاً.",
            ],
            f"تحقق بالجمع العكسي: المجموع {m(ans)} ريالاً!",
            diagram_en=svg_pre_coin_purse(coins, tag_lbl="Sum: ?"),
        )

    coin_med = [
        (["10", "10", "5", "2"], 19, "change", "sticker album", "دفتر ملصقات", "Joey", "جوي"),
        (["10", "5", "5", "2", "2"], 17, "change", "paint set", "علبة ألوان", "Mimi", "ميمي"),
        (["10", "10", "5", "5", "1"], 23, "change", "puzzle box", "صندوق أحجية", "Koko", "كوكو"),
        (["10", "5", "2", "1"], 25, "need", "soccer ball", "كرة قدم", "Bibi", "بيبي"),
        (["10", "10", "2", "2"], 33, "need", "toy train", "قطار لعبة", "Toto", "توتو"),
    ]
    for coins, price, mmode, toy_en, toy_ar, nm_en, nm_ar in coin_med:
        have = sum(int(c) for c in coins)
        c_list_str = ", ".join(m(c) for c in coins)
        if mmode == "change":
            ans = have - price
            assert ans > 0
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en}'s purse holds coins worth {c_list_str} riyals. {nm_en} buys a {toy_en} that costs **{m(price)} riyals**. How many riyals does {nm_en} have **left over**?",
                f"تحوي محفظة {nm_ar} عملات بقيم {c_list_str} ريالات. اشترى {toy_ar} بسعر **{m(price)} ريالاً**. كم ريالاً **تبقى** معه؟",
                ans, [have, ans + 2, max(1, ans - 1), ans + 5],
                f"First add all coins in the purse ({m(have)} riyals), then subtract {m(price)}!",
                f"اجمع أولاً نقود المحفظة ({m(have)} ريالاً)، ثم اطرح السعر {m(price)}!",
                "Sum the coin values in the purse, then subtract the item's price.",
                [
                    f"Purse total = {' + '.join(coins)} = {m(have)} riyals.",
                    f"Money left after paying {m(price)} riyals = {m(f'{have} - {price} = {ans}')} riyals.",
                ],
                f"Check: {m(f'{price} + {ans} = {have}')} riyals!",
                "نجمع قيمة العملات في المحفظة أولاً ثم نطرح سعر اللعبة.",
                [
                    f"مجموع ما في المحفظة = {' + '.join(coins)} = {m(have)} ريالاً.",
                    f"المتبقي بعد الشراء = {m(f'{have} - {price} = {ans}')} ريالات.",
                ],
                f"تحقق: {m(f'{price} + {ans} = {have}')} ريالاً!",
                diagram_en=svg_pre_coin_purse(coins, tag_lbl=f"Cost: {price}"),
            )
        else:
            ans = price - have
            assert ans > 0
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en} has these coins in a purse: {c_list_str} riyals, and wants to buy a {toy_en} priced at **{m(price)} riyals**. How many **more riyals** does {nm_en} still need to save?",
                f"لدى {nm_ar} في المحفظة العملات {c_list_str} ريالات، ويريد شراء {toy_ar} بسعر **{m(price)} ريالاً**. كم **ريالاً إضافياً** يحتاج أن يدّخر؟",
                ans, [have, ans + 2, max(1, ans - 2), price - len(coins)],
                f"Add the coins ({m(have)} riyals) and find how far {m(have)} is from {m(price)}!",
                f"اجمع العملات ({m(have)} ريالاً) واحسب الفرق للوصول إلى {m(price)}!",
                "Subtract the current purse total from the goal price.",
                [
                    f"Current savings = {' + '.join(coins)} = {m(have)} riyals.",
                    f"Extra riyals needed = {m(f'{price} - {have} = {ans}')} riyals.",
                ],
                f"Check: {m(f'{have} + {ans} = {price}')} riyals!",
                "نطرح مجموع النقود الحالية من السعر المطلوب.",
                [
                    f"المبلغ الحالي = {' + '.join(coins)} = {m(have)} ريالاً.",
                    f"المبلغ المتبقي لإتمام السعر = {m(f'{price} - {have} = {ans}')} ريالات.",
                ],
                f"تحقق: {m(f'{have} + {ans} = {price}')} ريالاً!",
                diagram_en=svg_pre_coin_purse(coins, tag_lbl=f"Goal: {price}"),
            )

    coin_hard = [
        (16, "Jude", "جود"),
        (18, "Salman", "سلمان"),
        (34, "Rayan", "ريان"),
        (39, "Dana", "دانة"),
        (48, "Karam", "كرم"),
    ]
    for target_p, nm_en, nm_ar in coin_hard:
        # Exact DP for minimum coins from {1, 2, 5, 10}
        dp = [0] + [999] * target_p
        for v in range(1, target_p + 1):
            for c_val in (1, 2, 5, 10):
                if v >= c_val:
                    dp[v] = min(dp[v], dp[v - c_val] + 1)
        ans = dp[target_p]
        rem = target_p
        used_coins = []
        for c_val in (10, 5, 2, 1):
            while rem >= c_val:
                used_coins.append(c_val)
                rem -= c_val
        assert len(used_coins) == ans and sum(used_coins) == target_p
        B.add_math(
            tp, "Hard", bp,
            f"A toy shop accepts coins of **{m(1)}, {m(2)}, {m(5)}, and {m(10)} riyals** (plenty of each type). What is the **smallest number of coins** {nm_en} can hand over to pay **exact {m(target_p)} riyals** (with no change back)?",
            f"يقبل متجر الألعاب عملات من فئات **{m(1)} و{m(2)} و{m(5)} و{m(10)} ريالات** (يتوفر الكثير من كل فئة). ما **أقل عدد من العملات** يمكن أن يدفعه {nm_ar} لسداد مبلغ **{m(target_p)} ريالاً بالضبط** (دون باقٍ)؟",
            ans, [ans + 1, ans + 2, max(1, ans - 1), target_p // 5 + (target_p % 5)],
            f"Use as many **{m(10)}-riyal** coins as fit first, then **{m(5)}**, then **{m(2)}**, then **{m(1)}**!",
            f"استعمل أكبر عدد ممكن من عملة **{m(10)} ريالات** أولاً، ثم **{m(5)}**، ثم **{m(2)}**، ثم **{m(1)}**!",
            "Pack the largest coin values (10, then 5, then 2, then 1) to use the fewest coins.",
            [
                f"To minimize coins for {m(target_p)} riyals, pick largest coins first: {' + '.join(str(x) for x in used_coins)} = {m(target_p)}.",
                f"Counting those coins gives **{m(ans)}** coins.",
            ],
            f"Coin count check: {', '.join(str(x) for x in used_coins)} uses exact **{m(ans)}** coins!",
            "نختار أكبر فئة ممكنة في كل خطوة (10 ثم 5 ثم 2 ثم 1) لتقليل عدد العملات.",
            [
                f"نمثل المبلغ {m(target_p)} بأكبر الفئات: {' + '.join(str(x) for x in used_coins)} = {m(target_p)}.",
                f"عدد هذه العملات هو **{m(ans)}** عملات.",
            ],
            f"تحقق: لا يمكن تكوين {m(target_p)} بعدد أقل من **{m(ans)}** عملات!",
            diagram_en=svg_pre_coin_purse(["1", "2", "5", "10"], tag_lbl=f"Pay: {target_p}"),
        )

    # 19. kang_pre_outfit_icecream_pairs (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_outfit_icecream_pairs"
    pair_easy = [
        (3, 4, "hats", "shirts", "Hat", "Shirt", "قبعات", "قمصان", "Maya", "مايا"),
        (2, 5, "cones", "ice-cream flavors", "Cone", "Scoop", "بسكويتات", "نكهات مثلجات", "Faris", "فارس"),
        (4, 4, "scarves", "coats", "Scarf", "Coat", "أوشحة", "معاطف", "Layan", "ليان"),
        (3, 5, "cups", "juices", "Cup", "Juice", "أكواب", "عصائر", "Sami", "سامي"),
        (4, 2, "bows", "bags", "Bow", "Bag", "شرائط", "حقائب", "Tala", "تالا"),
    ]
    for a, b, it1_en, it2_en, sl1, sl2, it1_ar, it2_ar, nm_en, nm_ar in pair_easy:
        ans = a * b
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en} has **{m(a)} different {it1_en}** and **{m(b)} different {it2_en}**. Choosing **1 of each**, how many different pairs can {nm_en} make?",
            f"لدى {nm_ar} عدد **{m(a)} من {it1_ar} المختلفة** و**{m(b)} من {it2_ar} المختلفة**. عند اختيار **واحدة من كل نوع**، كم زوجاً مختلفاً يمكن تكوينه؟",
            ans, [a + b, ans + 2, max(2, ans - 2), a + b + 1],
            f"Each of the {m(a)} {it1_en} can match with all {m(b)} {it2_en}: add {m(b)} to itself {m(a)} times!",
            f"كل اختيار من الـ {m(a)} يقترن مع جميع الـ {m(b)} الأخرى: اجمع {m(b)} لنفسها {m(a)} مرات!",
            "Pair each choice from the first group with every choice from the second group.",
            [
                f"Each of the {m(a)} {it1_en} pairs with {m(b)} {it2_en}.",
                f"Total pairs = {m(' + '.join([str(b)] * a) + f' = {ans}')}.",
            ],
            f"Check: {m(f'{a} \\times {b} = {ans}')} combinations!",
            "نربط كل خيار من المجموعة الأولى بجميع خيارات المجموعة الثانية.",
            [
                f"كل خيار من الـ {m(a)} له {m(b)} خيارات مقابلة.",
                f"إجمالي الأزواج = {m(' + '.join([str(b)] * a) + f' = {ans}')}.",
            ],
            f"تحقق: {m(f'{a} \\times {b} = {ans}')} أزواج مختلفة!",
            diagram_en=svg_digit_slots([sl1, sl2], top_note="Pairs: ?"),
        )

    pair_med = [
        ("two_flavors", 4, 0, 0, "Kangy", "الكنغر"),
        ("two_flavors", 5, 0, 0, "Lina", "لينا"),
        ("two_flavors", 6, 0, 0, "Omar", "عمر"),
        ("three_parts", 2, 3, 2, "Sara", "سارة"),
        ("three_parts", 2, 2, 4, "Tariq", "طارق"),
    ]
    for mmode, x, y, z, nm_en, nm_ar in pair_med:
        if mmode == "two_flavors":
            ans = x * (x - 1) // 2
            terms = " + ".join(str(k) for k in range(x - 1, 0, -1))
            B.add_math(
                tp, "Medium", bp,
                f"An ice-cream shop has **{m(x)} different flavors**. {nm_en} orders a bowl with **2 scoops of DIFFERENT flavors** (the order in the bowl does not matter). How many different 2-flavor bowls can {nm_en} choose?",
                f"يقدم محل مثلجات **{m(x)} نكهات مختلفة**. يطلب {nm_ar} كوباً فيه **كرتان من نكهتين مختلفتين** (الترتيب داخل الكوب لا يهم). بكم طريقة مختلفة يمكن اختيار النكهتين؟",
                ans, [x * (x - 1), x * 2, ans + 1, max(1, ans - 1)],
                f"Pair Flavor 1 with the other {m(x - 1)} flavors, then Flavor 2 with the remaining {m(x - 2)} new ones ({m(terms)})!",
                f"اربط النكهة 1 مع الـ {m(x - 1)} الباقية، ثم النكهة 2 مع الـ {m(x - 2)} التالية دون تكرار ({m(terms)})!",
                "List pairs systematically without repeating reversed pairs.",
                [
                    f"Flavor 1 makes {m(x - 1)} pairs; Flavor 2 makes {m(x - 2)} new pairs; continuing down to {m(1)} gives {m(f'{terms} = {ans}')}.",
                ],
                f"No pair is counted twice: total = **{m(ans)}** bowls!",
                "نعدّ الأزواج بالترتيب دون تكرار الزوج نفسه معكوساً.",
                [
                    f"النكهة الأولى تكوّن {m(x - 1)} أزواج، والثانية {m(x - 2)} أزواج جديدة... فالمجموع {m(f'{terms} = {ans}')}.",
                ],
                f"تحقق: عدد الأكواب المختلفة هو **{m(ans)}**!",
                diagram_en=svg_digit_slots(["Flv A", "Flv B"], top_note=f"{x} Kinds"),
            )
        else:
            ans = x * y * z
            B.add_math(
                tp, "Medium", bp,
                f"For school lunch, {nm_en} picks **1 sandwich** (from {m(x)} kinds), **1 fruit** (from {m(y)} kinds), and **1 drink** (from {m(z)} kinds). How many different 3-item lunches can {nm_en} pack?",
                f"لوجبة المدرسة يختار {nm_ar} **شطيرة واحدة** (من {m(x)} أنواع)، و**فاكهة واحدة** (من {m(y)} أنواع)، و**مشروباً واحداً** (من {m(z)} أنواع). كم وجبة ثلاثية مختلفة يمكن تجهيزها؟",
                ans, [x + y + z, x * y + z, ans - 2, ans + 2],
                f"First pair sandwiches and fruits ({m(f'{x} \\times {y} = {x * y}')}), then pair each with the {m(z)} drinks!",
                f"اربط أولاً الشطائر بالفواكه ({m(f'{x} \\times {y} = {x * y}')})، ثم اربط كل خيار بالمشروبات الـ {m(z)}!",
                "Multiply the choices for sandwich, fruit, and drink step-by-step.",
                [
                    f"Sandwich and fruit pairs = {m(f'{x} \\times {y} = {x * y}')}.",
                    f"With {m(z)} drink choices for each, total lunches = {m(f'{x * y} \\times {z} = {ans}')}.",
                ],
                f"Check: {m(f'{x} \\times {y} \\times {z} = {ans}')} lunches!",
                "نحسب خيارات الصنفين الأولين ثم نضرب في خيارات الصنف الثالث.",
                [
                    f"أزواج الشطيرة والفاكهة = {m(f'{x} \\times {y} = {x * y}')}.",
                    f"ومع {m(z)} مشروبات يصبح المجموع {m(f'{x * y} \\times {z} = {ans}')} وجبة.",
                ],
                f"تحقق: {m(f'{x} \\times {y} \\times {z} = {ans}')}!",
                diagram_en=svg_digit_slots(["Sand", "Fruit", "Drink"], top_note="Lunch: ?"),
            )

    pair_hard = [
        (3, 4, 1, "the red shirt cannot be worn with the red pants (1 clashing pair)", "لا يرتدي القميص الأحمر مع البنطال الأحمر (زوج واحد غير مسموح)", "Nora", "نورة"),
        (4, 3, 2, "2 of the cap-and-jacket pairs have clashing stripes and are not allowed", "زوجان من أزواج القبعة والسترة غير مسموحين لتعارض الخطوط", "Zaid", "زيد"),
        (4, 4, 3, "the 3 sparkly tops cannot be worn with the 1 muddy pair of boots (3 pairs not allowed)", "القمصان اللامعة الـ 3 لا تُلبس مع الحذاء الطيني الواحد (3 أزواج غير مسموحة)", "Hala", "هلا"),
        (5, 3, 2, "2 of the combinations are out of stock today", "مزيجان اثنان غير متوفرين اليوم", "Yousef", "يوسف"),
        (4, 5, 4, "the 4 sour toppings are never put on the 1 mint cone (4 pairs not allowed)", "الإضافات الحامضة الـ 4 لا توضع مع بسكويت النعناع الواحد (4 أزواج غير مسموحة)", "Amal", "أمل"),
    ]
    for a, b, bad, rule_en, rule_ar, nm_en, nm_ar in pair_hard:
        all_p = a * b
        ans = all_p - bad
        B.add_math(
            tp, "Hard", bp,
            f"{nm_en} chooses **1 item from Group A ({m(a)} choices)** and **1 item from Group B ({m(b)} choices)**, EXCEPT {rule_en}. How many **allowed** pairs can {nm_en} make?",
            f"يختار {nm_ar} **عنصراً من المجموعة A ({m(a)} خيارات)** و**عنصراً من المجموعة B ({m(b)} خيارات)**، ولكن {rule_ar}. كم زوجاً **مسموحاً** يمكن تكوينه؟",
            ans, [all_p, (a - 1) * (b - 1) if (a - 1) * (b - 1) != ans else ans - 2, ans + 1, ans - 1],
            f"Count **all** pairs first ({m(f'{a} \\times {b} = {all_p}')}), then cross out the {m(bad)} forbidden pair(s)!",
            f"احسب **جميع** الأزواج أولاً ({m(f'{a} \\times {b} = {all_p}')})، ثم اطرح الأزواج غير المسموحة ({m(bad)})!",
            "Find all possible A × B pairs, then subtract the forbidden combinations.",
            [
                f"Without the restriction, there are {m(f'{a} \\times {b} = {all_p}')} total pairs.",
                f"Removing the {m(bad)} forbidden pair(s) leaves {m(f'{all_p} - {bad} = {ans}')} allowed pairs.",
            ],
            f"Check: {m(ans)} allowed + {m(bad)} forbidden = {m(all_p)} total pairs!",
            "نحسب جميع الأزواج الممكنة أولاً ثم نطرح الأزواج المستثناة.",
            [
                f"إجمالي الأزواج من دون شرط = {m(f'{a} \\times {b} = {all_p}')}.",
                f"نطرح الأزواج غير المسموحة ({m(bad)}): {m(f'{all_p} - {bad} = {ans}')} زوجاً مسموحاً.",
            ],
            f"تحقق: {m(f'{ans} + {bad} = {all_p}')}!",
            diagram_en=svg_digit_slots([f"A ({a})", f"B ({b})"], top_note="Allowed?"),
        )

    # 20. kang_pre_magic_cross_five (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_magic_cross_five"
    cross_easy = [
        (4, 3, 6, 2, "Joey", "جوي"),
        (5, 2, 7, 4, "Mimi", "ميمي"),
        (8, 5, 3, 6, "Koko", "كوكو"),
        (7, 4, 6, 9, "Bibi", "بيبي"),
        (9, 6, 5, 8, "Toto", "توتو"),
    ]
    for top_v, ctr_v, bot_v, left_v, nm_en, nm_ar in cross_easy:
        col_sum = top_v + ctr_v + bot_v
        ans = col_sum - left_v - ctr_v
        assert ans == top_v + bot_v - left_v and ans > 0
        B.add_math(
            tp, "Easy", bp,
            f"In {nm_en}'s 5-box number cross, the **3 vertical boxes** add up to the **exact same total** as the **3 horizontal boxes**. What number belongs in the `{m('?')}` box on the right?",
            f"في لغز التقاطع العددي لدى {nm_ar}، مجموع **الخانات الثلاث الرأسية** يساوي **تماماً** مجموع **الخانات الثلاث الأفقية**. ما العدد الذي يوضع في خانة `{m('?')}` اليمنى؟",
            ans, [col_sum, ans + 1, max(1, ans - 1), ans + ctr_v],
            f"Add the vertical column ({m(f'{top_v} + {ctr_v} + {bot_v} = {col_sum}')}) to find the target sum!",
            f"اجمع العمود الرأسي الكامل ({m(f'{top_v} + {ctr_v} + {bot_v} = {col_sum}')}) لتعرف المجموع المطلوب!",
            "Sum the complete vertical column, then find the missing right box so the horizontal row matches.",
            [
                f"Vertical sum = {m(f'{top_v} + {ctr_v} + {bot_v} = {col_sum}')}.",
                f"Horizontal row needs {m(f'{left_v} + {ctr_v} + ? = {col_sum}')}, so `{m('?')}` = {m(f'{col_sum} - {left_v + ctr_v} = {ans}')}.",
            ],
            f"Shortcut check: center {m(ctr_v)} is shared, so {m(f'{left_v} + {ans} = {top_v} + {bot_v} = {top_v + bot_v}')}!",
            "نجمع العمود الرأسي المكتمل ثم نكمل الصف الأفقي ليصل إلى المجموع نفسه.",
            [
                f"مجموع العمود الرأسي = {m(f'{top_v} + {ctr_v} + {bot_v} = {col_sum}')}.",
                f"في الصف الأفقي: {m(f'{left_v} + {ctr_v} + ? = {col_sum}')}، إذن `{m('?')}` = {m(f'{col_sum} - {left_v + ctr_v} = {ans}')}.",
            ],
            f"تحقق سريع: {m(f'{left_v} + {ans} = {top_v} + {bot_v} = {top_v + bot_v}')}!",
            diagram_en=svg_kang_magic_cross(str(ctr_v), str(top_v), "?", str(bot_v), str(left_v)),
        )

    cross_med = [
        (15, 4, 6, 3, "Jude", "جود"),
        (18, 7, 5, 8, "Salman", "سلمان"),
        (16, 5, 4, 9, "Rayan", "ريان"),
        (20, 6, 8, 5, "Dana", "دانة"),
        (17, 3, 7, 4, "Karam", "كرم"),
    ]
    for line_s, top_v, left_v, right_v, nm_en, nm_ar in cross_med:
        ctr_v = line_s - left_v - right_v
        ans = line_s - top_v - ctr_v
        assert ctr_v > 0 and ans > 0
        B.add_math(
            tp, "Medium", bp,
            f"In {nm_en}'s magic cross, **both** the 3-box horizontal row AND the 3-box vertical column must add up to **{m(line_s)}** (`Sum={line_s}`). The center box is blank, the top is {m(top_v)}, the left is {m(left_v)}, and the right is {m(right_v)}. What number goes in the bottom box `{m('?')}`?",
            f"في التقاطع السحري لدى {nm_ar}، يجب أن يكون مجموع الصف الأفقي ومجموع العمود الرأسي مساوياً لـ **{m(line_s)}** (`Sum={line_s}`). الخانة الوسطى فارغة، والعليا {m(top_v)}، واليسرى {m(left_v)}، واليمنى {m(right_v)}. ما العدد في الخانة السفلية `{m('?')}`؟",
            ans, [ctr_v, line_s - top_v, ans + 2, max(1, ans - 2)],
            f"First find the blank **center** box from the horizontal row ({m(f'{line_s} - {left_v} - {right_v} = {ctr_v}')}), then finish the vertical column!",
            f"أوجد أولاً قيمة **الوسط** الفارغ من الصف الأفقي ({m(f'{line_s} - {left_v} - {right_v} = {ctr_v}')})، ثم أكمل العمود الرأسي!",
            "Use the horizontal row to find the hidden center number first, then use the vertical column to find '?'.",
            [
                f"Horizontal row sum is {m(line_s)}, so the blank center box = {m(f'{line_s} - {left_v} - {right_v} = {ctr_v}')}.",
                f"Vertical column sum is also {m(line_s)}, so bottom `{m('?')}` = {m(f'{line_s} - {top_v} - {ctr_v} = {ans}')}.",
            ],
            f"Check: outer pairs match too — {m(f'{top_v} + {ans} = {left_v} + {right_v} = {left_v + right_v}')}!",
            "نحسب خانة الوسط الفارغة من الصف الأفقي أولاً ثم نستنتج الخانة السفلية من العمود الرأسي.",
            [
                f"من الصف الأفقي: خانة الوسط = {m(f'{line_s} - {left_v} - {right_v} = {ctr_v}')}.",
                f"من العمود الرأسي: الخانة السفلية `{m('?')}` = {m(f'{line_s} - {top_v} - {ctr_v} = {ans}')}.",
            ],
            f"تحقق: {m(f'{top_v} + {ctr_v} + {ans} = {line_s}')}!",
            diagram_en=svg_kang_magic_cross("", str(top_v), str(right_v), "?", str(left_v), note=f"Sum={line_s}"),
        )

    cross_hard = [
        ("unique_ctr", (2, 4, 5, 8, 10), "Maya", "مايا"),
        ("unique_ctr", (1, 4, 6, 8, 10), "Faris", "فارس"),
        ("unique_ctr", (2, 6, 7, 8, 12), "Layan", "ليان"),
        ("max_sum", (1, 2, 3, 4, 5), "Sami", "سامي"),
        ("max_sum", (3, 4, 5, 6, 7), "Tala", "تالا"),
    ]
    for hmode, nums5, nm_en, nm_ar in cross_hard:
        # Programmatically inspect all valid centers and line sums
        valid_centers = []
        valid_line_sums = []
        for idx_c, c_cand in enumerate(nums5):
            rem4 = [nums5[j] for j in range(5) if j != idx_c]
            # Check if rem4 splits into two pairs of equal sum: a+b == c+d
            if rem4[0] + rem4[3] == rem4[1] + rem4[2] or rem4[0] + rem4[2] == rem4[1] + rem4[3] or rem4[0] + rem4[1] == rem4[2] + rem4[3]:
                valid_centers.append(c_cand)
                valid_line_sums.append(c_cand + sum(rem4) // 2)
        nums_str = ", ".join(m(v) for v in nums5)
        if hmode == "unique_ctr":
            assert len(valid_centers) == 1
            ans = valid_centers[0]
            rem4 = sorted(v for v in nums5 if v != ans)
            other_opts = [v for v in nums5 if v != ans]
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} places the five numbers {nums_str} into the 5 boxes of this cross (one in each box) so the **3 vertical boxes** and **3 horizontal boxes** have the **same sum**. Which number **MUST** go in the yellow center box?",
                f"يضع {nm_ar} الأعداد الخمسة {nums_str} داخل خانات التقاطع الخمس (عدد في كل خانة) بحيث يتساوى **مجموع الخانات الثلاث الرأسية** مع **مجموع الخانات الثلاث الأفقية**. أي عدد **يجب** أن يوضع في خانة الوسط الصفراء؟",
                ans, other_opts,
                f"After picking the center number, the **other 4 numbers** must split into **two pairs with the exact same sum**!",
                f"بعد وضع عدد الوسط، يجب أن تنقسم **الأعداد الأربعة الباقية** إلى **زوجين لهما المجموع نفسه تماماً**!",
                "The four outer arms must form two equal-sum pairs (top + bottom = left + right).",
                [
                    f"Put {m(ans)} in the center: the remaining four numbers are {m(rem4[0])}, {m(rem4[1])}, {m(rem4[2])}, {m(rem4[3])}, which pair cleanly as {m(f'{rem4[0]} + {rem4[3]} = {rem4[1]} + {rem4[2]} = {rem4[0] + rem4[3]}')}.",
                    f"Any other choice leaves an odd sum for the 4 outer boxes, which can never split into two equal whole-number pairs!",
                ],
                f"Both lines then sum to {m(f'{ans} + {rem4[0] + rem4[3]} = {ans + rem4[0] + rem4[3]}')}!",
                "يجب أن تنقسم الأعداد الأربعة على الأطراف إلى زوجين متساويي المجموع.",
                [
                    f"عند وضع {m(ans)} في الوسط يتبقى {m(rem4[0])} و{m(rem4[1])} و{m(rem4[2])} و{m(rem4[3])}، وهي تنقسم إلى {m(f'{rem4[0]} + {rem4[3]} = {rem4[1]} + {rem4[2]} = {rem4[0] + rem4[3]}')}.",
                    f"أي اختيار آخر يجعل مجموع الأربعة الباقية فردياً فلا ينقسم إلى زوجين متساويين!",
                ],
                f"تحقق: مجموع كل خط يصبح {m(ans + rem4[0] + rem4[3])}!",
                diagram_en=svg_kang_magic_cross("?", "?", "?", "?", "?"),
            )
        else:
            ans = max(valid_line_sums)
            best_c = max(valid_centers)
            rem4 = sorted(v for v in nums5 if v != best_c)
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} places the five numbers {nums_str} into the 5 boxes of this cross (one per box) so the 3-box vertical sum equals the 3-box horizontal sum. What is the **LARGEST possible sum** of one 3-box line?",
                f"تضع {nm_ar} الأعداد الخمسة {nums_str} في خانات التقاطع الخمس (عدد في كل خانة) بحيث يتساوى مجموع العمود الرأسي مع مجموع الصف الأفقي. ما **أكبر مجموع ممكن** للخط الواحد المكوّن من 3 خانات؟",
                ans, [min(valid_line_sums), valid_line_sums[1], ans + 1, ans - 1],
                f"Because the **center** number gets counted in **both** lines, put the **biggest** number ({m(best_c)}) in the center!",
                f"لأن عدد **الوسط** يدخل في حساب **الخطين معاً**، ضع **أكبر** عدد ({m(best_c)}) في خانة الوسط!",
                "Place the largest number in the shared center box and pair the remaining four into two equal sums.",
                [
                    f"To make the line sum as large as possible, put the largest number {m(best_c)} in the center.",
                    f"Pair the remaining four numbers as {m(f'{rem4[0]} + {rem4[3]} = {rem4[1]} + {rem4[2]} = {rem4[0] + rem4[3]}')}.",
                    f"Each 3-box line then adds up to {m(f'{best_c} + {rem4[0] + rem4[3]} = {ans}')}.",
                ],
                f"All valid line sums for these numbers are {', '.join(m(s) for s in sorted(valid_line_sums))}, and the largest is **{m(ans)}**!",
                "للحصول على أكبر مجموع ممكن للخط، نضع أكبر عدد في الوسط المشترك ونوزع الأربعة الباقية في زوجين متساويين.",
                [
                    f"نضع أكبر عدد {m(best_c)} في الوسط.",
                    f"نوزع الباقي إلى زوجين متساويين: {m(f'{rem4[0]} + {rem4[3]} = {rem4[1]} + {rem4[2]} = {rem4[0] + rem4[3]}')}.",
                    f"يصبح مجموع كل خط من 3 خانات {m(f'{best_c} + {rem4[0] + rem4[3]} = {ans}')}.",
                ],
                f"تحقق: المجاميع الممكنة هي {', '.join(m(s) for s in sorted(valid_line_sums))} وأكبرها **{m(ans)}**!",
                diagram_en=svg_kang_magic_cross("?", "?", "?", "?", "?"),
            )


# ==============================================================================
# UNIT 6 — Data & Probability (60 Questions: KANG-PRE-301 .. KANG-PRE-360)
# Blueprints: kang_pre_clock_hour_halfhour, kang_pre_bar_pictograph_read,
#             kang_pre_dark_room_marbles, kang_pre_spinner_most_likely
# ==============================================================================
def _fmt_hm(total_mins: int) -> str:
    h24 = (total_mins // 60) % 12
    h12 = 12 if h24 == 0 else h24
    mn = total_mins % 60
    return f"{h12}:{mn:02d}"


def _add_unit_1_6(B: BankBuilder) -> None:
    tp = "Data & Probability"

    # 21. kang_pre_clock_hour_halfhour (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_clock_hour_halfhour"
    clk_easy = [
        (2, 3, "park playtime", "اللعب في الحديقة", "Kangy", "الكنغر"),
        (4, 2, "art class", "حصة الرسم", "Lina", "لينا"),
        (7, 2, "grandma's visit", "زيارة الجدة", "Omar", "عمر"),
        (8, 3, "zoo trip", "رحلة حديقة الحيوان", "Sara", "سارة"),
        (1, 4, "beach picnic", "نزهة الشاطئ", "Tariq", "طارق"),
    ]
    for h_start, dh, act_en, act_ar, nm_en, nm_ar in clk_easy:
        t0 = h_start * 60
        ans_t = t0 + dh * 60
        ans_s = _fmt_hm(ans_t)
        d_times = [_fmt_hm(t0), _fmt_hm(ans_t - 60), _fmt_hm(ans_t + 60), _fmt_hm(ans_t - 30)]
        pairs = [(ans_s, ans_s)] + [(x, x) for x in d_times]
        B.add_bilingual(
            tp, "Easy", bp,
            f"The wall clock shows when {nm_en} starts {act_en} (`{h_start}:00`). {nm_en} finishes **{m(dh)} hours later**. What time will the clock show when {nm_en} finishes?",
            f"تُظهر ساعة الحائط وقت بدء {nm_ar} في {act_ar} (`{h_start}:00`). ينتهي بعد مرور **{m(dh)} ساعات**. كم ستكون الساعة عند الانتهاء؟",
            pairs, 0,
            f"Start at `{h_start}:00` and count {m(dh)} hours forward around the clock!",
            f"ابدأ من الساعة `{h_start}:00` وتقدّم {m(dh)} ساعات للأمام!",
            "Read the starting o'clock hour from the hands, then add the elapsed hours.",
            [
                f"The short red hour hand points to {m(h_start)} and the long blue minute hand points to {m(12)}, showing `{h_start}:00`.",
                f"Adding {m(dh)} hours gives **{ans_s}**.",
            ],
            f"Check: `{h_start} + {dh} = {h_start + dh}`, so the time is `{ans_s}`!",
            "نقرأ الساعة الابتدائية من العقربين ثم نضيف عدد الساعات المنقضية.",
            [
                f"تشير الساعة المرسومة إلى `{h_start}:00`.",
                f"بإضافة {m(dh)} ساعات تصبح الساعة **{ans_s}**.",
            ],
            f"تحقق: `{h_start} + {dh} = {h_start + dh}` أي الساعة `{ans_s}`!",
            diagram_en=svg_analog_clock(h_start, 0, angle_lbl=""),
        )

    clk_med = [
        ("analog_shift", 3, 30, 90, "Nora", "نورة"),
        ("analog_shift", 6, 30, 60, "Zaid", "زيد"),
        ("analog_shift", 5, 0, -30, "Hala", "هلا"),
        ("mins_len", 2, 15, 55, "Yousef", "يوسف"),
        ("mins_len", 4, 30, 50, "Amal", "أمل"),
    ]
    for mmode, h0, m0, delta_m, nm_en, nm_ar in clk_med:
        t0 = h0 * 60 + m0
        if mmode == "analog_shift":
            ans_t = t0 + delta_m
            ans_s = _fmt_hm(ans_t)
            d_times: list[str] = []
            for cand_t in (t0, ans_t + 30, ans_t - 30, ans_t + 60, ans_t - 60, t0 - delta_m):
                cs = _fmt_hm(cand_t)
                if cs != ans_s and cs not in d_times:
                    d_times.append(cs)
                if len(d_times) == 4:
                    break
            pairs = [(ans_s, ans_s)] + [(x, x) for x in d_times]
            if delta_m == 90:
                sh_en, sh_ar = "**1 hour and 30 minutes later**", "**بعد ساعة واحدة و30 دقيقة**"
            elif delta_m == 60:
                sh_en, sh_ar = "**1 hour later**", "**بعد ساعة واحدة**"
            else:
                sh_en, sh_ar = "**30 minutes EARLIER**", "**قبل 30 دقيقة**"
            B.add_bilingual(
                tp, "Medium", bp,
                f"Look at {nm_en}'s room clock (`{_fmt_hm(t0)}`). What time is {sh_en}?",
                f"انظر إلى ساعة غرفة {nm_ar} (`{_fmt_hm(t0)}`). كم تكون الساعة {sh_ar}؟",
                pairs, 0,
                "Remember 1 full hour is `60` minutes, and half an hour (`30` minutes) moves `:30` to the next `:00` (or `:00` back to `:30`)!",
                "تذكّر أن الساعة الكاملة `60` دقيقة، ونصف الساعة (`30` دقيقة) ينقل `:30` إلى رأس الساعة التالية!",
                "Step forward or backward in 30-minute half-hours from the shown clock time.",
                [
                    f"The clock shows `{_fmt_hm(t0)}`.",
                    f"Moving {sh_en} reaches **{ans_s}**.",
                ],
                f"Half-hour check confirms `{ans_s}`!",
                "نتحرك للأمام أو للخلف بخطوات من 30 دقيقة انطلاقاً من الوقت المرسوم.",
                [
                    f"الساعة المرسومة تشير إلى `{_fmt_hm(t0)}`.",
                    f"وبحساب الوقت {sh_ar} نصل إلى **{ans_s}**.",
                ],
                f"تحقق بأنصاف الساعات يؤكد `{ans_s}`!",
                diagram_en=svg_analog_clock(h0, m0, angle_lbl=""),
            )
        else:
            start_s = f"{h0:02d}:{m0:02d}"
            end_s = _fmt_hm(t0 + delta_m)
            h_end, m_end = (t0 + delta_m) // 60, (t0 + delta_m) % 60
            end_24 = f"{h_end:02d}:{m_end:02d}"
            ans = delta_m
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en}'s cartoon movie starts at `{start_s}` (shown on the digital clock) and finishes at `{end_24}`. How many **minutes** long is the movie?",
                f"يبدأ فيلم الكرتون لدى {nm_ar} عند الساعة `{start_s}` (كما على الساعة الرقمية) وينتهي عند `{end_24}`. كم **دقيقة** مدة الفيلم؟",
                ans, [ans - 10, ans + 10, ans + 5, 60],
                f"Count minutes from `{start_s}` up to `{h0 + 1:02d}:00` first ({m(60 - m0)} min), then add the minutes after `{h0 + 1:02d}:00`!",
                f"احسب الدقائق من `{start_s}` حتى `{h0 + 1:02d}:00` أولاً ({m(60 - m0)} دقيقة)، ثم أضف الدقائق التي بعدها!",
                "Bridge across the whole hour (:00) by adding minutes to the next hour plus minutes past that hour.",
                [
                    f"From `{start_s}` to `{h0 + 1:02d}:00` is {m(f'60 - {m0} = {60 - m0}')} minutes.",
                    f"From `{h0 + 1:02d}:00` to `{end_24}` is {m(m_end)} more minutes, totaling {m(f'{60 - m0} + {m_end} = {ans}')} minutes.",
                ],
                f"Check: `{start_s}` + {m(ans)} min = `{end_24}`!",
                "نحسب الدقائق المتبقية لإتمام الساعة التالية ثم نضيف الدقائق التي تليها.",
                [
                    f"من `{start_s}` إلى `{h0 + 1:02d}:00` توجد {m(60 - m0)} دقيقة.",
                    f"ومن `{h0 + 1:02d}:00` إلى `{end_24}` توجد {m(m_end)} دقيقة، فالمجموع {m(f'{60 - m0} + {m_end} = {ans}')} دقيقة.",
                ],
                f"تحقق: إضافة {m(ans)} دقيقة إلى `{start_s}` تعطي `{end_24}`!",
                diagram_en=svg_digital_clock(start_s, sub_lbl="Start"),
            )

    clk_hard = [
        ("offset", "08:20", +10, 25, "Joey", "جوي"),
        ("offset", "07:40", -15, 20, "Mimi", "ميمي"),
        ("offset", "09:10", +15, 35, "Koko", "كوكو"),
        ("cuckoo", 1, 15, 225, "Bibi", "بيبي"),
        ("cuckoo", 2, 15, 315, "Toto", "توتو"),
    ]
    for hmode, p1, p2, p3, nm_en, nm_ar in clk_hard:
        if hmode == "offset":
            hh, mm = [int(x) for x in str(p1).split(":")]
            shown_m = hh * 60 + mm
            offset_m = int(p2)  # + means clock is fast (ahead of real), - means slow (behind real)
            wait_m = int(p3)
            real_now = shown_m - offset_m
            bus_m = real_now + wait_m
            ans_s = f"{bus_m // 60:02d}:{bus_m % 60:02d}"
            wrong3 = f"{real_now // 60:02d}:{real_now % 60:02d}"
            wrongs: list[str] = []
            for cand_m in (shown_m + offset_m + wait_m, shown_m + wait_m, real_now, bus_m + 5, bus_m - 5, bus_m + 10, bus_m - 10):
                ws = f"{cand_m // 60:02d}:{cand_m % 60:02d}"
                if ws != ans_s and ws not in wrongs:
                    wrongs.append(ws)
                if len(wrongs) == 4:
                    break
            pairs = [(ans_s, ans_s)] + [(w, w) for w in wrongs]
            off_en = f"**{m(abs(offset_m))} minutes FAST** (ahead of the real time)" if offset_m > 0 else f"**{m(abs(offset_m))} minutes SLOW** (behind the real time)"
            off_ar = f"**متقدمة بـ {m(abs(offset_m))} دقائق** عن الوقت الحقيقي" if offset_m > 0 else f"**متأخرة بـ {m(abs(offset_m))} دقيقة** عن الوقت الحقيقي"
            B.add_bilingual(
                tp, "Hard", bp,
                f"{nm_en}'s toy clock reads `{p1}`, which is {off_en}. The school bus arrives **{m(wait_m)} minutes after the REAL time right now**. At what **real time** does the bus arrive?",
                f"تُشير ساعة {nm_ar} إلى `{p1}`، وهي {off_ar}. تصل الحافلة **بعد {m(wait_m)} دقيقة من الوقت الحقيقي الآن**. في أي **وقت حقيقي** تصل الحافلة؟",
                pairs, 0,
                f"First fix the clock to find the **real time right now** (`{wrong3}`), then add {m(wait_m)} minutes!",
                f"صحّح الساعة أولاً لمعرفة **الوقت الحقيقي الآن** (`{wrong3}`)، ثم أضف {m(wait_m)} دقيقة!",
                "Correct the fast/slow clock to get the true current time, then add the wait time.",
                [
                    f"Since `{p1}` is {'ahead' if offset_m > 0 else 'behind'} by {m(abs(offset_m))} minutes, the real time right now is `{wrong3}`.",
                    f"Adding {m(wait_m)} minutes gives the real arrival time **{ans_s}**.",
                ],
                f"Double check: `{wrong3}` + {m(wait_m)} min = `{ans_s}`!",
                "نصحح قراءة الساعة للوصول إلى الوقت الحقيقي الآن ثم نضيف مدة الانتظار.",
                [
                    f"الوقت الحقيقي الآن هو `{wrong3}`.",
                    f"وبعد مرور {m(wait_m)} دقيقة تصل الحافلة عند الساعة **{ans_s}**.",
                ],
                f"تحقق: `{wrong3}` + {m(wait_m)} دقيقة = `{ans_s}`!",
                diagram_en=svg_digital_clock(str(p1), sub_lbl="Clock"),
            )
        else:
            h_s, m_s = int(p1), int(p2)
            t_start = h_s * 60 + m_s
            t_end = int(p3)
            calls = 0
            detail = []
            for tm in range(t_start + 1, t_end + 1):
                if tm % 60 == 30:
                    calls += 1
                    detail.append(f"`{_fmt_hm(tm)}` (1)")
                elif tm % 60 == 0:
                    hc = (tm // 60) % 12 or 12
                    calls += hc
                    detail.append(f"`{_fmt_hm(tm)}` ({hc})")
            ans = calls
            B.add_math(
                tp, "Hard", bp,
                f"A wooden cuckoo bird pops out to chirp **1 time** at every half-hour (`:30`) and chirps **as many times as the hour** at every o'clock (`2` chirps at `2:00`, `3` chirps at `3:00`, and so on). How many chirps does {nm_en} hear in all from `{_fmt_hm(t_start)}` to `{_fmt_hm(t_end)}`?",
                f"يخرج طائر الكوكو الخشبي ليغرّد **مرة واحدة** عند كل نصف ساعة (`:30`)، ويغرّد **بعدد الساعة** عند تمام الساعة (`2` عند `2:00`، و`3` عند `3:00`، وهكذا). كم تغريدة يسمع {nm_ar} إجمالاً من `{_fmt_hm(t_start)}` حتى `{_fmt_hm(t_end)}`؟",
                ans, [len(detail), ans - 1, ans + 1, ans + 2],
                f"List every `:30` and `:00` stop between `{_fmt_hm(t_start)}` and `{_fmt_hm(t_end)}` and add their chirps!",
                f"اكتب كل محطة `:30` و`:00` بين `{_fmt_hm(t_start)}` و`{_fmt_hm(t_end)}` ثم اجمع تغريداتها!",
                "List each half-hour (1 chirp) and full hour (H chirps) in the interval and sum them.",
                [
                    f"Chirp stops between `{_fmt_hm(t_start)}` and `{_fmt_hm(t_end)}`: {', '.join(detail)}.",
                    f"Adding them all gives **{m(ans)}** chirps.",
                ],
                f"Interval check confirms exact **{m(ans)}** chirps!",
                "نسجل جميع أنصاف الساعات ورؤوس الساعات الواقعة في الفترة ثم نجمع التغريدات.",
                [
                    f"محطات التغريد هي: {'، '.join(detail)}.",
                    f"المجموع الكلي = **{m(ans)}** تغريدات.",
                ],
                f"تحقق من الفترة الزمنية يعطي **{m(ans)}** تغريدات!",
                diagram_en=svg_analog_clock(h_s, 0, angle_lbl=""),
            )

    # 22. kang_pre_bar_pictograph_read (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_bar_pictograph_read"
    bar_easy = [
        ([("Cat", 5, "5"), ("Dog", 4, "4"), ("Bird", 3, "3")], 6, "favorite pets", "الحيوانات المفضلة", "Jude", "جود"),
        ([("Apple", 6, "6"), ("Pear", 3, "3"), ("Plum", 5, "5")], 8, "fruits eaten", "الفواكه المأكولة", "Salman", "سلمان"),
        ([("Red", 4, "4"), ("Blue", 7, "7"), ("Gold", 2, "2"), ("Pink", 3, "3")], 8, "balloons", "البالونات", "Rayan", "ريان"),
        ([("Car", 5, "5"), ("Boat", 2, "2"), (" Kite", 6, "6"), ("Drum", 4, "4")], 8, "toys", "الألعاب", "Dana", "دانة"),
        ([("Sun", 8, "8"), ("Rain", 3, "3"), ("Wind", 4, "4")], 8, "weather days", "أيام الطقس", "Karam", "كرم"),
    ]
    for bars, ym, topic_en, topic_ar, nm_en, nm_ar in bar_easy:
        clean_bars = [(lbl.strip(), v, d) for lbl, v, d in bars]
        ans = sum(v for _, v, _ in clean_bars)
        vals = [v for _, v, _ in clean_bars]
        B.add_math(
            tp, "Easy", bp,
            f"{nm_en}'s class made this bar chart of **{topic_en}**. What is the **total** count across all {m(len(clean_bars))} bars combined?",
            f"رسم صف {nm_ar} هذا التمثيل بالأعمدة لعدد **{topic_ar}**. ما **المجموع الكلي** لجميع الأعمدة الـ {m(len(clean_bars))} معاً؟",
            ans, [max(vals), ans - 2, ans + 2, ans - min(vals)],
            "Read the number above each bar and add them all together!",
            "اقرأ العدد فوق كل عمود ثم اجمع الأعداد كلها معاً!",
            "Sum the heights of all bars shown on the chart.",
            [
                f"Bar counts are {', '.join(m(v) for v in vals)}.",
                f"Total = {m(' + '.join(str(v) for v in vals) + f' = {ans}')}.",
            ],
            f"Re-adding confirms **{m(ans)}** in total!",
            "نقرأ قيم الأعمدة جميعاً ثم نجمعها.",
            [
                f"قيم الأعمدة هي: {'، '.join(m(v) for v in vals)}.",
                f"المجموع الكلي = {m(' + '.join(str(v) for v in vals) + f' = {ans}')}.",
            ],
            f"تحقق: المجموع هو **{m(ans)}**!",
            diagram_en=svg_bar_chart(clean_bars, y_max=ym),
        )

    bar_med = [
        ("diff_comb", [("Cake", 5, "5"), ("Pie", 4, "4"), ("Tart", 3, "3")], 8, "Maya", "مايا"),
        ("diff_comb", [("Lion", 6, "6"), ("Bear", 5, "5"), ("Seal", 4, "4")], 8, "Faris", "فارس"),
        ("diff_comb", [("Star", 7, "7"), ("Moon", 3, "3"), ("Cloud", 6, "6")], 8, "Layan", "ليان"),
        ("beat_lead", [("TeamA", 8, "8"), ("TeamB", 5, "5"), ("TeamC", 6, "6")], 8, "Sami", "سامي"),
        ("beat_lead", [("Lina", 9, "9"), ("Omar", 4, "4"), ("Zaid", 7, "7")], 12, "Tala", "تالا"),
    ]
    for mmode, bars, ym, nm_en, nm_ar in bar_med:
        if mmode == "diff_comb":
            (n1, v1, _), (n2, v2, _), (n3, v3, _) = bars
            ans = (v1 + v2) - v3
            B.add_math(
                tp, "Medium", bp,
                f"Look at {nm_en}'s chart (`{n1}` = {m(v1)}, `{n2}` = {m(v2)}, `{n3}` = {m(v3)}). How many **more** votes did `{n1}` and `{n2}` get **together** than `{n3}` got alone?",
                f"انظر إلى مخطط {nm_ar} (`{n1}` = {m(v1)}، `{n2}` = {m(v2)}، `{n3}` = {m(v3)}). بكم يزيد مجموع أصوات `{n1}` و`{n2}` **معاً** عن أصوات `{n3}` وحده؟",
                ans, [v1 + v2 + v3, v1 - v3, ans + 2, max(1, ans - 2)],
                f"First add `{n1}` and `{n2}` ({m(f'{v1} + {v2} = {v1 + v2}')}), then subtract `{n3}` ({m(v3)})!",
                f"اجمع أولاً `{n1}` و`{n2}` ({m(f'{v1} + {v2} = {v1 + v2}')})، ثم اطرح `{n3}` ({m(v3)})!",
                "Add the first two bars together, then subtract the third bar.",
                [
                    f"`{n1}` + `{n2}` together = {m(f'{v1} + {v2} = {v1 + v2}')}.",
                    f"Subtracting `{n3}` ({m(v3)}) gives {m(f'{v1 + v2} - {v3} = {ans}')}.",
                ],
                f"Check: {m(f'{v3} + {ans} = {v1 + v2}')}!",
                "نجمع العمودين الأولين معاً ثم نطرح قيمة العمود الثالث.",
                [
                    f"مجموع `{n1}` و`{n2}` = {m(f'{v1} + {v2} = {v1 + v2}')}.",
                    f"الزيادة على `{n3}` = {m(f'{v1 + v2} - {v3} = {ans}')}.",
                ],
                f"تحقق: {m(f'{v3} + {ans} = {v1 + v2}')}!",
                diagram_en=svg_bar_chart(bars, y_max=ym),
            )
        else:
            (n1, v1, _), (n2, v2, _), (n3, v3, _) = bars
            # n2 is lowest, n1 is leader: how many points must n2 score to be 1 point AHEAD of n1?
            ans = (v1 + 1) - v2
            B.add_math(
                tp, "Medium", bp,
                f"On {nm_en}'s scoreboard (`{n1}` = {m(v1)}, `{n2}` = {m(v2)}, `{n3}` = {m(v3)}), how many **more** points must `{n2}` earn to be **1 point ahead** of `{n1}`?",
                f"على لوحة نقاط {nm_ar} (`{n1}` = {m(v1)}، `{n2}` = {m(v2)}، `{n3}` = {m(v3)})، كم نقطة **إضافية** يحتاج `{n2}` ليصبح متقدماً على `{n1}` بفارق **نقطة واحدة**؟",
                ans, [v1 - v2, ans + 1, max(1, ans - 2), v1 + 1],
                f"To tie `{n1}`, `{n2}` needs {m(f'{v1} - {v2} = {v1 - v2}')} points — then add {m(1)} more point to take the lead!",
                f"للتعادل مع `{n1}` يحتاج `{n2}` إلى {m(f'{v1} - {v2} = {v1 - v2}')} نقاط — ثم أضف نقطة واحدة للتقدم عليه!",
                "Target score is (leader + 1); subtract the current score from that target.",
                [
                    f"To be 1 point ahead of `{n1}` ({m(v1)}), `{n2}` must reach {m(f'{v1} + 1 = {v1 + 1}')} points.",
                    f"Since `{n2}` currently has {m(v2)}, `{n2}` needs {m(f'{v1 + 1} - {v2} = {ans}')} more points.",
                ],
                f"Check: {m(f'{v2} + {ans} = {v1 + 1}')}, which beats {m(v1)} by {m(1)}!",
                "الهدف هو (نقاط المتصدر + 1)، ثم نطرح النقاط الحالية منه.",
                [
                    f"ليتقدم على `{n1}` ({m(v1)}) بنقطة يجب أن يصل إلى {m(v1 + 1)}.",
                    f"يحتاج إذن {m(f'{v1 + 1} - {v2} = {ans}')} نقاط إضافية.",
                ],
                f"تحقق: {m(f'{v2} + {ans} = {v1 + 1}')}!",
                diagram_en=svg_bar_chart(bars, y_max=ym),
            )

    bar_hard = [
        ("scale", [("Mon", 3, "3"), ("Tue", 5, "5"), ("Wed", 4, "4")], 8, 2, "cupcakes", "كعكات", "Kangy", "الكنغر"),
        ("scale", [("BoxA", 4, "4"), ("BoxB", 2, "2"), ("BoxC", 5, "5")], 8, 3, "books", "كتب", "Lina", "لينا"),
        ("scale", [("Row1", 2, "2"), ("Row2", 4, "4"), ("Row3", 3, "3")], 8, 5, "seeds", "بذور", "Omar", "عمر"),
        ("equalize", [("Bag1", 9, "9"), ("Bag2", 6, "6"), ("Bag3", 3, "3")], 12, 0, "apples", "تفاحات", "Sara", "سارة"),
        ("equalize", [("Jar1", 10, "10"), ("Jar2", 6, "6"), ("Jar3", 2, "2")], 12, 0, "cookies", "بسكويتات", "Tariq", "طارق"),
    ]
    for hmode, bars, ym, sc, item_en, item_ar, nm_en, nm_ar in bar_hard:
        vals = [v for _, v, _ in bars]
        if hmode == "scale":
            units_sum = sum(vals)
            ans = units_sum * sc
            B.add_math(
                tp, "Hard", bp,
                f"On {nm_en}'s chart, **each {m(1)} unit on a bar stands for {m(sc)} real {item_en}**! How many **real {item_en}** do all three bars represent altogether?",
                f"في مخطط {nm_ar}، **كل وحدة واحدة ({m(1)}) في العمود تمثل {m(sc)} من {item_ar} الحقيقية**! كم يبلغ مجموع **{item_ar} الحقيقية** في الأعمدة الثلاثة معاً؟",
                ans, [units_sum, ans - sc, ans + sc, units_sum + sc],
                f"Add all bar units first ({m(' + '.join(str(v) for v in vals) + f' = {units_sum}')}), then multiply by {m(sc)} {item_en} per unit!",
                f"اجمع وحدات الأعمدة أولاً ({m(' + '.join(str(v) for v in vals) + f' = {units_sum}')})، ثم اضرب في {m(sc)} لكل وحدة!",
                "Sum the chart units across all bars, then multiply by the scale value per unit.",
                [
                    f"Total units shown = {m(' + '.join(str(v) for v in vals) + f' = {units_sum}')} units.",
                    f"Since 1 unit = {m(sc)} {item_en}, real total = {m(f'{units_sum} \\times {sc} = {ans}')} {item_en}.",
                ],
                f"Bar-by-bar check: {' + '.join(str(v * sc) for v in vals)} = **{m(ans)}**!",
                "نجمع وحدات الأعمدة كلها ثم نضرب المجموع في قيمة الوحدة الواحدة.",
                [
                    f"مجموع الوحدات على المخطط = {m(units_sum)}.",
                    f"العدد الحقيقي = {m(f'{units_sum} \\times {sc} = {ans}')}.",
                ],
                f"تحقق عموداً بعمود: {' + '.join(str(v * sc) for v in vals)} = **{m(ans)}**!",
                diagram_en=svg_bar_chart(bars, y_max=ym),
            )
        else:
            tot_v = sum(vals)
            assert tot_v % 3 == 0
            avg_v = tot_v // 3
            assert vals[1] == avg_v
            ans = vals[0] - avg_v
            assert avg_v - vals[2] == ans
            B.add_math(
                tp, "Hard", bp,
                f"The chart shows {item_en} in three containers (`{bars[0][0]}` = {m(vals[0])}, `{bars[1][0]}` = {m(vals[1])}, `{bars[2][0]}` = {m(vals[2])}). How many {item_en} must {nm_en} move from `{bars[0][0]}` into `{bars[2][0]}` so **all three containers hold the exact same number**?",
                f"يبيّن المخطط عدد {item_ar} في ثلاث حاويات (`{bars[0][0]}` = {m(vals[0])}، `{bars[1][0]}` = {m(vals[1])}، `{bars[2][0]}` = {m(vals[2])}). كم واحدة يجب أن ينقل {nm_ar} من `{bars[0][0]}` إلى `{bars[2][0]}` لتصبح **الحاويات الثلاث متساوية تماماً**؟",
                ans, [vals[0] - vals[2], avg_v, ans + 1, max(1, ans - 1)],
                f"Add all three ({m(tot_v)}) and split into 3 equal shares ({m(avg_v)} each) — see how many `{bars[0][0]}` gives away!",
                f"اجمع الثلاثة ({m(tot_v)}) وقسّمها إلى 3 حصص متساوية ({m(avg_v)} لكل حاوية) لتعرف كم تعطي `{bars[0][0]}`!",
                "Find the equal target share (total ÷ 3), then subtract it from the tallest bar.",
                [
                    f"Total {item_en} = {m(f'{vals[0]} + {vals[1]} + {vals[2]} = {tot_v}')}, so equal shares mean {m(avg_v)} in each container.",
                    f"`{bars[1][0]}` already has {m(avg_v)}! Moving {m(f'{vals[0]} - {avg_v} = {ans}')} from `{bars[0][0]}` to `{bars[2][0]}` makes all three equal {m(avg_v)}.",
                ],
                f"After moving {m(ans)}: {m(f'{vals[0]}-{ans}={avg_v}')}, {m(avg_v)}, and {m(f'{vals[2]}+{ans}={avg_v}')}!",
                "نوجد الحصة المتساوية بقسمة المجموع الكلي على 3 ثم نحسب الفائض في الحاوية الكبرى.",
                [
                    f"المجموع الكلي = {m(tot_v)}، والحصة المتساوية لكل حاوية هي {m(avg_v)}.",
                    f"ينقل {m(f'{vals[0]} - {avg_v} = {ans}')} من `{bars[0][0]}` إلى `{bars[2][0]}` فتتساوى الثلاث عند {m(avg_v)}.",
                ],
                f"تحقق: {m(f'{vals[0]}-{ans}={avg_v}')} و{m(avg_v)} و{m(f'{vals[2]}+{ans}={avg_v}')}!",
                diagram_en=svg_bar_chart(bars, y_max=ym),
            )

    # 23. kang_pre_dark_room_marbles (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_dark_room_marbles"
    mrb_easy = [
        ([("R", 4), ("B", 3)], "R", "Red (`R`)", "حمراء (`R`)", "Nora", "نورة"),
        ([("R", 5), ("Y", 4)], "R", "Red (`R`)", "حمراء (`R`)", "Zaid", "زيد"),
        ([("B", 3), ("G", 6)], "B", "Blue (`B`)", "زرقاء (`B`)", "Hala", "هلا"),
        ([("Y", 5), ("G", 2)], "G", "Green (`G`)", "خضراء (`G`)", "Yousef", "يوسف"),
        ([("R", 3), ("B", 7)], "R", "Red (`R`)", "حمراء (`R`)", "Amal", "أمل"),
    ]
    for counts, want_c, want_en, want_ar, nm_en, nm_ar in mrb_easy:
        other_sum = sum(cnt for c, cnt in counts if c != want_c)
        ans = other_sum + 1
        tot_m = sum(cnt for _, cnt in counts)
        desc_en = " and ".join(f"{m(cnt)} `{c}`" for c, cnt in counts)
        desc_ar = " و".join(f"{m(cnt)} من `{c}`" for c, cnt in counts)
        B.add_math(
            tp, "Easy", bp,
            f"A dark pouch holds {desc_en} marbles. Without looking, what is the **smallest** number of marbles {nm_en} must pull out to be **100% sure** of getting **at least 1 {want_en}** marble?",
            f"في كيس معتم توجد كرات زجاجية: {desc_ar}. من دون النظر، ما **أقل** عدد من الكرات يجب أن يسحبه {nm_ar} ليكون **متأكداً تماماً** من الحصول على **كرة واحدة على الأقل من اللون {want_ar}**؟",
            ans, [1, 2, other_sum, tot_m],
            f"Think of the **unluckiest** start: {nm_en} could pull out ALL {m(other_sum)} marbles of the other color first, and then {m(1)} more!",
            f"فكّر في **أسوأ حظ ممكن**: قد يسحب أولاً جميع الكرات الأخرى وعددها {m(other_sum)}، ثم الكرة التالية حتماً هي المطلوبة!",
            "Worst-case rule: pull all marbles of the unwanted color(s), plus 1 more.",
            [
                f"In the unluckiest case, the first {m(other_sum)} marbles pulled are all the other color.",
                f"The very next marble (`+ 1`) MUST be {want_en}, so {m(f'{other_sum} + 1 = {ans}')} marbles guarantee success.",
            ],
            f"With {m(other_sum)} picks you might still have {m(0)} `{want_c}`, so **{m(ans)}** is the exact minimum!",
            "نطبق قاعدة الحالة الأسوأ: سحب كل الكرات من اللون الآخر أولاً ثم إضافة كرة واحدة.",
            [
                f"في أسوأ حالة قد تكون أول {m(other_sum)} كرات مسحوبة كلها من اللون الآخر.",
                f"الكرة التالية مباشرة (`+ 1`) ستكون حتماً {want_ar}، إذن نحتاج {m(f'{other_sum} + 1 = {ans}')} كرات.",
            ],
            f"تحقق: عند سحب {m(other_sum)} فقط قد لا تظهر `{want_c}`، لذا **{m(ans)}** هو الحد الأدنى الأكيد!",
            diagram_en=svg_pre_marble_bag(counts, top_lbl="Dark Bag"),
        )

    mrb_med = [
        ([("R", 5), ("B", 5)], 2, "Joey", "جوي"),
        ([("R", 4), ("B", 4), ("Y", 4)], 2, "Mimi", "ميمي"),
        ([("R", 3), ("B", 4), ("G", 3), ("Y", 5)], 2, "Koko", "كوكو"),
        ([("R", 5), ("G", 5)], 3, "Bibi", "بيبي"),
        ([("R", 4), ("B", 5), ("Y", 4)], 3, "Toto", "توتو"),
    ]
    for counts, k_same, nm_en, nm_ar in mrb_med:
        worst_no_match = sum(min(cnt, k_same - 1) for _, cnt in counts)
        ans = worst_no_match + 1
        desc_en = ", ".join(f"{m(cnt)} `{c}`" for c, cnt in counts)
        desc_ar = "، ".join(f"{m(cnt)} من `{c}`" for c, cnt in counts)
        B.add_math(
            tp, "Medium", bp,
            f"A dark bag contains {desc_en} marbles ({m(len(counts))} colors). Without looking, what is the **smallest** number of marbles {nm_en} must take out to be **100% sure** of having **{m(k_same)} marbles of the SAME color**?",
            f"يحوي كيس معتم الكرات: {desc_ar} ({m(len(counts))} ألوان). من دون النظر، ما **أقل** عدد من الكرات يجب أن يسحبه {nm_ar} ليضمن الحصول على **{m(k_same)} كرات من اللون نفسه**؟",
            ans, [k_same, worst_no_match, ans + 1, ans + 2],
            f"Unluckiest start: {nm_en} gets **{m(k_same - 1)} of each of the {m(len(counts))} colors** ({m(worst_no_match)} marbles) before the next marble forces a group of {m(k_same)}!",
            f"أسوأ بداية: أن يسحب **{m(k_same - 1)} من كل لون من الألوان الـ {m(len(counts))}** ({m(worst_no_match)} كرات)، ثم الكرة التالية تكمل {m(k_same)} حتماً!",
            "Take (k - 1) marbles from each color in the worst case, then add 1.",
            [
                f"Worst case without {m(k_same)} of one color: {m(k_same - 1)} from each of the {m(len(counts))} colors = {m(worst_no_match)} marbles.",
                f"Picking {m(1)} more marble ({m(f'{worst_no_match} + 1 = {ans}')}) MUST match one of those colors and complete {m(k_same)} of a kind!",
            ],
            f"Pigeonhole check: {m(worst_no_match)} picks can tie at {m(k_same - 1)} each, so **{m(ans)}** guarantees {m(k_same)}!",
            "في أسوأ حالة نسحب (المطلوب - 1) من كل لون متاح ثم نضيف كرة واحدة.",
            [
                f"أقصى ما يُسحب دون إكمال {m(k_same)} من لون واحد هو {m(k_same - 1)} من كل لون = {m(worst_no_match)} كرات.",
                f"الكرة التالية (`+ 1`) ترفع أحد الألوان حتماً إلى {m(k_same)}، فالجواب {m(f'{worst_no_match} + 1 = {ans}')}.",
            ],
            f"تحقق: **{m(ans)}** كرات تضمن النتيجة 100%!",
            diagram_en=svg_pre_marble_bag(counts, top_lbl="Dark Bag"),
        )

    mrb_hard = [
        ("two_of_c", [("R", 4), ("B", 5), ("G", 3)], "G", "Jude", "جود"),
        ("two_of_c", [("R", 3), ("B", 4), ("Y", 6)], "R", "Salman", "سلمان"),
        ("two_of_c", [("B", 5), ("G", 4), ("Y", 3)], "Y", "Rayan", "ريان"),
        ("all_colors", [("R", 5), ("B", 4), ("G", 2)], "", "Dana", "دانة"),
        ("all_colors", [("R", 6), ("Y", 5), ("B", 3)], "", "Karam", "كرم"),
    ]
    for hmode, counts, want_c, nm_en, nm_ar in mrb_hard:
        desc_en = ", ".join(f"{m(cnt)} `{c}`" for c, cnt in counts)
        desc_ar = "، ".join(f"{m(cnt)} من `{c}`" for c, cnt in counts)
        tot_m = sum(cnt for _, cnt in counts)
        if hmode == "two_of_c":
            others = sum(cnt for c, cnt in counts if c != want_c)
            ans = others + 2
            B.add_math(
                tp, "Hard", bp,
                f"A dark bag holds {desc_en} marbles. Without looking, what is the **smallest** number of marbles {nm_en} must pick to be **100% sure** of getting **at least {m(2)} `{want_c}` marbles**?",
                f"في كيس معتم توجد الكرات: {desc_ar}. من دون النظر، ما **أقل** عدد من الكرات يجب أن يسحبه {nm_ar} ليضمن الحصول على **كرتين على الأقل من `{want_c}`**؟",
                ans, [others + 1, others, tot_m, 4],
                f"Worst case: pull ALL marbles of the **other two colors** ({m(others)} marbles), and then **{m(2)} more**!",
                f"أسوأ حالة: سحب جميع كرات **اللونين الآخرين** كلها ({m(others)} كرة)، ثم إضافة **كرتين ({m(2)})**!",
                "Pull all non-target colors in the worst case, then add 2.",
                [
                    f"Unluckiest start pulls all {m(others)} marbles that are NOT `{want_c}`.",
                    f"Only `{want_c}` marbles remain in the bag, so {m(2)} more picks give {m(f'{others} + 2 = {ans}')} marbles.",
                ],
                f"With {m(others + 1)} picks you might have only {m(1)} `{want_c}`, so **{m(ans)}** is exact!",
                "في أسوأ حالة تخرج جميع كرات الألوان الأخرى أولاً ثم نحتاج كرتين إضافيتين.",
                [
                    f"مجموع كرات اللونين الآخرين = {m(others)}.",
                    f"نضيف كرتين لضمان ظهور `{want_c}` مرتين: {m(f'{others} + 2 = {ans}')}.",
                ],
                f"تحقق: {m(others + 1)} تضمن كرة واحدة فقط من `{want_c}`، أما **{m(ans)}** فتضمن كرتين!",
                diagram_en=svg_pre_marble_bag(counts, top_lbl="Dark Bag"),
            )
        else:
            smallest_grp = min(cnt for _, cnt in counts)
            two_biggest = tot_m - smallest_grp
            ans = two_biggest + 1
            B.add_math(
                tp, "Hard", bp,
                f"A dark pouch holds {desc_en} marbles. Without looking, what is the **smallest** number of marbles {nm_en} must pull out to be **100% sure** of having **at least 1 marble of EVERY color** (all 3 colors)?",
                f"يحوي كيس معتم الكرات: {desc_ar}. من دون النظر، ما **أقل** عدد من الكرات يجب أن تسحبه {nm_ar} لتكون **متأكدة تماماً** من الحصول على **كرة واحدة على الأقل من كل لون من الألوان الثلاثة**؟",
                ans, [3, 4, two_biggest, tot_m],
                f"Unluckiest case: pull **every single marble of the TWO biggest color groups** ({m(two_biggest)} marbles) before finally getting the rarest color!",
                f"أسوأ حالة: أن تسحب **جميع كرات المجموعتين الأكبر عدداً** ({m(two_biggest)} كرة) قبل أن تخرج أول كرة من اللون الأقل عدداً!",
                "Sum the two largest color counts (worst case missing the rarest color), then add 1.",
                [
                    f"The rarest color has only {m(smallest_grp)} marbles, while the other two colors have {m(two_biggest)} marbles combined.",
                    f"In the worst case, all {m(two_biggest)} of those come out first, and pick #{m(ans)} ({m(f'{two_biggest} + 1')}) MUST be the 3rd color!",
                ],
                f"Check: {m(two_biggest)} picks can still miss the {m(smallest_grp)}-marble color, so **{m(ans)}** is required!",
                "في أسوأ حالة تُسحب جميع كرات اللونين الأكثر عدداً أولاً، ثم الكرة التالية تضمن اللون الثالث.",
                [
                    f"مجموع اللونين الأكثر عدداً = {m(two_biggest)} كرة (تاركاً اللون الأقل ذا الـ {m(smallest_grp)} كرات).",
                    f"بإضافة كرة واحدة (`+ 1`) نضمن ظهور الألوان الثلاثة: {m(f'{two_biggest} + 1 = {ans}')}.",
                ],
                f"تحقق: الحد الأدنى المضمون هو **{m(ans)}** كرات!",
                diagram_en=svg_pre_marble_bag(counts, top_lbl="Dark Bag"),
            )

    # 24. kang_pre_spinner_most_likely (5 Easy, 5 Medium, 5 Hard)
    bp = "kang_pre_spinner_most_likely"
    spin_opts_5 = [
        ("Region `1`", "المنطقة `1`"),
        ("Region `2`", "المنطقة `2`"),
        ("Region `3`", "المنطقة `3`"),
        ("Region `4`", "المنطقة `4`"),
        ("Region `5`", "المنطقة `5`"),
    ]
    spin_easy = [
        ([(0.40, "1"), (0.20, "2"), (0.15, "3"), (0.15, "4"), (0.10, "5")], "most", 0, "Maya", "مايا"),
        ([(0.15, "1"), (0.35, "2"), (0.20, "3"), (0.20, "4"), (0.10, "5")], "most", 1, "Faris", "فارس"),
        ([(0.10, "1"), (0.20, "2"), (0.45, "3"), (0.15, "4"), (0.10, "5")], "most", 2, "Layan", "ليان"),
        ([(0.25, "1"), (0.25, "2"), (0.20, "3"), (0.08, "4"), (0.22, "5")], "least", 3, "Sami", "سامي"),
        ([(0.22, "1"), (0.24, "2"), (0.26, "3"), (0.20, "4"), (0.08, "5")], "least", 4, "Tala", "تالا"),
    ]
    for sectors, ask_ml, expected_idx, nm_en, nm_ar in spin_easy:
        assert abs(sum(f for f, _ in sectors) - 1.0) < 1e-9
        fracs = [f for f, _ in sectors]
        if ask_ml == "most":
            best_f = max(fracs)
            assert fracs.count(best_f) == 1 and fracs.index(best_f) == expected_idx
            q_word_en, q_word_ar = "**MOST likely** (biggest slice)", "**الأكثر احتمالاً** (أكبر مساحة)"
        else:
            best_f = min(fracs)
            assert fracs.count(best_f) == 1 and fracs.index(best_f) == expected_idx
            q_word_en, q_word_ar = "**LEAST likely** (narrowest slice)", "**الأقل احتمالاً** (أصغر مساحة)"
        B.add_bilingual(
            tp, "Easy", bp,
            f"{nm_en} gives this fair spinner a big spin! Which numbered region is the arrow {q_word_en} to stop on?",
            f"يدير {nm_ar} هذا القرص الدوّار! أي منطقة مرقّمة هي {q_word_ar} أن يتوقف السهم عندها؟",
            spin_opts_5, expected_idx,
            "Compare the sizes of the pie slices — a wider slice gives a bigger chance, and a narrower slice gives a smaller chance!",
            "قارن أحجام القطاعات على القرص — القطاع الأوسع فرصته أكبر والقطاع الأضيق فرصته أقل!",
            "Match greatest/smallest likelihood directly to the widest/narrowest sector of the wheel.",
            [
                f"Comparing the 5 slices around the circle, **{spin_opts_5[expected_idx][0]}** has the {'widest' if ask_ml == 'most' else 'narrowest'} slice.",
                f"So the arrow is {'most' if ask_ml == 'most' else 'least'} likely to stop on **{spin_opts_5[expected_idx][0]}**.",
            ],
            f"Slice size check confirms `{expected_idx + 1}` is strictly the {'largest' if ask_ml == 'most' else 'smallest'}!",
            "الفرصة الأكبر تقابل القطاع الأوسع، والفرصة الأقل تقابل القطاع الأضيق.",
            [
                f"بمقارنة القطاعات الخمسة نجد أن **{spin_opts_5[expected_idx][1]}** هي {'الأوسع' if ask_ml == 'most' else 'الأضيق'} على القرص.",
            ],
            f"تحقق بصري وحسابي يؤكد أن المنطقة `{expected_idx + 1}` هي الصحيحة!",
            diagram_en=svg_spinner(sectors),
        )

    spin_med = [
        ("repaint", ["★", "B", "B", "★", "Y", "B", "Y", "B"], "Kangy", "الكنغر"),
        ("repaint", ["★", "R", "R", "G", "R", "G"], "Lina", "لينا"),
        ("repaint", ["★", "B", "★", "Y", "B", "★", "Y", "B", "Y", "B"], "Omar", "عمر"),
        ("score_all", ["2", "5", "4", "1", "6", "3"], "Sara", "سارة"),
        ("score_all", ["1", "8", "3", "2", "5", "4", "7", "6"], "Tariq", "طارق"),
    ]
    for mmode, wedges, nm_en, nm_ar in spin_med:
        n_w = len(wedges)
        sectors = [(1.0 / n_w, w) for w in wedges]
        if mmode == "repaint":
            cur_st = wedges.count("★")
            need_tot = n_w // 2 + 1
            ans = need_tot - cur_st
            B.add_math(
                tp, "Medium", bp,
                f"This wheel is cut into **{m(n_w)} equal slices**, and right now **{m(cur_st)} slice(s)** have a star `★`. What is the **smallest** number of non-star slices {nm_en} must repaint with `★` so that `★` covers **strictly MORE than half** of the wheel?",
                f"قُسّم هذا القرص إلى **{m(n_w)} قطاعات متساوية**، ويحمل حالياً **{m(cur_st)} منها** رمز النجمة `★`. ما **أقل** عدد من القطاعات الأخرى يجب أن يلوّنه {nm_ar} بالنجمة `★` لتغطي النجوم **أكثر من نصف القرص**؟",
                ans, [n_w // 2 - cur_st, need_tot, ans + 1, ans + 2],
                f"Half of {m(n_w)} is {m(n_w // 2)} slices, so **more than half** means at least **{m(need_tot)} star slices**!",
                f"نصف الـ {m(n_w)} هو {m(n_w // 2)} قطاعات، لذا **أكثر من النصف** يعني **{m(need_tot)} قطاعات نجمة على الأقل**!",
                "Find (N ÷ 2) + 1 slices needed for strictly more than half, then subtract current star slices.",
                [
                    f"Half of {m(n_w)} equal slices is {m(n_w // 2)}, so strictly more than half requires {m(f'{n_w // 2} + 1 = {need_tot}')} star slices.",
                    f"Since {m(cur_st)} slice(s) already have `★`, {nm_en} must repaint {m(f'{need_tot} - {cur_st} = {ans}')} more slice(s).",
                ],
                f"Check: {m(f'{cur_st} + {ans} = {need_tot}')} out of {m(n_w)} is more than half ({m(n_w // 2)})!",
                "أكثر من نصف القرص يتطلب (نصف عدد القطاعات + 1)، ثم نطرح النجوم الموجودة حالياً.",
                [
                    f"نصف الـ {m(n_w)} يساوي {m(n_w // 2)}، وأكثر من النصف يتطلب {m(need_tot)} قطاعات `★`.",
                    f"نطرح الموجود ({m(cur_st)}): {m(f'{need_tot} - {cur_st} = {ans}')} قطاعات إضافية.",
                ],
                f"تحقق: {m(need_tot)} من أصل {m(n_w)} أكبر من النصف ({m(n_w // 2)})!",
                diagram_en=svg_spinner(sectors),
            )
        else:
            nums_w = [int(w) for w in wedges]
            evens = sum(1 for v in nums_w if v % 2 == 0)
            odds = sum(1 for v in nums_w if v % 2 == 1)
            ans = 3 * evens + 1 * odds
            B.add_math(
                tp, "Medium", bp,
                f"{nm_en}'s {m(n_w)}-slice game wheel carries the numbers {', '.join(m(v) for v in nums_w)}. Landing on an **even** number wins **{m(3)} stickers**, and landing on an **odd** number wins **{m(1)} sticker**. If {nm_en}'s token visits **each of the {m(n_w)} slices once**, how many stickers does {nm_en} win altogether?",
                f"قرص اللعب ذو الـ {m(n_w)} قطاعات لدى {nm_ar} يحمل الأعداد {', '.join(m(v) for v in nums_w)}. الوقوف على عدد **زوجي** يربح **{m(3)} ملصقات**، وعلى عدد **فردي** يربح **ملصقاً واحداً ({m(1)})**. إذا وقف المؤشر على **كل قطاع من القطاعات الـ {m(n_w)} مرة واحدة**، فكم ملصقاً يربح إجمالاً؟",
                ans, [n_w, 2 * n_w, ans - 2, ans + 2],
                f"Count how many slices have **even** numbers ({m(evens)}) and how many have **odd** numbers ({m(odds)})!",
                f"عُدّ كم قطاعاً يحمل عدداً **زوجياً** ({m(evens)}) وكم قطاعاً يحمل عدداً **فردياً** ({m(odds)})!",
                "Separate the wheel numbers into even (× 3 stickers) and odd (× 1 sticker), then add.",
                [
                    f"There are {m(evens)} even slices and {m(odds)} odd slices.",
                    f"Total stickers = {m(f'{evens} \\times 3 + {odds} \\times 1 = {3 * evens} + {odds} = {ans}')}.",
                ],
                f"Check: {m(f'{3 * evens} + {odds} = {ans}')} stickers!",
                "نفصل الأعداد الزوجية (× 3) عن الأعداد الفردية (× 1) ثم نجمع الناتجين.",
                [
                    f"عدد القطاعات الزوجية = {m(evens)}، والفردية = {m(odds)}.",
                    f"مجموع الملصقات = {m(f'{evens} \\times 3 + {odds} \\times 1 = {ans}')}.",
                ],
                f"تحقق: {m(f'{3 * evens} + {odds} = {ans}')} ملصقاً!",
                diagram_en=svg_spinner(sectors),
            )

    spin_hard = [
        ("impossible", [1, 3, 7], 5, "Nora", "نورة"),
        ("impossible", [2, 5, 9], 8, "Zaid", "زيد"),
        ("impossible", [1, 4, 8], 6, "Hala", "هلا"),
        ("count_sums", [1, 3, 7], 0, "Yousef", "يوسف"),
        ("count_sums", [1, 2, 5, 10], 0, "Amal", "أمل"),
    ]
    for hmode, nums_s, imp_val, nm_en, nm_ar in spin_hard:
        sectors = [(1.0 / len(nums_s), str(v)) for v in nums_s]
        possible_sums = sorted({x + y for x in nums_s for y in nums_s})
        nums_str = ", ".join(m(v) for v in nums_s)
        if hmode == "impossible":
            assert imp_val not in possible_sums and len(possible_sums) >= 4
            ans = imp_val
            valid_4 = possible_sums[:4]
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} spins this wheel (with numbers {nums_str}) **twice** and **adds** the two numbers together (the arrow CAN land on the same number twice!). Which of these totals is **IMPOSSIBLE** to get?",
                f"تدير {nm_ar} هذا القرص (الذي يحمل الأعداد {nums_str}) **مرتين** ثم **تجمع** العددين الناتجين (ويمكن أن يقف السهم على العدد نفسه مرتين!). أي مجموع من المجاميع التالية **مستحيل** الحصول عليه؟",
                ans, valid_4,
                f"List every two-spin sum (including doubles like {m(f'{nums_s[0]}+{nums_s[0]}')}, {m(f'{nums_s[1]}+{nums_s[1]}')}, ...) and spot the outsider!",
                f"اكتب جميع مجاميع الرميتين (بما فيها جمع العدد مع نفسه مثل {m(f'{nums_s[0]}+{nums_s[0]}')}) واكتشف العدد غير الموجود!",
                "Compute all pairwise sums (including doubles) from the wheel's numbers and find which option never appears.",
                [
                    f"Possible two-spin sums from {nums_str} are {', '.join(m(s) for s in possible_sums)}.",
                    f"Every other choice is in that list, while **{m(ans)}** cannot be made by adding any two numbers on the wheel!",
                ],
                f"Checking all {m(len(possible_sums))} sums confirms {m(ans)} never occurs!",
                "نحسب جميع المجاميع الممكنة من دورانين (مع السماح بتكرار العدد نفسه) ونحدد العدد المستحيل.",
                [
                    f"جميع المجاميع الممكنة هي: {', '.join(m(s) for s in possible_sums)}.",
                    f"العدد الوحيد بين الخيارات غير الموجود في القائمة هو **{m(ans)}**!",
                ],
                f"تحقق: لا يوجد عددان على القرص مجموعهما {m(ans)}!",
                diagram_en=svg_spinner(sectors),
            )
        else:
            ans = len(possible_sums)
            B.add_math(
                tp, "Hard", bp,
                f"{nm_en} spins this wheel ({nums_str}) **twice** and **adds** the two numbers (landing on the same number twice is allowed!). How many **different totals** are possible?",
                f"يدير {nm_ar} هذا القرص ({nums_str}) **مرتين** ويجمع العددين الناتجين (يُسمح بتكرار العدد نفسه مرتين!). كم **مجموعاً مختلفاً** يمكن الحصول عليه؟",
                ans, [len(nums_s) * len(nums_s), len(nums_s) * 2 - 1, ans - 1, ans + 1],
                f"Add each number to itself AND to each bigger number, then make sure you don't count any duplicate sum twice!",
                f"اجمع كل عدد مع نفسه ومع كل عدد أكبر منه، وتأكد من عدم عدّ أي مجموع متكرر مرتين!",
                "Form all sums a + b (with a ≤ b) and count the distinct totals.",
                [
                    f"All distinct two-spin sums are {', '.join(m(s) for s in possible_sums)}.",
                    f"Counting them gives **{m(ans)}** different totals.",
                ],
                f"Distinct totals list has exact length **{m(ans)}**!",
                "نكوّن جميع الأزواج الممكنة (بما فيها العدد مع نفسه) ونعدّ النواتج المختلفة دون تكرار.",
                [
                    f"المجاميع المختلفة الممكنة هي: {', '.join(m(s) for s in possible_sums)}.",
                    f"عدد هذه المجاميع المختلفة يساوي **{m(ans)}**.",
                ],
                f"تحقق: القائمة تحوي **{m(ans)}** مجاميع مختلفة بالضبط!",
                diagram_en=svg_spinner(sectors),
            )


EXPECTED_PREECOLIER_BLUEPRINTS = (
    "kang_pre_skip_counting_hops",
    "kang_pre_two_digit_place_cards",
    "kang_pre_mini_brick_pyramids",
    "kang_pre_even_odd_sock_gloves",
    "kang_pre_toy_pan_balance",
    "kang_pre_fruit_icon_sums",
    "kang_pre_repeating_bead_train",
    "kang_pre_in_out_number_box",
    "kang_pre_shape_polygon_counting",
    "kang_pre_grid_tile_completion",
    "kang_pre_stamp_mirror_turns",
    "kang_pre_toy_cube_stacks",
    "kang_pre_grid_step_paths",
    "kang_pre_tree_lamp_gaps",
    "kang_pre_folded_strip_cuts",
    "kang_pre_opposite_die_dots",
    "kang_pre_queue_line_positions",
    "kang_pre_coin_bill_totals",
    "kang_pre_outfit_icecream_pairs",
    "kang_pre_magic_cross_five",
    "kang_pre_clock_hour_halfhour",
    "kang_pre_bar_pictograph_read",
    "kang_pre_dark_room_marbles",
    "kang_pre_spinner_most_likely",
)


def build_preecolier_bank() -> list[dict]:
    """Build and programmatically validate all 360 Kangaroo PreEcolier (Grades 1–2) questions."""
    B = BankBuilder()
    _add_unit_1_1(B)
    _add_unit_1_2(B)
    _add_unit_1_3(B)
    _add_unit_1_4(B)
    _add_unit_1_5(B)
    _add_unit_1_6(B)

    assert len(B.items) == 360, f"Expected 360 PreEcolier questions, got {len(B.items)}"

    # Verify sequential IDs, level, SVGs, blueprint counts, and difficulty splits
    bp_diff_counts: dict[tuple[str, str], int] = {}
    for idx, it in enumerate(B.items, 1):
        exp_id = f"KANG-PRE-{idx:03d}"
        assert it["id"] == exp_id, f"Expected ID {exp_id}, got {it['id']}"
        assert it["level"] == "PreEcolier", f"Unexpected level in {it['id']}: {it['level']}"
        svg_en = it["content"]["en"].get("diagram", "")
        svg_ar = it["content"]["ar"].get("diagram", "")
        assert svg_en.startswith("<svg") and svg_ar.startswith("<svg"), f"Missing SVG in {it['id']}"
        ET.fromstring(svg_en)
        ET.fromstring(svg_ar)
        # Ensure no algebraic x/y equations in Grade 1–2 stems
        stem_no_tex_cmd = re.sub(r"\\[a-zA-Z]+", " ", it["content"]["en"]["question"])
        assert not re.search(r"\b[xy]\b", stem_no_tex_cmd), f"Algebraic x/y found in {it['id']}: {stem_no_tex_cmd}"
        key = (it["kangaroo_blueprint"], it["difficulty"])
        bp_diff_counts[key] = bp_diff_counts.get(key, 0) + 1

    assert len({it["kangaroo_blueprint"] for it in B.items}) == 24
    for bp_name in EXPECTED_PREECOLIER_BLUEPRINTS:
        for diff_name in ("Easy", "Medium", "Hard"):
            cnt = bp_diff_counts.get((bp_name, diff_name), 0)
            assert cnt == 5, f"Blueprint {bp_name} ({diff_name}) has {cnt} items, expected 5"

    # Global stem uniqueness across all tracks AND existing Kangaroo divisions
    other_stems = load_other_track_stems()
    kang_path = ROOT / "data" / "kangaroo.json"
    if kang_path.exists():
        for q in json.loads(kang_path.read_text(encoding="utf-8")):
            if q.get("level") != "PreEcolier":
                other_stems.add(norm_text(q["content"]["en"]["question"]))

    seen_stems: set[str] = set()
    for it in B.items:
        ns = norm_text(it["content"]["en"]["question"])
        assert ns not in seen_stems, f"Duplicate PreEcolier stem in {it['id']}: {ns}"
        assert ns not in other_stems, f"Cross-track/division stem collision in {it['id']}: {ns}"
        seen_stems.add(ns)

    return B.items
