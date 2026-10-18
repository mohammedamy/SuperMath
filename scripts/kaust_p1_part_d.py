#!/usr/bin/env python3
"""
KAUST Phase 1 Questions Part D: 401 to 450
Combinatorics, Number Theory, Linear Algebra, Geometry, Probability.
"""

def get_part_d():
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

    # 401: Dirichlet's approximation
    q("KAUST-P1-401", "Number Theory", "Hard",
      "Dirichlet's approximation theorem states that for any real number \\( \\alpha \\) and integer \\( N \\ge 1 \\), there exist integers \\( p, q \\) with \\( 1 \\le q \\le N \\) such that:",
      "تنص مبرهنة ديركلي للتقريب على أنه لأي عدد حقيقي \\( \\alpha \\) وعدد صحيح \\( N \\ge 1 \\)، يوجد عددان صحيحان \\( p, q \\) بحيث \\( 1 \\le q \\le N \\) ويحققان:",
      ["\\( |q\\alpha - p| < \\dfrac{1}{N} \\)", "\\( |q\\alpha - p| < \\dfrac{1}{N^2} \\)", "\\( |q\\alpha - p| = 0 \\)", "\\( |q\\alpha - p| < \\dfrac{1}{2} \\)"], 0,
      "Dirichlet proved using the pigeonhole principle on fractional parts that \\( |q\\alpha - p| < \\dfrac{1}{N} \\), which implies \\( \\left| \\alpha - \\dfrac{p}{q} \\right| < \\dfrac{1}{qN} \\le \\dfrac{1}{q^2} \\). [Lineage: Dirichlet's Approximation Theorem / Putnam]",
      "أثبت ديركلي بمبدأ برج الحمام على الأجزاء الكسرية أن \\( |q\\alpha - p| < 1/N \\). [المرجع: مبرهنة ديركلي للتقريب الديوفانتي]",
      "Recall Dirichlet's bound for Diophantine approximation.", "تذكر حد ديركلي للتقريب الكسري.")

    # 402: Surjective functions
    q("KAUST-P1-402", "Combinatorics", "Medium",
      "How many surjective (onto) functions from a 4-element set \\( A \\) to a 3-element set \\( B \\) exist?",
      "كم دالة شاملة (surjective) توجد من مجموعة \\( A \\) ذات 4 عناصر إلى مجموعة \\( B \\) ذات 3 عناصر؟",
      ["\\( 24 \\)", "\\( 36 \\)", "\\( 64 \\)", "\\( 81 \\)"], 1,
      "The number of surjective functions is \\( k! S(n, k) \\). For \\( n = 4, k = 3 \\): \\( S(4, 3) = 6 \\), so \\( 3! \\times 6 = 6 \\times 6 = 36 \\). [Lineage: Surjective Functions / Combinatorics]",
      "عدد الدوال الشاملة هو \\( k! S(n, k) = 3! \\times 6 = 36 \\). [المرجع: الدوال الشاملة وأعداد ستيرلينغ]",
      "Multiply \\( 3! \\) by the Stirling number \\( S(4, 3) \\).", "اضرب مضروب 3 في عدد ستيرلينغ من النوع الثاني.")

    # 403: Graph isomorphism invariant
    q("KAUST-P1-403", "Graph Theory", "Easy",
      "Which of the following is NOT an invariant under graph isomorphism?",
      "أي مما يلي لا يُعد من الثوابت (invariants) المحفوظة تحت تماثل الرسوم البيانية؟",
      ["Number of vertices", "Degree sequence", "Vertex labels / names", "Chromatic number"], 2,
      "Graph isomorphism preserves all intrinsic structural properties (degrees, edges, cycles, chromatic number), but vertex labels are arbitrary naming choices that do not affect the graph structure. [Lineage: Graph Isomorphism]",
      "التماثل يحفظ البنية المجردة للرسم بينما أسماء أو مسميات الرؤوس هي تسميات اعتباطية. [المرجع: تماثل الرسوم البيانية]",
      "Which feature is purely cosmetic rather than structural?", "أي من الخواص شكلية فقط ولا تتبع بنية الرسم؟")

    # 404: Berge's Lemma
    q("KAUST-P1-404", "Graph Theory", "Medium",
      "Berge's Lemma states that a matching \\( M \\) in a graph is of maximum cardinality if and only if there is NO:",
      "تنص توطئة بيرج على أن التطابق \\( M \\) في رسم بياني يكون أعظمياً إذا وفقط إذا خلا الرسم من أي:",
      ["Alternating cycle", "Augmenting path", "Isolated vertex", "Bridge edge"], 1,
      "Claude Berge proved in 1957 that a matching \\( M \\) is maximum if and only if there is no augmenting path with respect to \\( M \\). [Lineage: Berge's Lemma / Matching Theory]",
      "أثبت بيرج أن التطابق يكون أعظمياً إذا وفقط إذا لم يوجد مسار تعزيز (augmenting path). [المرجع: توطئة بيرج في نظرية التطابق]",
      "Recall the augmenting path theorem for matchings.", "تذكر مبرهنة مسارات التعزيز للتطابق الأعظمي.")

    # 405: Eulerian trail
    q("KAUST-P1-405", "Graph Theory", "Easy",
      "A connected graph has an open Eulerian trail (starting and ending at different vertices) if and only if it has exactly:",
      "يمتلك رسم بياني متصل مساراً أويلرياً مفتوحاً (يبدأ وينتهي برأسين مختلفين) إذا وفقط إذا كان يحتوي بالضبط على:",
      ["0 odd-degree vertices", "2 odd-degree vertices", "4 odd-degree vertices", "All odd-degree vertices"], 1,
      "An open Eulerian trail must start at one odd vertex and end at the other odd vertex, so exactly two vertices must have odd degree. [Lineage: Euler Trail Theorem]",
      "المسار الأويلري المفتوح يتطلب أن يكون رأسا البداية والنهاية فرديي الدرجة، لذا يجب أن يكون هناك رأسان فرديان بالضبط. [المرجع: مبرهنة المسار الأويلري]",
      "The endpoints must be the only vertices with odd degree.", "طرفا المسار هما الرأسان الوحيدان ذوا الدرجة الفردية.")

    # 406: Wilson's Corollary
    q("KAUST-P1-406", "Number Theory", "Medium",
      "For any prime \\( p \\), what is the value of \\( (p - 2)! \\pmod p \\)?",
      "لأي عدد أولي \\( p \\)، ما هي قيمة \\( (p - 2)! \\pmod p \\)؟",
      ["\\( -1 \\)", "\\( 0 \\)", "\\( 1 \\)", "\\( p - 1 \\)"], 2,
      "By Wilson's theorem: \\( (p - 1)! = (p - 1)(p - 2)! \\equiv -1 \\pmod p \\). Since \\( p - 1 \\equiv -1 \\pmod p \\), we divide by \\( -1 \\) to get \\( (p - 2)! \\equiv 1 \\pmod p \\). [Lineage: Wilson's Theorem Corollary]",
      "بما أن \\( (p-1)! \\equiv -1 \\) و \\( p-1 \\equiv -1 \\)، بالقسمة نحصل على \\( (p-2)! \\equiv 1 \\pmod p \\). [المرجع: نتائج مبرهنة ويلسون]",
      "Divide Wilson's theorem \\( (p-1)! \\equiv -1 \\) by \\( (p-1) \\equiv -1 \\).", "اقسم تطابق ويلسون على -1.")

    # 407: Totient Multiplicative
    q("KAUST-P1-407", "Number Theory", "Easy",
      "Euler's totient function \\( \\phi(n) \\) is strictly multiplicative, meaning \\( \\phi(mn) = \\phi(m)\\phi(n) \\) holds whenever:",
      "تكون دالة أويلر المؤشرية \\( \\phi(n) \\) ضربية تماماً، أي \\( \\phi(mn) = \\phi(m)\\phi(n) \\)، عندما يتحقق الشرط:",
      ["\\( m = n \\)", "\\( \\gcd(m, n) = 1 \\)", "\\( m \\) is prime", "\\( n \\) is prime"], 1,
      "A number-theoretic function is multiplicative if \\( f(mn) = f(m)f(n) \\) whenever \\( \\gcd(m, n) = 1 \\). [Lineage: Multiplicative Arithmetic Functions]",
      "تكون الدالة الحسابية ضربية إذا تحقق التفكيك عند كون العددين أوليين نسبياً \\( \\gcd(m, n) = 1 \\). [المرجع: الدوال الحسابية الضربية]",
      "Recall the definition of a multiplicative arithmetic function.", "تذكر شرط أولية العددين نسبياً للدوال الضربية.")

    # 408: Primitive root existence
    q("KAUST-P1-408", "Number Theory", "Medium",
      "A primitive root modulo \\( m \\) exists if and only if \\( m \\) is equal to:",
      "يوجد جذر بدائي مقياس \\( m \\) إذا وفقط إذا كان \\( m \\) من الصورة:",
      ["Any integer \\( m \\ge 2 \\)", "\\( 2, 4, p^k, \\) or \\( 2p^k \\) (for odd prime \\( p \\))", "Any power of 2", "Any composite number"], 1,
      "Gauss proved that primitive roots exist exclusively for \\( m \\in \\{2, 4, p^k, 2p^k\\} \\) where \\( p \\) is an odd prime and \\( k \\ge 1 \\). [Lineage: Gauss Disquisitiones Arithmeticae]",
      "أثبت غاوس أن الجذور البدائية توجد حصرياً للمقاييس \\( 2, 4, p^k, 2p^k \\) حيث p أولي فردي. [المرجع: مبرهنة غاوس للجذور البدائية]",
      "Recall Gauss's characterization of moduli having primitive roots.", "تذكر مبرهنة غاوس للمقاييس ذات الجذور البدائية.")

    # 409: Pythagorean Triples
    q("KAUST-P1-409", "Number Theory", "Easy",
      "In Euclid's formula for generating primitive Pythagorean triples \\( (a, b, c) \\) from coprime integers \\( m > n > 0 \\) of opposite parity, the hypotenuse \\( c \\) is given by:",
      "في صيغة إقليدس لتوليد الثلاثيات الفيثاغورسية الأولية \\( (a, b, c) \\) من عددين أوليين نسبياً \\( m > n > 0 \\) مختلفي الزوجية، يُعطى الوتر \\( c \\) بـ:",
      ["\\( m^2 - n^2 \\)", "\\( 2mn \\)", "\\( m^2 + n^2 \\)", "\\( (m + n)^2 \\)"], 2,
      "Euclid's formula states \\( a = m^2 - n^2 \\), \\( b = 2mn \\), and \\( c = m^2 + n^2 \\). Notice \\( (m^2 - n^2)^2 + (2mn)^2 = (m^2 + n^2)^2 \\). [Lineage: Pythagorean Triples / Euclid]",
      "صيغة إقليدس للوتر هي \\( c = m^2 + n^2 \\) حيث تحقق \\( a^2 + b^2 = c^2 \\). [المرجع: الثلاثيات الفيثاغورسية]",
      "Check which expression satisfies \\( a^2 + b^2 = c^2 \\).", "تأكد من المتطابقة \\( (m^2-n^2)^2 + (2mn)^2 = (m^2+n^2)^2 \\).")

    # 410: Transpose product
    q("KAUST-P1-410", "Linear Algebra", "Easy",
      "For compatible matrices \\( A \\) and \\( B \\), the transpose of their product \\( (AB)^T \\) is:",
      "لمصفوفتين متوافقتين \\( A \\) و \\( B \\)، منقول حاصل ضربهما \\( (AB)^T \\) يساوي:",
      ["\\( A^T B^T \\)", "\\( B^T A^T \\)", "\\( (BA)^T \\)", "\\( -A^T B^T \\)"], 1,
      "The transpose reverses the order of multiplication: \\( (AB)^T = B^T A^T \\). [Lineage: Matrix Transpose Property]",
      "منقول حاصل الضرب يعكس الترتيب: \\( (AB)^T = B^T A^T \\). [المرجع: خواص المنقول في الجبر الخطي]",
      "The order of factors reverses upon transposition.", "ترتيب العوامل ينعكس عند أخذ المنقول.")

    # 411: Determinant scalar multiple
    q("KAUST-P1-411", "Linear Algebra", "Easy",
      "Let \\( A \\) be a \\( 3 \\times 3 \\) matrix with \\( \\det(A) = 4 \\). What is \\( \\det(2A) \\)?",
      "لتكن \\( A \\) مصفوفة من الرتبة \\( 3 \\times 3 \\) محددها \\( \\det(A) = 4 \\). ما هي قيمة \\( \\det(2A) \\)؟",
      ["\\( 8 \\)", "\\( 16 \\)", "\\( 24 \\)", "\\( 32 \\)"], 3,
      "For an \\( n \\times n \\) matrix, \\( \\det(kA) = k^n \\det(A) \\). For \\( n = 3 \\) and \\( k = 2 \\): \\( \\det(2A) = 2^3 \\det(A) = 8 \\times 4 = 32 \\). [Lineage: Determinant Scaling / AMC 12]",
      "لأي مصفوفة من الرتبة n: \\( \\det(kA) = k^n \\det(A) \\). عند \\( n = 3 \\): \\( 2^3 \\times 4 = 32 \\). [المرجع: خواص المحددات]",
      "Raise the scalar factor to the power of the matrix dimension \\( n = 3 \\).", "ارفع المعامل العددي لأس رتبة المصفوفة.")

    # 412: Zero eigenvalue
    q("KAUST-P1-412", "Linear Algebra", "Easy",
      "A square matrix \\( A \\) has \\( \\det(A) = 0 \\) if and only if \\( A \\) has:",
      "يكون محدد المصفوفة المربعة \\( A \\) مساوياً للصفر إذا وفقط إذا كان للمصفوفة:",
      ["Only negative eigenvalues", "An eigenvalue equal to \\( 0 \\)", "Complex eigenvalues only", "No eigenvectors"], 1,
      "Since the determinant is the product of all eigenvalues, \\( \\det(A) = \\prod \\lambda_i = 0 \\) if and only if at least one eigenvalue is \\( 0 \\). [Lineage: Invertible Matrix Theorem]",
      "بما أن المحدد هو حاصل ضرب القيم الذاتية، فإنه ينعدم إذا وفقط إذا كانت إحدى القيم الذاتية تساوي صفراً. [المرجع: مبرهنة المصفوفات]",
      "Determinant equals the product of eigenvalues.", "المحدد يساوي حاصل ضرب القيم الذاتية.")

    # 413: Similar matrices
    q("KAUST-P1-413", "Linear Algebra", "Easy",
      "If matrices \\( A \\) and \\( B \\) are similar (meaning \\( B = P^{-1}AP \\)), they MUST share the same:",
      "إذا كانت المصفوفتان \\( A \\) و \\( B \\) متشابهتين (أي \\( B = P^{-1}AP \\))، فيجب أن تشتركا في:",
      ["Eigenvectors", "Characteristic polynomial", "Individual entries", "Row space"], 1,
      "Similar matrices represent the same linear transformation in different bases, so they share the same characteristic polynomial, eigenvalues, trace, and determinant. [Lineage: Matrix Similarity / MIT 18.06]",
      "المصفوفات المتشابهة تشترك في كثير الحدود المميز، والقيم الذاتية، والأثر، والمحدد. [المرجع: تشابه المصفوفات]",
      "Similarity preserves the characteristic polynomial.", "التشابه يحفظ كثيرة الحدود المميزة.")

    # 414: Cauchy-Schwarz equality
    q("KAUST-P1-414", "Linear Algebra", "Easy",
      "Under what condition does equality hold in the Cauchy-Schwarz inequality \\( |\\mathbf{u} \\cdot \\mathbf{v}| = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\)?",
      "متى تتحقق المساواة في متراجحة كوشي-شفارز \\( |\\mathbf{u} \\cdot \\mathbf{v}| = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\)؟",
      ["\\( \\mathbf{u} \\) and \\( \\mathbf{v} \\) are orthogonal", "\\( \\mathbf{u} \\) and \\( \\mathbf{v} \\) are linearly dependent (collinear)", "\\( \\|\\mathbf{u}\\| = \\|\\mathbf{v}\\| \\)", "\\( \\mathbf{u} = \\mathbf{0} \\) only"], 1,
      "Equality in Cauchy-Schwarz occurs if and only if the angle between the vectors is \\( 0 \\) or \\( \\pi \\), meaning one vector is a scalar multiple of the other (linearly dependent). [Lineage: Cauchy-Schwarz Equality Condition]",
      "تتحقق المساواة إذا وفقط إذا كان المتجهان على استقامة واحدة (مرتبطين خطياً). [المرجع: متراجحة كوشي-شفارز]",
      "Consider when \\( |\\cos\\theta| = 1 \\).", "تكون القيمة المطلقة لجيب التمام مساوية لـ 1 عند التوازي.")

    # 415: Fundamental Theorem of Algebra
    q("KAUST-P1-415", "Polynomials", "Easy",
      "The Fundamental Theorem of Algebra proves that every non-constant polynomial of degree \\( n \\) over \\( \\mathbb{C} \\) has:",
      "تثبت المبرهنة الأساسية في الجبر أن كل كثيرة حدود غير ثابتة من الدرجة \\( n \\) على \\( \\mathbb{C} \\) تمتلك:",
      ["At least one real root", "Exactly \\( n \\) complex roots (counted with multiplicity)", "At most \\( n - 1 \\) roots", "Only distinct roots"], 1,
      "Gauss and d'Alembert proved that any degree \\( n \\) complex polynomial factors completely into \\( n \\) linear factors over \\( \\mathbb{C} \\). [Lineage: Fundamental Theorem of Algebra]",
      "تنص المبرهنة الأساسية في الجبر على أن لكثيرة الحدود من الدرجة n بالضبط n من الجذور المركبة بحساب التكرار. [المرجع: المبرهنة الأساسية في الجبر]",
      "Recall the fundamental theorem of algebra statement.", "تذكر نص المبرهنة الأساسية في الجبر.")

    # 416: Vieta Quartic
    q("KAUST-P1-416", "Polynomials", "Easy",
      "What is the sum of the roots of the quartic polynomial \\( P(x) = x^4 - 4x^3 + 6x^2 - 4x + 1 \\)?",
      "ما هو مجموع جذور كثيرة الحدود من الدرجة الرابعة \\( P(x) = x^4 - 4x^3 + 6x^2 - 4x + 1 \\)؟",
      ["\\( -4 \\)", "\\( 1 \\)", "\\( 4 \\)", "\\( 6 \\)"], 2,
      "By Vieta's formulas, the sum of roots is \\( -a_{n-1}/a_n = -(-4)/1 = 4 \\) (indeed, \\( P(x) = (x - 1)^4 \\) with four roots of 1). [Lineage: Vieta's Formulas / AMC 12]",
      "حسب علاقات فييتا، مجموع الجذور هو \\( -(-4)/1 = 4 \\). [المرجع: علاقات فييتا]",
      "Use \\( -a_{n-1}/a_n \\).", "طبق قانون مجموع الجذور لفييتا.")

    # 417: Complex conjugate sum
    q("KAUST-P1-417", "Complex Numbers", "Easy",
      "Which property of the complex conjugate operation \\( \\overline{z} \\) is always true?",
      "أي خاصية لمرافق العدد المركب \\( \\overline{z} \\) تكون صحيحة دائماً؟",
      ["\\( \\overline{z_1 + z_2} = \\overline{z_1} + \\overline{z_2} \\)", "\\( \\overline{z_1 + z_2} = \\overline{z_1} - \\overline{z_2} \\)", "\\( \\overline{z} = -z \\)", "\\( |\\overline{z}| = -|z| \\)"], 0,
      "The complex conjugation operator is an automorphism of \\( \\mathbb{C} \\) over \\( \\mathbb{R} \\), preserving addition: \\( \\overline{z_1 + z_2} = \\overline{z_1} + \\overline{z_2} \\). [Lineage: Complex Conjugate Properties]",
      "المرافق المركب يوزع على الجمع: \\( \\overline{z_1 + z_2} = \\overline{z_1} + \\overline{z_2} \\). [المرجع: خواص الأعداد المركبة]",
      "Conjugation distributes over addition.", "المرافق يتوزع على عمليتي الجمع والضرب.")

    # 418: Triangle Inequality
    q("KAUST-P1-418", "Complex Numbers", "Easy",
      "For any complex numbers \\( z_1 \\) and \\( z_2 \\), the Triangle Inequality asserts:",
      "لأي عددين مركبين \\( z_1 \\) و \\( z_2 \\)، تؤكد متباينة المثلث أن:",
      ["\\( |z_1 + z_2| \\le |z_1| + |z_2| \\)", "\\( |z_1 + z_2| \\ge |z_1| + |z_2| \\)", "\\( |z_1 + z_2| = |z_1| + |z_2| \\)", "\\( |z_1 z_2| \\le |z_1| + |z_2| \\)"], 0,
      "The Triangle Inequality states that the straight-line distance \\( |z_1 + z_2| \\) never exceeds the sum of the individual side lengths \\( |z_1| + |z_2| \\). [Lineage: Triangle Inequality in C]",
      "متراجحة المثلث تؤكد أن \\( |z_1 + z_2| \\le |z_1| + |z_2| \\). [المرجع: متباينة المثلث في المستوى المركب]",
      "Recall the geometric interpretation of vector addition.", "تذكر التفسير الهندسي لجمع المتجهات.")

    # 419: Telescoping ln
    q("KAUST-P1-419", "Sequences & Series", "Medium",
      "Evaluate the partial sum \\( \\sum_{n=1}^{99} \\ln\\left(1 + \\dfrac{1}{n}\\right) \\).",
      "احسب قيمة المجموع الجزئي \\( \\sum_{n=1}^{99} \\ln\\left(1 + \\dfrac{1}{n}\\right) \\).",
      ["\\( \\ln(99) \\)", "\\( \\ln(100) \\)", "\\( 2 \\)", "\\( 100 \\)"], 1,
      "Notice \\( \\ln(1 + 1/n) = \\ln\\left(\\dfrac{n+1}{n}\\right) = \\ln(n+1) - \\ln(n) \\). The sum telescopes: \\( (\\ln 2 - \\ln 1) + (\\ln 3 - \\ln 2) + \\dots + (\\ln 100 - \\ln 99) = \\ln(100) - \\ln(1) = \\ln(100) \\). [Lineage: Telescoping Logarithms / AMC 12]",
      "باستخدام \\( \\ln(n+1) - \\ln(n) \\)، تتلاشى الحدود بالتعاقب ليتبقى \\( \\ln(100) - \\ln(1) = \\ln(100) \\). [المرجع: المتسلسلات اللوغاريتمية التلسكوبية]",
      "Rewrite as \\( \\ln(n+1) - \\ln(n) \\).", "أعد كتابة اللوغاريتم كفرق بين لوغاريتمين.")

    # 420: Exponential dominance
    q("KAUST-P1-420", "Calculus & Limits", "Easy",
      "What is the value of the limit \\( \\lim_{n \\to \\infty} \\dfrac{n^{100}}{2^n} \\)?",
      "ما هي قيمة النهاية \\( \\lim_{n \\to \\infty} \\dfrac{n^{100}}{2^n} \\)؟",
      ["\\( 0 \\)", "\\( 1 \\)", "\\( 50 \\)", "\\( \\infty \\)"], 0,
      "Exponential growth dominates any polynomial growth. By repeated application of L'Hôpital's Rule (or ratio test), \\( \\lim_{n \\to \\infty} \\dfrac{n^{100}}{2^n} = 0 \\). [Lineage: Growth Orders / Calculus]",
      "النمو الأسي يتفوق دائماً على أي نمو لكثيرات الحدود، إذن النهاية تساوي صفراً. [المرجع: مراتب نمو الدوال]",
      "Exponential functions grow faster than any power of n.", "الدالة الأسية تنمو أسرع من أي قوة لكثيرات الحدود.")

    # 421: AM-HM Inequality
    q("KAUST-P1-421", "Algebra & Inequalities", "Easy",
      "For positive real numbers \\( a \\) and \\( b \\), which inequality is ALWAYS true?",
      "للأعداد الحقيقية الموجبة \\( a \\) و \\( b \\)، أي متراجحة تكون صحيحة دائماً؟",
      ["\\( \\dfrac{a + b}{2} \\ge \\dfrac{2ab}{a + b} \\)", "\\( \\dfrac{a + b}{2} \\le \\dfrac{2ab}{a + b} \\)", "\\( \\dfrac{a + b}{2} = \\dfrac{2ab}{a + b} \\)", "\\( \\sqrt{ab} \\le \\dfrac{2ab}{a + b} \\)"], 0,
      "The Arithmetic Mean-Harmonic Mean (AM-HM) inequality establishes that \\( \\text{AM} \\ge \\text{GM} \\ge \\text{HM} \\), so \\( \\dfrac{a + b}{2} \\ge \\dfrac{2}{1/a + 1/b} = \\dfrac{2ab}{a + b} \\). [Lineage: AM-GM-HM Inequality Chain]",
      "متراجحة المتوسطين الحسابي والتوافقي: المتوسط الحسابي أكبر من أو يساوي المتوسط التوافقي دائماً. [المرجع: متراجحات المتوسطات]",
      "Recall \\( \\text{AM} \\ge \\text{HM} \\).", "تذكر أن المتوسط الحسابي أكبر من التوافقي.")

    # 422: Conic eccentricity
    q("KAUST-P1-422", "Geometry", "Easy",
      "A conic section with eccentricity \\( e = 1 \\) is classified as:",
      "يُصنف القطع المخروطي الذي يمتلك اختلافاً مركزياً \\( e = 1 \\) على أنه:",
      ["A circle", "An ellipse", "A parabola", "A hyperbola"], 2,
      "By definition of conic sections: \\( e = 0 \\) is a circle, \\( 0 < e < 1 \\) is an ellipse, \\( e = 1 \\) is a parabola, and \\( e > 1 \\) is a hyperbola. [Lineage: Conic Eccentricity Classification]",
      "حسب تعريف القطوع المخروطية: \\( e = 1 \\) يمثل قطعاً مكافئاً دائماً. [المرجع: تصنيف القطوع المخروطية]",
      "Recall eccentricity values for conics.", "تذكر قيم الاختلاف المركزي للقطوع.")

    # 423: Angle between lines
    q("KAUST-P1-423", "Geometry", "Easy",
      "What is the acute angle of intersection between two perpendicular lines with slopes \\( m_1 \\) and \\( m_2 \\) (where \\( m_1 m_2 = -1 \\))?",
      "ما هي الزاوية الحادة بين مستقيمين متعامدين ميلاهما \\( m_1 \\) و \\( m_2 \\) (حيث \\( m_1 m_2 = -1 \\))؟",
      ["\\( 0^\\circ \\)", "\\( 45^\\circ \\)", "\\( 60^\\circ \\)", "\\( 90^\\circ \\)"], 3,
      "Two lines are perpendicular if and only if their angle of intersection is \\( 90^\\circ \\), corresponding to \\( m_1 m_2 = -1 \\). [Lineage: Coordinate Geometry / Perpendicular Lines]",
      "المستقيمان المتعامدان يتقاطعان بزاوية قياسها \\( 90^\\circ \\). [المرجع: الهندسة التحليلية المستوية]",
      "Perpendicular lines form a right angle.", "المستقيمان المتعامدان يصنعان زاوية قائمة.")

    # 424: Tangent to Circle
    q("KAUST-P1-424", "Geometry", "Easy",
      "What is the equation of the tangent line to the circle \\( x^2 + y^2 = 25 \\) at the point \\( (3, 4) \\)?",
      "ما هي معادلة المماس للدائرة \\( x^2 + y^2 = 25 \\) عند النقطة \\( (3, 4) \\)؟",
      ["\\( 3x + 4y = 25 \\)", "\\( 4x + 3y = 25 \\)", "\\( 3x - 4y = 25 \\)", "\\( 4x - 3y = 25 \\)"], 0,
      "The equation of the tangent line to \\( x^2 + y^2 = r^2 \\) at point \\( (x_0, y_0) \\) is \\( x_0 x + y_0 y = r^2 \\). For \\( (3, 4) \\): \\( 3x + 4y = 25 \\). [Lineage: Circle Tangent Equation / High School]",
      "معادلة مماس الدائرة عند النقطة \\( (x_0, y_0) \\) هي \\( x_0 x + y_0 y = r^2 \\). بالتعويض: \\( 3x + 4y = 25 \\). [المرجع: معادلة مماس الدائرة]",
      "Use \\( x_0 x + y_0 y = r^2 \\).", "طبق صيغة معادلة مماس الدائرة.")

    # 425: Independent Expectation
    q("KAUST-P1-425", "Probability", "Easy",
      "If \\( X \\) and \\( Y \\) are independent random variables, what does \\( E[XY] \\) equal?",
      "إذا كان \\( X \\) و \\( Y \\) متغيرين عشوائيين مستقلين، فماذا يساوي \\( E[XY] \\)؟",
      ["\\( E[X] + E[Y] \\)", "\\( E[X] \\cdot E[Y] \\)", "\\( E[X^2] E[Y^2] \\)", "\\( \\text{Var}(X)\\text{Var}(Y) \\)"], 1,
      "For independent random variables, the expectation of the product factors: \\( E[XY] = E[X]E[Y] \\). [Lineage: Independent Random Variables]",
      "للمتغيرات المستقلة، يتوزع التوقع على الضرب: \\( E[XY] = E[X]E[Y] \\). [المرجع: خواص المتغيرات العشوائية المستقلة]",
      "Independence implies multiplicativity of expectation.", "الاستقلال يقتضي ضربية القيمة المتوقعة.")

    # 426: Variance scaling
    q("KAUST-P1-426", "Probability", "Easy",
      "If \\( \\text{Var}(X) = 5 \\), what is \\( \\text{Var}(3X - 7) \\)?",
      "إذا كان تباين المتغير \\( \\text{Var}(X) = 5 \\)، فما هو \\( \\text{Var}(3X - 7) \\)؟",
      ["\\( 8 \\)", "\\( 15 \\)", "\\( 38 \\)", "\\( 45 \\)"], 3,
      "By the variance scaling property: \\( \\text{Var}(aX + b) = a^2 \\text{Var}(X) \\). Here: \\( 3^2 \\times 5 = 9 \\times 5 = 45 \\). [Lineage: Variance Scaling / Statistics]",
      "تباين التحويل الخطي هو \\( \\text{Var}(aX + b) = a^2 \\text{Var}(X) \\). إذن: \\( 3^2 \\times 5 = 45 \\). [المرجع: خواص التباين الإحصائي]",
      "Square the multiplicative coefficient 3.", "ربع المعامل المضروب 3.")

    # 427: Tower Rule
    q("KAUST-P1-427", "Probability", "Medium",
      "The Law of Total Expectation (Tower Property) states that for any integrable random variables \\( X \\) and \\( Y \\):",
      "ينص قانون التوقع الكلي (خاصية البرج) على أنه لأي متغيرين عشوائيين قابلين للتكامل \\( X \\) و \\( Y \\):",
      ["\\( E[E[X \\mid Y]] = E[X] \\)", "\\( E[E[X \\mid Y]] = E[Y] \\)", "\\( E[X \\mid Y] = E[X] \\)", "\\( E[XY] = E[X \\mid Y] \\)"], 0,
      "The Tower Property of conditional expectation states that taking the expectation over \\( Y \\) of the conditional expectation \\( E[X \\mid Y] \\) recovers the unconditional expectation: \\( E[E[X \\mid Y]] = E[X] \\). [Lineage: Tower Property / Measure-Theoretic Probability]",
      "خاصية البرج للتوقع الشرطي: أخذ توقع التوقع الشرطي يعيد التوقع غير الشرطي الأصلي \\( E[E[X \\mid Y]] = E[X] \\). [المرجع: خاصية البرج في نظرية الاحتمالات]",
      "Recall the Law of Total Expectation.", "تذكر قانون التوقع الكلي.")

    # 428: Random walk harmonic
    q("KAUST-P1-428", "Probability", "Medium",
      "In a 1D simple symmetric random walk on integers, the probability of reaching \\( N \\) before \\( 0 \\) satisfies which type of difference equation?",
      "في المشي العشوائي البسيط المتماثل على خط الأعداد الصحيحة، ما نوع معادلة الفروق التي يحققها احتمال الوصول إلى \\( N \\) قبل \\( 0 \\)؟",
      ["Nonlinear Riccati equation", "Harmonic difference equation \\( P(x) = \\dfrac{P(x-1) + P(x+1)}{2} \\)", "First-order logistic equation", "Differential wave equation"], 1,
      "By first-step analysis, \\( P(x) = \\dfrac{1}{2}P(x+1) + \\dfrac{1}{2}P(x-1) \\), meaning \\( P(x) \\) is a discrete harmonic function whose solution is linear: \\( P(x) = x/N \\). [Lineage: Random Walk First-Step Analysis]",
      "بتحليل الخطوة الأولى، الاحتمال يحقق معادلة توافقية متقطعة: \\( P(x) = \\dfrac{P(x-1) + P(x+1)}{2} \\). [المرجع: دوال التوافق والمشي العشوائي]",
      "Express the probability at x as the average of its neighbors.", "عبر عن الاحتمال عند x كمتوسط لجاريه.")

    # 429: Nim-sum state (1, 2, 3)
    q("KAUST-P1-429", "Game Theory", "Easy",
      "Why is the Nim game state with heaps \\( (1, 2, 3) \\) a P-position (previous-player-winning, meaning the player whose turn it is to move will lose under optimal play)?",
      "لماذا تعتبر حالة لعبة نيم بالأكوام \\( (1, 2, 3) \\) وضعية فوز للاعب السابق P-position (أي أن اللاعب الذي عليه الدور سيخسر حتماً باللعب المثالي)؟",
      ["Because \\( 1 + 2 = 3 \\)", "Because the Nim-sum \\( 1 \\oplus 2 \\oplus 3 = 0 \\)", "Because there are 3 heaps", "Because all numbers are distinct"], 1,
      "A Nim state is a P-position (zero-state) if and only if its bitwise XOR sum is \\( 0 \\). In binary: \\( 1 = 01_2, 2 = 10_2, 3 = 11_2 \\). \\( 01_2 \\oplus 10_2 \\oplus 11_2 = 00_2 = 0 \\). [Lineage: Bouton's Theorem / Nim Games]",
      "تكون الوضعية وضعية خسارة للاعب الحالي إذا كان مجموع نيم الثنائي يساوي صفراً: \\( 1 \\oplus 2 \\oplus 3 = 0 \\). [المرجع: نظرية بوتون للعبة نيم]",
      "Compute \\( 1 \\oplus 2 \\oplus 3 \\) in binary.", "احسب مجموع XOR الثنائي للأعداد 1 و 2 و 3.")

    # 430: Lucas' theorem C(7, 2) mod 5
    q("KAUST-P1-430", "Number Theory", "Easy",
      "What is the remainder when \\( \\binom{7}{2} = 21 \\) is divided by \\( 5 \\)?",
      "ما هو باقي قسمة المعامل الثنائي \\( \\binom{7}{2} = 21 \\) على \\( 5 \\)؟",
      ["\\( 0 \\)", "\\( 1 \\)", "\\( 2 \\)", "\\( 4 \\)"], 1,
      "\\( 21 = 4(5) + 1 \\equiv 1 \\pmod 5 \\). Using Lucas' Theorem: \\( 7 = 12_5 \\) and \\( 2 = 02_5 \\), so \\( \\binom{7}{2} \\equiv \\binom{1}{0}\\binom{2}{2} = 1 \\times 1 = 1 \\pmod 5 \\). [Lineage: Lucas' Theorem]",
      "\\( 21 \\equiv 1 \\pmod 5 \\). وبمبرهنة لوكاس: \\( \\binom{1}{0}\\binom{2}{2} = 1 \\). [المرجع: مبرهنة لوكاس]",
      "Divide 21 by 5.", "اقسم 21 على 5 وأوجد الباقي.")

    # 431: Derangements D_4
    q("KAUST-P1-431", "Combinatorics", "Easy",
      "How many derangements of \\( 4 \\) elements exist (\\( D_4 \\))?",
      "كم عدد التباديل اللاتوافقية لـ 4 عناصر (\\( D_4 \\))؟",
      ["\\( 6 \\)", "\\( 8 \\)", "\\( 9 \\)", "\\( 12 \\)"], 2,
      "\\( D_4 = 4! \\left( \\dfrac{1}{2} - \\dfrac{1}{6} + \\dfrac{1}{24} \\right) = 24 \\left( \\dfrac{12 - 4 + 1}{24} \\right) = 9 \\). [Lineage: Derangements Formula / AMC 12]",
      "\\( D_4 = 9 \\). [المرجع: التباديل اللاتوافقية]",
      "Use the formula \\( D_4 = 4!(1/2 - 1/6 + 1/24) \\).", "احسب قيمة \\( D_4 \\).")

    # 432: Vizing's Theorem
    q("KAUST-P1-432", "Graph Theory", "Medium",
      "Vizing's Theorem bounds the chromatic index \\( \\chi'(G) \\) (minimum colors for edge coloring) of a simple graph with maximum degree \\( \\Delta \\) to be either:",
      "تحصر مبرهنة فيزينغ المؤشر اللوني \\( \\chi'(G) \\) (تلوين الحواف) لرسم بياني بسيط ذي درجة قصوى \\( \\Delta \\) في إحدى القيمتين:",
      ["\\( \\Delta - 1 \\) or \\( \\Delta \\)", "\\( \\Delta \\) or \\( \\Delta + 1 \\)", "\\( \\Delta \\) or \\( 2\\Delta \\)", "\\( \\Delta + 1 \\) or \\( \\Delta + 2 \\)"], 1,
      "Vizing's theorem (1964) proves that the edge chromatic number is always either \\( \\Delta \\) (Class 1) or \\( \\Delta + 1 \\) (Class 2). [Lineage: Vizing's Edge Coloring Theorem]",
      "أثبت فيزينغ أن المؤشر اللوني للحواف يساوي دائماً إما \\( \\Delta \\) أو \\( \\Delta + 1 \\). [المرجع: مبرهنة فيزينغ لتلوين الحواف]",
      "Vizing classifies all graphs into Class 1 and Class 2.", "تقسم مبرهنة فيزينغ الرسوم إلى فئتين فقط.")

    # 433: Tree edge count
    q("KAUST-P1-433", "Graph Theory", "Easy",
      "A tree with \\( n \\) vertices has exactly how many edges?",
      "شجرة تحتوي على \\( n \\) من الرؤوس تمتلك كم حافة بالضبط؟",
      ["\\( n - 2 \\)", "\\( n - 1 \\)", "\\( n \\)", "\\( n + 1 \\)"], 1,
      "By definition and induction, every tree on \\( n \\) vertices has exactly \\( n - 1 \\) edges. [Lineage: Graph Theory Fundamentals]",
      "كل شجرة متصلة خالية من الدورات ذات n رأساً تمتلك بالضبط \\( n - 1 \\) حافة. [المرجع: أساسيات نظرية الأشجار]",
      "Recall the fundamental relationship between vertices and edges in trees.", "تذكر العلاقة الأساسية بين رؤوس وحواف الشجرة.")

    # 434: Carmichael Number
    q("KAUST-P1-434", "Number Theory", "Medium",
      "What is the smallest Carmichael number (a composite number \\( n \\) satisfying \\( a^{n-1} \\equiv 1 \\pmod n \\) for all \\( \\gcd(a, n) = 1 \\))?",
      "ما هو أصغر عدد كارمايكل (عدد مركب \\( n \\) يحقق \\( a^{n-1} \\equiv 1 \\pmod n \\) لجميع \\( \\gcd(a, n) = 1 \\))؟",
      ["\\( 341 \\)", "\\( 561 \\)", "\\( 645 \\)", "\\( 1105 \\)"], 1,
      "The smallest Carmichael number is \\( 561 = 3 \\times 11 \\times 17 \\). By Korselt's criterion, \\( p - 1 \\) divides \\( 560 \\) for all three prime factors: \\( 2|560, 10|560, 16|560 \\). [Lineage: Carmichael Numbers / Cryptography]",
      "أصغر عدد كارمايكل هو \\( 561 = 3 \\times 11 \\times 17 \\) ويحقق معيار كورسيلت. [المرجع: أعداد كارمايكل في نظرية الأعداد]",
      "Factor 561 into distinct square-free primes.", "حلل 561 إلى عوامله الأولية.")

    # 435: Modulo 2^100 mod 7
    q("KAUST-P1-435", "Number Theory", "Easy",
      "What is the remainder when \\( 2^{100} \\) is divided by \\( 7 \\)?",
      "ما هو باقي قسمة \\( 2^{100} \\) على \\( 7 \\)؟",
      ["\\( 1 \\)", "\\( 2 \\)", "\\( 4 \\)", "\\( 6 \\)"], 1,
      "Notice \\( 2^3 = 8 \\equiv 1 \\pmod 7 \\). Then \\( 2^{100} = 2^{3(33) + 1} = (2^3)^{33} \\times 2 \\equiv 1^{33} \\times 2 = 2 \\pmod 7 \\). [Lineage: Modular Arithmetic / AMC 12]",
      "بما أن \\( 2^3 \\equiv 1 \\pmod 7 \\)، فإن \\( 2^{100} = (2^3)^{33} \\times 2 \\equiv 2 \\pmod 7 \\). [المرجع: الحساب المقياسي]",
      "Use \\( 2^3 = 8 \\equiv 1 \\pmod 7 \\).", "استخدم أن مكعب 2 يكافئ 1 مقياس 7.")

    # 436: Symmetric Matrix Eigenvalues
    q("KAUST-P1-436", "Linear Algebra", "Easy",
      "If \\( A \\) is a real symmetric matrix, what can be concluded about its eigenvalues?",
      "إذا كانت \\( A \\) مصفوفة حقيقية متماثلة، فماذا يمكن استنتاجه بشأن قيمها الذاتية؟",
      ["They must all be strictly positive.", "They are all real numbers.", "They must all be rational.", "They are all distinct."], 1,
      "A cornerstone theorem of linear algebra states that all eigenvalues of any real symmetric matrix are guaranteed to be real numbers. [Lineage: Spectral Theorem / MIT 18.06]",
      "حسب المبرهنة الطيفية، جميع القيم الذاتية لأي مصفوفة حقيقية متماثلة هي أعداد حقيقية. [المرجع: الجبر الخطي في MIT]",
      "Recall the Spectral Theorem for real symmetric matrices.", "تذكر مبرهنة التحليل الطيفي.")

    # 437: Projection Matrix
    q("KAUST-P1-437", "Linear Algebra", "Easy",
      "An orthogonal projection matrix \\( P \\) onto a subspace must satisfy which pair of conditions?",
      "مصفوفة الإسقاط المتعامد \\( P \\) على فضاء جزئي يجب أن تحقق أي زوج من الشروط؟",
      ["\\( P^2 = P \\) and \\( P^T = P \\)", "\\( P^2 = I \\) and \\( P^T = -P \\)", "\\( P^2 = -P \\) and \\( \\det(P) = 1 \\)", "\\( P^T P = -I \\)"], 0,
      "An orthogonal projector is both idempotent (\\( P^2 = P \\)) and self-adjoint / symmetric (\\( P^T = P \\)). [Lineage: Orthogonal Projection / MIT 18.06]",
      "مصفوفة الإسقاط المتعامد تكون ارتدادية ومتماثلة: \\( P^2 = P \\) و \\( P^T = P \\). [المرجع: الإسقاط المتعامد في الجبر الخطي]",
      "It must be idempotent and symmetric.", "يجب أن تكون متماثلة ومحققة لخاصية الإسقاط.")

    # 438: Polynomial remainder x^100 mod (x^2 - 1)
    q("KAUST-P1-438", "Polynomials", "Easy",
      "What is the remainder when \\( x^{100} \\) is divided by \\( x^2 - 1 \\)?",
      "ما هو باقي قسمة \\( x^{100} \\) على \\( x^2 - 1 \\)؟",
      ["\\( 0 \\)", "\\( 1 \\)", "\\( x \\)", "\\( x - 1 \\)"], 1,
      "Since \\( x^2 \\equiv 1 \\pmod{x^2 - 1} \\), we have \\( x^{100} = (x^2)^{50} \\equiv 1^{50} = 1 \\pmod{x^2 - 1} \\). [Lineage: Polynomial Congruences / AMC 12]",
      "بما أن \\( x^2 \\equiv 1 \\pmod{x^2 - 1} \\)، فإن \\( x^{100} = (x^2)^{50} \\equiv 1 \\). الباقي هو 1. [المرجع: قسمة كثيرات الحدود]",
      "Replace \\( x^2 \\) with 1.", "عوض عن \\( x^2 \\) بالعدد 1.")

    # 439: Division Algorithm Degree
    q("KAUST-P1-439", "Polynomials", "Easy",
      "When a polynomial \\( P(x) \\) is divided by a non-zero divisor \\( D(x) \\), what is the constraint on the remainder \\( R(x) \\)?",
      "عند قسمة كثيرة حدود \\( P(x) \\) على قاسم غير صفري \\( D(x) \\)، ما هو القيد على الباقي \\( R(x) \\)؟",
      ["\\( \\deg(R) = \\deg(D) \\)", "\\( \\deg(R) < \\deg(D) \\) (or \\( R(x) = 0 \\))", "\\( \\deg(R) > \\deg(D) \\)", "\\( \\deg(R) \\le 1 \\) always"], 1,
      "By the Polynomial Division Algorithm, the remainder \\( R(x) \\) is either the zero polynomial or satisfies \\( \\deg(R) < \\deg(D) \\). [Lineage: Polynomial Division Algorithm]",
      "خوارزمية قسمة كثيرات الحدود تقتضي أن تكون درجة الباقي أقل تماماً من درجة القاسم. [المرجع: خوارزمية القسمة الإقليدية لكثيرات الحدود]",
      "The remainder must have strictly smaller degree than the divisor.", "درجة الباقي دائماً أصغر من درجة المقسوم عليه.")

    # 440: Geometric series expansion
    q("KAUST-P1-440", "Sequences & Series", "Easy",
      "For \\( |x| < 1 \\), what is the power series expansion of \\( \\dfrac{1}{1 - x} \\)?",
      "عندما \\( |x| < 1 \\)، ما هو مفكوك متسلسلة القوى للمقدار \\( \\dfrac{1}{1 - x} \\)؟",
      ["\\( \\sum_{n=0}^{\\infty} x^n \\)", "\\( \\sum_{n=1}^{\\infty} \\dfrac{x^n}{n} \\)", "\\( \\sum_{n=0}^{\\infty} (-1)^n x^n \\)", "\\( \\sum_{n=0}^{\\infty} \\dfrac{x^n}{n!} \\)"], 0,
      "The standard geometric series expansion is \\( \\dfrac{1}{1 - x} = 1 + x + x^2 + x^3 + \\dots = \\sum_{n=0}^{\\infty} x^n \\) for \\( |x| < 1 \\). [Lineage: Geometric Series]",
      "مفكوك المتسلسلة الهندسية القياسية هو \\( \\sum_{n=0}^{\\infty} x^n \\). [المرجع: المتسلسلات الهندسية]",
      "Recall the standard geometric series.", "تذكر مفكوك المتسلسلة الهندسية الأساسي.")

    # 441: Cesaro Mean
    q("KAUST-P1-441", "Sequences & Series", "Medium",
      "If a sequence of real numbers converges to \\( L \\) (\\( \\lim_{n \\to \\infty} a_n = L \\)), what is the limit of its Cesàro means \\( \\lim_{n \\to \\infty} \\dfrac{a_1 + a_2 + \\dots + a_n}{n} \\)?",
      "إذا تقاربت متتالية من الأعداد الحقيقية إلى \\( L \\)، فما هي نهاية أوساطها الحسابية (أوساط سيزاور) \\( \\lim_{n \\to \\infty} \\dfrac{a_1 + a_2 + \\dots + a_n}{n} \\)؟",
      ["\\( 0 \\)", "\\( L/2 \\)", "\\( L \\)", "\\( 2L \\)"], 2,
      "By the Stolz-Cesàro theorem (Cesàro mean theorem), if a sequence converges to \\( L \\), the sequence of its arithmetic averages also converges to the same limit \\( L \\). [Lineage: Stolz-Cesàro Theorem]",
      "حسب مبرهنة سيزاور، إذا تقاربت متتالية إلى L فإن متوسطاتها الحسابية تتقارب إلى نفس النهاية L. [المرجع: مبرهنة سيزاور للأوساط الحسابية]",
      "Recall the Cesàro summation theorem for convergent sequences.", "تذكر مبرهنة سيزاور للمتتاليات المتقاربة.")

    # 442: Ellipse Area
    q("KAUST-P1-442", "Geometry", "Easy",
      "What is the exact area enclosed by the ellipse \\( \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1 \\)?",
      "ما هي المساحة الدقيقة المحصورة داخل القطع الناقص \\( \\dfrac{x^2}{25} + \\dfrac{y^2}{9} = 1 \\)؟",
      ["\\( 15 \\)", "\\( 15\\pi \\)", "\\( 30\\pi \\)", "\\( 34\\pi \\)"], 1,
      "The area of an ellipse with semi-axes \\( a \\) and \\( b \\) is \\( \\pi a b \\). Here \\( a = 5 \\) and \\( b = 3 \\), so \\( \\text{Area} = \\pi (5)(3) = 15\\pi \\). [Lineage: Area of Ellipse / High School]",
      "مساحة القطع الناقص هي \\( \\pi a b \\). بالتعويض: \\( \\pi \\times 5 \\times 3 = 15\\pi \\). [المرجع: مساحة القطع الناقص]",
      "Use the formula \\( \\text{Area} = \\pi a b \\).", "طبق قانون مساحة القطع الناقص.")

    # 443: Parabola Reflection
    q("KAUST-P1-443", "Geometry", "Easy",
      "According to the reflective property of a parabola, light rays emitted from the focus will reflect off the parabolic mirror:",
      "وفقاً للخاصية الانعكاسية للقطع المكافئ، فإن الأشعة الضوئية المنبعثة من البؤرة تنعكس عن المرآة المكافئة:",
      ["Back toward the focus", "Parallel to the axis of symmetry", "Perpendicular to the directrix only at the vertex", "In random directions"], 1,
      "By the parabolic reflection property, any ray originating from the focus reflects parallel to the parabola's axis of symmetry (and vice versa). [Lineage: Parabola Optical Property]",
      "الخاصية البصرية للقطع المكافئ تضمن أن الأشعة المنبعثة من البؤرة تنعكس موازية لمحور التماثل. [المرجع: الخواص البصرية للقطع المكافئ]",
      "Think about parabolic satellite dishes and headlights.", "فكر في عمل هوائيات الأقمار الصناعية وكشافات الإضاءة.")

    # 444: Cyclic Quad Angles
    q("KAUST-P1-444", "Geometry", "Easy",
      "In any cyclic quadrilateral \\( ABCD \\) inscribed in a circle, the sum of opposite angles \\( \\angle A + \\angle C \\) is:",
      "في أي رباعي دائري \\( ABCD \\) مرسوم داخل دائرة، مجموع قياسي الزاويتين المتقابلتين \\( \\angle A + \\angle C \\) يساوي:",
      ["\\( 90^\\circ \\)", "\\( 180^\\circ \\)", "\\( 270^\\circ \\)", "\\( 360^\\circ \\)"], 1,
      "The opposite angles of a cyclic quadrilateral subtend complementary arcs that together form the entire \\( 360^\\circ \\) circle, so their inscribed angle sum is \\( \\dfrac{360^\\circ}{2} = 180^\\circ \\). [Lineage: Cyclic Quadrilateral Inscribed Angles / High School]",
      "الزاويتان المتقابلتان تقابلان قوسين يكملان الدائرة، إذن مجموع قياسهما يساوي \\( 180^\\circ \\). [المرجع: خواص الرباعي الدائري]",
      "Inscribed angles intercept half the opposite arcs.", "الزاويتان المتقابلتان في الرباعي الدائري متكاملتان.")

    # 445: Coin toss at least one head
    q("KAUST-P1-445", "Probability", "Easy",
      "A fair coin is flipped \\( 4 \\) times. What is the probability of obtaining AT LEAST one head?",
      "أُلقيت عملة نقدية عادلة 4 مرات. ما احتمال الحصول على وجه (صورة) واحد على الأقل؟",
      ["\\( \\dfrac{1}{16} \\)", "\\( \\dfrac{7}{8} \\)", "\\( \\dfrac{15}{16} \\)", "\\( 1 \\)"], 2,
      "Complementary probability: the only outcome with no heads is all tails (TTTT), which has probability \\( (1/2)^4 = 1/16 \\). Thus, \\( P(\\ge 1 \\text{ head}) = 1 - 1/16 = 15/16 \\). [Lineage: Complement Rule / Probability Foundations]",
      "باستخدام الحدث المتمم: احتمال عدم ظهور أي صورة (كتابة في الرميات الأربع) هو \\( 1/16 \\)، إذن الاحتمال المطلوب هو \\( 1 - 1/16 = 15/16 \\). [المرجع: قاعدة الحدث المتمم]",
      "Subtract the probability of all tails from 1.", "اطرح احتمال ظهور الكتابة دائماً من 1.")

    # 446: Poisson Sum
    q("KAUST-P1-446", "Probability", "Easy",
      "If independent random variables \\( X \\sim \\text{Poisson}(\\lambda_1) \\) and \\( Y \\sim \\text{Poisson}(\\lambda_2) \\), what is the distribution of \\( X + Y \\)?",
      "إذا كان المتغيران العشوائيان المستقلان \\( X \\sim \\text{Poisson}(\\lambda_1) \\) و \\( Y \\sim \\text{Poisson}(\\lambda_2) \\)، فما هو توزيع المجموع \\( X + Y \\)؟",
      ["\\( \\text{Poisson}(\\lambda_1 + \\lambda_2) \\)", "\\( \\text{Poisson}(\\lambda_1 \\lambda_2) \\)", "\\( \\text{Binomial}(\\lambda_1 + \\lambda_2) \\)", "\\( \\text{Normal}(\\lambda_1, \\lambda_2) \\)"], 0,
      "The Poisson distribution is reproductive under convolution of independent variables: \\( X + Y \\sim \\text{Poisson}(\\lambda_1 + \\lambda_2) \\). [Lineage: Poisson Additivity Property]",
      "خاصية انغلاق توزيع بواسون تضمن أن مجموع متغيري بواسون مستقلين هو متغير بواسون بمعلمة \\( \\lambda_1 + \\lambda_2 \\). [المرجع: جمع متغيرات بواسون]",
      "Sum the rate parameters.", "اجمع معلمتي المعدل.")

    # 447: Memoryless Property
    q("KAUST-P1-447", "Probability", "Easy",
      "The memoryless property \\( P(X > s + t \\mid X > s) = P(X > t) \\) uniquely characterizes which continuous probability distribution?",
      "خاصية فقدان الذاكرة \\( P(X > s + t \\mid X > s) = P(X > t) \\) تميز بشكل فريد أي توزيع احتمالي متصل؟",
      ["Normal distribution", "Exponential distribution", "Uniform distribution", "Cauchy distribution"], 1,
      "Among all continuous probability distributions with support on \\( [0, \\infty) \\), the Exponential distribution is the unique distribution possessing the memoryless property. [Lineage: Exponential Distribution Memoryless Property]",
      "التوزيع الأسي هو التوزيع الاحتمالي المتصل الوحيد الذي يمتلك خاصية انعدام الذاكرة. [المرجع: التوزيع الأسي وفقدان الذاكرة]",
      "Recall the continuous analog of the geometric distribution.", "تذكر النظير المتصل للتوزيع الهندسي.")

    # 448: Expected tosses until HH
    q("KAUST-P1-448", "Probability", "Hard",
      "A fair coin is tossed repeatedly. What is the expected number of tosses until two consecutive Heads (\\( HH \\)) appear?",
      "تُلقى عملة نقدية عادلة بشكل متكرر. ما هي القيمة المتوقعة لعدد الرميات حتى ظهور وجهين متتاليين (\\( HH \\))؟",
      ["\\( 4 \\)", "\\( 6 \\)", "\\( 8 \\)", "\\( 10 \\)"], 1,
      "Let \\( E \\) be expected tosses from start. \\( E = 1 + \\dfrac{1}{2} E + \\dfrac{1}{2} E_H \\), where \\( E_H \\) is expected tosses given the last toss was \\( H \\). \\( E_H = 1 + \\dfrac{1}{2}(0) + \\dfrac{1}{2} E \\). Substituting: \\( E_H = 1 + \\dfrac{1}{2}E \\implies E = 1 + \\dfrac{1}{2}E + \\dfrac{1}{2}(1 + \\dfrac{1}{2}E) = \\dfrac{3}{2} + \\dfrac{3}{4}E \\implies \\dfrac{1}{4}E = \\dfrac{3}{2} \\implies E = 6 \\). [Lineage: Markov Stopping Times / HMMT]",
      "بتحليل الخطوة الأولى: توقع ظهور HH لعملة عادلة هو 6 رميات. [المرجع: سلاسل ماركوف وأزمنة التوقف في مسابقة HMMT]",
      "Set up first-step equations for states Start and H.", "اكتب معادلات الخطوة الأولى للحالتين البداية و H.")

    # 449: Standard deviation definition
    q("KAUST-P1-449", "Probability", "Easy",
      "The standard deviation \\( \\sigma \\) of a random variable is mathematically defined as:",
      "الانحراف المعياري \\( \\sigma \\) لمتغير عشوائي يُعرّف رياضياً بأنه:",
      ["\\( (\\text{Var}(X))^2 \\)", "\\( \\sqrt{\\text{Var}(X)} \\)", "\\( E[X^2] \\)", "\\( \\dfrac{\\text{Var}(X)}{E[X]} \\)"], 1,
      "Standard deviation is the non-negative square root of the variance: \\( \\sigma = \\sqrt{\\text{Var}(X)} \\). [Lineage: Standard Deviation Definition]",
      "الانحراف المعياري هو الجذر التربيعي الموجب للتباين: \\( \\sigma = \\sqrt{\\text{Var}(X)} \\). [المرجع: تعريف الانحراف المعياري]",
      "Take the square root of the variance.", "خذ الجذر التربيعي للتباين.")

    # 450: Weak Law of Large Numbers
    q("KAUST-P1-450", "Probability", "Medium",
      "The Weak Law of Large Numbers (WLLN) states that as sample size \\( n \\to \\infty \\), the sample mean \\( \\bar{X}_n \\) of i.i.d. random variables with mean \\( \\mu \\):",
      "ينص القانون الضعيف للأعداد الكبيرة على أنه عندما \\( n \\to \\infty \\)، فإن المتوسط الحسابي للعينة \\( \\bar{X}_n \\) لمتغيرات مستقلة ومتطابقة التوزيع ذات متوسط \\( \\mu \\):",
      ["Converges in probability to \\( \\mu \\)", "Converges to 0", "Becomes normally distributed with variance 1", "Increases without bound"], 0,
      "Khinchin's Weak Law of Large Numbers asserts convergence in probability: for any \\( \\epsilon > 0 \\), \\( \\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\epsilon) = 1 \\). [Lineage: Law of Large Numbers / Probability Theory]",
      "ينص قانون الأعداد الكبيرة الضعيف على التقارب في الاحتمال إلى المتوسط الحقيقي للمجتمع \\( \\mu \\). [المرجع: قانون الأعداد الكبيرة]",
      "Recall the mode of convergence in the Weak Law of Large Numbers.", "تذكر نوع التقارب في القانون الضعيف للأعداد الكبيرة.")

    return questions

if __name__ == "__main__":
    qs = get_part_d()
    print(f"Generated {len(qs)} Part D questions (401-450).")
