#!/usr/bin/env python3
"""
KAUST Phase 3 Questions Part A: 251 to 300
Elite Research: Partial Differential Equations & Boundary Value Problems:
Heat equation, Wave equation, Laplace/Poisson equation, Method of Characteristics,
Burgers' equation, shock formation, weak formulations, Lax-Milgram theorem,
Green's functions for PDEs, Separation of variables in spherical/polar coordinates.
Authentic lineages: MIT 18.152 / 18.303, Cambridge Tripos Part II, Stanford Math 220, Princeton MAT 330.
"""

def get_p3_part_a():
    questions = []

    def q(qid, topic, diff, q_en, q_ar, options, corr_idx, exp_en, exp_ar, hint_en, hint_ar, diagram=None):
        item = {
            "id": qid,
            "track": "kaust",
            "level": "Phase 3: Elite Research",
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

    # 251: d'Alembert's Formula for 1D Wave Equation
    svg_wave = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-60 -40 120 80' width='100%' height='100%' style='background:#0d1117;'>
  <line x1='-55' y1='25' x2='55' y2='25' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-35' x2='0' y2='35' stroke='#8b949e' stroke-width='1.5'/>
  <!-- Right-traveling pulse -->
  <path d='M 10,25 Q 25,-15 40,25' fill='none' stroke='#58a6ff' stroke-width='2'/>
  <polygon points='38,5 45,5 40,-2' fill='#58a6ff'/>
  <!-- Left-traveling pulse -->
  <path d='M -40,25 Q -25,-15 -10,25' fill='none' stroke='#f0883e' stroke-width='2'/>
  <polygon points='-38,5 -45,5 -40,-2' fill='#f0883e'/>
  <text x='15' y='-20' fill='#58a6ff' font-size='9' font-family='sans-serif'>+ct</text>
  <text x='-35' y='-20' fill='#f0883e' font-size='9' font-family='sans-serif'>-ct</text>
</svg>"""
    q("KAUST-P3-251", "Partial Differential Equations", "Hard",
      "Using d'Alembert's formula, solve the Cauchy problem for the 1D wave equation \\(u_{tt} = 4 u_{xx}\\) for \\(-\\infty < x < \\infty, t > 0\\) with initial displacement \\(u(x, 0) = \\sin x\\) and initial velocity \\(u_t(x, 0) = 0\\). What is \\(u(\\pi/2, \\pi/4)\\)?",
      "باستخدام صيغة دالمبير، حل مسألة كوشي لمعادلة الموجة أحادية البعد \\(u_{tt} = 4 u_{xx}\\) مع الإزاحة الابتدائية \\(u(x, 0) = \\sin x\\) والسرعة الابتدائية \\(u_t(x, 0) = 0\\). ما قيمة \\(u(\\pi/2, \\pi/4)\\)؟",
      ["\\(0\\)", "\\(1\\)", "\\(1/2\\)", "\\(-1\\)"],
      0,
      "The wave speed is \\(c = \\sqrt{4} = 2\\). By d'Alembert's formula with zero initial velocity \\(\\psi(x) = 0\\): \\(u(x, t) = \\frac{1}{2}[\\phi(x - ct) + \\phi(x + ct)] = \\frac{1}{2}[\\sin(x - 2t) + \\sin(x + 2t)] = \\sin x \\cos(2t)\\). Evaluating at \\(x = \\pi/2\\) and \\(t = \\pi/4\\): \\(u(\\pi/2, \\pi/4) = \\sin(\\pi/2) \\cos(2(\\pi/4)) = (1) \\cos(\\pi/2) = 0\\).",
      "سرعة الموجة هي \\(c = \\sqrt{4} = 2\\). حسب صيغة دالمبير مع سرعة ابتدائية منعدمة: \\(u(x, t) = \\frac{1}{2}[\\sin(x-2t) + \\sin(x+2t)] = \\sin x \\cos(2t)\\). بالتعويض عند \\(x = \\pi/2\\) و \\(t = \\pi/4\\) نجد: \\(u = \\sin(\\pi/2)\\cos(\\pi/2) = 1 \\times 0 = 0\\).",
      "Use d'Alembert's solution \\(u(x, t) = \\frac{1}{2}[\\phi(x-ct) + \\phi(x+ct)]\\) with \\(c = 2\\).",
      "استخدم صيغة دالمبير مع سرعة الموجة \\(c = 2\\).",
      diagram=svg_wave)

    # 252: Heat Kernel (Fundamental Solution)
    q("KAUST-P3-252", "Partial Differential Equations", "Hard",
      "What is the fundamental solution (heat kernel) \\(\\Phi(x, t)\\) of the 1D heat equation \\(u_t = D u_{xx}\\) for \\(t > 0\\)?",
      "ما هو الحل الأساسي (نواة الحرارة) \\(\\Phi(x, t)\\) لمعادلة الحرارة أحادية البعد \\(u_t = D u_{xx}\\) لـ \\(t > 0\\)؟",
      ["\\(\\Phi(x, t) = \\frac{1}{\\sqrt{4\\pi D t}} \\exp\\left(-\\frac{x^2}{4Dt}\\right)\\)",
       "\\(\\Phi(x, t) = \\frac{1}{2\\pi D t} \\exp\\left(-\\frac{x^2}{2Dt}\\right)\\)",
       "\\(\\Phi(x, t) = \\frac{1}{\\sqrt{2\\pi D t}} \\exp\\left(-\\frac{x^2}{Dt}\\right)\\)",
       "\\(\\Phi(x, t) = \\frac{1}{4\\pi D t^2} \\exp\\left(-\\frac{x}{4Dt}\\right)\\)"],
      0,
      "The fundamental solution of the diffusion equation \\(u_t = D u_{xx}\\) corresponds to the temperature profile resulting from an initial Dirac delta heat source at the origin \\(u(x, 0) = \\delta(x)\\). By Fourier transform in \\(x\\): \\(\\hat{u}_t = -D k^2 \\hat{u} \\implies \\hat{u}(k, t) = e^{-D k^2 t}\\). Taking the inverse Fourier transform yields the Gaussian distribution \\(\\Phi(x, t) = \\frac{1}{\\sqrt{4\\pi D t}} e^{-\\frac{x^2}{4Dt}}\\).",
      "الحل الأساسي لمعادلة الانتشار هو التوزيع الغاوسي الناتج عن نبضة حرارية ابتدائية مركزة عند نقطة الأصل. باستخدام تحويل فورييه بالنسبة للموضع نجد \\(\\hat{u}(k, t) = e^{-Dk^2 t}\\)، وبالتحويل العكسي نحصل على نواة الحرارة القياسية.",
      "The heat kernel is a normalized Gaussian whose variance grows linearly with time as \\(2Dt\\).",
      "نواة الحرارة هي توزيع غاوسي معياري ينمو تباينه خطياً مع الزمن بمقدار \\(2Dt\\).")

    # 253: Maximum Principle for Harmonic Functions
    q("KAUST-P3-253", "Partial Differential Equations", "Medium",
      "Let \\(u(x, y)\\) be harmonic on a bounded open domain \\(\\Omega \\subset \\mathbb{R}^2\\) and continuous on \\(\\bar{\\Omega}\\). If \\(u(x, y) = 3x - 4y\\) on the boundary \\(\\partial \\Omega\\), where \\(\\Omega\\) is the disc \\(x^2 + y^2 < 1\\), what is the maximum value of \\(u\\) on \\(\\bar{\\Omega}\\)?",
      "لتكن \\(u(x, y)\\) دالة توافقية على النطاق المحدود \\(\\Omega\\) ومتصلة على غلاقه. إذا كانت \\(u(x, y) = 3x - 4y\\) على الحدود \\(\\partial \\Omega\\) لقرص الوحدة \\(x^2 + y^2 < 1\\)، فما هي القيمة العظمى لـ \\(u\\) على النطاق المغلق؟",
      ["\\(5\\)", "\\(7\\)", "\\(1\\)", "\\(25\\)"],
      0,
      "By the Strong Maximum Principle for elliptic PDEs, the maximum of any non-constant harmonic function must be achieved strictly on the boundary \\(\\partial \\Omega\\). On the boundary circle \\(x^2 + y^2 = 1\\), we maximize the linear function \\(3x - 4y\\). By Cauchy-Schwarz: \\(3x - 4y \\le \\sqrt{3^2 + (-4)^2}\\sqrt{x^2 + y^2} = \\sqrt{25}(1) = 5\\). Equality is achieved at \\((x, y) = (3/5, -4/5) \\in \\partial \\Omega\\). Thus the maximum is \\(5\\).",
      "حسب مبدأ النهاية العظمى للدوال التوافقية، تقع القيمة العظمى حتماً على المحيط الحدودي \\(\\partial \\Omega\\). على محيط دائرة الوحدة، نوجد النهاية العظمى للمقدار الخطي \\(3x - 4y\\) بمتراجحة كوشي-شفارتز: \\(\\sqrt{3^2 + (-4)^2} = 5\\). إذن القيمة العظمى هي 5.",
      "By the maximum principle, maximize \\(3x - 4y\\) on the circle \\(x^2 + y^2 = 1\\).",
      "بمبدأ النهاية العظمى، ابحث عن النهاية العظمى على محيط الدائرة.")

    # 254: Method of Characteristics (Quasilinear PDE)
    q("KAUST-P3-254", "Partial Differential Equations", "Hard",
      "Solve the initial value problem \\(u_t + u u_x = 0\\) with initial data \\(u(x, 0) = 2x\\). For what time \\(t\\) does the solution blow up or become multivalued?",
      "حل مسألة القيمة الابتدائية لمعادلة بيرغرز غير اللزجة \\(u_t + u u_x = 0\\) مع الشرط الابتدائي \\(u(x, 0) = 2x\\). عند أي زمن \\(t\\) تنفجر الدالة أو تصبح متعددة القيم؟",
      ["\\(t = -1/2\\) (so no shock forms for \\(t > 0\\); expansion wave)",
       "\\(t = 1/2\\)",
       "\\(t = 2\\)",
       "\\(t = 1\\)"],
      0,
      "The characteristic equations are \\(\\frac{dt}{ds} = 1\\), \\(\\frac{du}{ds} = 0\\), \\(\\frac{dx}{ds} = u\\). Along a characteristic starting at \\(x_0\\), \\(u = u(x_0, 0) = 2x_0\\) is constant. The characteristic curve is \\(x(t) = x_0 + u(x_0) t = x_0 + 2x_0 t = x_0(1 + 2t)\\). Solving for \\(x_0\\): \\(x_0 = \\frac{x}{1 + 2t}\\). Thus \\(u(x, t) = 2x_0 = \\frac{2x}{1 + 2t}\\). The derivative \\(u_x = \\frac{2}{1 + 2t}\\) blows up when \\(1 + 2t = 0 \\implies t = -1/2\\). For \\(t > 0\\), the characteristics diverge (expansion / rarefaction), so no shock wave forms in forward time.",
      "معادلات الخصائص تعطي \\(x = x_0(1+2t)\\) و \\(u = 2x_0\\). بالحل بالنسبة لـ \\(x_0\\) نجد \\(u(x, t) = \\frac{2x}{1+2t}\\). ينعدم المقام عند \\(t = -1/2\\). بالنسبة للزمن الموجب \\(t > 0\\)، تتباعد مسارات الخصائص (موجة تخلخل) ولا تتشكل أي صدمة في الزمن الموجب.",
      "Determine \\(x(t) = x_0 + u(x_0)t\\) and express \\(x_0\\) in terms of \\(x\\) and \\(t\\).",
      "أوجد مسار الخاصية بدلالة النقطة الابتدائية وعبر عن الحل.")

    # 255: Shock Speed via Rankine-Hugoniot Condition
    q("KAUST-P3-255", "Partial Differential Equations", "Hard",
      "For the conservation law \\(u_t + \\left(\\frac{u^2}{2}\\right)_x = 0\\), consider the Riemann problem with initial data \\(u(x, 0) = 4\\) for \\(x < 0\\) and \\(u(x, 0) = 2\\) for \\(x > 0\\). By the Rankine-Hugoniot jump condition, what is the speed \\(s\\) of the shock wave?",
      "لقانون الانحفاظ \\(u_t + (u^2/2)_x = 0\\)، تأمل مسألة ريمان مع الشرط الابتدائي \\(u(x, 0) = 4\\) لـ \\(x < 0\\) و \\(u(x, 0) = 2\\) لـ \\(x > 0\\). باستخدام شرط قفزة رانكين-هوغونيوت، ما هي سرعة موجة الصدمة \\(s\\)؟",
      ["\\(s = 3\\)", "\\(s = 6\\)", "\\(s = 2\\)", "\\(s = 4\\)"],
      0,
      "The flux function is \\(F(u) = \\frac{u^2}{2}\\). The Rankine-Hugoniot condition for the shock speed \\(s\\) is \\(s = \\frac{F(u_L) - F(u_R)}{u_L - u_R}\\). Here \\(u_L = 4\\) and \\(u_R = 2\\). Then \\(F(u_L) = \\frac{4^2}{2} = 8\\) and \\(F(u_R) = \\frac{2^2}{2} = 2\\). Thus \\(s = \\frac{8 - 2}{4 - 2} = \\frac{6}{2} = 3\\). Note that \\(u_L = 4 > s = 3 > u_R = 2\\), which satisfies the Lax entropy condition for a stable shock.",
      "دالة التدفق هي \\(F(u) = u^2/2\\). شرط رانكين-هوغونيوت لسرعة الصدمة هو \\(s = \\frac{F(u_L) - F(u_R)}{u_L - u_R}\\). بالتعويض عن \\(u_L = 4\\) و \\(u_R = 2\\): \\(s = \\frac{8 - 2}{4 - 2} = \\frac{6}{2} = 3\\).",
      "Use the Rankine-Hugoniot condition \\(s = \\frac{[F(u)]}{[u]}\\).",
      "طبق شرط رانكين-هوغونيوت لنسبة قفزة التدفق إلى قفزة الحالة.")

    # 256: Poisson Equation Fundamental Solution in 2D vs 3D
    q("KAUST-P3-256", "Partial Differential Equations", "Medium",
      "What is the fundamental solution \\(\\Phi(\\mathbf{x})\\) of Laplace's equation in \\(\\mathbb{R}^2\\) satisfying \\(-\\Delta \\Phi = \\delta(\\mathbf{x})\\)?",
      "ما هو الحل الأساسي \\(\\Phi(\\mathbf{x})\\) لمعادلة لابلاس في \\(\\mathbb{R}^2\\) الذي يحقق \\(-\\Delta \\Phi = \\delta(\\mathbf{x})\\)؟",
      ["\\(\\Phi(\\mathbf{x}) = -\\frac{1}{2\\pi} \\ln|\\mathbf{x}|\\)",
       "\\(\\Phi(\\mathbf{x}) = \\frac{1}{4\\pi |\\mathbf{x}|}\\)",
       "\\(\\Phi(\\mathbf{x}) = -\\frac{1}{4\\pi} |\\mathbf{x}|^2\\)",
       "\\(\\Phi(\\mathbf{x}) = \\frac{1}{2\\pi |\\mathbf{x}|}\\)"],
      0,
      "In \\(\\mathbb{R}^n\\), the fundamental solution of \\(-\\Delta \\Phi = \\delta\\) has radial symmetry \\(\\Phi(r)\\). In 2D: \\(-\\frac{1}{r}\\frac{d}{dr}\\left(r \\frac{d\\Phi}{dr}\\right) = 0 \\implies r \\frac{d\\Phi}{dr} = C \\implies \\Phi(r) = C \\ln r\\). Integrating over a small disc and applying Gauss's divergence theorem: \\(-\\int_{\\partial B_r} \\nabla \\Phi \\cdot \\mathbf{n} dS = -C (1/r)(2\\pi r) = -2\\pi C = 1 \\implies C = -\\frac{1}{2\\pi}\\). Thus \\(\\Phi(\\mathbf{x}) = -\\frac{1}{2\\pi}\\ln|\\mathbf{x}|\\). (In 3D, it is \\(\\frac{1}{4\\pi |\\mathbf{x}|}\\)).",
      "في \\(\\mathbb{R}^2\\)، بالتماثل القطري نجد \\(\\Phi(r) = C \\ln r\\). بتطبيق مبرهنة التباعد على قرص صغير لحساب الشحنة النقطية نجد \\(-2\\pi C = 1 \\implies C = -1/(2\\pi)\\). بالتالي فإن الحل الأساسي في بعدين هو \\(-\\frac{1}{2\\pi}\\ln|\\mathbf{x}|\\).",
      "Recall that the 2D Green's function for the Laplacian involves a logarithm, while 3D involves \\(1/r\\).",
      "تذكر أن دالة غرين للابلاسي في بعدين تحوي لوغاريتم المسافة، بينما في ثلاثة أبعاد تحوي مقلوب المسافة.")

    # 257: Separation of Variables in Cylindrical Coordinates
    q("KAUST-P3-257", "Partial Differential Equations", "Hard",
      "When solving Laplace's equation \\(\\Delta u = 0\\) on a circular cylinder in cylindrical coordinates \\((r, \\theta, z)\\) with no \\(\\theta\\)-dependence, separation of variables \\(u(r, z) = R(r)Z(z)\\) with \\(Z''(z) = -k^2 Z(z)\\) leads to which ODE for \\(R(r)\\)?",
      "عند حل معادلة لابلاس على أسطوانة دائرية بدون اعتماد على الزاوية \\(\\theta\\)، يؤدي فصل المتغيرات \\(u = R(r)Z(z)\\) مع \\(Z'' = -k^2 Z\\) إلى أي معادلة تفاضلية لـ \\(R(r)\\)؟",
      ["\\(r^2 R'' + r R' - k^2 r^2 R = 0\\) (Modified Bessel equation of order 0)",
       "\\(r^2 R'' + r R' + k^2 r^2 R = 0\\) (Bessel equation of order 0)",
       "\\(R'' + k^2 R = 0\\) (Harmonic oscillator)",
       "\\(r R'' + 2 R' - k^2 R = 0\\) (Euler-Cauchy equation)"],
      0,
      "The Laplacian in axisymmetric cylindrical coordinates is \\(\\Delta u = u_{rr} + \\frac{1}{r}u_r + u_{zz} = 0\\). Substituting \\(u = R(r)Z(z)\\): \\(R'' Z + \\frac{1}{r}R' Z + R Z'' = 0\\). Divide by \\(RZ\\): \\(\\frac{R'' + \\frac{1}{r}R'}{R} = -\\frac{Z''}{Z}\\). Setting \\(Z''/Z = -k^2\\) (so \\(Z(z) = \\sin(kz)\\) or \\(\\cos(kz)\\)) gives \\(\\frac{R'' + \\frac{1}{r}R'}{R} = k^2 \\implies R'' + \\frac{1}{r}R' - k^2 R = 0\\). Multiplying by \\(r^2\\) yields \\(r^2 R'' + r R' - k^2 r^2 R = 0\\), which is precisely the modified Bessel equation of order 0, whose bounded solution at \\(r=0\\) is \\(I_0(kr)\\).",
      "المؤثر التفاضلي في الإحداثيات الأسطوانية يعطي \\(\\frac{R'' + \\frac{1}{r}R'}{R} = -\\frac{Z''}{Z} = k^2\\). بضرب المعادلة في \\(r^2\\) نحصل على \\(r^2 R'' + r R' - k^2 r^2 R = 0\\)، وهي معادلة بيسل المعدلة من الرتبة صفر.",
      "Notice the minus sign in front of \\(k^2 r^2\\) resulting from \\(-Z''/Z = k^2\\).",
      "لاحظ إشارة السالب أمام \\(k^2 r^2\\) الناتجة عن إشارة الحد المشتق الثاني لـ \\(Z\\).")

    # 258: Lax-Milgram Theorem
    q("KAUST-P3-258", "Functional Analysis", "Hard",
      "The Lax-Milgram theorem guarantees the existence and uniqueness of a weak solution to an elliptic boundary value problem. For a real Hilbert space \\(H\\) and a bilinear form \\(a(u, v)\\), what are the two required conditions on \\(a\\)?",
      "تضمن نظرية لاكس-ميلغرام وجود ووحدانية الحل الضعيف لمسائل القيمة الحدية الإهليلجية على فضاء هيلبرت \\(H\\) مع شكل ثنائي الخطية \\(a(u, v)\\). ما هما الشرطان الأساسيان على \\(a\\)؟",
      ["Boundedness (continuity) and Coercivity (ellipticity)",
       "Symmetry and Compactness",
       "Positivity and Translatability",
       "Self-adjointness and Nilpotency"],
      0,
      "The Lax-Milgram Theorem requires the bilinear form \\(a: H \\times H \\to \\mathbb{R}\\) to be: 1) Bounded (continuous): \\(|a(u, v)| \\le C \\|u\\|_H \\|v\\|_H\\) for some constant \\(C > 0\\); and 2) Coercive (strictly positive/elliptic): \\(a(u, u) \\ge \\alpha \\|u\\|_H^2\\) for some constant \\(\\alpha > 0\\). Under these two hypotheses, for any bounded linear functional \\(L \\in H^*\\), there exists a unique \\(u \\in H\\) such that \\(a(u, v) = L(v)\\) for all \\(v \\in H\\).",
      "تتطلب مبرهنة لاكس-ميلغرام شرطين: 1) المحدودية (الاتصال): \\(|a(u, v)| \\le C \\|u\\| \\|v\\|\\)، و 2) الإكراهية (الرمز الإهليلجي): \\(a(u, u) \\ge \\alpha \\|u\\|^2\\) بثابت \\(\\alpha > 0\\). هذان الشرطان يضمنان وجود ووحدانية الحل الضعيف.",
      "Recall the two core estimates: \\(|a(u,v)| \\le C\\|u\\|\\|v\\|\\) and \\(a(u,u) \\ge \\alpha\\|u\\|^2\\).",
      "تذكر التقديرين الأساسيين: الاستمرار والإكراهية.")

    # 259: Energy Conservation in Wave Equation
    q("KAUST-P3-259", "Partial Differential Equations", "Medium",
      "For the wave equation \\(u_{tt} = c^2 u_{xx}\\) on the whole line with compactly supported initial data, the total energy is \\(E(t) = \\frac{1}{2}\\int_{-\\infty}^\\infty (u_t^2 + c^2 u_x^2) dx\\). What is \\(\\frac{dE}{dt}\\)?",
      "لمعادلة الموجة \\(u_{tt} = c^2 u_{xx}\\) مع شروط ابتدائية ذات حامل مدمج، الطاقة الكلية هي \\(E(t) = \\frac{1}{2}\\int (u_t^2 + c^2 u_x^2) dx\\). ما قيمة \\(\\frac{dE}{dt}\\)؟",
      ["\\(0\\) (Energy is conserved)", "\\(c^2 E(t)\\)", "\\(-E(t)\\)", "\\(\\int u_t^2 dx\\)"],
      0,
      "Differentiate inside the integral: \\(\\frac{dE}{dt} = \\int_{-\\infty}^\\infty (u_t u_{tt} + c^2 u_x u_{xt}) dx\\). Substitute \\(u_{tt} = c^2 u_{xx}\\): \\(\\frac{dE}{dt} = \\int_{-\\infty}^\\infty (c^2 u_t u_{xx} + c^2 u_x u_{xt}) dx = c^2 \\int_{-\\infty}^\\infty \\frac{\\partial}{\\partial x}(u_t u_x) dx = c^2 [u_t u_x]_{-\\infty}^\\infty\\). Since the initial data has compact support, the disturbance has finite propagation speed \\(c\\), so \\(u_t\\) and \\(u_x\\) vanish at \\(\\pm\\infty\\). Thus \\(dE/dt = 0\\), establishing total energy conservation.",
      "باشتقاق الطاقة تحت إشارة التكامل واستبدال \\(u_{tt} = c^2 u_{xx}\\) نحصل على تكامل المشتق التام: \\(c^2 \\int \\frac{\\partial}{\\partial x}(u_t u_x) dx = 0\\) بفضل انعدام الموجة في اللانهاية. وبالتالي فإن الطاقة محفوظة وثابتة مع الزمن.",
      "Differentiate under the integral sign and integrate by parts.",
      "فاضل تحت إشارة التكامل وكامل بالتجزئة.")

    # 260: Heat Equation Backward in Time (Ill-posedness)
    q("KAUST-P3-260", "Partial Differential Equations", "Medium",
      "Why is the backward heat equation \\(u_t = -u_{xx}\\) considered severely ill-posed in the sense of Hadamard?",
      "لماذا تعتبر معادلة الحرارة العكسية في الزمن \\(u_t = -u_{xx}\\) مسألة غير منضبطة بشدة (ill-posed) بمفهوم هادامارد؟",
      ["Solutions do not depend continuously on the initial data (arbitrarily small high-frequency perturbations grow exponentially without bound)",
       "No solutions exist for any initial condition",
       "The maximum principle is violated",
       "The spatial derivative cannot be defined"],
      0,
      "Consider the initial data \\(u_n(x, 0) = \\frac{1}{n}\\sin(nx)\\). For the backward heat equation, the Fourier mode evolves as \\(u_n(x, t) = \\frac{1}{n}\\sin(nx) e^{n^2 t}\\). As \\(n \\to \\infty\\), the initial condition vanishes uniformly: \\(\\sup_x |u_n(x, 0)| = 1/n \\to 0\\). However, for any \\(t > 0\\), the solution \\(u_n(x, t) \\to \\infty\\) explosively due to \\(e^{n^2 t}/n\\). Thus, a tiny perturbation creates an infinite change in arbitrarily short time, destroying continuous dependence on data.",
      "تتطور الترددات العالية \\(\\sin(nx)\\) وفق العامل الأسي المتفجر \\(e^{n^2 t}\\). عندما \\(n \\to \\infty\\)، يقترب الاضطراب الابتدائي من الصفر بينما ينفجر الحل إلى اللانهاية عند أي زمن موجب. هذا يدمر شرط هادامارد للاعتماد المستمر على الشروط الابتدائية.",
      "Look at the Fourier multiplier \\(e^{n^2 t}\\) for high frequencies.",
      "انظر إلى العامل الأسي للترددات العالية.")

    # 261 to 300: Continue generating remaining 40 questions for Part A
    # 261: Spherical Harmonics & Legendre Polynomials
    q("KAUST-P3-261", "Partial Differential Equations", "Hard",
      "When solving Laplace's equation in spherical coordinates \\((r, \\theta, \\phi)\\) with azimuthal symmetry (no \\(\\phi\\) dependence), the radial solutions are \\(r^l\\) and \\(r^{-(l+1)}\\). What are the angular solutions in terms of \\(x = \\cos\\theta\\)?",
      "عند حل معادلة لابلاس بالإحداثيات الكروية بتناظر سمتي، تكون الحلول القطرية هي \\(r^l\\) و \\(r^{-(l+1)}\\). ما هي الحلول الزاوية بدلالة \\(x = \\cos\\theta\\)؟",
      ["Legendre polynomials \\(P_l(\\cos\\theta)\\)",
       "Chebyshev polynomials \\(T_l(\\cos\\theta)\\)",
       "Hermite polynomials \\(H_l(\\cos\\theta)\\)",
       "Laguerre polynomials \\(L_l(\\cos\\theta)\\)"],
      0,
      "The angular equation for azimuthal symmetry is \\(\\frac{1}{\\sin\\theta}\\frac{d}{d\\theta}\\left(\\sin\\theta \\frac{d\\Theta}{d\\theta}\\right) + l(l+1)\\Theta = 0\\). Substituting \\(x = \\cos\\theta\\) transforms this into Legendre's differential equation \\((1-x^2)y'' - 2x y' + l(l+1)y = 0\\). For \\(l\\) an integer, the bounded solutions on \\([-1, 1]\\) (from the North to South poles) are precisely the Legendre polynomials \\(P_l(x) = P_l(\\cos\\theta)\\).",
      "المعادلة الزاوية بعد التعويض \\(x = \\cos\\theta\\) تتحول إلى معادلة ليجاندر التفاضلية \\((1-x^2)y'' - 2xy' + l(l+1)y = 0\\). الحلول المنتظمة والمحدودة على المجال \\([-1, 1]\\) هي حصراً كثيرات حدود ليجاندر \\(P_l(\\cos\\theta)\\).",
      "Substitute \\(x = \\cos\\theta\\) into the spherical angular equation.",
      "عوض بـ \\(x = \\cos\\theta\\) في المعادلة التفاضلية الزاوية.")

    # 262: Wave Equation Domain of Dependence
    q("KAUST-P3-262", "Partial Differential Equations", "Medium",
      "For the 1D wave equation \\(u_{tt} = c^2 u_{xx}\\), what is the domain of dependence of a point \\((x_0, t_0)\\) with \\(t_0 > 0\\) on the initial line \\(t = 0\\)?",
      "لمعادلة الموجة أحادية البعد \\(u_{tt} = c^2 u_{xx}\\)، ما هو نطاق الاعتماد (domain of dependence) لنقطة \\((x_0, t_0)\\) على خط البداية \\(t = 0\\)؟",
      ["The closed interval \\([x_0 - ct_0, x_0 + ct_0]\\)",
       "The entire real line \\((-\\infty, \\infty)\\)",
       "Only the two discrete endpoints \\(x_0 - ct_0\\) and \\(x_0 + ct_0\\)",
       "The interval \\([x_0 - t_0/c, x_0 + t_0/c]\\)"],
      0,
      "From d'Alembert's formula \\(u(x_0, t_0) = \\frac{\\phi(x_0-ct_0) + \\phi(x_0+ct_0)}{2} + \\frac{1}{2c}\\int_{x_0-ct_0}^{x_0+ct_0} \\psi(s) ds\\), the value of \\(u\\) at \\((x_0, t_0)\\) depends only on the initial values \\(\\phi\\) and \\(\\psi\\) within the interval \\([x_0 - ct_0, x_0 + ct_0]\\). Any change in the initial data outside this interval has zero influence on \\(u(x_0, t_0)\\).",
      "من صيغة دالمبير، تتحدد قيمة الدالة عند \\((x_0, t_0)\\) حصراً بقيم الدالتين الابتدائيتين داخل الفترة \\([x_0 - ct_0, x_0 + ct_0]\\). أي تغير خارج هذه الفترة لا يؤثر إطلاقاً على الحل عند تلك النقطة.",
      "Look at the limits of integration in d'Alembert's formula.",
      "انظر إلى حدود التكامل في صيغة دالمبير.")

    # 263: Mean Value Property of Harmonic Functions
    q("KAUST-P3-263", "Partial Differential Equations", "Medium",
      "Let \\(u\\) be a harmonic function on \\(\\mathbb{R}^3\\). If the average value of \\(u\\) on the sphere of radius \\(R = 2\\) centered at \\((1, 2, 3)\\) is \\(10\\), what is \\(u(1, 2, 3)\\)?",
      "لتكن \\(u\\) دالة توافقية على \\(\\mathbb{R}^3\\). إذا كان متوسط قيمة \\(u\\) على سطح الكرة ذات نصف القطر 2 والمركز \\((1, 2, 3)\\) هو 10، فما هي قيمة \\(u(1, 2, 3)\\)؟",
      ["\\(10\\)", "\\(5\\)", "\\(20\\)", "\\(0\\)"],
      0,
      "By Gauss's Mean Value Property for harmonic functions, if \\(\\Delta u = 0\\), the value of \\(u\\) at the center of any ball equals the average value of \\(u\\) over the boundary sphere (as well as over the solid ball): \\(u(\\mathbf{x}_0) = \\frac{1}{4\\pi R^2} \\iint_{\\partial B_R(\\mathbf{x}_0)} u dS\\). Therefore, \\(u(1, 2, 3) = 10\\).",
      "حسب مبرهنة القيمة المتوسطة لغاوس للدوال التوافقية، فإن قيمة الدالة عند مركز أي كرة تساوي تماماً متوسط قيمتها على سطح تلك الكرة. بالتالي \\(u(1, 2, 3) = 10\\).",
      "Apply the Mean Value Theorem for harmonic functions.",
      "طبق مبرهنة القيمة المتوسطة للدوال التوافقية.")

    # 264: Elliptic, Parabolic, Hyperbolic Classification
    q("KAUST-P3-264", "Partial Differential Equations", "Medium",
      "Classify the second-order PDE \\(x u_{xx} + 2x u_{xy} + y u_{yy} = 0\\) in the region \\(x > 0, y > x\\).",
      "صنف المعادلة التفاضلية الجزئية من الرتبة الثانية \\(x u_{xx} + 2x u_{xy} + y u_{yy} = 0\\) في المنطقة \\(x > 0, y > x\\).",
      ["Hyperbolic if \\(x > y\\), Parabolic if \\(x = y\\), Elliptic if \\(y > x\\)",
       "Elliptic everywhere",
       "Parabolic everywhere",
       "Hyperbolic everywhere"],
      0,
      "The coefficients are \\(A = x\\), \\(B = 2x\\), \\(C = y\\). The discriminant is \\(\\Delta = B^2 - 4AC = (2x)^2 - 4(x)(y) = 4x^2 - 4xy = 4x(x - y)\\). For \\(x > 0\\): if \\(y > x\\), then \\(x - y < 0\\), so \\(\\Delta < 0\\) (Elliptic); if \\(x = y\\), \\(\\Delta = 0\\) (Parabolic); if \\(x > y\\), \\(\\Delta > 0\\) (Hyperbolic).",
      "المعاملات هي \\(A = x\\), \\(B = 2x\\), \\(C = y\\). المميز هو \\(B^2 - 4AC = 4x^2 - 4xy = 4x(x-y)\\). بما أن \\(x > 0\\): عندما \\(y > x\\) يكون المميز سالباً (إهليلجية)، وعند \\(x = y\\) ينعدم (مكافئة)، وعند \\(x > y\\) يكون موجباً (زائدية).",
      "Evaluate the discriminant \\(B^2 - 4AC\\).",
      "احسب مميز المعادلة التفاضلية الجزئية \\(B^2 - 4AC\\).")

    # 265: Telegrapher's Equation
    q("KAUST-P3-265", "Partial Differential Equations", "Hard",
      "The Telegrapher's equation for voltage in a transmission line is \\(u_{tt} + 2\\alpha u_t + \\alpha^2 u = c^2 u_{xx}\\). Using the transformation \\(u(x, t) = e^{-\\alpha t} v(x, t)\\), what equation does \\(v(x, t)\\) satisfy?",
      "معادلة التلغراف للجهد في خط نقل هي \\(u_{tt} + 2\\alpha u_t + \\alpha^2 u = c^2 u_{xx}\\). باستخدام التحويل \\(u(x, t) = e^{-\\alpha t} v(x, t)\\)، ما المعادلة التي تحققها \\(v(x, t)\\)؟",
      ["The standard wave equation \\(v_{tt} = c^2 v_{xx}\\)",
       "The heat equation \\(v_t = c^2 v_{xx}\\)",
       "The Klein-Gordon equation \\(v_{tt} - c^2 v_{xx} + \\alpha^2 v = 0\\)",
       "Laplace's equation \\(v_{tt} + c^2 v_{xx} = 0\\)"],
      0,
      "Notice the left side can be written as \\((\\partial_t + \\alpha)^2 u = c^2 u_{xx}\\). Differentiating \\(u = e^{-\\alpha t} v\\): \\(u_t = e^{-\\alpha t}(v_t - \\alpha v)\\), so \\((\\partial_t + \\alpha)u = e^{-\\alpha t} v_t\\). Applying \\((\\partial_t + \\alpha)\\) again gives \\((\\partial_t + \\alpha)^2 u = e^{-\\alpha t} v_{tt}\\). Since \\(u_{xx} = e^{-\\alpha t} v_{xx}\\), the equation becomes \\(e^{-\\alpha t} v_{tt} = c^2 e^{-\\alpha t} v_{xx} \\implies v_{tt} = c^2 v_{xx}\\), which is the standard undamped wave equation.",
      "يمكن كتابة الطرف الأيسر كمؤثر مركب: \\((\\partial_t + \\alpha)^2 u = c^2 u_{xx}\\). بالتعويض عن \\(u = e^{-\\alpha t}v\\) نجد \\((\\partial_t + \\alpha)u = e^{-\\alpha t}v_t\\)، وبتكرار الاشتقاق نحصل على \\(e^{-\\alpha t}v_{tt}\\). باختصار العامل الأسي نحصل على معادلة الموجة القياسية غير المخمدة.",
      "Factor the differential operator as \\((\\partial_t + \\alpha)^2\\).",
      "حلل المؤثر الزمني إلى مربع كامل \\((\\partial_t + \\alpha)^2\\).")

    # 266: Green's Second Identity
    q("KAUST-P3-266", "Partial Differential Equations", "Medium",
      "Green's Second Identity states that for two twice-differentiable functions \\(u\\) and \\(v\\) on domain \\(\\Omega\\) with smooth boundary \\(\\partial \\Omega\\):",
      "تنص متطابقة غرين الثانية على أنه لدالتين \\(u\\) و \\(v\\) قابلتين للاشتقاق مرتين على النطاق \\(\\Omega\\):",
      ["\\(\\int_\\Omega (u \\Delta v - v \\Delta u) dV = \\int_{\\partial \\Omega} \\left(u \\frac{\\partial v}{\\partial n} - v \\frac{\\partial u}{\\partial n}\\right) dS\\)",
       "\\(\\int_\\Omega (u \\Delta v + v \\Delta u) dV = \\int_{\\partial \\Omega} u v dS\\)",
       "\\(\\int_\\Omega \\nabla u \\cdot \\nabla v dV = \\int_{\\partial \\Omega} u \\frac{\\partial v}{\\partial n} dS\\)",
       "\\(\\int_\\Omega (u \\Delta v - v \\Delta u) dV = 0\\)"],
      0,
      "Apply the Divergence Theorem to the vector field \\(\\mathbf{F} = u \\nabla v - v \\nabla u\\). Compute \\(\\nabla \\cdot \\mathbf{F} = \\nabla u \\cdot \\nabla v + u \\Delta v - (\\nabla v \\cdot \\nabla u + v \\Delta u) = u \\Delta v - v \\Delta u\\). The boundary flux is \\(\\mathbf{F} \\cdot \\mathbf{n} = u (\\nabla v \\cdot \\mathbf{n}) - v (\\nabla u \\cdot \\mathbf{n}) = u \\frac{\\partial v}{\\partial n} - v \\frac{\\partial u}{\\partial n}\\). Applying Gauss's Divergence Theorem gives Green's Second Identity.",
      "بتطبيق مبرهنة التباعد على الحقل الشعاعي \\(\\mathbf{F} = u \\nabla v - v \\nabla u\\): نجد أن التباعد هو \\(u\\Delta v - v\\Delta u\\)، والتدفق عبر الحدود هو \\(u \\frac{\\partial v}{\\partial n} - v \\frac{\\partial u}{\\partial n}\\). هذه هي متطابقة غرين الثانية الشهيرة.",
      "Apply the divergence theorem to the vector field \\(u \\nabla v - v \\nabla u\\).",
      "طبق مبرهنة التباعد لغاوس على الحقل الشعاعي \\(u\\nabla v - v\\nabla u\\).")

    # 267: Duhamel's Principle for Inhomogeneous Heat Equation
    q("KAUST-P3-267", "Partial Differential Equations", "Hard",
      "Duhamel's principle represents the solution to the inhomogeneous heat equation \\(u_t - \\Delta u = f(x, t)\\) with \\(u(x, 0) = 0\\) as an integral of solutions \\(w(x, t; s)\\) to which homogeneous problem?",
      "يمثل مبدأ دوهاميل حل معادلة الحرارة غير المتجانسة \\(u_t - \\Delta u = f(x, t)\\) مع \\(u(x, 0) = 0\\) كتكامل لحلول المسألة المتجانسة \\(w(x, t; s)\\). ما هي تلك المسألة؟",
      ["\\(w_t - \\Delta w = 0\\) for \\(t > s\\), with \\(w(x, s; s) = f(x, s)\\)",
       "\\(w_t - \\Delta w = 0\\) for \\(t > 0\\), with \\(w(x, 0; s) = f(x, 0)\\)",
       "\\(-\\Delta w = f(x, s)\\) with zero Dirichlet boundary conditions",
       "\\(w_{tt} - \\Delta w = f(x, s)\\) with zero initial velocity"],
      0,
      "Duhamel's principle treats the external forcing \\(f(x, s)\\) as a continuous succession of initial conditions applied at each time instant \\(s\\). The solution is \\(u(x, t) = \\int_0^t w(x, t; s) ds\\), where each \\(w(x, t; s)\\) satisfies the homogeneous equation \\(w_t - \\Delta w = 0\\) for \\(t > s\\) starting with initial data \\(w(x, s; s) = f(x, s)\\).",
      "يتعامل مبدأ دوهاميل مع القوة الخارجية كنبضات متتابعة تعمل كشروط ابتدائية عند كل لحظة زمنية \\(s\\). الحل هو تكامل \\(u(x, t) = \\int_0^t w(x, t; s) ds\\) حيث يحقق \\(w\\) المعادلة المتجانسة بدءاً من \\(s\\) مع الشرط \\(w(x, s; s) = f(x, s)\\).",
      "Think of forcing as an ongoing series of impulsive initial conditions.",
      "فكر في الدالة غير المتجانسة كسلسلة مستمرة من النبضات الابتدائية.")

    # 268: Eigenvalues of Dirichlet Laplacian on Rectangle
    q("KAUST-P3-268", "Partial Differential Equations", "Medium",
      "Find the eigenvalues \\(\\lambda_{m,n}\\) of the Laplacian \\(-\\Delta u = \\lambda u\\) on the rectangular domain \\([0, a] \\times [0, b]\\) with zero Dirichlet boundary conditions.",
      "أوجد القيم الذاتية \\(\\lambda_{m,n}\\) لمؤثر لابلاس \\(-\\Delta u = \\lambda u\\) على المستطيل \\([0, a] \\times [0, b]\\) مع شروط ديريكليه الصفرية على الحدود.",
      ["\\(\\lambda_{m,n} = \\pi^2 \\left(\\frac{m^2}{a^2} + \\frac{n^2}{b^2}\\right)\\) for \\(m, n = 1, 2, 3, \\dots\\)",
       "\\(\\lambda_{m,n} = \\pi \\left(\\frac{m}{a} + \\frac{n}{b}\\right)\\)",
       "\\(\\lambda_{m,n} = \\pi^2 \\left(\\frac{m^2}{a^2} - \\frac{n^2}{b^2}\\right)\\)",
       "\\(\\lambda_{m,n} = \\frac{4\\pi^2}{ab}(m^2 + n^2)\\)"],
      0,
      "Separate variables: \\(u(x, y) = X(x)Y(y)\\). Then \\(-\\frac{X''}{X} - \\frac{Y''}{Y} = \\lambda\\). Let \\(-X''/X = \\mu\\) and \\(-Y''/Y = \\nu\\) with \\(\\lambda = \\mu + \\nu\\). With boundary conditions \\(X(0) = X(a) = 0\\), we have \\(X_m(x) = \\sin(m\\pi x / a)\\) and \\(\\mu_m = (m\\pi/a)^2\\). Similarly, \\(Y_n(y) = \\sin(n\\pi y / b)\\) and \\(\\nu_n = (n\\pi/b)^2\\). Therefore, \\(\\lambda_{m,n} = \\pi^2 \\left(\\frac{m^2}{a^2} + \\frac{n^2}{b^2}\\right)\\) for \\(m, n \\in \\mathbb{N}\\).",
      "بفصل المتغيرات \\(u = X(x)Y(y)\\) نصل إلى مسألتي شتورم-ليوفيل أحاديتي البعد. شروط ديريكليه الصفرية تعطي دوال الجيب \\(\\sin(m\\pi x/a)\\) و \\(\\sin(n\\pi y/b)\\). بجمع القيم الذاتية نجد \\(\\lambda_{m,n} = \\pi^2(m^2/a^2 + n^2/b^2)\\).",
      "Use separation of variables into two 1D Dirichlet eigenvalue problems.",
      "استخدم فصل المتغيرات إلى مسألتي قيم ذاتية أحاديتي البعد.")

    # 269: Huygens' Principle in Odd vs Even Dimensions
    q("KAUST-P3-269", "Partial Differential Equations", "Hard",
      "According to Huygens' Principle for the wave equation \\(u_{tt} = c^2 \\Delta u\\), a sharp disturbance at \\(t = 0\\) propagates with a sharp trailing edge (leaving no residual disturbance in its wake) in which spatial dimensions?",
      "وفقاً لمبدأ هويغنز لمعادلة الموجة، تنتشر النبضة الحادة تاركة خلفها سكوناً تاماً (حافة خلفية حادة بدون أثر متبقٍ) في أي أبعاد مكانية؟",
      ["Odd spatial dimensions \\(n \\ge 3\\) (e.g., \\(n = 3, 5, 7\\))",
       "Even spatial dimensions (e.g., \\(n = 2, 4\\))",
       "All spatial dimensions including \\(n = 1\\) and \\(n = 2\\)",
       "Only in dimension \\(n = 1\\)"],
      0,
      "Huygens' Principle in the strict sense holds only in odd dimensions \\(n \\ge 3\\). In \\(n = 3\\), Poisson's spherical means formula shows that the solution at \\((\\mathbf{x}, t)\\) depends solely on initial data on the sphere of radius \\(ct\\) (the wave front). In \\(n = 2\\) (by Hadamard's method of descent), the solution depends on the entire solid disc of radius \\(ct\\), causing waves to have a 'wake' or reverberation (like ripples on a pond). In \\(n = 1\\), d'Alembert's formula also contains an integral over the interior segment.",
      "ينطبق مبدأ هويغنز بالمعنى الصارم فقط في الأبعاد الفردية \\(n \\ge 3\\) (مثل \\(n=3\\)). في \\(n=3\\) تعتمد الموجة فقط على سطح كرة نصف قطرها \\(ct\\). بينما في بعدين \\(n=2\\) بطريقة النزول لهادامارد، يعتمد الحل على كامل القرص المصمت، مما يترك ذيلاً متموجاً خلف جبهة الموجة.",
      "In 3D, sound travels with sharp fronts and no reverberation, unlike surface ripples on 2D water.",
      "في ثلاثة أبعاد تنتشر الموجات الصوتية بحواف حادة دون أثر متبقٍ، بخلاف تموجات سطح الماء ثنائي البعد.")

    # 270: Hopf-Cole Transformation for Viscous Burgers' Equation
    q("KAUST-P3-270", "Partial Differential Equations", "Hard",
      "The Hopf-Cole transformation \\(u(x, t) = -2\\nu \\frac{\\phi_x}{\\phi}\\) linearizes the viscous Burgers' equation \\(u_t + u u_x = \\nu u_{xx}\\) into which classical linear PDE for \\(\\phi(x, t)\\)?",
      "يحول تحويل هوبف-كول \\(u(x, t) = -2\\nu \\frac{\\phi_x}{\\phi}\\) معادلة بيرغرز اللزجة اللاخطية \\(u_t + u u_x = \\nu u_{xx}\\) إلى أي معادلة خطية كلاسيكية لـ \\(\\phi\\)؟",
      ["The heat equation \\(\\phi_t = \\nu \\phi_{xx}\\)",
       "The wave equation \\(\\phi_{tt} = \\nu^2 \\phi_{xx}\\)",
       "Laplace's equation \\(\\phi_{xx} + \\phi_{tt} = 0\\)",
       "Korteweg-de Vries equation"],
      0,
      "Let \\(u = -2\\nu (\\ln\\phi)_x = -2\\nu \\frac{\\phi_x}{\\phi}\\). Integrate the Burgers' equation once with respect to \\(x\\): \\(\\psi_t + \\frac{1}{2}(\\psi_x)^2 = \\nu \\psi_{xx}\\) where \\(u = \\psi_x\\). Setting \\(\\psi = -2\\nu \\ln\\phi\\) and computing derivatives gives \\(\\psi_t = -2\\nu \\frac{\\phi_t}{\\phi}\\), \\(\\psi_x = -2\\nu \\frac{\\phi_x}{\\phi}\\), and \\(\\psi_{xx} = -2\\nu \\left(\\frac{\\phi_{xx}}{\\phi} - \\frac{\\phi_x^2}{\\phi^2}\\right)\\). Substituting yields \\(-2\\nu \\frac{\\phi_t}{\\phi} + 2\\nu^2 \\frac{\\phi_x^2}{\\phi^2} = -2\\nu^2 \\frac{\\phi_{xx}}{\\phi} + 2\\nu^2 \\frac{\\phi_x^2}{\\phi^2}\\). The nonlinear terms cancel out completely, leaving \\(\\phi_t = \\nu \\phi_{xx}\\), the linear heat equation.",
      "بالتعويض عن \\(u = -2\\nu (\\ln\\phi)_x\\) في معادلة بيرغرز اللزجة، تتلاشى الحدود اللاخطية التربيعية تماماً بفعل الاختصار الدقيق، وتتحول المعادلة مباشرة إلى معادلة الحرارة الخطية القياسية \\(\\phi_t = \\nu \\phi_{xx}\\).",
      "Notice that \\(u = -2\\nu \\partial_x \\ln\\phi\\) and substitute into the integrated equation.",
      "لاحظ أن \\(u = -2\\nu \\partial_x \\ln\\phi\\) وعوض في المعادلة المكاملة.")

    # 271: Helmholtz Equation
    q("KAUST-P3-271", "Partial Differential Equations", "Medium",
      "The time-harmonic acoustic wave equation \\(u_{tt} = c^2 \\Delta u\\) with ansatz \\(u(\\mathbf{x}, t) = v(\\mathbf{x}) e^{-i\\omega t}\\) reduces to which fundamental elliptic PDE?",
      "تختزل معادلة الموجة الصوتية التوافقية مع الزمن بفرض \\(u(\\mathbf{x}, t) = v(\\mathbf{x}) e^{-i\\omega t}\\) إلى أي معادلة تفاضلية جزئية إهليلجية أساسية؟",
      ["The Helmholtz equation \\(\\Delta v + k^2 v = 0\\), where \\(k = \\omega / c\\)",
       "The Laplace equation \\(\\Delta v = 0\\)",
       "The Poisson equation \\(\\Delta v = -\\omega^2\\)",
       "The Klein-Gordon equation with imaginary mass"],
      0,
      "Differentiating twice in time: \\(u_{tt} = -\\omega^2 v(\\mathbf{x}) e^{-i\\omega t}\\). The wave equation becomes \\(-\\omega^2 v e^{-i\\omega t} = c^2 (\\Delta v) e^{-i\\omega t}\\). Dividing by \\(c^2 e^{-i\\omega t}\\) gives \\(\\Delta v + \\frac{\\omega^2}{c^2} v = 0\\). Setting wavenumber \\(k = \\omega / c\\) yields the Helmholtz equation \\(\\Delta v + k^2 v = 0\\).",
      "باشتقاق الحل التوافقي مرتين بالنسبة للزمن نجد \\(u_{tt} = -\\omega^2 v e^{-i\\omega t}\\). بالتعويض في معادلة الموجة والقسمة على \\(c^2\\) نصل مباشرة إلى معادلة هيلمهولتز \\(\\Delta v + k^2 v = 0\\) حيث رقم الموجة \\(k = \\omega/c\\).",
      "Substitute \\(u_{tt} = -\\omega^2 u\\) into the wave equation.",
      "عوض بـ \\(u_{tt} = -\\omega^2 u\\) في معادلة الموجة.")

    # 272: Korteweg-de Vries (KdV) Equation Soliton
    q("KAUST-P3-272", "Nonlinear PDEs", "Hard",
      "The Korteweg-de Vries (KdV) equation \\(u_t + 6u u_x + u_{xxx} = 0\\) models shallow water waves. The traveling 1-soliton solution with speed \\(c > 0\\) has the shape \\(u(x, t) = \\frac{c}{2} \\text{sech}^2\\left(\\frac{\\sqrt{c}}{2}(x - ct)\\right)\\). What is the relationship between the soliton's amplitude and its speed \\(c\\)?",
      "تنمذج معادلة كورتفيغ-دي فريس (KdV) موجات المياه الضحلة. حل السوليتون المنفرد المنتقل بسرعة \\(c > 0\\) يتخذ شكل \\(\\text{sech}^2\\). ما العلاقة بين سعة السوليتون وسرعته \\(c\\)؟",
      ["Amplitude is directly proportional to speed \\(c\\) (taller solitons move faster)",
       "Amplitude is inversely proportional to speed \\(c\\)",
       "Amplitude is proportional to \\(\\sqrt{c}\\)",
       "Speed is independent of amplitude"],
      0,
      "From the explicit solution \\(u(x, t) = \\frac{c}{2} \\text{sech}^2\\left(\\frac{\\sqrt{c}}{2}(x - ct)\\right)\\), the peak occurs where the argument of \\(\\text{sech}\\) is zero, where \\(\\text{sech}(0) = 1\\). Thus the peak amplitude is \\(u_{\\max} = \\frac{c}{2}\\). This shows that the amplitude is directly proportional to speed \\(c\\): taller solitons travel strictly faster and have narrower width (since width \\(\\sim 1/\\sqrt{c}\\)).",
      "من صيغة الحل الصريح، تبلغ الدالة قيمتها العظمى عند انعدام الزاوية حيث \\(\\text{sech}(0) = 1\\)، فتكون السعة العظمى هي \\(c/2\\). هذا يثبت أن سعة السوليتون تتناسب طردياً مع سرعته: السوليتونات الأكثر ارتفاعاً تتحرك بسرعة أكبر وتكون أضيق عرضاً.",
      "Evaluate the maximum value of \\(\\frac{c}{2}\\text{sech}^2(\\dots)\\).",
      "احسب القيمة العظمى للحل عندما تكون زاوية القاطع الزائدي صفراً.")

    # 273: Sobolev Embedding Theorem (1D)
    q("KAUST-P3-273", "Sobolev Spaces", "Hard",
      "The Sobolev embedding theorem in 1D states that the Sobolev space \\(H^1(I) = W^{1,2}(I)\\) on a bounded interval \\(I\\) continuously embeds into which Hölder space?",
      "تنص نظرية التضمين لسوبوليف في بعد واحد على أن فضاء سوبوليف \\(H^1(I)\\) على فترة محدودة يُضمّن اتصالياً في أي فضاء هولدر؟",
      ["\\(C^{0, 1/2}(\\bar{I})\\) (Hölder continuous with exponent \\(1/2\\))",
       "\\(C^1(\\bar{I})\\)",
       "\\(L^\\infty(I)\\) but discontinuous everywhere",
       "\\(C^{0, 1}(\\bar{I})\\) (Lipschitz continuous)"],
      0,
      "By Morrey's inequality / Sobolev embedding for dimension \\(n = 1\\) with \\(p = 2 > n = 1\\): since \\(p > n\\), functions in \\(W^{1,p}\\) are Hölder continuous with exponent \\(\\gamma = 1 - n/p = 1 - 1/2 = 1/2\\). Explicitly, by Cauchy-Schwarz: \\(|u(x) - u(y)| = \\left|\\int_y^x u'(t)dt\\right| \\le \\left(\\int_y^x 1^2 dt\\right)^{1/2} \\left(\\int_y^x |u'|^2 dt\\right)^{1/2} \\le |x - y|^{1/2} \\|u'\\|_{L^2}\\). This proves \\(H^1(I) \\hookrightarrow C^{0, 1/2}(\\bar{I})\\).",
      "في بعد واحد \\(n=1\\) مع \\(p=2 > 1\\): باستخدام متراجحة كوشي-شفارتز نجد \\(|u(x) - u(y)| \\le |x-y|^{1/2} \\|u'\\|_{L^2}\\). هذا يثبت أن أي دالة في \\(H^1\\) هي دالة هولدر بأس \\(1/2\\) ومستمرة تماماً.",
      "Apply Cauchy-Schwarz to \\(|u(x) - u(y)| = |\\int_x^y u'(t)dt|\\).",
      "طبق متراجحة كوشي-شفارتز على تكامل المشتق الأول.")

    # 274: Heat Equation Irreversibility and Entropy
    q("KAUST-P3-274", "Partial Differential Equations", "Medium",
      "For a closed system governed by \\(u_t = \\Delta u\\) on \\(\\Omega\\) with Neumann boundary conditions \\(\\frac{\\partial u}{\\partial n} = 0\\), what is the long-term behavior of \\(u(x, t)\\) as \\(t \\to \\infty\\)?",
      "لنظام مغلق تحكمه معادلة الحرارة \\(u_t = \\Delta u\\) مع شروط نيومان \\(\\partial u / \\partial n = 0\\)، ما هو السلوك طويل الأمد لـ \\(u(x, t)\\) عندما \\(t \\to \\infty\\)؟",
      ["\\(u(x, t)\\) converges exponentially to the spatial average \\(\\bar{u} = \\frac{1}{|\\Omega|}\\int_\\Omega u(x, 0) dx\\)",
       "\\(u(x, t)\\) converges to zero everywhere",
       "\\(u(x, t)\\) oscillates periodically forever",
       "\\(u(x, t)\\) blows up to infinity"],
      0,
      "With homogeneous Neumann boundary conditions, the first non-zero eigenvalue of the Laplacian is \\(\\lambda_1 > 0\\) (by Poincaré-Wirtinger inequality). The eigenmode expansion gives \\(u(x, t) = a_0 + \\sum_{k=1}^\\infty a_k \\phi_k(x) e^{-\\lambda_k t}\\). Since \\(\\lambda_k \\ge \\lambda_1 > 0\\) for all \\(k \\ge 1\\), all spatial variations decay exponentially as \\(e^{-\\lambda_1 t}\\). The surviving constant term is \\(a_0 = \\frac{1}{|\\Omega|}\\int_\\Omega u(x, 0)dx\\), the initial average temperature.",
      "مع شروط نيومان المعزولة، فإن جميع الأنماط غير الثابتة تضمحل أسياً بمعدل \\(e^{-\\lambda_k t}\\). الحد الوحيد المتبقي هو القيمة المتوسطة الابتدائية للحرارة موزعة بانتظام على كامل النطاق.",
      "Recall that the zero eigenvalue corresponds to the constant eigenfunction, and all positive eigenvalues decay exponentially.",
      "تذكر أن القيمة الذاتية الصفرية تقابل الدالة الثابتة، بينما تضمحل باقي الأنماط أسياً.")

    # 275: Poisson Kernel in the Upper Half Plane
    q("KAUST-P3-275", "Partial Differential Equations", "Hard",
      "What is the Poisson kernel \\(P(x, y)\\) that solves the Dirichlet problem for Laplace's equation in the upper half plane \\(y > 0\\) with boundary data \\(u(x, 0) = f(x)\\)?",
      "ما هي نواة بواسون \\(P(x, y)\\) التي تحل مسألة ديريكليه لمعادلة لابلاس في النصف العلوي للمستوى \\(y > 0\\) مع الشرط الحدي \\(u(x, 0) = f(x)\\)؟",
      ["\\(P(x, y) = \\frac{1}{\\pi} \\frac{y}{x^2 + y^2}\\)",
       "\\(P(x, y) = \\frac{1}{2\\pi} \\frac{x}{x^2 + y^2}\\)",
       "\\(P(x, y) = \\frac{1}{\\pi} \\frac{x^2 - y^2}{(x^2 + y^2)^2}\\)",
       "\\(P(x, y) = \\frac{1}{\\sqrt{2\\pi y}} e^{-x^2/(4y)}\\)"],
      0,
      "Taking the Fourier transform in \\(x\\): \\(-k^2 \\hat{u} + \\hat{u}_{yy} = 0 \\implies \\hat{u}(k, y) = A(k)e^{-|k|y} + B(k)e^{+|k|y}\\). Boundedness as \\(y \\to \\infty\\) requires \\(B(k) = 0\\), so \\(\\hat{u}(k, y) = \\hat{f}(k)e^{-|k|y}\\). The inverse Fourier transform of \\(e^{-|k|y}\\) is the Cauchy density / Poisson kernel: \\(P(x, y) = \\frac{1}{2\\pi}\\int_{-\\infty}^\\infty e^{-|k|y} e^{ikx} dk = \\frac{1}{\\pi}\\frac{y}{x^2 + y^2}\\). The solution is \\(u(x, y) = (P(\\cdot, y) * f)(x)\\).",
      "بأخذ تحويل فورييه بالنسبة لـ \\(x\\) وفرض المحدودية عندما \\(y \\to \\infty\\) نجد \\(\\hat{u}(k, y) = \\hat{f}(k)e^{-|k|y}\\). بالتحويل العكسي نصل إلى نواة كوشي-بواسون \\(P(x, y) = \\frac{1}{\\pi}\\frac{y}{x^2+y^2}\\).",
      "Recognize the inverse Fourier transform of \\(e^{-|k|y}\\).",
      "تعرف على تحويل فورييه العكسي للدالة الأسية \\(e^{-|k|y}\\).")

    # 276: Green's Representation Formula
    q("KAUST-P3-276", "Partial Differential Equations", "Hard",
      "If \\(u\\) is a smooth solution to Poisson's equation \\(-\\Delta u = f\\) in \\(\\Omega\\), and \\(G(x, y)\\) is the Dirichlet Green's function (satisfying \\(G(x, y) = 0\\) for \\(y \\in \\partial \\Omega\\)), what is the representation formula for \\(u(x)\\)?",
      "إذا كانت \\(u\\) حلاً أملس لمعادلة بواسون \\(-\\Delta u = f\\) في \\(\\Omega\\)، وكانت \\(G(x, y)\\) دالة غرين لديريكليه، فما هي صيغة التمثيل لـ \\(u(x)\\)؟",
      ["\\(u(x) = \\int_\\Omega G(x, y) f(y) dy - \\int_{\\partial \\Omega} \\frac{\\partial G}{\\partial n_y}(x, y) u(y) dS_y\\)",
       "\\(u(x) = \\int_\\Omega G(x, y) f(y) dy + \\int_{\\partial \\Omega} G(x, y) \\frac{\\partial u}{\\partial n_y} dS_y\\)",
       "\\(u(x) = \\int_\\Omega \\nabla_y G(x, y) \\cdot \\nabla f(y) dy\\)",
       "\\(u(x) = \\frac{1}{|\\Omega|} \\int_\\Omega f(y) dy\\)"],
      0,
      "From Green's Second Identity: \\(\\int_\\Omega (u \\Delta_y G - G \\Delta_y u) dy = \\int_{\\partial \\Omega} \\left(u \\frac{\\partial G}{\\partial n_y} - G \\frac{\\partial u}{\\partial n_y}\\right) dS_y\\). Since \\(-\\Delta_y G(x, y) = \\delta(x - y)\\), the first term is \\(-u(x)\\). Since \\(-\\Delta u = f\\), the second term is \\(\\int G f dy\\). On \\(\\partial \\Omega\\), \\(G(x, y) = 0\\), so the \\(G \\frac{\\partial u}{\\partial n}\\) term vanishes entirely. Rearranging yields \\(u(x) = \\int_\\Omega G(x, y) f(y) dy - \\int_{\\partial \\Omega} \\frac{\\partial G}{\\partial n_y}(x, y) u(y) dS_y\\).",
      "من متطابقة غرين الثانية: بما أن \\(G = 0\\) على الحدود، يختفي حد المشتقة العمودية لـ \\(u\\)، وبنقل الحدود نصل مباشرة إلى صيغة التمثيل الكلاسيكية لحل مسألة ديريكليه لمعادلة بواسون.",
      "Use Green's second identity and the boundary condition \\(G(x, y) = 0\\) on \\(\\partial \\Omega\\).",
      "استخدم متطابقة غرين الثانية مع انعدام دالة غرين على الحدود.")

    # 277: Black-Scholes PDE
    q("KAUST-P3-277", "Financial PDEs", "Hard",
      "The Black-Scholes equation for European option price \\(V(S, t)\\) is \\(V_t + \\frac{1}{2}\\sigma^2 S^2 V_{SS} + r S V_S - r V = 0\\). Under the log-price transformation \\(x = \\ln S\\), what type of PDE does this become?",
      "معادلة بلاك-شولز لتسعير الخيارات الأوروبية هي \\(V_t + \\frac{1}{2}\\sigma^2 S^2 V_{SS} + r S V_S - r V = 0\\). تحت تحويل السعر اللوغاريتمي \\(x = \\ln S\\)، إلى أي نوع من المعادلات التفاضلية الجزئية تتحول؟",
      ["A parabolic convection-diffusion-reaction equation with constant coefficients",
       "An elliptic Laplace-type equation",
       "A hyperbolic wave equation",
       "A nonlinear KdV equation"],
      0,
      "Using \\(x = \\ln S\\), by the chain rule: \\(S V_S = V_x\\) and \\(S^2 V_{SS} = V_{xx} - V_x\\). Substituting into the Black-Scholes equation transforms the variable coefficients \\(S^2\\) and \\(S\\) into constant coefficients: \\(V_t + \\frac{1}{2}\\sigma^2 V_{xx} + \\left(r - \\frac{1}{2}\\sigma^2\\right)V_x - rV = 0\\). This is a parabolic linear PDE with constant coefficients (a backward convection-diffusion-reaction equation), which can be mapped directly to the heat equation via a further gauge transformation.",
      "باستخدام التحويل اللوغاريتمي \\(x = \\ln S\\)، تتحول المشتقات بالنسبة لـ \\(S\\) بواسطة قاعدة السلسلة بحيث تلغى المعاملات المتغيرة وتصبح المعادلة ذات معاملات ثابتة: معادلة حمل وانتشار مكافئة يمكن تحويلها مباشرة إلى معادلة الحرارة.",
      "Compute \\(S \\frac{\\partial}{\\partial S} = \\frac{\\partial}{\\partial x}\\) and \\(S^2 \\frac{\\partial^2}{\\partial S^2} = \\frac{\\partial^2}{\\partial x^2} - \\frac{\\partial}{\\partial x}\\).",
      "احسب المشتقات بالنسبة للمتغير اللوغاريتمي الجديد.")

    # 278: Maximum Principle Application - Uniqueness
    q("KAUST-P3-278", "Partial Differential Equations", "Medium",
      "How is the Maximum Principle used to prove the uniqueness of solutions to the Dirichlet problem for Poisson's equation \\(\\Delta u = f\\) in \\(\\Omega\\) with \\(u = g\\) on \\(\\partial \\Omega\\)?",
      "كيف يُستخدم مبدأ النهاية العظمى لإثبات وحدانية الحل لمسألة ديريكليه لمعادلة بواسون \\(\\Delta u = f\\) مع \\(u = g\\) على الحدود؟",
      ["Let \\(w = u_1 - u_2\\); then \\(\\Delta w = 0\\) and \\(w = 0\\) on \\(\\partial \\Omega\\), so \\(\\max w = \\min w = 0 \\implies w \\equiv 0\\)",
       "By showing that the energy must be strictly negative",
       "By using Fourier series convergence",
       "By proving that \\(f\\) must be identically zero"],
      0,
      "Suppose there are two solutions \\(u_1\\) and \\(u_2\\). Define their difference \\(w = u_1 - u_2\\). Then \\(\\Delta w = \\Delta u_1 - \\Delta u_2 = f - f = 0\\) in \\(\\Omega\\), so \\(w\\) is harmonic. On the boundary, \\(w = g - g = 0\\) on \\(\\partial \\Omega\\). By the Maximum and Minimum Principles for harmonic functions, \\(\\min_{\\partial \\Omega} w \\le w(x) \\le \\max_{\\partial \\Omega} w\\). Since \\(w = 0\\) on \\(\\partial \\Omega\\), we have \\(0 \\le w(x) \\le 0\\) everywhere in \\(\\Omega\\), forcing \\(w(x) \\equiv 0 \\implies u_1 = u_2\\).",
      "نفرض وجود حلين ونعرف الفرق \\(w = u_1 - u_2\\). الدالة \\(w\\) توافقية وتنعدم تماماً على الحدود. بمبدأ النهاية العظمى والصغرى، تكون الدالة محصورة بين أصغر وأكبر قيمة لها على الحدود (وهما صفر)، مما يقتضي \\(w \\equiv 0\\) وبالتالي \\(u_1 = u_2\\).",
      "Consider the difference of two solutions \\(w = u_1 - u_2\\).",
      "تأمل الفرق بين حلين مفترضين وطبق مبدأ النهاية العظمى عليه.")

    # 279: Heat Equation in 3D Fundamental Solution
    q("KAUST-P3-279", "Partial Differential Equations", "Medium",
      "What is the fundamental solution of the 3D heat equation \\(u_t = \\Delta u\\) in \\(\\mathbb{R}^3\\)?",
      "ما هو الحل الأساسي لمعادلة الحرارة ثلاثية الأبعاد \\(u_t = \\Delta u\\) في \\(\\mathbb{R}^3\\)؟",
      ["\\(\\Phi(\\mathbf{x}, t) = \\frac{1}{(4\\pi t)^{3/2}} \\exp\\left(-\\frac{|\\mathbf{x}|^2}{4t}\\right)\\)",
       "\\(\\Phi(\\mathbf{x}, t) = \\frac{1}{4\\pi t} \\exp\\left(-\\frac{|\\mathbf{x}|^2}{2t}\\right)\\)",
       "\\(\\Phi(\\mathbf{x}, t) = \\frac{1}{(2\\pi t)^{3/2}} \\exp\\left(-\\frac{|\\mathbf{x}|}{4t}\\right)\\)",
       "\\(\\Phi(\\mathbf{x}, t) = \\frac{1}{8\\pi^3 t} \\exp\\left(-\\frac{|\\mathbf{x}|^2}{4t}\\right)\\)"],
      0,
      "In \\(n\\) spatial dimensions, the fundamental solution of the heat equation \\(u_t = \\Delta u\\) is the product of \\(n\\) one-dimensional heat kernels: \\(\\Phi(\\mathbf{x}, t) = \\prod_{i=1}^n \\frac{1}{\\sqrt{4\\pi t}} e^{-x_i^2 / (4t)} = \\frac{1}{(4\\pi t)^{n/2}} \\exp\\left(-\\frac{|\\mathbf{x}|^2}{4t}\\right)\\). For \\(n = 3\\), the prefactor is \\(\\frac{1}{(4\\pi t)^{3/2}}\\).",
      "في \\(n\\) من الأبعاد المكانية، الحل الأساسي لمعادلة الحرارة هو جداء \\(n\\) من الأنوية أحادية البعد: \\(\\Phi = \\frac{1}{(4\\pi t)^{n/2}} \\exp(-|\\mathbf{x}|^2 / 4t)\\). لبُعد \\(n = 3\\)، يكون المعامل هو \\((4\\pi t)^{-3/2}\\).",
      "Multiply three independent 1D heat kernels: \\(\\Phi_{3D} = \\Phi_{1D}(x)\\Phi_{1D}(y)\\Phi_{1D}(z)\\).",
      "اضرب ثلاثة حلول أساسية أحادية البعد لكل من الإحداثيات الثلاثة.")

    # 280: Wave Equation in 3D Kirchhoff's Formula
    q("KAUST-P3-280", "Partial Differential Equations", "Hard",
      "Kirchhoff's formula for the solution of the 3D wave equation \\(u_{tt} = c^2 \\Delta u\\) with \\(u(\\mathbf{x}, 0) = 0\\) and \\(u_t(\\mathbf{x}, 0) = \\psi(\\mathbf{x})\\) is given by:",
      "صيغة كيرشوف لحل معادلة الموجة ثلاثية الأبعاد مع إزاحة ابتدائية صفرية وسرعة ابتدائية \\(\\psi(\\mathbf{x})\\) تُعطى بـ:",
      ["\\(u(\\mathbf{x}, t) = \\frac{t}{4\\pi} \\iint_{|\\mathbf{y}-\\mathbf{x}|=ct} \\psi(\\mathbf{y}) dS_y\\) (or \\(t\\) times the spherical average of \\(\\psi\\))",
       "\\(u(\\mathbf{x}, t) = \\frac{1}{4\\pi c t} \\iiint_{|\\mathbf{y}-\\mathbf{x}| \\le ct} \\psi(\\mathbf{y}) dy\\)",
       "\\(u(\\mathbf{x}, t) = \\frac{1}{2c}[\\psi(\\mathbf{x}-ct) + \\psi(\\mathbf{x}+ct)]\\)",
       "\\(u(\\mathbf{x}, t) = \\frac{1}{(4\\pi t)^{3/2}} \\iint_{|\\mathbf{y}|=ct} \\psi(\\mathbf{y}) dS_y\\)"],
      0,
      "Kirchhoff's formula states that for the 3D wave equation with initial velocity \\(\\psi\\), \\(u(\\mathbf{x}, t) = \\frac{1}{4\\pi c^2 t} \\iint_{|\\mathbf{y}-\\mathbf{x}|=ct} \\psi(\\mathbf{y}) dS_y = t M_\\psi(\\mathbf{x}, ct)\\), where \\(M_\\psi(\\mathbf{x}, ct) = \\frac{1}{4\\pi c^2 t^2} \\iint_{|\\mathbf{y}-\\mathbf{x}|=ct} \\psi(\\mathbf{y}) dS_y\\) is the average of \\(\\psi\\) over the sphere of radius \\(ct\\). Thus \\(u(\\mathbf{x}, t) = t \\bar{\\psi}_{\\partial B(\\mathbf{x}, ct)}\\).",
      "تنص صيغة كيرشوف على أن الحل في ثلاثة أبعاد يعطى بـ \\(t\\) مضروباً في المتوسط الكروي للسرعة الابتدائية على سطح الكرة ذات نصف القطر \\(ct\\): \\(u(\\mathbf{x}, t) = \\frac{t}{4\\pi (ct)^2} \\iint_{|\\mathbf{y}-\\mathbf{x}|=ct} \\psi(\\mathbf{y}) dS_y\\).",
      "Notice that the solution integrates strictly over the surface of the sphere of radius \\(ct\\), scaled by \\(t\\).",
      "لاحظ أن التكامل يقع حصراً على سطح كرة نصف قطرها \\(ct\\) ومضروباً في الزمن \\(t\\).")

    # 281 to 300: Finish questions 281-300
    # 281: Conservation Law Characteristic Collision
    q("KAUST-P3-281", "Partial Differential Equations", "Medium",
      "For the inviscid Burgers' equation \\(u_t + u u_x = 0\\), characteristics are straight lines \\(x(t) = x_0 + u(x_0, 0)t\\). If \\(u(x, 0) = -x\\), what happens to all characteristics as \\(t \\to 1\\)?",
      "لمعادلة بيرغرز غير اللزجة، مسارات الخصائص هي خطوط مستقيمة \\(x(t) = x_0 + u(x_0, 0)t\\). إذا كان \\(u(x, 0) = -x\\)، ماذا يحدث لجميع الخصائص عندما \\(t \\to 1\\)؟",
      ["All characteristics focus and intersect simultaneously at \\(x = 0\\) at time \\(t = 1\\) (gradient catastrophe)",
       "Characteristics never intersect",
       "Characteristics diverge to infinity",
       "Characteristics curve into parabolas"],
      0,
      "Substitute \\(u(x_0, 0) = -x_0\\): the characteristic equations are \\(x(t) = x_0 + (-x_0)t = x_0(1 - t)\\). At time \\(t = 1\\), \\(x(1) = x_0(1 - 1) = 0\\) for EVERY initial point \\(x_0\\). Thus all characteristics converge simultaneously at the origin at \\(t = 1\\), causing the slope \\(u_x = \\frac{-1}{1-t}\\) to blow up to \\(-\\infty\\) at \\(t = 1\\).",
      "بما أن \\(u(x_0, 0) = -x_0\\)، فإن معادلة الخاصية هي \\(x(t) = x_0(1-t)\\). عند \\(t = 1\\) نجد \\(x(1) = 0\\) لجميع النقاط الابتدائية \\(x_0\\). تتلاقى جميع الخصائص في نقطة واحدة عند الأصل مسببة صدمة كارثية للمنحدر.",
      "Evaluate \\(x(1)\\) from the characteristic equation \\(x(t) = x_0(1 - t)\\).",
      "احسب \\(x(1)\\) من معادلة الخاصية.")

    # 282: Heat Equation Self-Similar Variable
    q("KAUST-P3-282", "Partial Differential Equations", "Medium",
      "The 1D heat equation \\(u_t = u_{xx}\\) is invariant under the parabolic scaling \\(x \\to \\lambda x, t \\to \\lambda^2 t\\). What is the standard dimensionless similarity variable \\(\\eta\\)?",
      "معادلة الحرارة \\(u_t = u_{xx}\\) صامدة تحت التحجيم المكافئ \\(x \\to \\lambda x, t \\to \\lambda^2 t\\). ما هو متغير التشابه الذاتي القياسي \\(\\eta\\)؟",
      ["\\(\\eta = \\frac{x}{\\sqrt{t}}\\)", "\\(\\eta = \\frac{x}{t}\\)", "\\(\\eta = \\frac{x^2}{t}\\)", "\\(\\eta = x \\sqrt{t}\\)"],
      0,
      "Under the transformation \\(x' = \\lambda x\\) and \\(t' = \\lambda^2 t\\), the ratio \\(\\frac{x'}{\\sqrt{t'}} = \\frac{\\lambda x}{\\sqrt{\\lambda^2 t}} = \\frac{\\lambda x}{\\lambda \\sqrt{t}} = \\frac{x}{\\sqrt{t}}\\) is invariant (scale-free). Hence \\(\\eta = \\frac{x}{\\sqrt{t}}\\) (often written with a factor \\(2\\) as \\(\\eta = \\frac{x}{\\sqrt{4t}}\\)) is the canonical self-similar variable that reduces the heat PDE to an ordinary differential equation.",
      "تحت التحجيم \\(x' = \\lambda x\\) و \\(t' = \\lambda^2 t\\)، فإن النسبة \\(x/\\sqrt{t}\\) تظل ثابتة ومستقلة عن معامل التحجيم \\(\\lambda\\). بالتالي فإن متغير التشابه الذاتي هو \\(\\eta = x/\\sqrt{t}\\).",
      "Find the combination of \\(x\\) and \\(t\\) that is invariant when \\(x\\) scales as \\(\\lambda\\) and \\(t\\) scales as \\(\\lambda^2\\).",
      "ابحث عن التركيب الثابت تحت التحجيم المكافئ.")

    # 283: Wave Equation in 2D Method of Descent
    q("KAUST-P3-283", "Partial Differential Equations", "Hard",
      "Hadamard's method of descent solves the 2D wave equation by treating it as a 3D wave equation that is independent of \\(z\\). This reveals that the 2D wave solution depends on:",
      "تحل طريقة النزول لهادامارد معادلة الموجة ثنائية البعد باعتبارها مسألة ثلاثية الأبعاد مستقلة عن \\(z\\). يوضح هذا أن حل الموجة ثنائي البعد يعتمد على:",
      ["The entire solid disc \\(|\\mathbf{y} - \\mathbf{x}| \\le ct\\)",
       "Only the boundary circle \\(|\\mathbf{y} - \\mathbf{x}| = ct\\)",
       "Only the center point \\(\\mathbf{x}\\)",
       "The exterior of the disc \\(|\\mathbf{y} - \\mathbf{x}| \\ge ct\\)"],
      0,
      "In Hadamard's method of descent, the 3D spherical shell \\(|\\mathbf{y}_{3D} - \\mathbf{x}_{3D}| = ct\\) projects down onto the 2D plane as the solid disc \\(|\\mathbf{y} - \\mathbf{x}| \\le ct\\). Thus, in two dimensions, signals from the entire interior of the past light cone reach the observer, which is why 2D waves have a lingering reverberation (tail) rather than a sharp cutoff.",
      "في طريقة النزول، يسقط سطح الكرة ثلاثية الأبعاد على المستوى ثنائي البعد ليشكل القرص المصمت \\(|\\mathbf{y} - \\mathbf{x}| \\le ct\\). بالتالي، تعتمد الموجة ثنائية البعد على كامل داخل القرص، مما يخلق ذيلاً مستمراً للموجة.",
      "Projecting the surface of a 3D sphere onto a 2D plane fills the entire disc.",
      "إسقاط سطح كرة ثلاثية الأبعاد على مستوى يعطي قرصاً مصمتاً بالكامل.")

    # 284: Energy Identity for Poisson Equation
    q("KAUST-P3-284", "Partial Differential Equations", "Medium",
      "Let \\(u\\) be a smooth function on \\(\\Omega\\) with \\(u = 0\\) on \\(\\partial \\Omega\\). The Dirichlet energy functional is \\(J(u) = \\int_\\Omega \\left(\\frac{1}{2}|\\nabla u|^2 - f u\\right) dx\\). What is the Euler-Lagrange equation associated with minimizing \\(J(u)\\)?",
      "لتكن \\(u\\) دالة ملساء تحقق \\(u = 0\\) على الحدود. دالة طاقة ديريكليه هي \\(J(u) = \\int (\\frac{1}{2}|\\nabla u|^2 - fu) dx\\). ما هي معادلة أويلر-لاغرانج المرتبطة بتصغير \\(J(u)\\)؟",
      ["\\(-\\Delta u = f\\) (Poisson's equation)",
       "\\(\\Delta u = f^2\\)",
       "\\(\\Delta u + f u = 0\\)",
       "\\(-\\Delta u + \\nabla f = 0\\)"],
      0,
      "Compute the first variation \\(\\delta J(u)[v] = \\left.\\frac{d}{d\\epsilon} J(u + \\epsilon v)\\right|_{\\epsilon=0} = \\int_\\Omega (\\nabla u \\cdot \\nabla v - f v) dx\\). Using Green's first identity with \\(v = 0\\) on \\(\\partial \\Omega\\): \\(\\int_\\Omega \\nabla u \\cdot \\nabla v dx = -\\int_\\Omega (\\Delta u) v dx\\). Thus \\(\\delta J(u)[v] = \\int_\\Omega (-\\Delta u - f) v dx = 0\\) for all test functions \\(v \\in C_c^\\infty(\\Omega)\\). By the Fundamental Lemma of the Calculus of Variations, this implies \\(-\\Delta u = f\\).",
      "بحساب التغاير الأول \\(\\delta J(u)[v] = \\int (\\nabla u \\cdot \\nabla v - fv) dx\\) والتكامل بالتجزئة مع تلاشي الدالة الاختبارية على الحدود: نحصل على \\(\\int (-\\Delta u - f)v dx = 0\\). بالتالي، فإن مصغر الطاقة يحقق معادلة بواسون \\(-\\Delta u = f\\).",
      "Compute the first variation and integrate by parts.",
      "احسب التغاير الأول وكامل بالتجزئة لنقل التدرج.")

    # 285: Reaction-Diffusion Traveling Wave (Fisher-KPP)
    q("KAUST-P3-285", "Nonlinear PDEs", "Hard",
      "The Fisher-KPP reaction-diffusion equation \\(u_t = u_{xx} + u(1 - u)\\) admits traveling front solutions \\(u(x, t) = U(x - ct)\\) with \\(U(-\\infty) = 1\\) and \\(U(+\\infty) = 0\\). What is the minimum traveling wave speed \\(c_{\\min}\\) for which non-negative wavefronts exist?",
      "تقبل معادلة فيشر-KPP للانتشار والتفاعل \\(u_t = u_{xx} + u(1 - u)\\) حلول جبهة متنقلة \\(u(x, t) = U(x - ct)\\). ما هي السرعة الصغرى \\(c_{\\min}\\) التي توجد عندها جبهات غير سالبة؟",
      ["\\(c_{\\min} = 2\\)", "\\(c_{\\min} = 1\\)", "\\(c_{\\min} = \\sqrt{2}\\)", "\\(c_{\\min} = 4\\)"],
      0,
      "Substitute \\(u(x, t) = U(\\xi)\\) with \\(\\xi = x - ct\\). The PDE becomes \\(-c U' = U'' + U(1 - U) \\implies U'' + c U' + U(1 - U) = 0\\). Linearizing near the leading edge where \\(U \\approx 0\\) gives \\(U'' + c U' + U = 0\\). The characteristic roots are \\(r = \\frac{-c \\pm \\sqrt{c^2 - 4}}{2}\\). For \\(U(\\xi)\\) to remain non-negative (no oscillations around 0), the roots must be real, which requires \\(c^2 - 4 \\ge 0 \\implies c \\ge 2\\). Thus the minimal wave speed is \\(c_{\\min} = 2\\).",
      "بالتعويض عن \\(\\xi = x - ct\\) نحصل على معادلة تفاضلية عادية: \\(U'' + cU' + U(1-U) = 0\\). بالتقريب الخطي بالقرب من الصفر: \\(U'' + cU' + U = 0\\). لكي لا يتذبذب الحل ويبقى غير سالب، يجب أن يكون المميز \\(c^2 - 4 \\ge 0\\)، أي \\(c \\ge 2\\). السرعة الصغرى هي \\(c_{\\min} = 2\\).",
      "Linearize around \\(U = 0\\) and require real eigenvalues to prevent negative oscillations.",
      "قرب خطياً حول الصفر واشترط أن تكون القيم الذاتية حقيقية لمنع التذبذبات السالبة.")

    # 286: Wave Equation Radiation Condition (Sommerfeld)
    q("KAUST-P3-286", "Partial Differential Equations", "Hard",
      "The Sommerfeld radiation condition ensures that solutions to the Helmholtz equation \\(\\Delta u + k^2 u = 0\\) in an unbounded 3D domain represent outgoing rather than incoming waves. What is this condition as \\(r = |\\mathbf{x}| \\to \\infty\\)?",
      "يضمن شرط سومرفيلد للإشعاع لمعادلة هيلمهولتز في نطاق ثلاثي الأبعاد غير محدود أن الحلول تمثل موجات صادرة وليست واردة. ما هي صيغة هذا الشرط عندما \\(r \\to \\infty\\)؟",
      ["\\(\\lim_{r \\to \\infty} r \\left(\\frac{\\partial u}{\\partial r} - ik u\\right) = 0\\)",
       "\\(\\lim_{r \\to \\infty} \\left(\\frac{\\partial u}{\\partial r} + ik u\\right) = 0\\)",
       "\\(\\lim_{r \\to \\infty} u(r) = 0\\)",
       "\\(\\lim_{r \\to \\infty} r^2 u(r) = 1\\)"],
      0,
      "An outgoing spherical wave has asymptotic form \\(u(r) \\sim \\frac{e^{ikr}}{r}\\). Differentiating: \\(\\frac{\\partial u}{\\partial r} = \\left(ik - \\frac{1}{r}\\right)\\frac{e^{ikr}}{r} = ik u - \\frac{u}{r}\\). Thus \\(\\frac{\\partial u}{\\partial r} - ik u = -\\frac{u}{r} = O(r^{-2})\\). Multiplying by \\(r\\) gives \\(r\\left(\\frac{\\partial u}{\\partial r} - ik u\\right) = O(r^{-1}) \\to 0\\) as \\(r \\to \\infty\\). This is the Sommerfeld Radiation Condition, which uniquely selects outgoing scattered waves.",
      "الموجة الصادرة تتناسب مع \\(e^{ikr}/r\\). باشتقاقها نجد \\(\\frac{\\partial u}{\\partial r} - ik u = O(1/r^2)\\). بالضرب في \\(r\\) وجعل \\(r \\to \\infty\\) نحصل على شرط سومرفيلد للإشعاع الذي يضمن وحدانية الموجات الصادرة.",
      "Differentiate the outgoing spherical wave \\(e^{ikr}/r\\) with respect to \\(r\\).",
      "فاضل الموجة الكروية الصادرة \\(e^{ikr}/r\\) بالنسبة لنصف القطر.")

    # 287: Non-existence of Smooth Solutions - Gradient Catastrophe
    q("KAUST-P3-287", "Partial Differential Equations", "Hard",
      "For the conservation law \\(u_t + u u_x = 0\\) with smooth initial condition \\(u(x, 0) = -\\arctan(x)\\), what is the exact breaking time \\(T^*\\) when the gradient \\(u_x\\) first becomes infinite?",
      "لقانون الانحفاظ \\(u_t + u u_x = 0\\) مع الشرط الابتدائي \\(u(x, 0) = -\\arctan(x)\\)، ما هو زمن التكسر الدقيق \\(T^*\\) الذي يصبح عنده التدرج \\(u_x\\) لانهائياً لأول مرة؟",
      ["\\(T^* = 1\\)", "\\(T^* = \\pi/2\\)", "\\(T^* = 2\\)", "\\(T^* = 1/2\\)"],
      0,
      "Along characteristics, the spatial derivative evolves as \\(u_x(x(t), t) = \\frac{u_0'(x_0)}{1 + t u_0'(x_0)}\\). A shock forms at the minimum positive time \\(t\\) where the denominator vanishes: \\(T^* = -\\frac{1}{\\min_{x_0} u_0'(x_0)}\\). Here \\(u_0(x) = -\\arctan(x)\\), so \\(u_0'(x) = -\\frac{1}{1 + x^2}\\). The minimum value of \\(u_0'(x)\\) occurs at \\(x = 0\\), where \\(u_0'(0) = -1\\). Therefore, \\(T^* = -\\frac{1}{-1} = 1\\).",
      "يتطور تدرج الدالة وفق العلاقة \\(u_x = \\frac{u_0'(x_0)}{1 + t u_0'(x_0)}\\). يحدث التكسر عند أصغر زمن موجب ينعدم عنده المقام: \\(T^* = -1 / \\min u_0'(x)\\). مشتق الدالة هو \\(-1/(1+x^2)\\)، وأصغر قيمة له هي \\(-1\\) عند \\(x=0\\). بالتالي فإن زمن التكسر هو \\(T^* = -1/(-1) = 1\\).",
      "Find the minimum value of \\(u_0'(x) = -\\frac{1}{1+x^2}\\).",
      "أوجد القيمة الصغرى لمشتق الدالة الابتدائية.")

    # 288: Heat Equation Maximum Principle on Bounded Domain
    q("KAUST-P3-288", "Partial Differential Equations", "Medium",
      "Let \\(u(x, t)\\) satisfy \\(u_t = u_{xx}\\) on the spacetime cylinder \\(Q = (0, 1) \\times (0, T]\\). Where can the maximum of \\(u\\) on the closure \\(\\bar{Q}\\) occur?",
      "لتكن \\(u(x, t)\\) حلاً لـ \\(u_t = u_{xx}\\) على الأسطوانة المكانية الزمانية \\((0, 1) \\times (0, T]\\). أين يمكن أن تقع القيمة العظمى لـ \\(u\\) على الإغلاق؟",
      ["Only on the parabolic boundary: \\(t = 0\\), \\(x = 0\\), or \\(x = 1\\)",
       "At any interior point \\((x, t) \\in Q\\)",
       "Only at the final time slice \\(t = T\\)",
       "Only at the center point \\((1/2, T/2)\\)"],
      0,
      "By the Maximum Principle for parabolic equations, the maximum of \\(u(x, t)\\) must be achieved on the parabolic boundary \\(\\Gamma = (\\{0, 1\\} \\times [0, T]) \\cup ([0, 1] \\times \\{0\\})\\), consisting of the initial line and the lateral sides. It cannot occur in the interior or on the top boundary \\(t = T\\) unless \\(u\\) is constant.",
      "حسب مبدأ النهاية العظمى للمعادلات المكافئة، تقع النهاية العظمى حصراً على الحدود المكافئة المكونة من خط البداية الزمني \\(t = 0\\) والجانبين المكانيين \\(x = 0\\) و \\(x = 1\\). ولا يمكن أن تقع في الداخل أو على السطح النهائي إلا إذا كانت الدالة ثابتة.",
      "The parabolic boundary excludes the top time slice \\(t = T\\).",
      "تتكون الحدود المكافئة من القاع الابتدائي والجانبين وتستثني السطح العلوي عند \\(t = T\\).")

    # 289: Bessel Function Zeros and Membrane Vibrations
    q("KAUST-P3-289", "Partial Differential Equations", "Hard",
      "The fundamental frequency of a vibrating circular drum of radius \\(R\\) clamped at its edge (satisfying \\(u_{tt} = c^2 \\Delta u\\) with \\(u(R, \\theta, t) = 0\\)) is proportional to the first positive zero \\(j_{0,1} \\approx 2.4048\\) of which function?",
      "التردد الأساسي لغشاء طبل دائري مهتز نصف قطره \\(R\\) ومثبت عند حافته يتناسب طردياً مع أول جذر موجب \\(j_{0,1} \\approx 2.4048\\) لأي دالة؟",
      ["\\(J_0(x)\\) (Bessel function of the first kind of order 0)",
       "\\(J_1(x)\\) (Bessel function of the first kind of order 1)",
       "\\(Y_0(x)\\) (Bessel function of the second kind of order 0)",
       "\\(I_0(x)\\) (Modified Bessel function)"],
      0,
      "For a circular membrane with clamped edges, the radial modes satisfy Bessel's equation \\(r^2 R'' + r R' + \\frac{\\omega^2}{c^2} r^2 R = 0\\). Since the drum is physical and non-singular at the center \\(r = 0\\), the solution must discard the singular Neumann function \\(Y_0\\) and take \\(R(r) = J_0\\left(\\frac{\\omega}{c} r\\right)\\). The clamped boundary condition \\(R(R) = 0\\) requires \\(J_0\\left(\\frac{\\omega}{c} R\\right) = 0 \\implies \\frac{\\omega}{c} R = j_{0,1} \\approx 2.4048\\). Thus the fundamental frequency is \\(\\omega_{0,1} = \\frac{c j_{0,1}}{R}\\).",
      "بالنسبة لغشاء دائري مثبت عند الحافة، الحل الفيزيائي المنتظم عند المركز هو دالة بيسل من النوع الأول \\(J_0(\\frac{\\omega}{c}r)\\). الشرط الحدي \\(R(R) = 0\\) يتطلب أن يكون \\(\\frac{\\omega}{c}R\\) مساوياً لأول صفر موجب لـ \\(J_0\\)، وهو \\(j_{0,1} \\approx 2.4048\\).",
      "The axisymmetric non-singular radial solution is \\(J_0(kr)\\).",
      "الحل القطري المنتظم والمتناظر دائرياً هو دالة بيسل \\(J_0(kr)\\).")

    # 290: Method of Characteristics for Linear Transport
    q("KAUST-P3-290", "Partial Differential Equations", "Medium",
      "Solve the linear transport PDE \\(u_t + 3 u_x + 2u = 0\\) with initial condition \\(u(x, 0) = x^2\\). What is \\(u(3, 1)\\)?",
      "حل معادلة النقل الخطي \\(u_t + 3 u_x + 2u = 0\\) مع الشرط الابتدائي \\(u(x, 0) = x^2\\). ما قيمة \\(u(3, 1)\\)؟",
      ["\\(0\\)", "\\(9 e^{-2}\\)", "\\(e^{-2}\\)", "\\(4 e^{-2}\\)"],
      0,
      "The characteristic curves satisfy \\(\\frac{dx}{dt} = 3 \\implies x(t) = x_0 + 3t \\implies x_0 = x - 3t\\). Along each characteristic: \\(\\frac{du}{dt} = -2u \\implies u(t) = u(0) e^{-2t} = u_0(x_0) e^{-2t} = (x - 3t)^2 e^{-2t}\\). Evaluating at \\(x = 3, t = 1\\): \\(x_0 = 3 - 3(1) = 0\\). Therefore, \\(u(3, 1) = (0)^2 e^{-2(1)} = 0\\).",
      "معادلة الخصائص هي \\(x = x_0 + 3t \\implies x_0 = x - 3t\\). على طول الخاصية: \\(du/dt = -2u \\implies u = x_0^2 e^{-2t} = (x - 3t)^2 e^{-2t}\\). عند \\(x = 3\\) و \\(t = 1\\) نجد \\(x_0 = 0\\)، وبالتالي فإن \\(u(3, 1) = 0\\).",
      "Find the characteristic starting point \\(x_0 = x - 3t\\).",
      "أوجد النقطة الابتدائية للخاصية \\(x_0 = x - 3t\\).")

    # 291: Laplace Equation Mean Value Property for Balls
    q("KAUST-P3-291", "Partial Differential Equations", "Medium",
      "If \\(u\\) is harmonic in the solid unit ball \\(B_1(0) \\subset \\mathbb{R}^3\\), what is the value of the volume integral \\(\\iiint_{B_1(0)} u(x, y, z) dx dy dz\\) in terms of \\(u(0, 0, 0)\\)?",
      "إذا كانت \\(u\\) دالة توافقية في الكرة المصمتة \\(B_1(0) \\subset \\mathbb{R}^3\\)، فما هي قيمة التكامل الحجمي \\(\\iiint_{B_1(0)} u dx dy dz\\) بدلالة \\(u(0, 0, 0)\\)؟",
      ["\\(\\frac{4}{3}\\pi u(0, 0, 0)\\)",
       "\\(4\\pi u(0, 0, 0)\\)",
       "\\(2\\pi u(0, 0, 0)\\)",
       "\\(0\\)"],
      0,
      "By integrating the spherical mean value property \\(\\iint_{\\partial B_r} u dS = 4\\pi r^2 u(0)\\) with respect to radius \\(r\\) from \\(0\\) to \\(1\\): \\(\\iiint_{B_1} u dV = \\int_0^1 \\left(\\iint_{\\partial B_r} u dS\\right) dr = \\int_0^1 4\\pi r^2 u(0) dr = 4\\pi u(0) \\left[\\frac{r^3}{3}\\right]_0^1 = \\frac{4}{3}\\pi u(0)\\). This is simply the volume of the ball times the value at the center.",
      "بمكاملة خاصية القيمة المتوسطة على الكرات المتراكزة من \\(r = 0\\) إلى \\(1\\): \\(\\int_0^1 4\\pi r^2 u(0) dr = \\frac{4}{3}\\pi u(0)\\). التكامل الحجمي يساوي حجم الكرة مضروباً في قيمة الدالة عند المركز.",
      "The volume integral equals the volume of the ball multiplied by \\(u(0)\\).",
      "التكامل الحجمي لدالة توافقية يساوي حجم الكرة مضروباً في قيمتها عند المركز.")

    # 292: Non-homogeneous Wave Equation (Duhamel)
    q("KAUST-P3-292", "Partial Differential Equations", "Hard",
      "Solve \\(u_{tt} - u_{xx} = 2\\) with initial conditions \\(u(x, 0) = 0\\) and \\(u_t(x, 0) = 0\\). What is \\(u(x, t)\\)?",
      "حل \\(u_{tt} - u_{xx} = 2\\) مع الشروط الابتدائية \\(u(x, 0) = 0\\) و \\(u_t(x, 0) = 0\\). ما هو الحل \\(u(x, t)\\)؟",
      ["\\(u(x, t) = t^2\\)", "\\(u(x, t) = x^2\\)", "\\(u(x, t) = 2t\\)", "\\(u(x, t) = t^2 - x^2\\)"],
      0,
      "Since the forcing term is independent of \\(x\\) and the initial conditions are zero, look for a spatially homogeneous solution \\(u(x, t) = v(t)\\). The PDE reduces to the ODE \\(v''(t) = 2\\) with \\(v(0) = 0, v'(0) = 0\\). Integrating twice gives \\(v'(t) = 2t\\) and \\(v(t) = t^2\\). Indeed, \\(u_{tt} = 2\\) and \\(u_{xx} = 0\\), so \\(u_{tt} - u_{xx} = 2 - 0 = 2\\), satisfying all conditions.",
      "بما أن الدالة غير المتجانسة مستقلة عن \\(x\\) والشروط الابتدائية صفرية، نبحث عن حل يعتمد على الزمن فقط \\(u = v(t)\\). تصبح المعادلة \\(v''(t) = 2\\) مع \\(v(0) = v'(0) = 0\\). بالمكاملة مرتين نجد مباشرة \\(u(x, t) = t^2\\).",
      "Try a solution that depends only on \\(t\\).",
      "جرب حلاً يعتمد على الزمن \\(t\\) فقط.")

    # 293: Liouville's Theorem for Harmonic Functions
    q("KAUST-P3-293", "Partial Differential Equations", "Medium",
      "Liouville's theorem for harmonic functions states that any harmonic function \\(u: \\mathbb{R}^n \\to \\mathbb{R}\\) that is bounded from above (or bounded from below) on the entire space \\(\\mathbb{R}^n\\) must be:",
      "تنص نظرية ليوڤيل للدوال التوافقية على أن أي دالة توافقية \\(u: \\mathbb{R}^n \\to \\mathbb{R}\\) محدودة من الأعلى (أو محدودة من الأدنى) في كامل الفضاء يجب أن تكون:",
      ["A constant function",
       "A linear function",
       "Zero everywhere",
       "A radial function"],
      0,
      "By Harnack's inequality or the Poisson formula on expanding balls, if a harmonic function on \\(\\mathbb{R}^n\\) is bounded from below (or above), its gradient satisfies \\(|\\nabla u(\\mathbf{x})| \\le \\frac{C}{R}\\sup |u| \\to 0\\) as \\(R \\to \\infty\\). Thus \\(\\nabla u = 0\\) everywhere, proving that \\(u\\) is identically constant.",
      "باستخدام متباينة هارناك أو تمثيل بواسون على كرات متسعة، يؤول تدرج الدالة إلى الصفر عندما يؤول نصف القطر إلى اللانهاية. وبالتالي فإن مشتقات الدالة تنعدم في كل مكان، مما يثبت أنها دالة ثابتة.",
      "Recall the analogy to Liouville's theorem in complex analysis.",
      "تذكر الشبه بنظرية ليوڤيل في التحليل العقدي.")

    # 294: Ill-posed Cauchy Problem for Laplace's Equation (Hadamard's Example)
    q("KAUST-P3-294", "Partial Differential Equations", "Hard",
      "In Hadamard's celebrated counterexample showing that the Cauchy problem for Laplace's equation \\(u_{xx} + u_{yy} = 0\\) is ill-posed, consider initial data \\(u(x, 0) = 0\\) and \\(u_y(x, 0) = \\frac{1}{n}\\sin(nx)\\). What is the exact solution \\(u(x, y)\\)?",
      "في مثال هادامارد المضاد الشهير الذي يوضح أن مسألة كوشي لمعادلة لابلاس غير منضبطة، تأمل الشروط الابتدائية \\(u(x, 0) = 0\\) و \\(u_y(x, 0) = \\frac{1}{n}\\sin(nx)\\). ما هو الحل الدقيق \\(u(x, y)\\)؟",
      ["\\(u(x, y) = \\frac{1}{n^2} \\sin(nx) \\sinh(ny)\\)",
       "\\(u(x, y) = \\frac{1}{n^2} \\sin(nx) \\sin(ny)\\)",
       "\\(u(x, y) = \\frac{1}{n} \\cos(nx) e^{-ny}\\)",
       "\\(u(x, y) = \\frac{1}{n^2} \\sin(nx) \\cosh(ny)\\)"],
      0,
      "Separate variables: \\(u(x, y) = X(x)Y(y)\\). With \\(X(x) = \\sin(nx)\\), \\(X'' = -n^2 X\\). Laplace's equation requires \\(X'' Y + X Y'' = 0 \\implies -n^2 X Y + X Y'' = 0 \\implies Y'' - n^2 Y = 0\\). The general solution for \\(Y\\) is \\(A \\cosh(ny) + B \\sinh(ny)\\). With \\(u(x, 0) = 0 \\implies A = 0\\), and \\(u_y(x, 0) = n B \\sin(nx) = \\frac{1}{n}\\sin(nx) \\implies B = \\frac{1}{n^2}\\). Thus \\(u(x, y) = \\frac{1}{n^2}\\sin(nx)\\sinh(ny)\\). For any \\(y > 0\\), \\(\\sinh(ny) \\sim e^{ny}/2\\) grows exponentially, so \\(u(x, y) \\to \\infty\\) as \\(n \\to \\infty\\) despite the initial velocity \\(1/n \\to 0\\).",
      "بفصل المتغيرات نجد \\(Y'' - n^2 Y = 0\\). من الشروط الابتدائية نجد \\(Y(0) = 0\\) و \\(Y'(0) = 1/n\\)، ومنه \\(Y(y) = \\frac{1}{n^2}\\sinh(ny)\\). الحل هو \\(\\frac{1}{n^2}\\sin(nx)\\sinh(ny)\\). هذا الحل ينفجر أسياً عند أي \\(y > 0\\) مبيناً عدم انضباط المسألة.",
      "Solve \\(Y'' - n^2 Y = 0\\) with \\(Y(0) = 0\\) and \\(Y'(0) = 1/n\\).",
      "حل المعادلة التفاضلية لـ \\(Y\\) مع الشروط الابتدائية المعطاة.")

    # 295: Energy Decay in Damped Wave Equation
    q("KAUST-P3-295", "Partial Differential Equations", "Medium",
      "For the damped wave equation \\(u_{tt} + \\gamma u_t = c^2 u_{xx}\\) with \\(\\gamma > 0\\) on a bounded domain with clamped ends \\(u(0, t) = u(L, t) = 0\\), the energy is \\(E(t) = \\frac{1}{2}\\int_0^L (u_t^2 + c^2 u_x^2) dx\\). What is \\(\\frac{dE}{dt}\\)?",
      "لمعادلة الموجة المخمدة \\(u_{tt} + \\gamma u_t = c^2 u_{xx}\\) مع \\(\\gamma > 0\\) وأطراف مقيدة، الطاقة هي \\(E(t) = \\frac{1}{2}\\int_0^L (u_t^2 + c^2 u_x^2) dx\\). ما هي مشتقة الطاقة \\(\\frac{dE}{dt}\\)؟",
      ["\\(\\frac{dE}{dt} = -\\gamma \\int_0^L u_t^2 dx \\le 0\\)",
       "\\(\\frac{dE}{dt} = 0\\)",
       "\\(\\frac{dE}{dt} = -\\gamma E(t)\\)",
       "\\(\\frac{dE}{dt} = +\\gamma \\int_0^L u_t^2 dx\\)"],
      0,
      "Differentiate the energy: \\(\\frac{dE}{dt} = \\int_0^L (u_t u_{tt} + c^2 u_x u_{xt}) dx\\). Integrate the second term by parts: \\(\\int_0^L c^2 u_x u_{xt} dx = [c^2 u_x u_t]_0^L - \\int_0^L c^2 u_{xx} u_t dx\\). Because the ends are clamped, \\(u(0, t) = u(L, t) = 0 \\implies u_t(0, t) = u_t(L, t) = 0\\), so boundary terms vanish. Thus \\(\\frac{dE}{dt} = \\int_0^L u_t (u_{tt} - c^2 u_{xx}) dx\\). From the PDE, \\(u_{tt} - c^2 u_{xx} = -\\gamma u_t\\). Substituting gives \\(\\frac{dE}{dt} = \\int_0^L u_t(-\\gamma u_t) dx = -\\gamma \\int_0^L u_t^2 dx \\le 0\\). Energy dissipates monotonically.",
      "باشتقاق الطاقة والتكامل بالتجزئة مع انعدام الحدود الطرفية، نحصل على \\(\\int u_t(u_{tt} - c^2 u_{xx}) dx\\). بالتعويض من المعادلة الأصلية عن \\(u_{tt} - c^2 u_{xx} = -\\gamma u_t\\)، نجد مباشرة \\(\\frac{dE}{dt} = -\\gamma \\int_0^L u_t^2 dx \\le 0\\). الطاقة تتناقص باطراد بسبب التخميد.",
      "Substitute \\(u_{tt} - c^2 u_{xx} = -\\gamma u_t\\) into the differentiated energy expression.",
      "عوض بقيمة المقدار من المعادلة التفاضلية في مشتق الطاقة.")

    # 296: Radially Symmetric Laplace Equation in n Dimensions
    q("KAUST-P3-296", "Partial Differential Equations", "Hard",
      "For dimension \\(n \\ge 3\\), what is the general radially symmetric solution \\(u(r)\\) to Laplace's equation \\(\\Delta u = 0\\) on \\(\\mathbb{R}^n \\setminus \\{0\\}\\)?",
      "لأي بعد \\(n \\ge 3\\)، ما هو الحل العام المتناظر قطرياً \\(u(r)\\) لمعادلة لابلاس على \\(\\mathbb{R}^n \\setminus \\{0\\}\\)؟",
      ["\\(u(r) = \\frac{A}{r^{n-2}} + B\\)",
       "\\(u(r) = A \\ln r + B\\)",
       "\\(u(r) = \\frac{A}{r^n} + B\\)",
       "\\(u(r) = A r^{2-n} + B r\\)"],
      0,
      "In \\(n\\) dimensions, the radial Laplacian is \\(\\Delta u = u''(r) + \\frac{n-1}{r}u'(r) = 0\\). Divide by \\(u'\\): \\(\\frac{u''}{u'} = -\\frac{n-1}{r} \\implies \\ln u' = -(n-1)\\ln r + C_1 \\implies u'(r) = \\frac{C_2}{r^{n-1}}\\). For \\(n \\ge 3\\), integrating gives \\(u(r) = \\int C_2 r^{1-n} dr = \\frac{C_2}{2-n} r^{2-n} + B = \\frac{A}{r^{n-2}} + B\\).",
      "المؤثر التفاضلي القطري في \\(n\\) من الأبعاد هو \\(u'' + \\frac{n-1}{r}u' = 0\\). بحل المعادلة التفاضلية الأولى لـ \\(u'\\) نجد \\(u'(r) = C/r^{n-1}\\). بالمكاملة لـ \\(n \\ge 3\\) نجد \\(u(r) = \\frac{A}{r^{n-2}} + B\\).",
      "Solve the first-order ODE for \\(v = u'\\): \\(v' + \\frac{n-1}{r}v = 0\\).",
      "حل المعادلة التفاضلية من الرتبة الأولى لـ \\(v = u'\\).")

    # 297: Heat Equation Smoothing Property
    q("KAUST-P3-297", "Partial Differential Equations", "Medium",
      "Let \\(u(x, t)\\) solve the heat equation \\(u_t = u_{xx}\\) for \\(t > 0\\) with initial condition \\(u(x, 0) = \\text{sgn}(x)\\) (which is discontinuous at \\(x = 0\\)). What is the smoothness of \\(u(x, t)\\) for any \\(t > 0\\)?",
      "لتكن \\(u(x, t)\\) حلاً لمعادلة الحرارة لـ \\(t > 0\\) مع شرط ابتدائي غير متصل \\(u(x, 0) = \\text{sgn}(x)\\). ما هي درجة ملاسة \\(u(x, t)\\) لأي زمن موجب \\(t > 0\\)؟",
      ["\\(u(x, t) \\in C^\\infty\\) (infinitely differentiable, in fact real analytic)",
       "Discontinuous at \\(x = 0\\) for all \\(t > 0\\)",
       "Only once continuously differentiable \\(C^1\\)",
       "Continuous but nowhere differentiable"],
      0,
      "The heat equation possesses an instantaneous infinite smoothing property. The solution is given by convolution with the smooth Gaussian heat kernel \\(u(x, t) = \\Phi(\\cdot, t) * u_0\\). Because the heat kernel \\(\\Phi(x, t)\\) is infinitely differentiable and real analytic for \\(t > 0\\), differentiation can be passed onto the kernel: \\(\\partial_x^k u = (\\partial_x^k \\Phi) * u_0\\). Hence, any jump discontinuity or rough feature in the initial data is instantly smoothed into a \\(C^\\infty\\) real analytic function for any \\(t > 0\\).",
      "تمتلك معادلة الحرارة خاصية التنعيم الفوري اللانهائي. بما أن الحل هو التفاف مع نواة الحرارة الغاوسية التحليلية، فإن أي انقطاع في الشروط الابتدائية يختفي فوراً ويصبح الحل أملس من الصنف \\(C^\\infty\\) وتحليلياً حقيقياً عند أي لحظة \\(t > 0\\).",
      "Convolving any bounded function with the Gaussian heat kernel yields a \\(C^\\infty\\) function.",
      "التفاف أي دالة محدودة مع نواة الحرارة الغاوسية ينتج دالة ملساء تماماً.")

    # 298: Wave Equation on Half-Line (Odd Extension)
    q("KAUST-P3-298", "Partial Differential Equations", "Hard",
      "To solve the wave equation \\(u_{tt} = c^2 u_{xx}\\) on the half-line \\(x > 0, t > 0\\) with fixed Dirichlet boundary condition \\(u(0, t) = 0\\) and initial data \\(u(x, 0) = \\phi(x), u_t(x, 0) = 0\\), which mathematical technique is used?",
      "لحل معادلة الموجة على نصف المستقيم \\(x > 0\\) مع الشرط الحدي الثابت \\(u(0, t) = 0\\) وشروط ابتدائية، أي تقنية رياضية تُستخدم؟",
      ["Odd reflection extension of the initial data across \\(x = 0\\)",
       "Even reflection extension of the initial data across \\(x = 0\\)",
       "Fourier transform on the entire real line without extension",
       "Periodic extension of period \\(c\\)"],
      0,
      "To preserve the Dirichlet boundary condition \\(u(0, t) = 0\\) automatically, extend the initial displacement \\(\\phi(x)\\) as an odd function: \\(\\phi_{\\text{odd}}(x) = \\phi(x)\\) for \\(x > 0\\), and \\(\\phi_{\\text{odd}}(x) = -\\phi(-x)\\) for \\(x < 0\\). Substituting into d'Alembert's formula gives \\(u(0, t) = \\frac{1}{2}[\\phi_{\\text{odd}}(-ct) + \\phi_{\\text{odd}}(ct)] = \\frac{1}{2}[-\\phi(ct) + \\phi(ct)] = 0\\). Thus the wave reflects off the boundary with an inverted sign.",
      "لضمان تحقق شرط ديريكليه \\(u(0, t) = 0\\) تلقائياً، نمدد الدالة الابتدائية كدالة فردية: \\(\\phi_{\\text{odd}}(-x) = -\\phi(x)\\). عند تطبيق صيغة دالمبير عند \\(x = 0\\) نجد \\([\\phi(-ct) + \\phi(ct)]/2 = 0\\)، مما يفسر انعكاس الموجة مع انقلاب إشارتها.",
      "An odd function satisfies \\(f(-x) = -f(x)\\), which guarantees \\(f(0) = 0\\).",
      "الدالة الفردية تحقق \\(f(-x) = -f(x)\\) مما يضمن انعدام الدالة عند الصفر.")

    # 299: Wave Equation on Half-Line (Even Extension for Neumann)
    q("KAUST-P3-299", "Partial Differential Equations", "Hard",
      "Similarly, if the half-line wave equation has a free boundary (Neumann condition) \\(u_x(0, t) = 0\\), which extension of the initial data is required?",
      "بالمثل، إذا كان لمعادلة الموجة على نصف المستقيم طرف حر (شرط نيومان) \\(u_x(0, t) = 0\\)، فما هو التمديد المطلوب للشروط الابتدائية؟",
      ["Even reflection extension across \\(x = 0\\)",
       "Odd reflection extension across \\(x = 0\\)",
       "Zero extension for \\(x < 0\\)",
       "Linear extrapolation"],
      0,
      "To satisfy the Neumann condition \\(u_x(0, t) = 0\\), extend the initial data \\(\\phi(x)\\) as an even function: \\(\\phi_{\\text{even}}(x) = \\phi(|x|)\\). Then \\(\\phi_{\\text{even}}'(x)\\) is an odd function, so \\(\\phi_{\\text{even}}'(0) = 0\\). In d'Alembert's formula, \\(u_x(0, t) = \\frac{1}{2}[\\phi_{\\text{even}}'(-ct) + \\phi_{\\text{even}}'(ct)] = 0\\). The reflected wave returns with the same sign (no phase inversion).",
      "لتحقيق شرط نيومان \\(u_x(0, t) = 0\\)، نمدد الشروط الابتدائية كدالة زوجية \\(\\phi(-x) = \\phi(x)\\). مشتق الدالة الزوجية دالة فردية ينعدم عند الصفر، مما يضمن \\(u_x(0, t) = 0\\) وتنعكس الموجة بنفس الإشارة دون انقلاب.",
      "The derivative of an even function is an odd function, which vanishes at zero.",
      "مشتق الدالة الزوجية هو دالة فردية تنعدم عند نقطة الأصل.")

    # 300: Burgers' Shock Formation Time for Sinusoidal Wave
    q("KAUST-P3-300", "Partial Differential Equations", "Hard",
      "For the inviscid Burgers' equation \\(u_t + u u_x = 0\\) with initial condition \\(u(x, 0) = \\sin x\\), what is the shock formation time \\(T^*\\)?",
      "لمعادلة بيرغرز غير اللزجة \\(u_t + u u_x = 0\\) مع الشرط الابتدائي \\(u(x, 0) = \\sin x\\)، ما هو زمن تشكل الصدمة \\(T^*\\)؟",
      ["\\(T^* = 1\\)", "\\(T^* = \\pi\\)", "\\(T^* = 2\\)", "\\(T^* = 1/2\\)"],
      0,
      "The breaking time formula for \\(u_t + u u_x = 0\\) is \\(T^* = \\frac{-1}{\\min_x u_0'(x)}\\). For \\(u_0(x) = \\sin x\\), the derivative is \\(u_0'(x) = \\cos x\\). The minimum value of \\(\\cos x\\) is \\(-1\\), attained at \\(x = \\pi\\). Therefore, \\(T^* = \\frac{-1}{-1} = 1\\). At \\(t = 1\\), the wave steepens infinitely at \\(x = \\pi\\), forming the first shock discontinuity.",
      "قانون زمن تشكل الصدمة هو \\(T^* = -1 / \\min u_0'(x)\\). مشتق \\(\\sin x\\) هو \\(\\cos x\\)، وأصغر قيمة له هي \\(-1\\) عند \\(x = \\pi\\). بالتالي فإن زمن تشكل الصدمة هو \\(T^* = -1 / (-1) = 1\\).",
      "Find the minimum slope of \\(u_0(x) = \\sin x\\).",
      "أوجد أصغر ميل للدالة الابتدائية \\(\\sin x\\).")

    return questions

if __name__ == "__main__":
    qs = get_p3_part_a()
    print(f"Loaded {len(qs)} questions for Phase 3 Part A.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=251):
        expected_id = f"KAUST-P3-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 3 Part A questions successfully verified!")
