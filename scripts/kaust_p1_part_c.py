#!/usr/bin/env python3
"""
KAUST Phase 1 Questions Part C: 351 to 400
Probability, Statistics, Graph Theory, Number Theory, Linear Algebra, Geometry.
"""

def get_part_c():
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

    # 351: Variance of fair die
    q("KAUST-P1-351", "Probability", "Easy",
      "What is the exact variance \\( \\text{Var}(X) \\) of a single roll of a fair six-sided die?",
      "ما هو التباين الدقيق \\( \\text{Var}(X) \\) لرمية واحدة لنرد عادل ذي ستة أوجه؟",
      ["\\( \\dfrac{35}{12} \\)", "\\( \\dfrac{17}{6} \\)", "\\( 3 \\)", "\\( \\dfrac{35}{6} \\)"], 0,
      "\\( E[X] = \\dfrac{7}{2} \\). \\( E[X^2] = \\dfrac{1^2 + 2^2 + \\dots + 6^2}{6} = \\dfrac{91}{6} \\). \\( \\text{Var}(X) = E[X^2] - (E[X])^2 = \\dfrac{91}{6} - \\dfrac{49}{4} = \\dfrac{182 - 147}{12} = \\dfrac{35}{12} \\). [Lineage: Probability Foundations]",
      "التوقع هو 7/2، وتوقع المربع هو 91/6. التباين: \\( \\dfrac{91}{6} - \\dfrac{49}{4} = \\dfrac{35}{12} \\). [المرجع: أساسيات الاحتمالات]",
      "Use \\( \\text{Var}(X) = E[X^2] - (E[X])^2 \\) or \\( (n^2 - 1)/12 \\).", "استخدم قانون التباين أو صيغة التوزيع المنتظم المتقطع.")

    # 352: Binomial Variance
    q("KAUST-P1-352", "Probability", "Easy",
      "For a binomial random variable \\( X \\sim \\text{Binomial}(n = 20, p = 0.4) \\), what is the variance \\( \\text{Var}(X) \\)?",
      "لمتغير عشوائي ذي حدين \\( X \\sim \\text{Binomial}(n = 20, p = 0.4) \\)، ما هو التباين \\( \\text{Var}(X) \\)؟",
      ["\\( 4.8 \\)", "\\( 6.0 \\)", "\\( 8.0 \\)", "\\( 12.0 \\)"], 0,
      "For a binomial distribution: \\( \\text{Var}(X) = np(1 - p) = 20(0.4)(0.6) = 4.8 \\). [Lineage: Binomial Distribution / AMC 12]",
      "تباين توزيع ذي الحدين هو \\( np(1-p) = 20 \\times 0.4 \\times 0.6 = 4.8 \\). [المرجع: توزيع ذي الحدين]",
      "Compute \\( np(1 - p) \\).", "احسب حاصل ضرب \\( np(1-p) \\).")

    # 353: Poisson P(X = 0)
    q("KAUST-P1-353", "Probability", "Easy",
      "A Poisson process has an average rate of \\( \\lambda = 3 \\) events per hour. What is the exact probability that NO events occur in a given hour?",
      "عملية بواسون يبلغ معدلها المتوسط \\( \\lambda = 3 \\) أحداث في الساعة. ما هو الاحتمال الدقيق لعدم وقوع أي حدث في ساعة معينة؟",
      ["\\( e^{-3} \\)", "\\( 3e^{-3} \\)", "\\( 1 - e^{-3} \\)", "\\( e^{-1} \\)"], 0,
      "For \\( X \\sim \\text{Poisson}(\\lambda) \\), \\( P(X = k) = \\dfrac{\\lambda^k e^{-\\lambda}}{k!} \\). Setting \\( k = 0 \\) and \\( \\lambda = 3 \\): \\( P(X = 0) = \\dfrac{3^0 e^{-3}}{0!} = e^{-3} \\). [Lineage: Poisson Process]",
      "في توزيع بواسون: \\( P(X = 0) = \\dfrac{\\lambda^0 e^{-\\lambda}}{0!} = e^{-3} \\). [المرجع: توزيع بواسون]",
      "Evaluate \\( P(X = 0) = e^{-\\lambda} \\).", "عوض بـ \\( k = 0 \\) في صيغة بواسون.")

    # 354: Hypergeometric
    q("KAUST-P1-354", "Probability", "Easy",
      "An urn contains \\( 4 \\) red and \\( 6 \\) blue marbles. If \\( 2 \\) marbles are drawn uniformly at random without replacement, what is the probability that both are red?",
      "يحتوي صندوق على \\( 4 \\) كرات حمراء و \\( 6 \\) كرات زرقاء. إذا سُحبت كرتان عشوائياً بدون إرجاع، فما احتمال أن تكون الكرتان حمراوين؟",
      ["\\( \\dfrac{2}{15} \\)", "\\( \\dfrac{4}{25} \\)", "\\( \\dfrac{1}{5} \\)", "\\( \\dfrac{6}{25} \\)"], 0,
      "\\( P = \\dfrac{\\binom{4}{2}}{\\binom{10}{2}} = \\dfrac{6}{45} = \\dfrac{2}{15} \\). [Lineage: Hypergeometric Distribution / AMC 12]",
      "الاحتمال هو \\( \\dfrac{\\binom{4}{2}}{\\binom{10}{2}} = \\dfrac{6}{45} = \\dfrac{2}{15} \\). [المرجع: التوزيع فوق الهندسي]",
      "Divide favorable pairs by total pairs.", "اقسم عدد الأزواج الحمراء على إجمالي الأزواج الممكنة.")

    # 355: Covariance formula
    q("KAUST-P1-355", "Probability", "Easy",
      "Which formula correctly defines the covariance \\( \\text{Cov}(X, Y) \\) between two random variables?",
      "أي صيغة تعرّف بشكل صحيح التغاير \\( \\text{Cov}(X, Y) \\) بين متغيرين عشوائيين؟",
      ["\\( E[XY] - E[X]E[Y] \\)", "\\( E[X^2] - E[Y^2] \\)", "\\( E[X + Y] - E[X]E[Y] \\)", "\\( \\text{Var}(X) + \\text{Var}(Y) \\)"], 0,
      "By definition: \\( \\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y] \\). [Lineage: Covariance Definition]",
      "تعريف التغاير الرياضي: \\( \\text{Cov}(X, Y) = E[XY] - E[X]E[Y] \\). [المرجع: مبادئ الإحصاء الرياضي]",
      "Recall the algebraic expansion of \\( E[(X - \\mu_X)(Y - \\mu_Y)] \\).", "فك القيمة المتوقعة لحاصل ضرب الانحرافات.")

    # 356: Independence
    q("KAUST-P1-356", "Probability", "Easy",
      "Two events \\( A \\) and \\( B \\) are independent if and only if:",
      "يكون الحدثان \\( A \\) و \\( B \\) مستقلين إذا وفقط إذا كان:",
      ["\\( P(A \\cap B) = P(A) + P(B) \\)", "\\( P(A \\cap B) = P(A) P(B) \\)", "\\( P(A \\cup B) = P(A) P(B) \\)", "\\( P(A \\mid B) = 0 \\)"], 1,
      "Two events are statistically independent if and only if the probability of their intersection equals the product of their individual probabilities: \\( P(A \\cap B) = P(A)P(B) \\). [Lineage: Probability Axioms]",
      "الاستقلال الإحصائي للحدثين يتحقق إذا وفقط إذا كان احتمال التقاطع يساوي حاصل ضرب الاحتمالين. [المرجع: بديهيات الاحتمالات]",
      "Recall the multiplicative rule for independent events.", "تذكر شرط الضرب لاستقلال الأحداث.")

    # 357: Chebyshev's Inequality
    q("KAUST-P1-357", "Probability", "Medium",
      "According to Chebyshev's Inequality, what is the maximum possible probability that a random variable \\( X \\) deviates from its mean \\( \\mu \\) by at least \\( 2 \\) standard deviations \\( (\\ge 2\\sigma) \\)?",
      "وفقاً لمتراجحة تشيبيشيف، ما هو الحد الأقصى لاحتمال أن ينحرف متغير عشوائي \\( X \\) عن متوسطه \\( \\mu \\) بمقدار انحرافين معياريين على الأقل \\( (\\ge 2\\sigma) \\)؟",
      ["\\( 0.05 \\)", "\\( 0.10 \\)", "\\( 0.25 \\)", "\\( 0.50 \\)"], 2,
      "Chebyshev's inequality states \\( P(|X - \\mu| \\ge k\\sigma) \\le \\dfrac{1}{k^2} \\). For \\( k = 2 \\): \\( \\dfrac{1}{2^2} = \\dfrac{1}{4} = 0.25 \\). [Lineage: Chebyshev's Inequality / Probability]",
      "تنص متراجحة تشيبيشيف على أن \\( P(|X - \\mu| \\ge k\\sigma) \\le \\dfrac{1}{k^2} \\). عند \\( k = 2 \\): الاحتمال لا يتجاوز \\( 1/4 = 0.25 \\). [المرجع: متراجحة تشيبيشيف]",
      "Apply \\( 1/k^2 \\) with \\( k = 2 \\).", "عوض بـ \\( k = 2 \\) في \\( 1/k^2 \\).")

    # 358: Monty Hall
    q("KAUST-P1-358", "Probability", "Easy",
      "In the classic Monty Hall problem with \\( 3 \\) doors, what is the contestant's probability of winning the prize if they always switch doors after the host reveals a goat?",
      "في معضلة مونتي هول الكلاسيكية ذات الأبواب الثلاثة، ما هو احتمال فوز المتسابق بالجائزة إذا قام دائماً بتبديل بابه بعد أن يكشف المضيف ماعزاً؟",
      ["\\( \\dfrac{1}{3} \\)", "\\( \\dfrac{1}{2} \\)", "\\( \\dfrac{2}{3} \\)", "\\( \\dfrac{3}{4} \\)"], 2,
      "The initial choice has a \\( 1/3 \\) chance of being the car and a \\( 2/3 \\) chance of being a goat. When switching, the contestant wins if and only if their initial pick was a goat. Thus, switching wins with probability \\( 2/3 \\). [Lineage: Monty Hall Problem]",
      "احتمال اختيار الماعز في البداية هو 2/3، وعند التبديل يفوز المتسابق دائماً إذا كان اختياره الأول ماعزاً، إذن احتمال الفوز بالتبديل هو 2/3. [المرجع: معضلة مونتي هول الشهيرة]",
      "Switching wins whenever the initial guess was wrong.", "التبديل يضمن الفوز في كل مرة كان فيها الاختيار المبدئي خاطئاً.")

    # 359: Birthday Problem
    q("KAUST-P1-359", "Probability", "Easy",
      "What is the minimum number of people in a room required so that the probability of at least two sharing the same birthday exceeds \\( 50\\% \\) (assuming 365 days)?",
      "ما هو أقل عدد من الأشخاص في غرفة بحيث يتجاوز احتمال اشتراك شخصين على الأقل في يوم الميلاد نفسه نسبة 50%؟",
      ["\\( 23 \\)", "\\( 50 \\)", "\\( 183 \\)", "\\( 365 \\)"], 0,
      "The complementary probability of all distinct birthdays drops below \\( 0.50 \\) at \\( n = 23 \\): \\( P(\\text{match}) = 1 - \\dfrac{365 \\times 364 \\times \\dots \\times 343}{365^{23}} \\approx 0.507 \\). [Lineage: Birthday Paradox / AMC 12]",
      "يهبط احتمال اختلاف جميع أعياد الميلاد إلى أقل من 0.5 عند \\( n = 23 \\)، مما يجعل احتمال التطابق يتجاوز 50%. [المرجع: مفارقة أعياد الميلاد]",
      "Recall the famous Birthday Paradox threshold.", "تذكر عتبة مفارقة أعياد الميلاد الشهيرة.")

    # 360: Expected min uniform
    q("KAUST-P1-360", "Probability", "Medium",
      "Let \\( X, Y \\sim \\text{Uniform}(0, 1) \\) be independent. What is the expected value \\( E[\\min(X, Y)] \\)?",
      "ليكن \\( X, Y \\sim \\text{Uniform}(0, 1) \\) متغيرين عشوائيين مستقلين يتبعان التوزيع المنتظم. ما هي القيمة المتوقعة لـ \\( E[\\min(X, Y)] \\)؟",
      ["\\( \\dfrac{1}{4} \\)", "\\( \\dfrac{1}{3} \\)", "\\( \\dfrac{1}{2} \\)", "\\( \\dfrac{2}{3} \\)"], 1,
      "For independent uniform variables, \\( n \\) points divide \\( [0, 1] \\) into \\( n + 1 \\) equal expected intervals of length \\( \\dfrac{1}{n+1} \\). For \\( n = 2 \\), \\( E[\\min(X, Y)] = \\dfrac{1}{2+1} = \\dfrac{1}{3} \\). Alternatively: \\( P(\\min > t) = (1-t)^2 \\), so \\( E = \\int_0^1 (1-t)^2 dt = \\left[ -\\dfrac{(1-t)^3}{3} \\right]_0^1 = \\dfrac{1}{3} \\). [Lineage: Order Statistics / SMT]",
      "نقطتان عشوائيتان تقسمان الفترة [0, 1] إلى 3 فترات متساوية التوقع، إذن توقع الأصغر هو \\( 1/3 \\). [المرجع: إحصاءات الرتب والتوزيع المنتظم]",
      "Integrate the tail probability \\( \\int_0^1 P(\\min > t) dt \\).", "كامل دالة البقاء من 0 إلى 1.")

    # 361: Permutation Sign
    q("KAUST-P1-361", "Abstract Algebra", "Medium",
      "In the symmetric group \\( S_5 \\), what is the sign (parity) of the permutation \\( \\sigma = (1 \\, 2 \\, 3)(4 \\, 5) \\)?",
      "في زمرة التماثل \\( S_5 \\)، ما هي إشارة (زوجية) التبديلة \\( \\sigma = (1 \\, 2 \\, 3)(4 \\, 5) \\)؟",
      ["\\( \\text{sgn}(\\sigma) = +1 \\) (even)", "\\( \\text{sgn}(\\sigma) = -1 \\) (odd)", "\\( 0 \\)", "Undefined"], 1,
      "A \\( k \\)-cycle has parity \\( (-1)^{k-1} \\). The 3-cycle \\( (1 \\, 2 \\, 3) \\) is even (\\( (-1)^2 = +1 \\)), and the 2-cycle (transposition) \\( (4 \\, 5) \\) is odd (\\( (-1)^1 = -1 \\)). The product has sign \\( (+1)(-1) = -1 \\) (odd permutation). [Lineage: Permutation Parity / Abstract Algebra]",
      "الدورة ذات الطول 3 زوجية، والتبديلة البسيطة (4 5) فردية. حاصل ضربهما يعطي تبديلة فردية ذات إشارة \\( -1 \\). [المرجع: زوجية التباديل في الجبر المجرد]",
      "Multiply the signs of the disjoint cycles.", "اضرب إشارات الدورات المنفصلة.")

    # 362: Partition Generating Function
    q("KAUST-P1-362", "Combinatorics", "Medium",
      "Which infinite product is Euler's generating function for the integer partition function \\( p(n) \\)?",
      "أي جداء لانهائي يمثل دالة أويلر المولدة لتجزئات الأعداد الصحيحة \\( p(n) \\)؟",
      ["\\( \\prod_{k=1}^{\\infty} (1 - x^k) \\)", "\\( \\prod_{k=1}^{\\infty} \\dfrac{1}{1 - x^k} \\)", "\\( \\sum_{k=1}^{\\infty} \\dfrac{x^k}{k!} \\)", "\\( \\prod_{k=1}^{\\infty} (1 + x^k) \\)"], 1,
      "Euler proved that \\( \\sum_{n=0}^{\\infty} p(n) x^n = \\prod_{k=1}^{\\infty} \\dfrac{1}{1 - x^k} \\). [Lineage: Euler Partition Identity / Number Theory]",
      "أثبت أويلر أن الدالة المولدة لعدد تجزئات الأعداد هي \\( \\prod_{k=1}^{\\infty} \\dfrac{1}{1 - x^k} \\). [المرجع: متطابقة أويلر للتجزئات]",
      "Recall Euler's product for unrestrained partitions.", "تذكر جداء أويلر اللانهائي للتجزئات.")

    # 363: Catalan C_5
    q("KAUST-P1-363", "Combinatorics", "Easy",
      "What is the \\( 5 \\)-th Catalan number \\( C_5 \\)?",
      "ما هو عدد كاتالان الخامس \\( C_5 \\)؟",
      ["\\( 14 \\)", "\\( 28 \\)", "\\( 42 \\)", "\\( 90 \\)"], 2,
      "\\( C_5 = \\dfrac{1}{6} \\binom{10}{5} = \\dfrac{252}{6} = 42 \\). [Lineage: Catalan Numbers / AMC 12]",
      "\\( C_5 = \\dfrac{1}{6} \\binom{10}{5} = \\dfrac{252}{6} = 42 \\). [المرجع: أعداد كاتالان]",
      "Compute \\( \\frac{1}{6} \\binom{10}{5} \\).", "احسب \\( \\frac{1}{6} \\binom{10}{5} \\).")

    # 364: Binomial Symmetry
    q("KAUST-P1-364", "Combinatorics", "Easy",
      "Which identity demonstrates the combinatorial symmetry of selecting \\( k \\) items versus leaving behind \\( n - k \\) items?",
      "أي متطابقة توضح التماثل التوافقي لاختيار \\( k \\) من العناصر مقابل ترك \\( n - k \\) منها؟",
      ["\\( \\binom{n}{k} = \\binom{n}{n-k} \\)", "\\( \\binom{n}{k} = \\binom{n-1}{k} \\)", "\\( \\binom{n}{k} = \\dfrac{n}{k} \\)", "\\( \\binom{n}{k} = \\binom{n+1}{k+1} \\)"], 0,
      "The binomial coefficients are symmetric: \\( \\binom{n}{k} = \\dfrac{n!}{k!(n-k)!} = \\binom{n}{n-k} \\). [Lineage: Combinatorial Identities]",
      "المعاملات الثنائية متماثلة: \\( \\binom{n}{k} = \\binom{n}{n-k} \\). [المرجع: متطابقات التوافيق]",
      "Recall Pascal's symmetry property.", "تذكر خاصية التماثل في مثلث باسكال.")

    # 365: Stars and bars upper bound
    q("KAUST-P1-365", "Combinatorics", "Hard",
      "Three standard 6-sided dice are rolled. How many outcomes produce a sum of exactly \\( 10 \\)?",
      "أُلقيت 3 نردات قياسية ذات 6 أوجه. كم نتيجة مختلفة تعطي مجموعاً يساوي 10 بالضبط؟",
      ["\\( 24 \\)", "\\( 27 \\)", "\\( 30 \\)", "\\( 36 \\)"], 1,
      "Let \\( x_1 + x_2 + x_3 = 10 \\) with \\( 1 \\le x_i \\le 6 \\). Let \\( y_i = x_i - 1 \\ge 0 \\), so \\( y_1 + y_2 + y_3 = 7 \\) with \\( y_i \\le 5 \\). Total non-negative solutions: \\( \\binom{7+3-1}{3-1} = \\binom{9}{2} = 36 \\). Subtract solutions where some \\( y_i \\ge 6 \\): If \\( y_1 \\ge 6 \\), let \\( z_1 = y_1 - 6 \\ge 0 \\implies z_1 + y_2 + y_3 = 1 \\), giving \\( \\binom{1+2}{2} = 3 \\) solutions. There are \\( 3 \\) variables that could exceed 5, so subtract \\( 3 \\times 3 = 9 \\). Valid outcomes: \\( 36 - 9 = 27 \\). [Lineage: AIME / Generating Functions Dice Sum]",
      "بتحويل المسألة إلى \\( y_1 + y_2 + y_3 = 7 \\) مع \\( y_i \\le 5 \\): الحلول الكلية \\( \\binom{9}{2} = 36 \\). نطرح الحالات التي يتجاوز فيها أحد المتغيرات 5 (وعددها \\( 3 \\times 3 = 9 \\)): \\( 36 - 9 = 27 \\). [المرجع: أولمبياد AIME للرياضيات]",
      "Use inclusion-exclusion on the upper bound \\( y_i \\le 5 \\).", "استخدم مبدأ الشمول والاستبعاد على الحد الأعلى 5.")

    # 366: Mantel's Theorem
    q("KAUST-P1-366", "Graph Theory", "Medium",
      "According to Mantel's Theorem, what is the maximum number of edges in a triangle-free simple graph on \\( 8 \\) vertices?",
      "وفقاً لمبرهنة مانتل، ما هو أكبر عدد من الحواف في رسم بياني بسيط خالٍ من المثلثات يحتوي على \\( 8 \\) رؤوس؟",
      ["\\( 12 \\)", "\\( 14 \\)", "\\( 16 \\)", "\\( 28 \\)"], 2,
      "Mantel's theorem states that a triangle-free graph on \\( n \\) vertices has at most \\( \\lfloor n^2 / 4 \\rfloor \\) edges. For \\( n = 8 \\): \\( \\lfloor 64 / 4 \\rfloor = 16 \\) (achieved by \\( K_{4, 4} \\)). [Lineage: Mantel's Extremal Graph Theorem]",
      "تنص مبرهنة مانتل على أن الحد الأقصى للحواف هو \\( \\lfloor n^2 / 4 \\rfloor \\). عند \\( n = 8 \\): \\( 64 / 4 = 16 \\). [المرجع: مبرهنة مانتل في نظرية الرسوم المتطرفة]",
      "Evaluate \\( \\lfloor n^2 / 4 \\rfloor \\).", "احسب \\( \\lfloor n^2 / 4 \\rfloor \\).")

    # 367: Complement graph edges
    q("KAUST-P1-367", "Graph Theory", "Easy",
      "A simple graph \\( G \\) on \\( 6 \\) vertices contains \\( 7 \\) edges. How many edges does its complement graph \\( \\overline{G} \\) have?",
      "رسم بياني بسيط \\( G \\) على \\( 6 \\) رؤوس يحتوي على \\( 7 \\) حواف. كم عدد حواف متممه \\( \\overline{G} \\)؟",
      ["\\( 6 \\)", "\\( 7 \\)", "\\( 8 \\)", "\\( 15 \\)"], 2,
      "The complete graph \\( K_6 \\) has \\( \\binom{6}{2} = 15 \\) edges. Thus, \\( |E(\\overline{G})| = \\binom{6}{2} - |E(G)| = 15 - 7 = 8 \\). [Lineage: Complement Graphs / AMC 12]",
      "الرسم الكامل \\( K_6 \\) يحتوي على 15 حافة. عدد حواف المتمم هو \\( 15 - 7 = 8 \\). [المرجع: متمم الرسم البياني]",
      "Subtract the edge count from \\( \\binom{6}{2} \\).", "اطرح عدد الحواف من 15.")

    # 368: Tree Center
    q("KAUST-P1-368", "Graph Theory", "Medium",
      "By Jordan's Theorem (1869), the center of any tree consists of:",
      "وفقاً لمبرهنة جوردان، يتكون مركز أي شجرة من:",
      ["Exactly 1 vertex only", "Either 1 vertex or 2 adjacent vertices", "Any number of vertices forming a cycle", "The set of all leaves"], 1,
      "Camille Jordan proved in 1869 that every tree has a center consisting of either a single vertex or two adjacent vertices. [Lineage: Tree Center / Jordan's Theorem]",
      "أثبت جوردان أن مركز أي شجرة يتكون إما من رأس واحد فقط أو رأسين متجاورين. [المرجع: مبرهنة جوردان لمراكز الأشجار]",
      "Think about iteratively pruning leaves from a tree.", "فكر في عملية الحذف المتتالي لأوراق الشجرة.")

    # 369: Kuratowski's Theorem
    q("KAUST-P1-369", "Graph Theory", "Easy",
      "Kuratowski's Theorem states that a graph is planar if and only if it contains no subgraph homeomorphic to:",
      "تنص مبرهنة كوراتوفسكي على أن الرسم البياني يكون مستوياً إذا وفقط إذا لم يحتوِ على رسم جزئي متماثل طوبولوجياً مع:",
      ["\\( K_3 \\) or \\( C_4 \\)", "\\( K_4 \\) or \\( K_{2, 3} \\)", "\\( K_5 \\) or \\( K_{3, 3} \\)", "\\( C_5 \\) or \\( C_6 \\)"], 2,
      "Kuratowski's celebrated 1930 theorem characterizes planar graphs by the forbidden topological minors \\( K_5 \\) (complete on 5 vertices) and \\( K_{3, 3} \\) (utility graph). [Lineage: Kuratowski's Planarity Theorem]",
      "مبرهنة كوراتوفسكي تميز الرسوم المستوية بعدم احتوائها على \\( K_5 \\) أو \\( K_{3, 3} \\). [المرجع: مبرهنة كوراتوفسكي]",
      "Recall the two minimal non-planar graphs.", "تذكر أصغر رسمين غير مستويين.")

    # 370: Dirac's Theorem
    q("KAUST-P1-370", "Graph Theory", "Medium",
      "Dirac's Theorem guarantees that a simple graph with \\( n \\ge 3 \\) vertices contains a Hamiltonian cycle if every vertex \\( v \\) has degree:",
      "تضمن مبرهنة ديراك احتواء رسم بسيط ذي \\( n \\ge 3 \\) رؤوس على دورة هاملتونية إذا كانت درجة كل رأس تحقق:",
      ["\\( \\deg(v) \\ge 2 \\)", "\\( \\deg(v) \\ge \\dfrac{n}{2} \\)", "\\( \\deg(v) \\ge \\dfrac{n-1}{2} \\)", "\\( \\deg(v) \\ge \\sqrt{n} \\)"], 1,
      "Dirac's Theorem (1952) states that if every vertex in a graph of \\( n \\ge 3 \\) vertices satisfies \\( \\deg(v) \\ge n/2 \\), then the graph is Hamiltonian. [Lineage: Dirac's Hamiltonian Theorem]",
      "تنص مبرهنة ديراك على أن شرط وجود دورة هاملتونية هو أن تكون درجة كل رأس \\( \\deg(v) \\ge n/2 \\). [المرجع: مبرهنة ديراك]",
      "Recall Dirac's minimum degree condition.", "تذكر شرط الدرجة الصغرى عند ديراك.")

    # 371: Fermat's Little Theorem 3^30 mod 31
    q("KAUST-P1-371", "Number Theory", "Easy",
      "What is the value of \\( 3^{30} \\pmod{31} \\)?",
      "ما هي قيمة \\( 3^{30} \\pmod{31} \\)؟",
      ["\\( 0 \\)", "\\( 1 \\)", "\\( 3 \\)", "\\( 30 \\)"], 1,
      "Since \\( 31 \\) is prime and \\( \\gcd(3, 31) = 1 \\), by Fermat's Little Theorem \\( a^{p-1} \\equiv 1 \\pmod p \\), so \\( 3^{30} \\equiv 1 \\pmod{31} \\). [Lineage: Fermat's Little Theorem]",
      "بما أن 31 عدد أولي، فبمبرهنة فيرما الصغرى \\( 3^{31-1} \\equiv 1 \\pmod{31} \\). [المرجع: مبرهنة فيرما الصغرى]",
      "Apply Fermat's Little Theorem \\( a^{p-1} \\equiv 1 \\pmod p \\).", "طبق مبرهنة فيرما الصغرى مباشرة.")

    # 372: Quadratic residues mod 11
    q("KAUST-P1-372", "Number Theory", "Easy",
      "How many non-zero quadratic residues exist modulo the prime \\( 11 \\)?",
      "كم عدد البواقي التربيعية غير الصفرية مقياس العدد الأولي \\( 11 \\)؟",
      ["\\( 4 \\)", "\\( 5 \\)", "\\( 6 \\)", "\\( 10 \\)"], 1,
      "For any odd prime \\( p \\), there are exactly \\( \\dfrac{p - 1}{2} \\) non-zero quadratic residues. For \\( p = 11 \\): \\( \\dfrac{10}{2} = 5 \\) (specifically \\( 1, 3, 4, 5, 9 \\)). [Lineage: Quadratic Residues / Number Theory]",
      "لأي عدد أولي فردي، يوجد بالضبط \\( (p-1)/2 \\) باقياً تربيعياً. عند \\( p = 11 \\): يوجد 5 بواقي تربيعية. [المرجع: البواقي التربيعية]",
      "Compute \\( (p-1)/2 \\).", "احسب \\( (p-1)/2 \\).")

    # 373: Euclidean algorithm
    q("KAUST-P1-373", "Number Theory", "Easy",
      "Compute \\( \\gcd(252, 105) \\) using the Euclidean algorithm.",
      "احسب \\( \\gcd(252, 105) \\) باستخدام خوارزمية إقليدس.",
      ["\\( 7 \\)", "\\( 14 \\)", "\\( 21 \\)", "\\( 42 \\)"], 2,
      "\\( 252 = 2(105) + 42 \\); \\( 105 = 2(42) + 21 \\); \\( 42 = 2(21) + 0 \\). Thus \\( \\gcd(252, 105) = 21 \\). [Lineage: Euclidean Algorithm / AMC 12]",
      "بقسمة 252 على 105 نحصل على باقٍ 42، ثم 105 على 42 يعطي 21، ثم 42 على 21 يعطي صفراً. إذن القاسم المشترك الأكبر هو 21. [المرجع: خوارزمية إقليدس]",
      "Apply successive divisions.", "طبق القسمات المتتالية بخوارزمية إقليدس.")

    # 374: Bezout identity
    q("KAUST-P1-374", "Number Theory", "Easy",
      "Bézout's identity asserts that for integers \\( a \\) and \\( b \\), there exist integers \\( x, y \\) such that \\( ax + by \\) equals:",
      "تؤكد متطابقة بيزو أنه لأي عددين صحيحين \\( a \\) و \\( b \\)، يوجد عددان صحيحان \\( x, y \\) بحيث \\( ax + by \\) يساوي:",
      ["\\( a \\cdot b \\)", "\\( \\text{lcm}(a, b) \\)", "\\( \\gcd(a, b) \\)", "\\( a + b \\)"], 2,
      "Bézout's identity states that the greatest common divisor \\( \\gcd(a, b) \\) can always be expressed as an integer linear combination \\( ax + by \\). [Lineage: Bezout's Identity]",
      "تنص متطابقة بيزو على إمكانية كتابة القاسم المشترك الأكبر \\( \\gcd(a, b) \\) كتركيبة خطية صحيحة \\( ax + by \\). [المرجع: متطابقة بيزو]",
      "Recall the fundamental theorem of Bezout.", "تذكر نص مبرهنة بيزو.")

    # 375: Goldbach
    q("KAUST-P1-375", "Number Theory", "Easy",
      "Goldbach's famous conjecture states that every even integer greater than \\( 2 \\) can be written as the sum of:",
      "تنص حدسية غولدباخ الشهيرة على أن كل عدد صحيح زوجي أكبر من 2 يمكن كتابته كمجموع:",
      ["Two odd integers", "Two prime numbers", "Three distinct squares", "Two triangular numbers"], 1,
      "Goldbach's conjecture (1742) proposes that every even integer greater than 2 is the sum of two primes. [Lineage: Goldbach Conjecture]",
      "تنص حدسية غولدباخ على أن كل عدد زوجي أكبر من 2 هو مجموع عددين أوليين. [المرجع: حدسية غولدباخ]",
      "Recall Goldbach's conjecture statement.", "تذكر نص حدسية غولدباخ.")

    # 376: Skew-symmetric 3x3
    q("KAUST-P1-376", "Linear Algebra", "Easy",
      "Let \\( A \\) be a \\( 3 \\times 3 \\) real skew-symmetric matrix (meaning \\( A^T = -A \\)). What is the value of \\( \\det(A) \\)?",
      "لتكن \\( A \\) مصفوفة حقيقية متخالفة التماثل (skew-symmetric) من الرتبة \\( 3 \\times 3 \\) (أي \\( A^T = -A \\)). ما هي قيمة \\( \\det(A) \\)؟",
      ["\\( -1 \\)", "\\( 0 \\)", "\\( 1 \\)", "Cannot be determined"], 1,
      "\\( \\det(A) = \\det(A^T) = \\det(-A) = (-1)^3 \\det(A) = -\\det(A) \\implies 2\\det(A) = 0 \\implies \\det(A) = 0 \\). [Lineage: Linear Algebra / Skew-Symmetric Matrices]",
      "بما أن الرتبة 3 فردية: \\( \\det(A) = (-1)^3 \\det(A) = -\\det(A) \\implies \\det(A) = 0 \\). [المرجع: محددات المصفوفات متخالفة التماثل]",
      "Use \\( \\det(A^T) = \\det(A) \\) and \\( \\det(-A) = (-1)^n \\det(A) \\).", "استخدم خاصية إخراج الإشارة السالبة من المحدد الفردي الرتبة.")

    # 377: Block triangular
    q("KAUST-P1-377", "Linear Algebra", "Easy",
      "What is the determinant of the block matrix \\( M = \\begin{pmatrix} A & B \\\\ \\mathbf{0} & D \\end{pmatrix} \\), where \\( A \\) and \\( D \\) are square matrices?",
      "ما هو محدد مصفوفة الكتل \\( M = \\begin{pmatrix} A & B \\\\ \\mathbf{0} & D \\end{pmatrix} \\) حيث \\( A \\) و \\( D \\) مصفوفتان مربعتان؟",
      ["\\( \\det(A) + \\det(D) \\)", "\\( \\det(A)\\det(D) \\)", "\\( \\det(A)\\det(D) - \\det(B) \\)", "\\( \\det(AD - BC) \\)"], 1,
      "For a block upper triangular matrix, \\( \\det(M) = \\det(A) \\det(D) \\). [Lineage: Block Matrix Determinants / MIT 18.06]",
      "محدد مصفوفة الكتل المثلثية العلوية هو حاصل ضرب محددي كتلتي القطر: \\( \\det(A)\\det(D) \\). [المرجع: الجبر الخطي في MIT]",
      "The determinant of a block triangular matrix is the product of diagonal block determinants.", "محدد مصفوفة الكتل المثلثية هو جداء محددي كتلتي القطر.")

    # 378: Angle between vectors
    q("KAUST-P1-378", "Linear Algebra", "Easy",
      "What is the angle \\( \\theta \\) between vectors \\( \\mathbf{u} = \\langle 1, 1 \\rangle \\) and \\( \\mathbf{v} = \\langle 1, 0 \\rangle \\)?",
      "ما هي الزاوية \\( \\theta \\) بين المتجهين \\( \\mathbf{u} = \\langle 1, 1 \\rangle \\) و \\( \\mathbf{v} = \\langle 1, 0 \\rangle \\)؟",
      ["\\( 30^\\circ \\)", "\\( 45^\\circ \\)", "\\( 60^\\circ \\)", "\\( 90^\\circ \\)"], 1,
      "\\( \\cos\\theta = \\dfrac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|} = \\dfrac{1}{\\sqrt{2} \\times 1} = \\dfrac{1}{\\sqrt{2}} \\implies \\theta = 45^\\circ \\). [Lineage: Vector Angles / AMC 12]",
      "\\( \\cos\\theta = \\dfrac{1}{\\sqrt{2}} \\implies \\theta = 45^\\circ \\). [المرجع: الزوايا بين المتجهات]",
      "Use \\( \\cos\\theta = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|} \\).", "طبق قانون جيب تمام الزاوية بين متجهين.")

    # 379: Linear dependence in R^3
    q("KAUST-P1-379", "Linear Algebra", "Medium",
      "For which value of \\( c \\) are the three vectors \\( \\langle 1, 2, 3 \\rangle \\), \\( \\langle 0, 1, 2 \\rangle \\), and \\( \\langle 1, 3, c \\rangle \\) linearly dependent?",
      "لأي قيمة للثابت \\( c \\) تكون المتجهات الثلاثة \\( \\langle 1, 2, 3 \\rangle \\) و \\( \\langle 0, 1, 2 \\rangle \\) و \\( \\langle 1, 3, c \\rangle \\) مرتبطة خطياً؟",
      ["\\( c = 3 \\)", "\\( c = 4 \\)", "\\( c = 5 \\)", "\\( c = 6 \\)"], 2,
      "Notice \\( \\langle 1, 3, c \\rangle = \\langle 1, 2, 3 \\rangle + \\langle 0, 1, 2 \\rangle = \\langle 1, 3, 5 \\rangle \\). Setting the determinant to zero: \\( \\begin{vmatrix} 1 & 0 & 1 \\\\ 2 & 1 & 3 \\\\ 3 & 2 & c \\end{vmatrix} = 1(c - 6) + 1(4 - 3) = c - 6 + 1 = c - 5 = 0 \\implies c = 5 \\). [Lineage: Linear Independence / MIT 18.06]",
      "بمساواة محدد المصفوفة بالصفر نجد: \\( c - 5 = 0 \\implies c = 5 \\) (وهو مجموع المتجهين الأول والثاني). [المرجع: الارتباط الخطي]",
      "Set the determinant of the 3x3 matrix to zero.", "ساوِ محدد مصفوفة المتجهات الثلاثة بالصفر.")

    # 380: Matrix multiplication
    q("KAUST-P1-380", "Linear Algebra", "Easy",
      "In general, which algebraic property does NOT hold for matrix multiplication of square matrices?",
      "بشكل عام، أي خاصية جبرية لا تنطبق على ضرب المصفوفات المربعة؟",
      ["Associativity: \\( A(BC) = (AB)C \\)", "Distributivity: \\( A(B + C) = AB + AC \\)", "Commutativity: \\( AB = BA \\)", "Identity: \\( AI = IA = A \\)"], 2,
      "Matrix multiplication is generally non-commutative (\\( AB \\ne BA \\) in general). [Lineage: Matrix Algebra]",
      "ضرب المصفوفات ليس عملية إبدالية بشكل عام: \\( AB \\ne BA \\). [المرجع: جبر المصفوفات]",
      "Which property fails when order of operands matters?", "أي خاصية تفشل عندما يكون ترتيب العناصر مؤثراً؟")

    # 381: Complex roots x^3 = 1
    q("KAUST-P1-381", "Complex Numbers", "Easy",
      "What are the three complex roots of \\( z^3 = 1 \\)?",
      "ما هي الجذور المركبة الثلاثة للمعادلة \\( z^3 = 1 \\)؟",
      ["\\( 1, i, -i \\)", "\\( 1, -1, 0 \\)", "\\( 1, \\dfrac{-1 + i\\sqrt{3}}{2}, \\dfrac{-1 - i\\sqrt{3}}{2} \\)", "\\( 1, \\dfrac{1 + i\\sqrt{3}}{2}, \\dfrac{1 - i\\sqrt{3}}{2} \\)"], 2,
      "\\( z^3 - 1 = (z - 1)(z^2 + z + 1) = 0 \\). Solving \\( z^2 + z + 1 = 0 \\) by the quadratic formula gives \\( z = \\dfrac{-1 \\pm i\\sqrt{3}}{2} \\). [Lineage: Roots of Unity / AMC 12]",
      "بتحليل فرق المكعبين \\( (z-1)(z^2+z+1) = 0 \\)، جذور المعادلة التربيعية هي \\( \\dfrac{-1 \\pm i\\sqrt{3}}{2} \\). [المرجع: جذور الوحدة التكعيبية]",
      "Factor \\( z^3 - 1 = (z - 1)(z^2 + z + 1) \\).", "حلل فرق المكعبين.")

    # 382: Modulus multiplication
    q("KAUST-P1-382", "Complex Numbers", "Easy",
      "If \\( z_1 = 3 + 4i \\) and \\( z_2 = 1 - i \\), what is the modulus \\( |z_1 z_2| \\)?",
      "إذا كان \\( z_1 = 3 + 4i \\) و \\( z_2 = 1 - i \\)، فما هو المقياس \\( |z_1 z_2| \\)؟",
      ["\\( 5 \\)", "\\( 5\\sqrt{2} \\)", "\\( 10 \\)", "\\( 25 \\)"], 1,
      "By multiplicativity of modulus: \\( |z_1 z_2| = |z_1| \\cdot |z_2| = \\sqrt{3^2 + 4^2} \\cdot \\sqrt{1^2 + (-1)^2} = 5\\sqrt{2} \\). [Lineage: Complex Modulus]",
      "مقياس حاصل الضرب يساوي حاصل ضرب المقياسين: \\( 5 \\times \\sqrt{2} = 5\\sqrt{2} \\). [المرجع: مقياس الأعداد المركبة]",
      "Multiply the individual moduli.", "اضرب معياري العددين.")

    # 383: Argument quotient
    q("KAUST-P1-383", "Complex Numbers", "Easy",
      "For non-zero complex numbers \\( z_1 \\) and \\( z_2 \\), what is \\( \\arg\\left(\\dfrac{z_1}{z_2}\\right) \\)?",
      "لأي عددين مركبين غير صفريين \\( z_1 \\) و \\( z_2 \\)، ما هي سعة خارج القسمة \\( \\arg\\left(\\dfrac{z_1}{z_2}\\right) \\)؟",
      ["\\( \\arg(z_1) \\cdot \\arg(z_2) \\)", "\\( \\arg(z_1) + \\arg(z_2) \\)", "\\( \\arg(z_1) - \\arg(z_2) \\)", "\\( \\dfrac{\\arg(z_1)}{\\arg(z_2)} \\)"], 2,
      "Under division in polar form: \\( \\arg(z_1 / z_2) = \\arg(z_1) - \\arg(z_2) \\pmod{2\\pi} \\). [Lineage: Complex Polar Form]",
      "سعة خارج قسمة عددين مركبين هي الفرق بين سعتيهما: \\( \\arg(z_1) - \\arg(z_2) \\). [المرجع: الصورة القطبية للأعداد المركبة]",
      "Recall polar division rules.", "تذكر قواعد قسمة الأعداد المركبة بالصورة القطبية.")

    # 384: Euler's identity
    q("KAUST-P1-384", "Complex Numbers", "Easy",
      "Which famous identity connects five fundamental mathematical constants (\\( e, i, \\pi, 1, 0 \\))?",
      "أي متطابقة شهيرة تربط بين خمسة من أهم الثوابت الرياضية الأساسية (\\( e, i, \\pi, 1, 0 \\))؟",
      ["\\( e^{i\\pi} + 1 = 0 \\)", "\\( e^{\\pi} - i = 0 \\)", "\\( e^{2\\pi} = 1 \\)", "\\( i^2 + \\pi = e \\)"], 0,
      "Euler's identity states \\( e^{i\\pi} + 1 = 0 \\), derived from \\( e^{i\\theta} = \\cos\\theta + i\\sin\\theta \\) with \\( \\theta = \\pi \\). [Lineage: Euler's Identity]",
      "متطابقة أويلر الشهيرة: \\( e^{i\\pi} + 1 = 0 \\). [المرجع: متطابقة أويلر]",
      "Recall Euler's formula evaluated at \\( \\pi \\).", "عوض بـ \\( \\pi \\) في صيغة أويلر.")

    # 385: Cauchy functional equation
    q("KAUST-P1-385", "Functions & Analysis", "Medium",
      "If a continuous function \\( f: \\mathbb{R} \\to \\mathbb{R} \\) satisfies \\( f(x + y) = f(x) + f(y) \\) for all \\( x, y \\in \\mathbb{R} \\), what form MUST \\( f(x) \\) take?",
      "إذا كانت الدالة المتصلة \\( f: \\mathbb{R} \\to \\mathbb{R} \\) تحقق \\( f(x + y) = f(x) + f(y) \\) لجميع \\( x, y \\in \\mathbb{R} \\)، فما هي الصورة الإلزامية لـ \\( f(x) \\)؟",
      ["\\( f(x) = c x \\)", "\\( f(x) = x^c \\)", "\\( f(x) = c e^x \\)", "\\( f(x) = x + c \\)"], 0,
      "Cauchy's functional equation with continuity implies linearity: \\( f(x) = cx \\) where \\( c = f(1) \\). [Lineage: Cauchy Functional Equation / Putnam]",
      "معادلة كوشي التابعية مع شرط الاتصال تقتضي خطية الدالة: \\( f(x) = cx \\). [المرجع: معادلة كوشي التابعية]",
      "Recall Cauchy's additive functional equation solution.", "تذكر حل معادلة كوشي الجمعية.")

    # 386: Telescoping Product
    q("KAUST-P1-386", "Sequences & Series", "Medium",
      "Evaluate the infinite product: \\( \\prod_{k=2}^{\\infty} \\left(1 - \\dfrac{1}{k^2}\\right) = \\left(1 - \\dfrac{1}{4}\\right)\\left(1 - \\dfrac{1}{9}\\right)\\left(1 - \\dfrac{1}{16}\\right) \\dots \\).",
      "احسب قيمة الجداء اللانهائي: \\( \\prod_{k=2}^{\\infty} \\left(1 - \\dfrac{1}{k^2}\\right) \\).",
      ["\\( \\dfrac{1}{4} \\)", "\\( \\dfrac{1}{2} \\)", "\\( \\dfrac{2}{3} \\)", "\\( \\dfrac{3}{4} \\)"], 1,
      "Notice \\( 1 - \\dfrac{1}{k^2} = \\dfrac{k^2 - 1}{k^2} = \\dfrac{(k-1)(k+1)}{k^2} = \\dfrac{k-1}{k} \\cdot \\dfrac{k+1}{k} \\). The partial product telescopes: \\( P_N = \\left( \\dfrac{1}{2} \\cdot \\dfrac{2}{3} \\dots \\dfrac{N-1}{N} \\right) \\times \\left( \\dfrac{3}{2} \\cdot \\dfrac{4}{3} \\dots \\dfrac{N+1}{N} \\right) = \\dfrac{1}{N} \\times \\dfrac{N+1}{2} = \\dfrac{N+1}{2N} \\). Taking \\( N \\to \\infty \\), the limit is \\( \\dfrac{1}{2} \\). [Lineage: Telescoping Products / Putnam]",
      "بتحليل \\( \\dfrac{(k-1)(k+1)}{k^2} \\)، يتلاشى الجداء ليعطي \\( \\dfrac{N+1}{2N} \\). وبأخذ النهاية نحصل على \\( 1/2 \\). [المرجع: الجداءات التلسكوبية في مسابقة بوتنام]",
      "Factor \\( 1 - 1/k^2 = (k-1)(k+1)/k^2 \\) and telescope.", "حلل إلى فرق مربعات واختصر الحدود المتتالية.")

    # 387: Stirling limit
    q("KAUST-P1-387", "Sequences & Series", "Hard",
      "Evaluate the limit \\( \\lim_{n \\to \\infty} \\dfrac{(n!)^{1/n}}{n} \\).",
      "احسب قيمة النهاية \\( \\lim_{n \\to \\infty} \\dfrac{(n!)^{1/n}}{n} \\).",
      ["\\( 0 \\)", "\\( \\dfrac{1}{e} \\)", "\\( 1 \\)", "\\( e \\)"], 1,
      "By Stirling's approximation \\( n! \\sim \\sqrt{2\\pi n} (n/e)^n \\), taking the \\( n \\)-th root gives \\( (n!)^{1/n} \\sim \\dfrac{n}{e} \\). Thus, \\( \\lim_{n \\to \\infty} \\dfrac{(n!)^{1/n}}{n} = \\dfrac{1}{e} \\). [Lineage: Stirling's Formula / Cambridge Tripos]",
      "باستخدام تقريب ستيرلينغ \\( n! \\approx (n/e)^n \\)، وبأخذ الجذر النوني وقسمته على n نحصل على \\( 1/e \\). [المرجع: صيغة ستيرلينغ للتقريب]",
      "Use Stirling's approximation \\( n! \\approx (n/e)^n \\sqrt{2\\pi n} \\).", "طبق تقريب ستيرلينغ للمضروب.")

    # 388: Rearrangement Inequality
    q("KAUST-P1-388", "Algebra & Inequalities", "Medium",
      "For two similarly ordered sequences \\( a_1 \\le a_2 \\le a_3 \\) and \\( b_1 \\le b_2 \\le b_3 \\), which permutation \\( \\pi \\) of \\( \\{1, 2, 3\\} \\) MAXIMIZES the dot product \\( \\sum_{i=1}^3 a_i b_{\\pi(i)} \\)?",
      "لمتتاليتين مرتبتين بالترتيب نفسه \\( a_1 \\le a_2 \\le a_3 \\) و \\( b_1 \\le b_2 \\le b_3 \\)، أي تبديلة \\( \\pi \\) تعطي أقصى قيمة للمجموع \\( \\sum_{i=1}^3 a_i b_{\\pi(i)} \\)؟",
      ["Identity permutation (matching order)", "Reverse order permutation", "Cyclic shift \\( (1 \\, 2 \\, 3) \\)", "All permutations give the same sum"], 0,
      "The Rearrangement Inequality states that the sum of products is maximized when both sequences are sorted in the same order, and minimized when sorted in opposite orders. [Lineage: Rearrangement Inequality]",
      "تنص متراجحة إعادة الترتيب على أن القيمة العظمى تتحقق عندما ترتبط العناصر الأكبر بالأكبر (الترتيب المتطابق نفسه). [المرجع: متراجحة إعادة الترتيب]",
      "Largest elements should pair with largest elements.", "اربط العناصر الكبيرة مع الكبيرة للحصول على أقصى مجموع.")

    # 389: Root test
    q("KAUST-P1-389", "Sequences & Series", "Easy",
      "According to Cauchy's Root Test, the series \\( \\sum a_n \\) converges absolutely if \\( \\limsup_{n \\to \\infty} |a_n|^{1/n} = L \\) satisfies:",
      "وفقاً لاختبار الجذر لكوشي، تتقارب المتسلسلة \\( \\sum a_n \\) تقارباً مطلقاً إذا كانت النهاية العليا \\( L \\) تحقق:",
      ["\\( L < 1 \\)", "\\( L = 1 \\)", "\\( L > 1 \\)", "\\( L = \\infty \\)"], 0,
      "The Root Test concludes absolute convergence when \\( L < 1 \\), divergence when \\( L > 1 \\), and is inconclusive when \\( L = 1 \\). [Lineage: Cauchy Root Test]",
      "يضمن اختبار الجذر التقارب المطلق عندما يكون \\( L < 1 \\). [المرجع: اختبار الجذر لكوشي]",
      "Recall the condition for convergence in the Root Test.", "تذكر شرط التقارب في اختبار الجذر.")

    # 390: p-series test
    q("KAUST-P1-390", "Sequences & Series", "Easy",
      "For which values of real \\( p \\) does the \\( p \\)-series \\( \\sum_{n=1}^{\\infty} \\dfrac{1}{n^p} \\) converge?",
      "لأي قيم للعدد الحقيقي \\( p \\) تتقارب متسلسلة \\( p \\): \\( \\sum_{n=1}^{\\infty} \\dfrac{1}{n^p} \\)؟",
      ["\\( p < 1 \\)", "\\( p \\le 1 \\)", "\\( p > 1 \\)", "\\( p \\ge 0 \\)"], 2,
      "By the integral test, \\( \\int_1^\\infty x^{-p} dx \\) converges if and only if \\( p > 1 \\). [Lineage: p-Series Convergence]",
      "تتقارب متسلسلة p إذا وفقط إذا كان \\( p > 1 \\). [المرجع: تقارب متسلسلات p]",
      "Recall the p-series test result.", "تذكر نتيجة اختبار متسلسلة p.")

    # 391: Reflection across y = x
    q("KAUST-P1-391", "Geometry", "Easy",
      "What are the coordinates of the reflection of the point \\( (2, -5) \\) across the line \\( y = x \\)?",
      "ما هي إحداثيات انعكاس النقطة \\( (2, -5) \\) حول المستقيم \\( y = x \\)؟",
      ["\\( (-2, 5) \\)", "\\( (-5, 2) \\)", "\\( (5, -2) \\)", "\\( (-2, -5) \\)"], 1,
      "Reflection across \\( y = x \\) simply swaps coordinates: \\( (x, y) \\mapsto (y, x) \\). For \\( (2, -5) \\), the reflected point is \\( (-5, 2) \\). [Lineage: Coordinate Reflections]",
      "الانعكاس حول \\( y = x \\) يبدل الإحداثيات: \\( (x, y) \\mapsto (y, x) \\)، فيصبح \\( (-5, 2) \\). [المرجع: التحويلات الهندسية]",
      "Swap x and y.", "بادل بين الإحداثيين السيني والصادي.")

    # 392: Euler Line Ratio
    q("KAUST-P1-392", "Geometry", "Medium",
      "On the Euler line of a non-equilateral triangle, in what ratio does the centroid \\( G \\) divide the segment between the orthocenter \\( H \\) and the circumcenter \\( O \\)?",
      "على خط أويلر لمثلث غير متساوي الأضلاع، بأي نسبة تقسم نقطة تلاقي المتوسطات \\( G \\) القطعة المستقيمة بين ملتقى الارتفاعات \\( H \\) ومركز الدائرة المحيطة \\( O \\)؟",
      ["\\( HG : GO = 1 : 1 \\)", "\\( HG : GO = 2 : 1 \\)", "\\( HG : GO = 3 : 1 \\)", "\\( HG : GO = 1 : 2 \\)"], 1,
      "Leonhard Euler proved in 1765 that \\( H, G, O \\) are collinear with \\( G \\) lying between \\( H \\) and \\( O \\) such that \\( HG = 2 GO \\) (ratio \\( 2:1 \\)). [Lineage: Euler Line / Triangle Geometry]",
      "أثبت أويلر أن النقطة G تقع بين H و O بحيث تقسم القطعة بنسبة \\( HG : GO = 2 : 1 \\). [المرجع: خط أويلر في هندسة المثلث]",
      "Recall the famous 2:1 distance ratio on the Euler line.", "تذكر نسبة 2 إلى 1 الشهيرة على خط أويلر.")

    # 393: Intersecting Chords (Diagram)
    d393 = svg_box('<circle cx="130" cy="90" r="65" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/><line x1="75" y1="50" x2="185" y2="130" stroke="#ef4444" stroke-width="2"/><line x1="75" y1="130" x2="185" y2="50" stroke="#16a34a" stroke-width="2"/><circle cx="130" cy="90" r="4" fill="#1e293b"/><text x="135" y="85" font-size="12" fill="#1e293b" font-weight="bold">P</text><text x="95" y="65" font-size="11" fill="#ef4444">PA=3</text><text x="145" y="125" font-size="11" fill="#ef4444">PB=8</text><text x="95" y="125" font-size="11" fill="#16a34a">PC=4</text><text x="150" y="65" font-size="11" fill="#16a34a">PD=?</text>', "Intersecting Chords", 360, 180)
    q("KAUST-P1-393", "Geometry", "Easy",
      "Two chords \\( AB \\) and \\( CD \\) intersect inside a circle at point \\( P \\). If \\( PA = 3 \\), \\( PB = 8 \\), and \\( PC = 4 \\), find the length of segment \\( PD \\).",
      "يتقاطع وتران \\( AB \\) و \\( CD \\) داخل دائرة عند نقطة \\( P \\). إذا كان \\( PA = 3 \\) و \\( PB = 8 \\) و \\( PC = 4 \\)، فما طول القطعة \\( PD \\)؟",
      ["\\( 4 \\)", "\\( 6 \\)", "\\( 7 \\)", "\\( 8 \\)"], 1,
      "By the Intersecting Chords Theorem: \\( PA \\cdot PB = PC \\cdot PD \\implies 3 \\times 8 = 4 \\cdot PD \\implies 24 = 4 \\cdot PD \\implies PD = 6 \\). [Lineage: Intersecting Chords Theorem / AMC 12]",
      "حسب نظرية الأوتار المتقاطعة داخل دائرة: \\( PA \\cdot PB = PC \\cdot PD \\implies 3 \\times 8 = 4 \\cdot PD \\implies PD = 6 \\). [المرجع: نظرية الأوتار المتقاطعة]",
      "Use \\( PA \\cdot PB = PC \\cdot PD \\).", "طبق قانون جداء قطعتي الوترين المتقاطعين.", diagram=d393)

    # 394: Stewart's Theorem
    q("KAUST-P1-394", "Geometry", "Medium",
      "Which classical theorem relates the lengths of the sides of a triangle to the length of a cevian dividing the opposite side?",
      "أي مبرهنة كلاسيكية تربط بين أطوال أضلاع المثلث وطول قاطع رأسي (cevian) يقسم الضلع المقابل؟",
      ["Stewart's Theorem", "Ptolemy's Theorem", "Simson's Theorem", "Brahmagupta's Formula"], 0,
      "Stewart's Theorem states: \\( b^2 m + c^2 n = a(d^2 + mn) \\), relating cevian length \\( d \\) to the side segments. [Lineage: Stewart's Theorem]",
      "مبرهنة ستيوارت تعطي العلاقة الشهيرة \\( b^2 m + c^2 n = a(d^2 + mn) \\). [المرجع: مبرهنة ستيوارت في هندسة المثلث]",
      "Remember the mnemonic 'man + dad = bmb + cnc'.", "تذكر مبرهنة أطوال القواطع الرأسية في المثلث.")

    # 395: Ptolemy's Theorem
    q("KAUST-P1-395", "Geometry", "Easy",
      "For a cyclic quadrilateral \\( ABCD \\) inscribed in a circle, what does Ptolemy's Theorem state about the product of its diagonals \\( AC \\cdot BD \\)?",
      "للرباعي الدائري \\( ABCD \\) المرسوم داخل دائرة، ماذا تنص مبرهنة بطليموس بشأن حاصل ضرب قطريه \\( AC \\cdot BD \\)؟",
      ["\\( AC \\cdot BD = AB \\cdot CD + BC \\cdot AD \\)", "\\( AC \\cdot BD = AB \\cdot BC + CD \\cdot DA \\)", "\\( AC \\cdot BD = AB + BC + CD + DA \\)", "\\( AC = BD \\)"], 0,
      "Ptolemy's Theorem states that for any cyclic quadrilateral, the product of the diagonals equals the sum of the products of opposite sides: \\( AC \\cdot BD = AB \\cdot CD + BC \\cdot AD \\). [Lineage: Ptolemy's Theorem / AMC 12]",
      "تنص مبرهنة بطليموس على أن حاصل ضرب القطرين يساوي مجموع حاصلي ضرب كل ضلعين متقابلين: \\( AC \\cdot BD = AB \\cdot CD + BC \\cdot AD \\). [المرجع: مبرهنة بطليموس للرباعي الدائري]",
      "Product of diagonals equals sum of products of opposite sides.", "جداء القطرين يساوي مجموع جداءي الأضلاع المتقابلة.")

    # 396: Gambler's ruin
    q("KAUST-P1-396", "Probability", "Medium",
      "A gambler plays a fair game (win or lose \\$1 with probability \\( 1/2 \\)). Starting with \\$20, what is the probability they reach \\$100 before going bankrupt (\\$0)?",
      "يلعب مقامر لعبة عادلة (يربح أو يخسر دولاراً باحتمال 1/2). إذا بدأ برصيد 20 دولاراً، فما احتمال وصوله إلى 100 دولار قبل أن يفلس (يصل إلى 0)؟",
      ["\\( \\dfrac{1}{5} \\)", "\\( \\dfrac{1}{4} \\)", "\\( \\dfrac{2}{5} \\)", "\\( \\dfrac{1}{2} \\)"], 0,
      "For a fair gambler's ruin with initial fortune \\( i \\) and target \\( N \\), the ruin/success probabilities are linear: \\( P(\\text{reach } N) = \\dfrac{i}{N} = \\dfrac{20}{100} = \\dfrac{1}{5} \\). [Lineage: Gambler's Ruin / Stochastic Processes]",
      "في مسألة إفلاس المقامر العادلة: احتمال الوصول إلى الهدف N بدءاً من الرصيد i هو \\( i/N = 20/100 = 1/5 \\). [المرجع: مسألة إفلاس المقامر]",
      "In a fair random walk, the probability of hitting N before 0 is \\( i/N \\).", "في المشي العشوائي العادل، الاحتمال يساوي النسبة بين الرصيد المبدئي والهدف.")

    # 397: Total probability
    q("KAUST-P1-397", "Probability", "Easy",
      "If \\( B_1, B_2, B_3 \\) form a partition of the sample space, the Law of Total Probability expresses \\( P(A) \\) as:",
      "إذا كانت \\( B_1, B_2, B_3 \\) تمثل تجزئة لفضاء العينة، فإن قانون الاحتمال الكلي يعبر عن \\( P(A) \\) بـ:",
      ["\\( \\sum_{i=1}^3 P(A \\mid B_i) P(B_i) \\)", "\\( \\sum_{i=1}^3 P(A \\cap B_i) P(B_i) \\)", "\\( \\prod_{i=1}^3 P(A \\mid B_i) \\)", "\\( P(A \\mid B_1) + P(A \\mid B_2) + P(A \\mid B_3) \\)"], 0,
      "By the Law of Total Probability: \\( P(A) = \\sum_{i=1}^n P(A \\mid B_i) P(B_i) \\). [Lineage: Law of Total Probability]",
      "قانون الاحتمال الكلي يجمع الاحتمالات الشرطية الموزونة باحتمالات التجزئة: \\( \\sum P(A \\mid B_i) P(B_i) \\). [المرجع: قانون الاحتمال الكلي]",
      "Recall the definition of total probability expansion.", "تذكر صيغة قانون الاحتمال الكلي.")

    # 398: Negative Binomial
    q("KAUST-P1-398", "Probability", "Medium",
      "The Negative Binomial distribution models which scenario?",
      "أي سيناريو يعبر عنه توزيع ذي الحدين السالب؟",
      ["Number of successes in \\( n \\) fixed trials", "Number of failures before achieving the \\( r \\)-th success", "Time between continuous arrivals", "Number of events in a fixed time interval"], 1,
      "The Negative Binomial distribution models the number of failures (or trials) required to achieve a predetermined number \\( r \\) of successes in independent Bernoulli trials. [Lineage: Discrete Probability Distributions]",
      "يمثل توزيع ذي الحدين السالب عدد المحاولات الفاشلة قبل تحقيق النجاح رقم r في محاولات برنولي المستقلة. [المرجع: التوزيعات الاحتمالية]",
      "Focus on the number of trials to achieve r successes.", "يركز على عدد المحاولات حتى الوصول إلى عدد محدد من النجاحات.")

    # 399: Continuous uniform variance
    q("KAUST-P1-399", "Probability", "Easy",
      "What is the variance of a continuous uniform random variable \\( X \\sim \\text{Uniform}(a, b) \\)?",
      "ما هو تباين متغير عشوائي متصل يتبع التوزيع المنتظم \\( X \\sim \\text{Uniform}(a, b) \\)؟",
      ["\\( \\dfrac{b - a}{2} \\)", "\\( \\dfrac{(b - a)^2}{12} \\)", "\\( \\dfrac{(b - a)^2}{6} \\)", "\\( \\dfrac{b^2 - a^2}{12} \\)"], 1,
      "For \\( X \\sim \\text{Uniform}(a, b) \\): \\( E[X] = \\dfrac{a+b}{2} \\) and \\( \\text{Var}(X) = \\dfrac{(b - a)^2}{12} \\). [Lineage: Continuous Distributions]",
      "تباين التوزيع المنتظم المتصل هو \\( \\dfrac{(b-a)^2}{12} \\). [المرجع: التوزيع المنتظم المتصل]",
      "Evaluate \\( \\int_a^b (x - \\mu)^2 \\frac{1}{b-a} dx \\).", "احسب تكامل التباين للتوزيع المنتظم.")

    # 400: Markov's Inequality
    q("KAUST-P1-400", "Probability", "Easy",
      "For a non-negative random variable \\( X \\ge 0 \\) with finite expectation \\( E[X] \\), Markov's Inequality states that for any \\( a > 0 \\):",
      "لمتغير عشوائي غير سالب \\( X \\ge 0 \\) ذي توقع منتهٍ \\( E[X] \\)، تنص متراجحة ماركوف على أنه لأي \\( a > 0 \\):",
      ["\\( P(X \\ge a) \\le \\dfrac{E[X]}{a} \\)", "\\( P(X \\ge a) \\le \\dfrac{a}{E[X]} \\)", "\\( P(X \\ge a) \\le \\dfrac{\\text{Var}(X)}{a^2} \\)", "\\( P(X \\ge a) = \\dfrac{1}{a} \\)"], 0,
      "Markov's inequality provides the fundamental tail bound \\( P(X \\ge a) \\le \\dfrac{E[X]}{a} \\) for any non-negative random variable. [Lineage: Markov's Inequality]",
      "متراجحة ماركوف الأساسية لذيول التوزيع: \\( P(X \\ge a) \\le \\dfrac{E[X]}{a} \\). [المرجع: متراجحة ماركوف]",
      "Recall Markov's tail bound formula.", "تذكر نص متراجحة ماركوف.")

    return questions

if __name__ == "__main__":
    qs = get_part_c()
    print(f"Generated {len(qs)} Part C questions (351-400).")
