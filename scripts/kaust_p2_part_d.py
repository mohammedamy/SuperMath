#!/usr/bin/env python3
"""
KAUST Phase 2 Questions Part D: 401 to 450
Complex Analysis & Advanced Probability/Statistics:
Cauchy-Riemann equations, Cauchy's Integral Formula, Residue Theorem,
Laurent series, Conformal Mappings, Maximum Modulus Principle,
Rouche's Theorem, Bivariate Normal, MGFs/Characteristic Functions,
Order Statistics, Inequalities (Markov, Chebyshev, Chernoff), Central Limit Theorem.
Authentic lineages: MIT 18.04 / 18.440, Cambridge Tripos Part IB, Harvard Math 113, Putnam, Stanford STATS 200.
"""

def get_p2_part_d():
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

    # 401: Cauchy Integral Formula with SVG
    svg_contour = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-60 -60 120 120' width='100%' height='100%' style='background:#0d1117;'>
  <line x1='-55' y1='0' x2='55' y2='0' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-55' x2='0' y2='55' stroke='#8b949e' stroke-width='1.5'/>
  <!-- Circle of radius 40 (representing |z| = 2) -->
  <circle cx='0' cy='0' r='40' fill='rgba(88, 166, 255, 0.15)' stroke='#58a6ff' stroke-width='2'/>
  <!-- Pole at z = 1 (20px) -->
  <circle cx='20' cy='0' r='3.5' fill='#f85149'/>
  <text x='16' y='-8' fill='#f85149' font-size='10' font-family='sans-serif'>z = 1</text>
  <!-- Direction arrow on circle -->
  <polygon points='0,-40 -6,-45 -4,-37' fill='#58a6ff'/>
  <text x='-38' y='-38' fill='#8b949e' font-size='10' font-family='sans-serif'>|z| = 2</text>
</svg>"""
    q("KAUST-P2-401", "Complex Analysis", "Medium",
      "Evaluate the contour integral \\(\\oint_{|z|=2} \\frac{e^{3z}}{z - 1} dz\\) oriented counterclockwise.",
      "احسب التكامل الخطي العقدي \\(\\oint_{|z|=2} \\frac{e^{3z}}{z - 1} dz\\) بالاتجاه الموجب عكس عقارب الساعة.",
      ["\\(2\\pi i e^3\\)", "\\(\\pi i e^3\\)", "\\(0\\)", "\\(6\\pi i\\)"],
      0,
      "The integrand \\(f(z) = \\frac{e^{3z}}{z - 1}\\) has a simple pole at \\(z = 1\\), which lies inside the circle \\(|z| = 2\\). By Cauchy's Integral Formula, \\(\\oint_C \\frac{g(z)}{z - z_0} dz = 2\\pi i g(z_0)\\), where \\(g(z) = e^{3z}\\) is holomorphic everywhere. Evaluating at \\(z_0 = 1\\) gives \\(g(1) = e^3\\). Therefore, the integral is \\(2\\pi i e^3\\).",
      "الدالة المكاملة لها قطب بسيط عند \\(z = 1\\) يقع داخل الدائرة \\(|z| = 2\\). بتطبيق صيغة كوشي التكاملية: \\(\\oint_C \\frac{g(z)}{z-z_0} dz = 2\\pi i g(z_0)\\) حيث \\(g(z) = e^{3z}\\). بالتعويض عند \\(z_0 = 1\\) نجد \\(g(1) = e^3\\). بالتالي قيمة التكامل هي \\(2\\pi i e^3\\).",
      "Apply Cauchy's Integral Formula: \\(\\oint_C \\frac{g(z)}{z-z_0} dz = 2\\pi i g(z_0)\\).",
      "طبق صيغة كوشي التكاملية للدوال التحليلية.",
      diagram=svg_contour)

    # 402: Residue at a Second-Order Pole
    q("KAUST-P2-402", "Complex Analysis", "Medium",
      "Find the residue of \\(f(z) = \\frac{\\cos z}{(z - \\pi)^2}\\) at \\(z = \\pi\\).",
      "أوجد الباقي (residue) للدالة \\(f(z) = \\frac{\\cos z}{(z - \\pi)^2}\\) عند \\(z = \\pi\\).",
      ["\\(0\\)", "\\(-1\\)", "\\(1\\)", "\\(-\\pi\\)"],
      0,
      "At \\(z = \\pi\\), the function has a pole of order 2. The residue formula for a pole of order 2 is \\(\\text{Res}(f, \\pi) = \\lim_{z \\to \\pi} \\frac{d}{dz}\\left((z - \\pi)^2 f(z)\\right) = \\lim_{z \\to \\pi} \\frac{d}{dz}(\\cos z) = \\lim_{z \\to \\pi} (-\\sin z) = -\\sin(\\pi) = 0\\).",
      "عند \\(z = \\pi\\)، تمتلك الدالة قطباً من الرتبة الثانية. قانون الباقي لقطب من الرتبة الثانية هو \\(\\lim_{z \\to \\pi} \\frac{d}{dz}((z-\\pi)^2 f(z)) = \\lim_{z \\to \\pi} (-\\sin z) = -\\sin(\\pi) = 0\\).",
      "Use the residue formula for a pole of order 2: \\(\\lim_{z \\to z_0} \\frac{d}{dz}((z-z_0)^2 f(z))\\).",
      "استخدم قانون الباقي لقطب من الرتبة الثانية بالتفاضل مرة واحدة.")

    # 403: Real Integral via Residue Calculus
    q("KAUST-P2-403", "Complex Analysis", "Hard",
      "Compute the improper real integral \\(\\int_{-\\infty}^\\infty \\frac{1}{(x^2 + 1)(x^2 + 4)} dx\\) using contour integration.",
      "احسب التكامل الحقيقي المعتل \\(\\int_{-\\infty}^\\infty \\frac{1}{(x^2 + 1)(x^2 + 4)} dx\\) باستخدام تكامل المسار العقدي.",
      ["\\(\\frac{\\pi}{6}\\)", "\\(\\frac{\\pi}{3}\\)", "\\(\\frac{\\pi}{12}\\)", "\\(\\frac{\\pi}{2}\\)"],
      0,
      "Close the contour with a semicircle in the upper half-plane. The poles of \\(f(z) = \\frac{1}{(z^2+1)(z^2+4)}\\) in the upper half-plane are at \\(z = i\\) and \\(z = 2i\\). The residues are: \\(\\text{Res}(f, i) = \\frac{1}{2i(i^2 + 4)} = \\frac{1}{2i(3)} = \\frac{1}{6i}\\); and \\(\\text{Res}(f, 2i) = \\frac{1}{((2i)^2 + 1)(2(2i))} = \\frac{1}{(-3)(4i)} = -\\frac{1}{12i}\\). Sum of residues: \\(\\frac{1}{6i} - \\frac{1}{12i} = \\frac{1}{12i}\\). By the Residue Theorem: \\(\\int_{-\\infty}^\\infty f(x) dx = 2\\pi i \\sum \\text{Res} = 2\\pi i \\left(\\frac{1}{12i}\\right) = \\frac{2\\pi}{12} = \\frac{\\pi}{6}\\).",
      "نغلق المسار بنصف دائرة في النصف العلوي للمستوى. الأقطاب العلوية هي عند \\(z = i\\) و \\(z = 2i\\). البواقي هي \\(\\frac{1}{6i}\\) و \\(-\\frac{1}{12i}\\). مجموعهما \\(\\frac{1}{12i}\\). بنظرية البواقي: التكامل يساوي \\(2\\pi i \\times \\frac{1}{12i} = \\frac{\\pi}{6}\\).",
      "Sum the residues at the two poles in the upper half-plane: \\(z = i\\) and \\(z = 2i\\).",
      "اجمع البواقي عند القطبين الواقعين في النصف العلوي للمستوى العقدي.")

    # 404: Möbius Transformation Mapping
    q("KAUST-P2-404", "Complex Analysis", "Hard",
      "Find the Möbius transformation \\(w = f(z) = \\frac{az+b}{cz+d}\\) that maps the points \\(z_1 = 0, z_2 = 1, z_3 = \\infty\\) to \\(w_1 = -1, w_2 = 0, w_3 = 1\\) respectively.",
      "أوجد تحويل موبيوس \\(w = \\frac{az+b}{cz+d}\\) الذي ينقل النقاط \\(z_1 = 0, z_2 = 1, z_3 = \\infty\\) إلى \\(w_1 = -1, w_2 = 0, w_3 = 1\\) على الترتيب.",
      ["\\(w = \\frac{z - 1}{z + 1}\\)", "\\(w = \\frac{z + 1}{z - 1}\\)", "\\(w = \\frac{2z - 1}{z + 1}\\)", "\\(w = \\frac{1 - z}{1 + z}\\)"],
      0,
      "Use the cross-ratio identity: \\(\\frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \\frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}\\). With \\(z_3 = \\infty\\), the right side simplifies to \\(\\frac{z - z_1}{z_2 - z_1} = \\frac{z - 0}{1 - 0} = z\\). Substituting the \\(w\\) values: \\(\\frac{(w - (-1))(0 - 1)}{(w - 1)(0 - (-1))} = \\frac{(w + 1)(-1)}{(w - 1)(1)} = -\\frac{w + 1}{w - 1} = z \\implies -(w+1) = z(w-1) = zw - z \\implies z - 1 = w(z + 1) \\implies w = \\frac{z - 1}{z + 1}\\).",
      "باستخدام النسبة التوافقية (cross-ratio) للنقاط الأربع مع \\(z_3 = \\infty\\): نجد \\(z = -\\frac{w+1}{w-1}\\). بحل المعادلة بالنسبة لـ \\(w\\) نصل مباشرة إلى \\(w = \\frac{z-1}{z+1}\\).",
      "Use the cross-ratio formula preserving collinear and circular configurations.",
      "استخدم صيغة النسبة التقاطعية الثلاثية الثابتة تحت تحويلات موبيوس.")

    # 405: Rouché's Theorem - Root Counting
    q("KAUST-P2-405", "Complex Analysis", "Hard",
      "Using Rouché's theorem, determine how many zeros the polynomial \\(p(z) = z^5 + 3z^2 + 1\\) has inside the unit circle \\(|z| < 1\\).",
      "باستخدام نظرية روشيه، حدد كم صفراً تمتلكه كثيرة الحدود \\(p(z) = z^5 + 3z^2 + 1\\) داخل قرص الوحدة \\(|z| < 1\\).",
      ["\\(2\\)", "\\(5\\)", "\\(3\\)", "\\(0\\)"],
      0,
      "On the boundary \\(|z| = 1\\), choose \\(f(z) = 3z^2\\) and \\(g(z) = z^5 + 1\\). Then \\(|f(z)| = 3|z|^2 = 3\\). By triangle inequality, \\(|g(z)| = |z^5 + 1| \\le |z|^5 + 1 = 1 + 1 = 2\\). Thus \\(|g(z)| < |f(z)|\\) on \\(|z| = 1\\). By Rouché's theorem, \\(p(z) = f(z) + g(z)\\) and \\(f(z)\\) have the same number of zeros inside \\(|z| < 1\\). The function \\(f(z) = 3z^2\\) has a double root at \\(z = 0\\), which means it has exactly 2 zeros inside \\(|z| < 1\\). Therefore, \\(p(z)\\) has exactly 2 zeros inside the unit circle.",
      "على المحيط \\(|z| = 1\\)، نختار \\(f(z) = 3z^2\\) و \\(g(z) = z^5 + 1\\). نجد \\(|f(z)| = 3\\) و \\(|g(z)| \\le 2\\). بما أن \\(|g(z)| < |f(z)|\\)، فإن لـ \\(p(z)\\) و \\(f(z)\\) نفس عدد الأصفار داخل القرص حسب نظرية روشيه. أصفار \\(3z^2\\) هما صفران مكرران عند الأصل. إذن هناك صفران بالضبط.",
      "Compare the magnitude of the term \\(3z^2\\) against the sum of the remaining terms on \\(|z| = 1\\).",
      "قارن مقدار الحد \\(3z^2\\) بمجموع الحدود الأخرى على محيط دائرة الوحدة.")

    # 406: Laurent Series Annulus
    q("KAUST-P2-406", "Complex Analysis", "Hard",
      "In the Laurent series expansion of \\(f(z) = \\frac{1}{(z - 1)(z - 2)}\\) valid in the annular region \\(1 < |z| < 2\\), what is the coefficient of \\(z^{-1}\\)?",
      "في نشر متسلسلة لوران للدالة \\(f(z) = \\frac{1}{(z - 1)(z - 2)}\\) في المنطقة الحلقية \\(1 < |z| < 2\\)، ما هو معامل \\(z^{-1}\\)؟",
      ["\\(-1\\)", "\\(1\\)", "\\(0\\)", "\\(1/2\\)"],
      0,
      "Partial fractions: \\(f(z) = \\frac{1}{z - 2} - \\frac{1}{z - 1}\\). For \\(|z| > 1\\): \\(-\\frac{1}{z - 1} = -\\frac{1}{z}\\frac{1}{1 - 1/z} = -\\frac{1}{z}\\sum_{n=0}^\\infty z^{-n} = -\\sum_{n=1}^\\infty z^{-n}\\). For \\(|z| < 2\\): \\(\\frac{1}{z - 2} = -\\frac{1}{2}\\frac{1}{1 - z/2} = -\\sum_{n=0}^\\infty \\frac{z^n}{2^{n+1}}\\). Combining them gives the complete Laurent series in \\(1 < |z| < 2\\): \\(f(z) = -\\sum_{n=1}^\\infty z^{-n} - \\sum_{n=0}^\\infty \\frac{z^n}{2^{n+1}}\\). The coefficient of \\(z^{-1}\\) comes from the \\(n=1\\) term of the first sum, which is \\(-1\\).",
      "بالكسور الجزئية: \\(f(z) = \\frac{1}{z-2} - \\frac{1}{z-1}\\). للكسر الأول مع \\(|z| < 2\\) ننشر بالقوى الموجبة. وللكسر الثاني مع \\(|z| > 1\\) ننشر بقوى \\(1/z\\): \\(-\\frac{1}{z}(1 + 1/z + \\dots) = -z^{-1} - z^{-2} - \\dots\\). معامل \\(z^{-1}\\) هو \\(-1\\).",
      "Expand \\(\\frac{1}{z-1}\\) in powers of \\(1/z\\) because \\(|z| > 1\\).",
      "انشر \\(\\frac{1}{z-1}\\) بقوى \\(1/z\\) لأن \\(|z| > 1\\).")

    # 407: Maximum Modulus Principle
    q("KAUST-P2-407", "Complex Analysis", "Medium",
      "Let \\(f(z) = z^2 - 2z\\) on the closed unit disc \\(D = \\{z \\in \\mathbb{C} : |z| \\le 1\\}\\). What is the maximum value of \\(|f(z)|\\) on \\(D\\)?",
      "لتكن \\(f(z) = z^2 - 2z\\) على القرص المغلق \\(D = \\{z \\in \\mathbb{C} : |z| \\le 1\\}\\). ما هي القيمة العظمى لـ \\(|f(z)|\\) على \\(D\\)؟",
      ["\\(3\\)", "\\(1\\)", "\\(2\\)", "\\(\\sqrt{5}\\)"],
      0,
      "By the Maximum Modulus Principle, the maximum of \\(|f(z)|\\) must occur on the boundary \\(|z| = 1\\). On the boundary, let \\(z = e^{i\\theta}\\). Then \\(|f(e^{i\\theta})|^2 = |e^{2i\\theta} - 2e^{i\\theta}|^2 = |e^{i\\theta}(e^{i\\theta} - 2)|^2 = |e^{i\\theta} - 2|^2 = (\\cos\\theta - 2)^2 + \\sin^2\\theta = \\cos^2\\theta - 4\\cos\\theta + 4 + \\sin^2\\theta = 5 - 4\\cos\\theta\\). This is maximized when \\(\\cos\\theta = -1\\) (i.e., at \\(z = -1\\)), giving maximum value \\(\\sqrt{5 - 4(-1)} = \\sqrt{9} = 3\\).",
      "حسب مبدأ المقياس الأعظم، تقع القيمة العظمى لمقياس الدالة التحليلية على المحيط \\(|z| = 1\\). بوضع \\(z = e^{i\\theta}\\) نجد \\(|f(z)|^2 = 5 - 4\\cos\\theta\\). تكون هذه القيمة في نهايتها العظمى عندما \\(\\cos\\theta = -1\\) (أي عند \\(z = -1\\))، فتكون القيمة العظمى هي \\(\\sqrt{9} = 3\\).",
      "Parametrize the boundary as \\(z = e^{i\\theta}\\) and maximize \\(5 - 4\\cos\\theta\\).",
      "مثل المحيط بـ \\(z = e^{i\\theta}\\) وأوجد النهاية العظمى للمقدار.")

    # 408: Schwarz Lemma
    q("KAUST-P2-408", "Complex Analysis", "Hard",
      "Let \\(f: \\mathbb{D} \\to \\mathbb{D}\\) be a holomorphic map on the open unit disc with \\(f(0) = 0\\). If \\(f(1/2) = i/2\\), what can be said about \\(f(z)\\) everywhere in \\(\\mathbb{D}\\)?",
      "لتكن \\(f: \\mathbb{D} \\to \\mathbb{D}\\) دالة تحليلية على قرص الوحدة المفتوح تحقق \\(f(0) = 0\\). إذا كان \\(f(1/2) = i/2\\)، فما الذي يمكن استنتاجه حول \\(f(z)\\) في كامل القرص؟",
      ["\\(f(z) = iz\\) (a pure rotation)",
       "\\(|f(z)| < |z|\\) strictly for all \\(z \\neq 1/2\\)",
       "\\(f(z) = z^2\\)",
       "\\(f(z) = 0\\)"],
      0,
      "Schwarz's Lemma states that if \\(f: \\mathbb{D} \\to \\mathbb{D}\\) is holomorphic with \\(f(0) = 0\\), then \\(|f(z)| \\le |z|\\) for all \\(z \\in \\mathbb{D}\\). Furthermore, if equality \\(|f(z_0)| = |z_0|\\) holds for any non-zero point \\(z_0 \\in \\mathbb{D}\\), then \\(f(z) = e^{i\\alpha} z\\) for some real constant \\(\\alpha\\). Here, \\(|f(1/2)| = |i/2| = 1/2 = |1/2|\\). Because equality holds at \\(z = 1/2\\), \\(f(z) = e^{i\\alpha} z\\). Substituting \\(z = 1/2\\) gives \\(e^{i\\alpha}(1/2) = i/2 \\implies e^{i\\alpha} = i\\). Thus \\(f(z) = iz\\).",
      "حسب توطئة شفارتز، إذا كان \\(|f(z_0)| = |z_0|\\) عند أي نقطة غير صفرية، فإن الدالة هي بالضرورة دوران \\(f(z) = e^{i\\alpha} z\\). بما أن \\(|f(1/2)| = 1/2\\)، فإن المساواة متحققة. وبالتعويض نجد \\(e^{i\\alpha} = i\\)، إذن \\(f(z) = iz\\).",
      "Notice that \\(|f(1/2)| = |1/2|\\) reaches the Schwarz lemma bound.",
      "لاحظ أن مقياس الدالة عند 1/2 يبلغ الحد الأقصى لتوطئة شفارتز.")

    # 409: Bivariate Normal Conditional Distribution
    q("KAUST-P2-409", "Probability & Statistics", "Hard",
      "Let \\((X, Y)\\) be bivariate normal with means \\(\\mu_X = 10, \\mu_Y = 20\\), variances \\(\\sigma_X^2 = 4, \\sigma_Y^2 = 9\\), and correlation \\(\\rho = 0.5\\). What is the conditional expectation \\(\\mathbb{E}[Y \\mid X = 12]\\)?",
      "ليكن \\((X, Y)\\) زوجاً عشوائياً طبيعياً ثنائياً بمتوسطين \\(\\mu_X = 10, \\mu_Y = 20\\) وتباينين \\(\\sigma_X^2 = 4, \\sigma_Y^2 = 9\\) ومعامل ارتباط \\(\\rho = 0.5\\). ما هو التوقع الشرطي \\(\\mathbb{E}[Y \\mid X = 12]\\)؟",
      ["\\(21.5\\)", "\\(21.0\\)", "\\(22.0\\)", "\\(23.0\\)"],
      0,
      "For a bivariate normal distribution, the conditional expectation is given by \\(\\mathbb{E}[Y \\mid X = x] = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X}(x - \\mu_X)\\). Here \\(\\mu_Y = 20\\), \\(\\rho = 0.5\\), \\(\\sigma_Y = \\sqrt{9} = 3\\), \\(\\sigma_X = \\sqrt{4} = 2\\), and \\(x = 12\\). Substituting these values: \\(\\mathbb{E}[Y \\mid X = 12] = 20 + 0.5 \\left(\\frac{3}{2}\\right)(12 - 10) = 20 + 0.5 \\times 1.5 \\times 2 = 20 + 1.5 = 21.5\\).",
      "في التوزيع الطبيعي الثنائي، التوقع الشرطي هو \\(\\mathbb{E}[Y \\mid X = x] = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X}(x - \\mu_X)\\). هنا \\(\\sigma_X = 2\\) و \\(\\sigma_Y = 3\\). بالتعويض: \\(20 + 0.5 \\times (3/2) \\times (12 - 10) = 20 + 1.5 = 21.5\\).",
      "Apply the linear regression formula for conditional expectation of bivariate normal variables.",
      "طبق صيغة الانحدار الخطي للتوقع الشرطي في التوزيع الطبيعي الثنائي.")

    # 410: Bivariate Normal Conditional Variance
    q("KAUST-P2-410", "Probability & Statistics", "Medium",
      "Under the same bivariate normal setup (\\(\\sigma_Y^2 = 9, \\rho = 0.5\\)), what is the conditional variance \\(\\text{Var}(Y \\mid X = x)\\)?",
      "في نفس النموذج الطبيعي الثنائي السابق (\\(\\sigma_Y^2 = 9, \\rho = 0.5\\))، ما هو التباين الشرطي \\(\\text{Var}(Y \\mid X = x)\\)؟",
      ["\\(6.75\\)", "\\(4.50\\)", "\\(9.00\\)", "\\(2.25\\)"],
      0,
      "The conditional variance of a bivariate normal distribution is homoscedastic (independent of the conditioning value \\(x\\)) and given by \\(\\text{Var}(Y \\mid X = x) = \\sigma_Y^2 (1 - \\rho^2)\\). Here \\(\\sigma_Y^2 = 9\\) and \\(\\rho = 0.5\\), so \\(\\rho^2 = 0.25\\). Thus \\(\\text{Var}(Y \\mid X = x) = 9(1 - 0.25) = 9 \\times 0.75 = 6.75\\).",
      "التباين الشرطي للتوزيع الطبيعي الثنائي ثابت ولا يعتمد على قيمة \\(x\\)، ويعطى بـ \\(\\sigma_Y^2(1 - \\rho^2)\\). بالتعويض: \\(9 \\times (1 - 0.25) = 9 \\times 0.75 = 6.75\\).",
      "Use \\(\\text{Var}(Y \\mid X = x) = \\sigma_Y^2 (1 - \\rho^2)\\).",
      "استخدم قانون التباين الشرطي \\(\\sigma_Y^2 (1 - \\rho^2)\\).")

    # 411: Order Statistics Distribution
    q("KAUST-P2-411", "Probability & Statistics", "Hard",
      "Let \\(X_1, X_2, \\dots, X_n\\) be i.i.d. continuous random variables with CDF \\(F(x)\\) and PDF \\(f(x)\\). What is the probability density function \\(f_{(k)}(x)\\) of the \\(k\\)-th order statistic \\(X_{(k)}\\)?",
      "لتكن \\(X_1, \\dots, X_n\\) متغيرات عشوائية مستقلة ومتطابقة التوزيع بدالة توزيع تراكمي \\(F(x)\\) وكثافة \\(f(x)\\). ما هي دالة كثافة الاحتمال \\(f_{(k)}(x)\\) لإحصاء الترتيب الـ \\(k\\)؟",
      ["\\(\\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)\\)",
       "\\(\\frac{n!}{k!(n-k)!} [F(x)]^k [1 - F(x)]^{n-k}\\)",
       "\\(n [F(x)]^{n-1} f(x)\\)",
       "\\(\\frac{1}{n} [F(x)]^{k-1} f(x)\\)"],
      0,
      "For \\(X_{(k)}\\) to fall in the infinitesimal interval \\([x, x+dx]\\): exactly 1 variable must fall in \\([x, x+dx]\\) (with probability \\(f(x)dx\\)), exactly \\(k-1\\) variables must be strictly less than \\(x\\) (probability \\([F(x)]^{k-1}\\)), and the remaining \\(n-k\\) variables must be strictly greater than \\(x\\) (probability \\([1-F(x)]^{n-k}\\)). The multinomial coefficient for assigning the \\(n\\) distinct variables to these three outcomes is \\(\\frac{n!}{(k-1)! 1! (n-k)!}\\). Multiplying yields \\(f_{(k)}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)\\).",
      "لكي تقع القيمة في الفترة \\([x, x+dx]\\): يجب أن يقع متغير واحد فيها، و \\(k-1\\) متغيرات قبل \\(x\\)، و \\(n-k\\) متغيرات بعد \\(x\\). معامل التباديل متعدد الحدود هو \\(\\frac{n!}{(k-1)!(n-k)!}\\). بالضرب في الاحتمالات ينتج القانون المطلوب.",
      "Think of the trinomial partition: \\(k-1\\) below, 1 at \\(x\\), and \\(n-k\\) above.",
      "فكر في التقسيم الثلاثي: \\(k-1\\) قبله، وواحد عنده، و \\(n-k\\) بعده.")

    # 412: Characteristic Function of Cauchy Distribution
    q("KAUST-P2-412", "Probability & Statistics", "Hard",
      "What is the characteristic function \\(\\phi_X(t) = \\mathbb{E}[e^{itX}]\\) of a standard Cauchy random variable with density \\(f(x) = \\frac{1}{\\pi(1 + x^2)}\\)?",
      "ما هي الدالة المميزة \\(\\phi_X(t) = \\mathbb{E}[e^{itX}]\\) لمتغير كوشي العشوائي القياسي ذي الكثافة \\(f(x) = \\frac{1}{\\pi(1 + x^2)}\\)؟",
      ["\\(\\phi_X(t) = e^{-|t|}\\)", "\\(\\phi_X(t) = e^{-t^2/2}\\)", "\\(\\phi_X(t) = \\frac{1}{1 + t^2}\\)", "\\(\\phi_X(t) = e^{-t}\\)"],
      0,
      "Compute \\(\\phi_X(t) = \\frac{1}{\\pi}\\int_{-\\infty}^\\infty \\frac{e^{itx}}{1 + x^2} dx\\). For \\(t > 0\\), close the contour in the upper half-plane with a semicircle. The only pole in the UHP is at \\(x = i\\). The residue is \\(\\text{Res}\\left(\\frac{e^{itz}}{(z-i)(z+i)}, i\\right) = \\frac{e^{it(i)}}{2i} = \\frac{e^{-t}}{2i}\\). By the Residue Theorem: \\(\\int_{-\\infty}^\\infty = 2\\pi i \\left(\\frac{e^{-t}}{2i}\\right) = \\pi e^{-t}\\). Dividing by \\(\\pi\\) gives \\(e^{-t}\\). For general real \\(t\\), by symmetry (the distribution is symmetric, so \\(\\phi(t)\\) is real and even), \\(\\phi_X(t) = e^{-|t|}\\).",
      "بحساب التكامل العقدي باستخدام نظرية البواقي مع إغلاق المسار في النصف العلوي لـ \\(t > 0\\)، نجد قطباً عند \\(i\\) بباقٍ \\(e^{-t}/(2i)\\). التكامل يساوي \\(\\pi e^{-t}\\)، وبالقسمة على \\(\\pi\\) نحصل على \\(e^{-t}\\). ولأن التوزيع متناظر، فإن الدالة زوجية: \\(\\phi(t) = e^{-|t|}\\).",
      "Use contour integration and note that the characteristic function of any symmetric real distribution is an even function of \\(t\\).",
      "استخدم التكامل العقدي وتذكر أن الدالة المميزة للتوزيع المتناظر دالة زوجية.")

    # 413: Chernoff Bound Derivation
    q("KAUST-P2-413", "Probability & Statistics", "Hard",
      "The Chernoff bound for the tail probability of a random variable \\(X\\) states that for any \\(a\\) and any \\(t > 0\\):",
      "ينص حصر تشيرنوف لاحتمال ذيل المتغير العشوائي \\(X\\) على أنه لأي \\(a\\) ولأي \\(t > 0\\):",
      ["\\(\\mathbb{P}(X \\ge a) \\le e^{-ta} M_X(t)\\)",
       "\\(\\mathbb{P}(X \\ge a) \\le \\frac{M_X(t)}{a}\\)",
       "\\(\\mathbb{P}(X \\ge a) \\le e^{ta} M_X(t)\\)",
       "\\(\\mathbb{P}(X \\ge a) \\le \\frac{\\text{Var}(X)}{(a - \\mu)^2}\\)"],
      0,
      "For \\(t > 0\\), the event \\(\\{X \\ge a\\}\\) is identical to \\(\\{e^{tX} \\ge e^{ta}\\}\\). Applying Markov's inequality to the strictly positive random variable \\(e^{tX}\\): \\(\\mathbb{P}(e^{tX} \\ge e^{ta}) \\le \\frac{\\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)\\). Minimizing over \\(t > 0\\) yields the tightest Chernoff bound.",
      "لأي \\(t > 0\\)، الحدث \\(X \\ge a\\) يكافئ \\(e^{tX} \\ge e^{ta}\\). بتطبيق متباينة ماركوف على المتغير الموجب \\(e^{tX}\\) نجد: \\(\\mathbb{P}(e^{tX} \\ge e^{ta}) \\le \\frac{\\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)\\).",
      "Apply Markov's inequality to the monotonically increasing transformation \\(e^{tX}\\).",
      "طبق متباينة ماركوف على التحويل المتزايد \\(e^{tX}\\).")

    # 414: Jacobian Transformation for Random Vectors
    q("KAUST-P2-414", "Probability & Statistics", "Medium",
      "Let \\(X, Y\\) be independent exponential random variables with parameter \\(\\lambda = 1\\). Let \\(U = X + Y\\) and \\(V = \\frac{X}{X + Y}\\). What is the joint density \\(f_{U,V}(u, v)\\) for \\(u > 0, 0 < v < 1\\)?",
      "ليكن \\(X, Y\\) متغيرين عشوائيين أسيين مستقلين مع \\(\\lambda = 1\\). ليكن \\(U = X + Y\\) و \\(V = \\frac{X}{X + Y}\\). ما هي الكثافة المشتركة \\(f_{U,V}(u, v)\\) حيث \\(u > 0, 0 < v < 1\\)؟",
      ["\\(f_{U,V}(u, v) = u e^{-u}\\)", "\\(f_{U,V}(u, v) = e^{-u}\\)", "\\(f_{U,V}(u, v) = \\frac{e^{-u}}{u}\\)", "\\(f_{U,V}(u, v) = 2u e^{-2u}\\)"],
      0,
      "Inverse transformation: \\(X = UV\\) and \\(Y = U(1 - V)\\). The Jacobian matrix is \\(J = \\begin{pmatrix} \\partial X/\\partial U & \\partial X/\\partial V \\\\ \\partial Y/\\partial U & \\partial Y/\\partial V \\end{pmatrix} = \\begin{pmatrix} V & U \\\\ 1 - V & -U \\end{pmatrix}\\). Determinant: \\(|\\det(J)| = |V(-U) - U(1-V)| = |-VU - U + VU| = |-U| = u\\). The joint density of \\((X, Y)\\) is \\(f_{X,Y}(x, y) = e^{-x} e^{-y} = e^{-(x+y)} = e^{-u}\\). Multiplying by the Jacobian determinant yields \\(f_{U,V}(u, v) = f_{X,Y}(uv, u(1-v)) |\\det(J)| = e^{-u} \\cdot u = u e^{-u}\\). Notice \\(U \\sim \\text{Gamma}(2, 1)\\) and \\(V \\sim \\text{Uniform}(0, 1)\\) are independent!",
      "التحويل العكسي: \\(X = UV\\) و \\(Y = U(1-V)\\). محدد مصفوفة جاكوبي هو \\(|\\det(J)| = u\\). الكثافة الأصلية هي \\(e^{-(x+y)} = e^{-u}\\). بالضرب في محدد جاكوبي نحصل على \\(f_{U,V}(u, v) = u e^{-u}\\). (نلاحظ استقلال \\(U\\) عن \\(V\\)).",
      "Invert the transformation to get \\(X = UV, Y = U(1-V)\\) and compute the determinant of the Jacobian.",
      "أوجد التحويل العكسي واحسب محدد جاكوبي.")

    # 415: Central Limit Theorem - Delta Method
    q("KAUST-P2-415", "Probability & Statistics", "Hard",
      "Let \\(\\bar{X}_n\\) be the sample mean of \\(n\\) i.i.d. random variables with mean \\(\\mu > 0\\) and variance \\(\\sigma^2\\). By the Delta Method, what is the asymptotic distribution of \\(\\sqrt{n}\\left(\\frac{1}{\\bar{X}_n} - \\frac{1}{\\mu}\\right)\\)?",
      "لتكن \\(\\bar{X}_n\\) المتوسط الحسابي لعينة من \\(n\\) متغيرات عشوائية مستقلة بمتوسط \\(\\mu > 0\\) وتباين \\(\\sigma^2\\). باستخدام طريقة دلتا، ما هو التوزيع المقارب لـ \\(\\sqrt{n}\\left(\\frac{1}{\\bar{X}_n} - \\frac{1}{\\mu}\\right)\\)؟",
      ["\\(\\mathcal{N}\\left(0, \\frac{\\sigma^2}{\\mu^4}\\right)\\)",
       "\\(\\mathcal{N}\\left(0, \\frac{\\sigma^2}{\\mu^2}\\right)\\)",
       "\\(\\mathcal{N}\\left(0, \\frac{\\sigma^4}{\\mu^2}\\right)\\)",
       "\\(\\mathcal{N}\\left(0, \\sigma^2 \\mu^4\\right)\\)"],
      0,
      "By the classical Central Limit Theorem, \\(\\sqrt{n}(\\bar{X}_n - \\mu) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2)\\). The Delta Method states that if \\(g\\) is differentiable with \\(g'(\\mu) \\neq 0\\), then \\(\\sqrt{n}(g(\\bar{X}_n) - g(\\mu)) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2 [g'(\\mu)]^2)\\). Here \\(g(x) = 1/x\\), so \\(g'(x) = -1/x^2\\) and \\([g'(\\mu)]^2 = 1/\\mu^4\\). Thus the asymptotic variance is \\(\\sigma^2 / \\mu^4\\), so the distribution is \\(\\mathcal{N}\\left(0, \\frac{\\sigma^2}{\\mu^4}\\right)\\).",
      "حسب نظرية النهاية المركزية، \\(\\sqrt{n}(\\bar{X}_n - \\mu) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2)\\). بتطبيق طريقة دلتا للدالة \\(g(x) = 1/x\\) حيث \\(g'(\\mu) = -1/\\mu^2\\)، يكون التباين المقارب هو \\(\\sigma^2 [g'(\\mu)]^2 = \\frac{\\sigma^2}{\\mu^4}\\).",
      "Use the Delta method formula: asymptotic variance is \\(\\sigma^2 [g'(\\mu)]^2\\).",
      "استخدم صيغة طريقة دلتا: التباين المقارب هو \\(\\sigma^2 [g'(\\mu)]^2\\).")

    # 416: Conformal Mapping - Upper Half-Plane to Unit Disc
    q("KAUST-P2-416", "Complex Analysis", "Medium",
      "Which function maps the upper half-plane \\(\\mathbb{H} = \\{z \\in \\mathbb{C} : \\text{Im}(z) > 0\\}\\) conformally and bijectively onto the open unit disc \\(\\mathbb{D} = \\{w : |w| < 1\\}\\), sending \\(z = i\\) to \\(w = 0\\)?",
      "أي دالة تنقل النصف العلوي للمستوى العقدي \\(\\text{Im}(z) > 0\\) بشكل امتثالي وتقابلي إلى قرص الوحدة المفتوح \\(|w| < 1\\) ناقلة \\(z = i\\) إلى \\(w = 0\\)؟",
      ["\\(w = \\frac{z - i}{z + i}\\)", "\\(w = \\frac{z + i}{z - i}\\)", "\\(w = \\frac{z - 1}{z + 1}\\)", "\\(w = \\frac{i z}{z + 1}\\)"],
      0,
      "The Cayley transform \\(w = \\frac{z - i}{z + i}\\) maps the upper half-plane onto the unit disc. To verify: for any \\(z = x + iy\\) with \\(y > 0\\), the distance from \\(z\\) to \\(i\\) is \\(|z - i| = \\sqrt{x^2 + (y-1)^2}\\), while the distance from \\(z\\) to \\(-i\\) is \\(|z + i| = \\sqrt{x^2 + (y+1)^2}\\). Since \\(y > 0\\), \\((y-1)^2 < (y+1)^2\\), so \\(|z - i| < |z + i|\\), which means \\(|w| = \\frac{|z - i|}{|z + i|} < 1\\). At \\(z = i\\), \\(w = \\frac{i - i}{i + i} = 0\\). On the real boundary (\\(y = 0\\)), \\(|x - i| = |x + i|\\), so \\(|w| = 1\\).",
      "تحويل كايلي \\(w = \\frac{z-i}{z+i}\\) ينقل النصف العلوي إلى قرص الوحدة. عندما يكون \\(\\text{Im}(z) > 0\\)، تكون المسافة إلى \\(i\\) أصغر تماماً من المسافة إلى \\(-i\\)، فيكون مقياس النسبة أقل من 1 تماماً، وعند \\(z=i\\) ينعدم البسط ليصبح \\(w = 0\\).",
      "Check which point in the lower half-plane cancels out the denominator.",
      "تحقق من أن النقطة المقابلة في النصف السفلي تجعل المقام متوافقاً.")

    # 417: Argument Principle - Number of Poles and Zeros
    q("KAUST-P2-417", "Complex Analysis", "Hard",
      "By the Argument Principle, if \\(f(z)\\) is meromorphic inside and on a simple closed contour \\(C\\) with \\(N\\) zeros and \\(P\\) poles (counted with multiplicity) inside \\(C\\), what does \\(\\frac{1}{2\\pi i}\\oint_C \\frac{f'(z)}{f(z)} dz\\) equal?",
      "وفقاً لمبدأ العمدة (Argument Principle)، إذا كانت \\(f(z)\\) دالة ميرومورفية داخل وعلى مسار بسيط مغلق \\(C\\) بها \\(N\\) من الأصفار و \\(P\\) من الأقطاب داخل \\(C\\)، فماذا يساوي التكامل \\(\\frac{1}{2\\pi i}\\oint_C \\frac{f'(z)}{f(z)} dz\\)؟",
      ["\\(N - P\\)", "\\(N + P\\)", "\\(P - N\\)", "\\(2(N - P)\\)"],
      0,
      "Near a zero \\(z_0\\) of order \\(k\\), \\(f(z) = (z - z_0)^k g(z)\\), so \\(\\frac{f'(z)}{f(z)} = \\frac{k}{z - z_0} + \\frac{g'(z)}{g(z)}\\), which has residue \\(+k\\). Near a pole \\(p_0\\) of order \\(m\\), \\(f(z) = (z - p_0)^{-m} h(z)\\), giving residue \\(-m\\). By the Residue Theorem, summing all residues inside \\(C\\) gives \\(\\frac{1}{2\\pi i}\\oint_C \\frac{f'(z)}{f(z)} dz = \\sum k_j - \\sum m_l = N - P\\).",
      "بالقرب من صفر من الرتبة \\(k\\) يكون الباقي \\(+k\\)، وبالقرب من قطب من الرتبة \\(m\\) يكون الباقي \\(-m\\). بجمع البواقي داخل المسار المغلق ينتج مباشرة \\(N - P\\).",
      "Recall the residues of the logarithmic derivative \\(f'/f\\) at zeros and poles.",
      "تذكر بواقي المشتق اللوغاريتمي \\(f'/f\\) عند الأصفار والأقطاب.")

    # 418: Casorati-Weierstrass Theorem
    q("KAUST-P2-418", "Complex Analysis", "Medium",
      "Which famous theorem states that if \\(z_0\\) is an essential singularity of \\(f(z)\\), then the image of any punctured neighborhood \\(0 < |z - z_0| < \\epsilon\\) under \\(f\\) is dense in \\(\\mathbb{C}\\)?",
      "أي نظرية شهيرة تنص على أنه إذا كانت \\(z_0\\) نقطة شاذة جوهرية (essential singularity) لـ \\(f(z)\\)، فإن صورة أي جوار مثقوب \\(0 < |z - z_0| < \\epsilon\\) تكون كثيفة في \\(\\mathbb{C}\\)؟",
      ["Casorati-Weierstrass Theorem", "Picard's Little Theorem", "Liouville's Theorem", "Morera's Theorem"],
      0,
      "The Casorati-Weierstrass Theorem states that an analytic function comes arbitrarily close to any complex value in every neighborhood of an essential singularity (its image is dense in \\(\\mathbb{C}\\)). Picard's Great Theorem strengthens this by showing that it actually assumes every complex value with at most one exception infinitely often.",
      "تنص نظرية كازوراتي-فايرشتراس على أن الدالة التحليلية تقترب بشكل تعسفي من أي قيمة عقدية في أي جوار لنقطة شاذة جوهرية (الصورة كثيفة في المستوى العقدي).",
      "This theorem concerns the dense range of an analytic function near an essential singularity.",
      "تتعلق هذه النظرية بكثافة مدى الدالة التحليلية بالقرب من الشذوذ الجوهري.")

    # 419: Morera's Theorem
    q("KAUST-P2-419", "Complex Analysis", "Medium",
      "Morera's Theorem serves as a converse to Cauchy's Integral Theorem. It states that if \\(f(z)\\) is continuous on an open domain \\(D\\) and \\(\\oint_C f(z) dz = 0\\) for every closed contour \\(C \\subset D\\), then \\(f(z)\\) is:",
      "تعتبر نظرية موريرا عكساً لنظرية كوشي التكاملية. تنص على أنه إذا كانت \\(f(z)\\) متصلة في نطاق مفتوح \\(D\\) وكان \\(\\oint_C f(z) dz = 0\\) لكل مسار مغلق، فإن \\(f(z)\\):",
      ["Holomorphic (analytic) throughout \\(D\\)",
       "Constant throughout \\(D\\)",
       "A polynomial of finite degree",
       "Harmonic but not necessarily holomorphic"],
      0,
      "Morera's Theorem states that a continuous function on a domain whose contour integral vanishes along every closed curve has a local primitive \\(F(z) = \\int_{z_0}^z f(\\zeta)d\\zeta\\). Since \\(F'(z) = f(z)\\), \\(F\\) is holomorphic, and by the regularity of holomorphic functions, its derivative \\(f(z)\\) is infinitely differentiable and hence holomorphic on \\(D\\).",
      "تنص نظرية موريرا على أن الدالة المتصلة التي ينعدم تكاملها على أي مسار مغلق تمتلك دالة أصلية محلية، وبما أن المشتقة لدالة تحليلية هي دالة تحليلية أيضاً، فإن \\(f\\) تحليلية في كامل النطاق.",
      "A vanishing closed-contour integral implies the existence of an analytic antiderivative.",
      "انعدام التكامل على المسارات المغلقة يضمن وجود دالة أصلية تحليلية.")

    # 420: Poisson Kernel on the Unit Disc
    q("KAUST-P2-420", "Complex Analysis", "Hard",
      "The Poisson kernel \\(P_r(\\theta)\\) solves the Dirichlet problem for Laplace's equation on the unit disc. What is its explicit formula for \\(0 \\le r < 1\\)?",
      "نواة بواسون \\(P_r(\\theta)\\) تحل مسألة ديريكليه لمعادلة لابلاس على قرص الوحدة. ما هي صيغتها الصريحة لـ \\(0 \\le r < 1\\)؟",
      ["\\(P_r(\\theta) = \\frac{1 - r^2}{1 - 2r\\cos\\theta + r^2}\\)",
       "\\(P_r(\\theta) = \\frac{1 + r^2}{1 - 2r\\cos\\theta + r^2}\\)",
       "\\(P_r(\\theta) = \\frac{1 - r}{1 - 2r\\sin\\theta + r^2}\\)",
       "\\(P_r(\\theta) = \\frac{1 - r^2}{(1 - r)^2}\\)"],
      0,
      "The Poisson kernel is derived from the real part of the Schwarz kernel: \\(P_r(\\theta) = \\text{Re}\\left(\\frac{1 + z}{1 - z}\\right)\\) where \\(z = r e^{i\\theta}\\). Multiplying numerator and denominator by \\(1 - \\bar{z}\\): \\(\\frac{(1+z)(1-\\bar{z})}{|1-z|^2} = \\frac{1 - |z|^2 + (z - \\bar{z})}{|1-z|^2}\\). The real part is \\(\\frac{1 - |z|^2}{|1 - z|^2} = \\frac{1 - r^2}{|1 - r\\cos\\theta - i r\\sin\\theta|^2} = \\frac{1 - r^2}{(1 - r\\cos\\theta)^2 + r^2\\sin^2\\theta} = \\frac{1 - r^2}{1 - 2r\\cos\\theta + r^2}\\).",
      "تشتق نواة بواسون من الجزء الحقيقي لكايلي-شفارتز: \\(\\text{Re}(\\frac{1+z}{1-z})\\) مع \\(z = r e^{i\\theta}\\). بالضرب في المرافق وحساب الجزء الحقيقي نجد \\(\\frac{1 - r^2}{1 - 2r\\cos\\theta + r^2}\\).",
      "Compute \\(\\text{Re}\\left(\\frac{1 + re^{i\\theta}}{1 - re^{i\\theta}}\\right)\\).",
      "احسب الجزء الحقيقي للكسر العقدي.")

    # 421 to 450: Complete Part D
    # 421: Entire Functions and Liouville's Theorem
    q("KAUST-P2-421", "Complex Analysis", "Medium",
      "If \\(f(z)\\) is an entire function such that \\(|f(z)| \\le M |z|^2\\) for all \\(|z| \\ge 1\\), what can be concluded about \\(f(z)\\)?",
      "إذا كانت \\(f(z)\\) دالة كلية (entire) بحيث \\(|f(z)| \\le M |z|^2\\) لجميع \\(|z| \\ge 1\\)، فما الاستنتاج حول \\(f(z)\\)؟",
      ["\\(f(z)\\) is a polynomial of degree at most 2",
       "\\(f(z)\\) is a constant function",
       "\\(f(z)\\) is identically zero",
       "\\(f(z)\\) must be a trigonometric function"],
      0,
      "By Cauchy's inequality for derivatives of an entire function, the \\(n\\)-th Taylor coefficient around 0 satisfies \\(|a_n| \\le \\frac{M(R)}{R^n}\\). For \\(R \\to \\infty\\), \\(|a_n| \\le \\frac{M R^2}{R^n} = M R^{2-n}\\). For all \\(n > 2\\), \\(2 - n < 0\\), so taking \\(R \\to \\infty\\) yields \\(|a_n| \\le 0 \\implies a_n = 0\\). Therefore, all terms beyond \\(z^2\\) vanish, proving that \\(f(z)\\) is a polynomial of degree at most 2.",
      "باستخدام متباينات كوشي لمعاملات متسلسلة تايلور، \\(|a_n| \\le M R^{2-n}\\). بجعل \\(R \\to \\infty\\)، فإن \\(a_n = 0\\) لجميع \\(n > 2\\). بالتالي تنعدم جميع المعاملات بعد الرتبة 2، فتكون \\(f(z)\\) كثيرة حدود من الدرجة الثانية على الأكثر.",
      "Apply Cauchy's estimate for derivatives as \\(R \\to \\infty\\).",
      "طبق تقدير كوشي للمشتقات بجعل نصف القطر يؤول إلى اللانهاية.")

    # 422: Conformal Mapping - Joukowsky Transform
    q("KAUST-P2-422", "Complex Analysis", "Hard",
      "The Joukowsky transform is defined by \\(w = \\frac{1}{2}\\left(z + \\frac{1}{z}\\right)\\). What is the image of the unit circle \\(|z| = 1\\) in the \\(w\\)-plane?",
      "يُعرّف تحويل جوكوفسكي بـ \\(w = \\frac{1}{2}\\left(z + \\frac{1}{z}\\right)\\). ما هي صورة دائرة الوحدة \\(|z| = 1\\) في مستوى \\(w\\)؟",
      ["The real segment \\([-1, 1]\\) traversed twice",
       "The unit circle \\(|w| = 1\\)",
       "The imaginary axis",
       "An ellipse with foci at \\(\\pm i\\)"],
      0,
      "On the unit circle, set \\(z = e^{i\\theta}\\). Then \\(w = \\frac{1}{2}(e^{i\\theta} + e^{-i\\theta}) = \\cos\\theta\\). As \\(\\theta\\) varies from \\(0\\) to \\(2\\pi\\), \\(\\cos\\theta\\) is purely real and traverses the interval from \\(1\\) down to \\(-1\\) (from \\(0\\) to \\(\\pi\\)) and back from \\(-1\\) to \\(1\\) (from \\(\\pi\\) to \\(2\\pi\\)). Thus the image is the real line segment \\([-1, 1]\\) covered twice.",
      "على دائرة الوحدة، نضع \\(z = e^{i\\theta}\\). نجد \\(w = \\frac{1}{2}(e^{i\\theta} + e^{-i\\theta}) = \\cos\\theta\\). بما أن \\(\\cos\\theta\\) عدد حقيقي ينتمي إلى \\([-1, 1]\\)، فإن الصورة هي القطعة المستقيمة \\([-1, 1]\\) على المحور الحقيقي مقطوعة مرتين.",
      "Substitute \\(z = e^{i\\theta}\\) and apply Euler's formula.",
      "عوض بـ \\(z = e^{i\\theta}\\) واستخدم صيغة أويلر لدالة جيب التمام.")

    # 423: Jensen's Formula
    q("KAUST-P2-423", "Complex Analysis", "Hard",
      "Jensen's formula relates the modulus of an analytic function on a circle to its zeros inside the circle. If \\(f(z)\\) is analytic on \\(|z| \\le R\\) with \\(f(0) \\neq 0\\) and has zeros \\(a_1, a_2, \\dots, a_n\\) inside \\(|z| < R\\), what is \\(\\ln|f(0)|\\)?",
      "تربط صيغة ينسن مقياس الدالة التحليلية على دائرة بأصفارها داخل الدائرة. إذا كانت \\(f\\) تحليلية على \\(|z| \\le R\\) مع \\(f(0) \\neq 0\\) وأصفارها \\(a_1, \\dots, a_n\\)، فما قيمة \\(\\ln|f(0)|\\)؟",
      ["\\(\\frac{1}{2\\pi}\\int_0^{2\\pi} \\ln|f(R e^{i\\theta})| d\\theta - \\sum_{k=1}^n \\ln\\left(\\frac{R}{|a_k|}\\right)\\)",
       "\\(\\frac{1}{2\\pi}\\int_0^{2\\pi} \\ln|f(R e^{i\\theta})| d\\theta + \\sum_{k=1}^n \\ln\\left(\\frac{R}{|a_k|}\\right)\\)",
       "\\(\\int_0^{2\\pi} |f(R e^{i\\theta})| d\\theta\\)",
       "\\(\\sum_{k=1}^n |a_k|\\)"],
      0,
      "Jensen's formula states: \\(\\ln|f(0)| = \\frac{1}{2\\pi}\\int_0^{2\\pi} \\ln|f(R e^{i\\theta})| d\\theta - \\sum_{k=1}^n \\ln\\left(\\frac{R}{|a_k|}\\right)\\). When \\(f\\) has no zeros inside the disc, the summation vanishes, reducing to the Mean Value Property for the harmonic function \\(\\ln|f(z)|\\). Each zero \\(a_k\\) inside introduces a factor from the Blaschke product.",
      "تنص صيغة ينسن على أن \\(\\ln|f(0)| = \\frac{1}{2\\pi}\\int_0^{2\\pi} \\ln|f(Re^{i\\theta})| d\\theta - \\sum \\ln(R/|a_k|)\\). عند عدم وجود أصفار تختزل الصيغة إلى خاصية القيمة المتوسطة للدوال التوافقية.",
      "Recall the correction terms coming from the Blaschke factors.",
      "تذكر حدود التصحيح الناتجة عن عوامل بلاشكه للأصفار الداخلية.")

    # 424: Open Mapping Theorem
    q("KAUST-P2-424", "Complex Analysis", "Medium",
      "The Open Mapping Theorem in complex analysis asserts that if \\(U \\subset \\mathbb{C}\\) is open and connected, and \\(f: U \\to \\mathbb{C}\\) is a non-constant holomorphic function, then \\(f(U)\\) is:",
      "تنص نظرية التطبيق المفتوح في التحليل العقدي على أنه إذا كانت \\(U\\) مجموعة مفتوحة ومترابطة، وكانت \\(f\\) دالة هولومورفية غير ثابتة، فإن \\(f(U)\\):",
      ["An open set in \\(\\mathbb{C}\\)",
       "A closed set in \\(\\mathbb{C}\\)",
       "A compact set in \\(\\mathbb{C}\\)",
       "A discrete set of points"],
      0,
      "The Open Mapping Theorem states that non-constant holomorphic functions map open sets to open sets. This fundamental topological property immediately implies the Maximum Modulus Principle, because if \\(f(U)\\) is open, no interior point \\(f(z_0)\\) can have maximal modulus in \\(f(U)\\).",
      "تنص نظرية التطبيق المفتوح على أن أي دالة هولومورفية غير ثابتة تنقل المجموعات المفتوحة إلى مجموعات مفتوحة. وهذه الخاصية تؤدي مباشرة إلى برهان مبدأ المقياس الأعظم.",
      "Non-constant holomorphic maps are open maps.",
      "التطبيقات الهولومورفية غير الثابتة تنقل المجموعات المفتوحة إلى مجموعات مفتوحة.")

    # 425: Characteristic Function of Poisson Distribution
    q("KAUST-P2-425", "Probability & Statistics", "Medium",
      "Find the characteristic function \\(\\phi_X(t) = \\mathbb{E}[e^{itX}]\\) of a Poisson random variable \\(X \\sim \\text{Poisson}(\\lambda)\\).",
      "أوجد الدالة المميزة \\(\\phi_X(t) = \\mathbb{E}[e^{itX}]\\) لمتغير بواسون العشوائي \\(X \\sim \\text{Poisson}(\\lambda)\\).",
      ["\\(\\exp\\left(\\lambda(e^{it} - 1)\\right)\\)",
       "\\(\\exp\\left(\\lambda(e^{it} + 1)\\right)\\)",
       "\\(\\frac{1}{1 - \\lambda it}\\)",
       "\\(\\exp\\left(-\\frac{1}{2}\\lambda t^2\\right)\\)"],
      0,
      "By definition: \\(\\phi_X(t) = \\sum_{k=0}^\\infty e^{itk} \\frac{\\lambda^k e^{-\\lambda}}{k!} = e^{-\\lambda} \\sum_{k=0}^\\infty \\frac{(\\lambda e^{it})^k}{k!} = e^{-\\lambda} \\exp(\\lambda e^{it}) = \\exp(\\lambda(e^{it} - 1))\\).",
      "حسب التعريف: \\(\\mathbb{E}[e^{itX}] = \\sum e^{itk} \\frac{\\lambda^k e^{-\\lambda}}{k!} = e^{-\\lambda} e^{\\lambda e^{it}} = \\exp(\\lambda(e^{it} - 1))\\).",
      "Sum the Taylor series for \\(\\exp(\\lambda e^{it})\\).",
      "اجمع متسلسلة تايلور للأس \\(\\exp(\\lambda e^{it})\\).")

    # 426: Conformal Invariance of Laplace's Equation
    q("KAUST-P2-426", "Complex Analysis", "Hard",
      "Let \\(u(x, y)\\) be harmonic on domain \\(\\Omega\\). If \\(f(z) = u + iv\\) is holomorphic, what is \\(\\Delta (u^2)\\) in terms of \\(f'(z)\\)?",
      "لتكن \\(u(x, y)\\) دالة توافقية على النطاق \\(\\Omega\\). إذا كانت \\(f(z) = u + iv\\) هولومورفية، فما هي قيمة \\(\\Delta (u^2)\\) بدلالة \\(f'(z)\\)؟",
      ["\\(\\Delta(u^2) = 2|f'(z)|^2\\)",
       "\\(\\Delta(u^2) = |f'(z)|^2\\)",
       "\\(\\Delta(u^2) = 4|f'(z)|^2\\)",
       "\\(\\Delta(u^2) = 0\\)"],
      0,
      "Using vector calculus identities: \\(\\Delta(u^2) = \\nabla \\cdot \\nabla(u^2) = \\nabla \\cdot (2u \\nabla u) = 2|\\nabla u|^2 + 2u \\Delta u\\). Since \\(u\\) is harmonic, \\(\\Delta u = 0\\), so \\(\\Delta(u^2) = 2|\\nabla u|^2 = 2(u_x^2 + u_y^2)\\). By the Cauchy-Riemann equations, \\(f'(z) = u_x + i v_x = u_x - i u_y\\), so \\(|f'(z)|^2 = u_x^2 + u_y^2\\). Therefore, \\(\\Delta(u^2) = 2|f'(z)|^2\\).",
      "نحسب لابلاسي مربع الدالة: \\(\\Delta(u^2) = 2|\\nabla u|^2 + 2u \\Delta u\\). وبما أن \\(u\\) توافقية، فإن \\(\\Delta u = 0\\). ومن معادلات كوشي-ريمان نجد \\(|f'(z)|^2 = u_x^2 + u_y^2 = |\\nabla u|^2\\). بالتالي \\(\\Delta(u^2) = 2|f'(z)|^2\\).",
      "Expand \\(\\Delta(u^2) = 2|\\nabla u|^2 + 2u\\Delta u\\) and use \\(|f'|^2 = |\\nabla u|^2\\).",
      "فك لابلاسي \\(u^2\\) واستخدم العلاقة بين مشتق الدالة وتدرج جزئها الحقيقي.")

    # 427: Weak vs Strong Law of Large Numbers
    q("KAUST-P2-427", "Probability & Statistics", "Medium",
      "What is the precise mathematical difference between the Weak Law of Large Numbers (WLLN) and the Strong Law of Large Numbers (SLLN)?",
      "ما هو الفارق الرياضي الدقيق بين قانون الأعداد الكبيرة الضعيف (WLLN) والقوي (SLLN)؟",
      ["WLLN asserts convergence in probability; SLLN asserts almost sure convergence",
       "WLLN requires finite variance; SLLN requires only finite third moment",
       "WLLN applies to independent variables; SLLN applies only to Markov chains",
       "WLLN holds for discrete variables; SLLN holds for continuous variables"],
      0,
      "The Weak Law of Large Numbers asserts that the sample mean \\(\\bar{X}_n\\) converges in probability to \\(\\mu\\), written \\(\\bar{X}_n \\xrightarrow{P} \\mu\\), meaning \\(\\lim_{n\\to\\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| > \\epsilon) = 0\\). The Strong Law of Large Numbers asserts that \\(\\bar{X}_n\\) converges almost surely (with probability 1) to \\(\\mu\\), written \\(\\bar{X}_n \\xrightarrow{a.s.} \\mu\\), meaning \\(\\mathbb{P}\\left(\\lim_{n\\to\\infty} \\bar{X}_n = \\mu\\right) = 1\\).",
      "ينص قانون الأعداد الكبيرة الضعيف على التقارب في الاحتمال (convergence in probability)، بينما ينص القانون القوي على التقارب شبه المؤكد أو باحتمال 1 (almost sure convergence)، وهو نوع أقوى من التقارب في نظرية القياس والاحتمالات.",
      "Compare convergence in probability with almost sure convergence.",
      "قارن بين التقارب في الاحتمال والتقارب شبه المؤكد.")

    # 428: Maximum of Independent Uniform Variables
    q("KAUST-P2-428", "Probability & Statistics", "Medium",
      "Let \\(X_1, X_2, \\dots, X_n\\) be i.i.d. random variables uniformly distributed on \\([0, 1]\\). Let \\(M_n = \\max(X_1, \\dots, X_n)\\). What is \\(\\mathbb{E}[M_n]\\)?",
      "لتكن \\(X_1, \\dots, X_n\\) متغيرات عشوائية مستقلة ومتطابقة التوزيع بانتظام على \\([0, 1]\\). ليكن \\(M_n = \\max(X_1, \\dots, X_n)\\). ما هو التوقع الرياضي \\(\\mathbb{E}[M_n]\\)؟",
      ["\\(\\frac{n}{n + 1}\\)", "\\(\\frac{1}{n + 1}\\)", "\\(\\frac{n - 1}{n}\\)", "\\(\\frac{1}{2}\\)"],
      0,
      "The CDF of each \\(X_i\\) is \\(F(x) = x\\) for \\(x \\in [0, 1]\\). The CDF of the maximum is \\(F_{M_n}(x) = [F(x)]^n = x^n\\). The probability density function is \\(f_{M_n}(x) = n x^{n-1}\\). The expected value is \\(\\mathbb{E}[M_n] = \\int_0^1 x (n x^{n-1}) dx = n \\int_0^1 x^n dx = \\frac{n}{n + 1}\\).",
      "دالة التوزيع التراكمي للقيمة العظمى هي \\(F_{M_n}(x) = x^n\\). دالة الكثافة هي مشتقتها \\(n x^{n-1}\\). التوقع هو \\(\\int_0^1 x \\cdot n x^{n-1} dx = n \\int_0^1 x^n dx = \\frac{n}{n+1}\\).",
      "The CDF of \\(\\max\\) is the product of the individual CDFs: \\(F_{M_n}(x) = [F(x)]^n\\).",
      "دالة التوزيع للقيمة العظمى هي حاصل ضرب دوال التوزيع الفردية.")

    # 429: Minimum of Independent Exponential Variables
    q("KAUST-P2-429", "Probability & Statistics", "Medium",
      "Let \\(X_1, X_2, \\dots, X_n\\) be independent exponential random variables with rate parameters \\(\\lambda_1, \\lambda_2, \\dots, \\lambda_n\\). What is the distribution of \\(T = \\min(X_1, \\dots, X_n)\\)?",
      "لتكن \\(X_1, \\dots, X_n\\) متغيرات عشوائية أسية مستقلة بمعالم معدل \\(\\lambda_1, \\dots, \\lambda_n\\). ما هو توزيع \\(T = \\min(X_1, \\dots, X_n)\\)؟",
      ["\\(\\text{Exponential}\\left(\\sum_{i=1}^n \\lambda_i\\right)\\)",
       "\\(\\text{Exponential}\\left(\\prod_{i=1}^n \\lambda_i\\right)\\)",
       "\\(\\text{Gamma}\\left(n, \\sum_{i=1}^n \\lambda_i\\right)\\)",
       "\\(\\text{Weibull}\\left(\\min \\lambda_i\\right)\\)"],
      0,
      "The survival function of \\(T\\) is \\(\\mathbb{P}(T > t) = \\mathbb{P}(\\min X_i > t) = \\prod_{i=1}^n \\mathbb{P}(X_i > t) = \\prod_{i=1}^n e^{-\\lambda_i t} = \\exp\\left(-\\left(\\sum_{i=1}^n \\lambda_i\\right) t\\right)\\). This is precisely the survival function of an exponential random variable with rate parameter \\(\\Lambda = \\sum_{i=1}^n \\lambda_i\\).",
      "دالة البقاء للقيمة الصغرى هي احتمال أن تكون جميع المتغيرات أكبر من \\(t\\): \\(\\prod e^{-\\lambda_i t} = e^{-(\\sum \\lambda_i) t}\\). وهذا يمثل بدقة دالة البقاء لتوزيع أسي بمعدل يساوي مجموع المعدلات \\(\\sum \\lambda_i\\).",
      "Multiply the individual survival functions \\(\\mathbb{P}(X_i > t) = e^{-\\lambda_i t}\\).",
      "اضرب دوال البقاء الفردية لجميع المتغيرات المستقلة.")

    # 430: Chebyshev's Inequality Exact Bound
    q("KAUST-P2-430", "Probability & Statistics", "Medium",
      "A random variable \\(X\\) has mean \\(\\mu = 50\\) and variance \\(\\sigma^2 = 25\\). Using Chebyshev's inequality, what is the best upper bound on \\(\\mathbb{P}(|X - 50| \\ge 15)\\)?",
      "متغير عشوائي \\(X\\) له متوسط \\(\\mu = 50\\) وتباين \\(\\sigma^2 = 25\\). باستخدام متباينة تشيبيشيف، ما هو أفضل حد أعلى لـ \\(\\mathbb{P}(|X - 50| \\ge 15)\\)؟",
      ["\\(\\frac{1}{9}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{1}{25}\\)", "\\(\\frac{5}{9}\\)"],
      0,
      "Chebyshev's inequality states \\(\\mathbb{P}(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}\\). Here \\(\\sigma = \\sqrt{25} = 5\\). The deviation is \\(15\\), so \\(k\\sigma = 15 \\implies k(5) = 15 \\implies k = 3\\). Thus \\(\\mathbb{P}(|X - 50| \\ge 15) \\le \\frac{1}{3^2} = \\frac{1}{9}\\).",
      "تنص متباينة تشيبيشيف على أن \\(\\mathbb{P}(|X - \\mu| \\ge k\\sigma) \\le 1/k^2\\). هنا الانحراف المعياري هو \\(\\sigma = 5\\). وبما أن المسافة هي 15، فإن \\(k = 15/5 = 3\\). الحد الأعلى هو \\(1/3^2 = 1/9\\).",
      "Express the deviation 15 as \\(k \\sigma\\) with \\(\\sigma = 5\\).",
      "عبر عن الانحراف 15 كمضاعف للانحراف المعياري \\(k\\sigma\\).")

    # 431: Riemann Mapping Theorem
    q("KAUST-P2-431", "Complex Analysis", "Medium",
      "The Riemann Mapping Theorem guarantees that any non-empty simply connected open proper subset of \\(\\mathbb{C}\\) can be conformally mapped bijectively onto which canonical domain?",
      "تضمن نظرية ريمان للتطبيقات الامتثالية إمكانية تحويل أي مجموعة جزئية فعلية مفتوحة وبسيطة الترابط في \\(\\mathbb{C}\\) امتثالياً وبشكل تقابلي إلى أي نطاق قياسي؟",
      ["The open unit disc \\(\\mathbb{D} = \\{z \\in \\mathbb{C} : |z| < 1\\}\\)",
       "The entire complex plane \\(\\mathbb{C}\\)",
       "The upper half plane minus a disc",
       "An open annulus \\(r < |z| < R\\)"],
      0,
      "The Riemann Mapping Theorem states that every non-empty simply connected open subset \\(U \\subsetneq \\mathbb{C}\\) is conformally equivalent (biholomorphic) to the open unit disc \\(\\mathbb{D}\\). The condition \\(U \\neq \\mathbb{C}\\) is essential by Liouville's theorem.",
      "تنص نظرية ريمان للتطبيقات على أن أي نطاق مفتوح مترابط بسيط لا يساوي كامل المستوى العقدي يكافئ امتثالياً قرص الوحدة المفتوح.",
      "Recall the standard canonical target domain of Riemann's mapping theorem.",
      "تذكر النطاق القياسي المستهدف في نظرية ريمان.")

    # 432: Poisson Distribution Sum of Independents
    q("KAUST-P2-432", "Probability & Statistics", "Medium",
      "If \\(X \\sim \\text{Poisson}(\\lambda_1)\\) and \\(Y \\sim \\text{Poisson}(\\lambda_2)\\) are independent, what is the conditional distribution of \\(X\\) given \\(X + Y = n\\)?",
      "إذا كان \\(X \\sim \\text{Poisson}(\\lambda_1)\\) و \\(Y \\sim \\text{Poisson}(\\lambda_2)\\) مستقلين، فما هو التوزيع الشرطي لـ \\(X\\) بشرط \\(X + Y = n\\)؟",
      ["\\(\\text{Binomial}\\left(n, \\frac{\\lambda_1}{\\lambda_1 + \\lambda_2}\\right)\\)",
       "\\(\\text{Poisson}\\left(\\frac{\\lambda_1}{\\lambda_1 + \\lambda_2}\\right)\\)",
       "\\(\\text{Hypergeometric}\\left(n, \\lambda_1, \\lambda_2\\right)\\)",
       "\\(\\text{Uniform}(0, n)\\)"],
      0,
      "Compute \\(\\mathbb{P}(X = k \\mid X + Y = n) = \\frac{\\mathbb{P}(X = k, Y = n - k)}{\\mathbb{P}(X + Y = n)}\\). Since the sum of independent Poissons is \\(\\text{Poisson}(\\lambda_1 + \\lambda_2)\\): \\(\\frac{\\frac{e^{-\\lambda_1}\\lambda_1^k}{k!} \\frac{e^{-\\lambda_2}\\lambda_2^{n-k}}{(n-k)!}}{\\frac{e^{-(\\lambda_1+\\lambda_2)}(\\lambda_1+\\lambda_2)^n}{n!}} = \\frac{n!}{k!(n-k)!} \\left(\\frac{\\lambda_1}{\\lambda_1+\\lambda_2}\\right)^k \\left(\\frac{\\lambda_2}{\\lambda_1+\\lambda_2}\\right)^{n-k} = \\binom{n}{k} p^k (1-p)^{n-k}\\) where \\(p = \\frac{\\lambda_1}{\\lambda_1+\\lambda_2}\\). This is the Binomial distribution \\(\\text{Binomial}(n, p)\\).",
      "باحتمال الشرط: بسط النسبة يحوي جداء احتمالين منفصلين والمقام يحوي توزيع المجموع البواسوني. بالاختصار يظهر المعامل التوافقي \\(\\binom{n}{k}\\) وقوى النسب، وهو توزيع ذو الحدين \\(\\text{Binomial}(n, \\frac{\\lambda_1}{\\lambda_1+\\lambda_2})\\).",
      "Divide the joint probability by the Poisson probability of the sum.",
      "اقسم الاحتمال المشترك على احتمال المجموع.")

    # 433: Contour Integral with Branch Cut
    q("KAUST-P2-433", "Complex Analysis", "Hard",
      "Using a keyhole contour, what is the value of the integral \\(\\int_0^\\infty \\frac{x^{-1/2}}{1 + x} dx\\)?",
      "باستخدام مسار ثقب المفتاح (keyhole contour)، ما هي قيمة التكامل \\(\\int_0^\\infty \\frac{x^{-1/2}}{1 + x} dx\\)؟",
      ["\\(\\pi\\)", "\\(2\\pi\\)", "\\(\\frac{\\pi}{2}\\)", "\\(\\sqrt{2}\\pi\\)"],
      0,
      "Consider \\(f(z) = \\frac{z^{-1/2}}{1 + z}\\) with branch cut along the positive real axis \\([0, \\infty)\\), where \\(z = r e^{i\\theta}\\) with \\(0 < \\theta < 2\\pi\\). Along the upper edge (\\(\\theta = 0\\)), \\(z^{-1/2} = x^{-1/2}\\). Along the lower edge (\\(\\theta = 2\\pi\\)), \\(z^{-1/2} = x^{-1/2} e^{-i\\pi} = -x^{-1/2}\\). The integral along the keyhole contour gives \\((1 - e^{-i\\pi})\\int_0^\\infty \\frac{x^{-1/2}}{1+x} dx = 2 \\int_0^\\infty \\frac{x^{-1/2}}{1+x} dx\\). The only pole inside the contour is at \\(z = -1 = e^{i\\pi}\\). The residue is \\(\\text{Res}(f, -1) = (e^{i\\pi})^{-1/2} = e^{-i\\pi/2} = -i\\). By Residue theorem: \\(2 I = 2\\pi i (-i) = 2\\pi \\implies I = \\pi\\). (Alternatively, substitute \\(u = \\sqrt{x}\\): \\(\\int_0^\\infty \\frac{2 du}{1+u^2} = 2 [\\arctan(u)]_0^\\infty = 2(\\pi/2) = \\pi\\)).",
      "باستخدام مسار ثقب المفتاح حول الفرع أو بالتعويض الحقيقي المباشر \\(u = \\sqrt{x}\\): \\(dx = 2u du\\)، يصبح التكامل \\(\\int_0^\\infty \\frac{2du}{1+u^2} = 2 \\times \\frac{\\pi}{2} = \\pi\\).",
      "Substitute \\(u = x^{1/2}\\) to turn the integral into a standard arctangent integral.",
      "عوض بـ \\(u = x^{1/2}\\) لتحويل التكامل إلى صورة دالة ظل الزاوية العكسية.")

    # 434: MGF of Normal Distribution
    q("KAUST-P2-434", "Probability & Statistics", "Medium",
      "What is the moment-generating function \\(M_X(t) = \\mathbb{E}[e^{tX}]\\) of a normal random variable \\(X \\sim \\mathcal{N}(\\mu, \\sigma^2)\\)?",
      "ما هي دالة توليد العزوم \\(M_X(t) = \\mathbb{E}[e^{tX}]\\) لمتغير طبيعي عشوائي \\(X \\sim \\mathcal{N}(\\mu, \\sigma^2)\\)؟",
      ["\\(\\exp\\left(\\mu t + \\frac{1}{2}\\sigma^2 t^2\\right)\\)",
       "\\(\\exp\\left(\\mu t - \\frac{1}{2}\\sigma^2 t^2\\right)\\)",
       "\\(\\exp\\left(\\frac{1}{2}(\\mu t + \\sigma t)^2\\right)\\)",
       "\\(\\frac{1}{\\sqrt{2\\pi}}\\exp\\left(\\mu t + \\sigma^2 t^2\\right)\\)"],
      0,
      "Complete the square in the Gaussian integral: \\(\\mathbb{E}[e^{tX}] = \\frac{1}{\\sigma\\sqrt{2\\pi}}\\int_{-\\infty}^\\infty \\exp\\left(tx - \\frac{(x-\\mu)^2}{2\\sigma^2}\\right)dx\\). Setting \\(z = \\frac{x-\\mu}{\\sigma}\\), the exponent becomes \\(t(\\mu + \\sigma z) - \\frac{z^2}{2} = \\mu t - \\frac{1}{2}(z^2 - 2\\sigma t z) = \\mu t + \\frac{1}{2}\\sigma^2 t^2 - \\frac{1}{2}(z - \\sigma t)^2\\). The integral of the normalized Gaussian density over \\(z\\) equals 1, leaving \\(M_X(t) = \\exp\\left(\\mu t + \\frac{1}{2}\\sigma^2 t^2\\right)\\).",
      "بإكمال المربع في تكامل التوزيع الطبيعي: نجد أن المعامل الثابت خارج التكامل هو \\(\\exp(\\mu t + \\frac{1}{2}\\sigma^2 t^2)\\)، والتكامل المتبقي لكثافة طبيعية يساوي 1. إذن دالة توليد العزوم هي \\(\\exp(\\mu t + \\frac{1}{2}\\sigma^2 t^2)\\).",
      "Complete the square in the exponent of the integrand.",
      "أكمل المربع في أس الدالة المكاملة.")

    # 435: Picard's Little Theorem
    q("KAUST-P2-435", "Complex Analysis", "Medium",
      "According to Picard's Little Theorem, any non-constant entire function \\(f: \\mathbb{C} \\to \\mathbb{C}\\) attains every complex value with at most how many exceptions?",
      "وفقاً لنظرية بيكارد الصغرى، أي دالة كلية غير ثابتة \\(f: \\mathbb{C} \\to \\mathbb{C}\\) تأخذ كل قيمة عقدية باستثناء كم قيمة على الأكثر؟",
      ["At most 1 exception", "At most 2 exceptions", "At most 0 exceptions (no exceptions)", "Infinitely many exceptions"],
      0,
      "Picard's Little Theorem states that if an entire function \\(f\\) omits two or more complex values, then \\(f\\) must be constant. Consequently, any non-constant entire function omits at most ONE complex value. For example, \\(f(z) = e^z\\) omits only the single value \\(0\\).",
      "تنص نظرية بيكارد الصغرى على أن أي دالة كلية تغفل قيمتين عقديتين أو أكثر يجب أن تكون ثابتة. بالتالي، فإن أي دالة كلية غير ثابتة يمكن أن تغفل قيمة واحدة على الأكثر (مثل الدالة الأسية \\(e^z\\) التي تغفل القيمة 0 فقط).",
      "Consider \\(e^z\\) which never takes the value 0.",
      "فكر في الدالة الأسية \\(e^z\\) التي لا تأخذ القيمة صفر أبداً.")

    # 436: Bivariate Normal Independence via Zero Covariance
    q("KAUST-P2-436", "Probability & Statistics", "Medium",
      "If \\((X, Y)\\) are jointly normally distributed, which condition is necessary AND sufficient for \\(X\\) and \\(Y\\) to be statistically independent?",
      "إذا كان \\((X, Y)\\) زوجاً عشوائياً طبيعياً مشتركاً، فأي شرط هو لازم وكافٍ لكي يكون \\(X\\) و \\(Y\\) مستقلين إحصائياً؟",
      ["\\(\\text{Cov}(X, Y) = 0\\)",
       "\\(\\mathbb{E}[X] = \\mathbb{E}[Y]\\)",
       "\\(\\text{Var}(X) = \\text{Var}(Y)\\)",
       "\\(\\mathbb{P}(X > 0) = \\mathbb{P}(Y > 0)\\)"],
      0,
      "In general probability theory, independence implies zero covariance (uncorrelated), but zero covariance does not imply independence. However, for jointly Gaussian random variables, the joint PDF factors as \\(f_{X,Y}(x,y) = f_X(x) f_Y(y)\\) if and only if the correlation coefficient \\(\\rho = 0\\), which is equivalent to \\(\\text{Cov}(X, Y) = 0\\).",
      "في الحالة العامة، الاستقلال يقتضي انعدام التغاير، ولكن العكس غير صحيح عموماً. ومع ذلك، للمتغيرات ذات التوزيع الطبيعي المشترك، ينفصل التوزيع المشترك إلى جداء توزيعين هامشيين إذا وفقط إذا كان التغاير صفراً: \\(\\text{Cov}(X, Y) = 0\\).",
      "For joint Gaussian variables, uncorrelatedness is equivalent to independence.",
      "للمتغيرات الطبيعية المشتركة، انعدام الارتباط يكافئ الاستقلال التام.")

    # 437: Entire Function with Positive Real Part
    q("KAUST-P2-437", "Complex Analysis", "Hard",
      "Let \\(f(z)\\) be an entire function such that \\(\\text{Re}(f(z)) > 0\\) for all \\(z \\in \\mathbb{C}\\). What must \\(f(z)\\) be?",
      "لتكن \\(f(z)\\) دالة كلية بحيث \\(\\text{Re}(f(z)) > 0\\) لجميع \\(z \\in \\mathbb{C}\\). ماذا يجب أن تكون \\(f(z)\\)؟",
      ["A constant function",
       "A linear function \\(az + b\\)",
       "An exponential function \\(e^{az}\\)",
       "A polynomial of odd degree"],
      0,
      "Consider the function \\(g(z) = e^{-f(z)}\\). Since \\(f\\) is entire, \\(g\\) is also entire. Compute its modulus: \\(|g(z)| = |e^{-\\text{Re}(f) - i \\text{Im}(f)}| = e^{-\\text{Re}(f(z))}\\). Because \\(\\text{Re}(f(z)) > 0\\), we have \\(-\\text{Re}(f(z)) < 0\\), which means \\(|g(z)| < e^0 = 1\\) for all \\(z \\in \\mathbb{C}\\). Thus \\(g(z)\\) is a bounded entire function. By Liouville's Theorem, \\(g(z)\\) must be constant: \\(e^{-f(z)} = c \\implies f(z) = -\\ln c = \\text{constant}\\).",
      "نأخذ الدالة المساعدة \\(g(z) = e^{-f(z)}\\). بما أن \\(f\\) كلية، فإن \\(g\\) كلية. مقياسها \\(|g(z)| = e^{-\\text{Re}(f)} < 1\\) لأن الجزء الحقيقي موجب دائماً. حسب نظرية ليوڤيل، أي دالة كلية ومحدودة هي دالة ثابتة، إذن \\(g\\) ثابتة ومن ثم \\(f\\) ثابتة بالضرورة.",
      "Apply Liouville's theorem to the auxiliary function \\(g(z) = e^{-f(z)}\\).",
      "طبق نظرية ليوڤيل على الدالة المساعدة \\(e^{-f(z)}\\).")

    # 438: Joint CDF to Marginal CDF
    q("KAUST-P2-438", "Probability & Statistics", "Medium",
      "Given the joint cumulative distribution function \\(F_{X,Y}(x, y)\\), how is the marginal CDF \\(F_X(x)\\) obtained?",
      "إذا عُلمت دالة التوزيع التراكمي المشتركة \\(F_{X,Y}(x, y)\\)، كيف نحصل على دالة التوزيع الهامشية \\(F_X(x)\\)؟",
      ["\\(F_X(x) = \\lim_{y \\to \\infty} F_{X,Y}(x, y)\\)",
       "\\(F_X(x) = F_{X,Y}(x, 0)\\)",
       "\\(F_X(x) = \\frac{\\partial}{\\partial x} F_{X,Y}(x, y)\\)",
       "\\(F_X(x) = \\lim_{y \\to 0} F_{X,Y}(x, y)\\)"],
      0,
      "By definition of cumulative probability: \\(F_X(x) = \\mathbb{P}(X \\le x) = \\mathbb{P}(X \\le x, Y < \\infty) = \\lim_{y \\to \\infty} F_{X,Y}(x, y)\\). Letting \\(y \\to \\infty\\) removes any restriction on \\(Y\\), leaving the marginal probability for \\(X\\).",
      "حسب تعريف الاحتمال التراكمي: \\(F_X(x) = \\mathbb{P}(X \\le x) = \\mathbb{P}(X \\le x, Y < \\infty) = \\lim_{y \\to \\infty} F_{X,Y}(x, y)\\). جعل \\(y \\to \\infty\\) يرفع أي قيد على \\(Y\\).",
      "Consider the event \\(Y < \\infty\\) as an unconstrained condition.",
      "تأمل الحدث \\(Y < \\infty\\) كشرط غير مقيد.")

    # 439: Identity Theorem in Complex Analysis
    q("KAUST-P2-439", "Complex Analysis", "Hard",
      "Let \\(f\\) and \\(g\\) be holomorphic functions on a connected open domain \\(D\\). If \\(f(1/n) = g(1/n)\\) for all integers \\(n \\ge 1\\), which theorem implies that \\(f(z) = g(z)\\) everywhere on \\(D\\)?",
      "لتكن \\(f\\) و \\(g\\) دالتين هولومورفيتين على نطاق مفتوح مترابط \\(D\\). إذا كان \\(f(1/n) = g(1/n)\\) لجميع الأعداد الصحيحة \\(n \\ge 1\\)، فأي نظرية تقتضي أن \\(f(z) = g(z)\\) في كامل النطاق \\(D\\)؟",
      ["The Identity Theorem (Uniqueness Theorem)",
       "The Open Mapping Theorem",
       "Weierstrass Factorization Theorem",
       "Cauchy's Residue Theorem"],
      0,
      "The Identity Theorem states that if two holomorphic functions on a connected domain coincide on a set that has an accumulation point (limit point) inside the domain, then they coincide on the entire domain. The sequence of points \\(z_n = 1/n\\) has accumulation point \\(z = 0\\). Since \\(0 \\in D\\), the coincidence set has an interior limit point, forcing \\(f(z) \\equiv g(z)\\) on all of \\(D\\).",
      "تنص نظرية المطابقة (أو الأحادية) على أنه إذا اتفقت دالتان هولومورفيتان على مجموعة نقاط لها نقطة تراكم (limit point) تقع داخل النطاق، فإنهما متطابقتان في كامل النطاق. المتتالية \\(1/n\\) تتقارب للصفر، فتنطبق النظرية تماماً.",
      "Notice that \\(z_n = 1/n\\) has an accumulation point at \\(z = 0\\).",
      "لاحظ أن المتتالية \\(1/n\\) تمتلك نقطة تراكم عند الصفر داخل النطاق.")

    # 440: Chi-Square Distribution Degrees of Freedom
    q("KAUST-P2-440", "Probability & Statistics", "Medium",
      "If \\(Z_1, Z_2, \\dots, Z_k\\) are independent standard normal variables \\(\\mathcal{N}(0, 1)\\), what is the mean and variance of \\(Q = \\sum_{i=1}^k Z_i^2\\)?",
      "إذا كانت \\(Z_1, \\dots, Z_k\\) متغيرات عشوائية طبيعية قياسية مستقلة \\(\\mathcal{N}(0, 1)\\)، فما هما المتوسط والتباين لـ \\(Q = \\sum_{i=1}^k Z_i^2\\)؟",
      ["\\(\\mathbb{E}[Q] = k, \\quad \\text{Var}(Q) = 2k\\)",
       "\\(\\mathbb{E}[Q] = k, \\quad \\text{Var}(Q) = k\\)",
       "\\(\\mathbb{E}[Q] = 2k, \\quad \\text{Var}(Q) = 4k\\)",
       "\\(\\mathbb{E}[Q] = k^2, \\quad \\text{Var}(Q) = 2k^2\\)"],
      0,
      "The random variable \\(Q = \\sum_{i=1}^k Z_i^2\\) follows a Chi-square distribution with \\(k\\) degrees of freedom, \\(Q \\sim \\chi^2(k)\\). For each \\(Z_i^2\\): \\(\\mathbb{E}[Z_i^2] = 1\\) and \\(\\text{Var}(Z_i^2) = \\mathbb{E}[Z_i^4] - (\\mathbb{E}[Z_i^2])^2 = 3(1)^2 - 1^2 = 2\\). By independence and linearity of expectation and variance: \\(\\mathbb{E}[Q] = \\sum_{i=1}^k 1 = k\\), and \\(\\text{Var}(Q) = \\sum_{i=1}^k 2 = 2k\\).",
      "المتغير \\(Q\\) يتبع توزيع كاي-تربيع بدرجات حرية \\(k\\). لكل متغير: \\(\\mathbb{E}[Z_i^2] = 1\\) و \\(\\text{Var}(Z_i^2) = 3 - 1 = 2\\). بجمع المتغيرات المستقلة نجد المتوسط \\(k\\) والتباين \\(2k\\).",
      "Recall \\(\\mathbb{E}[Z^4] = 3\\sigma^4 = 3\\) for a standard normal variable.",
      "تذكر أن العزم الرابع للمتغير الطبيعي القياسي هو 3.")

    # 441: Entire Function with Restricted Real Part
    q("KAUST-P2-441", "Complex Analysis", "Medium",
      "If \\(f(z) = u(x, y) + i v(x, y)\\) is an entire function such that \\(u(x, y) \\le 5\\) for all \\(z \\in \\mathbb{C}\\), what can be concluded?",
      "إذا كانت \\(f(z) = u(x, y) + i v(x, y)\\) دالة كلية بحيث \\(u(x, y) \\le 5\\) لجميع \\(z \\in \\mathbb{C}\\)، فما الاستنتاج؟",
      ["\\(f(z)\\) is a constant function",
       "\\(f(z)\\) is a polynomial of degree 5",
       "\\(f(z)\\) must be a periodic function",
       "\\(f(z) = 5\\)"],
      0,
      "Consider \\(g(z) = e^{f(z)}\\). Then \\(|g(z)| = e^{u(x, y)} \\le e^5\\). Since \\(g(z)\\) is entire and bounded by the constant \\(e^5\\) on the entire complex plane, Liouville's Theorem implies that \\(g(z)\\) is constant. Therefore, \\(f(z)\\) must also be a constant function.",
      "نأخذ الدالة المساعدة \\(g(z) = e^{f(z)}\\). مقياسها \\(|g(z)| = e^{u} \\le e^5\\). بما أن \\(g(z)\\) كلية ومحدودة بالعدد \\(e^5\\)، فإنها ثابتة حسب نظرية ليوڤيل، وبالتالي فإن \\(f(z)\\) ثابتة أيضاً.",
      "Consider \\(g(z) = e^{f(z)}\\) and check its boundedness.",
      "انظر إلى الدالة \\(e^{f(z)}\\) وافحص محدوديتها.")

    # 442: Sample Mean and Sample Variance Independence
    q("KAUST-P2-442", "Probability & Statistics", "Hard",
      "Basu's Theorem / Cochran's Theorem establishes that for a random sample \\(X_1, \\dots, X_n\\) from a normal distribution \\(\\mathcal{N}(\\mu, \\sigma^2)\\), the sample mean \\(\\bar{X}\\) and the sample variance \\(S^2\\) are:",
      "تثبت نظرية كوشران / نظرية باسو أنه لعينة عشوائية \\(X_1, \\dots, X_n\\) من توزيع طبيعي، فإن المتوسط الحسابي للعينة \\(\\bar{X}\\) وتباين العينة \\(S^2\\):",
      ["Statistically independent",
       "Positively correlated with \\(\\rho = 1/\\sqrt{n}\\)",
       "Identically distributed",
       "Negatively correlated"],
      0,
      "A celebrated property unique to normal distributions (proven by Geary and Cochran) is that the sample mean \\(\\bar{X}\\) and sample variance \\(S^2 = \\frac{1}{n-1}\\sum (X_i - \\bar{X})^2\\) are statistically independent. This property forms the mathematical foundation of Student's \\(t\\)-test and Fisher's \\(F\\)-test.",
      "من الخواص الفريدة للتوزيع الطبيعي أن المتوسط الحسابي للعينة \\(\\bar{X}\\) وتباين العينة \\(S^2\\) مستقلان إحصائياً تماماً. وهذه الخاصية تشكل الأساس الرياضي لاختبار \\(t\\) واختبار \\(F\\).",
      "Recall this fundamental property that underlies the derivation of Student's t-distribution.",
      "تذكر هذه الخاصية الجوهرية التي يستند إليها اشتقاق توزيع ستودنت.")

    # 443: Winding Number (Index of a Curve)
    q("KAUST-P2-443", "Complex Analysis", "Medium",
      "The winding number (index) of a closed path \\(\\gamma\\) with respect to a point \\(z_0 \\notin \\gamma\\) is defined as \\(I(\\gamma, z_0) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{dz}{z - z_0}\\). If \\(\\gamma\\) traverses the circle \\(|z| = 3\\) three times counterclockwise, what is \\(I(\\gamma, 1 + i)\\)?",
      "دليل الدوران (winding number) لمسار مغلق \\(\\gamma\\) بالنسبة لنقطة \\(z_0\\) يعرف بـ \\(I(\\gamma, z_0) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{dz}{z - z_0}\\). إذا كان \\(\\gamma\\) يطوف حول الدائرة \\(|z| = 3\\) ثلاث مرات بعكس اتجاه عقارب الساعة، فما قيمة \\(I(\\gamma, 1 + i)\\)؟",
      ["\\(3\\)", "\\(1\\)", "\\(0\\)", "\\(3/2\\)"],
      0,
      "The point \\(z_0 = 1 + i\\) has distance \\(|1 + i| = \\sqrt{1^2 + 1^2} = \\sqrt{2} \\approx 1.414 < 3\\), so it lies strictly inside the circle \\(|z| = 3\\). The winding number counts how many times the closed curve winds counterclockwise around the point. Since the curve winds 3 times in the positive counterclockwise direction around the disc containing \\(1 + i\\), the winding number is exactly \\(3\\).",
      "النقطة \\(1 + i\\) تقع داخل الدائرة لأن معيارها \\(\\sqrt{2} < 3\\). بما أن المسار يلتف 3 مرات بالاتجاه الموجب حول القرص الذي يحوي النقطة، فإن دليل الدوران هو 3 بالضبط.",
      "Check whether \\(1+i\\) is inside the circle and count the number of counterclockwise loops.",
      "تحقق من وقوع النقطة داخل الدائرة واعدد الدورات الموجبة.")

    # 444: Transformation of Uniform to Cauchy
    q("KAUST-P2-444", "Probability & Statistics", "Hard",
      "Let \\(U \\sim \\text{Uniform}(-\\pi/2, \\pi/2)\\). What is the probability distribution of \\(X = \\tan(U)\\)?",
      "ليكن \\(U \\sim \\text{Uniform}(-\\pi/2, \\pi/2)\\). ما هو التوزيع الاحتمالي لـ \\(X = \\tan(U)\\)؟",
      ["Standard Cauchy distribution", "Standard Normal distribution", "Standard Logistic distribution", "Student's t-distribution with 2 degrees of freedom"],
      0,
      "The CDF of \\(X\\) is \\(F_X(x) = \\mathbb{P}(\\tan U \\le x) = \\mathbb{P}(U \\le \\arctan x)\\). Since \\(U\\) is uniform on \\((-\\pi/2, \\pi/2)\\), its CDF is \\(F_U(u) = \\frac{u - (-\\pi/2)}{\\pi} = \\frac{u}{\\pi} + \\frac{1}{2}\\). Thus \\(F_X(x) = \\frac{\\arctan x}{\\pi} + \\frac{1}{2}\\). Differentiating with respect to \\(x\\): \\(f_X(x) = \\frac{1}{\\pi(1 + x^2)}\\), which is precisely the standard Cauchy distribution.",
      "دالة التوزيع لـ \\(X\\) هي \\(\\mathbb{P}(U \\le \\arctan x) = \\frac{\\arctan x}{\\pi} + \\frac{1}{2}\\). باشتقاقها بالنسبة لـ \\(x\\) نجد الكثافة \\(f(x) = \\frac{1}{\\pi(1+x^2)}\\)، وهي كثافة توزيع كوشي القياسي.",
      "Compute \\(\\frac{d}{dx} \\left(\\frac{\\arctan(x)}{\\pi}\\right)\\).",
      "فاضل دالة التوزيع التراكمي المحتوية على \\(\\arctan(x)\\).")

    # 445: Great Picard Theorem
    q("KAUST-P2-445", "Complex Analysis", "Hard",
      "Picard's Great Theorem describes the behavior of a function near an essential singularity \\(z_0\\). It states that in any punctured neighborhood of \\(z_0\\), the function takes every complex value infinitely often, with at most:",
      "تصف نظرية بيكارد الكبرى سلوك الدالة بالقرب من الشذوذ الجوهري \\(z_0\\). تنص على أنه في أي جوار مثقوب، تأخذ الدالة كل قيمة عقدية عدداً لا نهائياً من المرات باستثناء:",
      ["At most one value", "At most two values", "At most finitely many values", "No exceptions"],
      0,
      "Picard's Great Theorem states that if \\(z_0\\) is an essential singularity of \\(f(z)\\), then in any punctured neighborhood of \\(z_0\\), \\(f(z)\\) assumes every complex value infinitely many times, with at most one exception. For example, \\(f(z) = e^{1/z}\\) has an essential singularity at \\(z = 0\\), and it takes every non-zero value infinitely often, omitting only \\(0\\).",
      "تنص نظرية بيكارد الكبرى على أن الدالة في أي جوار لشذوذ جوهري تأخذ كل قيمة عقدية عدداً لا نهائياً من المرات باستثناء قيمة واحدة على الأكثر (مثل \\(e^{1/z}\\) التي تغفل القيمة 0 فقط).",
      "Recall the example \\(f(z) = e^{1/z}\\) at \\(z = 0\\).",
      "تذكر مثال الدالة \\(e^{1/z}\\) عند نقطة الأصل.")

    # 446: Convex Combination of Normal Means
    q("KAUST-P2-446", "Probability & Statistics", "Medium",
      "Let \\(X_1, X_2\\) be independent random variables with \\(X_1 \\sim \\mathcal{N}(\\mu, \\sigma_1^2)\\) and \\(X_2 \\sim \\mathcal{N}(\\mu, \\sigma_2^2)\\). Which unbiased estimator \\(\\hat{\\mu} = w X_1 + (1 - w) X_2\\) minimizes the variance \\(\\text{Var}(\\hat{\\mu})\\)?",
      "ليكن \\(X_1, X_2\\) متغيرين مستقلين مع \\(X_1 \\sim \\mathcal{N}(\\mu, \\sigma_1^2)\\) و \\(X_2 \\sim \\mathcal{N}(\\mu, \\sigma_2^2)\\). أي مقدر غير متحيز \\(\\hat{\\mu} = w X_1 + (1 - w) X_2\\) يقلل التباين \\(\\text{Var}(\\hat{\\mu})\\) إلى أدنى حد؟",
      ["\\(w = \\frac{\\sigma_2^2}{\\sigma_1^2 + \\sigma_2^2}\\)",
       "\\(w = \\frac{\\sigma_1^2}{\\sigma_1^2 + \\sigma_2^2}\\)",
       "\\(w = \\frac{1}{2}\\)",
       "\\(w = \\frac{\\sigma_1}{\\sigma_1 + \\sigma_2}\\)"],
      0,
      "The variance is \\(V(w) = w^2 \\sigma_1^2 + (1 - w)^2 \\sigma_2^2\\). Differentiating with respect to \\(w\\) and setting to zero: \\(V'(w) = 2w \\sigma_1^2 - 2(1 - w) \\sigma_2^2 = 0 \\implies w(\\sigma_1^2 + \\sigma_2^2) = \\sigma_2^2 \\implies w = \\frac{\\sigma_2^2}{\\sigma_1^2 + \\sigma_2^2}\\). This gives inverse-variance weighting.",
      "التباين هو \\(V(w) = w^2 \\sigma_1^2 + (1-w)^2 \\sigma_2^2\\). باشتقاق التباين ومساواته بالصفر: \\(2w\\sigma_1^2 - 2(1-w)\\sigma_2^2 = 0\\)، ومنه \\(w = \\frac{\\sigma_2^2}{\\sigma_1^2 + \\sigma_2^2}\\)، وهو ما يعرف بالترجيح العكسي للتباين.",
      "Minimize \\(w^2 \\sigma_1^2 + (1-w)^2 \\sigma_2^2\\) with respect to \\(w\\).",
      "أوجد النهاية الصغرى لدالة التباين بالنسبة للوزن \\(w\\).")

    # 447: Rescaling Möbius Transformation Fixpoints
    q("KAUST-P2-447", "Complex Analysis", "Hard",
      "Find the fixed points (solutions to \\(f(z) = z\\)) of the Möbius transformation \\(f(z) = \\frac{3z - 1}{z + 1}\\).",
      "أوجد النقاط الصامدة (حلول \\(f(z) = z\\)) لتحويل موبيوس \\(f(z) = \\frac{3z - 1}{z + 1}\\).",
      ["\\(z = 1\\) (a single fixed point of multiplicity 2)",
       "\\(z = 1\\) and \\(z = -1\\)",
       "\\(z = 0\\) and \\(z = 3\\)",
       "\\(z = 1 \\pm i\\)"],
      0,
      "Set \\(f(z) = z\\): \\(\\frac{3z - 1}{z + 1} = z \\implies 3z - 1 = z(z + 1) = z^2 + z \\implies z^2 - 2z + 1 = 0 \\implies (z - 1)^2 = 0\\). Thus there is a single repeated fixed point at \\(z = 1\\). In the classification of Möbius transformations, a transformation with a single repeated fixed point is parabolic.",
      "بمساواة \\(f(z) = z\\): \\(3z - 1 = z^2 + z \\implies z^2 - 2z + 1 = 0\\)، أي \\((z-1)^2 = 0\\). يوجد جذر مكرر واحد هو \\(z = 1\\). وهذا يصنف التحويل على أنه تحويل مكافئ (parabolic).",
      "Solve the quadratic equation \\(z(z+1) = 3z - 1\\).",
      "حل المعادلة التربيعية الناتجة عن مساواة الدالة بـ \\(z\\).")

    # 448: Conformal Angle Preservation
    q("KAUST-P2-448", "Complex Analysis", "Medium",
      "At which points does the holomorphic mapping \\(f(z) = z^3 - 3z\\) FAIL to be conformal?",
      "عند أي نقاط يفشل التطبيق الهولومورفي \\(f(z) = z^3 - 3z\\) في أن يكون امتثالياً (conformal)؟",
      ["\\(z = \\pm 1\\)", "\\(z = 0\\)", "\\(z = \\pm \\sqrt{3}\\)", "\\(z = \\pm i\\)"],
      0,
      "A holomorphic function is conformal at all points where its complex derivative is non-zero (\\(f'(z) \\neq 0\\)). Differentiating: \\(f'(z) = 3z^2 - 3 = 3(z^2 - 1) = 0 \\implies z^2 = 1 \\implies z = \\pm 1\\). At \\(z = \\pm 1\\), angles between curves are multiplied by the multiplicity of the zero (doubled), so the mapping fails to be conformal at \\(z = 1\\) and \\(z = -1\\).",
      "تكون الدالة التحليلية امتثالية (حافظة للزوايا) عند جميع النقاط التي لا ينعدم عندها مشتقها: \\(f'(z) \\neq 0\\). المشتق هو \\(3z^2 - 3 = 0 \\implies z = \\pm 1\\). عند هاتين النقطتين تتضاعف الزوايا ولا تكون الدالة امتثالية.",
      "Find the points where the derivative \\(f'(z) = 0\\).",
      "أوجد النقاط التي ينعدم عندها المشتق الأول للدالة.")

    # 449: Log-Normal Mean and Variance
    q("KAUST-P2-449", "Probability & Statistics", "Medium",
      "If \\(Y = \\ln X \\sim \\mathcal{N}(\\mu, \\sigma^2)\\), what is the median of the log-normal distribution \\(X\\)?",
      "إذا كان \\(Y = \\ln X \\sim \\mathcal{N}(\\mu, \\sigma^2)\\)، فما هو وسيط (median) التوزيع اللوغاريتمي الطبيعي \\(X\\)؟",
      ["\\(e^\\mu\\)", "\\(e^{\\mu + \\sigma^2/2}\\)", "\\(e^{\\mu - \\sigma^2/2}\\)", "\\(\\mu\\)"],
      0,
      "The normal random variable \\(Y\\) is symmetric about its mean, so the median of \\(Y\\) is \\(\\mu\\). Since the exponential function \\(g(y) = e^y\\) is strictly monotonically increasing, it preserves percentiles. Thus the median of \\(X = e^Y\\) is simply \\(e^{\\text{median}(Y)} = e^\\mu\\). Note that the mean is \\(e^{\\mu + \\sigma^2/2} > e^\\mu\\).",
      "المتغير الطبيعي \\(Y\\) متناظر، لذا وسيطه يساوي متوسطه \\(\\mu\\). وبما أن الدالة الأسية دالة متزايدة تماماً، فإنها تحافظ على المئينات، ويكون وسيط \\(X = e^Y\\) هو \\(e^\\mu\\).",
      "Apply the strictly increasing transformation \\(e^y\\) to the median of the normal distribution.",
      "طبق التحويل المتزايد تماماً على وسيط التوزيع الطبيعي.")

    # 450: Poisson Summation Formula (Fourier / Complex Analysis)
    q("KAUST-P2-450", "Complex Analysis", "Hard",
      "The Poisson Summation Formula states that for a Schwartz function \\(f\\), \\(\\sum_{n=-\\infty}^\\infty f(n) = \\sum_{k=-\\infty}^\\infty \\hat{f}(k)\\). Applying this to \\(f(x) = e^{-\\pi a x^2}\\) with \\(\\hat{f}(\\xi) = a^{-1/2} e^{-\\pi \\xi^2 / a}\\) yields which famous modular relation for the Jacobi theta function \\(\\vartheta(a) = \\sum_{n=-\\infty}^\\infty e^{-\\pi n^2 a}\\)?",
      "تنص صيغة بواسون التجميعية على أن \\(\\sum f(n) = \\sum \\hat{f}(k)\\). بتطبيقها على دالة غاوسية نصل إلى أي علاقة نمطية (modular relation) شهيرة لدالة ثيتا لجاكوبي \\(\\vartheta(a) = \\sum_{n=-\\infty}^\\infty e^{-\\pi n^2 a}\\)؟",
      ["\\(\\vartheta(a) = \\frac{1}{\\sqrt{a}} \\vartheta\\left(\\frac{1}{a}\\right)\\)",
       "\\(\\vartheta(a) = \\sqrt{a} \\vartheta\\left(\\frac{1}{a}\\right)\\)",
       "\\(\\vartheta(a) = a \\vartheta(a^2)\\)",
       "\\(\\vartheta(a) = \\frac{1}{a} \\vartheta(a)\\)"],
      0,
      "Substituting \\(f(n) = e^{-\\pi a n^2}\\) and \\(\\hat{f}(k) = \\frac{1}{\\sqrt{a}} e^{-\\pi k^2 / a}\\) into the Poisson summation formula \\(\\sum_{n=-\\infty}^\\infty f(n) = \\sum_{k=-\\infty}^\\infty \\hat{f}(k)\\) gives immediately: \\(\\sum_{n=-\\infty}^\\infty e^{-\\pi a n^2} = \\frac{1}{\\sqrt{a}} \\sum_{k=-\\infty}^\\infty e^{-\\pi k^2 (1/a)}\\). In terms of the Jacobi theta function \\(\\vartheta(a)\\), this is the celebrated functional equation \\(\\vartheta(a) = \\frac{1}{\\sqrt{a}}\\vartheta(1/a)\\), which Riemann used to prove the functional equation of the Riemann zeta function.",
      "بالتعويض في صيغة بواسون التجميعية نجد \\(\\sum e^{-\\pi a n^2} = \\frac{1}{\\sqrt{a}} \\sum e^{-\\pi k^2 / a}\\). بدلالة دالة ثيتا، تصبح \\(\\vartheta(a) = \\frac{1}{\\sqrt{a}}\\vartheta(1/a)\\)، وهي المعادلة الدالية المحورية التي استند إليها ريمان لإثبات المعادلة الدالية لدالة زيتا ريمان.",
      "Directly substitute \\(f(n)\\) and \\(\\hat{f}(k)\\) into Poisson's summation formula.",
      "عوض بالدالة وتحويل فورييه الخاص بها في صيغة بواسون التجميعية مباشرة.")

    return questions

if __name__ == "__main__":
    qs = get_p2_part_d()
    print(f"Loaded {len(qs)} questions for Phase 2 Part D.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=401):
        expected_id = f"KAUST-P2-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 2 Part D questions successfully verified!")
