"""Shared Study Academy enhancement module for NSMO, Math Olympiad, Kangaroo, and Nafes lessons:
1. 100% Bespoke Worked-Example SVG Coverage (adds custom bilingual SVGs to all 19 previously-unillustrated examples).
2. 4-Card Bilingual Quick Formula & Strategy Cheat-Sheets (`cheat_sheet`) across all 90 remaining lessons.
"""
import xml.etree.ElementTree as ET

import kmc_diagrams_extra as D2
from ar_svg_localizer import localize_svg_to_ar
from kangaroo_cheat_sheets import KANGAROO_CHEAT_SHEETS, _cs


def _build_missing_example_svgs() -> dict[str, tuple[str, str]]:
    """Return {example_id: (svg_en, svg_ar)} for all 19 bespoke examples missing diagrams."""
    return {
        # ── NSMO (12 examples) ──
        "L11-E4": (
            D2.svg_cycle_ring(
                ["3¹=3", "3²=9", "3³=..7", "3⁴=..1"],
                top_lbl="3⁴⁷ → ..7  &  7³⁰ → ..9",
                center_lbl="(7+9) mod 10 = 6",
            ),
            D2.svg_cycle_ring(
                ["3¹=3", "3²=9", "3³=..7", "3⁴=..1"],
                top_lbl="آحاد 3⁴⁷ هو 7 وآحاد 7³⁰ هو 9",
                center_lbl="(7+9) mod 10 = 6",
            ),
        ),
        "L12-E1": (
            D2.svg_telescoping_chain(
                ["1/2", "−1/3 + 1/3", "−1/4 + …", "−1/12"],
                op_sym="",
                title_lbl="1/(2×3) + 1/(3×4) + … + 1/(11×12)",
                footer_lbl="1/2 − 1/12 = 5/12",
            ),
            D2.svg_telescoping_chain(
                ["1/2", "−1/3 + 1/3", "−1/4 + …", "−1/12"],
                op_sym="",
                title_lbl="تفكيك الكسور المتداخلة",
                footer_lbl="1/2 − 1/12 = 5/12",
            ),
        ),
        "L13-E3": (
            D2.svg_digit_cards(
                ["23", "25", "27", "29", "31"],
                badge_lbl="Sum = 135  ⇒  Middle = 135 ÷ 5 = 27",
                note_lbl="Largest odd integer = 27 + 4 = 31",
            ),
            D2.svg_digit_cards(
                ["23", "25", "27", "29", "31"],
                badge_lbl="المجموع = 135  ⇐  الأوسط = 135 ÷ 5 = 27",
                note_lbl="أكبر عدد فردي = 27 + 4 = 31",
            ),
        ),
        "L14-E1": (
            D2.svg_tape_bar_split(
                [(1.0, "Son = 16"), (2.0, "Gap = 42 − 10 = 32")],
                total_lbl="Father = 3 × Son  ⇒  2 parts = 32",
                sub_lbl="Son = 16  ⇒  16 − 10 = 6 years",
            ),
            D2.svg_tape_bar_split(
                [(1.0, "الابن = 16"), (2.0, "الفرق الثابت = 32")],
                total_lbl="الأب = 3 × الابن  ⇐  جزآن = 32",
                sub_lbl="الابن = 16  ⇐  بعد 16 − 10 = 6 سنوات",
            ),
        ),
        "L16-E3": (
            D2.svg_pigeonhole_bins(
                [("Red (10)", "max 3"), ("Blue (8)", "max 3"), ("Green (5)", "max 3")],
                header_lbl="Worst case avoiding 4 of one color = 3 + 3 + 3 = 9",
                footer_lbl="Next draw: 9 + 1 = 10 guarantees 4 same!",
            ),
            D2.svg_pigeonhole_bins(
                [("أحمر (10)", "أقصى 3"), ("أزرق (8)", "أقصى 3"), ("أخضر (5)", "أقصى 3")],
                header_lbl="أسوأ حالة لتجنب 4 من نفس اللون = 3 + 3 + 3 = 9",
                footer_lbl="السحبة التالية: 9 + 1 = 10 تضمن 4 متماثلة!",
            ),
        ),
        "L16-E4": (
            D2.svg_two_dice_grid(
                title_lbl="Sum ≥ 10: (4,6),(5,5),(5,6),(6,4),(6,5),(6,6) → 6/36 = 1/6",
                d1_lbl="Die 1 (1..6)",
                d2_lbl="Die 2 (1..6)",
            ),
            D2.svg_two_dice_grid(
                title_lbl="المجموع ≥ 10: 6 أزواج من أصل 36 = 1/6",
                d1_lbl="النرد 1 (1..6)",
                d2_lbl="النرد 2 (1..6)",
            ),
        ),
        "L31-E3": (
            D2.svg_factorial_padic_bars(
                "v₃(85!) = ⌊85/3⌋ + ⌊85/9⌋ + ⌊85/27⌋ + ⌊85/81⌋",
                [("÷3", 1.0, "28"), ("÷9", 0.38, "9"), ("÷27", 0.16, "3"), ("÷81", 0.08, "1")],
                footer_lbl="k = 28 + 9 + 3 + 1 = 41",
            ),
            D2.svg_factorial_padic_bars(
                "أسّ العامل 3 في 85! بصيغة ليجاندر",
                [("÷3", 1.0, "28"), ("÷9", 0.38, "9"), ("÷27", 0.16, "3"), ("÷81", 0.08, "1")],
                footer_lbl="k = 28 + 9 + 3 + 1 = 41",
            ),
        ),
        "L32-E2": (
            D2.svg_algebra_flow(
                [("Split", "(n + 3) + 12/(n + 2)"), ("Divisors of 12", "±1, ±2, ±3, ±4, ±6, ±12")],
                arrows=["⇒"],
                title_lbl="(n² + 5n + 18) / (n + 2) ∈ ℤ",
                footer_lbl="6 positive + 6 negative divisors = 12 integers n",
            ),
            D2.svg_algebra_flow(
                [("القسمة", "(n + 3) + 12/(n + 2)"), ("قواسم 12", "±1, ±2, ±3, ±4, ±6, ±12")],
                arrows=["⇐"],
                title_lbl="شرط كون الكسر عدداً صحيحاً",
                footer_lbl="6 قواسم موجبة + 6 سالبة = 12 قيمة صحيحة لـ n",
            ),
        ),
        "L32-E4": (
            D2.svg_algebra_flow(
                [("Mod 2", "p = 2 ⇒ q²+r² = 178"), ("Mod 3", "q = 3 ⇒ r² = 169"), ("Root", "r = 13")],
                arrows=["⇒", "⇒"],
                title_lbl="Primes p < q < r with p² + q² + r² = 182",
                footer_lbl="p + q + r = 2 + 3 + 13 = 18",
            ),
            D2.svg_algebra_flow(
                [("باقي 2", "p = 2 ⇒ q²+r² = 178"), ("باقي 3", "q = 3 ⇒ r² = 169"), ("الجذر", "r = 13")],
                arrows=["⇐", "⇐"],
                title_lbl="أعداد أولية p < q < r تحقق p² + q² + r² = 182",
                footer_lbl="p + q + r = 2 + 3 + 13 = 18",
            ),
        ),
        "L33-E2": (
            D2.svg_algebra_flow(
                [("Given", "s₁=6, s₂=9, s₃=2"), ("Gauss", "3(2) + 6(36 − 27)"), ("Value", "6 + 54 = 60")],
                arrows=["⇒", "="],
                title_lbl="a³ + b³ + c³ = 3abc + (a+b+c)[(a+b+c)² − 3(ab+bc+ca)]",
                footer_lbl="Exact sum of cubes = 60",
            ),
            D2.svg_algebra_flow(
                [("المعطيات", "s₁=6, s₂=9, s₃=2"), ("متطابقة غاوس", "3(2) + 6(36 − 27)"), ("الناتج", "6 + 54 = 60")],
                arrows=["⇐", "="],
                title_lbl="حساب a³ + b³ + c³ بمتطابقة غاوس",
                footer_lbl="مجموع المكعبات = 60",
            ),
        ),
        "L33-E3": (
            D2.svg_algebra_flow(
                [("Match u+v=14, uv=45", "(u, v) = (9, 5)"), ("Denest", "(3 + √5) + (3 − √5)")],
                arrows=["⇒"],
                title_lbl="√(14 + 2√45) + √(14 − 2√45)",
                footer_lbl="Conjugate surds cancel: 3 + 3 = 6",
            ),
            D2.svg_algebra_flow(
                [("عددَان مجموعهما 14 وجداؤهما 45", "(9, 5)"), ("فك الجذرين", "(3 + √5) + (3 − √5)")],
                arrows=["⇐"],
                title_lbl="√(14 + 2√45) + √(14 − 2√45)",
                footer_lbl="حذف الجذرين المترافقين: 3 + 3 = 6",
            ),
        ),
        "L34-E3": (
            D2.svg_algebra_flow(
                [("Squares", "2²/x + 3²/y + 6²/z"), ("Titu Bound", "≥ (2+3+6)² / (x+y+z)"), ("Min", "11² / 11 = 11")],
                arrows=["⇒", "="],
                title_lbl="Minimum for x + y + z = 11 (x, y, z > 0)",
                footer_lbl="Equality at (x, y, z) = (2, 3, 6) → Min = 11",
            ),
            D2.svg_algebra_flow(
                [("المربعات", "2²/x + 3²/y + 6²/z"), ("متباينة تيتو", "≥ (2+3+6)² / (x+y+z)"), ("الأصغر", "11² / 11 = 11")],
                arrows=["⇐", "="],
                title_lbl="القيمة الصغرى بشرط x + y + z = 11",
                footer_lbl="تتحقق المساواة عند (2, 3, 6) ⇐ القيمة الصغرى = 11",
            ),
        ),
        # ── Kangaroo (7 examples) ──
        "KANG-L2-01-EX2": (
            D2.svg_divisor_rainbow(
                "Blue every 6 min  &  Gold every 8 min",
                ["6 = 2×3", "8 = 2³", "LCM = 2³×3 = 24"],
                sub_lbl="Next simultaneous flash: 24 minutes later (10:24 AM)",
            ),
            D2.svg_divisor_rainbow(
                "أزرق كل 6 دقائق  وذهبي كل 8 دقائق",
                ["6 = 2×3", "8 = 2³", "م.م.أ = 24"],
                sub_lbl="الوميض المتزامن التالي بعد 24 دقيقة (10:24 صباحاً)",
            ),
        ),
        "KANG-L4-01-EX3": (
            D2.svg_factorial_padic_bars(
                "Trailing zeros of 135! = v₅(135!)",
                [("÷5", 1.0, "27"), ("÷25", 0.24, "5"), ("÷125", 0.08, "1")],
                footer_lbl="Total zeros = 27 + 5 + 1 = 33",
            ),
            D2.svg_factorial_padic_bars(
                "عدد الأصفار الطرفية في 135! = v₅(135!)",
                [("÷5", 1.0, "27"), ("÷25", 0.24, "5"), ("÷125", 0.08, "1")],
                footer_lbl="مجموع الأصفار = 27 + 5 + 1 = 33",
            ),
        ),
        "KANG-L4-02-EX1": (
            D2.svg_algebra_flow(
                [("Midpoint m = 2029", "(2029−3)(2029+3) + 9"), ("Simplify", "√(2029² − 9 + 9) = 2029")],
                arrows=["⇒"],
                title_lbl="√(2026 × 2032 + 9)",
                footer_lbl="Difference of squares cancels −3² + 9!",
            ),
            D2.svg_algebra_flow(
                [("المنتصف m = 2029", "(2029−3)(2029+3) + 9"), ("التبسيط", "√(2029² − 9 + 9) = 2029")],
                arrows=["⇐"],
                title_lbl="√(2026 × 2032 + 9)",
                footer_lbl="فرق المربعين يختصر −9 مع +9 مباشرة!",
            ),
        ),
        "KANG-L4-02-EX3": (
            D2.svg_algebra_flow(
                [("x − 1/x = 4", "x² + 1/x² = 4² + 2 = 18"), ("Square again", "x⁴ + 1/x⁴ = 18² − 2 = 322")],
                arrows=["⇒"],
                title_lbl="Two-Step Reciprocal Power Climb",
                footer_lbl="First step adds +2; second step subtracts −2!",
            ),
            D2.svg_algebra_flow(
                [("x − 1/x = 4", "x² + 1/x² = 4² + 2 = 18"), ("نربّع ثانيةً", "x⁴ + 1/x⁴ = 18² − 2 = 322")],
                arrows=["⇐"],
                title_lbl="سلّم القوى المقلوبة على خطوتين",
                footer_lbl="التربيع الأول يضيف +2 والتربيع الثاني يطرح −2!",
            ),
        ),
        "KANG-L4-04-EX2": (
            D2.svg_algebra_flow(
                [("Cube", "(V,E,F) = (8,12,6)"), ("8 Corners", "+8×(2, 3, 1)"), ("Truncated", "(24, 36, 14)")],
                arrows=["→", "="],
                title_lbl="Euler Check: 24 − 36 + 14 = 2 ✓",
                footer_lbl="V + E + F = 24 + 36 + 14 = 74",
            ),
            D2.svg_algebra_flow(
                [("المكعب", "(V,E,F) = (8,12,6)"), ("8 أركان", "+8×(2, 3, 1)"), ("الناتج", "(24, 36, 14)")],
                arrows=["←", "="],
                title_lbl="تحقق أويلر: 24 − 36 + 14 = 2 ✓",
                footer_lbl="V + E + F = 24 + 36 + 14 = 74",
            ),
        ),
        "KANG-L4-05-EX2": (
            D2.svg_pigeonhole_bins(
                [("P₁", "≥2"), ("P₂", "≥2"), ("P₃", "≥2"), ("P₄", "≥2")],
                header_lbl="Pre-assign 4×2 = 8 tokens  ⇒  5 free tokens left",
                footer_lbl="Stars & Bars: C(5 + 4 − 1, 4 − 1) = C(8, 3) = 56",
            ),
            D2.svg_pigeonhole_bins(
                [("لاعب 1", "≥2"), ("لاعب 2", "≥2"), ("لاعب 3", "≥2"), ("لاعب 4", "≥2")],
                header_lbl="نوزع 4×2 = 8 ميداليات أولاً ⇐ يتبقى 5 حرة",
                footer_lbl="النجوم والفواصل: C(5 + 4 − 1, 3) = C(8, 3) = 56",
            ),
        ),
        "KANG-L4-05-EX3": (
            D2.svg_digit_cards(
                ["58", "→ −3 →", "55", "→ … →", "5", "→", "0"],
                badge_lbl="Take 1..4 pebbles  ⇒  Losing multiples of 4 + 1 = 5",
                note_lbl="58 mod 5 = 3  ⇒  Remove 3 pebbles on Move 1!",
            ),
            D2.svg_digit_cards(
                ["58", "← −3 ←", "55", "← … ←", "5", "←", "0"],
                badge_lbl="سحب 1..4 حصى ⇐ المواقع الخاسرة مضاعفات 5",
                note_lbl="58 mod 5 = 3 ⇐ اسحب 3 حصيات في البداية!",
            ),
        ),
    }


CHEAT_SHEETS: dict[str, dict] = {
    # ══════════════════════════════════════════════════════════════════════════
    # NSMO / Mawhiba (Grades 7–10): NSMO-L1-01 .. NSMO-L3-06 (18 lessons)
    # ══════════════════════════════════════════════════════════════════════════
    "NSMO-L1-01": _cs(
        [
            ("Divisibility by 8, 9 & 11", r"By \( 8 \): last \( 3 \) digits; by \( 9 \): digit sum; by \( 11 \): \((d_{\text{odd}} - d_{\text{even}}) \equiv 0 \pmod{11}\)"),
            ("Divisor Count Formula", r"For \( n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k} \), total positive divisors \( \tau(n) = \prod (a_i + 1) \)"),
            ("Units-Digit Power Cycle", r"Powers mod \( 10 \) repeat with period \( 1, 2, \) or \( 4 \); replace exponent \( E \) by \( ((E - 1) \bmod 4) + 1 \)"),
            ("Euclidean Division Bound", r"\( N = d \cdot q + r \) with strict remainder bound \( 0 \le r < d \)"),
        ],
        [
            ("قابلية القسمة على 8 و9 و11", r"على \( 8 \): آخر 3 أرقام؛ على \( 9 \): مجموع الأرقام؛ على \( 11 \): فرق مجموعي الخانات المتناوبة يقبل على \( 11 \)"),
            ("قانون عدد القواسم الموجبة", r"للعدد \( n = p_1^{a_1} \cdots p_k^{a_k} \) يكون عدد القواسم \( \tau(n) = \prod (a_i + 1) \)"),
            ("دورة خانة الآحاد للقوى", r"تتكرر آحاد القوى كل \( 4 \) خطوات على الأكثر؛ استبدل الأس \( E \) بـ \( ((E - 1) \bmod 4) + 1 \)"),
            ("قانون القسمة الإقليدية", r"\( N = d \cdot q + r \) مع الشرط الصارم للباقي \( 0 \le r < d \)"),
        ],
    ),
    "NSMO-L1-02": _cs(
        [
            ("Telescoping Fraction Split", r"\( \frac{1}{k(k + d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k + d}\right) \)"),
            ("Successive Remainder Chain", r"Spending \( f_1 \) then \( f_2 \) of the rest leaves \( (1 - f_1)(1 - f_2) \) of the original total"),
            ("Unchanged Quantity Anchor", r"When only component \( A \) changes in a mixture, anchor component \( B = \text{constant} \)"),
            ("3-Digit Reversal Identity", r"\( \overline{abc} - \overline{cba} = 99(a - c) \) and \( \overline{ab} + \overline{ba} = 11(a + b) \)"),
        ],
        [
            ("تفكيك الكسور المتداخلة", r"\( \frac{1}{k(k + d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k + d}\right) \)"),
            ("سلسلة الكسور المتبقية", r"صرف \( f_1 \) ثم \( f_2 \) من الباقي يترك \( (1 - f_1)(1 - f_2) \) من الكمية الأصلية"),
            ("تثبيت المقدار غير المتغير", r"عند إضافة مادة واحدة للخليط، اجعل كمية المادة الأخرى ثابتة في النسبتين"),
            ("متطابقة عكس الأرقام", r"\( \overline{abc} - \overline{cba} = 99(a - c) \) و\( \overline{ab} + \overline{ba} = 11(a + b) \)"),
        ],
    ),
    "NSMO-L1-03": _cs(
        [
            ("Arithmetic Sequence & Sum", r"\( a_n = a_1 + (n - 1)d \) and \( S_n = \frac{n(a_1 + a_n)}{2} \)"),
            ("Consecutive Odd/Even Mean", r"For odd \( k \), the sum of \( k \) consecutive integers/odds equals \( k \times (\text{middle term}) \)"),
            ("3-Row Additive Pyramid", r"Base \( (a, b, c) \implies \text{Top} = a + 2b + c \) (middle cell counts twice!)"),
            ("Triangular & Square Sums", r"\( 1 + 2 + \dots + n = \frac{n(n + 1)}{2} \); sum of first \( n \) odd numbers \( = n^2 \)"),
        ],
        [
            ("المتتابعة الحسابية ومجموعها", r"\( a_n = a_1 + (n - 1)d \) والمجموع \( S_n = \frac{n(a_1 + a_n)}{2} \)"),
            ("متوسط الأعداد المتتالية", r"لعدد فردي \( k \) من الأعداد المتتالية: \(\text{المجموع} = k \times (\text{الحد الأوسط})\)"),
            ("الهرم العددي ذو 3 صفوف", r"القاعدة \( (a, b, c) \implies \text{القمة} = a + 2b + c \) (الوسط يُحسب مرتين!)"),
            ("الأعداد المثلثية والمربعة", r"\( 1 + 2 + \dots + n = \frac{n(n + 1)}{2} \)؛ ومجموع أول \( n \) أعداد فردية \( = n^2 \)"),
        ],
    ),
    "NSMO-L1-04": _cs(
        [
            ("Age Difference Invariant", r"\( A - B = D \) never changes; when \( A = kB \), the younger age is \( B = \frac{D}{k - 1} \)"),
            ("Train Crossing a Bridge", r"Total distance for a train of length \( L_{\text{tr}} \) to clear bridge \( L_{\text{br}} \) is \( L_{\text{tr}} + L_{\text{br}} \)"),
            ("Combined Work Rate", r"\( \frac{1}{T_{\text{together}}} = \frac{1}{t_1} + \frac{1}{t_2} \implies T_{\text{together}} = \frac{t_1 t_2}{t_1 + t_2} \)"),
            ("Two-Type Replacement", r"Assume all \( N \) items have value \( v_1 \); divide discrepancy \( |S - N v_1| \) by \( |v_2 - v_1| \)"),
        ],
        [
            ("ثبات فرق الأعمار", r"\( A - B = D \) ثابت دائماً؛ وعندما \( A = kB \) يكون عمر الأصغر \( B = \frac{D}{k - 1} \)"),
            ("عبور القطار للجسر", r"المسافة الكلية لعبور قطار طوله \( L_{\text{tr}} \) جسراً طوله \( L_{\text{br}} \) هي \( L_{\text{tr}} + L_{\text{br}} \)"),
            ("معدل العمل المشترك", r"\( \frac{1}{T_{\text{معاً}}} = \frac{1}{t_1} + \frac{1}{t_2} \implies T_{\text{معاً}} = \frac{t_1 t_2}{t_1 + t_2} \)"),
            ("طريقة الافتراض والتعويض", r"افترض كل \( N \) من الفئة \( v_1 \) ثم اقسم الفرق \( |S - N v_1| \) على \( |v_2 - v_1| \)"),
        ],
    ),
    "NSMO-L1-05": _cs(
        [
            ("Parallel Zigzag Angle Law", r"Between parallel lines: \( \sum \theta_{\text{left}} = \sum \theta_{\text{right}} \)"),
            ("Paper-Fold Reflection", r"Crease bisects the fold: folded angle \( \alpha' = \alpha \), so on a straight edge \( 2\alpha + \beta = 180^\circ \)"),
            ("Staircase Perimeter", r"Any monotonic staircase inside bounding box \( W \times H \) has perimeter \( 2(W + H) \)"),
            ("Painted n × n × n Cube", r"3 faces: \( 8 \); 2 faces: \( 12(n - 2) \); 1 face: \( 6(n - 2)^2 \); 0 faces: \( (n - 2)^3 \)"),
        ],
        [
            ("زوايا الخط المتعرج بين متوازيين", r"مجموع رؤوس الزوايا المتجهة يساراً يساوي مجموع المتجهة يميناً"),
            ("انعكاس طيّ الورق", r"خط الطيّ منصف زاوية: الزاوية بعد الطيّ تطابق موقعها الأصلي تماماً"),
            ("محيط المضلع الدرجي", r"أي شكل درجي رتيب أبعاده الكلية \( W \times H \) محيطه \( 2(W + H) \)"),
            ("تجزئة المكعب المطلي n×n×n", r"3 أوجه: \( 8 \)؛ وجهان: \( 12(n - 2) \)؛ وجه: \( 6(n - 2)^2 \)؛ بلا طلاء: \( (n - 2)^3 \)"),
        ],
    ),
    "NSMO-L1-06": _cs(
        [
            ("Shortest Lattice Grid Paths", r"From \( (0, 0) \) to \( (m, n) \) moving only E/N: \( \binom{m + n}{m} \) paths"),
            ("Generalized Pigeonhole", r"To guarantee \( k \) items in one of \( b \) boxes, draw \( b(k - 1) + 1 \) items"),
            ("3×3 Magic Square Constant", r"Line sum \( M = 3c \) and total of all \( 9 \) entries \( = 9c \), where \( c \) is the center cell"),
            ("Two-Dice Sum Symmetry", r"Out of \( 36 \) pairs, sum \( s \) occurs \( 6 - |s - 7| \) times (peak \( 6 \) ways at \( s = 7 \))"),
        ],
        [
            ("أقصر مسارات الشبكة", r"من \( (0, 0) \) إلى \( (m, n) \) بالحركة شرقاً وشمالاً فقط: \( \binom{m + n}{m} \) مساراً"),
            ("مبدأ برج الحمام المعمم", r"لضمان \( k \) عناصر في أحد \( b \) صناديق، اسحب \( b(k - 1) + 1 \) عنصراً"),
            ("ثابت المربع السحري 3×3", r"مجموع كل خط \( M = 3c \) ومجموع الأعداد التسعة \( = 9c \) حيث \( c \) الخلية الوسطى"),
            ("تماثل مجموع حجرَي النرد", r"من أصل \( 36 \) زوجاً، يظهر المجموع \( s \) بعدد \( 6 - |s - 7| \) طرق (الذروة عند \( 7 \))"),
        ],
    ),
    "NSMO-L2-01": _cs(
        [
            ("Chinese Remainder Stepping", r"For \( x \equiv a \pmod m,\; x \equiv b \pmod n \): step \( a, a + m, a + 2m, \dots \) then add \( \operatorname{LCM}(m, n) \)"),
            ("Trailing Zeros of n!", r"\( Z(n!) = v_5(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{5^k} \right\rfloor \)"),
            ("Coprime GCD–LCM Identity", r"\( a = gx,\; b = gy \) with \( \gcd(x, y) = 1 \implies g = \gcd(a, b),\; L = gxy \)"),
            ("Base-b Conversion", r"\( (d_k \dots d_1 d_0)_b = \sum_{i=0}^{k} d_i b^i \); repeated division by \( b \) reads digits bottom-up"),
        ],
        [
            ("القفز في البواقي المتزامنة (CRT)", r"ابدأ بحل المعادلة ذات المقسوم الأكبر \( a + km \) ثم أضف مضاعفات \( \operatorname{LCM}(m, n) \)"),
            ("الأصفار الطرفية للمضروب n!", r"\( Z(n!) = v_5(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{5^k} \right\rfloor \)"),
            ("تمثيل القاسم والمضاعف المشترك", r"\( a = gx,\; b = gy \) مع \( \gcd(x, y) = 1 \implies L = gxy \)"),
            ("التحويل بين أنظمة العد", r"\( (d_k \dots d_1 d_0)_b = \sum_{i=0}^{k} d_i b^i \) مع \( 0 \le d_i < b \)"),
        ],
    ),
    "NSMO-L2-02": _cs(
        [
            ("Strictly Increasing Digits", r"Strictly increasing \( k \)-digit numbers from \( \{1..9\} \): \( \binom{9}{k} \); non-decreasing: \( \binom{9 + k - 1}{k} \)"),
            ("Even-Length Palindrome Rule", r"Every palindrome with an even number of digits (`abba`, `abccba`) is divisible by \( 11 \)"),
            ("Chicken McNugget Theorem", r"For coprime \( a, b > 1 \): largest unattainable \( = ab - a - b \); count \( = \frac{(a - 1)(b - 1)}{2} \)"),
            ("Unit Fraction Pair Split", r"\( \frac{1}{x} + \frac{1}{y} = \frac{1}{n} \iff (x - n)(y - n) = n^2 \), giving \( \tau(n^2) \) ordered positive pairs"),
        ],
        [
            ("الأرقام المرتبة تصاعدياً", r"أعداد من \( k \) أرقام متزايدة بصرامة من \( \{1..9\} \): \( \binom{9}{k} \)؛ وغير متناقصة: \( \binom{9 + k - 1}{k} \)"),
            ("قاعدة المتناظرات زوجية الطول", r"كل عدد متناظر عددُ خاناته زوجي (`abba`, `abccba`) يقبل القسمة دائماً على \( 11 \)"),
            ("مبرهنة الطوابع (ماك ناجت)", r"لأوليين نسبياً \( a, b > 1 \): أكبر عدد مستحيل \( = ab - a - b \) وعدد المستحيلة \( \frac{(a - 1)(b - 1)}{2} \)"),
            ("تفكيك كسر الوحدة", r"\( \frac{1}{x} + \frac{1}{y} = \frac{1}{n} \iff (x - n)(y - n) = n^2 \) وعدد الأزواج المرتبة \( \tau(n^2) \)"),
        ],
    ),
    "NSMO-L2-03": _cs(
        [
            ("Simon's Factoring Trick", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("Difference-of-Squares Chain", r"\( \prod_{k=2}^{n} \left(1 - \frac{1}{k^2}\right) = \prod_{k=2}^{n} \frac{(k - 1)(k + 1)}{k^2} = \frac{n + 1}{2n} \)"),
            ("Rationalizing Surd Sums", r"\( \frac{1}{\sqrt{k + 1} + \sqrt{k}} = \sqrt{k + 1} - \sqrt{k} \implies \sum_{k=1}^{n} = \sqrt{n + 1} - 1 \)"),
            ("3-Variable Square Identity", r"\( a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) \)"),
        ],
        [
            ("حيلة سايمون للتحليل", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("سلسلة فرق المربعين", r"\( \prod_{k=2}^{n} \left(1 - \frac{1}{k^2}\right) = \frac{n + 1}{2n} \)"),
            ("إنطاق المقامات الجذرية المتداخلة", r"\( \frac{1}{\sqrt{k + 1} + \sqrt{k}} = \sqrt{k + 1} - \sqrt{k} \implies \sum_{k=1}^{n} = \sqrt{n + 1} - 1 \)"),
            ("متطابقة مجموع المربعات الثلاثية", r"\( a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) \)"),
        ],
    ),
    "NSMO-L2-04": _cs(
        [
            ("Vieta's Root Relations", r"For \( ax^2 + bx + c = 0 \): \( r_1 + r_2 = -\frac{b}{a} \), \( r_1 r_2 = \frac{c}{a} \), \( (r_1 - r_2)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \)"),
            ("Completing the Square Vertex", r"\( a(x - h)^2 + k \) reaches its extremum \( k \) at \( x = h = -\frac{b}{2a} \)"),
            ("Piecewise Absolute Minimum", r"\( |x - a_1| + \dots + |x - a_m| \) is minimized when \( x \) equals the median of \( a_1, \dots, a_m \)"),
            ("AP & GP Mean Links", r"AP middle: \( 2b = a + c \); GP middle: \( b^2 = ac \); round-trip speed: \( \frac{2v_1 v_2}{v_1 + v_2} \)"),
        ],
        [
            ("علاقات فييت للجذرين", r"للمعادلة \( ax^2 + bx + c = 0 \): \( r_1 + r_2 = -\frac{b}{a} \)، \( r_1 r_2 = \frac{c}{a} \)، \( (r_1 - r_2)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \)"),
            ("إكمال المربع ورأس القطع", r"\( a(x - h)^2 + k \) تبلغ قيمتها القصوى/الصغرى \( k \) عند \( x = -\frac{b}{2a} \)"),
            ("القيمة الصغرى لمجموع القيم المطلقة", r"المقدار \( \sum |x - a_i| \) يبلغ أصغر قيمة له عندما يساوي \( x \) وسيط القيم \( a_i \)"),
            ("الأوساط الحسابية والهندسية والتوافقية", r"حسابي: \( 2b = a + c \)؛ هندسي: \( b^2 = ac \)؛ سرعة الذهاب والإياب: \( \frac{2v_1 v_2}{v_1 + v_2} \)"),
        ],
    ),
    "NSMO-L2-05": _cs(
        [
            ("Similarity Area Scaling", r"If \( \triangle ABC \sim \triangle DEF \) with side ratio \( k \), then \( \frac{[ABC]}{[DEF]} = k^2 \)"),
            ("Thales' Semicircle Right Angle", r"If \( AB \) is a diameter and \( C \) lies on the circle, then \( \angle ACB = 90^\circ \) and \( R = \frac{AB}{2} \)"),
            ("Shared-Altitude Area Ratio", r"Triangles sharing an apex and base line divide area in exact base ratio: \( \frac{[ABD]}{[ADC]} = \frac{BD}{DC} \)"),
            ("Convex Polygon Angle Sums", r"Interior sum \( = (n - 2) \times 180^\circ \); regular interior angle \( = 180^\circ - \frac{360^\circ}{n} \)"),
        ],
        [
            ("نسبة المساحات في التشابه", r"إذا تشابه مثلثان بمعامل خطي \( k \) فإن نسبة مساحتيهما \( k^2 \)"),
            ("مبرهنة طاليس في نصف الدائرة", r"إذا كان \( AB \) قطراً و\( C \) على الدائرة فإن \( \angle ACB = 90^\circ \) و\( R = \frac{AB}{2} \)"),
            ("نسبة مساحتي مثلثين لهما نفس الارتفاع", r"المثلثان المشتركان في الرأس على استقامة واحدة: \( \frac{[ABD]}{[ADC]} = \frac{BD}{DC} \)"),
            ("مجموع زوايا المضلع المحدب", r"مجموع الزوايا الداخلية \( = (n - 2)\times 180^\circ \)؛ وزاوية المنتظم \( = 180^\circ - \frac{360^\circ}{n} \)"),
        ],
    ),
    "NSMO-L2-06": _cs(
        [
            ("Blocked-Node Lattice Paths", r"Paths avoiding \( P \) equal \( \binom{m+n}{m} - \binom{x_P + y_P}{x_P}\binom{(m - x_P) + (n - y_P)}{m - x_P} \)"),
            ("Stars and Bars Formula", r"Non-negative integer solutions to \( x_1 + \dots + x_k = n \): \( \binom{n + k - 1}{k - 1} \)"),
            ("3-Set Inclusion–Exclusion", r"\( |A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C| \)"),
            ("Law of Total Probability", r"\( P(B) = \sum_{i} P(A_i) P(B \mid A_i) \) across mutually exclusive Stage-1 cases \( A_i \)"),
        ],
        [
            ("مسارات الشبكة مع نقطة محظورة", r"اطرح المسارات المارة بـ \( P \): \( \binom{m+n}{m} - \binom{x_P + y_P}{x_P}\binom{(m - x_P) + (n - y_P)}{m - x_P} \)"),
            ("صيغة النجوم والفواصل", r"عدد الحلول الصحيحة غير السالبة لـ \( x_1 + \dots + x_k = n \) هو \( \binom{n + k - 1}{k - 1} \)"),
            ("التضمين والإقصاء لثلاث مجموعات", r"\( |A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C| \)"),
            ("قانون الاحتمال الكلي", r"\( P(B) = \sum_{i} P(A_i) P(B \mid A_i) \) عبر جميع فروع المرحلة الأولى"),
        ],
    ),
    "NSMO-L3-01": _cs(
        [
            ("Euler's Totient Theorem", r"\( \varphi(n) = n \prod_{p \mid n}\left(1 - \frac{1}{p}\right) \); for \( \gcd(a, n) = 1 \), \( a^{\varphi(n)} \equiv 1 \pmod n \)"),
            ("Legendre's p-adic Valuation", r"\( v_p(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - s_p(n)}{p - 1} \)"),
            ("Square & Cube Divisors", r"For \( n = \prod p_i^{e_i} \): square divisors \( = \prod \left(\lfloor e_i / 2 \rfloor + 1\right) \); cube divisors \( = \prod \left(\lfloor e_i / 3 \rfloor + 1\right) \)"),
            ("Frobenius Two-Generator Bound", r"Coprime \( a, b > 1 \): max unattainable \( = ab - a - b \); unattainable count \( = \frac{(a - 1)(b - 1)}{2} \)"),
        ],
        [
            ("دالة أويلر ومبرهنة أويلر", r"\( \varphi(n) = n \prod_{p \mid n}\left(1 - \frac{1}{p}\right) \)؛ وعند \( \gcd(a, n) = 1 \): \( a^{\varphi(n)} \equiv 1 \pmod n \)"),
            ("صيغة ليجاندر لأس العامل الأولي", r"\( v_p(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - s_p(n)}{p - 1} \)"),
            ("عدد القواسم المربعة والمكعبة", r"للعدد \( \prod p_i^{e_i} \): القواسم المربعة \( = \prod \left(\lfloor e_i / 2 \rfloor + 1\right) \) والمكعبة \( = \prod \left(\lfloor e_i / 3 \rfloor + 1\right) \)"),
            ("حد فروبينيوس لمولّدين أوليين نسبياً", r"أكبر عدد غير قابل للتمثيل \( = ab - a - b \) وعدد الأعداد المستحيلة \( = \frac{(a - 1)(b - 1)}{2} \)"),
        ],
    ),
    "NSMO-L3-02": _cs(
        [
            ("Polynomial Remainder Trick", r"To make \( \frac{P(n)}{n - a} \in \mathbb{Z} \), rewrite \( P(n) = Q(n)(n - a) + P(a) \) so \( (n - a) \mid P(a) \)"),
            ("Integer Square-Block Sum", r"Between \( m^2 \) and \( (m + 1)^2 - 1 \) there are \( 2m + 1 \) integers all having \( \lfloor \sqrt{k} \rfloor = m \)"),
            ("Floor-Fractional Split", r"Substitute \( x = \lfloor x \rfloor + \{x\} \) with integer \( \lfloor x \rfloor \in \mathbb{Z} \) and \( 0 \le \{x\} < 1 \)"),
            ("Prime Mod 2 & Mod 3 Sieve", r"Even prime \( p = 2 \); every prime \( p > 3 \) satisfies \( p^2 \equiv 1 \pmod{24} \) (so \( p^2 \equiv 1 \pmod 3 \) and \( \pmod 8 \))"),
        ],
        [
            ("عزل الباقي الثابت لكثيرة الحدود", r"لجعل \( \frac{P(n)}{n - a} \in \mathbb{Z} \) اكتب \( P(n) = Q(n)(n - a) + P(a) \) فيجب \( (n - a) \mid P(a) \)"),
            ("كتل دالة جذر الجزء الصحيح", r"بين \( m^2 \) و\( (m + 1)^2 - 1 \) يوجد \( 2m + 1 \) عدداً جميعها تحقق \( \lfloor \sqrt{k} \rfloor = m \)"),
            ("تفكيك الجزء الصحيح والكسري", r"عوّض \( x = \lfloor x \rfloor + \{x\} \) حيث \( \lfloor x \rfloor \in \mathbb{Z} \) و\( 0 \le \{x\} < 1 \)"),
            ("غربال الأعداد الأولية mod 2 وmod 3", r"الأولي الزوجي الوحيد \( 2 \)؛ ولكل أولي \( p > 3 \) يتحقق \( p^2 \equiv 1 \pmod{24} \)"),
        ],
    ),
    "NSMO-L3-03": _cs(
        [
            ("Linear Remainder System", r"\( P(x) = Q(x)(x - a)(x - b) + mx + c \); plug in \( x = a \) and \( x = b \) to solve for \( m, c \)"),
            ("Gauss's Cubic Identity", r"\( a^3 + b^3 + c^3 - 3abc = (a + b + c)\!\left[(a + b + c)^2 - 3(ab + bc + ca)\right] \)"),
            ("Denesting Square Roots", r"\( \sqrt{(u + v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \) for \( u \ge v \ge 0 \)"),
            ("Sophie Germain Identity", r"\( a^4 + 4b^4 = (a^2 - 2ab + 2b^2)(a^2 + 2ab + 2b^2) \)"),
        ],
        [
            ("الباقي الخطي لقسمة كثيرات الحدود", r"\( P(x) = Q(x)(x - a)(x - b) + mx + c \)؛ عوّض \( x = a \) و\( x = b \) لإيجاد \( m, c \)"),
            ("متطابقة غاوس التكعيبية", r"\( a^3 + b^3 + c^3 - 3abc = (a + b + c)\!\left[(a + b + c)^2 - 3(ab + bc + ca)\right] \)"),
            ("فك الجذور المزدوجة", r"\( \sqrt{(u + v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \) بشرط \( u \ge v \ge 0 \)"),
            ("متطابقة صوفي جيرمان", r"\( a^4 + 4b^4 = (a^2 - 2ab + 2b^2)(a^2 + 2ab + 2b^2) \)"),
        ],
    ),
    "NSMO-L3-04": _cs(
        [
            ("Involution Elimination", r"Given \( a f(x) + b f(g(x)) = h(x) \) with \( g(g(x)) = x \), substitute \( x \leftarrow g(x) \) and eliminate \( f(g(x)) \)"),
            ("AM-GM Equal-Piece Split", r"For \( x > 0 \): \( x + \frac{c}{x^n} = \underbrace{\frac{x}{n} + \dots + \frac{x}{n}}_{n} + \frac{c}{x^n} \ge (n + 1)\sqrt[n+1]{\frac{c}{n^n}} \)"),
            ("Titu's Lemma (Engel Form)", r"For \( b_i > 0 \): \( \sum_{i=1}^{n} \frac{a_i^2}{b_i} \ge \frac{(a_1 + \dots + a_n)^2}{b_1 + \dots + b_n} \)"),
            ("Manhattan Lattice Count", r"Integer points satisfying \( |x| + |y| \le R \) equal \( 2R^2 + 2R + 1 \) (area \( = 2R^2 \))"),
        ],
        [
            ("الحذف بالدوال الالتفافية", r"إذا كان \( g(g(x)) = x \) في \( a f(x) + b f(g(x)) = h(x) \) فعوّض \( g(x) \) واحذف \( f(g(x)) \)"),
            ("تجزئة الحدود في متباينة AM-GM", r"\( x + \frac{c}{x^n} = \frac{x}{n} + \dots + \frac{x}{n} + \frac{c}{x^n} \ge (n + 1)\sqrt[n+1]{\frac{c}{n^n}} \)"),
            ("متباينة تيتو (صورة إنجل)", r"لكل \( b_i > 0 \): \( \sum_{i=1}^{n} \frac{a_i^2}{b_i} \ge \frac{(a_1 + \dots + a_n)^2}{b_1 + \dots + b_n} \)"),
            ("النقاط الصحيحة لمعين مانهاتن", r"عدد النقاط الصحيحة التي تحقق \( |x| + |y| \le R \) هو \( 2R^2 + 2R + 1 \) والمساحة \( 2R^2 \)"),
        ],
    ),
    "NSMO-L3-05": _cs(
        [
            ("Power of a Point", r"Chords: \( PA \cdot PB = PC \cdot PD \); Secant-Tangent: \( PT^2 = PA \cdot PB = d^2 - R^2 \)"),
            ("Ptolemy's Cyclic Quad Theorem", r"For cyclic quadrilateral \( ABCD \): \( AC \cdot BD = AB \cdot CD + BC \cdot DA \)"),
            ("Angle Bisector & Apollonius", r"Bisector: \( \frac{BD}{DC} = \frac{AB}{AC} \), \( \ell_a^2 = bc - BD\cdot DC \); Median: \( m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4} \)"),
            ("Heron Area & Inradius", r"\( [ABC] = \sqrt{s(s - a)(s - b)(s - c)} = r \cdot s = \frac{abc}{4R} \) where \( s = \frac{a + b + c}{2} \)"),
        ],
        [
            ("قوة نقطة بالنسبة لدائرة", r"الأوتار: \( PA \cdot PB = PC \cdot PD \)؛ المماس والقاطع: \( PT^2 = PA \cdot PB = d^2 - R^2 \)"),
            ("مبرهنة بطليموس للرباعي الدائري", r"في الرباعي الدائري \( ABCD \): \( AC \cdot BD = AB \cdot CD + BC \cdot DA \)"),
            ("منصّف الزاوية ومتوسط أبولونيوس", r"المنصف: \( \frac{BD}{DC} = \frac{c}{b} \) و\( \ell_a^2 = bc - BD\cdot DC \)؛ المتوسط: \( m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4} \)"),
            ("صيغة هيرون ونصف قطر الداخلة", r"\( [ABC] = \sqrt{s(s - a)(s - b)(s - c)} = r \cdot s = \frac{abc}{4R} \)"),
        ],
    ),
    "NSMO-L3-06": _cs(
        [
            ("Derangements & Circular Seats", r"\( D_n = (n - 1)(D_{n - 1} + D_{n - 2}) \) (\( 0, 1, 2, 9, 44 \)); \( n \) around a round table: \( (n - 1)! \)"),
            ("No-Consecutive-1s Binary Strings", r"Binary strings of length \( n \) with no `11` satisfy \( a_n = a_{n - 1} + a_{n - 2} = F_{n + 2} \)"),
            ("Handshaking & Polygon Chords", r"\( \sum \deg(v) = 2|E| \); interior chord intersections of convex \( n \)-gon (general position) \( = \binom{n}{4} \)"),
            ("Bayes' Rule & Vandermonde", r"\( P(A \mid B) = \frac{P(A)P(B \mid A)}{P(B)} \); Vandermonde convolution: \( \sum_{k=0}^{r} \binom{m}{k}\binom{n}{r - k} = \binom{m + n}{r} \)"),
        ],
        [
            ("التشويشات والجلوس الدائري", r"\( D_n = (n - 1)(D_{n - 1} + D_{n - 2}) \) (\( 0, 1, 2, 9, 44 \))؛ وحول طاولة دائرية \( (n - 1)! \)"),
            ("السلاسل الثنائية بلا `11` متجاورين", r"عدد السلاسل الثنائية بطول \( n \) دون واحدين متجاورين يحقق فيبوناتشي \( a_n = F_{n + 2} \)"),
            ("المصافحات وتقاطعات الأوتار", r"\( \sum \deg(v) = 2|E| \)؛ وتقاطعات أوتار مضلع محدب \( n \)-ي تساوي \( \binom{n}{4} \)"),
            ("قاعدة بايز وهوية فاندرموند", r"\( P(A \mid B) = \frac{P(A)P(B \mid A)}{P(B)} \)؛ وهوية فاندرموند \( \sum \binom{m}{k}\binom{n}{r - k} = \binom{m + n}{r} \)"),
        ],
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # Math Olympiad (Grades 7–12): OLYM-L1-01 .. OLYM-L3-06 (18 lessons)
    # ══════════════════════════════════════════════════════════════════════════
    "OLYM-L1-01": _cs(
        [
            ("Divisor Count & Sum", r"For \( n = \prod p_i^{e_i} \): \( \tau(n) = \prod(e_i + 1) \) and \( \sigma(n) = \prod \frac{p_i^{e_i + 1} - 1}{p_i - 1} \)"),
            ("Euclidean GCD Invariant", r"\( \gcd(a, b) = \gcd(a - kb, b) \), and \( a \cdot b = \gcd(a, b) \cdot \operatorname{LCM}(a, b) \)"),
            ("Simon's Factoring Trick", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("Difference of Squares Parity", r"\( x^2 - y^2 = N \iff (x - y)(x + y) = N \) with factors of identical parity"),
        ],
        [
            ("عدد القواسم ومجموعها", r"للعدد \( n = \prod p_i^{e_i} \): \( \tau(n) = \prod(e_i + 1) \) و\( \sigma(n) = \prod \frac{p_i^{e_i + 1} - 1}{p_i - 1} \)"),
            ("ثابت خوارزمية إقليدس", r"\( \gcd(a, b) = \gcd(a - kb, b) \)، وكذلك \( a \cdot b = \gcd(a, b) \cdot \operatorname{LCM}(a, b) \)"),
            ("حيلة سايمون للتحليل", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("زوجية عوامل فرق المربعين", r"\( x^2 - y^2 = N \iff (x - y)(x + y) = N \) لعاملين من نفس الزوجية"),
        ],
    ),
    "OLYM-L1-02": _cs(
        [
            ("Telescoping Partial Fractions", r"\( \frac{1}{k(k + 1)(k + 2)} = \frac{1}{2}\!\left[\frac{1}{k(k + 1)} - \frac{1}{(k + 1)(k + 2)}\right] \)"),
            ("Gauss's Cubic Factorization", r"\( a^3 + b^3 + c^3 - 3abc = \frac{1}{2}(a + b + c)\!\left[(a - b)^2 + (b - c)^2 + (c - a)^2\right] \)"),
            ("Radical Denesting Rule", r"\( \sqrt{(u + v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \) for \( u \ge v \ge 0 \)"),
            ("Reciprocal Power Recurrence", r"If \( x + x^{-1} = t \), then \( S_n = x^n + x^{-n} \) satisfies \( S_n = t S_{n - 1} - S_{n - 2} \)"),
        ],
        [
            ("الكسور الجزئية المتداخلة", r"\( \frac{1}{k(k + 1)(k + 2)} = \frac{1}{2}\!\left[\frac{1}{k(k + 1)} - \frac{1}{(k + 1)(k + 2)}\right] \)"),
            ("متطابقة غاوس التكعيبية", r"\( a^3 + b^3 + c^3 - 3abc = \frac{1}{2}(a + b + c)\!\left[(a - b)^2 + (b - c)^2 + (c - a)^2\right] \)"),
            ("قاعدة فك الجذور المركبة", r"\( \sqrt{(u + v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \) بشرط \( u \ge v \ge 0 \)"),
            ("تراجعية القوى المقلوبة", r"إذا كان \( x + x^{-1} = t \) فإن \( S_n = x^n + x^{-n} \) تحقق \( S_n = t S_{n - 1} - S_{n - 2} \)"),
        ],
    ),
    "OLYM-L1-03": _cs(
        [
            ("Trivial Square Inequality", r"\( (A - B)^2 \ge 0 \implies A^2 + B^2 \ge 2AB \) and \( a^2 + b^2 + c^2 \ge ab + bc + ca \)"),
            ("Domain-Shifted AM–GM", r"For \( x > c \): \( x + \frac{k}{x - c} = (x - c) + \frac{k}{x - c} + c \ge 2\sqrt{k} + c \)"),
            ("Ravi Triangle Substitution", r"For triangle sides \( a, b, c \), set \( a = y + z,\; b = z + x,\; c = x + y \) with \( x, y, z > 0 \)"),
            ("Discrete Sum-Product Bound", r"With fixed sum \( A + B = S \), \( A \cdot B \) increases as \( |A - B| \) decreases"),
        ],
        [
            ("المتباينة التربيعية الأساسية", r"\( (A - B)^2 \ge 0 \implies A^2 + B^2 \ge 2AB \) وكذلك \( a^2 + b^2 + c^2 \ge ab + bc + ca \)"),
            ("إزاحة المجال في AM–GM", r"لكل \( x > c \): \( x + \frac{k}{x - c} = (x - c) + \frac{k}{x - c} + c \ge 2\sqrt{k} + c \)"),
            ("تعويض رافي لأضلاع المثلث", r"لأضلاع مثلث \( a, b, c \) ضع \( a = y + z,\; b = z + x,\; c = x + y \) مع \( x, y, z > 0 \)"),
            ("تقريب المتغيرات عند ثبات المجموع", r"مع ثبات المجموع \( A + B = S \)، يزداد الجداء \( A \cdot B \) كلما صغر الفرق \( |A - B| \)"),
        ],
    ),
    "OLYM-L1-04": _cs(
        [
            ("Cyclic Quad & Tangent-Chord", r"Cyclic iff \( \angle A + \angle C = 180^\circ \) or \( \angle ADB = \angle ACB \); tangent-chord angle \( = \) inscribed angle"),
            ("Shared-Altitude & Similarity", r"Same altitude: \( \frac{[ABD]}{[ADC]} = \frac{BD}{DC} \); similar with scale \( k \implies \text{Area ratio} = k^2 \)"),
            ("Incircle Tangent Lengths", r"From vertices \( A, B, C \) to touchpoints: \( s - a,\; s - b,\; s - c \) where \( s = \frac{a + b + c}{2} \)"),
            ("Inradius & Right-Triangle r", r"General: \( [ABC] = r \cdot s \); right triangle with legs \( a, b \) and hypotenuse \( c \): \( r = \frac{a + b - c}{2} \)"),
        ],
        [
            ("الرباعي الدائري والزاوية المماسية", r"رباعي دائري \(\iff \angle A + \angle C = 180^\circ\) أو \(\angle ADB = \angle ACB\)؛ والمماسية تساوي المحيطية"),
            ("نسبة القواعد والتشابه", r"نفس الارتفاع: \( \frac{[ABD]}{[ADC]} = \frac{BD}{DC} \)؛ والتشابه بمعامل \( k \) يعطي نسبة مساحة \( k^2 \)"),
            ("أطوال مماسات الدائرة الداخلة", r"من الرؤوس \( A, B, C \) لنقاط التماس: \( s - a,\; s - b,\; s - c \) حيث \( s = \frac{a + b + c}{2} \)"),
            ("نصف قطر الدائرة الداخلة", r"عامّاً: \( [ABC] = r \cdot s \)؛ وفي المثلث القائم \( r = \frac{a + b - c}{2} \)"),
        ],
    ),
    "OLYM-L1-05": _cs(
        [
            ("Heron's Mirror Reflection", r"Shortest \( A \to P \to B \) with \( P \in \ell \) equals straight segment \( A'B \) where \( A' = \text{Ref}_\ell(A) \)"),
            ("Polygon Angles & Diagonals", r"Interior sum \( = (n - 2)180^\circ \); number of diagonals \( = \frac{n(n - 3)}{2} \)"),
            ("Pick's Lattice Theorem", r"For a simple lattice polygon: \( \text{Area} = I + \frac{B}{2} - 1 \)"),
            ("Unfolded 3D Ant Geodesic", r"On an \( a \times b \times c \) box (\( a \le b \le c \)), shortest corner-to-opposite-corner surface path \( = \sqrt{(a + b)^2 + c^2} \)"),
        ],
        [
            ("مبدأ انعكاس هيرون لأقصر مسار", r"أقصر مسار \( A \to P \to B \) عبر المستقيم \( \ell \) هو القطعة المستقيمة \( A'B \) بانعكاس \( A \)"),
            ("زوايا وأقطار المضلع", r"مجموع الزوايا الداخلية \( = (n - 2)180^\circ \)؛ وعدد الأقطار \( = \frac{n(n - 3)}{2} \)"),
            ("مبرهنة بيك للشبكات", r"مساحة مضلع رؤوسه شبكية بسيطة: \( \text{Area} = I + \frac{B}{2} - 1 \)"),
            ("أقصر مسار سطحي على الصندوق", r"على متوازي مستطيلات \( a \le b \le c \)، أقصر مسار سطحي بين ركنين متقابلين \( = \sqrt{(a + b)^2 + c^2} \)"),
        ],
    ),
    "OLYM-L1-06": _cs(
        [
            ("Stars & Bars with Quotas", r"For \( x_i \ge c_i \) and \( \sum_{i=1}^{k} x_i = n \), set \( y_i = x_i - c_i \ge 0 \implies \binom{n - \sum c_i + k - 1}{k - 1} \)"),
            ("Dirichlet Ceiling Pigeonhole", r"\( N \) objects into \( k \) boxes guarantees a box with at least \( \lceil N / k \rceil \) objects"),
            ("Parity & Mod Invariants", r"Check whether a move changes sum mod \( 2 \), inversions mod \( 2 \), or alternating color difference"),
            ("Inclusion–Exclusion (PIE)", r"\( \left|\bigcup_{i=1}^{m} A_i\right| = \sum |A_i| - \sum_{i < j} |A_i \cap A_j| + \sum_{i < j < k} |A_i \cap A_j \cap A_k| - \cdots \)"),
        ],
        [
            ("النجوم والفواصل مع حدود دنيا", r"للشرط \( x_i \ge c_i \) مع \( \sum x_i = n \)، ضع \( y_i = x_i - c_i \ge 0 \implies \binom{n - \sum c_i + k - 1}{k - 1} \)"),
            ("صيغة السقف لمبدأ برج الحمام", r"توزيع \( N \) عنصراً على \( k \) صناديق يضمن صندوقاً يحوي \( \lceil N / k \rceil \) عنصراً على الأقل"),
            ("ثوابت الزوجية والتلوين", r"افحص تغيّر المجموع mod \( 2 \) أو فرق الخلايا السوداء والبيضاء بعد كل حركة"),
            ("مبدأ التضمين والإقصاء", r"\( \left|\bigcup_{i=1}^{m} A_i\right| = \sum |A_i| - \sum_{i < j} |A_i \cap A_j| + \cdots \)"),
        ],
    ),
    "OLYM-L2-01": _cs(
        [
            ("Euler–Fermat Congruence", r"\( \gcd(a, n) = 1 \implies a^{\varphi(n)} \equiv 1 \pmod n \), where \( \varphi(n) = n \prod_{p \mid n}(1 - 1/p) \)"),
            ("Chinese Remainder Uniqueness", r"Pairwise coprime moduli \( m_1, \dots, m_k \) determine a unique residue mod \( M = m_1 \cdots m_k \)"),
            ("Legendre's Factorial Formula", r"\( v_p(n!) = \sum_{j \ge 1} \left\lfloor \frac{n}{p^j} \right\rfloor = \frac{n - s_p(n)}{p - 1} \)"),
            ("PPT & Pell Solutions", r"Primitive Pythagorean: \( (m^2 - n^2, 2mn, m^2 + n^2) \); Pell \( x^2 - dy^2 = 1 \): \( x_k + y_k\sqrt{d} = (x_1 + y_1\sqrt{d})^k \)"),
        ],
        [
            ("مبرهنة أويلر–فيرما", r"\( \gcd(a, n) = 1 \implies a^{\varphi(n)} \equiv 1 \pmod n \) حيث \( \varphi(n) = n \prod_{p \mid n}(1 - 1/p) \)"),
            ("وحدانية الباقي الصيني (CRT)", r"المقاسات الأولية مثنى مثنى \( m_1, \dots, m_k \) تحدد حلاً وحيداً mod \( M = m_1 \cdots m_k \)"),
            ("صيغة ليجاندر للمضروب", r"\( v_p(n!) = \sum_{j \ge 1} \left\lfloor \frac{n}{p^j} \right\rfloor = \frac{n - s_p(n)}{p - 1} \)"),
            ("ثلاثيات فيثاغورس ومعادلة بيل", r"فيثاغورس الأولية: \( (m^2 - n^2, 2mn, m^2 + n^2) \)؛ وبيل: \( x_k + y_k\sqrt{d} = (x_1 + y_1\sqrt{d})^k \)"),
        ],
    ),
    "OLYM-L2-02": _cs(
        [
            ("Newton's Power-Sum Identity", r"For \( x^n - e_1 x^{n-1} + e_2 x^{n-2} - \dots = 0 \): \( p_k - e_1 p_{k-1} + e_2 p_{k-2} - \dots + (-1)^k k e_k = 0 \)"),
            ("Remainder Reconstruction", r"Degree-\( d \) monic \( P \) with \( P(k) = Q(k) \) at \( k = 1..d \) satisfies \( P(x) = Q(x) + \prod_{k=1}^{d}(x - k) \)"),
            ("Fractional-Order Involution", r"For \( T(x) = \frac{1}{1 - x} \), \( T^3(x) = x \): substitute \( x,\; T(x),\; T^2(x) \) for a cyclic \( 3 \)-equation system"),
            ("Hermite's Floor Identity", r"\( \sum_{k=0}^{n - 1} \left\lfloor x + \frac{k}{n} \right\rfloor = \lfloor nx \rfloor \) for every real \( x \) and positive integer \( n \)"),
        ],
        [
            ("متطابقة نيوتن لمجاميع القوى", r"للجذور: \( p_k - e_1 p_{k-1} + e_2 p_{k-2} - \dots + (-1)^k k e_k = 0 \)"),
            ("إعادة بناء كثيرة الحدود", r"أحادية من الدرجة \( d \) تحقق \( P(k) = Q(k) \) عند \( k = 1..d \): \( P(x) = Q(x) + \prod_{k=1}^{d}(x - k) \)"),
            ("الدورة الثلاثية للدوال الكسرية", r"للتحويل \( T(x) = \frac{1}{1 - x} \) يتحقق \( T^3(x) = x \)؛ عوّض الحدود الثلاثة لحل النظام"),
            ("متطابقة هيرميت للجزء الصحيح", r"\( \sum_{k=0}^{n - 1} \left\lfloor x + \frac{k}{n} \right\rfloor = \lfloor nx \rfloor \) لكل \( x \in \mathbb{R} \) و\( n \in \mathbb{Z}^+ \)"),
        ],
    ),
    "OLYM-L2-03": _cs(
        [
            ("Equal-Weight AM–GM Splitting", r"Split terms so equality holds at the target point \( x = x_0 \) before applying \( \text{AM} \ge \text{GM} \)"),
            ("Cauchy–Schwarz & Titu's Lemma", r"\( (\sum a_i^2)(\sum b_i^2) \ge (\sum a_i b_i)^2 \), and \( \sum \frac{a_i^2}{b_i} \ge \frac{(\sum a_i)^2}{\sum b_i} \) for \( b_i > 0 \)"),
            ("Nesbitt's 3-Variable Bound", r"For \( a, b, c > 0 \): \( \frac{a}{b + c} + \frac{b}{c + a} + \frac{c}{a + b} \ge \frac{3}{2} \)"),
            ("Rearrangement Inequality", r"For sorted \( a_1 \le \dots \le a_n \) and \( b_1 \le \dots \le b_n \): \( \sum a_i b_{n + 1 - i} \le \sum a_i b_{\pi(i)} \le \sum a_i b_i \)"),
        ],
        [
            ("موازنة الأوزان في AM–GM", r"جزّئ الحدود بحيث تتساوى جميع القطع عند نقطة المساواة المستهدفة"),
            ("متباينة كوشي–شفارتز وتيتو", r"\( (\sum a_i^2)(\sum b_i^2) \ge (\sum a_i b_i)^2 \)، و\( \sum \frac{a_i^2}{b_i} \ge \frac{(\sum a_i)^2}{\sum b_i} \)"),
            ("متباينة نسبيت الشهيرة", r"لكل \( a, b, c > 0 \): \( \frac{a}{b + c} + \frac{b}{c + a} + \frac{c}{a + b} \ge \frac{3}{2} \)"),
            ("متباينة إعادة الترتيب", r"للمتتابعتين المرتبتين: عكس الترتيب يعطي الأصغر ونفس الترتيب يعطي الأكبر"),
        ],
    ),
    "OLYM-L2-04": _cs(
        [
            ("Power of a Point & Radical Axis", r"\( \operatorname{Pow}_\omega(P) = d^2 - R^2 \); points of equal power to two circles form a line \( \perp O_1 O_2 \)"),
            ("Ptolemy & Brahmagupta", r"Cyclic quad: \( ef = ac + bd \) and \( [ABCD] = \sqrt{(s - a)(s - b)(s - c)(s - d)} \)"),
            ("Ceva & Menelaus", r"\( \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1 \) (concurrent cevians / collinear transversal)"),
            ("Stewart's Cevian Identity", r"On side \( BC = a \) split into \( m + n = a \) by \( AD = d \): \( m b^2 + n c^2 = a(d^2 + mn) \) (‘man + dad = bmb + cnc’)"),
        ],
        [
            ("قوة نقطة والمحور الأساسي", r"\( \operatorname{Pow}_\omega(P) = d^2 - R^2 \)؛ المحل الهندسي لتساوي القوة خط عمودي على خط المركزين"),
            ("بطليموس وبراهماغوبتا", r"في الرباعي الدائري: \( ef = ac + bd \) والمساحة \( \sqrt{(s - a)(s - b)(s - c)(s - d)} \)"),
            ("سيفا ومنيلاوس", r"\( \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1 \) لتلاقي المستقيمات أو استقامة النقاط"),
            ("متطابقة ستيوارت للقطعة الداخلية", r"لقسمَي القاعدة \( m + n = a \) والقطعة \( AD = d \): \( m b^2 + n c^2 = a(d^2 + mn) \)"),
        ],
    ),
    "OLYM-L2-05": _cs(
        [
            ("Euler Line & Nine-Point Circle", r"Collinear \( O, G, H \) with \( OG : GH = 1 : 2 \); nine-point radius \( R_9 = \frac{R}{2} \) centered at midpoint of \( OH \)"),
            ("Exradii & Carnot's Theorem", r"\( [ABC] = r_a(s - a) \), \( \frac{1}{r_a} + \frac{1}{r_b} + \frac{1}{r_c} = \frac{1}{r} \), and \( d_a + d_b + d_c = R + r \)"),
            ("Centroid Medial Homothety", r"Homothety \( \mathcal{H}(G, -\frac{1}{2}) \) maps \( \triangle ABC \) to its medial triangle and \( H \mapsto O \)"),
            ("Tangent Spheres & Descartes Circle", r"Externally tangent radii \( R_1, R_2 \) have common tangent segment \( 2\sqrt{R_1 R_2} \)"),
        ],
        [
            ("خط أويلر ودائرة النقاط التسع", r"تقع \( O, G, H \) على استقامة بنسبة \( OG : GH = 1 : 2 \)؛ ونصف قطر دائرة التسع \( R / 2 \)"),
            ("الدوائر الخارجة ومبرهنة كارنو", r"\( [ABC] = r_a(s - a) \)، و\( \sum \frac{1}{r_a} = \frac{1}{r} \)، ومجموع أبعاد المركز عن الأضلاع \( R + r \)"),
            ("التحاكي حول مركز الثقل", r"التحاكي \( \mathcal{H}(G, -\frac{1}{2}) \) يحوّل \( \triangle ABC \) إلى مثلث المنتصفات ويحوّل \( H \mapsto O \)"),
            ("تماس الكرات والدوائر", r"دائرتان متماستان خارجياً نصفا قطريهما \( R_1, R_2 \) طول مماسهما المشترك \( 2\sqrt{R_1 R_2} \)"),
        ],
    ),
    "OLYM-L2-06": _cs(
        [
            ("Catalan Bijection Family", r"\( C_n = \frac{1}{n + 1}\binom{2n}{n} \) counts Dyck paths, valid \( n \)-parentheses, and \((n + 2)\)-gon triangulations"),
            ("Characteristic Root Recurrence", r"\( a_n = p a_{n-1} + q a_{n-2} \) solves via roots of \( r^2 - pr - q = 0 \): \( \alpha r_1^n + \beta r_2^n \)"),
            ("Trees & Planar Euler Formula", r"Every tree has \( |E| = |V| - 1 \); connected planar graph satisfies \( V - E + F = 2 \) and \( E \le 3V - 6 \)"),
            ("Nim XOR & Monovariants", r"Nim position \((n_1, \dots, n_k)\) is P-position (second wins) iff \( n_1 \oplus \dots \oplus n_k = 0 \); strictly decreasing integer monovariant forces termination"),
        ],
        [
            ("عائلة تقابلات كاتالان", r"\( C_n = \frac{1}{n + 1}\binom{2n}{n} \) تعدّ مسارات دايك والأقواس المتزنة وتثليثات المضلع \( (n + 2) \)"),
            ("المعادلة المميزة للتراجعيات", r"\( a_n = p a_{n-1} + q a_{n-2} \) تُحل بجذور \( r^2 - pr - q = 0 \)"),
            ("الأشجار والبيانات المستوية", r"كل شجرة تحقق \( |E| = |V| - 1 \)؛ والبيان المستوي المتصل يحقق \( V - E + F = 2 \)"),
            ("لعبة نيم وشبه الثوابت", r"وضعية نيم خاسرة للبادئ \(\iff n_1 \oplus \dots \oplus n_k = 0\)؛ وشبه الثابت المتناقص يضمن التوقف"),
        ],
    ),
    "OLYM-L3-01": _cs(
        [
            ("Lifting the Exponent (LTE)", r"Odd \( p \mid x - y,\; p \nmid xy \implies v_p(x^n - y^n) = v_p(x - y) + v_p(n) \)"),
            ("Multiplicative Order Law", r"\( a^k \equiv 1 \pmod m \iff \operatorname{ord}_m(a) \mid k \); in particular \( \operatorname{ord}_p(a) \mid (p - 1) \)"),
            ("Fermat's 4k + 3 Prime Lemma", r"If prime \( q \equiv 3 \pmod 4 \) divides \( x^2 + y^2 \), then \( q \mid x \) and \( q \mid y \)"),
            ("Vieta Jumping Descent", r"In \( a^2 - k ab + b^2 = c \) with \( a \ge b \), replace \( a \mapsto a' = kb - a = \frac{b^2 - c}{a} \) to descend to a base case"),
        ],
        [
            ("توطئة رفع الأس (LTE)", r"لعدد أولي فردي \( p \mid x - y \) و\( p \nmid xy \): \( v_p(x^n - y^n) = v_p(x - y) + v_p(n) \)"),
            ("قانون الرتبة الضربية", r"\( a^k \equiv 1 \pmod m \iff \operatorname{ord}_m(a) \mid k \)؛ وبخاصة \( \operatorname{ord}_p(a) \mid (p - 1) \)"),
            ("توطئة فيرما للأولي 4k + 3", r"إذا قسم أولي \( q \equiv 3 \pmod 4 \) المقدار \( x^2 + y^2 \) فإن \( q \mid x \) و\( q \mid y \) معاً"),
            ("النزول بقفز فييت", r"في \( a^2 - k ab + b^2 = c \) استبدل الجذر الأكبر \( a \) بـ \( a' = kb - a = \frac{b^2 - c}{a} \)"),
        ],
    ),
    "OLYM-L3-02": _cs(
        [
            ("Eisenstein & Cyclotomics", r"\( p \mid a_0..a_{n-1},\; p \nmid a_n,\; p^2 \nmid a_0 \implies \) irreducible over \( \mathbb{Q} \); \( \deg \Phi_n = \varphi(n) \)"),
            ("Roots-of-Unity Filter", r"For primitive \( \zeta_m \): \( \sum_{k \equiv r \pmod m} c_k = \frac{1}{m} \sum_{j=0}^{m - 1} \zeta_m^{-jr} P(\zeta_m^j) \)"),
            ("Chebyshev Polynomials", r"\( T_0 = 1,\; T_1 = x,\; T_{n + 1}(x) = 2x T_n(x) - T_{n - 1}(x) \), mapping \( [-1, 1] \to [-1, 1] \)"),
            ("Radical Conjugate Pairing", r"Pair \( (a + b\sqrt{d})^n + (a - b\sqrt{d})^n \in \mathbb{Z} \) and bound \( |a - b\sqrt{d}| < 1 \) to trap floors!"),
        ],
        [
            ("معيار أيزنشتاين وكثيرات الحدود الدورية", r"\( p \mid a_0..a_{n-1},\; p \nmid a_n,\; p^2 \nmid a_0 \implies \) غير قابلة للتحليل في \( \mathbb{Q} \)؛ و\( \deg \Phi_n = \varphi(n) \)"),
            ("مرشّح جذور الوحدة", r"للجذر البدائي \( \zeta_m \): \( \sum_{k \equiv r \pmod m} c_k = \frac{1}{m} \sum_{j=0}^{m - 1} \zeta_m^{-jr} P(\zeta_m^j) \)"),
            ("كثيرات حدود تشيبيشيف", r"\( T_0 = 1,\; T_1 = x,\; T_{n + 1}(x) = 2x T_n(x) - T_{n - 1}(x) \)"),
            ("إقران الجذور المترافقة", r"\( (a + b\sqrt{d})^n + (a - b\sqrt{d})^n \in \mathbb{Z} \) مع حصر المرافق الأصغر \( |a - b\sqrt{d}| < 1 \)"),
        ],
    ),
    "OLYM-L3-03": _cs(
        [
            ("Hölder's 3-Bracket Inequality", r"For \( a_i, b_i, c_i > 0 \): \( \left(\sum a_i\right)\!\left(\sum b_i\right)\!\left(\sum c_i\right) \ge \left(\sum \sqrt[3]{a_i b_i c_i}\right)^3 \)"),
            ("Degree-1 Schur's Inequality", r"For \( a, b, c \ge 0 \): \( a^3 + b^3 + c^3 + 3abc \ge ab(a + b) + bc(b + c) + ca(c + a) \)"),
            ("Tangent-Line Trick", r"Prove \( f(x) \ge f(x_0) + m(x - x_0) \) via \( (x - x_0)^2 Q(x) \ge 0 \), then sum over \( x_i \) with fixed \( \sum x_i = n x_0 \)"),
            ("Aczél's Reverse Cauchy", r"If \( A^2 \ge \sum_{i=1}^{n} a_i^2 \) and \( B^2 \ge \sum_{i=1}^{n} b_i^2 \), then \( (AB - \sum a_i b_i)^2 \ge (A^2 - \sum a_i^2)(B^2 - \sum b_i^2) \)"),
        ],
        [
            ("متباينة هولدر لثلاثة أقواس", r"لكل حدود موجبة: \( \left(\sum a_i\right)\!\left(\sum b_i\right)\!\left(\sum c_i\right) \ge \left(\sum \sqrt[3]{a_i b_i c_i}\right)^3 \)"),
            ("متباينة شور من الدرجة الأولى", r"لكل \( a, b, c \ge 0 \): \( a^3 + b^3 + c^3 + 3abc \ge \sum_{\text{sym}} a^2 b \)"),
            ("طريقة خط المماس الداعم", r"أثبت \( f(x) \ge f(x_0) + m(x - x_0) \) بالتحليل لـ \( (x - x_0)^2 Q(x) \ge 0 \) ثم اجمع"),
            ("متباينة أكزيل العكسية", r"إذا كان \( A^2 \ge \sum a_i^2 \) و\( B^2 \ge \sum b_i^2 \) فإن \( AB - \sum a_i b_i \ge \sqrt{(A^2 - \sum a_i^2)(B^2 - \sum b_i^2)} \)"),
        ],
    ),
    "OLYM-L3-04": _cs(
        [
            ("Incenter–Excenter Trident", r"Arc midpoint \( M \) of \( BC \) not containing \( A \) satisfies \( MB = MC = MI = MI_A \) (and \( IM = M I_A \))"),
            ("Harmonic Cross-Ratio", r"\( (A, B; C, D) = -1 \iff \frac{AC}{CB} = \frac{AD}{BD} \iff MB^2 = MC \cdot MD \) where \( M \) is midpoint of \( AB \)"),
            ("Circular Inversion Scaling", r"Under inversion in \( (O, k^2) \): \( OP \cdot OP^* = k^2 \) and \( A^*B^* = AB \cdot \frac{k^2}{OA \cdot OB} \)"),
            ("Centroid & Orthocenter Vectors", r"With origin at circumcenter \( O \): \( \vec{OG} = \frac{1}{3}(\vec{OA} + \vec{OB} + \vec{OC}) \) and \( \vec{OH} = \vec{OA} + \vec{OB} + \vec{OC} \)"),
        ],
        [
            ("توطئة الرمح لمركزي الداخلة والخارجة", r"منتصف القوس \( M \) المقابل لـ \( A \) يحقق \( MB = MC = MI = MI_A \)"),
            ("الحزمة التوافقية الأربع", r"\( (A, B; C, D) = -1 \iff \frac{AC}{CB} = \frac{AD}{BD} \iff MB^2 = MC \cdot MD \) حيث \( M \) منتصف \( AB \)"),
            ("تحويل الانعكاس الدائري", r"تحت الانعكاس في \( (O, k^2) \): \( OP \cdot OP^* = k^2 \) وطول الصورة \( A^*B^* = AB \cdot \frac{k^2}{OA \cdot OB} \)"),
            ("علاقة متجهات المركز القائم والثقل", r"بأخذ مركز الخارجة \( O \) مبدأً: \( \vec{OH} = \vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG} \)"),
        ],
    ),
    "OLYM-L3-05": _cs(
        [
            ("Desargues, Pascal & Brianchon", r"Perspective from a point \(\iff\) perspective from a line; cyclic 6-gon opposite-side meets are collinear; tangential 6-gon diagonals concur"),
            ("Orthocentric & Disphenoid 3D", r"Tetrahedron altitudes concur iff \( AB^2 + CD^2 = AC^2 + BD^2 = AD^2 + BC^2 \); isosceles tetrahedron volume \( V = \frac{1}{6\sqrt{2}}\sqrt{(a^2+b^2-c^2)(b^2+c^2-a^2)(c^2+a^2-b^2)} \)"),
            ("Helly's Convexity Theorem", r"In \( \mathbb{R}^d \), if every \( d + 1 \) of a finite family of convex sets intersect, then ALL of them share a common point"),
            ("Fagnano's Orthic Triangle", r"Among all inscribed triangles in acute \( \triangle ABC \), the orthic triangle minimizes perimeter: \( P_{\min} = \frac{4[ABC]}{R} \)"),
        ],
        [
            ("ديزارغ وباسكال وبريانشون", r"تقاطع الأضلاع المتقابلة لسداسي دائري يقع على استقامة؛ وأقطار السداسي المماسي تتلاقى"),
            ("رباعي الوجوه متعامد الارتفاعات ومتساوي الأوجه", r"تتلاقى الارتفاعات \(\iff AB^2 + CD^2 = AC^2 + BD^2 = AD^2 + BC^2\)"),
            ("مبرهنة هيلي للمجموعات المحدبة", r"في \( \mathbb{R}^d \)، تقاطع كل \( d + 1 \) مجموعة محدبة يضمن وجود نقطة مشتركة للجميع"),
            ("مثلث فانيانو الأصغري المحيط", r"المثلث القائم القدمي يصغّر المحيط داخل المثلث الحاد الزوايا وقيمته \( P_{\min} = \frac{4[ABC]}{R} \)"),
        ],
    ),
    "OLYM-L3-06": _cs(
        [
            ("Mantel & Turán Bounds", r"Triangle-free on \( n \) vertices: \( |E| \le \lfloor n^2 / 4 \rfloor \); \( K_{r + 1} \)-free: maximized by balanced \( r \)-partite Turán graph \( T(n, r) \)"),
            ("Double-Counting Cherries", r"In bipartite incidence table \( (R, C) \): \( \sum_{c \in C} \binom{d(c)}{2} \le \binom{|R|}{2} \) if no \( K_{2, 2} \) rectangle exists"),
            ("Burnside's Orbit-Counting Lemma", r"Number of distinct orbits under group \( G \): \( |X / G| = \frac{1}{|G|} \sum_{g \in G} |\operatorname{Fix}(g)| \)"),
            ("Probabilistic Method Bound", r"If \( E[X] = \mu \), some outcome has \( X \ge \lceil \mu \rceil \) and some outcome has \( X \le \lfloor \mu \rfloor \)"),
        ],
        [
            ("حدّا مانتل وتوران", r"بيان بلا مثلثات على \( n \) رؤوس: \( |E| \le \lfloor n^2 / 4 \rfloor \)؛ وبلا \( K_{r+1} \) يحققه بيان توران المتوازن"),
            ("العدّ المزدوج للأزواج", r"في جدول الوقوع الثنائي بلا مستطيل \( K_{2,2} \): \( \sum_{c \in C} \binom{d(c)}{2} \le \binom{|R|}{2} \)"),
            ("توطئة بيرنسايد لعدّ المدارات", r"عدد الأنماط المتميزة تحت زمرة التماثل \( G \): \( |X / G| = \frac{1}{|G|} \sum_{g \in G} |\operatorname{Fix}(g)| \)"),
            ("الطريقة الاحتمالية للتوقع", r"إذا كان التوقع \( E[X] = \mu \)، فلا بد من وجود حالة تحقق \( X \ge \lceil \mu \rceil \) وأخرى تحقق \( X \le \lfloor \mu \rfloor \)"),
        ],
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # Nafes National Benchmark (Grades 3, 6, 9): NAFS-L1-01 .. NAFS-L3-06 (18)
    # ══════════════════════════════════════════════════════════════════════════
    "NAFS-L1-01": _cs(
        [
            ("4-Digit Expanded Form", r"\( \overline{abcd} = 1000a + 100b + 10c + d \) (e.g., \( 4,307 = 4000 + 300 + 7 \))"),
            ("Comparing Multi-Digit Numbers", r"Compare digit count first; if equal, compare leftmost place (thousands \(\to\) hundreds \(\to\) tens \(\to\) ones)"),
            ("Halfway Rounding Rule", r"Look one digit right of target place: \( 0\text{–}4 \implies \) keep down; \( 5\text{–}9 \implies \) round up \( +1 \)"),
            ("Regrouping & Zero Borrowing", r"10 ones \(= 1\) ten, 10 tens \(= 1\) hundred; check subtraction via \( \text{Difference} + \text{Subtrahend} = \text{Minuend} \)"),
        ],
        [
            ("الصيغة التحليلية لأربعة أرقام", r"\( \overline{abcd} = 1000a + 100b + 10c + d \) (مثال: \( 4307 = 4000 + 300 + 7 \))"),
            ("مقارنة الأعداد من اليسار", r"قارن عدد المنازل أولاً؛ وعند التساوي قارن من الألوف فالمئات فالعشرات فالآحاد"),
            ("قاعدة التقريب عند المنتصف", r"انظر للرقم عن يمين المنزلة: \( 0\text{–}4 \) يبقى كما هو، و\( 5\text{–}9 \) نضيف \( +1 \)"),
            ("إعادة التجميع والتحقق من الطرح", r"10 آحاد \(= 1\) عشرة، 10 عشرات \(= 1\) مئة؛ تحقق بـ \(\text{الناتج} + \text{المطروح} = \text{المطروح منه}\)"),
        ],
    ),
    "NAFS-L1-02": _cs(
        [
            ("Array Multiplication", r"\( r \) rows of \( c \) items \(= r \times c \) items, and \( r \times c = c \times r \)"),
            ("Inverse Fact Family", r"If \( a \times b = P \), then \( P \div a = b \) and \( P \div b = a \)"),
            ("Comparing Unit Fractions", r"Same whole: smaller denominator means LARGER slice (\( \frac{1}{2} > \frac{1}{3} > \frac{1}{4} > \frac{1}{8} \))"),
            ("Adding Like Fractions", r"\( \frac{a}{d} + \frac{b}{d} = \frac{a + b}{d} \) — add numerators only and keep denominator \( d \)!"),
        ],
        [
            ("الضرب بالصفوف والأعمدة", r"\( r \) صفوف في كل منها \( c \) عناصر \(= r \times c \)، والضرب إبدالي \( r \times c = c \times r \)"),
            ("عائلة الحقائق المترابطة", r"إذا كان \( a \times b = P \) فإن \( P \div a = b \) و\( P \div b = a \)"),
            ("مقارنة كسور الوحدة", r"لنفس الكل: المقام الأصغر يعطي جزءاً أكبر (\( \frac{1}{2} > \frac{1}{3} > \frac{1}{4} > \frac{1}{8} \))"),
            ("جمع الكسور المتشابهة", r"\( \frac{a}{d} + \frac{b}{d} = \frac{a + b}{d} \) — اجمع البسطين فقط وأبقِ المقام \( d \) ثابتاً!"),
        ],
    ),
    "NAFS-L1-03": _cs(
        [
            ("Constant-Jump Number Pattern", r"Find step \( d = a_2 - a_1 \); next term equals \( a_{\text{last}} + d \)"),
            ("Repeating Cycle Shape", r"For a core block of length \( L \), the \( N \)-th shape matches position \( ((N - 1) \bmod L) + 1 \)"),
            ("Input–Output Function Table", r"Test the candidate rule (\( +k, -k, \times k, \div k \)) on ALL given rows before computing `?`"),
            ("Balanced Number Sentence", r"Both sides of `=` must evaluate to the exact same total: \( L = R \)"),
        ],
        [
            ("النمط العددي ثابت القفزة", r"احسب مقدار القفزة \( d = a_2 - a_1 \)؛ الحد التالي يساوي \( a_{\text{الأخير}} + d \)"),
            ("الأنماط البصرية المتكررة", r"حدّد أصغر وحدة متكررة في النمط وتتبّع ترتيب الشكل المطلوب داخلها"),
            ("جدول المدخلات والمخرجات", r"جرّب القاعدة المقترحة على جميع الصفوف المعطاة قبل حساب القيمة المجهولة"),
            ("توازن الجملة العددية", r"يجب أن يتساوى ناتج الطرف الأيمن والطرف الأيسر لعلامة المساواة `=` تماماً"),
        ],
    ),
    "NAFS-L1-04": _cs(
        [
            ("Reading Analog Clock Hands", r"Short hand \( = \) hour; long hand at number \( k \) means \( 5 \times k \) minutes (\( 1\text{ hr} = 60\text{ min} \))"),
            ("Counting Elapsed Minutes", r"Bridge to the next whole hour (\( 60 - m_{\text{start}} \)), then add remaining minutes"),
            ("Saudi Riyals & Change", r"\(\text{Change} = \text{Amount Paid} - \text{Total Cost}\) (in SAR)"),
            ("Core Metric Benchmarks", r"\( 1\text{ m} = 100\text{ cm},\; 1\text{ km} = 1000\text{ m},\; 1\text{ kg} = 1000\text{ g},\; 1\text{ L} = 1000\text{ mL} \)"),
        ],
        [
            ("قراءة عقارب الساعة", r"العقرب القصير للساعات؛ والطويل عند الرقم \( k \) يعني \( 5 \times k \) دقيقة (\( 1\text{ ساعة} = 60\text{ دقيقة} \))"),
            ("حساب الزمن المنقضي", r"أكمل الدقائق إلى الساعة التالية (\( 60 - m_{\text{البداية}} \)) ثم أضف الدقائق المتبقية"),
            ("النقود والباقي بالريال", r"\(\text{الباقي} = \text{المبلغ المدفوع} - \text{مجموع المشتريات}\) بالريال السعودي"),
            ("الوحدات المترية الأساسية", r"\( 1\text{ م} = 100\text{ سم}،\; 1\text{ كم} = 1000\text{ م}،\; 1\text{ كجم} = 1000\text{ جم}،\; 1\text{ لتر} = 1000\text{ مل} \)"),
        ],
    ),
    "NAFS-L1-05": _cs(
        [
            ("Perimeter vs Area", r"Perimeter \( P = \) sum of outer rim lengths (\( 2L + 2W \)); Area \( A = \) unit squares inside (\( L \times W \))"),
            ("Cube & Prism 3D Counts", r"Cube / Rectangular prism has \( 6 \) faces, \( 12 \) edges, and \( 8 \) vertices"),
            ("Square Pyramid 3D Counts", r"Square pyramid has \( 5 \) faces (\( 1 \) square \( + 4 \) triangles), \( 8 \) edges, and \( 5 \) vertices"),
            ("Line Symmetry & Congruence", r"Regular \( n \)-gon has \( n \) symmetry lines; congruent figures satisfy \( A_1 = A_2 \) and \( P_1 = P_2 \)"),
        ],
        [
            ("المحيط مقابل المساحة", r"المحيط \( P = \) طول الإطار الخارجي (\( 2L + 2W \))؛ المساحة \( A = \) عدد الوحدات المربعة بالداخل (\( L \times W \))"),
            ("خصائص المكعب ومتوازي المستطيلات", r"للمكعب ومتوازي المستطيلات \( 6 \) أوجه و\( 12 \) حرفاً و\( 8 \) رؤوس"),
            ("خصائص الهرم الرباعي", r"للهرم الرباعي \( 5 \) أوجه (مربع \( + 4 \) مثلثات) و\( 8 \) أحرف و\( 5 \) رؤوس"),
            ("محور التماثل والتطابق", r"محور التماثل يقسم الشكل نصفين متطابقين بالطيّ؛ والأشكال المتطابقة لها نفس الشكل والقياس"),
        ],
    ),
    "NAFS-L1-06": _cs(
        [
            ("Pictograph Symbol Key", r"Always check the key first! Half-symbol equals \( \frac{1}{2} \times (\text{symbol value}) \)"),
            ("Tally Bundles of Five", r"Each crossed tally group \(\not\||||\) equals \( 5 \); total \(= 5 \times (\text{bundles}) + \text{extra strokes}\)"),
            ("Bar Chart Sum & Difference", r"Total surveyed \( = \sum h_i \); difference between two bars \( = h_{\max} - h_{\min} \)"),
            ("Likelihood Vocabulary", r"Impossible \(= 0\), Unlikely \(< \frac{1}{2}\), Equally likely \(= \frac{1}{2}\), Likely \(> \frac{1}{2}\), Certain \(= 1\)"),
        ],
        [
            ("مفتاح التمثيل بالصور", r"اقرأ المفتاح أولاً! نصف الرمز يساوي \( \frac{1}{2} \times (\text{قيمة الرمز الكامل}) \)"),
            ("حزم إشارات العدّ الخماسية", r"كل حزمة مشطوبة تمثل \( 5 \)؛ العدد الكلي \(= 5 \times (\text{الحزم}) + \text{الخطوط المفردة}\)"),
            ("قراءة التمثيل بالأعمدة", r"المجموع الكلي \( = \sum h_i \)؛ والفرق بين عمودين \( = h_{\text{الأطول}} - h_{\text{الأقصر}} \)"),
            ("وصف الاحتمال بالكلمات", r"مستحيل \(= 0\)، أقل احتمالاً \(< \frac{1}{2}\)، متساوي الإمكانية \(= \frac{1}{2}\)، أكثر احتمالاً \(> \frac{1}{2}\)، مؤكد \(= 1\)"),
        ],
    ),
    "NAFS-L2-01": _cs(
        [
            ("Prime Factorization", r"Primes have exactly \( 2 \) divisors (\( 1 \) is NOT prime; \( 2 \) is the only even prime)"),
            ("GCD vs LCM from Primes", r"\( \gcd \): smallest prime exponents; \( \operatorname{LCM} \): largest prime exponents; \( a \cdot b = \gcd(a, b)\operatorname{LCM}(a, b) \)"),
            ("Unlike Fractions (+/-)", r"Convert to common denominator \( L = \operatorname{LCM}(b, d) \): \( \frac{a}{b} \pm \frac{c}{d} = \frac{a(L/b) \pm c(L/d)}{L} \)"),
            ("Multiplying & Dividing Mixed Numbers", r"Convert \( m\frac{r}{d} = \frac{md + r}{d} \) first; divide by multiplying by the reciprocal \( \frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} \)"),
        ],
        [
            ("التحليل إلى العوامل الأولية", r"العدد الأولي له قاسمان فقط (\( 1 \) ليس أولياً، و\( 2 \) الأولي الزوجي الوحيد)"),
            ("القاسم والمضاعف المشترك", r"ق.م.أ يأخذ أصغر الأسس المشتركة، وم.م.أ يأخذ أكبر الأسس؛ و\( a \cdot b = \gcd \times \operatorname{LCM} \)"),
            ("جمع وطرح الكسور غير المتشابهة", r"وحّد المقامات بـ \( L = \operatorname{LCM}(b, d) \) ثم اجمع أو اطرح البسوط"),
            ("ضرب وقسمة الأعداد الكسرية", r"حوّل العدد الكسري لكسر غير فعلي أولاً؛ وفي القسمة اضرب في مقلوب المقسوم عليه"),
        ],
    ),
    "NAFS-L2-02": _cs(
        [
            ("Decimal Operations", r"Add/subtract: align decimal points; divide by decimal: shift both divisor & dividend by \( 10^k \)"),
            ("Unit Rate & Proportion", r"Unit rate \( = \frac{\text{Quantity}}{\text{1 unit}} \); proportion \( \frac{a}{b} = \frac{c}{d} \iff ad = bc \)"),
            ("Fraction–Decimal–Percent", r"\( \frac{1}{4} = 0.25 = 25\%,\; \frac{1}{5} = 0.2 = 20\%,\; \frac{1}{8} = 0.125 = 12.5\%,\; \frac{3}{4} = 0.75 = 75\% \)"),
            ("Percentage Discount & Tax", r"Discount \( p\% \implies \text{Sale} = \text{Price} \times \left(1 - \frac{p}{100}\right) \)"),
        ],
        [
            ("العمليات على الكسور العشرية", r"في الجمع والطرح رتب الفواصل؛ وفي القسمة اضرب المقسوم والمقسوم عليه في \( 10^k \)"),
            ("معدل الوحدة والتناسب", r"معدل الوحدة مقامه \( 1 \)؛ وفي التناسب \( \frac{a}{b} = \frac{c}{d} \iff ad = bc \)"),
            ("التحويل بين كسر وعشري ونسبة", r"\( \frac{1}{4} = 25\%،\; \frac{1}{5} = 20\%،\; \frac{1}{8} = 12.5\%،\; \frac{3}{4} = 75\% \)"),
            ("حساب الخصم المئوي", r"خصم بنسبة \( p\% \implies \text{سعر البيع} = \text{السعر الأصلي} \times \left(1 - \frac{p}{100}\right) \)"),
        ],
    ),
    "NAFS-L2-03": _cs(
        [
            ("Order of Operations", r"1. Parentheses `()` \(\to\) 2. Exponents \( a^n \) \(\to\) 3. `×` and `÷` left-to-right \(\to\) 4. `+` and `−` left-to-right"),
            ("Algebraic Substitution", r"Replace variables in parentheses (e.g., for \( x = 4, y = 3 \): \( 2x^2 - 5y = 2(16) - 15 = 17 \))"),
            ("Linear Rule from Table", r"Constant output jump \( m \) per \( +1 \) input gives \( y = mx + b \)"),
            ("Solving Equations by Inverse", r"For \( ax + b = c \): subtract \( b \) first (\( ax = c - b \)), then divide by \( a \) (\( x = \frac{c - b}{a} \))"),
        ],
        [
            ("ترتيب العمليات الحسابية", r"1. الأقواس \(\to\) 2. الأسس \(\to\) 3. الضرب والقسمة بالترتيب \(\to\) 4. الجمع والطرح بالترتيب"),
            ("التعويض في العبارات الجبرية", r"عوّض قيمة كل متغير داخل قوسين ثم اتبع ترتيب العمليات بدقة"),
            ("استنتاج قاعدة الدالة الخطية", r"التغير الثابت \( m \) لكل زيادة \( +1 \) في المدخلة يعطي القاعدة \( y = mx + b \)"),
            ("حل المعادلات بالعمليات العكسية", r"لحل \( ax + b = c \): اطرح \( b \) من الطرفين أولاً ثم اقسم على \( a \)"),
        ],
    ),
    "NAFS-L2-04": _cs(
        [
            ("Metric Ladder Conversions", r"Larger \(\to\) smaller unit: multiply; \( 1\text{ m}^2 = 10{,}000\text{ cm}^2 \), \( 1\text{ L} = 1000\text{ cm}^3 \)"),
            ("Parallelogram & Triangle Area", r"Parallelogram: \( A = b \cdot h \); Triangle: \( A = \frac{1}{2} b \cdot h \) (always use perpendicular height \( h \)!)"),
            ("Circle Circumference & Area", r"\( C = 2\pi r = \pi d \) and \( A = \pi r^2 \) (use \( \pi \approx \frac{22}{7} \) when \( r \) is a multiple of \( 7 \))"),
            ("Rectangular Prism 3D Formulas", r"Volume \( V = \ell w h \); Total Surface Area \( SA = 2(\ell w + \ell h + wh) \)"),
        ],
        [
            ("تحويل الوحدات المترية", r"من الكبير للصغير نضرب؛ \( 1\text{ م}^2 = 10000\text{ سم}^2 \) و\( 1\text{ لتر} = 1000\text{ سم}^3 \)"),
            ("مساحة متوازي الأضلاع والمثلث", r"متوازي الأضلاع: \( A = b \cdot h \)؛ المثلث: \( A = \frac{1}{2} b \cdot h \) بالارتفاع العمودي"),
            ("محيط الدائرة ومساحتها", r"\( C = 2\pi r = \pi d \) و\( A = \pi r^2 \) (استخدم \( \pi \approx \frac{22}{7} \) لمضاعفات \( 7 \))"),
            ("حجم ومساحة سطح المنشور الرباعي", r"الحجم \( V = \ell w h \)؛ المساحة الكلية للسطح \( SA = 2(\ell w + \ell h + wh) \)"),
        ],
    ),
    "NAFS-L2-05": _cs(
        [
            ("Special Angle Pairs", r"Complementary \(= 90^\circ\); Supplementary (straight line) \(= 180^\circ\); Vertically opposite angles are equal"),
            ("Triangle & Isosceles Angles", r"Angles in a triangle sum to \( 180^\circ \); isosceles base angles with apex \( A \) equal \( \frac{180^\circ - A}{2} \)"),
            ("Quadrilateral Angle Sum", r"Interior angles of any quadrilateral sum to \( 360^\circ \)"),
            ("Axis-Aligned Coordinate Length", r"Same \( y \): horizontal length \( = |x_2 - x_1| \); same \( x \): vertical length \( = |y_2 - y_1| \)"),
        ],
        [
            ("العلاقات بين الزوايا", r"المتتامتان \(= 90^\circ\)؛ المتكاملتان (على مستقيم) \(= 180^\circ\)؛ المتقابلتان بالرأس متساويتان"),
            ("زوايا المثلث والمتطابق الضلعين", r"مجموع زوايا المثلث \( 180^\circ \)؛ وزاوية قاعدة المتطابق الضلعين \( = \frac{180^\circ - A}{2} \)"),
            ("مجموع زوايا الشكل الرباعي", r"مجموع الزوايا الداخلية لأي شكل رباعي يساوي \( 360^\circ \)"),
            ("المسافة على المستوى الإحداثي", r"أفقياً: \( |x_2 - x_1| \)؛ ورأسياً: \( |y_2 - y_1| \)"),
        ],
    ),
    "NAFS-L2-06": _cs(
        [
            ("Mean & Missing Score", r"\( \text{Mean} = \frac{\sum x_i}{n} \implies \text{Target Sum} = n \times \text{Mean} \); Range \( = x_{\max} - x_{\min} \)"),
            ("Median & Mode", r"Sort data first! Odd \( n \): middle value; Even \( n \): average of two middle values; Mode \( = \) most frequent"),
            ("Pie Chart Sector Calculation", r"\( \text{Quantity} = \frac{\theta}{360^\circ} \times N = \frac{p\%}{100\%} \times N \)"),
            ("Complementary & Product Counting", r"\( P(\text{not } E) = 1 - P(E) \); independent multi-stage outcomes \( = n_1 \times n_2 \times \cdots \)"),
        ],
        [
            ("المتوسط الحسابي والمدى", r"\( \text{المتوسط} = \frac{\sum x_i}{n} \implies \text{المجموع} = n \times \text{المتوسط} \)؛ والمدى \( = x_{\max} - x_{\min} \)"),
            ("الوسيط والمنوال", r"رتّب البيانات تصاعدياً أولاً! لعدد زوجي خذ متوسط القيمتين الوسطيين؛ والمنوال الأكثر تكراراً"),
            ("القطاعات الدائرية", r"\( \text{قيمة القطاع} = \frac{\theta}{360^\circ} \times N = \frac{p\%}{100\%} \times N \)"),
            ("الحادثة المتممة ومبدأ العد", r"\( P(\text{متممة } E) = 1 - P(E) \)؛ وعدد النواتج الممكنة \( = n_1 \times n_2 \times \cdots \)"),
        ],
    ),
    "NAFS-L3-01": _cs(
        [
            ("Bounding Irrational Roots", r"Bracket \( a^2 < N < (a + 1)^2 \implies a < \sqrt{N} < a + 1 \); compare distances \( N - a^2 \) vs \( (a + 1)^2 - N \)"),
            ("Square-Root Radical Algebra", r"\( \sqrt{k^2 m} = k\sqrt{m} \) (\( k > 0 \)); combine like radicals \( a\sqrt{m} + b\sqrt{m} = (a + b)\sqrt{m} \)"),
            ("Integer Exponent Laws", r"\( a^m \cdot a^n = a^{m+n},\; \frac{a^m}{a^n} = a^{m-n},\; (a^m)^n = a^{mn},\; a^0 = 1,\; a^{-n} = \frac{1}{a^n} \)"),
            ("Normalized Scientific Notation", r"\( c \times 10^n \) requires \( 1 \le |c| < 10 \); shifting \( c \div 10 \) increases exponent \( n \to n + 1 \)"),
        ],
        [
            ("حصر الجذور غير النسبية", r"\( a^2 < N < (a + 1)^2 \implies a < \sqrt{N} < a + 1 \)؛ وقارن قرب \( N \) من المربعين"),
            ("تبسيط وجمع الجذور التربيعية", r"\( \sqrt{k^2 m} = k\sqrt{m} \)؛ وتُجمع الجذور المتشابهة فقط \( a\sqrt{m} + b\sqrt{m} = (a + b)\sqrt{m} \)"),
            ("قوانين الأسس الصحيحة", r"\( a^m \cdot a^n = a^{m+n}،\; \frac{a^m}{a^n} = a^{m-n}،\; (a^m)^n = a^{mn}،\; a^0 = 1،\; a^{-n} = \frac{1}{a^n} \)"),
            ("الصيغة العلمية القياسية", r"\( c \times 10^n \) تشترط \( 1 \le |c| < 10 \)؛ قسمة \( c \) على \( 10 \) تزيد الأس \( +1 \)"),
        ],
    ),
    "NAFS-L3-02": _cs(
        [
            ("Successive Percent & 15% VAT", r"Discount \( d\% \) then VAT \( 15\% \): \( P_{\text{final}} = P_0 \left(1 - \frac{d}{100}\right)(1.15) \) — divide by multipliers for \( P_0 \)!"),
            ("Direct vs Inverse Variation", r"Direct: \( \frac{y_1}{x_1} = \frac{y_2}{x_2} \); Inverse (workers \(\times\) time): \( x_1 y_1 = x_2 y_2 \)"),
            ("Combined Rate Equation", r"Two pipes/workers together: \( \frac{1}{T} = \frac{1}{t_1} + \frac{1}{t_2} \) (subtract \( \frac{1}{t_{\text{drain}}} \) for an outlet)"),
            ("Weighted Mixture Balance", r"\( c_1 m_1 + c_2 m_2 = c_{\text{mix}}(m_1 + m_2) \) — track pure solute mass!"),
        ],
        [
            ("النسب المتتالية وضريبة 15%", r"خصم \( d\% \) ثم ضريبة \( 15\% \): \( P_{\text{نهائي}} = P_0 \left(1 - \frac{d}{100}\right)(1.15) \)"),
            ("التغير الطردي مقابل العكسي", r"طردي: \( \frac{y_1}{x_1} = \frac{y_2}{x_2} \)؛ عكسي (عمال \(\times\) زمن): \( x_1 y_1 = x_2 y_2 \)"),
            ("معدل الإنجاز المشترك", r"\( \frac{1}{T} = \frac{1}{t_1} + \frac{1}{t_2} \) (واطرح معدل التفريغ عند وجود مخرج)"),
            ("توازن تراكيز المخاليط", r"\( c_1 m_1 + c_2 m_2 = c_{\text{خليط}}(m_1 + m_2) \) بحفظ كمية المادة النقية"),
        ],
    ),
    "NAFS-L3-03": _cs(
        [
            ("Absolute Value & Inequalities", r"\( |ax + b| = c \;(c \ge 0) \implies ax + b = \pm c \); dividing an inequality by a negative FLIPS `<` \(\leftrightarrow\) `>`"),
            ("Slope & Parallel/Perpendicular", r"\( m = \frac{y_2 - y_1}{x_2 - x_1} \); parallel lines: \( m_1 = m_2 \); perpendicular lines: \( m_1 m_2 = -1 \)"),
            ("Special Algebraic Identities", r"\( (a \pm b)^2 = a^2 \pm 2ab + b^2 \) and \( a^2 - b^2 = (a - b)(a + b) \)"),
            ("Parabola Vertex & Quadratic Roots", r"For \( y = ax^2 + bx + c \): vertex at \( x_v = -\frac{b}{2a} \); roots \( x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \)"),
        ],
        [
            ("القيمة المطلقة والمتباينات", r"\( |ax + b| = c \implies ax + b = \pm c \)؛ والقسمة على عدد سالب تعكس اتجاه المتباينة!"),
            ("الميل والتوازي والتعامد", r"\( m = \frac{y_2 - y_1}{x_2 - x_1} \)؛ التوازي: \( m_1 = m_2 \)؛ التعامد: \( m_1 m_2 = -1 \)"),
            ("المتطابقات الجبرية الشهيرة", r"\( (a \pm b)^2 = a^2 \pm 2ab + b^2 \) وفرق المربعين \( a^2 - b^2 = (a - b)(a + b) \)"),
            ("رأس القطع المكافئ والجذور", r"للدالة \( y = ax^2 + bx + c \): إحداثي الرأس \( x_v = -\frac{b}{2a} \) والمميز \( \Delta = b^2 - 4ac \)"),
        ],
    ),
    "NAFS-L3-04": _cs(
        [
            ("Pythagoras & Classic Triples", r"\( a^2 + b^2 = c^2 \); memorize \((3,4,5),\; (5,12,13),\; (8,15,17),\; (7,24,25)\) and multiples"),
            ("Coordinate Distance & Midpoint", r"\( d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \) and \( M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right) \)"),
            ("Shaded Composite Area", r"\( A_{\text{shaded}} = A_{\text{outer}} - A_{\text{cutout}} \) (circle in side-\( 2r \) square: \( 4r^2 - \pi r^2 \))"),
            ("Cylinder, Cone & Sphere Volumes", r"Cylinder: \( \pi r^2 h \); Cone: \( \frac{1}{3}\pi r^2 h \); Sphere: \( \frac{4}{3}\pi r^3 \)"),
        ],
        [
            ("فيثاغورس والثلاثيات الشهيرة", r"\( a^2 + b^2 = c^2 \)؛ احفظ \((3,4,5),\; (5,12,13),\; (8,15,17),\; (7,24,25)\) ومضاعفاتها"),
            ("قانونا المسافة ونقطة المنتصف", r"\( d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \) والمنتصف \( M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right) \)"),
            ("مساحة المناطق المظللة المركبة", r"\( A_{\text{مظلل}} = A_{\text{خارجي}} - A_{\text{مقتطع}} \) (دائرة داخل مربع ضلعه \( 2r \): \( 4r^2 - \pi r^2 \))"),
            ("حجوم الأسطوانة والمخروط والكرة", r"الأسطوانة: \( \pi r^2 h \)؛ المخروط: \( \frac{1}{3}\pi r^2 h \)؛ الكرة: \( \frac{4}{3}\pi r^3 \)"),
        ],
    ),
    "NAFS-L3-05": _cs(
        [
            ("Parallel Lines & Exterior Angle", r"Alternate/corresponding angles equal; co-interior sum \(= 180^\circ\); triangle exterior angle \(= \alpha + \beta\)"),
            ("Convex n-gon Angle Laws", r"Interior sum \(= (n - 2)180^\circ\); exterior sum \(= 360^\circ\); regular sides from interior \( \theta \): \( n = \frac{360^\circ}{180^\circ - \theta} \)"),
            ("Similarity Scale k vs k²", r"Side/perimeter/altitude ratio \(= k \implies \) Area ratio \(= k^2\)"),
            ("Coordinate Transformations", r"Reflect \( x \)-axis: \((x, -y)\); \( y \)-axis: \((-x, y)\); \( 180^\circ \) origin: \((-x, -y)\); translate: \((x + a, y + b)\)"),
        ],
        [
            ("التوازي والزاوية الخارجية للمثلث", r"المتبادلتان والمتناظرتان متساويتان؛ والمتحالفتان مجموعهما \( 180^\circ \)؛ والخارجية \( = \alpha + \beta \)"),
            ("زوايا المضلع المحدب والمنتظم", r"الداخلية \(= (n - 2)180^\circ\)؛ الخارجية \(= 360^\circ\)؛ وللمنتظم \( n = \frac{360^\circ}{180^\circ - \theta} \)"),
            ("نسبة التشابه للمحيط والمساحة", r"نسبة الأضلاع والمحيطات \(= k \implies \) نسبة المساحات \(= k^2\)"),
            ("التحويلات الهندسية في المستوى", r"انعكاس حول \( x \): \((x, -y)\)؛ حول \( y \): \((-x, y)\)؛ دوران \( 180^\circ \): \((-x, -y)\)؛ إزاحة: \((x+a, y+b)\)"),
        ],
    ),
    "NAFS-L3-06": _cs(
        [
            ("Box Plot & IQR", r"\( \text{IQR} = Q_3 - Q_1 \) spans the middle \( 50\% \) of the data; Range \(= \text{Max} - \text{Min}\)"),
            ("Two-Way Conditional Probability", r"\( P(A \mid B) = \frac{\text{Cell}(A \cap B)}{\text{Marginal Total of } B} \) — divide by the given condition's total!"),
            ("Permutations vs Combinations", r"Ordered: \( P(n, r) = \frac{n!}{(n - r)!} \); Unordered committee: \( \binom{n}{r} = \frac{n!}{r!(n - r)!} \)"),
            ("Compound Probability (With/Without)", r"With replacement: \( \frac{a}{N} \cdot \frac{b}{N} \); Without replacement: \( \frac{a}{N} \cdot \frac{a - 1}{N - 1} \) (or \( \frac{b}{N - 1} \))"),
        ],
        [
            ("الصندوق وطرفاه والمدى الربيعي", r"\( \text{IQR} = Q_3 - Q_1 \) يضم الـ \( 50\% \) الوسطى من البيانات؛ والمدى \(= \text{الأكبر} - \text{الأصغر}\)"),
            ("الاحتمال المشروط في الجداول المزدوجة", r"\( P(A \mid B) = \frac{\text{خلية }(A \cap B)}{\text{المجموع الهامشي للشرط } B} \)"),
            ("التباديل مقابل التوافيق", r"بترتيب (مناصب): \( P(n, r) = \frac{n!}{(n - r)!} \)؛ بدون ترتيب (لجنة): \( \binom{n}{r} = \frac{n!}{r!(n - r)!} \)"),
            ("الحوادث المركبة (بإرجاع وبدونه)", r"مع الإرجاع يبقى المقام \( N \)؛ وبدون إرجاع ينقص الكل \( N - 1 \)"),
        ],
    ),
    **KANGAROO_CHEAT_SHEETS,
}


MISSING_EXAMPLE_SVGS = _build_missing_example_svgs()


def apply_lesson_enhancements(lessons: list[dict]) -> None:
    """Attach 4-card bilingual `cheat_sheet` and fill in any missing worked-example SVG diagrams."""
    for les in lessons:
        lid = les["id"]
        assert lid in CHEAT_SHEETS, f"Missing cheat_sheet definition for lesson {lid}"
        cs = CHEAT_SHEETS[lid]
        assert len(cs["en"]) == 4 and len(cs["ar"]) == 4, f"Expected 4 cheat_sheet items in {lid}"
        les["en"]["cheat_sheet"] = cs["en"]
        les["ar"]["cheat_sheet"] = cs["ar"]

        en_exs = les["en"]["examples"]
        ar_exs = les["ar"]["examples"]
        assert len(en_exs) == len(ar_exs), f"EN/AR example count mismatch in {lid}"
        for idx, (ex_en, ex_ar) in enumerate(zip(en_exs, ar_exs)):
            eid = ex_en["id"]
            if "<svg" not in (ex_en.get("diagram") or "") or "<svg" not in (ex_ar.get("diagram") or ""):
                assert eid in MISSING_EXAMPLE_SVGS, f"Missing custom SVG for {lid} example {eid}"
                svg_en, svg_ar = MISSING_EXAMPLE_SVGS[eid]
                ex_en["diagram"] = svg_en
                ex_ar["diagram"] = svg_ar
            ex_ar["diagram"] = localize_svg_to_ar(ex_ar["diagram"])
            ET.fromstring(ex_en["diagram"])
            ET.fromstring(ex_ar["diagram"])
        for c_ar in les["ar"]["concepts"]:
            if c_ar.get("diagram"):
                c_ar["diagram"] = localize_svg_to_ar(c_ar["diagram"])
