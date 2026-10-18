#!/usr/bin/env python3
"""
KAUST Phase 3 Questions Part B: 301 to 350
Elite Research: Functional Analysis, Spectral Theory & Calculus of Variations:
Banach and Hilbert spaces, Riesz representation, Hahn-Banach, Uniform boundedness,
Compact and self-adjoint operators, Spectral theorem, Weak convergence,
Calculus of Variations: Euler-Lagrange, Beltrami identity, Brachistochrone, Geodesics,
Isoperimetric problems, Minimal surfaces.
Authentic lineages: Cambridge Tripos Part II/III, MIT 18.102, Harvard Math 212, Princeton MAT 325.
"""

def get_p3_part_b():
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

    # 301: Parallelogram Law and Inner Product Spaces
    q("KAUST-P3-301", "Functional Analysis", "Medium",
      "The Jordan-von Neumann theorem establishes that a normed space \\((X, \\|\\cdot\\|)\\) can have its norm induced by an inner product \\(\\langle x, y \\rangle\\) if and only if which identity holds for all \\(x, y \\in X\\)?",
      "تثبت نظرية جوردان-فون نيومان أن فضاءً معيارياً \\((X, \\|\\cdot\\|)\\) يكون معياره مستحثاً من جداء داخلي إذا وفقط إذا تحققت أي متطابقة لجميع \\(x, y \\in X\\)؟",
      ["\\(\\|x + y\\|^2 + \\|x - y\\|^2 = 2\\|x\\|^2 + 2\\|y\\|^2\\) (Parallelogram Law)",
       "\\(\\|x + y\\| \\le \\|x\\| + \\|y\\|\\) (Triangle Inequality)",
       "\\(|\\langle x, y \\rangle| \\le \\|x\\| \\|y\\|\\) (Cauchy-Schwarz Inequality)",
       "\\(\\|x + y\\|^2 = \\|x\\|^2 + \\|y\\|^2\\) (Pythagorean Theorem)"],
      0,
      "The Jordan-von Neumann theorem (1935) proves that the parallelogram law \\(\\|x + y\\|^2 + \\|x - y\\|^2 = 2\\|x\\|^2 + 2\\|y\\|^2\\) is both necessary and sufficient for a norm to arise from an inner product. When this holds, the inner product is uniquely recovered via polarization: \\(\\langle x, y \\rangle = \\frac{1}{4}(\\|x+y\\|^2 - \\|x-y\\|^2)\\) for real spaces.",
      "تثبت مبرهنة جوردان-فون نيومان أن قانون متوازي الأضلاع \\(\\|x + y\\|^2 + \\|x - y\\|^2 = 2\\|x\\|^2 + 2\\|y\\|^2\\) هو الشرط اللازم والكافي لكي ينشأ المعيار من جداء داخلي، ويمكن استرجاع الجداء الداخلي عبر متطابقة الاستقطاب.",
      "Think of the geometric relation between diagonal lengths and side lengths of a parallelogram.",
      "فكر في العلاقة الهندسية بين أطوال أقطار وأضلاع متوازي الأضلاع.")

    # 302: Beltrami Identity for Autonomous Lagrangian
    q("KAUST-P3-302", "Calculus of Variations", "Hard",
      "When minimizing an action functional \\(J[y] = \\int_{x_1}^{x_2} L(y, y') dx\\) whose Lagrangian has no explicit dependence on the independent variable \\(x\\) (\\(\\partial L/\\partial x = 0\\)), the Euler-Lagrange equation integrates to which first integral (Beltrami identity)?",
      "عند تصغير دالية الفعل \\(J[y] = \\int L(y, y') dx\\) حيث لا يعتمد اللاغرانجي صراحة على المتغير المستقل \\(x\\)، يختزل قانون أويلر-لاغرانج إلى أي تكامل أول (متطابقة بلترامي)؟",
      ["\\(L - y' \\frac{\\partial L}{\\partial y'} = C\\)",
       "\\(L + y' \\frac{\\partial L}{\\partial y'} = C\\)",
       "\\(\\frac{\\partial L}{\\partial y'} = C\\)",
       "\\(y \\frac{\\partial L}{\\partial y'} - L = C\\)"],
      0,
      "Differentiate \\(H = L - y' \\frac{\\partial L}{\\partial y'}\\) with respect to \\(x\\): \\(\\frac{dH}{dx} = \\frac{dL}{dx} - y'' \\frac{\\partial L}{\\partial y'} - y' \\frac{d}{dx}\\left(\\frac{\\partial L}{\\partial y'}\\right)\\). By chain rule: \\(\\frac{dL}{dx} = \\frac{\\partial L}{\\partial x} + \\frac{\\partial L}{\\partial y}y' + \\frac{\\partial L}{\\partial y'}y''\\). Since \\(\\partial L/\\partial x = 0\\), we have \\(\\frac{dH}{dx} = y'\\left(\\frac{\\partial L}{\\partial y} - \\frac{d}{dx}\\frac{\\partial L}{\\partial y'}\\right) = y'(0) = 0\\) by the Euler-Lagrange equation. Thus \\(L - y'\\frac{\\partial L}{\\partial y'} = C\\) is conserved.",
      "باشتقاق المقدار \\(H = L - y' \\frac{\\partial L}{\\partial y'}\\) بالنسبة لـ \\(x\\) واستخدام قاعدة السلسلة ومعادلة أويلر-لاغرانج مع انعدام \\(\\partial L/\\partial x\\)، نجد أن \\(dH/dx = 0\\)، وبالتالي فإن المقدار \\(L - y'\\frac{\\partial L}{\\partial y'} = C\\) هو كمية محفوظة وثابتة.",
      "In classical mechanics, this conserved quantity corresponds to the Hamiltonian \\(H = p\\dot{q} - L\\).",
      "في الميكانيكا الكلاسيكية، هذه الكمية المحفوظة تقابل طاقة هاملتون.")

    # 303: Brachistochrone Problem Solution
    svg_cycloid = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-20 -20 160 100' width='100%' height='100%' style='background:#0d1117;'>
  <line x1='-15' y1='0' x2='135' y2='0' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-15' x2='0' y2='75' stroke='#8b949e' stroke-width='1.5'/>
  <!-- Cycloid curve -->
  <path d='M 0,0 C 20,45 60,65 110,60' fill='none' stroke='#58a6ff' stroke-width='2.5'/>
  <!-- Straight line comparison -->
  <line x1='0' y1='0' x2='110' y2='60' stroke='#8b949e' stroke-width='1.5' stroke-dasharray='4,4'/>
  <circle cx='0' cy='0' r='3.5' fill='#58a6ff'/>
  <circle cx='110' cy='60' r='3.5' fill='#f0883e'/>
  <text x='50' y='75' fill='#58a6ff' font-size='10' font-family='sans-serif'>Cycloid</text>
  <text x='55' y='25' fill='#8b949e' font-size='9' font-family='sans-serif'>Straight line</text>
</svg>"""
    q("KAUST-P3-303", "Calculus of Variations", "Hard",
      "The Brachistochrone problem (posed by Johann Bernoulli in 1696) asks for the path of fastest descent under gravity between two points. The optimal curve is:",
      "مسألة أسرع هبوط (البركستوكرون التي طرحها يوهان بيرنولي عام 1696) تبحث عن منحنى أسرع انحدار تحت تأثير الجاذبية بين نقطتين. المنحنى الأمثل هو:",
      ["A cycloid", "A catenary", "A parabola", "A straight line"],
      0,
      "The travel time functional is \\(T = \\int \\frac{ds}{v} = \\int \\frac{\\sqrt{1 + (y')^2}}{\\sqrt{2gy}} dx\\). The Lagrangian is \\(L(y, y') = \\frac{\\sqrt{1 + (y')^2}}{\\sqrt{y}}\\). Since \\(L\\) does not depend on \\(x\\), apply the Beltrami identity: \\(L - y' \\frac{\\partial L}{\\partial y'} = C \\implies \\frac{1}{\\sqrt{y(1 + (y')^2)}} = C\\). Setting \\(y'(x) = \\cot(\\theta/2)\\) and integrating yields the parametric equations of a cycloid: \\(x(\\theta) = R(\\theta - \\sin\\theta)\\), \\(y(\\theta) = R(1 - \\cos\\theta)\\).",
      "دالية زمن الانتقال هي \\(T = \\int \\frac{\\sqrt{1+(y')^2}}{\\sqrt{2gy}} dx\\). بتطبيق متطابقة بلترامي نصل إلى \\(y(1 + (y')^2) = 2R\\). بحل هذه المعادلة التفاضلية بالتعويض البارامتري، نحصل على المعادلات البارامترية لمنحنى الدويرية (cycloid).",
      "The curve is generated by a point on the rim of a rolling circle.",
      "المنحنى ناتج عن مسار نقطة على حافة دائرة تتدحرج على خط مستقيم.",
      diagram=svg_cycloid)

    # 304: Riesz Representation Theorem
    q("KAUST-P3-304", "Functional Analysis", "Medium",
      "The Riesz Representation Theorem for a Hilbert space \\(H\\) asserts that for every continuous linear functional \\(f \\in H^*\\), there exists a unique vector \\(y \\in H\\) such that for all \\(x \\in H\\):",
      "تنص نظرية ريس للتمثيل على فضاء هيلبرت \\(H\\) على أنه لكل تابع خطي مستمر \\(f \\in H^*\\)، يوجد متجه وحيد \\(y \\in H\\) بحيث يتحقق لكل \\(x \\in H\\):",
      ["\\(f(x) = \\langle x, y \\rangle\\) and \\(\\|f\\|_{H^*} = \\|y\\|_H\\)",
       "\\(f(x) = \\|x\\| \\|y\\|\\)",
       "\\(f(x) = \\langle x, x \\rangle + \\langle y, y \\rangle\\)",
       "\\(f(x) = \\frac{\\langle x, y \\rangle}{\\|y\\|}\\)"],
      0,
      "The Riesz-Fréchet Representation Theorem states that the mapping \\(y \\mapsto \\langle \\cdot, y \\rangle\\) is an isometric conjugate-linear isomorphism between \\(H\\) and its dual space \\(H^*\\). For every bounded linear functional \\(f\\), there exists a unique representing vector \\(y \\in H\\) such that \\(f(x) = \\langle x, y \\rangle\\), and the operator norm satisfies \\(\\|f\\|_{H^*} = \\|y\\|_H\\).",
      "تنص نظرية تمثيل ريس-فريشيه على وجود تقابل متساوي القياس بين فضاء هيلبرت وفضائه الثنوي، حيث يُمثَّل كل تابع خطي محدود \\(f\\) بمتجه وحيد \\(y\\) عبر الجداء الداخلي \\(f(x) = \\langle x, y \\rangle\\) مع تطابق المعيارين \\(\\|f\\| = \\|y\\|\\).",
      "Every bounded linear functional on a Hilbert space is given by inner product with a unique vector.",
      "كل تابع خطي محدود على فضاء هيلبرت يُعطى بالجداء الداخلي مع متجه فريد.")

    # 305: Catenoid as Minimal Surface of Revolution
    q("KAUST-P3-305", "Calculus of Variations", "Hard",
      "Find the surface of revolution obtained by rotating \\(y(x)\\) around the \\(x\\)-axis that minimizes the surface area functional \\(A[y] = 2\\pi \\int y \\sqrt{1 + (y')^2} dx\\).",
      "أوجد سطح الدوران الناتج عن تدوير \\(y(x)\\) حول محور السينات والذي يصغر مساحة السطح \\(A[y] = 2\\pi \\int y \\sqrt{1 + (y')^2} dx\\).",
      ["Catenoid \\(y(x) = c \\cosh\\left(\\frac{x - x_0}{c}\\right)\\)",
       "Cone \\(y(x) = m x\\)",
       "Sphere \\(y(x) = \\sqrt{R^2 - x^2}\\)",
       "Paraboloid \\(y(x) = a x^2\\)"],
      0,
      "The Lagrangian is \\(L(y, y') = y \\sqrt{1 + (y')^2}\\). Since \\(\\partial L/\\partial x = 0\\), apply the Beltrami identity: \\(L - y' \\frac{\\partial L}{\\partial y'} = C \\implies y \\sqrt{1 + (y')^2} - y' \\frac{y y'}{\\sqrt{1 + (y')^2}} = C \\implies \\frac{y(1 + (y')^2 - (y')^2)}{\\sqrt{1 + (y')^2}} = C \\implies \\frac{y}{\\sqrt{1 + (y')^2}} = C\\). Solving for \\(y'\\): \\((y')^2 = \\frac{y^2 - C^2}{C^2} \\implies \\frac{dy}{dx} = \\frac{\\sqrt{y^2 - C^2}}{C}\\). Separating variables: \\(\\int \\frac{C dy}{\\sqrt{y^2 - C^2}} = \\int dx \\implies C \\text{arcosh}(y/C) = x - x_0 \\implies y(x) = C \\cosh\\left(\\frac{x - x_0}{C}\\right)\\). The resulting surface is the catenoid, the only non-planar minimal surface of revolution.",
      "اللاغرانجي هو \\(L = y\\sqrt{1+(y')^2}\\). بمتطابقة بلترامي نجد \\(y / \\sqrt{1+(y')^2} = C\\). بفصل المتغيرات: \\(\\frac{C dy}{\\sqrt{y^2-C^2}} = dx\\). بالمكاملة ينتج \\(y = C\\cosh((x-x_0)/C)\\)، وهو منحنى السلسلة، وسطح دورانه هو القُطَيْعاني (catenoid).",
      "Use the Beltrami identity on \\(L = y\\sqrt{1+(y')^2}\\) and integrate using inverse hyperbolic cosine.",
      "طبق متطابقة بلترامي على اللاغرانجي وكامل باستخدام دالة جيب التمام الزائدي العكسية.")

    # 306: Compact Operator Spectrum
    q("KAUST-P3-306", "Spectral Theory", "Hard",
      "Let \\(T: H \\to H\\) be a compact linear operator on an infinite-dimensional Hilbert space. Which statement about its spectrum \\(\\sigma(T)\\) is FALSE?",
      "ليكن \\(T: H \\to H\\) مؤثراً خطياً مدمجاً (compact) على فضاء هيلبرت لا نهائي البعد. أي عبارة حول طيفه \\(\\sigma(T)\\) خاطئة؟",
      ["\\(\\sigma(T)\\) can contain an open interval of continuous spectrum",
       "\\(0 \\in \\sigma(T)\\)",
       "Every non-zero spectral value is an eigenvalue of finite multiplicity",
       "The non-zero eigenvalues form an at most countable set accumulating only at 0"],
      0,
      "The spectral theorem for compact operators (Fredholm-Riesz-Schauder theory) establishes that: 1) \\(0 \\in \\sigma(T)\\) in infinite dimensions; 2) every \\(\\lambda \\in \\sigma(T) \\setminus \\{0\\}\\) is an isolated eigenvalue of finite algebraic multiplicity; 3) the eigenvalues can only accumulate at 0. Therefore, \\(\\sigma(T)\\) cannot contain any open interval of continuous spectrum. Thus the statement that it can contain an open interval is false.",
      "تؤكد نظرية فريدهولم-ريس-شاودر للمؤثرات المدمجة أن الطيف غير الصفري يتكون حصراً من قيم ذاتية معزولة ذات تعدد منتهٍ تتراكم فقط عند الصفر، والصفر ينتمي حتماً للطيف. لا يمكن للطيف أن يحتوي على فترة مفتوحة متصلة أبداً.",
      "Recall the Fredholm alternative and isolated nature of non-zero eigenvalues for compact operators.",
      "تذكر أن القيم الذاتية غير الصفرية للمؤثر المدمج تكون معزولة وذات تعدد منتهٍ دائماً.")

    # 307: Hahn-Banach Theorem Consequence
    q("KAUST-P3-307", "Functional Analysis", "Medium",
      "A fundamental consequence of the Hahn-Banach theorem in a normed space \\(X\\) is that for any non-zero vector \\(x_0 \\in X\\), there exists a bounded linear functional \\(f \\in X^*\\) such that:",
      "من النتائج الجوهرية لنظرية هان-باناخ في الفضاء المعياري \\(X\\) أنه لأي متجه غير صفري \\(x_0\\)، يوجد تابع خطي محدود \\(f \\in X^*\\) يحقق:",
      ["\\(f(x_0) = \\|x_0\\|\\) and \\(\\|f\\|_{X^*} = 1\\)",
       "\\(f(x_0) = 0\\) and \\(\\|f\\|_{X^*} = 1\\)",
       "\\(f(x) = \\|x\\|^2\\) for all \\(x\\)",
       "\\(f(x_0) = 1\\) and \\(\\|f\\|_{X^*} = 0\\)"],
      0,
      "Define the functional on the 1-dimensional subspace \\(M = \\text{span}\\{x_0\\}\\) by \\(g(\\alpha x_0) = \\alpha \\|x_0\\|\\). The norm of \\(g\\) on \\(M\\) is \\(|g(\\alpha x_0)| / \\|\\alpha x_0\\| = |\\alpha| \\|x_0\\| / (|\\alpha| \\|x_0\\|) = 1\\). By the Hahn-Banach extension theorem, \\(g\\) can be extended to a bounded linear functional \\(f\\) on all of \\(X\\) with preserved norm \\(\\|f\\|_{X^*} = 1\\) and \\(f(x_0) = \\|x_0\\|\\). This ensures that \\(X^*\\) separates points in \\(X\\).",
      "نعرف تابعاً على الفضاء الجزئي \\(\\text{span}\\{x_0\\}\\) بـ \\(g(\\alpha x_0) = \\alpha \\|x_0\\|\\). حسب مبرهنة التمديد لهان-باناخ، يمكن تمديد هذا التابع إلى كامل الفضاء دون زيادة معياره، مما يعطي \\(f(x_0) = \\|x_0\\|\\) مع \\(\\|f\\| = 1\\).",
      "Hahn-Banach guarantees the existence of dual functionals that evaluate the norm of any given vector.",
      "تضمن نظرية هان-باناخ وجود دوال ثنوية تقيس معيار أي متجه معطى.")

    # 308: Uniform Boundedness Principle (Banach-Steinhaus)
    q("KAUST-P3-308", "Functional Analysis", "Medium",
      "The Uniform Boundedness Principle (Banach-Steinhaus theorem) states that if \\(X\\) is a Banach space, \\(Y\\) is a normed space, and \\(\\{T_i\\}_{i \\in I} \\subset B(X, Y)\\) satisfies \\(\\sup_{i \\in I} \\|T_i x\\| < \\infty\\) for all \\(x \\in X\\), then:",
      "ينص مبدأ المحدودية المنتظمة (مبرهنة باناخ-شتاينهاوس) على أنه إذا كان \\(X\\) فضاء باناخ وكانت عائلة المؤثرات مقيدة نقطياً لكل \\(x \\in X\\)، فإن:",
      ["\\(\\sup_{i \\in I} \\|T_i\\| < \\infty\\) (the family is uniformly bounded in operator norm)",
       "\\(T_i\\) converges strongly to zero",
       "Each \\(T_i\\) is a compact operator",
       "\\(X\\) must be finite-dimensional"],
      0,
      "The Banach-Steinhaus theorem establishes that pointwise boundedness implies uniform boundedness for families of continuous linear operators on a Banach space. That is, if \\(\\sup_{i \\in I} \\|T_i x\\| \\le M_x < \\infty\\) for every \\(x \\in X\\), then there exists a universal constant \\(M < \\infty\\) such that \\(\\sup_{i \\in I} \\|T_i\\|_{B(X,Y)} \\le M\\). The proof relies critically on the Baire Category Theorem.",
      "تثبت مبرهنة باناخ-شتاينهاوس أن المحدودية النقطية تستلزم المحدودية المنتظمة للمؤثرات على فضاءات باناخ، بالاعتماد الجوهري على مبرهنة بيري للفئات.",
      "Pointwise boundedness on a complete space promotes to uniform operator norm boundedness.",
      "المحدودية النقطية على فضاء تام ترتقي إلى محدودية منتظمة للمعيار المؤثري.")

    # 309: Open Mapping and Closed Graph Theorems
    q("KAUST-P3-309", "Functional Analysis", "Medium",
      "Let \\(T: X \\to Y\\) be a linear operator between Banach spaces \\(X\\) and \\(Y\\). The Closed Graph Theorem asserts that \\(T\\) is bounded (continuous) if and only if:",
      "ليكن \\(T: X \\to Y\\) مؤثراً خطياً بين فضاءي باناخ. تنص نظرية البيان المغلق على أن \\(T\\) يكون محدوداً (مستمراً) إذا وفقط إذا كان:",
      ["The graph \\(\\Gamma(T) = \\{(x, Tx) : x \\in X\\}\\) is closed in \\(X \\times Y\\)",
       "\\(T\\) is surjective",
       "The kernel \\(\\ker(T)\\) is closed",
       "\\(T\\) maps open sets to closed sets"],
      0,
      "The Closed Graph Theorem states that a linear map between Banach spaces is continuous if and only if its graph \\(\\Gamma(T)\\) is closed in the product space \\(X \\times Y\\). Concretely, this means: if \\(x_n \\to x\\) in \\(X\\) and \\(T x_n \\to y\\) in \\(Y\\), then necessarily \\(y = T x\\).",
      "تنص مبرهنة البيان المغلق على أن المؤثر الخطي بين فضاءي باناخ مستمر إذا وفقط إذا كان بيانه مغلقاً في الفضاء الجداء \\(X \\times Y\\). أي إذا تقارب \\(x_n \\to x\\) وتقارب \\(Tx_n \\to y\\)، فإن \\(y = Tx\\) حتماً.",
      "Check the condition on the graph \\(\\{(x, Tx)\\}\\).",
      "افحص الشرط المفروض على بيان المؤثر الخطي.")

    # 310: Weak Convergence in Hilbert Space
    q("KAUST-P3-310", "Functional Analysis", "Hard",
      "Let \\(\\{e_n\\}_{n=1}^\\infty\\) be an orthonormal basis for an infinite-dimensional Hilbert space \\(H\\). What is the weak limit of \\(e_n\\) as \\(n \\to \\infty\\)?",
      "لتكن \\(\\{e_n\\}\\) متتالية أساس متعامد عيارياً لفضاء هيلبرت لا نهائي البعد. ما هي النهاية الضعيفة لـ \\(e_n\\) عندما \\(n \\to \\infty\\)؟",
      ["\\(e_n \\rightharpoonup 0\\) weakly",
       "\\(e_n \\rightharpoonup e_1\\)",
       "The sequence does not converge weakly",
       "\\(e_n\\) converges strongly to 0"],
      0,
      "Weak convergence \\(e_n \\rightharpoonup x\\) means \\(\\lim_{n\\to\\infty} \\langle e_n, y \\rangle = \\langle x, y \\rangle\\) for every \\(y \\in H\\). By Bessel's inequality, \\(\\sum_{n=1}^\\infty |\\langle e_n, y \\rangle|^2 \\le \\|y\\|^2 < \\infty\\). For this convergent series, the general term must vanish: \\(\\lim_{n\\to\\infty} \\langle e_n, y \\rangle = 0\\). Therefore, \\(\\langle x, y \\rangle = 0\\) for all \\(y \\in H\\), which implies \\(x = 0\\). Thus \\(e_n \\rightharpoonup 0\\) weakly, even though \\(\\|e_n\\| = 1\\) (so it does not converge strongly to 0).",
      "التقارب الضعيف يعني \\(\\langle e_n, y \\rangle \\to \\langle x, y \\rangle\\) لكل \\(y\\). حسب متراجحة بيسل، المتسلسلة \\(\\sum |\\langle e_n, y \\rangle|^2\\) متقاربة، لذا فإن حدها النوني يؤول للصفر. هذا يثبت أن \\(e_n \\rightharpoonup 0\\) ضعيفاً، مع أن المعيار قوي وثابت \\(\\|e_n\\| = 1\\).",
      "Use Bessel's inequality \\(\\sum |\\langle e_n, y \\rangle|^2 < \\infty\\) to deduce the limit of the inner products.",
      "استخدم متراجحة بيسل لاستنتاج نهاية الجداء الداخلي.")

    # 311 to 350: Continuing systematic generation of Part B questions
    # 311: Banach-Alaoglu Theorem
    q("KAUST-P3-311", "Functional Analysis", "Hard",
      "The Banach-Alaoglu theorem is a cornerstone of modern functional analysis. It asserts that the closed unit ball of the dual space \\(X^*\\) of any normed space \\(X\\) is:",
      "تعتبر نظرية باناخ-علا أوغلو ركناً أساسياً في التحليل الدالي. تنص على أن كرة الوحدة المغلقة في الفضاء الثنوي \\(X^*\\) لأي فضاء معياري تكون:",
      ["Compact in the weak-* topology",
       "Compact in the strong norm topology",
       "Open in the weak-* topology",
       "Dense in \\(X^*\\)"],
      0,
      "The Banach-Alaoglu theorem states that the closed unit ball \\(B_{X^*} = \\{f \\in X^* : \\|f\\|_{X^*} \\le 1\\}\\) is compact in the weak-* topology \\(\\sigma(X^*, X)\\). In infinite dimensions, the unit ball is NEVER compact in the norm topology (by Riesz's lemma), making weak-* compactness indispensable for proving existence of minimizers in variational problems.",
      "تنص مبرهنة باناخ-علا أوغلو على أن كرة الوحدة المغلقة في الفضاء الثنوي مدمجة في الطوبولوجيا الضعيفة نجمة (weak-*). في الأبعاد اللانهائية لا تكون كرة الوحدة مدمجة في طوبولوجيا المعيار أبداً حسب توطئة ريس.",
      "The compactness holds in the weak-* topology, not the norm topology.",
      "المدموجية تتحقق في الطوبولوجيا الضعيفة نجمة وليس في طوبولوجيا المعيار القوي.")

    # 312: Riesz Lemma on Unit Sphere Compactness
    q("KAUST-P3-312", "Functional Analysis", "Medium",
      "Riesz's Lemma implies that the closed unit ball \\(B_X = \\{x \\in X : \\|x\\| \\le 1\\}\\) of a normed space \\(X\\) is compact in the norm topology if and only if:",
      "تقتضي توطئة ريس أن كرة الوحدة المغلقة لفضاء معياري \\(X\\) تكون مدمجة في طوبولوجيا المعيار إذا وفقط إذا كان:",
      ["\\(X\\) is finite-dimensional",
       "\\(X\\) is a Hilbert space",
       "\\(X\\) is reflexive",
       "\\(X\\) is separable"],
      0,
      "A classical theorem of F. Riesz (1918) states that a normed space \\(X\\) is finite-dimensional if and only if its closed unit ball is compact. In any infinite-dimensional space, one can construct an infinite sequence of unit vectors \\(x_n\\) with \\(\\|x_n - x_m\\| \\ge 1/2\\) for all \\(n \\neq m\\), from which no convergent subsequence can be extracted.",
      "تنص نظرية ريس الشهيرة على أن الفضاء المعياري يكون منتهي البعد إذا وفقط إذا كانت كرة الوحدة المغلقة مدمجة في طوبولوجيا المعيار. في الأبعاد اللانهائية تفقد كرة الوحدة خاصية الاندماج دائماً.",
      "Compactness of the unit ball characterizes finite-dimensional spaces.",
      "مدموجية كرة الوحدة تميز الفضاءات منتهية البعد حصراً.")

    # 313: Isoperimetric Inequality via Calculus of Variations
    q("KAUST-P3-313", "Calculus of Variations", "Medium",
      "The classical isoperimetric problem seeks the closed plane curve of fixed perimeter \\(L\\) that encloses the maximum area \\(A\\). What is the optimal geometric shape and the resulting inequality?",
      "تبحث المسألة متساوية المحيط الكلاسيكية عن المنحنى المستوي المغلق ذي المحيط الثابت \\(L\\) الذي يحصر أكبر مساحة \\(A\\). ما هو الشكل الأمثل والمتراجحة الناتجة؟",
      ["A circle; \\(4\\pi A \\le L^2\\)",
       "A square; \\(16 A \\le L^2\\)",
       "An equilateral triangle; \\(12\\sqrt{3} A \\le L^2\\)",
       "An ellipse of eccentricity \\(1/2\\); \\(2\\pi A \\le L^2\\)"],
      0,
      "Using the calculus of variations with Lagrange multipliers on the action \\(J = \\oint x dy - \\lambda \\oint \\sqrt{\\dot{x}^2 + \\dot{y}^2} dt\\), the Euler-Lagrange equations yield curves of constant curvature \\(\\kappa = 1/\\lambda\\), which are circles. The resulting isoperimetric inequality is \\(4\\pi A \\le L^2\\), with equality if and only if the boundary curve is a circle.",
      "باستخدام حساب التغاير مع مضاعفات لاغرانج نجد أن المنحنى الأمثل ذو انحناء ثابت، وهو الدائرة. المتراجحة متساوية المحيط الناتجة هي \\(4\\pi A \\le L^2\\)، وتتحقق المساواة إذا وفقط إذا كان الشكل دائرة.",
      "Recall the formula relating area \\(A = \\pi R^2\\) and circumference \\(L = 2\\pi R\\).",
      "تذكر العلاقة بين مساحة ومحيط الدائرة.")

    # 314: Geodesics on a Sphere
    q("KAUST-P3-314", "Calculus of Variations", "Medium",
      "What are the geodesics (curves of shortest distance) on the surface of a two-dimensional sphere \\(S^2\\)?",
      "ما هي الجيوديسيات (منحنيات أقصر مسافة) على سطح الكرة ثنائية البعد \\(S^2\\)؟",
      ["Great circles (intersections of the sphere with planes passing through the origin)",
       "Loxodromes (rhumb lines)",
       "Small circles (lines of constant latitude)",
       "Helices"],
      0,
      "The geodesic equation on a Riemannian manifold minimizes the arc length functional \\(L = \\int \\sqrt{g_{ij}\\dot{x}^i \\dot{x}^j} dt\\). On the sphere \\(S^2\\), the Euler-Lagrange equations require the acceleration vector in \\(\\mathbb{R}^3\\) to be normal to the surface: \\(\\ddot{\\mathbf{r}} \\parallel \\mathbf{r}\\). Thus \\(\\frac{d}{dt}(\\mathbf{r} \\times \\dot{\\mathbf{r}}) = \\mathbf{r} \\times \\ddot{\\mathbf{r}} = \\mathbf{0}\\), meaning the angular momentum vector \\(\\mathbf{r} \\times \\dot{\\mathbf{r}}\\) is constant. This confines the curve to a plane passing through the origin, which intersects the sphere in a great circle.",
      "تقلل الجيوديسيات دالية طول القوس. على سطح الكرة، يتطلب شرط أويلر-لاغرانج أن يكون متجه التسارع عمودياً على السطح، مما يقتضي أن الجداء الاتجاهي \\(\\mathbf{r} \\times \\dot{\\mathbf{r}}\\) ثابت، فيقع المنحنى في مستوى يمر بمركز الكرة، وهو ما يعرف بالدائرة العظمى.",
      "The intersection of a sphere with any plane passing through its center is a great circle.",
      "تقاطع الكرة مع أي مستوى يمر بمركزها يشكل دائرة عظمى.")

    # 315: Hilbert-Schmidt Operators
    q("KAUST-P3-315", "Spectral Theory", "Hard",
      "An operator \\(T: H \\to H\\) on a separable Hilbert space is Hilbert-Schmidt if for any orthonormal basis \\(\\{e_n\\}\\), \\(\\|T\\|_{HS}^2 = \\sum_{n=1}^\\infty \\|T e_n\\|^2 < \\infty\\). Which property is always true for every Hilbert-Schmidt operator?",
      "يكون المؤثر \\(T\\) على فضاء هيلبرت قابلاً للفصل مؤثراً من صنف هيلبرت-شميدت إذا كان مجموع مربعات معايير صور الأساس منتهياً. أي خاصية صحيحة دائماً لكل مؤثر هيلبرت-شميدت؟",
      ["\\(T\\) is a compact operator",
       "\\(T\\) is an invertible operator",
       "\\(T\\) is self-adjoint",
       "\\(T\\) is a projection operator"],
      0,
      "Every Hilbert-Schmidt operator is compact. The finite-rank approximations \\(T_N = \\sum_{n=1}^N \\langle \\cdot, e_n \\rangle T e_n\\) satisfy \\(\\|T - T_N\\|^2 \\le \\sum_{n=N+1}^\\infty \\|T e_n\\|^2 \\to 0\\) as \\(N \\to \\infty\\). Since the operator norm limit of finite-rank operators is compact, \\(T\\) is compact.",
      "كل مؤثر هيلبرت-شميدت هو مؤثر مدمج (compact). يمكن تقريبه بمؤثرات ذات رتبة منتهية تتقارب إليه في معيار المؤثرات، ونهاية مؤثرات الرتبة المنتهية هي دوماً مؤثر مدمج.",
      "Hilbert-Schmidt operators can be approximated in norm by finite-rank operators.",
      "مؤثرات هيلبرت-شميدت هي نهايات لمؤثرات ذات رتب منتهية في معيار المؤثرات.")

    # 316: Natural Boundary Conditions in Calculus of Variations
    q("KAUST-P3-316", "Calculus of Variations", "Hard",
      "When minimizing \\(J[y] = \\int_a^b L(x, y, y') dx\\) where the endpoint \\(y(b)\\) is completely free (unspecified), what natural boundary condition must hold at \\(x = b\\)?",
      "عند تصغير الدالية \\(J[y] = \\int_a^b L(x, y, y') dx\\) حيث الطرف \\(y(b)\\) حر تماماً وغير محدد، ما هو الشرط الحدي الطبيعي الذي يجب أن يتحقق عند \\(x = b\\)؟",
      ["\\(\\left.\\frac{\\partial L}{\\partial y'}\\right|_{x=b} = 0\\)",
       "\\(y(b) = 0\\)",
       "\\(\\left.\\frac{\\partial L}{\\partial y}\\right|_{x=b} = 0\\)",
       "\\(y'(b) = 0\\) always"],
      0,
      "The first variation is \\(\\delta J = \\left[\\frac{\\partial L}{\\partial y'} \\delta y\\right]_a^b + \\int_a^b \\left(\\frac{\\partial L}{\\partial y} - \\frac{d}{dx}\\frac{\\partial L}{\\partial y'}\\right)\\delta y dx\\). For the Euler-Lagrange equation to hold, the integral vanishes. At \\(x = b\\), since \\(y(b)\\) is free, \\(\\delta y(b)\\) can take any arbitrary non-zero value. To ensure \\(\\delta J = 0\\), the boundary term \\(\\frac{\\partial L}{\\partial y'}\\delta y(b)\\) must vanish, requiring \\(\\left.\\frac{\\partial L}{\\partial y'}\\right|_{x=b} = 0\\). This is the natural boundary condition.",
      "عند حساب التغاير الأول والتكامل بالتجزئة، يظهر الحد الحدودي \\([\\frac{\\partial L}{\\partial y'} \\delta y]_a^b\\). بما أن \\(y(b)\\) حر تماماً، فإن التغير \\(\\delta y(b)\\) اختياري ولا يساوي الصفر بالضرورة، مما يفرض انعدام معامله: \\(\\frac{\\partial L}{\\partial y'}\\Big|_{x=b} = 0\\).",
      "Examine the boundary term from integration by parts when \\(\\delta y(b) \\neq 0\\).",
      "انظر إلى الحد الحدودي الناتج عن التكامل بالتجزئة عند النقطة الحرة.")

    # 317: Fredholm Alternative
    q("KAUST-P3-317", "Functional Analysis", "Hard",
      "For a compact operator \\(K: H \\to H\\) on a Hilbert space and a non-zero complex scalar \\(\\lambda \\neq 0\\), the Fredholm Alternative asserts that either \\((K - \\lambda I)x = 0\\) has a non-trivial solution, OR:",
      "لمؤثر مدمج \\(K\\) على فضاء هيلبرت وعدد غير صفري \\(\\lambda\\)، تؤكد بديلة فريدهولم أنه إما أن المعادلة المتجانسة تمتلك حلاً غير صفري، أو:",
      ["For every \\(y \\in H\\), the equation \\((K - \\lambda I)x = y\\) has a unique solution",
       "\\(K = \\lambda I\\)",
       "The spectrum \\(\\sigma(K)\\) is empty",
       "\\(K\\) is the zero operator"],
      0,
      "The Fredholm Alternative states that for \\(\\lambda \\neq 0\\), the operator \\(T = K - \\lambda I\\) behaves like a finite-dimensional matrix: either \\(\\ker(K - \\lambda I) \\neq \\{0\\}\\) (so \\(\\lambda\\) is an eigenvalue), or \\(K - \\lambda I\\) is a bijection with a bounded inverse (so \\((K - \\lambda I)x = y\\) has a unique solution for all \\(y\\)). Injective implies surjective, exactly as in finite dimensions.",
      "تنص بديلة فريدهولم على أنه بالنسبة لمؤثر من الصورة \\(K - \\lambda I\\) مع \\(\\lambda \\neq 0\\): إما أن يكون للمسألة المتجانسة حل غير صفري (أي \\(\\lambda\\) قيمة ذاتية)، أو أن المؤثر تقابلي وعكوس بمقلوب محدود، تماماً كما في المصفوفات منتهية البعد.",
      "Think of the analogy with square matrices: either \\(\\det(A - \\lambda I) = 0\\) or \\((A - \\lambda I)^{-1}\\) exists.",
      "تذكر الشبه التام مع المصفوفات المربعة: إما أن يكون المحدد صفراً أو يوجد مقلوب وحيد.")

    # 318: Geodesics on a Circular Cylinder
    q("KAUST-P3-318", "Calculus of Variations", "Medium",
      "What curves form the geodesics on a right circular cylinder of radius \\(R\\) parameterized by \\((R\\cos\\theta, R\\sin\\theta, z)\\)?",
      "ما هي المنحنيات التي تشكل الجيوديسيات على أسطوانة دائرية قائمة؟",
      ["Helices (including circles and vertical straight lines as limiting cases)",
       "Only vertical lines \\(\\theta = \\text{const}\\)",
       "Only horizontal circles \\(z = \\text{const}\\)",
       "Parabolas in cylindrical coordinates"],
      0,
      "The metric on the cylinder is flat: \\(ds^2 = R^2 d\\theta^2 + dz^2\\). Unrolling the cylinder into the plane \\((\\theta, z)\\) yields a flat Euclidean strip where geodesics are straight lines: \\(z = m(R\\theta) + c\\). Rolling the strip back into 3D space wraps these straight lines into helices \\(z(\\theta) = k\\theta + c\\) (with vertical lines for \\(k = \\infty\\) and horizontal circles for \\(k = 0\\)).",
      "المقياس المتري للأسطوانة مسطح: \\(ds^2 = R^2 d\\theta^2 + dz^2\\). بفرد الأسطوانة إلى مستوى، تصبح الجيوديسيات خطوطاً مستقيمة في المستوى \\((\\theta, z)\\)، والتي تلتف مجدداً في الفضاء لتشكل خطوطاً حلزونية (helices) أو خطوطاً رأسية ودوائر أفقية.",
      "Unroll the surface of the cylinder into a flat 2D plane.",
      "افرد سطح الأسطوانة إلى مستوى ثنائي الأبعاد مسطح.")

    # 319: Reflexive Banach Spaces
    q("KAUST-P3-319", "Functional Analysis", "Medium",
      "A Banach space \\(X\\) is called reflexive if the canonical evaluation embedding \\(J: X \\to X^{**}\\) is surjective. Which of the following Banach spaces is NOT reflexive?",
      "يُسمى فضاء باناخ \\(X\\) فضاءً انعكاسياً إذا كان الغمر القانوني في الثنوي المزدوج \\(X^{**}\\) شاملاً. أي من فضاءات باناخ التالية ليس انعكاسياً؟",
      ["\\(L^1([0, 1])\\)", "\\(L^2([0, 1])\\)", "\\(L^p([0, 1])\\) for \\(1 < p < \\infty\\)", "Any finite-dimensional Banach space"],
      0,
      "For \\(1 < p < \\infty\\), \\(L^p\\) spaces are uniformly convex and reflexive by the Clarkson inequalities and Milman-Pettis theorem. Any Hilbert space (such as \\(L^2\\)) is reflexive. However, the dual of \\(L^1([0, 1])\\) is \\(L^\\infty([0, 1])\\), and the dual of \\(L^\\infty\\) is strictly larger than \\(L^1\\) (it includes finitely additive measures). Thus \\((L^1)^{**} \\neq L^1\\), so \\(L^1\\) is not reflexive.",
      "فضاءات \\(L^p\\) لـ \\(1 < p < \\infty\\) انعكاسية دوماً، وفضاء هيلبرت \\(L^2\\) انعكاسي. أما فضاء \\(L^1\\) فإن ثنويه هو \\(L^\\infty\\)، وثنوي \\(L^\\infty\\) أكبر بكثير من \\(L^1\\) (يحتوي قياسات قابلة للجمع المحدود)، لذا \\(L^1\\) ليس فضاءً انعكاسياً.",
      "The dual of \\(L^1\\) is \\(L^\\infty\\), but the dual of \\(L^\\infty\\) strictly contains \\(L^1\\).",
      "ثنوي \\(L^1\\) هو \\(L^\\infty\\)، لكن ثنوي \\(L^\\infty\\) أكبر قطعا من \\(L^1\\).")

    # 320: Rayleigh-Ritz Variational Principle for Laplacian
    q("KAUST-P3-320", "Calculus of Variations", "Hard",
      "The first Dirichlet eigenvalue \\(\\lambda_1\\) of \\(-\\Delta u = \\lambda u\\) on \\(\\Omega\\) with \\(u = 0\\) on \\(\\partial \\Omega\\) is characterized by the Rayleigh quotient as:",
      "تُوصف القيمة الذاتية الأولى لديريكليه \\(\\lambda_1\\) لمؤثر لابلاس على \\(\\Omega\\) بنسبة رايلي كـ:",
      ["\\(\\lambda_1 = \\inf_{u \\in H_0^1(\\Omega), u \\neq 0} \\frac{\\int_\\Omega |\\nabla u|^2 dx}{\\int_\\Omega u^2 dx}\\)",
       "\\(\\lambda_1 = \\sup_{u \\in H_0^1(\\Omega), u \\neq 0} \\frac{\\int_\\Omega |\\nabla u|^2 dx}{\\int_\\Omega u^2 dx}\\)",
       "\\(\\lambda_1 = \\int_\\Omega |\\nabla u|^2 dx\\)",
       "\\(\\lambda_1 = \\frac{1}{|\\Omega|}\\int_\\Omega u dx\\)"],
      0,
      "The Rayleigh-Ritz variational characterization states that the lowest eigenvalue \\(\\lambda_1\\) minimizes the Dirichlet energy \\(\\int |\\nabla u|^2 dx\\) subject to the normalization constraint \\(\\int u^2 dx = 1\\) in \\(H_0^1(\\Omega)\\). The minimizer is the ground state eigenfunction, which does not change sign in \\(\\Omega\\).",
      "ينص مبدأ رايلي-ريتز التبايني على أن أصغر قيمة ذاتية \\(\\lambda_1\\) تساوي أدنى قيمة لنسبة طاقة ديريكليه إلى معيار \\(L^2\\) على فضاء سوبوليف \\(H_0^1(\\Omega)\\). الدالة المصغرة هي الدالة الذاتية القاعية ولا تغير إشارتها داخل النطاق.",
      "Minimize the ratio of gradient energy to \\(L^2\\) norm.",
      "أوجد الحد الأدنى لنسبة طاقة التدرج إلى معيار الدالة التربيعي.")

    # 321 to 350: Continuing Part B
    # 321: Self-Adjoint Operator Eigenvalues Reality
    q("KAUST-P3-321", "Spectral Theory", "Medium",
      "Let \\(T\\) be a self-adjoint operator on a complex Hilbert space \\(H\\) (\\(T = T^*\\)). Why are all eigenvalues of \\(T\\) guaranteed to be real?",
      "ليكن \\(T\\) مؤثراً ذاتي المرافقة على فضاء هيلبرت عقدي (\\(T = T^*\\)). لماذا تضمن النظرية أن جميع قيمه الذاتية حقيقية؟",
      ["\\(\\lambda \\langle x, x \\rangle = \\langle Tx, x \\rangle = \\langle x, Tx \\rangle = \\bar{\\lambda} \\langle x, x \\rangle \\implies (\\lambda - \\bar{\\lambda})\\|x\\|^2 = 0\\)",
       "Because the trace of \\(T\\) is always an integer",
       "Because \\(T\\) must commute with the identity",
       "Because \\(\\|T\\| = 1\\)"],
      0,
      "Let \\(Tx = \\lambda x\\) with \\(x \\neq 0\\). Then \\(\\langle Tx, x \\rangle = \\langle \\lambda x, x \\rangle = \\lambda \\|x\\|^2\\). By self-adjointness, \\(\\langle Tx, x \\rangle = \\langle x, T^* x \\rangle = \\langle x, Tx \\rangle = \\langle x, \\lambda x \\rangle = \\bar{\\lambda} \\|x\\|^2\\). Equating the two gives \\(\\lambda \\|x\\|^2 = \\bar{\\lambda} \\|x\\|^2 \\implies (\\lambda - \\bar{\\lambda})\\|x\\|^2 = 0\\). Since \\(x \\neq 0 \\implies \\|x\\| > 0\\), we must have \\(\\lambda = \\bar{\\lambda}\\), proving \\(\\lambda \\in \\mathbb{R}\\).",
      "بحساب الجداء الداخلي \\(\\langle Tx, x \\rangle\\) بطريقتين: الأولى تعطي \\(\\lambda \\|x\\|^2\\) والثانية باستغلال المرافقة الذاتية تعطي \\(\\bar{\\lambda} \\|x\\|^2\\). بمساواتهما وبما أن \\(\\|x\\| \\neq 0\\)، ينتج \\(\\lambda = \\bar{\\lambda}\\)، أي أن القيمة الذاتية حقيقية تماماً.",
      "Compare \\(\\langle Tx, x \\rangle\\) with \\(\\langle x, Tx \\rangle\\).",
      "قارن بين الجداءين الداخليين باستخدام شرط المرافقة الذاتية.")

    # 322: Orthogonality of Eigenvectors for Distinct Eigenvalues
    q("KAUST-P3-322", "Spectral Theory", "Medium",
      "If \\(T = T^*\\) is a self-adjoint operator on \\(H\\) and \\(x, y\\) are eigenvectors corresponding to distinct eigenvalues \\(\\lambda_1 \\neq \\lambda_2\\), then:",
      "إذا كان \\(T = T^*\\) مؤثراً ذاتي المرافقة وكان \\(x, y\\) متجهين ذاتيين لقيمتين ذاتيتين مختلفتين \\(\\lambda_1 \\neq \\lambda_2\\)، فإن:",
      ["\\(\\langle x, y \\rangle = 0\\) (they are orthogonal)",
       "\\(\\langle x, y \\rangle = 1\\)",
       "\\(x\\) and \\(y\\) are linearly dependent",
       "\\(\\|x\\| = \\|y\\|\\)"],
      0,
      "Compute \\(\\lambda_1 \\langle x, y \\rangle = \\langle \\lambda_1 x, y \\rangle = \\langle Tx, y \\rangle = \\langle x, Ty \\rangle = \\langle x, \\lambda_2 y \\rangle = \\bar{\\lambda}_2 \\langle x, y \\rangle = \\lambda_2 \\langle x, y \\rangle\\) (since \\(\\lambda_2\\) is real). Thus \\((\\lambda_1 - \\lambda_2)\\langle x, y \\rangle = 0\\). Since \\(\\lambda_1 \\neq \\lambda_2\\), we must have \\(\\langle x, y \\rangle = 0\\).",
      "نحسب \\(\\lambda_1 \\langle x, y \\rangle = \\langle Tx, y \\rangle = \\langle x, Ty \\rangle = \\lambda_2 \\langle x, y \\rangle\\). بنقل الحدود: \\((\\lambda_1 - \\lambda_2)\\langle x, y \\rangle = 0\\). وبما أن القيمتين الذاتيتين متمايزتان، فإن المتجهين متعامدان بالضرورة.",
      "Evaluate \\(\\langle Tx, y \\rangle\\) in two different ways.",
      "احسب الجداء الداخلي بطريقتين مختلفتين.")

    # 323: Continuous Spectrum vs Point Spectrum
    q("KAUST-P3-323", "Spectral Theory", "Hard",
      "Consider the position operator \\((T f)(x) = x f(x)\\) on \\(L^2([0, 1])\\). What is its point spectrum (set of eigenvalues) and its full spectrum \\(\\sigma(T)\\)?",
      "تأمل مؤثر الموضع \\((Tf)(x) = x f(x)\\) على الفضاء \\(L^2([0, 1])\\). ما هو طيفه النقطي (مجموعة القيم الذاتية) وما هو طيفه الكامل \\(\\sigma(T)\\)؟",
      ["Point spectrum is empty (no eigenvalues); \\(\\sigma(T) = [0, 1]\\) (purely continuous spectrum)",
       "Point spectrum is \\([0, 1]\\); \\(\\sigma(T) = [0, 1]\\)",
       "Point spectrum is \\(\\{0, 1\\}\\); \\(\\sigma(T) = \\{0, 1\\}\\)",
       "\\(\\sigma(T) = \\mathbb{R}\\)"],
      0,
      "If \\(T f = \\lambda f\\), then \\((x - \\lambda) f(x) = 0\\) almost everywhere. This requires \\(f(x) = 0\\) for all \\(x \\neq \\lambda\\). In \\(L^2([0, 1])\\), a function non-zero only at a single point has norm zero, so \\(f = 0\\) in \\(L^2\\). Thus there are no non-trivial eigenvectors, meaning the point spectrum is empty: \\(\\sigma_p(T) = \\emptyset\\). However, for any \\(\\lambda \\in [0, 1]\\), the operator \\((T - \\lambda I)\\) is not invertible with bounded inverse (since \\(1/(x-\\lambda) \\notin L^\\infty\\)). Thus the spectrum is purely continuous: \\(\\sigma(T) = [0, 1]\\).",
      "المعادلة \\((x-\\lambda)f(x) = 0\\) تقتضي أن \\(f(x) = 0\\) في كل مكان ما عدا نقطة واحدة ذات قياس صفر، وبالتالي \\(f = 0\\) في \\(L^2\\)، فلا توجد قيم ذاتية (الطيف النقطي خالٍ). لكن لـ \\(\\lambda \\in [0, 1]\\)، لا يمتلك المؤثر مقلوباً محدوداً. بالتالي فإن الطيف متصل بالكامل: \\(\\sigma(T) = [0, 1]\\).",
      "Can a non-zero \\(L^2\\) function be supported at a single point?",
      "هل يمكن لدالة غير صفرية في \\(L^2\\) أن يكون حاملها نقطة واحدة؟")

    # 324: Shift Operator on l2
    q("KAUST-P3-324", "Spectral Theory", "Hard",
      "Let \\(S: \\ell^2 \\to \\ell^2\\) be the right shift operator \\(S(x_1, x_2, x_3, \\dots) = (0, x_1, x_2, \\dots)\\). What is its adjoint \\(S^*\\), and is \\(S\\) normal?",
      "ليكن \\(S: \\ell^2 \\to \\ell^2\\) مؤثر الإزاحة إلى اليمين \\(S(x_1, x_2, \\dots) = (0, x_1, x_2, \\dots)\\). ما هو مرافقه \\(S^*\\)، وهل \\(S\\) مؤثر ناظمي؟",
      ["\\(S^*(x_1, x_2, x_3, \\dots) = (x_2, x_3, \\dots)\\) (left shift); \\(S\\) is not normal",
       "\\(S^* = S\\); \\(S\\) is self-adjoint and normal",
       "\\(S^*(x_1, x_2, \\dots) = (x_1, 0, x_2, \\dots)\\); \\(S\\) is normal",
       "\\(S^* = -S\\); \\(S\\) is skew-adjoint"],
      0,
      "Compute \\(\\langle S x, y \\rangle = \\sum_{n=1}^\\infty (Sx)_n \\bar{y}_n = 0 \\bar{y}_1 + x_1 \\bar{y}_2 + x_2 \\bar{y}_3 + \\dots = \\sum_{k=1}^\\infty x_k \\bar{y}_{k+1} = \\langle x, S^* y \\rangle\\). Thus \\(S^*(y_1, y_2, y_3, \\dots) = (y_2, y_3, y_4, \\dots)\\), the left shift. To check normality: \\(S^* S (x_1, x_2, \\dots) = S^*(0, x_1, x_2, \\dots) = (x_1, x_2, \\dots) = I\\). But \\(S S^* (x_1, x_2, \\dots) = S(x_2, x_3, \\dots) = (0, x_2, x_3, \\dots) \\neq I\\). Since \\(S^* S \\neq S S^*\\), \\(S\\) is an isometry that is NOT unitary, and NOT normal.",
      "بحساب الجداء الداخلي نجد أن المرافق هو مؤثر الإزاحة إلى اليسار \\(S^*(y) = (y_2, y_3, \\dots)\\). نلاحظ أن \\(S^* S = I\\) بينما \\(S S^*(x) = (0, x_2, x_3, \\dots) \\neq I\\). بما أن \\(S^* S \\neq S S^*\\)، فالمؤثر ليس ناظمياً.",
      "Compute \\(S^* S\\) and \\(S S^*\\) and compare them.",
      "احسب كلا من \\(S^* S\\) و \\(S S^*\\) وقارن بينهما.")

    # 325: Geodesics on a Cone
    q("KAUST-P3-325", "Calculus of Variations", "Hard",
      "A geodesic on a right circular cone that does not pass through the apex intersects any generator (meridian) at most how many times?",
      "الجيوديسي على مخروط دائري قائم والذي لا يمر برأس المخروط يقطع أي مولد (خط طول) كم مرة على الأكثر؟",
      ["At most once (or at most finitely many times determined by the cone opening angle \\(\\alpha\\))",
       "Infinitely many times (it spirals endlessly)",
       "Always exactly twice",
       "Zero times"],
      0,
      "When a cone of semi-vertical angle \\(\\alpha\\) is cut along a generator and unrolled into the plane, it forms a planar circular sector of angle \\(\\beta = 2\\pi \\sin\\alpha < 2\\pi\\). Geodesics on the cone correspond to straight lines on this unrolled planar sector. A straight line in the plane can intersect any ray from the origin at most once. Therefore, when mapped back to the cone, the geodesic intersects any given generator at most once (or a finite number of times if the unrolled sector wraps around).",
      "عند قطع المخروط على طول أحد المولدات وفرده على مستوى، يتحول إلى قطاع دائري مسطح بزاوية \\(2\\pi \\sin\\alpha\\). الجيوديسيات تتحول إلى خطوط مستقيمة في المستوى. المستقيم في المستوى يقطع أي شعاع صادر من الأصل مرة واحدة على الأكثر. بالتالي، يقطع الجيوديسي أي مولد مرة واحدة على الأكثر.",
      "Unroll the cone into a flat circular sector in the plane.",
      "افرد المخروط إلى قطاع دائري مستوٍ.")

    # 326: Dual of Lp Space
    q("KAUST-P3-326", "Functional Analysis", "Medium",
      "For \\(1 < p < \\infty\\) with conjugate exponent \\(q\\) satisfying \\(\\frac{1}{p} + \\frac{1}{q} = 1\\), the Riesz representation theorem for \\(L^p(\\Omega)\\) establishes an isometric isomorphism between \\((L^p(\\Omega))^*\\) and:",
      "لكل \\(1 < p < \\infty\\) مع الأس المقترن \\(q\\) حيث \\(1/p + 1/q = 1\\)، تثبت نظرية ريس للتمثيل وجود تماكل متساوي القياس بين الفضاء الثنوي \\((L^p)^*\\) وفضاء:",
      ["\\(L^q(\\Omega)\\)", "\\(L^p(\\Omega)\\)", "\\(L^1(\\Omega)\\)", "\\(L^\\infty(\\Omega)\\)"],
      0,
      "The Riesz representation theorem for \\(L^p\\) spaces states that every continuous linear functional \\(\\Phi \\in (L^p)^*\\) can be uniquely represented as \\(\\Phi(f) = \\int_\\Omega f(x) g(x) dx\\) for a unique \\(g \\in L^q\\), with \\(\\|\\Phi\\|_{(L^p)^*} = \\|g\\|_{L^q}\\). Thus \\((L^p)^* \\cong L^q\\).",
      "تنص نظرية ريس لتمثيل فضاءات \\(L^p\\) على أن كل تابع خطي مستمر يُمثل بدالة وحيدة \\(g \\in L^q\\) بالتكامل \\(\\int fg dx\\)، وتتطابق المعايير تماماً، مما يثبت التماكل \\((L^p)^* \\cong L^q\\).",
      "Use Hölder's inequality conjugate exponents \\(1/p + 1/q = 1\\).",
      "استخدم الأسس المقترنة لمتراجحة هولدر.")

    # 327: Second Variation and Legendre Condition
    q("KAUST-P3-327", "Calculus of Variations", "Hard",
      "In the calculus of variations, a necessary condition for a stationary path \\(y(x)\\) of \\(J[y] = \\int L(x, y, y') dx\\) to be a local MINIMUM is the Legendre condition, which requires:",
      "في حساب التغاير، الشرط اللازم لكي يكون المسار المستقر نهاية صغرى محلية للدالية هو شرط ليجاندر، والذي يتطلب:",
      ["\\(\\frac{\\partial^2 L}{\\partial (y')^2} \\ge 0\\) along the path",
       "\\(\\frac{\\partial^2 L}{\\partial y^2} \\le 0\\)",
       "\\(\\frac{\\partial^2 L}{\\partial y \\partial y'} = 0\\)",
       "\\(\\frac{\\partial L}{\\partial y'} > 0\\)"],
      0,
      "The second variation is \\(\\delta^2 J[h] = \\int_{x_1}^{x_2} (P (h')^2 + Q h^2) dx\\) where \\(P(x) = \\frac{\\partial^2 L}{\\partial (y')^2}\\). By choosing high-frequency localized variations \\(h(x)\\) where \\(h'\\) dominates \\(h\\), the sign of \\(\\delta^2 J\\) is dictated entirely by \\(P(x)\\). For \\(\\delta^2 J \\ge 0\\) (a local minimum), we must have \\(P(x) = \\frac{\\partial^2 L}{\\partial (y')^2} \\ge 0\\) at every point along the extremal path. This is Legendre's necessary condition.",
      "التغاير الثاني يعطى بـ \\(\\int (P (h')^2 + Q h^2) dx\\) حيث \\(P = \\frac{\\partial^2 L}{\\partial (y')^2}\\). باختيار اضطرابات سريعة التذبذب، يهيمن المشتق \\(h'\\)، ولكي يكون التغاير الثاني غير سالب (نهاية صغرى)، يجب أن يتحقق شرط ليجاندر \\(P \\ge 0\\) على طول المسار.",
      "Examine the coefficient of \\((h')^2\\) in the second variation.",
      "انظر إلى معامل \\((h')^2\\) في صيغة التغاير الثاني.")

    # 328: Weierstraß-Erdmann Corner Conditions
    q("KAUST-P3-328", "Calculus of Variations", "Hard",
      "For a broken extremal with a corner (discontinuous slope \\(y'\\)) at point \\(c\\), the Weierstrass-Erdmann corner conditions require which quantities to be continuous across \\(c\\)?",
      "لمسار متطرف منكسر بزاوية (مشتق \\(y'\\) غير متصل) عند النقطة \\(c\\)، تتطلب شروط فايرشتراس-إردمان للزاوية أن تكون أي كميات متصلة عبر \\(c\\)؟",
      ["\\(\\frac{\\partial L}{\\partial y'}\\) and \\(L - y'\\frac{\\partial L}{\\partial y'}\\)",
       "\\(y'\\) and \\(y''\\)",
       "\\(\\frac{\\partial L}{\\partial y}\\) and \\(L\\)",
       "Only \\(y(x)\\) itself"],
      0,
      "The Weierstrass-Erdmann conditions state that at any corner of an extremal curve: 1) \\(\\left(\\frac{\\partial L}{\\partial y'}\\right)^- = \\left(\\frac{\\partial L}{\\partial y'}\\right)^+\\) (continuity of generalized momentum), and 2) \\(\\left(L - y'\\frac{\\partial L}{\\partial y'}\\right)^- = \\left(L - y'\\frac{\\partial L}{\\partial y'}\\right)^+\\) (continuity of the Hamiltonian/energy). These ensure that the boundary variations vanish when splitting the integral at the corner.",
      "تنص شروط فايرشتراس-إردمان على أنه عند أي زاوية انكسار، يجب أن يستمر كمية الحركة المعممة \\(\\partial L / \\partial y'\\) وهاملتونيان النظام \\(L - y' \\partial L / \\partial y'\\) عبر نقطة الانكسار دون قفزة.",
      "The generalized momentum and the Hamiltonian must remain continuous across corners.",
      "يجب أن تظل كمية الحركة المعممة وهاملتونيان النظام متصلين عبر نقطة الانكسار.")

    # 329: Orthogonal Decomposition Theorem
    q("KAUST-P3-329", "Functional Analysis", "Medium",
      "The Projection Theorem for Hilbert spaces asserts that if \\(M\\) is a CLOSED subspace of a Hilbert space \\(H\\), then \\(H\\) decomposes as the direct sum:",
      "تنص نظرية الإسقاط لفضاءات هيلبرت على أنه إذا كان \\(M\\) فضاءً جزئياً مغلقاً في \\(H\\)، فإن \\(H\\) يتحلل إلى المجموع المباشر:",
      ["\\(H = M \\oplus M^\\perp\\)",
       "\\(H = M \\cup M^\\perp\\)",
       "\\(H = M \\otimes M^\\perp\\)",
       "\\(H = M + H^*\\)"],
      0,
      "The Projection Theorem (Orthogonal Decomposition Theorem) states that for every closed subspace \\(M \\subset H\\), every element \\(x \\in H\\) can be uniquely written as \\(x = y + z\\) where \\(y \\in M\\) and \\(z \\in M^\\perp\\), with \\(y\\) being the unique closest point in \\(M\\) to \\(x\\). Thus \\(H = M \\oplus M^\\perp\\). The condition that \\(M\\) is closed is essential.",
      "تنص مبرهنة الإسقاط المتعامد على أنه لأي فضاء جزئي مغلق \\(M\\)، يُكتب أي متجه بشكل وحيد كـ \\(x = y + z\\) حيث \\(y \\in M\\) و \\(z \\in M^\\perp\\)، وبالتالي \\(H = M \\oplus M^\\perp\\). ويشترط أن يكون \\(M\\) مغلقاً.",
      "Every vector uniquely splits into a component in \\(M\\) and an orthogonal component.",
      "يتحلل كل متجه بشكل وحيد إلى مركبة في \\(M\\) ومركبة متعامدة مع \\(M\\).")

    # 330: Gram-Schmidt Process and Orthogonal Polynomials
    q("KAUST-P3-330", "Functional Analysis", "Medium",
      "Applying the Gram-Schmidt orthonormalization process to the monomial sequence \\(\\{1, x, x^2, x^3, \\dots\\}\\) in the Hilbert space \\(L^2([-1, 1])\\) with standard inner product \\(\\langle f, g \\rangle = \\int_{-1}^1 f(x) g(x) dx\\) produces which family of orthogonal polynomials?",
      "تطبيق عملية غرام-شميدت على متتالية وحيدات الحد \\(\\{1, x, x^2, \\dots\\}\\) في الفضاء \\(L^2([-1, 1])\\) بالجداء الداخلي المعتاد ينتج أي عائلة من كثيرات الحدود المتعامدة؟",
      ["Legendre polynomials", "Chebyshev polynomials", "Hermite polynomials", "Laguerre polynomials"],
      0,
      "Orthonormalizing \\(\\{1, x, x^2, \\dots\\}\\) on the interval \\([-1, 1]\\) with constant weight function \\(w(x) = 1\\) yields the Legendre polynomials \\(P_n(x)\\). (If the weight were \\(1/\\sqrt{1-x^2}\\), it would produce Chebyshev polynomials; if on \\(\\mathbb{R}\\) with weight \\(e^{-x^2}\\), Hermite polynomials; if on \\([0, \\infty)\\) with \\(e^{-x}\\), Laguerre polynomials).",
      "ينتج عن تعامد وحيدات الحد على \\([-1, 1]\\) مع دالة الوزن الثابتة \\(w(x) = 1\\) كثيرات حدود ليجاندر القياسية. بينما ينتج عن الوزن \\(1/\\sqrt{1-x^2}\\) كثيرات حدود تشيبيشيف، وعن الوزن الغاوسي كثيرات حدود هيرميت.",
      "The weight function on \\([-1, 1]\\) is the constant function 1.",
      "دالة الوزن على المجال \\([-1, 1]\\) هي الدالة الثابتة 1.")

    # 331 to 350: Continuing Part B
    # 331: Extremals of Dirichlet Integral in 1D
    q("KAUST-P3-331", "Calculus of Variations", "Medium",
      "Find the extremals of the functional \\(J[y] = \\int_0^1 (y')^2 dx\\) subject to boundary conditions \\(y(0) = 2\\) and \\(y(1) = 6\\).",
      "أوجد المسار الحرج للدالية \\(J[y] = \\int_0^1 (y')^2 dx\\) مع الشروط الطرفية \\(y(0) = 2\\) و \\(y(1) = 6\\).",
      ["\\(y(x) = 4x + 2\\)", "\\(y(x) = 4x^2 + 2\\)", "\\(y(x) = 2e^{\\ln(3) x}\\)", "\\(y(x) = 6 - 4(1-x)^2\\)"],
      0,
      "The Lagrangian is \\(L(x, y, y') = (y')^2\\). The Euler-Lagrange equation is \\(\\frac{\\partial L}{\\partial y} - \\frac{d}{dx}\\frac{\\partial L}{\\partial y'} = 0 - \\frac{d}{dx}(2y') = -2y'' = 0 \\implies y''(x) = 0\\). The general solution is a straight line \\(y(x) = Ax + B\\). Using the boundary conditions: \\(y(0) = B = 2\\), and \\(y(1) = A + 2 = 6 \\implies A = 4\\). Thus \\(y(x) = 4x + 2\\).",
      "اللاغرانجي هو \\(L = (y')^2\\). معادلة أويلر-لاغرانج تعطي \\(y'' = 0\\)، والحل العام هو خط مستقيم \\(y = Ax + B\\). من الشروط الحدية نجد \\(B = 2\\) و \\(A = 4\\)، فالمنحنى هو \\(y(x) = 4x + 2\\).",
      "The Euler-Lagrange equation for \\(L = (y')^2\\) is simply \\(y'' = 0\\).",
      "معادلة أويلر-لاغرانج لـ \\((y')^2\\) هي ببساطة \\(y'' = 0\\).")

    # 332: Bessel's Inequality in Hilbert Space
    q("KAUST-P3-332", "Functional Analysis", "Medium",
      "Let \\(\\{e_n\\}_{n=1}^\\infty\\) be an orthonormal sequence in a Hilbert space \\(H\\). Bessel's inequality states that for any \\(x \\in H\\):",
      "لتكن \\(\\{e_n\\}\\) متتالية متعامدة عيارياً في فضاء هيلبرت \\(H\\). تنص متراجحة بيسل على أنه لأي \\(x \\in H\\):",
      ["\\(\\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|^2 \\le \\|x\\|^2\\)",
       "\\(\\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|^2 \\ge \\|x\\|^2\\)",
       "\\(\\sum_{n=1}^\\infty |\\langle x, e_n \\rangle| \\le \\|x\\|\\)",
       "\\(\\sum_{n=1}^\\infty \\langle x, e_n \\rangle = \\|x\\|\\)"],
      0,
      "Consider the projection \\(x_N = \\sum_{n=1}^N \\langle x, e_n \\rangle e_n\\). Then \\(\\|x - x_N\\|^2 = \\|x\\|^2 - \\sum_{n=1}^N |\\langle x, e_n \\rangle|^2 \\ge 0\\). Thus \\(\\sum_{n=1}^N |\\langle x, e_n \\rangle|^2 \\le \\|x\\|^2\\) for all \\(N\\). Taking \\(N \\to \\infty\\) gives Bessel's inequality \\(\\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|^2 \\le \\|x\\|^2\\). Equality holds (Parseval's identity) if and only if the sequence \\(\\{e_n\\}\\) is complete (an orthonormal basis).",
      "بحساب معيار الفرق بين المتجه وإسقاطه على الفضاء المولد بأول \\(N\\) متجهات: \\(\\|x - x_N\\|^2 = \\|x\\|^2 - \\sum |\\langle x, e_n \\rangle|^2 \\ge 0\\). بجعل \\(N \\to \\infty\\) نحصل على متراجحة بيسل، وتتحقق المساواة (متطابقة بارسيفال) إذا وفقط إذا كان الأساس تاماً.",
      "The length of the projection onto a subspace cannot exceed the length of the vector.",
      "طول مسقط متجه على فضاء جزئي لا يمكن أن يتجاوز طول المتجه الأصلي.")

    # 333: Parseval's Identity
    q("KAUST-P3-333", "Functional Analysis", "Medium",
      "If \\(\\{e_n\\}\\) is an orthonormal BASIS for a Hilbert space \\(H\\), Parseval's identity states that for any \\(x \\in H\\):",
      "إذا كانت \\(\\{e_n\\}\\) أساساً متعامداً عيارياً لفضاء هيلبرت \\(H\\)، تنص متطابقة بارسيفال على أنه لأي \\(x \\in H\\):",
      ["\\(\\|x\\|^2 = \\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|^2\\)",
       "\\(\\|x\\| = \\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|\\)",
       "\\(\\|x\\|^2 = \\sum_{n=1}^\\infty \\langle x, e_n \\rangle\\)",
       "\\(\\langle x, x \\rangle = \\max_n |\\langle x, e_n \\rangle|^2\\)"],
      0,
      "Parseval's identity is the infinite-dimensional generalization of the Pythagorean theorem: when \\(\\{e_n\\}\\) is a complete orthonormal basis, no component of \\(x\\) is missed, so the square of the norm of \\(x\\) equals exactly the sum of the squares of its Fourier coefficients: \\(\\|x\\|^2 = \\sum_{n=1}^\\infty |\\langle x, e_n \\rangle|^2\\).",
      "متطابقة بارسيفال هي تعميم مبرهنة فيثاغورس للأبعاد اللانهائية: عندما يكون الأساس المتعامد تاماً، فإن مربع معيار أي متجه يساوي تماماً مجموع مربعات معاملات فورييه الخاصة به.",
      "This is the Pythagorean theorem for Fourier series.",
      "هذه هي مبرهنة فيثاغورس لمتسلسلات فورييه.")

    # 334: Unitary Operator Definition and Properties
    q("KAUST-P3-334", "Spectral Theory", "Medium",
      "An operator \\(U: H \\to H\\) on a complex Hilbert space is unitary if and only if:",
      "يكون المؤثر \\(U: H \\to H\\) على فضاء هيلبرت مؤثراً وحدوياً (unitary) إذا وفقط إذا كان:",
      ["\\(U^* U = U U^* = I\\) (it is a surjective isometry)",
       "\\(U^* = U\\)",
       "\\(U^2 = I\\)",
       "\\(\\|U\\| = 1\\)"],
      0,
      "A linear operator \\(U\\) is unitary if it preserves the inner product (\\(\\langle U x, U y \\rangle = \\langle x, y \\rangle\\) for all \\(x, y\\)) and is surjective. Equivalently, its adjoint is its inverse: \\(U^* = U^{-1}\\), meaning \\(U^* U = U U^* = I\\). The spectrum of any unitary operator is confined strictly to the unit circle in \\(\\mathbb{C}\\): \\(\\sigma(U) \\subseteq \\{z \\in \\mathbb{C} : |z| = 1\\}\\).",
      "المؤثر الوحدوي هو تشاكل متساوي القياس وشامل يحافظ على الجداء الداخلي، ومرافقه هو معكوسه تماماً: \\(U^* U = U U^* = I\\). وطيف أي مؤثر وحدوي يقع بالكامل على دائرة الوحدة في المستوى العقدي.",
      "Recall that \\(U^* = U^{-1}\\).",
      "تذكر أن مرافق المؤثر الوحدوي هو مقلوبه.")

    # 335: Spectral Theorem for Bounded Self-Adjoint Operators
    q("KAUST-P3-335", "Spectral Theory", "Hard",
      "The Spectral Theorem for a bounded self-adjoint operator \\(T\\) on a Hilbert space represents \\(T\\) as an integral with respect to a projection-valued measure \\(E\\):",
      "تمثل النظرية الطيفية لمؤثر ذاتي المرافقة ومحدود \\(T\\) على فضاء هيلبرت المؤثر كتكامل بالنسبة لقياس قيمي إسقاطي \\(E\\):",
      ["\\(T = \\int_{\\sigma(T)} \\lambda dE(\\lambda)\\)",
       "\\(T = \\sum_{n=1}^\\infty \\lambda_n E_n\\) for any bounded self-adjoint operator",
       "\\(T = e^{\\int dE}\\)",
       "\\(T = \\int_{\\sigma(T)} E(\\lambda) d\\lambda\\)"],
      0,
      "The continuous spectral theorem represents any bounded self-adjoint operator as \\(T = \\int_{\\sigma(T)} \\lambda dE(\\lambda)\\), where \\(E\\) is a resolution of the identity (projection-valued measure) supported on the real spectrum \\(\\sigma(T) \\subset \\mathbb{R}\\). This generalizes diagonalizing a Hermitian matrix to infinite-dimensional operators that may have continuous spectrum.",
      "تعمم النظرية الطيفية تقطير المصفوفات الهرميتية إلى الأبعاد اللانهائية: أي مؤثر ذاتي المرافقة يُمثَّل بتكامل \\(T = \\int_{\\sigma(T)} \\lambda dE(\\lambda)\\) بالنسبة لقياس ذي قيم إسقاطية على الطيف الحقيقي.",
      "The spectral theorem generalizes matrix diagonalization \\(A = \\sum \\lambda_i P_i\\) into an integral.",
      "تعمم النظرية الطيفية مجموع التقطير إلى تكامل طيفي مستمر.")

    # 336: Sturm-Liouville Operator Self-Adjointness
    q("KAUST-P3-336", "Spectral Theory", "Hard",
      "The regular Sturm-Liouville differential operator \\(L u = -\\frac{d}{dx}\\left(p(x) \\frac{du}{dx}\\right) + q(x) u\\) on \\([a, b]\\) with \\(p(x) > 0\\) is self-adjoint in \\(L^2([a, b])\\) under which boundary conditions?",
      "يكون مؤثر شتورم-ليوفيل التفاضلي \\(Lu = -(p u')' + qu\\) مع \\(p > 0\\) ذاتي المرافقة في \\(L^2([a, b])\\) تحت أي شروط حدية؟",
      ["Separated boundary conditions: \\(\\alpha_1 u(a) + \\alpha_2 u'(a) = 0\\) and \\(\\beta_1 u(b) + \\beta_2 u'(b) = 0\\)",
       "Arbitrary boundary conditions without restrictions",
       "Only \\(u(a) = u(b) = 1\\)",
       "Only if \\(p(x)\\) is constant"],
      0,
      "Using Lagrange's identity (integration by parts twice): \\(\\int_a^b (u L v - v L u) dx = [p(x)(u' v - u v')]_a^b\\). For \\(L\\) to be self-adjoint, the boundary terms must vanish identically: \\([p(x)(u' v - u v')]_a^b = 0\\). This occurs when the boundary conditions are separated (Robin/Dirichlet/Neumann) at each endpoint, or periodic with \\(p(a) = p(b)\\).",
      "بالمكاملة مرتين بالتجزئة تظهر حدود لاغرانج الطرفية \\([p(x)(u'v - uv')]_a^b\\). لكي يكون المؤثر ذاتي المرافقة، يجب أن تنعدم هذه الحدود، وهو ما يتحقق بالشروط الحدية المنفصلة (ديريكليه أو نيومان أو روبين) عند كل طرف.",
      "Check the condition for the boundary terms in Lagrange's identity to vanish.",
      "تحقق من شرط انعدام الحدود الطرفية في متطابقة لاغرانج.")

    # 337: Brachistochrone Acceleration Profile
    q("KAUST-P3-337", "Calculus of Variations", "Medium",
      "In the Brachistochrone problem, why is the optimal curve faster than a straight line even though the straight line has a shorter path length?",
      "في مسألة البركستوكرون، لماذا يكون المنحنى الأمثل أسرع من الخط المستقيم رغم أن الخط المستقيم يمتلك طول مسار أقصر؟",
      ["The cycloid drops steeply at the beginning, converting potential energy into kinetic energy early to maintain a higher average speed throughout the journey",
       "The cycloid has zero friction while the straight line has friction",
       "Gravity acts stronger on curved paths",
       "The arc length of the cycloid is actually shorter than the straight line"],
      0,
      "Travel time is the integral of \\(ds / v\\). The cycloid takes advantage of gravity by dipping steeply at the start, acquiring large velocity \\(v = \\sqrt{2gy}\\) early on. Although the total path length is longer, the substantial increase in velocity across the entire remainder of the path more than compensates, minimizing the total time \\(T\\).",
      "زمن السفر هو تكامل \\(ds/v\\). ينحدر منحنى الدويرية بشكل حاد في البداية ليكتسب الجسيم سرعة عالية مبكراً \\(v = \\sqrt{2gy}\\)، وبالتالي يقطع معظم المسار بسرعة متوسطة أعلى بكثير مما يعوض زيادة طول المسار ويقلل الزمن الكلي.",
      "Early steep descent yields high velocity for the rest of the transit.",
      "الهبوط الحاد في البداية يمنح سرعة عالية لما تبقى من المسار.")

    # 338: Dual of c0 is l1
    q("KAUST-P3-338", "Functional Analysis", "Hard",
      "Let \\(c_0\\) be the Banach space of all real sequences converging to 0, equipped with the supremum norm \\(\\|x\\|_\\infty = \\sup_n |x_n|\\). What is the dual space \\((c_0)^*\\)?",
      "ليكن \\(c_0\\) فضاء باناخ للمتتاليات التي تؤول للصفر بمعيار النهاية العظمى. ما هو الفضاء الثنوي \\((c_0)^*\\)؟",
      ["\\(\\ell^1\\) with the norm \\(\\|y\\|_1 = \\sum_{n=1}^\\infty |y_n|\\)",
       "\\(\\ell^\\infty\\)",
       "\\(c_0\\) itself (it is self-dual)",
       "\\(\\ell^2\\)"],
      0,
      "Every bounded linear functional on \\(c_0\\) is represented by a sequence \\(y \\in \\ell^1\\) via \\(f(x) = \\sum_{n=1}^\\infty x_n y_n\\), and the operator norm satisfies \\(\\|f\\| = \\sum |y_n| = \\|y\\|_1\\). Thus \\((c_0)^* \\cong \\ell^1\\). Conversely, the dual of \\(\\ell^1\\) is \\(\\ell^\\infty\\), showing that \\((c_0)^{**} \\cong \\ell^\\infty \\neq c_0\\), which also proves that \\(c_0\\) is not reflexive.",
      "كل تابع خطي محدود على \\(c_0\\) يُمثل بمتتالية في \\(\\ell^1\\) عبر المجموع \\(\\sum x_n y_n\\) مع تطابق المعيار المؤثري مع معيار \\(\\ell^1\\). إذن \\((c_0)^* \\cong \\ell^1\\).",
      "Evaluate the action of a functional on standard unit basis vectors \\(e_n\\).",
      "احسب تأثير التابع الخطي على متجهات الأساس القياسية.")

    # 339: Minimal Surface Equation
    q("KAUST-P3-339", "Calculus of Variations", "Hard",
      "The minimal surface equation for a nonparametric surface \\(z = u(x, y)\\) minimizing area \\(A = \\iint \\sqrt{1 + u_x^2 + u_y^2} dx dy\\) expresses which geometric property?",
      "تعبر معادلة السطوح الصغرى لسطح \\(z = u(x, y)\\) يصغر المساحة عن أي خاصية هندسية؟",
      ["The mean curvature \\(H\\) is zero everywhere (\\(H = 0\\))",
       "The Gaussian curvature \\(K\\) is zero everywhere (\\(K = 0\\))",
       "The surface is a sphere",
       "The gradient \\(\\nabla u\\) is constant"],
      0,
      "Minimizing the surface area functional yields the Euler-Lagrange equation \\(\\nabla \\cdot \\left(\\frac{\\nabla u}{\\sqrt{1 + |\\nabla u|^2}}\\right) = 0 \\implies (1 + u_y^2)u_{xx} - 2u_x u_y u_{xy} + (1 + u_x^2)u_{yy} = 0\\). In differential geometry, the mean curvature of the surface \\(z = u(x, y)\\) is given by \\(H = \\frac{1}{2}\\nabla \\cdot \\left(\\frac{\\nabla u}{\\sqrt{1 + |\\nabla u|^2}}\\right)\\). Therefore, minimal surfaces are precisely surfaces of zero mean curvature \\(H = 0\\) everywhere.",
      "ينتج عن تصغير مساحة السطح معادلة أويلر-لاغرانج التي تكافئ انعدام تباعد متجه الناظم الواحدي. وفي الهندسة التفاضلية، هذا المقدار يساوي تماماً ضعف الانحناء المتوسط \\(H\\). وبالتالي فإن السطوح الصغرى هي السطوح ذات الانحناء المتوسط المنعدم \\(H = 0\\) في كل مكان.",
      "Recall that soap films minimize area and satisfy \\(H = 0\\).",
      "تذكر أن أغشية الصابون تصغر مساحة السطح ويكون انحناؤها المتوسط صفراً.")

    # 340: Non-separable Hilbert Spaces
    q("KAUST-P3-340", "Functional Analysis", "Medium",
      "A Hilbert space \\(H\\) is separable if and only if:",
      "يكون فضاء هيلبرت \\(H\\) قابلاً للفصل (separable) إذا وفقط إذا كان:",
      ["It possesses a countable orthonormal basis",
       "Every bounded sequence has a strongly convergent subsequence",
       "\\(H\\) is finite-dimensional",
       "Its dual space is trivial"],
      0,
      "By definition, a topological space is separable if it contains a countable dense subset. In a Hilbert space, this is equivalent to having an orthonormal basis that is at most countable. If an orthonormal basis were uncountable, the distance between any two distinct basis vectors would be \\(\\sqrt{2}\\), making it impossible to contain a countable dense set.",
      "يكون فضاء هيلبرت قابلاً للفصل إذا وفقط إذا كان يمتلك أساساً متعامداً عيارياً قابلاً للعد. فإذا كان الأساس غير قابل للعد، فإن المسافة بين أي متجهين فيه هي \\(\\sqrt{2}\\)، مما يمنع وجود مجموعة كثيفة قابلة للعد.",
      "Separability means the existence of a countable dense subset.",
      "القابلية للفصل تعني وجود مجموعة جزئية كثيفة وقابلة للعد.")

    # 341: Euler-Lagrange for Higher Derivatives
    q("KAUST-P3-341", "Calculus of Variations", "Hard",
      "For a functional depending on second derivatives \\(J[y] = \\int L(x, y, y', y'') dx\\), what is the corresponding Euler-Lagrange equation?",
      "لدالية تعتمد على المشتقات من الرتبة الثانية \\(J[y] = \\int L(x, y, y', y'') dx\\)، ما هي معادلة أويلر-لاغرانج المقابلة؟",
      ["\\(\\frac{\\partial L}{\\partial y} - \\frac{d}{dx}\\left(\\frac{\\partial L}{\\partial y'}\\right) + \\frac{d^2}{dx^2}\\left(\\frac{\\partial L}{\\partial y''}\\right) = 0\\)",
       "\\(\\frac{\\partial L}{\\partial y} - \\frac{d^2}{dx^2}\\left(\\frac{\\partial L}{\\partial y''}\\right) = 0\\)",
       "\\(\\frac{\\partial L}{\\partial y'} + \\frac{d}{dx}\\left(\\frac{\\partial L}{\\partial y''}\\right) = 0\\)",
       "\\(\\frac{\\partial L}{\\partial y} + \\frac{d}{dx}\\left(\\frac{\\partial L}{\\partial y'}\\right) + \\frac{d^2}{dx^2}\\left(\\frac{\\partial L}{\\partial y''}\\right) = 0\\)"],
      0,
      "Taking the first variation: \\(\\delta J = \\int \\left(\\frac{\\partial L}{\\partial y}\\delta y + \\frac{\\partial L}{\\partial y'}\\delta y' + \\frac{\\partial L}{\\partial y''}\\delta y''\\right) dx\\). Integrating the second term by parts once introduces \\(-\\frac{d}{dx}\\frac{\\partial L}{\\partial y'}\\). Integrating the third term by parts twice introduces \\((-1)^2 \\frac{d^2}{dx^2}\\frac{\\partial L}{\\partial y''} = +\\frac{d^2}{dx^2}\\frac{\\partial L}{\\partial y''}\\). Factoring \\(\\delta y\\) yields the 4th-order ODE: \\(\\frac{\\partial L}{\\partial y} - \\frac{d}{dx}\\left(\\frac{\\partial L}{\\partial y'}\\right) + \\frac{d^2}{dx^2}\\left(\\frac{\\partial L}{\\partial y''}\\right) = 0\\). This governs beam bending (Euler-Bernoulli beam theory).",
      "بحساب التغاير الأول والتكامل بالتجزئة: الحد الذي يحوي \\(y'\\) يُكامل مرة واحدة بإشارة سالبة، والحد الذي يحوي \\(y''\\) يُكامل مرتين فيكتسب إشارة موجبة \\((-1)^2 = +1\\). المعادلة الناتجة هي معادلة من الرتبة الرابعة تصف انحناء العوارض في المرونة.",
      "Integrate by parts twice for the \\(y''\\) variation term, yielding \\((-1)^2 = +1\\).",
      "كامل بالتجزئة مرتين لحد التغاير للمشتق الثاني لتحصل على إشارة موجبة.")

    # 342: Projection Operator Orthogonality
    q("KAUST-P3-342", "Functional Analysis", "Medium",
      "A bounded linear operator \\(P: H \\to H\\) on a Hilbert space is an ORTHOGONAL projection if and only if:",
      "يكون المؤثر الخطي المحدود \\(P: H \\to H\\) على فضاء هيلبرت إسقاطاً متعامداً إذا وفقط إذا كان:",
      ["\\(P^2 = P\\) and \\(P^* = P\\)",
       "\\(P^2 = P\\) and \\(P^* = -P\\)",
       "\\(P^2 = I\\) and \\(P^* = P\\)",
       "\\(\\|P\\| = 1\\) only"],
      0,
      "An operator is a projection (idempotent) if \\(P^2 = P\\). It is an orthogonal projection (meaning its range and null space are orthogonal: \\(\\text{im}(P) \\perp \\ker(P)\\)) if and only if it is additionally self-adjoint: \\(P^* = P\\). If \\(P^2 = P\\) but \\(P^* \\neq P\\), it is an oblique projection.",
      "يكون المؤثر إسقاطاً إذا كان ارتكاسياً \\(P^2 = P\\). ويكون إسقاطاً متعامداً إذا وفقط إذا كان متمماً لخاصية التماثل الذاتي: \\(P^* = P\\)، مما يضمن تعامد المدى مع فضاء العدم.",
      "An orthogonal projection must be idempotent (\\(P^2 = P\\)) and self-adjoint (\\(P^* = P\\)).",
      "يجب أن يكون الإسقاط المتعامد ارتكاسياً وذا مرافقة ذاتية.")

    # 343: Isoperimetric Constraint with Lagrange Multipliers
    q("KAUST-P3-343", "Calculus of Variations", "Hard",
      "To maximize \\(I[y] = \\int_a^b F(x, y, y') dx\\) subject to an integral constraint \\(K[y] = \\int_a^b G(x, y, y') dx = C\\), one forms the modified Lagrangian \\(L^* = F - \\lambda G\\). What is the multiplier \\(\\lambda\\)?",
      "لتعظيم دالية مع قيد تكاملي، نشكل اللاغرانجي المعدل \\(L^* = F - \\lambda G\\). ما هو المضاعف \\(\\lambda\\)؟",
      ["A constant scalar undetermined multiplier chosen to satisfy the constraint \\(K[y] = C\\)",
       "A function of \\(x\\) varying along the curve",
       "Always equal to 1",
       "The curvature of the curve"],
      0,
      "In isoperimetric problems (integral constraints), the constraint is a single scalar equation \\(\\int G dx = C\\). Therefore, the Lagrange multiplier \\(\\lambda\\) is a CONSTANT parameter (not a function of \\(x\\)). One solves the Euler-Lagrange equation for \\(L^* = F - \\lambda G\\) treating \\(\\lambda\\) as a constant, and then determines the value of \\(\\lambda\\) by enforcing the constraint \\(K[y] = C\\).",
      "في المسائل ذات القيود التكاملية، يكون القيد معادلة سلمية واحدة، وبالتالي فإن مضاعف لاغرانج \\(\\lambda\\) هو ثابت عددي (وليس دالة في \\(x\\)). تُحل معادلة أويلر-لاغرانج باعتبار \\(\\lambda\\) ثابتاً، ثم تُعين قيمته بتطبيق شرط القيد التكاملي.",
      "An integral constraint involves a single constant multiplier, unlike pointwise constraints.",
      "القيود التكاملية تتطلب مضاعفاً ثابتاً بخلاف القيود النقطية.")

    # 344: Resolvent Set and Resolvent Operator
    q("KAUST-P3-344", "Spectral Theory", "Medium",
      "For a closed linear operator \\(T\\) on a Banach space, the resolvent set \\(\\rho(T)\\) consists of all \\(\\lambda \\in \\mathbb{C}\\) such that \\(R_\\lambda(T) = (T - \\lambda I)^{-1}\\) is a bounded linear operator. What topological property does \\(\\rho(T)\\) always possess?",
      "لمؤثر خطي مغلق \\(T\\) على فضاء باناخ، تتكون مجموعة المحل (resolvent set) \\(\\rho(T)\\) من جميع القيم التي تجعل مؤثر المحل \\((T - \\lambda I)^{-1}\\) محدوداً. ما هي الخاصية الطوبولوجية الدائمة لـ \\(\\rho(T)\\)؟",
      ["\\(\\rho(T)\\) is always an open subset of \\(\\mathbb{C}\\)",
       "\\(\\rho(T)\\) is always a compact set",
       "\\(\\rho(T)\\) is always empty",
       "\\(\\rho(T)\\) is always a discrete set of points"],
      0,
      "The resolvent set \\(\\rho(T)\\) is always an open subset of \\(\\mathbb{C}\\). If \\(\\lambda_0 \\in \\rho(T)\\), then for any \\(\\lambda\\) close enough to \\(\\lambda_0\\) (specifically \\(|\\lambda - \\lambda_0| < 1/\\|R_{\\lambda_0}(T)\\|\\)), the Neumann series \\(R_\\lambda(T) = \\sum_{n=0}^\\infty (\\lambda - \\lambda_0)^n (R_{\\lambda_0}(T))^{n+1}\\) converges, proving that \\(R_\\lambda(T)\\) is bounded. Consequently, the spectrum \\(\\sigma(T) = \\mathbb{C} \\setminus \\rho(T)\\) is always closed.",
      "مجموعة المحل \\(\\rho(T)\\) هي دائماً مجموعة مفتوحة في \\(\\mathbb{C}\\). باستخدام متسلسلة نويمان، إذا كانت نقطة تنتمي للمجموعة فإن أي جوار كروي صغير حولها ينتمي للمجموعة أيضاً. وكنتيجة مباشرة، يكون الطيف \\(\\sigma(T)\\) دائماً مجموعة مغلقة.",
      "Use the convergence of the Neumann series for \\((T - \\lambda I)^{-1}\\).",
      "استخدم تقارب متسلسلة نويمان لمؤثر المحل في جوار أي نقطة نظامية.")

    # 345: Brachistochrone with Friction
    q("KAUST-P3-345", "Calculus of Variations", "Hard",
      "If sliding friction with coefficient \\(\\mu\\) is included in the Brachistochrone descent, what type of curve is the resulting path of fastest descent?",
      "إذا أُضيف احتكاك انزلاقي بمعامل \\(\\mu\\) إلى مسألة البركستوكرون، ما نوع المنحنى الناتج لأسرع هبوط؟",
      ["Still a cycloid, but rotated and shifted by an angle related to \\(\\mu\\)",
       "A parabola",
       "A straight line",
       "An exponential horn curve"],
      0,
      "With Coulomb friction, energy conservation gives \\(v^2 = 2g(y - \\mu x)\\). Under the rotated coordinate transformation \\(X = x + \\mu y\\) and \\(Y = y - \\mu x\\), the Euler-Lagrange equations can be integrated in closed form to yield a cycloid generated by a circle rolling along an inclined line tilted at angle \\(\\phi = \\arctan\\mu\\). Thus, the optimal curve remains a cycloid.",
      "مع وجود احتكاك كولوم، تعطي معادلة حفظ الطاقة سرعة تعتمد على \\(y - \\mu x\\). بإجراء دوران للإحداثيات بزاوية الاحتكاك \\(\\arctan\\mu\\)، تختزل معادلات أويلر-لاغرانج مجدداً إلى منحنى دويرية ولكن بالنسبة لمستوى مائل بزاوية الاحتكاك.",
      "Rotate the coordinates by the friction angle \\(\\arctan(\\mu)\\).",
      "قم بتدوير المحاور بزاوية الاحتكاك.")

    # 346: Equivalent Norms in Finite Dimensions
    q("KAUST-P3-346", "Functional Analysis", "Medium",
      "A classic theorem in functional analysis states that on any FINITE-DIMENSIONAL vector space \\(V\\):",
      "تنص نظرية كلاسيكية في التحليل الدالي على أنه في أي فضاء متجهي منتهي البعد \\(V\\):",
      ["All norms are equivalent (they induce the exact same topology)",
       "Only the Euclidean norm is complete",
       "No two distinct norms can be equivalent",
       "The \\(L^1\\) and \\(L^\\infty\\) norms induce different open sets"],
      0,
      "In finite dimensions, any norm \\(\\|\\cdot\\|\\) satisfies \\(c_1 \\|x\\|_2 \\le \\|x\\| \\le c_2 \\|x\\|_2\\) for positive constants \\(c_1, c_2 > 0\\) (by compactness of the Euclidean unit sphere and the Extreme Value Theorem). Hence, all norms induce the exact same topology, the same open sets, and the same convergent sequences. This equivalence completely fails in infinite-dimensional spaces.",
      "في الأبعاد المنتهية، أي معيار يكافئ المعيار الإقليدي بوجود ثوابت موجبة تحصره من الأعلى والأسفل، بفضل مدموجية كرة الوحدة الإقليدية. بالتالي فإن جميع المعايير تكافئ بعضها وتولد نفس الطوبولوجيا تماماً.",
      "Compactness of the unit sphere implies all norms are bounded by each other.",
      "مدموجية كرة الوحدة الإقليدية تضمن تكافؤ جميع المعايير.")

    # 347: Brachistochrone Tautochrone Property
    q("KAUST-P3-347", "Calculus of Variations", "Medium",
      "Christiaan Huygens discovered that the cycloid is also a tautochrone (isochrone). What does this property state?",
      "اكتشف كريستيان هويغنز أن الدويرية تمتلك أيضاً خاصية تساوي الزمن (tautochrone). ماذا تعني هذه الخاصية؟",
      ["The time taken by a particle sliding down a cycloidal bowl to reach the bottom is completely independent of its starting point",
       "The path has the same length in all directions",
       "The velocity at the bottom is constant regardless of release height",
       "The particle travels at constant acceleration throughout"],
      0,
      "The tautochrone property states that a bead sliding frictionlessly down an inverted cycloidal curve under gravity takes exactly the SAME time \\(T = \\pi\\sqrt{R/g}\\) to reach the lowest point, regardless of where on the curve it is released from rest. Huygens used this property to design the isochronous cycloidal pendulum clock.",
      "تعني خاصية تساوي الزمن (tautochrone) أن الزمن الذي يستغرقه جسيم ينزلق بدون احتكاك على منحنى الدويرية المقلوب للوصول إلى أدنى نقطة هو ثابت تماماً \\(T = \\pi\\sqrt{R/g}\\) ولا يعتمد إطلاقاً على موضع نقطة البداية.",
      "The period of oscillation on a cycloid is strictly independent of amplitude.",
      "زمن الوصول إلى القاع مستقل تماماً عن نقطة الإفلات.")

    # 348: Essential Spectrum
    q("KAUST-P3-348", "Spectral Theory", "Hard",
      "Weyl's theorem on the essential spectrum asserts that if \\(A\\) is a self-adjoint operator and \\(K\\) is a compact self-adjoint operator, how does the essential spectrum \\(\\sigma_{\\text{ess}}(A + K)\\) compare to \\(\\sigma_{\\text{ess}}(A)\\)?",
      "تنص نظرية فايل للطيف الجوهري على أنه إذا كان \\(A\\) مؤثراً ذاتي المرافقة و \\(K\\) مؤثراً مدمجاً، فكيف يرتبط الطيف الجوهري للمجموع \\(\\sigma_{\\text{ess}}(A + K)\\) بـ \\(\\sigma_{\\text{ess}}(A)\\)؟",
      ["\\(\\sigma_{\\text{ess}}(A + K) = \\sigma_{\\text{ess}}(A)\\) (the essential spectrum is invariant under compact perturbations)",
       "\\(\\sigma_{\\text{ess}}(A + K) = \\emptyset\\)",
       "\\(\\sigma_{\\text{ess}}(A + K) = \\sigma(A) \\cup \\sigma(K)\\)",
       "\\(\\sigma_{\\text{ess}}(A + K) = \\sigma_{\\text{ess}}(A) + \\|K\\|\\)"],
      0,
      "Weyl's Essential Spectrum Invariance Theorem states that compact perturbations do not change the essential spectrum of a self-adjoint operator: \\(\\sigma_{\\text{ess}}(A + K) = \\sigma_{\\text{ess}}(A)\\). Compact operators can only create or destroy isolated eigenvalues of finite multiplicity, leaving the continuous spectrum and accumulation points completely untouched.",
      "تنص نظرية فايل على أن الاضطرابات المدمجة لا تغير الطيف الجوهري للمؤثرات ذاتية المرافقة: \\(\\sigma_{\\text{ess}}(A + K) = \\sigma_{\\text{ess}}(A)\\). المؤثرات المدمجة يمكنها فقط إضافة أو إزالة قيم ذاتية معزولة دون المساس بالطيف المتصل.",
      "Compact perturbations cannot alter the continuous spectrum.",
      "الاضطرابات المدمجة لا تؤثر على الطيف المستمر أو نقاط التراكم.")

    # 349: Weak-* Topology vs Weak Topology
    q("KAUST-P3-349", "Functional Analysis", "Hard",
      "In the dual space \\(X^*\\), a net of functionals \\(f_\\alpha\\) converges to \\(f\\) in the weak-* topology if and only if:",
      "في الفضاء الثنوي \\(X^*\\)، تتقارب شبكة من التوابع \\(f_\\alpha\\) نحو \\(f\\) في الطوبولوجيا الضعيفة نجمة إذا وفقط إذا كان:",
      ["\\(f_\\alpha(x) \\to f(x)\\) for all \\(x \\in X\\) (pointwise convergence on \\(X\\))",
       "\\(\\|f_\\alpha - f\\|_{X^*} \\to 0\\)",
       "\\(F(f_\\alpha) \\to F(f)\\) for all \\(F \\in X^{**}\\)",
       "\\(f_\\alpha\\) converges uniformly on the unit ball of \\(X\\)"],
      0,
      "The weak-* topology \\(\\sigma(X^*, X)\\) is defined as the coarsest topology on \\(X^*\\) making all evaluation maps \\(f \\mapsto f(x)\\) continuous for each \\(x \\in X\\). Hence, convergence in the weak-* topology is precisely pointwise convergence on vectors of \\(X\\): \\(f_\\alpha \\xrightarrow{w^*} f \\iff f_\\alpha(x) \\to f(x)\\) for all \\(x \\in X\\). In contrast, weak convergence \\(\\sigma(X^*, X^{**})\\) requires convergence on all elements of the larger bidual \\(X^{**}\\).",
      "تُعرّف الطوبولوجيا الضعيفة نجمة بأنها أضعف طوبولوجيا تجعل توابع التقييم \\(f \\mapsto f(x)\\) مستمرة لكل \\(x \\in X\\). بالتالي، فإن التقارب فيها هو بدقة التقارب النقطي على عناصر الفضاء الأصلي \\(X\\).",
      "Weak-* convergence is pointwise convergence on the pre-dual space \\(X\\).",
      "التقارب الضعيف نجمة هو التقارب النقطي على عناصر الفضاء الأصلي.")

    # 350: Geodesic Deviation (Jacobi Equation)
    q("KAUST-P3-350", "Calculus of Variations", "Hard",
      "The variation of neighboring geodesics on a Riemannian surface with Gaussian curvature \\(K\\) is governed by the Jacobi equation for normal separation \\(J(s)\\): \\(J''(s) + K(s) J(s) = 0\\). If \\(K = -1\\) (hyperbolic plane), how does the separation \\(J(s)\\) between initially parallel geodesics evolve?",
      "يوصف تباعد الجيوديسيات المتجاورة على سطح بمعادلة ياكوبي \\(J''(s) + K(s) J(s) = 0\\). إذا كان الانحناء \\(K = -1\\) (المستوى الزائدي)، كيف يتطور التباعد \\(J(s)\\) بين جيوديسيات متوازية في البداية؟",
      ["\\(J(s) = A \\cosh(s) + B \\sinh(s)\\) (separates exponentially)",
       "\\(J(s) = A \\cos(s) + B \\sin(s)\\) (oscillates periodically)",
       "\\(J(s) = A s + B\\) (diverges linearly)",
       "\\(J(s) = A e^{-s^2}\\) (converges to zero)"],
      0,
      "For constant negative curvature \\(K = -1\\), the Jacobi equation becomes \\(J''(s) - J(s) = 0\\). The characteristic roots of \\(r^2 - 1 = 0\\) are \\(r = \\pm 1\\), giving the general solution \\(J(s) = A \\cosh(s) + B \\sinh(s) = c_1 e^s + c_2 e^{-s}\\). The growing mode \\(e^s\\) causes neighboring geodesics to diverge exponentially from each other, which is the hallmark of negative curvature and geodesic chaos (hyperbolic geometry).",
      "عندما يكون الانحناء سالباً وثابتاً \\(K = -1\\)، تصبح معادلة ياكوبي \\(J'' - J = 0\\). حلولها هي دوال زائدية \\(J(s) = A\\cosh(s) + B\\sinh(s)\\)، وتتباعد المسارات أسياً بمعدل \\(e^s\\)، وهي السمة الأساسية للهندسة الزائدية والفوضى الحركية.",
      "Solve the linear ODE \\(J''(s) - J(s) = 0\\).",
      "حل المعادلة التفاضلية الخطية \\(J'' - J = 0\\).")

    return questions

if __name__ == "__main__":
    qs = get_p3_part_b()
    print(f"Loaded {len(qs)} questions for Phase 3 Part B.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=301):
        expected_id = f"KAUST-P3-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 3 Part B questions successfully verified!")
