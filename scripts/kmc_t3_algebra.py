"""Track 3 (Grades 10-11) — Algebra (115 authentic KMC Senior problems)."""
from fractions import Fraction

from kmc_common import (
    explain_ar,
    explain_en,
    fmt_val,
    m,
    make_5_math_options,
    make_kmc_question,
)

LEVEL = "Track 3: Grades 10-11"
TOPIC = "Algebra"


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar):
        nonlocal idx
        qid = f"KMC-T3-ALG-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, TOPIC, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar,
            )
        )

    # ------------------------------------------------------------------
    # 1. Negative & zero exponents (KMC Senior Cat B Q1!) (10 Qs)
    # ------------------------------------------------------------------
    exp_cases = [
        # (a, b, c): evaluate ((a^-2 + c^0) / (a/b)^-2)
        (2, 3, 5, "Easy"),
        (3, 2, 7, "Easy"),
        (2, 5, 9, "Easy"),
        (3, 4, 6, "Medium"),
        (4, 3, 8, "Medium"),
        (5, 2, 4, "Medium"),
        (2, 7, 3, "Medium"),
        (3, 5, 11, "Medium"),
        (4, 5, 10, "Hard"),
        (5, 4, 12, "Hard"),
    ]
    for v_i, (a, b, c, diff) in enumerate(exp_cases):
        num = Fraction(1, a * a) + Fraction(1, 1)   # (1 + a^2) / a^2
        den = Fraction(b * b, a * a)                # (a/b)^-2 = (b/a)^2
        ans = num / den                             # (1 + a^2) / b^2
        assert ans == Fraction(1 + a * a, b * b)
        distractors = [
            Fraction(1 + a * a, a * a),
            Fraction(a * a, b * b),
            Fraction(b * b, 1 + a * a),
            Fraction(2 + a * a, b * b),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_exp_{v_i}")
        expr_tex = f"\\frac{{{a}^{{-2}} + {c}^0}}{{\\left(\\frac{{{a}}}{{{b}}}\\right)^{{-2}}}}"
        q_en = f"What is the exact value of {m(expr_tex)}?"
        q_ar = f"ما القيمة الدقيقة للمقدار {m(expr_tex)}؟"
        h_en = f"Use three basic exponent rules step by step: {c}⁰ = 1, {a}⁻² = 1/{a*a}, and ({a}/{b})⁻² = ({b}/{a})²!"
        h_ar = f"استخدم ثلاث قواعد أساسية للأسس خطوة بخطوة: {c}⁰ = 1، و{a}⁻² = 1/{a*a}، و({a}/{b})⁻² = ({b}/{a})²!"
        s_en = explain_en(
            "Recall the three rules of zero and negative exponents: \\( x^0 = 1 \\) (for \\( x \\ne 0 \\)), \\( x^{-n} = \\frac{1}{x^n} \\), and \\( \\left(\\frac{p}{q}\\right)^{-n} = \\left(\\frac{q}{p}\\right)^n \\).",
            [
                f"Simplify the numerator: {m(f'{a}^{{-2}} + {c}^0 = \\frac{{1}}{{{a*a}}} + 1 = \\frac{{{1 + a*a}}}{{{a*a}}}')}.",
                f"Simplify the denominator by flipping the fraction: {m(f'\\left(\\frac{{{a}}}{{{b}}}\\right)^{{-2}} = \\left(\\frac{{{b}}}{{{a}}}\\right)^2 = \\frac{{{b*b}}}{{{a*a}}}')}.",
                f"Divide numerator by denominator (the {m(a*a)} denominators cancel!): {m(f'\\frac{{{1+a*a}}}{{{a*a}}} \\div \\frac{{{b*b}}}{{{a*a}}} = {fmt_val(ans)}')}.",
            ],
            f"Common trap avoided: \\( {c}^0 = 1 \\), NOT \\( 0 \\)!",
        )
        s_ar = explain_ar(
            "نتذكر قواعد الأس الصفري والأس السالب: \\( x^0 = 1 \\)، و\\( x^{-n} = \\frac{1}{x^n} \\)، و\\( \\left(\\frac{p}{q}\\right)^{-n} = \\left(\\frac{q}{p}\\right)^n \\).",
            [
                f"نبسّط البسط: {m(f'{a}^{{-2}} + {c}^0 = \\frac{{1}}{{{a*a}}} + 1 = \\frac{{{1 + a*a}}}{{{a*a}}}')}.",
                f"نبسّط المقام بقلب الكسر وتغيير إشارة الأس: {m(f'\\left(\\frac{{{a}}}{{{b}}}\\right)^{{-2}} = \\left(\\frac{{{b}}}{{{a}}}\\right)^2 = \\frac{{{b*b}}}{{{a*a}}}')}.",
                f"نقسم البسط على المقام (يُختصر المقام {m(a*a)} في كليهما!): {m(f'\\frac{{{1+a*a}}}{{{b*b}}} = {fmt_val(ans)}')}.",
            ],
            f"تجنبنا الخطأ الشائع: \\( {c}^0 = 1 \\) وليس \\( 0 \\)!",
        )
        push(diff, "kmc_g1011_neg_zero_exponents", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 2. Shifted function evaluation & composition (KMC Senior Cat B Q3!) (10 Qs)
    # ------------------------------------------------------------------
    fn_cases = [
        # F(x) = a*x^2 + b, G(x) = c*x + d, H(x) = F(x + s) + G(x - s), evaluate H(x0)
        (1, 2, 3, -1, 2, 1, "Easy"),
        (2, -1, 4, 3, 1, 2, "Easy"),
        (1, 5, -2, 7, 3, 1, "Easy"),
        (2, 3, 5, -4, 2, 2, "Medium"),
        (3, -2, -4, 6, 1, 3, "Medium"),
        (1, -3, 6, 2, 4, -1, "Medium"),
        (2, 1, -3, 8, 3, -1, "Medium"),
        (3, 4, 2, -5, 2, -3, "Medium"),
        (2, -5, 7, -3, 4, 2, "Hard"),
        (3, -4, -5, 9, 3, 2, "Hard"),
    ]
    for v_i, (a, b, c, d, s, x0, diff) in enumerate(fn_cases):
        in1 = x0 + s
        in2 = x0 - s
        f_val = a * (in1 ** 2) + b
        g_val = c * in2 + d
        ans = f_val + g_val
        # Distractor: forgetting shift or shifting wrong way
        trap_noshift = (a * x0 ** 2 + b) + (c * x0 + d)
        trap_swap = (a * in2 ** 2 + b) + (c * in1 + d)
        distractors = [trap_noshift, trap_swap, ans + 4, ans - 4]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_fn_{v_i}")
        f_tex = (f"{a}x^2" if a > 1 else "x^2") + (f" + {b}" if b >= 0 else f" - {abs(b)}")
        g_tex = (f"{c}x" if abs(c) != 1 else ("x" if c == 1 else "-x")) + (f" + {d}" if d >= 0 else f" - {abs(d)}")
        q_en = (
            f"Let {m(f'F(x) = {f_tex}')} and {m(f'G(x) = {g_tex}')}. "
            f"If a new function {m('H')} is defined by {m(f'H(x) = F(x + {s}) + G(x - {s})')}, what is the value of {m(f'H({x0})')}?"
        )
        q_ar = (
            f"لتكن {m(f'F(x) = {f_tex}')} و{m(f'G(x) = {g_tex}')}. "
            f"إذا عُرِّفت الدالة {m('H')} بالعلاقة {m(f'H(x) = F(x + {s}) + G(x - {s})')}، فما قيمة {m(f'H({x0})')}؟"
        )
        h_en = f"Don't expand F(x+{s}) algebraically! Just plug x = {x0} directly into the parentheses first: x+{s} = {in1} and x−{s} = {in2}!"
        h_ar = f"لا تفكّ الأقواس جبرياً! عوّض مباشرة بـ x = {x0} داخل القوسين أولاً: x+{s} = {in1} وx−{s} = {in2}!"
        s_en = explain_en(
            "Instead of expanding formulas in \\( x \\), evaluate the **shifted inputs** numerically first — it is faster and avoids sign errors!",
            [
                f"Substitute {m(f'x = {x0}')} into {m('H(x)')}: {m(f'H({x0}) = F({x0} + {s}) + G({x0} - {s}) = F({in1}) + G({in2})')}.",
                f"Compute each value: {m(f'F({in1}) = {a}({in1})^2 + ({b}) = {f_val}')} and {m(f'G({in2}) = {c}({in2}) + ({d}) = {g_val}')}.",
                f"Add them together: {m(f'{f_val} + ({g_val}) = {ans}')}.",
            ],
            f"Watch the signs when squaring: {m(f'({in1})^2 = {in1**2} \\ge 0')} always!",
        )
        s_ar = explain_ar(
            "بدلاً من فكّ الأقواس جبرياً بدلالة \\( x \\)، نحسب **المدخلات العددية** داخل الأقواس أولاً؛ فهذا أسرع ويمنع أخطاء الإشارات!",
            [
                f"نعوض {m(f'x = {x0}')} في تعريف {m('H(x)')}: {m(f'H({x0}) = F({x0} + {s}) + G({x0} - {s}) = F({in1}) + G({in2})')}.",
                f"نحسب كل دالة على حدة: {m(f'F({in1}) = {f_val}')} و{m(f'G({in2}) = {g_val}')}.",
                f"نجمع القيمتين: {m(f'{f_val} + ({g_val}) = {ans}')}.",
            ],
            f"انتبه للإشارات عند التربيع: {m(f'({in1})^2 = {in1**2}')} موجب دائماً!",
        )
        push(diff, "kmc_g1011_function_shift_comp", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 3. Symmetric polynomial systems (KMC Senior Cat B Q4 style!) (10 Qs)
    # ------------------------------------------------------------------
    sys_cases = [
        # Mode 'sq': x^2 + xy = A, xy + y^2 = B (x,y > 0) -> find x + y = sqrt(A+B)
        ("sq", 5, 3, "Easy"),      # A=40, B=24 -> A+B=64 -> x+y=8
        ("sq", 6, 4, "Easy"),      # A=60, B=40 -> 100 -> 10
        ("sq", 7, 5, "Medium"),    # A=84, B=60 -> 144 -> 12
        ("sq", 9, 6, "Medium"),    # A=135, B=90 -> 225 -> 15
        ("sq", 11, 7, "Medium"),   # A=198, B=126 -> 324 -> 18
        # Mode 'cube': x + y = S, x^3 + y^3 = C -> find xy via (S^3 - C)/(3S)
        ("cube", 4, 2, "Medium"),  # S=6, C=72 -> xy=8
        ("cube", 5, 3, "Medium"),  # S=8, C=152 -> xy=15
        ("cube", 6, 2, "Medium"),  # S=8, C=224 -> xy=12
        ("cube", 7, 3, "Hard"),    # S=10, C=370 -> xy=21
        ("cube", 8, 4, "Hard"),    # S=12, C=576 -> xy=32
    ]
    for v_i, (mode, x_v, y_v, diff) in enumerate(sys_cases):
        if mode == "sq":
            A = x_v * x_v + x_v * y_v
            B = x_v * y_v + y_v * y_v
            ans = x_v + y_v
            assert A + B == ans * ans
            distractors = [abs(x_v - y_v), ans + 2, ans - 2, (A - B) // ans + ans]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_sys_{v_i}")
            q_en = f"Positive real numbers {m('x')} and {m('y')} satisfy {m(f'x^2 + xy = {A}')} and {m(f'xy + y^2 = {B}')}. What is the value of {m('x + y')}?"
            q_ar = f"عددان حقيقيان موجبان {m('x')} و{m('y')} يحققان {m(f'x^2 + xy = {A}')} و{m(f'xy + y^2 = {B}')}. ما قيمة {m('x + y')}؟"
            h_en = "Add the two equations together and look at the left-hand side: x² + 2xy + y² is a famous perfect square!"
            h_ar = "اجمع المعادلتين معاً وتأمل الطرف الأيسر: المقدار x² + 2xy + y² مربع كامل مشهور!"
            s_en = explain_en(
                "Adding both equations forms the perfect square identity \\( (x + y)^2 = x^2 + 2xy + y^2 \\)!",
                [
                    f"Add the two equations: {m(f'(x^2 + xy) + (xy + y^2) = {A} + {B} = {A+B}')}.",
                    f"Rewrite the left side as a square: {m(f'x^2 + 2xy + y^2 = (x + y)^2 = {A+B}')}.",
                    f"Since {m('x, y > 0')}, we have {m('x + y > 0')}, so {m(f'x + y = \\sqrt{{{A+B}}} = {ans}')}.",
                ],
                f"Bonus check: {m(f'x(x+y)={A} \\implies x={x_v}')} and {m(f'y(x+y)={B} \\implies y={y_v}')}, which indeed satisfy both equations!",
            )
            s_ar = explain_ar(
                "جمع المعادلتين يكوّن مباشرة متطابقة المربع الكامل \\( (x + y)^2 = x^2 + 2xy + y^2 \\)!",
                [
                    f"نجمع المعادلتين طرفاً لطرف: {m(f'(x^2 + xy) + (xy + y^2) = {A} + {B} = {A+B}')}.",
                    f"نكتب الطرف الأيسر كمربع كامل: {m(f'x^2 + 2xy + y^2 = (x + y)^2 = {A+B}')}.",
                    f"بما أن {m('x, y > 0')} فإن {m('x + y > 0')}، ومنه {m(f'x + y = \\sqrt{{{A+B}}} = {ans}')}.",
                ],
                f"تحقق إضافي: {m(f'x={x_v}')} و{m(f'y={y_v}')} يحققان كلتا المعادلتين ومجموعهما {m(ans)}.",
            )
        else:
            S = x_v + y_v
            C = x_v ** 3 + y_v ** 3
            ans = x_v * y_v
            assert S ** 3 - 3 * ans * S == C
            distractors = [ans + S, max(1, ans - 3), (S * S) // 2, ans + 4]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_sys_{v_i}")
            q_en = f"Real numbers {m('x')} and {m('y')} satisfy {m(f'x + y = {S}')} and {m(f'x^3 + y^3 = {C}')}. What is the value of the product {m('xy')}?"
            q_ar = f"عددان حقيقيان {m('x')} و{m('y')} يحققان {m(f'x + y = {S}')} و{m(f'x^3 + y^3 = {C}')}. ما قيمة حاصل الضرب {m('xy')}؟"
            h_en = "Cube (x + y): remember (x + y)³ = x³ + y³ + 3xy(x + y)!"
            h_ar = "كعّب المقدار (x + y): تذكر أن (x + y)³ = x³ + y³ + 3xy(x + y)!"
            s_en = explain_en(
                "Use the cube-of-a-sum identity \\( (x + y)^3 = x^3 + y^3 + 3xy(x + y) \\) so you never have to solve for \\( x \\) and \\( y \\) individually!",
                [
                    f"Cube {m(f'x + y = {S}')}: {m(f'(x + y)^3 = {S}^3 = {S**3}')}.",
                    f"Substitute {m(f'x^3 + y^3 = {C}')} and {m(f'x + y = {S}')} into {m('(x+y)^3 = (x^3+y^3) + 3xy(x+y)')}: {m(f'{S**3} = {C} + 3({S})xy')}.",
                    f"Solve for {m('xy')}: {m(f'{3*S}xy = {S**3 - C} \\implies xy = \\frac{{{S**3 - C}}}{{{3*S}}} = {ans}')}.",
                ],
                f"Check with {m(f'x = {x_v}, y = {y_v}')}: {m(f'{x_v} + {y_v} = {S}')}, {m(f'{x_v}^3 + {y_v}^3 = {C}')}, and {m(f'xy = {ans}')}!",
            )
            s_ar = explain_ar(
                "نستخدم متطابقة مكعب مجموع حدين \\( (x + y)^3 = x^3 + y^3 + 3xy(x + y) \\) دون الحاجة لإيجاد \\( x \\) و\\( y \\) منفردين!",
                [
                    f"نكعّب {m(f'x + y = {S}')}: {m(f'(x + y)^3 = {S}^3 = {S**3}')}.",
                    f"نعوض {m(f'x^3 + y^3 = {C}')} و{m(f'x + y = {S}')}: {m(f'{S**3} = {C} + {3*S}xy')}.",
                    f"نحل لإيجاد {m('xy')}: {m(f'{3*S}xy = {S**3 - C} \\implies xy = {ans}')}.",
                ],
                f"تحقق: العددان {m(x_v)} و{m(y_v)} مجموعهما {m(S)} ومجموع مكعبيهما {m(C)} وحاصل ضربهما {m(ans)}!",
            )
        push(diff, "kmc_g1011_poly_system_factor", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 4. Radical equations sqrt(x + a) + sqrt(x + b) = c (10 Qs)
    # ------------------------------------------------------------------
    # Parameterize from u > v >= 1: x + a = u^2, x + b = v^2, c = u + v!
    rad_cases = [
        (3, 1, 5, "Easy"),     # x=5: a=4 (5+4=9, u=3), b=-4 (5-4=1, v=1), c=4
        (4, 2, 7, "Easy"),     # x=7: a=9, b=-3, c=6
        (5, 2, 10, "Easy"),    # x=10: a=15, b=-6, c=7
        (5, 3, 12, "Medium"),  # x=12: a=13, b=-3, c=8
        (6, 2, 15, "Medium"),  # x=15: a=21, b=-11, c=8
        (6, 4, 20, "Medium"),  # x=20: a=16, b=-4, c=10
        (7, 3, 18, "Medium"),  # x=18: a=31, b=-9, c=10
        (7, 5, 24, "Medium"),  # x=24: a=25, b=1, c=12
        (8, 4, 30, "Hard"),    # x=30: a=34, b=-14, c=12
        (9, 5, 40, "Hard"),    # x=40: a=41, b=-15, c=14
    ]
    for v_i, (u, v, x_ans, diff) in enumerate(rad_cases):
        a = u * u - x_ans
        b = v * v - x_ans
        c = u + v
        diff_ab = a - b
        assert diff_ab == u * u - v * v and diff_ab % c == 0
        u_minus_v = diff_ab // c
        assert u_minus_v == u - v
        t1 = f"x + {a}" if a >= 0 else f"x - {abs(a)}"
        t2 = f"x + {b}" if b >= 0 else f"x - {abs(b)}"
        distractors = [x_ans + 4, max(1, x_ans - 3), u * u, x_ans + 6]
        opts_en, opts_ar, cidx, cans = make_5_math_options(x_ans, distractors, f"t3a_rad_{v_i}")
        q_en = f"What is the real value of {m('x')} that satisfies {m(f'\\sqrt{{{t1}}} + \\sqrt{{{t2}}} = {c}')}?"
        q_ar = f"ما قيمة العدد الحقيقي {m('x')} الذي يحقق المعادلة {m(f'\\sqrt{{{t1}}} + \\sqrt{{{t2}}} = {c}')}؟"
        h_en = f"Clever shortcut: set A = √({t1}) and B = √({t2}). Then A + B = {c}, and A² − B² = ({t1}) − ({t2}) = {diff_ab}!"
        h_ar = f"اختصار ذكي: ضع A = √({t1}) وB = √({t2})؛ فيكون A + B = {c}، والفرق بين مربعيهما A² − B² = {diff_ab}!"
        s_en = explain_en(
            "Instead of messy repeated squaring, name the two roots \\( A = \\sqrt{" + t1 + "} \\) and \\( B = \\sqrt{" + t2 + "} \\) and use \\( A^2 - B^2 = (A - B)(A + B) \\)!",
            [
                f"Notice that {m(f'A^2 - B^2 = ({t1}) - ({t2}) = {diff_ab}')} (the {m('x')} cancels out!).",
                f"Since {m(f'A + B = {c}')} and {m('(A - B)(A + B) = A^2 - B^2')}, divide by {m(c)}: {m(f'A - B = \\frac{{{diff_ab}}}{{{c}}} = {u_minus_v}')}.",
                f"Add {m(f'A + B = {c}')} and {m(f'A - B = {u_minus_v}')}: {m(f'2A = {2*u} \\implies A = {u}')}. Squaring {m(f'\\sqrt{{{t1}}} = {u}')} gives {m(f'{t1} = {u*u} \\implies x = {x_ans}')}.",
            ],
            f"Substitute {m(f'x = {x_ans}')} back into the original equation: {m(f'\\sqrt{{{u*u}}} + \\sqrt{{{v*v}}} = {u} + {v} = {c}')} — verified!",
        )
        s_ar = explain_ar(
            "بدلاً من التربيع المتكرر المعقد، نرمز للجذرين بـ \\( A = \\sqrt{" + t1 + "} \\) و\\( B = \\sqrt{" + t2 + "} \\) ونستخدم متطابقة الفرق بين مربعين \\( A^2 - B^2 = (A - B)(A + B) \\)!",
            [
                f"نلاحظ أن {m(f'A^2 - B^2 = ({t1}) - ({t2}) = {diff_ab}')} (تختفي {m('x')} تماماً!).",
                f"بما أن {m(f'A + B = {c}')}، نقسم {m(diff_ab)} على {m(c)} فنحصل على {m(f'A - B = \\frac{{{diff_ab}}}{{{c}}} = {u_minus_v}')}.",
                f"بجمع المعادلتين نجد {m(f'2A = {2*u} \\implies A = {u}')}، وبتربيع {m(f'\\sqrt{{{t1}}} = {u}')} نحصل على {m(f'{t1} = {u*u} \\implies x = {x_ans}')}.",
            ],
            f"التعويض للتحقق في المعادلة الأصلية: {m(f'\\sqrt{{{u*u}}} + \\sqrt{{{v*v}}} = {u} + {v} = {c}')} — حل صحيح!",
        )
        push(diff, "kmc_g1011_radical_equations", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 5. Polynomial sign-chart integer inequalities (KMC Senior Round 1!) (10 Qs)
    # ------------------------------------------------------------------
    # How many integers k satisfy (k + a)(b - k)(k - c)^2 > 0 (or >= 0)?
    sign_cases = [
        (3, 6, 2, ">", "Easy"),       # (-3, 6) excluding 2: (-2,-1,0,1,3,4,5) -> 7
        (4, 5, 1, ">", "Easy"),       # (-4, 5) excluding 1 -> 7
        (2, 8, 5, ">", "Medium"),     # (-2, 8) excluding 5 -> 8
        (5, 7, 0, ">", "Medium"),     # (-5, 7) excluding 0 -> 10
        (6, 9, 3, ">", "Medium"),     # (-6, 9) excluding 3 -> 13
        (3, 5, 8, ">=", "Medium"),    # [-3, 5] U {8} -> 9 + 1 = 10! Look at c=8 outside [-3,5]!
        (4, 6, 10, ">=", "Medium"),   # [-4, 6] U {10} -> 11 + 1 = 12!
        (2, 7, -5, ">=", "Hard"),     # [-2, 7] U {-5} -> 10 + 1 = 11!
        (8, 10, 4, ">", "Hard"),      # (-8, 10) excluding 4 -> 16
        (5, 9, 12, ">=", "Hard"),     # [-5, 9] U {12} -> 15 + 1 = 16!
    ]
    for v_i, (a, b, c, rel, diff) in enumerate(sign_cases):
        def val_at(k):
            return (k + a) * (b - k) * ((k - c) ** 2)

        sols = [k for k in range(-100, 101) if (val_at(k) > 0 if rel == ">" else val_at(k) >= 0)]
        ans = len(sols)
        c_part = f"(k - {c})^2" if c >= 0 else f"(k + {abs(c)})^2"
        if rel == ">":
            assert -a < c < b
            # Trap: forgetting k = c makes (k-c)^2 = 0 (not > 0), or including endpoints -a, b
            distractors = [ans + 1, ans + 3, ans - 1, b - (-a)]
            ineq_tex = f"(k + {a})({b} - k){c_part} > 0"
            steps_en = [
                f"Notice that the squared factor {m(c_part)} is **positive for every {m(f'k \\ne {c}')}**, and equals **{m('0')}** when {m(f'k = {c}')}!",
                f"For {m(f'k \\ne {c}')}, we need {m(f'(k + {a})({b} - k) > 0')}, which holds strictly between the roots: {m(f'-{a} < k < {b}')}.",
                f"The integers in {m(f'(-{a}, {b})')} run from {m(-a + 1)} to {m(b - 1)} ({m(ans + 1)} integers), **minus {m(f'k = {c}')}** where the product is {m(0)}: {m(f'{ans + 1} - 1 = {ans}')} integers.",
            ]
            steps_ar = [
                f"نلاحظ أن العامل المربّع {m(c_part)} **موجب دائماً لكل {m(f'k \\ne {c}')}**، ويساوي **{m('0')}** عند {m(f'k = {c}')}!",
                f"لكي يكون الجداء موجباً تماماً ({m('> 0')}) يجب أن يكون {m(f'(k + {a})({b} - k) > 0')}، أي {m(f'-{a} < k < {b}')} مع استبعاد {m(f'k = {c}')}.",
                f"الأعداد الصحيحة من {m(-a + 1)} إلى {m(b - 1)} عددها {m(ans + 1)}، **نطرح منها العدد {m(f'k = {c}')}** فيكون الناتج **{m(ans)}**.",
            ]
        else:
            # >= 0 where c is outside [-a, b]
            assert c > b or c < -a
            distractors = [ans - 1, ans - 3, ans + 1, b - (-a)]
            ineq_tex = f"(k + {a})({b} - k){c_part} \\ge 0"
            steps_en = [
                f"Where is {m(f'(k + {a})({b} - k) \\ge 0')}? On the closed interval {m(f'-{a} \\le k \\le {b}')}, which contains {m(f'{b} - (-{a}) + 1 = {ans - 1}')} integers.",
                f"WAIT — don't forget where the squared factor {m(c_part)} equals **zero**! At {m(f'k = {c}')} (outside {m(f'[-{a}, {b}]')}), the entire product equals {m('0 \\ge 0')}!",
                f"Adding that isolated zero {m(f'k = {c}')} gives {m(f'{ans - 1} + 1 = {ans}')} integers in total.",
            ]
            steps_ar = [
                f"متى يكون {m(f'(k + {a})({b} - k) \\ge 0')}؟ في الفترة المغلقة {m(f'-{a} \\le k \\le {b}')} التي تضم {m(f'{b} - (-{a}) + 1 = {ans - 1}')} عدداً صحيحاً.",
                f"انتبه للفخ الذهبي! العامل المربّع {m(c_part)} يساوي **صفراً** عند {m(f'k = {c}')}، مما يجعل الجداء الكلي يساوي {m('0 \\ge 0')} أيضاً!",
                f"بإضافة الحل المنفرد {m(f'k = {c}')} يصبح إجمالي الأعداد الصحيحة: {m(f'{ans - 1} + 1 = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_sgn_{v_i}")
        q_en = f"How many **integers** {m('k')} satisfy the inequality {m(ineq_tex)}?"
        q_ar = f"كم **عدداً صحيحاً** {m('k')} يحقق المتباينة {m(ineq_tex)}؟"
        h_en = "Watch the squared factor carefully! A square is ≥ 0 everywhere, and equals 0 at its root (which is EXCLUDED for '> 0' and INCLUDED for '≥ 0')!"
        h_ar = "انتبه جيداً للعامل المربّع! فالمربع غير سالب دائماً، ويساوي صفراً عند جذره (فيُستبعد في حالة «< 0» ويُحسب ضمن الحلول في حالة «≤ 0»)!"
        s_en = explain_en("Squared factors never flip the sign of an inequality, **but** their root makes the whole product zero!", steps_en, f"Programmatic check over all integers confirms exactly {m(ans)} integer solutions.")
        s_ar = explain_ar("العوامل المربّعة لا تغيّر إشارة المتباينة أبداً، **لكن** جذرها يجعل حاصل الضرب الكلي مساوياً للصفر!", steps_ar, f"بالتحقق من أطراف الفترة وجذر العامل المربّع نتأكد أن عدد الحلول الصحيحة هو {m(ans)} بالضبط.")
        push(diff, "kmc_g1011_sign_chart_inequality", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. Telescoping fraction & radical sums (10 Qs)
    # ------------------------------------------------------------------
    tel_cases = [
        ("frac", 1, 20, "Easy"),
        ("frac", 1, 50, "Easy"),
        ("frac", 2, 22, "Medium"),
        ("frac", 3, 30, "Medium"),
        ("frac", 4, 40, "Medium"),
        ("rad", 1, 16, "Easy"),
        ("rad", 1, 25, "Medium"),
        ("rad", 4, 36, "Medium"),
        ("rad", 9, 49, "Hard"),
        ("rad", 16, 100, "Hard"),
    ]
    for v_i, (kind, a, b, diff) in enumerate(tel_cases):
        if kind == "frac":
            ans = Fraction(1, a) - Fraction(1, b)
            distractors = [
                Fraction(1, b),
                Fraction(b - a + 1, a * b),
                Fraction(1, a) + Fraction(1, b),
                Fraction(b - a - 1, a * b),
            ]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_tel_{v_i}")
            sum_tex = f"\\frac{{1}}{{{a}\\times{a+1}}} + \\frac{{1}}{{{a+1}\\times{a+2}}} + \\dots + \\frac{{1}}{{{b-1}\\times{b}}}"
            q_en = f"What is the exact value of the sum {m(sum_tex)}?"
            q_ar = f"ما القيمة الدقيقة للمجموع {m(sum_tex)}؟"
            h_en = "Rewrite each fraction using 1/(k(k+1)) = 1/k − 1/(k+1) and watch almost every term cancel out!"
            h_ar = "أعد كتابة كل كسر بالمتطابقة 1/(k(k+1)) = 1/k − 1/(k+1) وستلاحظ شطب جميع الحدود الوسطى بالتعاقب!"
            s_en = explain_en(
                "Use the telescoping identity \\( \\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1} \\): every inner negative fraction cancels the next positive fraction!",
                [
                    f"Split each term: {m(f'\\left(\\frac{{1}}{{{a}}} - \\frac{{1}}{{{a+1}}}\\right) + \\left(\\frac{{1}}{{{a+1}}} - \\frac{{1}}{{{a+2}}}\\right) + \\dots + \\left(\\frac{{1}}{{{b-1}}} - \\frac{{1}}{{{b}}}\\right)')}.",
                    f"All middle terms cancel in pairs, leaving only the **very first** and **very last** pieces: {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}}')}.",
                    f"Combine over common denominator {m(a*b)} and simplify: {m(fmt_val(ans))}.",
                ],
                f"Test with just 2 terms ({m(f'\\frac{{1}}{{{a}({a+1})}} + \\frac{{1}}{{({a+1})({a+2})}}')}): the formula {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{a+2}}}')} works identically!",
            )
            s_ar = explain_ar(
                "نستخدم المتطابقة التلسكوبية \\( \\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1} \\) حيث يُشطب كل حد سالب مع الحد الموجب الذي يليه!",
                [
                    f"نفكّك كل كسر: {m(f'\\left(\\frac{{1}}{{{a}}} - \\frac{{1}}{{{a+1}}}\\right) + \\left(\\frac{{1}}{{{a+1}}} - \\frac{{1}}{{{a+2}}}\\right) + \\dots + \\left(\\frac{{1}}{{{b-1}}} - \\frac{{1}}{{{b}}}\\right)')}.",
                    f"تُختصر جميع الحدود الوسطى ولا يتبقى سوى **الحد الأول** و**الحد الأخير**: {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}}')}.",
                    f"نوحد المقامات ونبسّط الكسر: {m(fmt_val(ans))}.",
                ],
                f"يمكنك تجربة أول حدّين فقط للتأكد فوراً من صحة الاختصار التلسكوبي!",
            )
        else:
            ra, rb = int(a ** 0.5), int(b ** 0.5)
            assert ra * ra == a and rb * rb == b
            ans = rb - ra
            distractors = [rb + ra, ans + 1, max(1, ans - 1), rb]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_tel_{v_i}")
            sum_tex = f"\\frac{{1}}{{\\sqrt{{{a}}}+\\sqrt{{{a+1}}}}} + \\frac{{1}}{{\\sqrt{{{a+1}}}+\\sqrt{{{a+2}}}}} + \\dots + \\frac{{1}}{{\\sqrt{{{b-1}}}+\\sqrt{{{b}}}}}"
            q_en = f"What is the exact value of {m(sum_tex)}?"
            q_ar = f"ما القيمة الدقيقة للمجموع {m(sum_tex)}؟"
            h_en = "Rationalize the denominator of 1/(√k + √(k+1)) by multiplying top and bottom by (√(k+1) − √k)!"
            h_ar = "أنطق مقام الحد العام 1/(√k + √(k+1)) بالضرب بسطاً ومقاماً في المرافق (√(k+1) − √k)!"
            s_en = explain_en(
                "Multiply numerator and denominator of \\( \\frac{1}{\\sqrt{k}+\\sqrt{k+1}} \\) by its conjugate \\( \\sqrt{k+1} - \\sqrt{k} \\): since \\( (\\sqrt{k+1})^2 - (\\sqrt{k})^2 = 1 \\), each fraction becomes simply \\( \\sqrt{k+1} - \\sqrt{k} \\)!",
                [
                    f"Rewrite every term: {m(f'(\\sqrt{{{a+1}}} - \\sqrt{{{a}}}) + (\\sqrt{{{a+2}}} - \\sqrt{{{a+1}}}) + \\dots + (\\sqrt{{{b}}} - \\sqrt{{{b-1}}})')}.",
                    f"All intermediate square roots cancel out, leaving {m(f'\\sqrt{{{b}}} - \\sqrt{{{a}}}')}.",
                    f"Evaluate the exact square roots: {m(f'{rb} - {ra} = {ans}')}.",
                ],
                f"Both {m(b)} and {m(a)} are perfect squares ({m(f'{rb}^2')} and {m(f'{ra}^2')}), giving the clean integer {m(ans)}!",
            )
            s_ar = explain_ar(
                "بضرب البسط والمقام للكسر \\( \\frac{1}{\\sqrt{k}+\\sqrt{k+1}} \\) في المرافق \\( \\sqrt{k+1} - \\sqrt{k} \\)، يصبح المقام \\( (k+1) - k = 1 \\)، فيتحول كل حد إلى \\( \\sqrt{k+1} - \\sqrt{k} \\)!",
                [
                    f"نعيد كتابة المجموع: {m(f'(\\sqrt{{{a+1}}} - \\sqrt{{{a}}}) + (\\sqrt{{{a+2}}} - \\sqrt{{{a+1}}}) + \\dots + (\\sqrt{{{b}}} - \\sqrt{{{b-1}}})')}.",
                    f"تُشطب جميع الجذور الوسطى بالتعاقب ولا يبقى سوى {m(f'\\sqrt{{{b}}} - \\sqrt{{{a}}}')}.",
                    f"نحسب الجذرين التربيعيين: {m(f'{rb} - {ra} = {ans}')}.",
                ],
                f"كلا العددين {m(b)} و{m(a)} مربعان كاملان، فيكون الناتج عدداً صحيحاً بسيطاً هو {m(ans)}!",
            )
        push(diff, "kmc_g1011_telescoping_sums", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 7. Maximizing product when incrementing one factor (KMC Senior!) (10 Qs)
    # ------------------------------------------------------------------
    inc_cases = [
        (3, 5, 8, 1, "gain", "Easy"),
        (4, 7, 10, 1, "gain", "Easy"),
        (2, 6, 9, 2, "gain", "Easy"),
        (5, 8, 12, 1, "max_prod", "Medium"),
        (4, 9, 11, 2, "gain", "Medium"),
        (6, 10, 15, 1, "gain", "Medium"),
        (3, 8, 14, 2, "max_prod", "Medium"),
        (7, 11, 16, 1, "gain", "Medium"),
        (5, 12, 18, 2, "gain", "Hard"),
        (8, 13, 20, 3, "gain", "Hard"),
    ]
    for v_i, (a, b, c, d, ask, diff) in enumerate(inc_cases):
        orig = a * b * c
        g_a = d * b * c
        g_b = d * a * c
        g_c = d * a * b
        assert g_a > g_b > g_c
        if ask == "gain":
            ans = g_a
            distractors = [g_c, g_b, d * (a + b + c), g_a + b]
            q_en = (
                f"Consider the product {m(f'{a} \\times {b} \\times {c}')}. You are allowed to add {m(d)} to **exactly one** of the three factors. "
                f"What is the **largest possible increase** in the value of the product?"
            )
            q_ar = (
                f"لديك حاصل الضرب {m(f'{a} \\times {b} \\times {c}')}. يُسمح لك بإضافة {m(d)} إلى **عامل واحد فقط** من العوامل الثلاثة. "
                f"ما **أكبر زيادة ممكنة** في قيمة حاصل الضرب؟"
            )
            final_line_en = f"The largest increase comes from adding {m(d)} to the **smallest** factor {m(a)}: {m(f'{d} \\times {b} \\times {c} = {ans}')}."
            final_line_ar = f"أكبر زيادة تنتج من إضافة {m(d)} إلى **أصغر** عامل {m(a)}: {m(f'{d} \\times {b} \\times {c} = {ans}')}."
        else:
            ans = orig + g_a
            distractors = [orig + g_c, orig + g_b, orig + d, (a + d) * (b + d) * c]
            q_en = (
                f"Starting with the three numbers {m(f'{a}, {b}, {c}')}, you add {m(d)} to **exactly one** of them and then multiply all three numbers together. "
                f"What is the **maximum possible product** you can obtain?"
            )
            q_ar = (
                f"لديك الأعداد الثلاثة {m(f'{a}, {b}, {c}')}. إذا أضفت {m(d)} إلى **عدد واحد فقط** منها ثم ضربت الأعداد الثلاثة معاً، "
                f"فما **أكبر حاصل ضرب ممكن** يمكنك الحصول عليه؟"
            )
            final_line_en = f"Increasing the smallest factor {m(a)} to {m(a+d)} gives the maximum product: {m(f'{a+d} \\times {b} \\times {c} = {ans}')}."
            final_line_ar = f"بزيادة أصغر عامل {m(a)} ليصبح {m(a+d)} نحصل على أكبر حاصل ضرب: {m(f'{a+d} \\times {b} \\times {c} = {ans}')}."

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_inc_{v_i}")
        h_en = "Many students guess you should increase the LARGEST factor — expand (a + d)bc = abc + d·bc to see why the opposite is true!"
        h_ar = "يظن كثير من الطلاب أنه يجب زيادة أكبر عامل! فكّ القوس (a + d)bc = abc + d·bc لتكتشف لماذا العكس هو الصحيح!"
        s_en = explain_en(
            "When \\( a < b < c \\), increasing \\( a \\) by \\( d \\) adds \\( d \\cdot b c \\), whereas increasing \\( c \\) by \\( d \\) only adds \\( d \\cdot a b \\). Since \\( b c > a c > a b \\), **always increase the smallest positive factor**!",
            [
                f"Compare the three gains: increasing {m(a)} adds {m(f'{d} \\times {b} \\times {c} = {g_a}')}; increasing {m(b)} adds {m(f'{d} \\times {a} \\times {c} = {g_b}')}; increasing {m(c)} adds {m(f'{d} \\times {a} \\times {b} = {g_c}')}.",
                final_line_en,
            ],
            f"Trap busted: increasing the largest factor {m(c)} gives the **smallest** gain ({m(g_c)}), not the largest!",
        )
        s_ar = explain_ar(
            "عندما يكون \\( a < b < c \\)، فإن زيادة \\( a \\) بمقدار \\( d \\) تضيف \\( d \\cdot b c \\)، بينما زيادة \\( c \\) تضيف \\( d \\cdot a b \\) فقط! وبما أن \\( b c > a c > a b \\)، **نزيد دائماً أصغر عامل موجب**!",
            [
                f"نقارن الزيادات الثلاث: زيادة {m(a)} تضيف {m(g_a)}، وزيادة {m(b)} تضيف {m(g_b)}، وزيادة {m(c)} تضيف {m(g_c)}.",
                final_line_ar,
            ],
            f"انتبه للفخ: زيادة أكبر عامل ({m(c)}) تعطي **أقل** زيادة ({m(g_c)}) وليس أكبرها!",
        )
        push(diff, "kmc_g1011_increment_factor_max_prod", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 8. Mean & median shift when appending elements to a dataset (10 Qs)
    # ------------------------------------------------------------------
    stat_cases = [
        # (n_orig, orig_mean, new_mean_target, med_val, diff): append 2 numbers x <= med_val <= y so median stays med_val!
        (5, 12, 14, 11, 8, "Easy"),    # given x=8 <= 11, find y so new mean of 7 numbers is 14 -> sum_new=98, orig=60 -> x+y=38 -> y=30 >= 11!
        (6, 15, 17, 14, 10, "Easy"),   # orig=90, new=8*17=136 -> x+y=46 -> y=36
        (7, 20, 22, 19, 15, "Easy"),   # orig=140, new=9*22=198 -> x+y=58 -> y=43
        (8, 18, 21, 18, 12, "Medium"), # orig=144, new=10*21=210 -> x+y=66 -> y=54
        (9, 25, 27, 24, 20, "Medium"), # orig=225, new=11*27=297 -> x+y=72 -> y=52
        (10, 30, 33, 29, 22, "Medium"),
        (11, 24, 26, 25, 18, "Medium"),
        (12, 35, 38, 34, 28, "Medium"),
        (13, 40, 43, 39, 31, "Hard"),
        (14, 50, 54, 48, 40, "Hard"),
    ]
    for v_i, (n0, m0, m1, med0, x_low, diff) in enumerate(stat_cases):
        s0 = n0 * m0
        n1 = n0 + 2
        s1 = n1 * m1
        y_high = (s1 - s0) - x_low
        assert x_low < med0 < y_high
        ans = y_high
        distractors = [s1 - s0, y_high - x_low, m1 * 2 - x_low, ans + m1 - m0]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_stat_{v_i}")
        q_en = (
            f"A list of {m(n0)} numbers has a mean (average) of {m(m0)} and a median of {m(med0)}. "
            f"Two new numbers, {m(x_low)} and {m('y')}, are added to the list. "
            f"If the median remains {m(med0)} and the new mean of all {m(n1)} numbers becomes {m(m1)}, what is {m('y')}?"
        )
        q_ar = (
            f"قائمة مكوّنة من {m(n0)} أعداد متوسطها الحسابي {m(m0)} ووسيطها {m(med0)}. "
            f"أُضيف عددان جديدان هما {m(x_low)} و{m('y')} إلى القائمة. "
            f"إذا بقي الوسيط {m(med0)} وأصبح المتوسط الحسابي الجديد للأعداد الـ {m(n1)} يساوي {m(m1)}، فما قيمة {m('y')}؟"
        )
        h_en = f"Convert both averages into TOTAL SUMS: original sum = {n0}×{m0}, new sum = {n1}×{m1}!"
        h_ar = f"حوّل المتوسطين إلى مجموعين كليين: المجموع الأصلي = {n0}×{m0}، والمجموع الجديد = {n1}×{m1}!"
        s_en = explain_en(
            "Adding one number below the median and one number above the median keeps the middle position unchanged, while the **total sum** determines \\( y \\)!",
            [
                f"Original total sum of the {m(n0)} numbers: {m(f'{n0} \\times {m0} = {s0}')}.",
                f"New total sum of all {m(n1)} numbers: {m(f'{n1} \\times {m1} = {s1}')}.",
                f"So {m(f'{x_low} + y = {s1} - {s0} = {s1 - s0} \\implies y = {s1 - s0} - {x_low} = {ans}')} (and since {m(f'{x_low} < {med0} < {ans}')}, the median indeed stays {m(med0)}!).",
            ],
            f"Check: \\( \\frac{{{s0} + {x_low} + {ans}}}{{{n1}}} = \\frac{{{s1}}}{{{n1}}} = {m1} \\).",
        )
        s_ar = explain_ar(
            "إضافة عدد أصغر من الوسيط وعدد أكبر من الوسيط يحافظ على موقع الوسيط ثابتاً، بينما يحدد **المجموع الكلي** قيمة \\( y \\)!",
            [
                f"المجموع الأصلي للأعداد الـ {m(n0)}: {m(f'{n0} \\times {m0} = {s0}')}.",
                f"المجموع الجديد للأعداد الـ {m(n1)}: {m(f'{n1} \\times {m1} = {s1}')}.",
                f"إذن {m(f'{x_low} + y = {s1} - {s0} = {s1 - s0} \\implies y = {ans}')} (وبما أن {m(f'{x_low} < {med0} < {ans}')} يبقى الوسيط {m(med0)} كما هو!).",
            ],
            f"تحقق: \\( \\frac{{{s0} + {x_low} + {ans}}}{{{n1}}} = {m1} \\) بالضبط.",
        )
        push(diff, "kmc_g1011_dataset_shift_stats", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 9. Vieta symmetric quadratic expressions (real roots only!) (9 Qs)
    # ------------------------------------------------------------------
    vieta_cases = [
        (5, 3, "sum_sq", "Easy"),      # s=5, p=3 (disc=13>0) -> r^2+t^2 = 25-6 = 19
        (6, 4, "sum_sq", "Easy"),      # 36-8 = 28
        (7, 5, "sum_sq", "Medium"),    # 49-10 = 39
        (8, 3, "recip", "Easy"),       # 1/r + 1/t = 8/3
        (9, 4, "recip", "Medium"),     # 9/4
        (7, 6, "diff_sq", "Medium"),   # (r-t)^2 = 49 - 24 = 25
        (10, 11, "sum_sq", "Medium"),  # 100 - 22 = 78
        (9, 14, "diff_sq", "Hard"),    # (r-t)^2 = 81 - 56 = 25
        (11, 15, "sum_sq", "Hard"),    # 121 - 30 = 91
    ]
    for v_i, (s, p, mode, diff) in enumerate(vieta_cases):
        assert s * s - 4 * p > 0, "Must have two distinct real roots!"
        eq_tex = f"x^2 - {s}x + {p} = 0"
        if mode == "sum_sq":
            ans = s * s - 2 * p
            distractors = [s * s - p, s * s + 2 * p, s * s - 4 * p, s * s]
            target_tex = "r^2 + t^2"
            steps_en = [
                f"By Vieta's formulas on {m(eq_tex)}, the sum of roots is {m(f'r + t = {s}')} and the product is {m(f'rt = {p}')}.",
                f"Use the identity {m('r^2 + t^2 = (r + t)^2 - 2rt')}.",
                f"Substitute: {m(f'({s})^2 - 2({p}) = {s*s} - {2*p} = {ans}')}.",
            ]
            steps_ar = [
                f"من علاقات فييت للمعادلة {m(eq_tex)}: مجموع الجذرين {m(f'r + t = {s}')} وحاصل ضربهما {m(f'rt = {p}')}.",
                f"نستخدم المتطابقة {m('r^2 + t^2 = (r + t)^2 - 2rt')}.",
                f"نعوض: {m(f'({s})^2 - 2({p}) = {s*s} - {2*p} = {ans}')}.",
            ]
        elif mode == "recip":
            ans = Fraction(s, p)
            distractors = [Fraction(p, s), Fraction(s, 2 * p), Fraction(s - 1, p), Fraction(s + 1, p)]
            target_tex = "\\frac{1}{r} + \\frac{1}{t}"
            steps_en = [
                f"By Vieta's formulas, {m(f'r + t = {s}')} and {m(f'rt = {p}')}.",
                f"Combine the fractions over a common denominator: {m('\\frac{1}{r} + \\frac{1}{t} = \\frac{r + t}{rt}')}.",
                f"Substitute {m(f'r + t = {s}')} and {m(f'rt = {p}')} to get {m(fmt_val(ans))}.",
            ]
            steps_ar = [
                f"من علاقات فييت: مجموع الجذرين {m(f'r + t = {s}')} وحاصل ضربهما {m(f'rt = {p}')}.",
                f"نوحد المقامات: {m('\\frac{1}{r} + \\frac{1}{t} = \\frac{r + t}{rt}')}.",
                f"بالتعويض نحصل فوراً على {m(fmt_val(ans))}.",
            ]
        else:
            ans = s * s - 4 * p
            distractors = [s * s - 2 * p, s * s - p, ans + 4, max(1, ans - 4)]
            target_tex = "(r - t)^2"
            steps_en = [
                f"By Vieta's formulas, {m(f'r + t = {s}')} and {m(f'rt = {p}')}.",
                f"Notice that {m('(r - t)^2 = r^2 - 2rt + t^2 = (r + t)^2 - 4rt')}.",
                f"Substitute: {m(f'({s})^2 - 4({p}) = {s*s} - {4*p} = {ans}')}.",
            ]
            steps_ar = [
                f"من علاقات فييت: {m(f'r + t = {s}')} و{m(f'rt = {p}')}.",
                f"نلاحظ المتطابقة: {m('(r - t)^2 = (r + t)^2 - 4rt')}.",
                f"نعوض: {m(f'({s})^2 - 4({p}) = {s*s} - {4*p} = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_vie_{v_i}")
        q_en = f"Let {m('r')} and {m('t')} be the two real roots of the quadratic equation {m(eq_tex)}. What is the value of {m(target_tex)}?"
        q_ar = f"ليكن {m('r')} و{m('t')} الجذرين الحقيقيين للمعادلة التربيعية {m(eq_tex)}. ما قيمة المقدار {m(target_tex)}؟"
        h_en = f"Don't use the quadratic formula! In x² − {s}x + {p} = 0, the sum of roots is r + t = {s} and the product is r·t = {p}!"
        h_ar = f"لا تحل بالقانون العام للجذور! في المعادلة x² − {s}x + {p} = 0، مجموع الجذرين r + t = {s} وحاصل ضربهما r·t = {p}!"
        s_en = explain_en("For any quadratic \\( x^2 - sx + p = 0 \\) with roots \\( r, t \\), expanding \\( (x - r)(x - t) = x^2 - (r+t)x + rt \\) shows \\( r + t = s \\) and \\( rt = p \\).", steps_en, f"Discriminant check: \\( {s}^2 - 4({p}) = {s*s - 4*p} > 0 \\), confirming both roots are real.")
        s_ar = explain_ar("لأي معادلة تربيعية \\( x^2 - sx + p = 0 \\) جذراها \\( r, t \\)، فكّ القوسين \\( (x - r)(x - t) \\) يبيّن أن \\( r + t = s \\) و\\( rt = p \\).", steps_ar, f"تحقق من المميز: \\( {s}^2 - 4({p}) = {s*s - 4*p} > 0 \\)، فالجذران حقيقيان.")
        push(diff, "kmc_g1011_vieta_real_quadratics", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 10. Sum & difference of cubes mental-math simplification (9 Qs)
    # ------------------------------------------------------------------
    cube_id_cases = [
        (2026, 26, "-", "Easy"),
        (150, 50, "-", "Easy"),
        (300, 120, "+", "Easy"),
        (2025, 1975, "-", "Medium"),
        (1200, 800, "+", "Medium"),
        (2026, 1026, "-", "Medium"),
        (1350, 650, "+", "Medium"),
        (2026, 1926, "+", "Hard"),
        (5000, 2974, "-", "Hard"),
    ]
    for v_i, (a, b, sign, diff) in enumerate(cube_id_cases):
        if sign == "-":
            ans = a - b
            expr_tex = f"\\frac{{{a}^3 - {b}^3}}{{{a}^2 + {a}\\times{b} + {b}^2}}"
            id_tex = "a^3 - b^3 = (a - b)(a^2 + ab + b^2)"
            distractors = [a + b, ans // 2, ans + 100, abs(a - 2 * b)]
        else:
            ans = a + b
            expr_tex = f"\\frac{{{a}^3 + {b}^3}}{{{a}^2 - {a}\\times{b} + {b}^2}}"
            id_tex = "a^3 + b^3 = (a + b)(a^2 - ab + b^2)"
            distractors = [a - b, ans // 2, ans + 100, ans - 100]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_cub_{v_i}")
        q_en = f"Without a calculator, find the exact value of {m(expr_tex)}."
        q_ar = f"بدون استخدام الآلة الحاسبة، أوجد القيمة الدقيقة للمقدار {m(expr_tex)}."
        h_en = f"Replace {a} with 'a' and {b} with 'b' — recognize the classic cube factorization {id_tex}!"
        h_ar = f"استبدل {a} بالرمز a و{b} بالرمز b — ستظهر لك فوراً متطابقة المكعبين الشهيرة {id_tex}!"
        s_en = explain_en(
            f"Never cube big numbers by hand in KMC! Let \\( a = {a} \\) and \\( b = {b} \\) and apply \\( {id_tex} \\).",
            [
                f"Factor the numerator: the quadratic factor in the denominator cancels out completely!",
                f"The entire fraction simplifies to {m('a - b' if sign == '-' else 'a + b')}.",
                f"Compute: {m(f'{a} {sign} {b} = {ans}')}.",
            ],
            f"Test on tiny numbers like \\( a=3, b=1 \\): \\( \\frac{{27 {sign} 1}}{{9 {'+' if sign=='-' else '-'} 3 + 1}} = {3 - 1 if sign=='-' else 3 + 1} \\) — works every time!",
        )
        s_ar = explain_ar(
            f"لا تحسب مكعبات الأعداد الكبيرة يدوياً في مسابقة كاوست! ضع \\( a = {a} \\) و\\( b = {b} \\) واستخدم المتطابقة \\( {id_tex} \\).",
            [
                f"نحلّل البسط فيُختصر القوس التربيعي كاملاً مع المقام!",
                f"يتبسّط الكسر بأكمله إلى {m('a - b' if sign == '-' else 'a + b')}.",
                f"نحسب مباشرة: {m(f'{a} {sign} {b} = {ans}')}.",
            ],
            f"جرّب أعداداً صغيرة مثل \\( a=3, b=1 \\) للتأكد من صحة الاختصار!",
        )
        push(diff, "kmc_g1011_sum_diff_cubes", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 11. Odd-power polynomial + constant symmetry f(-a) = 2K - f(a) (9 Qs)
    # ------------------------------------------------------------------
    sym_cases = [
        (2, -5, 7, 10, 3, 28, "Easy"),
        (3, 4, -2, 6, 4, 25, "Easy"),
        (1, -7, 5, 12, 5, 40, "Medium"),
        (4, 2, -9, -3, 7, 15, "Medium"),
        (5, -3, 8, 9, 6, -4, "Medium"),
        (2, 6, -11, 14, 8, 50, "Medium"),
        (7, -4, 3, -8, 9, 12, "Hard"),
        (3, -8, 13, 20, 11, 7, "Hard"),
        (6, 5, -7, 15, 2026, 43, "Hard"),
    ]
    for v_i, (c5, c3, c1, K, a_in, f_pos, diff) in enumerate(sym_cases):
        # Note: treat c5, c3, c1 as unknown constants a, b, c in the problem so f(a_in) = f_pos is always achievable!
        ans = 2 * K - f_pos
        distractors = [-f_pos, K - f_pos, f_pos - 2 * K, ans + K]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_sym_{v_i}")
        k_str = f"+ {K}" if K >= 0 else f"- {abs(K)}"
        q_en = (
            f"Let {m(f'f(x) = ax^5 + bx^3 + cx {k_str}')}, where {m('a, b, c')} are real constants. "
            f"If {m(f'f({a_in}) = {f_pos}')}, what is the value of {m(f'f(-{a_in})')}?"
        )
        q_ar = (
            f"لتكن {m(f'f(x) = ax^5 + bx^3 + cx {k_str}')} حيث {m('a, b, c')} ثوابت حقيقية. "
            f"إذا كان {m(f'f({a_in}) = {f_pos}')}، فما قيمة {m(f'f(-{a_in})')}؟"
        )
        h_en = f"Every exponent of x (5, 3, and 1) is ODD! Replacing x with −x flips the sign of (ax⁵ + bx³ + cx)!"
        h_ar = f"جميع أسس x (وهي 5 و3 و1) **فردية**! استبدال x بـ (−x) يعكس إشارة المقدار (ax⁵ + bx³ + cx) بالكامل!"
        odd_val = f_pos - K
        s_en = explain_en(
            "Because \\( (-x)^5 = -x^5 \\), \\( (-x)^3 = -x^3 \\), and \\( (-x)^1 = -x \\), the odd-power block \\( g(x) = ax^5 + bx^3 + cx \\) reverses sign at \\( -x \\): \\( g(-x) = -g(x) \\)!",
            [
                f"From {m(f'f({a_in}) = g({a_in}) + ({K}) = {f_pos}')}, isolate the odd part: {m(f'g({a_in}) = {f_pos} - ({K}) = {odd_val}')}.",
                f"Flip the input sign: {m(f'g(-{a_in}) = -g({a_in}) = {-odd_val}')}.",
                f"Add the constant {m(K)} back: {m(f'f(-{a_in}) = {-odd_val} + ({K}) = {ans}')}.",
            ],
            f"Shortcut check: \\( f({a_in}) + f(-{a_in}) = {f_pos} + ({ans}) = {2*K} = 2 \\times ({K}) \\)!",
        )
        s_ar = explain_ar(
            "بما أن الأسس 5 و3 و1 كلها فردية، فإن الجزء الفردي \\( g(x) = ax^5 + bx^3 + cx \\) يحقق \\( g(-x) = -g(x) \\)!",
            [
                f"من المعطى {m(f'f({a_in}) = g({a_in}) + ({K}) = {f_pos}')} نوجد قيمة الجزء الفردي: {m(f'g({a_in}) = {f_pos} - ({K}) = {odd_val}')}.",
                f"عند عكس إشارة المدخل تنعكس إشارة الجزء الفردي: {m(f'g(-{a_in}) = {-odd_val}')}.",
                f"نضيف الحد الثابت {m(K)}: {m(f'f(-{a_in}) = {-odd_val} + ({K}) = {ans}')}.",
            ],
            f"تحقق سريع: مجموع القيمتين \\( f({a_in}) + f(-{a_in}) = {f_pos} + ({ans}) = {2*K} \\) وهو ضعف الحد الثابت!",
        )
        push(diff, "kmc_g1011_odd_plus_const_symmetry", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 12. Absolute value distance equations & inequalities (8 Qs)
    # ------------------------------------------------------------------
    abs_cases = [
        (-2, 5, 7, "=", "Easy"),       # c = b - a = 7 -> every integer in [-2, 5] -> 8
        (1, 9, 8, "=", "Easy"),        # [1, 9] -> 9
        (-4, 6, 10, "=", "Medium"),    # [-4, 6] -> 11
        (2, 8, 10, "<=", "Medium"),    # |x-2| + |x-8| <= 10 -> [0, 10] -> 11
        (-3, 5, 12, "<=", "Medium"),   # [-5, 7] -> 13
        (0, 11, 11, "=", "Medium"),    # [0, 11] -> 12
        (-5, 7, 16, "<=", "Hard"),     # [-7, 9] -> 17
        (3, 15, 18, "<=", "Hard"),     # [0, 18] -> 19
    ]
    for v_i, (a, b, c, rel, diff) in enumerate(abs_cases):
        sols = [x for x in range(-100, 101) if (abs(x - a) + abs(x - b) == c if rel == "=" else abs(x - a) + abs(x - b) <= c)]
        ans = len(sols)
        t_a = f"|x - {a}|" if a >= 0 else f"|x + {abs(a)}|"
        t_b = f"|x - {b}|"
        eq_tex = f"{t_a} + {t_b} {'=' if rel == '=' else '\\le'} {c}"
        distractors = [2, ans - 1, ans + 1, ans - 2]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3a_abs_{v_i}")
        q_en = f"How many **integers** {m('x')} satisfy {m(eq_tex)}?"
        q_ar = f"كم **عدداً صحيحاً** {m('x')} يحقق العلاقة {m(eq_tex)}؟"
        h_en = f"Geometric meaning: |x − ({a})| + |x − {b}| is the sum of distances from x to {a} and to {b} on the number line!"
        h_ar = f"التفسير الهندسي على خط الأعداد: المقدار |x − ({a})| + |x − {b}| هو مجموع بُعدَي النقطة x عن {a} وعن {b}!"
        if rel == "=":
            steps_en = [
                f"On the number line, the distance between {m(a)} and {m(b)} is {m(f'{b} - ({a}) = {b - a}')}.",
                f"For ANY point {m('x')} between {m(a)} and {m(b)} (inclusive), the sum of its distances to the two endpoints equals the full segment length {m(c)}!",
                f"Count all integers from {m(a)} to {m(b)} inclusive: {m(f'{b} - ({a}) + 1 = {ans}')}.",
            ]
            steps_ar = [
                f"على خط الأعداد، المسافة بين {m(a)} و{m(b)} تساوي {m(f'{b} - ({a}) = {b - a}')}.",
                f"لأي نقطة {m('x')} تقع بين {m(a)} و{m(b)} (شاملة الطرفين)، يكون مجموع بُعديها عن الطرفين مساوياً لطول القطعة {m(c)} بالضبط!",
                f"نعدّ جميع الأعداد الصحيحة من {m(a)} إلى {m(b)}: {m(f'{b} - ({a}) + 1 = {ans}')}.",
            ]
        else:
            extra = (c - (b - a)) // 2
            lo, hi = a - extra, b + extra
            steps_en = [
                f"Between {m(a)} and {m(b)}, the distance sum is {m(b - a)}. Stepping {m('d')} units outside either endpoint adds {m('2d')} to the distance sum!",
                f"Since we have {m(f'{c} - {b-a} = {c - (b-a)}')} of slack, {m('x')} can go up to {m(f'{c-(b-a)} \\div 2 = {extra}')} units left of {m(a)} or right of {m(b)}: {m(f'{lo} \\le x \\le {hi}')}.",
                f"Count the integers in {m(f'[{lo}, {hi}]')}: {m(f'{hi} - ({lo}) + 1 = {ans}')}.",
            ]
            steps_ar = [
                f"بين {m(a)} و{m(b)} يساوي مجموع المسافتين {m(b - a)}، والابتعاد بمقدار {m('d')} خارج أي طرف يزيد مجموع المسافتين بمقدار {m('2d')}!",
                f"الزيادة المسموحة هي {m(f'{c} - {b-a} = {c - (b-a)}')}, أي يمكن التحرك حتى {m(extra)} وحدات يسار {m(a)} أو يمين {m(b)}: {m(f'{lo} \\le x \\le {hi}')}.",
                f"عدد الأعداد الصحيحة في الفترة {m(f'[{lo}, {hi}]')} هو: {m(f'{hi} - ({lo}) + 1 = {ans}')}.",
            ]
        s_en = explain_en("Interpreting \\( |x - p| \\) as **distance on a number line** solves absolute-value sums without tedious sign cases!", steps_en, f"Classic trap avoided: when \\( c = b - a \\), there isn't just 2 solutions — the entire interval \\( [{a}, {b}] \\) works!")
        s_ar = explain_ar("تفسير \\( |x - p| \\) على أنه **المسافة على خط الأعداد** يحل معادلات ومتباينات القيمة المطلقة فوراً دون تقسيم مطوّل للحالات!", steps_ar, f"تجنبنا الفخ الشهير: لا يقتصر الحل على طرفين فقط بل يشمل جميع الأعداد الصحيحة في الفترة المستنتجة!")
        push(diff, "kmc_g1011_abs_piecewise_solutions", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    assert len(out) == 115, f"Expected 115, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 3 Algebra questions cleanly.")

