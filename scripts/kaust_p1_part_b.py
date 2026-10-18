#!/usr/bin/env python3
"""
KAUST Phase 1 Questions Part B: 301 to 350
Number Theory, Linear Algebra, Polynomials, Sequences, Geometry.
"""

def get_part_b():
    questions = []
    
    def q(qid, topic, diff, q_en, q_ar, options, corr_idx, exp_en, exp_ar, hint_en, hint_ar, diagram=None):
        item = {
            "id": qid,
            "track": "kaust",
            "level": "Phase 1: Foundation Research",
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

    # 301: Primitive roots mod 19
    q("KAUST-P1-301", "Number Theory", "Medium",
      "How many primitive roots modulo the prime \\( 19 \\) exist?",
      "كم جذراً بدائياً يوجد مقياس العدد الأولي \\( 19 \\)؟",
      ["\\( 4 \\)", "\\( 6 \\)", "\\( 8 \\)", "\\( 9 \\)"], 1,
      "The number of primitive roots modulo a prime \\( p \\) is \\( \\phi(\\phi(p)) = \\phi(p-1) \\). For \\( p = 19 \\): \\( \\phi(18) = 18 \\times \\left(1 - \\dfrac{1}{2}\\right) \\left(1 - \\dfrac{1}{3}\\right) = 18 \\times \\dfrac{1}{2} \\times \\dfrac{2}{3} = 6 \\). [Lineage: AIME / Primitive Roots]",
      "عدد الجذور البدائية مقياس عدد أولي \\( p \\) هو \\( \\phi(p-1) \\). عند \\( p = 19 \\): \\( \\phi(18) = 6 \\). [المرجع: الجذور البدائية في نظرية الأعداد]",
      "Compute \\( \\phi(p-1) \\).", "احسب قيمة دالة أويلر لـ \\( p-1 \\).")

    # 302: Legendre Symbol
    q("KAUST-P1-302", "Number Theory", "Hard",
      "Evaluate the Legendre symbol \\( \\left( \\dfrac{5}{23} \\right) \\) using Gauss's Law of Quadratic Reciprocity.",
      "احسب قيمة رمز ليجاندر \\( \\left( \\dfrac{5}{23} \\right) \\) باستخدام قانون التبادل التربيعي لغاوس.",
      ["\\( -1 \\)", "\\( 0 \\)", "\\( 1 \\)", "\\( 2 \\)"], 0,
      "Since \\( 5 \\equiv 1 \\pmod 4 \\), by Quadratic Reciprocity \\( \\left( \\dfrac{5}{23} \\right) = \\left( \\dfrac{23}{5} \\right) = \\left( \\dfrac{3}{5} \\right) \\). Quadratic residues mod 5 are \\( 1^2=1, 2^2=4 \\), so \\( 3 \\) is a non-residue, giving \\( \\left( \\dfrac{3}{5} \\right) = -1 \\). Thus, \\( \\left( \\dfrac{5}{23} \\right) = -1 \\). [Lineage: Quadratic Reciprocity / SMT]",
      "بما أن \\( 5 \\equiv 1 \\pmod 4 \\)، فإن قانون التبادل التربيعي يعطي \\( (5/23) = (23/5) = (3/5) = -1 \\). [المرجع: قانون التبادل التربيعي لغاوس]",
      "Use \\( (p/q) = (q/p) \\) when \\( p \\equiv 1 \\pmod 4 \\).", "طبق قانون التبادل التربيعي عندما يكون أحد العددين يكافئ 1 مقياس 4.")

    # 303: Sum of two squares
    q("KAUST-P1-303", "Number Theory", "Medium",
      "According to Fermat's Christmas Theorem, which of the following prime numbers can be expressed as the sum of two integer squares \\( a^2 + b^2 \\)?",
      "وفق مبرهنة فيرما لمجموع المربعين، أي من الأعداد الأولية التالية يمكن كتابته كمجموع مربعي عددين صحيحين \\( a^2 + b^2 \\)؟",
      ["\\( 67 \\)", "\\( 71 \\)", "\\( 73 \\)", "\\( 79 \\)"], 2,
      "Fermat's theorem on sums of two squares states that an odd prime \\( p \\) is expressible as \\( a^2 + b^2 \\) if and only if \\( p \\equiv 1 \\pmod 4 \\). Checking mod 4: \\( 67 \\equiv 3 \\), \\( 71 \\equiv 3 \\), \\( 79 \\equiv 3 \\), while \\( 73 = 4(18) + 1 \\equiv 1 \\pmod 4 \\) (indeed, \\( 73 = 8^2 + 3^2 \\)). [Lineage: Fermat's Two Square Theorem]",
      "العدد الأولي الفردي يُكتب كمجموع مربعين إذا وفقط إذا كان يطابق 1 مقياس 4. العدد 73 هو الوحيد الذي يحقق \\( 73 \\equiv 1 \\pmod 4 \\) حيث \\( 73 = 8^2 + 3^2 \\). [المرجع: مبرهنة فيرما لمجموع المربعين]",
      "Check which prime is congruent to \\( 1 \\pmod 4 \\).", "ابحث عن العدد الأولي الذي يكافئ 1 مقياس 4.")

    # 304: Linear Diophantine
    q("KAUST-P1-304", "Number Theory", "Medium",
      "Find an integer pair \\( (x, y) \\) satisfying the linear Diophantine equation \\( 17x + 23y = 1 \\).",
      "أوجد زوجاً من الأعداد الصحيحة \\( (x, y) \\) يحقق المعادلة الديوفانتية الخطية \\( 17x + 23y = 1 \\).",
      ["\\( (-4, 3) \\)", "\\( (-3, 2) \\)", "\\( (4, -3) \\)", "\\( (3, -2) \\)"], 1,
      "Using the Extended Euclidean Algorithm: \\( 23 = 1(17) + 6 \\), \\( 17 = 2(6) + 5 \\), \\( 6 = 1(5) + 1 \\). Back-substituting: \\( 1 = 6 - 5 = 6 - (17 - 2(6)) = 3(6) - 17 = 3(23 - 17) - 17 = 3(23) - 4(17) \\). Wait, \\( 3(23) - 4(17) = 69 - 68 = 1 \\), so \\( 17(-4) + 23(3) = 1 \\). Let's check options: \\( 17(-4) + 23(3) = -68 + 69 = 1 \\). Thus \\( (x, y) = (-4, 3) \\). [Lineage: Extended Euclidean Algorithm]",
      "باستخدام خوارزمية إقليدس الممتدة: \\( 17(-4) + 23(3) = -68 + 69 = 1 \\). إذن الحل هو \\( (-4, 3) \\). [المرجع: خوارزمية إقليدس الممتدة]",
      "Apply the Extended Euclidean Algorithm.", "طبق خوارزمية إقليدس الممتدة.")

    # 305: Divisor count tau(720)
    q("KAUST-P1-305", "Number Theory", "Easy",
      "Find the total number of positive integer divisors of \\( 720 \\), denoted \\( \\tau(720) \\).",
      "أوجد العدد الإجمالي للقواسم الصحيحة الموجبة للعدد \\( 720 \\)، والمشار إليها بـ \\( \\tau(720) \\).",
      ["\\( 24 \\)", "\\( 30 \\)", "\\( 36 \\)", "\\( 40 \\)"], 1,
      "Prime factorization: \\( 720 = 2^4 \\times 3^2 \\times 5^1 \\). The number of divisors is \\( (4+1)(2+1)(1+1) = 5 \\times 3 \\times 2 = 30 \\). [Lineage: AMC 12 / Divisor Function]",
      "التحليل إلى عوامل أولية: \\( 720 = 2^4 \\times 3^2 \\times 5 \\). عدد القواسم: \\( 5 \\times 3 \\times 2 = 30 \\). [المرجع: مسابقة AMC 12]",
      "Multiply exponents incremented by one: \\( \\prod (a_i + 1) \\).", "اضرب قوى العوامل الأولية مضافاً إلى كل منها 1.")

    # 306: Last digit 7^2026
    q("KAUST-P1-306", "Number Theory", "Easy",
      "What is the units digit of \\( 7^{2026} \\)?",
      "ما هو رقم آحاد العدد \\( 7^{2026} \\)؟",
      ["\\( 1 \\)", "\\( 3 \\)", "\\( 7 \\)", "\\( 9 \\)"], 3,
      "Powers of 7 modulo 10 cycle with period 4: \\( 7^1 \\equiv 7 \\), \\( 7^2 \\equiv 9 \\), \\( 7^3 \\equiv 3 \\), \\( 7^4 \\equiv 1 \\). Since \\( 2026 \\equiv 2 \\pmod 4 \\), \\( 7^{2026} \\equiv 7^2 \\equiv 9 \\pmod{10} \\). [Lineage: Modular Exponentiation / AMC 12]",
      "قوى العدد 7 تدور بدورة طولها 4 مقياس 10: 7، 9، 3، 1. بما أن \\( 2026 \\equiv 2 \\pmod 4 \\)، فإن الآحاد هو 9. [المرجع: الحساب المقياسي]",
      "Determine \\( 2026 \\pmod 4 \\).", "حدد باقي قسمة 2026 على 4.")

    # 307: Multiplicative inverse mod 37
    q("KAUST-P1-307", "Number Theory", "Medium",
      "What is the multiplicative inverse of \\( 11 \\) modulo \\( 37 \\)?",
      "ما هو المعكوس الضربي للعدد \\( 11 \\) مقياس \\( 37 \\)؟",
      ["\\( 17 \\)", "\\( 24 \\)", "\\( 27 \\)", "\\( 31 \\)"], 2,
      "We seek \\( x \\) such that \\( 11x \\equiv 1 \\pmod{37} \\). Notice \\( 11 \\times 27 = 297 = 8 \\times 37 + 1 = 296 + 1 \\equiv 1 \\pmod{37} \\). Thus, \\( 11^{-1} \\equiv 27 \\pmod{37} \\). [Lineage: Modular Inverses / Cryptography Foundations]",
      "نبحث عن \\( x \\) بحيث \\( 11x \\equiv 1 \\pmod{37} \\). بما أن \\( 11 \\times 27 = 297 = 296 + 1 \\)، فإن المعكوس هو 27. [المرجع: أساسيات التشفير الرياضي]",
      "Solve \\( 11x \\equiv 1 \\pmod{37} \\).", "حل المعادلة التطابقية لإيجاد المعكوس.")

    # 308: Perfect numbers
    q("KAUST-P1-308", "Number Theory", "Easy",
      "Using the Euclid-Euler theorem with the Mersenne prime \\( M_5 = 2^5 - 1 = 31 \\), what is the corresponding even perfect number?",
      "باستخدام مبرهنة إقليدس-أويلر مع عدد ميرسين الأولي \\( M_5 = 2^5 - 1 = 31 \\)، ما هو العدد التام الزوجي المقابل؟",
      ["\\( 248 \\)", "\\( 496 \\)", "\\( 512 \\)", "\\( 992 \\)"], 1,
      "By the Euclid-Euler theorem, even perfect numbers are of the form \\( 2^{p-1}(2^p - 1) \\). For \\( p = 5 \\): \\( 2^4(31) = 16 \\times 31 = 496 \\). [Lineage: Euclid-Euler Perfect Numbers]",
      "صيغة إقليدس وأويلر للأعداد التامة: \\( 2^{p-1}(2^p - 1) \\). عند \\( p = 5 \\): \\( 16 \\times 31 = 496 \\). [المرجع: مبرهنة إقليدس وأويلر]",
      "Compute \\( 2^4 \\times 31 \\).", "احسب حاصل ضرب \\( 16 \\times 31 \\).")

    # 309: Pell's equation
    q("KAUST-P1-309", "Number Theory", "Medium",
      "What is the fundamental (minimal positive integer) solution \\( (x_1, y_1) \\) to Pell's equation \\( x^2 - 2y^2 = 1 \\)?",
      "ما هو الحل الأساسي (الأصغر في الأعداد الصحيحة الموجبة) \\( (x_1, y_1) \\) لمعادلة بيل \\( x^2 - 2y^2 = 1 \\)؟",
      ["\\( (1, 1) \\)", "\\( (3, 2) \\)", "\\( (7, 5) \\)", "\\( (17, 12) \\)"], 1,
      "Testing small positive integers: For \\( y = 1 \\), \\( x^2 = 3 \\) (no integer). For \\( y = 2 \\), \\( x^2 = 2(4) + 1 = 9 \\implies x = 3 \\). Thus, the fundamental solution is \\( (3, 2) \\). [Lineage: Pell's Equation / AIME]",
      "بالتعويض عن \\( y = 2 \\) نجد \\( x^2 = 9 \\implies x = 3 \\). الحل الأساسي هو \\( (3, 2) \\). [المرجع: معادلة بيل]",
      "Test small integers for y starting from 1.", "عوض بقيم صحيحة صغيرة لـ y بدءاً من 1.")

    # 310: Divisibility n^5 - n
    q("KAUST-P1-310", "Number Theory", "Easy",
      "For every integer \\( n \\), the expression \\( n^5 - n \\) is always divisible by which integer?",
      "لكل عدد صحيح \\( n \\)، المقدار \\( n^5 - n \\) يقبل القسمة دائماً على أي من الأعداد التالية؟",
      ["\\( 15 \\)", "\\( 24 \\)", "\\( 30 \\)", "\\( 60 \\)"], 2,
      "Factoring: \\( n^5 - n = n(n^4 - 1) = n(n-1)(n+1)(n^2+1) \\). It contains three consecutive integers \\( (n-1)n(n+1) \\), so it is divisible by \\( 6 \\). By Fermat's Little Theorem, \\( n^5 \\equiv n \\pmod 5 \\), so it is divisible by \\( 5 \\). Since \\( \\gcd(6, 5) = 1 \\), it is divisible by \\( 30 \\). [Lineage: Number Theory Divisibility / Putnam]",
      "المقدار يقبل القسمة على 6 لأنه يضم 3 أعداد متتالية، ويقبل القسمة على 5 بمبرهنة فيرما الصغرى. إذن يقبل القسمة دائماً على 30. [المرجع: خواص قابلية القسمة في بوتنام]",
      "Factor the expression and apply Fermat's Little Theorem for prime 5.", "حلل المقدار وطبق مبرهنة فيرما الصغرى للعدد 5.")

    # 311: Characteristic poly triangular matrix
    q("KAUST-P1-311", "Linear Algebra", "Easy",
      "What are the eigenvalues of the upper triangular matrix \\( A = \\begin{pmatrix} 2 & 5 & 7 \\\\ 0 & -3 & 4 \\\\ 0 & 0 & 5 \\end{pmatrix} \\)?",
      "ما هي القيم الذاتية للمصفوفة المثلثية العلوية \\( A = \\begin{pmatrix} 2 & 5 & 7 \\\\ 0 & -3 & 4 \\\\ 0 & 0 & 5 \\end{pmatrix} \\)؟",
      ["\\( \\{2, 5, 7\\} \\)", "\\( \\{2, -3, 5\\} \\)", "\\( \\{-3, 0, 5\\} \\)", "\\( \\{1, 2, 3\\} \\)"], 1,
      "The determinant of a triangular matrix is the product of its diagonal entries. The characteristic polynomial is \\( \\det(A - \\lambda I) = (2 - \\lambda)(-3 - \\lambda)(5 - \\lambda) = 0 \\), so the eigenvalues are precisely the diagonal entries: \\( 2, -3, 5 \\). [Lineage: MIT 18.06 / Eigenvalues of Triangular Matrices]",
      "محدد المصفوفة المثلثية هو حاصل ضرب عناصر القطر الرئيسي، وبالتالي فإن القيم الذاتية هي عناصر القطر نفسه: \\( 2, -3, 5 \\). [المرجع: الجبر الخطي في MIT]",
      "The eigenvalues of any triangular matrix are its diagonal entries.", "القيم الذاتية لأي مصفوفة مثلثية هي عناصر قطرها الرئيسي.")

    # 312: Orthogonal Projection (Diagram)
    d312 = svg_box('<line x1="20" y1="140" x2="240" y2="140" stroke="#94a3b8" stroke-width="1.5"/><line x1="40" y1="160" x2="40" y2="20" stroke="#94a3b8" stroke-width="1.5"/><line x1="40" y1="140" x2="160" y2="50" stroke="#2563eb" stroke-width="3"/><circle cx="160" cy="50" r="4" fill="#2563eb"/><text x="165" y="45" font-size="12" fill="#2563eb" font-weight="bold">u = (3, 4)</text><line x1="160" y1="50" x2="160" y2="140" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/><line x1="40" y1="140" x2="160" y2="140" stroke="#16a34a" stroke-width="3.5"/><circle cx="160" cy="140" r="4" fill="#16a34a"/><text x="130" y="160" font-size="12" fill="#16a34a" font-weight="bold">proj = (3, 0)</text>', "Orthogonal Projection", 360, 180)
    q("KAUST-P1-312", "Linear Algebra", "Easy",
      "What is the orthogonal projection of vector \\( \\mathbf{u} = \\langle 3, 4 \\rangle \\) onto the horizontal vector \\( \\mathbf{v} = \\langle 1, 0 \\rangle \\)?",
      "ما هو الإسقاط المتعامد للمتجه \\( \\mathbf{u} = \\langle 3, 4 \\rangle \\) على المتجه الأفقي \\( \\mathbf{v} = \\langle 1, 0 \\rangle \\)؟",
      ["\\( \\langle 0, 4 \\rangle \\)", "\\( \\langle 3, 0 \\rangle \\)", "\\( \\langle 3, 4 \\rangle \\)", "\\( \\langle 4, 3 \\rangle \\)"], 1,
      "\\( \\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\dfrac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{v}\\|^2} \\mathbf{v} = \\dfrac{3(1) + 4(0)}{1} \\langle 1, 0 \\rangle = \\langle 3, 0 \\rangle \\). [Lineage: Vector Projections / MIT 18.02]",
      "صيغة الإسقاط المتعامد تعطي مباشرة \\( \\langle 3, 0 \\rangle \\). [المرجع: التفاضل الشعاعي في MIT]",
      "Use \\( \\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\mathbf{v} \\cdot \\mathbf{v}} \\mathbf{v} \\).", "طبق قانون الإسقاط المتعامد على المتجه v.", diagram=d312)

    # 313: Vandermonde 3x3
    q("KAUST-P1-313", "Linear Algebra", "Medium",
      "What is the determinant of the \\( 3 \\times 3 \\) Vandermonde matrix \\( V = \\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 4 & 9 \\end{pmatrix} \\)?",
      "ما هو محدد مصفوفة فانديرموند \\( V = \\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 4 & 9 \\end{pmatrix} \\) من الرتبة \\( 3 \\times 3 \\)؟",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( 4 \\)", "\\( 6 \\)"], 1,
      "The Vandermonde determinant for \\( x_1 = 1, x_2 = 2, x_3 = 3 \\) is \\( \\prod_{1 \\le i < j \\le 3} (x_j - x_i) = (3 - 2)(3 - 1)(2 - 1) = 1 \\times 2 \\times 1 = 2 \\). [Lineage: Vandermonde Determinant / Linear Algebra]",
      "محدد فانديرموند يُعطى بحاصل ضرب الفروق: \\( (3-2)(3-1)(2-1) = 1 \\times 2 \\times 1 = 2 \\). [المرجع: محدد فانديرموند الشهير]",
      "Compute \\( (x_3 - x_2)(x_3 - x_1)(x_2 - x_1) \\).", "احسب حاصل ضرب فروق العناصر.")

    # 314: Idempotent Matrix
    q("KAUST-P1-314", "Linear Algebra", "Easy",
      "If a square matrix \\( P \\) is idempotent (meaning \\( P^2 = P \\)), what are the ONLY possible eigenvalues of \\( P \\)?",
      "إذا كانت المصفوفة المربعة \\( P \\) ارتدادية أو إسقاطية (أي تحقق \\( P^2 = P \\))، فما هي القيم الذاتية الممكنة فقط للمصفوفة \\( P \\)؟",
      ["\\( \\{0, 1\\} \\)", "\\( \\{-1, 1\\} \\)", "\\( \\{0, -1\\} \\)", "\\( \\{1, 2\\} \\)"], 0,
      "If \\( \\lambda \\) is an eigenvalue with eigenvector \\( \\mathbf{v} \\ne 0 \\), then \\( P \\mathbf{v} = \\lambda \\mathbf{v} \\). Applying \\( P \\) again: \\( P^2 \\mathbf{v} = P(\\lambda \\mathbf{v}) = \\lambda^2 \\mathbf{v} \\). Since \\( P^2 = P \\), \\( \\lambda^2 \\mathbf{v} = \\lambda \\mathbf{v} \\implies \\lambda^2 - \\lambda = 0 \\implies \\lambda(\\lambda - 1) = 0 \\), so \\( \\lambda \\in \\{0, 1\\} \\). [Lineage: Idempotent Matrices / MIT 18.06]",
      "بما أن \\( P^2 = P \\)، فإن أي قيمة ذاتية تحقق \\( \\lambda^2 = \\lambda \\implies \\lambda(\\lambda - 1) = 0 \\)، إذن القيم الذاتية الممكنة هي فقط 0 و 1. [المرجع: الجبر الخطي في MIT]",
      "Apply the eigenvalue equation to \\( P^2 = P \\).", "طبق معادلة القيمة الذاتية على طرفي العلاقة.")

    # 315: Invertibility
    q("KAUST-P1-315", "Linear Algebra", "Easy",
      "A square real matrix \\( A \\) is invertible if and only if:",
      "تكون المصفوفة المربعة الحقيقية \\( A \\) قابلة للانعكاس إذا وفقط إذا كان:",
      ["\\( \\det(A) = 0 \\)", "\\( \\det(A) \\ne 0 \\)", "\\( \\text{Tr}(A) = 0 \\)", "\\( A^T = A \\)"], 1,
      "By the Invertible Matrix Theorem, a matrix \\( A \\) is invertible if and only if its determinant is non-zero (\\( \\det(A) \\ne 0 \\)). [Lineage: Invertible Matrix Theorem]",
      "تكون المصفوفة قابلة للعكس إذا وفقط إذا كان محددها لا يساوي صفراً. [المرجع: مبرهنة المصفوفات القابلة للعكس]",
      "Recall the determinant condition for matrix invertibility.", "تذكر شرط المحدد لانعكاس المصفوفة.")

    # 316: Change of Basis
    q("KAUST-P1-316", "Linear Algebra", "Medium",
      "If matrix \\( A \\) represents a linear operator \\( T \\) in basis \\( \\mathcal{B} \\) and \\( P \\) is the change-of-basis matrix, the representation of \\( T \\) in the new basis is given by:",
      "إذا كانت المصفوفة \\( A \\) تمثل المؤثر الخطي \\( T \\) في الأساس \\( \\mathcal{B} \\) وكانت \\( P \\) مصفوفة تغيير الأساس، فإن تمثيل \\( T \\) في الأساس الجديد هو:",
      ["\\( P A P \\)", "\\( P^{-1} A P \\)", "\\( P A P^{-1} \\)", "\\( P^T A P \\)"], 1,
      "Under a change of basis with transition matrix \\( P \\), similar matrices represent the same operator: \\( [T]_{\\mathcal{C}} = P^{-1} [T]_{\\mathcal{B}} P \\). [Lineage: Change of Basis / MIT 18.06]",
      "تغيير الأساس يغير مصفوفة المؤثر بالتشابه: \\( P^{-1} A P \\). [المرجع: تغيير الأساس في الجبر الخطي]",
      "Recall the similarity transformation formula.", "تذكر صيغة تحويل التشابه للمصفوفات.")

    # 317: Nilpotent Matrix
    q("KAUST-P1-317", "Linear Algebra", "Medium",
      "A matrix \\( N \\) is called nilpotent if \\( N^k = \\mathbf{0} \\) for some positive integer \\( k \\). What is the trace \\( \\text{Tr}(N) \\) of any nilpotent matrix?",
      "تُسمى المصفوفة \\( N \\) معدومة القوى (nilpotent) إذا كان \\( N^k = \\mathbf{0} \\) لعدد صحيح موجب \\( k \\). ما هي قيمة أثر \\( \\text{Tr}(N) \\) لأي مصفوفة معدومة القوى؟",
      ["\\( -1 \\)", "\\( 0 \\)", "\\( 1 \\)", "\\( k \\)"], 1,
      "If \\( N^k = \\mathbf{0} \\), all eigenvalues \\( \\lambda \\) must satisfy \\( \\lambda^k = 0 \\implies \\lambda = 0 \\). Since the trace is the sum of eigenvalues, \\( \\text{Tr}(N) = 0 \\). [Lineage: Nilpotent Matrices / Linear Algebra]",
      "جميع القيم الذاتية للمصفوفة معدومة القوى تساوي صفراً، وبما أن الأثر هو مجموع القيم الذاتية، فإن \\( \\text{Tr}(N) = 0 \\). [المرجع: الجبر الخطي المتقدم]",
      "What are the eigenvalues of a nilpotent matrix?", "ما هي القيم الذاتية لمصفوفة تحقق \\( N^k = 0 \\)؟")

    # 318: Gram-Schmidt
    q("KAUST-P1-318", "Linear Algebra", "Medium",
      "Given linearly independent vectors \\( \\mathbf{u}_1 = \\langle 1, 0 \\rangle \\) and \\( \\mathbf{u}_2 = \\langle 2, 3 \\rangle \\), what is the second orthogonal vector \\( \\mathbf{v}_2 \\) obtained from the Gram-Schmidt process (without normalization)?",
      "بفرض المتجهين المستقلين خطياً \\( \\mathbf{u}_1 = \\langle 1, 0 \\rangle \\) و \\( \\mathbf{u}_2 = \\langle 2, 3 \\rangle \\)، ما هو المتجه المتعامد الثاني \\( \\mathbf{v}_2 \\) الناتج من طريقة غرام-شميت (دون تسوية المعيار)؟",
      ["\\( \\langle 0, 3 \\rangle \\)", "\\( \\langle 2, 0 \\rangle \\)", "\\( \\langle -2, 3 \\rangle \\)", "\\( \\langle 3, 0 \\rangle \\)"], 0,
      "In Gram-Schmidt: \\( \\mathbf{v}_1 = \\mathbf{u}_1 = \\langle 1, 0 \\rangle \\). Then \\( \\mathbf{v}_2 = \\mathbf{u}_2 - \\text{proj}_{\\mathbf{v}_1}(\\mathbf{u}_2) = \\langle 2, 3 \\rangle - \\dfrac{2(1) + 3(0)}{1} \\langle 1, 0 \\rangle = \\langle 2, 3 \\rangle - \\langle 2, 0 \\rangle = \\langle 0, 3 \\rangle \\). [Lineage: Gram-Schmidt Orthogonalization / MIT 18.06]",
      "في طريقة غرام-شميت: \\( \\mathbf{v}_2 = \\mathbf{u}_2 - \\text{proj}_{\\mathbf{v}_1}(\\mathbf{u}_2) = \\langle 2, 3 \\rangle - \\langle 2, 0 \\rangle = \\langle 0, 3 \\rangle \\). [المرجع: طريقة غرام-شميت للتعامد]",
      "Subtract the projection of \\( \\mathbf{u}_2 \\) onto \\( \\mathbf{v}_1 \\).", "اطرح مسقط المتجه الثاني على المتجه الأول.")

    # 319: Spectral Theorem
    q("KAUST-P1-319", "Linear Algebra", "Easy",
      "Which fundamental property is GUARANTEED for every real symmetric matrix \\( A \\) (where \\( A^T = A \\))?",
      "أي خاصية أساسية تكون مضمونة دائماً لكل مصفوفة حقيقية متماثلة \\( A \\) (حيث \\( A^T = A \\))؟",
      ["All its eigenvalues are purely imaginary.", "All its eigenvalues are real.", "Its determinant is always positive.", "It has no zero eigenvalues."], 1,
      "The Spectral Theorem for real symmetric matrices guarantees that all eigenvalues are real and that the matrix can be orthogonally diagonalized. [Lineage: Spectral Theorem / MIT 18.06]",
      "تنص مبرهنة التحليل الطيفي على أن جميع القيم الذاتية لأي مصفوفة حقيقية متماثلة هي أعداد حقيقية دائماً. [المرجع: المبرهنة الطيفية للمصفوفات المتماثلة]",
      "Recall the Spectral Theorem for symmetric operators.", "تذكر نص المبرهنة الطيفية.")

    # 320: Vector BAC-CAB
    q("KAUST-P1-320", "Linear Algebra", "Medium",
      "Which identity correctly expands the vector triple product \\( \\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C}) \\)?",
      "أي متطابقة تعبر بشكل صحيح عن حاصل الضرب الاتجاهي الثلاثي \\( \\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C}) \\)؟",
      ["\\( (\\mathbf{A} \\cdot \\mathbf{C})\\mathbf{B} - (\\mathbf{A} \\cdot \\mathbf{B})\\mathbf{C} \\)", "\\( (\\mathbf{A} \\cdot \\mathbf{B})\\mathbf{C} - (\\mathbf{A} \\cdot \\mathbf{C})\\mathbf{B} \\)", "\\( (\\mathbf{B} \\cdot \\mathbf{C})\\mathbf{A} - (\\mathbf{A} \\cdot \\mathbf{C})\\mathbf{B} \\)", "\\( \\mathbf{0} \\)"], 0,
      "Lagrange's vector triple product identity is famously remembered as 'BAC-CAB': \\( \\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{C}) = \\mathbf{B}(\\mathbf{A} \\cdot \\mathbf{C}) - \\mathbf{C}(\\mathbf{A} \\cdot \\mathbf{B}) \\). [Lineage: Vector Algebra / MIT 18.02]",
      "متطابقة لاغرانج للضرب الثلاثي الشعاعي: \\( (\\mathbf{A} \\cdot \\mathbf{C})\\mathbf{B} - (\\mathbf{A} \\cdot \\mathbf{B})\\mathbf{C} \\). [المرجع: متطابقات الجبر الشعاعي]",
      "Remember the mnemonic 'BAC minus CAB'.", "تذكر القاعدة الشهيرة BAC ناقص CAB.")

    # 321: Remainder Theorem quadratic divisor
    q("KAUST-P1-321", "Polynomials", "Medium",
      "When a polynomial \\( P(x) \\) is divided by \\( (x - 1) \\), the remainder is \\( 3 \\). When divided by \\( (x - 2) \\), the remainder is \\( 5 \\). What is the remainder when \\( P(x) \\) is divided by \\( (x - 1)(x - 2) \\)?",
      "عند قسمة كثيرة حدود \\( P(x) \\) على \\( (x - 1) \\) يكون الباقي \\( 3 \\)، وعند قسمتها على \\( (x - 2) \\) يكون الباقي \\( 5 \\). ما هو باقي قسمة \\( P(x) \\) على \\( (x - 1)(x - 2) \\)؟",
      ["\\( 2x + 1 \\)", "\\( 2x - 1 \\)", "\\( x + 2 \\)", "\\( 3x - 1 \\)"], 0,
      "Let the remainder be \\( R(x) = ax + b \\). By the Remainder Theorem, \\( R(1) = P(1) = 3 \\implies a + b = 3 \\), and \\( R(2) = P(2) = 5 \\implies 2a + b = 5 \\). Subtracting gives \\( a = 2 \\), so \\( b = 1 \\). The remainder is \\( 2x + 1 \\). [Lineage: Polynomial Remainder Theorem / AMC 12]",
      "نفرض الباقي \\( R(x) = ax + b \\). بالتعويض: \\( a + b = 3 \\) و \\( 2a + b = 5 \\). بحل النظام: \\( a = 2, b = 1 \\)، إذن الباقي هو \\( 2x + 1 \\). [المرجع: نظرية باقي قسمة كثيرات الحدود]",
      "Set the linear remainder as \\( ax + b \\) and evaluate at \\( x = 1 \\) and \\( x = 2 \\).", "افرض الباقي خطياً وعوض بجذور المقسوم عليه.")

    # 322: Rational Root Theorem
    q("KAUST-P1-322", "Polynomials", "Easy",
      "Which of the following is a rational root of the cubic equation \\( 2x^3 - 5x + 3 = 0 \\)?",
      "أي مما يلي يمثل جذراً نسبياً للمعادلة التكعيبية \\( 2x^3 - 5x + 3 = 0 \\)؟",
      ["\\( -1 \\)", "\\( 1 \\)", "\\( 2 \\)", "\\( -3 \\)"], 1,
      "Testing \\( x = 1 \\): \\( 2(1)^3 - 5(1) + 3 = 2 - 5 + 3 = 0 \\). Thus, \\( x = 1 \\) is an exact rational root. [Lineage: Rational Root Theorem / High School Gifted]",
      "بالتعويض عن \\( x = 1 \\): \\( 2(1) - 5(1) + 3 = 0 \\). إذن \\( x = 1 \\) هو جذر نسبي صحيح. [المرجع: مبرهنة الجذور النسبية]",
      "Test candidate factors of the constant term.", "عوض بعوامل الحد الثابت.")

    # 323: Descartes' Rule of Signs
    q("KAUST-P1-323", "Polynomials", "Medium",
      "How many sign changes occur in the coefficients of \\( P(x) = x^4 - 3x^3 + 2x^2 - x + 5 \\), and what does Descartes' Rule of Signs state about the possible number of positive real roots?",
      "كم عدد تغيرات الإشارة في معاملات \\( P(x) = x^4 - 3x^3 + 2x^2 - x + 5 \\)، وماذا تحدد قاعدة ديكارت للإشارات بخصوص عدد الجذور الحقيقية الموجبة المحتملة؟",
      ["\\( 2 \\) changes; 2 or 0 roots", "\\( 3 \\) changes; 3 or 1 roots", "\\( 4 \\) changes; 4, 2, or 0 roots", "\\( 4 \\) changes; exactly 4 roots"], 2,
      "The signs are \\( +, -, +, -, + \\), which has \\( 4 \\) sign changes. By Descartes' Rule of Signs, the number of positive real roots is either \\( 4 \\) or differs from \\( 4 \\) by an even integer: \\( 4, 2, \\) or \\( 0 \\). [Lineage: Descartes' Rule of Signs]",
      "الإشارات هي (+, -, +, -, +) وتتغير 4 مرات. وفق قاعدة ديكارت، عدد الجذور الموجبة هو 4 أو 2 أو 0. [المرجع: قاعدة ديكارت للإشارات]",
      "Count sign transitions from term to term.", "عد مرات تغير الإشارة بين الحدود المتتالية.")

    # 324: Eisenstein's Criterion
    q("KAUST-P1-324", "Polynomials", "Medium",
      "Which prime \\( p \\) certifies the irreducibility over \\( \\mathbb{Q} \\) of \\( P(x) = x^3 - 6x^2 + 9x - 3 \\) via Eisenstein's Criterion?",
      "أي عدد أولي \\( p \\) يثبت عدم قابلية كثيرة الحدود \\( P(x) = x^3 - 6x^2 + 9x - 3 \\) للاختزال على \\( \\mathbb{Q} \\) باستخدام معيار أيزنشتاين؟",
      ["\\( p = 2 \\)", "\\( p = 3 \\)", "\\( p = 5 \\)", "\\( p = 7 \\)"], 1,
      "For \\( p = 3 \\): \\( 3 \\) does not divide the leading coefficient \\( 1 \\); \\( 3 \\) divides \\( -6, 9, -3 \\); and \\( 3^2 = 9 \\) does not divide the constant term \\( -3 \\). By Eisenstein's criterion, \\( P(x) \\) is irreducible over \\( \\mathbb{Q} \\). [Lineage: Eisenstein's Criterion / Abstract Algebra]",
      "للعدد الأولي \\( p = 3 \\): يقسم جميع المعاملات غير الرئيسة، ومربعه لا يقسم الحد الثابت، ولا يقسم المعامل الرئيسي. إذن كثيرة الحدود غير قابلة للاختزال. [المرجع: معيار أيزنشتاين للاختزال]",
      "Check prime divisibility of intermediate and constant terms.", "تحقق من قابلية قسمة المعاملات على العدد الأولي 3.")

    # 325: Partial fraction
    q("KAUST-P1-325", "Polynomials", "Medium",
      "Find the partial fraction decomposition coefficient \\( B \\) in \\( \\dfrac{2x + 3}{(x + 1)(x - 2)} = \\dfrac{A}{x + 1} + \\dfrac{B}{x - 2} \\).",
      "أوجد معامل التفكيك بالكسور الجزئية \\( B \\) في المتطابقة \\( \\dfrac{2x + 3}{(x + 1)(x - 2)} = \\dfrac{A}{x + 1} + \\dfrac{B}{x - 2} \\).",
      ["\\( -\\dfrac{1}{3} \\)", "\\( 1 \\)", "\\( \\dfrac{7}{3} \\)", "\\( 3 \\)"], 2,
      "Using the Heaviside cover-up method: multiply by \\( (x - 2) \\) and evaluate at \\( x = 2 \\): \\( B = \\dfrac{2(2) + 3}{2 + 1} = \\dfrac{7}{3} \\). [Lineage: Calculus Partial Fractions / STEP]",
      "بطريقة هيفيسايد: بالتعويض عن \\( x = 2 \\) في المقدار بعد حذف \\( (x-2) \\) نجد \\( B = \\dfrac{7}{3} \\). [المرجع: الكسور الجزئية في التفاضل والتكامل]",
      "Apply the cover-up method at \\( x = 2 \\).", "عوض بالقيمة التي تصفر مقام B بعد تغطيته.")

    # 326: de Moivre cos(3 theta)
    q("KAUST-P1-326", "Trigonometry", "Easy",
      "According to de Moivre's formula, which expression correctly gives \\( \\cos(3\\theta) \\) in terms of \\( \\cos\\theta \\)?",
      "وفقاً لصيغة دي موافر، أي تعبير يمثل \\( \\cos(3\\theta) \\) بدلالة \\( \\cos\\theta \\)؟",
      ["\\( 3\\cos\\theta - 4\\cos^3\\theta \\)", "\\( 4\\cos^3\\theta - 3\\cos\\theta \\)", "\\( 4\\cos^3\\theta + 3\\cos\\theta \\)", "\\( 3\\cos^2\\theta - 1 \\)"], 1,
      "Expanding \\( (\\cos\\theta + i\\sin\\theta)^3 = \\cos(3\\theta) + i\\sin(3\\theta) \\), the real part is \\( \\cos^3\\theta - 3\\cos\\theta\\sin^2\\theta = \\cos^3\\theta - 3\\cos\\theta(1 - \\cos^2\\theta) = 4\\cos^3\\theta - 3\\cos\\theta \\). [Lineage: de Moivre's Theorem / AMC 12]",
      "بفك المقدار \\( (\\cos\\theta + i\\sin\\theta)^3 \\) وأخذ الجزء الحقيقي: \\( 4\\cos^3\\theta - 3\\cos\\theta \\). [المرجع: مبرهنة دي موافر]",
      "Expand the real part of \\( e^{3i\\theta} \\).", "فك الجزء الحقيقي للأس التخيلي الثلاثي.")

    # 327: Sophie Germain Identity
    q("KAUST-P1-327", "Algebra", "Medium",
      "Using the Sophie Germain identity, how does \\( x^4 + 4 \\) factor into the product of two quadratic polynomials?",
      "باستخدام متطابقة صوفي جيرمان، كيف يُحلل المقدار \\( x^4 + 4 \\) إلى حاصل ضرب كثيرتي حدود من الدرجة الثانية؟",
      ["\\( (x^2 - 2)(x^2 + 2) \\)", "\\( (x^2 - 2x + 2)(x^2 + 2x + 2) \\)", "\\( (x^2 - 2x - 2)(x^2 + 2x - 2) \\)", "\\( (x^2 + 2)^2 \\)"], 1,
      "\\( x^4 + 4 = x^4 + 4x^2 + 4 - 4x^2 = (x^2 + 2)^2 - (2x)^2 = (x^2 - 2x + 2)(x^2 + 2x + 2) \\). [Lineage: Sophie Germain Identity / Olympiad Algebra]",
      "بإضافة وطرح \\( 4x^2 \\): \\( (x^2 + 2)^2 - (2x)^2 = (x^2 - 2x + 2)(x^2 + 2x + 2) \\). [المرجع: متطابقة صوفي جيرمان]",
      "Complete the square by adding and subtracting \\( 4x^2 \\).", "أكمل المربع بإضافة وطرح \\( 4x^2 \\).")

    # 328: Cubic Discriminant
    q("KAUST-P1-328", "Polynomials", "Medium",
      "For the depressed cubic equation \\( x^3 + px + q = 0 \\), what is the formula for the polynomial discriminant \\( \\Delta \\)?",
      "للمعادلة التكعيبية المختزلة \\( x^3 + px + q = 0 \\)، ما هي صيغة مميز كثيرة الحدود \\( \\Delta \\)؟",
      ["\\( -4p^3 - 27q^2 \\)", "\\( 4p^3 - 27q^2 \\)", "\\( -4p^2 - 27q^3 \\)", "\\( p^2 - 4q \\)"], 0,
      "The discriminant of \\( x^3 + px + q = 0 \\) is \\( \\Delta = -4p^3 - 27q^2 \\). If \\( \\Delta > 0 \\), there are three distinct real roots; if \\( \\Delta < 0 \\), one real root and two complex conjugate roots. [Lineage: Cardano-Tartaglia / Cubic Discriminant]",
      "مميز المعادلة التكعيبية المختزلة هو \\( \\Delta = -4p^3 - 27q^2 \\). [المرجع: صيغ كاردانو لحل المعادلات التكعيبية]",
      "Recall Cardano's discriminant formula for cubics.", "تذكر صيغة كاردانو لمميز المعادلة التكعيبية.")

    # 329: Conjugate root theorem
    q("KAUST-P1-329", "Polynomials", "Easy",
      "If \\( 2 + 3i \\) is a root of a polynomial with real coefficients, which other number MUST also be a root?",
      "إذا كان \\( 2 + 3i \\) جذراً لكثيرة حدود ذات معاملات حقيقية، فأي عدد آخر يجب أن يكون جذراً لها أيضاً؟",
      ["\\( -2 + 3i \\)", "\\( 2 - 3i \\)", "\\( -2 - 3i \\)", "\\( 3 + 2i \\)"], 1,
      "By the Complex Conjugate Root Theorem, if a polynomial has real coefficients and \\( z = a + bi \\) is a root, then its complex conjugate \\( \\bar{z} = a - bi = 2 - 3i \\) must also be a root. [Lineage: Complex Conjugate Root Theorem]",
      "حسب مبرهنة الجذور المترافقة لكثيرات الحدود الحقيقية، المرافق المركب \\( 2 - 3i \\) يجب أن يكون جذراً أيضاً. [المرجع: مبرهنة الجذور المترافقة]",
      "The complex conjugate of \\( a + bi \\) is \\( a - bi \\).", "المرافق المركب لـ \\( a+bi \\) هو \\( a-bi \\).")

    # 330: AM-GM minimum (Diagram)
    d330 = svg_box('<line x1="20" y1="150" x2="240" y2="150" stroke="#94a3b8" stroke-width="1.5"/><line x1="30" y1="160" x2="30" y2="20" stroke="#94a3b8" stroke-width="1.5"/><path d="M 40,30 Q 90,140 130,90 T 230,50" fill="none" stroke="#2563eb" stroke-width="2.5"/><circle cx="110" cy="90" r="5" fill="#ef4444"/><text x="120" y="95" font-size="12" fill="#ef4444" font-weight="bold">Min (3, 6)</text><line x1="110" y1="90" x2="110" y2="150" stroke="#ef4444" stroke-width="1" stroke-dasharray="3,3"/><text x="105" y="165" font-size="11" fill="#1e293b">x = 3</text>', "AM-GM Minimum", 360, 180)
    q("KAUST-P1-330", "Algebra & Inequalities", "Easy",
      "For positive real \\( x > 0 \\), what is the minimum value of the function \\( f(x) = x + \\dfrac{9}{x} \\)?",
      "للأعداد الحقيقية الموجبة \\( x > 0 \\)، ما هي أقل قيمة للدالة \\( f(x) = x + \\dfrac{9}{x} \\)؟",
      ["\\( 3 \\)", "\\( 6 \\)", "\\( 9 \\)", "\\( 12 \\)"], 1,
      "By the AM-GM inequality: \\( \\dfrac{x + 9/x}{2} \\ge \\sqrt{x \\cdot \\dfrac{9}{x}} = \\sqrt{9} = 3 \\implies x + \\dfrac{9}{x} \\ge 6 \\). Equality holds when \\( x = 9/x \\implies x = 3 \\). [Lineage: AM-GM Inequality / AMC 12]",
      "بمتراجحة المتوسطين الحسابي والهندسي: \\( x + 9/x \\ge 2\\sqrt{9} = 6 \\). وتتحقق المساواة عند \\( x = 3 \\). [المرجع: متراجحة المتوسطين الحسابي والهندسي]",
      "Apply AM-GM to \\( x \\) and \\( 9/x \\).", "طبق متراجحة AM-GM على الحدين.", diagram=d330)

    # 331: Binet's Formula
    q("KAUST-P1-331", "Sequences & Series", "Easy",
      "Binet's formula expresses the \\( n \\)-th Fibonacci number as \\( F_n = \\dfrac{\\phi^n - \\psi^n}{\\sqrt{5}} \\). What is the exact value of the golden ratio \\( \\phi \\)?",
      "تعبر صيغة بينيه عن عدد فيبوناتشي النوني بالصيغة \\( F_n = \\dfrac{\\phi^n - \\psi^n}{\\sqrt{5}} \\). ما هي القيمة الدقيقة للنسبة الذهبية \\( \\phi \\)؟",
      ["\\( \\dfrac{1 + \\sqrt{3}}{2} \\)", "\\( \\dfrac{1 + \\sqrt{5}}{2} \\)", "\\( \\dfrac{1 + \\sqrt{5}}{4} \\)", "\\( 1 + \\sqrt{5} \\)"], 1,
      "The golden ratio is the positive root of \\( x^2 - x - 1 = 0 \\), which is \\( \\phi = \\dfrac{1 + \\sqrt{5}}{2} \\approx 1.618 \\). [Lineage: Fibonacci / Golden Ratio]",
      "النسبة الذهبية هي الجذر الموجب للمعادلة \\( x^2 - x - 1 = 0 \\): \\( \\phi = \\dfrac{1 + \\sqrt{5}}{2} \\). [المرجع: النسبة الذهبية ومتتالية فيبوناتشي]",
      "Solve \\( x^2 - x - 1 = 0 \\).", "حل المعادلة التربيعية للنسبة الذهبية.")

    # 332: Fibonacci Generating Function
    q("KAUST-P1-332", "Sequences & Series", "Medium",
      "What is the closed-form generating function \\( F(x) = \\sum_{n=0}^{\\infty} F_n x^n \\) for the Fibonacci sequence (where \\( F_0 = 0, F_1 = 1 \\))?",
      "ما هي الدالة المولدة ذات الشكل المغلق \\( F(x) = \\sum_{n=0}^{\\infty} F_n x^n \\) لمتتالية فيبوناتشي (حيث \\( F_0 = 0, F_1 = 1 \\))؟",
      ["\\( \\dfrac{1}{1 - x - x^2} \\)", "\\( \\dfrac{x}{1 - x - x^2} \\)", "\\( \\dfrac{x}{1 - 2x - x^2} \\)", "\\( \\dfrac{1 - x}{1 - x - x^2} \\)"], 1,
      "Using the recurrence \\( F_n = F_{n-1} + F_{n-2} \\): \\( F(x) - x F(x) - x^2 F(x) = F_0 + (F_1 - F_0)x = x \\). Hence \\( F(x) = \\dfrac{x}{1 - x - x^2} \\). [Lineage: Generating Functions / Cambridge Tripos]",
      "باستخدام العلاقة التكرارية \\( F_n = F_{n-1} + F_{n-2} \\) والشروط الابتدائية نجد \\( F(x) = \\dfrac{x}{1 - x - x^2} \\). [المرجع: الدوال المولدة في الرياضيات المتقطعة]",
      "Multiply the generating function by \\( (1 - x - x^2) \\).", "اضرب الدالة المولدة في كثير الحدود المميز المعكوس.")

    # 333: Sum of Squares
    q("KAUST-P1-333", "Sequences & Series", "Easy",
      "What is the exact sum of the first \\( 10 \\) positive squares: \\( 1^2 + 2^2 + \\dots + 10^2 \\)?",
      "ما هو المجموع الدقيق لمربعات أول 10 أعداد صحيحة موجبة: \\( 1^2 + 2^2 + \\dots + 10^2 \\)؟",
      ["\\( 330 \\)", "\\( 385 \\)", "\\( 420 \\)", "\\( 505 \\)"], 1,
      "Using the formula \\( \\sum_{k=1}^n k^2 = \\dfrac{n(n+1)(2n+1)}{6} \\): For \\( n = 10 \\), \\( \\dfrac{10(11)(21)}{6} = 5 \\times 11 \\times 7 = 385 \\). [Lineage: Sum of Squares Formula / AMC 12]",
      "بالقانون: \\( \\dfrac{10 \\times 11 \\times 21}{6} = 385 \\). [المرجع: مجموع المربعات]",
      "Use \\( \\frac{n(n+1)(2n+1)}{6} \\).", "طبق قانون مجموع المربعات.")

    # 334: Sum of Cubes
    q("KAUST-P1-334", "Sequences & Series", "Easy",
      "What is the value of \\( 1^3 + 2^3 + \\dots + 10^3 \\)?",
      "ما هي قيمة المجموع \\( 1^3 + 2^3 + \\dots + 10^3 \\)؟",
      ["\\( 2500 \\)", "\\( 3025 \\)", "\\( 3600 \\)", "\\( 4225 \\)"], 1,
      "Nicomachus's Theorem states \\( \\sum_{k=1}^n k^3 = \\left( \\sum_{k=1}^n k \\right)^2 = \\left( \\dfrac{n(n+1)}{2} \\right)^2 \\). For \\( n = 10 \\): \\( 55^2 = 3025 \\). [Lineage: Nicomachus Theorem / Sum of Cubes]",
      "مبرهنة نيقوماخوس: مجموع المكعبات يساوي مربع مجموع الأعداد: \\( 55^2 = 3025 \\). [المرجع: مبرهنة نيقوماخوس لمجموع المكعبات]",
      "Square the triangular number 55.", "ربع العدد المثلثي 55.")

    # 335: Ratio Test for e^x
    q("KAUST-P1-335", "Sequences & Series", "Easy",
      "What is the radius of convergence \\( R \\) of the Maclaurin series for \\( e^x = \\sum_{n=0}^{\\infty} \\dfrac{x^n}{n!} \\)?",
      "ما هو نصف قطر التقارب \\( R \\) لمتسلسلة ماكلوران للدالة الأسية \\( e^x = \\sum_{n=0}^{\\infty} \\dfrac{x^n}{n!} \\)؟",
      ["\\( R = 1 \\)", "\\( R = e \\)", "\\( R = \\pi \\)", "\\( R = \\infty \\)"], 3,
      "By the ratio test: \\( \\lim_{n \\to \\infty} \\left| \\dfrac{x^{n+1}/(n+1)!}{x^n/n!} \\right| = \\lim_{n \\to \\infty} \\dfrac{|x|}{n+1} = 0 < 1 \\) for all real \\( x \\). Thus, the radius of convergence is \\( R = \\infty \\). [Lineage: Calculus Series Convergence / STEP]",
      "باختبار النسبة: نهاية النسبة بين حدين متتاليين تساوي صفراً لجميع قيم x، إذن نصف قطر التقارب هو \\( R = \\infty \\). [المرجع: اختبار النسبة للمتسلسلات]",
      "Compute \\( \\lim |a_{n+1}/a_n| \\).", "احسب نهاية النسبة بين الحدود.")

    # 336: Alternating Series Error
    q("KAUST-P1-336", "Sequences & Series", "Easy",
      "For an alternating series \\( \\sum_{n=1}^{\\infty} (-1)^{n-1} a_n \\) satisfying the Leibniz criteria, the absolute error \\( |S - S_N| \\) of the \\( N \\)-th partial sum is strictly bounded by:",
      "لمتسلسلة متناوبة \\( \\sum_{n=1}^{\\infty} (-1)^{n-1} a_n \\) تحقق شروط لايبنتز، الخطأ المطلق \\( |S - S_N| \\) للمجموع الجزئي النوني محصور بـ:",
      ["\\( a_N \\)", "\\( a_{N+1} \\)", "\\( a_{N+2} \\)", "\\( \\dfrac{a_{N+1}}{2} \\)"], 1,
      "The Alternating Series Estimation Theorem guarantees that \\( |S - S_N| \\le a_{N+1} \\), meaning the error never exceeds the magnitude of the first omitted term. [Lineage: Leibniz Alternating Series]",
      "مبرهنة تقدير الخطأ للمتسلسلات المتناوبة تضمن أن الخطأ لا يتجاوز مقدار أول حد مهمل \\( a_{N+1} \\). [المرجع: مبرهنة لايبنتز]",
      "The error is bounded by the first omitted term.", "الخطأ محصور بأول حد تم استبعاده.")

    # 337: Limit (1 + 2/n)^n
    q("KAUST-P1-337", "Calculus & Limits", "Easy",
      "Evaluate the limit: \\( \\lim_{n \\to \\infty} \\left(1 + \\dfrac{2}{n}\\right)^n \\).",
      "احسب قيمة النهاية: \\( \\lim_{n \\to \\infty} \\left(1 + \\dfrac{2}{n}\\right)^n \\).",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( e \\)", "\\( e^2 \\)"], 3,
      "Using the standard exponential limit \\( \\lim_{n \\to \\infty} \\left(1 + \\dfrac{x}{n}\\right)^n = e^x \\): With \\( x = 2 \\), the limit is \\( e^2 \\). [Lineage: Standard Limits / STEP]",
      "باستخدام النهاية الأسية الأساسية \\( \\lim (1 + x/n)^n = e^x \\): عند \\( x = 2 \\) تكون النهاية \\( e^2 \\). [المرجع: النهايات الأسية]",
      "Recall \\( \\lim (1 + x/n)^n = e^x \\).", "تذكر تعريف الدالة الأسية كنهاية.")

    # 338: Squeeze Theorem
    q("KAUST-P1-338", "Calculus & Limits", "Easy",
      "Evaluate the limit \\( \\lim_{n \\to \\infty} \\dfrac{\\cos(n)}{n} \\).",
      "احسب قيمة النهاية \\( \\lim_{n \\to \\infty} \\dfrac{\\cos(n)}{n} \\).",
      ["\\( -1 \\)", "\\( 0 \\)", "\\( 1 \\)", "Does not exist"], 1,
      "Since \\( -1 \\le \\cos(n) \\le 1 \\) for all \\( n \\), we have \\( -\\dfrac{1}{n} \\le \\dfrac{\\cos(n)}{n} \\le \\dfrac{1}{n} \\). Since \\( \\lim (-1/n) = \\lim (1/n) = 0 \\), by the Squeeze Theorem the limit is \\( 0 \\). [Lineage: Squeeze Theorem / High School Gifted]",
      "بما أن \\( -1 \\le \\cos(n) \\le 1 \\)، وبقسمة الأطراف على n وأخذ النهاية نجد أنها محصورة بين الصفرين، فتساوي 0 بنظرية الشطيرة (الإحاطة). [المرجع: مبرهنة الإحاطة]",
      "Bound \\( \\cos(n) \\) between \\( -1 \\) and \\( 1 \\).", "احصر جيب التمام بين -1 و 1.")

    # 339: Infinite Geometric Series
    q("KAUST-P1-339", "Sequences & Series", "Easy",
      "Find the exact sum of the infinite series \\( \\sum_{n=0}^{\\infty} \\left(\\dfrac{2}{3}\\right)^n = 1 + \\dfrac{2}{3} + \\dfrac{4}{9} + \\dots \\).",
      "أوجد المجموع الدقيق للمتسلسلة الهندسية اللانهائية \\( \\sum_{n=0}^{\\infty} \\left(\\dfrac{2}{3}\\right)^n \\).",
      ["\\( 2 \\)", "\\( \\dfrac{5}{2} \\)", "\\( 3 \\)", "\\( \\dfrac{9}{2} \\)"], 2,
      "For a geometric series with \\( |r| < 1 \\): \\( S = \\dfrac{a}{1 - r} = \\dfrac{1}{1 - 2/3} = \\dfrac{1}{1/3} = 3 \\). [Lineage: Geometric Series Formula / AMC 12]",
      "مجموع المتسلسلة الهندسية: \\( S = \\dfrac{a}{1 - r} = \\dfrac{1}{1 - 2/3} = 3 \\). [المرجع: المتسلسلات الهندسية]",
      "Use \\( S = \\frac{a}{1 - r} \\).", "طبق قانون مجموع المتسلسلة الهندسية.")

    # 340: Harmonic Divergence
    q("KAUST-P1-340", "Sequences & Series", "Easy",
      "Which test formally proves that the harmonic series \\( \\sum_{n=1}^{\\infty} \\dfrac{1}{n} \\) diverges by comparing it to \\( \\int_1^{\\infty} \\dfrac{1}{x} \\, dx \\)?",
      "أي اختبار يثبت رسمياً تباعد المتسلسلة التوافقية \\( \\sum_{n=1}^{\\infty} \\dfrac{1}{n} \\) بمقارنتها بالتكامل \\( \\int_1^{\\infty} \\dfrac{1}{x} \\, dx \\)؟",
      ["The Ratio Test", "The Root Test", "The Integral Test", "The Alternating Series Test"], 2,
      "The Integral Test compares the series to \\( \\int_1^\\infty \\dfrac{1}{x} dx = [\\ln x]_1^\\infty = \\infty \\). Since the improper integral diverges, the series also diverges. [Lineage: Integral Test for Series]",
      "اختبار التكامل يقارن المتسلسلة بالتكامل المعتل \\( \\int_1^\\infty \\frac{1}{x} dx = \\infty \\)، مما يثبت تباعدها. [المرجع: اختبار التكامل للمتسلسلات]",
      "The test using improper integrals is the Integral Test.", "الاختبار الذي يستخدم التكاملات المعتلة هو اختبار التكامل.")

    # 341: Ellipse Foci (Diagram)
    d341 = svg_box('<ellipse cx="130" cy="90" rx="90" ry="54" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/><line x1="20" y1="90" x2="240" y2="90" stroke="#94a3b8" stroke-width="1.5"/><line x1="130" y1="20" x2="130" y2="160" stroke="#94a3b8" stroke-width="1.5"/><circle cx="58" cy="90" r="4.5" fill="#ef4444"/><circle cx="202" cy="90" r="4.5" fill="#ef4444"/><text x="45" y="110" font-size="12" fill="#ef4444" font-weight="bold">F1(-4,0)</text><text x="190" y="110" font-size="12" fill="#ef4444" font-weight="bold">F2(4,0)</text>', "Ellipse Foci", 360, 180)
    q("KAUST-P1-341", "Geometry", "Easy",
      "What is the distance between the two foci of the ellipse \\( \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1 \\)?",
      "ما هي المسافة بين بؤرتي القطع الناقص \\( \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1 \\)؟",
      ["\\( 6 \\)", "\\( 8 \\)", "\\( 10 \\)", "\\( 16 \\)"], 1,
      "Here \\( a^2 = 25 \\) and \\( b^2 = 9 \\). The focal distance is \\( c = \\sqrt{a^2 - b^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4 \\). The distance between the foci is \\( 2c = 2(4) = 8 \\). [Lineage: Analytic Geometry / JEE Main]",
      "\\( c = \\sqrt{25 - 9} = 4 \\). البعد بين البؤرتين هو \\( 2c = 8 \\). [المرجع: القطوع المخروطية]",
      "Use \\( c = \\sqrt{a^2 - b^2} \\) and double it.", "احسب البعد البؤري واضربه في 2.", diagram=d341)

    # 342: Parabola Directrix
    q("KAUST-P1-342", "Geometry", "Easy",
      "What is the equation of the directrix of the parabola \\( y^2 = 12x \\)?",
      "ما هي معادلة الدليل للقطع المكافئ \\( y^2 = 12x \\)؟",
      ["\\( x = -3 \\)", "\\( x = 3 \\)", "\\( y = -3 \\)", "\\( x = -6 \\)"], 0,
      "Comparing \\( y^2 = 4ax \\) with \\( y^2 = 12x \\) gives \\( 4a = 12 \\implies a = 3 \\). The directrix of a right-opening parabola is \\( x = -a = -3 \\). [Lineage: Conic Sections / Parabola]",
      "بالمقارنة مع \\( y^2 = 4ax \\) نجد \\( a = 3 \\). معادلة الدليل هي \\( x = -a = -3 \\). [المرجع: القطع المكافئ]",
      "Compare with the standard form \\( y^2 = 4ax \\).", "قارن بالصورة القياسية لمعادلة القطع المكافئ.")

    # 343: Ceva's Theorem
    q("KAUST-P1-343", "Geometry", "Medium",
      "In \\( \\triangle ABC \\), cevians \\( AD, BE, CF \\) concur at a single interior point \\( P \\). According to Ceva's Theorem, what is the value of \\( \\dfrac{AF}{FB} \\cdot \\dfrac{BD}{DC} \\cdot \\dfrac{CE}{EA} \\)?",
      "في المثلث \\( ABC \\)، تتقاطع المستقيمات الراسية \\( AD, BE, CF \\) في نقطة داخلية واحدة \\( P \\). وفقاً لمبرهنة سيفا، ما هي قيمة المقدار \\( \\dfrac{AF}{FB} \\cdot \\dfrac{BD}{DC} \\cdot \\dfrac{CE}{EA} \\)؟",
      ["\\( \\dfrac{1}{2} \\)", "\\( 1 \\)", "\\( 2 \\)", "\\( 3 \\)"], 1,
      "Ceva's Theorem states that cevians from the three vertices of a triangle are concurrent if and only if \\( \\dfrac{AF}{FB} \\cdot \\dfrac{BD}{DC} \\cdot \\dfrac{CE}{EA} = 1 \\). [Lineage: Ceva's Theorem / Olympiad Geometry]",
      "تنص مبرهنة سيفا على أن المستقيمات تتقاطع في نقطة واحدة إذا وفقط إذا كان حاصل ضرب نسب التقسيم يساوي 1. [المرجع: مبرهنة سيفا في الهندسة]",
      "Recall the statement of Ceva's theorem.", "تذكر نص مبرهنة سيفا لتقاطع المستقيمات.")

    # 344: Menelaus' Theorem
    q("KAUST-P1-344", "Geometry", "Medium",
      "Which famous classical theorem states that points \\( D, E, F \\) on the extended sides of \\( \\triangle ABC \\) are collinear if and only if \\( \\dfrac{AF}{FB} \\cdot \\dfrac{BD}{DC} \\cdot \\dfrac{CE}{EA} = 1 \\)?",
      "أي مبرهنة كلاسيكية شهيرة تنص على أن النقاط \\( D, E, F \\) الواقعة على امتدادات أضلاع المثلث \\( ABC \\) تكون على استقامة واحدة إذا وفقط إذا كان حاصل ضرب نسب التقسيم يساوي 1؟",
      ["Ptolemy's Theorem", "Menelaus' Theorem", "Stewart's Theorem", "Euler's Theorem"], 1,
      "Menelaus' Theorem provides the criterion for collinearity of points lying on the lines containing the sides of a triangle. [Lineage: Menelaus' Theorem / Geometry]",
      "مبرهنة مينلاوس هي المبرهنة المعيارية لاستقامة النقاط على أضلاع المثلث. [المرجع: مبرهنة مينلاوس]",
      "Differentiate between Ceva (concurrence) and Menelaus (collinearity).", "ميز بين مبرهنة سيفا للتقاطع ومينلاوس للاستقامة.")

    # 345: Angle Bisector Theorem
    q("KAUST-P1-345", "Geometry", "Easy",
      "In \\( \\triangle ABC \\), \\( AB = 6 \\), \\( AC = 10 \\), and \\( BC = 8 \\). The internal bisector of \\( \\angle A \\) meets \\( BC \\) at point \\( D \\). What is the length of segment \\( BD \\)?",
      "في المثلث \\( ABC \\)، الأضلاع هي \\( AB = 6 \\)، \\( AC = 10 \\)، و \\( BC = 8 \\). ينصف منصف الزاوية \\( A \\) الضلع \\( BC \\) عند النقطة \\( D \\). ما هو طول القطعة \\( BD \\)؟",
      ["\\( 2.5 \\)", "\\( 3 \\)", "\\( 3.5 \\)", "\\( 4 \\)"], 1,
      "By the Angle Bisector Theorem: \\( \\dfrac{BD}{DC} = \\dfrac{AB}{AC} = \\dfrac{6}{10} = \\dfrac{3}{5} \\). Since \\( BD + DC = 8 \\), \\( BD = \\dfrac{3}{3 + 5} \\times 8 = 3 \\). [Lineage: Angle Bisector Theorem / AMC 12]",
      "حسب نظرية منصف الزاوية الداخلي: \\( \\dfrac{BD}{DC} = \\dfrac{6}{10} = \\dfrac{3}{5} \\). إذن \\( BD = \\dfrac{3}{8} \\times 8 = 3 \\). [المرجع: نظرية منصف الزاوية]",
      "Apply the ratio \\( BD/DC = AB/AC \\).", "طبق نسبة أطوال الأضلاع على قطعتي الضلع المقابل.")

    # 346: Point-to-line distance
    q("KAUST-P1-346", "Geometry", "Easy",
      "What is the shortest perpendicular distance from the point \\( (1, 2) \\) to the line \\( 3x + 4y - 1 = 0 \\)?",
      "ما هي أقصر مسافة عمودية من النقطة \\( (1, 2) \\) إلى المستقيم \\( 3x + 4y - 1 = 0 \\)؟",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( 2.5 \\)", "\\( 3 \\)"], 1,
      "\\( d = \\dfrac{|3(1) + 4(2) - 1|}{\\sqrt{3^2 + 4^2}} = \\dfrac{|3 + 8 - 1|}{5} = \\dfrac{10}{5} = 2 \\). [Lineage: Coordinate Geometry / High School]",
      "باستخدام قانون بعد نقطة عن مستقيم: \\( d = \\dfrac{|3(1) + 4(2) - 1|}{5} = \\dfrac{10}{5} = 2 \\). [المرجع: الهندسة الإحداثية]",
      "Use \\( d = \\frac{|Ax_0 + By_0 + C|}{\\sqrt{A^2 + B^2}} \\).", "طبق قانون بعد نقطة عن مستقيم.")

    # 347: Heron's Formula
    q("KAUST-P1-347", "Geometry", "Easy",
      "Using Heron's formula, calculate the area of an isosceles triangle with side lengths \\( 5, 5, \\) and \\( 6 \\).",
      "باستخدام صيغة هيرون، احسب مساحة مثلث متطابق الضلعين أطوال أضلاعه \\( 5 \\) و \\( 5 \\) و \\( 6 \\).",
      ["\\( 10 \\)", "\\( 12 \\)", "\\( 14 \\)", "\\( 15 \\)"], 1,
      "Semi-perimeter: \\( s = \\dfrac{5 + 5 + 6}{2} = 8 \\). By Heron's formula: \\( \\text{Area} = \\sqrt{s(s-a)(s-b)(s-c)} = \\sqrt{8(8-5)(8-5)(8-6)} = \\sqrt{8 \\times 3 \\times 3 \\times 2} = \\sqrt{144} = 12 \\). [Lineage: Heron's Formula / AMC 12]",
      "نصف المحيط: \\( s = 8 \\). المساحة: \\( \\sqrt{8 \\times 3 \\times 3 \\times 2} = \\sqrt{144} = 12 \\). [المرجع: صيغة هيرون لحساب المساحة]",
      "Compute \\( s = 8 \\) and evaluate the square root.", "احسب نصف المحيط ثم عوض في جذر هيرون.")

    # 348: Inradius right triangle
    q("KAUST-P1-348", "Geometry", "Easy",
      "What is the radius \\( r \\) of the incircle (inradius) of a right-angled triangle with sides \\( 6, 8, \\) and \\( 10 \\)?",
      "ما هو نصف قطر الدائرة الداخلية المماسة (inradius) لمثلث قائم الزاوية أطوال أضلاعه \\( 6 \\) و \\( 8 \\) و \\( 10 \\)؟",
      ["\\( 1.5 \\)", "\\( 2 \\)", "\\( 2.5 \\)", "\\( 3 \\)"], 1,
      "For a right triangle with legs \\( a, b \\) and hypotenuse \\( c \\), \\( r = \\dfrac{a + b - c}{2} = \\dfrac{6 + 8 - 10}{2} = \\dfrac{4}{2} = 2 \\). [Lineage: Incircle of Right Triangle / AMC 12]",
      "في المثلث القائم: \\( r = \\dfrac{a + b - c}{2} = \\dfrac{6 + 8 - 10}{2} = 2 \\). [المرجع: الدائرة الداخلية للمثلث القائم]",
      "Use \\( r = (a + b - c)/2 \\) for right triangles.", "استخدم قانون نصف قطر الدائرة الداخلية للمثلث القائم.")

    # 349: Circumradius right triangle
    q("KAUST-P1-349", "Geometry", "Easy",
      "What is the circumradius \\( R \\) of a right-angled triangle with hypotenuse of length \\( 10 \\)?",
      "ما هو نصف قطر الدائرة المحيطة \\( R \\) بمثلث قائم الزاوية طول وتره \\( 10 \\)؟",
      ["\\( 4 \\)", "\\( 5 \\)", "\\( 6 \\)", "\\( 10 \\)"], 1,
      "By Thales's Theorem, the hypotenuse of a right triangle inscribed in a circle is a diameter. Thus, the circumradius is \\( R = \\dfrac{c}{2} = \\dfrac{10}{2} = 5 \\). [Lineage: Thales's Theorem / Circumradius]",
      "وفق نظرية طاليس، وتر المثلث القائم يمثل قطراً في الدائرة المحيطة به، إذن نصف القطر هو \\( R = 10/2 = 5 \\). [المرجع: نظرية طاليس]",
      "The circumradius of a right triangle is half its hypotenuse.", "نصف قطر الدائرة المحيطة بالمثلث القائم يساوي نصف طول الوتر.")

    # 350: Radical Axis
    q("KAUST-P1-350", "Geometry", "Medium",
      "What is the equation of the radical axis of the two circles \\( x^2 + y^2 = 4 \\) and \\( (x - 4)^2 + y^2 = 4 \\)?",
      "ما هي معادلة المحور الجذري للدائرتين \\( x^2 + y^2 = 4 \\) و \\( (x - 4)^2 + y^2 = 4 \\)؟",
      ["\\( x = 1 \\)", "\\( x = 2 \\)", "\\( y = 2 \\)", "\\( x = 4 \\)"], 1,
      "Expanding the second circle: \\( x^2 - 8x + 16 + y^2 - 4 = 0 \\implies x^2 + y^2 - 8x + 12 = 0 \\). Subtracting \\( x^2 + y^2 - 4 = 0 \\) yields: \\( -8x + 16 = 0 \\implies 8x = 16 \\implies x = 2 \\). [Lineage: Radical Axis of Circles / Geometry]",
      "بطرح معادلتي الدائرتين نحصل على: \\( -8x + 16 = 0 \\implies x = 2 \\). [المرجع: المحور الجذري للدائرتين]",
      "Subtract the two circle equations in standard form.", "اطرح معادلتي الدائرتين بالصورة العامة.")

    return questions

if __name__ == "__main__":
    qs = get_part_b()
    print(f"Generated {len(qs)} Part B questions (301-350).")
