"""Rich Bilingual Study Lessons for ETEC Nafes National Assessment — Grade 6 (الصف السادس الابتدائي)."""
import math
from fractions import Fraction

from nafes_common import (
    BLUE,
    GREEN,
    GRID,
    MUTED,
    ORANGE,
    RED,
    SHADE,
    SHADE_ALT,
    STROKE,
    WATER,
    _wrap_nafes_svg,
    dm,
    esc,
    m,
    make_nafes_lesson,
    nafes_concept,
    nafes_worked_example,
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

LEVEL = "Grade 6"


def svg_g6_angle_pair(mode: str, lbl1: str, lbl2: str, caption: str = "") -> str:
    """Grade 6 angle relationships: 'comp' (90°), 'supp' (180°), or 'vert' (intersecting lines)."""
    w, h = 300, (182 if caption else 164)
    parts = []
    if mode == "comp":
        ox, oy = 78, 134
        parts.append(f'<line x1="{ox}" y1="{oy}" x2="236" y2="{oy}" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="24" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<rect x="{ox}" y="{oy - 14}" width="14" height="14" fill="none" stroke="{MUTED}" stroke-width="1.4"/>')
        parts.append(f'<line x1="{ox}" y1="{oy}" x2="196" y2="46" stroke="{BLUE}" stroke-width="2.2"/>')
        parts.append(f'<text x="{ox + 58}" y="{oy - 12}" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="{ox + 22}" y="{oy - 48}" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    elif mode == "supp":
        ox, oy = 150, 128
        parts.append(f'<line x1="38" y1="{oy}" x2="262" y2="{oy}" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<line x1="{ox}" y1="{oy}" x2="212" y2="38" stroke="{BLUE}" stroke-width="2.2"/>')
        parts.append(f'<circle cx="{ox}" cy="{oy}" r="3.5" fill="{STROKE}"/>')
        parts.append(f'<text x="{ox + 44}" y="{oy - 14}" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="{ox - 48}" y="{oy - 16}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    else:
        cx, cy = 150, 86
        parts.append(f'<line x1="48" y1="134" x2="252" y2="38" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<line x1="48" y1="38" x2="252" y2="134" stroke="{BLUE}" stroke-width="2.2"/>')
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{STROKE}"/>')
        parts.append(f'<text x="{cx - 48}" y="{cy + 5}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="{cx + 48}" y="{cy + 5}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    if caption:
        parts.append(f'<text x="150" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g6_triangle(a_top: str, a_bl: str, a_br: str, caption: str = "", right_bl: bool = False) -> str:
    """Triangle ABC with three labeled interior angles and optional right-angle marker at B."""
    w, h = 300, (186 if caption else 168)
    tx, ty = 146, 26
    bx, by = (68, 138) if right_bl else (56, 138)
    cx, cy = 244, 138
    if right_bl:
        tx = bx
    parts = [
        f'<polygon points="{tx},{ty} {bx},{by} {cx},{cy}" fill="#f5f3ff" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
    ]
    if right_bl:
        parts.append(f'<rect x="{bx}" y="{by - 13}" width="13" height="13" fill="none" stroke="{BLUE}" stroke-width="1.5"/>')
        parts.append(f'<text x="{tx + 18}" y="{ty + 34}" font-size="12" font-weight="800" fill="{RED}">{esc(a_top)}</text>')
        parts.append(f'<text x="{bx + 20}" y="{by - 16}" font-size="11.5" font-weight="700" fill="{BLUE}">{esc(a_bl)}</text>')
    else:
        parts.append(f'<text x="{tx}" y="{ty + 34}" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(a_top)}</text>')
        parts.append(f'<text x="{bx + 32}" y="{by - 10}" font-size="12" font-weight="800" fill="{STROKE}">{esc(a_bl)}</text>')
    parts.append(f'<text x="{cx - 34}" y="{cy - 10}" text-anchor="end" font-size="12" font-weight="800" fill="{RED}">{esc(a_br)}</text>')
    if caption:
        parts.append(f'<text x="150" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g6_parallelogram(base_lbl: str, height_lbl: str, slant_lbl: str = "") -> str:
    """Parallelogram showing base b, dashed perpendicular height h, and optional slant side."""
    w, h = 310, 172
    x0, y_bot, bw, shift, ph = 52, 134, 164, 42, 92
    y_top = y_bot - ph
    pts = f"{x0},{y_bot} {x0 + bw},{y_bot} {x0 + bw + shift},{y_top} {x0 + shift},{y_top}"
    hx = x0 + shift
    parts = [
        f'<polygon points="{pts}" fill="{WATER}" fill-opacity="0.7" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
        f'<line x1="{hx}" y1="{y_top}" x2="{hx}" y2="{y_bot}" stroke="{RED}" stroke-width="1.9" stroke-dasharray="5,3"/>',
        f'<rect x="{hx}" y="{y_bot - 11}" width="11" height="11" fill="none" stroke="{RED}" stroke-width="1.4"/>',
        f'<text x="{x0 + bw / 2:.1f}" y="{y_bot + 20}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(base_lbl)}</text>',
        f'<text x="{hx + 8}" y="{(y_top + y_bot) / 2 + 4:.1f}" font-size="12.5" font-weight="800" fill="{RED}">{esc(height_lbl)}</text>',
    ]
    if slant_lbl:
        parts.append(f'<text x="{x0 + bw + shift / 2 + 12:.1f}" y="{(y_top + y_bot) / 2:.1f}" font-size="12" font-weight="700" fill="{BLUE}">{esc(slant_lbl)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g6_quad_angles(a_tl: str, a_tr: str, a_br: str, a_bl: str, caption: str = "") -> str:
    """Quadrilateral with four labeled interior angles summing to 360°."""
    w, h = 300, (184 if caption else 166)
    tl, tr, br, bl = (78, 34), (222, 42), (248, 136), (54, 136)
    pts = f"{tl[0]},{tl[1]} {tr[0]},{tr[1]} {br[0]},{br[1]} {bl[0]},{bl[1]}"
    parts = [
        f'<polygon points="{pts}" fill="{SHADE}" fill-opacity="0.48" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
        f'<text x="{tl[0] + 18}" y="{tl[1] + 22}" font-size="12" font-weight="800" fill="{STROKE}">{esc(a_tl)}</text>',
        f'<text x="{tr[0] - 18}" y="{tr[1] + 22}" text-anchor="end" font-size="12" font-weight="800" fill="{BLUE}">{esc(a_tr)}</text>',
        f'<text x="{br[0] - 22}" y="{br[1] - 12}" text-anchor="end" font-size="12" font-weight="800" fill="{RED}">{esc(a_br)}</text>',
        f'<text x="{bl[0] + 20}" y="{bl[1] - 12}" font-size="12" font-weight="800" fill="{GREEN}">{esc(a_bl)}</text>',
    ]
    if caption:
        parts.append(f'<text x="150" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g6_circle(lbl: str, is_diameter: bool = False, caption: str = "") -> str:
    """Circle with center O and labeled radius r or full diameter d."""
    w, h = 260, (186 if caption else 168)
    cx, cy, r = 130, 84, 62
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#eff6ff" stroke="{STROKE}" stroke-width="2.1"/>',
    ]
    if is_diameter:
        parts.append(f'<line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{BLUE}" stroke-width="2.2"/>')
        parts.append(f'<circle cx="{cx - r}" cy="{cy}" r="3" fill="{STROKE}"/>')
        parts.append(f'<circle cx="{cx + r}" cy="{cy}" r="3" fill="{STROKE}"/>')
        parts.append(f'<text x="{cx}" y="{cy - 9}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl)}</text>')
    else:
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{RED}" stroke-width="2.2"/>')
        parts.append(f'<circle cx="{cx + r}" cy="{cy}" r="3" fill="{STROKE}"/>')
        parts.append(f'<text x="{cx + r / 2:.1f}" y="{cy - 9}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl)}</text>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{STROKE}"/>')
    parts.append(f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" font-size="11" font-weight="700" fill="{STROKE}">O</text>')
    if caption:
        parts.append(f'<text x="{cx}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g6_composite_l(total_w: str, total_h: str, top_w: str, right_h: str) -> str:
    """L-shaped rectilinear polygon with outer width/height and step dimensions."""
    w, h = 300, 178
    x0, y0, tw, th, lw, bh = 62, 26, 172, 114, 74, 52
    pts = f"{x0},{y0} {x0 + lw},{y0} {x0 + lw},{y0 + th - bh} {x0 + tw},{y0 + th - bh} {x0 + tw},{y0 + th} {x0},{y0 + th}"
    parts = [
        f'<polygon points="{pts}" fill="{SHADE_ALT}" fill-opacity="0.72" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
        f'<line x1="{x0 + lw}" y1="{y0 + th - bh}" x2="{x0 + lw}" y2="{y0 + th}" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4,3"/>',
        f'<text x="{x0 + lw / 2:.1f}" y="{y0 - 7}" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(top_w)}</text>',
        f'<text x="{x0 - 10}" y="{y0 + th / 2 + 4:.1f}" text-anchor="end" font-size="12" font-weight="800" fill="{STROKE}">{esc(total_h)}</text>',
        f'<text x="{x0 + tw / 2:.1f}" y="{y0 + th + 18}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(total_w)}</text>',
        f'<text x="{x0 + tw + 10}" y="{y0 + th - bh / 2 + 4:.1f}" font-size="12" font-weight="800" fill="{RED}">{esc(right_h)}</text>',
    ]
    return _wrap_nafes_svg(w, h, "".join(parts))


def _lesson_2_1() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-01",
        level=LEVEL,
        unit_num="2.1",
        topic="Numbers & Operations",
        title_en="Prime Factorization, GCD & LCM, and Fraction & Mixed-Number Operations",
        title_ar="التحليل إلى العوامل الأولية، القاسم والمضاعف المشترك، والعمليات على الكسور والأعداد الكسرية",
        summary_en="Build a rock-solid Grade 6 number foundation: factor whole numbers into prime powers, distinguish GCD grouping problems from LCM cycle problems, and add, subtract, multiply, and divide fractions and mixed numbers in simplest form.",
        summary_ar="ابنِ أساساً متيناً في الأعداد للصف السادس الابتدائي: حلّل الأعداد الكلية إلى عواملها الأولية باستعمال الأسس، وميّز بين مسائل القاسم المشترك الأكبر (ق.م.أ) والمضاعف المشترك الأصغر (م.م.أ)، وأتقن العمليات الأربع على الكسور والأعداد الكسرية في أبسط صورة.",
        goals_en=[
            f"Classify prime and composite numbers and write prime factorizations using exponents such as {m('72 = 2^3 \\times 3^2')}.",
            "Solve equal-grouping problems with **GCD** and repeating-schedule problems with **LCM**.",
            "Add and subtract unlike fractions and mixed numbers using the least common denominator (LCD) and regrouping.",
            "Multiply and divide fractions and mixed numbers by converting to improper fractions and multiplying by the reciprocal.",
        ],
        goals_ar=[
            f"تصنيف الأعداد إلى أولية وغير أولية وكتابة التحليل إلى العوامل الأولية بالأسس مثل {m('72 = 2^3 \\times 3^2')}.",
            "حل مسائل التوزيع المتساوي باستعمال **ق.م.أ** ومسائل الدورات المتكررة باستعمال **م.م.أ**.",
            "جمع وطرح الكسور غير المتشابهة والأعداد الكسرية باستعمال المقام المشترك الأصغر وإعادة التجميع.",
            "ضرب وقسمة الكسور والأعداد الكسرية بتحويلها إلى كسور غير فعلية والضرب في المقلوب.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Prime vs Composite Numbers, Exponents & Factor Trees",
                title_ar="١. الأعداد الأولية وغير الأولية والأسس وشجرة العوامل",
                body_en=f"A **prime number** greater than {m(1)} has exactly two factors ({m(1)} and itself), such as {m('2, 3, 5, 7, 11, 13')}. Notice that {m(2)} is the **only even prime**, while {m(1)} is **neither prime nor composite**! A factor tree splits any composite number until every leaf is prime, and repeated prime factors are grouped with exponents.",
                body_ar=f"**العدد الأولي** الأكبر من {m(1)} له قاسمان فقط هما {m(1)} ونفسه، مثل {m('2, 3, 5, 7, 11, 13')}. لاحظ أن {m(2)} هو **العدد الأولي الزوجي الوحيد**، بينما العدد {m(1)} **ليس أولياً ولا غير أولي**! تفكك شجرة العوامل أي عدد غير أولي حتى تصبح جميع الأطراف أعداداً أولية، ثم نجمع العوامل المتكررة بالأسس.",
                formula_en=dm("36 = 4 \\times 9 = 2 \\times 2 \\times 3 \\times 3 = 2^2 \\times 3^2"),
                caption_ar="تحليل العدد 36 إلى عوامله الأولية باستعمال الأسس:",
                formula_math_ar=dm("36 = 2^2 \\times 3^2"),
                diagram_en=svg_factor_tree("36", "4", "9", "3", "3"),
            ),
            nafes_concept(
                title_en="2. Greatest Common Divisor (GCD) vs Least Common Multiple (LCM)",
                title_ar="٢. القاسم المشترك الأكبر (ق.م.أ) والمضاعف المشترك الأصغر (م.م.أ)",
                body_en=f"Use **GCD** when cutting ribbons or packing items into the **largest equal groups** with no remainder—multiply shared prime factors with the **smallest** exponents. Use **LCM** when buses, bells, or lights repeat and **meet again** at the same time—multiply all prime factors using the **largest** exponents.",
                body_ar=f"استعمل **القاسم المشترك الأكبر (ق.م.أ)** عند تقسيم الأشرطة أو توزيع العناصر في **أكبر مجموعات متساوية** دون باقٍ (نأخذ العوامل المشتركة بأصغر أس). واستعمل **المضاعف المشترك الأصغر (م.م.أ)** عند التقاء الحافلات أو الأجراس الدورية مجدداً (نأخذ جميع العوامل بأكبر أس).",
                formula_en=dm("18 = 2 \\times 3^2,\\; 24 = 2^3 \\times 3 \\implies \\gcd(18,24) = 6,\\; \\operatorname{lcm}(18,24) = 72"),
                caption_ar="مقارنة القاسم المشترك الأكبر والمضاعف المشترك الأصغر للعددين 18 و24:",
                formula_math_ar=dm("\\gcd(18,24) = 6, \\qquad \\operatorname{lcm}(18,24) = 72"),
                diagram_en=svg_venn_2("18 = 2×3²", "24 = 2³×3", "3", "2 × 3", "2 × 2"),
            ),
            nafes_concept(
                title_en="3. Operations on Unlike Fractions & Mixed Numbers",
                title_ar="٣. العمليات الأربع على الكسور غير المتشابهة والأعداد الكسرية",
                body_en=f"To **add or subtract** unlike fractions, rewrite them over their LCD {m('\\operatorname{lcm}(b,d)')} and combine numerators only. To **multiply or divide** mixed numbers, first convert every mixed number {m('a\\frac{b}{c} = \\frac{ac+b}{c}')} into an improper fraction; for division, keep the first fraction, change {m('\\div')} to {m('\\times')}, and flip the second fraction!",
                body_ar=f"لـ **جمع أو طرح** الكسور غير المتشابهة نوحّد المقامات باستعمال المقام المشترك الأصغر ثم نجمع أو نطرح البسوط فقط. ولـ **ضرب أو قسمة** الأعداد الكسرية نحوّل كلاً منها أولاً إلى كسر غير فعلي {m('a\\frac{b}{c} = \\frac{ac+b}{c}')}؛ وفي القسمة نثبّت الكسر الأول ونحوّل القسمة إلى ضرب في **مقلوب** الكسر الثاني!",
                formula_en=dm("\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c} = \\frac{ad}{bc}"),
                caption_ar="قاعدة قسمة الكسور بالضرب في المقلوب:",
                formula_math_ar=dm("\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}"),
                diagram_en=svg_nafes_fraction_bars(4, 6, 1, 6, "2/3 = 4/6", "+ 1/6 = 5/6"),
            ),
        ],
        traps_en=[
            f"Counting {m(1)} as a prime number or forgetting that {m('2^3 = 2 \\times 2 \\times 2 = 8')} (NOT {m('2 \\times 3 = 6')}).",
            f"Adding denominators directly: {m('\\frac{1}{3} + \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2}')}, NEVER {m('\\frac{2}{9}')}.",
            f"Multiplying whole parts and fraction parts separately ({m('2\\frac{1}{2} \\times 1\\frac{1}{2} \\ne 2\\frac{1}{4}')}); always convert to improper fractions ({m('\\frac{5}{2} \\times \\frac{3}{2} = \\frac{15}{4} = 3\\frac{3}{4}')}).",
        ],
        traps_ar=[
            f"اعتبار العدد {m(1)} عدداً أولياً، أو الوقوع في خطأ حساب القوى مثل كتابة {m('2^3 = 6')} بدلاً من {m('2 \\times 2 \\times 2 = 8')}.",
            f"جمع المقامين معاً عند جمع الكسور: {m('\\frac{1}{3} + \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2}')} وليس {m('\\frac{2}{9}')} أبداً.",
            f"ضرب الأجزاء الصحيحة وحدها والكسور وحدها؛ بل يجب التحويل إلى كسور غير فعلية أولاً ({m('\\frac{5}{2} \\times \\frac{3}{2} = \\frac{15}{4} = 3\\frac{3}{4}')}).",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-01-EX1",
                title_en="Prime Factorization with Exponents",
                title_ar="التحليل إلى العوامل الأولية بالأسس",
                q_en=f"In a Grade 6 STEM challenge, Sara builds a factor tree for {m(72)}. Which expression gives the prime factorization of {m(72)}?",
                q_ar=f"في تحدي العلوم والرياضيات للصف السادس، رسمت سارة شجرة العوامل للعدد {m(72)}. أي عبارة مما يلي تمثّل التحليل إلى العوامل الأولية للعدد {m(72)}؟",
                correct_val="2^3 \\times 3^2",
                distractors=["2^2 \\times 3^3", "8 \\times 9", "2^3 \\times 6"],
                idea_en="Split 72 into 8 and 9, then factor both completely into primes 2 and 3.",
                steps_en=[
                    f"Write {m('72 = 8 \\times 9')}.",
                    f"Factor each composite branch: {m('8 = 2 \\times 2 \\times 2 = 2^3')} and {m('9 = 3 \\times 3 = 3^2')}.",
                    f"Combine the prime powers: {m('72 = 2^3 \\times 3^2')}.",
                ],
                check_en=f"{m('8 \\times 9 = 72')}, and both {m(2)} and {m(3)} are prime.",
                idea_ar="فكّك العدد 72 إلى 8 × 9 ثم حلّل كل فرع إلى عوامله الأولية 2 و3.",
                steps_ar=[
                    f"نكتب {m('72 = 8 \\times 9')}.",
                    f"نحلّل كل عدد غير أولي: {m('8 = 2^3')} و{m('9 = 3^2')}.",
                    f"إذن التحليل التام إلى العوامل الأولية هو {m('2^3 \\times 3^2')}.",
                ],
                check_ar=f"{m('2^3 \\times 3^2 = 8 \\times 9 = 72')} وجميع الأساسات أولية.",
                diagram_en=svg_factor_tree("72", "8", "9", "3", "3"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-01-EX2",
                title_en="Repeating Shuttle Buses with LCM",
                title_ar="التقاء الحافلات الترددية بالمضاعف المشترك الأصغر",
                q_en=f"At a Riyadh science exhibition, Shuttle A departs every {m(12)} minutes and Shuttle B departs every {m(18)} minutes. If both depart together at {m('8{:}00')}, after how many minutes will they next depart together?",
                q_ar=f"في معرض علمي بالرياض، تنطلق الحافلة (أ) كل {m(12)} دقيقة وتنطلق الحافلة (ب) كل {m(18)} دقيقة. إذا انطلقتا معاً الساعة {m('8{:}00')}، فبعد كم دقيقة تنطلقان معاً للمرة التالية؟",
                correct_val=36,
                distractors=[6, 24, 72],
                idea_en="Repeating departures align at the Least Common Multiple (LCM) of 12 and 18.",
                steps_en=[
                    f"List multiples of {m(12)}: {m('12, 24, 36, 48, \\dots')}",
                    f"List multiples of {m(18)}: {m('18, 36, 54, \\dots')}",
                    f"The smallest shared multiple is {m('\\operatorname{lcm}(12, 18) = 36')} minutes.",
                ],
                check_en=f"{m('36 \\div 12 = 3')} trips of A and {m('36 \\div 18 = 2')} trips of B.",
                idea_ar="تلتقي المواعيد الدورية عند المضاعف المشترك الأصغر (م.م.أ) للعددين 12 و18.",
                steps_ar=[
                    f"مضاعفات العدد {m(12)} هي: {m('12, 24, 36, 48, \\dots')}",
                    f"مضاعفات العدد {m(18)} هي: {m('18, 36, 54, \\dots')}",
                    f"أصغر مضاعف مشترك بينهما هو {m(36)} دقيقة.",
                ],
                check_ar=f"{m('36 \\div 12 = 3')} رحلات و{m('36 \\div 18 = 2')} رحلتان دون باقٍ.",
                diagram_en=svg_number_strip(["0 min", "12 min", "18 min", "24 min", "? min"]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-01-EX3",
                title_en="Adding Unlike Fractions in Simplest Form",
                title_ar="جمع كسرين غير متشابهين في أبسط صورة",
                q_en=f"Noura used {m('\\frac{3}{8}')} liter of rose water in one recipe and {m('\\frac{1}{4}')} liter in another. How many liters of rose water did she use altogether?",
                q_ar=f"استعملت نورة {m('\\frac{3}{8}')} لتر من ماء الورد في وصفة أولى و{m('\\frac{1}{4}')} لتر في وصفة ثانية. كم لتراً من ماء الورد استعملت في الوصفتين معاً؟",
                correct_val=Fraction(5, 8),
                distractors=[Fraction(4, 12), Fraction(1, 2), Fraction(3, 4)],
                idea_en="Rewrite 1/4 with denominator 8, then add the numerators.",
                steps_en=[
                    f"The least common denominator of {m(8)} and {m(4)} is {m(8)}.",
                    f"Convert {m('\\frac{1}{4} = \\frac{2}{8}')}.",
                    f"Add numerators: {m('\\frac{3}{8} + \\frac{2}{8} = \\frac{5}{8}')} liter.",
                ],
                check_en=f"{m('\\gcd(5, 8) = 1')}, so {m('\\frac{5}{8}')} is already in simplest form.",
                idea_ar="نوحّد المقامين على المقام المشترك الأصغر 8 ثم نجمع البسطين.",
                steps_ar=[
                    f"المقام المشترك الأصغر للعددين {m(8)} و{m(4)} هو {m(8)}.",
                    f"نكتب الكسر المكافئ: {m('\\frac{1}{4} = \\frac{2}{8}')}.",
                    f"نجمع البسطين: {m('\\frac{3}{8} + \\frac{2}{8} = \\frac{5}{8}')} لتر.",
                ],
                check_ar=f"القاسم المشترك الأكبر للعددين 5 و8 هو 1، فالكسر {m('\\frac{5}{8}')} في أبسط صورة.",
                diagram_en=svg_nafes_fraction_bars(3, 8, 2, 8, "3/8 L", "1/4 = 2/8 L"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-01-EX4",
                title_en="Dividing a Mixed Number by a Fraction",
                title_ar="قسمة عدد كسري على كسر اعتيادي",
                q_en=f"An art teacher cuts a {m('4\\frac{1}{2}')}-meter green ribbon into equal badges of length {m('\\frac{3}{4}')} meter each. How many badges can she make?",
                q_ar=f"قصّت معلمة التربية الفنية شريطاً أخضر طوله {m('4\\frac{1}{2}')} متر إلى أوسمة متساوية طول كلٍّ منها {m('\\frac{3}{4}')} متر. كم وساماً يمكنها صنعه؟",
                correct_val=6,
                distractors=[4, 5, 8],
                idea_en="Convert 4 1/2 to an improper fraction and multiply by the reciprocal of 3/4.",
                steps_en=[
                    f"Convert the mixed number: {m('4\\frac{1}{2} = \\frac{9}{2}')}.",
                    f"Multiply by the reciprocal of {m('\\frac{3}{4}')}: {m('\\frac{9}{2} \\times \\frac{4}{3}')}.",
                    f"Simplify: {m('\\frac{36}{6} = 6')} badges.",
                ],
                check_en=f"{m('6 \\times \\frac{3}{4} = \\frac{18}{4} = 4\\frac{1}{2}')} meters.",
                idea_ar="نحوّل العدد الكسري 4 و1/2 إلى كسر غير فعلي ثم نضرب في مقلوب 3/4.",
                steps_ar=[
                    f"نحوّل العدد الكسري: {m('4\\frac{1}{2} = \\frac{9}{2}')}.",
                    f"نضرب في مقلوب المقسوم عليه: {m('\\frac{9}{2} \\times \\frac{4}{3}')}.",
                    f"نبسّط الناتج: {m('\\frac{36}{6} = 6')} أوسمة.",
                ],
                check_ar=f"التحقق بالضرب العكسي: {m('6 \\times \\frac{3}{4} = \\frac{18}{4} = 4\\frac{1}{2}')} متر.",
                diagram_en=svg_nafes_fraction_bars(3, 4, 6, 8, "3/4 m badge", "Total: 9/2 m"),
            ),
        ],
        blueprints=["G6-NUM-01", "G6-NUM-02", "G6-NUM-03", "G6-NUM-04"],
    )


def _lesson_2_2() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-02",
        level=LEVEL,
        unit_num="2.2",
        topic="Numbers & Operations",
        title_en="Decimals, Ratios, Unit Rates, Proportions & Percentages",
        title_ar="الكسور العشرية، النسبة والمعدل، التناسب، والنسب المئوية",
        summary_en="Master everyday proportional reasoning on the ETEC Nafes test: compute accurately with decimals, compare ratios and unit rates, solve scale-map proportions, and calculate percentages and Saudi Riyal (SAR) discounts.",
        summary_ar="أتقن مهارات التناسب والحسابات اليومية في اختبار نافس: نفّذ العمليات الأربع على الكسور العشرية بدقة، وقارن النسب ومعدلات الوحدة، وحل تناسبات مقياس الرسم، واحسب النسب المئوية والتخفيضات بالريال السعودي.",
        goals_en=[
            "Round, add, subtract, multiply, and divide decimals up to thousandths accurately.",
            "Write ratios in simplest form, complete ratio tables, and compute unit rates (speed and unit price).",
            f"Solve proportions {m('\\frac{a}{b} = \\frac{c}{x}')} using scaling or cross-products and interpret map scales.",
            "Convert fluently among fractions, decimals, and percentages and calculate SAR sale prices.",
        ],
        goals_ar=[
            "تقريب الكسور العشرية حتى جزء من ألف وجمعها وطرحها وضربها وقسمتها بدقة.",
            "كتابة النسب في أبسط صورة وإكمال جداول النسب وحساب معدل الوحدة (السرعة وسعر الوحدة).",
            f"حل التناسبات {m('\\frac{a}{b} = \\frac{c}{x}')} باستعمال الكسور المتكافئة أو الضرب التبادلي وتطبيق مقياس الرسم.",
            "التحويل بطلاقة بين الكسور الاعتيادية والعشرية والنسب المئوية وحساب سعر البيع بالريال بعد الخصم.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Decimal Place Value, Alignment & Decimal Point Shifts",
                title_ar="١. القيمة المنزلية للكسور العشرية ومحاذاة الفاصلة وتحريكها",
                body_en=f"When **adding or subtracting** decimals, line up the **decimal points** vertically and pad empty places with zeros. When **multiplying**, count the total decimal places in both factors ({m('1.2 \\times 0.04 = 0.048')} has {m('1+2=3')} places). When **dividing** by a decimal, multiply both dividend and divisor by {m(10)} or {m(100)} first so the divisor becomes a whole number!",
                body_ar=f"عند **جمع أو طرح** الكسور العشرية، رتّب **الفواصل العشرية** بعضها فوق بعض وأضف أصفاراً للمنازل الخالية. وعند **الضرب** اجمع عدد المنازل العشرية في العاملين ({m('1.2 \\times 0.04 = 0.048')} ثلاث منازل). وعند **القسمة** على كسر عشري، اضرب المقسوم والمقسوم عليه في {m(10)} أو {m(100)} ليصبح المقسوم عليه عدداً كلياً!",
                formula_en=dm("14.4 \\div 0.6 = \\frac{14.4 \\times 10}{0.6 \\times 10} = \\frac{144}{6} = 24"),
                caption_ar="تحويل المقسوم عليه إلى عدد كلي بضرب الحدين في 10:",
                formula_math_ar=dm("14.4 \\div 0.6 = 144 \\div 6 = 24"),
                diagram_en=svg_nafes_function_table(
                    ["Place", "Ones", "Tenths", "Hundredths", "Thousandths"],
                    [["Value", "4", "0.3", "0.07", "0.005"]],
                ),
            ),
            nafes_concept(
                title_en="2. Ratios, Unit Rates & Solving Proportions",
                title_ar="٢. النسبة ومعدل الوحدة وحل التناسب",
                body_en=f"A **unit rate** compares a quantity to **1 unit** of another quantity (such as {m('80\\text{ km/h}')} or {m('6\\text{ SAR per notebook}')}). Two equal ratios form a **proportion** {m('\\frac{a}{b} = \\frac{c}{d}')}, which always satisfies the cross-product rule {m('a \\times d = b \\times c')}. On maps, {m('1\\text{ cm} : 25\\text{ km}')} means every centimeter on paper represents {m(25)} km on the ground.",
                body_ar=f"**معدل الوحدة** يقارن كمية بـ **وحدة واحدة** من كمية أخرى (مثل {m('80\\text{ كم/ساعة}')} أو {m('6\\text{ ريالات للدفتر}')}). وتشكّل النسبتان المتساويتان **تناسباً** {m('\\frac{a}{b} = \\frac{c}{d}')} يحقق دائماً قاعدة الضرب التبادلي {m('a \\times d = b \\times c')}. وفي الخرائط يعني المقياس {m('1\\text{ سم} : 25\\text{ كم}')} أن كل سنتيمتر على الخريطة يقابل {m(25)} كم في الواقع.",
                formula_en=dm("\\frac{a}{b} = \\frac{c}{x} \\implies a \\cdot x = b \\cdot c \\implies x = \\frac{b \\cdot c}{a}"),
                caption_ar="حل التناسب باستعمال الضرب التبادلي:",
                formula_math_ar=dm("\\frac{a}{b} = \\frac{c}{x} \\implies x = \\frac{b \\cdot c}{a}"),
                diagram_en=svg_nafes_function_table(
                    ["Notebooks", "3", "6", "9", "12"],
                    [["Price (SAR)", "18", "36", "?", "72"]],
                    highlight_cell=(0, 3),
                ),
            ),
            nafes_concept(
                title_en="3. Fractions, Decimals, Percentages & SAR Discounts",
                title_ar="٣. التحويل بين الكسور والنسب المئوية وحساب الخصم بالريال",
                body_en=f"**Percent** means **out of 100**: {m('25\\% = \\frac{25}{100} = \\frac{1}{4} = 0.25')}, {m('20\\% = \\frac{1}{5} = 0.2')}, and {m('75\\% = \\frac{3}{4} = 0.75')}. To find a **sale price** after a {m('p\\%')} discount, first compute the discount {m('\\frac{p}{100} \\times \\text{Original Price}')}, then **subtract** it from the original price!",
                body_ar=f"كلمة **بالمئة** تعني **من كل 100**: {m('25\\% = \\frac{1}{4} = 0.25')}، و{m('20\\% = \\frac{1}{5} = 0.2')}، و{m('75\\% = \\frac{3}{4} = 0.75')}. ولإيجاد **سعر البيع بعد الخصم** بنسبة {m('p\\%')}، احسب أولاً مقدار الخصم {m('\\frac{p}{100} \\times \\text{السعر الأصلي}')} ثم **اطرحه** من السعر الأصلي!",
                formula_en=dm("\\text{Sale Price} = \\text{Original} - \\left(\\frac{p}{100} \\times \\text{Original}\\right)"),
                caption_ar="قانون سعر البيع النهائي بعد الخصم:",
                formula_math_ar=dm("\\text{Sale Price} = \\left(1 - \\frac{p}{100}\\right) \\times \\text{Original}"),
                diagram_en=svg_fraction_grid(10, 5, 15, 0),
            ),
        ],
        traps_en=[
            f"Right-aligning digits instead of decimal points: {m('4.8 + 0.35 = 5.15')}, NOT {m('0.83')} or {m('8.3')}.",
            f"Misplacing the decimal in multiplication: {m('0.3 \\times 0.4 = 0.12')} (two decimal places), NOT {m('1.2')}.",
            "Stopping at the discount amount (e.g., 30 SAR) when the question asks for the **final sale price** paid at checkout!",
        ],
        traps_ar=[
            f"محاذاة الأرقام يميناً بدلاً من محاذاة الفاصلة العشرية: {m('4.8 + 0.35 = 5.15')} وليس {m('0.83')}.",
            f"الخطأ في عدّ المنازل العشرية عند الضرب: {m('0.3 \\times 0.4 = 0.12')} (منزلتان عشريتان) وليس {m('1.2')}.",
            "التوقف عند قيمة الخصم فقط بينما السؤال يطلب **سعر البيع النهائي** بعد طرح الخصم!",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-02-EX1",
                title_en="Dividing a Decimal by a Decimal",
                title_ar="قسمة كسر عشري على كسر عشري",
                q_en=f"A Qassim honey producer pours {m('13.5')} liters of Sidr honey equally into jars holding {m('0.45')} liter each. How many jars are filled?",
                q_ar=f"يفرّغ منتج عسل في القصيم {m('13.5')} لتر من عسل السدر بالتساوي في عبوات سعة كلٍّ منها {m('0.45')} لتر. كم عبوة تمتلئ تماماً؟",
                correct_val=30,
                distractors=[3, 25, 300],
                idea_en="Multiply both 13.5 and 0.45 by 100 so you divide whole numbers.",
                steps_en=[
                    f"Shift both decimal points two places right: {m('13.5 \\div 0.45 = 1350 \\div 45')}.",
                    f"Since {m('45 \\times 3 = 135')}, we get {m('1350 \\div 45 = 30')}.",
                ],
                check_en=f"{m('30 \\times 0.45 = 13.5')} liters.",
                idea_ar="اضرب المقسوم والمقسوم عليه في 100 للتخلص من الفاصلة في المقسوم عليه.",
                steps_ar=[
                    f"نحرّك الفاصلة منزلتين لليمين في العددين: {m('13.5 \\div 0.45 = 1350 \\div 45')}.",
                    f"بما أن {m('45 \\times 3 = 135')} فإن {m('1350 \\div 45 = 30')} عبوة.",
                ],
                check_ar=f"{m('30 \\times 0.45 = 13.5')} لتر بالضبط.",
                diagram_en=svg_two_jars("13.5 L total", 0.85, "0.45 L jar", 0.32, "÷ 0.45"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-02-EX2",
                title_en="Finding Unit Speed",
                title_ar="إيجاد معدل الوحدة للسرعة",
                q_en=f"Haramain High-Speed Train covers {m(270)} kilometers at a steady rate in {m('1.5')} hours. What is its unit speed in kilometers per hour?",
                q_ar=f"يقطع قطار الحرمين السريع مسافة {m(270)} كيلومتراً بسرعة ثابتة خلال {m('1.5')} ساعة. ما معدل سرعته بالكيلومتر في الساعة الواحدة؟",
                correct_val=180,
                distractors=[135, 160, 405],
                idea_en="Divide total distance (270 km) by time (1.5 hours) to get kilometers per 1 hour.",
                steps_en=[
                    f"Write the rate: {m('\\frac{270\\text{ km}}{1.5\\text{ h}}')}.",
                    f"Multiply numerator and denominator by {m(10)}: {m('\\frac{2700}{15} = 180')} km/h.",
                ],
                check_en=f"{m('180 \\times 1.5 = 270')} km.",
                idea_ar="اقسم المسافة الكلية (270 كم) على الزمن (1.5 ساعة) لإيجاد المسافة في ساعة واحدة.",
                steps_ar=[
                    f"نكتب المعدل: {m('270 \\div 1.5')}.",
                    f"نضرب الحدين في {m(10)}: {m('2700 \\div 15 = 180')} كم/ساعة.",
                ],
                check_ar=f"{m('180 \\times 1.5 = 270')} كم.",
                diagram_en=svg_motion_timeline("Start", "270 km", "Time = 1.5 h", "v = ? km/h", "", meet=False),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-02-EX3",
                title_en="Map Scale Proportion",
                title_ar="تناسب مقياس الرسم على الخريطة",
                q_en=f"On a tourist map of Al-Ula, the scale is {m('2\\text{ cm} : 15\\text{ km}')}. If two heritage sites are {m(8)} cm apart on the map, what is the actual distance between them in kilometers?",
                q_ar=f"على خريطة سياحية للعلا، مقياس الرسم هو {m('2\\text{ سم} : 15\\text{ كم}')}. إذا كانت المسافة بين موقعين أثريين على الخريطة {m(8)} سم، فكم المسافة الحقيقية بينهما بالكيلومترات؟",
                correct_val=60,
                distractors=[30, 45, 120],
                idea_en="Set up the proportion 2 / 15 = 8 / x and scale both terms by 4.",
                steps_en=[
                    f"Write the proportion: {m('\\frac{2}{15} = \\frac{8}{x}')}.",
                    f"Since {m('2 \\times 4 = 8')}, multiply {m(15)} by {m(4)} as well: {m('x = 15 \\times 4 = 60')} km.",
                ],
                check_en=f"Cross-products match: {m('2 \\times 60 = 120')} and {m('15 \\times 8 = 120')}.",
                idea_ar="نكتب التناسب 2 / 15 = 8 / س ونضرب حدي النسبة الأولى في 4.",
                steps_ar=[
                    f"نكتب التناسب: {m('\\frac{2}{15} = \\frac{8}{x}')}.",
                    f"بما أن {m('2 \\times 4 = 8')}، نضرب المقام في {m(4)}: {m('x = 15 \\times 4 = 60')} كم.",
                ],
                check_ar=f"الضرب التبادلي متساوٍ: {m('2 \\times 60 = 15 \\times 8 = 120')}.",
                diagram_en=svg_nafes_function_table(
                    ["Map (cm)", "2", "8"],
                    [["Actual (km)", "15", "?"]],
                    highlight_cell=(0, 2),
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-02-EX4",
                title_en="Sale Price After Percentage Discount",
                title_ar="سعر البيع بعد خصم بنسبة مئوية",
                q_en=f"A bookstore in Jeddah offers a {m('25\\%')} discount on an encyclopedia priced at {m(160)} SAR. What is the sale price after the discount?",
                q_ar=f"تقدّم مكتبة في جدة خصماً نسبته {m('25\\%')} على موسوعة علمية سعرها الأصلي {m(160)} ريالاً. فما سعر بيعها بعد الخصم؟",
                correct_val=120,
                distractors=[40, 125, 135],
                idea_en="Find 25% (one-fourth) of 160 SAR, then subtract it from 160 SAR.",
                steps_en=[
                    f"Recall {m('25\\% = \\frac{1}{4}')}, so the discount is {m('\\frac{1}{4} \\times 160 = 40')} SAR.",
                    f"Subtract from the original price: {m('160 - 40 = 120')} SAR.",
                ],
                check_en=f"Paying {m('75\\%')} of {m(160)} gives {m('\\frac{3}{4} \\times 160 = 120')} SAR.",
                idea_ar="نحسب ربع المبلغ (25% من 160 ريالاً) ثم نطرحه من السعر الأصلي.",
                steps_ar=[
                    f"بما أن {m('25\\% = \\frac{1}{4}')} فإن قيمة الخصم هي {m('\\frac{1}{4} \\times 160 = 40')} ريالاً.",
                    f"سعر البيع بعد الخصم: {m('160 - 40 = 120')} ريالاً.",
                ],
                check_ar=f"يدفع المشتري {m('75\\%')} من السعر: {m('\\frac{3}{4} \\times 160 = 120')} ريالاً.",
                diagram_en=svg_nafes_sar_money([100, 50, 10], "Original: 160 SAR (-25%)"),
            ),
        ],
        blueprints=["G6-NUM-05", "G6-NUM-06", "G6-NUM-07", "G6-NUM-08"],
    )


def _lesson_2_3() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-03",
        level=LEVEL,
        unit_num="2.3",
        topic="Algebra",
        title_en="Order of Operations, Algebraic Expressions, Function Tables & One-Step Equations",
        title_ar="ترتيب العمليات، العبارات الجبرية، جداول الدوال، ومعادلات الخطوة الواحدة",
        summary_en="Transition smoothly into Grade 6 algebra: apply parentheses and exponents in the exact order of operations, evaluate multi-variable expressions, uncover rules in linear function tables, and solve equations on balance models.",
        summary_ar="انتقل بثقة إلى جبر الصف السادس الابتدائي: طبّق ترتيب العمليات الحسابية مع الأقواس والأسس، واحسب قيم العبارات الجبرية، واكتشف قواعد المتتابعات وجداول الدوال الخطية، وحل المعادلات باستعمال الميزان والعمليات العكسية.",
        goals_en=[
            "Evaluate numerical expressions containing parentheses, exponents, multiplication/division, and addition/subtraction.",
            f"Translate verbal phrases into algebraic expressions and evaluate {m('ax + by')} for given values.",
            f"Extend arithmetic/geometric sequences and complete two-operation function tables {m('y = ax + b')}.",
            f"Solve one-step and simple two-step equations ({m('x + a = b')}, {m('ax = c')}, {m('ax + b = c')}) and balance puzzles.",
        ],
        goals_ar=[
            "إيجاد قيمة العبارات العددية المتضمنة أقواساً وأسساً وضرباً وقسمة وجمعاً وطرحاً بالترتيب الصحيح.",
            f"ترجمة العبارات اللفظية إلى عبارات جبرية وحساب قيمة {m('ax + by')} عند قيم معطاة للمتغيرات.",
            f"توسيع المتتابعات الحسابية والهندسية وإكمال جداول الدوال ذات الخطوتين {m('y = ax + b')}.",
            f"حل معادلات الخطوة الواحدة والخطوتين البسيطة ({m('x + a = b')}، {m('ax = c')}، {m('ax + b = c')}) ونماذج الميزان.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Order of Operations (Parentheses, Exponents, ×/÷, +/−)",
                title_ar="١. ترتيب العمليات الحسابية (الأقواس، الأسس، الضرب والقسمة، الجمع والطرح)",
                body_en=f"Every mathematician evaluates expressions in four strict stages: **(1)** inside **parentheses** {m('(\\ )')}, **(2)** **exponents/powers** {m('a^n')}, **(3)** **multiplication and division** from **left to right**, and **(4)** **addition and subtraction** from **left to right**.",
                body_ar=f"تُحسب قيمة أي عبارة عددية وفق أربع مراحل مرتبة: **(1)** ما بداخل **الأقواس** {m('(\\ )')} أولاً، **(2)** **القوى والأسس** {m('a^n')}، **(3)** **الضرب والقسمة** بالترتيب من اليمين إلى اليسار حسب كتابة العبارة الإنجليزية (من اليسار إلى اليمين في الصيغة الرياضية اللاتينية)، **(4)** **الجمع والطرح** بالترتيب نفسه.",
                formula_en=dm("20 - 12 \\div 3 + 2^3 = 20 - 12 \\div 3 + 8 = 20 - 4 + 8 = 24"),
                caption_ar="مثال تطبيقي على ترتيب العمليات الحسابية:",
                formula_math_ar=dm("20 - 12 \\div 3 + 2^3 = 20 - 4 + 8 = 24"),
                diagram_en=svg_function_machine("( ) then aⁿ", "× and ÷", "+ and −", "Result"),
            ),
            nafes_concept(
                title_en="2. Evaluating Algebraic Expressions & Linear Function Tables",
                title_ar="٢. حساب قيمة العبارات الجبرية وجداول الدوال الخطية",
                body_en=f"To evaluate an expression like {m('3m - 2n')}, substitute the given number for each variable and follow the order of operations. In a **function table** {m('y = ax + b')}, when the input {m('x')} increases by {m(1)}, the output {m('y')} changes by a constant step {m('a')}!",
                body_ar=f"لحساب قيمة عبارة جبرية مثل {m('3m - 2n')}، نعوّض عن كل متغير بقيمته المعطاة ثم نتّبع ترتيب العمليات. وفي **جدول الدالة الخطية** {m('y = ax + b')}، كلما زادت المدخلة {m('x')} بمقدار {m(1)} تتغير المخرجة {m('y')} بمقدار ثابت يساوي {m('a')}!",
                formula_en=dm("y = 3x + 2: \\quad x = 1 \\mapsto 5,\\quad x = 2 \\mapsto 8,\\quad x = 3 \\mapsto 11"),
                caption_ar="قاعدة جدول الدالة الخطية ذات الخطوتين:",
                formula_math_ar=dm("y = 3x + 2"),
                diagram_en=svg_nafes_function_table(
                    ["Input x", "1", "2", "3", "4"],
                    [["Output 3x + 2", "5", "8", "11", "?"]],
                    highlight_cell=(0, 4),
                ),
            ),
            nafes_concept(
                title_en="3. Solving Equations by Inverse Operations & Balance Scales",
                title_ar="٣. حل المعادلات بالعمليات العكسية ونماذج الميزان",
                body_en=f"An equation is a balanced scale: whatever you do to one pan, you **must do to the other pan**. Undo addition with **subtraction**, undo subtraction with **addition**, and undo multiplication with **division**. For {m('ax + b = c')}, subtract {m('b')} first, then divide by {m('a')}.",
                body_ar=f"المعادلة تشبه ميزاناً متعادلاً: أي عملية تجريها على إحدى الكفتين يجب إجراؤها على الكفة الأخرى. نلغي الجمع بـ **الطرح**، ونلغي الطرح بـ **الجمع**، ونلغي الضرب بـ **القسمة**. وفي المعادلة {m('ax + b = c')} نطرح {m('b')} أولاً ثم نقسم على {m('a')}.",
                formula_en=dm("3x + 5 = 26 \\implies 3x = 21 \\implies x = \\frac{21}{3} = 7"),
                caption_ar="حل معادلة ذات خطوتين بالعمليات العكسية:",
                formula_math_ar=dm("3x + 5 = 26 \\implies 3x = 21 \\implies x = 7"),
                diagram_en=svg_balance_scales(2, 4, 1, 2),
            ),
        ],
        traps_en=[
            f"Adding before multiplying: in {m('6 + 4 \\times 5')}, compute {m('4 \\times 5 = 20')} first to get {m(26)}, NOT {m('10 \\times 5 = 50')}.",
            f"Translating '5 less than 3 times x' backwards as {m('5 - 3x')} instead of the correct {m('3x - 5')}.",
            f"Dividing before subtracting in {m('2x + 6 = 18')}: always undo {m('+6')} first ({m('2x = 12 \\implies x = 6')}).",
        ],
        traps_ar=[
            f"تنفيذ الجمع قبل الضرب: في {m('6 + 4 \\times 5')} نضرب أولاً {m('4 \\times 5 = 20')} ليكون الناتج {m(26)} وليس {m(50)}.",
            f"عكس ترتيب الطرح اللفظي: عبارة «أقل من ثلاثة أمثال س بمقدار 5» تُكتب {m('3x - 5')} وليس {m('5 - 3x')}.",
            f"القسمة على معامل المتغير قبل التخلص من الثابت المجموع في المعادلة {m('2x + 6 = 18')}.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-03-EX1",
                title_en="Order of Operations with Parentheses & Exponents",
                title_ar="ترتيب العمليات مع الأقواس والأسس",
                q_en=f"What is the value of the numerical expression {m('36 \\div (2 + 4) + 3^2 \\times 2')}?",
                q_ar=f"ما قيمة العبارة العددية {m('36 \\div (2 + 4) + 3^2 \\times 2')}؟",
                correct_val=24,
                distractors=[18, 30, 84],
                idea_en="Evaluate parentheses (2+4=6), then the power 3^2=9, then divide and multiply before adding.",
                steps_en=[
                    f"Parentheses first: {m('2 + 4 = 6')}.",
                    f"Exponent next: {m('3^2 = 9')}, giving {m('36 \\div 6 + 9 \\times 2')}.",
                    f"Divide and multiply: {m('6 + 18 = 24')}.",
                ],
                check_en=f"{m('36 \\div 6 = 6')} and {m('9 \\times 2 = 18')}; {m('6 + 18 = 24')}.",
                idea_ar="نحسب ما داخل القوس أولاً ثم الأس، ثم القسمة والضرب، وأخيراً الجمع.",
                steps_ar=[
                    f"نحسب القوس: {m('2 + 4 = 6')}.",
                    f"نحسب القوة: {m('3^2 = 9')} فتصبح العبارة {m('36 \\div 6 + 9 \\times 2')}.",
                    f"نجري القسمة والضرب ثم الجمع: {m('6 + 18 = 24')}.",
                ],
                check_ar=f"{m('6 + 18 = 24')} بالترتيب الصحيح للعمليات.",
                diagram_en=svg_number_strip(["36 ÷ (2+4)", "+", "3² × 2", "=", "?"]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-03-EX2",
                title_en="Evaluating a Two-Variable Expression",
                title_ar="حساب قيمة عبارة جبرية بمتغيرين",
                q_en=f"If {m('a = 7')} and {m('b = 5')}, what is the value of {m('4a - 3b + 2')}?",
                q_ar=f"إذا كانت {m('a = 7')} و{m('b = 5')}، فما قيمة العبارة الجبرية {m('4a - 3b + 2')}؟",
                correct_val=15,
                distractors=[11, 13, 25],
                idea_en="Substitute a = 7 and b = 5, compute 4(7) and 3(5), then subtract and add.",
                steps_en=[
                    f"Substitute: {m('4(7) - 3(5) + 2')}.",
                    f"Multiply first: {m('28 - 15 + 2')}.",
                    f"Work left to right: {m('13 + 2 = 15')}.",
                ],
                check_en=f"{m('28 + 2 - 15 = 30 - 15 = 15')}.",
                idea_ar="نعوّض عن المتغيرين ثم نضرب قبل الطرح والجمع.",
                steps_ar=[
                    f"بالتعويض: {m('4(7) - 3(5) + 2')}.",
                    f"نجري الضرب أولاً: {m('28 - 15 + 2')}.",
                    f"نطرح ثم نجمع: {m('13 + 2 = 15')}.",
                ],
                check_ar=f"{m('28 - 15 = 13')} ثم {m('13 + 2 = 15')}.",
                diagram_en=svg_function_machine("a=7, b=5", "4a − 3b = 13", "+ 2", "15"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-03-EX3",
                title_en="Finding the Missing Output in a Function Table",
                title_ar="إيجاد المخرجة المفقودة في جدول دالة",
                q_en=f"A STEM robotics club tracks sensor readings using the linear rule in the table: {m('(2 \\mapsto 5,\\; 4 \\mapsto 13,\\; 6 \\mapsto 21)')}. What is the output {m('y')} when {m('x = 9')}?",
                q_ar=f"يرصد نادي الروبوت قراءات حسّاس وفق القاعدة الخطية في الجدول: {m('(2 \\mapsto 5،\\; 4 \\mapsto 13،\\; 6 \\mapsto 21)')}. ما قيمة المخرجة {m('y')} عندما تكون المدخلة {m('x = 9')}؟",
                correct_val=33,
                distractors=[29, 31, 35],
                idea_en="When x increases by 2, y increases by 8, so the rule multiplies x by 4 and subtracts 3.",
                steps_en=[
                    f"Each step of {m('+2')} in {m('x')} adds {m('+8')} to {m('y')}, so the multiplier is {m('8 \\div 2 = 4')}.",
                    f"Test {m('x = 2')}: {m('4(2) - 3 = 5')}, confirming the rule {m('y = 4x - 3')}.",
                    f"For {m('x = 9')}: {m('y = 4(9) - 3 = 36 - 3 = 33')}.",
                ],
                check_en=f"Rule check on {m('x = 6')}: {m('4(6) - 3 = 21')}, matching the table.",
                idea_ar="كلما زادت س بمقدار 2 زادت ص بمقدار 8، أي أن القاعدة تضرب في 4 ثم تطرح 3.",
                steps_ar=[
                    f"معدل التغير هو {m('8 \\div 2 = 4')} لكل وحدة من {m('x')}.",
                    f"نجرّب عند {m('x = 2')}: {m('4(2) - 3 = 5')}، فالقاعدة هي {m('y = 4x - 3')}.",
                    f"عند {m('x = 9')}: {m('y = 4(9) - 3 = 36 - 3 = 33')}.",
                ],
                check_ar=f"التحقق عند {m('x = 6')}: {m('4(6) - 3 = 21')} وهو مطابق للجدول.",
                diagram_en=svg_nafes_function_table(
                    ["x", "2", "4", "6", "9"],
                    [["y", "5", "13", "21", "?"]],
                    highlight_cell=(0, 4),
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-03-EX4",
                title_en="Solving an Equation from a Ticket Purchase",
                title_ar="حل معادلة من مسألة تذاكر متحف",
                q_en=f"Faisal bought {m(3)} identical Diriyah museum tickets plus a {m(7)}-SAR guidebook for a total of {m(52)} SAR, modeled by {m('3x + 7 = 52')}. What is the price {m('x')} of one ticket in SAR?",
                q_ar=f"اشترى فيصل {m(3)} تذاكر متماثلة لمتحف الدرعية مع كتيّب إرشادي بسعر {m(7)} ريالات، فدفع إجمالاً {m(52)} ريالاً وفق المعادلة {m('3x + 7 = 52')}. ما سعر التذكرة الواحدة {m('x')} بالريال؟",
                correct_val=15,
                distractors=[13, 17, 20],
                idea_en="Subtract the 7-SAR guidebook first, then divide the remaining 45 SAR by 3 tickets.",
                steps_en=[
                    f"Subtract {m(7)} from both sides: {m('3x = 52 - 7 = 45')}.",
                    f"Divide both sides by {m(3)}: {m('x = 45 \\div 3 = 15')} SAR.",
                ],
                check_en=f"{m('3(15) + 7 = 45 + 7 = 52')} SAR.",
                idea_ar="نطرح سعر الكتيّب (7 ريالات) من الطرفين أولاً ثم نقسم الباقي (45 ريالاً) على 3.",
                steps_ar=[
                    f"نطرح {m(7)} من الطرفين: {m('3x = 52 - 7 = 45')}.",
                    f"نقسم الطرفين على {m(3)}: {m('x = 45 \\div 3 = 15')} ريالاً.",
                ],
                check_ar=f"التحقق بالتعويض: {m('3(15) + 7 = 45 + 7 = 52')} ريالاً.",
                diagram_en=svg_balance_scales(3, 6, 1, 2),
            ),
        ],
        blueprints=["G6-ALG-01", "G6-ALG-02", "G6-ALG-03", "G6-ALG-04"],
    )


def _lesson_2_4() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-04",
        level=LEVEL,
        unit_num="2.4",
        topic="Geometry",
        title_en="Metric Unit Conversions, Area of Triangles & Parallelograms & Prism Volume/Surface Area",
        title_ar="التحويل في النظام المتري، مساحة المثلث ومتوازي الأضلاع، وحجم ومساحة سطح المنشور الرباعي",
        summary_en="Conquer Grade 6 measurement and 3D geometry: convert metric length, mass, and capacity units, compute elapsed time across hours, find areas of triangles, parallelograms, and composite figures, calculate circle circumference, and find prism volume and surface area.",
        summary_ar="أتقن القياس والهندسة الفراغية للصف السادس الابتدائي: حوّل بين وحدات الطول والكتلة والسعة في النظام المتري، واحسب الزمن المنقضي، وأوجد مساحة المثلث ومتوازي الأضلاع والأشكال المركبة ومحيط الدائرة، واحسب حجم المنشور الرباعي ومساحة سطحه الكلية.",
        goals_en=[
            "Convert metric units (mm, cm, m, km; mg, g, kg; mL, L) and compute elapsed time across hour boundaries.",
            f"Calculate perimeter and area of parallelograms ({m('A = bh')}) and triangles ({m('A = \\frac{1}{2}bh')}).",
            f"Find areas of composite rectilinear figures and circumference of circles ({m('C = 2\\pi r = \\pi d')}).",
            f"Compute volume ({m('V = lwh')}) and total surface area ({m('SA = 2(lw + lh + wh)')}) of rectangular prisms.",
        ],
        goals_ar=[
            "التحويل بين وحدات النظام المتري (ملم، سم، م، كم؛ ملجم، جم، كجم؛ مل، ل) وحساب الزمن المنقضي.",
            f"حساب محيط ومساحة متوازي الأضلاع ({m('A = bh')}) والمثلث ({m('A = \\frac{1}{2}bh')}).",
            f"إيجاد مساحة الأشكال المركبة وحساب محيط الدائرة ({m('C = 2\\pi r = \\pi d')}).",
            f"حساب حجم المنشور الرباعي ({m('V = lwh')}) ومساحة سطحه الكلية ({m('SA = 2(lw + lh + wh)')}).",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Metric Unit Conversions & Elapsed Time",
                title_ar="١. التحويل في النظام المتري وحساب الزمن المنقضي",
                body_en=f"From a **larger** unit to a **smaller** unit, **multiply** ({m('1\\text{ km} = 1000\\text{ m}')}, {m('1\\text{ m} = 100\\text{ cm}')}, {m('1\\text{ cm} = 10\\text{ mm}')}, {m('1\\text{ kg} = 1000\\text{ g}')}, {m('1\\text{ L} = 1000\\text{ mL}')}). From **smaller** to **larger**, **divide**! For elapsed time across hours, bridge to the next whole hour first ({m('60\\text{ min} = 1\\text{ h}')}).",
                body_ar=f"للتحويل من وحدة **كبيرة** إلى وحدة **صغيرة** **نضرب** ({m('1\\text{ كم} = 1000\\text{ م}')}، {m('1\\text{ م} = 100\\text{ سم}')}، {m('1\\text{ سم} = 10\\text{ ملم}')}، {m('1\\text{ كجم} = 1000\\text{ جم}')}، {m('1\\text{ ل} = 1000\\text{ مل}')})، ومن صغيرة إلى كبيرة **نقسم**! ولحساب الزمن المنقضي نكمّل الدقائق إلى الساعة التالية ({m('60\\text{ دقيقة} = 1\\text{ ساعة}')}).",
                formula_en=dm("1\\text{ km} = 1000\\text{ m}, \\qquad 1\\text{ kg} = 1000\\text{ g}, \\qquad 1\\text{ L} = 1000\\text{ mL}"),
                caption_ar="علاقات التحويل الأساسية في النظام المتري:",
                formula_math_ar=dm("1\\text{ km} = 1000\\text{ m}, \\quad 1\\text{ kg} = 1000\\text{ g}, \\quad 1\\text{ L} = 1000\\text{ mL}"),
                diagram_en=svg_nafes_analog_clock(9, 40, "Start 09:40 -> +1 h 35 min"),
            ),
            nafes_concept(
                title_en="2. Area of Parallelograms, Triangles & Circle Circumference",
                title_ar="٢. مساحة متوازي الأضلاع والمثلث ومحيط الدائرة",
                body_en=f"Always multiply the base {m('b')} by the **perpendicular height** {m('h')} (at {m('90^\\circ')}, never the slant side!): {m('A_{\\text{para}} = bh')} and {m('A_{\\text{tri}} = \\frac{1}{2}bh')}. In any circle, the diameter is twice the radius ({m('d = 2r')}), and circumference is {m('C = \\pi d = 2\\pi r')} (using {m('\\pi \\approx \\frac{22}{7}')} when {m('r')} or {m('d')} is a multiple of {m(7)}).",
                body_ar=f"اضرب دائماً طول القاعدة {m('b')} في **الارتفاع العمودي** {m('h')} (الذي يصنع زاوية {m('90^\\circ')}، وليس الضلع المائل!): {m('A_{\\text{para}} = bh')} و{m('A_{\\text{tri}} = \\frac{1}{2}bh')}. وفي الدائرة القطر يساوي مثلي نصف القطر ({m('d = 2r')})، والمحيط {m('C = \\pi d = 2\\pi r')} (نستعمل {m('\\pi \\approx \\frac{22}{7}')} عندما يكون نصف القطر من مضاعفات {m(7)}).",
                formula_en=dm("A_{\\text{para}} = b \\cdot h, \\qquad A_{\\text{tri}} = \\frac{1}{2} b \\cdot h, \\qquad C = 2\\pi r = \\pi d"),
                caption_ar="قوانين المساحة ومحيط الدائرة:",
                formula_math_ar=dm("A_{\\text{para}} = bh, \\qquad A_{\\text{tri}} = \\frac{1}{2}bh, \\qquad C = 2\\pi r"),
                diagram_en=svg_g6_parallelogram("b = 12 cm", "h = 7 cm", "9 cm"),
            ),
            nafes_concept(
                title_en="3. Volume & Surface Area of a Rectangular Prism",
                title_ar="٣. حجم المنشور الرباعي ومساحة سطحه الكلية",
                body_en=f"**Volume** counts unit cubes filling the interior: {m('V = l \\times w \\times h')} (in cubic units {m('\\text{cm}^3')}). **Total surface area** adds the areas of all **6 rectangular faces** (top/bottom, front/back, left/right): {m('SA = 2(lw + lh + wh)')} (in square units {m('\\text{cm}^2')}).",
                body_ar=f"**الحجم** يقيس عدد الوحدات المكعبة التي تملأ المنشور من الداخل: {m('V = l \\times w \\times h')} (بالوحدات المكعبة {m('\\text{سم}^3')}). أما **المساحة الكلية للسطح** فتساوي مجموع مساحات **الأوجه الستة** المستطيلة: {m('SA = 2(lw + lh + wh)')} (بالوحدات المربعة {m('\\text{سم}^2')}).",
                formula_en=dm("V = l \\cdot w \\cdot h, \\qquad SA = 2(lw + lh + wh)"),
                caption_ar="حجم المنشور الرباعي ومساحة سطحه الكلية:",
                formula_math_ar=dm("V = lwh, \\qquad SA = 2(lw + lh + wh)"),
                diagram_en=svg_water_tank_3d("10 cm", "6 cm", "5 cm", 0.75),
            ),
        ],
        traps_en=[
            f"Multiplying the base by the **slant side** instead of the perpendicular height {m('h')}, or forgetting the factor {m('\\frac{1}{2}')} for a triangle.",
            f"Dividing by {m(100)} instead of {m(1000)} when converting {m('\\text{g} \\to \\text{kg}')} or {m('\\text{mL} \\to \\text{L}')} ({m('450\\text{ mL} = 0.45\\text{ L}')}, NOT {m('4.5\\text{ L}')}).",
            f"Forgetting to double the three face pairs in surface area: {m('lw + lh + wh')} is only **half** of the 6 faces!",
        ],
        traps_ar=[
            f"ضرب القاعدة في **الضلع المائل** بدلاً من الارتفاع العمودي {m('h')}، أو نسيان الضرب في {m('\\frac{1}{2}')} عند حساب مساحة المثلث.",
            f"القسمة على {m(100)} بدلاً من {m(1000)} عند التحويل من جرام إلى كيلوجرام أو من مللتر إلى لتر ({m('450\\text{ مل} = 0.45\\text{ ل}')}).",
            "جمع مساحات ثلاثة أوجه فقط ونسيان ضرب المجموع في 2 لحساب المساحة الكلية للأوجه الستة!",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-04-EX1",
                title_en="Subtracting Mixed Metric Lengths",
                title_ar="طرح أطوال بوحدات مترية مختلفة",
                q_en=f"A walking trail in Abha Park is {m('3.4')} kilometers long. After Tariq walks {m(850)} meters, how many **meters** remain?",
                q_ar=f"يبلغ طول مسار المشي في منتزه أبها {m('3.4')} كيلومتر. بعد أن مشى طارق مسافة {m(850)} متراً، كم **متراً** بقي عليه لإتمام المسار؟",
                correct_val=2550,
                distractors=[510, 2450, 2650],
                idea_en="Convert 3.4 km to meters by multiplying by 1000, then subtract 850 m.",
                steps_en=[
                    f"Convert kilometers to meters: {m('3.4 \\times 1000 = 3400')} m.",
                    f"Subtract the distance walked: {m('3400 - 850 = 2550')} m.",
                ],
                check_en=f"{m('2550 + 850 = 3400\\text{ m} = 3.4\\text{ km}')}.",
                idea_ar="نحوّل 3.4 كم إلى أمتار بالضرب في 1000 ثم نطرح 850 متراً.",
                steps_ar=[
                    f"نحوّل الكيلومترات إلى أمتار: {m('3.4 \\times 1000 = 3400')} م.",
                    f"نطرح المسافة المقطوعة: {m('3400 - 850 = 2550')} م.",
                ],
                check_ar=f"{m('2550 + 850 = 3400\\text{ م} = 3.4\\text{ كم}')}.",
                diagram_en=svg_fenceposts("850 m", "3.4 km = 3400 m"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-04-EX2",
                title_en="Area of a Triangular Sail",
                title_ar="مساحة شراع مثلث الشكل",
                q_en=f"A triangular boat sail in Yanbu has base {m(16)} m and perpendicular height {m(9)} m. What is its area in {m('\\text{m}^2')}?",
                q_ar=f"شراع قارب مثلث الشكل في ينبع طول قاعدته {m(16)} م وارتفاعه العمودي {m(9)} م. ما مساحته بالمتر المربع {m('\\text{م}^2')}؟",
                correct_val=72,
                distractors=[25, 64, 144],
                idea_en="Apply A = 1/2 * b * h = 1/2 * 16 * 9.",
                steps_en=[
                    f"Write the triangle area formula: {m('A = \\frac{1}{2} \\times b \\times h')}.",
                    f"Substitute {m('b = 16')} and {m('h = 9')}: {m('A = \\frac{1}{2} \\times 16 \\times 9 = 8 \\times 9 = 72\\text{ m}^2')}.",
                ],
                check_en=f"Half of the {m('16 \\times 9 = 144\\text{ m}^2')} bounding rectangle is {m('72\\text{ m}^2')}.",
                idea_ar="نطبّق قانون مساحة المثلث: نصف القاعدة في الارتفاع العمودي.",
                steps_ar=[
                    f"نكتب القانون: {m('A = \\frac{1}{2} \\times b \\times h')}.",
                    f"نعوّض {m('b = 16')} و{m('h = 9')}: {m('A = \\frac{1}{2} \\times 16 \\times 9 = 72\\text{ م}^2')}.",
                ],
                check_ar=f"مساحة المستطيل المحيط {m('16 \\times 9 = 144')} ونصفها {m(72)}.",
                diagram_en=svg_shaded_triangle_in_rect(16, 9, 0.55, "m"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-04-EX3",
                title_en="Circle Circumference Using π ≈ 22/7",
                title_ar="محيط الدائرة باستعمال ط ≈ 22/7",
                q_en=f"A circular fountain in Madinah has radius {m('r = 14')} m. Using {m('\\pi \\approx \\frac{22}{7}')}, what is its circumference in meters?",
                q_ar=f"نافورة دائرية في المدينة المنورة نصف قطرها {m('r = 14')} م. باستعمال {m('\\pi \\approx \\frac{22}{7}')}، ما محيطها بالأمتار؟",
                correct_val=88,
                distractors=[44, 154, 176],
                idea_en="Use C = 2 * pi * r with r = 14 and pi = 22/7.",
                steps_en=[
                    f"Write {m('C = 2 \\times \\pi \\times r = 2 \\times \\frac{22}{7} \\times 14')}.",
                    f"Cancel {m('14 \\div 7 = 2')}: {m('C = 2 \\times 22 \\times 2 = 88')} m.",
                ],
                check_en=f"Diameter {m('d = 28')} m, and {m('28 \\times \\frac{22}{7} = 4 \\times 22 = 88')} m.",
                idea_ar="نطبّق قانون المحيط مح = 2 × ط × نق مع نق = 14 وط = 22/7.",
                steps_ar=[
                    f"نكتب القانون: {m('C = 2 \\times \\frac{22}{7} \\times 14')}.",
                    f"نختصر {m('14 \\div 7 = 2')} فنجد {m('C = 2 \\times 22 \\times 2 = 88')} م.",
                ],
                check_ar=f"القطر {m('d = 28')} م، و{m('28 \\times \\frac{22}{7} = 88')} م.",
                diagram_en=svg_g6_circle("r = 14 m", is_diameter=False, caption="C = 2πr"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-04-EX4",
                title_en="Total Surface Area of a Gift Box",
                title_ar="المساحة الكلية لسطح صندوق هدايا",
                q_en=f"Lama wraps a rectangular gift box of length {m(8)} cm, width {m(5)} cm, and height {m(3)} cm. What is its total surface area in {m('\\text{cm}^2')}?",
                q_ar=f"تغلّف لمى صندوق هدايا على شكل منشور رباعي طوله {m(8)} سم وعرضه {m(5)} سم وارتفاعه {m(3)} سم. ما المساحة الكلية لسطحه بـ {m('\\text{سم}^2')}؟",
                correct_val=158,
                distractors=[79, 120, 148],
                idea_en="Compute lw + lh + wh = 40 + 24 + 15 = 79, then multiply by 2.",
                steps_en=[
                    f"Find the three distinct face areas: {m('lw = 8 \\times 5 = 40')}, {m('lh = 8 \\times 3 = 24')}, {m('wh = 5 \\times 3 = 15')}.",
                    f"Sum and double: {m('SA = 2(40 + 24 + 15) = 2 \\times 79 = 158\\text{ cm}^2')}.",
                ],
                check_en=f"Top+bottom {m(80)} + front+back {m(48)} + sides {m(30)} = {m(158)}.",
                idea_ar="نحسب مساحات الأوجه الثلاثة المختلفة (40 و24 و15) ثم نضرب مجموعها في 2.",
                steps_ar=[
                    f"مساحات الأوجه الثلاثة: {m('8 \\times 5 = 40')}، و{m('8 \\times 3 = 24')}، و{m('5 \\times 3 = 15')}.",
                    f"المساحة الكلية: {m('SA = 2(40 + 24 + 15) = 2 \\times 79 = 158\\text{ سم}^2')}.",
                ],
                check_ar=f"{m('80 + 48 + 30 = 158\\text{ سم}^2')}.",
                diagram_en=svg_water_tank_3d("8 cm", "5 cm", "3 cm", 0.0),
            ),
        ],
        blueprints=["G6-GEO-01", "G6-GEO-02", "G6-GEO-03", "G6-GEO-04"],
    )


def _lesson_2_5() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-05",
        level=LEVEL,
        unit_num="2.5",
        topic="Geometry",
        title_en="Angle Pairs, Triangle & Quadrilateral Angle Sums & Coordinate Plane Polygons",
        title_ar="العلاقات بين الزوايا، زوايا المثلث والشكل الرباعي، والمضلعات في المستوى الإحداثي",
        summary_en="Unlock geometric reasoning for Grade 6 Nafes: find unknown angles using complementary, supplementary, and vertical pairs, apply the 180° triangle sum and 360° quadrilateral sum, classify polygons, and measure or transform figures on the coordinate plane.",
        summary_ar="أتقن الاستدلال الهندسي للصف السادس في اختبار نافس: أوجد الزوايا المجهولة باستعمال التتام والتكامل والتقابل بالرأس، وطبّق مجموع زوايا المثلث (180°) والشكل الرباعي (360°)، وصنّف المضلعات، واحسب المسافات والتحويلات في المستوى الإحداثي.",
        goals_en=[
            f"Find unknown angles using complementary ({m('90^\\circ')}), supplementary ({m('180^\\circ')}), and vertically opposite relationships.",
            f"Classify triangles by sides and angles and solve for missing angles using the {m('180^\\circ')} sum.",
            f"Classify quadrilaterals (parallelogram, rectangle, rhombus, square, trapezoid) and use the {m('360^\\circ')} sum.",
            "Plot ordered pairs, find horizontal/vertical side lengths, and perform translations and reflections.",
        ],
        goals_ar=[
            f"إيجاد قياسات الزوايا المجهولة باستعمال الزوايا المتتامة ({m('90^\\circ')}) والمتكاملة ({m('180^\\circ')}) والمتقابلة بالرأس.",
            f"تصنيف المثلثات وفق أضلاعها وزواياها وإيجاد الزوايا المفقودة باستعمال مجموع {m('180^\\circ')}.",
            f"تصنيف الأشكال الرباعية (متوازي أضلاع، مستطيل، معين، مربع، شبه منحرف) واستعمال مجموع {m('360^\\circ')}.",
            "تمثيل الأزواج المرتبة وحساب المسافات الأفقية والرأسية وإجراء الانسحاب والانعكاس في المستوى الإحداثي.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Complementary, Supplementary & Vertically Opposite Angles",
                title_ar="١. الزوايا المتتامة والمتكاملة والمتقابلة بالرأس",
                body_en=f"Two angles are **complementary** if their sum is {m('90^\\circ')} (a right corner) and **supplementary** if their sum is {m('180^\\circ')} (a straight line). When two straight lines intersect, **vertically opposite angles** across the vertex are always **equal**!",
                body_ar=f"تكون الزاويتان **متتامتين** إذا كان مجموع قياسيهما {m('90^\\circ')} (زاوية قائمة)، وتكونان **متكاملتين** إذا كان مجموعهما {m('180^\\circ')} (خط مستقيم). وعند تقاطع مستقيمين فإن كل زاويتين **متقابلتين بالرأس** تكونان **متطابقتين** دائماً!",
                formula_en=dm("\\text{Comp: } \\alpha + \\beta = 90^\\circ, \\qquad \\text{Supp: } \\alpha + \\beta = 180^\\circ, \\qquad \\text{Vert: } \\alpha = \\beta"),
                caption_ar="ملخص علاقات أزواج الزوايا الأساسية:",
                formula_math_ar=dm("\\alpha + \\beta = 90^\\circ, \\qquad \\alpha + \\beta = 180^\\circ, \\qquad \\alpha = \\beta"),
                diagram_en=svg_g6_angle_pair("supp", "55°", "x = 125°", "Supplementary angles on a straight line"),
            ),
            nafes_concept(
                title_en="2. Triangle (180°) & Quadrilateral (360°) Interior Angle Sums",
                title_ar="٢. مجموع الزوايا الداخلية للمثلث (180°) والشكل الرباعي (360°)",
                body_en=f"The three interior angles of **every triangle** sum to {m('180^\\circ')} (an equilateral triangle has three {m('60^\\circ')} angles; an isosceles triangle has two equal base angles). Every **quadrilateral** splits into two triangles, so its four interior angles sum to {m('2 \\times 180^\\circ = 360^\\circ')}. Remember: a **square** is both a rectangle ({m(4)} right angles) and a rhombus ({m(4)} equal sides)!",
                body_ar=f"مجموع قياسات الزوايا الداخلية لأي **مثلث** يساوي {m('180^\\circ')} (المثلث المتطابق الأضلاع زواياه {m('60^\\circ')}، والمتطابق الضلعين زاويتا قاعدته متساويتان). وكل **شكل رباعي** ينقسم إلى مثلثين، فمجموع زواياه الأربع {m('360^\\circ')}. وتذكّر أن **المربع** هو مستطيل ومعين في آنٍ واحد!",
                formula_en=dm("\\angle A + \\angle B + \\angle C = 180^\\circ, \\qquad \\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ"),
                caption_ar="مجموع زوايا المثلث ومجموع زوايا الشكل الرباعي:",
                formula_math_ar=dm("\\sum_{\\triangle} = 180^\\circ, \\qquad \\sum_{\\square} = 360^\\circ"),
                diagram_en=svg_g6_quad_angles("110°", "85°", "x", "70°", "110° + 85° + 70° + x = 360°"),
            ),
            nafes_concept(
                title_en="3. Coordinate Plane Distances, Translations & Reflections",
                title_ar="٣. المسافات والانسحاب والانعكاس في المستوى الإحداثي",
                body_en=f"In an ordered pair {m('(x, y)')}, move **horizontally** to {m('x')} first, then **vertically** to {m('y')}. Along a horizontal segment (same {m('y')}), length is {m('|x_2 - x_1|')}; along a vertical segment (same {m('x')}), length is {m('|y_2 - y_1|')}. Reflecting across the **x-axis** flips the sign of {m('y')} ({m('(x, -y)')}); reflecting across the **y-axis** flips the sign of {m('x')} ({m('(-x, y)')}).",
                body_ar=f"في الزوج المرتب {m('(x, y)')} نتحرك **أفقياً** إلى {m('x')} أولاً ثم **رأسياً** إلى {m('y')}. المسافة الأفقية (عند ثبات {m('y')}) هي {m('|x_2 - x_1|')}، والرأسية هي {m('|y_2 - y_1|')}. الانعكاس حول **محور السينات** يعكس إشارة {m('y')} ليصبح {m('(x, -y)')}، والانعكاس حول **محور الصادات** يعكس إشارة {m('x')} ليصبح {m('(-x, y)')}.",
                formula_en=dm("T_{(a,b)}(x,y) = (x+a,\\; y+b), \\qquad R_{x\\text{-axis}}(x,y) = (x,\\; -y), \\qquad R_{y\\text{-axis}}(x,y) = (-x,\\; y)"),
                caption_ar="قواعد الانسحاب والانعكاس في المستوى الإحداثي:",
                formula_math_ar=dm("(x,y) \\xrightarrow{+(a,b)} (x+a, y+b), \\qquad R_x(x,y) = (x,-y)"),
                diagram_en=svg_nafes_coordinate_line(
                    [(1, 2, "A(1,2)"), (5, 2, "B(5,2)"), (5, 5, "C(5,5)"), (1, 5, "D(1,5)")],
                    max_coord=6,
                ),
            ),
        ],
        traps_en=[
            f"Confusing **complementary** ({m('90^\\circ')}) with **supplementary** ({m('180^\\circ')})—think **C** comes before **S** in the alphabet just as {m(90)} comes before {m(180)}!",
            f"Subtracting three quadrilateral angles from {m('180^\\circ')} instead of {m('360^\\circ')}.",
            f"Flipping the wrong coordinate during reflection: reflecting {m('(4, 3)')} across the **x-axis** gives {m('(4, -3)')}, NOT {m('(-4, 3)')}.",
        ],
        traps_ar=[
            f"الخلط بين **المتتامتين** ({m('90^\\circ')}) و**المتكاملتين** ({m('180^\\circ')})؛ تذكّر أن المتكاملتين تكملان خطاً مستقيماً قياسه {m('180^\\circ')}!",
            f"طرح زوايا الشكل الرباعي من {m('180^\\circ')} بدلاً من مجموع زوايا الرباعي {m('360^\\circ')}.",
            f"عكس الإحداثي الخطأ عند الانعكاس: انعكاس {m('(4, 3)')} حول محور {m('x')} هو {m('(4, -3)')} وليس {m('(-4, 3)')}.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-05-EX1",
                title_en="Supplementary Angles on a Straight Beam",
                title_ar="زاويتان متكاملتان على عارضة مستقيمة",
                q_en=f"In a solar panel frame in Tabuk, a support strut meets a straight horizontal beam at {m('68^\\circ')}. What is the supplementary angle {m('x')} in degrees?",
                q_ar=f"في إطار لوح شمسي بتبوك، تلتقي دعامة بعارضة أفقية مستقيمة بزاوية قياسها {m('68^\\circ')}. ما قياس الزاوية المكملة {m('x')} بالدرجات؟",
                correct_val=112,
                distractors=[22, 68, 122],
                idea_en="Angles on a straight line add up to 180°, so x = 180 - 68.",
                steps_en=[
                    f"Supplementary angles satisfy {m('x + 68^\\circ = 180^\\circ')}.",
                    f"Subtract: {m('x = 180^\\circ - 68^\\circ = 112^\\circ')}.",
                ],
                check_en=f"{m('112^\\circ + 68^\\circ = 180^\\circ')}.",
                idea_ar="مجموع الزاويتين المتجاورتين على مستقيم يساوي 180°.",
                steps_ar=[
                    f"نكتب العلاقة: {m('x + 68^\\circ = 180^\\circ')}.",
                    f"نطرح: {m('x = 180^\\circ - 68^\\circ = 112^\\circ')}.",
                ],
                check_ar=f"{m('112^\\circ + 68^\\circ = 180^\\circ')}.",
                diagram_en=svg_g6_angle_pair("supp", "68°", "x", "x + 68° = 180°"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-05-EX2",
                title_en="Base Angle of an Isosceles Triangle",
                title_ar="زاوية القاعدة في مثلث متطابق الضلعين",
                q_en=f"An isosceles triangular gable has vertex angle {m('46^\\circ')} and two equal base angles of {m('x^\\circ')} each. What is the value of {m('x')}?",
                q_ar=f"واجهة سقف على شكل مثلث متطابق الضلعين قياس زاوية رأسه {m('46^\\circ')} وزاويتا قاعدته متساويتان وقياس كلٍّ منهما {m('x^\\circ')}. ما قيمة {m('x')}؟",
                correct_val=67,
                distractors=[44, 62, 134],
                idea_en="Subtract 46° from 180°, then divide equally between the two base angles.",
                steps_en=[
                    f"Triangle sum: {m('46^\\circ + 2x = 180^\\circ')}.",
                    f"Subtract {m('46^\\circ')}: {m('2x = 134^\\circ \\implies x = 67^\\circ')}.",
                ],
                check_en=f"{m('46^\\circ + 67^\\circ + 67^\\circ = 180^\\circ')}.",
                idea_ar="نطرح زاوية الرأس 46° من 180° ثم نقسم الباقي بالتساوي على زاويتي القاعدة.",
                steps_ar=[
                    f"مجموع زوايا المثلث: {m('46^\\circ + 2x = 180^\\circ')}.",
                    f"إذن {m('2x = 134^\\circ')} ومنها {m('x = 67^\\circ')}.",
                ],
                check_ar=f"{m('46^\\circ + 67^\\circ + 67^\\circ = 180^\\circ')}.",
                diagram_en=svg_g6_triangle("46°", "x°", "x°", "Isosceles triangle"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-05-EX3",
                title_en="Missing Angle in a Quadrilateral",
                title_ar="الزاوية المجهولة في شكل رباعي",
                q_en=f"Three interior angles of a quadrilateral courtyard measure {m('95^\\circ')}, {m('110^\\circ')}, and {m('75^\\circ')}. What is the measure of the fourth angle in degrees?",
                q_ar=f"قياسات ثلاث زوايا داخلية لفناء رباعي الشكل هي {m('95^\\circ')} و{m('110^\\circ')} و{m('75^\\circ')}. ما قياس الزاوية الرابعة بالدرجات؟",
                correct_val=80,
                distractors=[70, 85, 90],
                idea_en="Add the three known angles and subtract their sum from 360°.",
                steps_en=[
                    f"Sum the known angles: {m('95^\\circ + 110^\\circ + 75^\\circ = 280^\\circ')}.",
                    f"Subtract from {m('360^\\circ')}: {m('360^\\circ - 280^\\circ = 80^\\circ')}.",
                ],
                check_en=f"{m('95 + 110 + 75 + 80 = 360')}.",
                idea_ar="نجمع الزوايا الثلاث المعلومة ثم نطرح المجموع من 360°.",
                steps_ar=[
                    f"مجموع الزوايا الثلاث: {m('95^\\circ + 110^\\circ + 75^\\circ = 280^\\circ')}.",
                    f"قياس الزاوية الرابعة: {m('360^\\circ - 280^\\circ = 80^\\circ')}.",
                ],
                check_ar=f"{m('280^\\circ + 80^\\circ = 360^\\circ')}.",
                diagram_en=svg_g6_quad_angles("95°", "110°", "x", "75°"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-05-EX4",
                title_en="Perimeter of a Coordinate Rectangle",
                title_ar="محيط مستطيل مرسوم في المستوى الإحداثي",
                q_en=f"A garden bed has vertices {m('A(1, 1)')}, {m('B(6, 1)')}, {m('C(6, 5)')}, and {m('D(1, 5)')} on a coordinate grid in meters. What is its perimeter in meters?",
                q_ar=f"حوض زراعي رؤوسه في المستوى الإحداثي بالأمتار هي {m('A(1, 1)')} و{m('B(6, 1)')} و{m('C(6, 5)')} و{m('D(1, 5)')}. ما محيطه بالأمتار؟",
                correct_val=18,
                distractors=[9, 20, 24],
                idea_en="Find horizontal width |6 - 1| = 5 and vertical height |5 - 1| = 4, then double their sum.",
                steps_en=[
                    f"Horizontal length {m('AB = 6 - 1 = 5')} m; vertical width {m('BC = 5 - 1 = 4')} m.",
                    f"Perimeter {m('P = 2(5 + 4) = 18')} m.",
                ],
                check_en=f"Area would be {m('5 \\times 4 = 20')}, while perimeter is {m('5+4+5+4 = 18')} m.",
                idea_ar="نحسب الطول الأفقي (6 − 1 = 5) والعرض الرأسي (5 − 1 = 4) ثم نطبّق قانون المحيط.",
                steps_ar=[
                    f"الطول الأفقي {m('AB = 6 - 1 = 5')} م، والعرض الرأسي {m('BC = 5 - 1 = 4')} م.",
                    f"المحيط {m('P = 2(5 + 4) = 18')} م.",
                ],
                check_ar=f"مجموع الأضلاع الأربعة: {m('5 + 4 + 5 + 4 = 18')} م.",
                diagram_en=svg_nafes_coordinate_line(
                    [(1, 1, "A(1,1)"), (6, 1, "B(6,1)"), (6, 5, "C(6,5)"), (1, 5, "D(1,5)")],
                    max_coord=6,
                ),
            ),
        ],
        blueprints=["G6-GEO-05", "G6-GEO-06", "G6-GEO-07", "G6-GEO-08"],
    )


def _lesson_2_6() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L2-06",
        level=LEVEL,
        unit_num="2.6",
        topic="Data & Probability",
        title_en="Mean, Median, Mode, Range, Pie Charts & Sample-Space Probability",
        title_ar="المتوسط الحسابي والوسيط والمنوال والمدى، القطاعات الدائرية، وفضاء العينة والاحتمال",
        summary_en="Shine on ETEC Nafes statistics and probability questions: compute arithmetic mean (including missing values), compare median, mode, range, and outlier effects, read percentages and central angles in circle pie charts, and find probabilities and sample-space counts.",
        summary_ar="تميّز في أسئلة الإحصاء والاحتمالات في اختبار نافس: احسب المتوسط الحسابي (بما في ذلك إيجاد القيمة المفقودة)، وقارن الوسيط والمنوال والمدى وأثر القيم المتطرفة، واقرأ النسب المئوية والزوايا المركزية في القطاعات الدائرية، واحسب الاحتمال النظري وفضاء العينة.",
        goals_en=[
            "Calculate the arithmetic mean and range, and work backwards from a target mean to find a missing value.",
            "Order data to find the median and mode, and determine how an outlier affects mean vs median.",
            f"Interpret circle pie charts using both {m('100\\%')} totals and {m('360^\\circ')} central angles.",
            f"Compute theoretical probability {m('P(E)')}, complementary probability {m('1 - P(E)')}, and sample-space sizes ({m('m \\times n')}).",
        ],
        goals_ar=[
            "حساب المتوسط الحسابي والمدى، والعمل عكسياً من متوسط معلوم لإيجاد قيمة مفقودة.",
            "ترتيب البيانات لإيجاد الوسيط والمنوال، وتحديد أثر القيمة المتطرفة في المتوسط مقارنةً بالوسيط.",
            f"تفسير القطاعات الدائرية باستعمال مجموع النسب ({m('100\\%')}) ومجموع الزوايا المركزية ({m('360^\\circ')}).",
            f"حساب الاحتمال النظري {m('P(E)')} واحتمال الحادثة المتممة {m('1 - P(E)')} وعدد نواتج فضاء العينة ({m('m \\times n')}).",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Arithmetic Mean, Target Sum & Range",
                title_ar="١. المتوسط الحسابي والمجموع الكلي والمدى",
                body_en=f"The **mean** (average) redistributes data equally: {m('\\text{Mean} = \\frac{\\text{Sum of values}}{n}')}. Flipping this gives the golden Nafes shortcut: **Total Sum = Mean × Count** ({m('S = \\bar{x} \\cdot n')}), which finds any missing test score instantly! The **range** measures spread: {m('\\text{Range} = \\text{Max} - \\text{Min}')}.",
                body_ar=f"**المتوسط الحسابي** يساوي مجموع البيانات مقسوماً على عددها {m('n')}. ومن ذلك نستنتج القاعدة الذهبية لإيجاد أي درجة مفقودة: **المجموع الكلي = المتوسط × عدد القيم**! أما **المدى** فيقيس انتشار البيانات ويساوي **أكبر قيمة − أصغر قيمة**.",
                formula_en=dm("\\text{Mean} = \\frac{\\sum x_i}{n} \\iff \\sum x_i = n \\times \\text{Mean}, \\qquad \\text{Range} = x_{\\max} - x_{\\min}"),
                caption_ar="قانون المتوسط الحسابي والمدى:",
                formula_math_ar=dm("\\text{Mean} = \\frac{\\sum x_i}{n}, \\qquad \\text{Range} = x_{\\max} - x_{\\min}"),
                diagram_en=svg_bar_chart([("Quiz 1", 16, "16"), ("Quiz 2", 19, "19"), ("Quiz 3", 15, "15"), ("Quiz 4", 18, "?")], y_max=20),
            ),
            nafes_concept(
                title_en="2. Median, Mode & Outlier Effects",
                title_ar="٢. الوسيط والمنوال وأثر القيم المتطرفة",
                body_en=f"Always **sort the data from least to greatest first**! The **median** is the middle value (or the average of the two middle values when {m('n')} is even). The **mode** is the most frequent value. An extreme **outlier** pulls the **mean** strongly toward it, while the **median** barely changes!",
                body_ar=f"**رتّب البيانات تصاعدياً أولاً دائماً**! **الوسيط** هو القيمة التي تتوسط البيانات المرتبة (أو متوسط القيمتين الأوسطتين إذا كان عدد البيانات زوجياً)، و**المنوال** هو القيمة الأكثر تكراراً. وتذكّر أن **القيمة المتطرفة** تسحب **المتوسط الحسابي** نحوها بشدة بينما يبقى **الوسيط** شبه ثابت!",
                formula_en=dm("\\{12, 14, 15, 17, 42\\}: \\quad \\text{Median} = 15, \\quad \\text{Mean} = \\frac{100}{5} = 20"),
                caption_ar="مقارنة تأثر المتوسط الحسابي والوسيط بالقيمة المتطرفة 42:",
                formula_math_ar=dm("\\text{Median} = 15, \\qquad \\text{Mean} = 20"),
                diagram_en=svg_nafes_box_plot(12, 13, 15, 19, 42, "Dataset with High Outlier 42"),
            ),
            nafes_concept(
                title_en="3. Circle Pie Charts, Probability & Counting Principle",
                title_ar="٣. القطاعات الدائرية والاحتمال ومبدأ العد الأساسي",
                body_en=f"In a **pie chart**, all sectors add up to {m('100\\%')} of the data and {m('360^\\circ')} around the center ({m('25\\% = 90^\\circ')}, {m('50\\% = 180^\\circ')}). Theoretical probability is {m('P(E) = \\frac{\\text{favorable}}{\\text{total}}')}, and {m('P(\\text{not } E) = 1 - P(E)')}. By the **Fundamental Counting Principle**, {m('m')} choices followed by {m('n')} choices yield {m('m \\times n')} total outcomes.",
                body_ar=f"في **القطاعات الدائرية** مجموع النسب {m('100\\%')} ومجموع الزوايا المركزية {m('360^\\circ')} ({m('25\\% = 90^\\circ')} و{m('50\\% = 180^\\circ')}). الاحتمال النظري هو {m('P(E) = \\frac{\\text{عدد النواتج المواتية}}{\\text{العدد الكلي}}')}، واحتمال المتممة {m('1 - P(E)')}. وبموجب **مبدأ العد الأساسي** فإن {m('m')} خيارات متبوعة بـ {m('n')} خيارات تعطي {m('m \\times n')} ناتجاً ممكناً.",
                formula_en=dm("\\theta = \\frac{p}{100} \\times 360^\\circ, \\qquad P(\\text{not } E) = 1 - P(E), \\qquad N_{\\text{total}} = m \\times n"),
                caption_ar="زاوية القطاع الدائري والحدث المتمم ومبدأ العد:",
                formula_math_ar=dm("\\theta = \\frac{p}{100} \\times 360^\\circ, \\qquad P(\\overline{E}) = 1 - P(E)"),
                diagram_en=svg_nafes_pie_chart(
                    [("Football 40%", 40), ("Swimming 25%", 25), ("Reading 20%", 20), ("Robotics 15%", 15)],
                    "Grade 6 Activity Survey",
                ),
            ),
        ],
        traps_en=[
            "Grabbing the middle number of an **unsorted** list as the median—always sort from smallest to largest first!",
            f"Confusing percent ({m('100\\%')}) with central degrees ({m('360^\\circ')}): {m('25\\%')} of a circle is {m('90^\\circ')}, NOT {m('25^\\circ')}.",
            f"Adding {m('m + n')} instead of multiplying {m('m \\times n')} when counting outfit, menu, or coin-and-die combinations.",
        ],
        traps_ar=[
            "اختيار الرقم الأوسط في قائمة **غير مرتبة** على أنه الوسيط؛ يجب الترتيب التصاعدي أولاً في كل مرة!",
            f"الخلط بين النسبة المئوية ({m('100\\%')}) ومجموع زوايا الدائرة ({m('360^\\circ')}): قطاع نسبته {m('25\\%')} زاويته {m('90^\\circ')} وليست {m('25^\\circ')}.",
            f"جمع عدد الخيارات {m('m + n')} بدلاً من ضربها {m('m \\times n')} في مسائل مبدأ العد الأساسي.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L2-06-EX1",
                title_en="Finding a Missing Score from a Target Mean",
                title_ar="إيجاد الدرجة المفقودة بمعلومية المتوسط الحسابي",
                q_en=f"Yasser scored {m(17)}, {m(19)}, and {m(15)} on his first three math quizzes. What score must he earn on the fourth quiz so that his mean across all {m(4)} quizzes is {m(18)}?",
                q_ar=f"حصل ياسر على الدرجات {m(17)} و{m(19)} و{m(15)} في أول ثلاثة اختبارات قصيرة. ما الدرجة التي يجب أن يحصل عليها في الاختبار الرابع ليصبح متوسط درجاته في الاختبارات الـ {m(4)} مساوياً لـ {m(18)}؟",
                correct_val=21,
                distractors=[17, 18, 20],
                idea_en="Multiply the target mean 18 by 4 quizzes to get the required sum 72, then subtract the three known scores.",
                steps_en=[
                    f"Required total sum: {m('4 \\times 18 = 72')}.",
                    f"Sum of first three quizzes: {m('17 + 19 + 15 = 51')}.",
                    f"Fourth quiz score: {m('72 - 51 = 21')}.",
                ],
                check_en=f"{m('(17 + 19 + 15 + 21) \\div 4 = 72 \\div 4 = 18')}.",
                idea_ar="اضرب المتوسط المطلوب (18) في عدد الاختبارات (4) لإيجاد المجموع الكلي (72)، ثم اطرح مجموع الدرجات الثلاث.",
                steps_ar=[
                    f"المجموع الكلي المطلوب: {m('4 \\times 18 = 72')}.",
                    f"مجموع أول ثلاث درجات: {m('17 + 19 + 15 = 51')}.",
                    f"الدرجة الرابعة المطلوبة: {m('72 - 51 = 21')}.",
                ],
                check_ar=f"{m('(51 + 21) \\div 4 = 72 \\div 4 = 18')}.",
                diagram_en=svg_bar_chart([("Q1", 17, "17"), ("Q2", 19, "19"), ("Q3", 15, "15"), ("Q4", 21, "?")], y_max=24),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-06-EX2",
                title_en="Median of an Even Number of Values",
                title_ar="الوسيط لعدد زوجي من القيم",
                q_en=f"The daily high temperatures (°C) in Hail over {m(6)} days were {m('24, 19, 27, 21, 25, 20')}. What is the median temperature?",
                q_ar=f"سُجّلت درجات الحرارة العظمى (°س) في حائل خلال {m(6)} أيام كما يلي: {m('24، 19، 27، 21، 25، 20')}. ما الوسيط لدرجات الحرارة؟",
                correct_val="22.5",
                distractors=["21", "23", "24"],
                idea_en="Sort all 6 temperatures from least to greatest and average the 3rd and 4th values.",
                steps_en=[
                    f"Sort in ascending order: {m('19, 20, 21, 24, 25, 27')}.",
                    f"The two middle values are {m(21)} and {m(24)}.",
                    f"Median = {m('\\frac{21 + 24}{2} = \\frac{45}{2} = 22.5')}.",
                ],
                check_en=f"Three values ({m('19, 20, 21')}) lie below {m('22.5')} and three ({m('24, 25, 27')}) lie above it.",
                idea_ar="نرتب القيم الست تصاعدياً ثم نأخذ متوسط القيمتين الثالثة والرابعة.",
                steps_ar=[
                    f"الترتيب التصاعدي: {m('19, 20, 21, 24, 25, 27')}.",
                    f"القيمتان الأوسطتان هما {m(21)} و{m(24)}.",
                    f"الوسيط = {m('(21 + 24) \\div 2 = 22.5')}.",
                ],
                check_ar=f"ثلاث قيم أصغر من {m('22.5')} وثلاث قيم أكبر منها.",
                diagram_en=svg_number_strip(["19", "20", "21", "24", "25", "27"]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-06-EX3",
                title_en="Reading Quantities from a Pie Chart",
                title_ar="إيجاد العدد من قطاع دائري",
                q_en=f"A survey of {m(200)} Grade 6 students in Dammam shows {m('35\\%')} chose Science Club, {m('25\\%')} Robotics, {m('25\\%')} Sports, and {m('15\\%')} Art. How many students chose Science Club?",
                q_ar=f"في استبانة شملت {m(200)} طالب من الصف السادس في الدمام، اختار {m('35\\%')} نادي العلوم، و{m('25\\%')} الروبوت، و{m('25\\%')} الرياضة، و{m('15\\%')} الفنون. كم طالباً اختار نادي العلوم؟",
                correct_val=70,
                distractors=[35, 50, 65],
                idea_en="Multiply 35% (35/100) by the 200 surveyed students.",
                steps_en=[
                    f"Write {m('35\\%')} of {m(200)} as {m('\\frac{35}{100} \\times 200')}.",
                    f"Simplify {m('200 \\div 100 = 2')}, then {m('35 \\times 2 = 70')} students.",
                ],
                check_en=f"Counts are {m('70 + 50 + 50 + 30 = 200')} students.",
                idea_ar="نضرب النسبة 35/100 في العدد الكلي للطلاب وهو 200.",
                steps_ar=[
                    f"نحسب {m('\\frac{35}{100} \\times 200')}.",
                    f"بالاختصار {m('35 \\times 2 = 70')} طالباً.",
                ],
                check_ar=f"مجموع الفئات الأربع: {m('70 + 50 + 50 + 30 = 200')} طالب.",
                diagram_en=svg_nafes_pie_chart(
                    [("Science 35%", 35), ("Robotics 25%", 25), ("Sports 25%", 25), ("Art 15%", 15)],
                    "200 Grade 6 Students",
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L2-06-EX4",
                title_en="Complementary Spinner Probability",
                title_ar="احتمال الحادثة المتممة على القرص الدوّار",
                q_en=f"An {m(8)}-sector spinner is labeled with {m('A, A, B, B, B, C, C, D')}. What is the probability in simplest form that the pointer does **NOT** land on {m('A')}?",
                q_ar=f"قُسّم قرص دوّار إلى {m(8)} قطاعات متطابقة كُتبت عليها الحروف {m('A, A, B, B, B, C, C, D')}. ما احتمال **عدم** وقوف المؤشر على الحرف {m('A')} في أبسط صورة؟",
                correct_val=Fraction(3, 4),
                distractors=[Fraction(1, 4), Fraction(3, 8), Fraction(5, 8)],
                idea_en="Out of 8 equal sectors, 2 are A, so 8 - 2 = 6 sectors are NOT A; simplify 6/8.",
                steps_en=[
                    f"Count sectors NOT labeled {m('A')}: {m('8 - 2 = 6')} sectors.",
                    f"Form the probability: {m('P(\\text{not } A) = \\frac{6}{8}')}.",
                    f"Divide top and bottom by {m(2)}: {m('\\frac{3}{4}')}.",
                ],
                check_en=f"{m('P(A) + P(\\text{not } A) = \\frac{1}{4} + \\frac{3}{4} = 1')}.",
                idea_ar="من بين 8 قطاعات متساوية يوجد قطاعان للحرف A، إذن 6 قطاعات ليست A، ونبسّط 6/8.",
                steps_ar=[
                    f"عدد القطاعات التي لا تحمل {m('A')} هو {m('8 - 2 = 6')}.",
                    f"الاحتمال هو {m('\\frac{6}{8}')}، وبالقسمة على {m(2)} يصبح {m('\\frac{3}{4}')}.",
                ],
                check_ar=f"{m('\\frac{1}{4} + \\frac{3}{4} = 1')}.",
                diagram_en=svg_nafes_spinner(["A", "A", "B", "B", "B", "C", "C", "D"], "P(not A) = ?"),
            ),
        ],
        blueprints=["G6-DAT-01", "G6-DAT-02", "G6-DAT-03", "G6-DAT-04"],
    )


def get_grade6_lessons() -> list[dict]:
    return [
        _lesson_2_1(),
        _lesson_2_2(),
        _lesson_2_3(),
        _lesson_2_4(),
        _lesson_2_5(),
        _lesson_2_6(),
    ]
