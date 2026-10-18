#!/usr/bin/env python3
"""
KAUST Phase 2 Questions Part A: 251 to 300
Advanced Analysis: Single & Multivariable Calculus, Integration Techniques, Green's Theorem.
Authentic lineages: STEP II/III, Putnam, MIT 18.01/18.02, JEE Advanced.
"""

def get_p2_part_a():
    questions = []

    def q(qid, topic, diff, q_en, q_ar, options, corr_idx, exp_en, exp_ar, hint_en, hint_ar, diagram=None):
        item = {
            "id": qid,
            "track": "kaust",
            "level": "Phase 2: Advanced Analysis",
            "topic": topic,
            "type": "MCQ",
            "difficulty": diff,
            "content": {
                "en": {
                    "question": q_en,
                    "options": options,
                    "hint": hint_en,
                    "explanation": exp_en
                },
                "ar": {
                    "question": q_ar,
                    "options": options,
                    "hint": hint_ar,
                    "explanation": exp_ar
                }
            },
            "correct_index": corr_idx
        }
        if diagram:
            item["diagram"] = diagram
        questions.append(item)

    svg_box = lambda inner, title, w=380, h=180: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 {h}" style="display:block;max-width:100%;width:{w}px;margin:16px auto;background:#ffffff;border-radius:8px;border:1px solid #cbd5e1"><title>{title}</title>{inner}</svg>'

    # 251: Gaussian Integral
    q("KAUST-P2-251", "Multivariable Calculus", "Medium",
      "Evaluate the famous Gaussian integral \\( I = \\int_{-\\infty}^{\\infty} e^{-x^2} \\, dx \\).",
      "احسب قيمة تكامل غاوس الشهير \\( I = \\int_{-\\infty}^{\\infty} e^{-x^2} \\, dx \\).",
      ["\\( \\sqrt{\\pi} \\)", "\\( \\pi \\)", "\\( \\dfrac{\\sqrt{\\pi}}{2} \\)", "\\( 2\\sqrt{\\pi} \\)"], 0,
      "Consider \\( I^2 = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty e^{-(x^2+y^2)} dx dy \\). Converting to polar coordinates: \\( I^2 = \\int_0^{2\\pi} d\\theta \\int_0^\\infty r e^{-r^2} dr = 2\\pi \\left[ -\\dfrac{1}{2} e^{-r^2} \\right]_0^\\infty = 2\\pi \\left( \\dfrac{1}{2} \\right) = \\pi \\). Thus, \\( I = \\sqrt{\\pi} \\). [Lineage: Gaussian Integral / MIT 18.02]",
      "بحساب \\( I^2 \\) في الإحداثيات القطبية: \\( I^2 = \\int_0^{2\\pi} d\\theta \\int_0^\\infty r e^{-r^2} dr = \\pi \\). إذن \\( I = \\sqrt{\\pi} \\). [المرجع: تكامل غاوس في التحليل الرياضي]",
      "Square the integral and switch to polar coordinates.", "ربع التكامل وتحول إلى الإحداثيات القطبية.")

    # 252: Gamma function at 1/2
    q("KAUST-P2-252", "Advanced Calculus", "Easy",
      "What is the exact value of the Gamma function evaluated at \\( 1/2 \\), \\( \\Gamma(1/2) \\)?",
      "ما هي القيمة الدقيقة لدالة غاما عند النصف \\( \\Gamma(1/2) \\)؟",
      ["\\( \\dfrac{1}{2} \\)", "\\( 1 \\)", "\\( \\sqrt{\\pi} \\)", "\\( \\pi \\)"], 2,
      "\\( \\Gamma(1/2) = \\int_0^\\infty t^{-1/2} e^{-t} dt \\). Substituting \\( t = u^2 \\implies dt = 2u du \\): \\( \\Gamma(1/2) = 2 \\int_0^\\infty e^{-u^2} du = \\int_{-\\infty}^\\infty e^{-u^2} du = \\sqrt{\\pi} \\). [Lineage: Euler's Gamma Function / Cambridge STEP III]",
      "بالتعويض \\( t = u^2 \\) في تعريف دالة غاما، يؤول التكامل إلى تكامل غاوس الذي يساوي \\( \\sqrt{\\pi} \\). [المرجع: دالة غاما لأويلر]",
      "Substitute \\( t = u^2 \\) to relate to the Gaussian integral.", "عوض بـ \\( t = u^2 \\) لربط الدالة بتكامل غاوس.")

    # 253: Feynman's trick / Dirichlet integral
    q("KAUST-P2-253", "Advanced Calculus", "Hard",
      "Evaluate the Dirichlet improper integral \\( \\int_0^{\\infty} \\dfrac{\\sin x}{x} \\, dx \\).",
      "احسب قيمة تكامل ديركلي المعتل \\( \\int_0^{\\infty} \\dfrac{\\sin x}{x} \\, dx \\).",
      ["\\( \\dfrac{\\pi}{4} \\)", "\\( \\dfrac{\\pi}{2} \\)", "\\( \\pi \\)", "\\( 2\\pi \\)"], 1,
      "Let \\( I(a) = \\int_0^\\infty e^{-ax} \\dfrac{\\sin x}{x} dx \\) for \\( a > 0 \\). Differentiating under the integral sign: \\( I'(a) = -\\int_0^\\infty e^{-ax} \\sin x dx = -\\dfrac{1}{a^2 + 1} \\). Integrating gives \\( I(a) = -\\arctan(a) + C \\). Since \\( \\lim_{a \\to \\infty} I(a) = 0 \\), \\( C = \\pi/2 \\). Setting \\( a = 0 \\) yields \\( I(0) = \\pi/2 \\). [Lineage: Feynman Technique / Dirichlet Integral / Putnam]",
      "باستخدام تقنية فاينمان (الاشتقاق تحت علامة التكامل): \\( I(a) = \\int_0^\\infty e^{-ax} \\frac{\\sin x}{x} dx \\)، نجد \\( I'(a) = -\\frac{1}{a^2+1} \\implies I(0) = \\pi/2 \\). [المرجع: تقنية فاينمان للتكامل في مسابقة بوتنام]",
      "Introduce a parameter \\( e^{-ax} \\) and differentiate with respect to \\( a \\).", "أدخل المعلمة \\( e^{-ax} \\) واشتق بالنسبة لـ a.")

    # 254: Arc length of catenary (Diagram)
    d254 = svg_box('<path d="M 40,130 Q 130,40 220,130" fill="none" stroke="#2563eb" stroke-width="2.5"/><line x1="20" y1="140" x2="240" y2="140" stroke="#94a3b8" stroke-width="1.5"/><line x1="130" y1="20" x2="130" y2="160" stroke="#94a3b8" stroke-width="1.5"/><circle cx="130" cy="50" r="4" fill="#ef4444"/><text x="140" y="55" font-size="12" fill="#ef4444" font-weight="bold">y = cosh(x)</text><text x="70" y="160" font-size="11" fill="#1e293b">-1</text><text x="190" y="160" font-size="11" fill="#1e293b">1</text>', "Catenary Curve", 360, 180)
    q("KAUST-P2-254", "Calculus", "Medium",
      "What is the arc length of the catenary curve \\( y = \\cosh x \\) from \\( x = 0 \\) to \\( x = 1 \\)?",
      "ما هو طول قوس منحنى السلسلة \\( y = \\cosh x \\) من \\( x = 0 \\) إلى \\( x = 1 \\)؟",
      ["\\( 1 \\)", "\\( \\sinh(1) \\)", "\\( \\cosh(1) \\)", "\\( e \\)"], 1,
      "The arc length formula is \\( L = \\int_0^1 \\sqrt{1 + (y')^2} dx \\). Since \\( y' = \\sinh x \\), \\( \\sqrt{1 + \\sinh^2 x} = \\sqrt{\\cosh^2 x} = \\cosh x \\). Thus \\( L = \\int_0^1 \\cosh x dx = [\\sinh x]_0^1 = \\sinh(1) \\). [Lineage: Arc Length of Catenary / STEP II]",
      "قانون طول القوس: \\( L = \\int_0^1 \\sqrt{1 + \\sinh^2 x} dx = \\int_0^1 \\cosh x dx = \\sinh(1) \\). [المرجع: طول قوس المنحنيات في STEP]",
      "Use the identity \\( 1 + \\sinh^2 x = \\cosh^2 x \\).", "استخدم المتطابقة الزائدية الأساسية.", diagram=d254)

    # 255: Green's Theorem Area
    q("KAUST-P2-255", "Multivariable Calculus", "Medium",
      "According to Green's Theorem, which line integral along a positively oriented simple closed curve \\( C \\) computes the enclosed area \\( A \\)?",
      "وفقاً لمبرهنة غرين، أي تكامل خطي على مسار مغلق بسيط موجب الاتجاه \\( C \\) يحسب المساحة المحصورة \\( A \\)؟",
      ["\\( \\oint_C (x dy + y dx) \\)", "\\( \\dfrac{1}{2} \\oint_C (x dy - y dx) \\)", "\\( \\oint_C (x dx + y dy) \\)", "\\( \\oint_C xy \\, ds \\)"], 1,
      "By Green's Theorem: \\( \\oint_C (L dx + M dy) = \\iint_D \\left( \\dfrac{\\partial M}{\\partial x} - \\dfrac{\\partial L}{\\partial y} \\right) dA \\). For \\( L = -y/2, M = x/2 \\): \\( \\dfrac{\\partial M}{\\partial x} - \\dfrac{\\partial L}{\\partial y} = \\dfrac{1}{2} - \\left(-\\dfrac{1}{2}\\right) = 1 \\), so \\( \\text{Area} = \\dfrac{1}{2} \\oint_C (x dy - y dx) \\). [Lineage: Green's Theorem Area Formula / MIT 18.02]",
      "باستخدام مبرهنة غرين، باختيار \\( L = -y/2 \\) و \\( M = x/2 \\) يصبح التكامل الثنائي مساوياً لمساحة المنطقة تماماً. [المرجع: مبرهنة غرين لحساب المساحات]",
      "Apply Green's Theorem with \\( \\partial M/\\partial x - \\partial L/\\partial y = 1 \\).", "طبق مبرهنة غرين بحيث ينتج 1 داخل التكامل الثنائي.")

    # 256: Gradient and Level Curves (Diagram)
    d256 = svg_box('<ellipse cx="130" cy="90" rx="90" ry="60" fill="none" stroke="#3b82f6" stroke-width="1.5"/><ellipse cx="130" cy="90" rx="60" ry="40" fill="none" stroke="#2563eb" stroke-width="2"/><ellipse cx="130" cy="90" rx="30" ry="20" fill="none" stroke="#1d4ed8" stroke-width="2"/><circle cx="172" cy="62" r="4" fill="#ef4444"/><line x1="172" y1="62" x2="210" y2="35" stroke="#ef4444" stroke-width="2.5"/><text x="195" y="30" font-size="12" fill="#ef4444" font-weight="bold">∇f</text><text x="130" y="95" font-size="11" fill="#1e293b" text-anchor="middle">Level curves f(x,y)=c</text>', "Gradient Orthogonal to Level Curve", 360, 180)
    q("KAUST-P2-256", "Multivariable Calculus", "Easy",
      "What is the geometric relationship between the gradient vector \\( \\nabla f(x_0, y_0) \\) and the level curve \\( f(x, y) = c \\) passing through \\( (x_0, y_0) \\)?",
      "ما هي العلاقة الهندسية بين متجه التدرج \\( \\nabla f(x_0, y_0) \\) ومنحنى المستوى \\( f(x, y) = c \\) المار بالنقطة \\( (x_0, y_0) \\)؟",
      ["\\( \\nabla f \\) is tangent to the level curve.", "\\( \\nabla f \\) is perpendicular (orthogonal) to the level curve.", "\\( \\nabla f \\) is parallel to the coordinate axis.", "There is no fixed geometric relationship."], 1,
      "The gradient vector \\( \\nabla f \\) is always perpendicular (orthogonal) to the tangent vector of the level curve \\( f(x, y) = c \\) at every regular point, pointing in the direction of steepest increase. [Lineage: Gradient Vector Geometry / MIT 18.02]",
      "متجه التدرج \\( \\nabla f \\) يكون دائماً عمودياً على منحنى المستوى عند كل نقطة، ويشير إلى اتجاه الصعود الأكثر انحداراً. [المرجع: الهندسة التفاضلية في MIT]",
      "Recall the direction of steepest ascent relative to constant-height contours.", "تذكر اتجاه الانحدار الأقصى بالنسبة لخطوط الكنتور.", diagram=d256)

    # 257: Directional derivative
    q("KAUST-P2-257", "Multivariable Calculus", "Medium",
      "Find the directional derivative of \\( f(x, y) = x^2 y + 3y \\) at the point \\( (1, 2) \\) in the direction of the unit vector \\( \\mathbf{u} = \\left\\langle \\dfrac{3}{5}, \\dfrac{4}{5} \\right\\rangle \\).",
      "أوجد المشتقة الاتجاهية للدالة \\( f(x, y) = x^2 y + 3y \\) عند النقطة \\( (1, 2) \\) في اتجاه متجه الوحدة \\( \\mathbf{u} = \\left\\langle \\dfrac{3}{5}, \\dfrac{4}{5} \\right\\rangle \\).",
      ["\\( 4.8 \\)", "\\( 5.6 \\)", "\\( 6.0 \\)", "\\( 7.2 \\)"], 1,
      "Compute the gradient: \\( \\nabla f = \\langle 2xy, x^2 + 3 \\rangle \\). At \\( (1, 2) \\): \\( \\nabla f(1, 2) = \\langle 2(1)(2), 1^2 + 3 \\rangle = \\langle 4, 4 \\rangle \\). The directional derivative is \\( D_{\\mathbf{u}} f = \\nabla f \\cdot \\mathbf{u} = 4\\left(\\dfrac{3}{5}\\right) + 4\\left(\\dfrac{4}{5}\\right) = \\dfrac{12 + 16}{5} = \\dfrac{28}{5} = 5.6 \\). [Lineage: Directional Derivatives / Calculus III]",
      "التدرج عند النقطة هو \\( \\langle 4, 4 \\rangle \\). المشتقة الاتجاهية: \\( \\langle 4, 4 \\rangle \\cdot \\langle 3/5, 4/5 \\rangle = \\dfrac{28}{5} = 5.6 \\). [المرجع: المشتقات الاتجاهية في التحليل الرياضي]",
      "Compute \\( \\nabla f(1, 2) \\cdot \\mathbf{u} \\).", "احسب حاصل الضرب القياسي للتدرج في متجه الوحدة.")

    # 258: Tangent plane to surface
    q("KAUST-P2-258", "Multivariable Calculus", "Medium",
      "Find the equation of the tangent plane to the surface \\( z = x^2 + y^2 \\) at the point \\( (1, 2, 5) \\).",
      "أوجد معادلة المستوى المماس للسطح \\( z = x^2 + y^2 \\) عند النقطة \\( (1, 2, 5) \\).",
      ["\\( 2x + 4y - z = 5 \\)", "\\( 2x + 4y - z = 0 \\)", "\\( x + 2y - z = 0 \\)", "\\( 4x + 2y - z = 3 \\)"], 0,
      "Let \\( F(x, y, z) = x^2 + y^2 - z = 0 \\). The normal vector is \\( \\nabla F = \\langle 2x, 2y, -1 \\rangle \\). At \\( (1, 2, 5) \\): \\( \\mathbf{n} = \\langle 2, 4, -1 \\rangle \\). The tangent plane is \\( 2(x - 1) + 4(y - 2) - 1(z - 5) = 0 \\implies 2x + 4y - z - 2 - 8 + 5 = 0 \\implies 2x + 4y - z = 5 \\). [Lineage: Tangent Planes / MIT 18.02]",
      "المتجه العمودي هو \\( \\nabla F = \\langle 2, 4, -1 \\rangle \\). معادلة المستوى المماس: \\( 2(x-1) + 4(y-2) - (z-5) = 0 \\implies 2x + 4y - z = 5 \\). [المرجع: المستويات المماسة للسطوح]",
      "Use \\( f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) - (z - z_0) = 0 \\).", "طبق صيغة المستوى المماس بدلالة المشتقات الجزئية.")

    # 259: Lagrange Multipliers
    q("KAUST-P2-259", "Multivariable Calculus", "Medium",
      "Using Lagrange multipliers, find the maximum value of \\( f(x, y) = xy \\) subject to the constraint \\( x^2 + y^2 = 8 \\) for positive \\( x, y > 0 \\).",
      "باستخدام مضاعفات لاغرانج، أوجد القيمة العظمى للدالة \\( f(x, y) = xy \\) تحت القيد \\( x^2 + y^2 = 8 \\) للأعداد الموجبة \\( x, y > 0 \\).",
      ["\\( 2 \\)", "\\( 4 \\)", "\\( 8 \\)", "\\( 16 \\)"], 1,
      "\\( \\nabla f = \\lambda \\nabla g \\implies \\langle y, x \\rangle = \\lambda \\langle 2x, 2y \\rangle \\). Thus \\( y = 2\\lambda x \\) and \\( x = 2\\lambda y \\implies y/x = x/y \\implies x^2 = y^2 \\). Since \\( x, y > 0 \\), \\( x = y \\). Substituting into \\( x^2 + y^2 = 8 \\) gives \\( 2x^2 = 8 \\implies x = 2, y = 2 \\). Max value \\( f(2, 2) = 2 \\times 2 = 4 \\). [Lineage: Lagrange Multipliers / AMC 12]",
      "بمضاعفات لاغرانج نجد \\( x = y \\). بالتعويض في القيد: \\( 2x^2 = 8 \\implies x = y = 2 \\). القيمة العظمى هي \\( 2 \\times 2 = 4 \\). [المرجع: مضاعفات لاغرانج]",
      "By symmetry and Lagrange conditions, \\( x = y \\).", "بشروط لاغرانج والتماثل نجد \\( x = y \\).")

    # 260: Jacobian transformation
    q("KAUST-P2-260", "Multivariable Calculus", "Easy",
      "What is the Jacobian determinant \\( \\dfrac{\\partial(x, y)}{\\partial(r, \\theta)} \\) of the transformation from Cartesian to polar coordinates \\( x = r\\cos\\theta, y = r\\sin\\theta \\)?",
      "ما هو محدد جاكوبي \\( \\dfrac{\\partial(x, y)}{\\partial(r, \\theta)} \\) للتحويل من الإحداثيات الديكارتية إلى القطبية \\( x = r\\cos\\theta, y = r\\sin\\theta \\)؟",
      ["\\( 1 \\)", "\\( r \\)", "\\( r^2 \\)", "\\( \\dfrac{1}{r} \\)"], 1,
      "\\( J = \\begin{vmatrix} \\partial x/\\partial r & \\partial x/\\partial \\theta \\\\ \\partial y/\\partial r & \\partial y/\\partial \\theta \\end{vmatrix} = \\begin{vmatrix} \\cos\\theta & -r\\sin\\theta \\\\ \\sin\\theta & r\\cos\\theta \\end{vmatrix} = r\\cos^2\\theta - (-r\\sin^2\\theta) = r(\\cos^2\\theta + \\sin^2\\theta) = r \\). [Lineage: Polar Jacobian / MIT 18.02]",
      "محدد جاكوبي هو \\( r\\cos^2\\theta + r\\sin^2\\theta = r \\)، وهو عامل التمدد المساحي في التكاملات القطبية. [المرجع: محدد جاكوبي في التفاضل والتكامل]",
      "Evaluate the \\( 2 \\times 2 \\) determinant of partial derivatives.", "احسب محدد المشتقات الجزئية للمصفوفة 2x2.")

    # 261: Conservative Vector Field
    q("KAUST-P2-261", "Multivariable Calculus", "Medium",
      "Which condition confirms that a continuously differentiable 2D vector field \\( \\mathbf{F} = \\langle P(x, y), Q(x, y) \\rangle \\) on \\( \\mathbb{R}^2 \\) is conservative (has a scalar potential \\( f \\) with \\( \\nabla f = \\mathbf{F} \\))?",
      "أي شرط يثبت أن المجال الشعاعي \\( \\mathbf{F} = \\langle P(x, y), Q(x, y) \\rangle \\) على \\( \\mathbb{R}^2 \\) هو مجال محافظ (يمتلك دالة جهد قياسية \\( \\nabla f = \\mathbf{F} \\))؟",
      ["\\( \\dfrac{\\partial P}{\\partial x} = \\dfrac{\\partial Q}{\\partial y} \\)", "\\( \\dfrac{\\partial P}{\\partial y} = \\dfrac{\\partial Q}{\\partial x} \\)", "\\( P^2 + Q^2 = 1 \\)", "\\( \\dfrac{\\partial P}{\\partial x} + \\dfrac{\\partial Q}{\\partial y} = 0 \\)"], 1,
      "By Clairaut's theorem on mixed partial derivatives, for \\( \\mathbf{F} = \\nabla f = \\langle f_x, f_y \\rangle \\), we must have \\( \\dfrac{\\partial P}{\\partial y} = f_{xy} = f_{yx} = \\dfrac{\\partial Q}{\\partial x} \\). On a simply connected domain like \\( \\mathbb{R}^2 \\), this condition is both necessary and sufficient. [Lineage: Conservative Vector Fields / MIT 18.02]",
      "شرط المجال المحافظ بمبرهنة كليرو للمشتقات المختلطة هو \\( \\dfrac{\\partial P}{\\partial y} = \\dfrac{\\partial Q}{\\partial x} \\). [المرجع: المجالات الشعاعية المحافظة]",
      "Equate mixed partial derivatives \\( f_{xy} = f_{yx} \\).", "ساوِ بين المشتقات الجزئية المختلطة لدالة الجهد.")

    # 262: Stokes' Theorem formulation
    q("KAUST-P2-262", "Multivariable Calculus", "Easy",
      "Stokes' Theorem relates the surface integral of the curl of a vector field over an oriented surface \\( S \\) to which line integral along its boundary curve \\( \\partial S \\)?",
      "تربط مبرهنة ستوكس التكامل السطحي لدوران مجال شعاعي على سطح \\( S \\) بأي تكامل خطي على منحنى حدوده \\( \\partial S \\)؟",
      ["\\( \\oint_{\\partial S} \\mathbf{F} \\cdot d\\mathbf{r} \\)", "\\( \\oint_{\\partial S} (\\nabla \\cdot \\mathbf{F}) \\, ds \\)", "\\( \\oint_{\\partial S} \\|\\mathbf{F}\\| \\, dr \\)", "\\( 0 \\)"], 0,
      "Classical Stokes' Theorem states: \\( \\iint_S (\\nabla \\times \\mathbf{F}) \\cdot d\\mathbf{S} = \\oint_{\\partial S} \\mathbf{F} \\cdot d\\mathbf{r} \\). [Lineage: Stokes' Theorem / MIT 18.02]",
      "تنص مبرهنة ستوكس على أن: \\( \\iint_S (\\nabla \\times \\mathbf{F}) \\cdot d\\mathbf{S} = \\oint_{\\partial S} \\mathbf{F} \\cdot d\\mathbf{r} \\). [المرجع: مبرهنة ستوكس]",
      "Recall Stokes' theorem: flux of curl equals circulation.", "تذكر نص مبرهنة ستوكس الكلاسيكية.")

    # 263: Divergence Theorem
    q("KAUST-P2-263", "Multivariable Calculus", "Easy",
      "The Divergence Theorem (Gauss's Theorem) equates the volume integral of \\( \\nabla \\cdot \\mathbf{F} \\) over a solid region \\( V \\) to:",
      "تساوي مبرهنة التباعد (مبرهنة غاوس) التكامل الحجمي لـ \\( \\nabla \\cdot \\mathbf{F} \\) على منطقة ثلاثية الأبعاد \\( V \\) بـ:",
      ["The flux \\( \\iint_{\\partial V} \\mathbf{F} \\cdot d\\mathbf{S} \\) across the closed boundary", "The line integral \\( \\oint_{\\partial V} \\mathbf{F} \\cdot d\\mathbf{r} \\)", "The curl \\( \\nabla \\times \\mathbf{F} \\)", "Zero always"], 0,
      "The Divergence Theorem states that \\( \\iiint_V (\\nabla \\cdot \\mathbf{F}) \\, dV = \\iint_{\\partial V} \\mathbf{F} \\cdot d\\mathbf{S} \\). [Lineage: Divergence Theorem / MIT 18.02]",
      "تنص مبرهنة التباعد لغاوس على أن تكامل التباعد الحجمي يساوي تدفق المجال عبر السطح المغلق المحيط. [المرجع: مبرهنة التباعد لغاوس]",
      "Divergence integrated over volume equals outward flux.", "تكامل التباعد على الحجم يساوي التدفق الخارجي عبر السطح.")

    # 264: Leibniz integral rule
    q("KAUST-P2-264", "Advanced Calculus", "Medium",
      "According to the Leibniz integral rule, what is \\( \\dfrac{d}{dx} \\int_0^{x^2} \\sin(t) \\, dt \\)?",
      "وفقاً لقاعدة لايبنتز لاشتقاق التكاملات المحددة، ما هي قيمة \\( \\dfrac{d}{dx} \\int_0^{x^2} \\sin(t) \\, dt \\)؟",
      ["\\( \\sin(x^2) \\)", "\\( 2x \\sin(x^2) \\)", "\\( 2x \\cos(x^2) \\)", "\\( x^2 \\sin(x) \\)"], 1,
      "By the Fundamental Theorem of Calculus with chain rule (Leibniz rule): \\( \\dfrac{d}{dx} \\int_{a(x)}^{b(x)} f(t) dt = f(b(x)) b'(x) - f(a(x)) a'(x) \\). Here: \\( \\sin(x^2) \\cdot (x^2)' = 2x \\sin(x^2) \\). [Lineage: Leibniz Rule / STEP I]",
      "حسب قاعدة السلسلة للتكامل: نضرب قيمة الدالة عند الحد العلوي في مشتقة الحد العلوي: \\( 2x \\sin(x^2) \\). [المرجع: قاعدة لايبنتز لاشتقاق التكاملات]",
      "Multiply \\( f(b(x)) \\) by \\( b'(x) \\).", "عوض بالحد العلوي واضرب في مشتقته.")

    # 265: Double integral polar
    q("KAUST-P2-265", "Multivariable Calculus", "Easy",
      "Evaluate \\( \\iint_D (x^2 + y^2) \\, dA \\) where \\( D \\) is the unit disk \\( x^2 + y^2 \\le 1 \\).",
      "احسب قيمة التكامل الثنائي \\( \\iint_D (x^2 + y^2) \\, dA \\) حيث \\( D \\) هو القرص الدائري الموحد \\( x^2 + y^2 \\le 1 \\).",
      ["\\( \\dfrac{\\pi}{4} \\)", "\\( \\dfrac{\\pi}{2} \\)", "\\( \\pi \\)", "\\( 2\\pi \\)"], 1,
      "In polar coordinates: \\( x^2 + y^2 = r^2 \\) and \\( dA = r dr d\\theta \\). Thus \\( \\int_0^{2\\pi} d\\theta \\int_0^1 r^2 (r dr) = 2\\pi \\int_0^1 r^3 dr = 2\\pi \\left[ \\dfrac{r^4}{4} \\right]_0^1 = 2\\pi \\left(\\dfrac{1}{4}\\right) = \\dfrac{\\pi}{2} \\). [Lineage: Polar Integration / MIT 18.02]",
      "بالتحويل للقطبي: \\( 2\\pi \\int_0^1 r^3 dr = 2\\pi (1/4) = \\pi/2 \\). [المرجع: التكاملات الثنائية القطبية]",
      "Remember the Jacobian factor \\( r \\) in \\( dA = r dr d\\theta \\).", "لا تنسَ عامل جاكوبي r في عنصر المساحة القطبية.")

    # 266: Center of Mass
    q("KAUST-P2-266", "Calculus", "Medium",
      "What is the \\( y \\)-coordinate of the centroid of a uniform semicircular lamina of radius \\( R \\) centered at the origin for \\( y \\ge 0 \\)?",
      "ما هو الإحداثي الصادي \\( \\bar{y} \\) لمركز ثقل صفيحة نصف دائرية منتظمة نصف قطرها \\( R \\) في النصف العلوي \\( y \\ge 0 \\)؟",
      ["\\( \\dfrac{2R}{\\pi} \\)", "\\( \\dfrac{4R}{3\\pi} \\)", "\\( \\dfrac{3R}{8} \\)", "\\( \\dfrac{R}{2} \\)"], 1,
      "\\( \\bar{y} = \\dfrac{\\iint y dA}{\\text{Area}} \\). In polar coordinates: \\( \\iint y dA = \\int_0^\\pi \\sin\\theta d\\theta \\int_0^R r^2 dr = (2) \\left( \\dfrac{R^3}{3} \\right) = \\dfrac{2R^3}{3} \\). Area of semicircle is \\( \\dfrac{\\pi R^2}{2} \\). Thus \\( \\bar{y} = \\dfrac{2R^3/3}{\\pi R^2/2} = \\dfrac{4R}{3\\pi} \\). [Lineage: Centroid of Semicircle / JEE Advanced]",
      "مركز ثقل نصف القرص هو \\( \\bar{y} = \\dfrac{4R}{3\\pi} \\). [المرجع: مراكز الثقل في التفاضل والتكامل]",
      "Divide the moment about the x-axis by the area of the semicircle.", "اقسم عزم المساحة حول محور السينات على مساحة نصف القرص.")

    # 267: Clairaut's theorem
    q("KAUST-P2-267", "Multivariable Calculus", "Easy",
      "Clairaut's (Schwarz's) Theorem states that if mixed second partial derivatives of \\( f(x, y) \\) are continuous, then:",
      "تنص مبرهنة كليرو (شفارز) على أنه إذا كانت المشتقات الجزئية الثانية المختلطة للدالة \\( f(x, y) \\) متصلة، فإن:",
      ["\\( f_{xx} = f_{yy} \\)", "\\( f_{xy} = f_{yx} \\)", "\\( f_{xy} = -f_{yx} \\)", "\\( f_{xx} + f_{yy} = 0 \\)"], 1,
      "Clairaut's Theorem guarantees the symmetry of second derivatives for \\( C^2 \\) functions: \\( \\dfrac{\\partial^2 f}{\\partial x \\partial y} = \\dfrac{\\partial^2 f}{\\partial y \\partial x} \\). [Lineage: Clairaut's Theorem / Calculus III]",
      "تضمن مبرهنة كليرو تساوي المشتقات الجزئية المختلطة: \\( f_{xy} = f_{yx} \\). [المرجع: مبرهنة كليرو]",
      "Mixed partial derivatives are independent of the order of differentiation.", "المشتقات المختلطة لا تعتمد على ترتيب التفاضل.")

    # 268: Curvature of a Circle
    q("KAUST-P2-268", "Differential Geometry", "Easy",
      "What is the curvature \\( \\kappa \\) of a circle of radius \\( R \\)?",
      "ما هو انحناء \\( \\kappa \\) دائرة نصف قطرها \\( R \\)؟",
      ["\\( R \\)", "\\( \\dfrac{1}{R} \\)", "\\( \\dfrac{1}{R^2} \\)", "\\( 2\\pi R \\)"], 1,
      "By definition, the curvature of a circle is constant and inversely proportional to its radius: \\( \\kappa = \\dfrac{1}{R} \\). [Lineage: Differential Geometry / Curvature]",
      "انحناء الدائرة ثابت في جميع نقاطها ويساوي مقلوب نصف القطر: \\( \\kappa = 1/R \\). [المرجع: الهندسة التفاضلية للمنحنيات]",
      "Curvature is the reciprocal of the radius of curvature.", "الانحناء هو مقلوب نصف قطر الانحناء.")

    # 269: Taylor series of ln(1 + x)
    q("KAUST-P2-269", "Calculus", "Easy",
      "What is the coefficient of \\( x^3 \\) in the Maclaurin series of \\( \\ln(1 + x) \\)?",
      "ما هو معامل \\( x^3 \\) في متسلسلة ماكلوران للدالة \\( \\ln(1 + x) \\)؟",
      ["\\( -\\dfrac{1}{6} \\)", "\\( \\dfrac{1}{6} \\)", "\\( -\\dfrac{1}{3} \\)", "\\( \\dfrac{1}{3} \\)"], 3,
      "The series expansion is \\( \\ln(1 + x) = x - \\dfrac{x^2}{2} + \\dfrac{x^3}{3} - \\dfrac{x^4}{4} + \\dots \\). The coefficient of \\( x^3 \\) is \\( \\dfrac{1}{3} \\). [Lineage: Maclaurin Series / Calculus]",
      "المتسلسلة هي \\( x - x^2/2 + x^3/3 - \\dots \\)، إذن معامل \\( x^3 \\) هو \\( 1/3 \\). [المرجع: متسلسلات ماكلوران]",
      "Recall the standard Mercator series for \\( \\ln(1+x) \\).", "تذكر متسلسلة ميركاتور للوغاريتم الطبيعي.")

    # 270: Improper integral 1/(1 + x^2)
    q("KAUST-P2-270", "Calculus", "Easy",
      "Evaluate \\( \\int_{-\\infty}^{\\infty} \\dfrac{1}{1 + x^2} \\, dx \\).",
      "احسب قيمة \\( \\int_{-\\infty}^{\\infty} \\dfrac{1}{1 + x^2} \\, dx \\).",
      ["\\( 1 \\)", "\\( \\dfrac{\\pi}{2} \\)", "\\( \\pi \\)", "\\( 2\\pi \\)"], 2,
      "\\( \\int_{-\\infty}^\\infty \\dfrac{1}{1 + x^2} dx = [\\arctan(x)]_{-\\infty}^\\infty = \\dfrac{\\pi}{2} - \\left(-\\dfrac{\\pi}{2}\\right) = \\pi \\). [Lineage: Improper Integrals / High School]",
      "التكامل المعتل: \\( [\\arctan(x)]_{-\\infty}^\\infty = \\pi/2 - (-\\pi/2) = \\pi \\). [المرجع: التكاملات المعتلة]",
      "Antiderivative is \\( \\arctan(x) \\).", "الدالة الأصلية هي قوس الظل.")

    # 271: Integration by Parts x e^x
    q("KAUST-P2-271", "Calculus", "Easy",
      "Evaluate \\( \\int_0^1 x e^x \\, dx \\).",
      "احسب قيمة التكامل \\( \\int_0^1 x e^x \\, dx \\).",
      ["\\( 1 \\)", "\\( e - 1 \\)", "\\( e \\)", "\\( 2e - 1 \\)"], 0,
      "By integration by parts with \\( u = x, dv = e^x dx \\): \\( \\int x e^x dx = x e^x - e^x = e^x(x - 1) \\). Evaluating from 0 to 1: \\( e^1(1 - 1) - e^0(0 - 1) = 0 - (-1) = 1 \\). [Lineage: Integration by Parts / High School]",
      "بالتكامل بالتجزيء: \\( [e^x(x-1)]_0^1 = 0 - (-1) = 1 \\). [المرجع: التكامل بالتجزيء]",
      "Use \\( \\int u dv = uv - \\int v du \\).", "طبق قانون التكامل بالتجزيء.")

    # 272: Volume of Sphere by Shells
    q("KAUST-P2-272", "Calculus", "Easy",
      "What is the volume of a sphere of radius \\( R \\) obtained by rotating the region under \\( y = \\sqrt{R^2 - x^2} \\) about the \\( x \\)-axis?",
      "ما هو حجم كرة نصف قطرها \\( R \\) الناتجة من دوران المنطقة الواقعة تحت \\( y = \\sqrt{R^2 - x^2} \\) حول محور السينات؟",
      ["\\( \\pi R^3 \\)", "\\( \\dfrac{4}{3}\\pi R^3 \\)", "\\( 2\\pi R^3 \\)", "\\( \\dfrac{4}{3}\\pi R^2 \\)"], 1,
      "By the disk method: \\( V = \\pi \\int_{-R}^R y^2 dx = \\pi \\int_{-R}^R (R^2 - x^2) dx = 2\\pi \\left[ R^2 x - \\dfrac{x^3}{3} \\right]_0^R = 2\\pi \\left( \\dfrac{2R^3}{3} \\right) = \\dfrac{4}{3}\\pi R^3 \\). [Lineage: Volumes of Revolution / Calculus]",
      "بطريقة الأقراص: \\( V = \\pi \\int_{-R}^R (R^2 - x^2) dx = \\dfrac{4}{3}\\pi R^3 \\). [المرجع: حجوم المجسمات الدورانية]",
      "Integrate \\( \\pi y^2 dx \\).", "كامل مساحة المقطع الدائري.")

    # 273: L'Hopital 0/0
    q("KAUST-P2-273", "Calculus", "Easy",
      "Evaluate \\( \\lim_{x \\to 0} \\dfrac{1 - \\cos x}{x^2} \\).",
      "احسب قيمة \\( \\lim_{x \\to 0} \\dfrac{1 - \\cos x}{x^2} \\).",
      ["\\( 0 \\)", "\\( \\dfrac{1}{2} \\)", "\\( 1 \\)", "Does not exist"], 1,
      "Applying L'Hôpital's Rule twice: \\( \\lim_{x \\to 0} \\dfrac{\\sin x}{2x} = \\lim_{x \\to 0} \\dfrac{\\cos x}{2} = \\dfrac{1}{2} \\). [Lineage: L'Hopital's Rule / AMC 12]",
      "بتطبيق قاعدة لوبيتال مرتين: \\( \\dfrac{\\cos 0}{2} = \\dfrac{1}{2} \\). [المرجع: قاعدة لوبيتال]",
      "Differentiate numerator and denominator twice.", "اشتق البسط والمقام مرتين.")

    # 274: Critical Points Classification
    q("KAUST-P2-274", "Multivariable Calculus", "Medium",
      "For a function \\( f(x, y) \\) with critical point \\( (x_0, y_0) \\), if the Hessian determinant \\( D = f_{xx}f_{yy} - (f_{xy})^2 < 0 \\), what type of critical point is \\( (x_0, y_0) \\)?",
      "لدالة \\( f(x, y) \\) ذات نقطة حرجة \\( (x_0, y_0) \\)، إذا كان محدد هيسيان \\( D = f_{xx}f_{yy} - (f_{xy})^2 < 0 \\)، فما نوع هذه النقطة الحرجة؟",
      ["Local minimum", "Local maximum", "Saddle point", "Inconclusive"], 2,
      "By the Second Derivative Test for functions of two variables, if the discriminant \\( D < 0 \\), the critical point is a saddle point. [Lineage: Second Derivative Test / Multivariable Calculus]",
      "وفق اختبار المشتقة الثانية للمتغيرين، إذا كان المميز سالباً \\( D < 0 \\)، فإن النقطة تمثل نقطة سرج (saddle point). [المرجع: تصنيف النقاط الحرجة]",
      "A negative Hessian determinant signifies a saddle point.", "محدد هيسيان السالب يشير دائماً إلى نقطة سرج.")

    # 275: Laplace Equation
    q("KAUST-P2-275", "Partial Differential Equations", "Easy",
      "A function \\( u(x, y) \\) satisfying Laplace's equation \\( \\nabla^2 u = \\dfrac{\\partial^2 u}{\\partial x^2} + \\dfrac{\\partial^2 u}{\\partial y^2} = 0 \\) is called:",
      "تُسمى الدالة \\( u(x, y) \\) التي تحقق معادلة لابلاس \\( \\nabla^2 u = 0 \\) بـ:",
      ["Harmonic function", "Analytic function", "Wave function", "Holomorphic function"], 0,
      "By definition, any \\( C^2 \\) solution to Laplace's equation \\( \\Delta u = 0 \\) is termed a harmonic function. [Lineage: Potential Theory / Laplace Equation]",
      "تُعرف أي دالة تحقق معادلة لابلاس بالدالة التوافقية (Harmonic function). [المرجع: نظرية الجهد ومعادلة لابلاس]",
      "Recall the name of solutions to \\( \\Delta u = 0 \\).", "تذكر اسم حلول معادلة لابلاس.")

    # 276: Area between parabolas
    q("KAUST-P2-276", "Calculus", "Easy",
      "Find the area enclosed between the two parabolas \\( y = x^2 \\) and \\( y = 2x - x^2 \\).",
      "أوجد المساحة المحصورة بين القطعين المكافئين \\( y = x^2 \\) و \\( y = 2x - x^2 \\).",
      ["\\( \\dfrac{1}{6} \\)", "\\( \\dfrac{1}{3} \\)", "\\( \\dfrac{1}{2} \\)", "\\( 1 \\)"], 1,
      "Intersection points: \\( x^2 = 2x - x^2 \\implies 2x^2 - 2x = 0 \\implies x = 0, 1 \\). Area: \\( \\int_0^1 ((2x - x^2) - x^2) dx = \\int_0^1 (2x - 2x^2) dx = \\left[ x^2 - \\dfrac{2x^3}{3} \\right]_0^1 = 1 - \\dfrac{2}{3} = \\dfrac{1}{3} \\). [Lineage: Area Between Curves / High School]",
      "نقاط التقاطع عند 0 و 1. تكامل الفرق يعطي \\( 1 - 2/3 = 1/3 \\). [المرجع: حساب المساحات بالتكامل]",
      "Find the intersection points and integrate \\( y_{\\text{top}} - y_{\\text{bottom}} \\).", "أوجد نقاط التقاطع وكامل الفرق بين المنحنيين.")

    # 277: Fundamental Theorem of Line Integrals
    q("KAUST-P2-277", "Multivariable Calculus", "Easy",
      "If \\( \\mathbf{F} = \\nabla f \\) is a conservative vector field, what is the value of the line integral \\( \\int_C \\mathbf{F} \\cdot d\\mathbf{r} \\) along any curve \\( C \\) from point \\( A \\) to point \\( B \\)?",
      "إذا كان \\( \\mathbf{F} = \\nabla f \\) مجالاً شعاعياً محافظاً، فما هي قيمة التكامل الخطي \\( \\int_C \\mathbf{F} \\cdot d\\mathbf{r} \\) على أي منحنى \\( C \\) من النقطة \\( A \\) إلى النقطة \\( B \\)؟",
      ["\\( f(B) - f(A) \\)", "\\( f(A) + f(B) \\)", "\\( \\|B - A\\| \\)", "\\( 0 \\) always"], 0,
      "By the Fundamental Theorem for Line Integrals: \\( \\int_C \\nabla f \\cdot d\\mathbf{r} = f(B) - f(A) \\), depending only on the endpoints. [Lineage: Fundamental Theorem of Line Integrals / MIT 18.02]",
      "حسب المبرهنة الأساسية للتكاملات الخطية، تعتمد القيمة فقط على طرفي المنحنى: \\( f(B) - f(A) \\). [المرجع: المبرهنة الأساسية للتكامل الخطي]",
      "The integral depends only on the potential values at the endpoints.", "التكامل يعتمد فقط على قيمة دالة الجهد عند نقطتي البداية والنهاية.")

    # 278: Taylor series sin(x)
    q("KAUST-P2-278", "Calculus", "Easy",
      "What is the general term in the Maclaurin series expansion of \\( \\sin x \\)?",
      "ما هو الحد العام في مفكوك متسلسلة ماكلوران لدالة الجيب \\( \\sin x \\)؟",
      ["\\( \\sum_{n=0}^{\\infty} \\dfrac{(-1)^n x^{2n+1}}{(2n+1)!} \\)", "\\( \\sum_{n=0}^{\\infty} \\dfrac{(-1)^n x^{2n}}{(2n)!} \\)", "\\( \\sum_{n=0}^{\\infty} \\dfrac{x^{2n+1}}{(2n+1)!} \\)", "\\( \\sum_{n=1}^{\\infty} \\dfrac{x^n}{n} \\)"], 0,
      "The sine function is odd, so its Maclaurin series contains only odd powers of \\( x \\) with alternating signs: \\( \\sum_{n=0}^\\infty \\dfrac{(-1)^n x^{2n+1}}{(2n+1)!} \\). [Lineage: Maclaurin Series / Calculus]",
      "دالة الجيب دالة فردية، لذا تحتوي متسلسلتها على القوى الفردية بإشارات متناوبة: \\( \\sum \\dfrac{(-1)^n x^{2n+1}}{(2n+1)!} \\). [المرجع: متسلسلات تايلور وماكلوران]",
      "Recall that sine is an odd function.", "تذكر أن الجيب دالة فردية.")

    # 279: Surface Area of Revolution
    q("KAUST-P2-279", "Calculus", "Medium",
      "Which formula calculates the surface area generated by rotating \\( y = f(x) \\ge 0 \\) from \\( x = a \\) to \\( x = b \\) about the \\( x \\)-axis?",
      "أي صيغة تحسب مساحة السطح الدوراني المتولد من دوران \\( y = f(x) \\ge 0 \\) من \\( x = a \\) إلى \\( x = b \\) حول محور السينات؟",
      ["\\( 2\\pi \\int_a^b y \\sqrt{1 + (y')^2} \\, dx \\)", "\\( \\pi \\int_a^b y^2 \\, dx \\)", "\\( 2\\pi \\int_a^b x y \\, dx \\)", "\\( \\int_a^b \\sqrt{1 + (y')^2} \\, dx \\)"], 0,
      "Surface area of revolution about the x-axis is \\( S = 2\\pi \\int y \\, ds = 2\\pi \\int_a^b f(x) \\sqrt{1 + (f'(x))^2} dx \\). [Lineage: Surface Area of Revolution / Calculus]",
      "مساحة السطح الدوراني حول محور السينات: \\( 2\\pi \\int y \\sqrt{1 + (y')^2} dx \\). [المرجع: مساحات السطوح الدورانية]",
      "Integrate circumference \\( 2\\pi y \\) times arc length element \\( ds \\).", "كامل محيط الدوران مضروباً في عنصر طول القوس.")

    # 280: Mean Value Theorem
    q("KAUST-P2-280", "Calculus", "Easy",
      "If \\( f \\) is continuous on \\( [a, b] \\) and differentiable on \\( (a, b) \\), the Mean Value Theorem asserts the existence of \\( c \\in (a, b) \\) such that:",
      "إذا كانت \\( f \\) متصلة على \\( [a, b] \\) وقابلة للاشتقاق على \\( (a, b) \\)، فإن مبرهنة القيمة المتوسطة تؤكد وجود \\( c \\in (a, b) \\) بحيث:",
      ["\\( f'(c) = \\dfrac{f(b) - f(a)}{b - a} \\)", "\\( f'(c) = 0 \\)", "\\( f(c) = \\dfrac{f(a) + f(b)}{2} \\)", "\\( f'(c) = f(b) - f(a) \\)"], 0,
      "The Mean Value Theorem states that the instantaneous rate of change \\( f'(c) \\) equals the average rate of change \\( \\dfrac{f(b) - f(a)}{b - a} \\) at some point. [Lineage: Mean Value Theorem]",
      "تنص مبرهنة القيمة المتوسطة على وجود نقطة يتساوى عندها الميل اللحظي مع الميل المتوسط: \\( f'(c) = \\dfrac{f(b) - f(a)}{b - a} \\). [المرجع: مبرهنة القيمة المتوسطة]",
      "Instantaneous slope equals secant slope.", "الميل اللحظي يساوي ميل القاطع.")

    # 281-300: remaining questions of Part A
    # 281: Integral of ln(x)
    q("KAUST-P2-281", "Calculus", "Easy",
      "Evaluate \\( \\int_1^e \\ln(x) \\, dx \\).",
      "احسب قيمة التكامل \\( \\int_1^e \\ln(x) \\, dx \\).",
      ["\\( 1 \\)", "\\( e - 1 \\)", "\\( e \\)", "\\( \\dfrac{1}{e} \\)"], 0,
      "\\( \\int \\ln(x) dx = x\\ln(x) - x \\). Evaluating from 1 to \\( e \\): \\( (e\\ln e - e) - (1\\ln 1 - 1) = (e - e) - (0 - 1) = 1 \\). [Lineage: Calculus Integration / High School]",
      "بالتكامل بالتجزيء: \\( [x\\ln x - x]_1^e = 0 - (-1) = 1 \\). [المرجع: تكامل اللوغاريتم الطبيعي]",
      "Use \\( \\int \\ln x dx = x \\ln x - x \\).", "الدالة الأصلية للوغاريتم هي \\( x\\ln x - x \\).")

    # 282: Wallis product
    q("KAUST-P2-282", "Calculus & Analysis", "Hard",
      "Wallis's formula expresses \\( \\dfrac{\\pi}{2} \\) as an infinite product of which sequence of ratios?",
      "تعبر صيغة فاليس عن \\( \\dfrac{\\pi}{2} \\) كجداء لانهائي لأي متتالية من النسب؟",
      ["\\( \\prod_{n=1}^{\\infty} \\left( \\dfrac{2n}{2n - 1} \\cdot \\dfrac{2n}{2n + 1} \\right) \\)", "\\( \\prod_{n=1}^{\\infty} \\left(1 - \\dfrac{1}{n^2}\\right) \\)", "\\( \\sum_{n=1}^{\\infty} \\dfrac{1}{n^2} \\)", "\\( \\prod_{n=1}^{\\infty} \\dfrac{n}{n+1} \\)"], 0,
      "John Wallis proved in 1655 that \\( \\dfrac{\\pi}{2} = \\prod_{n=1}^\\infty \\left( \\dfrac{2n}{2n-1} \\cdot \\dfrac{2n}{2n+1} \\right) = \\dfrac{2}{1} \\cdot \\dfrac{2}{3} \\cdot \\dfrac{4}{3} \\cdot \\dfrac{4}{5} \\dots \\). [Lineage: Wallis' Formula / Analysis]",
      "أثبت فاليس صيغة الجداء اللانهائي الشهيرة لـ \\( \\pi/2 \\): \\( \\prod \\dfrac{4n^2}{4n^2-1} \\). [المرجع: صيغة فاليس للجداء اللانهائي]",
      "Recall the famous alternating rational fraction product for pi/2.", "تذكر جداء فاليس لحساب باي.")

    # 283: Beta and Gamma relation
    q("KAUST-P2-283", "Advanced Calculus", "Medium",
      "How is Euler's Beta function \\( B(x, y) \\) related to the Gamma function \\( \\Gamma \\)?",
      "كيف ترتبط دالة بيتا لأويلر \\( B(x, y) \\) بدالة غاما \\( \\Gamma \\)؟",
      ["\\( B(x, y) = \\dfrac{\\Gamma(x)\\Gamma(y)}{\\Gamma(x + y)} \\)", "\\( B(x, y) = \\Gamma(x)\\Gamma(y) \\)", "\\( B(x, y) = \\dfrac{\\Gamma(x + y)}{\\Gamma(x)\\Gamma(y)} \\)", "\\( B(x, y) = \\Gamma(xy) \\)"], 0,
      "The fundamental identity connecting Beta and Gamma functions is \\( B(x, y) = \\dfrac{\\Gamma(x)\\Gamma(y)}{\\Gamma(x + y)} \\). [Lineage: Special Functions / Cambridge Tripos]",
      "العلاقة الأساسية بين دالتي بيتا وغاما: \\( B(x, y) = \\dfrac{\\Gamma(x)\\Gamma(y)}{\\Gamma(x + y)} \\). [المرجع: الدوال الخاصة في التحليل الرياضي]",
      "Recall the integral relation between Beta and Gamma.", "تذكر المتطابقة الأساسية بين دالتي بيتا وغاما.")

    # 284: Integral of sec(x)
    q("KAUST-P2-284", "Calculus", "Easy",
      "What is the standard antiderivative of \\( \\sec x \\)?",
      "ما هي الدالة الأصلية القياسية لـ \\( \\sec x \\)؟",
      ["\\( \\ln|\\sec x + \\tan x| + C \\)", "\\( \\tan x + C \\)", "\\( \\sec x \\tan x + C \\)", "\\( \\ln|\\cos x| + C \\)"], 0,
      "Multiplying numerator and denominator by \\( (\\sec x + \\tan x) \\): \\( \\int \\sec x dx = \\ln|\\sec x + \\tan x| + C \\). [Lineage: Trigonometric Integration]",
      "بالضرب في \\( (\\sec x + \\tan x) \\) بسطاً ومقاماً: \\( \\ln|\\sec x + \\tan x| + C \\). [المرجع: تكامل الدوال المثلثية]",
      "Multiply by \\( \\frac{\\sec x + \\tan x}{\\sec x + \\tan x} \\).", "اضرب في مرافق القاطع والظل.")

    # 285: Saddle point Hessian
    q("KAUST-P2-285", "Multivariable Calculus", "Easy",
      "For \\( f(x, y) = x^2 - y^2 \\), the origin \\( (0, 0) \\) is a:",
      "للدالة \\( f(x, y) = x^2 - y^2 \\)، النقطة الأصل \\( (0, 0) \\) تمثل:",
      ["Global maximum", "Global minimum", "Saddle point", "Inflection point"], 2,
      "\\( f_{xx} = 2, f_{yy} = -2, f_{xy} = 0 \\). Discriminant \\( D = (2)(-2) - 0 = -4 < 0 \\). Thus \\( (0, 0) \\) is a saddle point. [Lineage: Multivariable Extrema]",
      "المميز \\( D = -4 < 0 \\)، إذن النقطة الأصل هي نقطة سرج. [المرجع: القيم القصوى لدوال بعدين]",
      "The function increases along x and decreases along y.", "الدالة تتزايد باتجاه x وتتناقص باتجاه y.")

    # 286: Curl of Gradient
    q("KAUST-P2-286", "Vector Calculus", "Easy",
      "For any twice continuously differentiable scalar field \\( f \\), what is \\( \\nabla \\times (\\nabla f) \\)?",
      "لأي مجال قياسي \\( f \\) قابل للاشتقاق مرتين باستمرار، ما هي قيمة دوران التدرج \\( \\nabla \\times (\\nabla f) \\)؟",
      ["\\( \\mathbf{0} \\)", "\\( \\nabla^2 f \\)", "\\( \\nabla f \\)", "\\( 1 \\)"], 0,
      "The curl of any gradient field is identically zero: \\( \\text{curl}(\\text{grad } f) = \\mathbf{0} \\), reflecting Clairaut's theorem. [Lineage: Vector Calculus Identities / MIT 18.02]",
      "دوران أي مجال تدرج يساوي دائماً المتجه الصفري: \\( \\text{curl}(\\nabla f) = \\mathbf{0} \\). [المرجع: متطابقات التفاضل الشعاعي]",
      "Gradient fields are irrotational.", "المجالات التدرجية لا دورانية.")

    # 287: Divergence of Curl
    q("KAUST-P2-287", "Vector Calculus", "Easy",
      "For any twice continuously differentiable vector field \\( \\mathbf{F} \\), what is \\( \\nabla \\cdot (\\nabla \\times \\mathbf{F}) \\)?",
      "لأي مجال شعاعي \\( \\mathbf{F} \\) قابل للاشتقاق مرتين، ما هي قيمة تباعد الدوران \\( \\nabla \\cdot (\\nabla \\times \\mathbf{F}) \\)؟",
      ["\\( 0 \\)", "\\( \\|\\mathbf{F}\\| \\)", "\\( \\nabla^2 \\mathbf{F} \\)", "\\( \\nabla \\cdot \\mathbf{F} \\)"], 0,
      "The divergence of any curl field is identically zero: \\( \\text{div}(\\text{curl } \\mathbf{F}) = 0 \\). [Lineage: Vector Calculus Identities]",
      "تباعد أي دوران يساوي صفراً دائماً: \\( \\text{div}(\\text{curl } \\mathbf{F}) = 0 \\). [المرجع: متطابقات التحليل الشعاعي]",
      "Curl fields are solenoidal (incompressible).", "مجالات الدوران أنبوبية (عديمة التباعد).")

    # 288: Harmonic Conjugate
    q("KAUST-P2-288", "Complex Analysis", "Medium",
      "If \\( u(x, y) = x^2 - y^2 \\) is the real part of an entire function \\( f(z) = u + iv \\), find its harmonic conjugate \\( v(x, y) \\) (up to an additive constant).",
      "إذا كان \\( u(x, y) = x^2 - y^2 \\) هو الجزء الحقيقي لدالة تامة \\( f(z) = u + iv \\)، فأوجد المرافق التوافقي \\( v(x, y) \\).",
      ["\\( 2xy \\)", "\\( -2xy \\)", "\\( x^2 + y^2 \\)", "\\( y^2 - x^2 \\)"], 0,
      "By Cauchy-Riemann: \\( u_x = 2x = v_y \\implies v(x, y) = 2xy + g(x) \\). Also \\( u_y = -2y = -v_x \\implies v_x = 2y \\). Since \\( \\partial(2xy)/\\partial x = 2y \\), \\( g'(x) = 0 \\). Thus \\( v(x, y) = 2xy \\) (notice \\( f(z) = z^2 = (x+iy)^2 = x^2 - y^2 + 2ixy \\)). [Lineage: Cauchy-Riemann Equations / Complex Analysis]",
      "بمعادلتي كوشي-ريمان: \\( v_y = 2x \\) و \\( v_x = 2y \\)، نجد أن المرافق التوافقي هو \\( 2xy \\). [المرجع: المرافق التوافقي في التحليل المركب]",
      "Use the Cauchy-Riemann equations \\( u_x = v_y \\) and \\( u_y = -v_x \\).", "طبق معادلتي كوشي-ريمان.")

    # 289: Improper Integral p-test
    q("KAUST-P2-289", "Calculus", "Easy",
      "For what values of \\( p \\) does the improper integral \\( \\int_0^1 \\dfrac{1}{x^p} \\, dx \\) converge?",
      "لأي قيم لـ \\( p \\) يتقارب التكامل المعتل \\( \\int_0^1 \\dfrac{1}{x^p} \\, dx \\)؟",
      ["\\( p < 1 \\)", "\\( p = 1 \\)", "\\( p > 1 \\)", "\\( p \\ge 2 \\)"], 0,
      "\\( \\int_0^1 x^{-p} dx = \\left[ \\dfrac{x^{1-p}}{1 - p} \\right]_0^1 \\). For the limit as \\( x \\to 0^+ \\) to be finite, we require the exponent \\( 1 - p > 0 \\implies p < 1 \\). [Lineage: Improper Integral Convergence]",
      "لكي تكون النهاية عند الصفر منتهية، يجب أن يكون الأس \\( 1 - p > 0 \\implies p < 1 \\). [المرجع: تقارب التكاملات المعتلة]",
      "Integrate \\( x^{-p} \\) and check the behavior at 0.", "كامل المقدار وتأكد من بقاء النهاية منتهية عند الصفر.")

    # 290: Washer Method
    q("KAUST-P2-290", "Calculus", "Easy",
      "The region bounded by \\( y = x \\) and \\( y = x^2 \\) is rotated about the \\( x \\)-axis. What is the volume of the resulting solid?",
      "دارت المنطقة المحصورة بين \\( y = x \\) و \\( y = x^2 \\) حول محور السينات. ما هو حجم المجسم الناتج؟",
      ["\\( \\dfrac{2\\pi}{15} \\)", "\\( \\dfrac{\\pi}{15} \\)", "\\( \\dfrac{\\pi}{5} \\)", "\\( \\dfrac{4\\pi}{15} \\)"], 0,
      "Intersection points are \\( x = 0 \\) and \\( x = 1 \\). Outer radius is \\( R(x) = x \\), inner radius is \\( r(x) = x^2 \\). \\( V = \\pi \\int_0^1 (x^2 - x^4) dx = \\pi \\left[ \\dfrac{x^3}{3} - \\dfrac{x^5}{5} \\right]_0^1 = \\pi \\left( \\dfrac{1}{3} - \\dfrac{1}{5} \\right) = \\dfrac{2\\pi}{15} \\). [Lineage: Washer Method / Calculus]",
      "بطريقة الحلقات: \\( V = \\pi \\int_0^1 (x^2 - x^4) dx = \\pi (1/3 - 1/5) = \\dfrac{2\\pi}{15} \\). [المرجع: حجوم الأجسام الدورانية]",
      "Use \\( V = \\pi \\int (R^2 - r^2) dx \\).", "اطرح مساحة الدائرة الداخلية من الخارجية وكامل.")

    # 291: Polar area of cardioid
    q("KAUST-P2-291", "Calculus", "Medium",
      "What is the total area enclosed by the cardioid \\( r = 1 + \\cos\\theta \\)?",
      "ما هي المساحة الكلية المحصورة داخل المنحنى القلبي \\( r = 1 + \\cos\\theta \\)؟",
      ["\\( \\pi \\)", "\\( \\dfrac{3\\pi}{2} \\)", "\\( 2\\pi \\)", "\\( 3\\pi \\)"], 1,
      "\\( A = \\dfrac{1}{2} \\int_0^{2\\pi} r^2 d\\theta = \\dfrac{1}{2} \\int_0^{2\\pi} (1 + 2\\cos\\theta + \\cos^2\\theta) d\\theta = \\dfrac{1}{2} \\left( 2\\pi + 0 + \\pi \\right) = \\dfrac{3\\pi}{2} \\). [Lineage: Polar Area / STEP I]",
      "المساحة في الإحداثيات القطبية: \\( A = \\dfrac{1}{2} \\int_0^{2\\pi} (1 + 2\\cos\\theta + \\cos^2\\theta) d\\theta = \\dfrac{3\\pi}{2} \\). [المرجع: المساحات بالصيغة القطبية]",
      "Use \\( A = \\frac{1}{2} \\int r^2 d\\theta \\).", "طبق قانون المساحة في الإحداثيات القطبية.")

    # 292: Radius of convergence
    q("KAUST-P2-292", "Calculus & Analysis", "Easy",
      "What is the radius of convergence of the power series \\( \\sum_{n=1}^{\\infty} \\dfrac{(x - 2)^n}{n \\cdot 3^n} \\)?",
      "ما هو نصف قطر تقارب متسلسلة القوى \\( \\sum_{n=1}^{\\infty} \\dfrac{(x - 2)^n}{n \\cdot 3^n} \\)؟",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( 3 \\)", "\\( \\infty \\)"], 2,
      "By the ratio test: \\( \\lim_{n \\to \\infty} \\left| \\dfrac{a_{n+1}}{a_n} \\right| = \\lim_{n \\to \\infty} \\dfrac{|x - 2|}{3} \\cdot \\dfrac{n}{n+1} = \\dfrac{|x - 2|}{3} < 1 \\implies |x - 2| < 3 \\). Radius of convergence is \\( R = 3 \\). [Lineage: Power Series Radius / Calculus]",
      "باختبار النسبة نجد \\( |x - 2|/3 < 1 \\implies |x - 2| < 3 \\)، إذن نصف قطر التقارب هو 3. [المرجع: نصف قطر التقارب لمتسلسلات القوى]",
      "Apply the ratio test to find \\( R \\).", "طبق اختبار النسبة.")

    # 293: Differential form d(omega)
    q("KAUST-P2-293", "Differential Forms", "Medium",
      "For the 1-form \\( \\omega = x^2 y \\, dx + x y^2 \\, dy \\), what is the exterior derivative \\( d\\omega \\)?",
      "للصورة التفاضلية \\( \\omega = x^2 y \\, dx + x y^2 \\, dy \\)، ما هي المشتقة الخارجية \\( d\\omega \\)؟",
      ["\\( (y^2 - x^2) \\, dx \\wedge dy \\)", "\\( (2xy) \\, dx \\wedge dy \\)", "\\( 0 \\)", "\\( (x^2 + y^2) \\, dx \\wedge dy \\)"], 0,
      "\\( d\\omega = d(x^2 y) \\wedge dx + d(x y^2) \\wedge dy = (2xy dx + x^2 dy) \\wedge dx + (y^2 dx + 2xy dy) \\wedge dy \\). Since \\( dx \\wedge dx = dy \\wedge dy = 0 \\) and \\( dy \\wedge dx = -dx \\wedge dy \\): \\( d\\omega = -x^2 dx \\wedge dy + y^2 dx \\wedge dy = (y^2 - x^2) dx \\wedge dy \\). [Lineage: Exterior Calculus / Differential Forms]",
      "باستخدام قواعد التفاضل الخارجي وخواص الضرب الوتدي: \\( d\\omega = (y^2 - x^2) dx \\wedge dy \\). [المرجع: الحساب التفاضلي الخارجي]",
      "Remember \\( dy \\wedge dx = -dx \\wedge dy \\) and \\( dx \\wedge dx = 0 \\).", "تذكر خاصية التخالف للضرب الوتدي.")

    # 294: Surface integral of vector field (Flux)
    q("KAUST-P2-294", "Multivariable Calculus", "Medium",
      "What is the outward flux of \\( \\mathbf{F} = \\langle x, y, z \\rangle \\) across the boundary of the unit cube \\( [0, 1]^3 \\)?",
      "ما هو التدفق الخارجي للمجال \\( \\mathbf{F} = \\langle x, y, z \\rangle \\) عبر حدود مكعب الوحدة \\( [0, 1]^3 \\)؟",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( 3 \\)", "\\( 6 \\)"], 2,
      "By the Divergence Theorem: \\( \\nabla \\cdot \\mathbf{F} = \\dfrac{\\partial x}{\\partial x} + \\dfrac{\\partial y}{\\partial y} + \\dfrac{\\partial z}{\\partial z} = 1 + 1 + 1 = 3 \\). The flux is \\( \\iiint_V 3 \\, dV = 3 \\times \\text{Volume}(V) = 3(1) = 3 \\). [Lineage: Divergence Theorem / MIT 18.02]",
      "بمبرهنة التباعد: التباعد يساوي \\( 1 + 1 + 1 = 3 \\). التدفق = \\( 3 \\times \\text{الحجم} = 3 \\times 1 = 3 \\). [المرجع: مبرهنة التباعد لغاوس]",
      "Compute \\( \\nabla \\cdot \\mathbf{F} \\) and multiply by volume.", "احسب تباعد المجال واضربه في حجم المكعب.")

    # 295: Line integral on circle
    q("KAUST-P2-295", "Multivariable Calculus", "Medium",
      "Evaluate the line integral \\( \\oint_C (-y \\, dx + x \\, dy) \\) along the circle \\( x^2 + y^2 = 4 \\) oriented counterclockwise.",
      "احسب قيمة التكامل الخطي \\( \\oint_C (-y \\, dx + x \\, dy) \\) على الدائرة \\( x^2 + y^2 = 4 \\) بالاتجاه الموجب.",
      ["\\( 4\\pi \\)", "\\( 8\\pi \\)", "\\( 16\\pi \\)", "\\( 0 \\)"], 1,
      "By Green's Theorem: \\( \\oint_C (-y dx + x dy) = \\iint_D (1 - (-1)) dA = 2 \\iint_D dA = 2 \\times \\text{Area}(D) \\). The circle has radius 2, so area is \\( \\pi(2^2) = 4\\pi \\). Thus the integral is \\( 2(4\\pi) = 8\\pi \\). [Lineage: Green's Theorem / AMC 12]",
      "بمبرهنة غرين: التكامل يساوي \\( 2 \\times \\text{المساحة} = 2 \\times 4\\pi = 8\\pi \\). [المرجع: مبرهنة غرين]",
      "Apply Green's Theorem: the integrand becomes \\( 2 dA \\).", "طبق مبرهنة غرين لتحويله إلى ضعف المساحة.")

    # 296: Level surface normal
    q("KAUST-P2-296", "Multivariable Calculus", "Easy",
      "Find a normal vector to the ellipsoid \\( x^2 + 2y^2 + 3z^2 = 6 \\) at the point \\( (1, 1, 1) \\).",
      "أوجد متجهاً عمودياً على السطح الناقصي \\( x^2 + 2y^2 + 3z^2 = 6 \\) عند النقطة \\( (1, 1, 1) \\).",
      ["\\( \\langle 1, 1, 1 \\rangle \\)", "\\( \\langle 2, 4, 6 \\rangle \\)", "\\( \\langle 1, 2, 3 \\rangle \\)", "\\( \\langle 2, 2, 2 \\rangle \\)"], 1,
      "The normal vector is given by the gradient: \\( \\nabla F = \\langle 2x, 4y, 6z \\rangle \\). At \\( (1, 1, 1) \\): \\( \\mathbf{n} = \\langle 2, 4, 6 \\rangle \\). [Lineage: Normal Vectors to Surfaces / Calculus III]",
      "المتجه العمودي هو تدرج الدالة: \\( \\nabla F(1, 1, 1) = \\langle 2, 4, 6 \\rangle \\). [المرجع: المتجهات العمودية على السطوح]",
      "Compute the gradient of \\( F(x, y, z) = x^2 + 2y^2 + 3z^2 - 6 \\).", "احسب تدرج دالة السطح.")

    # 297: Double integral triangle
    q("KAUST-P2-297", "Multivariable Calculus", "Medium",
      "Evaluate \\( \\iint_T xy \\, dA \\) where \\( T \\) is the triangle with vertices \\( (0, 0), (1, 0), (0, 1) \\).",
      "احسب قيمة \\( \\iint_T xy \\, dA \\) حيث \\( T \\) هو المثلث ذو الرؤوس \\( (0, 0), (1, 0), (0, 1) \\).",
      ["\\( \\dfrac{1}{24} \\)", "\\( \\dfrac{1}{12} \\)", "\\( \\dfrac{1}{6} \\)", "\\( \\dfrac{1}{4} \\)"], 0,
      "The region is \\( 0 \\le x \\le 1 \\), \\( 0 \\le y \\le 1 - x \\). \\( \\int_0^1 x \\left[ \\dfrac{y^2}{2} \\right]_0^{1-x} dx = \\dfrac{1}{2} \\int_0^1 x(1 - x)^2 dx = \\dfrac{1}{2} \\int_0^1 (x - 2x^2 + x^3) dx = \\dfrac{1}{2} \\left( \\dfrac{1}{2} - \\dfrac{2}{3} + \\dfrac{1}{4} \\right) = \\dfrac{1}{2} \\left( \\dfrac{1}{12} \\right) = \\dfrac{1}{24} \\). [Lineage: Double Integrals / STEP I]",
      "حدود التكامل: y من 0 إلى \\( 1-x \\). بحساب التكامل نجد \\( 1/24 \\). [المرجع: التكاملات الثنائية]",
      "Set limits \\( 0 \\le y \\le 1 - x \\) and integrate.", "حدد حدود التكامل وكامل بالنسبة لـ y ثم x.")

    # 298: Curvature of Parabola at Vertex
    q("KAUST-P2-298", "Differential Geometry", "Easy",
      "What is the curvature \\( \\kappa \\) of the parabola \\( y = x^2 \\) at its vertex \\( (0, 0) \\)?",
      "ما هو انحناء \\( \\kappa \\) القطع المكافئ \\( y = x^2 \\) عند رأسه \\( (0, 0) \\)؟",
      ["\\( 0 \\)", "\\( 1 \\)", "\\( 2 \\)", "\\( 4 \\)"], 2,
      "Curvature formula: \\( \\kappa = \\dfrac{|y''|}{(1 + (y')^2)^{3/2}} \\). Here \\( y' = 2x \\) and \\( y'' = 2 \\). At \\( x = 0 \\): \\( \\kappa = \\dfrac{2}{(1 + 0)^{3/2}} = 2 \\). [Lineage: Curvature of Curves / Calculus]",
      "صيغة الانحناء: \\( \\kappa = \\dfrac{|y''|}{(1 + (y')^2)^{3/2}} \\). عند \\( x = 0 \\) نجد \\( \\kappa = 2 \\). [المرجع: انحناء المنحنيات المستوية]",
      "Use \\( \\kappa = \\frac{|y''|}{(1 + (y')^2)^{3/2}} \\).", "عوض في قانون انحناء المنحنى عند الرأس.")

    # 299: Work Done by Force
    q("KAUST-P2-299", "Vector Calculus", "Easy",
      "Find the work done by the constant force \\( \\mathbf{F} = \\langle 2, 5 \\rangle \\) in moving an object along the straight line from \\( (0, 0) \\) to \\( (3, 4) \\).",
      "أوجد الشغل المبذول بواسطة القوة الثابتة \\( \\mathbf{F} = \\langle 2, 5 \\rangle \\) في تحريك جسم على خط مستقيم من \\( (0, 0) \\) إلى \\( (3, 4) \\).",
      ["\\( 20 \\)", "\\( 26 \\)", "\\( 30 \\)", "\\( 34 \\)"], 1,
      "Work is the dot product of force and displacement: \\( W = \\mathbf{F} \\cdot \\mathbf{d} = \\langle 2, 5 \\rangle \\cdot \\langle 3, 4 \\rangle = 2(3) + 5(4) = 6 + 20 = 26 \\). [Lineage: Work Line Integral / Physics Foundations]",
      "الشغل يساوي حاصل الضرب القياسي للقوة في الإزاحة: \\( 2(3) + 5(4) = 26 \\). [المرجع: الشغل الميكانيكي والتكاملات]",
      "Compute \\( \\mathbf{F} \\cdot \\mathbf{d} \\).", "احسب الضرب القياسي لمتجه القوة في الإزاحة.")

    # 300: Potential Function
    q("KAUST-P2-300", "Vector Calculus", "Medium",
      "Find the potential function \\( f(x, y) \\) for the conservative field \\( \\mathbf{F} = \\langle 2xy + 1, x^2 + 2y \\rangle \\) satisfying \\( f(0, 0) = 0 \\).",
      "أوجد دالة الجهد \\( f(x, y) \\) للمجال المحافظ \\( \\mathbf{F} = \\langle 2xy + 1, x^2 + 2y \\rangle \\) والتي تحقق \\( f(0, 0) = 0 \\).",
      ["\\( x^2 y + x + y^2 \\)", "\\( x^2 y^2 + x + y \\)", "\\( 2x^2 + 2y^2 \\)", "\\( xy + x + y \\)"], 0,
      "\\( f_x = 2xy + 1 \\implies f(x, y) = x^2 y + x + g(y) \\). Differentiating with respect to \\( y \\): \\( f_y = x^2 + g'(y) = x^2 + 2y \\implies g'(y) = 2y \\implies g(y) = y^2 + C \\). Setting \\( f(0, 0) = 0 \\implies C = 0 \\). Thus \\( f(x, y) = x^2 y + x + y^2 \\). [Lineage: Potential Functions / MIT 18.02]",
      "بمكاملة المركبة الأولى بالنسبة لـ x ثم مطابقتها مع المشتقة الجزئية بالنسبة لـ y نجد \\( f(x, y) = x^2 y + x + y^2 \\). [المرجع: دوال الجهد القياسية]",
      "Integrate \\( P \\) with respect to \\( x \\) and differentiate with respect to \\( y \\).", "كامل بالنسبة لـ x ثم اشتق بالنسبة لـ y لمطابقة المركبة الثانية.")

    return questions

if __name__ == "__main__":
    qs = get_p2_part_a()
    print(f"Generated {len(qs)} Phase 2 Part A questions (251-300).")
