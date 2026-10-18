#!/usr/bin/env python3
"""
KAUST Phase 2 Questions Part C: 351 to 400
Linear Algebra & Matrix Analysis:
Jordan Canonical Forms, Minimal Polynomials, Singular Value Decomposition (SVD),
Rayleigh Quotient, Positive Definiteness, Cholesky, Gershgorin Discs,
Matrix Norms, Projection Operators, Cayley-Hamilton Theorem.
Authentic lineages: MIT 18.06 / 18.065, Harvard Math 21b, Cambridge Tripos, Putnam, Stanford EE263.
"""

def get_p2_part_c():
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

    # 351: Gershgorin Circle Theorem with SVG
    svg_gershgorin = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-20 -60 160 120' width='100%' height='100%' style='background:#0d1117;'>
  <line x1='-15' y1='0' x2='135' y2='0' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-55' x2='0' y2='55' stroke='#8b949e' stroke-width='1.5'/>
  <!-- Disc 1: center (10, 0), radius 30 (representing center 1, radius 3) -->
  <circle cx='30' cy='0' r='30' fill='rgba(88, 166, 255, 0.2)' stroke='#58a6ff' stroke-width='2'/>
  <circle cx='30' cy='0' r='3' fill='#58a6ff'/>
  <text x='35' y='-5' fill='#58a6ff' font-size='10' font-family='sans-serif'>D₁: c=4, R=2</text>
  <!-- Disc 2: center (80, 0), radius 20 -->
  <circle cx='80' cy='0' r='20' fill='rgba(240, 136, 62, 0.2)' stroke='#f0883e' stroke-width='2'/>
  <circle cx='80' cy='0' r='3' fill='#f0883e'/>
  <text x='85' y='-5' fill='#f0883e' font-size='10' font-family='sans-serif'>D₂: c=8, R=1</text>
</svg>"""
    q("KAUST-P2-351", "Matrix Analysis", "Medium",
      "Using Gershgorin's Disc Theorem, find the bound on the eigenvalues of \\(A = \\begin{pmatrix} 4 & 1 & 1 \\\\ 0 & 8 & 1 \\\\ 1 & 2 & 10 \\end{pmatrix}\\). In which union of real intervals must all real eigenvalues lie?",
      "باستخدام نظرية أقراص غيرشغورين، أوجد الحصر للقيم الذاتية للمصفوفة \\(A = \\begin{pmatrix} 4 & 1 & 1 \\\\ 0 & 8 & 1 \\\\ 1 & 2 & 10 \\end{pmatrix}\\). في أي اتحاد من الفترات الحقيقية تقع جميع القيم الذاتية الحقيقية؟",
      ["\\([2, 6] \\cup [7, 9] \\cup [7, 13]\\)", "\\([1, 5] \\cup [6, 10] \\cup [8, 12]\\)", "\\([3, 5] \\cup [7, 9] \\cup [9, 11]\\)", "\\([0, 6] \\cup [8, 14]\\)"],
      0,
      "The Gershgorin discs are \\(D_i = \\{z \\in \\mathbb{C} : |z - a_{ii}| \\le R_i\\}\\) where \\(R_i = \\sum_{j \\neq i} |a_{ij}|\\). For row 1: center \\(4\\), radius \\(1+1 = 2\\), interval \\([4-2, 4+2] = [2, 6]\\). For row 2: center \\(8\\), radius \\(0+1 = 1\\), interval \\([8-1, 8+1] = [7, 9]\\). For row 3: center \\(10\\), radius \\(1+2 = 3\\), interval \\([10-3, 10+3] = [7, 13]\\). Thus every eigenvalue lies in the union \\(D_1 \\cup D_2 \\cup D_3\\), so real eigenvalues lie in \\([2, 6] \\cup [7, 9] \\cup [7, 13]\\).",
      "أقراص غيرشغورين مركزها \\(a_{ii}\\) ونصف قطرها مجموع القيم المطلقة لبقية عناصر الصف. للصف الأول: المركز 4 ونصف القطر 2، أي \\([2, 6]\\). للصف الثاني: المركز 8 ونصف القطر 1، أي \\([7, 9]\\). للصف الثالث: المركز 10 ونصف القطر 3، أي \\([7, 13]\\). اتحاد الفترات يحصر جميع القيم الذاتية.",
      "Calculate \\(R_i = \\sum_{j \\neq i} |a_{ij}|\\) for each row.",
      "احسب نصف قطر كل قرص بجمع القيم المطلقة للعناصر غير القطرية في كل صف.",
      diagram=svg_gershgorin)

    # 352: Minimal Polynomial and Diagonalizability
    q("KAUST-P2-352", "Linear Algebra", "Hard",
      "Let \\(A = \\begin{pmatrix} 2 & 1 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 3 \\end{pmatrix}\\). What is the minimal polynomial \\(m_A(x)\\) of \\(A\\), and is \\(A\\) diagonalizable over \\(\\mathbb{C}\\)?",
      "لتكن \\(A = \\begin{pmatrix} 2 & 1 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 3 \\end{pmatrix}\\). ما هو كثير الحدود الأصغري \\(m_A(x)\\) للمصفوفة \\(A\\)، وهل \\(A\\) قابلة للتقطير على \\(\\mathbb{C}\\)؟",
      ["\\(m_A(x) = (x-2)^2(x-3)\\); Not diagonalizable",
       "\\(m_A(x) = (x-2)(x-3)\\); Diagonalizable",
       "\\(m_A(x) = (x-2)(x-3)^2\\); Not diagonalizable",
       "\\(m_A(x) = (x-2)^3\\); Not diagonalizable"],
      0,
      "The characteristic polynomial is \\(p(x) = (x-2)^2(x-3)\\). The candidates for minimal polynomial are \\((x-2)(x-3)\\) or \\((x-2)^2(x-3)\\). Test \\((A - 2I)(A - 3I)\\): \\(A - 2I = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}\\), \\(A - 3I = \\begin{pmatrix} -1 & 1 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}\\). Their product has top-left entry \\(0(-1) + 1(0) + 0(0) = 0\\), but entry \\((1, 2)\\) is \\(0(1) + 1(-1) + 0(0) = -1 \\neq 0\\). Thus \\((A-2I)(A-3I) \\neq 0\\), meaning the minimal polynomial must be \\(m_A(x) = (x-2)^2(x-3)\\). Because \\(m_A(x)\\) has a repeated linear factor \\((x-2)^2\\), \\(A\\) is not diagonalizable.",
      "كثير الحدود المميز هو \\((x-2)^2(x-3)\\). بفحص \\((A-2I)(A-3I)\\) نجد أنه لا يساوي المصفوفة الصفرية. بالتالي كثير الحدود الأصغري هو \\(m_A(x) = (x-2)^2(x-3)\\). وبما أنه يحتوي على عامل خطي مكرر، فإن المصفوفة غير قابلة للتقطير.",
      "A matrix is diagonalizable if and only if its minimal polynomial has distinct linear factors.",
      "تكون المصفوفة قابلة للتقطير إذا وفقط إذا كان كثير حدودها الأصغري حاصل ضرب عوامل خطية غير مكررة.")

    # 353: Jordan Canonical Form
    q("KAUST-P2-353", "Linear Algebra", "Hard",
      "A matrix \\(A \\in \\mathbb{C}^{5 \\times 5}\\) has characteristic polynomial \\(p(\\lambda) = (\\lambda - 4)^5\\). If \\(\\text{rank}(A - 4I) = 3\\) and \\(\\text{rank}((A - 4I)^2) = 1\\), what are the sizes of the Jordan blocks of \\(A\\)?",
      "مصفوفة \\(A \\in \\mathbb{C}^{5 \\times 5}\\) لها متعددة حدود مميزة \\(p(\\lambda) = (\\lambda - 4)^5\\). إذا كان \\(\\text{rank}(A - 4I) = 3\\) و \\(\\text{rank}((A - 4I)^2) = 1\\)، فما هي أبعاد كتل جوردان للمصفوفة \\(A\\)؟",
      ["One block of size 3 and one block of size 2",
       "One block of size 4 and one block of size 1",
       "Two blocks of size 2 and one block of size 1",
       "One block of size 5"],
      0,
      "The geometric multiplicity of \\(\\lambda = 4\\) is \\(\\dim(\\ker(A - 4I)) = 5 - \\text{rank}(A - 4I) = 5 - 3 = 2\\). This means there are exactly 2 Jordan blocks. The nullity of \\((A - 4I)^2\\) is \\(5 - \\text{rank}((A - 4I)^2) = 5 - 1 = 4\\). The number of blocks of size \\(\\ge 1\\) is \\(5 - 3 = 2\\). The number of blocks of size \\(\\ge 2\\) is \\(\\text{nullity}((A-4I)^2) - \\text{nullity}(A-4I) = 4 - 2 = 2\\). The number of blocks of size \\(\\ge 3\\) is \\(5 - 4 = 1\\). Thus, the block sizes must partition 5 into 2 parts with maximum size 3: \\(3 + 2 = 5\\). So the Jordan form consists of one \\(3 \\times 3\\) block and one \\(2 \\times 2\\) block.",
      "التعدد الهندسي هو \\(5 - 3 = 2\\)، مما يعني وجود كتلتين من كتل جوردان. بُعد فضاء العدم للمربع \\((A-4I)^2\\) هو \\(5 - 1 = 4\\). عدد الكتل ذات الحجم \\(\\ge 2\\) هو \\(4 - 2 = 2\\)، وعدد الكتل ذات الحجم \\(\\ge 3\\) هو \\(5 - 4 = 1\\). بالتالي، كتلا جوردان هما ذات البعدين 3 و 2.",
      "The number of blocks equals \\(\\text{nullity}(A - \\lambda I)\\), and the block sizes are given by differences of nullities of powers.",
      "عدد الكتل يساوي بُعد فضاء العدم لـ \\(A - \\lambda I\\)، وأحجام الكتل تُحدد بفروق أبعاد فضاء العدم للقوى المتعاقبة.")

    # 354: Singular Value Decomposition (SVD)
    q("KAUST-P2-354", "Matrix Analysis", "Medium",
      "Find the singular values \\(\\sigma_1 \\ge \\sigma_2\\) of the matrix \\(A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -4 \\end{pmatrix}\\).",
      "أوجد القيم المفردة (singular values) \\(\\sigma_1 \\ge \\sigma_2\\) للمصفوفة \\(A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -4 \\end{pmatrix}\\).",
      ["\\(\\sigma_1 = 4, \\sigma_2 = 3\\)", "\\(\\sigma_1 = 16, \\sigma_2 = 9\\)", "\\(\\sigma_1 = 4, \\sigma_2 = -3\\)", "\\(\\sigma_1 = 5, \\sigma_2 = 1\\)"],
      0,
      "The singular values of \\(A\\) are the square roots of the eigenvalues of \\(A^T A\\). Compute \\(A^T A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -4 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & -4 \\end{pmatrix} = \\begin{pmatrix} 9 & 0 \\\\ 0 & 16 \\end{pmatrix}\\). The eigenvalues of \\(A^T A\\) are \\(\\lambda_1 = 16\\) and \\(\\lambda_2 = 9\\). Therefore, the singular values are \\(\\sigma_1 = \\sqrt{16} = 4\\) and \\(\\sigma_2 = \\sqrt{9} = 3\\). By convention, singular values are always non-negative real numbers.",
      "القيم المفردة هي الجذور التربيعية للقيم الذاتية للمصفوفة \\(A^T A\\). نجد \\(A^T A = \\text{diag}(9, 16)\\)، وبالتالي فإن القيم المفردة هي \\(\\sqrt{16} = 4\\) و \\(\\sqrt{9} = 3\\). القيم المفردة دائماً أعداد حقيقية غير سالبة.",
      "Singular values are defined as \\(\\sigma_i = \\sqrt{\\lambda_i(A^T A)}\\) and are always non-negative.",
      "القيم المفردة هي الجذور التربيعية للقيم الذاتية لـ \\(A^T A\\) وتكون دائماً موجبة أو صفراً.")

    # 355: Rayleigh Quotient & Extremal Eigenvalues
    q("KAUST-P2-355", "Matrix Analysis", "Hard",
      "For a real symmetric matrix \\(S\\), the Rayleigh quotient is \\(R_S(\\mathbf{x}) = \\frac{\\mathbf{x}^T S \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}\\). If \\(S = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}\\), what is the maximum value of \\(R_S(\\mathbf{x})\\) over all \\(\\mathbf{x} \\neq \\mathbf{0}\\)?",
      "لمصفوفة حقيقية متماثلة \\(S\\)، حاصل قسمة رايلي هو \\(R_S(\\mathbf{x}) = \\frac{\\mathbf{x}^T S \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}\\). إذا كانت \\(S = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}\\)، فما هي القيمة العظمى لـ \\(R_S(\\mathbf{x})\\) لجميع \\(\\mathbf{x} \\neq \\mathbf{0}\\)؟",
      ["\\(3\\)", "\\(2\\)", "\\(1\\)", "\\(4\\)"],
      0,
      "By Rayleigh's quotient theorem for symmetric matrices, \\(\\max_{\\mathbf{x} \\neq \\mathbf{0}} R_S(\\mathbf{x}) = \\lambda_{\\max}(S)\\). The characteristic equation of \\(S\\) is \\(\\det\\begin{pmatrix} 2-\\lambda & 1 \\\\ 1 & 2-\\lambda \\end{pmatrix} = (2-\\lambda)^2 - 1 = 0 \\implies 2 - \\lambda = \\pm 1 \\implies \\lambda_1 = 3, \\lambda_2 = 1\\). Therefore, \\(\\lambda_{\\max} = 3\\), achieved when \\(\\mathbf{x}\\) is an eigenvector corresponding to \\(\\lambda = 3\\), such as \\(\\mathbf{x} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}\\).",
      "حسب نظرية رايلي للمصفوفات المتماثلة، القيمة العظمى لحاصل قسمة رايلي تساوي أكبر قيمة ذاتية للمصفوفة. المعادلة المميزة تعطي \\((2-\\lambda)^2 = 1\\)، ومنها \\(\\lambda = 3\\) و \\(\\lambda = 1\\). إذن القيمة العظمى هي 3.",
      "The maximum of the Rayleigh quotient equals the maximum eigenvalue of the symmetric matrix.",
      "القيمة العظمى لنسبة رايلي تساوي أكبر قيمة ذاتية للمصفوفة المتماثلة.")

    # 356: Sylvester's Criterion for Positive Definiteness
    q("KAUST-P2-356", "Matrix Analysis", "Medium",
      "Find the condition on parameter \\(k\\) such that the matrix \\(A = \\begin{pmatrix} 1 & 2 & 0 \\\\ 2 & k & 1 \\\\ 0 & 1 & 2 \\end{pmatrix}\\) is positive definite.",
      "أوجد الشرط على المعلمة \\(k\\) بحيث تكون المصفوفة \\(A = \\begin{pmatrix} 1 & 2 & 0 \\\\ 2 & k & 1 \\\\ 0 & 1 & 2 \\end{pmatrix}\\) موجبة المعرّفة (positive definite).",
      ["\\(k > \\frac{9}{2}\\)", "\\(k > 4\\)", "\\(k > 5\\)", "\\(k > 2\\)"],
      0,
      "By Sylvester's criterion, a symmetric matrix is positive definite iff all its leading principal minors are strictly positive: 1) \\(\\Delta_1 = 1 > 0\\). 2) \\(\\Delta_2 = \\det\\begin{pmatrix} 1 & 2 \\\\ 2 & k \\end{pmatrix} = k - 4 > 0 \\implies k > 4\\). 3) \\(\\Delta_3 = \\det(A) = 1(2k - 1) - 2(4 - 0) + 0 = 2k - 1 - 8 = 2k - 9 > 0 \\implies k > 9/2\\). Since \\(9/2 = 4.5 > 4\\), the necessary and sufficient condition is \\(k > \\frac{9}{2}\\).",
      "باستخدام معيار سيلفستر، تكون المصفوفة موجبة المعرفة إذا وفقط إذا كانت جميع محددات الأقليات الرئيسية الرائدة موجبة تماماً: \\(\\Delta_1 = 1 > 0\\)، و \\(\\Delta_2 = k - 4 > 0 \\implies k > 4\\)، و \\(\\Delta_3 = 2k - 9 > 0 \\implies k > 9/2\\). الشرط الحاكم هو \\(k > 9/2\\).",
      "Evaluate the third leading principal minor (the determinant of the whole matrix).",
      "احسب محدد المصفوفة بالكامل وتحقق من أنه موجب تماماً.")

    # 357: Cayley-Hamilton Inverse Calculation
    q("KAUST-P2-357", "Linear Algebra", "Medium",
      "Let \\(A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\). Using the Cayley-Hamilton theorem, express \\(A^{-1}\\) as a linear polynomial in \\(A\\).",
      "لتكن \\(A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\). باستخدام نظرية كايلي-هاميلتون، عبّر عن \\(A^{-1}\\) ككثيرة حدود خطية في \\(A\\).",
      ["\\(A^{-1} = \\frac{1}{2}A - \\frac{5}{2}I\\)", "\\(A^{-1} = -\\frac{1}{2}A + \\frac{5}{2}I\\)", "\\(A^{-1} = \\frac{1}{2}A + \\frac{5}{2}I\\)", "\\(A^{-1} = -A + 5I\\)"],
      0,
      "The characteristic polynomial is \\(p(\\lambda) = \\det(\\lambda I - A) = \\lambda^2 - \\text{tr}(A)\\lambda + \\det(A)\\). Here \\(\\text{tr}(A) = 1 + 4 = 5\\) and \\(\\det(A) = 4 - 6 = -2\\). So \\(p(\\lambda) = \\lambda^2 - 5\\lambda - 2\\). By Cayley-Hamilton: \\(A^2 - 5A - 2I = 0\\). Multiply by \\(A^{-1}\\): \\(A - 5I - 2A^{-1} = 0 \\implies 2A^{-1} = A - 5I \\implies A^{-1} = \\frac{1}{2}A - \\frac{5}{2}I\\).",
      "كثير الحدود المميز هو \\(\\lambda^2 - 5\\lambda - 2 = 0\\). بنظرية كايلي-هاميلتون: \\(A^2 - 5A - 2I = 0\\). بالضرب في \\(A^{-1}\\): \\(A - 5I - 2A^{-1} = 0\\)، ومنه \\(A^{-1} = \\frac{1}{2}A - \\frac{5}{2}I\\).",
      "Multiply the characteristic relation \\(A^2 - 5A - 2I = 0\\) by \\(A^{-1}\\).",
      "اضرب المعادلة المميزة للمصفوفة في مقلوب المصفوفة \\(A^{-1}\\).")

    # 358: Projection Matrix Properties
    q("KAUST-P2-358", "Linear Algebra", "Medium",
      "Let \\(P \\in \\mathbb{R}^{n \\times n}\\) be an orthogonal projection matrix onto a subspace \\(V\\) of dimension \\(k < n\\). What are the trace and eigenvalues of \\(P\\)?",
      "لتكن \\(P \\in \\mathbb{R}^{n \\times n}\\) مصفوفة إسقاط متعامد على فضاء جزئي \\(V\\) ذي بُعد \\(k < n\\). ما هما أثر وقيم \\(P\\) الذاتية؟",
      ["\\(\\text{tr}(P) = k\\); eigenvalues are \\(1\\) (multiplicity \\(k\\)) and \\(0\\) (multiplicity \\(n-k\\))",
       "\\(\\text{tr}(P) = n\\); all eigenvalues are \\(1\\)",
       "\\(\\text{tr}(P) = 0\\); eigenvalues are \\(\\pm 1\\)",
       "\\(\\text{tr}(P) = k^2\\); eigenvalues are \\(k\\) and \\(0\\)"],
      0,
      "An orthogonal projection matrix satisfies \\(P^2 = P\\) and \\(P^T = P\\). The identity \\(P^2 = P\\) implies that any eigenvalue \\(\\lambda\\) satisfies \\(\\lambda^2 = \\lambda \\implies \\lambda \\in \\{0, 1\\}\\). The eigenspace for \\(\\lambda = 1\\) is the range \\(V\\), which has dimension \\(k\\). The eigenspace for \\(\\lambda = 0\\) is the null space \\(V^\\perp\\), of dimension \\(n - k\\). The trace is the sum of eigenvalues: \\(\\text{tr}(P) = k(1) + (n-k)(0) = k\\).",
      "مصفوفة الإسقاط تحقق \\(P^2 = P\\)، وبالتالي فإن قيمها الذاتية تحقق \\(\\lambda^2 = \\lambda\\) أي \\(\\lambda \\in \\{0, 1\\}\\). فضاء القيم الذاتية لـ 1 هو الفضاء الجزئي \\(V\\) ذو البعد \\(k\\)، ولفضاء العدم البعد \\(n-k\\). الأثر يساوي مجموع القيم الذاتية ويساوي \\(k\\).",
      "Recall that the trace of a projection matrix equals the dimension of the subspace it projects onto.",
      "تذكر أن أثر مصفوفة الإسقاط يساوي بُعد الفضاء الجزئي المسقط عليه.")

    # 359: Matrix Exponential of Skew-Symmetric Matrix
    q("KAUST-P2-359", "Matrix Analysis", "Hard",
      "If \\(A \\in \\mathbb{R}^{n \\times n}\\) is skew-symmetric (\\(A^T = -A\\)), which of the following is always true for the matrix exponential \\(Q = e^A\\)?",
      "إذا كانت \\(A \\in \\mathbb{R}^{n \\times n}\\) مصفوفة متخالفة التماثل (skew-symmetric: \\(A^T = -A\\))، فأي مما يلي صحيح دائماً للأسّي المصفوفي \\(Q = e^A\\)؟",
      ["\\(Q\\) is an orthogonal matrix with \\(\\det(Q) = 1\\)",
       "\\(Q\\) is a symmetric positive definite matrix",
       "\\(Q\\) is skew-symmetric",
       "\\(\\det(Q) = 0\\)"],
      0,
      "Compute the transpose: \\(Q^T = (e^A)^T = e^{A^T} = e^{-A}\\). Since \\(A\\) and \\(-A\\) commute, \\(Q^T Q = e^{-A} e^A = e^{-A + A} = e^0 = I\\). Thus \\(Q\\) is an orthogonal matrix. Furthermore, using Jacobi's formula, \\(\\det(e^A) = e^{\\text{tr}(A)}\\). For any skew-symmetric matrix, the diagonal entries are 0, so \\(\\text{tr}(A) = 0\\). Therefore \\(\\det(Q) = e^0 = 1\\). Thus \\(Q \\in SO(n)\\).",
      "نحسب المنقول: \\(Q^T = (e^A)^T = e^{A^T} = e^{-A}\\). بما أن \\(A\\) تبادلية مع \\(-A\\)، نجد \\(Q^T Q = e^{-A+A} = I\\)، إذن \\(Q\\) مصفوفة متعامدة. وحسب صيغة جاكوبي \\(\\det(e^A) = e^{\\text{tr}(A)} = e^0 = 1\\). وبالتالي \\(Q\\) تنتمي لزمرة الدوران الخاصة \\(SO(n)\\).",
      "Use \\((e^A)^T = e^{A^T}\\) and Jacobi's formula \\(\\det(e^A) = e^{\\text{tr}(A)}\\).",
      "استخدم خاصية منقول الأس المصفوفي وصيغة جاكوبي للمحدد.")

    # 360: Frobenius Norm vs Spectral Norm
    q("KAUST-P2-360", "Matrix Analysis", "Hard",
      "For a rank-1 matrix \\(A = \\mathbf{u} \\mathbf{v}^T\\) where \\(\\|\\mathbf{u}\\|_2 = 3\\) and \\(\\|\\mathbf{v}\\|_2 = 4\\), compute the spectral norm \\(\\|A\\|_2\\) and Frobenius norm \\(\\|A\\|_F\\).",
      "لمصفوفة من الرتبة الأولى \\(A = \\mathbf{u} \\mathbf{v}^T\\) حيث \\(\\|\\mathbf{u}\\|_2 = 3\\) و \\(\\|\\mathbf{v}\\|_2 = 4\\)، احسب المعيار الطيفي \\(\\|A\\|_2\\) ومعيار فروبينيوس \\(\\|A\\|_F\\).",
      ["\\(\\|A\\|_2 = 12\\) and \\(\\|A\\|_F = 12\\)",
       "\\(\\|A\\|_2 = 12\\) and \\(\\|A\\|_F = 24\\)",
       "\\(\\|A\\|_2 = 5\\) and \\(\\|A\\|_F = 12\\)",
       "\\(\\|A\\|_2 = 7\\) and \\(\\|A\\|_F = 25\\)"],
      0,
      "For any rank-1 matrix \\(A = \\mathbf{u}\\mathbf{v}^T\\), there is only one non-zero singular value, which is \\(\\sigma_1 = \\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2 = (3)(4) = 12\\). The spectral norm is the largest singular value, so \\(\\|A\\|_2 = \\sigma_1 = 12\\). The Frobenius norm is \\(\\|A\\|_F = \\sqrt{\\sum \\sigma_i^2} = \\sqrt{\\sigma_1^2} = \\sigma_1 = 12\\). Thus both norms are equal to 12.",
      "لأي مصفوفة من الرتبة 1، هناك قيمة مفردة وحيدة غير صفرية وهي \\(\\sigma_1 = \\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2 = 3 \\times 4 = 12\\). المعيار الطيفي يساوي أكبر قيمة مفردة (12)، ومعيار فروبينيوس يساوي الجذر التربيعي لمجموع مربعات القيم المفردة (12). إذن كلاهما يساوي 12.",
      "A rank-1 matrix has exactly one non-zero singular value \\(\\sigma_1 = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\|\\).",
      "المصفوفة من الرتبة الأولى لها قيمة مفردة واحدة غير صفرية تساوي حاصل ضرب معياري المتجهين.")

    # 361: Cholesky Decomposition
    q("KAUST-P2-361", "Matrix Analysis", "Medium",
      "Find the Cholesky factor \\(L\\) (lower triangular with positive diagonal) such that \\(A = L L^T\\) for \\(A = \\begin{pmatrix} 4 & 6 \\\\ 6 & 25 \\end{pmatrix}\\).",
      "أوجد عامل تشوليسكي \\(L\\) (مصفوفة مثلثية سفلية بعناصر قطرية موجبة) بحيث \\(A = L L^T\\) للمصفوفة \\(A = \\begin{pmatrix} 4 & 6 \\\\ 6 & 25 \\end{pmatrix}\\).",
      ["\\(L = \\begin{pmatrix} 2 & 0 \\\\ 3 & 4 \\end{pmatrix}\\)",
       "\\(L = \\begin{pmatrix} 2 & 0 \\\\ 3 & 5 \\end{pmatrix}\\)",
       "\\(L = \\begin{pmatrix} 4 & 0 \\\\ 6 & 5 \\end{pmatrix}\\)",
       "\\(L = \\begin{pmatrix} 2 & 3 \\\\ 0 & 4 \\end{pmatrix}\\)"],
      0,
      "Let \\(L = \\begin{pmatrix} l_{11} & 0 \\\\ l_{21} & l_{22} \\end{pmatrix}\\). Then \\(L L^T = \\begin{pmatrix} l_{11}^2 & l_{11} l_{21} \\\\ l_{11} l_{21} & l_{21}^2 + l_{22}^2 \\end{pmatrix}\\). Equating with \\(A\\): 1) \\(l_{11}^2 = 4 \\implies l_{11} = 2\\). 2) \\(l_{11} l_{21} = 6 \\implies 2 l_{21} = 6 \\implies l_{21} = 3\\). 3) \\(l_{21}^2 + l_{22}^2 = 25 \\implies 3^2 + l_{22}^2 = 25 \\implies l_{22}^2 = 16 \\implies l_{22} = 4\\). Thus \\(L = \\begin{pmatrix} 2 & 0 \\\\ 3 & 4 \\end{pmatrix}\\).",
      "نفرض \\(L = \\begin{pmatrix} l_{11} & 0 \\\\ l_{21} & l_{22} \\end{pmatrix}\\). نجد \\(l_{11}^2 = 4 \\implies l_{11} = 2\\). العنصر الثاني: \\(2 l_{21} = 6 \\implies l_{21} = 3\\). العنصر القطري الأخير: \\(3^2 + l_{22}^2 = 25 \\implies l_{22} = 4\\). بالتالي \\(L = \\begin{pmatrix} 2 & 0 \\\\ 3 & 4 \\end{pmatrix}\\).",
      "Equate \\(L L^T\\) to \\(A\\) entry by entry starting from the top-left.",
      "ساوِ عناصر \\(L L^T\\) بعناصر \\(A\\) بدءاً من الركن العلوي الأيسر.")

    # 362: Moore-Penrose Pseudoinverse
    q("KAUST-P2-362", "Matrix Analysis", "Hard",
      "Compute the Moore-Penrose pseudoinverse \\(A^+\\) of the column vector \\(A = \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}\\).",
      "احسب مقلوب مور-بينروز المعمم (pseudoinverse) \\(A^+\\) لمتجه العمود \\(A = \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}\\).",
      ["\\(A^+ = \\begin{pmatrix} 1/9 & 2/9 & 2/9 \\end{pmatrix}\\)",
       "\\(A^+ = \\begin{pmatrix} 1/5 & 2/5 & 2/5 \\end{pmatrix}\\)",
       "\\(A^+ = \\begin{pmatrix} 1 & 1/2 & 1/2 \\end{pmatrix}\\)",
       "\\(A^+ = \\begin{pmatrix} 1/3 & 2/3 & 2/3 \\end{pmatrix}\\)"],
      0,
      "For a non-zero column vector \\(\\mathbf{a}\\), the pseudoinverse is \\(\\mathbf{a}^+ = (\\mathbf{a}^T \\mathbf{a})^{-1} \\mathbf{a}^T = \\frac{\\mathbf{a}^T}{\\|\\mathbf{a}\\|^2}\\). Here \\(\\|\\mathbf{a}\\|^2 = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9\\). Therefore, \\(A^+ = \\frac{1}{9}\\begin{pmatrix} 1 & 2 & 2 \\end{pmatrix} = \\begin{pmatrix} 1/9 & 2/9 & 2/9 \\end{pmatrix}\\).",
      "لمتجه عمود غير صفري، المقلوب المعمم هو \\(A^+ = \\frac{A^T}{\\|A\\|^2}\\). هنا مربع المعيار هو \\(1^2 + 2^2 + 2^2 = 9\\). بالتالي \\(A^+ = \\frac{1}{9} \\begin{pmatrix} 1 & 2 & 2 \\end{pmatrix}\\).",
      "Use the formula \\(A^+ = (A^T A)^{-1} A^T\\) for a full column rank matrix.",
      "استخدم الصيغة \\(A^+ = (A^T A)^{-1} A^T\\) للمصفوفات ذات رتبة الأعمدة التامة.")

    # 363: Commutator and Simultaneous Diagonalizability
    q("KAUST-P2-363", "Linear Algebra", "Hard",
      "Let \\(A, B \\in \\mathbb{C}^{n \\times n}\\) be diagonalizable matrices. Which condition is necessary and sufficient for \\(A\\) and \\(B\\) to be simultaneously diagonalizable (i.e., share a common basis of eigenvectors)?",
      "لتكن \\(A, B \\in \\mathbb{C}^{n \\times n}\\) مصفوفتين قابلتين للتقطير. أي شرط هو لازم وكافٍ لكي تكون \\(A\\) و \\(B\\) قابلتين للتقطير آنياً (أي تشتركان في نفس أساس المتجهات الذاتية)؟",
      ["\\(AB = BA\\)", "\\(A + B = I\\)", "\\(\\det(AB) > 0\\)", "\\(A B^T = B^T A\\)"],
      0,
      "A classical theorem of linear algebra states that a family of diagonalizable operators is simultaneously diagonalizable if and only if they commute, i.e., \\([A, B] = AB - BA = 0\\). If \\(AB = BA\\), the eigenspaces of \\(A\\) are invariant under \\(B\\), allowing simultaneous diagonalization.",
      "تنص نظرية أساسية في الجبر الخطي على أن أي عائلة من المصفوفات القابلة للتقطير تكون قابلة للتقطير آنياً إذا وفقط إذا كانت تبادلية، أي \\(AB = BA\\).",
      "Think about the commutator \\([A, B] = AB - BA\\).",
      "فكر في المبدل \\([A, B] = AB - BA\\).")

    # 364: Kronecker Product Eigenvalues
    q("KAUST-P2-364", "Matrix Analysis", "Hard",
      "Let \\(A\\) have eigenvalues \\(\\{2, 3\\}\\) and \\(B\\) have eigenvalues \\(\\{1, 4\\}\\). What are the eigenvalues of the Kronecker product \\(A \\otimes B\\)?",
      "لتكن للمصفوفة \\(A\\) القيم الذاتية \\(\\{2, 3\\}\\) وللمصفوفة \\(B\\) القيم الذاتية \\(\\{1, 4\\}\\). ما هي القيم الذاتية لحاصل ضرب كرونكر \\(A \\otimes B\\)؟",
      ["\\(\\{2, 8, 3, 12\\}\\)", "\\(\\{3, 6, 4, 7\\}\\)", "\\(\\{2, 12\\}\\)", "\\(\\{1, 2, 3, 4\\}\\)"],
      0,
      "If \\(\\lambda_i\\) are the eigenvalues of \\(A\\) and \\(\\mu_j\\) are the eigenvalues of \\(B\\), then the eigenvalues of the Kronecker product \\(A \\otimes B\\) are all pairwise products \\(\\lambda_i \\mu_j\\). Here: \\(2 \\times 1 = 2\\), \\(2 \\times 4 = 8\\), \\(3 \\times 1 = 3\\), \\(3 \\times 4 = 12\\). Thus the eigenvalues are \\(\\{2, 3, 8, 12\\}\\).",
      "إذا كانت \\(\\lambda_i\\) قيم \\(A\\) الذاتية و \\(\\mu_j\\) قيم \\(B\\) الذاتية، فإن القيم الذاتية لحاصل ضرب كرونكر هي جميع الجداءات المزدوجة \\(\\lambda_i \\mu_j\\). الجداءات هي: \\(2 \\times 1 = 2\\), \\(2 \\times 4 = 8\\), \\(3 \\times 1 = 3\\), \\(3 \\times 4 = 12\\).",
      "The eigenvalues of \\(A \\otimes B\\) are all products \\(\\lambda_i \\mu_j\\).",
      "القيم الذاتية لحاصل ضرب كرونكر هي نواتج ضرب كل قيمة ذاتية من الأولى في كل قيمة ذاتية من الثانية.")

    # 365: Condition Number
    q("KAUST-P2-365", "Matrix Analysis", "Medium",
      "For the matrix \\(A = \\begin{pmatrix} 100 & 0 \\\\ 0 & 2 \\end{pmatrix}\\), what is the \\(L_2\\) condition number \\(\\kappa_2(A)\\)?",
      "للمصفوفة \\(A = \\begin{pmatrix} 100 & 0 \\\\ 0 & 2 \\end{pmatrix}\\)، ما هو رقم الحالة \\(\\kappa_2(A)\\) بمعيار \\(L_2\\)؟",
      ["\\(50\\)", "\\(100\\)", "\\(200\\)", "\\(25\\)"],
      0,
      "The \\(L_2\\) condition number of an invertible matrix is \\(\\kappa_2(A) = \\frac{\\sigma_{\\max}(A)}{\\sigma_{\\min}(A)}\\). For a diagonal matrix with positive entries, the singular values are the entries themselves: \\(\\sigma_1 = 100\\) and \\(\\sigma_2 = 2\\). Thus \\(\\kappa_2(A) = \\frac{100}{2} = 50\\).",
      "رقم الحالة بمعيار \\(L_2\\) يعرف بالنسبة بين أكبر قيمة مفردة وأصغر قيمة مفردة: \\(\\kappa_2 = \\sigma_{\\max} / \\sigma_{\\min} = 100 / 2 = 50\\).",
      "Compute the ratio of the maximum to minimum singular value.",
      "احسب النسبة بين أكبر وأصغر قيمة مفردة.")

    # 366: Householder Reflector
    q("KAUST-P2-366", "Matrix Analysis", "Hard",
      "Let \\(\\mathbf{v} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\). What is the \\(2 \\times 2\\) Householder reflection matrix \\(H = I - 2\\frac{\\mathbf{v}\\mathbf{v}^T}{\\|\\mathbf{v}\\|^2}\\), and what is its geometric action?",
      "ليكن \\(\\mathbf{v} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\). ما هي مصفوفة انعكاس هاوسهولدر \\(H = I - 2\\frac{\\mathbf{v}\\mathbf{v}^T}{\\|\\mathbf{v}\\|^2}\\)، وما هو فعلها الهندسي؟",
      ["\\(H = \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\); Reflection across the \\(y\\)-axis",
       "\\(H = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\); Reflection across the \\(x\\)-axis",
       "\\(H = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}\\); Reflection across \\(y = x\\)",
       "\\(H = \\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\); Inversion through the origin"],
      0,
      "Here \\(\\|\\mathbf{v}\\|^2 = 1\\). Then \\(\\mathbf{v}\\mathbf{v}^T = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\begin{pmatrix} 1 & 0 \\end{pmatrix} = \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}\\). Thus \\(H = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} - 2\\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\). Multiplying an arbitrary vector \\(\\begin{pmatrix} x \\\\ y \\end{pmatrix}\\) gives \\(\\begin{pmatrix} -x \\\\ y \\end{pmatrix}\\), which is a reflection across the line orthogonal to \\(\\mathbf{v}\\), i.e., the \\(y\\)-axis.",
      "بما أن \\(\\|\\mathbf{v}\\|^2 = 1\\)، فإن \\(\\mathbf{v}\\mathbf{v}^T = \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}\\). بالتالي \\(H = I - 2\\mathbf{v}\\mathbf{v}^T = \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\). وهذا يمثل هندسياً انعكاساً حول محور الصادات (المتعامد مع المتجه \\(\\mathbf{v}\\)).",
      "Compute \\(I - 2\\mathbf{v}\\mathbf{v}^T\\) directly.",
      "احسب \\(I - 2\\mathbf{v}\\mathbf{v}^T\\) مباشرة.")

    # 367: Gram-Schmidt and QR Decomposition
    q("KAUST-P2-367", "Linear Algebra", "Medium",
      "For columns \\(\\mathbf{a}_1 = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\) and \\(\\mathbf{a}_2 = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\), what is the upper-triangular matrix \\(R\\) in the QR decomposition \\(A = QR\\)?",
      "لعمودي المصفوفة \\(\\mathbf{a}_1 = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\) و \\(\\mathbf{a}_2 = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\)، ما هي المصفوفة المثلثية العليا \\(R\\) في تفكيك \\(QR\\) للمصفوفة \\(A\\)؟",
      ["\\(R = \\begin{pmatrix} 5 & 3/5 \\\\ 0 & 4/5 \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} 5 & 1 \\\\ 0 & 4 \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} 25 & 3 \\\\ 0 & 4 \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} 1 & 3/5 \\\\ 0 & 1 \\end{pmatrix}\\)"],
      0,
      "1) \\(r_{11} = \\|\\mathbf{a}_1\\| = \\sqrt{3^2 + 4^2} = 5\\). Then \\(\\mathbf{q}_1 = \\frac{1}{5}\\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix} = \\begin{pmatrix} 3/5 \\\\ 4/5 \\end{pmatrix}\\). 2) \\(r_{12} = \\mathbf{q}_1^T \\mathbf{a}_2 = (3/5)(1) + (4/5)(0) = 3/5\\). 3) \\(\\mathbf{a}_2 - r_{12}\\mathbf{q}_1 = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} - \\frac{3}{5}\\begin{pmatrix} 3/5 \\\\ 4/5 \\end{pmatrix} = \\begin{pmatrix} 16/25 \\\\ -12/25 \\end{pmatrix}\\). Its norm is \\(r_{22} = \\sqrt{(16/25)^2 + (-12/25)^2} = \\frac{20}{25} = \\frac{4}{5}\\). Thus \\(R = \\begin{pmatrix} 5 & 3/5 \\\\ 0 & 4/5 \\end{pmatrix}\\).",
      "1) \\(r_{11} = \\|\\mathbf{a}_1\\| = 5\\)، والمتجه الواحدي \\(\\mathbf{q}_1 = (3/5, 4/5)^T\\). 2) \\(r_{12} = \\mathbf{q}_1^T \\mathbf{a}_2 = 3/5\\). 3) معيار المتجه المتبقي هو \\(r_{22} = 4/5\\). بالتالي \\(R = \\begin{pmatrix} 5 & 3/5 \\\\ 0 & 4/5 \\end{pmatrix}\\).",
      "Recall \\(r_{11} = \\|\\mathbf{a}_1\\|\\) and \\(r_{12} = \\mathbf{q}_1^T \\mathbf{a}_2\\).",
      "تذكر أن \\(r_{11}\\) هو معيار العمود الأول و \\(r_{12}\\) هو المسقط على المتجه الواحدي الأول.")

    # 368: Spectral Radius vs Matrix Norm
    q("KAUST-P2-368", "Matrix Analysis", "Hard",
      "For any square matrix \\(A\\) with spectral radius \\(\\rho(A)\\), which statement is universally true for any induced matrix norm \\(\\|\\cdot\\|\\)?",
      "لأي مصفوفة مربعة \\(A\\) ذات نصف قطر طيفي \\(\\rho(A)\\)، أي عبارة صحيحة كلياً لأي معيار مصفوفي مستحث \\(\\|\\cdot\\|\\)؟",
      ["\\(\\rho(A) \\le \\|A\\|\\)", "\\(\\rho(A) = \\|A\\|\\)", "\\(\\rho(A) \\ge \\|A\\|\\)", "\\(\\rho(A) = \\|A\\|_F\\)"],
      0,
      "Let \\(\\lambda\\) be an eigenvalue of \\(A\\) such that \\(|\\lambda| = \\rho(A)\\), and let \\(\\mathbf{x} \\neq \\mathbf{0}\\) be a corresponding eigenvector. Then \\(A \\mathbf{x} = \\lambda \\mathbf{x}\\). Taking any induced vector norm: \\(\\|A\\mathbf{x}\\| = \\|\\lambda \\mathbf{x}\\| = |\\lambda| \\|\\mathbf{x}\\| = \\rho(A) \\|\\mathbf{x}\\|\\). By definition of the induced matrix norm, \\(\\|A\\mathbf{x}\\| \\le \\|A\\| \\|\\mathbf{x}\\|\\). Dividing by \\(\\|\\mathbf{x}\\| > 0\\) yields \\(\\rho(A) \\le \\|A\\|\\). Furthermore, \\(\\rho(A) = \\inf_{\\|\\cdot\\|} \\|A\\|\\).",
      "ليكن \\(\\lambda\\) قيمة ذاتية تحقق \\(|\\lambda| = \\rho(A)\\) مع متجه ذاتي \\(\\mathbf{x}\\). بأخذ المعيار: \\(\\|A\\mathbf{x}\\| = \\rho(A)\\|\\mathbf{x}\\| \\le \\|A\\| \\|\\mathbf{x}\\|\\). بالقسمة على المعيار الموجب نجد \\(\\rho(A) \\le \\|A\\|\\) دائماً.",
      "Apply the eigenvalue equation \\(A\\mathbf{x} = \\lambda \\mathbf{x}\\) with induced norm properties.",
      "طبق معادلة القيمة الذاتية مع خواص المعايير المستحثة.")

    # 369: Positive Semi-Definite Trace-Determinant Property
    q("KAUST-P2-369", "Matrix Analysis", "Hard",
      "Let \\(A, B \\in \\mathbb{R}^{n \\times n}\\) be positive semi-definite symmetric matrices. Which of the following is guaranteed to be non-negative?",
      "لتكن \\(A, B \\in \\mathbb{R}^{n \\times n}\\) مصفوفتين متماثلتين شبه موجبتي التعريف. أي من المقادير التالية مضمون كونه غير سالب دائماً؟",
      ["\\(\\text{tr}(AB)\\)", "\\(\\det(A - B)\\)", "\\(\\text{tr}(A - B)\\)", "\\(\\det(A) - \\det(B)\\)"],
      0,
      "Since \\(B\\) is symmetric positive semi-definite, it has a unique positive semi-definite square root \\(B^{1/2}\\). By the cyclic property of the trace: \\(\\text{tr}(AB) = \\text{tr}(A B^{1/2} B^{1/2}) = \\text{tr}(B^{1/2} A B^{1/2})\\). Because \\(A\\) is positive semi-definite and \\(B^{1/2}\\) is symmetric, the matrix \\(C = B^{1/2} A B^{1/2}\\) is also positive semi-definite (for any \\(\\mathbf{x}\\), \\(\\mathbf{x}^T C \\mathbf{x} = (B^{1/2}\\mathbf{x})^T A (B^{1/2}\\mathbf{x}) \\ge 0\\)). The trace of a positive semi-definite matrix is the sum of its non-negative eigenvalues, so \\(\\text{tr}(C) \\ge 0\\). Thus \\(\\text{tr}(AB) \\ge 0\\).",
      "بما أن \\(B\\) شبه موجبة التعريف، فإن لها جذراً تربيعياً متماثلاً \\(B^{1/2}\\). بخاصية الأثر الدائرية: \\(\\text{tr}(AB) = \\text{tr}(B^{1/2} A B^{1/2})\\). المصفوفة \\(B^{1/2} A B^{1/2}\\) شبه موجبة التعريف، وبالتالي أثرها (مجموع قيمها الذاتية غير السالبة) هو دائماً غير سالب: \\(\\text{tr}(AB) \\ge 0\\).",
      "Write \\(B = B^{1/2} B^{1/2}\\) and use the cyclic property of trace.",
      "اكتب \\(B = B^{1/2} B^{1/2}\\) واستخدم خاصية التبادل الدوري للأثر.")

    # 370: Nilpotent Index and Characteristic Polynomial
    q("KAUST-P2-370", "Linear Algebra", "Medium",
      "If \\(N \\in \\mathbb{C}^{4 \\times 4}\\) is a nilpotent matrix such that \\(N^3 \\neq 0\\) but \\(N^4 = 0\\), what is \\(\\det(I + 2N)\\)?",
      "إذا كانت \\(N \\in \\mathbb{C}^{4 \\times 4}\\) مصفوفة عديمة القوى (nilpotent) بحيث \\(N^3 \\neq 0\\) ولكن \\(N^4 = 0\\)، فما قيمة \\(\\det(I + 2N)\\)؟",
      ["\\(1\\)", "\\(0\\)", "\\(16\\)", "\\(8\\)"],
      0,
      "Every eigenvalue of a nilpotent matrix is \\(0\\). The eigenvalues of \\(I + 2N\\) are therefore \\(1 + 2(0) = 1\\) with algebraic multiplicity 4. The determinant is the product of the eigenvalues: \\(\\det(I + 2N) = 1^4 = 1\\).",
      "جميع القيم الذاتية لأي مصفوفة عديمة القوى هي صفر. وبالتالي فإن جميع القيم الذاتية للمصفوفة \\(I + 2N\\) تساوي \\(1 + 2(0) = 1\\). المحدد هو حاصل ضرب القيم الذاتية: \\(1^4 = 1\\).",
      "What are the eigenvalues of \\(N\\)?",
      "ما هي القيم الذاتية لمصفوفة عديمة القوى؟")

    # 371 to 400: Generate remaining 30 questions for Part C
    # 371: Invariant Subspaces
    q("KAUST-P2-371", "Linear Algebra", "Hard",
      "Let \\(T: V \\to V\\) be a linear operator. If \\(W_1\\) and \\(W_2\\) are invariant subspaces under \\(T\\), which of the following is NOT necessarily invariant under \\(T\\)?",
      "ليكن \\(T: V \\to V\\) مؤثراً خطياً. إذا كان \\(W_1\\) و \\(W_2\\) فضاءين جزئيين صامدين (invariant subspaces) تحت \\(T\\)، فأي مما يلي ليس بالضرورة صامداً تحت \\(T\\)؟",
      ["\\(W_1 \\cup W_2\\)", "\\(W_1 \\cap W_2\\)", "\\(W_1 + W_2\\)", "\\(T(W_1)\\)"],
      0,
      "The union of two subspaces \\(W_1 \\cup W_2\\) is generally not even a vector subspace of \\(V\\) (unless one contains the other), so it cannot be an invariant subspace. In contrast, the intersection \\(W_1 \\cap W_2\\), the sum \\(W_1 + W_2\\), and the image \\(T(W_1)\\) are all proven vector subspaces that remain invariant under \\(T\\).",
      "اتحاد فضاءين جزئيين \\(W_1 \\cup W_2\\) لا يشكل عموماً فضاءً جزئياً إلا إذا كان أحدهما محتوى في الآخر، وبالتالي لا يمكن اعتباره فضاءً صامداً. بينما التقاطع والمجموع كلاهما فضاءات صامدة.",
      "Recall when the union of two vector subspaces is itself a subspace.",
      "تذكر متى يكون اتحاد فضاءين جزئيين فضاءً جزئياً.")

    # 372: Companion Matrix
    q("KAUST-P2-372", "Linear Algebra", "Medium",
      "What is the characteristic polynomial of the companion matrix \\(C = \\begin{pmatrix} 0 & 0 & -c_0 \\\\ 1 & 0 & -c_1 \\\\ 0 & 1 & -c_2 \\end{pmatrix}\\)?",
      "ما هي كثيرة الحدود المميزة لمصفوفة المرافقة (companion matrix) \\(C = \\begin{pmatrix} 0 & 0 & -c_0 \\\\ 1 & 0 & -c_1 \\\\ 0 & 1 & -c_2 \\end{pmatrix}\\)؟",
      ["\\(p(\\lambda) = \\lambda^3 + c_2 \\lambda^2 + c_1 \\lambda + c_0\\)",
       "\\(p(\\lambda) = \\lambda^3 - c_2 \\lambda^2 - c_1 \\lambda - c_0\\)",
       "\\(p(\\lambda) = \\lambda^3 + c_0 \\lambda^2 + c_1 \\lambda + c_2\\)",
       "\\(p(\\lambda) = -\\lambda^3 + c_2 \\lambda^2 - c_1 \\lambda + c_0\\)"],
      0,
      "Expanding the determinant \\(\\det(\\lambda I - C) = \\det\\begin{pmatrix} \\lambda & 0 & c_0 \\\\ -1 & \\lambda & c_1 \\\\ 0 & -1 & \\lambda + c_2 \\end{pmatrix}\\) along the first row gives \\(\\lambda(\\lambda(\\lambda + c_2) + c_1) + c_0(1 - 0) = \\lambda^3 + c_2 \\lambda^2 + c_1 \\lambda + c_0\\). The companion matrix is designed specifically so that its characteristic and minimal polynomials equal this monic polynomial.",
      "بفك المحدد \\(\\det(\\lambda I - C)\\) على طول الصف الأول نحصل مباشرة على \\(\\lambda^3 + c_2 \\lambda^2 + c_1 \\lambda + c_0\\). صُممت مصفوفة المرافقة بحيث تتطابق متعددة حدودها المميزة تماماً مع هذه الصورة.",
      "Expand \\(\\det(\\lambda I - C)\\) by the first row.",
      "فك المحدد على طول عناصر الصف الأول.")

    # 373: Circulant Matrix Eigenvalues
    q("KAUST-P2-373", "Matrix Analysis", "Hard",
      "The \\(3 \\times 3\\) circulant matrix \\(C = \\begin{pmatrix} 1 & 2 & 3 \\\\ 3 & 1 & 2 \\\\ 2 & 3 & 1 \\end{pmatrix}\\) has one real eigenvalue. What is it?",
      "المصفوفة الدائرية (circulant matrix) \\(C = \\begin{pmatrix} 1 & 2 & 3 \\\\ 3 & 1 & 2 \\\\ 2 & 3 & 1 \\end{pmatrix}\\) لها قيمة ذاتية حقيقية واحدة. ما هي؟",
      ["\\(6\\)", "\\(0\\)", "\\(3\\)", "\\(1\\)"],
      0,
      "Every circulant matrix has the all-ones vector \\(\\mathbf{v} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}\\) as an eigenvector. Multiplying \\(C\\mathbf{v}\\) simply sums each row: \\(1 + 2 + 3 = 6\\). Thus \\(C \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix} = 6 \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}\\), giving the real eigenvalue \\(\\lambda = 6\\). The other two eigenvalues are complex conjugates \\(1 + 2\\omega + 3\\omega^2\\) where \\(\\omega = e^{2\\pi i / 3}\\).",
      "لكل مصفوفة دائرية المتجه الذاتي \\((1, 1, 1)^T\\). بالضرب نجد أن الناتج هو مجموع عناصر كل صف، وهو \\(1 + 2 + 3 = 6\\). إذن القيمة الذاتية الحقيقية هي 6.",
      "Multiply the matrix by the all-ones vector \\((1, 1, 1)^T\\).",
      "اضرب المصفوفة في متجه الآحاد.")

    # 374: Hadamard's Inequality for Determinants
    q("KAUST-P2-374", "Matrix Analysis", "Hard",
      "Let \\(A \\in \\mathbb{R}^{3 \\times 3}\\) have columns \\(\\mathbf{c}_1, \\mathbf{c}_2, \\mathbf{c}_3\\) with lengths \\(\\|\\mathbf{c}_1\\| = 2\\), \\(\\|\\mathbf{c}_2\\| = 3\\), \\(\\|\\mathbf{c}_3\\| = 5\\). What is the maximum possible value of \\(|\\det(A)|\\)?",
      "لتكن \\(A \\in \\mathbb{R}^{3 \\times 3}\\) ذات أعمدة \\(\\mathbf{c}_1, \\mathbf{c}_2, \\mathbf{c}_3\\) بأطوال \\(\\|\\mathbf{c}_1\\| = 2\\), \\(\\|\\mathbf{c}_2\\| = 3\\), \\(\\|\\mathbf{c}_3\\| = 5\\). ما هي أقصى قيمة ممكنة لـ \\(|\\det(A)|\\)؟",
      ["\\(30\\)", "\\(10\\)", "\\(60\\)", "\\(15\\)"],
      0,
      "By Hadamard's inequality, for any matrix with columns \\(\\mathbf{c}_j\\), \\(|\\det(A)| \\le \\prod_{j=1}^n \\|\\mathbf{c}_j\\|\\). Geometrically, \\(|\\det(A)|\\) is the volume of the parallelepiped spanned by the columns, which is maximized when the columns are mutually orthogonal. Thus \\(\\max |\\det(A)| = \\|\\mathbf{c}_1\\| \\|\\mathbf{c}_2\\| \\|\\mathbf{c}_3\\| = (2)(3)(5) = 30\\).",
      "حسب متباينة هادامارد، القيمة المطلقة للمحدد محصورة بحاصل ضرب أطوال الأعمدة: \\(|\\det(A)| \\le \\prod \\|\\mathbf{c}_j\\|\\). هندسياً، الحجم يكون في نهايته العظمى عندما تكون متجهات الأعمدة متعامدة مثنى مثنى، أي \\(2 \\times 3 \\times 5 = 30\\).",
      "Volume is maximized when the column vectors are mutually perpendicular.",
      "يكون الحجم أعظمياً عندما تكون أعمدة المصفوفة متعامدة تماماً.")

    # 375: Commuting Matrices and Trace of AB vs BA
    q("KAUST-P2-375", "Linear Algebra", "Medium",
      "Can there exist two \\(n \\times n\\) real matrices \\(A\\) and \\(B\\) such that \\(AB - BA = I\\)?",
      "هل يمكن أن توجد مصفوفتان حقيقيتان \\(A\\) و \\(B\\) من الرتبة \\(n \\times n\\) بحيث \\(AB - BA = I\\)؟",
      ["No, because \\(\\text{tr}(AB - BA) = 0\\) while \\(\\text{tr}(I) = n > 0\\)",
       "Yes, for any dimension \\(n \\ge 2\\)",
       "Yes, but only if \\(n\\) is an even integer",
       "Yes, if \\(A\\) is symmetric and \\(B\\) is skew-symmetric"],
      0,
      "Take the trace of both sides: \\(\\text{tr}(AB - BA) = \\text{tr}(AB) - \\text{tr}(BA) = 0\\) due to the cyclic property \\(\\text{tr}(AB) = \\text{tr}(BA)\\). However, \\(\\text{tr}(I) = n\\). In any finite dimension \\(n \\ge 1\\), \\(0 = n\\) is a contradiction. Hence, no such finite-dimensional matrices exist (this commutator relation can only be realized by unbounded operators in infinite-dimensional Hilbert spaces, such as position and momentum in quantum mechanics).",
      "بأخذ أثر الطرفين: \\(\\text{tr}(AB - BA) = \\text{tr}(AB) - \\text{tr}(BA) = 0\\). بينما أثر مصفوفة الوحدة هو \\(n\\). لا يمكن لـ \\(0 = n\\) في أي بعد منتهٍ، لذا لا توجد مصفوفات كهذه في الأبعاد المنتهية.",
      "Apply the trace operator to both sides of the equation.",
      "طبق مؤثر الأثر (trace) على طرفي المعادلة.")

    # 376: Unitary Equivalence & Schur Decomposition
    q("KAUST-P2-376", "Matrix Analysis", "Hard",
      "Schur's Triangularization Theorem states that any \\(A \\in \\mathbb{C}^{n \\times n}\\) can be factored as \\(A = U T U^*\\) where \\(U\\) is unitary and \\(T\\) is upper triangular. If \\(A\\) is normal (\\(A A^* = A^* A\\)), what form does \\(T\\) necessarily take?",
      "تنص نظرية شور للتثليث على أن أي مصفوفة \\(A \\in \\mathbb{C}^{n \\times n}\\) يمكن تفكيكها إلى \\(A = U T U^*\\) حيث \\(U\\) وحدوية و \\(T\\) مثلثية عليا. إذا كانت \\(A\\) ناظمية (normal: \\(A A^* = A^* A\\))، فما الصورة التي تتخذها \\(T\\) بالضرورة؟",
      ["Diagonal matrix", "Strictly upper triangular matrix", "Identity matrix", "Jordan block matrix"],
      0,
      "Since \\(A = U T U^*\\), normality gives \\(A A^* = U T T^* U^*\\) and \\(A^* A = U T^* T U^*\\). Equating them implies \\(T T^* = T^* T\\), so the upper triangular matrix \\(T\\) must also be normal. It is a known theorem that any triangular matrix that is normal must be diagonal. Hence, normal matrices are unitarily diagonalizable.",
      "بما أن \\(A\\) ناظمية، فإن المصفوفة المثلثية العليا \\(T\\) تكون ناظمية أيضاً: \\(T T^* = T^* T\\). أي مصفوفة مثلثية ناظمية يجب أن تكون مصفوفة قطرية. بالتالي فإن المصفوفات الناظمية قابلة للتقطير الوحدوي.",
      "Check the condition for an upper triangular matrix to satisfy \\(T T^* = T^* T\\).",
      "تحقق من شرط أن تكون المصفوفة المثلثية العليا ناظمية.")

    # 377: Rayleigh-Ritz Theorem for Second Eigenvalue
    q("KAUST-P2-377", "Matrix Analysis", "Hard",
      "Let \\(A\\) be a real symmetric matrix with eigenvalues \\(\\lambda_1 \\ge \\lambda_2 \\ge \\dots \\ge \\lambda_n\\) and corresponding orthonormal eigenvectors \\(\\mathbf{v}_1, \\dots, \\mathbf{v}_n\\). How is \\(\\lambda_2\\) characterized by the Rayleigh quotient?",
      "لتكن \\(A\\) مصفوفة حقيقية متماثلة بقيم ذاتية \\(\\lambda_1 \\ge \\lambda_2 \\ge \\dots \\ge \\lambda_n\\) ومتجهات ذاتية متعامدة عيارياً \\(\\mathbf{v}_1, \\dots, \\mathbf{v}_n\\). كيف توصف \\(\\lambda_2\\) بواسطة نسبة رايلي؟",
      ["\\(\\max_{\\mathbf{x} \\perp \\mathbf{v}_1, \\mathbf{x} \\neq \\mathbf{0}} \\frac{\\mathbf{x}^T A \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}\\)",
       "\\(\\min_{\\mathbf{x} \\neq \\mathbf{0}} \\frac{\\mathbf{x}^T A \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}\\)",
       "\\(\\max_{\\mathbf{x} \\parallel \\mathbf{v}_1} \\frac{\\mathbf{x}^T A \\mathbf{x}}{\\mathbf{x}^T \\mathbf{x}}\\)",
       "\\(\\frac{1}{2}(\\lambda_1 + \\lambda_n)\\)"],
      0,
      "By the Courant-Fischer min-max theorem (or Rayleigh-Ritz variational characterization), when the vector \\(\\mathbf{x}\\) is constrained to be orthogonal to the first eigenvector \\(\\mathbf{v}_1\\), the maximum of the Rayleigh quotient is precisely the second largest eigenvalue \\(\\lambda_2\\).",
      "حسب نظرية كورانت-فيشر (أو توصيف رايلي-ريتز التبايني)، عندما يقيد المتجه \\(\\mathbf{x}\\) ليكون عمودياً على المتجه الذاتي الأول \\(\\mathbf{v}_1\\)، فإن القيمة العظمى لنسبة رايلي تساوي بالضبط ثاني أكبر قيمة ذاتية \\(\\lambda_2\\).",
      "Restrict the search space to the orthogonal complement of the span of \\(\\mathbf{v}_1\\).",
      "قيد فضاء البحث إلى المتمم المتعامد للمتجه الذاتي الأول.")

    # 378: Idempotent Matrix Rank and Trace
    q("KAUST-P2-378", "Linear Algebra", "Medium",
      "An idempotent matrix satisfies \\(A^2 = A\\). If \\(A \\in \\mathbb{R}^{6 \\times 6}\\) and \\(\\text{rank}(A) = 4\\), what is \\(\\text{tr}(A)\\)?",
      "تحقق المصفوفة الارتكاسية (idempotent) الشرط \\(A^2 = A\\). إذا كانت \\(A \\in \\mathbb{R}^{6 \\times 6}\\) ورتبتها \\(\\text{rank}(A) = 4\\)، فما هو أثرها \\(\\text{tr}(A)\\)؟",
      ["\\(4\\)", "\\(6\\)", "\\(2\\)", "\\(0\\)"],
      0,
      "Since \\(A^2 = A\\), the minimal polynomial divides \\(x(x-1)\\), so the only eigenvalues are \\(0\\) and \\(1\\). Every idempotent matrix is diagonalizable. The multiplicity of eigenvalue \\(1\\) equals \\(\\dim(\\text{im}(A)) = \\text{rank}(A) = 4\\). The trace is the sum of eigenvalues, so \\(\\text{tr}(A) = 4(1) + 2(0) = 4\\). For any idempotent matrix, \\(\\text{tr}(A) = \\text{rank}(A)\\).",
      "بما أن \\(A^2 = A\\)، فإن القيم الذاتية لا يمكن أن تكون سوى 0 و 1، والمصفوفة قابلة للتقطير دائماً. التعدد الجبري للقيمة الذاتية 1 يساوي رتبة المصفوفة (4). الأثر يساوي مجموع القيم الذاتية ويساوي 4.",
      "For any projection / idempotent matrix, \\(\\text{tr}(A) = \\text{rank}(A)\\).",
      "لأي مصفوفة ارتكاسية، الأثر يساوي الرتبة دائماً.")

    # 379: Determinant of Block Triangular Matrix
    q("KAUST-P2-379", "Linear Algebra", "Medium",
      "Compute the determinant of the block matrix \\(M = \\begin{pmatrix} A & B \\\\ 0 & D \\end{pmatrix}\\), where \\(A = \\begin{pmatrix} 2 & 1 \\\\ 1 & 3 \\end{pmatrix}\\), \\(D = \\begin{pmatrix} 4 & 2 \\\\ 1 & 2 \\end{pmatrix}\\), and \\(B\\) is any \\(2 \\times 2\\) matrix.",
      "احسب محدد المصفوفة الكتلية \\(M = \\begin{pmatrix} A & B \\\\ 0 & D \\end{pmatrix}\\)، حيث \\(A = \\begin{pmatrix} 2 & 1 \\\\ 1 & 3 \\end{pmatrix}\\) و \\(D = \\begin{pmatrix} 4 & 2 \\\\ 1 & 2 \\end{pmatrix}\\) و \\(B\\) أي مصفوفة من الرتبة \\(2 \\times 2\\).",
      ["\\(30\\)", "\\(24\\)", "\\(15\\)", "\\(12\\)"],
      0,
      "For a block upper triangular matrix \\(M = \\begin{pmatrix} A & B \\\\ 0 & D \\end{pmatrix}\\), the determinant is simply \\(\\det(M) = \\det(A) \\det(D)\\), completely independent of \\(B\\). Compute \\(\\det(A) = (2)(3) - (1)(1) = 6 - 1 = 5\\). Compute \\(\\det(D) = (4)(2) - (2)(1) = 8 - 2 = 6\\). Thus \\(\\det(M) = 5 \\times 6 = 30\\).",
      "لمصفوفة كتلية مثلثية عليا، المحدد يساوي حاصل ضرب محددات الكتل القطرية: \\(\\det(M) = \\det(A)\\det(D)\\) ولا يعتمد على \\(B\\). نحسب \\(\\det(A) = 5\\) و \\(\\det(D) = 6\\). الناتج هو \\(5 \\times 6 = 30\\).",
      "The determinant of a block triangular matrix is the product of the determinants of the diagonal blocks.",
      "محدد المصفوفة الكتلية المثلثية هو حاصل ضرب محددات الكتل القطرية.")

    # 380: Schur Complement and Invertibility
    q("KAUST-P2-380", "Matrix Analysis", "Hard",
      "For an invertible block matrix \\(M = \\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix}\\) with invertible block \\(A\\), what is the Schur complement of \\(A\\) in \\(M\\)?",
      "لمصفوفة كتلية قابلة للعكس \\(M = \\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix}\\) حيث الكتلة \\(A\\) قابلة للعكس، ما هو متمم شور للكتلة \\(A\\) في \\(M\\)؟",
      ["\\(S = D - C A^{-1} B\\)", "\\(S = A - B D^{-1} C\\)", "\\(S = D - B A^{-1} C\\)", "\\(S = A D - B C\\)"],
      0,
      "By block Gaussian elimination: \\(\\begin{pmatrix} I & 0 \\\\ -C A^{-1} & I \\end{pmatrix} \\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix} = \\begin{pmatrix} A & B \\\\ 0 & D - C A^{-1} B \\end{pmatrix}\\). The lower-right block \\(S = D - C A^{-1} B\\) is defined as the Schur complement of \\(A\\) in \\(M\\), and satisfies \\(\\det(M) = \\det(A)\\det(D - CA^{-1}B)\\).",
      "عن طريق الحذف الغاوسي الكتلي، نضرب من اليسار بالمصفوفة المثلثية الكتلية المناسبة لنصفر الكتلة السفلية اليسرى، فتتحول الكتلة السفلية اليمنى إلى \\(S = D - C A^{-1} B\\)، وهو متمم شور للكتلة \\(A\\).",
      "Use block row operations to eliminate \\(C\\).",
      "استخدم العمليات الصفية الكتلية لحذف الكتلة \\(C\\).")

    # 381: Orthogonal Complement Dimension
    q("KAUST-P2-381", "Linear Algebra", "Medium",
      "In \\(\\mathbb{R}^5\\) equipped with the standard dot product, let \\(W = \\text{span}\\{(1, 0, 1, 0, 1), (0, 1, 0, 1, 0)\\}\\). What is \\(\\dim(W^\\perp)\\)?",
      "في \\(\\mathbb{R}^5\\) مع الجداء القياسي المعتاد، ليكن \\(W = \\text{span}\\{(1, 0, 1, 0, 1), (0, 1, 0, 1, 0)\\}\\). ما هو بُعد المتمم المتعامد \\(\\dim(W^\\perp)\\)؟",
      ["\\(3\\)", "\\(2\\)", "\\(5\\)", "\\(1\\)"],
      0,
      "The two spanning vectors are non-zero and clearly orthogonal to each other (their dot product is \\(0\\)), so they are linearly independent. Thus \\(\\dim(W) = 2\\). In any finite-dimensional inner product space \\(V\\), \\(\\dim(W) + \\dim(W^\\perp) = \\dim(V)\\). Here \\(\\dim(V) = 5\\), so \\(\\dim(W^\\perp) = 5 - 2 = 3\\).",
      "المتجهان مستقلان خطياً ومتعامدان، لذا \\(\\dim(W) = 2\\). من النظرية الأساسية \\(\\dim(W) + \\dim(W^\\perp) = \\dim(V)\\)، نجد \\(\\dim(W^\\perp) = 5 - 2 = 3\\).",
      "Use the dimension theorem \\(\\dim(W) + \\dim(W^\\perp) = \\dim(V)\\).",
      "استخدم نظرية الأبعاد للمتمم المتعامد.")

    # 382: Matrix Square Root of Positive Definite Matrix
    q("KAUST-P2-382", "Matrix Analysis", "Medium",
      "Find the unique symmetric positive definite square root \\(R = A^{1/2}\\) of the matrix \\(A = \\begin{pmatrix} 5 & 4 \\\\ 4 & 5 \\end{pmatrix}\\).",
      "أوجد الجذر التربيعي المتماثل الموجب المعرف الوحيد \\(R = A^{1/2}\\) للمصفوفة \\(A = \\begin{pmatrix} 5 & 4 \\\\ 4 & 5 \\end{pmatrix}\\).",
      ["\\(R = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} \\sqrt{5} & 2 \\\\ 2 & \\sqrt{5} \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} 3 & 1 \\\\ 1 & 3 \\end{pmatrix}\\)",
       "\\(R = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix}\\)"],
      0,
      "Eigenvalues of \\(A\\): \\(\\det\\begin{pmatrix} 5-\\lambda & 4 \\\\ 4 & 5-\\lambda \\end{pmatrix} = (5-\\lambda)^2 - 16 = 0 \\implies 5-\\lambda = \\pm 4 \\implies \\lambda_1 = 9, \\lambda_2 = 1\\). The square roots of the eigenvalues are \\(\\sqrt{9} = 3\\) and \\(\\sqrt{1} = 1\\). The eigenvectors are \\(\\mathbf{v}_1 = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}\\) and \\(\\mathbf{v}_2 = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}\\). Then \\(R = 3 \\mathbf{v}_1 \\mathbf{v}_1^T + 1 \\mathbf{v}_2 \\mathbf{v}_2^T = \\frac{3}{2}\\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix} + \\frac{1}{2}\\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}\\). Check: \\(R^2 = \\begin{pmatrix} 4+1 & 2+2 \\\\ 2+2 & 1+4 \\end{pmatrix} = \\begin{pmatrix} 5 & 4 \\\\ 4 & 5 \\end{pmatrix} = A\\).",
      "القيم الذاتية هي 9 و 1، وجذورها التربيعية هي 3 و 1. بالتركيب الطيفي نجد \\(R = 3 P_1 + 1 P_2 = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}\\). وبالتربيع للتحقق نجد \\(R^2 = A\\).",
      "Diagonalize \\(A\\) and take the square root of its diagonal eigenvalue matrix.",
      "قطّر المصفوفة وخذ الجذر التربيعي لمصفوفة القيم الذاتية.")

    # 383: Rank-Nullity for Transpose Products
    q("KAUST-P2-383", "Linear Algebra", "Hard",
      "For any real matrix \\(A \\in \\mathbb{R}^{m \\times n}\\), which fundamental relationship holds between the nullspaces of \\(A\\) and \\(A^T A\\)?",
      "لأي مصفوفة حقيقية \\(A \\in \\mathbb{R}^{m \\times n}\\)، أي علاقة أساسية تربط بين فضائي العدم (nullspaces) للمصفوفتين \\(A\\) و \\(A^T A\\)؟",
      ["\\(\\text{null}(A^T A) = \\text{null}(A)\\)",
       "\\(\\text{null}(A^T A) \\subsetneq \\text{null}(A)\\)",
       "\\(\\text{null}(A) \\perp \\text{null}(A^T A)\\)",
       "\\(\\dim(\\text{null}(A^T A)) = 2\\dim(\\text{null}(A))\\)"],
      0,
      "Clearly if \\(\\mathbf{x} \\in \\text{null}(A)\\), then \\(A\\mathbf{x} = \\mathbf{0} \\implies A^T A \\mathbf{x} = \\mathbf{0}\\), so \\(\\text{null}(A) \\subseteq \\text{null}(A^T A)\\). Conversely, if \\(A^T A \\mathbf{x} = \\mathbf{0}\\), multiply on the left by \\(\\mathbf{x}^T\\): \\(\\mathbf{x}^T A^T A \\mathbf{x} = 0 \\implies (A\\mathbf{x})^T(A\\mathbf{x}) = \\|A\\mathbf{x}\\|^2 = 0\\). In a real inner product space, this implies \\(A\\mathbf{x} = \\mathbf{0}\\), so \\(\\mathbf{x} \\in \\text{null}(A)\\). Hence \\(\\text{null}(A^T A) = \\text{null}(A)\\), which also proves \\(\\text{rank}(A^T A) = \\text{rank}(A)\\).",
      "إذا كان \\(A\\mathbf{x} = 0\\) فإن \\(A^T A \\mathbf{x} = 0\\). وبالعكس، إذا كان \\(A^T A \\mathbf{x} = 0\\) فإن \\(\\mathbf{x}^T A^T A \\mathbf{x} = \\|A\\mathbf{x}\\|^2 = 0\\)، مما يقتضي \\(A\\mathbf{x} = 0\\). بالتالي فإن فضائي العدم متطابقان تماماً، مما يثبت أيضاً أن \\(\\text{rank}(A^T A) = \\text{rank}(A)\\).",
      "Consider \\(\\mathbf{x}^T A^T A \\mathbf{x} = \\|A\\mathbf{x}\\|^2\\).",
      "تأمل المقدار \\(\\mathbf{x}^T A^T A \\mathbf{x} = \\|A\\mathbf{x}\\|^2\\).")

    # 384: Dual Space and Annihilator
    q("KAUST-P2-384", "Linear Algebra", "Hard",
      "Let \\(V\\) be a 6-dimensional vector space and \\(W \\subset V\\) a 2-dimensional subspace. What is the dimension of the annihilator \\(W^0 = \\{f \\in V^* : f(w) = 0 \\quad \\forall w \\in W\\}\\) in the dual space \\(V^*\\)?",
      "ليكن \\(V\\) فضاءً متجهياً ذا 6 أبعاد و \\(W \\subset V\\) فضاءً جزئياً ذا بُعدين. ما هو بُعد المبيد (annihilator) \\(W^0\\) في الفضاء الثنوي \\(V^*\\)؟",
      ["\\(4\\)", "\\(2\\)", "\\(3\\)", "\\(6\\)"],
      0,
      "A standard theorem of duality in linear algebra states that for any subspace \\(W\\) of a finite-dimensional vector space \\(V\\), \\(\\dim(W) + \\dim(W^0) = \\dim(V)\\). Here \\(\\dim(V) = 6\\) and \\(\\dim(W) = 2\\), so \\(\\dim(W^0) = 6 - 2 = 4\\).",
      "تنص نظرية الثنوية الأساسية على أن \\(\\dim(W) + \\dim(W^0) = \\dim(V)\\). هنا \\(\\dim(V) = 6\\) و \\(\\dim(W) = 2\\)، وبالتالي \\(\\dim(W^0) = 6 - 2 = 4\\).",
      "Apply the duality relation \\(\\dim(W) + \\dim(W^0) = \\dim(V)\\).",
      "طبق العلاقة \\(\\dim(W) + \\dim(W^0) = \\dim(V)\\).")

    # 385: Normal Matrix Characterization
    q("KAUST-P2-385", "Matrix Analysis", "Hard",
      "Which of the following classes of matrices is NOT necessarily normal?",
      "أي من أصناف المصفوفات التالية ليس بالضرورة مصفوفة ناظمية (normal)؟",
      ["Invertible matrices", "Hermitian matrices", "Unitary matrices", "Skew-Hermitian matrices"],
      0,
      "A matrix \\(A\\) is normal if \\(A A^* = A^* A\\). Hermitian (\\(A^* = A\\)), Unitary (\\(A^* = A^{-1}\\)), and Skew-Hermitian (\\(A^* = -A\\)) matrices are all trivially normal. However, invertible matrices do not generally commute with their conjugate transpose (e.g., \\(A = \\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}\\) is invertible, but \\(A A^* = \\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix} \\neq A^* A = \\begin{pmatrix} 1 & 1 \\\\ 1 & 2 \\end{pmatrix}\\)).",
      "المصفوفة الناظمية تحقق \\(A A^* = A^* A\\). المصفوفات الهرميتية والوحدوية ومتخالفة الهرميتية كلها ناظمية بالضرورة. أما المصفوفات القابلة للعكس فليست بالضرورة ناظمية، مثل مصفوفة القص \\(\\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}\\).",
      "Test whether the shear matrix \\(\\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}\\) commutes with its transpose.",
      "اختبر ما إذا كانت مصفوفة القص تبادلية مع منقولها.")

    # 386: Trace of Projection onto a Line
    q("KAUST-P2-386", "Linear Algebra", "Medium",
      "Let \\(\\mathbf{u} = \\frac{1}{3}\\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}\\) be a unit vector in \\(\\mathbb{R}^3\\). The orthogonal projection matrix onto the line spanned by \\(\\mathbf{u}\\) is \\(P = \\mathbf{u}\\mathbf{u}^T\\). What is \\(\\det(I + 3P)\\)?",
      "ليكن \\(\\mathbf{u} = \\frac{1}{3}\\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}\\) متجه وحدة في \\(\\mathbb{R}^3\\). مصفوفة الإسقاط المتعامد على المستقيم المولد بـ \\(\\mathbf{u}\\) هي \\(P = \\mathbf{u}\\mathbf{u}^T\\). ما قيمة \\(\\det(I + 3P)\\)؟",
      ["\\(4\\)", "\\(1\\)", "\\(9\\)", "\\(12\\)"],
      0,
      "The eigenvalues of the rank-1 projection \\(P = \\mathbf{u}\\mathbf{u}^T\\) are \\(1\\) (with multiplicity 1, eigenvector \\(\\mathbf{u}\\)) and \\(0\\) (with multiplicity 2, corresponding to the orthogonal plane). The eigenvalues of \\(I + 3P\\) are therefore \\(1 + 3(1) = 4\\), \\(1 + 3(0) = 1\\), and \\(1 + 3(0) = 1\\). The determinant is the product of the eigenvalues: \\(\\det(I + 3P) = 4 \\times 1 \\times 1 = 4\\).",
      "القيم الذاتية لمصفوفة الإسقاط \\(P\\) هي 1 (بتعدد 1) و 0 (بتعدد 2). وبالتالي فإن القيم الذاتية لـ \\(I + 3P\\) هي \\(1+3(1)=4\\) و 1 و 1. المحدد هو حاصل ضرب هذه القيم ويساوي 4.",
      "Find the eigenvalues of \\(P\\) first.",
      "أوجد القيم الذاتية لمصفوفة الإسقاط أولاً.")

    # 387: Similarity Invariant
    q("KAUST-P2-387", "Linear Algebra", "Medium",
      "If \\(A\\) and \\(B\\) are similar matrices (\\(B = P^{-1} A P\\)), which of the following properties is NOT necessarily shared by \\(A\\) and \\(B\\)?",
      "إذا كانت \\(A\\) و \\(B\\) مصفوفتين متشابهتين (\\(B = P^{-1} A P\\))، فأي من الخواص التالية ليس بالضرورة مشتركاً بينهما؟",
      ["Eigenvectors", "Eigenvalues", "Determinant", "Trace"],
      0,
      "Similar matrices share the exact same characteristic polynomial, eigenvalues (with identical algebraic and geometric multiplicities), determinant, trace, and minimal polynomial. However, their eigenvectors are transformed by \\(P\\): if \\(A\\mathbf{v} = \\lambda \\mathbf{v}\\), then \\(B(P^{-1}\\mathbf{v}) = \\lambda (P^{-1}\\mathbf{v})\\), so the eigenvectors of \\(B\\) are \\(P^{-1}\\mathbf{v}\\), which are not generally the same vectors.",
      "المصفوفات المتشابهة تشترك في كثير الحدود المميز والقيم الذاتية والأثر والمحدد. لكن المتجهات الذاتية تتغير عبر التحويل \\(P^{-1}\\mathbf{v}\\) وبالتالي فهي ليست متطابقة عموماً.",
      "How do eigenvectors transform under a similarity transformation \\(P^{-1}AP\\)?",
      "كيف تتحول المتجهات الذاتية في التحويل التشابهي؟")

    # 388: Vandermonde Determinant
    q("KAUST-P2-388", "Linear Algebra", "Medium",
      "Compute the determinant of the \\(3 \\times 3\\) Vandermonde matrix \\(V = \\begin{pmatrix} 1 & 1 & 1 \\\\ 2 & 3 & 5 \\\\ 4 & 9 & 25 \\end{pmatrix}\\).",
      "احسب محدد مصفوفة فاندرموند \\(3 \\times 3\\): \\(V = \\begin{pmatrix} 1 & 1 & 1 \\\\ 2 & 3 & 5 \\\\ 4 & 9 & 25 \\end{pmatrix}\\).",
      ["\\(6\\)", "\\(12\\)", "\\(3\\)", "\\(24\\)"],
      0,
      "The determinant of a Vandermonde matrix with parameters \\(x_1, x_2, x_3\\) is given by \\(\\prod_{1 \\le i < j \\le 3} (x_j - x_i)\\). Here \\(x_1 = 2\\), \\(x_2 = 3\\), \\(x_3 = 5\\). Thus \\(\\det(V) = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2) = (3 - 2)(5 - 2)(5 - 3) = (1)(3)(2) = 6\\).",
      "محدد مصفوفة فاندرموند يعطى بالقانون \\(\\prod_{i < j} (x_j - x_i)\\). بالتعويض عن \\(x_1 = 2, x_2 = 3, x_3 = 5\\): \\(\\det = (3-2)(5-2)(5-3) = 1 \\times 3 \\times 2 = 6\\).",
      "Apply the product formula \\((x_2 - x_1)(x_3 - x_1)(x_3 - x_2)\\).",
      "طبق صيغة الجداء لمصفوفة فاندرموند.")

    # 389: Matrix Square Zero / Jordan Nilpotent Block
    q("KAUST-P2-389", "Linear Algebra", "Hard",
      "Let \\(T: V \\to V\\) be a linear operator on an \\(n\\)-dimensional space such that \\(T^2 = 0\\). What is the maximum possible dimension of the range \\(\\text{im}(T)\\)?",
      "ليكن \\(T: V \\to V\\) مؤثراً خطياً على فضاء ذي بُعد \\(n\\) يحقق \\(T^2 = 0\\). ما هو أقصى بُعد ممكن لمدى المؤثر \\(\\text{im}(T)\\)؟",
      ["\\(\\lfloor n/2 \\rfloor\\)", "\\(n - 1\\)", "\\(n\\)", "\\(1\\)"],
      0,
      "The condition \\(T^2 = 0\\) means that for any \\(\\mathbf{v} \\in V\\), \\(T(T\\mathbf{v}) = \\mathbf{0}\\), so \\(\\text{im}(T) \\subseteq \\ker(T)\\). Therefore, \\(\\dim(\\text{im}(T)) \\le \\dim(\\ker(T))\\). By the Rank-Nullity Theorem, \\(\\dim(\\text{im}(T)) + \\dim(\\ker(T)) = n\\). Substituting gives \\(2 \\dim(\\text{im}(T)) \\le n \\implies \\dim(\\text{im}(T)) \\le n/2\\). Since the dimension must be an integer, the maximum possible dimension is \\(\\lfloor n/2 \\rfloor\\).",
      "الشرط \\(T^2 = 0\\) يقتضي أن \\(\\text{im}(T) \\subseteq \\ker(T)\\)، ومنه \\(\\text{rank}(T) \\le \\text{nullity}(T)\\). بنظرية الرتبة وفضاء العدم: \\(\\text{rank} + \\text{nullity} = n\\)، إذن \\(2 \\text{rank} \\le n\\)، مما يعني أن أقصى رتبة ممكنة هي \\(\\lfloor n/2 \\rfloor\\).",
      "Notice that the image must be contained in the kernel.",
      "لاحظ أن الصورة محتواة بالكامل داخل النواة.")

    # 390: Positive Definite Diagonal Dominance
    q("KAUST-P2-390", "Matrix Analysis", "Medium",
      "A real symmetric matrix \\(A\\) is strictly diagonally dominant with strictly positive diagonal entries \\(a_{ii} > 0\\). Which theorem immediately proves that \\(A\\) is positive definite?",
      "مصفوفة حقيقية متماثلة \\(A\\) غالبة قطرياً بدقة (strictly diagonally dominant) مع عناصر قطرية موجبة تماماً \\(a_{ii} > 0\\). أي نظرية تثبت مباشرة أن \\(A\\) موجبة المعرّفة؟",
      ["Gershgorin Disc Theorem", "Cayley-Hamilton Theorem", "Perron-Frobenius Theorem", "Spectral Mapping Theorem"],
      0,
      "By the Gershgorin Disc Theorem, every eigenvalue \\(\\lambda\\) lies in at least one disc \\(|\\lambda - a_{ii}| \\le R_i = \\sum_{j \\neq i} |a_{ij}|\\). Strict diagonal dominance means \\(a_{ii} > R_i\\). Since \\(A\\) is symmetric, all its eigenvalues are real. The left endpoint of each interval is \\(a_{ii} - R_i > 0\\). Thus every eigenvalue \\(\\lambda\\) is strictly positive, proving that \\(A\\) is positive definite.",
      "باستخدام نظرية أقراص غيرشغورين، كل قيمة ذاتية تقع في قرص مركزه \\(a_{ii}\\) ونصف قطره \\(R_i\\). الغلبة القطرية الصارمة تعني \\(a_{ii} > R_i\\). وبما أن المصفوفة متماثلة فقيمها الذاتية حقيقية، وأصغر قيمة ممكنة لأي قرص هي \\(a_{ii} - R_i > 0\\). إذن جميع القيم الذاتية موجبة تماماً، فالمصفوفة موجبة المعرفة.",
      "Check the minimum possible value of the Gershgorin interval \\([a_{ii} - R_i, a_{ii} + R_i]\\).",
      "افحص الحد الأدنى لفترة غيرشغورين على المحور الحقيقي.")

    # 391: Adjugate Formula for Inverse
    q("KAUST-P2-391", "Linear Algebra", "Medium",
      "If \\(A \\in \\mathbb{R}^{3 \\times 3}\\) has \\(\\det(A) = 4\\), what is \\(\\det(\\text{adj}(A))\\)?",
      "إذا كانت \\(A \\in \\mathbb{R}^{3 \\times 3}\\) محددها \\(\\det(A) = 4\\)، فما هو محدد مصفوفة المرافقة الكلاسيكية \\(\\det(\\text{adj}(A))\\)؟",
      ["\\(16\\)", "\\(4\\)", "\\(64\\)", "\\(1/4\\)"],
      0,
      "From the fundamental relation \\(A \\text{adj}(A) = \\det(A) I_n\\), take the determinant of both sides: \\(\\det(A) \\det(\\text{adj}(A)) = (\\det(A))^n\\). Dividing by \\(\\det(A) \\neq 0\\) gives \\(\\det(\\text{adj}(A)) = (\\det(A))^{n-1}\\). For \\(n = 3\\): \\(\\det(\\text{adj}(A)) = (\\det(A))^2 = 4^2 = 16\\).",
      "من العلاقة الأساسية \\(A \\text{adj}(A) = \\det(A) I\\)، بأخذ المحدد نجد: \\(\\det(A) \\det(\\text{adj}(A)) = (\\det(A))^n\\). وبالتالي \\(\\det(\\text{adj}(A)) = (\\det(A))^{n-1}\\). لـ \\(n = 3\\)، الناتج هو \\(4^2 = 16\\).",
      "Use the identity \\(\\det(\\text{adj}(A)) = (\\det(A))^{n-1}\\).",
      "استخدم المتطابقة \\(\\det(\\text{adj}(A)) = (\\det(A))^{n-1}\\).")

    # 392: Commuting with All Matrices
    q("KAUST-P2-392", "Linear Algebra", "Medium",
      "Which matrices \\(A \\in \\mathbb{C}^{n \\times n}\\) commute with ALL matrices \\(B \\in \\mathbb{C}^{n \\times n}\\)?",
      "ما هي المصفوفات \\(A \\in \\mathbb{C}^{n \\times n}\\) التي تكون تبادلية مع جميع المصفوفات \\(B \\in \\mathbb{C}^{n \\times n}\\)؟",
      ["Scalar matrices \\(A = cI\\) where \\(c \\in \\mathbb{C}\\)",
       "All diagonal matrices",
       "All symmetric matrices",
       "Only the zero matrix \\(A = 0\\)"],
      0,
      "The center of the matrix algebra \\(M_n(\\mathbb{C})\\) consists solely of scalar multiples of the identity matrix, \\(A = cI\\). Testing commutation with the standard basis matrices \\(E_{ij}\\) (which have a 1 at position \\((i, j)\\) and 0 elsewhere) easily shows that \\(A\\) must be diagonal and all diagonal entries must be equal.",
      "مركز جبر المصفوفات يتكون حصراً من مضاعفات مصفوفة الوحدة السلمية \\(A = cI\\). باختبار التبادلية مع مصفوفات الأساس القياسي \\(E_{ij}\\) يتضح أن المصفوفة يجب أن تكون قطرية وجميع عناصرها القطرية متساوية.",
      "Test commutation with elementary basis matrices \\(E_{ij}\\).",
      "اختبر التبادلية مع مصفوفات الأساس الابتدائية.")

    # 393: SVD and Best Low-Rank Approximation (Eckart-Young-Mirsky)
    q("KAUST-P2-393", "Matrix Analysis", "Hard",
      "The Eckart-Young-Mirsky theorem states that the best rank-\\(k\\) approximation \\(A_k\\) to matrix \\(A\\) in the spectral norm is given by the truncated SVD \\(A_k = \\sum_{i=1}^k \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T\\). What is the approximation error \\(\\|A - A_k\\|_2\\)?",
      "تنص نظرية إيكارت-يونغ-ميرسكي على أن أفضل تقريب من الرتبة \\(k\\) للمصفوفة \\(A\\) بالمعيار الطيفي يعطى بالـ SVD المبتور. ما هو خطأ التقريب \\(\\|A - A_k\\|_2\\)؟",
      ["\\(\\sigma_{k+1}\\)", "\\(\\sqrt{\\sum_{i=k+1}^r \\sigma_i^2}\\)", "\\(\\sigma_k\\)", "\\(\\sum_{i=k+1}^r \\sigma_i\\)"],
      0,
      "In the truncated SVD, the residual matrix is \\(A - A_k = \\sum_{i=k+1}^r \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T\\). Since the singular values are ordered in descending order \\(\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge \\sigma_r\\), the largest singular value of the residual is \\(\\sigma_{k+1}\\). Therefore, the spectral norm of the error is exactly \\(\\|A - A_k\\|_2 = \\sigma_{k+1}\\).",
      "في تفكيك القيم المفردة المبتور، مصفوفة البواقي هي \\(A - A_k = \\sum_{i=k+1}^r \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T\\). أكبر قيمة مفردة في هذه المصفوفة هي \\(\\sigma_{k+1}\\). وبالتالي فإن المعيار الطيفي للخطأ يساوي تماماً \\(\\sigma_{k+1}\\).",
      "The spectral norm of a matrix equals its largest singular value.",
      "المعيار الطيفي لأي مصفوفة يساوي أكبر قيمة مفردة لها.")

    # 394: Trace of Outer Product
    q("KAUST-P2-394", "Linear Algebra", "Medium",
      "For column vectors \\(\\mathbf{u}, \\mathbf{v} \\in \\mathbb{R}^n\\), what is the trace of the outer product matrix \\(\\mathbf{u} \\mathbf{v}^T\\)?",
      "لمتجهي عمود \\(\\mathbf{u}, \\mathbf{v} \\in \\mathbb{R}^n\\)، ما هو أثر مصفوفة الجداء الخارجي \\(\\mathbf{u} \\mathbf{v}^T\\)؟",
      ["\\(\\mathbf{u}^T \\mathbf{v}\\) (the inner product)", "\\(\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|\\)", "\\(0\\)", "\\(\\mathbf{u} \\mathbf{v}\\)"],
      0,
      "By the cyclic property of the trace, \\(\\text{tr}(\\mathbf{u}\\mathbf{v}^T) = \\text{tr}(\\mathbf{v}^T \\mathbf{u})\\). Since \\(\\mathbf{v}^T \\mathbf{u}\\) is a scalar (a \\(1 \\times 1\\) matrix), its trace is simply the scalar itself, which is the inner product \\(\\mathbf{u}^T \\mathbf{v} = \\mathbf{v}^T \\mathbf{u}\\).",
      "بخاصية التبادل الدوري للأثر: \\(\\text{tr}(\\mathbf{u}\\mathbf{v}^T) = \\text{tr}(\\mathbf{v}^T \\mathbf{u})\\). وبما أن \\(\\mathbf{v}^T \\mathbf{u}\\) هو عدد سلمي، فإن أثره هو العدد نفسه، أي الجداء الداخلي المعتاد.",
      "Use the cyclic trace property: \\(\\text{tr}(AB) = \\text{tr}(BA)\\).",
      "استخدم خاصية التبادل الدوري للأثر.")

    # 395: Positive Definite Inverse
    q("KAUST-P2-395", "Matrix Analysis", "Medium",
      "If \\(A\\) is a symmetric positive definite matrix, which statement about \\(A^{-1}\\) is FALSE?",
      "إذا كانت \\(A\\) مصفوفة متماثلة موجبة المعرّفة، فأي عبارة حول \\(A^{-1}\\) خاطئة؟",
      ["\\(A^{-1}\\) has negative eigenvalues",
       "\\(A^{-1}\\) is symmetric positive definite",
       "The eigenvalues of \\(A^{-1}\\) are the reciprocals of the eigenvalues of \\(A\\)",
       "\\(\\det(A^{-1}) > 0\\)"],
      0,
      "If \\(A\\) is positive definite, all its eigenvalues \\(\\lambda_i > 0\\). The eigenvalues of \\(A^{-1}\\) are \\(1/\\lambda_i\\), which are also strictly positive. Hence \\(A^{-1}\\) is strictly positive definite and cannot have any negative eigenvalues. Thus the statement that \\(A^{-1}\\) has negative eigenvalues is false.",
      "إذا كانت \\(A\\) موجبة المعرفة، فإن جميع قيمها الذاتية موجبة. قيم مقلوبها الذاتية هي \\(1/\\lambda_i\\) وهي موجبة تماماً أيضاً. وبالتالي لا يمكن لـ \\(A^{-1}\\) أن تمتلك أي قيم ذاتية سالبة.",
      "Recall that the eigenvalues of \\(A^{-1}\\) are \\(1/\\lambda\\).",
      "تذكر أن القيم الذاتية لمقلوب المصفوفة هي مقلوبات القيم الذاتية الأصلية.")

    # 396: Rank of Skew-Symmetric Matrix
    q("KAUST-P2-396", "Linear Algebra", "Hard",
      "What can be stated about the rank of any real skew-symmetric matrix \\(A\\) (\\(A^T = -A\\))?",
      "ما الذي يمكن الجزم به حول رتبة أي مصفوفة حقيقية متخالفة التماثل \\(A\\) (\\(A^T = -A\\))؟",
      ["The rank is always an even integer",
       "The rank is always an odd integer",
       "The rank can be any integer from 0 to \\(n\\)",
       "The rank is always equal to \\(n\\)"],
      0,
      "The non-zero eigenvalues of a real skew-symmetric matrix are purely imaginary and must occur in complex conjugate pairs \\(\\pm i \\mu_k\\) with \\(\\mu_k \\in \\mathbb{R}\\setminus\\{0\\}\\). Since each conjugate pair contributes 2 to the rank, the total rank of any real skew-symmetric matrix is always an even integer. Consequently, any odd-dimensional skew-symmetric matrix must have a non-trivial nullspace and \\(\\det(A) = 0\\).",
      "القيم الذاتية غير الصفرية لمصفوفة حقيقية متخالفة التماثل تكون تخيلية بحتة وتأتي دائماً في أزواج مترافقة \\(\\pm i\\mu\\). وبما أن كل زوج يساهم بمقدار 2 في الرتبة، فإن رتبة أي مصفوفة حقيقية متخالفة التماثل هي دائماً عدد زوجي.",
      "Consider the complex conjugate pairing of purely imaginary eigenvalues.",
      "فكر في اقتران القيم الذاتية التخيلية البحتة في أزواج مترافقة.")

    # 397: QR Algorithm Convergence
    q("KAUST-P2-397", "Matrix Analysis", "Hard",
      "In numerical linear algebra, what does the pure unshifted QR algorithm (iterating \\(A_k = Q_k R_k\\), \\(A_{k+1} = R_k Q_k\\)) converge to for a symmetric matrix with distinct eigenvalues?",
      "في الجبر الخطي العددي، إلى ماذا تتقارب خوارزمية QR النقية بدون إزاحة (بتكرار \\(A_k = Q_k R_k\\) ثم \\(A_{k+1} = R_k Q_k\\)) لمصفوفة متماثلة ذات قيم ذاتية متمايزة؟",
      ["A diagonal matrix containing the eigenvalues in descending order of absolute value",
       "The zero matrix",
       "The identity matrix",
       "A companion matrix"],
      0,
      "The QR algorithm without shifts transforms \\(A_{k+1} = Q_k^T A_k Q_k\\) by similarity transformations. For a symmetric matrix whose eigenvalues have distinct absolute values \\(|\\lambda_1| > |\\lambda_2| > \\dots > |\\lambda_n|\\), the subdiagonal entries decay exponentially to 0, converging to a diagonal matrix with the eigenvalues on the diagonal ordered by decreasing magnitude.",
      "تحول خوارزمية QR المصفوفة عبر تحويلات تشابه متعامدة. للمصفوفات المتماثلة ذات القيم المتمايزة في المقدار، تتلاشى العناصر خارج القطر أسياً نحو الصفر، وتتقارب المصفوفة نحو مصفوفة قطرية تحوي القيم الذاتية مرتبة تنازلياً حسب القيمة المطلقة.",
      "Notice that \\(A_{k+1} = Q_k^T A_k Q_k\\) performs orthogonal similarity transformations that drive off-diagonal elements to zero.",
      "لاحظ أن خوارزمية QR تطبق تحويلات تشابه تجعل العناصر خارج القطر تؤول للصفر.")

    # 398: Singular Values of Orthogonal Matrix
    q("KAUST-P2-398", "Matrix Analysis", "Medium",
      "What are all the singular values of an \\(n \\times n\\) orthogonal matrix \\(Q\\)?",
      "ما هي جميع القيم المفردة لمصفوفة متعامدة \\(Q\\) من الرتبة \\(n \\times n\\)؟",
      ["All singular values are equal to \\(1\\)",
       "The singular values can be \\(\\pm 1\\)",
       "All singular values are equal to \\(0\\)",
       "The singular values depend on the dimension \\(n\\)"],
      0,
      "By definition, the singular values of \\(Q\\) are the square roots of the eigenvalues of \\(Q^T Q\\). Since \\(Q\\) is orthogonal, \\(Q^T Q = I_n\\). The eigenvalues of the identity matrix \\(I_n\\) are all \\(1\\). Therefore, every singular value of \\(Q\\) is \\(\\sqrt{1} = 1\\).",
      "القيم المفردة هي الجذور التربيعية للقيم الذاتية للمصفوفة \\(Q^T Q\\). وبما أن \\(Q\\) متعامدة، فإن \\(Q^T Q = I\\). قيم مصفوفة الوحدة الذاتية كلها تساوي 1، إذن جميع القيم المفردة تساوي 1.",
      "Recall \\(Q^T Q = I\\).",
      "تذكر أن \\(Q^T Q = I\\).")

    # 399: Generalized Eigenvalue Problem
    q("KAUST-P2-399", "Matrix Analysis", "Hard",
      "In the generalized eigenvalue problem \\(A \\mathbf{x} = \\lambda B \\mathbf{x}\\), where \\(A\\) is real symmetric and \\(B\\) is real symmetric positive definite, what can be guaranteed about the generalized eigenvalues \\(\\lambda\\)?",
      "في مسألة القيم الذاتية المعممة \\(A \\mathbf{x} = \\lambda B \\mathbf{x}\\)، حيث \\(A\\) متماثلة و \\(B\\) متماثلة موجبة المعرّفة، ما الذي يمكن ضمانه بشأن القيم الذاتية المعممة \\(\\lambda\\)؟",
      ["All eigenvalues \\(\\lambda\\) are real",
       "All eigenvalues \\(\\lambda\\) must be positive",
       "The eigenvalues must be on the unit circle",
       "The eigenvalues can have non-zero imaginary parts"],
      0,
      "Since \\(B\\) is symmetric positive definite, it has an invertible symmetric square root \\(B^{1/2}\\). Let \\(\\mathbf{y} = B^{1/2}\\mathbf{x}\\). Then \\(A B^{-1/2} \\mathbf{y} = \\lambda B^{1/2} \\mathbf{y}\\). Multiplying by \\(B^{-1/2}\\) yields the standard symmetric eigenvalue problem \\(C \\mathbf{y} = \\lambda \\mathbf{y}\\) where \\(C = B^{-1/2} A B^{-1/2}\\). Because \\(A\\) and \\(B^{-1/2}\\) are symmetric, \\(C^T = (B^{-1/2})^T A^T (B^{-1/2})^T = B^{-1/2} A B^{-1/2} = C\\). Any real symmetric matrix has exclusively real eigenvalues. Therefore, all generalized eigenvalues \\(\\lambda\\) must be real.",
      "بما أن \\(B\\) موجبة المعرفة، فإن لها جذراً تربيعياً متماثلاً قابلاً للعكس. بالتعويض \\(\\mathbf{y} = B^{1/2}\\mathbf{x}\\) تتحول المسألة إلى مسألة قيم ذاتية معتادة للمصفوفة المتماثلة \\(B^{-1/2} A B^{-1/2}\\). وبما أن أي مصفوفة حقيقية متماثلة قيمها الذاتية حقيقية تماماً، فإن جميع القيم الذاتية المعممة حقيقية.",
      "Transform the problem using the symmetric square root \\(B^{1/2}\\).",
      "حول المسألة باستخدام الجذر التربيعي المتماثل \\(B^{1/2}\\).")

    # 400: Spectral Theorem for Compact Self-Adjoint Operators
    q("KAUST-P2-400", "Linear Algebra", "Hard",
      "Let \\(A \\in \\mathbb{R}^{n \\times n}\\) be symmetric. If \\(\\mathbf{v}_1\\) and \\(\\mathbf{v}_2\\) are eigenvectors corresponding to distinct eigenvalues \\(\\lambda_1 \\neq \\lambda_2\\), which property must hold under the Euclidean dot product?",
      "لتكن \\(A \\in \\mathbb{R}^{n \\times n}\\) مصفوفة متماثلة. إذا كان \\(\\mathbf{v}_1\\) و \\(\\mathbf{v}_2\\) متجهين ذاتيين يقابلان قيمتين ذاتيتين متمايزتين \\(\\lambda_1 \\neq \\lambda_2\\)، فأي خاصية يجب أن تتحقق في الجداء القياسي الإقليدي؟",
      ["\\(\\mathbf{v}_1^T \\mathbf{v}_2 = 0\\) (they are orthogonal)",
       "\\(\\mathbf{v}_1^T \\mathbf{v}_2 = 1\\)",
       "\\(\\mathbf{v}_1 = -\\mathbf{v}_2\\)",
       "\\(\\mathbf{v}_1^T \\mathbf{v}_2 = \\lambda_1 \\lambda_2\\)"],
      0,
      "Consider \\(\\lambda_1 (\\mathbf{v}_1^T \\mathbf{v}_2) = (\\lambda_1 \\mathbf{v}_1)^T \\mathbf{v}_2 = (A\\mathbf{v}_1)^T \\mathbf{v}_2 = \\mathbf{v}_1^T A^T \\mathbf{v}_2 = \\mathbf{v}_1^T (A\\mathbf{v}_2) = \\mathbf{v}_1^T (\\lambda_2 \\mathbf{v}_2) = \\lambda_2 (\\mathbf{v}_1^T \\mathbf{v}_2)\\). Rearranging gives \\((\\lambda_1 - \\lambda_2)(\\mathbf{v}_1^T \\mathbf{v}_2) = 0\\). Since \\(\\lambda_1 \\neq \\lambda_2\\), we must have \\(\\mathbf{v}_1^T \\mathbf{v}_2 = 0\\). Thus eigenvectors of a symmetric matrix corresponding to distinct eigenvalues are always orthogonal.",
      "نحسب \\(\\lambda_1 (\\mathbf{v}_1^T \\mathbf{v}_2) = (A\\mathbf{v}_1)^T \\mathbf{v}_2 = \\mathbf{v}_1^T A \\mathbf{v}_2 = \\lambda_2 (\\mathbf{v}_1^T \\mathbf{v}_2)\\). بنقل الحدود: \\((\\lambda_1 - \\lambda_2)(\\mathbf{v}_1^T \\mathbf{v}_2) = 0\\). وبما أن القيمتين الذاتيتين مختلفتان، فإن الجداء القياسي يجب أن يساوي صفراً، أي أن المتجهين متعامدان.",
      "Evaluate \\(\\mathbf{v}_1^T A \\mathbf{v}_2\\) in two ways.",
      "احسب \\(\\mathbf{v}_1^T A \\mathbf{v}_2\\) بطريقتين مختلفتين.")

    return questions

if __name__ == "__main__":
    qs = get_p2_part_c()
    print(f"Loaded {len(qs)} questions for Phase 2 Part C.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=351):
        expected_id = f"KAUST-P2-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 2 Part C questions successfully verified!")
