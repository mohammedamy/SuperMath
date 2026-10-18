#!/usr/bin/env python3
"""
KAUST Phase 3 Questions Part D: 401 to 450
Elite Research:
- Differential Geometry & Lie Groups (401-412)
- Convex Optimization & Duality (413-425)
- Advanced Applied Mathematics, Signal Processing & Optimal Transport (426-438)
- Analytic Number Theory, Spectral Graph Theory & Advanced Discrete Math (439-450)
Lineages: Cambridge Tripos Part III, MIT 18.102/18.065/6.252, Stanford EE364a/STATS 300, Harvard Math 212/230.
"""

def get_p3_part_d():
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

    # 401: Tangent Space and Derivations
    q("KAUST-P3-401", "Differential Geometry", "Hard",
      "Let \\(M\\) be a smooth \\(n\\)-dimensional manifold and \\(p \\in M\\). A derivation at \\(p\\) is a linear mapping \\(v: C^\\infty(M) \\to \\mathbb{R}\\) satisfying the Leibniz product rule \\(v(fg) = v(f)g(p) + f(p)v(g)\\). What is the dimension of the vector space \\(T_p M\\) of all derivations at \\(p\\)?",
      "لتكن \\(M\\) متعدداً شعبياً أملس ذا بعد \\(n\\) ولتكن \\(p \\in M\\). الاشتقاق عند \\(p\\) هو تطبيق خطي \\(v: C^\\infty(M) \\to \\mathbb{R}\\) يحقق قاعدة لايبنتس لضرب الدوال \\(v(fg) = v(f)g(p) + f(p)v(g)\\). ما هو بعد فضاء المتجهات \\(T_p M\\) لجميع الاشتقاقات عند \\(p\\)؟",
      ["\\(n\\)",
       "\\(2n\\)",
       "\\(\\infty\\)",
       "\\(n(n+1)/2\\)"],
      0,
      "By the fundamental theorem of smooth manifolds, the space of derivations of \\(C^\\infty(M)\\) at \\(p\\) is canonically isomorphic to the geometric tangent space \\(\\mathbb{R}^n\\) via local coordinates \\(x^1, \\dots, x^n\\), spanned by the basis directional derivatives \\(\\left\\{ \\left.\\frac{\\partial}{\\partial x^i}\\right|_p \\right\\}_{i=1}^n\\). Hence \\(\\dim T_p M = n\\).",
      "وفقاً للنظرية الأساسية للمتعددات الشعبية الملساء، فإن فضاء الاشتقاقات عند النقطة \\(p\\) يطابق تجريدياً الفضاء المماسي الهندسي \\(\\mathbb{R}^n\\) من خلال الإحداثيات المحلية، ومولد بأساس المشتقات الاتجاهية \\(\\left\\{ \\left.\\frac{\\partial}{\\partial x^i}\\right|_p \\right\\}_{i=1}^n\\). بالتالي فإن بعده يساوي \\(n\\).",
      "Think of the coordinate partial derivatives spanning the tangent space at a point.",
      "تذكر أن المشتقات الجزئية الإحداثية تولد الفضاء المماسي عند نقطة وبعدها يساوي بعد المتعدد الشعبي.")

    # 402: Pullback of Differential Forms
    q("KAUST-P3-402", "Differential Geometry", "Hard",
      "Let \\(F: M \\to N\\) be a smooth map between smooth manifolds. If \\(\\omega \\in \\Omega^k(N)\\) is a smooth \\(k\\)-form, how does the exterior derivative \\(d\\) commute with the pullback operator \\(F^*\\)?",
      "ليكن \\(F: M \\to N\\) تطبيقاً أملس بين متعددين شعبيين أملسين. إذا كانت \\(\\omega \\in \\Omega^k(N)\\) صيغة تفاضلية ملساء من الرتبة \\(k\\)، فكيف يتبادل المؤثر التفاضلي الخارجي \\(d\\) مع مؤثر السحب للخلف \\(F^*\\)؟",
      ["\\(d(F^*\\omega) = F^*(d\\omega)\\)",
       "\\(d(F^*\\omega) = (-1)^k F^*(d\\omega)\\)",
       "\\(d(F^*\\omega) = F^*(d\\omega) + dF \\wedge \\omega\\)",
       "\\(d(F^*\\omega) = 0\\) for all \\(\\omega\\)"],
      0,
      "The pullback of differential forms is natural with respect to the exterior derivative: \\(d(F^*\\omega) = F^*(d\\omega)\\). This fundamental property ensures that the exterior derivative commutes with smooth coordinate transformations and maps smooth de Rham cohomology classes functorially.",
      "مؤثر السحب للخلف للصيغ التفاضلية متوافق طبيعياً مع المشتق الخارجي: \\(d(F^*\\omega) = F^*(d\\omega)\\). تضمن هذه الخاصية الجوهرية تبادل التفاضل الخارجي مع التحويلات الإحداثية الملساء وتجعل كوهومولوجيا دي رام دالّية.",
      "The pullback operator commutes directly with the exterior derivative without any extra sign or boundary terms.",
      "مؤثر السحب للخلف يتبادل مباشرة مع المشتق الخارجي دون أي إشارة سالبة أو حدود إضافية.")

    # 403: Christoffel Symbols of the Levi-Civita Connection
    q("KAUST-P3-403", "Differential Geometry", "Hard",
      "On a Riemannian manifold \\((M, g)\\), the unique torsion-free metric-compatible Levi-Civita connection has Christoffel symbols \\(\\Gamma^k_{ij}\\) expressed in local coordinates in terms of the metric tensor \\(g_{ij}\\) and its inverse \\(g^{kl}\\) as which of the following?",
      "على متعدد ريماني \\((M, g)\\)، يمتلك اتصال ليفي-تشيفيتا الوحيد المتوافق مع المتري والعديم الالتواء معاملات كريستوفل \\(\\Gamma^k_{ij}\\) المعبر عنها في إحداثيات محلية بدلالة موتر المتري \\(g_{ij}\\) ومعكوسه \\(g^{kl}\\) بأي صيغة؟",
      ["\\(\\Gamma^k_{ij} = \\frac{1}{2} g^{kl} \\left( \\frac{\\partial g_{jl}}{\\partial x^i} + \\frac{\\partial g_{il}}{\\partial x^j} - \\frac{\\partial g_{ij}}{\\partial x^l} \\right)\\)",
       "\\(\\Gamma^k_{ij} = \\frac{1}{2} g_{kl} \\left( \\frac{\\partial g^{jl}}{\\partial x^i} + \\frac{\\partial g^{il}}{\\partial x^j} - \\frac{\\partial g^{ij}}{\\partial x^l} \\right)\\)",
       "\\(\\Gamma^k_{ij} = g^{kl} \\frac{\\partial g_{ij}}{\\partial x^l}\\)",
       "\\(\\Gamma^k_{ij} = \\frac{\\partial g_{ij}}{\\partial x^k} - \\frac{\\partial g_{ik}}{\\partial x^j}\\)"],
      0,
      "The Levi-Civita connection satisfies metric compatibility \\(\\nabla g = 0\\) and torsion freedom \\(\\nabla_X Y - \\nabla_Y X = [X,Y]\\). Permuting the metric compatibility equations yields Koszul's formula, which in coordinate components gives \\(\\Gamma^k_{ij} = \\frac{1}{2} g^{kl} (\\partial_i g_{jl} + \\partial_j g_{il} - \\partial_l g_{ij})\\).",
      "يحقق اتصال ليفي-تشيفيتا التوافق مع المتري والصفة عديمة الالتواء. بتبديل معادلات التوافق المتري نحصل على صيغة كوزول، والتي تعطي في المكونات الإحداثية الصيغة الشهيرة بدلالة المشتقات الجزئية للمتري ومعكوسه.",
      "The two positive derivative terms involve index pairings with \\(l\\), while the subtracted term differentiates the components \\(g_{ij}\\) with respect to \\(x^l\\).",
      "الحدان الموجبان يربطان المؤشرات مع \\(l\\) بينما يطرح الحد الأخير مشتق \\(g_{ij}\\) بالنسبة للمؤشر \\(l\\).")

    # 404: Geodesic Differential Equation
    q("KAUST-P3-404", "Differential Geometry", "Hard",
      "A curve \\(\\gamma(t) = (x^1(t), \\dots, x^n(t))\\) on a Riemannian manifold is a geodesic parametrized by affine arc length if and only if its coordinates satisfy which second-order system of ordinary differential equations?",
      "يكون المنحنى \\(\\gamma(t) = (x^1(t), \\dots, x^n(t))\\) على متعدد ريماني مساراً جيوديسياً معلماً بطول القوس الأفيني إذا وفقط إذا حققت إحداثياته أي نظام من المعادلات التفاضلية العادية من الرتبة الثانية؟",
      ["\\(\\ddot{x}^k + \\sum_{i,j=1}^n \\Gamma^k_{ij} \\dot{x}^i \\dot{x}^j = 0\\)",
       "\\(\\ddot{x}^k - \\sum_{i,j=1}^n \\Gamma^k_{ij} \\dot{x}^i \\dot{x}^j = 0\\)",
       "\\(\\ddot{x}^k + \\sum_{i=1}^n \\Gamma^k_{ii} (\\dot{x}^i)^2 = 0\\)",
       "\\(\\dot{x}^k + \\sum_{i,j=1}^n g^{ij} \\Gamma^k_{ij} x^i x^j = 0\\)"],
      0,
      "A geodesic represents parallel transport of its own velocity vector field: \\(\\nabla_{\\dot{\\gamma}} \\dot{\\gamma} = 0\\). In local coordinates, applying the covariant derivative gives \\(\\frac{d^2 x^k}{dt^2} + \\Gamma^k_{ij} \\frac{dx^i}{dt}\\frac{dx^j}{dt} = 0\\).",
      "يمثل الجيوديسي نقلاً متوازياً لمتجه سرعته الذاتي: \\(\\nabla_{\\dot{\\gamma}} \\dot{\\gamma} = 0\\). في الإحداثيات المحلية، بتطبيق المشتق المتغير المشترك نحصل على نظام المعادلات: \\(\\ddot{x}^k + \\Gamma^k_{ij}\\dot{x}^i\\dot{x}^j = 0\\).",
      "The acceleration term is balanced by the quadratic velocity contraction with the Christoffel symbols.",
      "يتوازن تسارع المنحنى مع التقلص التربيعي للسرعات مع معاملات كريستوفل.")

    # 405: Riemann Curvature Tensor and Algebraic Bianchi Identity
    q("KAUST-P3-405", "Differential Geometry", "Hard",
      "Let \\(R(X,Y)Z = \\nabla_X \\nabla_Y Z - \\nabla_Y \\nabla_X Z - \\nabla_{[X,Y]} Z\\) be the Riemann curvature operator on a torsion-free Riemannian manifold. What is the First (Algebraic) Bianchi Identity satisfied by \\(R\\)?",
      "ليكن \\(R(X,Y)Z = \\nabla_X \\nabla_Y Z - \\nabla_Y \\nabla_X Z - \\nabla_{[X,Y]} Z\\) مؤثر انحناء ريمان على متعدد ريماني عديم الالتواء. ما هي متطابقة بيانكي الأولى (الجبرية) التي يحققها \\(R\\)؟",
      ["\\(R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0\\)",
       "\\(R(X,Y)Z - R(Y,Z)X + R(Z,X)Y = 0\\)",
       "\\(R(X,Y)Z + R(Y,X)Z = Z\\)",
       "\\(\\nabla_X R(Y,Z)W + \\nabla_Y R(Z,X)W + \\nabla_Z R(X,Y)W = 0\\)"],
      0,
      "For any torsion-free connection, the cyclic sum over three vector fields vanishes identically: \\(R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0\\). This is the First (Algebraic) Bianchi Identity. The differential identity involving covariant derivatives \\(\\sum_{\\text{cyclic}} \\nabla_X R(Y,Z) = 0\\) is the Second Bianchi Identity.",
      "لأي اتصال عديم الالتواء، يتلاشى المجموع الدوري لثلاثة حقول اتجاهية تماماً: \\(R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0\\). هذه هي متطابقة بيانكي الجبرية الأولى، بينما تسمى المتطابقة التفاضلية التي تتضمن المشتقات متطابقة بيانكي الثانية.",
      "Consider the cyclic permutation of the three vectors X, Y, Z summed to zero.",
      "انظر إلى التبديل الدوري للمتجهات الثلاثة X و Y و Z ومجموعها يساوي صفراً.")

    # 406: Sectional and Ricci Curvatures
    q("KAUST-P3-406", "Differential Geometry", "Hard",
      "A Riemannian manifold \\((M, g)\\) of dimension \\(n \\ge 3\\) is called an Einstein manifold if its Ricci curvature tensor \\(\\text{Ric}\\) satisfies which relation for some smooth function (or constant) \\(\\lambda\\)?",
      "يُسمى المتعدد الريماني \\((M, g)\\) ذو البعد \\(n \\ge 3\\) متعدداً لأينشتاين إذا حقق موتر انحناء ريتشي \\(\\text{Ric}\\) أي علاقة مع دالة ملساء (أو ثابت) \\(\\lambda\\)؟",
      ["\\(\\text{Ric} = \\lambda g\\)",
       "\\(\\text{Ric} = \\lambda R\\)",
       "\\(\\text{Ric} = 0\\) everywhere strictly",
       "\\(\\text{Ric}(X,Y) = \\lambda \\|X\\|\\|Y\\|\\)"],
      0,
      "An Einstein manifold is defined by the condition that its Ricci tensor is pointwise proportional to the metric tensor: \\(\\text{Ric} = \\lambda g\\). By Schur's lemma, for dimension \\(n \\ge 3\\), the proportionality factor \\(\\lambda\\) must be a constant on any connected manifold.",
      "يُعرّف متعدد أينشتاين بأن موتر ريتشي يتناسب نقطياً مع موتر المتري: \\(\\text{Ric} = \\lambda g\\). وبموجب مبرهنة شور، عندما يكون البعد \\(n \\ge 3\\)، فإن معامل التناسب \\(\\lambda\\) يكون ثابتاً حتماً على أي متعدد متصل.",
      "The Ricci tensor is directly proportional to the Riemannian metric tensor itself.",
      "موتر ريتشي يتناسب طردياً مع موتر المتري الريماني نفسه.")

    # 407: Gauss-Bonnet Theorem with SVG
    svg_gauss_bonnet = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 120' width='100%' height='100%' style='background:#0d1117;'>
  <!-- Sphere: chi=2 -->
  <circle cx='60' cy='60' r='35' fill='#161b22' stroke='#58a6ff' stroke-width='2'/>
  <ellipse cx='60' cy='60' rx='35' ry='12' fill='none' stroke='#58a6ff' stroke-width='1' stroke-dasharray='3,3'/>
  <text x='60' y='110' fill='#58a6ff' font-family='sans-serif' font-size='11' text-anchor='middle'>Sphere: \\(\\chi=2\\)</text>
  <!-- Torus: chi=0 -->
  <ellipse cx='160' cy='60' rx='45' ry='25' fill='#161b22' stroke='#3fb950' stroke-width='2'/>
  <path d='M 140 58 Q 160 70 180 58' fill='none' stroke='#3fb950' stroke-width='1.5'/>
  <path d='M 145 60 Q 160 50 175 60' fill='none' stroke='#3fb950' stroke-width='1.5'/>
  <text x='160' y='110' fill='#3fb950' font-family='sans-serif' font-size='11' text-anchor='middle'>Torus: \\(\\chi=0\\)</text>
  <!-- Double Torus: chi=-2 -->
  <ellipse cx='260' cy='60' rx='50' ry='25' fill='#161b22' stroke='#bc8cff' stroke-width='2'/>
  <circle cx='245' cy='60' r='6' fill='#0d1117' stroke='#bc8cff' stroke-width='1.5'/>
  <circle cx='275' cy='60' r='6' fill='#0d1117' stroke='#bc8cff' stroke-width='1.5'/>
  <text x='260' y='110' fill='#bc8cff' font-family='sans-serif' font-size='11' text-anchor='middle'>Genus 2: \\(\\chi=-2\\)</text>
</svg>"""

    q("KAUST-P3-407", "Differential Geometry", "Medium",
      "For a compact, boundaryless, orientable 2-dimensional Riemannian surface \\(M\\) of genus \\(g\\), the Gauss-Bonnet theorem states that \\(\\int_M K \\, dA = 2\\pi \\chi(M)\\), where \\(K\\) is the Gaussian curvature. What is the total integral \\(\\int_M K \\, dA\\) for a torus (genus \\(g=1\\))?",
      "لسطح ريماني ثنائي الأبعاد \\(M\\) متراص وموجه وبدون حدود ذي جنس \\(g\\)، تنص مبرهنة غاوس-بونيه على أن \\(\\int_M K \\, dA = 2\\pi \\chi(M)\\)، حيث \\(K\\) هو انحناء غاوس. ما هي قيمة التكامل الكلي \\(\\int_M K \\, dA\\) لطارة (جنس \\(g=1\\))؟",
      ["\\(0\\)",
       "\\(4\\pi\\)",
       "\\(2\\pi\\)",
       "\\(-2\\pi\\)"],
      0,
      "The Euler characteristic of a closed orientable surface of genus \\(g\\) is \\(\\chi(M) = 2 - 2g\\). For a torus, \\(g = 1\\), so \\(\\chi(M) = 2 - 2(1) = 0\\). By the Gauss-Bonnet theorem, \\(\\int_M K \\, dA = 2\\pi \\chi(M) = 2\\pi(0) = 0\\). The regions of positive curvature on the outer equator exactly cancel the negative curvature on the inner donut hole.",
      "الخاصية المميزة لأويلر لسطح مغلق موجه ذي جنس \\(g\\) هي \\(\\chi(M) = 2 - 2g\\). بالنسبة للطارة، \\(g=1\\)، وبالتالي \\(\\chi = 0\\). بموجب مبرهنة غاوس-بونيه، فإن \\(\\int_M K \\, dA = 2\\pi(0) = 0\\)، حيث تتلاشى مناطق الانحناء الموجب عند الحافة الخارجية تماماً مع مناطق الانحناء السالب عند الحفرة الداخلية.",
      "Recall Euler characteristic formula \\(\\chi = 2 - 2g\\) for a surface of genus \\(g\\).",
      "تذكر صيغة أويلر المميزة \\(\\chi = 2 - 2g\\) لسطح ذي جنس \\(g\\).",
      diagram=svg_gauss_bonnet)

    # 408: Lie Algebra so(3) and Commutation Relations
    q("KAUST-P3-408", "Lie Groups & Algebras", "Hard",
      "The Lie algebra \\(\\mathfrak{so}(3)\\) of the rotation group \\(SO(3)\\) consists of \\(3 \\times 3\\) skew-symmetric real matrices under the matrix commutator bracket \\([A, B] = AB - BA\\). If the standard basis is given by rotation generators \\(J_1, J_2, J_3\\), what are the commutation relations satisfied by these generators?",
      "يتكون جبر لي \\(\\mathfrak{so}(3)\\) لزمرة الدوران \\(SO(3)\\) من مصفوفات حقيقية متخالفة متماثلة من القياس \\(3 \\times 3\\) تحت قوس لي التبادلي \\([A, B] = AB - BA\\). إذا كان الأساس المعياري معطى بمولدات الدوران \\(J_1, J_2, J_3\\)، فما هي العلاقات التبادلية التي تحققها هذه المولدات؟",
      ["\\([J_i, J_j] = \\sum_{k=1}^3 \\epsilon_{ijk} J_k\\)",
       "\\([J_i, J_j] = \\delta_{ij} I\\)",
       "\\([J_i, J_j] = 0\\)",
       "\\([J_i, J_j] = J_i J_j + J_j J_i\\)"],
      0,
      "The rotation generators satisfy \\([J_1, J_2] = J_3\\), \\([J_2, J_3] = J_1\\), and \\([J_3, J_1] = J_2\\), which compactly summarizes via the Levi-Civita Levi symbol as \\([J_i, J_j] = \\epsilon_{ijk} J_k\\). This reflects the cross-product algebra in \\(\\mathbb{R}^3\\).",
      "تحقق مولدات الدوران العلاقات التبادلية \\([J_1, J_2] = J_3\\) وتبديلاتها الدورية، والتي يُعبر عنها بدقة بواسطة رمز ليفي-تشيفيتا بالتعبير \\([J_i, J_j] = \\epsilon_{ijk} J_k\\)، وهو ما يماثل جبر الضرب الاتجاهي في الفضاء ثلاثي الأبعاد.",
      "The Lie bracket of the rotation generators mirrors the vector cross product in three dimensions.",
      "قوس لي لمولدات الدوران يطابق تماماً الضرب الاتجاهي للمتجهات في الأبعاد الثلاثة.")

    # 409: SU(2) Covering of SO(3)
    q("KAUST-P3-409", "Lie Groups & Algebras", "Hard",
      "The special unitary group \\(SU(2)\\) forms the universal covering group of the 3D rotation group \\(SO(3)\\). What is the kernel of the standard double-cover homomorphism \\(\\Phi: SU(2) \\to SO(3)\\)?",
      "تشكل الزمرة الأحادية الخاصة \\(SU(2)\\) زمرة الغطاء الشامل لزمرة الدوران ثلاثية الأبعاد \\(SO(3)\\). ما هي نواة (kernel) تشاكل الغطاء المزدوج المعياري \\(\\Phi: SU(2) \\to SO(3)\\)؟",
      ["\\(\\{I, -I\\} \\cong \\mathbb{Z}_2\\)",
       "\\(\\{I\\}\\)",
       "\\(U(1)\\)",
       "\\(SO(2)\\)"],
      0,
      "The group \\(SU(2)\\) is simply connected (topologically the 3-sphere \\(S^3\\)) and double-covers \\(SO(3) \\cong \\mathbb{RP}^3\\). The covering map \\(\\Phi\\) has kernel \\(\\{\\pm I\\}\\), meaning \\(SO(3) \\cong SU(2)/\\{\\pm I\\}\\). Both \\(U\\) and \\(-U\\) represent the exact same physical rotation in \\(SO(3)\\), the mathematical basis for quantum spin-1/2 fermions.",
      "الزمرة \\(SU(2)\\) بسيطة الاتصال (طوبولوجياً هي الكرة ثلاثية الأبعاد \\(S^3\\)) وتغطي \\(SO(3)\\) تغطية مزدوجة. نواة التطبيق التشاكلي هي \\(\\{\\pm I\\}\\)، مما يعني أن \\(SO(3) \\cong SU(2)/\\{\\pm I\\}\\). يمثل كل من \\(U\\) و \\(-U\\) نفس الدوران الفيزيائي تماماً، وهو الأساس الرياضي للفرميونات ذات اللف المغزلي 1/2.",
      "A 360-degree rotation maps to -I in SU(2), requiring a 720-degree rotation to return to +I.",
      "الدوران بمقدار 360 درجة يقابل -I في SU(2)، ويتطلب دوراناً بمقدار 720 درجة للعودة للمصفوفة المحايدة +I.")

    # 410: Killing Form and Semisimplicity
    q("KAUST-P3-410", "Lie Groups & Algebras", "Hard",
      "The Killing form on a finite-dimensional Lie algebra \\(\\mathfrak{g}\\) is the symmetric bilinear form defined by \\(B(X, Y) = \\text{tr}(\\text{ad}_X \\circ \\text{ad}_Y)\\). By Cartan's Criterion, a Lie algebra \\(\\mathfrak{g}\\) is semisimple if and only if \\(B\\) satisfies which condition?",
      "شكل كيلينغ على جبر لي ذي بعد منتهٍ \\(\\mathfrak{g}\\) هو الشكل الخطي المزدوج المتماثل المعرف بواسطة \\(B(X, Y) = \\text{tr}(\\text{ad}_X \\circ \\text{ad}_Y)\\). وفق معيار كارتان، يكون جبر لي \\(\\mathfrak{g}\\) شبه بسيط (semisimple) إذا وفقط إذا حقق \\(B\\) أي شرط؟",
      ["\\(B\\) is non-degenerate (i.e., \\(\\det(B) \\ne 0\\))",
       "\\(B\\) is strictly positive definite",
       "\\(B(X, Y) = 0\\) for all \\(X, Y\\)",
       "\\(B\\) is skew-symmetric"],
      0,
      "Cartan's First and Second Criteria state that: (1) A Lie algebra is solvable if and only if \\(B(\\mathfrak{g}, [\\mathfrak{g}, \\mathfrak{g}]) = 0\\); (2) A Lie algebra is semisimple if and only if its Killing form \\(B\\) is non-degenerate (has trivial radical \\(\\mathfrak{g}^\\perp = \\{0\\}\\)).",
      "ينص معيار كارتان للتبسيط على أن جبر لي يكون شبه بسيط (semisimple) إذا وفقط إذا كان شكل كيلينغ \\(B\\) غير منحل (non-degenerate)، أي أن مصفوفته ذات محدد غير صفري وجذره تافه.",
      "Semisimplicity is characterized by the non-degeneracy of its canonical trace form.",
      "تتميز صفة شبه البساطة بعدم انحلال شكل الأثر القياسي لجبر لي.")

    # 411: Hodge Star Operator
    q("KAUST-P3-411", "Differential Geometry", "Hard",
      "On an oriented \\(n\\)-dimensional Riemannian manifold \\((M, g)\\), the Hodge star operator \\(*: \\Omega^k(M) \\to \\Omega^{n-k}(M)\\) satisfies \\(*(*\\omega) = (-1)^{k(n-k)} \\omega\\). If \\(n = 4\\) and \\(\\omega\\) is a 2-form (\\(k=2\\)), what is \\(*(*\\omega)\\)?",
      "على متعدد ريماني موجه ذي بعد \\(n=4\\)، يحقق مؤثر هودج النجمي \\(*: \\Omega^k(M) \\to \\Omega^{n-k}(M)\\) العلاقة \\(*(*\\omega) = (-1)^{k(n-k)} \\omega\\). إذا كانت \\(\\omega\\) صيغة من الرتبة 2 (\\(k=2\\))، فما هي قيمة \\(*(*\\omega)\\)؟",
      ["\\(\\omega\\)",
       "\\(-\\omega\\)",
       "\\(0\\)",
       "\\(4\\omega\\)"],
      0,
      "For \\(n = 4\\) and \\(k = 2\\), we compute the exponent \\(k(n - k) = 2(4 - 2) = 4\\). Therefore, \\(*(*\\omega) = (-1)^4 \\omega = \\omega\\). This involutive property \\(*^2 = \\text{id}\\) allows 2-forms in 4 dimensions to decompose into eigenspaces of eigenvalues \\(+1\\) (self-dual forms) and \\(-1\\) (anti-self-dual forms), central to Yang-Mills theory and Donaldson invariants.",
      "بتعويض \\(n=4\\) و \\(k=2\\)، نجد أن الأس هو \\(k(n-k) = 2(2) = 4\\). بالتالي، \\(*(*\\omega) = (-1)^4 \\omega = \\omega\\). تتيح هذه الخاصية الذاتية تجزئة الصيغ الثنائية في 4 أبعاد إلى فضاءات ذاتية بقيم ذاتية \\(+1\\) و \\(-1\\)، وهي جوهر نظرية يانغ-ميلز ومؤثرات دونالدسون.",
      "Calculate \\((-1)^{k(n-k)}\\) for \\(n=4, k=2\\).",
      "احسب \\((-1)^{k(n-k)}\\) حيث \\(n=4\\) و \\(k=2\\).")

    # 412: Hodge Decomposition Theorem
    q("KAUST-P3-412", "Differential Geometry", "Hard",
      "On a compact orientable Riemannian manifold without boundary, the Hodge Decomposition Theorem asserts that any smooth differential \\(k\\)-form \\(\\omega\\) uniquely decomposes as \\(\\omega = d\\alpha + \\delta\\beta + \\gamma\\), where \\(\\gamma\\) satisfies which condition?",
      "على متعدد ريماني متراص وموجه بدون حدود، تؤكد مبرهنة هودج للتفكيك أن أي صيغة تفاضلية ملساء \\(\\omega\\) تتفكك بشكل وحيد إلى \\(\\omega = d\\alpha + \\delta\\beta + \\gamma\\)، حيث تحقق الصيغة \\(\\gamma\\) أي شرط؟",
      ["\\(\\Delta \\gamma = 0\\) (harmonic form: \\(d\\gamma = 0\\) and \\(\\delta\\gamma = 0\\))",
       "\\(d\\gamma = \\gamma\\)",
       "\\(\\delta\\gamma = \\alpha\\)",
       "\\(*\\gamma = 0\\)"],
      0,
      "The Hodge Decomposition Theorem states that \\(\\Omega^k(M) = \\text{im}(d) \\oplus \\text{im}(\\delta) \\oplus \\mathcal{H}^k(M)\\), where \\(\\mathcal{H}^k(M) = \\ker(\\Delta)\\) is the finite-dimensional space of harmonic \\(k\\)-forms satisfying \\(\\Delta \\gamma = (d\\delta + \\delta d)\\gamma = 0\\), which is equivalent to \\(d\\gamma = 0\\) and \\(\\delta\\gamma = 0\\). Furthermore, \\(\\mathcal{H}^k(M) \\cong H^k_{\\text{dR}}(M)\\).",
      "تنص مبرهنة هودج للتفكيك على أن فضاء الصيغ التفاضلية يتفكك إلى مجموع مباشر لثلاثة فضاءات متعامدة: الصور التامة وصور المشتق المرافق وفضاء الصيغ التوافقية \\(\\mathcal{H}^k(M)\\) التي تحقق \\(\\Delta \\gamma = 0\\) (أي أنها مغلقة ومتوافقة معاً)، وهو متشاكل مع فضاء كوهومولوجيا دي رام.",
      "The component \\(\\gamma\\) represents the harmonic forms belonging to the kernel of the Hodge Laplacian.",
      "المركبة \\(\\gamma\\) تمثل الصيغ التوافقية التي تنتمي لنواة مؤثر لابلابسيان هودج.")

    # 413: Supporting Hyperplane Theorem
    q("KAUST-P3-413", "Convex Optimization", "Medium",
      "Let \\(C \\subset \\mathbb{R}^n\\) be a non-empty convex set and \\(x_0\\) a boundary point of \\(C\\). The Supporting Hyperplane Theorem guarantees the existence of a non-zero vector \\(a \\in \\mathbb{R}^n\\) such that for all \\(x \\in C\\):",
      "لتكن \\(C \\subset \\mathbb{R}^n\\) مجموعة محدبة غير خالية ولتكن \\(x_0\\) نقطة حدودية لـ \\(C\\). تضمن مبرهنة المستوى الفائق المساند وجود متجه غير صفري \\(a \\in \\mathbb{R}^n\\) بحيث يتحقق لكل \\(x \\in C\\):",
      ["\\(a^T x \\le a^T x_0\\)",
       "\\(a^T x = a^T x_0\\)",
       "\\(a^T x > a^T x_0\\)",
       "\\(\\|x - x_0\\| \\ge \\|a\\|\\)"],
      0,
      "The Supporting Hyperplane Theorem states that through any boundary point \\(x_0\\) of a convex set \\(C\\), there exists at least one supporting hyperplane \\(\\{x \\mid a^T x = a^T x_0\\}\\) such that the entire set \\(C\\) lies in one of the closed half-spaces: \\(a^T x \\le a^T x_0\\) for all \\(x \\in C\\).",
      "تنص مبرهنة المستوى الفائق المساند على أنه عند أي نقطة حدودية \\(x_0\\) لمجموعة محدبة \\(C\\)، يوجد مستوى فائق مساند بحيث تقع المجموعة بأكملها في أحد نصفي الفضاء المغلقين: \\(a^T x \\le a^T x_0\\) لجميع \\(x \\in C\\).",
      "All points of the convex set lie entirely on one side of the supporting hyperplane.",
      "تقع جميع نقاط المجموعة المحدبة بالكامل في جهة واحدة من المستوى الفائق المساند.")

    # 414: Subgradient of L1 Norm
    q("KAUST-P3-414", "Convex Optimization", "Hard",
      "Let \\(f(x) = \\|x\\|_1 = \\sum_{i=1}^n |x_i|\\) on \\(\\mathbb{R}^n\\). What is the subdifferential \\(\\partial f(x)\\) at a point \\(x\\)?",
      "لتكن \\(f(x) = \\|x\\|_1 = \\sum_{i=1}^n |x_i|\\) معرفة على \\(\\mathbb{R}^n\\). ما هو التفاضل الجزئي (subdifferential) \\(\\partial f(x)\\) عند نقطة \\(x\\)؟",
      ["\\(\\partial f(x) = \\{g \\in \\mathbb{R}^n \\mid g_i = \\text{sign}(x_i) \\text{ if } x_i \\ne 0, \\text{ and } g_i \\in [-1, 1] \\text{ if } x_i = 0\\}\\)",
       "\\(\\partial f(x) = \\{\\text{sign}(x)\\} \\text{ everywhere}\\)",
       "\\(\\partial f(x) = \\{g \\in \\mathbb{R}^n \\mid \\|g\\|_2 \\le 1\\}\\)",
       "\\(\\partial f(x) = \\emptyset \\text{ whenever } x_i = 0\\)"],
      0,
      "Since \\(f(x) = \\sum_i |x_i|\\) is separable, its subdifferential is the Cartesian product of the subdifferentials of the coordinate absolute values. For each coordinate, \\(\\partial |x_i| = \\{+1\\}\\) if \\(x_i > 0\\), \\(\\{-1\\}\\) if \\(x_i < 0\\), and the entire closed interval \\([-1, 1]\\) if \\(x_i = 0\\).",
      "بما أن دالة المعيار \\(\\ell_1\\) قابلة للفصل مجموعياً، فإن تفاضلها الجزئي هو الجداء الديكارتي للتفاضلات الجزئية للقيمة المطلقة لكل إحداثي. عند الصفر، يكون التفاضل الجزئي هو الفترة المغلقة كاملة \\([-1, 1]\\).",
      "At the origin, the slope of any secant line tangent to the absolute value function lies between -1 and 1.",
      "عند نقطة الأصل، ميل أي مستقيم مساند يقع بين -1 و 1.")

    # 415: Convex Conjugate (Fenchel-Legendre Transform)
    q("KAUST-P3-415", "Convex Optimization", "Hard",
      "The convex conjugate (Fenchel-Legendre transform) of a function \\(f: \\mathbb{R}^n \\to \\mathbb{R}\\) is defined by \\(f^*(y) = \\sup_{x \\in \\mathbb{R}^n} (y^T x - f(x))\\). For the strictly convex quadratic function \\(f(x) = \\frac{1}{2} x^T Q x\\), where \\(Q \\succ 0\\) is symmetric positive definite, what is \\(f^*(y)\\)?",
      "يُعرّف المرافق المحدب (تحويل فنشل-ليجاندر) لدالة \\(f: \\mathbb{R}^n \\to \\mathbb{R}\\) بالعلاقة \\(f^*(y) = \\sup_x (y^T x - f(x))\\). للدالة التربيعية المحدبة تماماً \\(f(x) = \\frac{1}{2} x^T Q x\\)، حيث \\(Q \\succ 0\\) مصفوفة متماثلة موجبة تماماً، ما هي \\(f^*(y)\\)؟",
      ["\\(\\frac{1}{2} y^T Q^{-1} y\\)",
       "\\(\\frac{1}{2} y^T Q y\\)",
       "\\(y^T Q^{-1} y\\)",
       "\\(-\\frac{1}{2} y^T Q^{-1} y\\)"],
      0,
      "To maximize \\(g(x) = y^T x - \\frac{1}{2} x^T Q x\\), we set the gradient to zero: \\(\\nabla_x g(x) = y - Q x = 0 \\implies x^* = Q^{-1} y\\). Substituting back gives \\(f^*(y) = y^T (Q^{-1}y) - \\frac{1}{2}(Q^{-1}y)^T Q (Q^{-1}y) = y^T Q^{-1}y - \\frac{1}{2}y^T Q^{-1}y = \\frac{1}{2} y^T Q^{-1} y\\).",
      "لإيجاد القيمة العظمى، نضع المشتق بالنسبة لـ \\(x\\) مساوياً للصفر: \\(y - Qx = 0 \\implies x^* = Q^{-1}y\\). بالتعويض في الدالة نحصل على \\(f^*(y) = \\frac{1}{2} y^T Q^{-1} y\\).",
      "Maximize with respect to x by differentiating and solving \\(Q x = y\\).",
      "اشتق بالنسبة لـ x وحل المعادلة \\(Qx = y\\) ثم عوض القيمة في الدالة المرافقة.")

    # 416: Slater's Condition and Strong Duality
    q("KAUST-P3-416", "Convex Optimization", "Medium",
      "In convex optimization, Slater's condition is a constraint qualification that guarantees strong duality (zero duality gap: \\(p^* = d^*\\)). For a problem with convex objective \\(f_0(x)\\), convex inequalities \\(f_i(x) \\le 0\\) (\\(i=1,\\dots,m\\)), and affine equalities \\(Ax = b\\), what does Slater's condition require?",
      "في التحسين المحدب، يُعد شرط سلاتر شرطاً للملاءمة يضمن تحقق الثنائية القوية (انعدام فجوة الثنائية: \\(p^* = d^*\\)). لمسألة ذات دالة هدف محدبة ومتباينات محدبة \\(f_i(x) \\le 0\\) ومعادلات خطية \\(Ax = b\\)، ما الذي يتطلبه شرط سلاتر؟",
      ["There exists a strictly feasible point \\(x\\) such that \\(f_i(x) < 0\\) for all non-affine inequalities, and \\(Ax = b\\)",
       "The objective function \\(f_0(x)\\) must be strictly convex",
       "The matrix \\(A\\) must be square and invertible",
       "The optimal value \\(p^*\\) must be strictly positive"],
      0,
      "Slater's constraint qualification requires the existence of at least one point in the relative interior of the feasible set where all non-linear inequality constraints hold with strict inequality: \\(f_i(x) < 0\\) for all \\(i=1,\\dots,m\\), alongside \\(Ax = b\\). This ensures strong duality and the existence of dual optimal multipliers.",
      "يتطلب شرط سلاتر وجود نقطة واحدة على الأقل داخل النطاق النسبي تحقق المتباينات غير الخطية بصرامة: \\(f_i(x) < 0\\) مع تحقيق القيود الخطية \\(Ax = b\\). يضمن هذا الشرط الثنائية القوية وتحقق مضاعفات لاغرانج المثلى.",
      "Look for strict feasibility of the inequality constraints.",
      "ابحث عن شرط الإمكانية الصارمة للمتباينات المحدبة.")

    # 417: KKT Complementary Slackness
    q("KAUST-P3-417", "Convex Optimization", "Hard",
      "Let \\(x^*\\) be a primal optimal solution and \\((\\lambda^*, \\nu^*)\\) dual optimal solutions for a convex problem with inequality constraints \\(f_i(x) \\le 0\\). What does the Karush-Kuhn-Tucker (KKT) complementary slackness condition state?",
      "لتكن \\(x^*\\) حلاً أصلياً أمثلاً و \\((\\lambda^*, \\nu^*)\\) حلولاً ثنائية مثلى لمسألة محدبة ذات قيود تباين \\(f_i(x) \\le 0\\). ما الذي تنص عليه حالة الركود التكاملي (complementary slackness) في شروط KKT؟",
      ["\\(\\lambda_i^* f_i(x^*) = 0\\) for every \\(i = 1, \\dots, m\\)",
       "\\(\\sum_{i=1}^m \\lambda_i^* = 1\\)",
       "\\(\\lambda_i^* + f_i(x^*) = 0\\)",
       "\\(f_i(x^*) = 0\\) for all \\(i\\)"],
      0,
      "Complementary slackness states that \\(\\lambda_i^* f_i(x^*) = 0\\) for each \\(i\\). Since \\(\\lambda_i^* \\ge 0\\) and \\(f_i(x^*) \\le 0\\), this implies that if an inequality constraint is inactive (slack, \\(f_i(x^*) < 0\\)), its multiplier must be zero (\\(\\lambda_i^* = 0\\)); conversely, if \\(\\lambda_i^* > 0\\), the constraint must be active (tight, \\(f_i(x^*) = 0\\)).",
      "ينص شرط الركود التكاملي على أن \\(\\lambda_i^* f_i(x^*) = 0\\) لكل قيد \\(i\\). هذا يعني أنه إذا كان القيد غير نشط (أي \\(f_i(x^*) < 0\\))، فإن المضاعف المرافق له ينعدم حتماً (\\(\\lambda_i^* = 0\\))، وإذا كان المضاعف موجباً، فإن القيد يكون نشطاً تماماً عند الحد (\\(f_i(x^*) = 0\\)).",
      "The product of the Lagrange multiplier and the constraint function value must be zero for each constraint.",
      "جداء مضاعف لاغرانج في قيمة دالة القيد يجب أن يساوي صفراً لكل قيد على حدة.")

    # 418: Proximal Operator Definition
    q("KAUST-P3-418", "Convex Optimization", "Hard",
      "For a closed, proper convex function \\(f: \\mathbb{R}^n \\to \\mathbb{R} \\cup \\{+\\infty\\}\\) and parameter \\(\\gamma > 0\\), how is the proximal operator \\(\\text{prox}_{\\gamma f}(x)\\) defined?",
      "لدالة محدبة ومغلقة ومناسبة \\(f: \\mathbb{R}^n \\to \\mathbb{R} \\cup \\{+\\infty\\}\\) ومعامل \\(\\gamma > 0\\)، كيف يُعرّف المؤثر التقريبي (proximal operator) \\(\\text{prox}_{\\gamma f}(x)\\)؟",
      ["\\(\\text{prox}_{\\gamma f}(x) = \\arg\\min_{z \\in \\mathbb{R}^n} \\left( f(z) + \\frac{1}{2\\gamma} \\|z - x\\|_2^2 \\right)\\)",
       "\\(\\text{prox}_{\\gamma f}(x) = x - \\gamma \\nabla f(x)\\)",
       "\\(\\text{prox}_{\\gamma f}(x) = \\arg\\max_{z \\in \\mathbb{R}^n} \\left( f(z) - \\frac{\\gamma}{2} \\|z - x\\|_2^2 \\right)\\)",
       "\\(\\text{prox}_{\\gamma f}(x) = \\frac{x}{1 + \\gamma f(x)}\\)"],
      0,
      "The proximal operator of \\(\\gamma f\\) balances minimizing \\(f(z)\\) while penalizing deviation from the point \\(x\\) with an isotropic quadratic term: \\(\\text{prox}_{\\gamma f}(x) = \\arg\\min_z \\left(f(z) + \\frac{1}{2\\gamma}\\|z - x\\|_2^2\\right)\\). It is uniquely valued, firmly non-expansive, and equals the resolvent of the subdifferential operator \\((I + \\gamma \\partial f)^{-1}(x)\\).",
      "يوازن المؤثر التقريبي بين تصغير الدالة \\(f(z)\\) وفرض عقوبة تربيعية على الابتعاد عن النقطة \\(x\\): \\(\\arg\\min_z \\left(f(z) + \\frac{1}{2\\gamma}\\|z - x\\|_2^2\\right)\\). وهو محدد بقيمة وحيدة وغير متوسع بإحكام، ويطابق مؤثر الحل للتفاضل الجزئي.",
      "Notice the tradeoff between minimizing \\(f(z)\\) and the Euclidean distance squared from \\(x\\) scaled by \\(1/(2\\gamma)\\).",
      "لاحظ الموازنة بين تصغير f والمحافظة على القرب الإقليدي من x بمقياس 1 على 2 غاما.")

    # 419: Soft-Thresholding Operator with SVG
    svg_soft_thresh = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-60 -60 120 120' width='100%' height='100%' style='background:#0d1117;'>
  <!-- Axes -->
  <line x1='-50' y1='0' x2='50' y2='0' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-50' x2='0' y2='50' stroke='#8b949e' stroke-width='1.5'/>
  <!-- y = x dashed line -->
  <line x1='-45' y1='45' x2='45' y2='-45' stroke='#30363d' stroke-width='1.5' stroke-dasharray='3,3'/>
  <!-- Threshold markers at -lambda and +lambda -->
  <line x1='-20' y1='-3' x2='-20' y2='3' stroke='#f85149' stroke-width='2'/>
  <text x='-20' y='14' fill='#f85149' font-family='sans-serif' font-size='9' text-anchor='middle'>-\\(\\lambda\\)</text>
  <line x1='20' y1='-3' x2='20' y2='3' stroke='#f85149' stroke-width='2'/>
  <text x='20' y='14' fill='#f85149' font-family='sans-serif' font-size='9' text-anchor='middle'>+\\(\\lambda\\)</text>
  <!-- Soft Thresholding curve -->
  <!-- Left branch: x < -20, y = x + 20 -> SVG y is inverted: y_svg = -(x+20) -->
  <line x1='-45' y1='25' x2='-20' y2='0' stroke='#58a6ff' stroke-width='2.5'/>
  <!-- Flat deadzone: [-20, 20], y = 0 -->
  <line x1='-20' y1='0' x2='20' y2='0' stroke='#58a6ff' stroke-width='3.5'/>
  <!-- Right branch: x > 20, y = x - 20 -> SVG y_svg = -(x-20) -->
  <line x1='20' y1='0' x2='45' y2='-25' stroke='#58a6ff' stroke-width='2.5'/>
</svg>"""

    q("KAUST-P3-419", "Convex Optimization", "Hard",
      "The proximal operator of the scaled \\(\\ell_1\\)-norm regularizer \\(g(x) = \\lambda \\|x\\|_1\\) acts elementwise as the soft-thresholding operator \\(\\mathcal{S}_\\lambda(x)\\). What is the explicit formula for \\(\\mathcal{S}_\\lambda(x)\\)?",
      "يعمل المؤثر التقريبي لمنظم معيار \\(\\ell_1\\) المقيس \\(g(x) = \\lambda \\|x\\|_1\\) عنصرياً كمؤثر عتبة لينة \\(\\mathcal{S}_\\lambda(x)\\). ما هي الصيغة الصريحة لـ \\(\\mathcal{S}_\\lambda(x)\\)؟",
      ["\\(\\mathcal{S}_\\lambda(x) = \\text{sign}(x) \\max(|x| - \\lambda, 0)\\)",
       "\\(\\mathcal{S}_\\lambda(x) = x - \\lambda\\)",
       "\\(\\mathcal{S}_\\lambda(x) = \\begin{cases} x & \\text{if } |x| \\ge \\lambda \\\\ 0 & \\text{if } |x| < \\lambda \\end{cases}\\)",
       "\\(\\mathcal{S}_\\lambda(x) = \\frac{x}{1 + \\lambda |x|}\\)"],
      0,
      "Solving \\(\\arg\\min_z (|z| + \\frac{1}{2\\lambda}(z - x)^2)\\) yields the soft-thresholding operator: for \\(|x| \\le \\lambda\\), \\(z = 0\\); for \\(x > \\lambda\\), \\(z = x - \\lambda\\); for \\(x < -\\lambda\\), \\(z = x + \\lambda\\). This is written compactly as \\(\\mathcal{S}_\\lambda(x) = \\text{sign}(x)\\max(|x| - \\lambda, 0)\\). The discontinuous case corresponds to hard thresholding (\\(\\ell_0\\)).",
      "بحل مسألة التصغير التحليلية نحصل على مؤثر العتبة اللينة: عندما يكون \\(|x| \\le \\lambda\\) تنعدم القيمة إلى الصفر، وعندما يكون \\(|x| > \\lambda\\) تنكمش القيمة بمقدار \\(\\lambda\\) نحو الصفر مع الحفاظ على الإشارة: \\(\\text{sign}(x)\\max(|x|-\\lambda, 0)\\).",
      "Values within \\([-\\lambda, \\lambda]\\) are set to zero, and values outside are shifted towards the origin by \\(\\lambda\\).",
      "القيم الواقعة ضمن المجال تُصفر تماماً، وتُسحب القيم الخارجية باتجاه نقطة الأصل بمقدار غاما.")

    # 420: Proximal Gradient Method / ISTA
    q("KAUST-P3-420", "Convex Optimization", "Hard",
      "Consider minimizing \\(F(x) = f(x) + g(x)\\), where \\(f\\) is convex and \\(L\\)-smooth, and \\(g\\) is a convex (possibly non-smooth) regularizer. What is the update rule for the Proximal Gradient Method (ISTA) with step-size \\(\\gamma \\le 1/L\\)?",
      "لتكن مسألة تصغير \\(F(x) = f(x) + g(x)\\)، حيث \\(f\\) دالة محدبة وذات تدرج ملساء بمعامل \\(L\\)، و \\(g\\) دالة تنظيم محدبة (قد تكون غير ملساء). ما هي قاعدة التحديث لطريقة التدرج التقريبي (ISTA) بخطوة \\(\\gamma \\le 1/L\\)؟",
      ["\\(x^{k+1} = \\text{prox}_{\\gamma g}\\left( x^k - \\gamma \\nabla f(x^k) \\right)\\)",
       "\\(x^{k+1} = x^k - \\gamma \\nabla f(x^k) - \\gamma \\nabla g(x^k)\\)",
       "\\(x^{k+1} = \\text{prox}_{\\gamma f}\\left( x^k - \\gamma \\nabla g(x^k) \\right)\\)",
       "\\(x^{k+1} = \\nabla f(x^k) + \\text{prox}_{\\gamma g}(x^k)\\)"],
      0,
      "The proximal gradient method (Forward-Backward splitting) performs a forward explicit gradient step on the smooth part \\(f\\), followed by a backward implicit proximal step on the non-smooth part \\(g\\): \\(x^{k+1} = \\text{prox}_{\\gamma g}(x^k - \\gamma \\nabla f(x^k))\\). It converges at rate \\(\\mathcal{O}(1/k)\\), which accelerates to \\(\\mathcal{O}(1/k^2)\\) under Nesterov acceleration (FISTA).",
      "تنفذ طريقة التدرج التقريبي خطوة تدرج صريحة للأمام على الجزء الأملس \\(f\\)، تليها خطوة تقريبية ضمنية للخلف على الجزء غير الأملس \\(g\\): \\(x^{k+1} = \\text{prox}_{\\gamma g}(x^k - \\gamma \\nabla f(x^k))\\). ويصل معدل تقاربها إلى \\(\\mathcal{O}(1/k)\\) ويتسارع عبر نيفستروف إلى \\(\\mathcal{O}(1/k^2)\\).",
      "First take a standard gradient descent step on f, then apply the prox operator of g to the result.",
      "خذ أولاً خطوة انحدار تدرجي عادية على الدالة الملساء f ثم طبق مؤثر التقريب الخاص بـ g على الناتج.")

    # 421: ADMM Form and Updates
    q("KAUST-P3-421", "Convex Optimization", "Hard",
      "The Alternating Direction Method of Multipliers (ADMM) solves problems of the form \\(\\min_{x, z} f(x) + g(z)\\) subject to \\(Ax + Bz = c\\). In scaled dual form with augmented parameter \\(\\rho > 0\\) and scaled dual variable \\(u\\), what is the dual variable update step?",
      "تحل طريقة الاتجاهات المتناوبة للمضاعفات (ADMM) المسائل ذات الصيغة \\(\\min f(x) + g(z)\\) تحت القيد \\(Ax + Bz = c\\). في الصيغة الثنائية المقيسة بمعامل تعزيز \\(\\rho > 0\\) ومتغير ثنائي مقيس \\(u\\)، ما هي خطوة تحديث المتغير الثنائي؟",
      ["\\(u^{k+1} = u^k + Ax^{k+1} + Bz^{k+1} - c\\)",
       "\\(u^{k+1} = u^k - \\rho (Ax^{k+1} + Bz^{k+1} - c)\\)",
       "\\(u^{k+1} = \\arg\\min_u \\|Ax^{k+1} + Bz^{k+1} - c\\|^2\\)",
       "\\(u^{k+1} = \\frac{1}{\\rho}(Ax^{k+1} + Bz^{k+1})\\)"],
      0,
      "In scaled ADMM, the unscaled multiplier is \\(y = \\rho u\\). The dual ascent step on the augmented Lagrangian is \\(y^{k+1} = y^k + \\rho(Ax^{k+1} + Bz^{k+1} - c)\\). Dividing both sides by \\(\\rho\\) gives the remarkably clean scaled update: \\(u^{k+1} = u^k + r^{k+1}\\), where \\(r^{k+1} = Ax^{k+1} + Bz^{k+1} - c\\) is the primal residual.",
      "في صيغة ADMM المقيسة، يرتبط المضاعف بالمتغير المقيس عبر \\(y = \\rho u\\). خطوة الصعود الثنائي تعطي \\(y^{k+1} = y^k + \\rho r^{k+1}\\). بقسمة الطرفين على \\(\\rho\\) نحصل على التحديث المقيس المباشر: \\(u^{k+1} = u^k + r^{k+1}\\)، حيث \\(r\\) هو الباقي الأصلي للقيد.",
      "The scaled dual update simply accumulates the primal residual into the dual variable.",
      "التحديث الثنائي المقيس يجمع ببساطة المتبقي الأصلي إلى المتغير الثنائي السابق.")

    # 422: Projection onto a Closed Convex Set
    q("KAUST-P3-422", "Convex Optimization", "Medium",
      "Let \\(C\\) be a non-empty closed convex set in \\(\\mathbb{R}^n\\) and \\(\\mathcal{P}_C(x) = \\arg\\min_{z \\in C} \\|z - x\\|_2\\) the Euclidean projection operator. Which fundamental geometric inequality characterizes \\(x^* = \\mathcal{P}_C(x)\\) for all \\(z \\in C\\)?",
      "لتكن \\(C\\) مجموعة محدبة مغلقة وغير خالية في \\(\\mathbb{R}^n\\) ولتكن \\(\\mathcal{P}_C(x)\\) مؤثر الإسقاط الإقليدي. ما هي المتباينة الهندسية الجوهرية التي تميز \\(x^* = \\mathcal{P}_C(x)\\) لجميع \\(z \\in C\\)؟",
      ["\\(\\langle x - x^*, z - x^* \\rangle \\le 0\\)",
       "\\(\\langle x - x^*, z - x^* \\rangle \\ge 0\\)",
       "\\(\\|x - x^*\\| \\le \\|z - x^*\\|\\)",
       "\\(\\langle x^*, z \\rangle = 0\\)"],
      0,
      "The projection \\(x^* = \\mathcal{P}_C(x)\\) is uniquely characterized by the first-order optimality condition for minimizing \\(\\frac{1}{2}\\|z - x\\|^2\\) over \\(C\\): the vector \\(x - x^*\\) forms an obtuse angle (\\(\\ge 90^\\circ\\)) with any displacement vector \\(z - x^*\\) pointing into \\(C\\), yielding \\(\\langle x - x^*, z - x^* \\rangle \\le 0\\) for all \\(z \\in C\\).",
      "يتميز الإسقاط الإقليدي \\(x^* = \\mathcal{P}_C(x)\\) بشرط الأمثلية: يشكل المتجه \\(x - x^*\\) زاوية منفرجة (أكبر من أو تساوي 90 درجة) مع أي متجه إزاحة \\(z - x^*\\) يتجه داخل المجموعة المحدبة، مما يعطي \\(\\langle x - x^*, z - x^* \\rangle \\le 0\\) لجميع \\(z \\in C\\).",
      "The angle between the residual vector \\(x - x^*\\) and any vector pointing into \\(C\\) from \\(x^*\\) is at least 90 degrees.",
      "الزاوية بين متجه الفرق والمتجه المتجه إلى داخل المجموعة من نقطة الإسقاط تكون منفرجة دائماً.")

    # 423: Self-Concordant Functions in Interior Point Methods
    q("KAUST-P3-423", "Convex Optimization", "Hard",
      "In Nesterov and Nemirovski's theory of interior-point polynomial-time algorithms, a convex function \\(f: \\mathbb{R} \\to \\mathbb{R}\\) with \\(f''(x) > 0\\) is called self-concordant with parameter 2 if it satisfies which inequality for all \\(x\\) in its domain?",
      "في نظرية نيستيروف ونيميروفسكي لخوارزميات النقاط الداخلية ذات الزمن كثير الحدود، تُسمى الدالة المحدبة \\(f: \\mathbb{R} \\to \\mathbb{R}\\) ذات المشتق الثاني الموجب متسقة ذاتياً (self-concordant) إذا حققت أي متباينة لجميع \\(x\\) في نطاقها؟",
      ["\\(|f'''(x)| \\le 2 (f''(x))^{3/2}\\)",
       "\\(|f'''(x)| \\le 2 f''(x)\\)",
       "\\(f''(x) \\ge 2 |f'(x)|^2\\)",
       "\\(|f''(x)| \\le 2 (f'(x))^{3/2}\\)"],
      0,
      "A three-times continuously differentiable convex function is standard self-concordant if \\(|f'''(x)| \\le 2 (f''(x))^{3/2}\\). The canonical barrier \\(f(x) = -\\log x\\) satisfies this with equality: \\(f''(x) = 1/x^2\\) and \\(f'''(x) = -2/x^3\\), so \\(|f'''(x)| = 2 (f''(x))^{3/2}\\). Self-concordance ensures affine invariance of Newton's method and guarantees polynomial-time convergence.",
      "تُعرف الدالة المحدبة بأنها متسقة ذاتياً إذا كان مشتقها الثالث محصوراً بالمشتق الثاني وفق \\(|f'''(x)| \\le 2 (f''(x))^{3/2}\\). تحقق دالة الحاجز اللوغاريتمي \\(-\\log x\\) هذه المتباينة بتطابق تام. تضمن هذه الخاصية الثبات التآلفي لطريقة نيوتن وتضمن تقاربها في زمن كثير حدود.",
      "Test the canonical logarithmic barrier function \\(f(x) = -\\log x\\).",
      "اختبر دالة الحاجز اللوغاريتمي الشهيرة \\(-\\log x\\) ومشتقاتها المتتالية.")

    # 424: Newton Decrement and Affine Invariance
    q("KAUST-P3-424", "Convex Optimization", "Hard",
      "For a strictly convex twice-differentiable function \\(f\\), the Newton decrement \\(\\lambda(x) = \\sqrt{\\nabla f(x)^T (\\nabla^2 f(x))^{-1} \\nabla f(x)}\\) provides an affine-invariant stopping criterion. What is the relationship between \\(\\frac{1}{2}\\lambda(x)^2\\) and the quadratic model approximation \\(\\Delta x_{\\text{nt}} = -(\\nabla^2 f(x))^{-1} \\nabla f(x)\\)?",
      "لدالة محدبة تماماً وقابلة للاشتقاق مرتين، يوفر مؤشر تناقص نيوتن \\(\\lambda(x) = \\sqrt{\\nabla f(x)^T (\\nabla^2 f(x))^{-1} \\nabla f(x)}\\) معيار إيقاف ثابتاً تآلفياً. ما هي العلاقة بين \\(\\frac{1}{2}\\lambda(x)^2\\) وتناقص النموذج التربيعي لخطوة نيوتن؟",
      ["\\(f(x) - \\inf_v \\left( f(x) + \\nabla f(x)^T v + \\frac{1}{2} v^T \\nabla^2 f(x) v \\right) = \\frac{1}{2}\\lambda(x)^2\\)",
       "\\(\\lambda(x)^2 = \\|\\nabla f(x)\\|_2^2\\)",
       "\\(\\frac{1}{2}\\lambda(x)^2 = f(x) - f(x^*)\\) exactly for non-quadratic functions",
       "\\(\\lambda(x) = 0\\) if and only if \\(x = 0\\)"],
      0,
      "The Newton decrement squared \\(\\lambda(x)^2 = -\\nabla f(x)^T \\Delta x_{\\text{nt}}\\) measures the exact predicted decrease in the second-order Taylor expansion of \\(f\\) when taking the full Newton step: \\(\\widehat{f}(x) - \\widehat{f}(x + \\Delta x_{\\text{nt}}) = \\frac{1}{2}\\lambda(x)^2\\). Moreover, \\(\\frac{1}{2}\\lambda(x)^2\\) bounds the suboptimality gap \\(f(x) - p^* \\le \\lambda(x)^2\\) in the quadratic convergence phase.",
      "يقيس مربع مؤشر تناقص نيوتن \\(\\frac{1}{2}\\lambda(x)^2\\) بالضبط مقدار الانخفاض المتوقع في منشور تايلور من الرتبة الثانية عند اتخاذ خطوة نيوتن كاملة. كما أنه يحدد حداً أعلى لفجوة الأمثلية \\(f(x) - p^*\\) أثناء مرحلة التقارب التربيعي الفائق.",
      "The Newton decrement measures the decrease in the quadratic approximation of f along the Newton step.",
      "يقيس مؤشر تناقص نيوتن مقدار الانخفاض في التقريب التربيعي للدالة على طول خطوة نيوتن.")

    # 425: Central Path in Primal-Dual Interior-Point Methods
    q("KAUST-P3-425", "Convex Optimization", "Hard",
      "In primal-dual interior-point methods for linear programming \\(\\min c^T x\\) s.t. \\(Ax = b, x \\ge 0\\), the central path \\(x(\\mu), s(\\mu)\\) parametrized by the barrier parameter \\(\\mu > 0\\) relaxes the complementary slackness condition \\(x_i s_i = 0\\) to which condition for all \\(i = 1, \\dots, n\\)?",
      "في خوارزميات النقاط الداخلية الثنائية-الأصلية للبرمجة الخطية، يحل المسار المركزي \\(x(\\mu), s(\\mu)\\) محل شرط الركود التكاملي \\(x_i s_i = 0\\) بأي شرط مخفف لكل \\(i = 1, \\dots, n\\) بمعامل الحاجز \\(\\mu > 0\\)؟",
      ["\\(x_i s_i = \\mu\\)",
       "\\(x_i + s_i = \\mu\\)",
       "\\(x_i / s_i = \\mu\\)",
       "\\(x_i s_i = \\mu^2\\)"],
      0,
      "The central path is the trajectory of solutions satisfying primal feasibility \\(Ax = b, x > 0\\), dual feasibility \\(A^T y + s = c, s > 0\\), and the relaxed complementarity equations \\(x_i s_i = \\mu\\) for all \\(i\\). As the barrier parameter \\(\\mu \\to 0^+\\), the central path converges smoothly to an optimal primal-dual solution pair \\((x^*, s^*)\\).",
      "المسار المركزي هو المسار المحقق لشروط الإمكانية الأصلية والثنائية مع استبدال شرط الركود التكاملي بالمعادلات المخففة \\(x_i s_i = \\mu\\). مع اقتراب معامل الحاجز \\(\\mu \\to 0^+\\)، يتقارب المسار المركزي بسلاسة نحو نقطة الحل الأمثل المشتركة.",
      "The pairwise coordinate products of primal and slack variables are set uniformly equal to \\(\\mu\\).",
      "توضع جذاءات الإحداثيات للمتغيرات الأصلية والراكدة متساوية بانتظام للقيمة الموجبة ميو.")

    # 426: Whittaker-Shannon Sampling Theorem
    q("KAUST-P3-426", "Applied Mathematics & Signal Processing", "Medium",
      "According to the Nyquist-Shannon sampling theorem, a continuous signal \\(f(t)\\) bandlimited to frequencies \\(|\\omega| \\le \\Omega_B\\) can be perfectly reconstructed from its discrete samples \\(f(n T_s)\\) via sinc interpolation if the sampling interval satisfies \\(T_s \\le \\frac{\\pi}{\\Omega_B}\\). What is the Whittaker-Shannon interpolation formula?",
      "وفقاً لمبرهنة نايكويست-شانون للاعتيان، يمكن استرجاع إشارة مستمرة \\(f(t)\\) ذات نطاق ترددي محدود \\(|\\omega| \\le \\Omega_B\\) استرجاعاً تاماً من عيناتها المتقطعة عبر استيفاء دالة sinc إذا تحقق \\(T_s \\le \\frac{\\pi}{\\Omega_B}\\). ما هي صيغة ويتاكر-شانون للاستيفاء؟",
      ["\\(f(t) = \\sum_{n=-\\infty}^{\\infty} f(n T_s) \\frac{\\sin(\\pi (t - n T_s)/T_s)}{\\pi (t - n T_s)/T_s}\\)",
       "\\(f(t) = \\sum_{n=-\\infty}^{\\infty} f(n T_s) e^{-i 2\\pi n t / T_s}\\)",
       "\\(f(t) = \\sum_{n=-\\infty}^{\\infty} f(n T_s) \\cos\\left(\\frac{\\pi (t - n T_s)}{T_s}\\right)\\)",
       "\\(f(t) = \\frac{1}{T_s} \\sum_{n=-\\infty}^{\\infty} f(n T_s) (t - n T_s)\\)"],
      0,
      "The Whittaker-Shannon interpolation formula represents the convolution of the sampled signal with the impulse response of an ideal brick-wall lowpass filter (the normalized sinc kernel): \\(f(t) = \\sum_n f(n T_s) \\text{sinc}\\left(\\frac{t - n T_s}{T_s}\\right) = \\sum_n f(n T_s) \\frac{\\sin(\\pi(t - nT_s)/T_s)}{\\pi(t - nT_s)/T_s}\\).",
      "تمثل صيغة ويتاكر-شانون التفاف الإشارة المعينة مع الاستجابة النبضية لمرشح الترددات المنخفضة المثالي (دالة sinc): \\(f(t) = \\sum_n f(n T_s) \\text{sinc}\\left(\\frac{t - nT_s}{T_s}\\right)\\)، مما يضمن الاستعادة المثالية دون أي فقدان للمعلومات.",
      "The reconstruction kernel is the sinc function \\(\\text{sinc}(u) = \\frac{\\sin(\\pi u)}{\\pi u}\\).",
      "دالة إعادة البناء هي دالة الجيب التوافقي sinc المعيارية.")

    # 427: Heisenberg-Gabor Uncertainty Principle
    q("KAUST-P3-427", "Applied Mathematics & Signal Processing", "Hard",
      "Let \\(f \\in L^2(\\mathbb{R})\\) with \\(\\|f\\|_2 = 1\\), and let \\(\\sigma_t^2 = \\int_{-\\infty}^\\infty (t - \\mu_t)^2 |f(t)|^2 \\, dt\\) and \\(\\sigma_\\omega^2 = \\int_{-\\infty}^\\infty (\\omega - \\mu_\\omega)^2 |\\widehat{f}(\\omega)|^2 \\, d\\omega\\) denote the time and frequency variances. What is the lower bound given by the Heisenberg-Gabor uncertainty principle, and for which signals is this bound attained?",
      "لتكن \\(f \\in L^2(\\mathbb{R})\\) إشارة معيرة بـ \\(\\|f\\|_2 = 1\\)، ولتكن \\(\\sigma_t^2\\) و \\(\\sigma_\\omega^2\\) تبايني الوقت والتردد. ما هو الحد الأدنى المعطى بمبدأ عدم اليقين لهايزنبرغ-غابور، ولأي إشارات يتحقق هذا الحد الأدنى؟",
      ["\\(\\sigma_t \\sigma_\\omega \\ge \\frac{1}{2}\\), attained uniquely by Gaussian wave packets \\(f(t) = C e^{-\\alpha t^2 + i \\omega_0 t}\\)",
       "\\(\\sigma_t \\sigma_\\omega \\ge 1\\), attained by rectangular pulses",
       "\\(\\sigma_t \\sigma_\\omega \\ge \\frac{1}{4\\pi}\\), attained by sine waves",
       "\\(\\sigma_t \\sigma_\\omega \\ge 0\\), attained by Dirac delta functions"],
      0,
      "The Heisenberg-Gabor uncertainty inequality states that \\(\\sigma_t \\sigma_\\omega \\ge \\frac{1}{2}\\). In quantum mechanics (with \\(p = \\hbar \\omega\\)), this is Heisenberg's relation \\(\\Delta x \\Delta p \\ge \\frac{\\hbar}{2}\\). Equality holds if and only if the Cauchy-Schwarz bound is tight, which occurs uniquely for complex Gaussian wave packets.",
      "ينص مبدأ عدم اليقين لهايزنبرغ-غابور في معالجة الإشارات على أن \\(\\sigma_t \\sigma_\\omega \\ge 1/2\\). وتتحقق المساواة الدقيقة حصرياً لحزم الموجات الغاوسية \\(e^{-\\alpha t^2}\\)، والتي تحقق أدنى حاصل ضرب لانتشار الوقت والتردد.",
      "Gaussian wave packets are the unique minimizers of the time-bandwidth product.",
      "الحزم الموجية الغاوسية هي الدوال الفريدة التي تحقق الحد الأدنى لضرب انتشار الزمن والتردد.")

    # 428: Multiresolution Analysis (MRA) Dilation Equation
    q("KAUST-P3-428", "Applied Mathematics & Signal Processing", "Hard",
      "In Mallat's Multiresolution Analysis (MRA) for wavelets, the scaling function \\(\\phi(t)\\) satisfies the two-scale dilation equation \\(\\phi(t) = \\sqrt{2} \\sum_{k=-\\infty}^\\infty h_k \\phi(2t - k)\\). How is the corresponding mother wavelet \\(\\psi(t)\\) constructed from \\(\\phi(t)\\) and the conjugate mirror filter coefficients \\(h_k\\)?",
      "في التحليل متعدد الدقة (MRA) لمويجات مالات، تحقق دالة التدريج \\(\\phi(t)\\) معادلة التمدد ثنائية المقياس \\(\\phi(t) = \\sqrt{2} \\sum_k h_k \\phi(2t - k)\\). كيف تُبنى المويجة الأم المقابلة \\(\\psi(t)\\) من دالة التدريج ومعاملات المرشح \\(h_k\\)؟",
      ["\\(\\psi(t) = \\sqrt{2} \\sum_{k=-\\infty}^\\infty (-1)^k h_{1-k} \\phi(2t - k)\\)",
       "\\(\\psi(t) = \\sqrt{2} \\sum_{k=-\\infty}^\\infty h_k \\phi(2t - k)\\)",
       "\\(\\psi(t) = \\frac{d}{dt} \\phi(t)\\)",
       "\\(\\psi(t) = \\sum_{k=-\\infty}^\\infty h_k^2 \\phi(t - k)\\)"],
      0,
      "The mother wavelet \\(\\psi(t)\\) spans the orthogonal complement detail space \\(W_0 = V_1 \\ominus V_0\\). Orthogonality requires the highpass wavelet filter \\(g_k\\) to be the quadrature mirror filter of the lowpass scaling filter \\(h_k\\): \\(g_k = (-1)^k h_{1-k}\\), giving \\(\\psi(t) = \\sqrt{2} \\sum_k (-1)^k h_{1-k} \\phi(2t - k)\\).",
      "تولد المويجة الأم \\(\\psi(t)\\) الفضاء المكمل المتعامد للتفاصيل \\(W_0\\). يتطلب التعامد أن يكون مرشح المويجة \\(g_k\\) هو المرشح المتطابق الرباعي لمرشح التدريج \\(h_k\\): \\(g_k = (-1)^k h_{1-k}\\)، مما يعطي صيغة المويجة الأم الشهيرة بالتناوب في الإشارات.",
      "The highpass wavelet coefficients alternate signs and reverse the index of the lowpass scaling filter.",
      "تتناوب إشارات معاملات مرشح المويجة عالي التردد وتعكس ترتيب معاملات مرشح التدريج.")

    # 429: Compressed Sensing and Restricted Isometry Property
    q("KAUST-P3-429", "Applied Mathematics & Signal Processing", "Hard",
      "In compressed sensing (Candès, Romberg, Tao, Donoho), an \\(m \\times n\\) sensing matrix \\(A\\) satisfies the Restricted Isometry Property (RIP) of order \\(s\\) with constant \\(\\delta_s \\in (0, 1)\\) if for all \\(s\\)-sparse vectors \\(x\\):",
      "في الاستشعار المضغوط، تحقق مصفوفة الاستشعار \\(A\\) ذات القياس \\(m \\times n\\) خاصية التساوي القياسي المقيد (RIP) من الرتبة \\(s\\) مع ثابت \\(\\delta_s \\in (0, 1)\\) إذا تحقق لجميع المتجهات \\(s\\)-شحيحة \\(x\\):",
      ["\\((1 - \\delta_s) \\|x\\|_2^2 \\le \\|Ax\\|_2^2 \\le (1 + \\delta_s) \\|x\\|_2^2\\)",
       "\\(\\|Ax\\|_1 = \\|x\\|_1\\)",
       "\\(\\det(A^T A) = 1 \\pm \\delta_s\\)",
       "\\(\\|Ax - x\\|_2 \\le \\delta_s\\)"],
      0,
      "The Restricted Isometry Property (RIP) requires that the sensing matrix \\(A\\) acts as an approximate isometry on the subset of all \\(s\\)-sparse vectors: \\((1 - \\delta_s)\\|x\\|_2^2 \\le \\|Ax\\|_2^2 \\le (1 + \\delta_s)\\|x\\|_2^2\\). If \\(\\delta_{2s} < \\sqrt{2} - 1\\), then \\(\\ell_1\\)-minimization (basis pursuit) is guaranteed to recover the exact sparse signal \\(x\\) from only \\(m = \\mathcal{O}(s \\log(n/s))\\) measurements.",
      "تتطلب خاصية التساوي القياسي المقيد أن تحافظ مصفوفة القياس تقريباً على الطاقة الإقليدية لجميع المتجهات الشحيحة (التي تحتوي على \\(s\\) عناصر غير صفرية على الأكثر). يضمن هذا الشرط استرجاع الإشارة الشحيحة بدقة تامة باستخدام الاستمثال القائم على معيار \\(\\ell_1\\).",
      "RIP guarantees that the sensing matrix approximately preserves the Euclidean norm of all sparse vectors.",
      "تضمن خاصية RIP الحفاظ التقريبي على المعيار الإقليدي لجميع المتجهات الشحيحة.")

    # 430: Nuclear Norm Minimization for Matrix Completion
    q("KAUST-P3-430", "Applied Mathematics & Signal Processing", "Hard",
      "In low-rank matrix completion and robust PCA (Candès & Recht), the rank function \\(\\text{rank}(X)\\) is non-convex. What is the tightest convex relaxation of the rank function on the unit spectral norm ball \\(\\{X \\mid \\|X\\| \\le 1\\}\\)?",
      "في استكمال المصفوفات ذات الرتبة المنخفضة، تكون دالة الرتبة \\(\\text{rank}(X)\\) غير محدبة. ما هو أدق تخفيف محدب (convex relaxation) لدالة الرتبة على كرة المعيار الطيفي؟",
      ["The nuclear (trace) norm \\(\\|X\\|_* = \\sum_{i=1}^r \\sigma_i(X)\\)",
       "The Frobenius norm \\(\\|X\\|_F = \\sqrt{\\sum_{i,j} X_{ij}^2}\\)",
       "The operator norm \\(\\|X\\|_2 = \\sigma_{\\max}(X)\\)",
       "The trace \\(\\text{tr}(X)\\)"],
      0,
      "The nuclear norm \\(\\|X\\|_* = \\sum_i \\sigma_i(X)\\) (the sum of the singular values of \\(X\\)) is the convex envelope (the tightest convex lower bound) of the rank function on the set \\(\\{X \\mid \\|X\\| \\le 1\\}\\), in exact analogy to how the \\(\\ell_1\\)-norm is the convex envelope of the \\(\\ell_0\\) sparsity counting function on the \\(\\ell_\\infty\\) ball.",
      "المعيار النووي \\(\\|X\\|_* = \\sum \\sigma_i(X)\\) (مجموع القيم الشاذة للمصفوفة) هو الغلاف المحدب الأدق لدالة الرتبة على كرة المعيار الطيفي، بنفس الطريقة التي يشكل بها معيار \\(\\ell_1\\) الغلاف المحدب لعدد العناصر غير الصفرية \\(\\ell_0\\).",
      "The nuclear norm sums all the singular values of the matrix.",
      "المعيار النووي يجمع القيم الشاذة للمصفوفة وهو النظير المحدب لرتبة المصفوفة.")

    # 431: Kantorovich Relaxation of Optimal Transport
    q("KAUST-P3-431", "Optimal Transport", "Hard",
      "In Monge's original optimal transport problem, one seeks a transport map \\(T: X \\to Y\\) pushing \\(\\mu\\) to \\(\\nu\\) minimizing \\(\\int c(x, T(x)) \\, d\\mu(x)\\). Why did Leonid Kantorovich relax this problem to finding a joint probability measure \\(\\gamma \\in \\mathcal{P}(X \\times Y)\\)?",
      "في مسألة مونج الأصلية للنقل الأمثل، يُبحث عن تطبيق نقل \\(T: X \\to Y\\) ينقل \\(\\mu\\) إلى \\(\\nu\\). لماذا خفف ليونيد كانتوروفيتش هذه المسألة إلى البحث عن قياس احتمالي مشترك \\(\\gamma \\in \\mathcal{P}(X \\times Y)\\)؟",
      ["Because Monge's problem is non-convex and may have no solution (e.g., splitting a Dirac mass), whereas Kantorovich's formulation is a convex linear program that always has a solution",
       "Because Kantorovich wanted to enforce that mass could never be divided",
       "Because Monge's cost function was restricted to strictly negative costs",
       "Because the joint transport plan \\(\\gamma\\) is always guaranteed to be a deterministic function"],
      0,
      "Monge's formulation requires deterministic transport \\(T\\), which cannot split mass (for instance, moving a single Dirac mass \\(\\delta_0\\) to \\(\\frac{1}{2}\\delta_{-1} + \\frac{1}{2}\\delta_1\\) has no Monge solution). Kantorovich relaxed this by allowing mass splitting via coupling measures \\(\\gamma \\in \\Pi(\\mu, \\nu)\\), transforming the problem into an infinite-dimensional convex linear program where existence of minimizers is guaranteed by Prokhorov's theorem.",
      "تتطلب صياغة مونج نقلاً حتمياً لا يمكنه تجزئة الكتلة (مثلاً نقل كتلة ديراك مفردة إلى نقطتين مختلفتين غير ممكن بمونج). خفف كانتوروفيتش المسألة بالسماح بتجزئة الكتل عبر قياسات الاقتران المشترك \\(\\gamma\\)، محولاً إياها إلى مسألة برمجة خطية محدبة ومضمونة الحلول.",
      "Kantorovich allows mass to be split, turning a difficult non-linear problem into a linear programming problem.",
      "سمح كانتوروفيتش بتجزئة الكتلة مما حول مسألة مونج الصعبة إلى مسألة برمجة خطية ذات حل مضمون دائماً.")

    # 432: 1-Wasserstein Distance and Kantorovich-Rubinstein Duality
    q("KAUST-P3-432", "Optimal Transport", "Hard",
      "For probability measures \\(\\mu, \\nu\\) on \\(\\mathbb{R}^d\\), the Kantorovich-Rubinstein duality theorem expresses the 1-Wasserstein (Earth Mover's) distance \\(W_1(\\mu, \\nu)\\) as which dual supremum?",
      "لقياسات الاحتمال \\(\\mu, \\nu\\) على \\(\\mathbb{R}^d\\)، تعبر مبرهنة ثنائية كانتوروفيتش-روبنشتاين عن مسافة فاسرشتاين الأولى \\(W_1(\\mu, \\nu)\\) كأي حد أعلى ثنائي؟",
      ["\\(W_1(\\mu, \\nu) = \\sup_{\\|f\\|_{\\text{Lip}} \\le 1} \\left( \\int_{\\mathbb{R}^d} f(x) \\, d\\mu(x) - \\int_{\\mathbb{R}^d} f(y) \\, d\\nu(y) \\right)\\)",
       "\\(W_1(\\mu, \\nu) = \\sup_{\\|f\\|_\\infty \\le 1} \\left( \\int f \\, d\\mu - \\int f \\, d\\nu \\right)\\)",
       "\\(W_1(\\mu, \\nu) = \\int |\\mu(x) - \\nu(x)| \\, dx\\)",
       "\\(W_1(\\mu, \\nu) = \\inf_{T} \\int \\|x - T(x)\\|_2^2 \\, d\\mu(x)\\)"],
      0,
      "The Kantorovich-Rubinstein theorem establishes that for the cost \\(c(x,y) = \\|x-y\\|\\), the dual problem reduces to maximizing \\(\\int f \\, d\\mu - \\int f \\, d\\nu\\) over all 1-Lipschitz functions \\(\\|f\\|_{\\text{Lip}} \\le 1\\). This formulation is the theoretical foundation of Wasserstein GANs (WGANs), where a neural network critic enforces the 1-Lipschitz condition.",
      "تثبت ثنائية كانتوروفيتش-روبنشتاين أنه عند استخدام المسافة الإقليدية كتكلفة، تُختزل المسألة الثنائية إلى إيجاد الحد الأعلى لفرق التوقعات للدوال التي تحقق شرط ليبشيتز بثابت 1: \\(\\|f\\|_{\\text{Lip}} \\le 1\\). هذه الصيغة هي الأساس الرياضي لشبكات فاسرشتاين التوليدية WGAN.",
      "The supremum is taken over all functions whose Lipschitz constant is at most 1.",
      "يؤخذ الحد الأعلى على جميع الدوال التي لا يتجاوز ثابت ليبشيتز الخاص بها الواحد الصحيح.")

    # 433: Brenier's Polar Factorization Theorem
    q("KAUST-P3-433", "Optimal Transport", "Hard",
      "Let \\(\\mu\\) and \\(\\nu\\) be probability measures on \\(\\mathbb{R}^d\\) with finite second moments, and assume \\(\\mu\\) is absolutely continuous with respect to Lebesgue measure. Brenier's Theorem (1991) asserts that for the quadratic cost \\(c(x,y) = \\frac{1}{2}\\|x-y\\|^2\\), the unique optimal transport map \\(T\\) pushing \\(\\mu\\) to \\(\\nu\\) is given by:",
      "لتكن \\(\\mu\\) و \\(\\nu\\) قياسات احتمال على \\(\\mathbb{R}^d\\) ذات عزوم ثانية منتهية، ولتكن \\(\\mu\\) متصلة مطلقاً بالنسبة لقياس ليبيغ. تؤكد مبرهنة برينيه (1991) أنه لتكلفة النقل التربيعية \\(c(x,y) = \\frac{1}{2}\\|x-y\\|^2\\)، فإن تطبيق النقل الأمثل الوحيد \\(T\\) معطى بواسطة:",
      ["\\(T = \\nabla \\phi\\), the gradient of a convex function \\(\\phi: \\mathbb{R}^d \\to \\mathbb{R}\\)",
       "\\(T = -\\nabla \\phi\\), where \\(\\phi\\) is strictly concave",
       "\\(T = R x\\), where \\(R\\) is an orthogonal rotation matrix",
       "\\(T = \\Delta \\phi\\), the Laplacian of a harmonic potential"],
      0,
      "Yann Brenier proved that the unique quadratic optimal transport map is the gradient of a convex function \\(T = \\nabla \\phi\\). The Jacobian \\(DT = D^2 \\phi\\) is symmetric positive semidefinite almost everywhere, ensuring that trajectories do not cross. Furthermore, \\(\\phi\\) satisfies the Monge-Ampère equation \\(\\det(D^2 \\phi(x)) = \\frac{\\mu(x)}{\\nu(\\nabla \\phi(x))}\\).",
      "أثبت يان برينيه أن تطبيق النقل التربيعي الأمثل الوحيد هو تدرج دالة محدبة \\(T = \\nabla \\phi\\). مصفوفة ياكوبي لهذا التطبيق هي مصفوفة هيسيان \\(D^2\\phi\\) وهي موجبة شبه معينة مما يمنع تقاطع مسارات النقل، وتحقق الدالة \\(\\phi\\) معادلة مونج-أمبير غير الخطية الشهيرة.",
      "The optimal map is the gradient of a convex scalar potential.",
      "تطبيق النقل الأمثل هو تدرج جهد عددي محدب.")

    # 434: Sinkhorn's Algorithm for Entropic Optimal Transport
    q("KAUST-P3-434", "Optimal Transport", "Hard",
      "Entropic regularization of optimal transport adds an entropy penalty \\(\\epsilon H(\\gamma) = \\epsilon \\sum_{i,j} \\gamma_{ij} (\\log \\gamma_{ij} - 1)\\) to the linear cost \\(\\langle C, \\gamma \\rangle\\). What form does the optimal regularized coupling matrix \\(\\gamma^*\\) take, allowing it to be solved via Sinkhorn matrix scaling?",
      "يضيف التنظيم الإنتروبي للنقل الأمثل عقوبة إنتروبيا \\(\\epsilon H(\\gamma)\\) إلى التكلفة الخطية. ما هو الشكل الذي تتخذه مصفوفة الاقتران المنظمة المثلى \\(\\gamma^*\\)، مما يسمح بحلها عبر خوارزمية سينكهورن لتقييس المصفوفات؟",
      ["\\(\\gamma^* = \\text{diag}(u) K \\text{diag}(v)\\), where \\(K_{ij} = e^{-C_{ij}/\\epsilon}\\)",
       "\\(\\gamma^* = C + \\epsilon (u v^T)\\)",
       "\\(\\gamma^* = K^{-1}\\)",
       "\\(\\gamma^* = \\text{diag}(u) + \\text{diag}(v) - K\\)"],
      0,
      "The first-order optimality condition for the strictly convex entropic problem yields \\(\\log \\gamma_{ij}^* = \\frac{\\alpha_i + \\beta_j - C_{ij}}{\\epsilon}\\), meaning \\(\\gamma_{ij}^* = e^{\\alpha_i/\\epsilon} e^{-C_{ij}/\\epsilon} e^{\\beta_j/\\epsilon} = u_i K_{ij} v_j\\). Hence \\(\\gamma^* = \\text{diag}(u) K \\text{diag}(v)\\) with Gibbs kernel \\(K = e^{-C/\\epsilon}\\). Sinkhorn's algorithm iteratively alternates updating \\(u = a ./ (Kv)\\) and \\(v = b ./ (K^T u)\\).",
      "شرط الأمثلية لمسألة الإنتروبيا يعطي التفكيك الأسي \\(\\gamma_{ij}^* = u_i K_{ij} v_j\\)، حيث \\(K_{ij} = e^{-C_{ij}/\\epsilon}\\) هي نواة غيبس. بالتالي \\(\\gamma^* = \\text{diag}(u) K \\text{diag}(v)\\)، وتقوم خوارزمية سينكهورن بتحديث المتجهين \\(u\\) و \\(v\\) بالتناوب عبر ضرب مصفوفات سريع للغاية.",
      "The optimal plan is a diagonal scaling of the Gibbs kernel \\(K = e^{-C/\\epsilon}\\).",
      "المصفوفة المثلى هي تقييس قطري لنواة غيبس الأسية.")

    # 435: Eckart-Young-Mirsky Theorem
    q("KAUST-P3-435", "Applied Mathematics & Linear Algebra", "Medium",
      "Let \\(A \\in \\mathbb{R}^{m \\times n}\\) have singular value decomposition \\(A = \\sum_{i=1}^r \\sigma_i u_i v_i^T\\) with \\(\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge \\sigma_r > 0\\). According to the Eckart-Young-Mirsky Theorem, what is the best rank-\\(k\\) approximation \\(A_k\\) minimizing \\(\\|A - B\\|_F\\), and what is the resulting minimal Frobenius error?",
      "لتكن \\(A\\) مصفوفة ذات تفكيك قيم شاذة \\(A = \\sum_{i=1}^r \\sigma_i u_i v_i^T\\). وفقاً لمبرهنة إيكارت-يونغ-ميرسكي، ما هو أفضل تقريب من الرتبة \\(k\\) الذي يصغر خطأ فروبينيوس \\(\\|A - B\\|_F\\)، وما هو الخطأ الأصغري الناتج؟",
      ["\\(A_k = \\sum_{i=1}^k \\sigma_i u_i v_i^T\\) with error \\(\\sqrt{\\sum_{i=k+1}^r \\sigma_i^2}\\)",
       "\\(A_k = \\sum_{i=1}^k u_i v_i^T\\) with error \\(\\sum_{i=k+1}^r \\sigma_i\\)",
       "\\(A_k = \\sum_{i=k+1}^r \\sigma_i u_i v_i^T\\) with error \\(\\sigma_{k+1}\\)",
       "\\(A_k = \\frac{k}{r} A\\) with error \\(0\\)"],
      0,
      "The Eckart-Young-Mirsky theorem establishes that truncating the SVD at the top \\(k\\) components gives the globally optimal rank-\\(k\\) approximation for both the spectral and Frobenius norms. In the Frobenius norm, the residual error equals the Euclidean norm of the discarded singular values: \\(\\|A - A_k\\|_F = \\sqrt{\\sum_{i=k+1}^r \\sigma_i^2}\\).",
      "تثبت مبرهنة إيكارت-يونغ-ميرسكي أن بتر تفكيك القيم الشاذة عند أول \\(k\\) مركبات يعطي أفضل تقريب من الرتبة \\(k\\) بالنسبة لمعيار فروبينيوس والمعيار الطيفي. ويساوي خطأ فروبينيوس المتبقي الجذر التربيعي لمجموع مربعات القيم الشاذة المهملة.",
      "Truncate the SVD sum to the first k terms; the Frobenius norm error squared is the sum of squares of the omitted singular values.",
      "اقطع مجموع القيم الشاذة عند أول k حدود، ويكون مربع خطأ فروبينيوس هو مجموع مربعات القيم المهملة.")

    # 436: Kernel PCA and Mercer's Theorem
    q("KAUST-P3-436", "Applied Mathematics & Machine Learning", "Hard",
      "In Kernel Principal Component Analysis (Schölkopf, Smola, Müller), a non-linear mapping \\(\\Phi(x)\\) maps input points into a reproducing kernel Hilbert space (RKHS) with Mercer kernel \\(k(x, y) = \\langle \\Phi(x), \\Phi(y) \\rangle\\). For a centered kernel Gram matrix \\(K\\), how are the principal component projections obtained?",
      "في تحليل المركبات الرئيسية النواتي (Kernel PCA)، ينقل تطبيق غير خطي \\(\\Phi(x)\\) البيانات إلى فضاء هلبرت ذي النواة المعيدة (RKHS) مع نواة ميرسر \\(k(x, y)\\). لمصفوفة غرام النواتية المركزية \\(K\\)، كيف نحصل على مساقط المركبات الرئيسية؟",
      ["By solving the matrix eigenvalue problem \\(K \\boldsymbol{\\alpha} = \\lambda \\boldsymbol{\\alpha}\\) and normalizing \\(\\boldsymbol{\\alpha}\\) such that \\(\\lambda \\|\\boldsymbol{\\alpha}\\|_2^2 = 1\\)",
       "By computing the inverse \\(K^{-1}\\)",
       "By running standard linear PCA directly on the raw coordinates without centering",
       "By computing the trace \\(\\text{tr}(K)\\)"],
      0,
      "Kernel PCA replaces the explicit covariance matrix in feature space with the \\(N \\times N\\) kernel matrix \\(K\\). The eigenvalue problem \\(C v = \\lambda v\\) transforms into \\(K \\boldsymbol{\\alpha} = \\lambda \\boldsymbol{\\alpha}\\). Because the eigenvector \\(v\\) in RKHS satisfies \\(v = \\sum_{i=1}^N \\alpha_i \\Phi(x_i)\\), the normalization \\(\\|v\\|^2 = 1\\) requires \\(v^T v = \\boldsymbol{\\alpha}^T K \\boldsymbol{\\alpha} = \\lambda \\boldsymbol{\\alpha}^T \\boldsymbol{\\alpha} = 1\\), hence \\(\\lambda \\|\\boldsymbol{\\alpha}\\|_2^2 = 1\\).",
      "يستبدل Kernel PCA مصفوفة التغاير اللانهائية بمصفوفة النواة \\(K\\) ذات القياس \\(N \\times N\\). وتتحول مسألة القيم الذاتية إلى \\(K \\boldsymbol{\\alpha} = \\lambda \\boldsymbol{\\alpha}\\). ولضمان أن متجه الوحدة في فضاء هلبرت ذو طول 1، يتطلب التعيير أن يكون \\(\\lambda \\|\\boldsymbol{\\alpha}\\|^2 = 1\\).",
      "Solve the eigenvalue problem for the kernel Gram matrix K and normalize the eigenvector by \\(\\sqrt{\\lambda}\\).",
      "حل مسألة القيم الذاتية لمصفوفة غرام النواتية K وعير المتجه الذاتي بقسمته على جذر القيمة الذاتية.")

    # 437: FFT Butterfly Operations and Twiddle Factors
    q("KAUST-P3-437", "Applied Mathematics & Signal Processing", "Medium",
      "The radix-2 Cooley-Tukey Fast Fourier Transform (FFT) computes the discrete Fourier transform of length \\(N = 2^m\\) by splitting into even and odd indices. What are the twiddle factors \\(W_N^k\\) in the butterfly recombining equation \\(X[k] = E[k] + W_N^k O[k]\\)?",
      "تحسب خوارزمية كولي-توكي لتحويل فورييه السريع (FFT) الأساس 2 تحويل فورييه المتقطع بطول \\(N = 2^m\\) عبر التجزئة إلى مؤشرات زوجية وفردية. ما هي معاملات الربط (twiddle factors) \\(W_N^k\\) في معادلة الفراشة لدمج التحويلين؟",
      ["\\(W_N^k = e^{-i 2\\pi k / N}\\)",
       "\\(W_N^k = e^{i \\pi k N}\\)",
       "\\(W_N^k = (-1)^k\\)",
       "\\(W_N^k = \\cos(2\\pi k N)\\)"],
      0,
      "The radix-2 decimation-in-time FFT divides the sum into even parts \\(E[k]\\) and odd parts \\(O[k]\\). Factoring out \\(e^{-i 2\\pi (2m+1)k/N}\\) introduces the phase rotation factor \\(W_N^k = e^{-i 2\\pi k / N}\\), known as the twiddle factor. This reduces complexity from \\(\\mathcal{O}(N^2)\\) to \\(\\mathcal{O}(N \\log_2 N)\\).",
      "تقسم خوارزمية كولي-توكي المجموع إلى حدود زوجية \\(E[k]\\) وحدود فردية \\(O[k]\\). باستخراج العامل المشترك ينتج معامل الطور \\(W_N^k = e^{-i 2\\pi k / N}\\) المسمى معامل التدوير (twiddle factor)، وهو ما يختزل التعقيد الحسابي من \\(\\mathcal{O}(N^2)\\) إلى \\(\\mathcal{O}(N \\log N)\\).",
      "The twiddle factor represents the \\(N\\)-th roots of unity in the complex plane.",
      "معامل التدوير يمثل الجذور النونية للواحد الصحيح في المستوى العقدي.")

    # 438: Discrete Cosine Transform Energy Compaction
    q("KAUST-P3-438", "Applied Mathematics & Signal Processing", "Medium",
      "Why is the Discrete Cosine Transform (specifically DCT-II) used instead of the Discrete Fourier Transform (DFT) in lossy image and video compression standards like JPEG and MPEG?",
      "لماذا يُستخدم تحويل جيب التمام المتقطع (تحديداً DCT-II) بدلاً من تحويل فورييه المتقطع (DFT) في معايير ضغط الصور والفيديو مثل JPEG و MPEG؟",
      ["Because DCT implicitly reflects the signal across boundaries, eliminating the artificial high-frequency jump discontinuities present in DFT's periodic extension and maximizing energy compaction",
       "Because DFT cannot be computed on computers",
       "Because DCT generates complex numbers which are easier to compress than real numbers",
       "Because DCT has time complexity \\(\\mathcal{O}(1)\\)"],
      0,
      "The standard DFT implicitly assumes periodic boundary conditions, causing a sharp step discontinuity between \\(x[N-1]\\) and \\(x[0]\\) that creates high-frequency spectral leakage. The DCT-II extends the sequence with even symmetry (mirror reflection) across boundaries, making the periodic extension continuous and eliminating edge artifacts. For first-order Markov (AR(1)) sources, DCT-II asymptotically matches the optimal Karhunen-Loève transform.",
      "يفترض DFT تمديداً دورياً للإشارة مما يسبب قفزة انقطاع حادة بين بداية الإشارة ونهايتها تؤدي لتسرب ترددات عالية غير حقيقية. بالمقابل، يمدد DCT الإشارة بتناظر زوجي عاكس، مما يجعل الدالة المستمرة خالية من قفزات الحدود ويركز معظم طاقة الإشارة في المعاملات الأولى المنخفضة.",
      "DCT uses even boundary reflections to avoid artificial edge jumps.",
      "يستخدم DCT التناظر الزوجي العاكس عند الحدود لتجنب قفزات الانقطاع الاصطناعية.")

    # 439: Cheeger's Inequality in Spectral Graph Theory
    q("KAUST-P3-439", "Spectral Graph Theory", "Hard",
      "Let \\(G = (V, E)\\) be a \\(d\\)-regular graph with normalized Laplacian matrix \\(\\mathcal{L} = I - \\frac{1}{d}A\\), and let \\(0 = \\lambda_1 \\le \\lambda_2 \\le \\dots \\le \\lambda_n\\) be its eigenvalues. Cheeger's Inequality bounds the graph conductance (Cheeger constant) \\(h_G\\) by the spectral gap \\(\\lambda_2\\) as which two-sided inequality?",
      "ليكن \\(G\\) رسماً بيانياً منتظماً من الدرجة \\(d\\) مع مصفوفة لابلابسيان المعيرة \\(\\mathcal{L} = I - \\frac{1}{d}A\\)، ولتكن \\(0 = \\lambda_1 \\le \\lambda_2 \\le \\dots \\le \\lambda_n\\) قيمه الذاتية. تربط متباينة شيغر ثابت شيغر للتوصيل \\(h_G\\) بالفجوة الطيفية \\(\\lambda_2\\) بأي متباينة مزدوجة؟",
      ["\\(\\frac{\\lambda_2}{2} \\le h_G \\le \\sqrt{2 \\lambda_2}\\)",
       "\\(\\lambda_2 \\le h_G \\le \\lambda_2^2\\)",
       "\\(h_G = \\lambda_2\\)",
       "\\(2 \\lambda_2 \\le h_G \\le 4 \\lambda_2\\)"],
      0,
      "Cheeger's inequality for graphs (proved by Alon and Milman) connects the combinatorial bottleneck ratio \\(h_G = \\min_{S \\subset V} \\frac{|E(S, V \\setminus S)|}{d \\min(|S|, |V \\setminus S|)}\\) with the algebraic spectral gap \\(\\lambda_2\\): \\(\\frac{\\lambda_2}{2} \\le h_G \\le \\sqrt{2 \\lambda_2}\\). This guarantees that a graph is an expander if and only if \\(\\lambda_2\\) is bounded away from zero.",
      "تربط متباينة شيغر (التي أثبتها ألون وميلمان) بين معامل عنق الزجاجة التوافقي \\(h_G\\) والفجوة الطيفية الجبرية \\(\\lambda_2\\) عبر \\(\\frac{\\lambda_2}{2} \\le h_G \\le \\sqrt{2 \\lambda_2}\\). تثبت هذه المتباينة أن الرسم يكون ممتداً (expander) إذا وفقط إذا كانت الفجوة الطيفية بعيدة عن الصفر.",
      "The lower bound is linear in \\(\\lambda_2\\), while the upper bound involves \\(\\sqrt{2\\lambda_2}\\).",
      "الحد الأدنى خطي في القيمة الذاتية الثانية، بينما يتضمن الحد الأعلى الجذر التربيعي لـ 2 مضروباً في القيمة الذاتية.")

    # 440: Random Walks on Graphs and Mixing Time
    q("KAUST-P3-440", "Spectral Graph Theory", "Hard",
      "For a lazy random walk on a connected, non-bipartite \\(d\\)-regular graph with transition matrix \\(P = \\frac{1}{2}I + \\frac{1}{2d}A\\), let \\(1 = \\mu_1 > \\mu_2 \\ge \\dots \\ge \\mu_n \\ge 0\\) be the eigenvalues of \\(P\\). The mixing time \\(t_{\\text{mix}}(\\epsilon)\\) to reach total variation distance \\(\\epsilon\\) from the uniform distribution satisfies which upper bound in terms of the spectral gap \\(\\gamma = 1 - \\mu_2\\)?",
      "لمسير عشوائي كسول على رسم بياني منتظم ومتصل ذي درجة \\(d\\) بمصفوفة انتقال \\(P\\)، لتكن \\(1 = \\mu_1 > \\mu_2 \\ge \\dots \\ge \\mu_n \\ge 0\\) القيم الذاتية لـ \\(P\\). ما هو الحد الأعلى لزمن الخلط \\(t_{\\text{mix}}(\\epsilon)\\) بدلالة الفجوة الطيفية \\(\\gamma = 1 - \\mu_2\\)؟",
      ["\\(t_{\\text{mix}}(\\epsilon) \\le \\frac{1}{\\gamma} \\left( \\frac{1}{2}\\log n + \\log(1/\\epsilon) \\right)\\)",
       "\\(t_{\\text{mix}}(\\epsilon) \\le \\gamma \\log n\\)",
       "\\(t_{\\text{mix}}(\\epsilon) \\le n^2 / \\gamma\\)",
       "\\(t_{\\text{mix}}(\\epsilon) = \\frac{1}{\\epsilon \\gamma}\\)"],
      0,
      "The rate of convergence of a Markov chain in \\(L^2\\) is governed geometrically by the second largest eigenvalue modulus \\(\\mu_2\\). Since \\(\\mu_2^t = (1 - \\gamma)^t \\le e^{-\\gamma t}\\), bounding the total variation distance by the \\(L^2\\) distance yields \\(t_{\\text{mix}}(\\epsilon) \\le \\frac{1}{\\gamma} (\\frac{1}{2} \\log n + \\log(1/\\epsilon))\\). Rapid mixing occurs when the spectral gap \\(\\gamma\\) is constant.",
      "يتحكم في معدل تقارب مسير ماركوف هندسياً بالقيمة الذاتية الثانية \\(\\mu_2\\). نظراً لأن \\(\\mu_2^t = (1-\\gamma)^t \\le e^{-\\gamma t}\\)، فإن ربط مسافة التغير الكلي بمسافة \\(L^2\\) يعطي الحد الأعلى \\(t_{\\text{mix}}(\\epsilon) \\le \\frac{1}{\\gamma} (\\frac{1}{2} \\log n + \\log(1/\\epsilon))\\).",
      "The mixing time is inversely proportional to the spectral gap \\(\\gamma\\) and scales logarithmically with graph size \\(n\\).",
      "زمن الخلط يتناسب عكساً مع الفجوة الطيفية غاما ولوغاريتمياً مع عدد رؤوس الرسم n.")

    # 441: Ramanujan Graphs and Alon-Boppana Bound
    q("KAUST-P3-441", "Spectral Graph Theory", "Hard",
      "The Alon-Boppana theorem states that for any infinite family of \\(d\\)-regular graphs, the second eigenvalue of the adjacency matrix satisfies \\(\\liminf_{n\\to\\infty} \\lambda_2(A) \\ge 2\\sqrt{d-1}\\). A \\(d\\)-regular graph is called a Ramanujan graph (Lubotzky, Phillips, Sarnak) if every non-trivial eigenvalue \\(\\lambda\\) satisfies which optimal bound?",
      "تنص مبرهنة ألون-بوبانا على أنه لأي عائلة لانهائية من الرسوم المنتظمة بدرجة \\(d\\)، تحقق القيمة الذاتية الثانية لمصفوفة المجاورة \\(\\liminf_{n\\to\\infty} \\lambda_2(A) \\ge 2\\sqrt{d-1}\\). يُسمى الرسم منتظماً ريمانياً (Ramanujan graph) إذا حققت كل قيمة ذاتية غير تافهة \\(\\lambda\\) أي شرط أمثل؟",
      ["\\(|\\lambda| \\le 2\\sqrt{d-1}\\)",
       "\\(|\\lambda| \\le \\sqrt{d}\\)",
       "\\(|\\lambda| \\le \\frac{d}{2}\\)",
       "\\(|\\lambda| \\le d - 1\\)"],
      0,
      "A Ramanujan graph is a regular graph whose spectral expansion is asymptotically optimal: all nontrivial eigenvalues satisfy \\(|\\lambda| \\le 2\\sqrt{d-1}\\). The term 'Ramanujan' originates from Lubotzky, Phillips, and Sarnak's explicit algebraic construction using quaternion algebras, which established this spectral bound by invoking Pierre Deligne's proof of the Ramanujan-Petersson conjecture in modular forms.",
      "الرسم البياني لرامانوجان هو رسم منتظم يتمتع بتوسع طيفي أمثل مقارب: جميع قيمه الذاتية غير التافهة تحقق \\(|\\lambda| \\le 2\\sqrt{d-1}\\). يعود الاسم إلى استخدام لوبوتزكي وفيليبس وسارناك لجبر الكواتيرنيون وبرهان بيير ديلين لفرضية رامانوجان-بيترسون في الأشكال النمطية.",
      "The bound \\(2\\sqrt{d-1}\\) matches the spectral radius of the universal cover (infinite d-regular tree).",
      "الحد \\(2\\sqrt{d-1}\\) يطابق نصف القطر الطيفي للغطاء الشامل (الشجرة المنتظمة اللانهائية).")

    # 442: Euler Product Formula for Riemann Zeta
    q("KAUST-P3-442", "Analytic Number Theory", "Medium",
      "Euler's product formula establishes the profound identity connecting the Riemann zeta function \\(\\zeta(s) = \\sum_{n=1}^\\infty \\frac{1}{n^s}\\) with the prime numbers for all \\(\\text{Re}(s) > 1\\). What is this product?",
      "تثبت صيغة جداء أويلر المطابقة العميقة التي تربط دالة زيتا لريمان \\(\\zeta(s) = \\sum_{n=1}^\\infty \\frac{1}{n^s}\\) بالأعداد الأولية لجميع \\(\\text{Re}(s) > 1\\). ما هو هذا الجداء؟",
      ["\\(\\zeta(s) = \\prod_{p \\text{ prime}} \\frac{1}{1 - p^{-s}}\\)",
       "\\(\\zeta(s) = \\prod_{p \\text{ prime}} (1 + p^{-s})\\)",
       "\\(\\zeta(s) = \\prod_{p \\text{ prime}} \\frac{1}{1 - s^{-p}}\\)",
       "\\(\\zeta(s) = \\sum_{p \\text{ prime}} \\frac{1}{p^s}\\)"],
      0,
      "By the Fundamental Theorem of Arithmetic, every integer \\(n \\ge 1\\) factors uniquely into primes \\(n = p_1^{a_1} \\dots p_k^{a_k}\\). Expanding each factor as a geometric series \\(\\frac{1}{1 - p^{-s}} = 1 + p^{-s} + p^{-2s} + \\dots\\) and multiplying across all primes yields every \\(n^{-s}\\) exactly once, proving \\(\\zeta(s) = \\prod_p (1 - p^{-s})^{-1}\\).",
      "وفقاً للمبرهنة الأساسية في الحساب، يتفكك كل عدد صحيح بشكل وحيد إلى جداء أعداد أولية. بفك كل حد في الجداء كمتسلسلة هندسية \\(\\frac{1}{1-p^{-s}} = 1 + p^{-s} + p^{-2s} + \\dots\\) وضربه لجميع الأعداد الأولية، ينتج كل حد \\(n^{-s}\\) مرة واحدة بالضبط، مما يثبت مطابقة أويلر الشهيرة.",
      "Each prime contributes a geometric series \\(\\sum_{k=0}^\\infty (p^{-s})^k\\).",
      "يساهم كل عدد أولي بمتسلسلة هندسية مجموعها \\(1/(1-p^{-s})\\).")

    # 443: Functional Equation of the Riemann Zeta Function
    q("KAUST-P3-443", "Analytic Number Theory", "Hard",
      "Riemann showed that \\(\\zeta(s)\\) extends meromorphically to the entire complex plane with a single simple pole at \\(s=1\\). The completed zeta function \\(\\xi(s) = \\frac{1}{2} s (s-1) \\pi^{-s/2} \\Gamma(s/2) \\zeta(s)\\) satisfies the functional equation \\(\\xi(s) = \\xi(1-s)\\). At which values of \\(s\\) are the trivial zeros of \\(\\zeta(s)\\) located?",
      "أثبت ريمان أن \\(\\zeta(s)\\) تمتد تحليلياً إلى المستوى العقدي بأكمله مع قطب بسيط وحيد عند \\(s=1\\). تحقق دالة زيتا المكتملة \\(\\xi(s)\\) المعادلة الدالية \\(\\xi(s) = \\xi(1-s)\\). عند أي قيم لـ \\(s\\) تقع الأصفار التافهة لدالة زيتا \\(\\zeta(s)\\)؟",
      ["\\(s = -2, -4, -6, -8, \\dots\\) (negative even integers)",
       "\\(s = -1, -3, -5, -7, \\dots\\) (negative odd integers)",
       "\\(s = 0, 1, 2, 3, \\dots\\)",
       "\\(s = \\frac{1}{2} + i n\\) for \\(n \\in \\mathbb{Z}\\)"],
      0,
      "The gamma factor \\(\\Gamma(s/2)\\) in the functional equation has simple poles at all non-positive even integers \\(s/2 = 0, -1, -2, \\dots\\), i.e., \\(s = 0, -2, -4, -6, \\dots\\). Since the completed function \\(\\xi(s)\\) is entire, \\(\\zeta(s)\\) must have zeros at \\(s = -2, -4, -6, \\dots\\) to cancel these poles (at \\(s=0\\), \\(\\zeta(0) = -1/2\\) cancels with \\(s\\)). These are the trivial zeros.",
      "تمتلك دالة غاما \\(\\Gamma(s/2)\\) في المعادلة الدالية أقطاباً بسيطة عند الأعداد الصحيحة غير الموجبة. بما أن دالة زيتا المكتملة دالة كلية (entire)، يجب أن تمتلك دالة زيتا أصفاراً عند الأعداد السالبة الزوجية \\(s = -2, -4, -6, \\dots\\) لإلغاء هذه الأقطاب. تُسمى هذه بالأصفار التافهة.",
      "The trivial zeros cancel the poles of the gamma function \\(\\Gamma(s/2)\\) on the negative real axis.",
      "تلغي الأصفار التافهة أقطاب دالة غاما الواقعة على المحور الحقيقي السالب.")

    # 444: Prime Number Theorem and Riemann Hypothesis Equivalence
    q("KAUST-P3-444", "Analytic Number Theory", "Hard",
      "The Prime Number Theorem states that \\(\\pi(x) \\sim \\text{Li}(x) = \\int_2^x \\frac{dt}{\\ln t}\\). The Riemann Hypothesis (that all non-trivial zeros of \\(\\zeta(s)\\) lie on the critical line \\(\\text{Re}(s) = 1/2\\)) is mathematically equivalent to which error bound on the prime counting function \\(\\pi(x)\\)?",
      "تنص مبرهنة الأعداد الأولية على أن \\(\\pi(x) \\sim \\text{Li}(x) = \\int_2^x \\frac{dt}{\\ln t}\\). إن فرضية ريمان (أن جميع الأصفار غير التافهة لدالة زيتا تقع على الخط الحرج \\(\\text{Re}(s) = 1/2\\)) تكافئ رياضياً أي حد للخطأ في دالة عد الأعداد الأولية \\(\\pi(x)\\)؟",
      ["\\(|\\pi(x) - \\text{Li}(x)| = \\mathcal{O}(\\sqrt{x} \\ln x)\\)",
       "\\(|\\pi(x) - \\text{Li}(x)| = \\mathcal{O}(x^{1/3})\\)",
       "\\(|\\pi(x) - \\text{Li}(x)| = \\mathcal{O}(1)\\)",
       "\\(|\\pi(x) - \\text{Li}(x)| = \\mathcal{O}(\\ln x)\\)"],
      0,
      "Helge von Koch proved in 1901 that the Riemann Hypothesis is strictly equivalent to the error bound \\(|\\pi(x) - \\text{Li}(x)| = \\mathcal{O}(\\sqrt{x} \\ln x)\\), or equivalently for Chebyshev's function, \\(|\\psi(x) - x| = \\mathcal{O}(\\sqrt{x} \\ln^2 x)\\). The exponent \\(1/2\\) of \\(\\sqrt{x} = x^{1/2}\\) directly reflects the supremum of the real parts of the non-trivial zeros.",
      "أثبت فون كوخ في عام 1901 أن فرضية ريمان تكافئ تماماً أن يكون حد الخطأ في عد الأعداد الأولية مقيداً بـ \\(\\mathcal{O}(\\sqrt{x} \\ln x)\\). يعكس الأس \\(1/2\\) في \\(x^{1/2}\\) مباشرة موضع الأصفار غير التافهة على الخط الحرج ذي الجزء الحقيقي 1/2.",
      "The square root factor \\(\\sqrt{x} = x^{1/2}\\) matches the critical line real part \\(1/2\\).",
      "يعكس جذر x ذو الأس 1/2 الجزء الحقيقي للخط الحرج في فرضية ريمان.")

    # 445: Dirichlet's Theorem on Primes in Arithmetic Progressions
    q("KAUST-P3-445", "Analytic Number Theory", "Hard",
      "To prove Dirichlet's Theorem (infinitely many primes in the arithmetic progression \\(a, a+q, a+2q, \\dots\\) when \\(\\gcd(a, q) = 1\\)), Dirichlet introduced Dirichlet \\(L\\)-functions \\(L(s, \\chi) = \\sum_{n=1}^\\infty \\frac{\\chi(n)}{n^s}\\). What was the crucial non-vanishing analytic fact that Dirichlet had to establish?",
      "لإثبات مبرهنة دركليه (وجود عدد لانهائي من الأعداد الأولية في المتتالية الحسابية \\(a, a+q, a+2q, \\dots\\) عندما \\(\\gcd(a, q) = 1\\))، أدخل دركليه دوال \\(L\\). ما هي الحقيقة التحليلية الجوهرية غير الصفرية التي كان على دركليه إثباتها؟",
      ["\\(L(1, \\chi) \\ne 0\\) for all non-principal characters \\(\\chi \\ne \\chi_0\\)",
       "\\(L(0, \\chi) = 0\\)",
       "\\(L(s, \\chi) > 0\\) for all complex \\(s\\)",
       "\\(L(2, \\chi) = \\pi^2\\)"],
      0,
      "Dirichlet proved that \\(\\sum_{p \\equiv a \\pmod q} \\frac{1}{p^s} = \\frac{1}{\\phi(q)} \\sum_{\\chi} \\overline{\\chi}(a) \\log L(s, \\chi)\\). As \\(s \\to 1^+\\), the term for the principal character \\(\\chi_0\\) diverges like \\(\\log \\zeta(s) \\to +\\infty\\). For this divergence not to be cancelled out by the other terms, Dirichlet proved that \\(L(1, \\chi) \\ne 0\\) for every non-principal character \\(\\chi\\), establishing the theorem.",
      "أثبت دركليه أن مجموع مقلوب الأعداد الأولية في المتتالية يتناسب مع مجموع لوغاريتمات دوال L. عند \\(s \\to 1^+\\)، يتباعد حد الرمز الرئيسي إلى ما لا نهاية. لضمان عدم إلغاء هذا التباعد بواسطة الرموز الأخرى، كان الإنجاز الأكبر لدركليه هو إثبات أن \\(L(1, \\chi) \\ne 0\\) لجميع الرموز غير الرئيسية.",
      "The value of the L-function at \\(s=1\\) cannot vanish.",
      "القيمة التحليلية لدالة L عند النقطة s=1 لا يمكن أن تساوي صفراً.")

    # 446: Eisenstein Series and Modular Forms
    q("KAUST-P3-446", "Analytic Number Theory & Modular Forms", "Hard",
      "A modular form of weight \\(k\\) for the full modular group \\(SL(2, \\mathbb{Z})\\) is a holomorphic function \\(f: \\mathbb{H} \\to \\mathbb{C}\\) satisfying \\(f\\left(\\frac{az+b}{cz+d}\\right) = (cz+d)^k f(z)\\) for all \\(\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\in SL(2, \\mathbb{Z})\\). What is the minimum even weight \\(k > 0\\) for which non-zero holomorphic modular forms exist?",
      "الشكل النمطي من الوزن \\(k\\) لزمرة الأشكال النمطية الكاملة \\(SL(2, \\mathbb{Z})\\) هو دالة هولومورفية \\(f: \\mathbb{H} \\to \\mathbb{C}\\) تحقق \\(f\\left(\\frac{az+b}{cz+d}\\right) = (cz+d)^k f(z)\\). ما هو أدنى وزن زوجي \\(k > 0\\) توجد له أشكال نمطية هولومورفية غير صفرية؟",
      ["\\(k = 4\\) (given by the Eisenstein series \\(E_4(z) = 1 + 240 \\sum_{n=1}^\\infty \\sigma_3(n) q^n\\))",
       "\\(k = 2\\)",
       "\\(k = 1\\)",
       "\\(k = 6\\)"],
      0,
      "For odd \\(k\\), taking \\(-I = \\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\) yields \\(f(z) = (-1)^k f(z) = -f(z) \\implies f \\equiv 0\\). For \\(k = 2\\), the Eisenstein series \\(G_2(z)\\) is only quasi-modular. By the valence formula (\\(k/12\\) theorem), the space of modular forms \\(M_k\\) has dimension 0 for \\(k = 2\\), and dimension 1 for \\(k = 4\\) spanned by \\(E_4(z)\\).",
      "بالنسبة للأوزان الفردية، ينتج فوراً أن \\(f(z) = -f(z) \\implies f \\equiv 0\\). وبالنسبة لـ \\(k=2\\)، فإن متسلسلة أيزنشتاين ليست نمطية تماماً بل شبه نمطية (quasi-modular). وبموجب صيغة التكافؤ (مبرهنة k/12)، فإن بعد فضاء الأشكال النمطية يساوي صفراً عند k=2، وأدنى وزن زوجي موجب يوجد له شكل نمطي غير صفري هو k=4 وتولده متسلسلة أيزنشتاين E4.",
      "Check the valence formula \\(v_\\infty(f) + \\frac{1}{2}v_i(f) + \\frac{1}{3}v_\\rho(f) + \\sum v_p(f) = \\frac{k}{12}\\).",
      "استخدم صيغة التكافؤ لمعرفة أدنى وزن كافٍ لجعل بعد الفضاء أكبر من صفر.")

    # 447: Perron's Formula and Contour Integration of Dirichlet Series
    q("KAUST-P3-447", "Analytic Number Theory", "Hard",
      "Perron's formula is the fundamental tool of analytic number theory that extracts the partial sum \\(A(x) = \\sum_{n \\le x} a_n\\) from the generating Dirichlet series \\(F(s) = \\sum_{n=1}^\\infty \\frac{a_n}{n^s}\\). For \\(c > 0\\) in the half-plane of absolute convergence and non-integer \\(x > 1\\), what is Perron's contour integral formula?",
      "صيغة بيرون هي الأداة الجوهرية في نظرية الأعداد التحليلية التي تستخرج المجموع الجزئي \\(A(x) = \\sum_{n \\le x} a_n\\) من متسلسلة دركليه المولدة \\(F(s) = \\sum \\frac{a_n}{n^s}\\). لثابت \\(c > 0\\) في نصف مستوى التقارب المطلق وعدد غير صحيح \\(x > 1\\)، ما هي صيغة تكامل بيرون الخطي؟",
      ["\\(\\sum_{n \\le x} a_n = \\frac{1}{2\\pi i} \\int_{c - i\\infty}^{c + i\\infty} F(s) \\frac{x^s}{s} \\, ds\\)",
       "\\(\\sum_{n \\le x} a_n = \\int_{0}^x F(s) \\, ds\\)",
       "\\(\\sum_{n \\le x} a_n = 2\\pi i \\text{Res}(F(s) x^s, 1)\\)",
       "\\(\\sum_{n \\le x} a_n = \\frac{1}{2\\pi i} \\oint_{|s|=c} \\frac{F(s)}{s} \\, ds\\)"],
      0,
      "Perron's formula is based on the discontinuous Cauchy integral \\(\\frac{1}{2\\pi i}\\int_{c-i\\infty}^{c+i\\infty} \\frac{y^s}{s} ds = 1\\) if \\(y > 1\\), and \\(0\\) if \\(0 < y < 1\\). Substituting \\(y = x/n\\) and swapping sum and integral yields \\(\\sum_{n \\le x} a_n = \\frac{1}{2\\pi i}\\int_{c-i\\infty}^{c+i\\infty} F(s) \\frac{x^s}{s} ds\\). Shifting the vertical contour to the left collects residues that determine the asymptotic behavior of \\(A(x)\\).",
      "تعتمد صيغة بيرون على التكامل العقدي المتقطع لدالة القفزة الأحادية لكوشي. بوضع \\(y = x/n\\) وتبادل المجموع والتكامل نحصل على الصيغة \\(\\frac{1}{2\\pi i}\\int_{c-i\\infty}^{c+i\\infty} F(s) \\frac{x^s}{s} ds\\). وبإزاحة المسار الرأسي نحو اليسار تُجمع الرواسب التي تعطي الحدود الرئيسية المقاربة للمجموع.",
      "The kernel in the complex contour integral is \\(x^s / s\\).",
      "النواة داخل التكامل العقدي على الخط الرأسي هي \\(x^s / s\\).")

    # 448: Lovász Local Lemma (Symmetric Version)
    q("KAUST-P3-448", "Probabilistic Combinatorics", "Hard",
      "Let \\(A_1, A_2, \\dots, A_m\\) be events in a probability space, each occurring with probability at most \\(p\\). Suppose each event \\(A_i\\) is mutually independent of all other events except for at most \\(d\\) of them. According to the symmetric Lovász Local Lemma, which condition guarantees that with positive probability, NONE of the bad events \\(A_i\\) occur (\\(\\mathbb{P}(\\bigcap_{i=1}^m \\overline{A_i}) > 0\\))?",
      "لتكن \\(A_1, \\dots, A_m\\) حوادث في فضاء احتمالي، احتمال كل منها لا يتجاوز \\(p\\). افترض أن كل حادثة \\(A_i\\) مستقلة تبادلياً عن جميع الحوادث الأخرى باستثناء \\(d\\) منها على الأكثر. وفقاً لتمهيدية لوفاس المحلية المتماثلة، ما هو الشرط الذي يضمن وجود احتمال موجب لعدم وقوع أي من هذه الحوادث السيئة إطلاقاً؟",
      ["\\(e \\cdot p \\cdot (d + 1) \\le 1\\)",
       "\\(p \\cdot m < 1\\)",
       "\\(p \\cdot d \\le \\frac{1}{2}\\)",
       "\\(p + d \\le 1\\)"],
      0,
      "The Lovász Local Lemma (Erdős & Lovász, 1975) is a cornerstone of the probabilistic method for non-independent events. The symmetric condition \\(e p (d + 1) \\le 1\\) (where \\(e \\approx 2.718\\)) guarantees that \\(\\mathbb{P}(\\bigcap \\overline{A_i}) \\ge (1 - \\frac{1}{d+1})^m > 0\\), establishing the existence of combinatorial objects satisfying specified constraints despite dependency among tests.",
      "تعد تمهيدية لوفاس المحلية ركيزة الطريقة الاحتمالية للأحداث ذات الاعتمادية المحدودة. يضمن الشرط المتماثل \\(e \\cdot p \\cdot (d+1) \\le 1\\) أن احتمال تقاطع المتممات موجب تماماً، مما يثبت وجود البنية التوافقية المنشودة حتى مع اعتمادية كل حادثة على d حادثة أخرى.",
      "Look for Euler's constant e multiplying the probability p and degree bound \\(d+1\\).",
      "ابحث عن ثابت أويلر e مضروباً في الاحتمال p والدرجة d+1.")

    # 449: Szemerédi's Regularity Lemma
    q("KAUST-P3-449", "Extremal Combinatorics & Additive Combinatorics", "Hard",
      "Szemerédi's Regularity Lemma is one of the most powerful tools in modern combinatorics and ergodic theory. Roughly speaking, what does the lemma state about any large dense graph \\(G = (V, E)\\)?",
      "تعتبر تمهيدية زيميريدي للانتظام واحدة من أقوى الأدوات في التوافقيات ونظرية إرغوديك الحديثة. بشكل عام، ما الذي تؤكده التمهيدية حول أي رسم بياني كثيف وكبير \\(G = (V, E)\\)؟",
      ["The vertex set \\(V\\) can be partitioned into a bounded number of equal-sized subsets such that the bipartite edges between almost all pairs behave like random bipartite graphs (\\(\\epsilon\\)-regular pairs)",
       "Every large dense graph contains a complete bipartite subgraph \\(K_{n,n}\\)",
       "The chromatic number of the graph is bounded by \\(\\mathcal{O}(\\log |V|)\\)",
       "The adjacency matrix of the graph must have only integer eigenvalues"],
      0,
      "Szemerédi's Regularity Lemma states that for every \\(\\epsilon > 0\\), there exists \\(M(\\epsilon)\\) such that any graph can be partitioned into \\(k\\) clusters (where \\(1/\\epsilon \\le k \\le M(\\epsilon)\\)) such that all but at most \\(\\epsilon k^2\\) pairs of clusters are \\(\\epsilon\\)-regular (their edge densities behave like independent random bipartite graphs). This opened the path to graph limits, property testing, and the Green-Tao theorem.",
      "تنص تمهيدية زيميريدي على أنه لأي \\(\\epsilon > 0\\)، يمكن تجزئة رؤوس أي رسم بياني إلى عدد محدود من المجموعات المتساوية بحيث تسلك الحواف بين الغالبية الساحقة من أزواج المجموعات سلوك رسوم عشوائية منتظمة. فتحت هذه النتيجة الباب لنظرية نهايات الرسوم ومبرهنة غرين-تاو للأعداد الأولية في المتتاليات الحسابية.",
      "It partitions the vertices so that almost all bipartite pairs between clusters look pseudorandom.",
      "تجزئ الرؤوس بحيث تسلك الحواف بين معظم الأزواج سلوكاً عشوائياً كاذباً ذا كثافة متجانسة.")

    # 450: Ricci Flow and Perelman's Geometrization Theorem
    q("KAUST-P3-450", "Differential Geometry & Geometric Analysis", "Hard",
      "Richard Hamilton introduced the Ricci flow equation to deform the Riemannian metric \\(g\\) on a smooth manifold in the direction of its Ricci curvature: \\(\\frac{\\partial g_{ij}}{\\partial t} = -2 R_{ij}\\). Grigori Perelman's monumental breakthrough proving the Poincaré Conjecture and Thurston's Geometrization Conjecture overcame which critical geometric obstruction in Ricci flow?",
      "أدخل ريتشارد هاميلتون معادلة تدفق ريتشي لتشويه المتري الريماني \\(g\\) على متعدد أملس في اتجاه انحناء ريتشي: \\(\\frac{\\partial g_{ij}}{\\partial t} = -2 R_{ij}\\). ما هو العائق الهندسي الجوهري الذي نجح غريغوري بيرلمان في تجاوزه لإثبات حدسية بوانكاريه وحدسية ثيرستون للتنسيق الهندسي؟",
      ["Formation of finite-time curvature singularities (such as neckpinches), successfully resolved by introducing Ricci flow with surgery and monotone entropy functionals (\\(\\mathcal{W}\\)-entropy)",
       "The non-existence of smooth metrics on 3-manifolds",
       "The fact that the Ricci tensor is always identically zero in three dimensions",
       "The failure of the Euler characteristic to be defined for compact 3-manifolds"],
      0,
      "In dimension 3, Ricci flow develops finite-time curvature blow-up singularities (such as cylindrical neckpinches). Perelman introduced groundbreaking monotone entropy functionals (the \\(\\mathcal{F}\\) and \\(\\mathcal{W}\\) entropies) that ruled out local collapsing (cigar solitons), and established a rigorous surgical procedure (Ricci flow with surgery) to excise high-curvature necks and continue the flow for all time, establishing Thurston's Geometrization Conjecture and the 100-year-old Poincaré Conjecture.",
      "في البعد 3، يطور تدفق ريتشي انفراديات تضخم انحناء في زمن منتهٍ (مثل انخناق العنق). استحدث بيرلمان دوال إنتروبيا رتيبة ثورية (إنتروبيا W) نفت الانهيار الموضعي، وطور إجراءً جراحياً هندسياً دقيقاً لاستئصال الأعناق ومواصلة التدفق لجميع الأوقات، مما مكنه من إثبات حدسية ثيرستون للتنسيق الهندسي وحدسية بوانكاريه.",
      "Perelman analyzed finite-time singularity formation and introduced Ricci flow with surgery.",
      "حلل بيرلمان تشكل الانفراديات في زمن منتهٍ واستحدث تدفق ريتشي مع العمليات الجراحية الموضعية.")

    return questions

if __name__ == "__main__":
    qs = get_p3_part_d()
    print(f"Loaded {len(qs)} questions for Phase 3 Part D.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=401):
        expected_id = f"KAUST-P3-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 3 Part D questions successfully verified!")
