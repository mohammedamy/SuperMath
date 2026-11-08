"""Tier 3 Olympiad Study Academy lessons (Grades 11–12): OLYM-L3-01 through OLYM-L3-06."""

import math
from fractions import Fraction

from olympiad_common import (
    BLUE,
    DARK,
    GREEN,
    MUTED,
    OLYMPIAD_LEVELS,
    ORANGE,
    PAL,
    RED,
    SHADE,
    STROKE,
    WATER,
    _nlabel,
    dm,
    m,
    make_olympiad_lesson,
    olym_concept,
    olym_worked_example,
    svg_olym_bipartite_graph,
    svg_olym_board_coloring,
    svg_olym_cyclic_ptolemy,
    svg_olym_divisibility_lattice,
    svg_olym_func_mapping,
    svg_olym_incircle_excircle,
    svg_olym_inequality_curve,
    svg_olym_nine_point_euler,
    svg_olym_pigeonhole_boxes,
    svg_olym_radical_axis,
    svg_olym_spiral_homothety,
    svg_olym_tetrahedron_3d,
    wrap_svg,
)

LEVEL_T3 = OLYMPIAD_LEVELS[2]


# ==============================================================================
# Tier 3 Bespoke Senior-Olympiad SVG Helpers
# ==============================================================================

def _svg_roots_of_unity(n: int = 7, top_note: str = "ω = exp(2πi/n)", bot_note: str = "") -> str:
    """Complex unit circle showing n-th roots of unity and chords from z = 1."""
    ox, oy, R = 160, 92, 56
    pts = [
        (ox + R * math.cos(2 * math.pi * k / n), oy - R * math.sin(2 * math.pi * k / n))
        for k in range(n)
    ]
    parts = [
        f'<line x1="84" y1="{oy}" x2="236" y2="{oy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        f'<line x1="{ox}" y1="26" x2="{ox}" y2="158" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        f'<circle cx="{ox}" cy="{oy}" r="{R}" fill="{WATER}" fill-opacity="0.30" stroke="{BLUE}" stroke-width="2"/>',
    ]
    x0, y0 = pts[0]
    for k in range(1, n):
        xk, yk = pts[k]
        parts.append(
            f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{xk:.1f}" y2="{yk:.1f}" stroke="{ORANGE}" stroke-width="1.4" stroke-opacity="0.8"/>'
        )
    for k, (xk, yk) in enumerate(pts):
        fc = RED if k == 0 else BLUE
        parts.append(f'<circle cx="{xk:.1f}" cy="{yk:.1f}" r="3.6" fill="{fc}"/>')
    parts.append(_nlabel(x0 + 13, y0 + 4, "1", size=10, color=RED))
    if n >= 3:
        parts.append(_nlabel(pts[1][0] + 10, pts[1][1] - 6, "ω", size=10, color=BLUE))
        parts.append(_nlabel(pts[2][0] - 8, pts[2][1] - 8, "ω²", size=10, color=BLUE))
    if top_note:
        parts.append(_nlabel(62, 22, top_note, size=10, color=GREEN))
    if bot_note:
        parts.append(_nlabel(256, 162, bot_note, size=11, color=RED if "?" in bot_note else DARK))
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Roots of unity on the unit circle")


def _svg_vieta_descent(step1: str = "(a, b)", step2: str = "(b, a')", stop_lbl: str = "a' = 0") -> str:
    """Root-flipping descent chain for Vieta jumping."""
    boxes = [
        (58, 50, step1, PAL["blue_fill"]),
        (160, 92, step2, PAL["amber_fill"]),
        (262, 134, stop_lbl, "#bbf7d0"),
    ]
    parts = [
        _nlabel(160, 20, "Vieta Root Flip: a' = kb − a", size=11, color=GREEN),
        f'<line x1="88" y1="60" x2="130" y2="82" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="190" y1="102" x2="232" y2="124" stroke="{RED}" stroke-width="2"/>',
    ]
    for x, y, lbl, fc in boxes:
        bw = max(68, int(len(lbl) * 7.2 + 18))
        parts.append(
            f'<rect x="{x - bw/2:.1f}" y="{y - 15}" width="{bw}" height="30" rx="8" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>'
        )
        parts.append(_nlabel(x, y + 4, lbl, size=11, color=RED if "?" in lbl else DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=370, title="Vieta jumping minimal descent")


def _svg_tangent_support(x0_lbl: str = "x₀", curve_lbl: str = "f(x)", line_lbl: str = "mx + c") -> str:
    """Algebraic supporting-line bound f(x) >= mx + c via (x - x0)^2 Q(x) >= 0."""
    # Parabola y_math = 0.008*(x - 150)^2 + 36 mapped to SVG y = 166 - y_math
    pts = [(x, 166 - (0.0075 * (x - 148) ** 2 + 34)) for x in range(56, 265, 8)]
    d_curve = "M " + " L ".join(f"{x},{y:.1f}" for x, y in pts)
    # Touch point at x0 = 172: y0_math = 0.0075*24^2 + 34 = 38.32, slope_math = 0.015*24 = 0.36
    x0 = 172
    y0_m = 0.0075 * (x0 - 148) ** 2 + 34
    sl = 0.015 * (x0 - 148)
    xl, xr = 62, 262
    yl = 166 - (y0_m + sl * (xl - x0))
    yr = 166 - (y0_m + sl * (xr - x0))
    y0 = 166 - y0_m
    parts = [
        f'<line x1="44" y1="152" x2="280" y2="152" stroke="{MUTED}" stroke-width="1.4"/>',
        f'<path d="{d_curve}" fill="none" stroke="{BLUE}" stroke-width="2.3"/>',
        f'<line x1="{xl}" y1="{yl:.1f}" x2="{xr}" y2="{yr:.1f}" stroke="{RED}" stroke-width="2" stroke-dasharray="5,3"/>',
        f'<line x1="{x0}" y1="{y0:.1f}" x2="{x0}" y2="152" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="3,3"/>',
        f'<circle cx="{x0}" cy="{y0:.1f}" r="4" fill="{RED}"/>',
        _nlabel(x0, 165, x0_lbl, size=11, color=GREEN),
        _nlabel(84, 52, curve_lbl, size=11, color=BLUE),
        _nlabel(248, yr + 15, line_lbl, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Supporting line inequality")


def _svg_pascal_hexagon(note: str = "Pascal Line: X, Y, Z") -> str:
    """Inscribed hexagon on a circle with collinear Pascal line indicator."""
    ox, oy, R = 156, 86, 56
    angs = [165, 112, 48, 345, 278, 214]
    pts = [(ox + R * math.cos(math.radians(a)), oy - R * math.sin(math.radians(a))) for a in angs]
    lbls = ["A", "B", "C", "D", "E", "F"]
    parts = [
        _nlabel(160, 16, note, size=11, color=RED if "?" in note else GREEN),
        f'<circle cx="{ox}" cy="{oy}" r="{R}" fill="{WATER}" fill-opacity="0.28" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{STROKE}" stroke-width="1.7"/>',
        f'<line x1="48" y1="156" x2="272" y2="156" stroke="{RED}" stroke-width="2.1" stroke-dasharray="5,3"/>',
    ]
    for (x, y), lb in zip(pts, lbls):
        dx = 11 * math.cos(math.radians(angs[lbls.index(lb)]))
        dy = -11 * math.sin(math.radians(angs[lbls.index(lb)]))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{DARK}"/>')
        parts.append(_nlabel(x + dx, y + dy, lb, size=9, color=DARK))
    for px, pl in [(88, "X"), (160, "Y"), (232, "Z")]:
        parts.append(f'<circle cx="{px}" cy="156" r="3.5" fill="{RED}"/>')
        parts.append(_nlabel(px, 170, pl, size=10, color=RED))
    return wrap_svg("".join(parts), w=320, h=178, disp_w=370, title="Projective Pascal configuration")


def _svg_convex_hull_set(note: str = "Convex Hull", ask_lbl: str = "") -> str:
    """Convex hull polygon around planar points for Helly and extremal geometry."""
    hull = [(64, 134), (92, 46), (194, 34), (258, 92), (218, 148)]
    inner = [(126, 88), (168, 76), (154, 116), (196, 104)]
    poly = " ".join(f"{x},{y}" for x, y in hull)
    parts = [
        _nlabel(160, 18, note, size=11, color=GREEN),
        f'<polygon points="{poly}" fill="{SHADE}" fill-opacity="0.48" stroke="{BLUE}" stroke-width="2.1"/>',
    ]
    for x, y in hull:
        parts.append(f'<circle cx="{x}" cy="{y}" r="3.8" fill="{BLUE}"/>')
    for x, y in inner:
        parts.append(f'<circle cx="{x}" cy="{y}" r="3.4" fill="{DARK}"/>')
    if ask_lbl:
        parts.append(_nlabel(256, 158, ask_lbl, size=11, color=RED if "?" in ask_lbl else DARK))
    return wrap_svg("".join(parts), w=320, h=174, disp_w=370, title="Convex hull configuration")


def _svg_turan_clusters(sizes: tuple[int, ...] = (3, 3, 2), note: str = "Turán T(n, r)") -> str:
    """Complete multipartite Turán graph clusters with cross-part edges."""
    k = len(sizes)
    xs = [68 + i * (184 / max(1, k - 1)) for i in range(k)]
    clusters = []
    for i, sz in enumerate(sizes):
        ys = [64 + j * (64 / max(1, sz - 1)) for j in range(sz)] if sz > 1 else [96]
        clusters.append([(xs[i], y) for y in ys])
    parts = [_nlabel(160, 20, note, size=11, color=RED if "?" in note else GREEN)]
    for a in range(k):
        for b in range(a + 1, k):
            for x1, y1 in clusters[a]:
                for x2, y2 in clusters[b]:
                    parts.append(
                        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{BLUE}" stroke-width="1.1" stroke-opacity="0.45"/>'
                    )
    for i, cl in enumerate(clusters):
        parts.append(
            f'<rect x="{xs[i]-18:.1f}" y="46" width="36" height="100" rx="14" fill="{WATER}" fill-opacity="0.45" stroke="{STROKE}" stroke-width="1.5"/>'
        )
        for x, y in cl:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{DARK}"/>')
        parts.append(_nlabel(xs[i], 162, f"V{i+1}", size=10, color=DARK))
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Turan multipartite extremal graph")


# ==============================================================================
# OLYM-L3-01: Number Theory (LTE, Multiplicative Orders, QR, Vieta Jumping)
# ==============================================================================

def _lesson_l3_01() -> dict:
    concepts = [
        olym_concept(
            title_en="Lifting the Exponent Lemma (LTE)",
            title_ar="توطئة رفع الأس (LTE)",
            body_en=(
                f"For a prime {m('p')} and integer {m('N \\neq 0')}, let {m('v_p(N)')} denote the highest exponent {m('e')} such that {m('p^e \\mid N')}. "
                f"When {m('p')} is an **odd prime** with {m('p \\nmid x')}, {m('p \\nmid y')}, and {m('p \\mid (x - y)')}, the Lifting the Exponent Lemma gives "
                f"{m('v_p(x^n - y^n) = v_p(x - y) + v_p(n)')} for every positive integer {m('n')}; similarly, for odd {m('n')} with {m('p \\mid (x + y)')}, "
                f"{m('v_p(x^n + y^n) = v_p(x + y) + v_p(n)')}. "
                f"For the critical prime {m('p = 2')} with odd integers {m('x, y')} and **even** {m('n')}, one extra factor of {m('2')} appears from {m('x^2 - y^2')}: "
                f"{m('v_2(x^n - y^n) = v_2(x - y) + v_2(x + y) + v_2(n) - 1')}."
            ),
            body_ar=(
                f"لعدد أولي {m('p')} وعدد صحيح {m('N \\neq 0')}، نرمز بالرمز {m('v_p(N)')} إلى أكبر أس {m('e')} يحقق {m('p^e \\mid N')}. "
                f"إذا كان {m('p')} **عدداً أولياً فردياً** بحيث {m('p \\nmid x')} و{m('p \\nmid y')} و{m('p \\mid (x - y)')}، فإن توطئة رفع الأس تعطي "
                f"{m('v_p(x^n - y^n) = v_p(x - y) + v_p(n)')} لكل عدد صحيح موجب {m('n')}؛ وبالمثل إذا كان {m('n')} فردياً و{m('p \\mid (x + y)')} فإن "
                f"{m('v_p(x^n + y^n) = v_p(x + y) + v_p(n)')}. "
                f"أما في الحالة الحاسمة {m('p = 2')} لعددين فرديين {m('x, y')} وأس **زوجي** {m('n')}، فإن الصيغة الصحيحة هي "
                f"{m('v_2(x^n - y^n) = v_2(x - y) + v_2(x + y) + v_2(n) - 1')}."
            ),
            formula_en=dm(
                r"v_p(x^n - y^n) = v_p(x - y) + v_p(n)\;\;(p\text{ odd}), \qquad "
                r"v_2(x^n - y^n) = v_2(x-y) + v_2(x+y) + v_2(n) - 1\;\;(2 \mid n)"
            ),
            caption_ar="صيغتا توطئة رفع الأس للأعداد الأولية الفردية وللحالة الزوجية عند p = 2:",
            formula_math_ar=dm(
                r"v_p(x^n - y^n) = v_p(x - y) + v_p(n), \qquad "
                r"v_2(x^n - y^n) = v_2(x-y) + v_2(x+y) + v_2(n) - 1"
            ),
            diagram_en=svg_olym_divisibility_lattice("xⁿ − yⁿ", "v_p(x − y)", "v_p(n)", "v_p = sum"),
        ),
        olym_concept(
            title_en="Multiplicative Orders, Primitive Roots & Sum-of-Squares Primes",
            title_ar="الرتبة الضربية والجذور البدائية وقواسم مجموع مربعين",
            body_en=(
                f"For {m('\\gcd(a, m) = 1')}, the **multiplicative order** {m('\\operatorname{ord}_m(a)')} is the least positive integer {m('d')} with "
                f"{m('a^d \\equiv 1 \\pmod{m}')}. Division with remainder proves the master equivalence {m('a^n \\equiv 1 \\pmod{m} \\iff \\operatorname{ord}_m(a) \\mid n')}. "
                f"For a prime {m('p')}, {m('\\mathbb{Z}_p^\\times')} is cyclic and possesses a **primitive root** {m('g')} of order {m('p - 1')}, while Euler's criterion states "
                f"{m('a^{(p-1)/2} \\equiv \\left(\\frac{a}{p}\\right) \\pmod{p}')}. Setting {m('a = -1')} shows {m('-1')} is a square mod {m('p')} if and only if {m('p = 2')} or "
                f"{m('p \\equiv 1 \\pmod{4}')}. Consequently, if a prime {m('q \\equiv 3 \\pmod{4}')} divides {m('x^2 + y^2')}, then {m('q \\mid x')} and {m('q \\mid y')}."
            ),
            body_ar=(
                f"عندما يكون {m('\\gcd(a, m) = 1')}، فإن **الرتبة الضربية** {m('\\operatorname{ord}_m(a)')} هي أصغر عدد صحيح موجب {m('d')} يحقق "
                f"{m('a^d \\equiv 1 \\pmod{m}')}. وتثبت خوارزمية القسمة التكافؤ الجوهري {m('a^n \\equiv 1 \\pmod{m} \\iff \\operatorname{ord}_m(a) \\mid n')}. "
                f"ولكل عدد أولي {m('p')} تكون الزمرة {m('\\mathbb{Z}_p^\\times')} دورية وتمتلك **جذراً بدائياً** {m('g')} رتبته {m('p - 1')}، وينص معيار أويلر على أن "
                f"{m('a^{(p-1)/2} \\equiv \\left(\\frac{a}{p}\\right) \\pmod{p}')}. وعند وضع {m('a = -1')} نجد أن {m('-1')} بواقي تربيعية بمقياس {m('p')} إذا وفقط إذا كان "
                f"{m('p = 2')} أو {m('p \\equiv 1 \\pmod{4}')}؛ ولذلك إذا قسم عدد أولي {m('q \\equiv 3 \\pmod{4}')} المقدار {m('x^2 + y^2')} فإنه يقسم كلاً من {m('x')} و{m('y')}."
            ),
            formula_en=dm(
                r"a^n \equiv 1 \pmod{p} \iff \operatorname{ord}_p(a) \mid \gcd(n, p-1), \qquad "
                r"q \equiv 3 \pmod{4},\; q \mid (x^2+y^2) \implies q \mid x,\; q \mid y"
            ),
            caption_ar="قانون قابلية القسمة للرتبة الضربية وتوطئة القاسم الأولي لمجموع مربعين:",
            formula_math_ar=dm(
                r"a^n \equiv 1 \pmod{p} \iff \operatorname{ord}_p(a) \mid \gcd(n, p-1), \qquad "
                r"q \equiv 3 \pmod{4},\; q \mid (x^2+y^2) \implies q \mid x,\; q \mid y"
            ),
            diagram_en=_svg_roots_of_unity(6, "ord_p(g) = p − 1", "g^k mod p"),
        ),
        olym_concept(
            title_en="Vieta Jumping & Minimal-Solution Descent",
            title_ar="قفز فييتا والنزول بالحل الأصغري",
            body_en=(
                f"To classify integer values of symmetric rational expressions such as {m('k = \\frac{a^2 + b^2 + c}{ab}')} over positive integers {m('a, b')}, "
                f"fix {m('k')} and select a positive integer solution {m('(a, b)')} with {m('a \\ge b \\ge 1')} that **minimizes** {m('a + b')}. "
                f"Rewrite the relation as a monic quadratic in {m('x')}: {m('x^2 - kbx + (b^2 + c) = 0')}, which has root {m('x_1 = a')}. "
                f"Vieta's formulas produce a second root {m('a\' = kb - a = \\frac{b^2 + c}{a}')}. The sum formula guarantees {m('a\' \\in \\mathbb{Z}')}, "
                f"while the product formula controls its sign and size; showing {m('0 < a\' < a')} contradicts minimality, forcing boundary cases like {m('a = b')} or {m('a\' \\le 0')}."
            ),
            body_ar=(
                f"لتحديد القيم الصحيحة الممكنة لعبارات كسرية متماثلة مثل {m('k = \\frac{a^2 + b^2 + c}{ab}')} على الأعداد الصحيحة الموجبة {m('a, b')}، "
                f"نثبّت {m('k')} ونختار حلاً صحيحاً موجباً {m('(a, b)')} يحقق {m('a \\ge b \\ge 1')} ويجعل المجموع {m('a + b')} **أصغر ما يمكن**. "
                f"نعيد كتابة المعادلة على صورة تربيعية في {m('x')}: {m('x^2 - kbx + (b^2 + c) = 0')} التي أحد جذريها {m('x_1 = a')}. "
                f"تعطي علاقات فييتا الجذر الثاني {m('a\' = kb - a = \\frac{b^2 + c}{a}')}؛ فتضمن صيغة المجموع كون {m('a\' \\in \\mathbb{Z}')}، "
                f"بينما تضبط صيغة الجداء إشارته وحجمه، فإذا نتج {m('0 < a\' < a')} حصلنا على تناقض مع الأصغرية مما يحصر الحل في الحالات الحدية."
            ),
            formula_en=dm(
                r"x^2 - kbx + (b^2 + c) = 0 \implies a' = kb - a = \frac{b^2 + c}{a}"
            ),
            caption_ar="معادلة قلب الجذر في تقنية قفز فييتا:",
            formula_math_ar=dm(
                r"x^2 - kbx + (b^2 + c) = 0 \implies a' = kb - a = \frac{b^2 + c}{a}"
            ),
            diagram_en=_svg_vieta_descent("(a, b) min", "(b, a')", "a = b or a' ≤ 0"),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-01-EX1",
            title_en="Combined Odd-Prime and 2-adic LTE",
            title_ar="الدمج بين توطئة رفع الأس لـ p فردي وحالة p = 2",
            q_en=(
                f"Let {m('N = 19^{56} - 5^{56}')}. Denote by {m('v_p(N)')} the largest integer {m('e')} such that {m('p^e \\mid N')}. "
                f"What is the value of {m('v_2(N) + v_7(N)')}?"
            ),
            q_ar=(
                f"ليكن {m('N = 19^{56} - 5^{56}')}، ولنرمز بالرمز {m('v_p(N)')} إلى أكبر عدد صحيح {m('e')} يحقق {m('p^e \\mid N')}. "
                f"ما قيمة {m('v_2(N) + v_7(N)')}؟"
            ),
            correct_val=8,
            distractors=[5, 7, 9, 10],
            idea_en=(
                f"Apply odd-prime LTE at {m('p = 7')} since {m('19 - 5 = 14')} is divisible by {m('7')}, and apply the even-exponent {m('p = 2')} LTE formula to the odd bases {m('19')} and {m('5')}."
            ),
            steps_en=[
                f"For {m('p = 7')}: {m('7 \\nmid 19')}, {m('7 \\nmid 5')}, and {m('19 - 5 = 14')} has {m('v_7(14) = 1')}. Since {m('56 = 7 \\cdot 8')}, odd-prime LTE gives {m('v_7(N) = v_7(14) + v_7(56) = 1 + 1 = 2')}.",
                f"For {m('p = 2')}: {m('19')} and {m('5')} are odd and {m('n = 56')} is even, so {m('v_2(N) = v_2(19 - 5) + v_2(19 + 5) + v_2(56) - 1')}.",
                f"Compute each valuation: {m('v_2(14) = 1')}, {m('v_2(24) = 3')}, and {m('v_2(56) = 3')}, giving {m('v_2(N) = 1 + 3 + 3 - 1 = 6')}.",
                f"Add the two exponents: {m('v_2(N) + v_7(N) = 6 + 2 = 8')}.",
            ],
            check_en=(
                f"Writing {m('19^{56} - 5^{56} = (19^2)^28 - (5^2)^28')} with {m('19^2 - 5^2 = 336 = 2^4 \\cdot 3 \\cdot 7')} confirms {m('v_2(N) = 4 + v_2(28) = 6')} and {m('v_7(N) = 1 + v_7(28) = 2')}."
            ),
            idea_ar=(
                f"نطبّق توطئة رفع الأس الفردية عند {m('p = 7')} لأن {m('19 - 5 = 14')} يقبل القسمة على {m('7')}، ونطبّق صيغة {m('p = 2')} للأس الزوجي على الأساسين الفرديين {m('19')} و{m('5')}."
            ),
            steps_ar=[
                f"عند {m('p = 7')}: لدينا {m('7 \\nmid 19')} و{m('7 \\nmid 5')} و{m('v_7(19 - 5) = v_7(14) = 1')}. وبما أن {m('56 = 7 \\cdot 8')} فإن {m('v_7(N) = 1 + 1 = 2')}.",
                f"عند {m('p = 2')}: الأساسان {m('19')} و{m('5')} فرديان والأس {m('56')} زوجي، لذا {m('v_2(N) = v_2(19 - 5) + v_2(19 + 5) + v_2(56) - 1')}.",
                f"نحسب التقييمات: {m('v_2(14) = 1')} و{m('v_2(24) = 3')} و{m('v_2(56) = 3')}، فيكون {m('v_2(N) = 1 + 3 + 3 - 1 = 6')}.",
                f"نجمع القيمتين: {m('v_2(N) + v_7(N) = 6 + 2 = 8')}.",
            ],
            check_ar=(
                f"بكتابة {m('(19^2)^{28} - (5^2)^{28}')} حيث {m('19^2 - 5^2 = 336 = 2^4 \\cdot 3 \\cdot 7')} نتحقق مباشرة أن {m('v_2(N) = 4 + v_2(28) = 6')} و{m('v_7(N) = 1 + v_7(28) = 2')}."
            ),
            diagram_en=svg_olym_divisibility_lattice("19⁵⁶ − 5⁵⁶", "v₂(N)", "v₇(N)", "v₂ + v₇ = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-01-EX2",
            title_en="Prime Divisors of Mersenne Numbers via Multiplicative Order",
            title_ar="العوامل الأولية لأعداد ميرسين عبر الرتبة الضربية",
            q_en=(
                f"Use multiplicative orders modulo {m('p')} to factor {m('M_{11} = 2^{11} - 1')}. "
                f"What is the sum of all distinct prime divisors of {m('2^{11} - 1')}?"
            ),
            q_ar=(
                f"باستخدام الرتبة الضربية بمقياس {m('p')} لتحليل العدد {m('M_{11} = 2^{11} - 1')}، "
                f"ما مجموع جميع القواسم الأولية المختلفة للعدد {m('2^{11} - 1')}؟"
            ),
            correct_val=112,
            distractors=[23, 89, 90, 134],
            idea_en=(
                f"Any prime {m('p \\mid (2^{11} - 1)')} must satisfy {m('\\operatorname{ord}_p(2) = 11')}, which forces {m('11 \\mid (p - 1)')} and therefore {m('p \\equiv 1 \\pmod{22}')}."
            ),
            steps_en=[
                f"If a prime {m('p')} divides {m('2^{11} - 1 = 2047')}, then {m('p')} is odd and {m('2^{11} \\equiv 1 \\pmod{p}')}, so {m('\\operatorname{ord}_p(2) \\mid 11')}.",
                f"Since {m('2^1 \\not\\equiv 1 \\pmod{p}')} and {m('11')} is prime, {m('\\operatorname{ord}_p(2) = 11')}. By Fermat's Little Theorem, {m('11 \\mid (p - 1)')}; since {m('p')} is odd, {m('p \\equiv 1 \\pmod{22}')}.",
                f"The smallest candidate up to {m('\\sqrt{2047} < 46')} is {m('p = 23')} (the next is {m('45')}, composite). Indeed {m('2047 = 23 \\times 89')}.",
                f"Since {m('89')} has no prime factor {m('\\le \\sqrt{89} < 10')}, both {m('23')} and {m('89')} are prime, giving sum {m('23 + 89 = 112')}.",
            ],
            check_en=(
                f"Also {m('23 \\equiv -1 \\pmod{8}')} implies {m('2')} is a quadratic residue mod {m('23')}, so Euler's criterion immediately gives {m('2^{11} \\equiv 1 \\pmod{23}')}; and {m('89 = 4 \\cdot 22 + 1 \\equiv 1 \\pmod{22}')}."
            ),
            idea_ar=(
                f"كل عامل أولي {m('p \\mid (2^{11} - 1)')} يحقق {m('\\operatorname{ord}_p(2) = 11')}، مما يفرض {m('11 \\mid (p - 1)')} وبالتالي {m('p \\equiv 1 \\pmod{22}')}."
            ),
            steps_ar=[
                f"إذا قسم عدد أولي {m('p')} العدد {m('2^{11} - 1 = 2047')} فإن {m('p')} فردي و{m('2^{11} \\equiv 1 \\pmod{p}')}، أي {m('\\operatorname{ord}_p(2) \\mid 11')}.",
                f"بما أن {m('11')} أولي و{m('2 \\not\\equiv 1 \\pmod{p}')}، فإن {m('\\operatorname{ord}_p(2) = 11')}. ومن مبرهنة فيرما الصغرى {m('11 \\mid (p - 1)')}، ولكون {m('p')} فردياً يكون {m('p \\equiv 1 \\pmod{22}')}.",
                f"المرشح الأولي الوحيد تحت {m('\\sqrt{2047} < 46')} هو {m('p = 23')} (إذ {m('45')} غير أولي)، وبالقسمة نجد {m('2047 = 23 \\times 89')}.",
                f"العدد {m('89')} أولي (لا يقبل القسمة على {m('2, 3, 5, 7')})، فيكون مجموع العوامل الأولية {m('23 + 89 = 112')}.",
            ],
            check_ar=(
                f"بما أن {m('23 \\equiv -1 \\pmod{8}')} فإن {m('2')} باقٍ تربيعي بمقياس {m('23')}، فيعطي معيار أويلر فوراً {m('2^{11} \\equiv 1 \\pmod{23}')}، كما أن {m('89 = 4 \\cdot 22 + 1')}."
            ),
            diagram_en=_svg_roots_of_unity(11, "ord_p(2) = 11", "Σ p = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-01-EX3",
            title_en="Counting Sum-of-Squares Representations via 3 (mod 4) Primes",
            title_ar="عدّ تمثيلات مجموع مربعين عبر الأعداد الأولية من النمط 3 (mod 4)",
            q_en=(
                f"How many ordered pairs of integers {m('(x, y)')} (allowing zero and negative integers) satisfy "
                f"{m('x^2 + y^2 = 3^4 \\cdot 7^2 \\cdot 25')}?"
            ),
            q_ar=(
                f"كم زوجاً مرتباً من الأعداد الصحيحة {m('(x, y)')} (بما في ذلك الصفر والأعداد السالبة) يحقق المعادلة "
                f"{m('x^2 + y^2 = 3^4 \\cdot 7^2 \\cdot 25')}؟"
            ),
            correct_val=12,
            distractors=[4, 8, 16, 24],
            idea_en=(
                f"Strip out the {m('3 \\pmod 4')} primes {m('3')} and {m('7')}: every representation must have {m('3^2 \\cdot 7 \\mid x')} and {m('3^2 \\cdot 7 \\mid y')}, reducing the count to {m('u^2 + v^2 = 25')}."
            ),
            steps_en=[
                f"Both {m('3')} and {m('7')} are primes congruent to {m('3 \\pmod{4}')}. Whenever such a prime {m('q')} divides {m('x^2 + y^2')}, we must have {m('q \\mid x')} and {m('q \\mid y')}.",
                f"Applying this descent twice for {m('q = 3')} and once for {m('q = 7')} forces {m('x = 63u')} and {m('y = 63v')} for some integers {m('u, v')}.",
                f"Cancelling {m('63^2 = 3^4 \\cdot 7^2')} from both sides gives the equivalent equation {m('u^2 + v^2 = 25')}.",
                f"The integer solutions to {m('u^2 + v^2 = 25')} are {m('(0, \\pm 5)')}, {m('(\\pm 5, 0)')}, {m('(\\pm 3, \\pm 4)')}, and {m('(\\pm 4, \\pm 3)')}, yielding {m('2 + 2 + 4 + 4 = 12')} ordered pairs.",
            ],
            check_en=(
                f"Testing {m('u^2 \\in \\{0, 1, 4, 9, 16, 25\\}')} confirms {m('25 - u^2')} is a square only at {m('u^2 \\in \\{0, 9, 16, 25\\}')}, giving {m('2 + 4 + 4 + 2 = 12')} pairs."
            ),
            idea_ar=(
                f"نتخلص من العوامل الأولية من النمط {m('3 \\pmod{4}')} وهما {m('3')} و{m('7')}: يجب أن يقسم {m('3^2 \\cdot 7 = 63')} كلاً من {m('x')} و{m('y')}، فتختزل المسألة إلى {m('u^2 + v^2 = 25')}."
            ),
            steps_ar=[
                f"العددان {m('3')} و{m('7')} أوليان يطابقان {m('3 \\pmod{4}')}؛ وكلما قسم مثل هذا العدد الأولي {m('x^2 + y^2')} وجب أن يقسم {m('x')} و{m('y')} معاً.",
                f"بتكرار الاختزال مرتين للعدد {m('3')} ومرة للعدد {m('7')} نستنتج أن {m('x = 63u')} و{m('y = 63v')} لعددين صحيحين {m('u, v')}.",
                f"بقسمة الطرفين على {m('63^2 = 3^4 \\cdot 7^2')} نحصل على المعادلة المكافئة {m('u^2 + v^2 = 25')}.",
                f"حلول {m('u^2 + v^2 = 25')} الصحيحة هي {m('(0, \\pm 5)')} و{m('(\\pm 5, 0)')} و{m('(\\pm 3, \\pm 4)')} و{m('(\\pm 4, \\pm 3)')}، وعددها {m('2 + 2 + 4 + 4 = 12')} زوجاً مرتباً.",
            ],
            check_ar=(
                f"بتجربة {m('u^2 \\in \\{0, 1, 4, 9, 16, 25\\}')} نجد أن {m('25 - u^2')} مربع كامل فقط عند {m('u^2 \\in \\{0, 9, 16, 25\\}')}، مما يؤكد وجود {m('12')} حلاً بالضبط."
            ),
            diagram_en=svg_olym_divisibility_lattice("x² + y²", "63 | x", "63 | y", "#(x, y) = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-01-EX4",
            title_en="Pinning Down a Diophantine Quotient by Vieta Jumping",
            title_ar="تحديد خارج قسمة ديوفانتي عبر قفز فييتا",
            q_en=(
                f"Find the unique integer {m('k')} for which there exist positive integers {m('a')} and {m('b')} satisfying "
                f"{m('a^2 + b^2 + 2 = k a b')}."
            ),
            q_ar=(
                f"أوجد العدد الصحيح الوحيد {m('k')} الذي يوجد من أجله عددان صحيحان موجبان {m('a')} و{m('b')} يحققان "
                f"{m('a^2 + b^2 + 2 = k a b')}."
            ),
            correct_val=4,
            distractors=[3, 5, 6, 7],
            idea_en=(
                f"Choose a positive integer solution {m('(a, b)')} with {m('a \\ge b \\ge 1')} minimizing {m('a + b')}, and flip the larger root {m('a')} of {m('x^2 - kbx + (b^2 + 2) = 0')}."
            ),
            steps_en=[
                f"Fix a valid integer {m('k')} and pick positive integers {m('a \\ge b \\ge 1')} minimizing {m('a + b')}.",
                f"If {m('a = b')}, then {m('2a^2 + 2 = ka^2 \\implies (k - 2)a^2 = 2')}, which forces {m('a = 1')} and {m('k = 4')}.",
                f"If {m('a > b = 1')}, then {m('a^2 + 3 = ka \\implies a \\mid 3')}, forcing {m('a = 3')} and again {m('k = (9 + 1 + 2)/3 = 4')}.",
                f"If {m('a > b \\ge 2')}, then {m('a \\ge b + 1')} gives {m('a^2 \\ge b^2 + 2b + 1 > b^2 + 2')}. The second root {m('a\' = kb - a = \\frac{b^2 + 2}{a}')} is a positive integer with {m('a\' < a')}, contradicting the minimality of {m('a + b')}. Thus {m('k = 4')} uniquely.",
            ],
            check_en=(
                f"At {m('k = 4')}, pairs {m('(1, 1)')}, {m('(3, 1)')}, and {m('(11, 3)')} all satisfy {m('a^2 + b^2 + 2 = 4ab')} (e.g., {m('121 + 9 + 2 = 132 = 4 \\cdot 33')})."
            ),
            idea_ar=(
                f"نختار حلاً صحيحاً موجباً {m('(a, b)')} يحقق {m('a \\ge b \\ge 1')} بأصغر مجموع {m('a + b')}، ثم نقلب الجذر الأكبر {m('a')} للمعادلة {m('x^2 - kbx + (b^2 + 2) = 0')}."
            ),
            steps_ar=[
                f"نثبّت {m('k')} ونختار حلاً موجباً {m('a \\ge b \\ge 1')} يجعل {m('a + b')} أصغرياً.",
                f"إذا كان {m('a = b')} فإن {m('2a^2 + 2 = ka^2 \\implies (k - 2)a^2 = 2')}، ومنه {m('a = 1')} و{m('k = 4')}.",
                f"وإذا كان {m('a > b = 1')} فإن {m('a^2 + 3 = ka \\implies a \\mid 3')}، فيكون {m('a = 3')} ومنه أيضاً {m('k = 12/3 = 4')}.",
                f"أما إذا كان {m('a > b \\ge 2')} فإن {m('a \\ge b + 1 \\implies a^2 > b^2 + 2')}، فيكون الجذر الثاني {m('a\' = kb - a = \\frac{b^2 + 2}{a}')} عدداً صحيحاً موجباً أصغر من {m('a')}، مناقضاً أصغرية {m('a + b')}. إذن {m('k = 4')} وحيد.",
            ],
            check_ar=(
                f"عند {m('k = 4')} تحقق الأزواج {m('(1, 1)')} و{m('(3, 1)')} و{m('(11, 3)')} المعادلة فعلاً (مثلاً {m('11^2 + 3^2 + 2 = 132 = 4 \\cdot 11 \\cdot 3')})."
            ),
            diagram_en=_svg_vieta_descent("a²+b²+2 = kab", "a' = (b²+2)/a", "k = ?"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-01",
        level=LEVEL_T3,
        unit_num="3.1",
        topic="Number Theory",
        title_en="p-adic Valuations, Multiplicative Orders & Vieta Jumping",
        title_ar="التقييمات الأسية لـ p، والرتب الضربية، وقفز فييتا",
        summary_en=(
            "Master Senior Olympiad Number Theory: compute exact prime-power valuations via Lifting the Exponent (LTE), "
            "constrain prime divisors using multiplicative orders and quadratic residues, and solve symmetric Diophantine equations by Vieta jumping."
        ),
        summary_ar=(
            "أتقن نظرية الأعداد للأولمبياد المتقدم: حساب التقييمات الأسية الدقيقة عبر توطئة رفع الأس (LTE)، "
            "وحصر القواسم الأولية بالرتب الضربية والبواقي التربيعية، وحل المعادلات الديوفانتية المتماثلة بتقنية قفز فييتا."
        ),
        goals_en=[
            f"Compute exact prime-power valuations {m('v_p(x^n \\pm y^n)')} using both odd-prime LTE and the {m('p = 2')} even-exponent formula.",
            f"Use {m('\\operatorname{ord}_p(a) \\mid \\gcd(n, p - 1)')} and primitive roots to restrict prime divisors of exponential expressions.",
            f"Apply Euler's criterion and the {m('q \\equiv 3 \\pmod{4}')} sum-of-squares lemma to descend on Diophantine equations.",
            f"Execute Vieta root flipping on minimal positive solutions of quadratic Diophantine equations.",
        ],
        goals_ar=[
            f"حساب التقييمات الأسية الدقيقة {m('v_p(x^n \\pm y^n)')} باستخدام توطئة رفع الأس للأعداد الفردية وصيغة {m('p = 2')} للأسس الزوجية.",
            f"توظيف علاقة {m('\\operatorname{ord}_p(a) \\mid \\gcd(n, p - 1)')} والجذور البدائية لتقييد العوامل الأولية للعبارات الأسية.",
            f"تطبيق معيار أويلر وتوطئة العوامل الأولية من النمط {m('q \\equiv 3 \\pmod{4}')} في مسائل مجموع مربعين.",
            f"تنفيذ قفز فييتا بقلب الجذور على الحل الموجب الأصغري للمعادلات الديوفانتية التربيعية.",
        ],
        concepts=concepts,
        traps_en=[
            f"Applying the odd-prime formula {m('v_2(x^n - y^n) = v_2(x - y) + v_2(n)')} when {m('p = 2')}, {m('n')} is even, and {m('x - y \\equiv 2 \\pmod{4}')}: you must use {m('v_2(x - y) + v_2(x + y) + v_2(n) - 1')}.",
            f"Invoking LTE or {m('\\operatorname{ord}_p(a)')} before factoring out {m('\\gcd(x, y)^n')} when {m('p')} divides {m('x')} or {m('y')}.",
            f"Assuming the flipped Vieta root {m('a\' = kb - a')} is strictly positive without analyzing {m('a\' \\le 0')} or {m('a = b')}, which are the exact stopping cases that determine {m('k')}.",
        ],
        traps_ar=[
            f"تطبيق صيغة الأعداد الفردية {m('v_2(x^n - y^n) = v_2(x - y) + v_2(n)')} عند {m('p = 2')} مع أس زوجي {m('n')} عندما {m('4 \\nmid (x - y)')}؛ والصواب استخدام {m('v_2(x - y) + v_2(x + y) + v_2(n) - 1')}.",
            f"استدعاء LTE أو الرتبة الضربية {m('\\operatorname{ord}_p(a)')} قبل إخراج العامل المشترك {m('\\gcd(x, y)^n')} عندما يقسم {m('p')} أحد الأساسين.",
            f"افتراض أن الجذر المقلوب {m('a\' = kb - a')} موجب قطعا دون فحص الحالتين الحديتين {m('a\' \\le 0')} أو {m('a = b')} اللتين تحددان قيمة {m('k')}.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_nt_lte_lifting_exponent",
            "olym_t3_nt_orders_primitive_roots",
            "olym_t3_nt_quadratic_residues_sumsq",
            "olym_t3_nt_vieta_jumping_descent",
        ],
    )


# ==============================================================================
# OLYM-L3-02: Algebra (Cyclotomic Polys, Roots of Unity, Func Eqs, Recurrences)
# ==============================================================================

def _lesson_l3_02() -> dict:
    concepts = [
        olym_concept(
            title_en="Eisenstein's Criterion & Cyclotomic Polynomials",
            title_ar="معيار أيزنشتاين وكثيرات الحدود الدويرية",
            body_en=(
                f"By Gauss's Lemma, a primitive polynomial in {m('\\mathbb{Z}[x]')} is irreducible over {m('\\mathbb{Q}')} iff it cannot split into nonconstant factors in {m('\\mathbb{Z}[x]')}. "
                f"**Eisenstein's Criterion** guarantees irreducibility of {m('P(x) = a_n x^n + \\dots + a_0')} whenever some prime {m('p')} satisfies "
                f"{m('p \\nmid a_n')}, {m('p \\mid a_i')} for {m('0 \\le i < n')}, and {m('p^2 \\nmid a_0')} (often applied after a shift {m('x = y + c')}). "
                f"The {m('n')}-th **cyclotomic polynomial** {m('\\Phi_n(x)')} collects all {m('\\varphi(n)')} primitive {m('n')}-th roots of unity, is monic and irreducible in {m('\\mathbb{Z}[x]')}, and satisfies {m('x^n - 1 = \\prod_{d \\mid n} \\Phi_d(x)')}."
            ),
            body_ar=(
                f"بموجب توطئة غاوس، تكون كثيرة الحدود البدائية في {m('\\mathbb{Z}[x]')} غير قابلة للتحليل على {m('\\mathbb{Q}')} إذا وفقط إذا تعذر تحليلها إلى عاملين غير ثابتين في {m('\\mathbb{Z}[x]')}. "
                f"ويضمن **معيار أيزنشتاين** عدم قابلية تحليل {m('P(x) = a_n x^n + \\dots + a_0')} إذا وُجد عدد أولي {m('p')} يحقق "
                f"{m('p \\nmid a_n')} و{m('p \\mid a_i')} لكل {m('0 \\le i < n')} و{m('p^2 \\nmid a_0')} (وغالباً ما يُطبَّق بعد إزاحة {m('x = y + c')}). "
                f"أما **كثيرة الحدود الدويرية** {m('\\Phi_n(x)')} فتجمع الجذور البدائية لـ {m('1')} من الرتبة {m('n')} وعددها {m('\\varphi(n)')}، وهي أحادية وغير قابلة للتحليل في {m('\\mathbb{Z}[x]')}, وتحقق {m('x^n - 1 = \\prod_{d \\mid n} \\Phi_d(x)')}."
            ),
            formula_en=dm(
                r"x^n - 1 = \prod_{d \mid n} \Phi_d(x), \qquad \deg \Phi_n = \varphi(n), \qquad \Phi_p(x) = 1 + x + \dots + x^{p-1}"
            ),
            caption_ar="تحليل x^n - 1 إلى كثيرات الحدود الدويرية غير القابلة للتحليل:",
            formula_math_ar=dm(
                r"x^n - 1 = \prod_{d \mid n} \Phi_d(x), \qquad \deg \Phi_n = \varphi(n), \qquad \Phi_p(x) = 1 + x + \dots + x^{p-1}"
            ),
            diagram_en=svg_olym_divisibility_lattice("xⁿ − 1", "Φ_d(x)", "Φ_n(x)", "deg = φ(n)"),
        ),
        olym_concept(
            title_en="Roots-of-Unity Filter & Chebyshev Polynomials",
            title_ar="مرشح جذور الوحدة وكثيرات حدود تشيبيشيف",
            body_en=(
                f"Let {m('\\omega = e^{2\\pi i/n}')}. Because {m('\\sum_{k=0}^{n-1} \\omega^{rk}')} equals {m('n')} when {m('n \\mid r')} and {m('0')} otherwise, "
                f"averaging {m('P(\\omega^k x)')} extracts every {m('n')}-th coefficient (**roots-of-unity filter**), while factoring {m('\\frac{z^n - 1}{z - 1} = \\prod_{k=1}^{n-1}(z - \\omega^k)')} "
                f"evaluates trigonometric products cleanly. Pairing {m('\\omega^k + \\omega^{-k} = 2\\cos(2k\\pi/n)')} connects directly to **Chebyshev polynomials** "
                f"{m('T_0(x)=1')}, {m('T_1(x)=x')}, {m('T_{m+1}(x) = 2x\\,T_m(x) - T_{m-1}(x)')}, which satisfy {m('T_m(\\cos\\theta) = \\cos(m\\theta)')}."
            ),
            body_ar=(
                f"ليكن {m('\\omega = e^{2\\pi i/n}')}. بما أن المجموع {m('\\sum_{k=0}^{n-1} \\omega^{rk}')} يساوي {m('n')} عندما {m('n \\mid r')} ويساوي {m('0')} خلاف ذلك، "
                f"فإن أخذ المتوسط {m('\\frac{1}{n}\\sum_{k=0}^{n-1} P(\\omega^k x)')} يعزل المعاملات ذات الأدلة المضاعفة لـ {m('n')} (**مرشح جذور الوحدة**)، كما أن التحليل {m('\\frac{z^n - 1}{z - 1} = \\prod_{k=1}^{n-1}(z - \\omega^k)')} "
                f"يحسب الجداءات المثلثية بدقة. ويرتبط تجميع الأزواج المترافقة {m('\\omega^k + \\omega^{-k} = 2\\cos(2k\\pi/n)')} مباشرةً بـ **كثيرات حدود تشيبيشيف** "
                f"{m('T_0(x)=1')}، {m('T_1(x)=x')}، {m('T_{m+1}(x) = 2x\\,T_m(x) - T_{m-1}(x)')} التي تحقق {m('T_m(\\cos\\theta) = \\cos(m\\theta)')}."
            ),
            formula_en=dm(
                r"\prod_{k=1}^{n-1}(z - \omega^k) = \sum_{j=0}^{n-1} z^j, \qquad "
                r"T_{m+1}(x) = 2x\,T_m(x) - T_{m-1}(x),\;\; T_m(\cos\theta) = \cos(m\theta)"
            ),
            caption_ar="متطابقة جداء جذور الوحدة والعلاقة التراجعية لكثيرات حدود تشيبيشيف:",
            formula_math_ar=dm(
                r"\prod_{k=1}^{n-1}(z - \omega^k) = \sum_{j=0}^{n-1} z^j, \qquad "
                r"T_{m+1}(x) = 2x\,T_m(x) - T_{m-1}(x)"
            ),
            diagram_en=_svg_roots_of_unity(7, "ω = exp(2πi/7)", "ω^k + ω^(−k)"),
        ),
        olym_concept(
            title_en="Functional Equations & Rational Conjugation of Recurrences",
            title_ar="المعادلات الدالية والمرافقة الكسرية للمتتاليات غير الخطية",
            body_en=(
                f"In Olympiad functional equations, first test whether an expression containing a free variable spans all of {m('\\mathbb{R}')} (**surjectivity**) or uniquely recovers its input (**injectivity**). "
                f"Surjectivity lets you choose {m('x_0')} with {m('f(x_0) = 0')} and replace {m('f(y)')} by an arbitrary variable {m('z')}; Cauchy's equation {m('f(x+y)=f(x)+f(y)')} forces {m('f(x)=cx')} over {m('\\mathbb{Q}')}, and over {m('\\mathbb{R}')} once monotonicity or positivity holds. "
                f"For nonlinear recurrences like {m('x_{n+1} = \\frac{x_n^2 + a^2}{2x_n}')}, conjugating around fixed points {m('\\pm a')} via {m('u_n = \\frac{x_n + a}{x_n - a}')} turns quadratic iteration into pure squaring {m('u_{n+1} = u_n^2')}."
            ),
            body_ar=(
                f"في المعادلات الدالية الأولمبية، نفحص أولاً ما إذا كانت عبارة تحوي متغيراً حراً تغطي كامل {m('\\mathbb{R}')} (**الشمولية**) أو تحدد مدخلها بوحدانية (**التباين**). "
                f"تتيح الشمولية اختيار {m('x_0')} يحقق {m('f(x_0) = 0')} واستبدال {m('f(y)')} بمتغير حر {m('z')}؛ كما تفرض معادلة كوشي {m('f(x+y)=f(x)+f(y)')} الصيغة {m('f(x)=cx')} على {m('\\mathbb{Q}')}، وعلى {m('\\mathbb{R}')} بوجود رتابة أو إيجابية. "
                f"وفي المتتاليات غير الخطية مثل {m('x_{n+1} = \\frac{x_n^2 + a^2}{2x_n}')}، يحوّل التحويل الكسري حول النقطتين الثابتتين {m('\\pm a')} عبر {m('u_n = \\frac{x_n + a}{x_n - a}')} العلاقة إلى تربيع مباشر {m('u_{n+1} = u_n^2')}."
            ),
            formula_en=dm(
                r"x_{n+1} = \frac{x_n^2 + a^2}{2x_n} \implies \frac{x_{n+1} + a}{x_{n+1} - a} = \left(\frac{x_n + a}{x_n - a}\right)^2"
            ),
            caption_ar="المرافقة الكسرية حول النقاط الثابتة لتحويل متتالية غير خطية إلى أس مضاعف:",
            formula_math_ar=dm(
                r"x_{n+1} = \frac{x_n^2 + a^2}{2x_n} \implies \frac{x_{n+1} + a}{x_{n+1} - a} = \left(\frac{x_n + a}{x_n - a}\right)^2"
            ),
            diagram_en=svg_olym_func_mapping(["x₀", "y", "f(y)"], ["0", "f(y)", "z"], "Surjectivity Reduction"),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-02-EX1",
            title_en="Evaluating a Cyclotomic Polynomial by Divisor Sieving",
            title_ar="حساب قيمة كثيرة حدود دويرية عبر غربلة القواسم",
            q_en=(
                f"Let {m('\\Phi_{12}(x)')} be the {m('12')}-th cyclotomic polynomial—the monic polynomial in {m('\\mathbb{Z}[x]')} whose roots are the primitive {m('12')}-th roots of unity. "
                f"What is {m('\\Phi_{12}(3)')}?"
            ),
            q_ar=(
                f"لتكن {m('\\Phi_{12}(x)')} كثيرة الحدود الدويرية الثانية عشرة (كثيرة الحدود الأحادية في {m('\\mathbb{Z}[x]')} التي جذورها هي الجذور البدائية للوحدة من الرتبة {m('12')}). "
                f"ما قيمة {m('\\Phi_{12}(3)')}؟"
            ),
            correct_val=73,
            distractors=[61, 71, 83, 91],
            idea_en=(
                f"Factor {m('x^{12} - 1 = (x^6 - 1)(x^6 + 1)')} and strip out non-primitive roots dividing {m('x^6 - 1')} and {m('x^4 - 1')}."
            ),
            steps_en=[
                f"Every {m('12')}-th root of unity satisfies {m('x^{12} - 1 = (x^6 - 1)(x^6 + 1) = 0')}; any root whose order divides {m('6')} is already a root of {m('x^6 - 1')}.",
                f"Factor the remaining part: {m('x^6 + 1 = (x^2 + 1)(x^4 - x^2 + 1)')}. Here {m('x^2 + 1 = \\Phi_4(x)')} accounts for the roots of order {m('4')}.",
                f"Since {m('\\deg \\Phi_{12} = \\varphi(12) = 4')}, the remaining monic factor must be {m('\\Phi_{12}(x) = x^4 - x^2 + 1')}.",
                f"Substitute {m('x = 3')}: {m('\\Phi_{12}(3) = 3^4 - 3^2 + 1 = 81 - 9 + 1 = 73')}.",
            ],
            check_en=(
                f"Inclusion-exclusion gives {m('\\Phi_{12}(3) = \\frac{(3^{12}-1)(3^2-1)}{(3^6-1)(3^4-1)} = \\frac{(3^6+1)\\cdot 8}{80} = \\frac{730}{10} = 73')}."
            ),
            idea_ar=(
                f"نحلل {m('x^{12} - 1 = (x^6 - 1)(x^6 + 1)')} ونستبعد الجذور غير البدائية التي تقسم رتبتها {m('6')} أو {m('4')}."
            ),
            steps_ar=[
                f"تحقق جذور الوحدة من الرتبة {m('12')} المعادلة {m('x^{12} - 1 = (x^6 - 1)(x^6 + 1) = 0')}، وكل جذر تقسم رتبته {m('6')} يقع في {m('x^6 - 1')}.",
                f"نحلل العامل المتبقي: {m('x^6 + 1 = (x^2 + 1)(x^4 - x^2 + 1)')}، حيث {m('x^2 + 1 = \\Phi_4(x)')} تمثل الجذور ذات الرتبة {m('4')}.",
                f"بما أن {m('\\deg \\Phi_{12} = \\varphi(12) = 4')}، فإن {m('\\Phi_{12}(x) = x^4 - x^2 + 1')}.",
                f"بالتعويض عند {m('x = 3')}: {m('\\Phi_{12}(3) = 3^4 - 3^2 + 1 = 81 - 9 + 1 = 73')}.",
            ],
            check_ar=(
                f"من صيغة التضمين والإقصاء: {m('\\Phi_{12}(3) = \\frac{(3^6+1)(3^2-1)}{3^4-1} = \\frac{730 \\times 8}{80} = 73')}."
            ),
            diagram_en=svg_olym_divisibility_lattice("x¹² − 1", "Φ₄ = x²+1", "Φ₁₂(x)", "Φ₁₂(3) = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-02-EX2",
            title_en="Trigonometric Cubic Product via 7-th Roots of Unity",
            title_ar="جداء مثلثي تكعيبي عبر جذور الوحدة السابعة",
            q_en=(
                f"Evaluate the exact product {m('\\prod_{k=1}^{3} \\left(3 - 2\\cos\\frac{2k\\pi}{7}\\right)')}."
            ),
            q_ar=(
                f"احسب القيمة الدقيقة للجداء {m('\\prod_{k=1}^{3} \\left(3 - 2\\cos\\frac{2k\\pi}{7}\\right)')}."
            ),
            correct_val=29,
            distractors=[19, 27, 31, 43],
            idea_en=(
                f"Write {m('y_k = 2\\cos(2k\\pi/7) = \\omega^k + \\omega^{-k}')} for {m('\\omega = e^{2\\pi i/7}')}, find the monic cubic polynomial with roots {m('y_1, y_2, y_3')}, and evaluate it at {m('y = 3')}."
            ),
            steps_en=[
                f"Let {m('\\omega = e^{2\\pi i/7}')}. Dividing {m('1 + \\omega + \\dots + \\omega^6 = 0')} by {m('\\omega^3')} gives {m('(\\omega^3 + \\omega^{-3}) + (\\omega^2 + \\omega^{-2}) + (\\omega + \\omega^{-1}) + 1 = 0')}.",
                f"For {m('y = \\omega^k + \\omega^{-k}')} ({m('k = 1, 2, 3')}), Chebyshev / power identities give {m('\\omega^{2k} + \\omega^{-2k} = y^2 - 2')} and {m('\\omega^{3k} + \\omega^{-3k} = y^3 - 3y')}.",
                f"Substituting yields {m('(y^3 - 3y) + (y^2 - 2) + y + 1 = y^3 + y^2 - 2y - 1 = 0')}; since {m('y_1, y_2, y_3')} are distinct, {m('\\prod_{k=1}^3 (y - y_k) = y^3 + y^2 - 2y - 1')}.",
                f"Evaluate at {m('y = 3')}: {m('3^3 + 3^2 - 2(3) - 1 = 27 + 9 - 6 - 1 = 29')}.",
            ],
            check_en=(
                f"At {m('y = 2')}, the same polynomial gives {m('8 + 4 - 4 - 1 = 7')}, matching the known identity {m('\\prod_{k=1}^3 (2 - 2\\cos\\frac{2k\\pi}{7}) = \\prod_{k=1}^6 2\\sin\\frac{k\\pi}{7} = 7')}."
            ),
            idea_ar=(
                f"نضع {m('y_k = 2\\cos(2k\\pi/7) = \\omega^k + \\omega^{-k}')} حيث {m('\\omega = e^{2\\pi i/7}')}، وننشئ كثيرة الحدود التكعيبية الأحادية التي جذورها {m('y_1, y_2, y_3')} ثم نعوض {m('y = 3')}."
            ),
            steps_ar=[
                f"ليكن {m('\\omega = e^{2\\pi i/7}')}؛ بقسمة {m('1 + \\omega + \\dots + \\omega^6 = 0')} على {m('\\omega^3')} نجد {m('(\\omega^3 + \\omega^{-3}) + (\\omega^2 + \\omega^{-2}) + (\\omega + \\omega^{-1}) + 1 = 0')}.",
                f"عند وضع {m('y = \\omega^k + \\omega^{-k}')} لقيم {m('k = 1, 2, 3')} يكون {m('\\omega^{2k} + \\omega^{-2k} = y^2 - 2')} و{m('\\omega^{3k} + \\omega^{-3k} = y^3 - 3y')}.",
                f"بالتعويض نحصل على {m('y^3 + y^2 - 2y - 1 = 0')}، وبما أن {m('y_1, y_2, y_3')} مختلفة فإن {m('\\prod_{k=1}^3 (y - y_k) = y^3 + y^2 - 2y - 1')}.",
                f"نعوض {m('y = 3')}: {m('3^3 + 3^2 - 2(3) - 1 = 27 + 9 - 6 - 1 = 29')}.",
            ],
            check_ar=(
                f"عند {m('y = 2')} تعطي كثيرة الحدود نفسها {m('8 + 4 - 4 - 1 = 7')}، وهو يطابق المتطابقة الشهيرة {m('\\prod_{k=1}^6 2\\sin(k\\pi/7) = 7')}."
            ),
            diagram_en=_svg_roots_of_unity(7, "y_k = 2cos(2kπ/7)", "Π(3 − y_k) = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-02-EX3",
            title_en="Solving an IMO-Style Functional Equation via Surjectivity",
            title_ar="حل معادلة دالية أولمبية عبر إثبات الشمولية",
            q_en=(
                f"Suppose {m('f : \\mathbb{R} \\to \\mathbb{R}')} satisfies {m('f(f(x) + y) = 2x + f(f(y) - x)')} for all {m('x, y \\in \\mathbb{R}')}. "
                f"Given that {m('f(4) = 12')}, what is {m('f(15)')}?"
            ),
            q_ar=(
                f"لنفترض أن الدالة {m('f : \\mathbb{R} \\to \\mathbb{R}')} تحقق {m('f(f(x) + y) = 2x + f(f(y) - x)')} لكل {m('x, y \\in \\mathbb{R}')}. "
                f"إذا علمت أن {m('f(4) = 12')}، فما قيمة {m('f(15)')}؟"
            ),
            correct_val=23,
            distractors=[19, 27, 34, 45],
            idea_en=(
                f"Substitute {m('y = -f(x)')} to prove {m('f')} is surjective, then pick {m('x_0')} with {m('f(x_0) = 0')} to force {m('f(t) = t + c')}."
            ),
            steps_en=[
                f"Set {m('y = -f(x)')}: {m('f(0) = 2x + f(f(-f(x)) - x)')}, so {m('f(f(-f(x)) - x) = f(0) - 2x')}. As {m('x')} ranges over {m('\\mathbb{R}')}, {m('f(0) - 2x')} takes every real value, so {m('f')} is surjective.",
                f"By surjectivity, choose {m('x_0 \\in \\mathbb{R}')} with {m('f(x_0) = 0')}. Setting {m('x = x_0')} gives {m('f(y) = 2x_0 + f(f(y) - x_0)')} for all {m('y \\in \\mathbb{R}')}.",
                f"Since {m('z = f(y)')} ranges over all of {m('\\mathbb{R}')}, we get {m('f(z - x_0) = z - 2x_0')}; letting {m('t = z - x_0')} yields {m('f(t) = t - x_0 = t + c')} for all {m('t \\in \\mathbb{R}')}.",
                f"Using {m('f(4) = 12')} gives {m('4 + c = 12 \\implies c = 8')}, so {m('f(15) = 15 + 8 = 23')}.",
            ],
            check_en=(
                f"Verify {m('f(t) = t + 8')}: LHS {m('= (x + 8) + y + 8 = x + y + 16')}, and RHS {m('= 2x + ((y + 8) - x + 8) = x + y + 16')} for all {m('x, y')}."
            ),
            idea_ar=(
                f"نعوّض {m('y = -f(x)')} لإثبات أن {m('f')} شاملة، ثم نختار {m('x_0')} يحقق {m('f(x_0) = 0')} لنستنتج أن {m('f(t) = t + c')}."
            ),
            steps_ar=[
                f"نضع {m('y = -f(x)')} فنجد {m('f(f(-f(x)) - x) = f(0) - 2x')}؛ ولما كان {m('f(0) - 2x')} يمسح كل الأعداد الحقيقية بتغير {m('x')} فإن {m('f')} دالة شاملة.",
                f"من الشمولية يوجد {m('x_0 \\in \\mathbb{R}')} يحقق {m('f(x_0) = 0')}. بوضع {m('x = x_0')} نحصل على {m('f(y) = 2x_0 + f(f(y) - x_0)')} لكل {m('y')}.",
                f"بما أن {m('z = f(y)')} يغطي كل {m('\\mathbb{R}')} فإن {m('f(z - x_0) = z - 2x_0')}، وبوضع {m('t = z - x_0')} نجد {m('f(t) = t - x_0 = t + c')}.",
                f"من الشرط {m('f(4) = 12')} نجد {m('c = 8')}، وبالتالي {m('f(15) = 15 + 8 = 23')}.",
            ],
            check_ar=(
                f"نتحقق من {m('f(t) = t + 8')}: الطرف الأيسر {m('x + y + 16')}، والطرف الأيمن {m('2x + (y + 8 - x + 8) = x + y + 16')} لكل {m('x, y')}."
            ),
            diagram_en=svg_olym_func_mapping(["4", "x₀", "15"], ["12", "0", "?"], "f(f(x)+y) = 2x + f(f(y)−x)"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-02-EX4",
            title_en="Fixed-Point Ratio Conjugation of a Nonlinear Recurrence",
            title_ar="المرافقة الكسرية لمتتالية غير خطية حول نقاطها الثابتة",
            q_en=(
                f"A sequence {m('\\{x_n\\}_{n \\ge 0}')} satisfies {m('x_0 = 6')} and {m('x_{n+1} = \\frac{x_n^2 + 4}{2x_n}')} for all {m('n \\ge 0')}. "
                f"What is the exact value of {m('\\log_2\\!\\left(\\frac{x_5 + 2}{x_5 - 2}\\right)')}?"
            ),
            q_ar=(
                f"تحقق المتتالية {m('\\{x_n\\}_{n \\ge 0}')} الشرط الابتدائي {m('x_0 = 6')} والعلاقة {m('x_{n+1} = \\frac{x_n^2 + 4}{2x_n}')} لكل {m('n \\ge 0')}. "
                f"ما القيمة الدقيقة للمقدار {m('\\log_2\\!\\left(\\frac{x_5 + 2}{x_5 - 2}\\right)')}؟"
            ),
            correct_val=32,
            distractors=[10, 16, 25, 64],
            idea_en=(
                f"Compare {m('x_{n+1} + 2')} and {m('x_{n+1} - 2')} around the fixed points {m('\\pm 2')}: their ratio squares at every step."
            ),
            steps_en=[
                f"Notice {m('x_{n+1} + 2 = \\frac{x_n^2 + 4x_n + 4}{2x_n} = \\frac{(x_n + 2)^2}{2x_n}')} and {m('x_{n+1} - 2 = \\frac{(x_n - 2)^2}{2x_n}')}.",
                f"Dividing the two identities (valid since {m('x_n > 2')} by induction) gives {m('u_{n+1} = u_n^2')} where {m('u_n = \\frac{x_n + 2}{x_n - 2}')}.",
                f"At {m('n = 0')}, {m('u_0 = \\frac{6 + 2}{6 - 2} = \\frac{8}{4} = 2')}. Repeated squaring yields {m('u_n = u_0^{2^n} = 2^{2^n}')}.",
                f"For {m('n = 5')}, {m('u_5 = 2^{2^5} = 2^{32}')}, so {m('\\log_2(u_5) = 32')}.",
            ],
            check_en=(
                f"Check {m('n = 1')}: {m('x_1 = \\frac{36 + 4}{12} = \\frac{10}{3}')}, so {m('\\frac{x_1 + 2}{x_1 - 2} = \\frac{16/3}{4/3} = 4 = 2^{2^1}')}, confirming {m('2^{2^n}')}."
            ),
            idea_ar=(
                f"نقارن بين {m('x_{n+1} + 2')} و{m('x_{n+1} - 2')} حول النقطتين الثابتتين {m('\\pm 2')}: فالنسبة بينهما تتربّع في كل خطوة."
            ),
            steps_ar=[
                f"نلاحظ أن {m('x_{n+1} + 2 = \\frac{(x_n + 2)^2}{2x_n}')} وكذلك {m('x_{n+1} - 2 = \\frac{(x_n - 2)^2}{2x_n}')}.",
                f"بقسمة المتطابقتين (والمقام موجب لأن {m('x_n > 2')} بالاستقراء) نحصل على {m('u_{n+1} = u_n^2')} حيث {m('u_n = \\frac{x_n + 2}{x_n - 2}')}.",
                f"عند {m('n = 0')} لدينا {m('u_0 = \\frac{6 + 2}{6 - 2} = 2')}، وبالتكرار نجد {m('u_n = u_0^{2^n} = 2^{2^n}')}.",
                f"عند {m('n = 5')} يكون {m('u_5 = 2^{2^5} = 2^{32}')}، ومنه {m('\\log_2(u_5) = 32')}.",
            ],
            check_ar=(
                f"نتحقق عند {m('n = 1')}: {m('x_1 = \\frac{40}{12} = \\frac{10}{3}')}، فتكون النسبة {m('\\frac{16/3}{4/3} = 4 = 2^{2^1}')}، مما يؤكد الصيغة {m('2^{2^n}')}."
            ),
            diagram_en=svg_olym_func_mapping(["u₀ = 2", "u₁ = 2²", "u₅"], ["2¹", "2²", "log₂ u₅ = ?"], "u_{n+1} = u_n²"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-02",
        level=LEVEL_T3,
        unit_num="3.2",
        topic="Algebra",
        title_en="Cyclotomic Irreducibility, Roots of Unity & Functional Equations",
        title_ar="كثيرات الحدود الدويرية، وجذور الوحدة، والمعادلات الدالية",
        summary_en=(
            "Build Olympiad Algebra mastery across polynomial irreducibility and cyclotomic factorizations, "
            "Chebyshev and roots-of-unity evaluations, functional equations over R, and rational conjugation of nonlinear recurrences."
        ),
        summary_ar=(
            "ابنِ إتقاناً متقدماً في جبر الأولمبياد: عدم قابلية التحليل وكثيرات الحدود الدويرية، "
            "وجذور الوحدة وكثيرات حدود تشيبيشيف، والمعادلات الدالية على الأعداد الحقيقية، والمرافقة الكسرية للمتتاليات غير الخطية."
        ),
        goals_en=[
            f"Test polynomial irreducibility with shifted Eisenstein criteria and compute cyclotomic factors via {m('x^n - 1 = \\prod_{d \\mid n} \\Phi_d(x)')}.",
            f"Evaluate trigonometric sums and products using {m('\\omega = e^{2\\pi i/n}')} and Chebyshev polynomials {m('T_n(\\cos\\theta) = \\cos(n\\theta)')}.",
            f"Establish injectivity and surjectivity to solve Olympiad functional equations without assuming regularity.",
            f"Conjugate nonlinear recurrences around fixed points to expose exponential or telescoping invariants.",
        ],
        goals_ar=[
            f"اختبار عدم قابلية تحليل كثيرات الحدود بمعيار أيزنشتاين المزاح واستخراج العوامل الدويرية عبر {m('x^n - 1 = \\prod_{d \\mid n} \\Phi_d(x)')}.",
            f"حساب المجاميع والجداءات المثلثية باستخدام جذور الوحدة {m('\\omega = e^{2\\pi i/n}')} وكثيرات حدود تشيبيشيف {m('T_n(\\cos\\theta) = \\cos(n\\theta)')}.",
            f"إثبات التباين والشمولية لحل المعادلات الدالية الأولمبية دون افتراضات مسبقة.",
            f"مرافقة المتتاليات غير الخطية حول نقاطها الثابتة لكشف الثوابت الأسية أو المتداخلة.",
        ],
        concepts=concepts,
        traps_en=[
            f"Assuming {m('\\frac{x^n - 1}{x - 1}')} is irreducible for composite {m('n')}: every divisor {m('d \\mid n')} with {m('1 < d < n')} contributes a proper factor {m('\\Phi_d(x)')}.",
            f"Claiming {m('f(x + y) = f(x) + f(y)')} on {m('\\mathbb{R}')} implies {m('f(x) = cx')} without proving positivity, monotonicity, boundedness, or an extra algebraic identity.",
            f"Confusing {m('u_n = u_0^{2^n}')} with {m('u_0^{2n}')} when iterating {m('u_{n+1} = u_n^2')}: each step doubles the exponent, so {m('n')} steps multiply the initial exponent by {m('2^n')}.",
        ],
        traps_ar=[
            f"افتراض أن {m('\\frac{x^n - 1}{x - 1}')} غير قابلة للتحليل عندما يكون {m('n')} مركباً؛ إذ يسهم كل قاسم {m('1 < d < n')} بعامل فعلي {m('\\Phi_d(x)')}.",
            f"استنتاج {m('f(x) = cx')} على {m('\\mathbb{R}')} من معادلة كوشي {m('f(x + y) = f(x) + f(y)')} دون إثبات رتابة أو إيجابية أو علاقة جبرية إضافية.",
            f"الخلط بين {m('u_0^{2^n}')} و{m('u_0^{2n}')} عند تكرار {m('u_{n+1} = u_n^2')}؛ فكل خطوة تضاعف الأس ليصبح العامل {m('2^n')}.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_alg_irred_cyclotomic_polys",
            "olym_t3_alg_chebyshev_roots_unity",
            "olym_t3_alg_olympiad_func_eqs",
            "olym_t3_alg_nonlinear_recurrences",
        ],
    )



# ==============================================================================
# OLYM-L3-03: Inequalities (Holder, Schur/Muirhead/uvw, Supporting Line, Aczel)
# ==============================================================================

def _lesson_l3_03() -> dict:
    concepts = [
        olym_concept(
            title_en="Hölder's Inequality & Power Mean Hierarchy",
            title_ar="متباينة هولدر وهرمية المتوسطات الأسية",
            body_en=(
                f"For positive reals, the 3-bracket **Hölder Inequality** states that "
                f"{m('\\left(\\sum a_i\\right)\\left(\\sum b_i\\right)\\left(\\sum c_i\\right) \\ge \\left(\\sum \\sqrt[3]{a_i b_i c_i}\\right)^3')}, "
                f"with equality when the three tuples are proportional. This clears radical or linear denominators in cyclic sums like {m('\\sum \\frac{a^3}{2b + c}')} in a single step. "
                f"More generally, the **Power Mean** {m('M_p(x) = \\left(\\frac{1}{n}\\sum_{i=1}^n x_i^p\\right)^{1/p}')} (with {m('M_0 = \\sqrt[n]{x_1\\cdots x_n}')}) is monotonically non-decreasing in {m('p')}: "
                f"{m('M_p \\le M_q')} whenever {m('p < q')}, unifying {m('\\text{HM} \\le \\text{GM} \\le \\text{AM} \\le \\text{QM}')}."
            ),
            body_ar=(
                f"للأعداد الحقيقية الموجبة، تنص **متباينة هولدر** ذات الأقواس الثلاثة على أن "
                f"{m('\\left(\\sum a_i\\right)\\left(\\sum b_i\\right)\\left(\\sum c_i\\right) \\ge \\left(\\sum \\sqrt[3]{a_i b_i c_i}\\right)^3')}، "
                f"مع تحقق المساواة عند تناسب الثلاثيات؛ وهي تزيل المقامات الخطية أو الجذرية في المجاميع الدورية مثل {m('\\sum \\frac{a^3}{2b + c}')} في خطوة واحدة. "
                f"وبصورة أعم، فإن **المتوسط الأسي** {m('M_p(x) = \\left(\\frac{1}{n}\\sum_{i=1}^n x_i^p\\right)^{1/p}')} غير متناقص برتابة بالنسبة إلى {m('p')}: "
                f"{m('M_p \\le M_q')} كلما كان {m('p < q')}، مما يوحّد سلسلة المتوسطات {m('\\text{HM} \\le \\text{GM} \\le \\text{AM} \\le \\text{QM}')}."
            ),
            formula_en=dm(
                r"\left(\sum_{i=1}^n a_i\right)\!\left(\sum_{i=1}^n b_i\right)\!\left(\sum_{i=1}^n c_i\right) \ge \left(\sum_{i=1}^n \sqrt[3]{a_i b_i c_i}\right)^{\!3}, \qquad M_p \le M_q\;\;(p < q)"
            ),
            caption_ar="متباينة هولدر الثلاثية ورتابة المتوسطات الأسية:",
            formula_math_ar=dm(
                r"\left(\sum_{i=1}^n a_i\right)\!\left(\sum_{i=1}^n b_i\right)\!\left(\sum_{i=1}^n c_i\right) \ge \left(\sum_{i=1}^n \sqrt[3]{a_i b_i c_i}\right)^{\!3}, \qquad M_p \le M_q"
            ),
            diagram_en=svg_olym_inequality_curve("a", "b", "M₋₁ ≤ M₀ ≤ M₁ ≤ M₂"),
        ),
        olym_concept(
            title_en="Schur's Inequality, Muirhead Majorization & the uvw Method",
            title_ar="متباينة شور والتغلب لمويرهيد وطريقة uvw",
            body_en=(
                f"For {m('x, y, z \\ge 0')} and {m('r > 0')}, **Schur's Inequality** asserts {m('\\sum_{\\text{cyc}} x^r(x - y)(x - z) \\ge 0')}. "
                f"At {m('r = 1')}, writing {m('p = x + y + z')}, {m('q = xy + yz + zx')}, and {m('r_0 = xyz')} yields {m('p^3 - 4pq + 9r_0 \\ge 0')}, "
                f"whose equality holds both at {m('x = y = z')} and at {m('(t, t, 0)')}. **Muirhead's Theorem** states {m('\\sum_{\\text{sym}} x^{a_1}y^{a_2}z^{a_3} \\ge \\sum_{\\text{sym}} x^{b_1}y^{b_2}z^{b_3}')} "
                f"whenever {m('(a) \\succ (b)')}, while the **uvw method** fixes {m('p, q')} and checks extremal values of {m('xyz')} where two variables coincide or one vanishes."
            ),
            body_ar=(
                f"للأعداد غير السالبة {m('x, y, z \\ge 0')} و{m('r > 0')}، تقرر **متباينة شور** أن {m('\\sum_{\\text{cyc}} x^r(x - y)(x - z) \\ge 0')}. "
                f"وعند {m('r = 1')} وبوضع {m('p = x + y + z')} و{m('q = xy + yz + zx')} و{m('r_0 = xyz')} نحصل على {m('p^3 - 4pq + 9r_0 \\ge 0')}، "
                f"وتتحقق فيها المساواة عند {m('x = y = z')} وكذلك عند {m('(t, t, 0)')}. وتنص **مبرهنة مويرهيد** على أن {m('\\sum_{\\text{sym}} x^{a_1}y^{a_2}z^{a_3} \\ge \\sum_{\\text{sym}} x^{b_1}y^{b_2}z^{b_3}')} "
                f"متى تغلّب المتجه {m('(a) \\succ (b)')}، بينما تثبّت **طريقة uvw** كلاً من {m('p, q')} وتفحص القيم الحدية للجداء {m('xyz')} عند تساوي متغيرين أو انعدام أحدها."
            ),
            formula_en=dm(
                r"\sum_{\text{cyc}} x(x-y)(x-z) \ge 0 \iff p^3 - 4pq + 9r_0 \ge 0 \qquad (p=\textstyle\sum x,\; q=\sum xy,\; r_0=xyz)"
            ),
            caption_ar="صيغة pqr لمتباينة شور من الدرجة الأولى:",
            formula_math_ar=dm(
                r"\sum_{\text{cyc}} x(x-y)(x-z) \ge 0 \iff p^3 - 4pq + 9r_0 \ge 0"
            ),
            diagram_en=svg_olym_divisibility_lattice("(3,0,0)", "(2,1,0)", "(2,0,1)", "(1,1,1)"),
        ),
        olym_concept(
            title_en="Supporting-Line Factorization, Aczél's Inequality & Weight Balancing",
            title_ar="تحليل خط الإسناد ومتباينة أتشيل وموازنة الأوزان",
            body_en=(
                f"To prove {m('\\sum_{i=1}^n f(x_i) \\ge n f(x_0)')} under {m('\\sum_{i=1}^n x_i = n x_0')}, **Jensen's Inequality** applies when {m('f')} is convex; "
                f"more generally, the **algebraic supporting-line method** chooses {m('m')} so that {m('f(x) - [f(x_0) + m(x - x_0)] = (x - x_0)^2 Q(x) \\ge 0')} with {m('Q(x) \\ge 0')} on the domain. "
                f"For reverse-sign quadratic forms, **Aczél's Inequality** states that if {m('a_0^2 \\ge \\sum_{i=1}^n a_i^2')} or {m('b_0^2 \\ge \\sum_{i=1}^n b_i^2')}, then "
                f"{m('(a_0^2 - \\sum a_i^2)(b_0^2 - \\sum b_i^2) \\le (a_0 b_0 - \\sum a_i b_i)^2')}."
            ),
            body_ar=(
                f"لإثبات {m('\\sum_{i=1}^n f(x_i) \\ge n f(x_0)')} تحت الشرط {m('\\sum_{i=1}^n x_i = n x_0')}، نطبّق **متباينة ينسن** إذا كانت {m('f')} محدبة؛ "
                f"وبصورة جبرية أعم، نختار في **طريقة خط الإسناد** الثابت {m('m')} بحيث يتحلل الفرق إلى {m('f(x) - [f(x_0) + m(x - x_0)] = (x - x_0)^2 Q(x) \\ge 0')} مع بقاء {m('Q(x) \\ge 0')} على المجال. "
                f"وفي الصيغ التربيعية العكسية، تقرر **متباينة أتشيل** أنه إذا كان {m('a_0^2 \\ge \\sum_{i=1}^n a_i^2')} أو {m('b_0^2 \\ge \\sum_{i=1}^n b_i^2')} فإن "
                f"{m('(a_0^2 - \\sum a_i^2)(b_0^2 - \\sum b_i^2) \\le (a_0 b_0 - \\sum a_i b_i)^2')}."
            ),
            formula_en=dm(
                r"f(x) - \bigl(f(x_0) + m(x - x_0)\bigr) = (x - x_0)^2 Q(x) \ge 0, \qquad "
                r"\Bigl(a_0^2 - \sum a_i^2\Bigr)\!\Bigl(b_0^2 - \sum b_i^2\Bigr) \le \Bigl(a_0 b_0 - \sum a_i b_i\Bigr)^2"
            ),
            caption_ar="تحليل خط الإسناد الجبري ومتباينة أتشيل:",
            formula_math_ar=dm(
                r"f(x) - \bigl(f(x_0) + m(x - x_0)\bigr) = (x - x_0)^2 Q(x) \ge 0, \qquad "
                r"\Bigl(a_0^2 - \sum a_i^2\Bigr)\!\Bigl(b_0^2 - \sum b_i^2\Bigr) \le \Bigl(a_0 b_0 - \sum a_i b_i\Bigr)^2"
            ),
            diagram_en=_svg_tangent_support("x₀", "f(x)", "f(x₀)+m(x−x₀)"),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-03-EX1",
            title_en="Clearing Asymmetric Denominators via 3-Bracket Hölder",
            title_ar="إزالة المقامات غير المتماثلة عبر متباينة هولدر الثلاثية",
            q_en=(
                f"Let {m('a, b, c')} be positive real numbers such that {m('a + b + c = 9')}. "
                f"What is the minimum possible value of {m('S = \\frac{a^3}{2b + c} + \\frac{b^3}{2c + a} + \\frac{c^3}{2a + b}')}?"
            ),
            q_ar=(
                f"لتكن {m('a, b, c')} أعداداً حقيقية موجبة تحقق {m('a + b + c = 9')}. "
                f"ما أصغر قيمة ممكنة للمقدار {m('S = \\frac{a^3}{2b + c} + \\frac{b^3}{2c + a} + \\frac{c^3}{2a + b}')}؟"
            ),
            correct_val=9,
            distractors=[3, 6, 12, 27],
            idea_en=(
                f"Multiply {m('S')} by {m('\\sum_{\\text{cyc}}(2b + c)')} and {m('(1 + 1 + 1)')}, then apply 3-bracket Hölder's inequality."
            ),
            steps_en=[
                f"By 3-bracket Hölder's inequality, {m('\\left(\\sum_{\\text{cyc}} \\frac{a^3}{2b + c}\\right)\\left(\\sum_{\\text{cyc}} (2b + c)\\right)(1 + 1 + 1) \\ge (a + b + c)^3')}.",
                f"Evaluate the auxiliary sums: {m('\\sum_{\\text{cyc}} (2b + c) = 3(a + b + c) = 27')} and {m('1 + 1 + 1 = 3')}.",
                f"Substitute {m('a + b + c = 9')}: {m('S \\cdot 27 \\cdot 3 \\ge 9^3 = 729 \\implies 81S \\ge 729 \\implies S \\ge 9')}.",
                f"Equality holds at {m('a = b = c = 3')}, where {m('S = 3 \\cdot \\frac{27}{9} = 9')}.",
            ],
            check_en=(
                f"At {m('a = b = c = 3')}, each fraction equals {m('27 / (6 + 3) = 3')}, so {m('S = 3 + 3 + 3 = 9')}."
            ),
            idea_ar=(
                f"نضرب {m('S')} في {m('\\sum_{\\text{cyc}}(2b + c)')} وفي {m('(1 + 1 + 1)')} ثم نطبّق متباينة هولدر الثلاثية."
            ),
            steps_ar=[
                f"من متباينة هولدر الثلاثية: {m('\\left(\\sum_{\\text{cyc}} \\frac{a^3}{2b + c}\\right)\\left(\\sum_{\\text{cyc}} (2b + c)\\right)(1 + 1 + 1) \\ge (a + b + c)^3')}.",
                f"نحسب المجموع المساعد: {m('\\sum_{\\text{cyc}} (2b + c) = 3(a + b + c) = 27')} ومجموع الواحدات يساوي {m('3')}.",
                f"بالتعويض عن {m('a + b + c = 9')} نجد {m('81 S \\ge 9^3 = 729 \\implies S \\ge 9')}.",
                f"تتحقق المساواة عند {m('a = b = c = 3')} حيث {m('S = 3 \\cdot \\frac{27}{9} = 9')}.",
            ],
            check_ar=(
                f"عند {m('a = b = c = 3')} يساوي كل كسر {m('27/9 = 3')}، فيكون المجموع {m('3 + 3 + 3 = 9')}."
            ),
            diagram_en=svg_olym_inequality_curve("a³/(2b+c)", "2b+c", "min S = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-03-EX2",
            title_en="Bounding a Symmetric Polynomial via Degree-1 Schur",
            title_ar="تحديد القيمة الصغرى لكثيرة حدود متماثلة عبر متباينة شور",
            q_en=(
                f"Let {m('x, y, z \\ge 0')} be non-negative real numbers satisfying {m('x + y + z = 6')}. "
                f"What is the minimum possible value of {m('E = x^2 + y^2 + z^2 + \\frac{3}{4}xyz')}?"
            ),
            q_ar=(
                f"لتكن {m('x, y, z \\ge 0')} أعداداً حقيقية غير سالبة تحقق {m('x + y + z = 6')}. "
                f"ما أصغر قيمة ممكنة للمقدار {m('E = x^2 + y^2 + z^2 + \\frac{3}{4}xyz')}؟"
            ),
            correct_val=18,
            distractors=[12, 15, 24, 36],
            idea_en=(
                f"Rewrite {m('E')} in terms of {m('p = 6')}, {m('q = xy + yz + zx')}, and {m('r = xyz')}, then apply Schur's inequality {m('p^3 - 4pq + 9r \\ge 0')}."
            ),
            steps_en=[
                f"Let {m('p = x + y + z = 6')}, {m('q = xy + yz + zx')}, and {m('r = xyz')}. Then {m('x^2 + y^2 + z^2 = p^2 - 2q = 36 - 2q')}.",
                f"By degree-1 Schur's inequality, {m('p^3 - 4pq + 9r \\ge 0')}, which for {m('p = 6')} reads {m('216 - 24q + 9r \\ge 0')}.",
                f"Dividing by {m('12')} gives {m('18 - 2q + \\frac{3}{4}r \\ge 0 \\implies -2q + \\frac{3}{4}r \\ge -18')}.",
                f"Therefore {m('E = 36 - 2q + \\frac{3}{4}r \\ge 36 - 18 = 18')}, achieved both at {m('(2, 2, 2)')} and at {m('(3, 3, 0)')}.",
            ],
            check_en=(
                f"At {m('(2, 2, 2)')}, {m('E = 12 + \\frac{3}{4}(8) = 18')}; at {m('(3, 3, 0)')}, {m('E = 9 + 9 + 0 + 0 = 18')}."
            ),
            idea_ar=(
                f"نكتب {m('E')} بدلالة {m('p = 6')} و{m('q = xy + yz + zx')} و{m('r = xyz')}، ثم نطبّق متباينة شور {m('p^3 - 4pq + 9r \\ge 0')}."
            ),
            steps_ar=[
                f"نضع {m('p = 6')} و{m('q = xy + yz + zx')} و{m('r = xyz')}، فيكون {m('x^2 + y^2 + z^2 = p^2 - 2q = 36 - 2q')}.",
                f"من متباينة شور للدرجة الأولى {m('p^3 - 4pq + 9r \\ge 0')}، وعند {m('p = 6')} تصبح {m('216 - 24q + 9r \\ge 0')}.",
                f"بقسمة المتباينة على {m('12')} نجد {m('18 - 2q + \\frac{3}{4}r \\ge 0 \\implies -2q + \\frac{3}{4}r \\ge -18')}.",
                f"إذن {m('E = 36 - 2q + \\frac{3}{4}r \\ge 36 - 18 = 18')}، وتتحقق المساواة عند {m('(2, 2, 2)')} وعند {m('(3, 3, 0)')}.",
            ],
            check_ar=(
                f"عند {m('(2, 2, 2)')} لدينا {m('E = 12 + 6 = 18')}، وعند {m('(3, 3, 0)')} لدينا {m('E = 9 + 9 + 0 = 18')}."
            ),
            diagram_en=svg_olym_divisibility_lattice("p = 6", "36 − 2q", "(3/4)r", "min E = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-03-EX3",
            title_en="Algebraic Supporting-Line Factorization at x₀ = 2",
            title_ar="تحليل خط الإسناد الجبري عند نقطة التساوي x₀ = 2",
            q_en=(
                f"Let {m('a, b, c > 0')} be positive real numbers satisfying {m('a + b + c = 6')}. "
                f"What is the minimum possible value of {m('S = \\sum_{\\text{cyc}} \\frac{4(a^2 - a + 1)}{a + 1}')}?"
            ),
            q_ar=(
                f"لتكن {m('a, b, c > 0')} أعداداً حقيقية موجبة تحقق {m('a + b + c = 6')}. "
                f"ما أصغر قيمة ممكنة للمجموع الدوري {m('S = \\sum_{\\text{cyc}} \\frac{4(a^2 - a + 1)}{a + 1}')}؟"
            ),
            correct_val=12,
            distractors=[8, 9, 15, 16],
            idea_en=(
                f"Use the algebraic supporting-line identity {m('\\frac{4(x^2 - x + 1)}{x + 1} - \\frac{4}{3}(2x - 1) = \\frac{4(x - 2)^2}{3(x + 1)} \\ge 0')} centered at {m('x_0 = 2')}."
            ),
            steps_en=[
                f"For {m('x > 0')}, notice the identity {m('3(x^2 - x + 1) - (2x - 1)(x + 1) = (3x^2 - 3x + 3) - (2x^2 + x - 1) = (x - 2)^2 \\ge 0')}.",
                f"Multiplying by {m('\\frac{4}{3(x + 1)} > 0')} gives the supporting-line bound {m('\\frac{4(x^2 - x + 1)}{x + 1} \\ge \\frac{4}{3}(2x - 1)')}.",
                f"Summing over {m('x \\in \\{a, b, c\\}')} with {m('a + b + c = 6')} yields {m('S \\ge \\frac{4}{3}\\bigl(2(a + b + c) - 3\\bigr) = \\frac{4}{3}(12 - 3) = 12')}.",
                f"Equality holds when {m('a = b = c = 2')}, giving {m('S = 3 \\cdot \\frac{4(4 - 2 + 1)}{3} = 12')}.",
            ],
            check_en=(
                f"At {m('x = 2')}, both {m('\\frac{4(x^2 - x + 1)}{x + 1}')} and {m('\\frac{4}{3}(2x - 1)')} equal {m('4')}, and the difference is {m('\\frac{4(x - 2)^2}{3(x + 1)} \\ge 0')}."
            ),
            idea_ar=(
                f"نستخدم متطابقة خط الإسناد الجبري {m('\\frac{4(x^2 - x + 1)}{x + 1} - \\frac{4}{3}(2x - 1) = \\frac{4(x - 2)^2}{3(x + 1)} \\ge 0')} حول {m('x_0 = 2')}."
            ),
            steps_ar=[
                f"لكل {m('x > 0')} لدينا المتطابقة الجبرية {m('3(x^2 - x + 1) - (2x - 1)(x + 1) = (x - 2)^2 \\ge 0')}.",
                f"بالضرب في {m('\\frac{4}{3(x + 1)} > 0')} نحصل على متباينة الإسناد الخطي {m('\\frac{4(x^2 - x + 1)}{x + 1} \\ge \\frac{4}{3}(2x - 1)')}.",
                f"بجمع المتباينة لـ {m('a, b, c')} مع {m('a + b + c = 6')} نجد {m('S \\ge \\frac{4}{3}\\bigl(2(6) - 3\\bigr) = 12')}.",
                f"تتحقق المساواة عند {m('a = b = c = 2')} حيث يصبح كل حد مساوياً لـ {m('4')} والمجموع {m('12')}.",
            ],
            check_ar=(
                f"عند {m('x = 2')} يتساوى الطرفان عند القيمة {m('4')}، والفرق بينهما مربع كامل مقسوم على مقدار موجب {m('\\frac{4(x - 2)^2}{3(x + 1)} \\ge 0')}."
            ),
            diagram_en=_svg_tangent_support("x₀ = 2", "4(x²−x+1)/(x+1)", "min S = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-03-EX4",
            title_en="Lorentz-Form Lower Bound via Aczél's Inequality",
            title_ar="إيجاد الحد الأدنى لصيغة تربيعية عكسية عبر متباينة أتشيل",
            q_en=(
                f"Positive real numbers {m('a_0, b_0')} and real numbers {m('x_1, x_2, x_3, y_1, y_2, y_3')} satisfy "
                f"{m('a_0^2 - (x_1^2 + x_2^2 + x_3^2) = 9')} and {m('b_0^2 - (y_1^2 + y_2^2 + y_3^2) = 25')}. "
                f"What is the minimum possible value of {m('a_0 b_0 - (x_1 y_1 + x_2 y_2 + x_3 y_3)')}?"
            ),
            q_ar=(
                f"تحقق الأعداد الحقيقية الموجبة {m('a_0, b_0')} والأعداد الحقيقية {m('x_1, x_2, x_3, y_1, y_2, y_3')} الشرطين "
                f"{m('a_0^2 - (x_1^2 + x_2^2 + x_3^2) = 9')} و{m('b_0^2 - (y_1^2 + y_2^2 + y_3^2) = 25')}. "
                f"ما أصغر قيمة ممكنة للمقدار {m('a_0 b_0 - (x_1 y_1 + x_2 y_2 + x_3 y_3)')}؟"
            ),
            correct_val=15,
            distractors=[12, 16, 20, 34],
            idea_en=(
                f"Apply Aczél's inequality {m('(a_0 b_0 - \\sum x_i y_i)^2 \\ge (a_0^2 - \\sum x_i^2)(b_0^2 - \\sum y_i^2)')} and confirm the left side is positive by Cauchy–Schwarz."
            ),
            steps_en=[
                f"Since {m('a_0 > \\sqrt{\\sum x_i^2}')} and {m('b_0 > \\sqrt{\\sum y_i^2}')}, Cauchy–Schwarz ensures {m('a_0 b_0 > \\sqrt{\\sum x_i^2}\\sqrt{\\sum y_i^2} \\ge \\sum x_i y_i')}, so {m('a_0 b_0 - \\sum x_i y_i > 0')}.",
                f"By Aczél's inequality, {m('\\bigl(a_0 b_0 - \\sum_{i=1}^3 x_i y_i\\bigr)^2 \\ge \\bigl(a_0^2 - \\sum_{i=1}^3 x_i^2\\bigr)\\bigl(b_0^2 - \\sum_{i=1}^3 y_i^2\\bigr)')}.",
                f"Substitute the given values {m('9')} and {m('25')}: {m('\\bigl(a_0 b_0 - \\sum_{i=1}^3 x_i y_i\\bigr)^2 \\ge 9 \\times 25 = 225')}.",
                f"Taking the positive square root yields {m('a_0 b_0 - \\sum_{i=1}^3 x_i y_i \\ge 15')}, achieved when {m('(b_0, y_1, y_2, y_3) = \\frac{5}{3}(a_0, x_1, x_2, x_3)')}.",
            ],
            check_en=(
                f"Taking {m('a_0 = 5, x_1 = 4, x_2 = x_3 = 0')} and {m('b_0 = 25/3, y_1 = 20/3, y_2 = y_3 = 0')} gives {m('a_0 b_0 - x_1 y_1 = 125/3 - 80/3 = 15')}."
            ),
            idea_ar=(
                f"نطبّق متباينة أتشيل {m('(a_0 b_0 - \\sum x_i y_i)^2 \\ge (a_0^2 - \\sum x_i^2)(b_0^2 - \\sum y_i^2)')} مع التحقق من إيجابية المقدار عبر كوشي-شوارتز."
            ),
            steps_ar=[
                f"بما أن {m('a_0 > \\sqrt{\\sum x_i^2}')} و{m('b_0 > \\sqrt{\\sum y_i^2}')}، تضمن متباينة كوشي-شوارتز أن {m('a_0 b_0 - \\sum x_i y_i > 0')}.",
                f"من متباينة أتشيل: {m('\\bigl(a_0 b_0 - \\sum_{i=1}^3 x_i y_i\\bigr)^2 \\ge \\bigl(a_0^2 - \\sum_{i=1}^3 x_i^2\\bigr)\\bigl(b_0^2 - \\sum_{i=1}^3 y_i^2\\bigr)')}.",
                f"نعوّض القيمتين المعطاتين {m('9')} و{m('25')}: {m('\\bigl(a_0 b_0 - \\sum_{i=1}^3 x_i y_i\\bigr)^2 \\ge 9 \\times 25 = 225')}.",
                f"بأخذ الجذر التربيعي الموجب نجد {m('a_0 b_0 - \\sum_{i=1}^3 x_i y_i \\ge 15')}، وتتحقق المساواة عند تناسب المتجهين بنسبة {m('5 : 3')}.",
            ],
            check_ar=(
                f"باختيار {m('a_0 = 5, x_1 = 4')} والبقية أصفاراً، و{m('b_0 = 25/3, y_1 = 20/3')}، نجد {m('a_0 b_0 - x_1 y_1 = 125/3 - 80/3 = 15')}."
            ),
            diagram_en=svg_olym_inequality_curve("9", "25", "min = ?"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-03",
        level=LEVEL_T3,
        unit_num="3.3",
        topic="Inequalities",
        title_en="Hölder, Schur & Algebraic Supporting-Line Inequalities",
        title_ar="متباينات هولدر وشور وخطوط الإسناد الجبرية",
        summary_en=(
            "Conquer Senior Olympiad Inequalities using multi-bracket Hölder and Power Means, "
            "Schur and Muirhead majorization with uvw reductions, algebraic supporting-line factorizations, and Aczél's inequality."
        ),
        summary_ar=(
            "أتقن متباينات الأولمبياد المتقدم باستخدام متباينة هولدر والمتوسطات الأسية، "
            "ومتباينة شور وتغلب مويرهيد وطريقة uvw، وتحليل خطوط الإسناد الجبرية، ومتباينة أتشيل."
        ),
        goals_en=[
            f"Eliminate radicals and asymmetric denominators using 3-bracket Hölder's inequality and the Power Mean chain {m('M_p \\le M_q')}.",
            f"Apply degree-1 Schur {m('p^3 - 4pq + 9r \\ge 0')}, Muirhead majorization, and {m('uvw')} extremal reductions.",
            f"Bound additive sums via Jensen's convexity inequality and the algebraic supporting-line factorization {m('(x - x_0)^2 Q(x) \\ge 0')}.",
            f"Use Aczél's inequality and weight-balanced Cauchy–Schwarz to solve constrained extremal problems.",
        ],
        goals_ar=[
            f"إزالة الجذور والمقامات غير المتماثلة عبر متباينة هولدر الثلاثية وسلسلة المتوسطات الأسية {m('M_p \\le M_q')}.",
            f"تطبيق متباينة شور {m('p^3 - 4pq + 9r \\ge 0')} وتغلب مويرهيد واختزالات {m('uvw')} الحدية.",
            f"تقدير المجاميع الجمعية عبر متباينة ينسن للتحدب وتحليل خط الإسناد الجبري {m('(x - x_0)^2 Q(x) \\ge 0')}.",
            f"توظيف متباينة أتشيل وموازنة الأوزان في كوشي-شوارتز لحل مسائل القيم القصوى المقيدة.",
        ],
        concepts=concepts,
        traps_en=[
            f"Applying Muirhead's majorization theorem to 3-term **cyclic** sums instead of full 6-term **symmetric** sums.",
            f"Using a linear supporting bound {m('f(x) \\ge f(x_0) + m(x - x_0)')} without verifying that the quotient {m('Q(x)')} in {m('(x - x_0)^2 Q(x)')} stays non-negative across the entire domain.",
            f"Forgetting that degree-1 Schur {m('p^3 - 4pq + 9r \\ge 0')} achieves equality not only at {m('x = y = z')} but also on the boundary {m('(t, t, 0)')}.",
        ],
        traps_ar=[
            f"تطبيق مبرهنة التغلب لمويرهيد على مجاميع **دورية** من 3 حدود بدلاً من المجاميع **المتماثلة** الكاملة ذات 6 حدود.",
            f"استخدام خط إسناد {m('f(x) \\ge f(x_0) + m(x - x_0)')} دون التحقق من أن العامل {m('Q(x)')} في {m('(x - x_0)^2 Q(x)')} غير سالب على كامل المجال.",
            f"إغفال أن متباينة شور {m('p^3 - 4pq + 9r \\ge 0')} تحقق المساواة عند الحالة الحدية {m('(t, t, 0)')} بالإضافة إلى {m('x = y = z')}.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_ineq_holder_power_means",
            "olym_t3_ineq_schur_muirhead_uvw",
            "olym_t3_ineq_jensen_tangent_line",
            "olym_t3_ineq_aczel_lagrange_opt",
        ],
    )


# ==============================================================================
# OLYM-L3-04: Geometry (Incenter-Excenter, Simson/Harmonic, Inversion, Bary)
# ==============================================================================

def _lesson_l3_04() -> dict:
    concepts = [
        olym_concept(
            title_en="The Incenter–Excenter Lemma & Harmonic Bundles",
            title_ar="توطئة المركز الداخلي والخارجي والحزم التوافقية",
            body_en=(
                f"Let {m('M')} be the midpoint of arc {m('BC')} of {m('(ABC)')} not containing {m('A')}. The **Incenter–Excenter Lemma** states that {m('M')} is the circumcenter of "
                f"cyclic quadrilateral {m('BICI_A')}, so {m('MB = MI = MC = MI_A = 2R\\sin(A/2)')} and {m('M')} bisects {m('II_A')}. "
                f"For any point {m('P \\in (ABC)')}, its pedal projections onto the three sidelines are collinear along the **Simson line**. "
                f"Four collinear points satisfy the **harmonic bundle** relation {m('(B, C; D, E) = -1')} when {m('\\frac{BD}{DC} = \\frac{BE}{EC}')}, notably when {m('AD, AE')} are the internal and external bisectors of {m('\\angle A')}."
            ),
            body_ar=(
                f"لتكن {m('M')} منتصف القوس {m('BC')} من الدائرة المحيطة {m('(ABC)')} الذي لا يحوي {m('A')}. تنص **توطئة المركز الداخلي والخارجي** على أن {m('M')} هي مركز الدائرة المارة برؤوس الرباعي الدائري "
                f"{m('BICI_A')}، بحيث {m('MB = MI = MC = MI_A = 2R\\sin(A/2)')} وتكون {m('M')} منتصف القطعة {m('II_A')}. "
                f"ولكل نقطة {m('P \\in (ABC)')} تقع مساقطها العمودية على أضلاع المثلث على استقامة واحدة هي **خط سيمسون**. "
                f"وتشكّل أربع نقاط مستقيمية **حزمة توافقية** {m('(B, C; D, E) = -1')} إذا كان {m('\\frac{BD}{DC} = \\frac{BE}{EC}')}، كما يحدث عند تقاطع المنصّفين الداخلي والخارجي للزاوية {m('A')} مع {m('BC')}."
            ),
            formula_en=dm(
                r"MB = MI = MC = MI_A = 2R\sin\frac{A}{2}, \qquad (B, C; D, E) = -1 \iff \frac{BD}{DC} = \frac{BE}{EC}"
            ),
            caption_ar="توطئة المركز الداخلي والخارجي وشرط القسمة التوافقية:",
            formula_math_ar=dm(
                r"MB = MI = MC = MI_A = 2R\sin\frac{A}{2}, \qquad \frac{BD}{DC} = \frac{BE}{EC}"
            ),
            diagram_en=svg_olym_incircle_excircle("BC", "CA", "AB", "MB = MI = MC"),
        ),
        olym_concept(
            title_en="Spiral Similarity & Circular Inversion",
            title_ar="التشابه الحلزوني والانعكاس الدائري",
            body_en=(
                f"A **spiral similarity** {m('\\mathcal{S}(S, k, \\theta)')} rotates by {m('\\theta')} and scales by {m('k')} around center {m('S')}; "
                f"if {m('\\mathcal{S}')} maps {m('AB \\mapsto CD')}, then a conjugate spiral similarity at the same center {m('S')} maps {m('AC \\mapsto BD')} ({m('\\triangle SAB \\sim \\triangle SCD \\iff \\triangle SAC \\sim \\triangle SBD')}). "
                f"**Circular inversion** with respect to circle {m('(O, R)')} sends {m('P \\mapsto P\'')} on ray {m('OP')} with {m('OP \\cdot OP\' = R^2')}. "
                f"Because {m('\\triangle OAB \\sim \\triangle OB\'A\'')}, chord lengths transform by {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB')}, and circles through {m('O')} invert into straight lines."
            ),
            body_ar=(
                f"يقوم **التشابه الحلزوني** {m('\\mathcal{S}(S, k, \\theta)')} بدوران زاويته {m('\\theta')} وتحاكٍ نسبته {m('k')} حول المركز {m('S')}؛ "
                f"فإذا حوّل {m('AB \\mapsto CD')} فإن تشابهاً حلزونياً مرافقاً حول المركز {m('S')} نفسه يحوّل {m('AC \\mapsto BD')} ({m('\\triangle SAB \\sim \\triangle SCD \\iff \\triangle SAC \\sim \\triangle SBD')}). "
                f"أما **الانعكاس الدائري** حول الدائرة {m('(O, R)')} فيحوّل {m('P \\mapsto P\'')} على نصف المستقيم {m('OP')} بحيث {m('OP \\cdot OP\' = R^2')}. "
                f"ومن تشابه المثلثين {m('\\triangle OAB \\sim \\triangle OB\'A\'')} تتحول المسافات وفق القانون {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB')}."
            ),
            formula_en=dm(
                r"OP \cdot OP' = R^2, \qquad A'B' = \frac{R^2}{OA \cdot OB}\,AB, \qquad \triangle SAB \sim \triangle SCD \iff \triangle SAC \sim \triangle SBD"
            ),
            caption_ar="قانون المسافة في الانعكاس الدائري وازدواجية التشابه الحلزوني:",
            formula_math_ar=dm(
                r"OP \cdot OP' = R^2, \qquad A'B' = \frac{R^2}{OA \cdot OB}\,AB"
            ),
            diagram_en=svg_olym_spiral_homothety("k, θ", "S"),
        ),
        olym_concept(
            title_en="Barycentric Coordinates & Vector Length Chasing",
            title_ar="الإحداثيات المرجحية وحساب الأطوال المتجهية",
            body_en=(
                f"In normalized **barycentric coordinates** {m('P = (x, y, z)')} with {m('x + y + z = 1')}, {m('\\vec{P} = x\\vec{A} + y\\vec{B} + z\\vec{C}')}. "
                f"For any displacement {m('\\vec{v} = P - Q = (\\Delta x, \\Delta y, \\Delta z)')} (so {m('\\Delta x + \\Delta y + \\Delta z = 0')}), the squared length is "
                f"{m('|P - Q|^2 = -a^2 \\Delta y\\,\\Delta z - b^2 \\Delta z\\,\\Delta x - c^2 \\Delta x\\,\\Delta y')}. "
                f"Measuring from the circumcenter {m('O')} yields the fundamental identity {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}, "
                f"which immediately gives {m('R^2 - OG^2 = \\frac{a^2 + b^2 + c^2}{9}')} at {m('G = (\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3})')} and {m('R^2 - OI^2 = 2Rr')} at {m('I = \\frac{1}{2s}(a, b, c)')}."
            ),
            body_ar=(
                f"في **الإحداثيات المرجحية المعيّرة** {m('P = (x, y, z)')} حيث {m('x + y + z = 1')}، يكون {m('\\vec{P} = x\\vec{A} + y\\vec{B} + z\\vec{C}')}. "
                f"ولأي متجه إزاحة {m('\\vec{v} = P - Q = (\\Delta x, \\Delta y, \\Delta z)')} (بحيث {m('\\Delta x + \\Delta y + \\Delta z = 0')}) يُعطى مربع الطول بالصيغة "
                f"{m('|P - Q|^2 = -a^2 \\Delta y\\,\\Delta z - b^2 \\Delta z\\,\\Delta x - c^2 \\Delta x\\,\\Delta y')}. "
                f"وعند القياس من مركز الدائرة المحيطة {m('O')} نحصل على المتطابقة الأساسية {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}، "
                f"ومنها نستنتج فوراً {m('R^2 - OG^2 = \\frac{a^2 + b^2 + c^2}{9}')} عند المركز الهندسي {m('G')} و{m('R^2 - OI^2 = 2Rr')} عند المركز الداخلي {m('I')}."
            ),
            formula_en=dm(
                r"|P - Q|^2 = -a^2\Delta y\,\Delta z - b^2\Delta z\,\Delta x - c^2\Delta x\,\Delta y, \qquad R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy"
            ),
            caption_ar="صيغة المسافة المرجحية وعلاقتها بقوة النقطة بالنسبة للدائرة المحيطة:",
            formula_math_ar=dm(
                r"|P - Q|^2 = -a^2\Delta y\,\Delta z - b^2\Delta z\,\Delta x - c^2\Delta x\,\Delta y, \qquad R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy"
            ),
            diagram_en=svg_olym_nine_point_euler("O", "G", "P(x,y,z)"),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-04-EX1",
            title_en="Side-Product Identity via the Incenter–Excenter Circle",
            title_ar="جداء الضلعين عبر دائرة المركز الداخلي والخارجي",
            q_en=(
                f"In {m('\\triangle ABC')}, let {m('I')} be the incenter and let {m('M')} be the midpoint of arc {m('BC')} of the circumcircle {m('(ABC)')} not containing {m('A')}. "
                f"Given that {m('AI = 4')} and {m('MB = 5')}, what is the product {m('AB \\cdot AC')}?"
            ),
            q_ar=(
                f"في المثلث {m('ABC')}، ليكن {m('I')} مركز الدائرة الداخلي ولتكن {m('M')} منتصف القوس {m('BC')} من الدائرة المحيطة {m('(ABC)')} الذي لا يحوي {m('A')}. "
                f"إذا كان {m('AI = 4')} و{m('MB = 5')}، فما قيمة الجداء {m('AB \\cdot AC')}؟"
            ),
            correct_val=56,
            distractors=[20, 36, 45, 70],
            idea_en=(
                f"By the Incenter–Excenter Lemma, {m('MI = MI_A = MB = 5')} so {m('AI_A = 14')}, and cyclic quadrilateral {m('BICI_A')} gives {m('\\triangle ABI \\sim \\triangle AI_A C')}."
            ),
            steps_en=[
                f"Let {m('I_A')} be the {m('A')}-excenter. By the Incenter–Excenter Lemma, {m('M')} is the midpoint of {m('II_A')} and {m('MI = MI_A = MB = 5')}.",
                f"Since {m('A, I, M, I_A')} are collinear in that order along the internal bisector of {m('\\angle A')}, we have {m('AI_A = AI + 2\\,MI = 4 + 10 = 14')}.",
                f"Because {m('B, I, C, I_A')} lie on the circle centered at {m('M')}, inscribed angles give {m('\\angle AI_A C = \\angle II_A C = \\angle IBC = \\angle ABI')}, while {m('\\angle BAI = \\angle I_A AC = A/2')}.",
                f"Thus {m('\\triangle ABI \\sim \\triangle AI_A C')}, so {m('\\frac{AB}{AI_A} = \\frac{AI}{AC} \\implies AB \\cdot AC = AI \\cdot AI_A = 4 \\times 14 = 56')}.",
            ],
            check_en=(
                f"Power of {m('I')} in {m('(ABC)')} is {m('AI \\cdot IM = 4 \\cdot 5 = 20 = 2Rr')}, and {m('AB \\cdot AC - AI^2 = AI \\cdot II_A = 4 \\cdot 10 = 40 \\implies AB \\cdot AC = 16 + 40 = 56')}."
            ),
            idea_ar=(
                f"من توطئة المركز الداخلي والخارجي يكون {m('MI = MI_A = MB = 5')} أي {m('AI_A = 14')}، ومن دائرية {m('BICI_A')} يتشابه المثلثان {m('\\triangle ABI \\sim \\triangle AI_A C')}."
            ),
            steps_ar=[
                f"ليكن {m('I_A')} المركز الخارجي المقابل للرأس {m('A')}؛ من توطئة المركز الداخلي والخارجي تكون {m('M')} منتصف {m('II_A')} و{m('MI = MI_A = MB = 5')}.",
                f"بما أن {m('A, I, M, I_A')} على استقامة واحدة بهذا الترتيب، فإن {m('AI_A = AI + 2\\,MI = 4 + 10 = 14')}.",
                f"من رباعي الدائرة {m('BICI_A')} تتساوى الزاويتان المحيطيتان {m('\\angle AI_A C = \\angle IBC = \\angle ABI')}، كما أن {m('\\angle BAI = \\angle I_A AC')}.",
                f"إذن {m('\\triangle ABI \\sim \\triangle AI_A C')}، ومنه {m('AB \\cdot AC = AI \\cdot AI_A = 4 \\times 14 = 56')}.",
            ],
            check_ar=(
                f"تتحقق المتطابقة {m('AB \\cdot AC - AI^2 = AI \\cdot II_A = 4 \\times 10 = 40')}، ومنه {m('AB \\cdot AC = 16 + 40 = 56')}."
            ),
            diagram_en=svg_olym_incircle_excircle("BC", "AC", "AB", "AB·AC = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-04-EX2",
            title_en="Harmonic Bisector Bundle on a Triangle Baseline",
            title_ar="الحزمة التوافقية لمنصّفي الزاوية الداخلي والخارجي",
            q_en=(
                f"In {m('\\triangle ABC')} with {m('AB = 10')}, {m('AC = 6')}, and {m('BC = 8')}, the internal and external angle bisectors of {m('\\angle A')} "
                f"intersect line {m('BC')} at {m('D')} and {m('E')}, respectively, so that {m('(B, C; D, E) = -1')}. What is the length of segment {m('DE')}?"
            ),
            q_ar=(
                f"في المثلث {m('ABC')} الذي فيه {m('AB = 10')} و{m('AC = 6')} و{m('BC = 8')}، يقطع المنصّفان الداخلي والخارجي للزاوية {m('A')} "
                f"المستقيم {m('BC')} في النقطتين {m('D')} و{m('E')} على الترتيب بحيث {m('(B, C; D, E) = -1')}. ما طول القطعة {m('DE')}؟"
            ),
            correct_val=15,
            distractors=[9, 12, 16, 20],
            idea_en=(
                f"Use the angle-bisector ratio {m('\\frac{BD}{DC} = \\frac{BE}{CE} = \\frac{AB}{AC} = \\frac{5}{3}')} to find {m('DC')} and {m('CE')}, then add {m('DE = DC + CE')}."
            ),
            steps_en=[
                f"By the Internal Angle Bisector Theorem, {m('BD : DC = AB : AC = 10 : 6 = 5 : 3')}. Since {m('BD + DC = 8')}, we get {m('BD = 5')} and {m('DC = 3')}.",
                f"Because {m('(B, C; D, E) = -1')}, {m('E')} lies on ray {m('BC')} beyond {m('C')} with {m('\\frac{BE}{CE} = \\frac{5}{3}')}.",
                f"Substitute {m('BE = BC + CE = 8 + CE')}: {m('\\frac{8 + CE}{CE} = \\frac{5}{3} \\implies 24 + 3\\,CE = 5\\,CE \\implies CE = 12')}.",
                f"Since {m('C')} lies between {m('D')} and {m('E')}, {m('DE = DC + CE = 3 + 12 = 15')}.",
            ],
            check_en=(
                f"Notice {m('6^2 + 8^2 = 10^2')} so {m('\\angle C = 90^\\circ')}; in right {m('\\triangle DAE')} ({m('AD \\perp AE')}), altitude {m('AC')} gives {m('AC^2 = DC \\cdot CE \\implies 36 = 3 \\cdot 12')}, confirming {m('DE = 15')}."
            ),
            idea_ar=(
                f"نستخدم نسبة المنصّف التوافقية {m('\\frac{BD}{DC} = \\frac{BE}{CE} = \\frac{AB}{AC} = \\frac{5}{3}')} لإيجاد {m('DC')} و{m('CE')} ثم نجمع {m('DE = DC + CE')}."
            ),
            steps_ar=[
                f"من مبرهنة المنصّف الداخلي {m('BD : DC = 10 : 6 = 5 : 3')}، وبما أن {m('BC = 8')} نجد {m('BD = 5')} و{m('DC = 3')}.",
                f"من القسمة التوافقية {m('(B, C; D, E) = -1')} تقع {m('E')} على امتداد {m('BC')} بعد {m('C')} وتحقق {m('\\frac{BE}{CE} = \\frac{5}{3}')}.",
                f"نعوّض {m('BE = 8 + CE')} فنجد {m('24 + 3\\,CE = 5\\,CE \\implies CE = 12')}.",
                f"بما أن {m('C')} تقع بين {m('D')} و{m('E')} فإن {m('DE = DC + CE = 3 + 12 = 15')}.",
            ],
            check_ar=(
                f"نلاحظ أن {m('\\angle C = 90^\\circ')} وأن {m('\\angle DAE = 90^\\circ')}، فيكون {m('AC^2 = DC \\cdot CE \\implies 36 = 3 \\times 12')}، مما يؤكد أن {m('DE = 15')}."
            ),
            diagram_en=svg_olym_cyclic_ptolemy("10", "8", "6", "AD⊥AE", "DE = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-04-EX3",
            title_en="Chord Length Transformation under Circular Inversion",
            title_ar="تحويل طول قطعة مستقيمة تحت تأثير الانعكاس الدائري",
            q_en=(
                f"Circular inversion about a circle centered at {m('O')} with radius {m('R = 12')} maps points {m('A')} and {m('B')} to {m('A\'')} and {m('B\'')}, respectively. "
                f"If {m('OA = 8')}, {m('OB = 9')}, and {m('AB = 10')}, what is the length of segment {m('A\'B\'')}?"
            ),
            q_ar=(
                f"يحوّل انعكاس دائري مركزه {m('O')} ونصف قطره {m('R = 12')} النقطتين {m('A')} و{m('B')} إلى {m('A\'')} و{m('B\'')} على الترتيب. "
                f"إذا كان {m('OA = 8')} و{m('OB = 9')} و{m('AB = 10')}، فما طول القطعة {m('A\'B\'')}؟"
            ),
            correct_val=20,
            distractors=[12, 15, 18, 24],
            idea_en=(
                f"Apply the inversion distance formula {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB')} derived from {m('\\triangle OAB \\sim \\triangle OB\'A\'')}."
            ),
            steps_en=[
                f"By definition of inversion, {m('OA \\cdot OA\' = OB \\cdot OB\' = R^2 = 144')}, so {m('OA\' = 18')} and {m('OB\' = 16')}.",
                f"Because {m('\\frac{OA\'}{OB} = \\frac{18}{9} = 2 = \\frac{16}{8} = \\frac{OB\'}{OA}')} and {m('\\angle AOB = \\angle B\'OA\'')}, we have {m('\\triangle OAB \\sim \\triangle OB\'A\'')} with scale factor {m('2')}.",
                f"Equivalently, {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB = \\frac{144}{8 \\times 9} \\times 10')}.",
                f"Evaluating gives {m('A\'B\' = 2 \\times 10 = 20')}.",
            ],
            check_en=(
                f"The side lengths of {m('\\triangle OB\'A\'')} are {m('OB\' = 16 = 2 \\cdot OA')}, {m('OA\' = 18 = 2 \\cdot OB')}, so the third side must be {m('A\'B\' = 2 \\cdot AB = 20')}."
            ),
            idea_ar=(
                f"نطبّق صيغة المسافة في الانعكاس الدائري {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB')} الناتجة عن تشابه {m('\\triangle OAB \\sim \\triangle OB\'A\'')}."
            ),
            steps_ar=[
                f"من تعريف الانعكاس الدائري: {m('OA \\cdot OA\' = OB \\cdot OB\' = R^2 = 144')}، ومنه {m('OA\' = 18')} و{m('OB\' = 16')}.",
                f"بما أن {m('\\frac{OA\'}{OB} = \\frac{OB\'}{OA} = 2')} والزاوية {m('\\angle AOB')} مشتركة، فإن {m('\\triangle OAB \\sim \\triangle OB\'A\'')} بنسبة تشابه {m('2')}.",
                f"وبالتعويض المباشر في الصيغة: {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}\\,AB = \\frac{144}{8 \\times 9} \\times 10')}.",
                f"إذن {m('A\'B\' = 2 \\times 10 = 20')}.",
            ],
            check_ar=(
                f"أضلاع المثلث {m('\\triangle OB\'A\'')} هي {m('16 = 2 \\times 8')} و{m('18 = 2 \\times 9')}، فيكون الضلع الثالث {m('2 \\times 10 = 20')}."
            ),
            diagram_en=svg_olym_spiral_homothety("A'B' = ?", "O"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-04-EX4",
            title_en="Circumcenter–Centroid Power via Barycentric Coordinates",
            title_ar="قوة المركز الهندسي بالنسبة للدائرة المحيطة بالإحداثيات المرجحية",
            q_en=(
                f"In {m('\\triangle ABC')} with side lengths {m('a = 8')}, {m('b = 7')}, and {m('c = 11')}, let {m('O')} be the circumcenter, "
                f"{m('G')} be the centroid, and {m('R')} be the circumradius. What is the exact value of {m('R^2 - OG^2')}?"
            ),
            q_ar=(
                f"في المثلث {m('ABC')} الذي أطوال أضلاعه {m('a = 8')} و{m('b = 7')} و{m('c = 11')}، ليكن {m('O')} مركز الدائرة المحيطة، "
                f"و{m('G')} المركز الهندسي (تلاقي المتوسطات)، و{m('R')} نصف قطر الدائرة المحيطة. ما القيمة الدقيقة للمقدار {m('R^2 - OG^2')}؟"
            ),
            correct_val=26,
            distractors=[22, 24, 28, 39],
            idea_en=(
                f"Substitute the normalized barycentric coordinates {m('G = \\left(\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}\\right)')} into {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}."
            ),
            steps_en=[
                f"In normalized barycentric coordinates, the centroid is {m('G = \\left(\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}\\right)')}.",
                f"Applying {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')} at {m('P = G')} gives {m('R^2 - OG^2 = \\frac{a^2 + b^2 + c^2}{9}')}.",
                f"Compute the sum of squared sides: {m('a^2 + b^2 + c^2 = 8^2 + 7^2 + 11^2 = 64 + 49 + 121 = 234')}.",
                f"Divide by {m('9')}: {m('R^2 - OG^2 = \\frac{234}{9} = 26')}.",
            ],
            check_en=(
                f"Check {m('9 \\times 26 = 234 = 64 + 49 + 121')}, and {m('7 + 8 = 15 > 11')} confirms {m('\\triangle ABC')} is a non-degenerate triangle."
            ),
            idea_ar=(
                f"نعوّض الإحداثيات المرجحية المعيّرة للمركز الهندسي {m('G = \\left(\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}\\right)')} في العلاقة {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}."
            ),
            steps_ar=[
                f"في الإحداثيات المرجحية المعيّرة، يُمثَّل المركز الهندسي بالثلاثية {m('G = \\left(\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}\\right)')}.",
                f"بتطبيق الصيغة {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')} عند {m('P = G')} نجد {m('R^2 - OG^2 = \\frac{a^2 + b^2 + c^2}{9}')}.",
                f"نحسب مجموع مربعات الأضلاع: {m('a^2 + b^2 + c^2 = 64 + 49 + 121 = 234')}.",
                f"بقسمة الناتج على {m('9')}: {m('R^2 - OG^2 = \\frac{234}{9} = 26')}.",
            ],
            check_ar=(
                f"نتحقق من أن {m('9 \\times 26 = 234 = 64 + 49 + 121')}، وأن متباينة المثلث {m('7 + 8 > 11')} محققة."
            ),
            diagram_en=svg_olym_nine_point_euler("O", "G", "R²−OG² = ?"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-04",
        level=LEVEL_T3,
        unit_num="3.4",
        topic="Geometry",
        title_en="Incenter–Excenter, Spiral Similarity, Inversion & Barycentrics",
        title_ar="توطئة المركز الداخلي والخارجي، التشابه الحلزوني، الانعكاس الدائري، والإحداثيات المرجحية",
        summary_en=(
            "Unlock synthetic and coordinate Olympiad Geometry: the Incenter–Excenter circle, Simson lines and harmonic bundles, "
            "spiral similarities and circular inversion, and barycentric displacement length formulas."
        ),
        summary_ar=(
            "أتقن الهندسة التركيبية والإحداثية للأولمبياد: دائرة المركز الداخلي والخارجي، وخطوط سيمسون والحزم التوافقية، "
            "والتشابه الحلزوني والانعكاس الدائري، وصيغ المسافات في الإحداثيات المرجحية."
        ),
        goals_en=[
            f"Apply the Incenter–Excenter Lemma {m('MB = MI = MC = MI_A = 2R\\sin(A/2)')} around arc midpoint {m('M')}.",
            f"Use Simson lines, Miquel points, and harmonic cross-ratios {m('(B, C; D, E) = -1')} to prove collinearity and compute lengths.",
            f"Transform geometric figures via spiral similarity {m('\\mathcal{S}(S, k, \\theta)')} and circular inversion {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}AB')}.",
            f"Evaluate distances between triangle centers using normalized barycentric coordinates and {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}.",
        ],
        goals_ar=[
            f"تطبيق توطئة المركز الداخلي والخارجي {m('MB = MI = MC = MI_A = 2R\\sin(A/2)')} حول منتصف القوس {m('M')}.",
            f"استخدام خطوط سيمسون ونقاط ميكيل والنسب التوافقية {m('(B, C; D, E) = -1')} لإثبات الاستقامية وحساب الأطوال.",
            f"تحويل الأشكال الهندسية عبر التشابه الحلزوني {m('\\mathcal{S}(S, k, \\theta)')} والانعكاس الدائري {m('A\'B\' = \\frac{R^2}{OA \\cdot OB}AB')}.",
            f"حساب المسافات بين مراكز المثلث عبر الإحداثيات المرجحية المعيّرة والعلاقة {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')}.",
        ],
        concepts=concepts,
        traps_en=[
            f"Plugging unnormalized homogeneous coordinates {m('(u : v : w)')} into {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')} without dividing by {m('u + v + w')} first.",
            f"Assuming the center of an inverted circle is the inverse of the original circle's center: inversion preserves circles (not through {m('O')}), not their centers.",
            f"Placing {m('M')} at the midpoint of segment {m('BC')} instead of the midpoint of circumcircle arc {m('BC')} in the Incenter–Excenter Lemma.",
        ],
        traps_ar=[
            f"تعويض إحداثيات مرجحية غير معيّرة {m('(u : v : w)')} مباشرةً في {m('R^2 - OP^2 = a^2 yz + b^2 zx + c^2 xy')} قبل القسمة على {m('u + v + w')}.",
            f"افتراض أن مركز الدائرة المنعكسة هو صورة مركز الدائرة الأصلية بالانعكاس؛ فالانعكاس يحفظ الدوائر ولا يحفظ مراكزها.",
            f"وضع النقطة {m('M')} في منتصف الضلع {m('BC')} بدلاً من منتصف القوس {m('BC')} من الدائرة المحيطة عند تطبيق توطئة المركز الداخلي والخارجي.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_geo_incenter_excenter_lemma",
            "olym_t3_geo_simson_miquel_harmonic",
            "olym_t3_geo_spiral_sim_inversion",
            "olym_t3_geo_barycentric_vector_len",
        ],
    )



# ==============================================================================
# OLYM-L3-05: Geometry (Projective, 3D Tetrahedra, Helly/Hull, Extremals)
# ==============================================================================

def _lesson_l3_05() -> dict:
    concepts = [
        olym_concept(
            title_en="Desargues's Theorem, Pascal's Hexagram & Brianchon Duality",
            title_ar="مبرهنة ديزارغ ومسدس باسكال وثنائية بريانشون",
            body_en=(
                f"**Desargues's Theorem** states that triangles {m('\\triangle ABC')} and {m('\\triangle A\'B\'C\'')} are perspective from a point "
                f"{m('P = AA\' \\cap BB\' \\cap CC\'')} if and only if the intersections of corresponding sidelines {m('AB \\cap A\'B\'')}, {m('BC \\cap B\'C\'')}, and {m('CA \\cap C\'A\'')} are collinear along the Desargues axis. "
                f"**Pascal's Theorem** states that for any hexagon {m('ABCDEF')} inscribed in a circle or conic, opposite side intersections {m('X = AB \\cap DE')}, {m('Y = BC \\cap EF')}, and {m('Z = CD \\cap FA')} are collinear (allowing tangent lines when adjacent vertices merge), "
                f"while **Brianchon's dual** asserts that in a circumscribed hexagon, the main diagonals {m('AD, BE, CF')} concur."
            ),
            body_ar=(
                f"تنص **مبرهنة ديزارغ** على أن المثلثين {m('\\triangle ABC')} و{m('\\triangle A\'B\'C\'')} متناظران من نقطة "
                f"{m('P = AA\' \\cap BB\' \\cap CC\'')} إذا وفقط إذا كانت نقاط تقاطع الأضلاع المتناظرة {m('AB \\cap A\'B\'')} و{m('BC \\cap B\'C\'')} و{m('CA \\cap C\'A\'')} على استقامة واحدة (محور ديزارغ). "
                f"وتنص **مبرهنة باسكال** على أنه لأي مسدس {m('ABCDEF')} محاط بدائرة أو قطع مخروطي تقع تقاطعات الأضلاع المتقابلة {m('X = AB \\cap DE')} و{m('Y = BC \\cap EF')} و{m('Z = CD \\cap FA')} على استقامة واحدة (مع استبدال الضلع بمماس عند انطباق رأسين)، "
                f"بينما تقرر **ثنائية بريانشون** تلاقي الأقطار الرئيسة {m('AD, BE, CF')} للمسدس المماس لدائرة."
            ),
            formula_en=dm(
                r"X = AB \cap DE,\;\; Y = BC \cap EF,\;\; Z = CD \cap FA \implies X, Y, Z\text{ are collinear}"
            ),
            caption_ar="شرط استقامية خط باسكال للمسدس الدائري:",
            formula_math_ar=dm(
                r"X = AB \cap DE,\;\; Y = BC \cap EF,\;\; Z = CD \cap FA \implies X, Y, Z\text{ collinear}"
            ),
            diagram_en=_svg_pascal_hexagon("Pascal Line: X, Y, Z"),
        ),
        olym_concept(
            title_en="3D Tetrahedra, Orthogonal Edges & the Cayley–Menger Edge-Square Formula",
            title_ar="رباعيات الوجوه الفضائية، الأحرف المتعامدة، وصيغة كيلي-منغر الحجمية",
            body_en=(
                f"In a 3D tetrahedron {m('ABCD')}, opposite edges {m('AB')} and {m('CD')} are perpendicular in space iff {m('AC^2 + BD^2 = AD^2 + BC^2')}; "
                f"if two opposite pairs are orthogonal, so is the third (**orthocentric tetrahedron**). The **bimedian** connecting the midpoints of {m('AB')} and {m('CD')} satisfies "
                f"{m('m_{AB,CD}^2 = \\frac{1}{4}(AC^2 + AD^2 + BC^2 + BD^2 - AB^2 - CD^2)')}. "
                f"For an **equifacial tetrahedron** with opposite edge pairs {m('a, b, c')}, the Cayley–Menger edge-square volume formula simplifies via box embedding to "
                f"{m('72 V^2 = (a^2 + b^2 - c^2)(b^2 + c^2 - a^2)(c^2 + a^2 - b^2)')}."
            ),
            body_ar=(
                f"في رباعي الوجوه الفضائي {m('ABCD')}، يتعامد الحرفان المتقابلان {m('AB')} و{m('CD')} في الفضاء إذا وفقط إذا كان {m('AC^2 + BD^2 = AD^2 + BC^2')}؛ "
                f"وإذا تعامد زوجان من الأحرف المتقابلة تعامد الزوج الثالث تلقائياً. ويحقق **المتوسط الثنائي** الواصل بين منتصفي {m('AB')} و{m('CD')} العلاقة "
                f"{m('m_{AB,CD}^2 = \\frac{1}{4}(AC^2 + AD^2 + BC^2 + BD^2 - AB^2 - CD^2)')}. "
                f"ولرباعي الوجوه **متساوي الوجوه** ذي الأزواج المتقابلة {m('a, b, c')}، تتبسط صيغة كيلي-منغر لمربعات الأحرف عبر الغمر في متوازي مستطيلات إلى "
                f"{m('72 V^2 = (a^2 + b^2 - c^2)(b^2 + c^2 - a^2)(c^2 + a^2 - b^2)')}."
            ),
            formula_en=dm(
                r"AB \perp CD \iff AC^2 + BD^2 = AD^2 + BC^2, \qquad 72V^2 = (a^2+b^2-c^2)(b^2+c^2-a^2)(c^2+a^2-b^2)"
            ),
            caption_ar="شرط تعامد الأحرف المتقابلة وصيغة مربعات الأحرف لحجم رباعي الوجوه متساوي الوجوه:",
            formula_math_ar=dm(
                r"AB \perp CD \iff AC^2 + BD^2 = AD^2 + BC^2, \qquad 72V^2 = (a^2+b^2-c^2)(b^2+c^2-a^2)(c^2+a^2-b^2)"
            ),
            diagram_en=svg_olym_tetrahedron_3d("a", "b", "V"),
        ),
        olym_concept(
            title_en="Helly's Theorem, Convex Hulls & Fagnano's Reflection Extremal",
            title_ar="مبرهنة هيلي، والغلاف المحدب، ومسألة فانيانو القصوى بالانعكاس",
            body_en=(
                f"**Helly's Theorem** states that if a finite collection of {m('N \\ge d + 1')} convex sets in {m('\\mathbb{R}^d')} has the property that every {m('d + 1')} of them have a non-empty intersection, "
                f"then the intersection of all {m('N')} sets is non-empty (in the plane {m('\\mathbb{R}^2')}, every {m('3')} sets intersect {m('\\implies')} all intersect). "
                f"In extremal geometry, **Fagnano's Problem** asks for the inscribed triangle {m('\\triangle DEF')} of minimum perimeter inside an acute {m('\\triangle ABC')}: "
                f"reflecting {m('D')} across {m('AB')} and {m('AC')} unfolds the perimeter into a chord of length {m('2\\,AD\\sin A')}, minimized at the **orthic triangle** with perimeter {m('\\frac{2[ABC]}{R}')}."
            ),
            body_ar=(
                f"تنص **مبرهنة هيلي** على أنه إذا كانت لدينا جماعة منتهية من {m('N \\ge d + 1')} مجموعات محدبة في {m('\\mathbb{R}^d')} بحيث تتقاطع كل {m('d + 1')} منها في نقطة مشتركة على الأقل، "
                f"فإن تقاطع جميع المجموعات غير خالٍ (وفي المستوي {m('\\mathbb{R}^2')} يكفي تقاطع كل {m('3')} مجموعات). "
                f"وفي الهندسة القصوى، تبحث **مسألة فانيانو** عن أصغر محيط لمثلث {m('\\triangle DEF')} محاط بمثلث حاد الزوايا {m('\\triangle ABC')}: "
                f"فعند عكس {m('D')} حول {m('AB')} و{m('AC')} ينفرد المحيط إلى وتر طوله {m('2\\,AD\\sin A')}، ويبلغ أصغره عند **المثلث الارتفاعي** بمحيط قدره {m('\\frac{2[ABC]}{R}')}."
            ),
            formula_en=dm(
                r"\bigcap_{i \in I} C_i \neq \emptyset\;\;(\forall\,|I|=d+1) \implies \bigcap_{k=1}^N C_k \neq \emptyset, \qquad "
                r"\min \operatorname{Perim}(\triangle DEF) = 2h_a\sin A = \frac{2[ABC]}{R}"
            ),
            caption_ar="مبرهنة هيلي للمجموعات المحدبة وأصغر محيط للمثلث الارتفاعي (فانيانو):",
            formula_math_ar=dm(
                r"\bigcap_{i \in I} C_i \neq \emptyset\;\;(\forall\,|I|=d+1) \implies \bigcap_{k=1}^N C_k \neq \emptyset, \qquad "
                r"\min \operatorname{Perim}(\triangle DEF) = \frac{2[ABC]}{R}"
            ),
            diagram_en=_svg_convex_hull_set("Helly & Convex Hull (d + 1)", ""),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-05-EX1",
            title_en="Desargues Axis & Projective Harmonic Division",
            title_ar="محور ديزارغ والقسمة التوافقية الإسقاطية",
            q_en=(
                f"In {m('\\triangle ABC')}, cevians {m('AD, BE, CF')} concur at a point {m('P')}, with {m('BD = 6')} and {m('DC = 4')}. "
                f"By Desargues's Theorem, the perspective axis of {m('\\triangle ABC')} and {m('\\triangle DEF')} meets line {m('BC')} at {m('X = EF \\cap BC')}, "
                f"forming a harmonic bundle {m('(B, C; D, X) = -1')}. What is the length {m('CX')}?"
            ),
            q_ar=(
                f"في المثلث {m('ABC')} تتلاقى القطع السيفية {m('AD, BE, CF')} في نقطة {m('P')}، حيث {m('BD = 6')} و{m('DC = 4')}. "
                f"بموجب مبرهنة ديزارغ يقطع محور التناظر للمثلثين {m('\\triangle ABC')} و{m('\\triangle DEF')} المستقيم {m('BC')} في {m('X = EF \\cap BC')} "
                f"مشكلاً حزمة توافقية {m('(B, C; D, X) = -1')}. ما طول القطعة {m('CX')}؟"
            ),
            correct_val=20,
            distractors=[12, 15, 16, 24],
            idea_en=(
                f"Combine Ceva's Theorem on {m('AD, BE, CF')} and Menelaus's Theorem on line {m('EFX')} to get {m('\\frac{BX}{CX} = \\frac{BD}{DC} = \\frac{3}{2}')}."
            ),
            steps_en=[
                f"By Ceva's Theorem on concurrent cevians {m('AD, BE, CF')} and Menelaus's Theorem on line {m('EFX')}, {m('\\frac{BX}{CX} = \\frac{BD}{DC} = \\frac{6}{4} = \\frac{3}{2}')}.",
                f"Since {m('BD = 6 > 4 = DC')}, {m('X')} lies on ray {m('BC')} beyond {m('C')}, so {m('BX = BC + CX = 10 + CX')}.",
                f"Substitute into the harmonic ratio: {m('\\frac{10 + CX}{CX} = \\frac{3}{2}')}.",
                f"Cross-multiplying gives {m('20 + 2\\,CX = 3\\,CX \\implies CX = 20')}.",
            ],
            check_en=(
                f"With {m('CX = 20')}, {m('BX = 30')}, and {m('\\frac{BX}{CX} = \\frac{30}{20} = \\frac{3}{2} = \\frac{6}{4} = \\frac{BD}{DC}')}."
            ),
            idea_ar=(
                f"نجمع بين مبرهنة سيفا للقطع المتلاقية ومبرهنة منيلاوس للمستقيم {m('EFX')} لنحصل على {m('\\frac{BX}{CX} = \\frac{BD}{DC} = \\frac{3}{2}')}."
            ),
            steps_ar=[
                f"من مبرهنة سيفا ومبرهنة منيلاوس على المستقيم القاطع {m('EFX')} نجد {m('\\frac{BX}{CX} = \\frac{BD}{DC} = \\frac{6}{4} = \\frac{3}{2}')}.",
                f"بما أن {m('BC = 6 + 4 = 10')} وتقع {m('X')} على امتداد {m('BC')} بعد {m('C')}، فإن {m('BX = 10 + CX')}.",
                f"نعوّض في تناسب الحزمة التوافقية: {m('\\frac{10 + CX}{CX} = \\frac{3}{2}')}.",
                f"بالضرب التبادلي نجد {m('20 + 2\\,CX = 3\\,CX \\implies CX = 20')}.",
            ],
            check_ar=(
                f"عند {m('CX = 20')} يكون {m('BX = 30')}، وتتحقق النسبة {m('\\frac{30}{20} = \\frac{3}{2} = \\frac{6}{4}')}."
            ),
            diagram_en=_svg_pascal_hexagon("Desargues Axis: CX = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-05-EX2",
            title_en="Volume of an Equifacial Tetrahedron via Edge-Square Formula",
            title_ar="حجم رباعي وجوه متساوي الوجوه عبر صيغة مربعات الأحرف",
            q_en=(
                f"An equifacial tetrahedron {m('ABCD')} has opposite edge lengths {m('AB = CD = \\sqrt{13}')}, "
                f"{m('AC = BD = \\sqrt{20}')}, and {m('AD = BC = 5')}. What is the volume {m('V')} of tetrahedron {m('ABCD')}?"
            ),
            q_ar=(
                f"في رباعي الوجوه متساوي الوجوه {m('ABCD')} أطوال الأحرف المتقابلة هي {m('AB = CD = \\sqrt{13}')}، "
                f"و{m('AC = BD = \\sqrt{20}')}، و{m('AD = BC = 5')}. ما حجم رباعي الوجوه {m('V')}؟"
            ),
            correct_val=8,
            distractors=[6, 12, 16, 24],
            idea_en=(
                f"Apply the Cayley–Menger edge-square volume identity {m('72 V^2 = (a^2 + b^2 - c^2)(b^2 + c^2 - a^2)(c^2 + a^2 - b^2)')} with {m('a^2 = 13, b^2 = 20, c^2 = 25')}."
            ),
            steps_en=[
                f"Set {m('a^2 = 13')}, {m('b^2 = 20')}, and {m('c^2 = 25')}.",
                f"Compute the three pairwise combinations: {m('a^2 + b^2 - c^2 = 13 + 20 - 25 = 8')}, {m('b^2 + c^2 - a^2 = 20 + 25 - 13 = 32')}, and {m('c^2 + a^2 - b^2 = 25 + 13 - 20 = 18')}.",
                f"Substitute into {m('72 V^2 = 8 \\times 32 \\times 18 = 4608')}.",
                f"Divide by {m('72')}: {m('V^2 = \\frac{4608}{72} = 64 \\implies V = 8')}.",
            ],
            check_en=(
                f"Equivalently, {m('ABCD')} inscribes in a cuboid of sides {m('x=2, y=3, z=4')} (since {m('2^2+3^2=13')}, {m('3^2+4^2=25')}, {m('2^2+4^2=20')}), giving {m('V = \\frac{1}{3}xyz = \\frac{24}{3} = 8')}."
            ),
            idea_ar=(
                f"نطبّق صيغة كيلي-منغر لمربعات الأحرف {m('72 V^2 = (a^2 + b^2 - c^2)(b^2 + c^2 - a^2)(c^2 + a^2 - b^2)')} مع {m('a^2 = 13, b^2 = 20, c^2 = 25')}."
            ),
            steps_ar=[
                f"نضع {m('a^2 = 13')} و{m('b^2 = 20')} و{m('c^2 = 25')}.",
                f"نحسب العوامل الثلاثة: {m('a^2 + b^2 - c^2 = 8')}، و{m('b^2 + c^2 - a^2 = 32')}، و{m('c^2 + a^2 - b^2 = 18')}.",
                f"نعوّض في صيغة الحجم: {m('72 V^2 = 8 \\times 32 \\times 18 = 4608')}.",
                f"بالقسمة على {m('72')} نجد {m('V^2 = 64 \\implies V = 8')}.",
            ],
            check_ar=(
                f"بطريقة مكافئة، يُحاط رباعي الوجوه بمتوازي مستطيلات أبعاده {m('2, 3, 4')}، فيكون الحجم {m('V = \\frac{1}{3}(2 \\times 3 \\times 4) = 8')}."
            ),
            diagram_en=svg_olym_tetrahedron_3d("√13", "√20", "V = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-05-EX3",
            title_en="Common Intersection Area of Convex Rectangles via Helly",
            title_ar="مساحة التقاطع المشترك للمستطيلات المحدبة عبر مبرهنة هيلي",
            q_en=(
                f"In {m('\\mathbb{R}^2')}, for each {m('k \\in \\{1, 2, \\dots, 8\\}')}, let {m('R_k')} be the closed rectangle "
                f"{m('[k,\\, k + 10] \\times [2k,\\, k + 20]')}. Every three of these convex sets intersect, so by Helly's Theorem "
                f"{m('I = \\bigcap_{k=1}^{8} R_k')} is non-empty. What is the area of {m('I')}?"
            ),
            q_ar=(
                f"في المستوي {m('\\mathbb{R}^2')}، لكل {m('k \\in \\{1, 2, \\dots, 8\\}')} ليكن {m('R_k')} المستطيل المغلق "
                f"{m('[k,\\, k + 10] \\times [2k,\\, k + 20]')}. تتقاطع كل ثلاثة من هذه المستطيلات المحدبة، فبموجب مبرهنة هيلي يكون تقاطعها الكلي "
                f"{m('I = \\bigcap_{k=1}^{8} R_k')} غير خالٍ. ما مساحة المنطقة {m('I')}؟"
            ),
            correct_val=15,
            distractors=[9, 12, 18, 24],
            idea_en=(
                f"Project onto the {m('x')}- and {m('y')}-axes: the intersection of axis-aligned rectangles is the product of the 1D interval intersections."
            ),
            steps_en=[
                f"Along the {m('x')}-axis, {m('\\bigcap_{k=1}^8 [k, k + 10] = [\\max_{k} k,\\, \\min_{k}(k + 10)] = [8, 11]')}, which has width {m('11 - 8 = 3')}.",
                f"Along the {m('y')}-axis, {m('\\bigcap_{k=1}^8 [2k, k + 20] = [\\max_{k}(2k),\\, \\min_{k}(k + 20)] = [16, 21]')}.",
                f"The vertical intersection has height {m('21 - 16 = 5')}.",
                f"Thus {m('I = [8, 11] \\times [16, 21]')} is a rectangle of area {m('3 \\times 5 = 15')}.",
            ],
            check_en=(
                f"Every {m('(x, y) \\in [8, 11] \\times [16, 21]')} satisfies {m('k \\le 8 \\le x \\le 11 \\le k + 10')} and {m('2k \\le 16 \\le y \\le 21 \\le k + 20')} for all {m('1 \\le k \\le 8')}."
            ),
            idea_ar=(
                f"نسقط المستطيلات على المحورين الأفقي والرأسي: فتقاطع المستطيلات الموازية للمحاور هو جداء تقاطع الفترات الأحادية."
            ),
            steps_ar=[
                f"على محور السينات: {m('\\bigcap_{k=1}^8 [k, k + 10] = [\\max k,\\, \\min(k + 10)] = [8, 11]')} وعرضها {m('11 - 8 = 3')}.",
                f"على محور الصادات: {m('\\bigcap_{k=1}^8 [2k, k + 20] = [\\max(2k),\\, \\min(k + 20)] = [16, 21]')}.",
                f"ارتفاع فترة التقاطع الرأسية يساوي {m('21 - 16 = 5')}.",
                f"إذن {m('I = [8, 11] \\times [16, 21]')} مستطيل مساحته {m('3 \\times 5 = 15')}.",
            ],
            check_ar=(
                f"كل نقطة في {m('[8, 11] \\times [16, 21]')} تحقق {m('k \\le 8 \\le x \\le 11 \\le k + 10')} و{m('2k \\le 16 \\le y \\le 21 \\le k + 20')} لجميع قيم {m('k')}."
            ),
            diagram_en=_svg_convex_hull_set("Helly Intersection I", "Area(I) = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-05-EX4",
            title_en="Minimum Inscribed Perimeter via Fagnano's Orthic Unfolding",
            title_ar="أصغر محيط لمثلث محاط عبر انعكاس فانيانو للمثلث الارتفاعي",
            q_en=(
                f"An acute triangle {m('ABC')} has area {m('[ABC] = 42')} and circumradius {m('R = 6')}. "
                f"Points {m('D, E, F')} are chosen on sides {m('BC, CA, AB')}, respectively. "
                f"What is the minimum possible perimeter of {m('\\triangle DEF')}?"
            ),
            q_ar=(
                f"مثلث حاد الزوايا {m('ABC')} مساحته {m('[ABC] = 42')} ونصف قطر دائرته المحيطة {m('R = 6')}. "
                f"اختيرت النقاط {m('D, E, F')} على الأضلاع {m('BC, CA, AB')} على الترتيب. "
                f"ما أصغر محيط ممكن للمثلث {m('\\triangle DEF')}؟"
            ),
            correct_val=14,
            distractors=[7, 12, 21, 28],
            idea_en=(
                f"Reflect {m('D')} across {m('AB')} and {m('AC')} to unfold the perimeter to {m('2\\,AD\\sin A \\ge 2 h_a \\sin A = \\frac{2[ABC]}{R}')}."
            ),
            steps_en=[
                f"Reflect {m('D')} across {m('AB')} to {m('D_1')} and across {m('AC')} to {m('D_2')}. Then {m('DF + FE + ED = D_1 F + FE + ED_2 \\ge D_1 D_2')}.",
                f"In isosceles {m('\\triangle D_1 A D_2')} with {m('AD_1 = AD_2 = AD')} and {m('\\angle D_1 A D_2 = 2A')}, the base is {m('D_1 D_2 = 2\\,AD\\sin A')}.",
                f"This is minimized when {m('AD = h_a = \\frac{2[ABC]}{a}')} (the altitude from {m('A')}), where {m('\\sin A = \\frac{a}{2R}')}.",
                f"Thus the minimum perimeter is {m('2 h_a \\sin A = 2 \\cdot \\frac{2[ABC]}{a} \\cdot \\frac{a}{2R} = \\frac{2[ABC]}{R} = \\frac{2 \\times 42}{6} = 14')}.",
            ],
            check_en=(
                f"For an equilateral triangle of side {m('a')}, {m('\\frac{2[ABC]}{R} = \\frac{2(\\sqrt{3}/4)a^2}{a/\\sqrt{3}} = \\frac{3}{2}a')}, which matches the medial/orthic perimeter."
            ),
            idea_ar=(
                f"نعكس {m('D')} حول {m('AB')} و{m('AC')} لينفرد المحيط إلى {m('2\\,AD\\sin A \\ge 2 h_a \\sin A = \\frac{2[ABC]}{R}')}."
            ),
            steps_ar=[
                f"نعكس {m('D')} حول {m('AB')} إلى {m('D_1')} وحول {m('AC')} إلى {m('D_2')}، فيكون {m('DF + FE + ED = D_1 F + FE + ED_2 \\ge D_1 D_2')}.",
                f"في المثلث متساوي الساقين {m('\\triangle D_1 A D_2')} حيث {m('AD_1 = AD_2 = AD')} و{m('\\angle D_1 A D_2 = 2A')} يكون {m('D_1 D_2 = 2\\,AD\\sin A')}.",
                f"يتحقق الأصغر عندما يكون {m('AD = h_a = \\frac{2[ABC]}{a}')}، ومن قانون الجيوب {m('\\sin A = \\frac{a}{2R}')}.",
                f"إذن أصغر محيط هو {m('2 h_a \\sin A = \\frac{2[ABC]}{R} = \\frac{2 \\times 42}{6} = 14')}.",
            ],
            check_ar=(
                f"في المثلث المتطابق الأضلاع طول ضلعه {m('a')} تعطي الصيغة {m('\\frac{2[ABC]}{R} = \\frac{3}{2}a')} وهو محيط المثلث الارتفاعي بالضبط."
            ),
            diagram_en=svg_olym_nine_point_euler("D₁", "F", "min P = ?"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-05",
        level=LEVEL_T3,
        unit_num="3.5",
        topic="Geometry",
        title_en="Projective Theorems, 3D Tetrahedra & Combinatorial Geometry",
        title_ar="الهندسة الإسقاطية، ورباعيات الوجوه الفضائية، والهندسة التوافقية",
        summary_en=(
            "Advance to IMO-level Geometry: Desargues perspective triangles and Pascal's hexagram, "
            "3D tetrahedra and Cayley–Menger edge-square volume formulas, Helly's theorem on convex sets, and Fagnano reflection extremals."
        ),
        summary_ar=(
            "ارتقِ إلى هندسة الأولمبياد العالمي: مبرهنتا ديزارغ وباسكال في الهندسة الإسقاطية، "
            "ورباعيات الوجوه الفضائية وصيغة كيلي-منغر الحجمية، ومبرهنة هيلي للمجموعات المحدبة، والقيم القصوى بالانعكاس."
        ),
        goals_en=[
            f"Prove collinearity and concurrency with Desargues's perspective theorem, Pascal's hexagram, and Brianchon duality.",
            f"Analyze 3D tetrahedra using {m('AB \\perp CD \\iff AC^2 + BD^2 = AD^2 + BC^2')} and the Cayley–Menger edge-square volume formula.",
            f"Apply Helly's Theorem ({m('d + 1')} intersecting convex sets in {m('\\mathbb{R}^d')}) and convex-hull arguments.",
            f"Solve geometric extremal problems via reflection unfolding and Fagnano's orthic-perimeter formula {m('\\frac{2[ABC]}{R}')}.",
        ],
        goals_ar=[
            f"إثبات الاستقامية والتلاقي باستخدام مبرهنة ديزارغ ومسدس باسكال وثنائية بريانشون.",
            f"تحليل رباعيات الوجوه الفضائية عبر {m('AB \\perp CD \\iff AC^2 + BD^2 = AD^2 + BC^2')} وصيغة كيلي-منغر الحجمية.",
            f"تطبيق مبرهنة هيلي ({m('d + 1')} مجموعات محدبة متقاطعة في {m('\\mathbb{R}^d')}) وخواص الغلاف المحدب.",
            f"حل مسائل القيم الهندسية القصوى عبر الانعكاس وصيغة فانيانو لمحيط المثلث الارتفاعي {m('\\frac{2[ABC]}{R}')}.",
        ],
        concepts=concepts,
        traps_en=[
            f"Checking only pairwise intersections instead of {m('d + 1 = 3')} sets at a time when applying Helly's Theorem in {m('\\mathbb{R}^2')}.",
            f"Using {m('\\frac{4[ABC]}{R}')} instead of {m('\\frac{2[ABC]}{R}')} for the orthic triangle perimeter, or applying Fagnano's formula to an obtuse triangle.",
            f"Forgetting the factor of {m('72')} in the equifacial tetrahedron edge-square identity {m('72 V^2 = (a^2+b^2-c^2)(b^2+c^2-a^2)(c^2+a^2-b^2)')}.",
        ],
        traps_ar=[
            f"الاكتفاء بفحص التقاطعات الثنائية بدلاً من تقاطع كل {m('d + 1 = 3')} مجموعات عند تطبيق مبرهنة هيلي في المستوي {m('\\mathbb{R}^2')}.",
            f"استخدام {m('\\frac{4[ABC]}{R}')} بدلاً من {m('\\frac{2[ABC]}{R}')} لمحيط المثلث الارتفاعي، أو تطبيق صيغة فانيانو على مثلث منفرج الزاوية.",
            f"نسيان المعامل {m('72')} في متطابقة حجم رباعي الوجوه متساوي الوجوه {m('72 V^2 = (a^2+b^2-c^2)(b^2+c^2-a^2)(c^2+a^2-b^2)')}.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_geo_projective_desargues_pascal",
            "olym_t3_geo_3d_tetrahedra_cayley",
            "olym_t3_geo_combinatorial_helly_hull",
            "olym_t3_geo_geometric_extremals",
        ],
    )


# ==============================================================================
# OLYM-L3-06: Combinatorics (Turan, Incidence Table, Burnside, Probabilistic)
# ==============================================================================

def _lesson_l3_06() -> dict:
    concepts = [
        olym_concept(
            title_en="Mantel's Theorem & Turán's Extremal Graph Theorem",
            title_ar="مبرهنة مانتل ومبرهنة توران للبيانات القصوى",
            body_en=(
                f"**Mantel's Theorem** proves that an {m('n')}-vertex triangle-free graph has at most {m('\\lfloor n^2/4 \\rfloor')} edges, achieved uniquely by {m('K_{\\lfloor n/2 \\rfloor, \\lceil n/2 \\rceil}')}. "
                f"Generalizing to {m('K_{r+1}')}-free graphs, **Turán's Theorem** shows the maximum edge count is achieved uniquely by the complete {m('r')}-partite **Turán graph** {m('T(n, r)')} "
                f"whose {m('r')} part sizes differ by at most {m('1')}. Its edge count satisfies {m('|E(T(n, r))| = \\binom{n}{2} - \\sum_{i=1}^r \\binom{n_i}{2} \\le \\left(1 - \\frac{1}{r}\\right)\\frac{n^2}{2}')}."
            ),
            body_ar=(
                f"تثبت **مبرهنة مانتل** أن أي بيان خالٍ من المثلثات على {m('n')} رؤوس يحوي على الأكثر {m('\\lfloor n^2/4 \\rfloor')} ضلعاً، ويتحقق الحد الأقصى عند البيان ثنائي التجزئة المتوازن. "
                f"وبالتعميم إلى البيانات الخالية من {m('K_{r+1}')}، تقرر **مبرهنة توران** أن أكبر عدد من الأضلاع يتحقق بوحدانية في **بيان توران** التام ذي {m('r')} أجزاء {m('T(n, r)')} "
                f"الذي تختلف أحجام أجزائه بمقدار لا يتجاوز {m('1')}، وعدد أضلاعه {m('|E(T(n, r))| = \\binom{n}{2} - \\sum_{i=1}^r \\binom{n_i}{2} \\le \\left(1 - \\frac{1}{r}\\right)\\frac{n^2}{2}')}."
            ),
            formula_en=dm(
                r"\operatorname{ex}(n, K_3) = \left\lfloor\frac{n^2}{4}\right\rfloor, \qquad |E(T(n, r))| = \binom{n}{2} - \sum_{i=1}^r \binom{n_i}{2} \le \left(1 - \frac{1}{r}\right)\frac{n^2}{2}"
            ),
            caption_ar="مبرهنة مانتل وصيغة عدد أضلاع بيان توران المتوازن:",
            formula_math_ar=dm(
                r"\operatorname{ex}(n, K_3) = \left\lfloor\frac{n^2}{4}\right\rfloor, \qquad |E(T(n, r))| = \binom{n}{2} - \sum_{i=1}^r \binom{n_i}{2}"
            ),
            diagram_en=_svg_turan_clusters((3, 3, 2), "Turán Graph T(n, r)"),
        ),
        olym_concept(
            title_en="Double Counting & Cherries in a 0–1 Incidence Table",
            title_ar="العد المزدوج وأزواج الجوار في جدول الوقوع (0–1)",
            body_en=(
                f"Represent a set system or bipartite graph as an {m('m \\times n')} **0–1 incidence table** with row sums {m('r_i')} and column sums {m('c_j')}: "
                f"double counting ones gives {m('\\sum_{i=1}^m r_i = \\sum_{j=1}^n c_j')}. Counting **cherries** (pairs of ones in the same row) in two ways yields "
                f"{m('\\sum_{i=1}^m \\binom{r_i}{2} = \\sum_{1 \\le j < k \\le n} \\binom{d_{jk}}{2}')}, where {m('d_{jk}')} is the number of rows containing ones in both columns {m('j')} and {m('k')}. "
                f"When no {m('2 \\times 2')} all-ones subgrid exists ({m('C_4')}-free), every {m('d_{jk} \\le 1')}, giving the Kővári–Sós–Turán bound {m('\\sum_{i=1}^m \\binom{r_i}{2} \\le \\binom{n}{2}')}."
            ),
            body_ar=(
                f"نمثّل منظومة المجموعات أو البيان ثنائي التجزئة عبر **جدول وقوع (0–1)** أبعاده {m('m \\times n')} بمجاميع صفوف {m('r_i')} ومجاميع أعمدة {m('c_j')}: "
                f"فيعطي العد المزدوج للواحدات {m('\\sum_{i=1}^m r_i = \\sum_{j=1}^n c_j')}. وعند عدّ **أزواج الواحدات** في الصف الواحد بطريقتين نحصل على "
                f"{m('\\sum_{i=1}^m \\binom{r_i}{2} = \\sum_{1 \\le j < k \\le n} \\binom{d_{jk}}{2}')}. "
                f"فإذا خلا الجدول من أي شبكة جزئية {m('2 \\times 2')} كلها واحدات (خالٍ من {m('C_4')})، كان {m('d_{jk} \\le 1')} وبالتالي {m('\\sum_{i=1}^m \\binom{r_i}{2} \\le \\binom{n}{2}')}."
            ),
            formula_en=dm(
                r"\sum_{i=1}^m r_i = \sum_{j=1}^n c_j, \qquad C_4\text{-free table} \implies \sum_{i=1}^m \binom{r_i}{2} \le \binom{n}{2}"
            ),
            caption_ar="متطابقة العد المزدوج وحد كوفاري-سوس-توران لجدول الوقوع الخالي من C₄:",
            formula_math_ar=dm(
                r"\sum_{i=1}^m r_i = \sum_{j=1}^n c_j, \qquad \sum_{i=1}^m \binom{r_i}{2} \le \binom{n}{2}"
            ),
            diagram_en=svg_olym_bipartite_graph(3, 4, None, "C₄-Free Incidence Table"),
        ),
        olym_concept(
            title_en="Burnside's Lemma, Generating Functions & Linearity of Expectation",
            title_ar="توطئة بيرنسايد، والدوال المولدة، وخطية التوقع الرياضي",
            body_en=(
                f"Under a symmetry group {m('G')} acting on colorings {m('X')}, **Burnside's Lemma** counts distinct orbits by averaging fixed points: "
                f"{m('|X/G| = \\frac{1}{|G|}\\sum_{g \\in G} |X^g|')}, where a permutation {m('g')} with {m('c(g)')} disjoint cycles fixes {m('k^{c(g)}')} colorings using {m('k')} colors. "
                f"In the **Probabilistic Method**, writing a combinatorial quantity as a sum of indicator variables {m('X = \\sum I_e')} gives "
                f"{m('\\mathbb{E}[X] = \\sum \\mathbb{P}(E_e)')} by **linearity of expectation** (requiring no independence!), proving the existence of an outcome with {m('X \\ge \\lceil \\mathbb{E}[X] \\rceil')}."
            ),
            body_ar=(
                f"تحت تأثير زمرة تناظر {m('G')} على تلوينات {m('X')}، تحصي **توطئة بيرنسايد** المدارات المختلفة بأخذ متوسط النقاط الثابتة: "
                f"{m('|X/G| = \\frac{1}{|G|}\\sum_{g \\in G} |X^g|')}، حيث يثبّت التبديل {m('g')} المكون من {m('c(g)')} دورات منفصلة {m('k^{c(g)}')} تلويناً باستعمال {m('k')} ألوان. "
                f"وفي **الطريقة الاحتمالية**، كتابة المقدار التوافقي كمجموع متغيرات مؤشرة {m('X = \\sum I_e')} تعطي "
                f"{m('\\mathbb{E}[X] = \\sum \\mathbb{P}(E_e)')} بفضل **خطية التوقع** (دون اشتراط الاستقلال!)، مما يثبت وجود حالة تحقق {m('X \\ge \\lceil \\mathbb{E}[X] \\rceil')}."
            ),
            formula_en=dm(
                r"|X/G| = \frac{1}{|G|}\sum_{g \in G} k^{c(g)}, \qquad \mathbb{E}\!\left[\sum_{i=1}^m I_i\right] = \sum_{i=1}^m \mathbb{P}(A_i)"
            ),
            caption_ar="توطئة بيرنسايد للتناظرات الدورانية وخطية التوقع للمتغيرات المؤشرة:",
            formula_math_ar=dm(
                r"|X/G| = \frac{1}{|G|}\sum_{g \in G} k^{c(g)}, \qquad \mathbb{E}\!\left[\sum_{i=1}^m I_i\right] = \sum_{i=1}^m \mathbb{P}(A_i)"
            ),
            diagram_en=svg_olym_pigeonhole_boxes(4, "E[X] = Σ P(A_i)", "∃ outcome ≥ E[X]"),
        ),
    ]

    examples = [
        olym_worked_example(
            ex_id="OLYM-L3-06-EX1",
            title_en="Maximum Edges in a K₄-Free Graph via Turán's Theorem",
            title_ar="أكبر عدد أضلاع في بيان خالٍ من K₄ عبر مبرهنة توران",
            q_en=(
                f"What is the maximum possible number of edges in a simple graph on {m('n = 11')} vertices "
                f"that contains no complete subgraph {m('K_4')}?"
            ),
            q_ar=(
                f"ما أكبر عدد ممكن من الأضلاع في بيان بسيط على {m('n = 11')} رأساً "
                f"لا يحوي أي بيان جزئي تام {m('K_4')}؟"
            ),
            correct_val=40,
            distractors=[36, 39, 41, 44],
            idea_en=(
                f"Partition the {m('11')} vertices into {m('r = 3')} parts as equally as possible ({m('4, 4, 3')}) to form the Turán graph {m('T(11, 3)')}."
            ),
            steps_en=[
                f"By Turán's Theorem for {m('K_{r+1} = K_4')} ({m('r = 3')}), the extremal graph is the balanced complete {m('3')}-partite graph {m('T(11, 3)')}.",
                f"Divide {m('11')} into {m('3')} parts differing by at most {m('1')}: {m('11 = 4 + 4 + 3')}.",
                f"Subtract the missing internal edges from {m('\\binom{11}{2} = 55')}: {m('|E| = 55 - \\binom{4}{2} - \\binom{4}{2} - \\binom{3}{2}')}.",
                f"Evaluate: {m('|E| = 55 - 6 - 6 - 3 = 40')} (equivalently {m('4 \\cdot 4 + 4 \\cdot 3 + 4 \\cdot 3 = 16 + 12 + 12 = 40')}).",
            ],
            check_en=(
                f"The upper bound {m('\\left(1 - \\frac{1}{3}\\right)\\frac{11^2}{2} = \\frac{121}{3} = 40.33\\dots')} confirms {m('|E| \\le 40')}."
            ),
            idea_ar=(
                f"نقسّم الرؤوس الـ {m('11')} إلى {m('r = 3')} مجموعات متقاربة الحجم ({m('4, 4, 3')}) لتكوين بيان توران {m('T(11, 3)')}."
            ),
            steps_ar=[
                f"من مبرهنة توران عند {m('K_{r+1} = K_4')} ({m('r = 3')}) يتحقق الحد الأقصى في البيان ثلاثي التجزئة المتوازن {m('T(11, 3)')}.",
                f"نقسّم {m('11')} إلى ثلاثة أجزاء متقاربة: {m('11 = 4 + 4 + 3')}.",
                f"نطرح الأضلاع الداخلية المحذوفة من {m('\\binom{11}{2} = 55')}: {m('|E| = 55 - \\binom{4}{2} - \\binom{4}{2} - \\binom{3}{2}')}.",
                f"نحسب الناتج: {m('55 - 6 - 6 - 3 = 40')} (أو {m('4 \\times 4 + 4 \\times 3 + 4 \\times 3 = 40')}).",
            ],
            check_ar=(
                f"التقدير الأعلى {m('\\left(1 - \\frac{1}{3}\\right)\\frac{121}{2} = 40.33\\dots')} يؤكد أن {m('40')} هو الحد الأقصى الصحيح."
            ),
            diagram_en=_svg_turan_clusters((4, 4, 3), "|E(T(11, 3))| = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-06-EX2",
            title_en="Maximum Ones in a 7×7 C₄-Free Incidence Table",
            title_ar="أكبر عدد من الواحدات في جدول وقوع 7×7 خالٍ من C₄",
            q_en=(
                f"A {m('7 \\times 7')} {m('0\\text{–}1')} incidence table contains no {m('2 \\times 2')} subgrid consisting of four {m('1')}'s. "
                f"What is the maximum possible total number of {m('1')}'s in the table?"
            ),
            q_ar=(
                f"جدول وقوع (من أصفار وواحدات) أبعاده {m('7 \\times 7')} لا يحوي أي شبكة جزئية {m('2 \\times 2')} مكوّنة من أربعة واحدات. "
                f"ما أكبر عدد كلي ممكن من الواحدات في هذا الجدول؟"
            ),
            correct_val=21,
            distractors=[18, 20, 24, 28],
            idea_en=(
                f"Double count horizontal pairs of ones (cherries): {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\le \\binom{7}{2} = 21')}, and apply convexity of {m('\\binom{r}{2}')}."
            ),
            steps_en=[
                f"Let row {m('i')} contain {m('r_i')} ones, with total ones {m('S = \\sum_{i=1}^7 r_i')}.",
                f"Since no two rows share ones in two columns, the {m('7')} rows contain at most {m('\\binom{7}{2} = 21')} horizontal pairs of ones: {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\le 21')}.",
                f"If {m('S \\ge 22')}, convexity of {m('\\binom{r}{2}')} gives {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\ge 6\\binom{3}{2} + \\binom{4}{2} = 18 + 6 = 24 > 21')}, a contradiction.",
                f"At {m('S = 21')} ({m('r_1 = \\dots = r_7 = 3')}), {m('7\\binom{3}{2} = 21')}, which is realized by the Fano plane incidence table. Thus the maximum is {m('21')}.",
            ],
            check_en=(
                f"In the Fano plane, {m('7')} lines each contain {m('3')} of the {m('7')} points and any two lines meet in exactly {m('1')} point, giving {m('7 \\times 3 = 21')} incidences."
            ),
            idea_ar=(
                f"نعدّ أزواج الواحدات الأفقية بطريقتين: {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\le \\binom{7}{2} = 21')}، ثم نستخدم تحدب {m('\\binom{r}{2}')}."
            ),
            steps_ar=[
                f"ليكن {m('r_i')} عدد الواحدات في الصف {m('i')}، ومجموعها الكلي {m('S = \\sum_{i=1}^7 r_i')}.",
                f"بما أنه لا توجد شبكة {m('2 \\times 2')} من الواحدات، فإن مجموع الأزواج الأفقية يحقق {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\le \\binom{7}{2} = 21')}.",
                f"لو كان {m('S \\ge 22')} لأعطى تحدب {m('\\binom{r}{2}')} أن {m('\\sum_{i=1}^7 \\binom{r_i}{2} \\ge 6\\binom{3}{2} + \\binom{4}{2} = 24 > 21')} وهو تناقض.",
                f"وعند {m('S = 21')} ({m('r_1 = \\dots = r_7 = 3')}) يتحقق التساوي {m('7 \\times 3 = 21')} في جدول وقوع مستوي فانو، فالحد الأقصى هو {m('21')}.",
            ],
            check_ar=(
                f"في مستوي فانو توجد {m('7')} مستقيمات يحوي كل منها {m('3')} نقاط ويتقاطع أي مستقيمين في نقطة واحدة، مما يحقق {m('21')} وقوعاً."
            ),
            diagram_en=svg_olym_bipartite_graph(4, 4, None, "7×7 C₄-Free: max 1s = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-06-EX3",
            title_en="Counting 2-Colored 6-Bead Necklaces via Burnside's Lemma",
            title_ar="عدّ العقود السداسية ثنائية اللون عبر توطئة بيرنسايد",
            q_en=(
                f"How many distinct {m('6')}-bead necklaces can be made using beads of {m('2')} colors (red and blue) "
                f"if two necklaces are considered identical when one is a rotation of the other (without flipping)?"
            ),
            q_ar=(
                f"كم عقداً مختلفاً مكوّناً من {m('6')} خرزات يمكن تشكيله باستعمال لونين (أحمر وأزرق) "
                f"إذا اعتُبر العقدان متطابقين عند نتوج أحدهما عن الآخر بدوران (دون قلب)؟"
            ),
            correct_val=14,
            distractors=[11, 12, 13, 16],
            idea_en=(
                f"Apply Burnside's Lemma over the cyclic group {m('C_6')}: a rotation by {m('k')} steps has {m('c(g_k) = \\gcd(k, 6)')} cycles and fixes {m('2^{\\gcd(k, 6)}')} colorings."
            ),
            steps_en=[
                f"The rotation group {m('C_6')} has {m('6')} elements {m('g_k')} ({m('k = 0, 1, 2, 3, 4, 5')}), each decomposing the {m('6')} beads into {m('\\gcd(k, 6)')} cycles.",
                f"For {m('k = 0')}: {m('\\gcd(0, 6) = 6')} cycles {m('\\implies 2^6 = 64')} fixed colorings; for {m('k = 3')}: {m('\\gcd(3, 6) = 3')} cycles {m('\\implies 2^3 = 8')} fixed colorings.",
                f"For {m('k = 2, 4')}: {m('\\gcd(k, 6) = 2')} cycles {m('\\implies 2 \\times 2^2 = 8')}; for {m('k = 1, 5')}: {m('\\gcd(k, 6) = 1')} cycle {m('\\implies 2 \\times 2^1 = 4')}.",
                f"By Burnside's Lemma, the number of distinct necklaces is {m('\\frac{64 + 8 + 8 + 4}{6} = \\frac{84}{6} = 14')}.",
            ],
            check_en=(
                f"Counting by number of red beads ({m('0')} to {m('6')}) gives {m('1 + 1 + 3 + 4 + 3 + 1 + 1 = 14')} necklaces."
            ),
            idea_ar=(
                f"نطبّق توطئة بيرنسايد على الزمرة الدورية {m('C_6')}: الدوران بمقدار {m('k')} يمتلك {m('\\gcd(k, 6)')} دورات ويثبّت {m('2^{\\gcd(k, 6)}')} تلويناً."
            ),
            steps_ar=[
                f"تضم زمرة الدورانات {m('C_6')} ستة عناصر {m('g_k')} ({m('k = 0, \\dots, 5')})، يقسّم كل منها الخرزات إلى {m('\\gcd(k, 6)')} دورات.",
                f"عند {m('k = 0')}: لدينا {m('2^6 = 64')} تلويناً ثابتاً؛ وعند {m('k = 3')}: لدينا {m('2^3 = 8')} تلوينات ثابتة.",
                f"وعند {m('k = 2, 4')}: لدينا {m('2 \\times 2^2 = 8')}؛ وعند {m('k = 1, 5')}: لدينا {m('2 \\times 2^1 = 4')}.",
                f"بموجب توطئة بيرنسايد يكون عدد العقود المختلفة {m('\\frac{64 + 8 + 8 + 4}{6} = \\frac{84}{6} = 14')}.",
            ],
            check_ar=(
                f"بتصنيف العقود حسب عدد الخرزات الحمراء من {m('0')} إلى {m('6')} نحصل على {m('1 + 1 + 3 + 4 + 3 + 1 + 1 = 14')} عقداً."
            ),
            diagram_en=_svg_roots_of_unity(6, "C₆: gcd(k, 6) cycles", "|X / C₆| = ?"),
        ),
        olym_worked_example(
            ex_id="OLYM-L3-06-EX4",
            title_en="Expected Directed 3-Cycles in a Random Tournament",
            title_ar="التوقع الرياضي لعدد الدورات الموجهة الثلاثية في بطولة عشوائية",
            q_en=(
                f"In a round-robin tournament among {m('10')} players, every pair of players plays one match, and each match is won independently "
                f"by either player with probability {m('\\frac{1}{2}')}. What is the expected number of directed {m('3')}-cycles "
                f"(triples {m('\\{A, B, C\\}')} where {m('A')} beats {m('B')}, {m('B')} beats {m('C')}, and {m('C')} beats {m('A')})?"
            ),
            q_ar=(
                f"في بطولة دوري كامل بين {m('10')} لاعبين، يلعب كل ثنائي مباراة واحدة يفوز بها أي منهما باحتمال مستقل قدره {m('\\frac{1}{2}')}. "
                f"ما القيمة المتوقعة لعدد الدورات الثلاثية الموجهة (الثلاثيات {m('\\{A, B, C\\}')} التي يهزم فيها {m('A')} اللاعب {m('B')} ويهزم {m('B')} اللاعب {m('C')} ويهزم {m('C')} اللاعب {m('A')})؟"
            ),
            correct_val=30,
            distractors=[15, 24, 40, 60],
            idea_en=(
                f"Assign an indicator variable {m('I_T')} to each of the {m('\\binom{10}{3} = 120')} triples; each triple forms a directed {m('3')}-cycle with probability {m('\\frac{2}{8} = \\frac{1}{4}')}."
            ),
            steps_en=[
                f"There are {m('\\binom{10}{3} = \\frac{10 \\times 9 \\times 8}{6} = 120')} unordered triples of players.",
                f"For any fixed triple {m('T = \\{A, B, C\\}')}, the {m('3')} matches among them have {m('2^3 = 8')} equally likely outcomes.",
                f"Exactly {m('2')} of the {m('8')} outcomes are cyclic ({m('A \\to B \\to C \\to A')} and {m('A \\to C \\to B \\to A')}), so {m('\\mathbb{E}[I_T] = \\frac{2}{8} = \\frac{1}{4}')}.",
                f"By linearity of expectation, the expected number of directed {m('3')}-cycles is {m('\\sum_{T} \\mathbb{E}[I_T] = 120 \\times \\frac{1}{4} = 30')}.",
            ],
            check_en=(
                f"Consequently, by the probabilistic pigeonhole principle, there exists a {m('10')}-player tournament containing at least {m('30')} directed {m('3')}-cycles."
            ),
            idea_ar=(
                f"نعرّف متغيراً مؤشراً {m('I_T')} لكل ثلاثية من الثلاثيات الـ {m('\\binom{10}{3} = 120')}؛ وكل ثلاثية تشكّل دورة ثلاثية باحتمال {m('\\frac{2}{8} = \\frac{1}{4}')}."
            ),
            steps_ar=[
                f"يوجد {m('\\binom{10}{3} = \\frac{10 \\times 9 \\times 8}{6} = 120')} ثلاثية غير مرتبة من اللاعبين.",
                f"لكل ثلاثية {m('T = \\{A, B, C\\}')} توجد {m('2^3 = 8')} نتائج متساوية الاحتمال للمباريات الثلاث بينهم.",
                f"نتيجتان فقط من الـ {m('8')} تشكّلان دورة موجهة في اتجاهين متعاكسين، لذا {m('\\mathbb{E}[I_T] = \\frac{2}{8} = \\frac{1}{4}')}.",
                f"بفضل خطية التوقع يكون العدد المتوقع للدورات الثلاثية {m('120 \\times \\frac{1}{4} = 30')}.",
            ],
            check_ar=(
                f"وبناءً على المبدأ الاحتمالي، لا بد من وجود بطولة من {m('10')} لاعبين تحوي {m('30')} دورة ثلاثية موجهة على الأقل."
            ),
            diagram_en=svg_olym_pigeonhole_boxes(4, "C(10,3) = 120 triples", "E[X] = ?"),
        ),
    ]

    return make_olympiad_lesson(
        lesson_id="OLYM-L3-06",
        level=LEVEL_T3,
        unit_num="3.6",
        topic="Combinatorics",
        title_en="Extremal Graph Theory, Double Counting, Burnside & Probabilistic Method",
        title_ar="نظرية البيانات القصوى، العد المزدوج، توطئة بيرنسايد، والطريقة الاحتمالية",
        summary_en=(
            "Complete Senior Olympiad Combinatorics with Mantel and Turán extremal graph bounds, "
            "double counting of cherries in 0–1 incidence tables, Burnside orbit enumeration, and the probabilistic method via linearity of expectation."
        ),
        summary_ar=(
            "أكمل توافقيات الأولمبياد المتقدم مع مبرهنتي مانتل وتوران للبيانات القصوى، "
            "والعد المزدوج لأزواج الواحدات في جداول الوقوع، وتوطئة بيرنسايد للتناظرات، والطريقة الاحتمالية عبر خطية التوقع."
        ),
        goals_en=[
            f"Determine maximum edge counts in {m('K_{r+1}')}-free graphs using Mantel's and Turán's theorems.",
            f"Bound incidences in {m('C_4')}-free configurations by double counting cherries {m('\\sum \\binom{r_i}{2} \\le \\binom{n}{2}')} in a {m('0\\text{–}1')} incidence table.",
            f"Count symmetry orbits and constrained configurations using Burnside's Lemma {m('\\frac{1}{|G|}\\sum k^{c(g)}')} and generating functions.",
            f"Apply indicator random variables and linearity of expectation to compute expectations and prove existence bounds.",
        ],
        goals_ar=[
            f"تحديد أكبر عدد من الأضلاع في البيانات الخالية من {m('K_{r+1}')} باستخدام مبرهنتي مانتل وتوران.",
            f"تقدير عدد الواحدات في الجداول الخالية من {m('C_4')} عبر العد المزدوج للأزواج {m('\\sum \\binom{r_i}{2} \\le \\binom{n}{2}')} في جدول الوقوع.",
            f"إحصاء المدارات التناظرية باستخدام توطئة بيرنسايد {m('\\frac{1}{|G|}\\sum k^{c(g)}')} والدوال المولدة.",
            f"توظيف المتغيرات المؤشرة وخطية التوقع لحساب القيم المتوقعة وإثبات حدود الوجود.",
        ],
        concepts=concepts,
        traps_en=[
            f"Using {m('\\left(1 - \\frac{1}{r}\\right)\\frac{n^2}{2}')} as an exact formula when {m('r \\nmid n')} instead of partitioning {m('n')} into {m('r')} nearly equal integer parts.",
            f"Dividing by {m('n')} instead of {m('2n')} when reflections are allowed (bracelets vs. rotational necklaces).",
            f"Hesitating to use {m('\\mathbb{E}[\\sum X_i] = \\sum \\mathbb{E}[X_i]')} when indicator variables overlap: linearity of expectation never requires independence.",
        ],
        traps_ar=[
            f"استعمال التقريب {m('\\left(1 - \\frac{1}{r}\\right)\\frac{n^2}{2}')} كقيمة دقيقة عندما {m('r \\nmid n')} بدلاً من تقسيم {m('n')} إلى {m('r')} أجزاء صحيحة متقاربة.",
            f"القسمة على {m('n')} بدلاً من {m('2n')} عندما تكون الانعكاسات مسموحة إلى جانب الدورانات.",
            f"التردد في تطبيق {m('\\mathbb{E}[\\sum X_i] = \\sum \\mathbb{E}[X_i]')} عند تداخل المتغيرات المؤشرة؛ فخطية التوقع لا تشترط الاستقلال إطلاقاً.",
        ],
        examples=examples,
        blueprints=[
            "olym_t3_comb_turan_extremal_graphs",
            "olym_t3_comb_double_counting_incidence",
            "olym_t3_comb_burnside_generating_fn",
            "olym_t3_comb_probabilistic_expectation",
        ],
    )


def get_tier3_lessons() -> list[dict]:
    """Return all 6 Tier 3 Senior Olympiad lessons (OLYM-L3-01..OLYM-L3-06)."""
    return [
        _lesson_l3_01(),
        _lesson_l3_02(),
        _lesson_l3_03(),
        _lesson_l3_04(),
        _lesson_l3_05(),
        _lesson_l3_06(),
    ]
