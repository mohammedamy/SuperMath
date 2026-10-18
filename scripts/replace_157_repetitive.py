"""Surgically replace 157 legacy repetitive/duplicate questions in SuperMath
with mathematically rich, unique, curriculum-aligned questions.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def m(x): return f"\\( {x} \\)"

REPLACEMENTS = {}

def add(track, qid, level, topic, diff, q_en, q_ar, options, correct_idx, hint_en, hint_ar, expl_en, expl_ar):
    opts = [m(o) for o in options]
    assert 0 <= correct_idx < len(opts), f"{qid}: invalid correct_idx {correct_idx} for {len(opts)} options"
    assert len(set(opts)) == len(opts), f"{qid}: duplicate options {opts}"
    if track not in REPLACEMENTS:
        REPLACEMENTS[track] = {}
    REPLACEMENTS[track][qid] = {
        "id": qid,
        "track": track,
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": diff,
        "content": {
            "en": {
                "question": q_en,
                "options": opts,
                "hint": hint_en,
                "explanation": expl_en
            },
            "ar": {
                "question": q_ar,
                "options": opts,
                "hint": hint_ar,
                "explanation": expl_ar
            }
        },
        "correct_index": correct_idx
    }

# ==================== JEE (1 replacement) ====================
add("jee", "JEE-249", "Grade 12", "Calculus", "medium",
    "Find the \( x \)-coordinate of the inflection point of \( f(x) = x^3 - 6x^2 + 9x + 1 \).",
    "أوجد الإحداثي \( x \) لنقطة الانقلاب للدالة \( f(x) = x^3 - 6x^2 + 9x + 1 \).",
    ["0", "2", "4", "-2"], 1,
    "An inflection point occurs where the second derivative changes sign: set \( f''(x) = 0 \).",
    "تحدث نقطة الانقلاب عندما تنعدم المشتقة الثانية ويتغير رمزها: ضع \( f''(x) = 0 \).",
    "\( f'(x) = 3x^2 - 12x + 9 \), so \( f''(x) = 6x - 12 = 0 \implies x = 2 \).",
    "\( f'(x) = 3x^2 - 12x + 9 \)، وبالتالي \( f''(x) = 6x - 12 = 0 \implies x = 2 \).")

# ==================== KAUST (23 replacements) ====================
add("kaust", "KAUST-P1-011", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "Find the trace of the \( 3 \\times 3 \) matrix \( A = \\begin{pmatrix} 4 & 1 & 0 \\\\ 2 & -3 & 5 \\\\ 7 & 6 & 8 \\end{pmatrix} \).",
    "أوجد أثر (Trace) المصفوفة \( 3 \\times 3 \) الآتية: \( A = \\begin{pmatrix} 4 & 1 & 0 \\\\ 2 & -3 & 5 \\\\ 7 & 6 & 8 \\end{pmatrix} \).",
    ["7", "8", "9", "12"], 2,
    "The trace of a square matrix is the sum of the elements on its main diagonal.",
    "أثر المصفوفة المربعة هو مجموع عناصر قطرها الرئيسي.",
    "\( \\text{Tr}(A) = 4 + (-3) + 8 = 9 \).",
    "\( \\text{Tr}(A) = 4 + (-3) + 8 = 9 \).")

add("kaust", "KAUST-P1-015", "Phase 1: Foundation Research", "Linear Algebra", "medium",
    "Let \( A \) be a \( 2 \\times 2 \) matrix with eigenvalues \( \\lambda_1 = 3 \) and \( \\lambda_2 = 5 \). What is the determinant \( \\det(A) \)?",
    "لتكن \( A \) مصفوفة \( 2 \\times 2 \) قيمها الذاتية \( \\lambda_1 = 3 \) و\( \\lambda_2 = 5 \). ما قيمة محددها \( \\det(A) \)؟",
    ["8", "15", "16", "2"], 1,
    "The determinant of a matrix equals the product of its eigenvalues.",
    "محدد المصفوفة يساوي حاصل ضرب قيمها الذاتية.",
    "\( \\det(A) = \\lambda_1 \\cdot \\lambda_2 = 3 \\times 5 = 15 \).",
    "\( \\det(A) = \\lambda_1 \\cdot \\lambda_2 = 3 \\times 5 = 15 \).")

add("kaust", "KAUST-P1-019", "Phase 1: Foundation Research", "Vector Analysis", "easy",
    "Find the dot product of the vectors \( \\mathbf{u} = \\langle 2, -3, 4 \\rangle \) and \( \\mathbf{v} = \\langle 5, 2, 1 \\rangle \).",
    "أوجد حاصل الضرب القياسي للمتجهين \( \\mathbf{u} = \\langle 2, -3, 4 \\rangle \) و\( \\mathbf{v} = \\langle 5, 2, 1 \\rangle \).",
    ["6", "8", "10", "12"], 1,
    "Multiply corresponding components and add the products together.",
    "اضرب المركبات المتناظرة واجمع النواتج.",
    "\( \\mathbf{u} \\cdot \\mathbf{v} = 2(5) + (-3)(2) + 4(1) = 10 - 6 + 4 = 8 \).",
    "\( \\mathbf{u} \\cdot \\mathbf{v} = 2(5) + (-3)(2) + 4(1) = 10 - 6 + 4 = 8 \).")

add("kaust", "KAUST-P1-023", "Phase 1: Foundation Research", "Vector Analysis", "medium",
    "What is the magnitude of the cross product \( |\\mathbf{u} \\times \\mathbf{v}| \) if \( |\\mathbf{u}| = 4 \), \( |\\mathbf{v}| = 6 \), and the angle between them is \( 30^\\circ \)?",
    "ما مقدار حاصل الضرب الاتجاهي \( |\\mathbf{u} \\times \\mathbf{v}| \) إذا كان \( |\\mathbf{u}| = 4 \) و\( |\\mathbf{v}| = 6 \) والزاوية بينهما \( 30^\\circ \)؟",
    ["6", "12", "12\\sqrt{3}", "24"], 1,
    "Use \( |\\mathbf{u} \\times \\mathbf{v}| = |\\mathbf{u}| |\\mathbf{v}| \\sin(\\theta) \).",
    "استخدم القانون \( |\\mathbf{u} \\times \\mathbf{v}| = |\\mathbf{u}| |\\mathbf{v}| \\sin(\\theta) \).",
    "\( |\\mathbf{u} \\times \\mathbf{v}| = 4 \\times 6 \\times \\sin(30^\\circ) = 24 \\times 0.5 = 12 \).",
    "\( |\\mathbf{u} \\times \\mathbf{v}| = 4 \\times 6 \\times \\sin(30^\\circ) = 24 \\times 0.5 = 12 \).")

add("kaust", "KAUST-P1-027", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "Find the rank of the \( 2 \\times 2 \) matrix \( A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 6 \\end{pmatrix} \).",
    "أوجد رتبة (Rank) المصفوفة \( A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 6 \\end{pmatrix} \).",
    ["0", "1", "2", "3"], 1,
    "The second row is a scalar multiple of the first row (\( 3 \\times R_1 \)).",
    "الصف الثاني مضاعف قياسي للصف الأول (\( 3 \\times R_1 \)).",
    "Row reduction gives \( \\begin{pmatrix} 1 & 2 \\\\ 0 & 0 \\end{pmatrix} \), which has \( 1 \) non-zero row, so rank = \( 1 \).",
    "بالاختزال الصفي نحصل على صف واحد غير صفري، لذا الرتبة = \( 1 \).")

add("kaust", "KAUST-P1-031", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "If \( A \) is an invertible \( 3 \\times 3 \) matrix with \( \\det(A) = 4 \), what is \( \\det(A^{-1}) \)?",
    "إذا كانت \( A \) مصفوفة قابلة للعكس من الرتبة \( 3 \\times 3 \) بحيث \( \\det(A) = 4 \)، فما قيمة \( \\det(A^{-1}) \)؟",
    ["\\frac{1}{4}", "4", "-4", "16"], 0,
    "Recall that \( \\det(A^{-1}) = \\frac{1}{\\det(A)} \).",
    "تذكر أن \( \\det(A^{-1}) = \\frac{1}{\\det(A)} \).",
    "\( \\det(A^{-1}) = \\frac{1}{4} \).",
    "\( \\det(A^{-1}) = \\frac{1}{4} \).")

add("kaust", "KAUST-P1-035", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "What are the eigenvalues of the diagonal matrix \( D = \\begin{pmatrix} 7 & 0 \\\\ 0 & -2 \\end{pmatrix} \)?",
    "ما القيم الذاتية للمصفوفة القطرية \( D = \\begin{pmatrix} 7 & 0 \\\\ 0 & -2 \\end{pmatrix} \)؟",
    ["7 \\text{ and } -2", "7 \\text{ and } 2", "-7 \\text{ and } -2", "5 \\text{ and } -14"], 0,
    "For any diagonal matrix, the eigenvalues are simply the entries on the main diagonal.",
    "لأي مصفوفة قطرية، القيم الذاتية هي ببساطة عناصر القطر الرئيسي.",
    "The diagonal elements are \( 7 \) and \( -2 \), which are the eigenvalues.",
    "عناصر القطر الرئيسي هي \( 7 \) و\( -2 \)، وهي تمثل القيم الذاتية.")

add("kaust", "KAUST-P1-039", "Phase 1: Foundation Research", "Vector Analysis", "medium",
    "Find the angle between the vectors \( \\mathbf{a} = \\langle 1, 1 \\rangle \) and \( \\mathbf{b} = \\langle 0, 1 \\rangle \).",
    "أوجد الزاوية بين المتجهين \( \\mathbf{a} = \\langle 1, 1 \\rangle \) و\( \\mathbf{b} = \\langle 0, 1 \\rangle \).",
    ["30^\\circ", "45^\\circ", "60^\\circ", "90^\\circ"], 1,
    "Use \( \\cos(\\theta) = \\frac{\\mathbf{a} \\cdot \\mathbf{b}}{|\\mathbf{a}| |\\mathbf{b}|} \).",
    "استخدم القانون \( \\cos(\\theta) = \\frac{\\mathbf{a} \\cdot \\mathbf{b}}{|\\mathbf{a}| |\\mathbf{b}|} \).",
    "\( \\mathbf{a} \\cdot \\mathbf{b} = 1 \), \( |\\mathbf{a}| = \\sqrt{2} \), \( |\\mathbf{b}| = 1 \). So \( \\cos(\\theta) = \\frac{1}{\\sqrt{2}} \\implies \\theta = 45^\\circ \).",
    "\( \\mathbf{a} \\cdot \\mathbf{b} = 1 \)، و\( |\\mathbf{a}| = \\sqrt{2} \)، و\( |\\mathbf{b}| = 1 \). إذن \( \\cos(\\theta) = \\frac{1}{\\sqrt{2}} \\implies \\theta = 45^\\circ \).")

add("kaust", "KAUST-P1-043", "Phase 1: Foundation Research", "Complex Numbers", "easy",
    "Find the modulus \( |z| \) of the complex number \( z = 3 - 4i \).",
    "أوجد مقياس (معيار) العدد المركب \( z = 3 - 4i \).",
    ["3", "4", "5", "7"], 2,
    "The modulus is defined as \( |a + bi| = \\sqrt{a^2 + b^2} \).",
    "يُعرف المقياس بالقانون \( |a + bi| = \\sqrt{a^2 + b^2} \).",
    "\( |z| = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5 \).",
    "\( |z| = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5 \).")

add("kaust", "KAUST-P1-047", "Phase 1: Foundation Research", "Complex Numbers", "easy",
    "Evaluate the expression \( e^{i\\pi} + 1 \) using Euler's identity.",
    "احسب قيمة المقدار \( e^{i\\pi} + 1 \) باستخدام متطابقة أويلر.",
    ["0", "1", "-1", "2i"], 0,
    "Euler's identity states that \( e^{i\\pi} = \\cos(\\pi) + i\\sin(\\pi) = -1 \).",
    "تنص متطابقة أويلر على أن \( e^{i\\pi} = \\cos(\\pi) + i\\sin(\\pi) = -1 \).",
    "\( e^{i\\pi} + 1 = -1 + 1 = 0 \).",
    "\( e^{i\\pi} + 1 = -1 + 1 = 0 \).")

add("kaust", "KAUST-P1-051", "Phase 1: Foundation Research", "Linear Algebra", "medium",
    "If \( A \) is an orthogonal matrix, which of the following is always true about \( \\det(A) \)?",
    "إذا كانت \( A \) مصفوفة متعامدة (Orthogonal)، فأي العبارات الآتية صحيحة دائمًا لمحددها \( \\det(A) \)؟",
    ["\\det(A) = \\pm 1", "\\det(A) = 0", "\\det(A) > 1", "\\det(A) = \\infty"], 0,
    "An orthogonal matrix satisfies \( A^T A = I \), so \( \\det(A)^2 = 1 \).",
    "تحقق المصفوفة المتعامدة الشرط \( A^T A = I \)، وبالتالي \( \\det(A)^2 = 1 \).",
    "Taking the square root gives \( \\det(A) = \\pm 1 \).",
    "بأخذ الجذر التربيعي نحصل على \( \\det(A) = \\pm 1 \).")

add("kaust", "KAUST-P1-055", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "Find the inverse of the diagonal matrix \( A = \\begin{pmatrix} 2 & 0 \\\\ 0 & 5 \\end{pmatrix} \).",
    "أوجد معكوس المصفوفة القطرية \( A = \\begin{pmatrix} 2 & 0 \\\\ 0 & 5 \\end{pmatrix} \).",
    ["\\begin{pmatrix} 1/2 & 0 \\\\ 0 & 1/5 \\end{pmatrix}", "\\begin{pmatrix} -2 & 0 \\\\ 0 & -5 \\end{pmatrix}", "\\begin{pmatrix} 5 & 0 \\\\ 0 & 2 \\end{pmatrix}", "\\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}"], 0,
    "The inverse of a diagonal matrix is formed by taking the reciprocal of each non-zero diagonal entry.",
    "معكوس المصفوفة القطرية ينتج عن أخذ مقلوب كل عنصر غير صفري على القطر الرئيسي.",
    "\( A^{-1} = \\begin{pmatrix} 1/2 & 0 \\\\ 0 & 1/5 \\end{pmatrix} \).",
    "\( A^{-1} = \\begin{pmatrix} 1/2 & 0 \\\\ 0 & 1/5 \\end{pmatrix} \).")

add("kaust", "KAUST-P1-059", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "Let \( A \) be a \( 2 \\times 2 \) symmetric matrix. If \( A_{12} = 7 \), what is the value of \( A_{21} \)?",
    "لتكن \( A \) مصفوفة متماثلة \( 2 \\times 2 \). إذا كان \( A_{12} = 7 \)، فما قيمة \( A_{21} \)؟",
    ["-7", "0", "7", "14"], 2,
    "A matrix is symmetric if \( A = A^T \), which implies \( A_{ij} = A_{ji} \).",
    "تكون المصفوفة متماثلة إذا كان \( A = A^T \)، مما يعني أن \( A_{ij} = A_{ji} \).",
    "Since \( A \) is symmetric, \( A_{21} = A_{12} = 7 \).",
    "بما أن \( A \) متماثلة، فإن \( A_{21} = A_{12} = 7 \).")

add("kaust", "KAUST-P1-063", "Phase 1: Foundation Research", "Linear Algebra", "easy",
    "What is the determinant of the upper triangular matrix \( U = \\begin{pmatrix} 3 & 4 & 5 \\\\ 0 & 2 & 6 \\\\ 0 & 0 & 4 \\end{pmatrix} \)?",
    "ما محدد المصفوفة المثلثية العليا \( U = \\begin{pmatrix} 3 & 4 & 5 \\\\ 0 & 2 & 6 \\\\ 0 & 0 & 4 \\end{pmatrix} \)؟",
    ["12", "18", "24", "48"], 2,
    "The determinant of any triangular matrix is the product of its diagonal entries.",
    "محدد أي مصفوفة مثلثية هو حاصل ضرب عناصر قطرها الرئيسي.",
    "\( \\det(U) = 3 \\times 2 \\times 4 = 24 \).",
    "\( \\det(U) = 3 \\times 2 \\times 4 = 24 \).")

add("kaust", "KAUST-P1-009", "Phase 1: Foundation Research", "Calculus", "easy",
    "Evaluate the limit \( \\lim_{x \\to 0} \\frac{\\sin(4x)}{x} \).",
    "احسب قيمة النهاية الآتية: \( \\lim_{x \\to 0} \\frac{\\sin(4x)}{x} \).",
    ["1", "2", "4", "0"], 2,
    "Use the fundamental limit \( \\lim_{u \\to 0} \\frac{\\sin(u)}{u} = 1 \) with \( u = 4x \).",
    "استخدم النهاية الشهيرة \( \\lim_{u \\to 0} \\frac{\\sin(u)}{u} = 1 \) بوضع \( u = 4x \).",
    "\( \\lim_{x \\to 0} 4 \\cdot \\frac{\\sin(4x)}{4x} = 4 \\times 1 = 4 \).",
    "\( \\lim_{x \\to 0} 4 \\cdot \\frac{\\sin(4x)}{4x} = 4 \\times 1 = 4 \).")

add("kaust", "KAUST-P1-017", "Phase 1: Foundation Research", "Calculus", "medium",
    "Find the value of the derivative of \( f(x) = \\ln(x^2 + 1) \) at \( x = 1 \).",
    "أوجد قيمة مشتقة الدالة \( f(x) = \\ln(x^2 + 1) \) عند \( x = 1 \).",
    ["\\frac{1}{2}", "1", "2", "\\ln(2)"], 1,
    "Apply the chain rule: \( \\frac{d}{dx}[\\ln(u)] = \\frac{u'}{u} \).",
    "طبق قاعدة السلسلة: \( \\frac{d}{dx}[\\ln(u)] = \\frac{u'}{u} \).",
    "\( f'(x) = \\frac{2x}{x^2 + 1} \\implies f'(1) = \\frac{2(1)}{1^2 + 1} = \\frac{2}{2} = 1 \).",
    "\( f'(x) = \\frac{2x}{x^2 + 1} \\implies f'(1) = \\frac{2(1)}{1^2 + 1} = \\frac{2}{2} = 1 \).")

add("kaust", "KAUST-P1-021", "Phase 1: Foundation Research", "Calculus", "medium",
    "Find the derivative of \( g(x) = e^{2x} \\sin(x) \) evaluated at \( x = 0 \).",
    "أوجد مشتقة الدالة \( g(x) = e^{2x} \\sin(x) \) عند \( x = 0 \).",
    ["0", "1", "2", "e"], 1,
    "Apply the product rule: \( (uv)' = u'v + uv' \).",
    "طبق قاعدة مشتقة حاصل الضرب: \( (uv)' = u'v + uv' \).",
    "\( g'(x) = 2e^{2x}\\sin(x) + e^{2x}\\cos(x) \\implies g'(0) = 0 + 1(1) = 1 \).",
    "\( g'(x) = 2e^{2x}\\sin(x) + e^{2x}\\cos(x) \\implies g'(0) = 0 + 1(1) = 1 \).")

add("kaust", "KAUST-P1-033", "Phase 1: Foundation Research", "Calculus", "easy",
    "Evaluate the definite integral \( \\int_0^2 (3x^2 - 2x + 1)\\,dx \).",
    "احسب التكامل المحدود الآتي: \( \\int_0^2 (3x^2 - 2x + 1)\\,dx \).",
    ["4", "6", "8", "10"], 1,
    "Find the antiderivative and evaluate between the limits \( 0 \) and \( 2 \).",
    "أوجد الدالة الأصلية وعوّض بحدود التكامل من \( 0 \) إلى \( 2 \).",
    "\( [x^3 - x^2 + x]_0^2 = (8 - 4 + 2) - 0 = 6 \).",
    "\( [x^3 - x^2 + x]_0^2 = (8 - 4 + 2) - 0 = 6 \).")

add("kaust", "KAUST-P1-037", "Phase 1: Foundation Research", "Calculus", "easy",
    "Evaluate the definite integral \( \\int_1^e \\frac{1}{x}\\,dx \).",
    "احسب التكامل المحدود الآتي: \( \\int_1^e \\frac{1}{x}\\,dx \).",
    ["0", "1", "e", "e - 1"], 1,
    "The antiderivative of \( 1/x \) is \( \\ln|x| \).",
    "الدالة الأصلية لـ \( 1/x \) هي \( \\ln|x| \).",
    "\( [\\ln x]_1^e = \\ln(e) - \\ln(1) = 1 - 0 = 1 \).",
    "\( [\\ln x]_1^e = \\ln(e) - \\ln(1) = 1 - 0 = 1 \).")

add("kaust", "KAUST-P1-045", "Phase 1: Foundation Research", "Calculus", "medium",
    "Find the sum of the infinite geometric series \( \\sum_{n=1}^\\infty \\left(\\frac{1}{3}\\right)^n \).",
    "أوجد مجموع المتسلسلة الهندسية اللانهائية: \( \\sum_{n=1}^\\infty \\left(\\frac{1}{3}\\right)^n \).",
    ["\\frac{1}{3}", "\\frac{1}{2}", "\\frac{2}{3}", "1"], 1,
    "Use the infinite sum formula \( S = \\frac{a}{1 - r} \) where \( a = 1/3 \) and \( r = 1/3 \).",
    "استخدم صيغة المجموع اللانهائي \( S = \\frac{a}{1 - r} \) حيث \( a = 1/3 \) و\( r = 1/3 \).",
    "\( S = \\frac{1/3}{1 - 1/3} = \\frac{1/3}{2/3} = \\frac{1}{2} \).",
    "\( S = \\frac{1/3}{1 - 1/3} = \\frac{1/3}{2/3} = \\frac{1}{2} \).")

add("kaust", "KAUST-P1-053", "Phase 1: Foundation Research", "Multivariable Calculus", "medium",
    "Find the gradient vector \( \\nabla f(1, 2) \) for the function \( f(x, y) = x^2 y + 3y \).",
    "أوجد متجه الانحدار (Gradient) \( \\nabla f(1, 2) \) للدالة \( f(x, y) = x^2 y + 3y \).",
    ["\\langle 2, 3 \\rangle", "\\langle 4, 4 \\rangle", "\\langle 4, 1 \\rangle", "\\langle 2, 4 \\rangle"], 1,
    "Compute the partial derivatives: \( f_x = 2xy \) and \( f_y = x^2 + 3 \).",
    "احسب المشتقات الجزئية: \( f_x = 2xy \) و\( f_y = x^2 + 3 \).",
    "\( f_x(1, 2) = 2(1)(2) = 4 \) and \( f_y(1, 2) = 1^2 + 3 = 4 \\implies \\nabla f(1, 2) = \\langle 4, 4 \\rangle \).",
    "\( f_x(1, 2) = 4 \) و\( f_y(1, 2) = 4 \\implies \\nabla f(1, 2) = \\langle 4, 4 \\rangle \).")

add("kaust", "KAUST-P1-057", "Phase 1: Foundation Research", "Calculus", "easy",
    "Find the value of the second derivative \( f''(0) \) for \( f(x) = \\cos(2x) \).",
    "أوجد قيمة المشتقة الثانية \( f''(0) \) للدالة \( f(x) = \\cos(2x) \).",
    ["-4", "-2", "0", "4"], 0,
    "Differentiate twice using the chain rule.",
    "اشتق مرتين باستخدام قاعدة السلسلة.",
    "\( f'(x) = -2\\sin(2x) \\implies f''(x) = -4\\cos(2x) \\implies f''(0) = -4(1) = -4 \).",
    "\( f'(x) = -2\\sin(2x) \\implies f''(x) = -4\\cos(2x) \\implies f''(0) = -4(1) = -4 \).")

add("kaust", "KAUST-P1-061", "Phase 1: Foundation Research", "Calculus", "easy",
    "Evaluate the horizontal asymptote limit: \( \\lim_{x \\to \\infty} \\frac{5x^2 + 2x}{2x^2 - 7} \).",
    "احسب قيمة النهاية عند اللانهاية: \( \\lim_{x \\to \\infty} \\frac{5x^2 + 2x}{2x^2 - 7} \).",
    ["\\frac{5}{2}", "\\infty", "0", "\\frac{2}{5}"], 0,
    "Divide the numerator and denominator by the highest power of \( x \), which is \( x^2 \).",
    "اقسم كلاً من البسط والمقام على أعلى قوة لـ \( x \)، وهي \( x^2 \).",
    "As \( x \\to \\infty \), the lower-order terms vanish, giving the ratio of leading coefficients: \( \\frac{5}{2} \).",
    "عندما \( x \\to \\infty \)، تتلاشى الحدود ذات الدرجات الأدنى وتبقى نسبة المعاملين الرئيسيين: \( \\frac{5}{2} \).")

# ==================== NAFES (31 replacements) ====================
add("nafes", "NAFES-219", "Grade 9", "Algebra", "medium",
    "Simplify the algebraic exponent expression: \( \\frac{(3a^2 b^3)^2}{9a^3 b^4} \).",
    "بسّط المقدار الجبري الآتي: \( \\frac{(3a^2 b^3)^2}{9a^3 b^4} \).",
    ["a b^2", "a^2 b", "a b", "a^2 b^2"], 0,
    "Square the numerator: \( (3a^2 b^3)^2 = 9a^4 b^6 \), then subtract the exponents of like bases.",
    "ربّع البسط: \( (3a^2 b^3)^2 = 9a^4 b^6 \)، ثم اطرح أسس الحدود ذات الأساسات المتشابهة.",
    "\( \\frac{9a^4 b^6}{9a^3 b^4} = a^{4-3} b^{6-4} = a b^2 \).",
    "\( \\frac{9a^4 b^6}{9a^3 b^4} = a^{4-3} b^{6-4} = a b^2 \).")

add("nafes", "NAFES-201", "Grade 3", "Word Problems", "easy",
    "Fatima has \( 24 \) stickers. She gave \( 6 \) stickers to her sister and \( 8 \) stickers to her friend. How many stickers does Fatima have left?",
    "لدى فاطمة \( 24 \) ملصقًا. أعطت أختها \( 6 \) ملصقات وصديقتها \( 8 \) ملصقات. كم ملصقًا بقي مع فاطمة؟",
    ["8", "10", "12", "14"], 1,
    "Subtract the stickers given away from the starting total.",
    "اطرح عدد الملصقات المعطاة من المجموع الأصلي.",
    "\( 24 - 6 - 8 = 18 - 8 = 10 \).",
    "\( 24 - 6 - 8 = 18 - 8 = 10 \).")

add("nafes", "NAFES-6-213", "Grade 6", "Percentages", "medium",
    "A company's revenue increased from \( 50{,}000 \) to \( 65{,}000 \) riyals. What was the percentage increase?",
    "زادت أرباح شركة من \( 50{,}000 \) إلى \( 65{,}000 \) ريال. ما النسبة المئوية للزيادة؟",
    ["15\\%", "20\\%", "30\\%", "35\\%"], 2,
    "Percentage increase is \( \\frac{\\text{Increase}}{\\text{Original}} \\times 100\\% \).",
    "النسبة المئوية للزيادة هي \( \\frac{\\text{مقدار الزيادة}}{\\text{القيمة الأصلية}} \\times 100\\% \).",
    "\( \\frac{65000 - 50000}{50000} \\times 100\\% = \\frac{15000}{50000} \\times 100\\% = 30\\% \).",
    "\( \\frac{65000 - 50000}{50000} \\times 100\\% = \\frac{15000}{50000} \\times 100\\% = 30\\% \).")

# Grade 6 UUIDs
add("nafes", "NAFES-9935-4cff", "Grade 6", "Number Theory", "easy",
    "What is the prime factorization of \( 72 \)?",
    "ما التحليل إلى العوامل الأولية للعدد \( 72 \)؟",
    ["2^3 \\times 3^2", "2^2 \\times 3^3", "2^4 \\times 3", "2 \\times 3^3"], 0,
    "Repeatedly divide by 2 and 3: \( 72 = 8 \\times 9 \).",
    "اقسم بالتتابع على 2 و3: \( 72 = 8 \\times 9 \).",
    "\( 72 = 2^3 \\times 3^2 \).",
    "\( 72 = 2^3 \\times 3^2 \).")

add("nafes", "NAFES-1106-e8f3", "Grade 6", "Decimals", "easy",
    "What is the result of dividing \( 4.8 \\div 0.6 \)?",
    "ما ناتج قسمة \( 4.8 \\div 0.6 \)؟",
    ["0.8", "8", "80", "0.08"], 1,
    "Multiply both dividend and divisor by 10 to clear the decimal: \( 48 \\div 6 \).",
    "اضرب كلاً من المقسوم والمقسوم عليه في 10 للتخلص من الفاصلة: \( 48 \\div 6 \).",
    "\( 4.8 \\div 0.6 = 48 \\div 6 = 8 \).",
    "\( 4.8 \\div 0.6 = 48 \\div 6 = 8 \).")

add("nafes", "NAFES-3705-980a", "Grade 6", "Ratios", "easy",
    "In a classroom, the ratio of boys to girls is \( 3 : 4 \). If there are \( 12 \) boys, how many girls are in the classroom?",
    "في أحد الفصول، نسبة البنين إلى البنات هي \( 3 : 4 \). إذا كان عدد البنين \( 12 \)، فكم عدد البنات؟",
    ["14", "15", "16", "18"], 2,
    "Set up the proportion: \( \\frac{3}{4} = \\frac{12}{G} \).",
    "اكتب التناسب: \( \\frac{3}{4} = \\frac{12}{G} \).",
    "\( G = \\frac{12 \\times 4}{3} = 16 \).",
    "\( G = \\frac{12 \\times 4}{3} = 16 \).")

add("nafes", "NAFES-4510-6684", "Grade 6", "Scale and Measurement", "easy",
    "On a road map, a distance of \( 1 \\text{ cm} \) represents \( 25 \\text{ km} \) in reality. What actual distance is represented by \( 6 \\text{ cm} \) on the map?",
    "على خريطة طرق، المسافة \( 1 \\text{ سم} \) تمثل \( 25 \\text{ كم} \) في الواقع. فما المسافة الفعلية التي تمثلها \( 6 \\text{ سم} \) على الخريطة؟",
    ["125 \\text{ km}", "150 \\text{ km}", "175 \\text{ km}", "200 \\text{ km}"], 1,
    "Multiply the measured distance on the map by the scale factor.",
    "اضرب المسافة المقاسة على الخريطة في معامل المقياس.",
    "\( 6 \\times 25 = 150 \\text{ km} \).",
    "\( 6 \\times 25 = 150 \\text{ كم} \).")

add("nafes", "NAFES-2612-c765", "Grade 6", "Statistics", "easy",
    "The high temperatures recorded over five consecutive days were \( 28^\\circ\\text{C}, 31^\\circ\\text{C}, 29^\\circ\\text{C}, 34^\\circ\\text{C}, 28^\\circ\\text{C} \). What is the mean temperature?",
    "درجات الحرارة العظمى المسجلة خلال خمسة أيام متتالية هي: \( 28^\\circ, 31^\\circ, 29^\\circ, 34^\\circ, 28^\\circ \). ما المتوسط الحسابي لدرجات الحرارة؟",
    ["29^\\circ\\text{C}", "30^\\circ\\text{C}", "31^\\circ\\text{C}", "32^\\circ\\text{C}"], 1,
    "Sum all the values and divide by 5.",
    "اجمع كل القيم واقسم على 5.",
    "\( \\frac{28 + 31 + 29 + 34 + 28}{5} = \\frac{150}{5} = 30^\\circ\\text{C} \).",
    "\( \\frac{28 + 31 + 29 + 34 + 28}{5} = \\frac{150}{5} = 30^\\circ\\text{C} \).")

add("nafes", "NAFES-2113-8f73", "Grade 6", "Statistics", "easy",
    "What is the range of the following dataset: \( 14, 28, 9, 35, 21 \)?",
    "ما المدى لمجموعة البيانات الآتية: \( 14, 28, 9, 35, 21 \)؟",
    ["21", "24", "26", "28"], 2,
    "The range is the difference between the maximum and minimum values.",
    "المدى هو الفرق بين أكبر قيمة وأصغر قيمة.",
    "\( \\text{Range} = 35 - 9 = 26 \).",
    "\( \\text{المدى} = 35 - 9 = 26 \).")

add("nafes", "NAFES-4450-c621", "Grade 6", "Geometry", "easy",
    "A circular garden has a diameter of \( 14 \\text{ m} \). Taking \( \\pi \\approx \\frac{22}{7} \), what is the circumference of the garden?",
    "حديقة دائرية الشكل قطرها \( 14 \\text{ م} \). بافتراض \( \\pi \\approx \\frac{22}{7} \)، ما محيط الحديقة؟",
    ["28 \\text{ m}", "44 \\text{ m}", "88 \\text{ m}", "154 \\text{ m}"], 1,
    "Use the circumference formula \( C = \\pi d \).",
    "استخدم صيغة محيط الدائرة \( C = \\pi d \).",
    "\( C = \\frac{22}{7} \\times 14 = 44 \\text{ m} \).",
    "\( C = \\frac{22}{7} \\times 14 = 44 \\text{ م} \).")

add("nafes", "NAFES-6728-1794", "Grade 6", "Geometry", "easy",
    "A triangle has a base of \( 10 \\text{ cm} \) and a height of \( 7 \\text{ cm} \). What is its area in \( \\text{cm}^2 \)?",
    "مثلث طول قاعدته \( 10 \\text{ سم} \) وارتفاعه \( 7 \\text{ سم} \). ما مساحته بالـ \( \\text{سم}^2 \)؟",
    ["30", "35", "40", "70"], 1,
    "The area of a triangle is \( \\frac{1}{2} \\times \\text{base} \\times \\text{height} \).",
    "مساحة المثلث تساوي \( \\frac{1}{2} \\times \\text{القاعدة} \\times \\text{الارتفاع} \).",
    "\( \\text{Area} = \\frac{1}{2} \\times 10 \\times 7 = 35 \\text{ cm}^2 \).",
    "\( \\text{المساحة} = \\frac{1}{2} \\times 10 \\times 7 = 35 \\text{ سم}^2 \).")

add("nafes", "NAFES-5920-416d", "Grade 6", "Probability", "easy",
    "A fair six-sided die is rolled once. What is the probability of rolling an even number?",
    "أُلقي مكعب أرقام منتظم ذو 6 أوجه مرة واحدة. ما احتمال ظهور عدد زوجي؟",
    ["\\frac{1}{6}", "\\frac{1}{3}", "\\frac{1}{2}", "\\frac{2}{3}"], 2,
    "The even numbers on a die are 2, 4, and 6 (3 out of 6 outcomes).",
    "الأعداد الزوجية على المكعب هي 2، 4، 6 (3 نواتج من أصل 6).",
    "\( \\frac{3}{6} = \\frac{1}{2} \).",
    "\( \\frac{3}{6} = \\frac{1}{2} \).")

add("nafes", "NAFES-2988-c92c", "Grade 6", "Coordinate Geometry", "easy",
    "In which quadrant of the Cartesian coordinate plane does the point \( (-4, 3) \) lie?",
    "في أي ربع من المستوى الإحداثي تقع النقطة \( (-4, 3) \)؟",
    ["\\text{Quadrant I}", "\\text{Quadrant II}", "\\text{Quadrant III}", "\\text{Quadrant IV}"], 1,
    "Points with negative x and positive y are in Quadrant II.",
    "النقاط ذات الإحداثي السيني السالب والصادي الموجب تقع في الربع الثاني.",
    "Since \( x = -4 < 0 \) and \( y = 3 > 0 \), the point is in Quadrant II.",
    "بما أن \( x = -4 < 0 \) و\( y = 3 > 0 \)، فإن النقطة تقع في الربع الثاني.")

add("nafes", "NAFES-2245-7f35", "Grade 6", "Algebra", "easy",
    "Solve the linear equation for \( x \): \( \\frac{x}{5} + 4 = 11 \).",
    "حل المعادلة الخطية الآتية لإيجاد \( x \): \( \\frac{x}{5} + 4 = 11 \).",
    ["25", "30", "35", "40"], 2,
    "Subtract 4 from both sides, then multiply by 5.",
    "اطرح 4 من الطرفين، ثم اضرب في 5.",
    "\( \\frac{x}{5} = 11 - 4 = 7 \\implies x = 7 \\times 5 = 35 \).",
    "\( \\frac{x}{5} = 11 - 4 = 7 \\implies x = 7 \\times 5 = 35 \).")

add("nafes", "NAFES-8753-e828", "Grade 6", "Percentages", "easy",
    "What is \( 25\\% \) of \( 320 \) riyals?",
    "ما قيمة \( 25\\% \) من \( 320 \) ريالاً؟",
    ["60 \\text{ riyals}", "75 \\text{ riyals}", "80 \\text{ riyals}", "90 \\text{ riyals}"], 2,
    "\( 25\\% \) is equivalent to finding one quarter (\( 1/4 \)) of the amount.",
    "\( 25\\% \) تكافئ ربع المبلغ (\( 1/4 \)).",
    "\( \\frac{1}{4} \\times 320 = 80 \\text{ riyals} \).",
    "\( \\frac{1}{4} \\times 320 = 80 \\text{ ريال} \).")

add("nafes", "NAFES-8216-82b2", "Grade 6", "Volume", "easy",
    "A rectangular prism has length \( 6 \\text{ cm} \), width \( 4 \\text{ cm} \), and height \( 5 \\text{ cm} \). What is its volume in \( \\text{cm}^3 \)?",
    "منشور رباعي (متوازي مستطيلات) طوله \( 6 \\text{ سم} \) وعرضه \( 4 \\text{ سم} \) وارتفاعه \( 5 \\text{ سم} \). ما حجمه بالـ \( \\text{سم}^3 \)؟",
    ["100", "110", "120", "150"], 2,
    "Volume = length \( \\times \) width \( \\times \) height.",
    "الحجم = الطول \( \\times \) العرض \( \\times \) الارتفاع.",
    "\( V = 6 \\times 4 \\times 5 = 120 \\text{ cm}^3 \).",
    "\( V = 6 \\times 4 \\times 5 = 120 \\text{ سم}^3 \).")

# Grade 9 UUIDs
add("nafes", "NAFES-3664-527b", "Grade 9", "Algebra", "medium",
    "Find the solution set of the quadratic equation \( x^2 - 7x + 10 = 0 \).",
    "أوجد مجموعة حل المعادلة التربيعية: \( x^2 - 7x + 10 = 0 \).",
    ["x = 2 \\text{ or } x = 5", "x = -2 \\text{ or } x = -5", "x = 1 \\text{ or } x = 10", "x = -1 \\text{ or } x = -10"], 0,
    "Factor into \( (x - a)(x - b) = 0 \) where \( a + b = 7 \) and \( ab = 10 \).",
    "حلل إلى \( (x - a)(x - b) = 0 \) بحيث \( a + b = 7 \) و\( ab = 10 \).",
    "\( (x - 2)(x - 5) = 0 \\implies x = 2 \\text{ or } x = 5 \).",
    "\( (x - 2)(x - 5) = 0 \\implies x = 2 \\text{ أو } x = 5 \).")

add("nafes", "NAFES-6313-c0a5", "Grade 9", "Coordinate Geometry", "easy",
    "What is the slope of a line that is perpendicular to a line with slope \( \\frac{3}{4} \)?",
    "ما ميل المستقيم العمودي على مستقيم ميله \( \\frac{3}{4} \)؟",
    ["\\frac{3}{4}", "-\\frac{3}{4}", "\\frac{4}{3}", "-\\frac{4}{3}"], 3,
    "Perpendicular lines have negative reciprocal slopes: \( m_1 \\cdot m_2 = -1 \).",
    "المستقيمات المتعامدة حاصل ضرب ميليها يساوي \( -1 \): المعكوس الجمعي للضربي.",
    "\( m_2 = -\\frac{1}{3/4} = -\\frac{4}{3} \).",
    "\( m_2 = -\\frac{1}{3/4} = -\\frac{4}{3} \).")

add("nafes", "NAFES-6155-daf3", "Grade 9", "Coordinate Geometry", "medium",
    "Find the distance between the two points \( A(2, 3) \) and \( B(6, 6) \) in the coordinate plane.",
    "أوجد المسافة بين النقطتين \( A(2, 3) \) و\( B(6, 6) \) في المستوى الإحداثي.",
    ["4", "5", "\\sqrt{13}", "7"], 1,
    "Use the distance formula: \( d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \).",
    "استخدم قانون المسافة بين نقطتين: \( d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \).",
    "\( d = \\sqrt{(6-2)^2 + (6-3)^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5 \).",
    "\( d = \\sqrt{(6-2)^2 + (6-3)^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5 \).")

add("nafes", "NAFES-9669-5885", "Grade 9", "Coordinate Geometry", "easy",
    "Find the coordinates of the midpoint of the line segment joining \( P(1, 7) \) and \( Q(5, 3) \).",
    "أوجد إحداثيات نقطة منتصف القطعة المستقيمة الواصلة بين النقطتين \( P(1, 7) \) و\( Q(5, 3) \).",
    ["(2, 4)", "(3, 5)", "(4, 5)", "(3, 4)"], 1,
    "The midpoint formula is \( \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right) \).",
    "قانون نقطة المنتصف هو \( \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right) \).",
    "\( M = \\left( \\frac{1+5}{2}, \\frac{7+3}{2} \\right) = (3, 5) \).",
    "\( M = \\left( \\frac{1+5}{2}, \\frac{7+3}{2} \\right) = (3, 5) \).")

add("nafes", "NAFES-2403-427a", "Grade 9", "Radicals", "easy",
    "Simplify the radical expression \( \\sqrt{72} \).",
    "بسّط المقدار الجذري الآتي: \( \\sqrt{72} \).",
    ["3\\sqrt{8}", "6\\sqrt{2}", "8\\sqrt{2}", "4\\sqrt{3}"], 1,
    "Find the largest perfect square factor of 72, which is 36.",
    "ابحث عن أكبر عامل مربع كامل للعدد 72، وهو 36.",
    "\( \\sqrt{72} = \\sqrt{36 \\times 2} = 6\\sqrt{2} \).",
    "\( \\sqrt{72} = \\sqrt{36 \\times 2} = 6\\sqrt{2} \).")

add("nafes", "NAFES-4119-faf5", "Grade 9", "Radicals", "easy",
    "Rationalize the denominator of the fraction \( \\frac{10}{\\sqrt{5}} \).",
    "أنطق مقام الكسر الآتي: \( \\frac{10}{\\sqrt{5}} \).",
    ["\\sqrt{5}", "2\\sqrt{5}", "5\\sqrt{2}", "10\\sqrt{5}"], 1,
    "Multiply both the numerator and the denominator by \( \\sqrt{5} \).",
    "اضرب كلاً من البسط والمقام في \( \\sqrt{5} \).",
    "\( \\frac{10\\sqrt{5}}{(\\sqrt{5})^2} = \\frac{10\\sqrt{5}}{5} = 2\\sqrt{5} \).",
    "\( \\frac{10\\sqrt{5}}{(\\sqrt{5})^2} = \\frac{10\\sqrt{5}}{5} = 2\\sqrt{5} \).")

add("nafes", "NAFES-5092-da5d", "Grade 9", "Algebra", "easy",
    "Factor completely the difference of two squares: \( 9x^2 - 49 \).",
    "حلل تحليلاً كاملاً الفرق بين مربعين: \( 9x^2 - 49 \).",
    ["(3x - 7)(3x + 7)", "(9x - 7)(x + 7)", "(3x - 7)^2", "(3x + 7)^2"], 0,
    "Use the identity \( a^2 - b^2 = (a - b)(a + b) \).",
    "استخدم المتطابقة الشهيرة \( a^2 - b^2 = (a - b)(a + b) \).",
    "\( (3x)^2 - 7^2 = (3x - 7)(3x + 7) \).",
    "\( (3x)^2 - 7^2 = (3x - 7)(3x + 7) \).")

add("nafes", "NAFES-2512-87ee", "Grade 9", "Geometry", "easy",
    "In a right-angled triangle, the legs have lengths \( 9 \\text{ cm} \) and \( 12 \\text{ cm} \). What is the length of the hypotenuse?",
    "في مثلث قائم الزاوية، طولا ضلعي القائمة هما \( 9 \\text{ سم} \) و\( 12 \\text{ سم} \). ما طول الوتر؟",
    ["13 \\text{ cm}", "14 \\text{ cm}", "15 \\text{ cm}", "18 \\text{ cm}"], 2,
    "Apply the Pythagorean theorem: \( c^2 = a^2 + b^2 \).",
    "طبق نظرية فيثاغورس: \( c^2 = a^2 + b^2 \).",
    "\( c = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15 \\text{ cm} \).",
    "\( c = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15 \\text{ سم} \).")

add("nafes", "NAFES-5371-3042", "Grade 9", "Scientific Notation", "easy",
    "Write the decimal number \( 0.00038 \) in standard scientific notation.",
    "اكتب العدد العشري \( 0.00038 \) بالصيغة العلمية القياسية.",
    ["3.8 \\times 10^{-3}", "3.8 \\times 10^{-4}", "3.8 \\times 10^{-5}", "38 \\times 10^{-5}"], 1,
    "Move the decimal point 4 places to the right to obtain a number between 1 and 10.",
    "حرك الفاصلة العشرية 4 منازل إلى اليمين للحصول على عدد بين 1 و10.",
    "\( 0.00038 = 3.8 \\times 10^{-4} \).",
    "\( 0.00038 = 3.8 \\times 10^{-4} \).")

add("nafes", "NAFES-6967-a72c", "Grade 9", "Trigonometry", "easy",
    "What is the exact value of \( \\tan(45^\\circ) \)?",
    "ما القيمة الدقيقة لـ \( \\tan(45^\\circ) \)؟",
    ["0", "\\frac{1}{2}", "1", "\\sqrt{2}"], 2,
    "In a right isosceles triangle with 45-degree acute angles, opposite = adjacent.",
    "في المثلث القائم متطابق الضلعين وزواياه الحادة 45 درجة، المقابل يساوي المجاور.",
    "\( \\tan(45^\\circ) = \\frac{\\text{opposite}}{\\text{adjacent}} = 1 \).",
    "\( \\tan(45^\\circ) = \\frac{\\text{المقابل}}{\\text{المجاور}} = 1 \).")

add("nafes", "NAFES-8244-2f9d", "Grade 9", "Surface Area", "easy",
    "What is the total surface area of a cube whose edge length is \( 4 \\text{ cm} \)?",
    "ما مساحة السطح الكلية لمكعب طول ضلعه \( 4 \\text{ سم} \)؟",
    ["64 \\text{ cm}^2", "80 \\text{ cm}^2", "96 \\text{ cm}^2", "128 \\text{ cm}^2"], 2,
    "A cube has 6 congruent square faces: \( \\text{Surface Area} = 6s^2 \).",
    "للمكعب 6 أوجه مربعة متطابقة: المساحة الكلية = \( 6s^2 \).",
    "\( 6 \\times 4^2 = 6 \\times 16 = 96 \\text{ cm}^2 \).",
    "\( 6 \\times 4^2 = 6 \\times 16 = 96 \\text{ سم}^2 \).")

add("nafes", "NAFES-8619-1dca", "Grade 9", "Probability", "easy",
    "A card is drawn at random from a standard deck of \( 52 \) playing cards. What is the probability of drawing an Ace?",
    "سُحبت بطاقة واحدة عشوائيًا من مجموعة ورق لعب قياسية مكونة من \( 52 \) بطاقة. ما احتمال أن تكون البطاقة من فئة الآص (Ace)؟",
    ["\\frac{1}{52}", "\\frac{1}{26}", "\\frac{1}{13}", "\\frac{1}{4}"], 2,
    "There are 4 Aces in a standard deck of 52 cards.",
    "توجد 4 بطاقات من فئة الآص في المجموعة الكاملة المكونة من 52 بطاقة.",
    "\( \\frac{4}{52} = \\frac{1}{13} \).",
    "\( \\frac{4}{52} = \\frac{1}{13} \).")

add("nafes", "NAFES-7071-4702", "Grade 9", "Systems of Equations", "easy",
    "Solve the system of equations by substitution: \( y = 3x \) and \( x + y = 16 \). What is the value of \( x \)?",
    "حل نظام المعادلتين بالتعويض: \( y = 3x \) و\( x + y = 16 \). ما قيمة \( x \)؟",
    ["3", "4", "5", "12"], 1,
    "Substitute \( y = 3x \) into the second equation: \( x + 3x = 16 \).",
    "عوض بـ \( y = 3x \) في المعادلة الثانية: \( x + 3x = 16 \).",
    "\( 4x = 16 \\implies x = 4 \).",
    "\( 4x = 16 \\implies x = 4 \).")

add("nafes", "NAFES-8381-e0f5", "Grade 9", "Inequalities", "easy",
    "Solve the linear inequality: \( -2x + 3 < 11 \).",
    "حل المتباينة الخطية الآتية: \( -2x + 3 < 11 \).",
    ["x > -4", "x < -4", "x > 4", "x < 4"], 0,
    "Subtract 3 from both sides, then divide by -2 (remember to reverse the inequality sign).",
    "اطرح 3 من الطرفين، ثم اقسم على -2 (تذكر عكس اتجاه إشارة التباين).",
    "\( -2x < 8 \\implies x > -4 \).",
    "\( -2x < 8 \\implies x > -4 \).")

add("nafes", "NAFES-3564-22d4", "Grade 9", "Exponents", "easy",
    "Simplify the algebraic expression: \( (x^3)^4 \\cdot x^2 \) for any non-zero real number \( x \).",
    "بسّط المقدار الجبري الآتي: \( (x^3)^4 \\cdot x^2 \) لأي عدد حقيقي غير صفري \( x \).",
    ["x^9", "x^{14}", "x^{24}", "x^{10}"], 1,
    "Apply the power of a power rule \( (x^a)^b = x^{ab} \), then add exponents: \( x^{12} \\cdot x^2 \).",
    "طبق قاعدة قوة القوة \( (x^a)^b = x^{ab} \)، ثم اجمع الأسس: \( x^{12} \\cdot x^2 \).",
    "\( x^{12} \\cdot x^2 = x^{12+2} = x^{14} \).",
    "\( x^{12} \\cdot x^2 = x^{12+2} = x^{14} \).")

# ==================== KANGAROO (57 replacements) ====================
# 4 Legacy Duplicates
add("kangaroo", "KANGAROO-187", "Cadet", "Combinatorics", "medium",
    "In a chess tournament with \( 8 \) players, every player plays against every other player exactly once. What is the total number of games played?",
    "في بطولة شطرنج يشارك فيها \( 8 \) لاعبين، يلعب كل لاعب ضد كل لاعب آخر مرة واحدة فقط. ما العدد الكلي للمباريات التي ستُلعب؟",
    ["24", "28", "32", "36", "56"], 1,
    "The number of matches among \( n \) players is \( \\binom{n}{2} = \\frac{n(n-1)}{2} \).",
    "عدد المباريات بين \( n \) من اللاعبين هو \( \\binom{n}{2} = \\frac{n(n-1)}{2} \).",
    "\( \\binom{8}{2} = \\frac{8 \\times 7}{2} = 28 \) matches.",
    "\( \\binom{8}{2} = \\frac{8 \\times 7}{2} = 28 \) مباراة.")

add("kangaroo", "KANGAROO-089", "Cadet", "Geometry", "easy",
    "In an isosceles triangle \( ABC \) with \( AB = AC \), the vertex angle \( \\angle A \) measures \( 40^\\circ \). What is the measure of each base angle \( \\angle B \)?",
    "في مثلث متطابق الضلعين \( ABC \) حيث \( AB = AC \)، قياس زاوية الرأس \( \\angle A \) هو \( 40^\\circ \). ما قياس كل زاوية من زاويتي القاعدة؟",
    ["50^\\circ", "60^\\circ", "70^\\circ", "80^\\circ", "100^\\circ"], 2,
    "The sum of angles in a triangle is \( 180^\\circ \), and base angles of an isosceles triangle are equal.",
    "مجموع زوايا المثلث \( 180^\\circ \)، وزاويتا القاعدة في المثلث متطابق الضلعين متساويتان.",
    "\( \\angle B = \\frac{180^\\circ - 40^\\circ}{2} = \\frac{140^\\circ}{2} = 70^\\circ \).",
    "\( \\angle B = \\frac{180^\\circ - 40^\\circ}{2} = \\frac{140^\\circ}{2} = 70^\\circ \).")

add("kangaroo", "KANGAROO-033", "Cadet", "Geometry", "medium",
    "A rectangle has a perimeter of \( 36 \\text{ cm} \). If its length is twice its width, what is the area of the rectangle in \( \\text{cm}^2 \)?",
    "مستطيل محيطه \( 36 \\text{ سم} \). إذا كان طوله مثلي عرضه، فما مساحة المستطيل بالـ \( \\text{سم}^2 \)؟",
    ["54", "64", "72", "80", "96"], 2,
    "Let width be \( w \) and length be \( 2w \). Perimeter is \( 2(w + 2w) = 6w \).",
    "افرض أن العرض \( w \) والطول \( 2w \). المحيط هو \( 2(w + 2w) = 6w \).",
    "\( 6w = 36 \\implies w = 6 \\text{ cm} \), length = \( 12 \\text{ cm} \). Area = \( 6 \\times 12 = 72 \\text{ cm}^2 \).",
    "\( 6w = 36 \\implies w = 6 \\text{ سم} \)، والطول = \( 12 \\text{ سم} \). المساحة = \( 6 \\times 12 = 72 \\text{ سم}^2 \).")

add("kangaroo", "KANGAROO-243", "Cadet", "Logic Puzzles", "easy",
    "A standard digital clock displays time in 24-hour format from 00:00 to 23:59. How many times during a full day do all four digits on the display match?",
    "ساعة رقمية تعرض الوقت بنظام 24 ساعة من 00:00 إلى 23:59. كم مرة في اليوم الواحد تتطابق جميع الأرقام الأربعة على الشاشة؟",
    ["1", "2", "3", "4", "5"], 2,
    "Check all four-digit matches: hours can only range from 00 to 23.",
    "افحص الأوقات التي تتطابق فيها الأرقام: الساعات تتراوح فقط من 00 إلى 23.",
    "The matching times are 00:00, 11:11, and 22:22 (33:33 is impossible). Total = 3 times.",
    "الأوقات المتطابقة هي 00:00، 11:11، 22:22 (لا يمكن ظهور 33:33). المجموع = 3 مرات.")

# 5 Benjamin Tournaments
add("kangaroo", "KANG-BENJ-012", "Benjamin", "Fractions", "easy",
    "A pizza is sliced into \( 8 \) equal pieces. Adam eats \( 3 \) pieces and Maya eats \( 2 \) pieces. What fraction of the pizza is left?",
    "قُسمت فطيرة بيتزا إلى \( 8 \) قطع متساوية. أكل آدم \( 3 \) قطع وأكلت مايا قطعتين. ما الكسر الذي يمثل الجزء المتبقي من البيتزا؟",
    ["\\frac{1}{8}", "\\frac{1}{4}", "\\frac{3}{8}", "\\frac{1}{2}", "\\frac{5}{8}"], 2,
    "Subtract the total pieces eaten from 8.",
    "اطرح مجموع القطع المأكولة من 8.",
    "Eaten = \( 3 + 2 = 5 \) pieces. Remaining = \( 8 - 5 = 3 \) pieces, so fraction is \( \\frac{3}{8} \).",
    "المأكول = \( 3 + 2 = 5 \) قطع. المتبقي = \( 8 - 5 = 3 \) قطع، إذن الكسر هو \( \\frac{3}{8} \).")

add("kangaroo", "KANG-BENJ-017", "Benjamin", "Geometry", "medium",
    "A wire of length \( 48 \\text{ cm} \) is bent to form a square. What is the area of this square in \( \\text{cm}^2 \)?",
    "سلك طوله \( 48 \\text{ سم} \) ثُني ليشكل مربعًا. ما مساحة هذا المربع بالـ \( \\text{سم}^2 \)؟",
    ["96", "120", "144", "160", "196"], 2,
    "The perimeter of the square is 48 cm. Divide by 4 to get side length, then square it.",
    "محيط المربع 48 سم. اقسم على 4 لإيجاد طول الضلع، ثم احسب مربعه.",
    "Side = \( 48 / 4 = 12 \\text{ cm} \). Area = \( 12^2 = 144 \\text{ cm}^2 \).",
    "طول الضلع = \( 48 / 4 = 12 \\text{ سم} \). المساحة = \( 12^2 = 144 \\text{ سم}^2 \).")

add("kangaroo", "KANG-BENJ-022", "Benjamin", "Time and Calendar", "easy",
    "If today is Tuesday, what day of the week will it be \( 50 \) days from today?",
    "إذا كان اليوم هو الثلاثاء، فما اليوم الذي سيكون بعد \( 50 \) يومًا من اليوم؟",
    ["\\text{Tuesday}", "\\text{Wednesday}", "\\text{Thursday}", "\\text{Friday}", "\\text{Saturday}"], 1,
    "Divide 50 by 7 to find the remainder of days after full weeks.",
    "اقسم 50 على 7 لإيجاد عدد الأيام المتبقية بعد الأسابيع الكاملة.",
    "\( 50 = 7 \\times 7 + 1 \). One day after Tuesday is Wednesday.",
    "\( 50 = 7 \\times 7 + 1 \). اليوم التالي ليوم الثلاثاء هو الأربعاء.")

add("kangaroo", "KANG-BENJ-027", "Benjamin", "Number Puzzles", "medium",
    "The product of the ages of three siblings is \( 36 \). If their ages are three distinct whole numbers, what is the maximum possible sum of their ages?",
    "حاصل ضرب أعمار ثلاثة أشقاء يساوي \( 36 \). إذا كانت أعمارهم ثلاثة أعداد كلية مختلفة تمامًا، فما أكبر مجموع ممكن لأعمارهم؟",
    ["13", "14", "16", "21", "24"], 3,
    "Find distinct positive factor triples of 36 and compute their sums.",
    "أوجد ثلاثيات العوامل الموجبة المختلفة للعدد 36 واحسب مجموعها.",
    "The triple \( (1, 2, 18) \) has distinct entries, product 36, and sum \( 1 + 2 + 18 = 21 \).",
    "الثلاثية \( (1, 2, 18) \) عناصرها مختلفة وحاصل ضربها 36 ومجموعها \( 1 + 2 + 18 = 21 \).")

add("kangaroo", "KANG-BENJ-032", "Benjamin", "Counting", "medium",
    "How many squares of any size are there in total on a \( 3 \\times 3 \) grid made of unit squares?",
    "كم مربعًا بمختلف الأحجام يوجد في شبكة مربعات \( 3 \\times 3 \) المكونة من مربعات وحدة؟",
    ["9", "10", "12", "14", "16"], 3,
    "Count squares of sizes \( 1 \\times 1 \), \( 2 \\times 2 \), and \( 3 \\times 3 \).",
    "عد المربعات ذات الأحجام \( 1 \\times 1 \) و\( 2 \\times 2 \) و\( 3 \\times 3 \).",
    "\( 3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14 \) squares.",
    "\( 3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14 \) مربعًا.")

# 18 Benjamin Wire Triangles
add("kangaroo", "KANG-BENJ-015", "Benjamin", "Geometry", "medium",
    "An L-shaped figure is formed by cutting a \( 2 \\times 2 \\text{ cm} \) square from one corner of a \( 6 \\times 6 \\text{ cm} \) square. What is the perimeter of this L-shaped figure?",
    "شكل على هيئة حرف L نتج عن قص مربع أبعاده \( 2 \\times 2 \\text{ سم} \) من ركن مربع أبعاده \( 6 \\times 6 \\text{ سم} \). ما محيط هذا الشكل الناتج؟",
    ["20", "22", "24", "28", "32"], 2,
    "Cutting a corner square does not change the perimeter of the original square.",
    "قص مربع من الركن لا يغير محيط المربع الأصلي.",
    "The perimeter equals that of the original square: \( 4 \\times 6 = 24 \\text{ cm} \).",
    "المحيط يساوي محيط المربع الأصلي: \( 4 \\times 6 = 24 \\text{ سم} \).")

add("kangaroo", "KANG-BENJ-020", "Benjamin", "Spatial Reasoning", "easy",
    "On a standard die, the numbers on opposite faces always sum to \( 7 \). What is the sum of the numbers on the faces opposite to \( 2 \), \( 4 \), and \( 5 \)?",
    "في نرد الأرقام المنتظم، مجموع كل وجهين متقابلين يساوي دائمًا \( 7 \). ما مجموع الأرقام الموجودة على الأوجه المقابلة للأوجه \( 2 \) و\( 4 \) و\( 5 \)؟",
    ["8", "9", "10", "11", "12"], 2,
    "Opposite to 2 is 5, opposite to 4 is 3, opposite to 5 is 2.",
    "المقابل للعدد 2 هو 5، والمقابل للعدد 4 هو 3، والمقابل للعدد 5 هو 2.",
    "\( (7 - 2) + (7 - 4) + (7 - 5) = 5 + 3 + 2 = 10 \).",
    "\( 5 + 3 + 2 = 10 \).")

add("kangaroo", "KANG-BENJ-025", "Benjamin", "Logic", "easy",
    "In a single-file line of \( 15 \) children, Tariq is \( 5^{\\text{th}} \) from the front. How many children are behind Tariq?",
    "في طابور من \( 15 \) طفلاً، ترتيب طارق هو الخامس من البداية. كم طفلاً يقف خلف طارق؟",
    ["9", "10", "11", "12", "14"], 1,
    "Subtract Tariq's position from the total number of children.",
    "اطرح ترتيب طارق من العدد الكلي للأطفال.",
    "\( 15 - 5 = 10 \) children are behind him.",
    "\( 15 - 5 = 10 \) أطفال يقفون خلفه.")

add("kangaroo", "KANG-BENJ-030", "Benjamin", "Number Theory", "easy",
    "How many prime numbers are there strictly between \( 20 \) and \( 35 \)?",
    "كم عددًا أوليًا يقع تمامًا بين \( 20 \) و\( 35 \)؟",
    ["2", "3", "4", "5", "6"], 1,
    "Test integers in this interval: 23, 29, and 31.",
    "افحص الأعداد في هذه الفترة: 23 و29 و31.",
    "The prime numbers are \( 23, 29, 31 \), so there are \( 3 \) primes.",
    "الأعداد الأولية هي \( 23, 29, 31 \)، وعددها \( 3 \).")

add("kangaroo", "KANG-BENJ-035", "Benjamin", "Word Problems", "easy",
    "Nasser has \( 6 \) riyals more than Layla. Together they have \( 38 \) riyals. How many riyals does Layla have?",
    "لدى ناصر \( 6 \) ريالات أكثر مما لدى ليلى. ومعهما معًا \( 38 \) ريالاً. كم ريالاً لدى ليلى؟",
    ["12", "14", "16", "18", "22"], 2,
    "Subtract the difference first, then divide equally.",
    "اطرح مقدار الزيادة أولاً، ثم اقسم بالتساوي.",
    "\( (38 - 6) / 2 = 32 / 2 = 16 \) riyals.",
    "\( (38 - 6) / 2 = 32 / 2 = 16 \) ريالاً.")

add("kangaroo", "KANG-BENJ-040", "Benjamin", "Geometry", "easy",
    "What is the angle formed between the hour hand and the minute hand of a clock at exactly 3:00?",
    "ما قياس الزاوية المتكونة بين عقربي الساعات والدقائق عند الساعة 3:00 تمامًا؟",
    ["45^\\circ", "60^\\circ", "90^\\circ", "120^\\circ", "180^\\circ"], 2,
    "The hands point directly at 12 and 3, which is one quarter of a full circle.",
    "يشير العقربان إلى 12 و3 تمامًا، وهو ما يمثل ربع دائرة كاملة.",
    "\( \\frac{360^\\circ}{4} = 90^\\circ \).",
    "\( \\frac{360^\\circ}{4} = 90^\\circ \).")

add("kangaroo", "KANG-BENJ-045", "Benjamin", "Symmetry", "easy",
    "Which of the following capital English letters has both a horizontal and a vertical line of reflection symmetry?",
    "أي من الحروف الإنجليزية الكبيرة الآتية له خط تماثل انعكاسي أفقي وخط تماثل رأسي معًا؟",
    ["A", "B", "C", "H", "V"], 3,
    "Check reflection across both horizontal and vertical midlines.",
    "افحص الانعكاس حول الخطين الأفقي والرأسي.",
    "The letter 'H' can be reflected across both axes onto itself.",
    "الحرف 'H' ينطبق على نفسه بالانعكاس حول المحورين الأفقي والرأسي.")

add("kangaroo", "KANG-BENJ-050", "Benjamin", "Fractions", "easy",
    "What is \( \\frac{3}{4} \) of \( 60 \) minutes?",
    "ما قيمة \( \\frac{3}{4} \) من \( 60 \) دقيقة؟",
    ["30", "40", "45", "50", "55"], 2,
    "Divide 60 by 4, then multiply by 3.",
    "اقسم 60 على 4 ثم اضرب الناتج في 3.",
    "\( \\frac{60}{4} \\times 3 = 15 \\times 3 = 45 \) minutes.",
    "\( 15 \\times 3 = 45 \) دقيقة.")

add("kangaroo", "KANG-BENJ-055", "Benjamin", "Combinatorics", "easy",
    "Four friends each shake hands with every other friend exactly once. How many total handshakes occur?",
    "صافح أربعة أصدقاء بعضهم بعضًا، بحيث صافح كل صديق كل صديق آخر مرة واحدة فقط. كم مصافحة تمت في المجموع؟",
    ["4", "6", "8", "10", "12"], 1,
    "Use \( \\binom{n}{2} = \\frac{n(n-1)}{2} \) for \( n = 4 \).",
    "استخدم القانون \( \\binom{n}{2} = \\frac{n(n-1)}{2} \) عندما \( n = 4 \).",
    "\( \\frac{4 \\times 3}{2} = 6 \) handshakes.",
    "\( \\frac{4 \\times 3}{2} = 6 \) مصافحات.")

add("kangaroo", "KANG-BENJ-060", "Benjamin", "Speed and Measurement", "easy",
    "A cyclist travels at a constant speed of \( 18 \\text{ km/h} \). How many meters does the cyclist travel in one minute?",
    "يسير دراج بسرعة ثابتة قدرها \( 18 \\text{ كم/ساعة} \). كم مترًا يقطع الدراج في دقيقة واحدة؟",
    ["180 \\text{ m}", "250 \\text{ m}", "300 \\text{ m}", "350 \\text{ m}", "400 \\text{ m}"], 2,
    "Convert km to meters and hours to minutes: \( 18000 \\text{ m} / 60 \\text{ min} \).",
    "حوّل الكيلومترات إلى أمتار والساعات إلى دقائق: \( 18000 \\text{ م} / 60 \\text{ دقيقة} \).",
    "\( \\frac{18{,}000 \\text{ m}}{60 \\text{ min}} = 300 \\text{ m/min} \).",
    "\( \\frac{18{,}000}{60} = 300 \\text{ مترًا} \).")

add("kangaroo", "KANG-BENJ-065", "Benjamin", "Patterns", "easy",
    "What is the next number in the pattern: \( 2, 5, 11, 23, 47, \\ldots \)?",
    "ما العدد التالي في النمط: \( 2, 5, 11, 23, 47, \\ldots \)؟",
    ["71", "89", "94", "95", "96"], 3,
    "Each number is obtained by doubling the previous number and adding 1: \( 2n + 1 \).",
    "كل عدد ينتج عن مضاعفة العدد السابق وإضافة 1: \( 2n + 1 \).",
    "\( 47 \\times 2 + 1 = 94 + 1 = 95 \).",
    "\( 47 \\times 2 + 1 = 94 + 1 = 95 \).")

add("kangaroo", "KANG-BENJ-070", "Benjamin", "Volume", "medium",
    "The total surface area of a solid cube is \( 54 \\text{ cm}^2 \). What is the volume of the cube in \( \\text{cm}^3 \)?",
    "مساحة السطح الكلية لمكعب مصمت هي \( 54 \\text{ سم}^2 \). ما حجم المكعب بالـ \( \\text{سم}^3 \)؟",
    ["9", "18", "27", "36", "81"], 2,
    "A cube has 6 faces: \( 6s^2 = 54 \\implies s = 3 \). Volume is \( s^3 \).",
    "للمكعب 6 أوجه متطابقة: \( 6s^2 = 54 \\implies s = 3 \). الحجم هو \( s^3 \).",
    "\( s = 3 \\text{ cm} \\implies V = 3^3 = 27 \\text{ cm}^3 \).",
    "\( s = 3 \\text{ سم} \\implies V = 3^3 = 27 \\text{ سم}^3 \).")

add("kangaroo", "KANG-BENJ-075", "Benjamin", "Logic Puzzles", "easy",
    "On a balance scale, \( 2 \) apples and \( 1 \) orange balance with \( 7 \) plums. If \( 1 \) orange balances with \( 3 \) plums, how many plums balance with \( 1 \) apple?",
    "في ميزان متزن، تفاحتان وبرتقالة تتزن مع \( 7 \) خوخات. إذا كانت البرتقالة الواحدة تتزن مع \( 3 \) خوخات، فكم خوخة تتزن مع تفاحة واحدة؟",
    ["1", "2", "3", "4", "5"], 1,
    "Substitute 3 plums for the orange: \( 2 \\text{ apples} + 3 = 7 \).",
    "عوض عن البرتقالة بـ 3 خوخات: تفاحتان + 3 = 7.",
    "\( 2 \\text{ apples} = 7 - 3 = 4 \\text{ plums} \\implies 1 \\text{ apple} = 2 \\text{ plums} \).",
    "تفاحتان = 4 خوخات، إذن التفاحة الواحدة = خوختان.")

add("kangaroo", "KANG-BENJ-080", "Benjamin", "Geometry", "easy",
    "A right triangle has legs of length \( 6 \\text{ cm} \) and \( 8 \\text{ cm} \). What is its area in \( \\text{cm}^2 \)?",
    "مثلث قائم الزاوية طولا ضلعي القائمة فيه هما \( 6 \\text{ سم} \) و\( 8 \\text{ سم} \). ما مساحته بالـ \( \\text{سم}^2 \)؟",
    ["14", "24", "28", "48", "50"], 1,
    "For a right triangle, Area = \( \\frac{1}{2} \\times \\text{leg}_1 \\times \\text{leg}_2 \).",
    "لمثلث قائم، المساحة = \( \\frac{1}{2} \\times \\text{ضلع}_1 \\times \\text{ضلع}_2 \).",
    "\( \\text{Area} = \\frac{1}{2} \\times 6 \\times 8 = 24 \\text{ cm}^2 \).",
    "\( \\text{المساحة} = \\frac{1}{2} \\times 6 \\times 8 = 24 \\text{ سم}^2 \).")

add("kangaroo", "KANG-BENJ-085", "Benjamin", "Consecutive Numbers", "easy",
    "The sum of three consecutive whole numbers is \( 42 \). What is the largest of these three numbers?",
    "مجموع ثلاثة أعداد كلية متتالية هو \( 42 \). ما أكبر هذه الأعداد الثلاثة؟",
    ["13", "14", "15", "16", "17"], 2,
    "Let the numbers be \( n-1, n, n+1 \). Their sum is \( 3n = 42 \).",
    "افرض الأعداد \( n-1, n, n+1 \). مجموعها \( 3n = 42 \).",
    "\( 3n = 42 \\implies n = 14 \). The numbers are 13, 14, 15; largest is 15.",
    "\( n = 14 \). الأعداد هي 13 و14 و15؛ أكبرها 15.")

add("kangaroo", "KANG-BENJ-090", "Benjamin", "Polygons", "easy",
    "How many edges does a pyramid with a square base have in total?",
    "كم حافة (ضلعًا) للهرم ذي القاعدة المربعة في المجموع؟",
    ["4", "5", "6", "8", "10"], 3,
    "Count the 4 edges of the base plus the 4 edges meeting at the top apex.",
    "عد أضلاع القاعدة الأربعة بالإضافة إلى الحواف الأربعة الصاعدة نحو القمة.",
    "\( 4 + 4 = 8 \) edges.",
    "\( 4 + 4 = 8 \) حواف.")

add("kangaroo", "KANG-BENJ-095", "Benjamin", "Digit Puzzles", "medium",
    "What is the sum of the digits of the number \( 10^{20} - 1 \)?",
    "ما مجموع أرقام العدد الناتج عن \( 10^{20} - 1 \)؟",
    ["90", "171", "180", "189", "198"], 2,
    "\( 10^{20} - 1 \) consists of 20 consecutive nines: \( 999\\ldots9 \).",
    "العدد \( 10^{20} - 1 \) يتكون من 20 تسعة متتالية: \( 999\\ldots9 \).",
    "Sum = \( 20 \\times 9 = 180 \).",
    "المجموع = \( 20 \\times 9 = 180 \).")

add("kangaroo", "KANG-BENJ-100", "Benjamin", "Probability", "easy",
    "A jar contains \( 5 \) blue, \( 3 \) red, and \( 2 \) green marbles. What is the probability of drawing a blue marble at random?",
    "وعاء يحتوي على \( 5 \) كرات زرقاء و\( 3 \) حمراء وكرتين خضراوين. ما احتمال سحب كرة زرقاء عشوائيًا؟",
    ["\\frac{1}{5}", "\\frac{3}{10}", "\\frac{1}{2}", "\\frac{3}{5}", "\\frac{7}{10}"], 2,
    "Divide the number of blue marbles by the total marbles in the jar.",
    "اقسم عدد الكرات الزرقاء على العدد الإجمالي للكرات في الوعاء.",
    "Total = \( 5 + 3 + 2 = 10 \). Probability = \( 5/10 = 1/2 \).",
    "الإجمالي = 10. الاحتمال = \( 5/10 = 1/2 \).")

# 7 Junior Coprimes
add("kangaroo", "KANG-JUN-019", "Junior", "Number Theory", "easy",
    "What is the remainder when \( 3^{50} \) is divided by \( 8 \)?",
    "ما باقي قسمة \( 3^{50} \) على \( 8 \)؟",
    ["1", "3", "5", "7", "0"], 0,
    "Notice that \( 3^2 = 9 \\equiv 1 \\pmod{8} \).",
    "لاحظ أن \( 3^2 = 9 \\equiv 1 \\pmod{8} \).",
    "\( 3^{50} = (3^2)^{25} = 9^{25} \\equiv 1^{25} = 1 \\pmod{8} \).",
    "\( 3^{50} = (3^2)^{25} \\equiv 1^{25} = 1 \\pmod{8} \).")

add("kangaroo", "KANG-JUN-031", "Junior", "Number Theory", "easy",
    "How many positive factors (divisors) does the integer \( 360 \) have?",
    "كم قاسمًا موجبًا (عاملًا) للعدد الصحيح \( 360 \)؟",
    ["18", "20", "24", "28", "36"], 2,
    "Prime factorize: \( 360 = 2^3 \\times 3^2 \\times 5^1 \).",
    "حلل إلى العوامل الأولية: \( 360 = 2^3 \\times 3^2 \\times 5^1 \).",
    "Number of divisors = \( (3+1)(2+1)(1+1) = 4 \\times 3 \\times 2 = 24 \).",
    "عدد القواسم = \( (3+1)(2+1)(1+1) = 4 \\times 3 \\times 2 = 24 \).")

add("kangaroo", "KANG-JUN-043", "Junior", "Number Theory", "easy",
    "What is the units digit of \( 7^{2024} \)?",
    "ما رقم الآحاد للعدد \( 7^{2024} \)؟",
    ["1", "3", "7", "9", "5"], 0,
    "The powers of 7 have units digits cycling in a period of 4: 7, 9, 3, 1.",
    "أرقام آحاد قوى العدد 7 تتكرر في دورة طولها 4: 7، 9، 3، 1.",
    "Since \( 2024 \) is divisible by 4, the units digit is the 4th in the cycle: 1.",
    "بما أن 2024 يقبل القسمة على 4، فإن رقم الآحاد هو 1.")

add("kangaroo", "KANG-JUN-055", "Junior", "Number Theory", "easy",
    "What is the greatest common divisor \( \\gcd(252, 198) \)?",
    "ما القاسم المشترك الأكبر \( \\gcd(252, 198) \)؟",
    ["9", "12", "18", "24", "36"], 2,
    "Apply the Euclidean algorithm: \( 252 - 198 = 54 \).",
    "طبق خوارزمية إقليدس: \( 252 - 198 = 54 \).",
    "\( \\gcd(198, 54) = \\gcd(54, 36) = \\gcd(36, 18) = 18 \).",
    "\( \\gcd(252, 198) = 18 \).")

add("kangaroo", "KANG-JUN-067", "Junior", "Number Theory", "easy",
    "What is the least common multiple \( \\operatorname{lcm}(24, 36) \)?",
    "ما المضاعف المشترك الأصغر \( \\operatorname{lcm}(24, 36) \)؟",
    ["48", "60", "72", "96", "144"], 2,
    "Take the highest power of each prime factor: \( 2^3 \\times 3^2 \).",
    "خذ أعلى قوة لكل عامل أولي: \( 2^3 \\times 3^2 \).",
    "\( \\operatorname{lcm}(24, 36) = 8 \\times 9 = 72 \).",
    "\( \\operatorname{lcm}(24, 36) = 72 \).")

add("kangaroo", "KANG-JUN-079", "Junior", "Number Theory", "medium",
    "What is the smallest positive integer that leaves a remainder of \( 2 \) when divided by \( 3 \), and a remainder of \( 3 \) when divided by \( 5 \)?",
    "ما أصغر عدد صحيح موجب يعطي باقيًا قدره \( 2 \) عند قسمته على \( 3 \)، وباقيًا قدره \( 3 \) عند قسمته على \( 5 \)؟",
    ["8", "13", "18", "23", "28"], 0,
    "Test numbers congruent to 3 mod 5: 3, 8, 13... for remainder 2 mod 3.",
    "افحص الأعداد التي تكافئ 3 موديولو 5: 3، 8، 13... وباقيها 2 عند القسمة على 3.",
    "\( 8 \\div 3 = 2 \) R \( 2 \), and \( 8 \\div 5 = 1 \) R \( 3 \). Smallest is 8.",
    "\( 8 \\div 3 = 2 \) والباقي \( 2 \)، و\( 8 \\div 5 = 1 \) والباقي \( 3 \). الأصغر هو 8.")

add("kangaroo", "KANG-JUN-091", "Junior", "Number Theory", "medium",
    "Find the number of trailing zeros at the end of \( 25! \) (25 factorial).",
    "أوجد عدد الأصفار المتتالية في نهاية العدد \( 25! \) (مضروب 25).",
    ["4", "5", "6", "7", "8"], 2,
    "Count the powers of 5 dividing 25! using Legendre's formula.",
    "عد قوى العدد 5 التي تقسم مضروب 25 باستخدام صيغة ليجاندر.",
    "\( \\lfloor 25/5 \\rfloor + \\lfloor 25/25 \\rfloor = 5 + 1 = 6 \) zeros.",
    "\( 5 + 1 = 6 \) أصفار.")

# 23 Junior Trapezoids
add("kangaroo", "KANG-JUN-010", "Junior", "Geometry", "easy",
    "A circle is inscribed in a square of area \( 64 \\text{ cm}^2 \). What is the area of the circle in \( \\text{cm}^2 \)?",
    "دائرة مُمَاسة من الداخل لأضلاع مربع مساحته \( 64 \\text{ سم}^2 \). ما مساحة الدائرة بالـ \( \\text{سم}^2 \)؟",
    ["8\\pi", "12\\pi", "16\\pi", "24\\pi", "32\\pi"], 2,
    "Square side is \( \\sqrt{64} = 8 \\text{ cm} \), so circle radius is \( r = 4 \\text{ cm} \).",
    "طول ضلع المربع هو 8 سم، وبالتالي نصف قطر الدائرة هو 4 سم.",
    "\( \\text{Area} = \\pi r^2 = \\pi (4^2) = 16\\pi \\text{ cm}^2 \).",
    "\( \\text{المساحة} = 16\\pi \\text{ سم}^2 \).")

add("kangaroo", "KANG-JUN-014", "Junior", "Geometry", "easy",
    "In a right triangle \( ABC \), the hypotenuse measures \( 10 \\text{ cm} \). What is the length of the median drawn to the hypotenuse?",
    "في مثلث قائم الزاوية، طول الوتر يساوي \( 10 \\text{ سم} \). ما طول المتوسط المرسوم إلى الوتر؟",
    ["4 \\text{ cm}", "5 \\text{ cm}", "6 \\text{ cm}", "7.5 \\text{ cm}", "8 \\text{ cm}"], 1,
    "The median to the hypotenuse of any right triangle equals half the length of the hypotenuse.",
    "طول المتوسط المتعلق بالوتر في المثلث القائم يساوي دائمًا نصف طول الوتر.",
    "\( m = \\frac{10}{2} = 5 \\text{ cm} \).",
    "\( m = \\frac{10}{2} = 5 \\text{ سم} \).")

add("kangaroo", "KANG-JUN-018", "Junior", "Geometry", "medium",
    "Two tangent segments from an external point \( P \) touch a circle at \( A \) and \( B \). If \( \\angle APB = 60^\\circ \) and the circle's radius is \( 6 \\text{ cm} \), what is the length of segment \( PA \)?",
    "مماسان مرسومان من نقطة خارجية \( P \) يماسان دائرة عند \( A \) و\( B \). إذا كان قياس الزاوية \( \\angle APB = 60^\\circ \) ونصف قطر الدائرة \( 6 \\text{ سم} \)، فما طول القطعة المماسة \( PA \)؟",
    ["6", "6\\sqrt{2}", "6\\sqrt{3}", "12", "12\\sqrt{3}"], 2,
    "Line \( OP \) bisects \( \\angle APB \), creating a \( 30^\\circ-60^\\circ-90^\\circ \) right triangle \( OAP \).",
    "الخط \( OP \) ينصف الزاوية إلى \( 30^\\circ \)، مما ينتج مثلثًا قائمًا ثلاثينيًا ستينيًا.",
    "\( PA = \\frac{r}{\\tan(30^\\circ)} = \\frac{6}{1/\\sqrt{3}} = 6\\sqrt{3} \\text{ cm} \).",
    "\( PA = 6\\sqrt{3} \\text{ سم} \).")

add("kangaroo", "KANG-JUN-022", "Junior", "Geometry", "easy",
    "What is the sum of the interior angles of a convex hexagon?",
    "ما مجموع قياسات الزوايا الداخلية لمضلع سداسي محدب؟",
    ["540^\\circ", "600^\\circ", "720^\\circ", "900^\\circ", "1080^\\circ"], 2,
    "Use the polygon angle sum formula: \( (n - 2) \\times 180^\\circ \) for \( n = 6 \).",
    "استخدم صيغة مجموع زوايا المضلع: \( (n - 2) \\times 180^\\circ \) مع \( n = 6 \).",
    "\( (6 - 2) \\times 180^\\circ = 4 \\times 180^\\circ = 720^\\circ \).",
    "\( 4 \\times 180^\\circ = 720^\\circ \).")

add("kangaroo", "KANG-JUN-026", "Junior", "Geometry", "medium",
    "A rhombus has diagonals of lengths \( 10 \\text{ cm} \) and \( 24 \\text{ cm} \). What is the perimeter of the rhombus in \( \\text{cm} \)?",
    "معين طولا قطريه \( 10 \\text{ سم} \) و\( 24 \\text{ سم} \). ما محيط المعين بالـ \( \\text{سم} \)؟",
    ["48", "50", "52", "60", "68"], 2,
    "The diagonals bisect each other perpendicularly, forming right triangles with legs 5 and 12.",
    "القطران ينصف كل منهما الآخر ويتعامدان، مكونين مثلثات قائمة أطوال أضلاعها 5 و12.",
    "Side = \( \\sqrt{5^2 + 12^2} = 13 \\text{ cm} \\implies \\text{Perimeter} = 4 \\times 13 = 52 \\text{ cm} \).",
    "طول الضلع = 13 سم، إذن المحيط = \( 4 \\times 13 = 52 \\text{ سم} \).")

add("kangaroo", "KANG-JUN-030", "Junior", "Algebra", "easy",
    "If \( x + y = 10 \) and \( xy = 21 \), what is the value of \( x^2 + y^2 \)?",
    "إذا كان \( x + y = 10 \) و\( xy = 21 \)، فما قيمة \( x^2 + y^2 \)؟",
    ["42", "50", "58", "64", "79"], 2,
    "Use the algebraic identity \( x^2 + y^2 = (x + y)^2 - 2xy \).",
    "استخدم المتطابقة الجبرية \( x^2 + y^2 = (x + y)^2 - 2xy \).",
    "\( x^2 + y^2 = 10^2 - 2(21) = 100 - 42 = 58 \).",
    "\( x^2 + y^2 = 100 - 42 = 58 \).")

add("kangaroo", "KANG-JUN-034", "Junior", "Algebra", "easy",
    "Find the sum of the roots of the quadratic equation \( 2x^2 - 14x + 15 = 0 \).",
    "أوجد مجموع جذري المعادلة التربيعية الآتية: \( 2x^2 - 14x + 15 = 0 \).",
    ["5", "7", "-7", "7.5", "15"], 1,
    "By Vieta's formulas, the sum of roots is \( -b / a \).",
    "وفقًا لعلاقات فييتا، مجموع الجذور يساوي \( -b / a \).",
    "\( -\\frac{-14}{2} = 7 \).",
    "\( -\\frac{-14}{2} = 7 \).")

add("kangaroo", "KANG-JUN-038", "Junior", "Algebra", "medium",
    "If \( 2^a = 3 \) and \( 3^b = 8 \), what is the value of the product \( ab \)?",
    "إذا كان \( 2^a = 3 \) و\( 3^b = 8 \)، فما قيمة حاصل الضرب \( ab \)؟",
    ["2", "3", "4", "5", "6"], 1,
    "Substitute \( 3 \) into the second equation: \( (2^a)^b = 2^{ab} \).",
    "عوض عن 3 في المعادلة الثانية: \( (2^a)^b = 2^{ab} \).",
    "\( 2^{ab} = 8 = 2^3 \\implies ab = 3 \).",
    "\( 2^{ab} = 8 = 2^3 \\implies ab = 3 \).")

add("kangaroo", "KANG-JUN-042", "Junior", "Algebra", "easy",
    "Solve the radical equation for \( x \): \( \\sqrt{x + 5} = 4 \).",
    "حل المعادلة الجذرية الآتية لإيجاد \( x \): \( \\sqrt{x + 5} = 4 \).",
    ["9", "11", "16", "21", "25"], 1,
    "Square both sides to remove the radical sign.",
    "ربّع الطرفين للتخلص من علامة الجذر.",
    "\( x + 5 = 4^2 = 16 \\implies x = 16 - 5 = 11 \).",
    "\( x + 5 = 16 \\implies x = 11 \).")

add("kangaroo", "KANG-JUN-046", "Junior", "Sequences", "easy",
    "In an arithmetic sequence, the \( 3^{\\text{rd}} \) term is \( 11 \) and the \( 7^{\\text{th}} \) term is \( 27 \). What is the common difference \( d \)?",
    "في متتالية حسابية، الحد الثالث يساوي \( 11 \) والحد السابع يساوي \( 27 \). ما أساس المتتالية \( d \)؟",
    ["2", "3", "4", "5", "6"], 2,
    "The difference between the two terms is \( a_7 - a_3 = 4d \).",
    "الفرق بين الحدين هو \( a_7 - a_3 = 4d \).",
    "\( 4d = 27 - 11 = 16 \\implies d = 4 \).",
    "\( 4d = 16 \\implies d = 4 \).")

add("kangaroo", "KANG-JUN-050", "Junior", "Sequences", "easy",
    "Find the sum of the first \( 20 \) positive even integers: \( 2 + 4 + 6 + \\cdots + 40 \).",
    "أوجد مجموع أول \( 20 \) عددًا زوجيًا موجبًا: \( 2 + 4 + 6 + \\cdots + 40 \).",
    ["380", "400", "420", "440", "460"], 2,
    "Use the formula for sum of first n even numbers: \( n(n+1) \).",
    "استخدم صيغة مجموع أول n عدد زوجي: \( n(n+1) \).",
    "\( 20 \\times 21 = 420 \).",
    "\( 20 \\times 21 = 420 \).")

add("kangaroo", "KANG-JUN-054", "Junior", "Combinatorics", "medium",
    "How many distinct diagonals does a regular convex decagon (\( 10 \)-sided polygon) have?",
    "كم قطرًا مميزًا لمضلع عشاري محدب منتظم (له 10 أضلاع)؟",
    ["25", "30", "35", "40", "45"], 2,
    "The number of diagonals of an n-gon is \( \\frac{n(n - 3)}{2} \).",
    "عدد أقطار المضلع الذي له n ضلعًا هو \( \\frac{n(n - 3)}{2} \).",
    "\( \\frac{10(10 - 3)}{2} = \\frac{10 \\times 7}{2} = 35 \).",
    "\( \\frac{10 \\times 7}{2} = 35 \).")

add("kangaroo", "KANG-JUN-058", "Junior", "Combinatorics", "easy",
    "In a race with \( 5 \) competitors, in how many distinct ways can the gold, silver, and bronze medals be awarded?",
    "في سباق يشارك فيه \( 5 \) متسابقين، بكم طريقة مختلفة يمكن منح الميداليات الذهبية والفضية والبرونزية؟",
    ["15", "30", "60", "120", "125"], 2,
    "Use permutations: \( P(5, 3) = 5 \\times 4 \\times 3 \).",
    "استخدم التباديل: \( P(5, 3) = 5 \\times 4 \\times 3 \).",
    "\( 5 \\times 4 \\times 3 = 60 \) ways.",
    "\( 5 \\times 4 \\times 3 = 60 \) طريقة.")

add("kangaroo", "KANG-JUN-062", "Junior", "Combinatorics", "easy",
    "How many total subsets (including the empty set and the set itself) does a set with \( 5 \) elements have?",
    "كم عدد المجموعات الجزئية الكلية لمجموعة تحتوي على \( 5 \) عناصر؟",
    ["10", "16", "25", "32", "64"], 3,
    "The number of subsets of an n-element set is \( 2^n \).",
    "عدد المجموعات الجزئية لمجموعة تحتوي على n عنصرًا هو \( 2^n \).",
    "\( 2^5 = 32 \) subsets.",
    "\( 2^5 = 32 \) مجموعة جزئية.")

add("kangaroo", "KANG-JUN-066", "Junior", "Probability", "medium",
    "A box contains \( 3 \) red, \( 4 \) blue, and \( 5 \) green pens. If two pens are drawn at random without replacement, what is the probability that both are green?",
    "صندوق يحتوي على \( 3 \) أقلام حمراء و\( 4 \) زرقاء و\( 5 \) خضراء. إذا سُحب قلمان عشوائيًا دون إرجاع، فما احتمال أن يكون كلاهما أخضر؟",
    ["\\frac{5}{33}", "\\frac{1}{6}", "\\frac{5}{36}", "\\frac{2}{11}", "\\frac{7}{33}"], 0,
    "Multiply the probability of first green by second green: \( \\frac{5}{12} \\times \\frac{4}{11} \).",
    "اضرب احتمال سحب القلم الأخضر الأول في احتمال الثاني: \( \\frac{5}{12} \\times \\frac{4}{11} \).",
    "\( \\frac{5}{12} \\times \\frac{4}{11} = \\frac{20}{132} = \\frac{5}{33} \).",
    "\( \\frac{5}{12} \\times \\frac{4}{11} = \\frac{5}{33} \).")

add("kangaroo", "KANG-JUN-070", "Junior", "Probability", "easy",
    "Two fair standard six-sided dice are rolled. What is the probability that the sum of the numbers shown is equal to \( 7 \)?",
    "أُلقي نردان منتظمان ذوا ستة أوجه. ما احتمال أن يكون مجموع العددين الظاهرين مساويًا لـ \( 7 \)؟",
    ["\\frac{1}{12}", "\\frac{1}{9}", "\\frac{1}{6}", "\\frac{5}{36}", "\\frac{7}{36}"], 2,
    "There are 6 favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) out of 36.",
    "توجد 6 نواتج مناسبة من أصل 36 ناتجًا ممكنًا.",
    "\( \\frac{6}{36} = \\frac{1}{6} \).",
    "\( \\frac{6}{36} = \\frac{1}{6} \).")

add("kangaroo", "KANG-JUN-074", "Junior", "Coordinate Geometry", "easy",
    "What is the slope of the straight line passing through the points \( A(-1, 3) \) and \( B(3, 11) \)?",
    "ما ميل المستقيم المار بالنقطتين \( A(-1, 3) \) و\( B(3, 11) \)؟",
    ["1", "2", "3", "4", "\\frac{1}{2}"], 1,
    "Use the slope formula: \( m = \\frac{y_2 - y_1}{x_2 - x_1} \).",
    "استخدم صيغة الميل: \( m = \\frac{y_2 - y_1}{x_2 - x_1} \).",
    "\( m = \\frac{11 - 3}{3 - (-1)} = \\frac{8}{4} = 2 \).",
    "\( m = \\frac{11 - 3}{3 - (-1)} = \\frac{8}{4} = 2 \).")

add("kangaroo", "KANG-JUN-078", "Junior", "Coordinate Geometry", "easy",
    "Find the straight-line distance between the points \( P(1, 1) \) and \( Q(4, 5) \) in the Cartesian plane.",
    "أوجد المسافة المستقيمة بين النقطتين \( P(1, 1) \) و\( Q(4, 5) \) في المستوى الإحداثي.",
    ["3", "4", "5", "6", "7"], 2,
    "Use the distance formula: \( d = \\sqrt{\\Delta x^2 + \\Delta y^2} \).",
    "استخدم قانون المسافة: \( d = \\sqrt{\\Delta x^2 + \\Delta y^2} \).",
    "\( d = \\sqrt{(4-1)^2 + (5-1)^2} = \\sqrt{9 + 16} = 5 \).",
    "\( d = \\sqrt{9 + 16} = 5 \).")

add("kangaroo", "KANG-JUN-082", "Junior", "Percentages", "medium",
    "An item originally priced at \( 100 \) riyals has its price increased by \( 20\\% \), and then the new price is decreased by \( 20\\% \). What is the final price?",
    "سلعة سعرها الأصلي \( 100 \) ريال زاد سعرها بنسبة \( 20\\% \)، ثم خُفّض السعر الجديد بنسبة \( 20\\% \). ما السعر النهائي للسلعة؟",
    ["94 \\text{ riyals}", "96 \\text{ riyals}", "98 \\text{ riyals}", "100 \\text{ riyals}", "104 \\text{ riyals}"], 1,
    "Compute step-by-step: \( 100 \\times 1.20 = 120 \), then reduce by 20%.",
    "احسب خطوة بخطوة: \( 100 \\times 1.20 = 120 \)، ثم اخفض بنسبة 20%.",
    "\( 120 \\times 0.80 = 96 \\text{ riyals} \).",
    "\( 120 \\times 0.80 = 96 \\text{ ريالاً} \).")

add("kangaroo", "KANG-JUN-086", "Junior", "Word Problems", "medium",
    "Two water taps can fill an empty pool. Tap A takes \( 3 \) hours and Tap B takes \( 6 \) hours. How many hours will it take to fill the pool if both taps run together?",
    "صنبوران يملآن مسبحًا فارغًا. الصنبور الأول يستغرق \( 3 \) ساعات والثاني \( 6 \) ساعات. كم ساعة يستغرق ملء المسبح إذا فُتح الصنبوران معًا؟",
    ["1.5 \\text{ hours}", "2 \\text{ hours}", "2.5 \\text{ hours}", "4.5 \\text{ hours}", "5 \\text{ hours}"], 1,
    "Add their work rates: \( \\frac{1}{3} + \\frac{1}{6} = \\frac{1}{T} \).",
    "اجمع معدلي التدفق: \( \\frac{1}{3} + \\frac{1}{6} = \\frac{1}{T} \).",
    "\( \\frac{1}{3} + \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2} \\implies T = 2 \\text{ hours} \).",
    "\( \\frac{1}{3} + \\frac{1}{6} = \\frac{1}{2} \\implies T = 2 \\text{ ساعتان} \).")

add("kangaroo", "KANG-JUN-090", "Junior", "Angles", "medium",
    "What is the acute angle formed between the hour hand and the minute hand of a clock at 3:30?",
    "ما قياس الزاوية الحادة المتكونة بين عقربي الساعات والدقائق عند الساعة 3:30؟",
    ["60^\\circ", "70^\\circ", "75^\\circ", "80^\\circ", "85^\\circ"], 2,
    "At 3:30, minute hand is at 180 degrees and hour hand is at \( 3 \\times 30 + 0.5 \\times 30 = 105 \) degrees.",
    "عند 3:30، عقرب الدقائق عند 180 درجة وعقرب الساعات عند 105 درجات.",
    "Angle = \( 180^\\circ - 105^\\circ = 75^\\circ \).",
    "الزاوية = \( 180^\\circ - 105^\\circ = 75^\\circ \).")

add("kangaroo", "KANG-JUN-094", "Junior", "Circle Geometry", "easy",
    "An angle inscribed in a circle intercepts a semicircular arc (a diameter). What is the measure of this inscribed angle?",
    "زاوية محيطية في دائرة تقابل قوس نصف دائرة (قوس القطر). ما قياس هذه الزاوية المحيطية؟",
    ["45^\\circ", "60^\\circ", "90^\\circ", "120^\\circ", "180^\\circ"], 2,
    "By Thales' theorem, an angle inscribed in a semicircle is always a right angle.",
    "وفقًا لنظرية طاليس، أي زاوية محيطية مرسومة في نصف دائرة تكون قائمة دائمًا.",
    "An inscribed angle is half its intercepted arc: \( \\frac{180^\\circ}{2} = 90^\\circ \).",
    "قياس الزاوية المحيطية يساوي نصف قياس القوس المقابل: \( 90^\\circ \).")

add("kangaroo", "KANG-JUN-098", "Junior", "Modular Arithmetic", "medium",
    "If an integer \( x \) satisfies \( x \\equiv 3 \\pmod{7} \), what is the remainder when \( x^2 + 2x \) is divided by \( 7 \)?",
    "إذا كان العدد الصحيح \( x \) يحقق \( x \\equiv 3 \\pmod{7} \)، فما باقي قسمة \( x^2 + 2x \) على \( 7 \)؟",
    ["1", "2", "3", "4", "5"], 0,
    "Substitute \( x = 3 \) into the polynomial and evaluate modulo 7.",
    "عوض بـ \( x = 3 \) في المقدار واحسب الناتج موديولو 7.",
    "\( 3^2 + 2(3) = 9 + 6 = 15 \\equiv 1 \\pmod{7} \).",
    "\( 3^2 + 2(3) = 15 \\equiv 1 \\pmod{7} \).")

# ==================== NSMO (45 replacements) ====================
# 24 Junior Olympiad Algebra / Number Theory
add("nsmo", "NSMO-P1-008", "Phase 1: Junior Olympiad (Grades 5-7)", "Divisibility", "easy",
    "What is the remainder when the 10-digit number \( 1234567890 \) is divided by \( 9 \)?",
    "ما باقي قسمة العدد المكون من 10 أرقام \( 1234567890 \) على \( 9 \)؟",
    ["0", "1", "3", "5"], 0,
    "A number has the same remainder modulo 9 as the sum of its digits.",
    "باقي قسمة أي عدد على 9 يساوي باقي قسمة مجموع أرقامه على 9.",
    "Sum of digits = \( 1+2+3+4+5+6+7+8+9+0 = 45 \), which is divisible by 9, so remainder is 0.",
    "مجموع الأرقام = 45، وهو يقبل القسمة على 9 تمامًا، إذن الباقي = 0.")

add("nsmo", "NSMO-P1-012", "Phase 1: Junior Olympiad (Grades 5-7)", "Prime Factorization", "easy",
    "How many distinct prime factors does the number \( 2024 \) have?",
    "كم عاملاً أوليًا مختلفًا للعدد \( 2024 \)؟",
    ["2", "3", "4", "5"], 1,
    "Find the prime factorization: \( 2024 = 8 \\times 253 = 2^3 \\times 11 \\times 23 \).",
    "حلل إلى العوامل الأولية: \( 2024 = 2^3 \\times 11 \\times 23 \).",
    "The distinct prime factors are 2, 11, and 23 (3 distinct primes).",
    "العوامل الأولية المختلفة هي 2 و11 و23 (3 عوامل أولية مختلفة).")

add("nsmo", "NSMO-P1-016", "Phase 1: Junior Olympiad (Grades 5-7)", "Combinatorics", "medium",
    "In how many ways can a committee of \( 3 \) students be chosen from a group of \( 7 \) students?",
    "بكم طريقة يمكن اختيار لجنة مكونة من \( 3 \) طلاب من بين مجموعة تضم \( 7 \) طلاب؟",
    ["21", "30", "35", "42"], 2,
    "Use combinations: \( \\binom{7}{3} = \\frac{7 \\times 6 \\times 5}{3 \\times 2 \\times 1} \).",
    "استخدم التوافيق: \( \\binom{7}{3} = \\frac{7 \\times 6 \\times 5}{3 \\times 2 \\times 1} \).",
    "\( \\binom{7}{3} = \\frac{210}{6} = 35 \) ways.",
    "\( \\binom{7}{3} = 35 \) طريقة.")

add("nsmo", "NSMO-P1-020", "Phase 1: Junior Olympiad (Grades 5-7)", "Divisibility", "medium",
    "Find the digit \( n \) such that the five-digit number \( 35n72 \) is divisible by \( 11 \).",
    "أوجد الرقم \( n \) الذي يجعل العدد المكون من خمسة أرقام \( 35n72 \) قابلاً للقسمة على \( 11 \).",
    ["3", "5", "7", "9"], 2,
    "The alternating sum of the digits must be divisible by 11: \( (3 + n + 2) - (5 + 7) \).",
    "الفرق بالتناوب بين مجموع الأرقام في المنازل الفردية والزوجية يجب أن يقبل القسمة على 11.",
    "\( (n + 5) - 12 = n - 7 \\equiv 0 \\implies n = 7 \).",
    "\( n - 7 = 0 \\implies n = 7 \).")

add("nsmo", "NSMO-P1-024", "Phase 1: Junior Olympiad (Grades 5-7)", "Algebra", "easy",
    "If \( a + b = 9 \) and \( a - b = 5 \), what is the value of \( a^2 - b^2 \)?",
    "إذا كان \( a + b = 9 \) و\( a - b = 5 \)، فما قيمة \( a^2 - b^2 \)؟",
    ["36", "40", "45", "54"], 2,
    "Use the difference of squares identity: \( a^2 - b^2 = (a + b)(a - b) \).",
    "استخدم متطابقة الفرق بين مربعين: \( a^2 - b^2 = (a + b)(a - b) \).",
    "\( a^2 - b^2 = 9 \\times 5 = 45 \).",
    "\( a^2 - b^2 = 9 \\times 5 = 45 \).")

add("nsmo", "NSMO-P1-028", "Phase 1: Junior Olympiad (Grades 5-7)", "Counting", "easy",
    "How many two-digit positive integers from \( 10 \) to \( 99 \) are NOT divisible by \( 5 \)?",
    "كم عددًا صحيحًا موجبًا مكونًا من رقمين (من 10 إلى 99) لا يقبل القسمة على \( 5 \)؟",
    ["60", "72", "75", "80"], 1,
    "There are 90 two-digit numbers in total. Subtract the count of multiples of 5.",
    "يوجد 90 عددًا من رقمين. اطرح منها مضاعفات العدد 5.",
    "Multiples of 5 are \( 18 \) numbers (\( 10, 15, \\ldots, 95 \)). Not divisible = \( 90 - 18 = 72 \).",
    "مضاعفات 5 عددها 18، إذن الأعداد غير القابلة للقسمة = \( 90 - 18 = 72 \).")

add("nsmo", "NSMO-P1-032", "Phase 1: Junior Olympiad (Grades 5-7)", "Number Theory", "easy",
    "What is the sum of all positive divisors of the prime number \( 17 \)?",
    "ما مجموع جميع القواسم الموجبة للعدد الأولي \( 17 \)؟",
    ["17", "18", "19", "34"], 1,
    "A prime number has exactly two positive divisors: 1 and itself.",
    "العدد الأولي له قاسمان موجبان فقط: الواحد الصحيح ونفسه.",
    "\( 1 + 17 = 18 \).",
    "\( 1 + 17 = 18 \).")

add("nsmo", "NSMO-P1-036", "Phase 1: Junior Olympiad (Grades 5-7)", "Averages", "easy",
    "The average of four numbers is \( 25 \). When a fifth number is added, the new average becomes \( 28 \). What is the fifth number?",
    "المتوسط الحسابي لأربعة أعداد هو \( 25 \). وعند إضافة عدد خامس، أصبح المتوسط الجديد \( 28 \). ما هو العدد الخامس؟",
    ["32", "35", "38", "40"], 3,
    "Calculate the total sum before and after: \( 5 \\times 28 - 4 \\times 25 \).",
    "احسب المجموع الكلي قبل وبعد إضافة العدد: \( 5 \\times 28 - 4 \\times 25 \).",
    "New total = \( 140 \), old total = \( 100 \). Fifth number = \( 140 - 100 = 40 \).",
    "المجموع الجديد = 140، والمجموع القديم = 100. إذن العدد الخامس = 40.")

add("nsmo", "NSMO-P1-040", "Phase 1: Junior Olympiad (Grades 5-7)", "Sequences", "easy",
    "What is the sum of the first \( 15 \) positive odd integers: \( 1 + 3 + 5 + \\cdots + 29 \)?",
    "ما مجموع أول \( 15 \) عددًا فرديًا موجبًا: \( 1 + 3 + 5 + \\cdots + 29 \)؟",
    ["210", "225", "240", "256"], 1,
    "The sum of the first n positive odd integers is always equal to \( n^2 \).",
    "مجموع أول n عدد فردي موجب يساوي دائمًا \( n^2 \).",
    "\( 15^2 = 225 \).",
    "\( 15^2 = 225 \).")

add("nsmo", "NSMO-P1-044", "Phase 1: Junior Olympiad (Grades 5-7)", "Exponents", "easy",
    "What is the exact value of \( 2^{10} - 2^9 \)?",
    "ما القيمة الدقيقة للمقدار \( 2^{10} - 2^9 \)؟",
    ["2", "256", "512", "1024"], 2,
    "Factor out \( 2^9 \): \( 2^9(2 - 1) \).",
    "أخرج \( 2^9 \) كعامل مشترك: \( 2^9(2 - 1) \).",
    "\( 2^9 \\times 1 = 512 \).",
    "\( 2^9 = 512 \).")

add("nsmo", "NSMO-P1-048", "Phase 1: Junior Olympiad (Grades 5-7)", "Pigeonhole Principle", "easy",
    "A drawer contains \( 10 \) blue socks and \( 10 \) black socks. What is the minimum number of socks that must be drawn in the dark to guarantee at least one matching pair?",
    "درج يحتوي على \( 10 \) جوارب زرقاء و\( 10 \) جوارب سوداء. ما أقل عدد من الجوارب يجب سحبه في الظلام لضمان الحصول على زوج متطابق من نفس اللون بالتأكيد؟",
    ["2", "3", "4", "5"], 1,
    "By the Pigeonhole Principle, with 2 colors, drawing 3 socks guarantees at least two of the same color.",
    "بمبدأ برج الحمام، بوجود لونين، سحب 3 جوارب يضمن بالضرورة زوجًا من نفس اللون.",
    "Worst-case draw is 1 blue and 1 black; the 3rd sock must match one of them. Answer = 3.",
    "أسوأ احتمال سحب جورب من كل لون، والجورب الثالث سيطابق أحدهما حتمًا. الجواب = 3.")

add("nsmo", "NSMO-P1-052", "Phase 1: Junior Olympiad (Grades 5-7)", "Percentages", "easy",
    "In a school with \( 500 \) students, \( 60\\% \) participate in sports. How many students do NOT participate in sports?",
    "في مدرسة بها \( 500 \) طالب، يشارك \( 60\\% \) في الأنشطة الرياضية. كم طالبًا لا يشارك في الأنشطة الرياضية؟",
    ["150", "200", "250", "300"], 1,
    "The non-participants account for \( 100\\% - 60\\% = 40\\% \) of the students.",
    "الطلاب غير المشاركين يشكلون \( 40\\% \) من طلاب المدرسة.",
    "\( 40\\% \\times 500 = 0.40 \\times 500 = 200 \).",
    "\( 0.40 \\times 500 = 200 \) طالب.")

add("nsmo", "NSMO-P1-056", "Phase 1: Junior Olympiad (Grades 5-7)", "Modular Arithmetic", "medium",
    "What is the remainder when \( 100! + 23 \) is divided by \( 19 \)?",
    "ما باقي قسمة المقدار \( 100! + 23 \) على \( 19 \)؟",
    ["0", "4", "5", "19"], 1,
    "Since 19 is a factor of 100!, \( 100! \\equiv 0 \\pmod{19} \).",
    "بما أن 19 من عوامل مضروب 100، فإن \( 100! \\equiv 0 \\pmod{19} \).",
    "The remainder is \( 23 \\pmod{19} = 4 \).",
    "الباقي هو باقي قسمة 23 على 19، وهو 4.")

add("nsmo", "NSMO-P1-060", "Phase 1: Junior Olympiad (Grades 5-7)", "Algebra", "easy",
    "If \( 3x + 2y = 19 \) and \( x + 2y = 11 \), what is the value of \( x \)?",
    "إذا كان \( 3x + 2y = 19 \) و\( x + 2y = 11 \)، فما قيمة \( x \)؟",
    ["2", "3", "4", "5"], 2,
    "Subtract the second equation from the first equation to eliminate \( y \).",
    "اطرح المعادلة الثانية من المعادلة الأولى لحذف المتغير \( y \).",
    "\( (3x + 2y) - (x + 2y) = 19 - 11 \\implies 2x = 8 \\implies x = 4 \).",
    "\( 2x = 8 \\implies x = 4 \).")

add("nsmo", "NSMO-P1-064", "Phase 1: Junior Olympiad (Grades 5-7)", "Base Systems", "easy",
    "Convert the binary number \( 11010_2 \) to standard decimal notation (base 10).",
    "حوّل العدد الثنائي \( 11010_2 \) إلى النظام العشري (الأساس 10).",
    ["22", "24", "26", "28"], 2,
    "Expand in powers of 2: \( 1(16) + 1(8) + 0(4) + 1(2) + 0(1) \).",
    "فكك العدد بقوى الأساس 2: \( 1(16) + 1(8) + 0(4) + 1(2) + 0(1) \).",
    "\( 16 + 8 + 2 = 26 \).",
    "\( 16 + 8 + 2 = 26 \).")

add("nsmo", "NSMO-P1-068", "Phase 1: Junior Olympiad (Grades 5-7)", "Number Theory", "easy",
    "Find the sum of all prime numbers strictly between \( 10 \) and \( 20 \).",
    "أوجد مجموع جميع الأعداد الأولية التي تقع تمامًا بين \( 10 \) و\( 20 \).",
    ["50", "58", "60", "62"], 2,
    "The primes between 10 and 20 are 11, 13, 17, and 19.",
    "الأعداد الأولية بين 10 و20 هي 11، 13، 17، 19.",
    "\( 11 + 13 + 17 + 19 = 60 \).",
    "\( 11 + 13 + 17 + 19 = 60 \).")

add("nsmo", "NSMO-P1-072", "Phase 1: Junior Olympiad (Grades 5-7)", "Probability", "easy",
    "A fair coin is tossed \( 3 \) times. What is the probability of obtaining exactly \( 2 \) heads?",
    "أُلقيت قطعة نقود منتظمة \( 3 \) مرات. ما احتمال ظهور وجه الصورة (Heads) مرتين بالضبط؟",
    ["\\frac{1}{4}", "\\frac{3}{8}", "\\frac{1}{2}", "\\frac{5}{8}"], 1,
    "There are 8 total outcomes, and 3 have exactly 2 heads: HHT, HTH, THH.",
    "يوجد 8 نواتج ممكنة متساوية الاحتمال، 3 منها تحتوي صورتين: HHT، HTH، THH.",
    "\( \\frac{3}{8} \).",
    "\( \\frac{3}{8} \).")

add("nsmo", "NSMO-P1-076", "Phase 1: Junior Olympiad (Grades 5-7)", "Logic", "easy",
    "If Ali is older than Badr, and Tariq is younger than Badr, who is the youngest among the three?",
    "إذا كان علي أكبر سنًا من بدر، وكان طارق أصغر سنًا من بدر، فمن هو الأصغر سنًا بين الثلاثة؟",
    ["Ali", "Badr", "Tariq", "\\text{Cannot be determined}"], 2,
    "Order by age: Ali > Badr > Tariq.",
    "رتب الأعمار: علي > بدر > طارق.",
    "Tariq is the youngest.",
    "طارق هو الأصغر سنًا.")

add("nsmo", "NSMO-P1-080", "Phase 1: Junior Olympiad (Grades 5-7)", "Inequalities", "easy",
    "How many positive integers \( n \) satisfy the strict inequality \( 3n < 25 \)?",
    "كم عددًا صحيحًا موجبًا \( n \) يحقق المتباينة: \( 3n < 25 \)؟",
    ["6", "7", "8", "9"], 2,
    "Divide by 3: \( n < 8.333\\ldots \). Positive integers are 1, 2, ..., 8.",
    "اقسم على 3: \( n < 8.333 \). الأعداد الصحيحة الموجبة هي من 1 إلى 8.",
    "There are 8 such integers.",
    "يوجد 8 أعداد صحيحة موجبة.")

add("nsmo", "NSMO-P1-084", "Phase 1: Junior Olympiad (Grades 5-7)", "Algebra", "medium",
    "Find the sum of all real solutions to the equation \( |x - 4| = 9 \).",
    "أوجد مجموع جميع الحلول الحقيقية للمعادلة: \( |x - 4| = 9 \).",
    ["0", "8", "9", "18"], 1,
    "The two solutions are \( x - 4 = 9 \\implies x = 13 \) and \( x - 4 = -9 \\implies x = -5 \).",
    "الحلان هما \( x = 13 \) و\( x = -5 \).",
    "Sum = \( 13 + (-5) = 8 \).",
    "المجموع = \( 13 + (-5) = 8 \).")

add("nsmo", "NSMO-P1-088", "Phase 1: Junior Olympiad (Grades 5-7)", "Speed and Time", "easy",
    "A car travels \( 150 \\text{ km} \) in \( 2 \\text{ hours and } 30 \\text{ minutes} \). What is its average speed in \( \\text{km/h} \)?",
    "قطعت سيارة مسافة \( 150 \\text{ كم} \) في زمن قدره ساعتان و\( 30 \\text{ دقيقة} \). ما متوسط سرعة السيارة بوحدة \( \\text{كم/ساعة} \)؟",
    ["50", "55", "60", "65"], 2,
    "Convert time to decimal hours: \( 2.5 \\text{ hours} \). Speed = distance / time.",
    "حوّل الزمن إلى ساعات عشرية: 2.5 ساعة. السرعة = المسافة / الزمن.",
    "\( \\frac{150}{2.5} = 60 \\text{ km/h} \).",
    "\( \\frac{150}{2.5} = 60 \\text{ كم/ساعة} \).")

add("nsmo", "NSMO-P1-092", "Phase 1: Junior Olympiad (Grades 5-7)", "Exponents", "easy",
    "Evaluate the expression: \( \\frac{2^{2025}}{2^{2022}} \).",
    "احسب القيمة العددية للمقدار الآتي: \( \\frac{2^{2025}}{2^{2022}} \).",
    ["3", "6", "8", "16"], 2,
    "Subtract the exponents: \( 2^{2025 - 2022} = 2^3 \).",
    "اطرح الأسس: \( 2^{2025 - 2022} = 2^3 \).",
    "\( 2^3 = 8 \).",
    "\( 2^3 = 8 \).")

add("nsmo", "NSMO-P1-096", "Phase 1: Junior Olympiad (Grades 5-7)", "Combinatorics", "medium",
    "How many 3-digit whole numbers are there in which every digit is an odd digit?",
    "كم عددًا كليًا مكونًا من 3 أرقام تكون جميع أرقامه أرقامًا فردية؟",
    ["100", "125", "150", "250"], 1,
    "The available odd digits are 1, 3, 5, 7, 9 (5 choices for each of the 3 places).",
    "الأرقام الفردية المتاحة هي 1، 3، 5، 7، 9 (5 خيارات لكل منزلة).",
    "\( 5 \\times 5 \\times 5 = 125 \) numbers.",
    "\( 5 \\times 5 \\times 5 = 125 \) عددًا.")

add("nsmo", "NSMO-P1-100", "Phase 1: Junior Olympiad (Grades 5-7)", "Number Theory", "medium",
    "Find the smallest positive integer greater than \( 1 \) that is simultaneously a perfect square and a perfect cube.",
    "أوجد أصغر عدد صحيح موجب أكبر من \( 1 \) ويكون مربعًا كاملاً ومكعبًا كاملاً في آن واحد.",
    ["16", "36", "64", "100"], 2,
    "A number is both a square and a cube if and only if it is a 6th power.",
    "يكون العدد مربعًا ومكعبًا معًا إذا وفقط إذا كان قوة سادسة كاملة.",
    "Smallest for base > 1 is \( 2^6 = 64 \).",
    "أصغر قوة سادسة بعد الواحد هي \( 2^6 = 64 \).")

# 21 Junior Olympiad Geometry
add("nsmo", "NSMO-P1-010", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "In a right triangle with legs of lengths \( 5 \\text{ cm} \) and \( 12 \\text{ cm} \), what is the length of the hypotenuse?",
    "في مثلث قائم الزاوية طولا ضلعي القائمة فيه \( 5 \\text{ سم} \) و\( 12 \\text{ سم} \)، ما طول الوتر؟",
    ["11 \\text{ cm}", "13 \\text{ cm}", "14 \\text{ cm}", "17 \\text{ cm}"], 1,
    "Apply the Pythagorean theorem: \( c = \\sqrt{5^2 + 12^2} \).",
    "طبق نظرية فيثاغورس: \( c = \\sqrt{5^2 + 12^2} \).",
    "\( \\sqrt{25 + 144} = \\sqrt{169} = 13 \\text{ cm} \).",
    "\( \\sqrt{169} = 13 \\text{ سم} \).")

add("nsmo", "NSMO-P1-014", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "Two complementary angles have measures in the ratio \( 2 : 3 \). What is the measure of the smaller angle?",
    "زاويتان متتامتان النسبة بين قياسيهما هي \( 2 : 3 \). ما قياس الزاوية الصغرى منهما؟",
    ["30^\\circ", "36^\\circ", "45^\\circ", "54^\\circ"], 1,
    "Complementary angles sum to 90 degrees. Divide into \( 2 + 3 = 5 \) parts.",
    "الزاويتان المتتامتان مجموعهما 90 درجة. قسّم على 5 أجزاء متساوية.",
    "One part = \( 90^\\circ / 5 = 18^\\circ \). Smaller = \( 2 \\times 18^\\circ = 36^\\circ \).",
    "الزاوية الصغرى = \( 2 \\times 18^\\circ = 36^\\circ \).")

add("nsmo", "NSMO-P1-018-R182", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "medium",
    "What is the area of an equilateral triangle whose side length is \( 6 \\text{ cm} \)?",
    "ما مساحة مثلث متطابق الأضلاع طول ضلعه \( 6 \\text{ سم} \)؟",
    ["6\\sqrt{3}", "9\\sqrt{3}", "12\\sqrt{3}", "18"], 1,
    "The area of an equilateral triangle with side s is \( \\frac{\\sqrt{3}}{4} s^2 \).",
    "مساحة المثلث متطابق الأضلاع تُحسب بالقانون: \( \\frac{\\sqrt{3}}{4} s^2 \).",
    "\( \\frac{\\sqrt{3}}{4} \\times 6^2 = \\frac{36\\sqrt{3}}{4} = 9\\sqrt{3} \\text{ cm}^2 \).",
    "\( \\frac{36\\sqrt{3}}{4} = 9\\sqrt{3} \\text{ سم}^2 \).")

add("nsmo", "NSMO-P1-022", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "The perimeter of a regular hexagon is \( 42 \\text{ cm} \). What is the length of one side?",
    "محيط مضلع سداسي منتظم يساوي \( 42 \\text{ سم} \). ما طول ضلعه الواحد؟",
    ["6 \\text{ cm}", "7 \\text{ cm}", "8 \\text{ cm}", "9 \\text{ cm}"], 1,
    "A regular hexagon has 6 equal sides: divide the perimeter by 6.",
    "المضلع السداسي المنتظم له 6 أضلاع متطابقة: اقسم المحيط على 6.",
    "\( 42 / 6 = 7 \\text{ cm} \).",
    "\( 42 / 6 = 7 \\text{ سم} \).")

add("nsmo", "NSMO-P1-026", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "In parallelogram \( ABCD \), angle \( \\angle A \) measures \( 65^\\circ \). What is the measure of the adjacent consecutive angle \( \\angle B \)?",
    "في متوازي الأضلاع \( ABCD \)، قياس الزاوية \( \\angle A \) هو \( 65^\\circ \). ما قياس الزاوية المجاورة المتتالية \( \\angle B \)؟",
    ["65^\\circ", "105^\\circ", "115^\\circ", "125^\\circ"], 2,
    "Adjacent angles in any parallelogram are supplementary (sum to 180 degrees).",
    "الزاويتان المتتاليتان في أي متوازي أضلاع متكاملتان (مجموعهما 180 درجة).",
    "\( 180^\\circ - 65^\\circ = 115^\\circ \).",
    "\( 180^\\circ - 65^\\circ = 115^\\circ \).")

add("nsmo", "NSMO-P1-034", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "What is the measure of each interior angle of a regular pentagon?",
    "ما قياس كل زاوية داخلية في مضلع خماسي منتظم؟",
    ["90^\\circ", "108^\\circ", "120^\\circ", "135^\\circ"], 1,
    "Formula for regular interior angle: \( \\frac{(n - 2) \\times 180^\\circ}{n} \) for \( n = 5 \).",
    "صيغة زاوية المضلع المنتظم: \( \\frac{(n - 2) \\times 180^\\circ}{n} \) مع \( n = 5 \).",
    "\( \\frac{3 \\times 180^\\circ}{5} = \\frac{540^\\circ}{5} = 108^\\circ \).",
    "\( \\frac{540^\\circ}{5} = 108^\\circ \).")

add("nsmo", "NSMO-P1-038", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "A circle has an area of \( 49\\pi \\text{ cm}^2 \). What is the diameter of this circle?",
    "دائرة مساحتها \( 49\\pi \\text{ سم}^2 \). ما طول قطر هذه الدائرة؟",
    ["7 \\text{ cm}", "14 \\text{ cm}", "21 \\text{ cm}", "28 \\text{ cm}"], 1,
    "Area = \( \\pi r^2 = 49\\pi \\implies r = 7 \\text{ cm} \). Diameter is \( 2r \).",
    "المساحة = \( \\pi r^2 = 49\\pi \\implies r = 7 \\text{ سم} \). القطر = \( 2r \).",
    "\( d = 2 \\times 7 = 14 \\text{ cm} \).",
    "\( d = 14 \\text{ سم} \).")

add("nsmo", "NSMO-P1-042", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "An exterior angle of a triangle measures \( 125^\\circ \). If one of the remote interior angles measures \( 55^\\circ \), what is the measure of the other remote interior angle?",
    "زاوية خارجية لمثلث قياسها \( 125^\\circ \). إذا كان قياس إحدى الزاويتين الداخليتين البعيدتين هو \( 55^\\circ \)، فما قياس الزاوية الداخلية البعيدة الأخرى؟",
    ["55^\\circ", "65^\\circ", "70^\\circ", "75^\\circ"], 2,
    "The exterior angle of a triangle equals the sum of the two remote interior angles.",
    "قياس الزاوية الخارجية للمثلث يساوي مجموع قياسي الزاويتين الداخليتين البعيدتين.",
    "\( 125^\\circ - 55^\\circ = 70^\\circ \).",
    "\( 125^\\circ - 55^\\circ = 70^\\circ \).")

add("nsmo", "NSMO-P1-046", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "What is the total number of lines of reflection symmetry of a regular octagon?",
    "ما العدد الكلي لخطوط التماثل الانعكاسي لمضلع ثماني منتظم؟",
    ["4", "6", "8", "16"], 2,
    "A regular n-sided polygon always has exactly n lines of reflection symmetry.",
    "أي مضلع منتظم له n ضلعًا يمتلك بالضبط n من خطوط التماثل.",
    "An octagon has 8 sides, hence 8 lines of symmetry.",
    "المضلع الثماني له 8 أضلاع، إذن له 8 خطوط تماثل.")

add("nsmo", "NSMO-P1-050", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "medium",
    "A trapezoid has parallel bases of lengths \( 8 \\text{ cm} \) and \( 14 \\text{ cm} \), and a perpendicular height of \( 6 \\text{ cm} \). What is its area in \( \\text{cm}^2 \)?",
    "شبه منحرف طولا قاعدتيه المتوازيتين \( 8 \\text{ سم} \) و\( 14 \\text{ سم} \)، وارتفاعه العمودي \( 6 \\text{ سم} \). ما مساحته بالـ \( \\text{سم}^2 \)؟",
    ["55", "60", "66", "72"], 2,
    "The area of a trapezoid is \( \\frac{a + b}{2} \\times h \).",
    "مساحة شبه المنحرف تساوي متوسط طولي القاعدتين مضروبًا في الارتفاع.",
    "\( \\frac{8 + 14}{2} \\times 6 = 11 \\times 6 = 66 \\text{ cm}^2 \).",
    "\( 11 \\times 6 = 66 \\text{ سم}^2 \).")

add("nsmo", "NSMO-P1-054", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "medium",
    "A square has a diagonal of length \( 8\\sqrt{2} \\text{ cm} \). What is the perimeter of this square?",
    "مربع طول قطره \( 8\\sqrt{2} \\text{ سم} \). ما محيط هذا المربع؟",
    ["16 \\text{ cm}", "24 \\text{ cm}", "32 \\text{ cm}", "64 \\text{ cm}"], 2,
    "The diagonal of a square with side s is \( s\\sqrt{2} \). Side is 8 cm.",
    "طول قطر المربع الذي طول ضلعه s هو \( s\\sqrt{2} \). إذن طول الضلع 8 سم.",
    "\( \\text{Perimeter} = 4 \\times 8 = 32 \\text{ cm} \).",
    "\( 4 \\times 8 = 32 \\text{ سم} \).")

add("nsmo", "NSMO-P1-058", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "Two angles of a triangle measure \( 48^\\circ \) and \( 72^\\circ \). What is the measure of the third angle?",
    "قياسا زاويتين في مثلث هما \( 48^\\circ \) و\( 72^\\circ \). ما قياس الزاوية الثالثة؟",
    ["50^\\circ", "55^\\circ", "60^\\circ", "65^\\circ"], 2,
    "The three interior angles of a triangle always sum to 180 degrees.",
    "مجموع زوايا المثلث الداخلية يساوي دائمًا 180 درجة.",
    "\( 180^\\circ - (48^\\circ + 72^\\circ) = 180^\\circ - 120^\\circ = 60^\\circ \).",
    "\( 180^\\circ - 120^\\circ = 60^\\circ \).")

add("nsmo", "NSMO-P1-062", "Phase 1: Junior Olympiad (Grades 5-7)", "Circle Geometry", "easy",
    "In a circle, a central angle intercepts an arc measuring \( 80^\\circ \). What is the measure of an inscribed angle intercepting the same arc?",
    "في دائرة، زاوية مركزية تقابل قوسًا قياسه \( 80^\\circ \). ما قياس الزاوية المحيطية التي تقابل القوس نفسه؟",
    ["20^\\circ", "40^\\circ", "80^\\circ", "160^\\circ"], 1,
    "The measure of an inscribed angle is half the measure of the intercepted arc.",
    "قياس الزاوية المحيطية يساوي نصف قياس القوس المقابل لها.",
    "\( 80^\\circ / 2 = 40^\\circ \).",
    "\( 80^\\circ / 2 = 40^\\circ \).")

add("nsmo", "NSMO-P1-066", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "What is the area of a square whose perimeter is \( 28 \\text{ cm} \)?",
    "ما مساحة مربع محيطه \( 28 \\text{ سم} \)؟",
    ["36", "42", "49", "56"], 2,
    "Divide perimeter by 4 to get side length: \( 28 / 4 = 7 \\text{ cm} \). Area is \( s^2 \).",
    "اقسم المحيط على 4 لإيجاد طول الضلع: \( 28 / 4 = 7 \\text{ سم} \). المساحة هي \( s^2 \).",
    "\( 7^2 = 49 \\text{ cm}^2 \).",
    "\( 7^2 = 49 \\text{ سم}^2 \).")

add("nsmo", "NSMO-P1-070", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "If the three side lengths of a triangle are \( 7 \\text{ cm} \), \( 24 \\text{ cm} \), and \( 25 \\text{ cm} \), what type of triangle is it?",
    "إذا كانت أطوال أضلاع مثلث هي \( 7 \\text{ سم} \) و\( 24 \\text{ سم} \) و\( 25 \\text{ سم} \)، فما نوع هذا المثلث؟",
    ["\\text{Acute}", "\\text{Right}", "\\text{Obtuse}", "\\text{Equilateral}"], 1,
    "Check the Pythagorean converse: \( 7^2 + 24^2 = 49 + 576 = 625 = 25^2 \).",
    "افحص عكس نظرية فيثاغورس: \( 7^2 + 24^2 = 49 + 576 = 625 = 25^2 \).",
    "Since \( a^2 + b^2 = c^2 \), the triangle is a right-angled triangle.",
    "بما أن مجموع مربعي الضلعين يساوي مربع الضلع الثالث، فإن المثلث قائم الزاوية.")

add("nsmo", "NSMO-P1-074", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "medium",
    "A rectangle has width \( 5 \\text{ cm} \) and diagonal \( 13 \\text{ cm} \). What is the area of the rectangle in \( \\text{cm}^2 \)?",
    "مستطيل عرضه \( 5 \\text{ سم} \) وطول قطره \( 13 \\text{ سم} \). ما مساحة المستطيل بالـ \( \\text{سم}^2 \)؟",
    ["50", "60", "65", "120"], 1,
    "Find the length using the Pythagorean theorem: \( L = \\sqrt{13^2 - 5^2} \).",
    "أوجد الطول باستخدام نظرية فيثاغورس: \( L = \\sqrt{13^2 - 5^2} \).",
    "\( L = \\sqrt{169 - 25} = 12 \\text{ cm} \\implies \\text{Area} = 12 \\times 5 = 60 \\text{ cm}^2 \).",
    "\( L = 12 \\text{ سم} \\implies \\text{المساحة} = 12 \\times 5 = 60 \\text{ سم}^2 \).")

add("nsmo", "NSMO-P1-078", "Phase 1: Junior Olympiad (Grades 5-7)", "Geometry", "easy",
    "What is the sum of the measures of the exterior angles (one at each vertex) of any convex polygon?",
    "ما مجموع قياسات الزوايا الخارجية (واحدة عند كل رأس) لأي مضلع محدب؟",
    ["180^\\circ", "360^\\circ", "540^\\circ", "720^\\circ"], 1,
    "The sum of exterior angles of any convex polygon is a constant 360 degrees.",
    "مجموع الزوايا الخارجية لأي مضلع محدب مقدار ثابت يساوي 360 درجة دائمًا.",
    "The sum is always \( 360^\\circ \).",
    "المجموع يساوي دائمًا \( 360^\\circ \).")

add("nsmo", "NSMO-P1-082", "Phase 1: Junior Olympiad (Grades 5-7)", "Circle Geometry", "medium",
    "In a cyclic quadrilateral \( ABCD \), opposite angle \( \\angle A \) measures \( 85^\\circ \). What is the measure of angle \( \\angle C \)?",
    "في شكل رباعي دائري \( ABCD \)، قياس الزاوية المقابلة \( \\angle A \) هو \( 85^\\circ \). ما قياس الزاوية \( \\angle C \)؟",
    ["85^\\circ", "90^\\circ", "95^\\circ", "105^\\circ"], 2,
    "Opposite angles in any cyclic quadrilateral are supplementary (sum to 180 degrees).",
    "الزاويتان المتقابلتان في أي رباعي دائري متكاملتان (مجموعهما 180 درجة).",
    "\( \\angle C = 180^\\circ - 85^\\circ = 95^\\circ \).",
    "\( \\angle C = 180^\\circ - 85^\\circ = 95^\\circ \).")

add("nsmo", "NSMO-P1-086", "Phase 1: Junior Olympiad (Grades 5-7)", "Solid Geometry", "easy",
    "A cube has a volume of \( 64 \\text{ cm}^3 \). What is the sum of the lengths of all its \( 12 \) edges combined?",
    "مكعب حجمه \( 64 \\text{ سم}^3 \). ما مجموع أطوال جميع حوافه (أضلاعه) الـ \( 12 \) معًا؟",
    ["36 \\text{ cm}", "48 \\text{ cm}", "64 \\text{ cm}", "96 \\text{ cm}"], 1,
    "Edge length is \( \\sqrt[3]{64} = 4 \\text{ cm} \). A cube has 12 edges.",
    "طول الحافة الواحدة هو الجذر التكعيبي لـ 64 وهو 4 سم. وللمكعب 12 حافة.",
    "\( 12 \\times 4 = 48 \\text{ cm} \).",
    "\( 12 \\times 4 = 48 \\text{ سم} \).")

add("nsmo", "NSMO-P1-094", "Phase 1: Junior Olympiad (Grades 5-7)", "Transformations", "easy",
    "Point \( P(3, 2) \) is translated by the vector \( \\langle -5, 4 \\rangle \). What are the coordinates of the image point?",
    "أُزيحت النقطة \( P(3, 2) \) بالمتجه \( \\langle -5, 4 \\rangle \). ما إحداثيات النقطة الناتجة عن الإزاحة؟",
    ["(-2, 6)", "(8, -2)", "(-2, -2)", "(2, 6)"], 0,
    "Add vector components to original coordinates: \( (x + \\Delta x, y + \\Delta y) \).",
    "اجمع مركبات المتجه مع الإحداثيات الأصلية: \( (x + \\Delta x, y + \\Delta y) \).",
    "\( (3 + (-5), 2 + 4) = (-2, 6) \).",
    "\( (-2, 6) \).")

add("nsmo", "NSMO-P1-098", "Phase 1: Junior Olympiad (Grades 5-7)", "Circle Geometry", "medium",
    "A circle has a radius of \( 10 \\text{ cm} \). What is the length of a chord that lies \( 6 \\text{ cm} \) away from the center of the circle?",
    "دائرة نصف قطرها \( 10 \\text{ سم} \). ما طول وتر يبعد مسافة \( 6 \\text{ سم} \) عن مركز الدائرة؟",
    ["12 \\text{ cm}", "14 \\text{ cm}", "16 \\text{ cm}", "18 \\text{ cm}"], 2,
    "Form a right triangle with radius (hypotenuse 10) and distance (leg 6). Half-chord is \( \\sqrt{10^2 - 6^2} \).",
    "كوّن مثلثًا قائمًا وتره نصف القطر 10 وأحد ضلعيه البعد 6. نصف طول الوتر = \( \\sqrt{10^2 - 6^2} \).",
    "Half-chord = \( \\sqrt{100 - 36} = 8 \\text{ cm} \\implies \\text{Chord} = 2 \\times 8 = 16 \\text{ cm} \).",
    "نصف الوتر = 8 سم، إذن طول الوتر كاملاً = \( 2 \\times 8 = 16 \\text{ سم} \).")

# ==================== APPLY REPLACEMENTS FUNCTION ====================
def apply_all():
    total_replaced = 0
    for track, reps in REPLACEMENTS.items():
        fpath = ROOT / "data" / f"{track}.json"
        bank = json.loads(fpath.read_text())
        b_map = {q["id"]: q for q in bank}
        count = 0
        for qid, new_q in reps.items():
            if qid in b_map:
                idx = bank.index(b_map[qid])
                bank[idx] = new_q
                count += 1
            else:
                print(f"ERROR: {qid} not in {track}!")
        fpath.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n")
        print(f"[{track}] Successfully replaced {count}/{len(reps)} questions.")
        total_replaced += count
    print(f"GRAND TOTAL: Successfully replaced {total_replaced} repetitive questions!")

if __name__ == "__main__":
    apply_all()
