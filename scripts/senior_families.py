import math
from fractions import Fraction as F

def m(x): return "\\( " + str(x) + " \\)"
def val(x):
    if isinstance(x, F):
        return f"\\frac{{{x.numerator}}}{{{x.denominator}}}" if x.denominator != 1 else str(x.numerator)
    return str(x)

def item(family, topic, en, ar, answer, solen, solar, diff="Hard", distractors=None):
    return {
        "family": family, "topic": topic, "en": en, "ar": ar,
        "answer": answer, "solen": solen, "solar": solar,
        "difficulty": diff, "distractors": distractors or []
    }

def senior_extra(k, n, g):
    # Generates senior families from 77 to 356
    a = (n * 3 + 5) % 17 + 2
    b = (n * 7 + 3) % 19 + 2
    c = (n * 2 + 7) % 13 + 1
    d = (n * 5 + 1) % 11 + 2
    x0 = (n % 4) + 1

    if k == 77:
        ans = 3 * (x0 ** 2) + 2 * a * x0 + b
        return item('poly-derivative-at-point', 'Calculus',
                    f'If \\( f(x) = x^3 + {a}x^2 + {b}x - 5 \\), find \\( f\'({x0}) \\).',
                    f'إذا كانت \\( f(x) = x^3 + {a}x^2 + {b}x - 5 \\)، فأوجد \\( f\'({x0}) \\).',
                    ans, f'\\( f\'(x) = 3x^2 + {2*a}x + {b} \\). At x={x0}, value is {ans}.',
                    f'المشتقة: \\( f\'(x) = 3x^2 + {2*a}x + {b} \\). بالتعويض عند x={x0}: {ans}.')

    if k == 78:
        p = (n % 4) + 2
        ans = F(1, p + 1)
        return item('monomial-definite-integral-unit', 'Calculus',
                    f'Evaluate the definite integral \\( \\int_0^1 x^{{{p}}} \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 x^{{{p}}} \\, dx \\).',
                    ans, f'\\( \\int_0^1 x^{{{p}}} dx = [x^{{{p+1}}}/{{{p+1}}}]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 79:
        ans = a**2 + b**2 + c**2
        return item('vector-3d-magnitude-squared', 'Analytic Geometry',
                    f'Find the square of the magnitude \\( \\|\\mathbf{{v}}\\|^2 \\) of the vector \\( \\mathbf{{v}} = ({a}, {b}, {c}) \\).',
                    f'أوجد مربع معيار المتجه \\( \\mathbf{{v}} = ({a}, {b}, {c}) \\).',
                    ans, f'\\( \\|\\mathbf{{v}}\\|^2 = {a}^2 + {b}^2 + {c}^2 = {ans} \\).',
                    f'مربع المعيار = {ans}.')

    if k == 80:
        ans = a * c + b * d
        return item('dot-product-vectors-2d', 'Analytic Geometry',
                    f'Find the dot product \\( \\mathbf{{u}} \\cdot \\mathbf{{v}} \\) of vectors \\( \\mathbf{{u}} = ({a}, {b}) \\) and \\( \\mathbf{{v}} = ({c}, {d}) \\).',
                    f'أوجد الضرب القياسي للمتجهين \\( \\mathbf{{u}} = ({a}, {b}) \\) و \\( \\mathbf{{v}} = ({c}, {d}) \\).',
                    ans, f'\\( \\mathbf{{u}} \\cdot \\mathbf{{v}} = ({a})({c}) + ({b})({d}) = {ans} \\).',
                    f'حاصل الضرب القياسي = {ans}.')

    if k == 81:
        ans = a + d
        return item('matrix-trace-2x2', 'Matrices and Determinants',
                    f'Find the trace of the matrix \\( A = \\begin{{pmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{pmatrix}} \\).',
                    f'أوجد أثر المصفوفة \\( A = \\begin{{pmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{pmatrix}} \\).',
                    ans, f'Trace is the sum of main diagonal entries: {a} + {d} = {ans}.',
                    f'أثر المصفوفة هو مجموع عناصر القطر الرئيسي = {ans}.')

    if k == 82:
        ans = a * d - b * c
        return item('matrix-determinant-2x2-int', 'Matrices and Determinants',
                    f'Calculate the determinant \\( \\det \\begin{{pmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{pmatrix}} \\).',
                    f'احسب محدد المصفوفة \\( \\begin{{pmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{pmatrix}} \\).',
                    ans, f'\\( \\det(A) = ({a})({d}) - ({b})({c}) = {ans} \\).',
                    f'المحدد = {ans}.')

    if k == 83:
        ans = a**2 + b**2
        return item('complex-number-modulus-squared', 'Complex Numbers',
                    f'If \\( z = {a} + {b}i \\), find \\( |z|^2 \\).',
                    f'إذا كان \\( z = {a} + {b}i \\)، فأوجد \\( |z|^2 \\).',
                    ans, f'\\( |z|^2 = {a}^2 + {b}^2 = {ans} \\).',
                    f'مربع المعيار = {ans}.')

    if k == 84:
        ans = a**2 - b**2
        return item('complex-square-real-part', 'Complex Numbers',
                    f'Find the real part \\( \\operatorname{{Re}}(z^2) \\) for \\( z = {a} + {b}i \\).',
                    f'أوجد الجزء الحقيقي \\( \\operatorname{{Re}}(z^2) \\) للعدد المركب \\( z = {a} + {b}i \\).',
                    ans, f'\\( z^2 = ({a}^2 - {b}^2) + 2({a})({b})i \\), so \\( \\operatorname{{Re}}(z^2) = {ans} \\).',
                    f'الجزء الحقيقي = {ans}.')

    if k == 85:
        first = a
        diff = d
        n_term = 10
        ans = first + (n_term - 1) * diff
        return item('arithmetic-progression-nth-term', 'Sequences and Series',
                    f'In an arithmetic sequence with first term {first} and common difference {diff}, find the {n_term}th term.',
                    f'في متتالية حسابية حدها الأول {first} وأساسها {diff}، أوجد الحد العاشر.',
                    ans, f'\\( a_{{10}} = {first} + 9 \\times {diff} = {ans} \\).',
                    f'الحد العاشر = {ans}.')

    if k == 86:
        r_den = c + 2
        ans = F(a * r_den, r_den - 1)
        return item('infinite-geometric-series-sum-fraction', 'Sequences and Series',
                    f'Find the sum of the infinite geometric series with first term {a} and common ratio \\( \\frac{{1}}{{{r_den}}} \\).',
                    f'أوجد مجموع المتسلسلة الهندسية اللانهائية حدها الأول {a} وأساسها \\( \\frac{{1}}{{{r_den}}} \\).',
                    ans, f'\\( S = \\frac{{a}}{{1 - r}} = \\frac{{{a}}}{{1 - 1/{r_den}}} = {val(ans)} \\).',
                    f'المجموع = {val(ans)}.')

    if k == 87:
        val1 = (n * 13 + 614) % 31 + 2
        val2 = (n * 17 + 960) % 37 + 2
        val_k = (n * 3 + 87) % 15 + 6
        x_eval = (n + 87) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 87) % 5
            n_p = 1 + (n * 3 + 87) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-87', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 88:
        val1 = (n * 13 + 621) % 31 + 2
        val2 = (n * 17 + 971) % 37 + 2
        val_k = (n * 3 + 88) % 15 + 6
        x_eval = (n + 88) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 88) % 5
            n_p = 1 + (n * 3 + 88) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-88', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 89:
        val1 = (n * 13 + 628) % 31 + 2
        val2 = (n * 17 + 982) % 37 + 2
        val_k = (n * 3 + 89) % 15 + 6
        x_eval = (n + 89) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 89) % 5
            n_p = 1 + (n * 3 + 89) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-89', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 90:
        val1 = (n * 13 + 635) % 31 + 2
        val2 = (n * 17 + 993) % 37 + 2
        val_k = (n * 3 + 90) % 15 + 6
        x_eval = (n + 90) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 90) % 5
            n_p = 1 + (n * 3 + 90) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-90', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 91:
        val1 = (n * 13 + 642) % 31 + 2
        val2 = (n * 17 + 1004) % 37 + 2
        val_k = (n * 3 + 91) % 15 + 6
        x_eval = (n + 91) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 91) % 5
            n_p = 1 + (n * 3 + 91) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-91', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 92:
        val1 = (n * 13 + 649) % 31 + 2
        val2 = (n * 17 + 1015) % 37 + 2
        val_k = (n * 3 + 92) % 15 + 6
        x_eval = (n + 92) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 92) % 5
            n_p = 1 + (n * 3 + 92) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-92', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 93:
        val1 = (n * 13 + 656) % 31 + 2
        val2 = (n * 17 + 1026) % 37 + 2
        val_k = (n * 3 + 93) % 15 + 6
        x_eval = (n + 93) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 93) % 5
            n_p = 1 + (n * 3 + 93) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-93', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 94:
        val1 = (n * 13 + 663) % 31 + 2
        val2 = (n * 17 + 1037) % 37 + 2
        val_k = (n * 3 + 94) % 15 + 6
        x_eval = (n + 94) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 94) % 5
            n_p = 1 + (n * 3 + 94) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-94', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 95:
        val1 = (n * 13 + 670) % 31 + 2
        val2 = (n * 17 + 1048) % 37 + 2
        val_k = (n * 3 + 95) % 15 + 6
        x_eval = (n + 95) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 95) % 5
            n_p = 1 + (n * 3 + 95) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-95', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 96:
        val1 = (n * 13 + 677) % 31 + 2
        val2 = (n * 17 + 1059) % 37 + 2
        val_k = (n * 3 + 96) % 15 + 6
        x_eval = (n + 96) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 96) % 5
            n_p = 1 + (n * 3 + 96) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-96', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 97:
        val1 = (n * 13 + 684) % 31 + 2
        val2 = (n * 17 + 1070) % 37 + 2
        val_k = (n * 3 + 97) % 15 + 6
        x_eval = (n + 97) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 97) % 5
            n_p = 1 + (n * 3 + 97) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-97', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 98:
        val1 = (n * 13 + 691) % 31 + 2
        val2 = (n * 17 + 1081) % 37 + 2
        val_k = (n * 3 + 98) % 15 + 6
        x_eval = (n + 98) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 98) % 5
            n_p = 1 + (n * 3 + 98) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-98', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 99:
        val1 = (n * 13 + 698) % 31 + 2
        val2 = (n * 17 + 1092) % 37 + 2
        val_k = (n * 3 + 99) % 15 + 6
        x_eval = (n + 99) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 99) % 5
            n_p = 1 + (n * 3 + 99) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-99', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 100:
        val1 = (n * 13 + 705) % 31 + 2
        val2 = (n * 17 + 1103) % 37 + 2
        val_k = (n * 3 + 100) % 15 + 6
        x_eval = (n + 100) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 100) % 5
            n_p = 1 + (n * 3 + 100) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-100', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 101:
        val1 = (n * 13 + 712) % 31 + 2
        val2 = (n * 17 + 1114) % 37 + 2
        val_k = (n * 3 + 101) % 15 + 6
        x_eval = (n + 101) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 101) % 5
            n_p = 1 + (n * 3 + 101) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-101', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 102:
        val1 = (n * 13 + 719) % 31 + 2
        val2 = (n * 17 + 1125) % 37 + 2
        val_k = (n * 3 + 102) % 15 + 6
        x_eval = (n + 102) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 102) % 5
            n_p = 1 + (n * 3 + 102) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-102', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 103:
        val1 = (n * 13 + 726) % 31 + 2
        val2 = (n * 17 + 1136) % 37 + 2
        val_k = (n * 3 + 103) % 15 + 6
        x_eval = (n + 103) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 103) % 5
            n_p = 1 + (n * 3 + 103) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-103', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 104:
        val1 = (n * 13 + 733) % 31 + 2
        val2 = (n * 17 + 1147) % 37 + 2
        val_k = (n * 3 + 104) % 15 + 6
        x_eval = (n + 104) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 104) % 5
            n_p = 1 + (n * 3 + 104) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-104', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 105:
        val1 = (n * 13 + 740) % 31 + 2
        val2 = (n * 17 + 1158) % 37 + 2
        val_k = (n * 3 + 105) % 15 + 6
        x_eval = (n + 105) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 105) % 5
            n_p = 1 + (n * 3 + 105) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-105', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 106:
        val1 = (n * 13 + 747) % 31 + 2
        val2 = (n * 17 + 1169) % 37 + 2
        val_k = (n * 3 + 106) % 15 + 6
        x_eval = (n + 106) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 106) % 5
            n_p = 1 + (n * 3 + 106) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-106', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 107:
        val1 = (n * 13 + 754) % 31 + 2
        val2 = (n * 17 + 1180) % 37 + 2
        val_k = (n * 3 + 107) % 15 + 6
        x_eval = (n + 107) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 107) % 5
            n_p = 1 + (n * 3 + 107) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-107', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 108:
        val1 = (n * 13 + 761) % 31 + 2
        val2 = (n * 17 + 1191) % 37 + 2
        val_k = (n * 3 + 108) % 15 + 6
        x_eval = (n + 108) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 108) % 5
            n_p = 1 + (n * 3 + 108) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-108', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 109:
        val1 = (n * 13 + 768) % 31 + 2
        val2 = (n * 17 + 1202) % 37 + 2
        val_k = (n * 3 + 109) % 15 + 6
        x_eval = (n + 109) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 109) % 5
            n_p = 1 + (n * 3 + 109) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-109', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 110:
        val1 = (n * 13 + 775) % 31 + 2
        val2 = (n * 17 + 1213) % 37 + 2
        val_k = (n * 3 + 110) % 15 + 6
        x_eval = (n + 110) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 110) % 5
            n_p = 1 + (n * 3 + 110) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-110', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 111:
        val1 = (n * 13 + 782) % 31 + 2
        val2 = (n * 17 + 1224) % 37 + 2
        val_k = (n * 3 + 111) % 15 + 6
        x_eval = (n + 111) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 111) % 5
            n_p = 1 + (n * 3 + 111) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-111', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 112:
        val1 = (n * 13 + 789) % 31 + 2
        val2 = (n * 17 + 1235) % 37 + 2
        val_k = (n * 3 + 112) % 15 + 6
        x_eval = (n + 112) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 112) % 5
            n_p = 1 + (n * 3 + 112) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-112', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 113:
        val1 = (n * 13 + 796) % 31 + 2
        val2 = (n * 17 + 1246) % 37 + 2
        val_k = (n * 3 + 113) % 15 + 6
        x_eval = (n + 113) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 113) % 5
            n_p = 1 + (n * 3 + 113) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-113', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 114:
        val1 = (n * 13 + 803) % 31 + 2
        val2 = (n * 17 + 1257) % 37 + 2
        val_k = (n * 3 + 114) % 15 + 6
        x_eval = (n + 114) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 114) % 5
            n_p = 1 + (n * 3 + 114) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-114', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 115:
        val1 = (n * 13 + 810) % 31 + 2
        val2 = (n * 17 + 1268) % 37 + 2
        val_k = (n * 3 + 115) % 15 + 6
        x_eval = (n + 115) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 115) % 5
            n_p = 1 + (n * 3 + 115) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-115', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 116:
        val1 = (n * 13 + 817) % 31 + 2
        val2 = (n * 17 + 1279) % 37 + 2
        val_k = (n * 3 + 116) % 15 + 6
        x_eval = (n + 116) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 116) % 5
            n_p = 1 + (n * 3 + 116) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-116', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 117:
        val1 = (n * 13 + 824) % 31 + 2
        val2 = (n * 17 + 1290) % 37 + 2
        val_k = (n * 3 + 117) % 15 + 6
        x_eval = (n + 117) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 117) % 5
            n_p = 1 + (n * 3 + 117) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-117', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 118:
        val1 = (n * 13 + 831) % 31 + 2
        val2 = (n * 17 + 1301) % 37 + 2
        val_k = (n * 3 + 118) % 15 + 6
        x_eval = (n + 118) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 118) % 5
            n_p = 1 + (n * 3 + 118) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-118', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 119:
        val1 = (n * 13 + 838) % 31 + 2
        val2 = (n * 17 + 1312) % 37 + 2
        val_k = (n * 3 + 119) % 15 + 6
        x_eval = (n + 119) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 119) % 5
            n_p = 1 + (n * 3 + 119) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-119', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 120:
        val1 = (n * 13 + 845) % 31 + 2
        val2 = (n * 17 + 1323) % 37 + 2
        val_k = (n * 3 + 120) % 15 + 6
        x_eval = (n + 120) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 120) % 5
            n_p = 1 + (n * 3 + 120) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-120', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 121:
        val1 = (n * 13 + 852) % 31 + 2
        val2 = (n * 17 + 1334) % 37 + 2
        val_k = (n * 3 + 121) % 15 + 6
        x_eval = (n + 121) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 121) % 5
            n_p = 1 + (n * 3 + 121) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-121', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 122:
        val1 = (n * 13 + 859) % 31 + 2
        val2 = (n * 17 + 1345) % 37 + 2
        val_k = (n * 3 + 122) % 15 + 6
        x_eval = (n + 122) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 122) % 5
            n_p = 1 + (n * 3 + 122) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-122', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 123:
        val1 = (n * 13 + 866) % 31 + 2
        val2 = (n * 17 + 1356) % 37 + 2
        val_k = (n * 3 + 123) % 15 + 6
        x_eval = (n + 123) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 123) % 5
            n_p = 1 + (n * 3 + 123) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-123', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 124:
        val1 = (n * 13 + 873) % 31 + 2
        val2 = (n * 17 + 1367) % 37 + 2
        val_k = (n * 3 + 124) % 15 + 6
        x_eval = (n + 124) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 124) % 5
            n_p = 1 + (n * 3 + 124) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-124', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 125:
        val1 = (n * 13 + 880) % 31 + 2
        val2 = (n * 17 + 1378) % 37 + 2
        val_k = (n * 3 + 125) % 15 + 6
        x_eval = (n + 125) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 125) % 5
            n_p = 1 + (n * 3 + 125) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-125', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 126:
        val1 = (n * 13 + 887) % 31 + 2
        val2 = (n * 17 + 1389) % 37 + 2
        val_k = (n * 3 + 126) % 15 + 6
        x_eval = (n + 126) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 126) % 5
            n_p = 1 + (n * 3 + 126) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-126', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 127:
        val1 = (n * 13 + 894) % 31 + 2
        val2 = (n * 17 + 1400) % 37 + 2
        val_k = (n * 3 + 127) % 15 + 6
        x_eval = (n + 127) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 127) % 5
            n_p = 1 + (n * 3 + 127) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-127', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 128:
        val1 = (n * 13 + 901) % 31 + 2
        val2 = (n * 17 + 1411) % 37 + 2
        val_k = (n * 3 + 128) % 15 + 6
        x_eval = (n + 128) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 128) % 5
            n_p = 1 + (n * 3 + 128) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-128', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 129:
        val1 = (n * 13 + 908) % 31 + 2
        val2 = (n * 17 + 1422) % 37 + 2
        val_k = (n * 3 + 129) % 15 + 6
        x_eval = (n + 129) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 129) % 5
            n_p = 1 + (n * 3 + 129) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-129', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 130:
        val1 = (n * 13 + 915) % 31 + 2
        val2 = (n * 17 + 1433) % 37 + 2
        val_k = (n * 3 + 130) % 15 + 6
        x_eval = (n + 130) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 130) % 5
            n_p = 1 + (n * 3 + 130) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-130', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 131:
        val1 = (n * 13 + 922) % 31 + 2
        val2 = (n * 17 + 1444) % 37 + 2
        val_k = (n * 3 + 131) % 15 + 6
        x_eval = (n + 131) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 131) % 5
            n_p = 1 + (n * 3 + 131) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-131', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 132:
        val1 = (n * 13 + 929) % 31 + 2
        val2 = (n * 17 + 1455) % 37 + 2
        val_k = (n * 3 + 132) % 15 + 6
        x_eval = (n + 132) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 132) % 5
            n_p = 1 + (n * 3 + 132) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-132', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 133:
        val1 = (n * 13 + 936) % 31 + 2
        val2 = (n * 17 + 1466) % 37 + 2
        val_k = (n * 3 + 133) % 15 + 6
        x_eval = (n + 133) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 133) % 5
            n_p = 1 + (n * 3 + 133) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-133', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 134:
        val1 = (n * 13 + 943) % 31 + 2
        val2 = (n * 17 + 1477) % 37 + 2
        val_k = (n * 3 + 134) % 15 + 6
        x_eval = (n + 134) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 134) % 5
            n_p = 1 + (n * 3 + 134) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-134', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 135:
        val1 = (n * 13 + 950) % 31 + 2
        val2 = (n * 17 + 1488) % 37 + 2
        val_k = (n * 3 + 135) % 15 + 6
        x_eval = (n + 135) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 135) % 5
            n_p = 1 + (n * 3 + 135) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-135', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 136:
        val1 = (n * 13 + 957) % 31 + 2
        val2 = (n * 17 + 1499) % 37 + 2
        val_k = (n * 3 + 136) % 15 + 6
        x_eval = (n + 136) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 136) % 5
            n_p = 1 + (n * 3 + 136) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-136', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 137:
        val1 = (n * 13 + 964) % 31 + 2
        val2 = (n * 17 + 1510) % 37 + 2
        val_k = (n * 3 + 137) % 15 + 6
        x_eval = (n + 137) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 137) % 5
            n_p = 1 + (n * 3 + 137) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-137', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 138:
        val1 = (n * 13 + 971) % 31 + 2
        val2 = (n * 17 + 1521) % 37 + 2
        val_k = (n * 3 + 138) % 15 + 6
        x_eval = (n + 138) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 138) % 5
            n_p = 1 + (n * 3 + 138) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-138', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 139:
        val1 = (n * 13 + 978) % 31 + 2
        val2 = (n * 17 + 1532) % 37 + 2
        val_k = (n * 3 + 139) % 15 + 6
        x_eval = (n + 139) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 139) % 5
            n_p = 1 + (n * 3 + 139) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-139', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 140:
        val1 = (n * 13 + 985) % 31 + 2
        val2 = (n * 17 + 1543) % 37 + 2
        val_k = (n * 3 + 140) % 15 + 6
        x_eval = (n + 140) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 140) % 5
            n_p = 1 + (n * 3 + 140) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-140', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 141:
        val1 = (n * 13 + 992) % 31 + 2
        val2 = (n * 17 + 1554) % 37 + 2
        val_k = (n * 3 + 141) % 15 + 6
        x_eval = (n + 141) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 141) % 5
            n_p = 1 + (n * 3 + 141) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-141', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 142:
        val1 = (n * 13 + 999) % 31 + 2
        val2 = (n * 17 + 1565) % 37 + 2
        val_k = (n * 3 + 142) % 15 + 6
        x_eval = (n + 142) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 142) % 5
            n_p = 1 + (n * 3 + 142) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-142', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 143:
        val1 = (n * 13 + 1006) % 31 + 2
        val2 = (n * 17 + 1576) % 37 + 2
        val_k = (n * 3 + 143) % 15 + 6
        x_eval = (n + 143) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 143) % 5
            n_p = 1 + (n * 3 + 143) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-143', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 144:
        val1 = (n * 13 + 1013) % 31 + 2
        val2 = (n * 17 + 1587) % 37 + 2
        val_k = (n * 3 + 144) % 15 + 6
        x_eval = (n + 144) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 144) % 5
            n_p = 1 + (n * 3 + 144) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-144', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 145:
        val1 = (n * 13 + 1020) % 31 + 2
        val2 = (n * 17 + 1598) % 37 + 2
        val_k = (n * 3 + 145) % 15 + 6
        x_eval = (n + 145) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 145) % 5
            n_p = 1 + (n * 3 + 145) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-145', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 146:
        val1 = (n * 13 + 1027) % 31 + 2
        val2 = (n * 17 + 1609) % 37 + 2
        val_k = (n * 3 + 146) % 15 + 6
        x_eval = (n + 146) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 146) % 5
            n_p = 1 + (n * 3 + 146) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-146', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 147:
        val1 = (n * 13 + 1034) % 31 + 2
        val2 = (n * 17 + 1620) % 37 + 2
        val_k = (n * 3 + 147) % 15 + 6
        x_eval = (n + 147) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 147) % 5
            n_p = 1 + (n * 3 + 147) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-147', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 148:
        val1 = (n * 13 + 1041) % 31 + 2
        val2 = (n * 17 + 1631) % 37 + 2
        val_k = (n * 3 + 148) % 15 + 6
        x_eval = (n + 148) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 148) % 5
            n_p = 1 + (n * 3 + 148) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-148', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 149:
        val1 = (n * 13 + 1048) % 31 + 2
        val2 = (n * 17 + 1642) % 37 + 2
        val_k = (n * 3 + 149) % 15 + 6
        x_eval = (n + 149) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 149) % 5
            n_p = 1 + (n * 3 + 149) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-149', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 150:
        val1 = (n * 13 + 1055) % 31 + 2
        val2 = (n * 17 + 1653) % 37 + 2
        val_k = (n * 3 + 150) % 15 + 6
        x_eval = (n + 150) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 150) % 5
            n_p = 1 + (n * 3 + 150) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-150', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 151:
        val1 = (n * 13 + 1062) % 31 + 2
        val2 = (n * 17 + 1664) % 37 + 2
        val_k = (n * 3 + 151) % 15 + 6
        x_eval = (n + 151) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 151) % 5
            n_p = 1 + (n * 3 + 151) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-151', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 152:
        val1 = (n * 13 + 1069) % 31 + 2
        val2 = (n * 17 + 1675) % 37 + 2
        val_k = (n * 3 + 152) % 15 + 6
        x_eval = (n + 152) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 152) % 5
            n_p = 1 + (n * 3 + 152) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-152', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 153:
        val1 = (n * 13 + 1076) % 31 + 2
        val2 = (n * 17 + 1686) % 37 + 2
        val_k = (n * 3 + 153) % 15 + 6
        x_eval = (n + 153) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 153) % 5
            n_p = 1 + (n * 3 + 153) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-153', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 154:
        val1 = (n * 13 + 1083) % 31 + 2
        val2 = (n * 17 + 1697) % 37 + 2
        val_k = (n * 3 + 154) % 15 + 6
        x_eval = (n + 154) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 154) % 5
            n_p = 1 + (n * 3 + 154) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-154', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 155:
        val1 = (n * 13 + 1090) % 31 + 2
        val2 = (n * 17 + 1708) % 37 + 2
        val_k = (n * 3 + 155) % 15 + 6
        x_eval = (n + 155) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 155) % 5
            n_p = 1 + (n * 3 + 155) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-155', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 156:
        val1 = (n * 13 + 1097) % 31 + 2
        val2 = (n * 17 + 1719) % 37 + 2
        val_k = (n * 3 + 156) % 15 + 6
        x_eval = (n + 156) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 156) % 5
            n_p = 1 + (n * 3 + 156) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-156', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 157:
        val1 = (n * 13 + 1104) % 31 + 2
        val2 = (n * 17 + 1730) % 37 + 2
        val_k = (n * 3 + 157) % 15 + 6
        x_eval = (n + 157) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 157) % 5
            n_p = 1 + (n * 3 + 157) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-157', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 158:
        val1 = (n * 13 + 1111) % 31 + 2
        val2 = (n * 17 + 1741) % 37 + 2
        val_k = (n * 3 + 158) % 15 + 6
        x_eval = (n + 158) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 158) % 5
            n_p = 1 + (n * 3 + 158) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-158', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 159:
        val1 = (n * 13 + 1118) % 31 + 2
        val2 = (n * 17 + 1752) % 37 + 2
        val_k = (n * 3 + 159) % 15 + 6
        x_eval = (n + 159) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 159) % 5
            n_p = 1 + (n * 3 + 159) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-159', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 160:
        val1 = (n * 13 + 1125) % 31 + 2
        val2 = (n * 17 + 1763) % 37 + 2
        val_k = (n * 3 + 160) % 15 + 6
        x_eval = (n + 160) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 160) % 5
            n_p = 1 + (n * 3 + 160) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-160', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 161:
        val1 = (n * 13 + 1132) % 31 + 2
        val2 = (n * 17 + 1774) % 37 + 2
        val_k = (n * 3 + 161) % 15 + 6
        x_eval = (n + 161) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 161) % 5
            n_p = 1 + (n * 3 + 161) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-161', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 162:
        val1 = (n * 13 + 1139) % 31 + 2
        val2 = (n * 17 + 1785) % 37 + 2
        val_k = (n * 3 + 162) % 15 + 6
        x_eval = (n + 162) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 162) % 5
            n_p = 1 + (n * 3 + 162) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-162', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 163:
        val1 = (n * 13 + 1146) % 31 + 2
        val2 = (n * 17 + 1796) % 37 + 2
        val_k = (n * 3 + 163) % 15 + 6
        x_eval = (n + 163) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 163) % 5
            n_p = 1 + (n * 3 + 163) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-163', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 164:
        val1 = (n * 13 + 1153) % 31 + 2
        val2 = (n * 17 + 1807) % 37 + 2
        val_k = (n * 3 + 164) % 15 + 6
        x_eval = (n + 164) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 164) % 5
            n_p = 1 + (n * 3 + 164) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-164', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 165:
        val1 = (n * 13 + 1160) % 31 + 2
        val2 = (n * 17 + 1818) % 37 + 2
        val_k = (n * 3 + 165) % 15 + 6
        x_eval = (n + 165) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 165) % 5
            n_p = 1 + (n * 3 + 165) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-165', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 166:
        val1 = (n * 13 + 1167) % 31 + 2
        val2 = (n * 17 + 1829) % 37 + 2
        val_k = (n * 3 + 166) % 15 + 6
        x_eval = (n + 166) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 166) % 5
            n_p = 1 + (n * 3 + 166) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-166', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 167:
        val1 = (n * 13 + 1174) % 31 + 2
        val2 = (n * 17 + 1840) % 37 + 2
        val_k = (n * 3 + 167) % 15 + 6
        x_eval = (n + 167) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 167) % 5
            n_p = 1 + (n * 3 + 167) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-167', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 168:
        val1 = (n * 13 + 1181) % 31 + 2
        val2 = (n * 17 + 1851) % 37 + 2
        val_k = (n * 3 + 168) % 15 + 6
        x_eval = (n + 168) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 168) % 5
            n_p = 1 + (n * 3 + 168) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-168', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 169:
        val1 = (n * 13 + 1188) % 31 + 2
        val2 = (n * 17 + 1862) % 37 + 2
        val_k = (n * 3 + 169) % 15 + 6
        x_eval = (n + 169) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 169) % 5
            n_p = 1 + (n * 3 + 169) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-169', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 170:
        val1 = (n * 13 + 1195) % 31 + 2
        val2 = (n * 17 + 1873) % 37 + 2
        val_k = (n * 3 + 170) % 15 + 6
        x_eval = (n + 170) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 170) % 5
            n_p = 1 + (n * 3 + 170) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-170', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 171:
        val1 = (n * 13 + 1202) % 31 + 2
        val2 = (n * 17 + 1884) % 37 + 2
        val_k = (n * 3 + 171) % 15 + 6
        x_eval = (n + 171) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 171) % 5
            n_p = 1 + (n * 3 + 171) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-171', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 172:
        val1 = (n * 13 + 1209) % 31 + 2
        val2 = (n * 17 + 1895) % 37 + 2
        val_k = (n * 3 + 172) % 15 + 6
        x_eval = (n + 172) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 172) % 5
            n_p = 1 + (n * 3 + 172) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-172', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 173:
        val1 = (n * 13 + 1216) % 31 + 2
        val2 = (n * 17 + 1906) % 37 + 2
        val_k = (n * 3 + 173) % 15 + 6
        x_eval = (n + 173) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 173) % 5
            n_p = 1 + (n * 3 + 173) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-173', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 174:
        val1 = (n * 13 + 1223) % 31 + 2
        val2 = (n * 17 + 1917) % 37 + 2
        val_k = (n * 3 + 174) % 15 + 6
        x_eval = (n + 174) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 174) % 5
            n_p = 1 + (n * 3 + 174) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-174', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 175:
        val1 = (n * 13 + 1230) % 31 + 2
        val2 = (n * 17 + 1928) % 37 + 2
        val_k = (n * 3 + 175) % 15 + 6
        x_eval = (n + 175) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 175) % 5
            n_p = 1 + (n * 3 + 175) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-175', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 176:
        val1 = (n * 13 + 1237) % 31 + 2
        val2 = (n * 17 + 1939) % 37 + 2
        val_k = (n * 3 + 176) % 15 + 6
        x_eval = (n + 176) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 176) % 5
            n_p = 1 + (n * 3 + 176) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-176', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 177:
        val1 = (n * 13 + 1244) % 31 + 2
        val2 = (n * 17 + 1950) % 37 + 2
        val_k = (n * 3 + 177) % 15 + 6
        x_eval = (n + 177) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 177) % 5
            n_p = 1 + (n * 3 + 177) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-177', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 178:
        val1 = (n * 13 + 1251) % 31 + 2
        val2 = (n * 17 + 1961) % 37 + 2
        val_k = (n * 3 + 178) % 15 + 6
        x_eval = (n + 178) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 178) % 5
            n_p = 1 + (n * 3 + 178) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-178', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 179:
        val1 = (n * 13 + 1258) % 31 + 2
        val2 = (n * 17 + 1972) % 37 + 2
        val_k = (n * 3 + 179) % 15 + 6
        x_eval = (n + 179) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 179) % 5
            n_p = 1 + (n * 3 + 179) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-179', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 180:
        val1 = (n * 13 + 1265) % 31 + 2
        val2 = (n * 17 + 1983) % 37 + 2
        val_k = (n * 3 + 180) % 15 + 6
        x_eval = (n + 180) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 180) % 5
            n_p = 1 + (n * 3 + 180) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-180', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 181:
        val1 = (n * 13 + 1272) % 31 + 2
        val2 = (n * 17 + 1994) % 37 + 2
        val_k = (n * 3 + 181) % 15 + 6
        x_eval = (n + 181) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 181) % 5
            n_p = 1 + (n * 3 + 181) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-181', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 182:
        val1 = (n * 13 + 1279) % 31 + 2
        val2 = (n * 17 + 2005) % 37 + 2
        val_k = (n * 3 + 182) % 15 + 6
        x_eval = (n + 182) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 182) % 5
            n_p = 1 + (n * 3 + 182) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-182', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 183:
        val1 = (n * 13 + 1286) % 31 + 2
        val2 = (n * 17 + 2016) % 37 + 2
        val_k = (n * 3 + 183) % 15 + 6
        x_eval = (n + 183) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 183) % 5
            n_p = 1 + (n * 3 + 183) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-183', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 184:
        val1 = (n * 13 + 1293) % 31 + 2
        val2 = (n * 17 + 2027) % 37 + 2
        val_k = (n * 3 + 184) % 15 + 6
        x_eval = (n + 184) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 184) % 5
            n_p = 1 + (n * 3 + 184) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-184', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 185:
        val1 = (n * 13 + 1300) % 31 + 2
        val2 = (n * 17 + 2038) % 37 + 2
        val_k = (n * 3 + 185) % 15 + 6
        x_eval = (n + 185) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 185) % 5
            n_p = 1 + (n * 3 + 185) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-185', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 186:
        val1 = (n * 13 + 1307) % 31 + 2
        val2 = (n * 17 + 2049) % 37 + 2
        val_k = (n * 3 + 186) % 15 + 6
        x_eval = (n + 186) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 186) % 5
            n_p = 1 + (n * 3 + 186) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-186', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 187:
        val1 = (n * 13 + 1314) % 31 + 2
        val2 = (n * 17 + 2060) % 37 + 2
        val_k = (n * 3 + 187) % 15 + 6
        x_eval = (n + 187) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 187) % 5
            n_p = 1 + (n * 3 + 187) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-187', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 188:
        val1 = (n * 13 + 1321) % 31 + 2
        val2 = (n * 17 + 2071) % 37 + 2
        val_k = (n * 3 + 188) % 15 + 6
        x_eval = (n + 188) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 188) % 5
            n_p = 1 + (n * 3 + 188) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-188', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 189:
        val1 = (n * 13 + 1328) % 31 + 2
        val2 = (n * 17 + 2082) % 37 + 2
        val_k = (n * 3 + 189) % 15 + 6
        x_eval = (n + 189) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 189) % 5
            n_p = 1 + (n * 3 + 189) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-189', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 190:
        val1 = (n * 13 + 1335) % 31 + 2
        val2 = (n * 17 + 2093) % 37 + 2
        val_k = (n * 3 + 190) % 15 + 6
        x_eval = (n + 190) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 190) % 5
            n_p = 1 + (n * 3 + 190) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-190', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 191:
        val1 = (n * 13 + 1342) % 31 + 2
        val2 = (n * 17 + 2104) % 37 + 2
        val_k = (n * 3 + 191) % 15 + 6
        x_eval = (n + 191) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 191) % 5
            n_p = 1 + (n * 3 + 191) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-191', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 192:
        val1 = (n * 13 + 1349) % 31 + 2
        val2 = (n * 17 + 2115) % 37 + 2
        val_k = (n * 3 + 192) % 15 + 6
        x_eval = (n + 192) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 192) % 5
            n_p = 1 + (n * 3 + 192) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-192', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 193:
        val1 = (n * 13 + 1356) % 31 + 2
        val2 = (n * 17 + 2126) % 37 + 2
        val_k = (n * 3 + 193) % 15 + 6
        x_eval = (n + 193) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 193) % 5
            n_p = 1 + (n * 3 + 193) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-193', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 194:
        val1 = (n * 13 + 1363) % 31 + 2
        val2 = (n * 17 + 2137) % 37 + 2
        val_k = (n * 3 + 194) % 15 + 6
        x_eval = (n + 194) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 194) % 5
            n_p = 1 + (n * 3 + 194) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-194', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 195:
        val1 = (n * 13 + 1370) % 31 + 2
        val2 = (n * 17 + 2148) % 37 + 2
        val_k = (n * 3 + 195) % 15 + 6
        x_eval = (n + 195) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 195) % 5
            n_p = 1 + (n * 3 + 195) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-195', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 196:
        val1 = (n * 13 + 1377) % 31 + 2
        val2 = (n * 17 + 2159) % 37 + 2
        val_k = (n * 3 + 196) % 15 + 6
        x_eval = (n + 196) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 196) % 5
            n_p = 1 + (n * 3 + 196) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-196', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 197:
        val1 = (n * 13 + 1384) % 31 + 2
        val2 = (n * 17 + 2170) % 37 + 2
        val_k = (n * 3 + 197) % 15 + 6
        x_eval = (n + 197) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 197) % 5
            n_p = 1 + (n * 3 + 197) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-197', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 198:
        val1 = (n * 13 + 1391) % 31 + 2
        val2 = (n * 17 + 2181) % 37 + 2
        val_k = (n * 3 + 198) % 15 + 6
        x_eval = (n + 198) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 198) % 5
            n_p = 1 + (n * 3 + 198) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-198', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 199:
        val1 = (n * 13 + 1398) % 31 + 2
        val2 = (n * 17 + 2192) % 37 + 2
        val_k = (n * 3 + 199) % 15 + 6
        x_eval = (n + 199) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 199) % 5
            n_p = 1 + (n * 3 + 199) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-199', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 200:
        val1 = (n * 13 + 1405) % 31 + 2
        val2 = (n * 17 + 2203) % 37 + 2
        val_k = (n * 3 + 200) % 15 + 6
        x_eval = (n + 200) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 200) % 5
            n_p = 1 + (n * 3 + 200) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-200', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 201:
        val1 = (n * 13 + 1412) % 31 + 2
        val2 = (n * 17 + 2214) % 37 + 2
        val_k = (n * 3 + 201) % 15 + 6
        x_eval = (n + 201) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 201) % 5
            n_p = 1 + (n * 3 + 201) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-201', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 202:
        val1 = (n * 13 + 1419) % 31 + 2
        val2 = (n * 17 + 2225) % 37 + 2
        val_k = (n * 3 + 202) % 15 + 6
        x_eval = (n + 202) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 202) % 5
            n_p = 1 + (n * 3 + 202) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-202', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 203:
        val1 = (n * 13 + 1426) % 31 + 2
        val2 = (n * 17 + 2236) % 37 + 2
        val_k = (n * 3 + 203) % 15 + 6
        x_eval = (n + 203) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 203) % 5
            n_p = 1 + (n * 3 + 203) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-203', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 204:
        val1 = (n * 13 + 1433) % 31 + 2
        val2 = (n * 17 + 2247) % 37 + 2
        val_k = (n * 3 + 204) % 15 + 6
        x_eval = (n + 204) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 204) % 5
            n_p = 1 + (n * 3 + 204) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-204', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 205:
        val1 = (n * 13 + 1440) % 31 + 2
        val2 = (n * 17 + 2258) % 37 + 2
        val_k = (n * 3 + 205) % 15 + 6
        x_eval = (n + 205) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 205) % 5
            n_p = 1 + (n * 3 + 205) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-205', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 206:
        val1 = (n * 13 + 1447) % 31 + 2
        val2 = (n * 17 + 2269) % 37 + 2
        val_k = (n * 3 + 206) % 15 + 6
        x_eval = (n + 206) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 206) % 5
            n_p = 1 + (n * 3 + 206) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-206', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 207:
        val1 = (n * 13 + 1454) % 31 + 2
        val2 = (n * 17 + 2280) % 37 + 2
        val_k = (n * 3 + 207) % 15 + 6
        x_eval = (n + 207) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 207) % 5
            n_p = 1 + (n * 3 + 207) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-207', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 208:
        val1 = (n * 13 + 1461) % 31 + 2
        val2 = (n * 17 + 2291) % 37 + 2
        val_k = (n * 3 + 208) % 15 + 6
        x_eval = (n + 208) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 208) % 5
            n_p = 1 + (n * 3 + 208) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-208', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 209:
        val1 = (n * 13 + 1468) % 31 + 2
        val2 = (n * 17 + 2302) % 37 + 2
        val_k = (n * 3 + 209) % 15 + 6
        x_eval = (n + 209) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 209) % 5
            n_p = 1 + (n * 3 + 209) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-209', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 210:
        val1 = (n * 13 + 1475) % 31 + 2
        val2 = (n * 17 + 2313) % 37 + 2
        val_k = (n * 3 + 210) % 15 + 6
        x_eval = (n + 210) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 210) % 5
            n_p = 1 + (n * 3 + 210) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-210', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 211:
        val1 = (n * 13 + 1482) % 31 + 2
        val2 = (n * 17 + 2324) % 37 + 2
        val_k = (n * 3 + 211) % 15 + 6
        x_eval = (n + 211) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 211) % 5
            n_p = 1 + (n * 3 + 211) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-211', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 212:
        val1 = (n * 13 + 1489) % 31 + 2
        val2 = (n * 17 + 2335) % 37 + 2
        val_k = (n * 3 + 212) % 15 + 6
        x_eval = (n + 212) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 212) % 5
            n_p = 1 + (n * 3 + 212) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-212', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 213:
        val1 = (n * 13 + 1496) % 31 + 2
        val2 = (n * 17 + 2346) % 37 + 2
        val_k = (n * 3 + 213) % 15 + 6
        x_eval = (n + 213) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 213) % 5
            n_p = 1 + (n * 3 + 213) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-213', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 214:
        val1 = (n * 13 + 1503) % 31 + 2
        val2 = (n * 17 + 2357) % 37 + 2
        val_k = (n * 3 + 214) % 15 + 6
        x_eval = (n + 214) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 214) % 5
            n_p = 1 + (n * 3 + 214) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-214', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 215:
        val1 = (n * 13 + 1510) % 31 + 2
        val2 = (n * 17 + 2368) % 37 + 2
        val_k = (n * 3 + 215) % 15 + 6
        x_eval = (n + 215) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 215) % 5
            n_p = 1 + (n * 3 + 215) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-215', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 216:
        val1 = (n * 13 + 1517) % 31 + 2
        val2 = (n * 17 + 2379) % 37 + 2
        val_k = (n * 3 + 216) % 15 + 6
        x_eval = (n + 216) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 216) % 5
            n_p = 1 + (n * 3 + 216) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-216', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 217:
        val1 = (n * 13 + 1524) % 31 + 2
        val2 = (n * 17 + 2390) % 37 + 2
        val_k = (n * 3 + 217) % 15 + 6
        x_eval = (n + 217) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 217) % 5
            n_p = 1 + (n * 3 + 217) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-217', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 218:
        val1 = (n * 13 + 1531) % 31 + 2
        val2 = (n * 17 + 2401) % 37 + 2
        val_k = (n * 3 + 218) % 15 + 6
        x_eval = (n + 218) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 218) % 5
            n_p = 1 + (n * 3 + 218) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-218', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 219:
        val1 = (n * 13 + 1538) % 31 + 2
        val2 = (n * 17 + 2412) % 37 + 2
        val_k = (n * 3 + 219) % 15 + 6
        x_eval = (n + 219) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 219) % 5
            n_p = 1 + (n * 3 + 219) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-219', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 220:
        val1 = (n * 13 + 1545) % 31 + 2
        val2 = (n * 17 + 2423) % 37 + 2
        val_k = (n * 3 + 220) % 15 + 6
        x_eval = (n + 220) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 220) % 5
            n_p = 1 + (n * 3 + 220) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-220', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 221:
        val1 = (n * 13 + 1552) % 31 + 2
        val2 = (n * 17 + 2434) % 37 + 2
        val_k = (n * 3 + 221) % 15 + 6
        x_eval = (n + 221) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 221) % 5
            n_p = 1 + (n * 3 + 221) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-221', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 222:
        val1 = (n * 13 + 1559) % 31 + 2
        val2 = (n * 17 + 2445) % 37 + 2
        val_k = (n * 3 + 222) % 15 + 6
        x_eval = (n + 222) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 222) % 5
            n_p = 1 + (n * 3 + 222) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-222', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 223:
        val1 = (n * 13 + 1566) % 31 + 2
        val2 = (n * 17 + 2456) % 37 + 2
        val_k = (n * 3 + 223) % 15 + 6
        x_eval = (n + 223) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 223) % 5
            n_p = 1 + (n * 3 + 223) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-223', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 224:
        val1 = (n * 13 + 1573) % 31 + 2
        val2 = (n * 17 + 2467) % 37 + 2
        val_k = (n * 3 + 224) % 15 + 6
        x_eval = (n + 224) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 224) % 5
            n_p = 1 + (n * 3 + 224) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-224', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 225:
        val1 = (n * 13 + 1580) % 31 + 2
        val2 = (n * 17 + 2478) % 37 + 2
        val_k = (n * 3 + 225) % 15 + 6
        x_eval = (n + 225) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 225) % 5
            n_p = 1 + (n * 3 + 225) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-225', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 226:
        val1 = (n * 13 + 1587) % 31 + 2
        val2 = (n * 17 + 2489) % 37 + 2
        val_k = (n * 3 + 226) % 15 + 6
        x_eval = (n + 226) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 226) % 5
            n_p = 1 + (n * 3 + 226) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-226', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 227:
        val1 = (n * 13 + 1594) % 31 + 2
        val2 = (n * 17 + 2500) % 37 + 2
        val_k = (n * 3 + 227) % 15 + 6
        x_eval = (n + 227) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 227) % 5
            n_p = 1 + (n * 3 + 227) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-227', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 228:
        val1 = (n * 13 + 1601) % 31 + 2
        val2 = (n * 17 + 2511) % 37 + 2
        val_k = (n * 3 + 228) % 15 + 6
        x_eval = (n + 228) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 228) % 5
            n_p = 1 + (n * 3 + 228) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-228', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 229:
        val1 = (n * 13 + 1608) % 31 + 2
        val2 = (n * 17 + 2522) % 37 + 2
        val_k = (n * 3 + 229) % 15 + 6
        x_eval = (n + 229) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 229) % 5
            n_p = 1 + (n * 3 + 229) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-229', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 230:
        val1 = (n * 13 + 1615) % 31 + 2
        val2 = (n * 17 + 2533) % 37 + 2
        val_k = (n * 3 + 230) % 15 + 6
        x_eval = (n + 230) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 230) % 5
            n_p = 1 + (n * 3 + 230) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-230', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 231:
        val1 = (n * 13 + 1622) % 31 + 2
        val2 = (n * 17 + 2544) % 37 + 2
        val_k = (n * 3 + 231) % 15 + 6
        x_eval = (n + 231) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 231) % 5
            n_p = 1 + (n * 3 + 231) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-231', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 232:
        val1 = (n * 13 + 1629) % 31 + 2
        val2 = (n * 17 + 2555) % 37 + 2
        val_k = (n * 3 + 232) % 15 + 6
        x_eval = (n + 232) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 232) % 5
            n_p = 1 + (n * 3 + 232) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-232', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 233:
        val1 = (n * 13 + 1636) % 31 + 2
        val2 = (n * 17 + 2566) % 37 + 2
        val_k = (n * 3 + 233) % 15 + 6
        x_eval = (n + 233) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 233) % 5
            n_p = 1 + (n * 3 + 233) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-233', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 234:
        val1 = (n * 13 + 1643) % 31 + 2
        val2 = (n * 17 + 2577) % 37 + 2
        val_k = (n * 3 + 234) % 15 + 6
        x_eval = (n + 234) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 234) % 5
            n_p = 1 + (n * 3 + 234) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-234', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 235:
        val1 = (n * 13 + 1650) % 31 + 2
        val2 = (n * 17 + 2588) % 37 + 2
        val_k = (n * 3 + 235) % 15 + 6
        x_eval = (n + 235) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 235) % 5
            n_p = 1 + (n * 3 + 235) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-235', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 236:
        val1 = (n * 13 + 1657) % 31 + 2
        val2 = (n * 17 + 2599) % 37 + 2
        val_k = (n * 3 + 236) % 15 + 6
        x_eval = (n + 236) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 236) % 5
            n_p = 1 + (n * 3 + 236) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-236', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 237:
        val1 = (n * 13 + 1664) % 31 + 2
        val2 = (n * 17 + 2610) % 37 + 2
        val_k = (n * 3 + 237) % 15 + 6
        x_eval = (n + 237) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 237) % 5
            n_p = 1 + (n * 3 + 237) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-237', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 238:
        val1 = (n * 13 + 1671) % 31 + 2
        val2 = (n * 17 + 2621) % 37 + 2
        val_k = (n * 3 + 238) % 15 + 6
        x_eval = (n + 238) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 238) % 5
            n_p = 1 + (n * 3 + 238) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-238', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 239:
        val1 = (n * 13 + 1678) % 31 + 2
        val2 = (n * 17 + 2632) % 37 + 2
        val_k = (n * 3 + 239) % 15 + 6
        x_eval = (n + 239) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 239) % 5
            n_p = 1 + (n * 3 + 239) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-239', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 240:
        val1 = (n * 13 + 1685) % 31 + 2
        val2 = (n * 17 + 2643) % 37 + 2
        val_k = (n * 3 + 240) % 15 + 6
        x_eval = (n + 240) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 240) % 5
            n_p = 1 + (n * 3 + 240) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-240', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 241:
        val1 = (n * 13 + 1692) % 31 + 2
        val2 = (n * 17 + 2654) % 37 + 2
        val_k = (n * 3 + 241) % 15 + 6
        x_eval = (n + 241) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 241) % 5
            n_p = 1 + (n * 3 + 241) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-241', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 242:
        val1 = (n * 13 + 1699) % 31 + 2
        val2 = (n * 17 + 2665) % 37 + 2
        val_k = (n * 3 + 242) % 15 + 6
        x_eval = (n + 242) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 242) % 5
            n_p = 1 + (n * 3 + 242) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-242', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 243:
        val1 = (n * 13 + 1706) % 31 + 2
        val2 = (n * 17 + 2676) % 37 + 2
        val_k = (n * 3 + 243) % 15 + 6
        x_eval = (n + 243) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 243) % 5
            n_p = 1 + (n * 3 + 243) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-243', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 244:
        val1 = (n * 13 + 1713) % 31 + 2
        val2 = (n * 17 + 2687) % 37 + 2
        val_k = (n * 3 + 244) % 15 + 6
        x_eval = (n + 244) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 244) % 5
            n_p = 1 + (n * 3 + 244) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-244', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 245:
        val1 = (n * 13 + 1720) % 31 + 2
        val2 = (n * 17 + 2698) % 37 + 2
        val_k = (n * 3 + 245) % 15 + 6
        x_eval = (n + 245) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 245) % 5
            n_p = 1 + (n * 3 + 245) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-245', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 246:
        val1 = (n * 13 + 1727) % 31 + 2
        val2 = (n * 17 + 2709) % 37 + 2
        val_k = (n * 3 + 246) % 15 + 6
        x_eval = (n + 246) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 246) % 5
            n_p = 1 + (n * 3 + 246) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-246', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 247:
        val1 = (n * 13 + 1734) % 31 + 2
        val2 = (n * 17 + 2720) % 37 + 2
        val_k = (n * 3 + 247) % 15 + 6
        x_eval = (n + 247) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 247) % 5
            n_p = 1 + (n * 3 + 247) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-247', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 248:
        val1 = (n * 13 + 1741) % 31 + 2
        val2 = (n * 17 + 2731) % 37 + 2
        val_k = (n * 3 + 248) % 15 + 6
        x_eval = (n + 248) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 248) % 5
            n_p = 1 + (n * 3 + 248) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-248', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 249:
        val1 = (n * 13 + 1748) % 31 + 2
        val2 = (n * 17 + 2742) % 37 + 2
        val_k = (n * 3 + 249) % 15 + 6
        x_eval = (n + 249) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 249) % 5
            n_p = 1 + (n * 3 + 249) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-249', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 250:
        val1 = (n * 13 + 1755) % 31 + 2
        val2 = (n * 17 + 2753) % 37 + 2
        val_k = (n * 3 + 250) % 15 + 6
        x_eval = (n + 250) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 250) % 5
            n_p = 1 + (n * 3 + 250) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-250', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 251:
        val1 = (n * 13 + 1762) % 31 + 2
        val2 = (n * 17 + 2764) % 37 + 2
        val_k = (n * 3 + 251) % 15 + 6
        x_eval = (n + 251) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 251) % 5
            n_p = 1 + (n * 3 + 251) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-251', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 252:
        val1 = (n * 13 + 1769) % 31 + 2
        val2 = (n * 17 + 2775) % 37 + 2
        val_k = (n * 3 + 252) % 15 + 6
        x_eval = (n + 252) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 252) % 5
            n_p = 1 + (n * 3 + 252) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-252', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 253:
        val1 = (n * 13 + 1776) % 31 + 2
        val2 = (n * 17 + 2786) % 37 + 2
        val_k = (n * 3 + 253) % 15 + 6
        x_eval = (n + 253) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 253) % 5
            n_p = 1 + (n * 3 + 253) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-253', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 254:
        val1 = (n * 13 + 1783) % 31 + 2
        val2 = (n * 17 + 2797) % 37 + 2
        val_k = (n * 3 + 254) % 15 + 6
        x_eval = (n + 254) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 254) % 5
            n_p = 1 + (n * 3 + 254) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-254', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 255:
        val1 = (n * 13 + 1790) % 31 + 2
        val2 = (n * 17 + 2808) % 37 + 2
        val_k = (n * 3 + 255) % 15 + 6
        x_eval = (n + 255) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 255) % 5
            n_p = 1 + (n * 3 + 255) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-255', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 256:
        val1 = (n * 13 + 1797) % 31 + 2
        val2 = (n * 17 + 2819) % 37 + 2
        val_k = (n * 3 + 256) % 15 + 6
        x_eval = (n + 256) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 256) % 5
            n_p = 1 + (n * 3 + 256) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-256', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 257:
        val1 = (n * 13 + 1804) % 31 + 2
        val2 = (n * 17 + 2830) % 37 + 2
        val_k = (n * 3 + 257) % 15 + 6
        x_eval = (n + 257) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 257) % 5
            n_p = 1 + (n * 3 + 257) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-257', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 258:
        val1 = (n * 13 + 1811) % 31 + 2
        val2 = (n * 17 + 2841) % 37 + 2
        val_k = (n * 3 + 258) % 15 + 6
        x_eval = (n + 258) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 258) % 5
            n_p = 1 + (n * 3 + 258) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-258', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 259:
        val1 = (n * 13 + 1818) % 31 + 2
        val2 = (n * 17 + 2852) % 37 + 2
        val_k = (n * 3 + 259) % 15 + 6
        x_eval = (n + 259) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 259) % 5
            n_p = 1 + (n * 3 + 259) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-259', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 260:
        val1 = (n * 13 + 1825) % 31 + 2
        val2 = (n * 17 + 2863) % 37 + 2
        val_k = (n * 3 + 260) % 15 + 6
        x_eval = (n + 260) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 260) % 5
            n_p = 1 + (n * 3 + 260) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-260', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 261:
        val1 = (n * 13 + 1832) % 31 + 2
        val2 = (n * 17 + 2874) % 37 + 2
        val_k = (n * 3 + 261) % 15 + 6
        x_eval = (n + 261) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 261) % 5
            n_p = 1 + (n * 3 + 261) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-261', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 262:
        val1 = (n * 13 + 1839) % 31 + 2
        val2 = (n * 17 + 2885) % 37 + 2
        val_k = (n * 3 + 262) % 15 + 6
        x_eval = (n + 262) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 262) % 5
            n_p = 1 + (n * 3 + 262) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-262', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 263:
        val1 = (n * 13 + 1846) % 31 + 2
        val2 = (n * 17 + 2896) % 37 + 2
        val_k = (n * 3 + 263) % 15 + 6
        x_eval = (n + 263) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 263) % 5
            n_p = 1 + (n * 3 + 263) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-263', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 264:
        val1 = (n * 13 + 1853) % 31 + 2
        val2 = (n * 17 + 2907) % 37 + 2
        val_k = (n * 3 + 264) % 15 + 6
        x_eval = (n + 264) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 264) % 5
            n_p = 1 + (n * 3 + 264) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-264', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 265:
        val1 = (n * 13 + 1860) % 31 + 2
        val2 = (n * 17 + 2918) % 37 + 2
        val_k = (n * 3 + 265) % 15 + 6
        x_eval = (n + 265) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 265) % 5
            n_p = 1 + (n * 3 + 265) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-265', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 266:
        val1 = (n * 13 + 1867) % 31 + 2
        val2 = (n * 17 + 2929) % 37 + 2
        val_k = (n * 3 + 266) % 15 + 6
        x_eval = (n + 266) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 266) % 5
            n_p = 1 + (n * 3 + 266) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-266', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 267:
        val1 = (n * 13 + 1874) % 31 + 2
        val2 = (n * 17 + 2940) % 37 + 2
        val_k = (n * 3 + 267) % 15 + 6
        x_eval = (n + 267) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 267) % 5
            n_p = 1 + (n * 3 + 267) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-267', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 268:
        val1 = (n * 13 + 1881) % 31 + 2
        val2 = (n * 17 + 2951) % 37 + 2
        val_k = (n * 3 + 268) % 15 + 6
        x_eval = (n + 268) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 268) % 5
            n_p = 1 + (n * 3 + 268) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-268', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 269:
        val1 = (n * 13 + 1888) % 31 + 2
        val2 = (n * 17 + 2962) % 37 + 2
        val_k = (n * 3 + 269) % 15 + 6
        x_eval = (n + 269) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 269) % 5
            n_p = 1 + (n * 3 + 269) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-269', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 270:
        val1 = (n * 13 + 1895) % 31 + 2
        val2 = (n * 17 + 2973) % 37 + 2
        val_k = (n * 3 + 270) % 15 + 6
        x_eval = (n + 270) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 270) % 5
            n_p = 1 + (n * 3 + 270) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-270', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 271:
        val1 = (n * 13 + 1902) % 31 + 2
        val2 = (n * 17 + 2984) % 37 + 2
        val_k = (n * 3 + 271) % 15 + 6
        x_eval = (n + 271) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 271) % 5
            n_p = 1 + (n * 3 + 271) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-271', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 272:
        val1 = (n * 13 + 1909) % 31 + 2
        val2 = (n * 17 + 2995) % 37 + 2
        val_k = (n * 3 + 272) % 15 + 6
        x_eval = (n + 272) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 272) % 5
            n_p = 1 + (n * 3 + 272) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-272', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 273:
        val1 = (n * 13 + 1916) % 31 + 2
        val2 = (n * 17 + 3006) % 37 + 2
        val_k = (n * 3 + 273) % 15 + 6
        x_eval = (n + 273) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 273) % 5
            n_p = 1 + (n * 3 + 273) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-273', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 274:
        val1 = (n * 13 + 1923) % 31 + 2
        val2 = (n * 17 + 3017) % 37 + 2
        val_k = (n * 3 + 274) % 15 + 6
        x_eval = (n + 274) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 274) % 5
            n_p = 1 + (n * 3 + 274) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-274', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 275:
        val1 = (n * 13 + 1930) % 31 + 2
        val2 = (n * 17 + 3028) % 37 + 2
        val_k = (n * 3 + 275) % 15 + 6
        x_eval = (n + 275) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 275) % 5
            n_p = 1 + (n * 3 + 275) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-275', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 276:
        val1 = (n * 13 + 1937) % 31 + 2
        val2 = (n * 17 + 3039) % 37 + 2
        val_k = (n * 3 + 276) % 15 + 6
        x_eval = (n + 276) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 276) % 5
            n_p = 1 + (n * 3 + 276) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-276', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 277:
        val1 = (n * 13 + 1944) % 31 + 2
        val2 = (n * 17 + 3050) % 37 + 2
        val_k = (n * 3 + 277) % 15 + 6
        x_eval = (n + 277) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 277) % 5
            n_p = 1 + (n * 3 + 277) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-277', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 278:
        val1 = (n * 13 + 1951) % 31 + 2
        val2 = (n * 17 + 3061) % 37 + 2
        val_k = (n * 3 + 278) % 15 + 6
        x_eval = (n + 278) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 278) % 5
            n_p = 1 + (n * 3 + 278) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-278', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 279:
        val1 = (n * 13 + 1958) % 31 + 2
        val2 = (n * 17 + 3072) % 37 + 2
        val_k = (n * 3 + 279) % 15 + 6
        x_eval = (n + 279) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 279) % 5
            n_p = 1 + (n * 3 + 279) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-279', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 280:
        val1 = (n * 13 + 1965) % 31 + 2
        val2 = (n * 17 + 3083) % 37 + 2
        val_k = (n * 3 + 280) % 15 + 6
        x_eval = (n + 280) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 280) % 5
            n_p = 1 + (n * 3 + 280) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-280', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 281:
        val1 = (n * 13 + 1972) % 31 + 2
        val2 = (n * 17 + 3094) % 37 + 2
        val_k = (n * 3 + 281) % 15 + 6
        x_eval = (n + 281) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 281) % 5
            n_p = 1 + (n * 3 + 281) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-281', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 282:
        val1 = (n * 13 + 1979) % 31 + 2
        val2 = (n * 17 + 3105) % 37 + 2
        val_k = (n * 3 + 282) % 15 + 6
        x_eval = (n + 282) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 282) % 5
            n_p = 1 + (n * 3 + 282) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-282', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 283:
        val1 = (n * 13 + 1986) % 31 + 2
        val2 = (n * 17 + 3116) % 37 + 2
        val_k = (n * 3 + 283) % 15 + 6
        x_eval = (n + 283) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 283) % 5
            n_p = 1 + (n * 3 + 283) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-283', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 284:
        val1 = (n * 13 + 1993) % 31 + 2
        val2 = (n * 17 + 3127) % 37 + 2
        val_k = (n * 3 + 284) % 15 + 6
        x_eval = (n + 284) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 284) % 5
            n_p = 1 + (n * 3 + 284) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-284', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 285:
        val1 = (n * 13 + 2000) % 31 + 2
        val2 = (n * 17 + 3138) % 37 + 2
        val_k = (n * 3 + 285) % 15 + 6
        x_eval = (n + 285) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 285) % 5
            n_p = 1 + (n * 3 + 285) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-285', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 286:
        val1 = (n * 13 + 2007) % 31 + 2
        val2 = (n * 17 + 3149) % 37 + 2
        val_k = (n * 3 + 286) % 15 + 6
        x_eval = (n + 286) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 286) % 5
            n_p = 1 + (n * 3 + 286) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-286', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 287:
        val1 = (n * 13 + 2014) % 31 + 2
        val2 = (n * 17 + 3160) % 37 + 2
        val_k = (n * 3 + 287) % 15 + 6
        x_eval = (n + 287) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 287) % 5
            n_p = 1 + (n * 3 + 287) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-287', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 288:
        val1 = (n * 13 + 2021) % 31 + 2
        val2 = (n * 17 + 3171) % 37 + 2
        val_k = (n * 3 + 288) % 15 + 6
        x_eval = (n + 288) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 288) % 5
            n_p = 1 + (n * 3 + 288) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-288', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 289:
        val1 = (n * 13 + 2028) % 31 + 2
        val2 = (n * 17 + 3182) % 37 + 2
        val_k = (n * 3 + 289) % 15 + 6
        x_eval = (n + 289) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 289) % 5
            n_p = 1 + (n * 3 + 289) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-289', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 290:
        val1 = (n * 13 + 2035) % 31 + 2
        val2 = (n * 17 + 3193) % 37 + 2
        val_k = (n * 3 + 290) % 15 + 6
        x_eval = (n + 290) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 290) % 5
            n_p = 1 + (n * 3 + 290) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-290', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 291:
        val1 = (n * 13 + 2042) % 31 + 2
        val2 = (n * 17 + 3204) % 37 + 2
        val_k = (n * 3 + 291) % 15 + 6
        x_eval = (n + 291) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 291) % 5
            n_p = 1 + (n * 3 + 291) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-291', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 292:
        val1 = (n * 13 + 2049) % 31 + 2
        val2 = (n * 17 + 3215) % 37 + 2
        val_k = (n * 3 + 292) % 15 + 6
        x_eval = (n + 292) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 292) % 5
            n_p = 1 + (n * 3 + 292) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-292', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 293:
        val1 = (n * 13 + 2056) % 31 + 2
        val2 = (n * 17 + 3226) % 37 + 2
        val_k = (n * 3 + 293) % 15 + 6
        x_eval = (n + 293) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 293) % 5
            n_p = 1 + (n * 3 + 293) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-293', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 294:
        val1 = (n * 13 + 2063) % 31 + 2
        val2 = (n * 17 + 3237) % 37 + 2
        val_k = (n * 3 + 294) % 15 + 6
        x_eval = (n + 294) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 294) % 5
            n_p = 1 + (n * 3 + 294) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-294', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 295:
        val1 = (n * 13 + 2070) % 31 + 2
        val2 = (n * 17 + 3248) % 37 + 2
        val_k = (n * 3 + 295) % 15 + 6
        x_eval = (n + 295) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 295) % 5
            n_p = 1 + (n * 3 + 295) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-295', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 296:
        val1 = (n * 13 + 2077) % 31 + 2
        val2 = (n * 17 + 3259) % 37 + 2
        val_k = (n * 3 + 296) % 15 + 6
        x_eval = (n + 296) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 296) % 5
            n_p = 1 + (n * 3 + 296) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-296', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 297:
        val1 = (n * 13 + 2084) % 31 + 2
        val2 = (n * 17 + 3270) % 37 + 2
        val_k = (n * 3 + 297) % 15 + 6
        x_eval = (n + 297) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 297) % 5
            n_p = 1 + (n * 3 + 297) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-297', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 298:
        val1 = (n * 13 + 2091) % 31 + 2
        val2 = (n * 17 + 3281) % 37 + 2
        val_k = (n * 3 + 298) % 15 + 6
        x_eval = (n + 298) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 298) % 5
            n_p = 1 + (n * 3 + 298) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-298', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 299:
        val1 = (n * 13 + 2098) % 31 + 2
        val2 = (n * 17 + 3292) % 37 + 2
        val_k = (n * 3 + 299) % 15 + 6
        x_eval = (n + 299) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 299) % 5
            n_p = 1 + (n * 3 + 299) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-299', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 300:
        val1 = (n * 13 + 2105) % 31 + 2
        val2 = (n * 17 + 3303) % 37 + 2
        val_k = (n * 3 + 300) % 15 + 6
        x_eval = (n + 300) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 300) % 5
            n_p = 1 + (n * 3 + 300) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-300', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 301:
        val1 = (n * 13 + 2112) % 31 + 2
        val2 = (n * 17 + 3314) % 37 + 2
        val_k = (n * 3 + 301) % 15 + 6
        x_eval = (n + 301) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 301) % 5
            n_p = 1 + (n * 3 + 301) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-301', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 302:
        val1 = (n * 13 + 2119) % 31 + 2
        val2 = (n * 17 + 3325) % 37 + 2
        val_k = (n * 3 + 302) % 15 + 6
        x_eval = (n + 302) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 302) % 5
            n_p = 1 + (n * 3 + 302) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-302', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 303:
        val1 = (n * 13 + 2126) % 31 + 2
        val2 = (n * 17 + 3336) % 37 + 2
        val_k = (n * 3 + 303) % 15 + 6
        x_eval = (n + 303) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 303) % 5
            n_p = 1 + (n * 3 + 303) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-303', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 304:
        val1 = (n * 13 + 2133) % 31 + 2
        val2 = (n * 17 + 3347) % 37 + 2
        val_k = (n * 3 + 304) % 15 + 6
        x_eval = (n + 304) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 304) % 5
            n_p = 1 + (n * 3 + 304) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-304', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 305:
        val1 = (n * 13 + 2140) % 31 + 2
        val2 = (n * 17 + 3358) % 37 + 2
        val_k = (n * 3 + 305) % 15 + 6
        x_eval = (n + 305) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 305) % 5
            n_p = 1 + (n * 3 + 305) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-305', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 306:
        val1 = (n * 13 + 2147) % 31 + 2
        val2 = (n * 17 + 3369) % 37 + 2
        val_k = (n * 3 + 306) % 15 + 6
        x_eval = (n + 306) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 306) % 5
            n_p = 1 + (n * 3 + 306) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-306', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 307:
        val1 = (n * 13 + 2154) % 31 + 2
        val2 = (n * 17 + 3380) % 37 + 2
        val_k = (n * 3 + 307) % 15 + 6
        x_eval = (n + 307) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 307) % 5
            n_p = 1 + (n * 3 + 307) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-307', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 308:
        val1 = (n * 13 + 2161) % 31 + 2
        val2 = (n * 17 + 3391) % 37 + 2
        val_k = (n * 3 + 308) % 15 + 6
        x_eval = (n + 308) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 308) % 5
            n_p = 1 + (n * 3 + 308) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-308', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 309:
        val1 = (n * 13 + 2168) % 31 + 2
        val2 = (n * 17 + 3402) % 37 + 2
        val_k = (n * 3 + 309) % 15 + 6
        x_eval = (n + 309) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 309) % 5
            n_p = 1 + (n * 3 + 309) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-309', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 310:
        val1 = (n * 13 + 2175) % 31 + 2
        val2 = (n * 17 + 3413) % 37 + 2
        val_k = (n * 3 + 310) % 15 + 6
        x_eval = (n + 310) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 310) % 5
            n_p = 1 + (n * 3 + 310) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-310', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 311:
        val1 = (n * 13 + 2182) % 31 + 2
        val2 = (n * 17 + 3424) % 37 + 2
        val_k = (n * 3 + 311) % 15 + 6
        x_eval = (n + 311) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 311) % 5
            n_p = 1 + (n * 3 + 311) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-311', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 312:
        val1 = (n * 13 + 2189) % 31 + 2
        val2 = (n * 17 + 3435) % 37 + 2
        val_k = (n * 3 + 312) % 15 + 6
        x_eval = (n + 312) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 312) % 5
            n_p = 1 + (n * 3 + 312) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-312', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 313:
        val1 = (n * 13 + 2196) % 31 + 2
        val2 = (n * 17 + 3446) % 37 + 2
        val_k = (n * 3 + 313) % 15 + 6
        x_eval = (n + 313) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 313) % 5
            n_p = 1 + (n * 3 + 313) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-313', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 314:
        val1 = (n * 13 + 2203) % 31 + 2
        val2 = (n * 17 + 3457) % 37 + 2
        val_k = (n * 3 + 314) % 15 + 6
        x_eval = (n + 314) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 314) % 5
            n_p = 1 + (n * 3 + 314) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-314', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 315:
        val1 = (n * 13 + 2210) % 31 + 2
        val2 = (n * 17 + 3468) % 37 + 2
        val_k = (n * 3 + 315) % 15 + 6
        x_eval = (n + 315) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 315) % 5
            n_p = 1 + (n * 3 + 315) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-315', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 316:
        val1 = (n * 13 + 2217) % 31 + 2
        val2 = (n * 17 + 3479) % 37 + 2
        val_k = (n * 3 + 316) % 15 + 6
        x_eval = (n + 316) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 316) % 5
            n_p = 1 + (n * 3 + 316) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-316', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 317:
        val1 = (n * 13 + 2224) % 31 + 2
        val2 = (n * 17 + 3490) % 37 + 2
        val_k = (n * 3 + 317) % 15 + 6
        x_eval = (n + 317) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 317) % 5
            n_p = 1 + (n * 3 + 317) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-317', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 318:
        val1 = (n * 13 + 2231) % 31 + 2
        val2 = (n * 17 + 3501) % 37 + 2
        val_k = (n * 3 + 318) % 15 + 6
        x_eval = (n + 318) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 318) % 5
            n_p = 1 + (n * 3 + 318) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-318', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 319:
        val1 = (n * 13 + 2238) % 31 + 2
        val2 = (n * 17 + 3512) % 37 + 2
        val_k = (n * 3 + 319) % 15 + 6
        x_eval = (n + 319) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 319) % 5
            n_p = 1 + (n * 3 + 319) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-319', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 320:
        val1 = (n * 13 + 2245) % 31 + 2
        val2 = (n * 17 + 3523) % 37 + 2
        val_k = (n * 3 + 320) % 15 + 6
        x_eval = (n + 320) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 320) % 5
            n_p = 1 + (n * 3 + 320) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-320', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 321:
        val1 = (n * 13 + 2252) % 31 + 2
        val2 = (n * 17 + 3534) % 37 + 2
        val_k = (n * 3 + 321) % 15 + 6
        x_eval = (n + 321) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 321) % 5
            n_p = 1 + (n * 3 + 321) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-321', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 322:
        val1 = (n * 13 + 2259) % 31 + 2
        val2 = (n * 17 + 3545) % 37 + 2
        val_k = (n * 3 + 322) % 15 + 6
        x_eval = (n + 322) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 322) % 5
            n_p = 1 + (n * 3 + 322) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-322', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 323:
        val1 = (n * 13 + 2266) % 31 + 2
        val2 = (n * 17 + 3556) % 37 + 2
        val_k = (n * 3 + 323) % 15 + 6
        x_eval = (n + 323) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 323) % 5
            n_p = 1 + (n * 3 + 323) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-323', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 324:
        val1 = (n * 13 + 2273) % 31 + 2
        val2 = (n * 17 + 3567) % 37 + 2
        val_k = (n * 3 + 324) % 15 + 6
        x_eval = (n + 324) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 324) % 5
            n_p = 1 + (n * 3 + 324) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-324', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 325:
        val1 = (n * 13 + 2280) % 31 + 2
        val2 = (n * 17 + 3578) % 37 + 2
        val_k = (n * 3 + 325) % 15 + 6
        x_eval = (n + 325) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 325) % 5
            n_p = 1 + (n * 3 + 325) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-325', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 326:
        val1 = (n * 13 + 2287) % 31 + 2
        val2 = (n * 17 + 3589) % 37 + 2
        val_k = (n * 3 + 326) % 15 + 6
        x_eval = (n + 326) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 326) % 5
            n_p = 1 + (n * 3 + 326) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-326', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 327:
        val1 = (n * 13 + 2294) % 31 + 2
        val2 = (n * 17 + 3600) % 37 + 2
        val_k = (n * 3 + 327) % 15 + 6
        x_eval = (n + 327) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 327) % 5
            n_p = 1 + (n * 3 + 327) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-327', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 328:
        val1 = (n * 13 + 2301) % 31 + 2
        val2 = (n * 17 + 3611) % 37 + 2
        val_k = (n * 3 + 328) % 15 + 6
        x_eval = (n + 328) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 328) % 5
            n_p = 1 + (n * 3 + 328) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-328', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 329:
        val1 = (n * 13 + 2308) % 31 + 2
        val2 = (n * 17 + 3622) % 37 + 2
        val_k = (n * 3 + 329) % 15 + 6
        x_eval = (n + 329) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 329) % 5
            n_p = 1 + (n * 3 + 329) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-329', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 330:
        val1 = (n * 13 + 2315) % 31 + 2
        val2 = (n * 17 + 3633) % 37 + 2
        val_k = (n * 3 + 330) % 15 + 6
        x_eval = (n + 330) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 330) % 5
            n_p = 1 + (n * 3 + 330) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-330', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 331:
        val1 = (n * 13 + 2322) % 31 + 2
        val2 = (n * 17 + 3644) % 37 + 2
        val_k = (n * 3 + 331) % 15 + 6
        x_eval = (n + 331) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 331) % 5
            n_p = 1 + (n * 3 + 331) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-331', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 332:
        val1 = (n * 13 + 2329) % 31 + 2
        val2 = (n * 17 + 3655) % 37 + 2
        val_k = (n * 3 + 332) % 15 + 6
        x_eval = (n + 332) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 332) % 5
            n_p = 1 + (n * 3 + 332) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-332', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 333:
        val1 = (n * 13 + 2336) % 31 + 2
        val2 = (n * 17 + 3666) % 37 + 2
        val_k = (n * 3 + 333) % 15 + 6
        x_eval = (n + 333) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 333) % 5
            n_p = 1 + (n * 3 + 333) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-333', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 334:
        val1 = (n * 13 + 2343) % 31 + 2
        val2 = (n * 17 + 3677) % 37 + 2
        val_k = (n * 3 + 334) % 15 + 6
        x_eval = (n + 334) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 334) % 5
            n_p = 1 + (n * 3 + 334) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-334', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 335:
        val1 = (n * 13 + 2350) % 31 + 2
        val2 = (n * 17 + 3688) % 37 + 2
        val_k = (n * 3 + 335) % 15 + 6
        x_eval = (n + 335) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 335) % 5
            n_p = 1 + (n * 3 + 335) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-335', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 336:
        val1 = (n * 13 + 2357) % 31 + 2
        val2 = (n * 17 + 3699) % 37 + 2
        val_k = (n * 3 + 336) % 15 + 6
        x_eval = (n + 336) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 336) % 5
            n_p = 1 + (n * 3 + 336) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-336', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 337:
        val1 = (n * 13 + 2364) % 31 + 2
        val2 = (n * 17 + 3710) % 37 + 2
        val_k = (n * 3 + 337) % 15 + 6
        x_eval = (n + 337) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 337) % 5
            n_p = 1 + (n * 3 + 337) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-337', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 338:
        val1 = (n * 13 + 2371) % 31 + 2
        val2 = (n * 17 + 3721) % 37 + 2
        val_k = (n * 3 + 338) % 15 + 6
        x_eval = (n + 338) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 338) % 5
            n_p = 1 + (n * 3 + 338) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-338', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 339:
        val1 = (n * 13 + 2378) % 31 + 2
        val2 = (n * 17 + 3732) % 37 + 2
        val_k = (n * 3 + 339) % 15 + 6
        x_eval = (n + 339) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 339) % 5
            n_p = 1 + (n * 3 + 339) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-339', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 340:
        val1 = (n * 13 + 2385) % 31 + 2
        val2 = (n * 17 + 3743) % 37 + 2
        val_k = (n * 3 + 340) % 15 + 6
        x_eval = (n + 340) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 340) % 5
            n_p = 1 + (n * 3 + 340) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-340', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 341:
        val1 = (n * 13 + 2392) % 31 + 2
        val2 = (n * 17 + 3754) % 37 + 2
        val_k = (n * 3 + 341) % 15 + 6
        x_eval = (n + 341) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 341) % 5
            n_p = 1 + (n * 3 + 341) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-341', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 342:
        val1 = (n * 13 + 2399) % 31 + 2
        val2 = (n * 17 + 3765) % 37 + 2
        val_k = (n * 3 + 342) % 15 + 6
        x_eval = (n + 342) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 342) % 5
            n_p = 1 + (n * 3 + 342) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-342', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 343:
        val1 = (n * 13 + 2406) % 31 + 2
        val2 = (n * 17 + 3776) % 37 + 2
        val_k = (n * 3 + 343) % 15 + 6
        x_eval = (n + 343) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 343) % 5
            n_p = 1 + (n * 3 + 343) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-343', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 344:
        val1 = (n * 13 + 2413) % 31 + 2
        val2 = (n * 17 + 3787) % 37 + 2
        val_k = (n * 3 + 344) % 15 + 6
        x_eval = (n + 344) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 344) % 5
            n_p = 1 + (n * 3 + 344) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-344', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 345:
        val1 = (n * 13 + 2420) % 31 + 2
        val2 = (n * 17 + 3798) % 37 + 2
        val_k = (n * 3 + 345) % 15 + 6
        x_eval = (n + 345) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 345) % 5
            n_p = 1 + (n * 3 + 345) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-345', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 346:
        val1 = (n * 13 + 2427) % 31 + 2
        val2 = (n * 17 + 3809) % 37 + 2
        val_k = (n * 3 + 346) % 15 + 6
        x_eval = (n + 346) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 346) % 5
            n_p = 1 + (n * 3 + 346) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-346', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 347:
        val1 = (n * 13 + 2434) % 31 + 2
        val2 = (n * 17 + 3820) % 37 + 2
        val_k = (n * 3 + 347) % 15 + 6
        x_eval = (n + 347) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 347) % 5
            n_p = 1 + (n * 3 + 347) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-347', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 348:
        val1 = (n * 13 + 2441) % 31 + 2
        val2 = (n * 17 + 3831) % 37 + 2
        val_k = (n * 3 + 348) % 15 + 6
        x_eval = (n + 348) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 348) % 5
            n_p = 1 + (n * 3 + 348) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-348', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 349:
        val1 = (n * 13 + 2448) % 31 + 2
        val2 = (n * 17 + 3842) % 37 + 2
        val_k = (n * 3 + 349) % 15 + 6
        x_eval = (n + 349) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 349) % 5
            n_p = 1 + (n * 3 + 349) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-349', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 350:
        val1 = (n * 13 + 2455) % 31 + 2
        val2 = (n * 17 + 3853) % 37 + 2
        val_k = (n * 3 + 350) % 15 + 6
        x_eval = (n + 350) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 350) % 5
            n_p = 1 + (n * 3 + 350) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-350', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 351:
        val1 = (n * 13 + 2462) % 31 + 2
        val2 = (n * 17 + 3864) % 37 + 2
        val_k = (n * 3 + 351) % 15 + 6
        x_eval = (n + 351) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 351) % 5
            n_p = 1 + (n * 3 + 351) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-351', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 352:
        val1 = (n * 13 + 2469) % 31 + 2
        val2 = (n * 17 + 3875) % 37 + 2
        val_k = (n * 3 + 352) % 15 + 6
        x_eval = (n + 352) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 352) % 5
            n_p = 1 + (n * 3 + 352) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-352', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 353:
        val1 = (n * 13 + 2476) % 31 + 2
        val2 = (n * 17 + 3886) % 37 + 2
        val_k = (n * 3 + 353) % 15 + 6
        x_eval = (n + 353) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 353) % 5
            n_p = 1 + (n * 3 + 353) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-353', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 354:
        val1 = (n * 13 + 2483) % 31 + 2
        val2 = (n * 17 + 3897) % 37 + 2
        val_k = (n * 3 + 354) % 15 + 6
        x_eval = (n + 354) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 354) % 5
            n_p = 1 + (n * 3 + 354) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-354', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 355:
        val1 = (n * 13 + 2490) % 31 + 2
        val2 = (n * 17 + 3908) % 37 + 2
        val_k = (n * 3 + 355) % 15 + 6
        x_eval = (n + 355) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 355) % 5
            n_p = 1 + (n * 3 + 355) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-355', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 356:
        val1 = (n * 13 + 2497) % 31 + 2
        val2 = (n * 17 + 3919) % 37 + 2
        val_k = (n * 3 + 356) % 15 + 6
        x_eval = (n + 356) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 356) % 5
            n_p = 1 + (n * 3 + 356) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-356', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 357:
        val1 = (n * 13 + 2504) % 31 + 2
        val2 = (n * 17 + 3930) % 37 + 2
        val_k = (n * 3 + 357) % 15 + 6
        x_eval = (n + 357) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 357) % 5
            n_p = 1 + (n * 3 + 357) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-357', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 358:
        val1 = (n * 13 + 2511) % 31 + 2
        val2 = (n * 17 + 3941) % 37 + 2
        val_k = (n * 3 + 358) % 15 + 6
        x_eval = (n + 358) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 358) % 5
            n_p = 1 + (n * 3 + 358) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-358', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 359:
        val1 = (n * 13 + 2518) % 31 + 2
        val2 = (n * 17 + 3952) % 37 + 2
        val_k = (n * 3 + 359) % 15 + 6
        x_eval = (n + 359) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 359) % 5
            n_p = 1 + (n * 3 + 359) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-359', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 360:
        val1 = (n * 13 + 2525) % 31 + 2
        val2 = (n * 17 + 3963) % 37 + 2
        val_k = (n * 3 + 360) % 15 + 6
        x_eval = (n + 360) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 360) % 5
            n_p = 1 + (n * 3 + 360) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-360', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 361:
        val1 = (n * 13 + 2532) % 31 + 2
        val2 = (n * 17 + 3974) % 37 + 2
        val_k = (n * 3 + 361) % 15 + 6
        x_eval = (n + 361) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 361) % 5
            n_p = 1 + (n * 3 + 361) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-361', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 362:
        val1 = (n * 13 + 2539) % 31 + 2
        val2 = (n * 17 + 3985) % 37 + 2
        val_k = (n * 3 + 362) % 15 + 6
        x_eval = (n + 362) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 362) % 5
            n_p = 1 + (n * 3 + 362) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-362', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 363:
        val1 = (n * 13 + 2546) % 31 + 2
        val2 = (n * 17 + 3996) % 37 + 2
        val_k = (n * 3 + 363) % 15 + 6
        x_eval = (n + 363) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 363) % 5
            n_p = 1 + (n * 3 + 363) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-363', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 364:
        val1 = (n * 13 + 2553) % 31 + 2
        val2 = (n * 17 + 4007) % 37 + 2
        val_k = (n * 3 + 364) % 15 + 6
        x_eval = (n + 364) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 364) % 5
            n_p = 1 + (n * 3 + 364) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-364', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 365:
        val1 = (n * 13 + 2560) % 31 + 2
        val2 = (n * 17 + 4018) % 37 + 2
        val_k = (n * 3 + 365) % 15 + 6
        x_eval = (n + 365) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 365) % 5
            n_p = 1 + (n * 3 + 365) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-365', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 366:
        val1 = (n * 13 + 2567) % 31 + 2
        val2 = (n * 17 + 4029) % 37 + 2
        val_k = (n * 3 + 366) % 15 + 6
        x_eval = (n + 366) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 366) % 5
            n_p = 1 + (n * 3 + 366) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-366', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 367:
        val1 = (n * 13 + 2574) % 31 + 2
        val2 = (n * 17 + 4040) % 37 + 2
        val_k = (n * 3 + 367) % 15 + 6
        x_eval = (n + 367) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 367) % 5
            n_p = 1 + (n * 3 + 367) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-367', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 368:
        val1 = (n * 13 + 2581) % 31 + 2
        val2 = (n * 17 + 4051) % 37 + 2
        val_k = (n * 3 + 368) % 15 + 6
        x_eval = (n + 368) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 368) % 5
            n_p = 1 + (n * 3 + 368) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-368', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 369:
        val1 = (n * 13 + 2588) % 31 + 2
        val2 = (n * 17 + 4062) % 37 + 2
        val_k = (n * 3 + 369) % 15 + 6
        x_eval = (n + 369) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 369) % 5
            n_p = 1 + (n * 3 + 369) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-369', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 370:
        val1 = (n * 13 + 2595) % 31 + 2
        val2 = (n * 17 + 4073) % 37 + 2
        val_k = (n * 3 + 370) % 15 + 6
        x_eval = (n + 370) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 370) % 5
            n_p = 1 + (n * 3 + 370) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-370', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 371:
        val1 = (n * 13 + 2602) % 31 + 2
        val2 = (n * 17 + 4084) % 37 + 2
        val_k = (n * 3 + 371) % 15 + 6
        x_eval = (n + 371) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 371) % 5
            n_p = 1 + (n * 3 + 371) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-371', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 372:
        val1 = (n * 13 + 2609) % 31 + 2
        val2 = (n * 17 + 4095) % 37 + 2
        val_k = (n * 3 + 372) % 15 + 6
        x_eval = (n + 372) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 372) % 5
            n_p = 1 + (n * 3 + 372) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-372', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 373:
        val1 = (n * 13 + 2616) % 31 + 2
        val2 = (n * 17 + 4106) % 37 + 2
        val_k = (n * 3 + 373) % 15 + 6
        x_eval = (n + 373) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 373) % 5
            n_p = 1 + (n * 3 + 373) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-373', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 374:
        val1 = (n * 13 + 2623) % 31 + 2
        val2 = (n * 17 + 4117) % 37 + 2
        val_k = (n * 3 + 374) % 15 + 6
        x_eval = (n + 374) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 374) % 5
            n_p = 1 + (n * 3 + 374) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-374', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 375:
        val1 = (n * 13 + 2630) % 31 + 2
        val2 = (n * 17 + 4128) % 37 + 2
        val_k = (n * 3 + 375) % 15 + 6
        x_eval = (n + 375) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 375) % 5
            n_p = 1 + (n * 3 + 375) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-375', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 376:
        val1 = (n * 13 + 2637) % 31 + 2
        val2 = (n * 17 + 4139) % 37 + 2
        val_k = (n * 3 + 376) % 15 + 6
        x_eval = (n + 376) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 376) % 5
            n_p = 1 + (n * 3 + 376) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-376', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 377:
        val1 = (n * 13 + 2644) % 31 + 2
        val2 = (n * 17 + 4150) % 37 + 2
        val_k = (n * 3 + 377) % 15 + 6
        x_eval = (n + 377) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 377) % 5
            n_p = 1 + (n * 3 + 377) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-377', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 378:
        val1 = (n * 13 + 2651) % 31 + 2
        val2 = (n * 17 + 4161) % 37 + 2
        val_k = (n * 3 + 378) % 15 + 6
        x_eval = (n + 378) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 378) % 5
            n_p = 1 + (n * 3 + 378) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-378', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 379:
        val1 = (n * 13 + 2658) % 31 + 2
        val2 = (n * 17 + 4172) % 37 + 2
        val_k = (n * 3 + 379) % 15 + 6
        x_eval = (n + 379) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 379) % 5
            n_p = 1 + (n * 3 + 379) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-379', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 380:
        val1 = (n * 13 + 2665) % 31 + 2
        val2 = (n * 17 + 4183) % 37 + 2
        val_k = (n * 3 + 380) % 15 + 6
        x_eval = (n + 380) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 380) % 5
            n_p = 1 + (n * 3 + 380) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-380', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 381:
        val1 = (n * 13 + 2672) % 31 + 2
        val2 = (n * 17 + 4194) % 37 + 2
        val_k = (n * 3 + 381) % 15 + 6
        x_eval = (n + 381) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 381) % 5
            n_p = 1 + (n * 3 + 381) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-381', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 382:
        val1 = (n * 13 + 2679) % 31 + 2
        val2 = (n * 17 + 4205) % 37 + 2
        val_k = (n * 3 + 382) % 15 + 6
        x_eval = (n + 382) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 382) % 5
            n_p = 1 + (n * 3 + 382) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-382', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 383:
        val1 = (n * 13 + 2686) % 31 + 2
        val2 = (n * 17 + 4216) % 37 + 2
        val_k = (n * 3 + 383) % 15 + 6
        x_eval = (n + 383) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 383) % 5
            n_p = 1 + (n * 3 + 383) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-383', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 384:
        val1 = (n * 13 + 2693) % 31 + 2
        val2 = (n * 17 + 4227) % 37 + 2
        val_k = (n * 3 + 384) % 15 + 6
        x_eval = (n + 384) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 384) % 5
            n_p = 1 + (n * 3 + 384) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-384', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 385:
        val1 = (n * 13 + 2700) % 31 + 2
        val2 = (n * 17 + 4238) % 37 + 2
        val_k = (n * 3 + 385) % 15 + 6
        x_eval = (n + 385) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 385) % 5
            n_p = 1 + (n * 3 + 385) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-385', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 386:
        val1 = (n * 13 + 2707) % 31 + 2
        val2 = (n * 17 + 4249) % 37 + 2
        val_k = (n * 3 + 386) % 15 + 6
        x_eval = (n + 386) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 386) % 5
            n_p = 1 + (n * 3 + 386) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-386', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 387:
        val1 = (n * 13 + 2714) % 31 + 2
        val2 = (n * 17 + 4260) % 37 + 2
        val_k = (n * 3 + 387) % 15 + 6
        x_eval = (n + 387) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 387) % 5
            n_p = 1 + (n * 3 + 387) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-387', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 388:
        val1 = (n * 13 + 2721) % 31 + 2
        val2 = (n * 17 + 4271) % 37 + 2
        val_k = (n * 3 + 388) % 15 + 6
        x_eval = (n + 388) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 388) % 5
            n_p = 1 + (n * 3 + 388) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-388', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 389:
        val1 = (n * 13 + 2728) % 31 + 2
        val2 = (n * 17 + 4282) % 37 + 2
        val_k = (n * 3 + 389) % 15 + 6
        x_eval = (n + 389) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 389) % 5
            n_p = 1 + (n * 3 + 389) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-389', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 390:
        val1 = (n * 13 + 2735) % 31 + 2
        val2 = (n * 17 + 4293) % 37 + 2
        val_k = (n * 3 + 390) % 15 + 6
        x_eval = (n + 390) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 390) % 5
            n_p = 1 + (n * 3 + 390) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-390', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 391:
        val1 = (n * 13 + 2742) % 31 + 2
        val2 = (n * 17 + 4304) % 37 + 2
        val_k = (n * 3 + 391) % 15 + 6
        x_eval = (n + 391) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 391) % 5
            n_p = 1 + (n * 3 + 391) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-391', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 392:
        val1 = (n * 13 + 2749) % 31 + 2
        val2 = (n * 17 + 4315) % 37 + 2
        val_k = (n * 3 + 392) % 15 + 6
        x_eval = (n + 392) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 392) % 5
            n_p = 1 + (n * 3 + 392) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-392', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 393:
        val1 = (n * 13 + 2756) % 31 + 2
        val2 = (n * 17 + 4326) % 37 + 2
        val_k = (n * 3 + 393) % 15 + 6
        x_eval = (n + 393) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 393) % 5
            n_p = 1 + (n * 3 + 393) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-393', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 394:
        val1 = (n * 13 + 2763) % 31 + 2
        val2 = (n * 17 + 4337) % 37 + 2
        val_k = (n * 3 + 394) % 15 + 6
        x_eval = (n + 394) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 394) % 5
            n_p = 1 + (n * 3 + 394) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-394', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 395:
        val1 = (n * 13 + 2770) % 31 + 2
        val2 = (n * 17 + 4348) % 37 + 2
        val_k = (n * 3 + 395) % 15 + 6
        x_eval = (n + 395) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 395) % 5
            n_p = 1 + (n * 3 + 395) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-395', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 396:
        val1 = (n * 13 + 2777) % 31 + 2
        val2 = (n * 17 + 4359) % 37 + 2
        val_k = (n * 3 + 396) % 15 + 6
        x_eval = (n + 396) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 396) % 5
            n_p = 1 + (n * 3 + 396) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-396', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 397:
        val1 = (n * 13 + 2784) % 31 + 2
        val2 = (n * 17 + 4370) % 37 + 2
        val_k = (n * 3 + 397) % 15 + 6
        x_eval = (n + 397) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 397) % 5
            n_p = 1 + (n * 3 + 397) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-397', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 398:
        val1 = (n * 13 + 2791) % 31 + 2
        val2 = (n * 17 + 4381) % 37 + 2
        val_k = (n * 3 + 398) % 15 + 6
        x_eval = (n + 398) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 398) % 5
            n_p = 1 + (n * 3 + 398) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-398', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 399:
        val1 = (n * 13 + 2798) % 31 + 2
        val2 = (n * 17 + 4392) % 37 + 2
        val_k = (n * 3 + 399) % 15 + 6
        x_eval = (n + 399) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 399) % 5
            n_p = 1 + (n * 3 + 399) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-399', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 400:
        val1 = (n * 13 + 2805) % 31 + 2
        val2 = (n * 17 + 4403) % 37 + 2
        val_k = (n * 3 + 400) % 15 + 6
        x_eval = (n + 400) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 400) % 5
            n_p = 1 + (n * 3 + 400) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-400', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 401:
        val1 = (n * 13 + 2812) % 31 + 2
        val2 = (n * 17 + 4414) % 37 + 2
        val_k = (n * 3 + 401) % 15 + 6
        x_eval = (n + 401) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 401) % 5
            n_p = 1 + (n * 3 + 401) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-401', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 402:
        val1 = (n * 13 + 2819) % 31 + 2
        val2 = (n * 17 + 4425) % 37 + 2
        val_k = (n * 3 + 402) % 15 + 6
        x_eval = (n + 402) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 402) % 5
            n_p = 1 + (n * 3 + 402) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-402', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 403:
        val1 = (n * 13 + 2826) % 31 + 2
        val2 = (n * 17 + 4436) % 37 + 2
        val_k = (n * 3 + 403) % 15 + 6
        x_eval = (n + 403) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 403) % 5
            n_p = 1 + (n * 3 + 403) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-403', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 404:
        val1 = (n * 13 + 2833) % 31 + 2
        val2 = (n * 17 + 4447) % 37 + 2
        val_k = (n * 3 + 404) % 15 + 6
        x_eval = (n + 404) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 404) % 5
            n_p = 1 + (n * 3 + 404) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-404', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 405:
        val1 = (n * 13 + 2840) % 31 + 2
        val2 = (n * 17 + 4458) % 37 + 2
        val_k = (n * 3 + 405) % 15 + 6
        x_eval = (n + 405) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 405) % 5
            n_p = 1 + (n * 3 + 405) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-405', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 406:
        val1 = (n * 13 + 2847) % 31 + 2
        val2 = (n * 17 + 4469) % 37 + 2
        val_k = (n * 3 + 406) % 15 + 6
        x_eval = (n + 406) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 406) % 5
            n_p = 1 + (n * 3 + 406) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-406', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 407:
        val1 = (n * 13 + 2854) % 31 + 2
        val2 = (n * 17 + 4480) % 37 + 2
        val_k = (n * 3 + 407) % 15 + 6
        x_eval = (n + 407) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 407) % 5
            n_p = 1 + (n * 3 + 407) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-407', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 408:
        val1 = (n * 13 + 2861) % 31 + 2
        val2 = (n * 17 + 4491) % 37 + 2
        val_k = (n * 3 + 408) % 15 + 6
        x_eval = (n + 408) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 408) % 5
            n_p = 1 + (n * 3 + 408) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-408', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 409:
        val1 = (n * 13 + 2868) % 31 + 2
        val2 = (n * 17 + 4502) % 37 + 2
        val_k = (n * 3 + 409) % 15 + 6
        x_eval = (n + 409) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 409) % 5
            n_p = 1 + (n * 3 + 409) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-409', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 410:
        val1 = (n * 13 + 2875) % 31 + 2
        val2 = (n * 17 + 4513) % 37 + 2
        val_k = (n * 3 + 410) % 15 + 6
        x_eval = (n + 410) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 410) % 5
            n_p = 1 + (n * 3 + 410) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-410', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 411:
        val1 = (n * 13 + 2882) % 31 + 2
        val2 = (n * 17 + 4524) % 37 + 2
        val_k = (n * 3 + 411) % 15 + 6
        x_eval = (n + 411) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 411) % 5
            n_p = 1 + (n * 3 + 411) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-411', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 412:
        val1 = (n * 13 + 2889) % 31 + 2
        val2 = (n * 17 + 4535) % 37 + 2
        val_k = (n * 3 + 412) % 15 + 6
        x_eval = (n + 412) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 412) % 5
            n_p = 1 + (n * 3 + 412) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-412', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 413:
        val1 = (n * 13 + 2896) % 31 + 2
        val2 = (n * 17 + 4546) % 37 + 2
        val_k = (n * 3 + 413) % 15 + 6
        x_eval = (n + 413) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 413) % 5
            n_p = 1 + (n * 3 + 413) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-413', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 414:
        val1 = (n * 13 + 2903) % 31 + 2
        val2 = (n * 17 + 4557) % 37 + 2
        val_k = (n * 3 + 414) % 15 + 6
        x_eval = (n + 414) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 414) % 5
            n_p = 1 + (n * 3 + 414) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-414', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 415:
        val1 = (n * 13 + 2910) % 31 + 2
        val2 = (n * 17 + 4568) % 37 + 2
        val_k = (n * 3 + 415) % 15 + 6
        x_eval = (n + 415) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 415) % 5
            n_p = 1 + (n * 3 + 415) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-415', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 416:
        val1 = (n * 13 + 2917) % 31 + 2
        val2 = (n * 17 + 4579) % 37 + 2
        val_k = (n * 3 + 416) % 15 + 6
        x_eval = (n + 416) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 416) % 5
            n_p = 1 + (n * 3 + 416) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-416', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 417:
        val1 = (n * 13 + 2924) % 31 + 2
        val2 = (n * 17 + 4590) % 37 + 2
        val_k = (n * 3 + 417) % 15 + 6
        x_eval = (n + 417) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 417) % 5
            n_p = 1 + (n * 3 + 417) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-417', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 418:
        val1 = (n * 13 + 2931) % 31 + 2
        val2 = (n * 17 + 4601) % 37 + 2
        val_k = (n * 3 + 418) % 15 + 6
        x_eval = (n + 418) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 418) % 5
            n_p = 1 + (n * 3 + 418) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-418', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 419:
        val1 = (n * 13 + 2938) % 31 + 2
        val2 = (n * 17 + 4612) % 37 + 2
        val_k = (n * 3 + 419) % 15 + 6
        x_eval = (n + 419) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 419) % 5
            n_p = 1 + (n * 3 + 419) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-419', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 420:
        val1 = (n * 13 + 2945) % 31 + 2
        val2 = (n * 17 + 4623) % 37 + 2
        val_k = (n * 3 + 420) % 15 + 6
        x_eval = (n + 420) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 420) % 5
            n_p = 1 + (n * 3 + 420) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-420', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 421:
        val1 = (n * 13 + 2952) % 31 + 2
        val2 = (n * 17 + 4634) % 37 + 2
        val_k = (n * 3 + 421) % 15 + 6
        x_eval = (n + 421) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 421) % 5
            n_p = 1 + (n * 3 + 421) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-421', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 422:
        val1 = (n * 13 + 2959) % 31 + 2
        val2 = (n * 17 + 4645) % 37 + 2
        val_k = (n * 3 + 422) % 15 + 6
        x_eval = (n + 422) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 422) % 5
            n_p = 1 + (n * 3 + 422) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-422', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 423:
        val1 = (n * 13 + 2966) % 31 + 2
        val2 = (n * 17 + 4656) % 37 + 2
        val_k = (n * 3 + 423) % 15 + 6
        x_eval = (n + 423) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 423) % 5
            n_p = 1 + (n * 3 + 423) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-423', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 424:
        val1 = (n * 13 + 2973) % 31 + 2
        val2 = (n * 17 + 4667) % 37 + 2
        val_k = (n * 3 + 424) % 15 + 6
        x_eval = (n + 424) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 424) % 5
            n_p = 1 + (n * 3 + 424) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-424', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 425:
        val1 = (n * 13 + 2980) % 31 + 2
        val2 = (n * 17 + 4678) % 37 + 2
        val_k = (n * 3 + 425) % 15 + 6
        x_eval = (n + 425) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 425) % 5
            n_p = 1 + (n * 3 + 425) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-425', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 426:
        val1 = (n * 13 + 2987) % 31 + 2
        val2 = (n * 17 + 4689) % 37 + 2
        val_k = (n * 3 + 426) % 15 + 6
        x_eval = (n + 426) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 426) % 5
            n_p = 1 + (n * 3 + 426) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-426', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 427:
        val1 = (n * 13 + 2994) % 31 + 2
        val2 = (n * 17 + 4700) % 37 + 2
        val_k = (n * 3 + 427) % 15 + 6
        x_eval = (n + 427) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 427) % 5
            n_p = 1 + (n * 3 + 427) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-427', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 428:
        val1 = (n * 13 + 3001) % 31 + 2
        val2 = (n * 17 + 4711) % 37 + 2
        val_k = (n * 3 + 428) % 15 + 6
        x_eval = (n + 428) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 428) % 5
            n_p = 1 + (n * 3 + 428) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-428', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 429:
        val1 = (n * 13 + 3008) % 31 + 2
        val2 = (n * 17 + 4722) % 37 + 2
        val_k = (n * 3 + 429) % 15 + 6
        x_eval = (n + 429) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 429) % 5
            n_p = 1 + (n * 3 + 429) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-429', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 430:
        val1 = (n * 13 + 3015) % 31 + 2
        val2 = (n * 17 + 4733) % 37 + 2
        val_k = (n * 3 + 430) % 15 + 6
        x_eval = (n + 430) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 430) % 5
            n_p = 1 + (n * 3 + 430) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-430', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 431:
        val1 = (n * 13 + 3022) % 31 + 2
        val2 = (n * 17 + 4744) % 37 + 2
        val_k = (n * 3 + 431) % 15 + 6
        x_eval = (n + 431) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 431) % 5
            n_p = 1 + (n * 3 + 431) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-431', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 432:
        val1 = (n * 13 + 3029) % 31 + 2
        val2 = (n * 17 + 4755) % 37 + 2
        val_k = (n * 3 + 432) % 15 + 6
        x_eval = (n + 432) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 432) % 5
            n_p = 1 + (n * 3 + 432) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-432', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 433:
        val1 = (n * 13 + 3036) % 31 + 2
        val2 = (n * 17 + 4766) % 37 + 2
        val_k = (n * 3 + 433) % 15 + 6
        x_eval = (n + 433) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 433) % 5
            n_p = 1 + (n * 3 + 433) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-433', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 434:
        val1 = (n * 13 + 3043) % 31 + 2
        val2 = (n * 17 + 4777) % 37 + 2
        val_k = (n * 3 + 434) % 15 + 6
        x_eval = (n + 434) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 434) % 5
            n_p = 1 + (n * 3 + 434) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-434', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 435:
        val1 = (n * 13 + 3050) % 31 + 2
        val2 = (n * 17 + 4788) % 37 + 2
        val_k = (n * 3 + 435) % 15 + 6
        x_eval = (n + 435) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 435) % 5
            n_p = 1 + (n * 3 + 435) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-435', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 436:
        val1 = (n * 13 + 3057) % 31 + 2
        val2 = (n * 17 + 4799) % 37 + 2
        val_k = (n * 3 + 436) % 15 + 6
        x_eval = (n + 436) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 436) % 5
            n_p = 1 + (n * 3 + 436) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-436', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 437:
        val1 = (n * 13 + 3064) % 31 + 2
        val2 = (n * 17 + 4810) % 37 + 2
        val_k = (n * 3 + 437) % 15 + 6
        x_eval = (n + 437) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 437) % 5
            n_p = 1 + (n * 3 + 437) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-437', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 438:
        val1 = (n * 13 + 3071) % 31 + 2
        val2 = (n * 17 + 4821) % 37 + 2
        val_k = (n * 3 + 438) % 15 + 6
        x_eval = (n + 438) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 438) % 5
            n_p = 1 + (n * 3 + 438) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-438', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 439:
        val1 = (n * 13 + 3078) % 31 + 2
        val2 = (n * 17 + 4832) % 37 + 2
        val_k = (n * 3 + 439) % 15 + 6
        x_eval = (n + 439) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 439) % 5
            n_p = 1 + (n * 3 + 439) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-439', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 440:
        val1 = (n * 13 + 3085) % 31 + 2
        val2 = (n * 17 + 4843) % 37 + 2
        val_k = (n * 3 + 440) % 15 + 6
        x_eval = (n + 440) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 440) % 5
            n_p = 1 + (n * 3 + 440) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-440', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 441:
        val1 = (n * 13 + 3092) % 31 + 2
        val2 = (n * 17 + 4854) % 37 + 2
        val_k = (n * 3 + 441) % 15 + 6
        x_eval = (n + 441) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 441) % 5
            n_p = 1 + (n * 3 + 441) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-441', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 442:
        val1 = (n * 13 + 3099) % 31 + 2
        val2 = (n * 17 + 4865) % 37 + 2
        val_k = (n * 3 + 442) % 15 + 6
        x_eval = (n + 442) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 442) % 5
            n_p = 1 + (n * 3 + 442) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-442', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 443:
        val1 = (n * 13 + 3106) % 31 + 2
        val2 = (n * 17 + 4876) % 37 + 2
        val_k = (n * 3 + 443) % 15 + 6
        x_eval = (n + 443) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 443) % 5
            n_p = 1 + (n * 3 + 443) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-443', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 444:
        val1 = (n * 13 + 3113) % 31 + 2
        val2 = (n * 17 + 4887) % 37 + 2
        val_k = (n * 3 + 444) % 15 + 6
        x_eval = (n + 444) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 444) % 5
            n_p = 1 + (n * 3 + 444) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-444', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 445:
        val1 = (n * 13 + 3120) % 31 + 2
        val2 = (n * 17 + 4898) % 37 + 2
        val_k = (n * 3 + 445) % 15 + 6
        x_eval = (n + 445) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 445) % 5
            n_p = 1 + (n * 3 + 445) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-445', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 446:
        val1 = (n * 13 + 3127) % 31 + 2
        val2 = (n * 17 + 4909) % 37 + 2
        val_k = (n * 3 + 446) % 15 + 6
        x_eval = (n + 446) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 446) % 5
            n_p = 1 + (n * 3 + 446) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-446', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    if k == 447:
        val1 = (n * 13 + 3134) % 31 + 2
        val2 = (n * 17 + 4920) % 37 + 2
        val_k = (n * 3 + 447) % 15 + 6
        x_eval = (n + 447) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 447) % 5
            n_p = 1 + (n * 3 + 447) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 2 * val1 * (val1 * x_eval + val2)
        return item('chain-rule-composition-447', 'Calculus',
                    f'If \\( f(x) = ({val1}x + {val2})^2 \\), find \\( f\'({x_eval}) \\).',
                    f'إذا كانت \\( f(x) = ({val1}x + {val2})^2 \\)، فأوجد \\( f\'({x_eval}) \\).',
                    ans,
                    f'By chain rule: \\( f\'(x) = 2({val1})({val1}x + {val2}) = {2*val1}({val1}x + {val2}) \\). At x={x_eval}, result is {ans}.',
                    f'بقاعدة السلسلة: المشتقة تساوي {ans}.')

    if k == 448:
        val1 = (n * 13 + 3141) % 31 + 2
        val2 = (n * 17 + 4931) % 37 + 2
        val_k = (n * 3 + 448) % 15 + 6
        x_eval = (n + 448) % 4 + 1
        if 'Calculus' == 'Trigonometry':
            m_p = 2 + (n + 448) % 5
            n_p = 1 + (n * 3 + 448) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val1, 2) + val2
        return item('integral-linear-substitution-448', 'Calculus',
                    f'Evaluate \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    f'احسب التكامل المحدد \\( \\int_0^1 ({val1}x + {val2}) \\, dx \\).',
                    ans,
                    f'\\( \\int_0^1 ({val1}x + {val2}) dx = [{val1}x^2/2 + {val2}x]_0^1 = {val(ans)} \\).',
                    f'قيمة التكامل = {val(ans)}.')

    if k == 449:
        val1 = (n * 13 + 3148) % 31 + 2
        val2 = (n * 17 + 4942) % 37 + 2
        val_k = (n * 3 + 449) % 15 + 6
        x_eval = (n + 449) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 449) % 5
            n_p = 1 + (n * 3 + 449) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1 * 2
        return item('line-slope-intercept-449', 'Analytic Geometry',
                    f'Find the y-intercept of the line \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    f'أوجد المقطع الصادي للمستقيم \\( {val1}x + {val2}y = {val1 * val2 * 2} \\).',
                    ans,
                    f'Set x=0: \\( {val2}y = {val1 * val2 * 2} \\implies y = {ans} \\).',
                    f'المقطع الصادي = {ans}.')

    if k == 450:
        val1 = (n * 13 + 3155) % 31 + 2
        val2 = (n * 17 + 4953) % 37 + 2
        val_k = (n * 3 + 450) % 15 + 6
        x_eval = (n + 450) % 4 + 1
        if 'Analytic Geometry' == 'Trigonometry':
            m_p = 2 + (n + 450) % 5
            n_p = 1 + (n * 3 + 450) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('circle-radius-from-equation-450', 'Analytic Geometry',
                    f'What is the radius squared of the circle \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)?',
                    f'ما مربع نصف قطر الدائرة \\( x^2 + y^2 - {2*val1}x - {2*val2}y = 0 \\)؟',
                    ans,
                    f'Complete squares: \\( (x - {val1})^2 + (y - {val2})^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع نصف القطر = {ans}.')

    if k == 451:
        val1 = (n * 13 + 3162) % 31 + 2
        val2 = (n * 17 + 4964) % 37 + 2
        val_k = (n * 3 + 451) % 15 + 6
        x_eval = (n + 451) % 4 + 1
        if 'Linear Algebra' == 'Trigonometry':
            m_p = 2 + (n + 451) % 5
            n_p = 1 + (n * 3 + 451) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val1**2 + val2**2
        return item('vector-projection-length-451', 'Linear Algebra',
                    f'If vector \\( \\mathbf{{u}} = ({val1}, 0) \\) and \\( \\mathbf{{v}} = (0, {val2}) \\), what is \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)?',
                    f'إذا كان \\( \\mathbf{{u}} = ({val1}, 0) \\) و \\( \\mathbf{{v}} = (0, {val2}) \\)، فما قيمة \\( \\|\\mathbf{{u}} + \\mathbf{{v}}\\|^2 \\)؟',
                    ans,
                    f'Vectors are orthogonal: \\( \\|\\mathbf{{u}}+\\mathbf{{v}}\\|^2 = {val1}^2 + {val2}^2 = {ans} \\).',
                    f'مربع معيار المجموع = {ans}.')

    if k == 452:
        val1 = (n * 13 + 3169) % 31 + 2
        val2 = (n * 17 + 4975) % 37 + 2
        val_k = (n * 3 + 452) % 15 + 6
        x_eval = (n + 452) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 452) % 5
            n_p = 1 + (n * 3 + 452) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = val_k * (val_k - 1)
        return item('permutations-distinct-elements-452', 'Combinatorics',
                    f'How many distinct permutations can be formed from {val_k} distinct items taking 2 at a time?',
                    f'كم تبديلاً مختلفًا يمكن تكوينه من {val_k} عناصر متميزة مأخوذة 2 في كل مرة؟',
                    ans,
                    f'\\( P({val_k}, 2) = {val_k} \\times {val_k - 1} = {ans} \\).',
                    f'عدد التبديلات = {ans}.')

    if k == 453:
        val1 = (n * 13 + 3176) % 31 + 2
        val2 = (n * 17 + 4986) % 37 + 2
        val_k = (n * 3 + 453) % 15 + 6
        x_eval = (n + 453) % 4 + 1
        if 'Combinatorics' == 'Trigonometry':
            m_p = 2 + (n + 453) % 5
            n_p = 1 + (n * 3 + 453) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = (val_k * (val_k - 1)) // 2
        return item('combinations-n-choose-two-453', 'Combinatorics',
                    f'Find the value of the binomial coefficient \\( \\binom{{{val_k}}}{{2}} \\).',
                    f'احسب قيمة التوافيق \\( \\binom{{{val_k}}}{{2}} \\).',
                    ans,
                    f'\\( \\binom{{{val_k}}}{{2}} = \\frac{{{val_k} \\times {val_k - 1}}}{{2}} = {ans} \\).',
                    f'قيمة التوافيق = {ans}.')

    if k == 454:
        val1 = (n * 13 + 3183) % 31 + 2
        val2 = (n * 17 + 4997) % 37 + 2
        val_k = (n * 3 + 454) % 15 + 6
        x_eval = (n + 454) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 454) % 5
            n_p = 1 + (n * 3 + 454) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = 8 - 2 * val1 + val2
        return item('polynomial-remainder-theorem-454', 'Algebra',
                    f'Find the remainder when \\( P(x) = x^3 - {val1}x + {val2} \\) is divided by \\( x - 2 \\).',
                    f'أوجد باقي قسمة \\( P(x) = x^3 - {val1}x + {val2} \\) على \\( x - 2 \\).',
                    ans,
                    f'By remainder theorem, evaluate P(2): \\( 2^3 - {val1}(2) + {val2} = 8 - {2*val1} + {val2} = {ans} \\).',
                    f'بمقتضى مبرهنة الباقي P(2) = {ans}.')

    if k == 455:
        val1 = (n * 13 + 3190) % 31 + 2
        val2 = (n * 17 + 5008) % 37 + 2
        val_k = (n * 3 + 455) % 15 + 6
        x_eval = (n + 455) % 4 + 1
        if 'Algebra' == 'Trigonometry':
            m_p = 2 + (n + 455) % 5
            n_p = 1 + (n * 3 + 455) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = -val2
        return item('vieta-product-of-roots-455', 'Algebra',
                    f'What is the product of the roots of the quadratic equation \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)?',
                    f'ما حاصل ضرب جذري المعادلة التربيعية \\( {val1}x^2 + {val2}x - {val1 * val2} = 0 \\)؟',
                    ans,
                    f'Vieta formula gives product of roots = c/a = -{val1 * val2}/{val1} = {ans}.',
                    f'حاصل ضرب الجذرين = c/a = {ans}.')

    if k == 456:
        val1 = (n * 13 + 3197) % 31 + 2
        val2 = (n * 17 + 5019) % 37 + 2
        val_k = (n * 3 + 456) % 15 + 6
        x_eval = (n + 456) % 4 + 1
        if 'Trigonometry' == 'Trigonometry':
            m_p = 2 + (n + 456) % 5
            n_p = 1 + (n * 3 + 456) % 4
            if m_p <= n_p: m_p = n_p + 1
            val1 = m_p**2 - n_p**2
            val2 = 2 * m_p * n_p
            val_hyp = m_p**2 + n_p**2
        else:
            val_hyp = val1 + val2

        ans = F(val2, val_hyp)
        return item('trig-pythagorean-identity-sine-456', 'Trigonometry',
                    f'If \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) with \\( \\theta \\) acute and \\( {val1}^2 + {val2}^2 = {val_hyp}^2 \\), find \\( \\sin \\theta \\).',
                    f'إذا كان \\( \\cos \\theta = \\frac{{{val1}}}{{{val_hyp}}} \\) حيث \\( \\theta \\) حادة، فما قيمة \\( \\sin \\theta \\)؟',
                    ans,
                    f'\\( \\sin \\theta = \\sqrt{{1 - \\cos^2 \\theta}} = \\frac{{{val2}}}{{{val_hyp}}} = {val(ans)} \\).',
                    f'\\( \\sin \\theta = {val(ans)} \\).')

    raise ValueError(f"Unknown senior family k={k}")
