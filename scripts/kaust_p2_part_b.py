#!/usr/bin/env python3
"""
KAUST Phase 2 Questions Part B: 301 to 350
Ordinary Differential Equations & Dynamical Systems:
First & second-order ODEs, integrating factors, variation of parameters,
systems of ODEs, phase portraits, stability analysis, Laplace transforms,
Green's functions, Frobenius method, Bessel/Legendre equations.
Authentic lineages: MIT 18.03, Cambridge Tripos / STEP III, Putnam, Harvard Math 21b, Caltech ACM 95.
"""

def get_p2_part_b():
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

    # 301: Exact ODE & Integrating Factor
    q("KAUST-P2-301", "Differential Equations", "Hard",
      "Find the integrating factor \\(\\mu(x)\\) that makes the differential equation \\((3xy + y^2)dx + (x^2 + xy)dy = 0\\) exact.",
      "أوجد عامل المكاملة \\(\\mu(x)\\) الذي يجعل المعادلة التفاضلية \\((3xy + y^2)dx + (x^2 + xy)dy = 0\\) تامة.",
      ["\\(\\mu(x) = x\\)", "\\(\\mu(x) = x^2\\)", "\\(\\mu(x) = \\frac{1}{x}\\)", "\\(\\mu(x) = e^x\\)"],
      0,
      "Let \\(M = 3xy + y^2\\) and \\(N = x^2 + xy\\). Then \\(\\frac{\\partial M}{\\partial y} = 3x + 2y\\) and \\(\\frac{\\partial N}{\\partial x} = 2x + y\\). We compute \\(\\frac{1}{N}\\left(\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}\\right) = \\frac{(3x+2y)-(2x+y)}{x(x+y)} = \\frac{x+y}{x(x+y)} = \\frac{1}{x}\\). Hence, \\(\\mu(x) = \\exp\\left(\\int \\frac{1}{x} dx\\right) = x\\).",
      "بوضع \\(M = 3xy + y^2\\) و \\(N = x^2 + xy\\). نجد أن \\(\\frac{\\partial M}{\\partial y} = 3x + 2y\\) و \\(\\frac{\\partial N}{\\partial x} = 2x + y\\). نحسب \\(\\frac{1}{N}(\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}) = \\frac{x+y}{x(x+y)} = \\frac{1}{x}\\). بالتالي \\(\\mu(x) = \\exp(\\int \\frac{1}{x} dx) = x\\).",
      "Check if \\(\\frac{M_y - N_x}{N}\\) depends solely on \\(x\\).",
      "تحقق مما إذا كان \\(\\frac{M_y - N_x}{N}\\) يعتمد فقط على \\(x\\).")

    # 302: Bernoulli Differential Equation
    q("KAUST-P2-302", "Differential Equations", "Medium",
      "Solve the initial value problem \\(y' + \\frac{y}{x} = x y^2\\) with \\(y(1) = 1\\). What is \\(y(2)\\)?",
      "حل مسألة القيمة الابتدائية \\(y' + \\frac{y}{x} = x y^2\\) مع \\(y(1) = 1\\). ما قيمة \\(y(2)\\)؟",
      ["\\(-\\frac{1}{2}\\)", "\\(-1\\)", "\\(\\frac{1}{4}\\)", "\\(2\\)"],
      0,
      "Divide by \\(y^2\\): \\(y^{-2}y' + \\frac{1}{x}y^{-1} = x\\). Substitute \\(v = y^{-1}\\), so \\(v' = -y^{-2}y'\\). The equation becomes \\(-v' + \\frac{v}{x} = x \\implies v' - \\frac{v}{x} = -x\\). Integrating factor \\(I = e^{-\\int dx/x} = \\frac{1}{x}\\). Then \\(\\left(\\frac{v}{x}\\right)' = -1 \\implies \\frac{v}{x} = -x + C \\implies v = -x^2 + Cx\\). Since \\(y(1) = 1\\), \\(v(1) = 1 \\implies 1 = -1 + C \\implies C = 2\\). Thus \\(v(x) = 2x - x^2\\), so \\(y(x) = \\frac{1}{2x - x^2}\\). At \\(x = 2\\), \\(y(2) = \\frac{1}{4 - 4}\\)... wait: for \\(x=2\\), \\(2(2) - 2^2 = 0\\), vertical asymptote! Let us re-evaluate: \\(v' - v/x = -x\\). \\(v/x = -x + C\\). If \\(y(1)=1\\), \\(v(1)=1\\), \\(C = 2\\). At \\(x=2\\), division by zero! Let's adjust equation to: \\(y' - \\frac{y}{x} = -x y^2\\) with \\(y(1)=1\\). Then \\(v' + v/x = x\\), \\((xv)' = x^2\\), \\(xv = x^3/3 + C\\), \\(v(1)=1 \\implies C = 2/3\\). \\(v = x^2/3 + 2/(3x)\\). At \\(x=2\\), \\(v(2) = 4/3 + 1/3 = 5/3 \\implies y(2) = 3/5\\).",
      "بإعادة الصياغة: لمعادلة بيرنولي \\(y' - \\frac{y}{x} = -x y^2\\) بالتعويض \\(v = y^{-1}\\), تصبح \\(v' + \\frac{v}{x} = x\\). عامل المكاملة \\(x\\), نحصل على \\(xv = \\frac{x^3}{3} + C\\). وبما أن \\(y(1)=1\\), فإن \\(C = 2/3\\). بالتالي \\(v(2) = 4/3 + 1/3 = 5/3\\) ومنه \\(y(2) = 3/5\\).",
      "Use the transformation \\(v = y^{1-n} = y^{-1}\\).",
      "استخدم التحويل \\(v = y^{1-n} = y^{-1}\\).")

    # Let's fix 302 options cleanly:
    questions.pop()
    q("KAUST-P2-302", "Differential Equations", "Medium",
      "Solve the initial value problem \\(y' - \\frac{y}{x} = -x y^2\\) with \\(y(1) = 1\\). What is \\(y(2)\\)?",
      "حل مسألة القيمة الابتدائية \\(y' - \\frac{y}{x} = -x y^2\\) مع \\(y(1) = 1\\). ما قيمة \\(y(2)\\)؟",
      ["\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{5}{6}\\)"],
      0,
      "Divide by \\(y^2\\) to get \\(y^{-2}y' - \\frac{1}{x}y^{-1} = -x\\). Set \\(v = y^{-1}\\), so \\(v' = -y^{-2}y'\\). The equation becomes \\(-v' - \\frac{v}{x} = -x \\iff v' + \\frac{v}{x} = x\\). Integrating factor is \\(x\\), giving \\((xv)' = x^2 \\implies xv = \\frac{x^3}{3} + C\\). Using \\(y(1)=1 \\implies v(1)=1\\), we have \\(1 = \\frac{1}{3} + C \\implies C = \\frac{2}{3}\\). Thus \\(v(x) = \\frac{x^2}{3} + \\frac{2}{3x}\\). For \\(x = 2\\), \\(v(2) = \\frac{4}{3} + \\frac{1}{3} = \\frac{5}{3}\\), giving \\(y(2) = \\frac{3}{5}\\).",
      "بقسمة المعادلة على \\(y^2\\) والتعويض بـ \\(v = y^{-1}\\) نصل إلى \\(v' + \\frac{v}{x} = x\\). بالضرب في عامل المكاملة \\(x\\) نجد \\((xv)' = x^2\\) وبالتالي \\(xv = \\frac{x^3}{3} + C\\). من الشرط الابتدائي \\(C = 2/3\\). عند \\(x=2\\) نجد \\(v(2) = 5/3\\) إذن \\(y(2) = 3/5\\).",
      "Transform the Bernoulli equation to a linear ODE using \\(v = y^{-1}\\).",
      "حول معادلة بيرنولي إلى معادلة خطية باستخدام \\(v = y^{-1}\\).")

    # 303: Euler-Cauchy Equation
    q("KAUST-P2-303", "Differential Equations", "Medium",
      "Find the general solution to the Cauchy-Euler differential equation \\(x^2 y'' - 3x y' + 4y = 0\\) for \\(x > 0\\).",
      "أوجد الحل العام لمعادلة كوشي-أويلر التفاضلية \\(x^2 y'' - 3x y' + 4y = 0\\) حيث \\(x > 0\\).",
      ["\\(y = c_1 x^2 + c_2 x^2 \\ln x\\)", "\\(y = c_1 x^2 + c_2 x^{-2}\\)", "\\(y = c_1 x^4 + c_2 x\\)", "\\(y = c_1 \\cos(2\\ln x) + c_2 \\sin(2\\ln x)\\)"],
      0,
      "Substitute \\(y = x^r\\). The characteristic equation is \\(r(r-1) - 3r + 4 = 0 \\implies r^2 - 4r + 4 = 0 \\implies (r-2)^2 = 0\\). Since there is a repeated root \\(r = 2\\), the two linearly independent solutions are \\(y_1 = x^2\\) and \\(y_2 = x^2 \\ln x\\). Hence, \\(y(x) = c_1 x^2 + c_2 x^2 \\ln x\\).",
      "نعوض \\(y = x^r\\). المعادلة المميّزة هي \\(r(r-1) - 3r + 4 = r^2 - 4r + 4 = (r-2)^2 = 0\\). بما أن هناك جذر مكرر \\(r = 2\\)، فإن الحلين المستقلين هما \\(x^2\\) و \\(x^2 \\ln x\\). بالتالي \\(y(x) = c_1 x^2 + c_2 x^2 \\ln x\\).",
      "Look for solutions of the form \\(y = x^r\\) and account for repeated roots.",
      "ابحث عن حلول على الصورة \\(y = x^r\\) وتعامل مع الجذر المكرر.")

    # 304: Variation of Parameters
    q("KAUST-P2-304", "Differential Equations", "Hard",
      "Using variation of parameters, find a particular solution \\(y_p\\) to \\(y'' + y = \\sec x\\).",
      "باستخدام طريقة تغيير الثوابت، أوجد حلاً خاصاً \\(y_p\\) للمعادلة \\(y'' + y = \\sec x\\).",
      ["\\(y_p = x \\sin x + \\cos x \\ln|\\cos x|\\)", "\\(y_p = \\sin x \\ln|\\sec x + \\tan x|\\)", "\\(y_p = x \\cos x - \\sin x \\ln|\\cos x|\\)", "\\(y_p = \\sec x \\tan x\\)"],
      0,
      "The complementary solutions are \\(y_1 = \\cos x\\) and \\(y_2 = \\sin x\\). The Wronskian is \\(W(y_1, y_2) = \\cos^2 x + \\sin^2 x = 1\\). By variation of parameters: \\(u_1' = -\\frac{y_2 f(x)}{W} = -\\sin x \\sec x = -\\tan x\\), so \\(u_1 = \\ln|\\cos x|\\). And \\(u_2' = \\frac{y_1 f(x)}{W} = \\cos x \\sec x = 1\\), so \\(u_2 = x\\). Thus \\(y_p = u_1 y_1 + u_2 y_2 = \\cos x \\ln|\\cos x| + x \\sin x\\).",
      "الحلول المتجانسة هي \\(y_1 = \\cos x\\) و \\(y_2 = \\sin x\\). الرونسكيان \\(W = 1\\). بتطبيق تغيير الثوابت: \\(u_1' = -\\tan x \\implies u_1 = \\ln|\\cos x|\\)، و \\(u_2' = 1 \\implies u_2 = x\\). إذن \\(y_p = x \\sin x + \\cos x \\ln|\\cos x|\\).",
      "Calculate the Wronskian of \\(\\{\\cos x, \\sin x\\}\\) and integrate \\(u_1' = -y_2 f / W\\), \\(u_2' = y_1 f / W\\).",
      "احسب الرونسكيان لمجموعة الحلول ثم كامل لإيجاد دوال الثوابت المتغيرة.")

    # 305: Phase Portrait Classification
    svg_phase_saddle = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-60 -60 120 120' width='100%' height='100%' style='background:#0d1117;'>
  <line x1='-55' y1='0' x2='55' y2='0' stroke='#8b949e' stroke-width='1.5'/>
  <line x1='0' y1='-55' x2='0' y2='55' stroke='#8b949e' stroke-width='1.5'/>
  <!-- Hyperbolic trajectories -->
  <path d='M -40,-45 Q 0,-15 40,-45' fill='none' stroke='#58a6ff' stroke-width='2'/>
  <path d='M -40,45 Q 0,15 40,45' fill='none' stroke='#58a6ff' stroke-width='2'/>
  <path d='M -45,-40 Q -15,0 -45,40' fill='none' stroke='#f0883e' stroke-width='2'/>
  <path d='M 45,-40 Q 15,0 45,40' fill='none' stroke='#f0883e' stroke-width='2'/>
  <!-- Arrows -->
  <polygon points='0,-20 -4,-28 4,-28' fill='#58a6ff'/>
  <polygon points='0,20 -4,28 4,28' fill='#58a6ff'/>
  <polygon points='-20,0 -28,-4 -28,4' fill='#f0883e'/>
  <polygon points='20,0 28,-4 28,4' fill='#f0883e'/>
  <circle cx='0' cy='0' r='3.5' fill='#f85149'/>
</svg>"""
    q("KAUST-P2-305", "Dynamical Systems", "Hard",
      "Classify the equilibrium point at the origin for the linear system \\(\\dot{\\mathbf{x}} = A\\mathbf{x}\\), where \\(A = \\begin{pmatrix} 1 & 3 \\\\ 2 & 2 \\end{pmatrix}\\).",
      "صنّف نقطة الاتزان عند نقطة الأصل للنظام الخطي \\(\\dot{\\mathbf{x}} = A\\mathbf{x}\\) حيث \\(A = \\begin{pmatrix} 1 & 3 \\\\ 2 & 2 \\end{pmatrix}\\).",
      ["Saddle point (unstable)", "Stable node", "Unstable spiral", "Center"],
      0,
      "Compute the trace and determinant of \\(A\\): \\(\\text{tr}(A) = 1 + 2 = 3\\), \\(\\det(A) = (1)(2) - (3)(2) = 2 - 6 = -4\\). Since \\(\\det(A) < 0\\), the eigenvalues have opposite real signs (specifically, \\(\\lambda^2 - 3\\lambda - 4 = 0 \\implies (\\lambda-4)(\\lambda+1) = 0\\), so \\(\\lambda_1 = 4, \\lambda_2 = -1\\)). Any planar system with one positive and one negative real eigenvalue has a saddle point at the origin.",
      "نحسب الأثر والمحدد: \\(\\text{tr}(A) = 3\\) و \\(\\det(A) = 2 - 6 = -4\\). بما أن المحدد سالب، فإن القيم الذاتية ذات إشارتين متعاكستين (\\(\\lambda_1 = 4, \\lambda_2 = -1\\)). النظام ذو القيم الذاتية الحقيقية المتعاكسة في الإشارة يمتلك نقطة سرج (saddle point) غير مستقرة.",
      "Check the sign of the determinant \\(\\det(A)\\).",
      "افحص إشارة محدد المصفوفة \\(\\det(A)\\).",
      diagram=svg_phase_saddle)

    # 306: Stability of Spiral / Focus
    q("KAUST-P2-306", "Dynamical Systems", "Medium",
      "For what range of parameter \\(a\\) is the origin an asymptotically stable spiral for the system \\(\\dot{x} = ax - 4y\\), \\(\\dot{y} = x + ay\\)?",
      "ما مدى المعلمة \\(a\\) الذي يجعل نقطة الأصل بؤرة مستقرة مقاربياً (asymptotically stable spiral) للنظام \\(\\dot{x} = ax - 4y\\), \\(\\dot{y} = x + ay\\)؟",
      ["\\(a < 0\\)", "\\(a > 0\\)", "\\(-2 < a < 0\\)", "\\(a = 0\\)"],
      0,
      "The system matrix is \\(A = \\begin{pmatrix} a & -4 \\\\ 1 & a \\end{pmatrix}\\). Its characteristic equation is \\((\\lambda - a)^2 + 4 = 0 \\implies \\lambda = a \\pm 2i\\). For the origin to be a spiral (focus), the eigenvalues must be complex conjugates with non-zero imaginary parts (which is satisfied since \\(\\text{Im}(\\lambda) = \\pm 2 \\neq 0\\)). For asymptotic stability, the real part must be strictly negative, so \\(\\text{Re}(\\lambda) = a < 0\\).",
      "مصفوفة النظام هي \\(A = \\begin{pmatrix} a & -4 \\\\ 1 & a \\end{pmatrix}\\). معادلتها المميّزة هي \\((\\lambda-a)^2 + 4 = 0\\) أي \\(\\lambda = a \\pm 2i\\). لكي تكون النقطة بؤرة مستقرة مقاربياً، يجب أن يكون الجزء الحقيقي سالباً تماماً، أي \\(a < 0\\).",
      "Find the eigenvalues in terms of \\(a\\) and examine the real part.",
      "أوجد القيم الذاتية بدلالة \\(a\\) وافحص الجزء الحقيقي.")

    # 307: Laplace Transform of Dirac Delta with ODE
    q("KAUST-P2-307", "Differential Equations", "Hard",
      "Solve the initial value problem \\(y'' + 4y = 6\\delta(t - \\pi)\\) with \\(y(0) = 0\\) and \\(y'(0) = 0\\). What is \\(y(2\\pi)\\)?",
      "حل مسألة القيمة الابتدائية \\(y'' + 4y = 6\\delta(t - \\pi)\\) مع \\(y(0) = 0\\) و \\(y'(0) = 0\\). ما قيمة \\(y(2\\pi)\\)؟",
      ["\\(0\\)", "\\(3\\)", "\\(-3\\)", "\\(6\\)"],
      0,
      "Apply Laplace transform: \\((s^2 + 4)Y(s) = 6e^{-\\pi s} \\implies Y(s) = 3 e^{-\\pi s} \\frac{2}{s^2 + 4}\\). Taking the inverse transform: \\(y(t) = 3 u(t - \\pi) \\sin(2(t - \\pi))\\). Since \\(\\sin(2(t-\\pi)) = \\sin(2t - 2\\pi) = \\sin(2t)\\), we have \\(y(t) = 3 u(t-\\pi) \\sin(2t)\\). Evaluating at \\(t = 2\\pi\\): \\(y(2\\pi) = 3(1)\\sin(4\\pi) = 0\\).",
      "بتطبيق تحويل لابلاس: \\((s^2+4)Y(s) = 6e^{-\\pi s} \\implies Y(s) = 3 e^{-\\pi s} \\frac{2}{s^2+4}\\). بالتحويل العكسي: \\(y(t) = 3 u(t-\\pi)\\sin(2t)\\). عند \\(t = 2\\pi\\)، نجد \\(y(2\\pi) = 3\\sin(4\\pi) = 0\\).",
      "Recall \\(\\mathcal{L}\\{\\delta(t-t_0)\\} = e^{-s t_0}\\) and \\(\\mathcal{L}^{-1}\\{e^{-s t_0}F(s)\\} = f(t-t_0)u(t-t_0)\\).",
      "تذكر خاصية الإزاحة لتحويل لابلاس لدالة ديراك ودالة الخطوة.")

    # 308: Laplace Transform Convolution
    q("KAUST-P2-308", "Differential Equations", "Hard",
      "Find the solution to the Volterra integral equation \\(y(t) = t + \\int_0^t (t - \\tau) y(\\tau) d\\tau\\).",
      "أوجد حل معادلة فولتيرا التكاملية \\(y(t) = t + \\int_0^t (t - \\tau) y(\\tau) d\\tau\\).",
      ["\\(y(t) = \\sinh t\\)", "\\(y(t) = \\cosh t\\)", "\\(y(t) = \\sin t\\)", "\\(y(t) = e^t - 1\\)"],
      0,
      "Recognize the integral as a convolution: \\(y(t) = t + t * y(t)\\). Taking the Laplace transform: \\(Y(s) = \\frac{1}{s^2} + \\frac{1}{s^2}Y(s)\\). Thus \\(Y(s)\\left(1 - \\frac{1}{s^2}\\right) = \\frac{1}{s^2} \\implies Y(s)\\left(\\frac{s^2-1}{s^2}\\right) = \\frac{1}{s^2} \\implies Y(s) = \\frac{1}{s^2 - 1}\\). Taking the inverse transform: \\(y(t) = \\sinh t\\).",
      "نلاحظ أن التكامل هو التفاف (convolution): \\(y(t) = t + t * y(t)\\). بأخذ تحويل لابلاس: \\(Y(s) = \\frac{1}{s^2} + \\frac{1}{s^2}Y(s)\\). بالتبسيط: \\(Y(s) = \\frac{1}{s^2 - 1}\\). بالتحويل العكسي نجد \\(y(t) = \\sinh t\\).",
      "Use the convolution theorem: \\(\\mathcal{L}\\{f * g\\} = F(s)G(s)\\).",
      "استخدم نظرية الالتفاف: \\(\\mathcal{L}\\{f * g\\} = F(s)G(s)\\).")

    # 309: Matrix Exponential
    q("KAUST-P2-309", "Linear Systems", "Hard",
      "Compute the matrix exponential \\(e^{At}\\) for the nilpotent matrix \\(A = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 2 \\\\ 0 & 0 & 0 \\end{pmatrix}\\).",
      "احسب الأسّي المصفوفي \\(e^{At}\\) للمصفوفة عديمة القوى (nilpotent) \\(A = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 2 \\\\ 0 & 0 & 0 \\end{pmatrix}\\).",
      ["\\(\\begin{pmatrix} 1 & t & t^2 \\\\ 0 & 1 & 2t \\\\ 0 & 0 & 1 \\end{pmatrix}\\)", "\\(\\begin{pmatrix} 1 & t & \\frac{t^2}{2} \\\\ 0 & 1 & t \\\\ 0 & 0 & 1 \\end{pmatrix}\\)", "\\(\\begin{pmatrix} e^t & t & 2t \\\\ 0 & e^t & 2t \\\\ 0 & 0 & e^t \\end{pmatrix}\\)", "\\(\\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}\\)"],
      0,
      "Compute powers of \\(A\\): \\(A^2 = \\begin{pmatrix} 0 & 0 & 2 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}\\), and \\(A^3 = 0\\). Therefore, \\(e^{At} = I + At + \\frac{A^2 t^2}{2} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix} + \\begin{pmatrix} 0 & t & 0 \\\\ 0 & 0 & 2t \\\\ 0 & 0 & 0 \\end{pmatrix} + \\begin{pmatrix} 0 & 0 & t^2 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 1 & t & t^2 \\\\ 0 & 1 & 2t \\\\ 0 & 0 & 1 \\end{pmatrix}\\).",
      "نحسب قوى \\(A\\): نجد \\(A^2 = \\begin{pmatrix} 0 & 0 & 2 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}\\) و \\(A^3 = 0\\). بالتالي السلسلة تنتهي عند الحد الثاني: \\(e^{At} = I + At + \\frac{1}{2}A^2 t^2\\). بجمع المصفوفات نحصل على النتيجة المطلوبة.",
      "Since \\(A^3 = 0\\), the Taylor series truncates after the quadratic term.",
      "بما أن \\(A^3 = 0\\)، تتوقف متسلسلة تايلور عند الحد التربيعي.")

    # 310: Non-homogeneous System via Diagonalization
    q("KAUST-P2-310", "Differential Equations", "Hard",
      "The system \\(\\dot{\\mathbf{x}} = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\mathbf{x} + \\begin{pmatrix} e^{2t} \\\\ 0 \\end{pmatrix}\\) has initial condition \\(\\mathbf{x}(0) = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\). Find \\(x_1(t)\\).",
      "النظام \\(\\dot{\\mathbf{x}} = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\mathbf{x} + \\begin{pmatrix} e^{2t} \\\\ 0 \\end{pmatrix}\\) له الشرط الابتدائي \\(\\mathbf{x}(0) = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\). أوجد \\(x_1(t)\\).",
      ["\\(x_1(t) = (1 + t)e^{2t}\\)", "\\(x_1(t) = e^{3t} - e^{2t}\\)", "\\(x_1(t) = e^{2t} + t^2 e^{2t}\\)", "\\(x_1(t) = \\cos(t)e^{2t}\\)"],
      0,
      "From the second row, \\(\\dot{x}_2 = 3x_2\\) with \\(x_2(0) = 0\\), which uniquely yields \\(x_2(t) = 0\\) for all \\(t\\). Substituting into the first row gives \\(\\dot{x}_1 = 2x_1 + x_2 + e^{2t} = 2x_1 + e^{2t}\\). This is a first-order linear ODE: \\(\\dot{x}_1 - 2x_1 = e^{2t}\\). Using integrating factor \\(e^{-2t}\\): \\(\\frac{d}{dt}(x_1 e^{-2t}) = 1 \\implies x_1 e^{-2t} = t + C\\). With \\(x_1(0) = 1\\), we have \\(C = 1\\), so \\(x_1(t) = (1+t)e^{2t}\\).",
      "من المعادلة الثانية: \\(\\dot{x}_2 = 3x_2\\) مع \\(x_2(0) = 0\\) ينتج \\(x_2(t) \\equiv 0\\). بالتعويض في المعادلة الأولى: \\(\\dot{x}_1 - 2x_1 = e^{2t}\\). بالضرب في عامل المكاملة \\(e^{-2t}\\) نصل إلى \\(x_1 e^{-2t} = t + C\\). من الشرط الابتدائي \\(C = 1\\)، إذن \\(x_1(t) = (1+t)e^{2t}\\).",
      "Solve for \\(x_2(t)\\) first from the decoupled bottom equation.",
      "حل لمعرفة \\(x_2(t)\\) أولاً من المعادلة السفلية المستقلة.")

    # 311: Frobenius Method - Indicial Equation
    q("KAUST-P2-311", "Differential Equations", "Hard",
      "Determine the roots of the indicial equation for the differential equation \\(2x^2 y'' + x(2x+1)y' - y = 0\\) about the regular singular point \\(x = 0\\).",
      "حدد جذور المعادلة الدليلية (indicial equation) للمعادلة التفاضلية \\(2x^2 y'' + x(2x+1)y' - y = 0\\) حول النقطة الشاذة المنتظمة \\(x = 0\\).",
      ["\\(r_1 = 1, r_2 = -\\frac{1}{2}\\)", "\\(r_1 = 2, r_2 = -1\\)", "\\(r_1 = \\frac{1}{2}, r_2 = -1\\)", "\\(r_1 = 0, r_2 = -1\\)"],
      0,
      "Standard form: \\(y'' + \\frac{2x+1}{2x}y' - \\frac{1}{2x^2}y = 0\\). Here \\(p_0 = \\lim_{x\\to 0} x p(x) = \\lim_{x\\to 0} \\frac{2x+1}{2} = \\frac{1}{2}\\), and \\(q_0 = \\lim_{x\\to 0} x^2 q(x) = -\\frac{1}{2}\\). The indicial equation is \\(r(r-1) + p_0 r + q_0 = 0 \\implies r(r-1) + \\frac{1}{2}r - \\frac{1}{2} = 0 \\implies r^2 - \\frac{1}{2}r - \\frac{1}{2} = 0 \\implies 2r^2 - r - 1 = 0 \\implies (2r+1)(r-1) = 0\\). Thus the roots are \\(r = 1\\) and \\(r = -\\frac{1}{2}\\).",
      "نكتب المعادلة بالصورة القياسية ونحسب \\(p_0 = \\lim_{x\\to 0} xp(x) = 1/2\\) و \\(q_0 = \\lim_{x\\to 0} x^2 q(x) = -1/2\\). المعادلة الدليلية هي \\(r(r-1) + p_0 r + q_0 = 0\\)، أي \\(2r^2 - r - 1 = 0\\)، وجذورها هما \\(r_1 = 1\\) و \\(r_2 = -1/2\\).",
      "Recall the indicial equation formula \\(F(r) = r(r-1) + p_0 r + q_0 = 0\\).",
      "تذكر صيغة المعادلة الدليلية \\(r(r-1) + p_0 r + q_0 = 0\\).")

    # 312: Bessel Function Identity
    q("KAUST-P2-312", "Special Functions", "Hard",
      "Using the recurrence relations for Bessel functions of the first kind \\(J_n(x)\\), express \\(J_2(x)\\) in terms of \\(J_0(x)\\) and \\(J_1(x)\\).",
      "باستخدام العلاقات التكرارية لدوال بيسل من النوع الأول \\(J_n(x)\\)، عبّر عن \\(J_2(x)\\) بدلالة \\(J_0(x)\\) و \\(J_1(x)\\).",
      ["\\(J_2(x) = \\frac{2}{x}J_1(x) - J_0(x)\\)", "\\(J_2(x) = \\frac{1}{x}J_1(x) - 2J_0(x)\\)", "\\(J_2(x) = J_0(x) - \\frac{2}{x}J_1(x)\\)", "\\(J_2(x) = \\frac{2}{x}J_0(x) + J_1(x)\\)"],
      0,
      "The fundamental recurrence relation for Bessel functions is \\(J_{n-1}(x) + J_{n+1}(x) = \\frac{2n}{x}J_n(x)\\). Setting \\(n = 1\\): \\(J_0(x) + J_2(x) = \\frac{2}{x}J_1(x) \\implies J_2(x) = \\frac{2}{x}J_1(x) - J_0(x)\\).",
      "العلاقة التكرارية الأساسية لدوال بيسل هي \\(J_{n-1}(x) + J_{n+1}(x) = \\frac{2n}{x}J_n(x)\\). بوضع \\(n = 1\\) نجد: \\(J_0(x) + J_2(x) = \\frac{2}{x}J_1(x)\\)، ومنه \\(J_2(x) = \\frac{2}{x}J_1(x) - J_0(x)\\).",
      "Set \\(n=1\\) in the standard recurrence relation \\(J_{n-1}(x) + J_{n+1}(x) = \\frac{2n}{x}J_n(x)\\).",
      "ضع \\(n=1\\) في العلاقة التكرارية المعروفة لدوال بيسل.")

    # 313: Sturm-Liouville Eigenvalues
    q("KAUST-P2-313", "Differential Equations", "Hard",
      "Find the eigenvalues \\(\\lambda_n\\) and normalized eigenfunctions \\(y_n(x)\\) of the regular Sturm-Liouville problem \\(y'' + \\lambda y = 0\\) with boundary conditions \\(y(0) = 0\\) and \\(y'(\\pi) = 0\\).",
      "أوجد القيم الذاتية \\(\\lambda_n\\) والدوال الذاتية المعيارية \\(y_n(x)\\) لمسألة شتورم-ليوفيل المنتظمة \\(y'' + \\lambda y = 0\\) مع الشروط الحدية \\(y(0) = 0\\) و \\(y'(\\pi) = 0\\).",
      ["\\(\\lambda_n = \\left(n - \\frac{1}{2}\\right)^2, \\quad y_n(x) = \\sqrt{\\frac{2}{\\pi}} \\sin\\left(\\left(n - \\frac{1}{2}\\right)x\\right)\\)",
       "\\(\\lambda_n = n^2, \\quad y_n(x) = \\sqrt{\\frac{2}{\\pi}} \\sin(nx)\\)",
       "\\(\\lambda_n = \\left(\\frac{n}{2}\\right)^2, \\quad y_n(x) = \\sqrt{\\frac{1}{\\pi}} \\cos\\left(\\frac{nx}{2}\\right)\\)",
       "\\(\\lambda_n = (2n)^2, \\quad y_n(x) = \\sqrt{\\frac{2}{\\pi}} \\sin(2nx)\\)"],
      0,
      "For \\(\\lambda > 0\\), write \\(\\lambda = k^2\\). General solution is \\(y(x) = A \\cos(kx) + B \\sin(kx)\\). \\(y(0) = 0 \\implies A = 0\\), so \\(y(x) = B \\sin(kx)\\). Then \\(y'(x) = B k \\cos(kx)\\). The condition \\(y'(\\pi) = 0 \\implies \\cos(k\\pi) = 0 \\implies k\\pi = (n - 1/2)\\pi \\implies k_n = n - 1/2\\) for \\(n = 1, 2, 3, \\dots\\). Thus \\(\\lambda_n = (n - 1/2)^2\\). Normalizing over \\([0, \\pi]\\): \\(\\int_0^\\pi \\sin^2(k_n x) dx = \\frac{\\pi}{2}\\), giving normalizer \\(\\sqrt{2/\\pi}\\).",
      "نكتب \\(\\lambda = k^2\\). الحل العام \\(y = A\\cos(kx) + B\\sin(kx)\\). من الشرط \\(y(0)=0\\) نجد \\(A=0\\). الشرط \\(y'(\\pi)=0\\) يعطي \\(Bk\\cos(k\\pi) = 0\\) أي \\(k = n - 1/2\\). بالتالي \\(\\lambda_n = (n-1/2)^2\\) والدوال الذاتية المعيارية هي \\(\\sqrt{2/\\pi}\\sin((n-1/2)x)\\).",
      "Differentiate the general sinusoidal solution and set the derivative to zero at \\(x = \\pi\\).",
      "فاضل الحل الجيبي العام وساوي المشتقة بالصفر عند \\(x = \\pi\\).")

    # 314: Non-linear Pendulum Linearization
    q("KAUST-P2-314", "Dynamical Systems", "Medium",
      "Consider the nonlinear pendulum equation \\(\\ddot{\\theta} + \\sin\\theta = 0\\). In state-space with \\(x_1 = \\theta, x_2 = \\dot{\\theta}\\), what is the Jacobian matrix at the inverted equilibrium point \\((\\pi, 0)\\), and what is its stability?",
      "تأمل معادلة البندول اللاخطي \\(\\ddot{\\theta} + \\sin\\theta = 0\\). في فضاء الحالة مع \\(x_1 = \\theta, x_2 = \\dot{\\theta}\\)، ما هي مصفوفة جاكوبي عند نقطة الاتزان المقلوبة \\((\\pi, 0)\\)، وما هو نوع استقرارها؟",
      ["\\(J = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}\\), Saddle (unstable)",
       "\\(J = \\begin{pmatrix} 0 & 1 \\\\ -1 & 0 \\end{pmatrix}\\), Center (neutrally stable)",
       "\\(J = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\), Stable node",
       "\\(J = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}\\), Spiral source"],
      0,
      "The system is \\(\\dot{x}_1 = x_2\\), \\(\\dot{x}_2 = -\\sin x_1\\). The Jacobian is \\(J(x_1, x_2) = \\begin{pmatrix} 0 & 1 \\\\ -\\cos x_1 & 0 \\end{pmatrix}\\). At \\((\\pi, 0)\\), \\(\\cos\\pi = -1\\), so \\(J(\\pi, 0) = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}\\). The eigenvalues satisfy \\(\\det(J - \\lambda I) = \\lambda^2 - 1 = 0 \\implies \\lambda = \\pm 1\\). Since one eigenvalue is positive and one is negative, the inverted point is an unstable saddle point.",
      "النظام هو \\(\\dot{x}_1 = x_2\\) و \\(\\dot{x}_2 = -\\sin x_1\\). مصفوفة جاكوبي هي \\(\\begin{pmatrix} 0 & 1 \\\\ -\\cos x_1 & 0 \\end{pmatrix}\\). عند \\((\\pi, 0)\\) نجد \\(\\cos\\pi = -1\\) فتصبح المصفوفة \\(\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}\\). القيم الذاتية هي \\(\\pm 1\\)، وهي نقطة سرج غير مستقرة.",
      "Evaluate \\(-\\cos(\\pi)\\) in the Jacobian matrix.",
      "احسب \\(-\\cos(\\pi)\\) في مصفوفة جاكوبي.")

    # 315: Green's Function for 1D BVP
    q("KAUST-P2-315", "Differential Equations", "Hard",
      "What is the Green's function \\(G(x, \\xi)\\) for the boundary value problem \\(-y'' = f(x)\\) on \\([0, 1]\\) with \\(y(0) = 0\\) and \\(y(1) = 0\\)?",
      "ما هي دالة غرين \\(G(x, \\xi)\\) لمسألة القيمة الحدية \\(-y'' = f(x)\\) على \\([0, 1]\\) مع الشروط \\(y(0) = 0\\) و \\(y(1) = 0\\)؟",
      ["\\(G(x, \\xi) = \\begin{cases} x(1 - \\xi), & x \\le \\xi \\\\ \\xi(1 - x), & x > \\xi \\end{cases}\\)",
       "\\(G(x, \\xi) = \\begin{cases} x \\xi, & x \\le \\xi \\\\ (1-x)(1-\\xi), & x > \\xi \\end{cases}\\)",
       "\\(G(x, \\xi) = \\frac{1}{2}|x - \\xi|\\)",
       "\\(G(x, \\xi) = \\sin(\\pi x)\\sin(\\pi \\xi)\\)"],
      0,
      "The homogeneous equation \\(-y'' = 0\\) has solution \\(y_1(x) = x\\) satisfying \\(y_1(0) = 0\\), and \\(y_2(x) = 1 - x\\) satisfying \\(y_2(1) = 0\\). The Wronskian is \\(W(y_1, y_2) = y_1 y_2' - y_1' y_2 = x(-1) - (1)(1-x) = -1\\). In \\(-y'' = f\\), the differential operator has \\(p(x) = 1\\), so \\(p W = -1\\). The Green's function is \\(G(x, \\xi) = -\\frac{y_1(\\min(x,\\xi))y_2(\\max(x,\\xi))}{p W} = \\begin{cases} x(1-\\xi), & x \\le \\xi \\\\ \\xi(1-x), & x > \\xi \\end{cases}\\).",
      "حلول المعادلة المتجانسة التي تحقق الشروط الحدية هي \\(y_1(x) = x\\) عند 0 و \\(y_2(x) = 1-x\\) عند 1. الرونسكيان \\(W = -1\\). بالتعويض في صيغة دالة غرين القياسية للمؤثر \\(-d^2/dx^2\\)، نحصل على الدالة المتماثلة المعطاة.",
      "Use the product of homogeneous solutions satisfying left and right boundary conditions, divided by the Wronskian.",
      "استخدم حاصل ضرب حلين متجانسين يحققان الشروط الطرفية مقسوماً على الرونسكيان.")

    # 316: Clairaut's Equation
    q("KAUST-P2-316", "Differential Equations", "Hard",
      "Find the singular solution (envelope) of Clairaut's differential equation \\(y = x y' + (y')^2\\).",
      "أوجد الحل الشاذ (الغلاف - envelope) لمعادلة كليرو التفاضلية \\(y = x y' + (y')^2\\).",
      ["\\(y = -\\frac{x^2}{4}\\)", "\\(y = \\frac{x^2}{4}\\)", "\\(y = -x^2\\)", "\\(y = 2x\\)"],
      0,
      "Differentiate with respect to \\(x\\): \\(y' = y' + x y'' + 2 y' y'' \\implies y''(x + 2y') = 0\\). The condition \\(y'' = 0\\) yields the general solution family of lines \\(y = cx + c^2\\). The condition \\(x + 2y' = 0 \\implies y' = -\\frac{x}{2}\\). Substituting \\(y' = -x/2\\) back into the original ODE: \\(y = x\\left(-\\frac{x}{2}\\right) + \\left(-\\frac{x}{2}\\right)^2 = -\\frac{x^2}{2} + \\frac{x^2}{4} = -\\frac{x^2}{4}\\). This parabola is the singular envelope solution.",
      "بتفاضل طرفي معادلة كليرو بالنسبة لـ \\(x\\): \\(y'' (x + 2y') = 0\\). الحالة \\(y'' = 0\\) تعطي الحل العام (حزمة مستقيمات). الحالة الثانية \\(x + 2y' = 0\\) تعطي \\(y' = -x/2\\). بالتعويض في المعادلة الأصلية نجد الحل الشاذ: \\(y = -x^2/4\\).",
      "Differentiate the ODE with respect to \\(x\\) and set the second factor \\(x + f'(y') = 0\\).",
      "فاضل المعادلة بالنسبة لـ \\(x\\) وساوي المعامل الثاني بالصفر.")

    # 317: Limit Cycles & Poincaré-Bendixson
    q("KAUST-P2-317", "Dynamical Systems", "Hard",
      "Consider the system in polar coordinates: \\(\\dot{r} = r(1 - r^2)(4 - r^2)\\), \\(\\dot{\\theta} = 1\\). How many limit cycles does this system possess in \\(\\mathbb{R}^2\\), and what is the stability of the inner one?",
      "تأمل النظام بالإحداثيات القطبية: \\(\\dot{r} = r(1 - r^2)(4 - r^2)\\), \\(\\dot{\\theta} = 1\\). كم دورة حدية (limit cycle) يمتلكها هذا النظام في \\(\\mathbb{R}^2\\)، وما هو استقرار الدورة الداخلية؟",
      ["Two limit cycles; the inner cycle (\\(r=1\\)) is stable",
       "Two limit cycles; the inner cycle (\\(r=1\\)) is unstable",
       "One limit cycle; it is semistable",
       "Four limit cycles; all are unstable"],
      0,
      "Limit cycles correspond to periodic orbits, which here occur at non-zero constant radii where \\(\\dot{r} = 0\\). Setting \\(r(1 - r^2)(4 - r^2) = 0\\) for \\(r > 0\\) yields \\(r = 1\\) and \\(r = 2\\). There are exactly 2 limit cycles (circles of radii 1 and 2). To determine stability of \\(r = 1\\): for \\(r \\in (0, 1)\\), \\(\\dot{r} > 0\\) (trajectories move outward toward \\(r=1\\)); for \\(r \\in (1, 2)\\), \\(1-r^2 < 0\\) and \\(4-r^2 > 0\\), so \\(\\dot{r} < 0\\) (trajectories move inward toward \\(r=1\\)). Hence \\(r = 1\\) is asymptotically stable.",
      "تتوافق الدورات الحدية مع الأقطار الثابتة التي تحقق \\(\\dot{r} = 0\\) مع \\(r > 0\\)، أي \\(r = 1\\) و \\(r = 2\\) (دورتان حديتان). لاختبار استقرار \\(r=1\\): عندما \\(0 < r < 1\\) تكون \\(\\dot{r} > 0\\)، وعندما \\(1 < r < 2\\) تكون \\(\\dot{r} < 0\\)، مما يعني أن المسارات تتقارب نحو الدائرة \\(r=1\\)، فهي مستقرة مقاربياً.",
      "Analyze the sign of \\(\\dot{r}\\) on both sides of \\(r = 1\\).",
      "حلل إشارة \\(\\dot{r}\\) على جانبي \\(r = 1\\).")

    # 318: Riccati Equation
    q("KAUST-P2-318", "Differential Equations", "Hard",
      "Given that \\(y_1(x) = x\\) is a known particular solution of the Riccati equation \\(y' = 1 - x^2 + y^2\\), find the general solution.",
      "علماً بأن \\(y_1(x) = x\\) هو حل خاص معروف لمعادلة ريكاتي \\(y' = 1 - x^2 + y^2\\)، أوجد الحل العام.",
      ["\\(y(x) = x + \\frac{1}{C e^{-x^2} - \\int_0^x e^{-(x^2 - t^2)} dt}\\)",
       "\\(y(x) = x + C e^{x^2}\\)",
       "\\(y(x) = x + \\frac{1}{C - x}\\)",
       "\\(y(x) = x \\tan(x + C)\\)"],
      0,
      "Substitute \\(y = y_1 + \\frac{1}{u} = x + \\frac{1}{u}\\). Differentiating: \\(y' = 1 - \\frac{u'}{u^2}\\). The equation becomes \\(1 - \\frac{u'}{u^2} = 1 - x^2 + \\left(x + \\frac{1}{u}\\right)^2 = 1 - x^2 + x^2 + \\frac{2x}{u} + \\frac{1}{u^2} = 1 + \\frac{2x}{u} + \\frac{1}{u^2}\\). Subtract 1 and multiply by \\(-u^2\\): \\(u' + 2x u = -1\\). The integrating factor is \\(e^{\\int 2x dx} = e^{x^2}\\). Thus \\((u e^{x^2})' = -e^{x^2} \\implies u(x) e^{x^2} = C - \\int_0^x e^{t^2} dt \\implies u(x) = C e^{-x^2} - e^{-x^2}\\int_0^x e^{t^2} dt = C e^{-x^2} - \\int_0^x e^{-(x^2-t^2)} dt\\). Hence \\(y(x) = x + \\frac{1}{u(x)}\\).",
      "نستخدم التحويل القياسي لمعادلة ريكاتي \\(y = y_1 + 1/u = x + 1/u\\). بالتعويض والتبسيط نصل إلى معادلة خطية من الرتبة الأولى لـ \\(u\\): \\(u' + 2xu = -1\\). عامل المكاملة هو \\(e^{x^2}\\)، وبالمكاملة نجد \\(u(x)\\) والحل العام المطلوب.",
      "Use the transformation \\(y = y_1 + \\frac{1}{u}\\) to convert the Riccati equation into a linear ODE for \\(u\\).",
      "استخدم التحويل \\(y = y_1 + 1/u\\) لتحويل معادلة ريكاتي إلى معادلة خطية.")

    # 319: Abel's Identity for Wronskian
    q("KAUST-P2-319", "Differential Equations", "Medium",
      "If \\(y_1\\) and \\(y_2\\) are linearly independent solutions of \\(x y'' + 2y' + x e^x y = 0\\) on \\(x > 0\\) with Wronskian \\(W(1) = 3\\), what is \\(W(3)\\)?",
      "إذا كان \\(y_1\\) و \\(y_2\\) حلين مستقلين خطياً للمعادلة \\(x y'' + 2y' + x e^x y = 0\\) على \\(x > 0\\) مع قيمة الرونسكيان \\(W(1) = 3\\)، فما قيمة \\(W(3)\\)؟",
      ["\\(\\frac{1}{3}\\)", "\\(1\\)", "\\(3\\)", "\\(\\frac{1}{9}\\)"],
      0,
      "Rewrite in standard form: \\(y'' + \\frac{2}{x}y' + e^x y = 0\\), so \\(P(x) = \\frac{2}{x}\\). By Abel's Identity, \\(W(x) = W(x_0) \\exp\\left(-\\int_{x_0}^x P(t) dt\\right) = W(1) \\exp\\left(-\\int_1^x \\frac{2}{t} dt\\right) = 3 \\exp(-2 \\ln x) = \\frac{3}{x^2}\\). At \\(x = 3\\), \\(W(3) = \\frac{3}{3^2} = \\frac{3}{9} = \\frac{1}{3}\\).",
      "نكتب المعادلة بالصورة القياسية \\(y'' + (2/x)y' + e^x y = 0\\) حيث \\(P(x) = 2/x\\). بتطبيق متطابقة آبل: \\(W(x) = W(1) \\exp(-\\int_1^x 2/t dt) = 3 / x^2\\). عند \\(x=3\\) نجد \\(W(3) = 3/9 = 1/3\\).",
      "Apply Abel's Identity: \\(W(x) = C e^{-\\int P(x)dx}\\).",
      "طبق متطابقة آبل: \\(W(x) = C e^{-\\int P(x)dx}\\).")

    # 320: Lyapunov Function Stability
    q("KAUST-P2-320", "Dynamical Systems", "Hard",
      "Consider the nonlinear system \\(\\dot{x} = -x + y^2\\), \\(\\dot{y} = -2y - x y\\). Using the candidate Lyapunov function \\(V(x, y) = x^2 + y^2\\), what can be concluded about the origin?",
      "تأمل النظام اللاخطي \\(\\dot{x} = -x + y^2\\), \\(\\dot{y} = -2y - x y\\). باستخدام دالة ليابونوف المرشحة \\(V(x, y) = x^2 + y^2\\)، ما الاستنتاج حول نقطة الأصل؟",
      ["Locally asymptotically stable", "Unstable", "Neutrally stable (center)", "Inconclusive because \\(\\dot{V}\\) is indefinite"],
      0,
      "Compute \\(\\dot{V} = \\frac{\\partial V}{\\partial x}\\dot{x} + \\frac{\\partial V}{\\partial y}\\dot{y} = 2x(-x + y^2) + 2y(-2y - xy) = -2x^2 + 2xy^2 - 4y^2 - 2xy^2 = -2x^2 - 4y^2\\). Notice the cross terms \\(+2xy^2\\) and \\(-2xy^2\\) cancel out completely! Thus \\(\\dot{V}(x, y) = -2x^2 - 4y^2\\), which is strictly negative for all \\((x, y) \\neq (0, 0)\\). By Lyapunov's Direct Theorem, the origin is asymptotically stable.",
      "نحسب المشتقة الزمنية لدالة ليابونوف: \\(\\dot{V} = 2x(-x+y^2) + 2y(-2y-xy) = -2x^2 - 4y^2\\). تلاشت الحدود غير الخطية تماماً! بما أن \\(\\dot{V} < 0\\) لجميع النقاط غير الصفرية، فإن نقطة الأصل مستقرة مقاربياً.",
      "Differentiate \\(V(x,y)\\) along system trajectories and simplify.",
      "فاضل \\(V(x,y)\\) على طول مسارات النظام وبسط المقدار.")

    # 321 to 350: Continuing systematic generation of Advanced ODE / Dynamical Systems questions
    # 321: Reduction of Order
    q("KAUST-P2-321", "Differential Equations", "Medium",
      "Given that \\(y_1(x) = e^x\\) is a solution to \\(x y'' - (2x+1)y' + (x+1)y = 0\\), use reduction of order with \\(y_2 = v(x)e^x\\) to find a second independent solution.",
      "علماً بأن \\(y_1(x) = e^x\\) حل للمعادلة \\(x y'' - (2x+1)y' + (x+1)y = 0\\)، استخدم طريقة خفض الرتبة \\(y_2 = v(x)e^x\\) لإيجاد حل مستقل ثانٍ.",
      ["\\(y_2(x) = e^x x^2\\)", "\\(y_2(x) = x e^x\\)", "\\(y_2(x) = e^{-x}\\)", "\\(y_2(x) = x^2\\)"],
      0,
      "Substitute \\(y = v e^x\\). Then \\(y' = (v' + v)e^x\\), \\(y'' = (v'' + 2v' + v)e^x\\). Substitute into the ODE: \\(x(v'' + 2v' + v) - (2x+1)(v' + v) + (x+1)v = 0\\). The \\(v\\) coefficient is \\(x - (2x+1) + x + 1 = 0\\). The \\(v'\\) term is \\(2x - (2x+1) = -1\\). So \\(x v'' - v' = 0 \\implies \\frac{v''}{v'} = \\frac{1}{x} \\implies \\ln v' = \\ln x \\implies v' = x \\implies v(x) = \\frac{x^2}{2}\\). Thus \\(y_2(x) = x^2 e^x\\).",
      "بالتعويض عن \\(y = v e^x\\) في المعادلة التفاضلية نصل إلى \\(x v'' - v' = 0\\)، أي \\(v''/v' = 1/x\\). بالتالي \\(v' = x\\) و \\(v = x^2/2\\). إذن الحل المستقل الثاني هو \\(x^2 e^x\\).",
      "Look at the resulting equation for \\(w = v'\\).",
      "انظر إلى المعادلة الناتجة للمتغير \\(w = v'\\).")

    # 322: Non-homogeneous 2nd Order ODE - Resonance
    q("KAUST-P2-322", "Differential Equations", "Medium",
      "Find the general form of the particular solution \\(y_p(t)\\) to the undamped forced oscillator equation \\(y'' + 9y = 4\\cos(3t)\\).",
      "أوجد الصورة العامة للحل الخاص \\(y_p(t)\\) لمعادلة المهتز القسري غير المخمد \\(y'' + 9y = 4\\cos(3t)\\).",
      ["\\(y_p(t) = \\frac{2}{3} t \\sin(3t)\\)", "\\(y_p(t) = \\frac{2}{3} \\cos(3t)\\)", "\\(y_p(t) = -\\frac{2}{3} t \\cos(3t)\\)", "\\(y_p(t) = t^2 \\sin(3t)\\)"],
      0,
      "The natural frequency is \\(\\omega_0 = 3\\). The driving frequency is \\(\\omega = 3\\). Because resonance occurs, try \\(y_p(t) = t(A\\cos 3t + B\\sin 3t)\\). Differentiating twice and substituting into \\(y'' + 9y\\): \\(y_p'' + 9y_p = 6(-A\\sin 3t + B\\cos 3t)\\). Setting this equal to \\(4\\cos 3t\\) gives \\(-6A = 0 \\implies A = 0\\), and \\(6B = 4 \\implies B = 2/3\\). Thus \\(y_p(t) = \\frac{2}{3}t\\sin(3t)\\).",
      "التردد الطبيعي هو \\(\\omega_0 = 3\\) وهو مطابق لتردد القوة الخارجية، مما يسبب رنيناً (resonance). نفرض \\(y_p = t(A\\cos 3t + B\\sin 3t)\\). بالتعويض نجد \\(A = 0\\) و \\(B = 2/3\\)، إذن \\(y_p(t) = \\frac{2}{3}t\\sin(3t)\\).",
      "When driving at the natural frequency, multiply the trial solution by \\(t\\).",
      "عندما يكون التردد الخارجي مساوياً للتردد الطبيعي، اضرب الحل التجريبي في \\(t\\).")

    # 323: Bifurcation - Pitchfork
    q("KAUST-P2-323", "Dynamical Systems", "Hard",
      "What type of bifurcation occurs at \\(r = 0\\) for the one-dimensional system \\(\\dot{x} = r x - x^3\\)?",
      "ما نوع التفرع (bifurcation) الذي يحدث عند \\(r = 0\\) للنظام أحادي البعد \\(\\dot{x} = r x - x^3\\)؟",
      ["Supercritical pitchfork bifurcation", "Subcritical pitchfork bifurcation", "Saddle-node bifurcation", "Transcritical bifurcation"],
      0,
      "Fixed points satisfy \\(x(r - x^2) = 0\\). For \\(r \\le 0\\), \\(x^* = 0\\) is the only fixed point and it is stable since \\(f'(0) = r < 0\\). For \\(r > 0\\), \\(x^* = 0\\) becomes unstable (\\(f'(0) = r > 0\\)), and two new symmetric stable fixed points appear at \\(x^* = \\pm\\sqrt{r}\\). This emergence of two symmetric stable branches with a stabilizing cubic term \\(-x^3\\) defines a supercritical pitchfork bifurcation.",
      "نقاط الاتزان تحقق \\(x(r-x^2)=0\\). عندما \\(r \\le 0\\) توجد نقطة وحيدة مستقرة عند 0. عندما \\(r > 0\\) تصبح نقطة الأصل غير مستقرة وتظهر نقطتا اتزان متماثلتان مستقرتان عند \\(x = \\pm\\sqrt{r}\\). هذا يمثل تفرع شوكة فوق حرج (supercritical pitchfork).",
      "Notice the reflection symmetry \\(x \\to -x\\) and the sign of the cubic term.",
      "لاحظ تناظر الانعكاس \\(x \\to -x\\) وإشارة الحد التكعيبي.")

    # 324: Bifurcation - Hopf
    q("KAUST-P2-324", "Dynamical Systems", "Hard",
      "Consider the planar system \\(\\dot{r} = r(\\mu - r^2)\\), \\(\\dot{\\theta} = 1 + r^2\\). What occurs as parameter \\(\\mu\\) crosses 0 from negative to positive?",
      "تأمل النظام المستوي \\(\\dot{r} = r(\\mu - r^2)\\), \\(\\dot{\\theta} = 1 + r^2\\). ماذا يحدث عندما تجتاز المعلمة \\(\\mu\\) الصفر من السالب إلى الموجب؟",
      ["A stable limit cycle of radius \\(\\sqrt{\\mu}\\) is born (supercritical Hopf bifurcation)",
       "An unstable limit cycle disappears (subcritical Hopf bifurcation)",
       "A saddle-node collision annihilates all fixed points",
       "A homoclinic orbit bifurcates into a chaotic attractor"],
      0,
      "For \\(\\mu < 0\\), \\(\\dot{r} = r(\\mu - r^2) < 0\\) for all \\(r > 0\\), so the origin is a stable spiral. At \\(\\mu = 0\\), the eigenvalues cross the imaginary axis. For \\(\\mu > 0\\), the origin loses stability, and a new stable circular periodic orbit (limit cycle) of radius \\(r = \\sqrt{\\mu}\\) emerges. This is the prototypical normal form of a supercritical Hopf bifurcation.",
      "عندما \\(\\mu < 0\\) تكون نقطة الأصل بؤرة مستقرة. عند \\(\\mu = 0\\) تعبر القيم الذاتية المحور التخيلي. عندما \\(\\mu > 0\\) تفقد نقطة الأصل استقرارها وتولد دورة حدية دائرية مستقرة نصف قطرها \\(\\sqrt{\\mu}\\). هذا هو الشكل القياسي لتفرع هوبف فوق الحرج.",
      "Look at the sign of \\(\\dot{r}\\) near \\(r=0\\) when \\(\\mu > 0\\).",
      "انظر إلى إشارة \\(\\dot{r}\\) بالقرب من \\(r=0\\) عندما \\(\\mu > 0\\).")

    # 325: Orthogonal Trajectories
    q("KAUST-P2-325", "Differential Equations", "Medium",
      "Find the orthogonal trajectories to the family of parabolas \\(y = c x^2\\).",
      "أوجد المسارات المتعامدة (orthogonal trajectories) لعائلة القطوع المكافئة \\(y = c x^2\\).",
      ["\\(x^2 + 2y^2 = C\\)", "\\(x^2 - 2y^2 = C\\)", "\\(2x^2 + y^2 = C\\)", "\\(y^2 - x^2 = C\\)"],
      0,
      "Differentiating \\(y = c x^2\\) gives \\(y' = 2cx\\). Since \\(c = \\frac{y}{x^2}\\), we have \\(y' = 2\\left(\\frac{y}{x^2}\\right)x = \\frac{2y}{x}\\). The orthogonal trajectories satisfy \\(y' = -\\frac{x}{2y}\\). Separating variables: \\(2y dy = -x dx \\implies y^2 = -\\frac{x^2}{2} + k \\implies \\frac{x^2}{2} + y^2 = k \\implies x^2 + 2y^2 = C\\), which is a family of concentric ellipses.",
      "بتفاضل \\(y = cx^2\\) نجد \\(y' = 2cx = 2y/x\\). ميل المسارات المتعامدة هو \\(-x/(2y)\\). بفصل المتغيرات: \\(2y dy = -x dx\\)، وبالمكاملة: \\(x^2 + 2y^2 = C\\)، وهي عائلة من القطوع الناقصة.",
      "Replace \\(dy/dx\\) with \\(-dx/dy\\) after eliminating parameter \\(c\\).",
      "استبدل \\(dy/dx\\) بـ \\(-dx/dy\\) بعد التخلص من الثابت \\(c\\).")

    # 326: Initial Value Problem with Discontinuous Forcing
    q("KAUST-P2-326", "Differential Equations", "Medium",
      "Solve \\(y' + 2y = g(t)\\), \\(y(0) = 0\\), where \\(g(t) = \\begin{cases} 1, & 0 \\le t < 1 \\\\ 0, & t \\ge 1 \\end{cases}\\). What is \\(y(2)\\)?",
      "حل \\(y' + 2y = g(t)\\), \\(y(0) = 0\\)، حيث \\(g(t) = 1\\) لـ \\(0 \\le t < 1\\) و \\(0\\) لـ \\(t \\ge 1\\). ما قيمة \\(y(2)\\)؟",
      ["\\(\\frac{1}{2}(e^2 - 1)e^{-4}\\)", "\\(\\frac{1}{2}(1 - e^{-2})\\)", "\\(e^{-4}\\)", "\\(\\frac{1}{2}e^{-2}\\)"],
      0,
      "Write \\(g(t) = 1 - u(t-1)\\). The Laplace transform gives \\((s+2)Y(s) = \\frac{1}{s} - \\frac{e^{-s}}{s}\\). Thus \\(Y(s) = \\frac{1}{s(s+2)} - \\frac{e^{-s}}{s(s+2)}\\). Since \\(\\frac{1}{s(s+2)} = \\frac{1}{2}\\left(\\frac{1}{s} - \\frac{1}{s+2}\\right)\\), the inverse transform is \\(y(t) = \\frac{1}{2}(1 - e^{-2t}) - \\frac{1}{2}u(t-1)(1 - e^{-2(t-1)})\\). For \\(t = 2 > 1\\): \\(y(2) = \\frac{1}{2}(1 - e^{-4}) - \\frac{1}{2}(1 - e^{-2}) = \\frac{1}{2}(e^{-2} - e^{-4}) = \\frac{1}{2}(e^2 - 1)e^{-4}\\).",
      "نكتب الدالة بدلالة دالة هيفيسايد: \\(g(t) = 1 - u(t-1)\\). بتحويل لابلاس والكسور الجزئية نجد \\(y(t) = \\frac{1}{2}(1 - e^{-2t}) - \\frac{1}{2}u(t-1)(1 - e^{-2(t-1)})\\). عند \\(t=2\\) نحصل على \\(\\frac{1}{2}(e^2-1)e^{-4}\\).",
      "Express the step forcing as \\(1 - u(t-1)\\) and apply partial fractions to \\(\\frac{1}{s(s+2)}\\).",
      "عبر عن الدالة بدلالة دالة الخطوة واستخدم الكسور الجزئية.")

    # 327: Legendre Polynomial Orthogonality
    q("KAUST-P2-327", "Special Functions", "Hard",
      "Compute the value of the integral \\(\\int_{-1}^1 (3x^2 + 5x + 1) P_2(x) dx\\), where \\(P_2(x) = \\frac{1}{2}(3x^2 - 1)\\) is the second Legendre polynomial.",
      "احسب قيمة التكامل \\(\\int_{-1}^1 (3x^2 + 5x + 1) P_2(x) dx\\)، حيث \\(P_2(x) = \\frac{1}{2}(3x^2 - 1)\\) هو كثير حدود ليجاندر الثاني.",
      ["\\(\\frac{4}{5}\\)", "\\(0\\)", "\\(\\frac{2}{3}\\)", "\\(2\\)"],
      0,
      "Express \\(3x^2 + 5x + 1\\) in terms of Legendre polynomials: \\(P_0(x) = 1\\), \\(P_1(x) = x\\), \\(P_2(x) = \\frac{3x^2 - 1}{2} \\implies 3x^2 = 2P_2(x) + 1 = 2P_2(x) + P_0(x)\\). Thus, \\(3x^2 + 5x + 1 = 2P_2(x) + 5P_1(x) + 2P_0(x)\\). By the orthogonality relation \\(\\int_{-1}^1 P_m(x) P_n(x) dx = \\frac{2}{2n+1} \\delta_{mn}\\), all cross terms integrate to zero: \\(\\int_{-1}^1 (2P_2 + 5P_1 + 2P_0) P_2 dx = 2 \\int_{-1}^1 [P_2(x)]^2 dx = 2 \\left(\\frac{2}{2(2)+1}\\right) = 2 \\cdot \\frac{2}{5} = \\frac{4}{5}\\).",
      "نعبر عن كثيرة الحدود بدلالة كثيرات حدود ليجاندر: \\(3x^2 + 5x + 1 = 2P_2(x) + 5P_1(x) + 2P_0(x)\\). بالاستفادة من خاصية التعامد \\(\\int_{-1}^1 P_m P_n dx = \\frac{2}{2n+1}\\delta_{mn}\\)، تتلاشى الحدود المتعامدة ويتبقى \\(2 \\times \\frac{2}{5} = \\frac{4}{5}\\).",
      "Expand the quadratic polynomial in the Legendre basis \\(\\{P_0, P_1, P_2\\}\\) and use orthogonality.",
      "فك كثيرة الحدود في أساس ليجاندر واستخدم خاصية التعامد.")

    # 328: Exact ODE with y-dependent integrating factor
    q("KAUST-P2-328", "Differential Equations", "Hard",
      "Find an integrating factor \\(\\mu(y)\\) for the equation \\((y + x^2 y)dx + x dy = 0\\).",
      "أوجد عامل المكاملة \\(\\mu(y)\\) للمعادلة \\((y + x^2 y)dx + x dy = 0\\).",
      ["\\(\\mu(y) = \\frac{1}{y}\\)", "\\(\\mu(y) = y^2\\)", "\\(\\mu(y) = e^y\\)", "\\(\\mu(y) = \\frac{1}{y^2}\\)"],
      0,
      "Here \\(M = y(1 + x^2)\\) and \\(N = x\\). Compute \\(\\frac{\\partial M}{\\partial y} = 1 + x^2\\) and \\(\\frac{\\partial N}{\\partial x} = 1\\). Then \\(\\frac{1}{M}\\left(\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}\\right) = \\frac{1 - (1+x^2)}{y(1+x^2)} = \\frac{-x^2}{y(1+x^2)}\\) which depends on \\(x\\) and \\(y\\). But wait! Notice \\((1+x^2)y dx + x dy = 0 \\iff \\frac{1+x^2}{x} dx + \\frac{1}{y} dy = 0\\), which is separable directly by dividing by \\(xy\\)! Thus multiplying by \\(\\frac{1}{xy}\\) separates it, so \\(\\mu = 1/(xy)\\). But for a factor purely in \\(y\\): dividing the original equation by \\(y\\) gives \\((1+x^2)dx + \\frac{x}{y}dy = 0\\), where \\(M_y = 0\\) and \\(N_x = 1/y\\). Alternatively, let us check \\(\\mu(x) = e^{x^2/2}/x\\)... wait: the question asks for \\(\\mu(x,y)\\) or separable: if we divide by \\(y\\), we get \\(dx(1+x^2) + \\frac{x}{y}dy = 0\\). Let us verify: \\(\\mu(x, y) = e^{x^2/2}/y\\). Let's make the question completely standard: \\((2xy^4 e^y + 2xy^3 + y)dx + (x^2 y^4 e^y - x^2 y^2 - 3x)dy = 0\\) or a clean standard problem.",
      "للتأكد من عامل المكاملة بدقة: يمكن فصل المتغيرات بقسمة طرفي المعادلة على \\(xy\\).",
      "Check if dividing by \\(xy\\) separates variables.",
      "تحقق مما إذا كانت القسمة على \\(xy\\) تفصل المتغيرات.")

    # Let's replace 328 with a crisp, unambiguous integrating factor problem
    questions.pop()
    q("KAUST-P2-328", "Differential Equations", "Hard",
      "Find an integrating factor depending only on \\(y\\) for the differential equation \\(2xy dx + (y^2 - 3x^2)dy = 0\\).",
      "أوجد عامل مكاملة يعتمد فقط على \\(y\\) للمعادلة التفاضلية \\(2xy dx + (y^2 - 3x^2)dy = 0\\).",
      ["\\(\\mu(y) = \\frac{1}{y^4}\\)", "\\(\\mu(y) = y^4\\)", "\\(\\mu(y) = \\frac{1}{y^2}\\)", "\\(\\mu(y) = e^{-y}\\)"],
      0,
      "Here \\(M = 2xy\\) and \\(N = y^2 - 3x^2\\). Then \\(M_y = 2x\\) and \\(N_x = -6x\\). We compute \\(\\frac{N_x - M_y}{M} = \\frac{-6x - 2x}{2xy} = \\frac{-8x}{2xy} = -\\frac{4}{y}\\). Since this depends only on \\(y\\), the integrating factor is \\(\\mu(y) = \\exp\\left(\\int -\\frac{4}{y} dy\\right) = \\exp(-4 \\ln y) = y^{-4} = \\frac{1}{y^4}\\).",
      "هنا \\(M = 2xy\\) و \\(N = y^2 - 3x^2\\). نحسب \\(M_y = 2x\\) و \\(N_x = -6x\\). نجد أن \\(\\frac{N_x - M_y}{M} = -\\frac{4}{y}\\). بما أنه يعتمد فقط على \\(y\\)، فإن عامل المكاملة هو \\(\\mu(y) = \\exp(\\int -4/y dy) = y^{-4} = 1/y^4\\).",
      "Evaluate \\(\\frac{N_x - M_y}{M}\\) and integrate with respect to \\(y\\).",
      "احسب \\(\\frac{N_x - M_y}{M}\\) وكامل بالنسبة لـ \\(y\\).")

    # 329: Damped Harmonic Oscillator Q-factor
    q("KAUST-P2-329", "Differential Equations", "Medium",
      "An underdamped harmonic oscillator is modeled by \\(m \\ddot{x} + b \\dot{x} + k x = 0\\). In terms of mass \\(m\\), damping coefficient \\(b\\), and stiffness \\(k\\), what is the quality factor \\(Q\\)?",
      "مهتز توافقي مخمد خفيفاً يوصف بالمعادلة \\(m \\ddot{x} + b \\dot{x} + k x = 0\\). بدلالة الكتلة \\(m\\) ومعامل التخميد \\(b\\) والصلابة \\(k\\)، ما هو معامل الجودة \\(Q\\)؟",
      ["\\(Q = \\frac{\\sqrt{mk}}{b}\\)", "\\(Q = \\frac{b}{2\\sqrt{mk}}\\)", "\\(Q = \\frac{k}{mb}\\)", "\\(Q = \\frac{m\\sqrt{k}}{b^2}\\)"],
      0,
      "The quality factor is defined as \\(Q = \\frac{\\omega_0}{2\\gamma}\\), where \\(\\omega_0 = \\sqrt{k/m}\\) is the undamped natural frequency and \\(\\gamma = \\frac{b}{2m}\\) is the damping ratio parameter. Substituting gives \\(Q = \\frac{\\sqrt{k/m}}{2(b/(2m))} = \\frac{\\sqrt{k/m}}{b/m} = \\frac{m\\sqrt{k/m}}{b} = \\frac{\\sqrt{mk}}{b}\\).",
      "يعرف معامل الجودة بـ \\(Q = \\omega_0 / (2\\gamma)\\)، حيث \\(\\omega_0 = \\sqrt{k/m}\\) و \\(\\gamma = b/(2m)\\). بالتعويض المباشر: \\(Q = \\frac{\\sqrt{mk}}{b}\\).",
      "Use \\(Q = \\frac{\\omega_0}{2\\gamma}\\) where \\(\\omega_0 = \\sqrt{k/m}\\) and \\(2\\gamma = b/m\\).",
      "استخدم \\(Q = \\frac{\\omega_0}{2\\gamma}\\) حيث \\(\\omega_0 = \\sqrt{k/m}\\) و \\(2\\gamma = b/m\\).")

    # 330: Airy's Differential Equation
    q("KAUST-P2-330", "Differential Equations", "Hard",
      "The Airy differential equation \\(y'' - xy = 0\\) has power series solution \\(y(x) = \\sum_{n=0}^\\infty a_n x^n\\). If \\(a_0 = 1\\) and \\(a_1 = 0\\), what is the non-zero coefficient \\(a_6\\)?",
      "معادلة إيري التفاضلية \\(y'' - xy = 0\\) لها حل بمتسلسلة قوى \\(y(x) = \\sum_{n=0}^\\infty a_n x^n\\). إذا كان \\(a_0 = 1\\) و \\(a_1 = 0\\)، فما هو المعامل غير الصفري \\(a_6\\)؟",
      ["\\(a_6 = \\frac{1}{180}\\)", "\\(a_6 = \\frac{1}{720}\\)", "\\(a_6 = \\frac{1}{36}\\)", "\\(a_6 = \\frac{1}{60}\\)"],
      0,
      "Substitute \\(y = \\sum a_n x^n\\): \\(\\sum_{n=2}^\\infty n(n-1)a_n x^{n-2} - \\sum_{n=0}^\\infty a_n x^{n+1} = 0\\). Shifting indices yields the recurrence relation \\(a_{n+2} = \\frac{a_{n-1}}{(n+2)(n+1)}\\) for \\(n \\ge 1\\), and \\(2a_2 = 0 \\implies a_2 = 0\\). For \\(n=1\\): \\(a_3 = \\frac{a_0}{3 \\cdot 2} = \\frac{1}{6}\\). For \\(n=4\\): \\(a_6 = \\frac{a_3}{6 \\cdot 5} = \\frac{1/6}{30} = \\frac{1}{180}\\).",
      "بالتعويض بالمتسلسلة في معادلة إيري نجد علاقة التكرار: \\(a_{n+2} = \\frac{a_{n-1}}{(n+2)(n+1)}\\). بما أن \\(a_0 = 1\\) و \\(a_1 = 0\\)، نجد \\(a_3 = 1/(3 \\times 2) = 1/6\\)، ومن ثم \\(a_6 = a_3 / (6 \\times 5) = (1/6)/30 = 1/180\\).",
      "Derive the 3-step recurrence relation \\(a_{k} = \\frac{a_{k-3}}{k(k-1)}\\).",
      "استنتج علاقة التكرار الثلاثية \\(a_k = \\frac{a_{k-3}}{k(k-1)}\\).")

    # 331: System of ODEs - Coupled Tanks / Real Eigenvalues
    q("KAUST-P2-331", "Differential Equations", "Medium",
      "Two interconnected tanks have brine volumes described by \\(\\dot{x}_1 = -2x_1 + x_2\\), \\(\\dot{x}_2 = x_1 - 2x_2\\). If \\(x_1(0) = 10\\) and \\(x_2(0) = 0\\), find \\(x_1(t) + x_2(t)\\).",
      "خزانان متصلان يحتويان على محلول ملحي يوصفان بـ \\(\\dot{x}_1 = -2x_1 + x_2\\), \\(\\dot{x}_2 = x_1 - 2x_2\\). إذا كان \\(x_1(0) = 10\\) و \\(x_2(0) = 0\\)، أوجد المجموع \\(x_1(t) + x_2(t)\\).",
      ["\\(10 e^{-t}\\)", "\\(10 e^{-3t}\\)", "\\(5(e^{-t} + e^{-3t})\\)", "\\(10 e^{-2t}\\)"],
      0,
      "Add the two differential equations: \\(\\frac{d}{dt}(x_1 + x_2) = (-2x_1 + x_2) + (x_1 - 2x_2) = -(x_1 + x_2)\\). Let \\(S(t) = x_1(t) + x_2(t)\\). Then \\(\\dot{S} = -S\\), with initial condition \\(S(0) = 10 + 0 = 10\\). The solution is immediately \\(S(t) = 10 e^{-t}\\).",
      "بجمع المعادلتين التفاضليتين مباشرة: \\(\\frac{d}{dt}(x_1+x_2) = -(x_1+x_2)\\). بوضع \\(S(t) = x_1+x_2\\)، نحصل على \\(\\dot{S} = -S\\) مع الشرط الابتدائي \\(S(0) = 10\\). الحل فوراً هو \\(S(t) = 10 e^{-t}\\).",
      "Add the two equations directly to decouple the sum \\(x_1 + x_2\\).",
      "اجمع المعادلتين مباشرة لفصل مجموع المتغيرين.")

    # 332: Non-autonomous ODE - Exact Form
    q("KAUST-P2-332", "Differential Equations", "Medium",
      "Solve the differential equation \\((2x + e^y)dx + x e^y dy = 0\\) with initial condition \\(y(1) = 0\\). What is \\(y(e)\\)?",
      "حل المعادلة التفاضلية \\((2x + e^y)dx + x e^y dy = 0\\) مع الشرط الابتدائي \\(y(1) = 0\\). ما قيمة \\(y(e)\\)؟",
      ["\\(\\ln(2 - e)\\) (for \\(e < 2\\), undefined on reals)", "\\(\\ln\\left(\\frac{2 - e^2}{e}\\right)\\)", "\\(1 - e\\)", "\\(0\\)"],
      1,
      "Notice \\(M_y = e^y\\) and \\(N_x = e^y\\), so the equation is exact. Integrate: \\(\\Psi(x, y) = x^2 + x e^y = C\\). At \\(x = 1, y = 0\\): \\(C = 1^2 + 1 e^0 = 2\\). Thus the solution curve is \\(x^2 + x e^y = 2 \\implies e^y = \\frac{2 - x^2}{x} \\implies y = \\ln\\left(\\frac{2 - x^2}{x}\\right)\\). At \\(x = e\\), this gives \\(y(e) = \\ln\\left(\\frac{2 - e^2}{e}\\right)\\).",
      "بما أن \\(M_y = N_x = e^y\\)، فالمعادلة تامة. بمكاملة الدالة الكامنة نجد \\(x^2 + xe^y = C\\). من الشرط الابتدائي \\(C = 2\\). إذن \\(e^y = (2 - x^2)/x\\)، وبالتالي \\(y = \\ln((2-x^2)/x)\\).",
      "Check that \\(\\frac{\\partial M}{\\partial y} = \\frac{\\partial N}{\\partial x}\\) and find the potential function \\(\\Psi(x, y)\\).",
      "تحقق من أن المعادلة تامة وأوجد دالة الجهد.")

    # 333: Bendixson-Dulac Criterion
    q("KAUST-P2-333", "Dynamical Systems", "Hard",
      "Consider the planar system \\(\\dot{x} = 2x - y + x^3\\), \\(\\dot{y} = x + 3y + y^3\\). By Bendixson's criterion, what can be concluded about periodic orbits in \\(\\mathbb{R}^2\\)?",
      "تأمل النظام المستوي \\(\\dot{x} = 2x - y + x^3\\), \\(\\dot{y} = x + 3y + y^3\\). باستخدام معيار بندكسون، ما الاستنتاج بشأن المدارات الدورية في \\(\\mathbb{R}^2\\)؟",
      ["No periodic orbits exist in \\(\\mathbb{R}^2\\)",
       "At least two stable periodic orbits exist",
       "A unique limit cycle encircles the origin",
       "The criterion is inconclusive"],
      0,
      "Let \\(f(x, y) = 2x - y + x^3\\) and \\(g(x, y) = x + 3y + y^3\\). Compute the divergence: \\(\\nabla \\cdot (f, g) = \\frac{\\partial f}{\\partial x} + \\frac{\\partial g}{\\partial y} = (2 + 3x^2) + (3 + 3y^2) = 5 + 3(x^2 + y^2)\\). Since \\(x^2 + y^2 \\ge 0\\), we have \\(\\nabla \\cdot (f, g) \\ge 5 > 0\\) everywhere in \\(\\mathbb{R}^2\\). Because the divergence is strictly positive and never changes sign on the simply connected domain \\(\\mathbb{R}^2\\), Bendixson's Negative Criterion guarantees that no closed periodic orbits can exist.",
      "نحسب تباعد الحقل الشعاعي (divergence): \\(\\text{div} = \\partial f/\\partial x + \\partial g/\\partial y = 5 + 3(x^2 + y^2) \\ge 5 > 0\\). بما أن التباعد موجب تماماً في كامل المستوى ولا يغير إشارته، فإن معيار بندكسون يؤكد عدم وجود أي مدارات دورية مغلقة.",
      "Compute \\(\\frac{\\partial f}{\\partial x} + \\frac{\\partial g}{\\partial y}\\) and check its sign.",
      "احسب التباعد وتحقق من ثبات إشارته.")

    # 334: Lotka-Volterra Conserved Quantity
    q("KAUST-P2-334", "Dynamical Systems", "Hard",
      "For the classical Lotka-Volterra predator-prey model \\(\\dot{x} = x(\\alpha - \\beta y)\\), \\(\\dot{y} = -y(\\gamma - \\delta x)\\) with \\(\\alpha, \\beta, \\gamma, \\delta > 0\\), what is the first integral (conserved quantity \\(H(x, y)\\)) of the system?",
      "لنموذج لوتكا-فولتيرا الكلاسيكي للمفترس والفريسة \\(\\dot{x} = x(\\alpha - \\beta y)\\), \\(\\dot{y} = -y(\\gamma - \\delta x)\\) مع معالم موجبة، ما هو التكامل الأول (الكمية المحفوظة \\(H(x, y)\\)) للنظام؟",
      ["\\(H(x, y) = \\delta x - \\gamma \\ln x + \\beta y - \\alpha \\ln y\\)",
       "\\(H(x, y) = \\alpha x^2 + \\gamma y^2 - \\beta x y\\)",
       "\\(H(x, y) = \\frac{\\alpha x - \\beta y}{\\gamma y - \\delta x}\\)",
       "\\(H(x, y) = e^{\\alpha x} + e^{-\\gamma y}\\)"],
      0,
      "Divide the two equations: \\(\\frac{dy}{dx} = \\frac{-y(\\gamma - \\delta x)}{x(\\alpha - \\beta y)} = \\frac{(\\delta x - \\gamma)y}{(\\alpha - \\beta y)x}\\). Separate variables: \\(\\frac{\\alpha - \\beta y}{y} dy = \\frac{\\delta x - \\gamma}{x} dx \\implies \\left(\\frac{\\alpha}{y} - \\beta\\right)dy = \\left(\\delta - \\frac{\\gamma}{x}\\right)dx\\). Integrating both sides: \\(\\alpha \\ln y - \\beta y = \\delta x - \\gamma \\ln x + C \\implies \\delta x - \\gamma \\ln x + \\beta y - \\alpha \\ln y = \\text{const}\\).",
      "بقسمة المعادلتين نحصل على \\(dy/dx\\). بفصل المتغيرات: \\((\\alpha/y - \\beta)dy = (\\delta - \\gamma/x)dx\\). بالمكاملة نجد \\(\\delta x - \\gamma \\ln x + \\beta y - \\alpha \\ln y = C\\)، وهي الكمية المحفوظة لجميع المسارات في الربع الأول.",
      "Separate variables in the quotient \\(\\frac{dy}{dx} = \\frac{\\dot{y}}{\\dot{x}}\\).",
      "افصل المتغيرات في النسبة \\(\\frac{dy}{dx} = \\frac{\\dot{y}}{\\dot{x}}\\).")

    # 335: Matrix Stability via Routh-Hurwitz / Trace-Det
    q("KAUST-P2-335", "Dynamical Systems", "Medium",
      "For a 3D linear system \\(\\dot{\\mathbf{x}} = A\\mathbf{x}\\), the characteristic polynomial is \\(p(\\lambda) = \\lambda^3 + 2\\lambda^2 + 4\\lambda + k\\). By the Routh-Hurwitz criterion, for what range of \\(k\\) is the origin asymptotically stable?",
      "لنظام خطي ثلاثي الأبعاد \\(\\dot{\\mathbf{x}} = A\\mathbf{x}\\)، متعددة الحدود المميّزة هي \\(p(\\lambda) = \\lambda^3 + 2\\lambda^2 + 4\\lambda + k\\). حسب معيار راوث-هورفيتز، ما مدى \\(k\\) الذي يجعل نقطة الأصل مستقرة مقاربياً؟",
      ["\\(0 < k < 8\\)", "\\(k > 0\\)", "\\(-8 < k < 8\\)", "\\(k < 4\\)"],
      0,
      "For a cubic polynomial \\(\\lambda^3 + a_1 \\lambda^2 + a_2 \\lambda + a_3 = 0\\), the Routh-Hurwitz stability conditions are: \\(a_1 > 0\\), \\(a_3 > 0\\), and \\(a_1 a_2 > a_3\\). Here \\(a_1 = 2 > 0\\), \\(a_2 = 4\\), \\(a_3 = k\\). Thus we require: \\(k > 0\\) and \\((2)(4) > k \\implies 8 > k\\). Combining gives \\(0 < k < 8\\).",
      "لكثيرة حدود من الدرجة الثالثة \\(\\lambda^3 + a_1\\lambda^2 + a_2\\lambda + a_3 = 0\\)، شروط راوث-هورفيتز للاستقرار هي \\(a_1 > 0\\)، \\(a_3 > 0\\)، و \\(a_1 a_2 > a_3\\). بالتعويض: \\(k > 0\\) و \\(8 > k\\)، أي \\(0 < k < 8\\).",
      "Apply the condition \\(a_1 a_2 > a_3\\) with \\(a_3 > 0\\).",
      "طبق الشرط \\(a_1 a_2 > a_3\\) مع \\(a_3 > 0\\).")

    # 336: Inhomogeneous Euler-Cauchy ODE
    q("KAUST-P2-336", "Differential Equations", "Hard",
      "Find a particular solution \\(y_p(x)\\) to the Cauchy-Euler equation \\(x^2 y'' - 2x y' + 2y = x^3\\) for \\(x > 0\\).",
      "أوجد حلاً خاصاً \\(y_p(x)\\) لمعادلة كوشي-أويلر \\(x^2 y'' - 2x y' + 2y = x^3\\) حيث \\(x > 0\\).",
      ["\\(y_p = \\frac{1}{2} x^3\\)", "\\(y_p = x^3 \\ln x\\)", "\\(y_p = \\frac{1}{6} x^3\\)", "\\(y_p = x^2\\)"],
      0,
      "Homogeneous equation: \\(r(r-1) - 2r + 2 = r^2 - 3r + 2 = (r-1)(r-2) = 0\\), so \\(y_h = c_1 x + c_2 x^2\\). Since the forcing term is \\(x^3\\) and \\(r=3\\) is not a root of the characteristic equation, try \\(y_p = A x^3\\). Then \\(y_p' = 3Ax^2\\) and \\(y_p'' = 6Ax\\). Substitute: \\(x^2(6Ax) - 2x(3Ax^2) + 2(Ax^3) = 6Ax^3 - 6Ax^3 + 2Ax^3 = 2Ax^3\\). Setting \\(2Ax^3 = x^3 \\implies A = 1/2\\). Thus \\(y_p = \\frac{1}{2}x^3\\).",
      "المعادلة المتجانسة لها حلول \\(x\\) و \\(x^2\\). بما أن الطرف الأيمن هو \\(x^3\\) وقوته ليست جذراً للمميز، نفرض \\(y_p = Ax^3\\). بالتعويض نجد \\(2Ax^3 = x^3\\) ومنه \\(A = 1/2\\). إذن الحل الخاص هو \\(x^3 / 2\\).",
      "Try a power ansatz \\(y_p = A x^3\\) and determine \\(A\\).",
      "جرب حلاً على صورة قوة \\(y_p = Ax^3\\) وحدد المعامل \\(A\\).")

    # 337: Laplace Transform of Periodic Function
    q("KAUST-P2-337", "Differential Equations", "Medium",
      "What is the Laplace transform of the square wave function \\(f(t)\\) of period \\(2\\) defined by \\(f(t) = 1\\) for \\(0 \\le t < 1\\) and \\(f(t) = -1\\) for \\(1 \\le t < 2\\)?",
      "ما هو تحويل لابلاس لدالة الموجة المربعة \\(f(t)\\) ذات الدورة \\(2\\) والمعرفة بـ \\(f(t) = 1\\) لـ \\(0 \\le t < 1\\) و \\(f(t) = -1\\) لـ \\(1 \\le t < 2\\)؟",
      ["\\(\\frac{1}{s}\\tanh\\left(\\frac{s}{2}\\right)\\)", "\\(\\frac{1}{s}\\coth\\left(\\frac{s}{2}\\right)\\)", "\\(\\frac{1}{s(1 + e^{-s})}\\)", "\\(\\frac{1 - e^{-s}}{s(1 + e^{-2s})}\\)"],
      0,
      "The Laplace transform of a periodic function with period \\(T\\) is \\(\\mathcal{L}\\{f\\} = \\frac{1}{1 - e^{-sT}} \\int_0^T e^{-st} f(t) dt\\). For \\(T = 2\\): \\(\\int_0^2 e^{-st} f(t) dt = \\int_0^1 e^{-st} dt - \\int_1^2 e^{-st} dt = \\frac{1 - e^{-s}}{s} - \\frac{e^{-s} - e^{-2s}}{s} = \\frac{(1 - e^{-s})^2}{s}\\). Then \\(\\mathcal{L}\\{f\\} = \\frac{(1 - e^{-s})^2}{s(1 - e^{-2s})} = \\frac{(1 - e^{-s})^2}{s(1 - e^{-s})(1 + e^{-s})} = \\frac{1 - e^{-s}}{s(1 + e^{-s})} = \\frac{1}{s} \\frac{e^{s/2} - e^{-s/2}}{e^{s/2} + e^{-s/2}} = \\frac{1}{s} \\tanh(s/2)\\).",
      "تحويل لابلاس لدالة دورية دورتها \\(T=2\\) يعطى بالقانون العام. بتكامل الفترة الأولى نجد البسط \\((1-e^{-s})^2 / s\\). وبقسمته على \\(1-e^{-2s} = (1-e^{-s})(1+e^{-s})\\) نصل إلى \\(\\frac{1-e^{-s}}{s(1+e^{-s})} = \\frac{1}{s}\\tanh(s/2)\\).",
      "Use the periodic transform formula and simplify using hyperbolic tangent.",
      "استخدم قانون تحويل الدوال الدورية وبسط باستخدام دالة الظل الزائدي.")

    # 338: Hermite Polynomials and Harmonic Oscillator
    q("KAUST-P2-338", "Special Functions", "Hard",
      "The quantum harmonic oscillator stationary states satisfy \\(-\\psi'' + x^2 \\psi = E \\psi\\). The ground state is \\(\\psi_0(x) = e^{-x^2/2}\\). What is its eigenvalue (energy) \\(E_0\\)?",
      "تحقق الحالات المستقرة للمهتز التوافقي الكمي المعادلة \\(-\\psi'' + x^2 \\psi = E \\psi\\). الحالة القاعية هي \\(\\psi_0(x) = e^{-x^2/2}\\). ما هي القيمة الذاتية (الطاقة) \\(E_0\\)؟",
      ["\\(1\\)", "\\(\\frac{1}{2}\\)", "\\(0\\)", "\\(2\\)"],
      0,
      "Differentiate \\(\\psi_0(x) = e^{-x^2/2}\\): \\(\\psi_0'(x) = -x e^{-x^2/2}\\). \\(\\psi_0''(x) = -e^{-x^2/2} + x^2 e^{-x^2/2} = (x^2 - 1)\\psi_0(x)\\). Substitute into the Hamiltonian: \\(-\\psi_0'' + x^2 \\psi_0 = -(x^2 - 1)\\psi_0 + x^2 \\psi_0 = \\psi_0(x)\\). Therefore \\(E_0 = 1\\) (in units where \\(\\hbar \\omega = 1\\)).",
      "بتفاضل الدالة القاعية مرتين نجد \\(\\psi_0'' = (x^2-1)\\psi_0\\). بالتعويض في معادلة شرودنجر نجد: \\(-\\psi_0'' + x^2 \\psi_0 = -(x^2-1)\\psi_0 + x^2 \\psi_0 = 1 \\cdot \\psi_0\\). إذن طاقة الحالة القاعية هي \\(E_0 = 1\\).",
      "Compute \\(\\psi_0''(x)\\) using the product rule and substitute directly.",
      "احسب المشتقة الثانية \\(\\psi_0''(x)\\) وعوض مباشرة.")

    # 339: Boundary Layer & Singular Perturbation
    q("KAUST-P2-339", "Differential Equations", "Hard",
      "Consider the singular perturbation problem \\(\\epsilon y'' + y' + y = 0\\) on \\(0 < x < 1\\) with \\(y(0) = 0\\), \\(y(1) = 1\\), and \\(0 < \\epsilon \\ll 1\\). Where does the boundary layer form, and what is the outer solution \\(y_{\\text{out}}(x)\\)?",
      "تأمل مسألة الاضطراب الشاذ \\(\\epsilon y'' + y' + y = 0\\) على \\(0 < x < 1\\) مع \\(y(0) = 0\\), \\(y(1) = 1\\) حيث \\(0 < \\epsilon \\ll 1\\). أين تتشكل الطبقة الحدية (boundary layer)، وما هو الحل الخارجي؟",
      ["Boundary layer at \\(x = 0\\); \\(y_{\\text{out}}(x) = e^{1 - x}\\)",
       "Boundary layer at \\(x = 1\\); \\(y_{\\text{out}}(x) = e^{-x}\\)",
       "Boundary layer at \\(x = 1/2\\); \\(y_{\\text{out}}(x) = x\\)",
       "No boundary layer; regular perturbation applies"],
      0,
      "The roots of \\(\\epsilon r^2 + r + 1 = 0\\) are \\(r \\approx -1/\\epsilon\\) and \\(r \\approx -1\\). The rapid decay term \\(e^{-x/\\epsilon}\\) acts near \\(x = 0\\), so the boundary layer is at \\(x = 0\\). The outer solution satisfies the reduced equation \\(y_{\\text{out}}' + y_{\\text{out}} = 0 \\implies y_{\\text{out}}(x) = C e^{-x}\\). Applying the right boundary condition \\(y_{\\text{out}}(1) = 1\\) gives \\(C e^{-1} = 1 \\implies C = e\\), so \\(y_{\\text{out}}(x) = e^{1 - x}\\).",
      "بما أن معامل المشتقة الأولى موجب، فإن التخميد السريع يحدث بالقرب من \\(x = 0\\) حيث تتشكل الطبقة الحدية. الحل الخارجي يحقق المعادلة المختزلة \\(y' + y = 0\\) مع الشرط عند \\(x = 1\\)، وهو \\(y(1) = 1\\)، فينتج \\(y_{\\text{out}}(x) = e^{1-x}\\).",
      "The boundary layer occurs at \\(x = 0\\) because the coefficient of \\(y'\\) is positive.",
      "تتشكل الطبقة الحدية عند \\(x = 0\\) لأن معامل المشتقة الأولى موجب.")

    # 340: Non-linear Conservative System - Energy Method
    q("KAUST-P2-340", "Dynamical Systems", "Medium",
      "A particle moves in potential \\(V(x) = \\frac{x^4}{4} - \\frac{x^2}{2}\\) according to \\(\\ddot{x} = -V'(x)\\). What are the stable equilibrium points of this system?",
      "يتحرك جسيم في مجال جهد \\(V(x) = \\frac{x^4}{4} - \\frac{x^2}{2}\\) وفقاً لـ \\(\\ddot{x} = -V'(x)\\). ما هي نقاط الاتزان المستقرة لهذا النظام؟",
      ["\\(x = 1\\) and \\(x = -1\\)", "\\(x = 0\\) only", "\\(x = 0, 1, -1\\)", "\\(x = \\pm \\frac{1}{\\sqrt{2}}\\)"],
      0,
      "Equilibria occur at critical points of \\(V(x)\\): \\(V'(x) = x^3 - x = x(x-1)(x+1) = 0 \\implies x = 0, 1, -1\\). The stability in conservative systems is determined by the second derivative \\(V''(x) = 3x^2 - 1\\). At \\(x = 0\\): \\(V''(0) = -1 < 0\\) (local maximum of potential, hence an unstable saddle). At \\(x = \\pm 1\\): \\(V''(\\pm 1) = 3(1) - 1 = 2 > 0\\) (local minima of potential, hence stable centers).",
      "نقاط الاتزان تقع عند النقاط الحرجة للجهد: \\(V'(x) = x^3 - x = 0\\) أي \\(x = 0, \\pm 1\\). الاستقرار يحدده المشتق الثاني: عند \\(x = 0\\) نجد \\(V'' < 0\\) (نهاية عظمى للجهد، غير مستقرة). عند \\(x = \\pm 1\\) نجد \\(V'' > 0\\) (نهايات صغرى للجهد، مراكز مستقرة).",
      "Stable equilibria in conservative mechanics correspond to local minima of the potential \\(V(x)\\).",
      "تتوافق نقاط الاتزان المستقرة مع النهايات الصغرى المحلية لدالة الجهد.")

    # 341: Homogeneous First Order ODE
    q("KAUST-P2-341", "Differential Equations", "Medium",
      "Solve the homogeneous differential equation \\(x y' = y + \\sqrt{x^2 + y^2}\\) for \\(x > 0\\) with \\(y(1) = 0\\). What is \\(y(e)\\)?",
      "حل المعادلة التفاضلية المتجانسة \\(x y' = y + \\sqrt{x^2 + y^2}\\) حيث \\(x > 0\\) مع الشرط \\(y(1) = 0\\). ما قيمة \\(y(e)\\)؟",
      ["\\(\\frac{e^2 - 1}{2}\\)", "\\(e\\)", "\\(\\frac{e^2 + 1}{2}\\)", "\\(e \\ln 2\\)"],
      0,
      "Divide by \\(x\\): \\(y' = \\frac{y}{x} + \\sqrt{1 + (y/x)^2}\\). Substitute \\(v = y/x\\), so \\(y' = v + x v'\\). The equation becomes \\(v + x v' = v + \\sqrt{1 + v^2} \\implies x \\frac{dv}{dx} = \\sqrt{1 + v^2}\\). Separating variables: \\(\\frac{dv}{\\sqrt{1+v^2}} = \\frac{dx}{x} \\implies \\text{arsinh}(v) = \\ln x + C\\). Since \\(y(1) = 0\\), \\(v(1) = 0 \\implies C = \\text{arsinh}(0) = 0\\). Thus \\(v = \\sinh(\\ln x) = \\frac{x - x^{-1}}{2}\\). Therefore \\(y(x) = x v = \\frac{x^2 - 1}{2}\\). At \\(x = e\\), \\(y(e) = \\frac{e^2 - 1}{2}\\).",
      "بقسمة المعادلة على \\(x\\) واستخدام التعويض المتجانس \\(v = y/x\\) نصل إلى \\(dv/\\sqrt{1+v^2} = dx/x\\). بالمكاملة \\(\\text{arsinh}(v) = \\ln x + C\\). من الشرط الابتدائي \\(C = 0\\). بالتالي \\(y(x) = \\frac{x^2 - 1}{2}\\)، وعند \\(x=e\\) نجد \\(y(e) = (e^2-1)/2\\).",
      "Use the substitution \\(v = y/x\\) and integrate using inverse hyperbolic sine.",
      "استخدم التعويض \\(v = y/x\\) وكامل باستخدام الدالة العكسية لـ \\(\\sinh\\).")

    # 342: Differential Form - Integrating Factor Theorem
    q("KAUST-P2-342", "Differential Equations", "Hard",
      "For what value of constant \\(k\\) is the differential form \\(\\omega = (x^2 + y^2 + k x)dx + 2xy dy\\) made exact by an integrating factor \\(\\mu(x) = x\\)?",
      "لأي قيمة للثابت \\(k\\) يكون الشكل التفاضلي \\(\\omega = (x^2 + y^2 + k x)dx + 2xy dy\\) تاماً باستخدام عامل مكاملة \\(\\mu(x) = x\\)؟",
      ["\\(k = 0\\)", "\\(k = 1\\)", "\\(k = -1\\)", "\\(k = 2\\)"],
      0,
      "Multiply by \\(\\mu(x) = x\\): \\(\\tilde{\\omega} = (x^3 + xy^2 + kx^2)dx + 2x^2 y dy\\). Now check exactness: \\(\\frac{\\partial \\tilde{M}}{\\partial y} = 2xy\\). And \\(\\frac{\\partial \\tilde{N}}{\\partial x} = \\frac{\\partial}{\\partial x}(2x^2 y) = 4xy\\). Wait! \\(2xy = 4xy\\) would imply \\(xy = 0\\), which is not true! Let's check general condition: \\(\\frac{M_y - N_x}{N} = \\frac{2y - 2y}{2xy} = 0\\) wait, for \\(\\omega = (x^2 + y^2 + kx)dx + 2xy dy\\), \\(M_y = 2y\\) and \\(N_x = 2y\\)! The original form is ALREADY exact for ANY \\(k\\)! Let's fix the question: \\(\\omega = (3x^2 y + y^3)dx + (x^3 + 3xy^2)dy\\) is exact, or \\(\\omega = (y + k x y^2)dx + x dy\\). Let's write an unmistakable question.",
      "للتأكد: نحسب الشرط الدقيق لعامل المكاملة بحيث تتساوى المشتقات الجزئية المتقاطعة.",
      "Compute \\(\\partial(\\mu M)/\\partial y = \\partial(\\mu N)/\\partial x\\).",
      "احسب \\(\\partial(\\mu M)/\\partial y = \\partial(\\mu N)/\\partial x\\).")

    # Let's cleanly replace 342
    questions.pop()
    q("KAUST-P2-342", "Differential Equations", "Hard",
      "The equation \\((y + x^3)dx + k x dy = 0\\) has an integrating factor that is a function of \\(x\\) alone if and only if \\(k\\) equals what value?",
      "المعادلة \\((y + x^3)dx + k x dy = 0\\) تمتلك عامل مكاملة يعتمد على \\(x\\) فقط إذا وفقط إذا كانت \\(k\\) تساوي أي قيمة؟",
      ["Any non-zero constant \\(k\\)", "\\(k = 1\\) only", "\\(k = -1\\) only", "\\(k = 3\\) only"],
      0,
      "Here \\(M = y + x^3\\) and \\(N = kx\\). Compute \\(M_y = 1\\) and \\(N_x = k\\). For an integrating factor depending only on \\(x\\), the ratio \\(\\frac{M_y - N_x}{N}\\) must be a function of \\(x\\) alone: \\(\\frac{M_y - N_x}{N} = \\frac{1 - k}{kx} = \\frac{1 - k}{k} \\frac{1}{x}\\). Since \\(\\frac{1-k}{k}\\) is a constant, this expression depends solely on \\(x\\) for ANY non-zero constant \\(k\\) (yielding \\(\\mu(x) = x^{(1-k)/k}\\)).",
      "هنا \\(M = y + x^3\\) و \\(N = kx\\). المشتقات هي \\(M_y = 1\\) و \\(N_x = k\\). النسبة \\(\\frac{M_y - N_x}{N} = \\frac{1-k}{kx}\\) تعتمد فقط على \\(x\\) لأي ثابت \\(k \\neq 0\\)، مما يعطي عامل مكاملة \\(\\mu(x) = x^{(1-k)/k}\\).",
      "Check whether \\(\\frac{M_y - N_x}{N}\\) depends on \\(y\\).",
      "تحقق مما إذا كان المقدار يعتمد على \\(y\\).")

    # 343: Linear Fractional / Invariant Transformation
    q("KAUST-P2-343", "Differential Equations", "Medium",
      "Transform the non-homogeneous linear system of coordinates \\(\\frac{dy}{dx} = \\frac{x - y + 1}{x + y - 3}\\) to a homogeneous equation \\(\\frac{dY}{dX} = \\frac{X - Y}{X + Y}\\) by setting \\(x = X + h\\) and \\(y = Y + k\\). What is the translation point \\((h, k)\\)?",
      "حول المعادلة \\(\\frac{dy}{dx} = \\frac{x - y + 1}{x + y - 3}\\) إلى معادلة متجانسة \\(\\frac{dY}{dX} = \\frac{X - Y}{X + Y}\\) بإجراء الإزاحة \\(x = X + h\\) و \\(y = Y + k\\). ما هي نقطة الإزاحة \\((h, k)\\)؟",
      ["\\((1, 2)\\)", "\\((2, 1)\\)", "\\((1, -2)\\)", "\\((-1, 2)\\)"],
      0,
      "The translation constants \\((h, k)\\) must satisfy the intersection of the two lines: \\(h - k + 1 = 0\\) and \\(h + k - 3 = 0\\). Adding the two equations: \\(2h - 2 = 0 \\implies h = 1\\). Substituting \\(h = 1\\) into the second equation: \\(1 + k - 3 = 0 \\implies k = 2\\). Thus the shift point is \\((h, k) = (1, 2)\\).",
      "ثوابت الإزاحة \\((h, k)\\) تمثل نقطة تقاطع المستقيمين: \\(h - k + 1 = 0\\) و \\(h + k - 3 = 0\\). بجمع المعادلتين نجد \\(2h = 2 \\implies h = 1\\)، وبالتعويض نجد \\(k = 2\\). إذن النقطة هي \\((1, 2)\\).",
      "Find the intersection point of the numerator and denominator lines.",
      "أوجد نقطة تقاطع مستقيمي البسط والمقام.")

    # 344: Floquet Theory - Hill's Equation Intro
    q("KAUST-P2-344", "Differential Equations", "Hard",
      "In Floquet theory for periodic linear systems \\(\\dot{\\mathbf{x}} = A(t)\\mathbf{x}\\) with period \\(T\\), if the monodromy matrix \\(M\\) has eigenvalues (Floquet multipliers) \\(\\mu_1 = 0.5\\) and \\(\\mu_2 = 0.8\\), what is the stability of the zero solution?",
      "في نظرية فلوكي للأنظمة الخطية الدورية \\(\\dot{\\mathbf{x}} = A(t)\\mathbf{x}\\) ذات الدورة \\(T\\)، إذا كانت القيم الذاتية لمصفوفة أحادية الدورة (مضاعفات فلوكي) هي \\(\\mu_1 = 0.5\\) و \\(\\mu_2 = 0.8\\)، فما هو استقرار الحل الصفري؟",
      ["Asymptotically stable", "Unstable", "Neutrally stable", "Linearly stable but nonlinearly unstable"],
      0,
      "By Floquet's theorem, solutions satisfy \\(\\mathbf{x}(t + T) = M \\mathbf{x}(t)\\). The asymptotic stability of the origin is governed by the magnitudes of the Floquet multipliers \\(\\mu_i\\). If all multipliers satisfy \\(|\\mu_i| < 1\\), then every solution decays exponentially to zero as \\(t \\to \\infty\\). Here, \\(|\\mu_1| = 0.5 < 1\\) and \\(|\\mu_2| = 0.8 < 1\\), so the zero solution is asymptotically stable.",
      "حسب نظرية فلوكي، تتحدد صفة الاستقرار بمقادير مضاعفات فلوكي \\(|\\mu_i|\\). إذا كانت جميع المضاعفات داخل دائرة الوحدة (أي \\(|\\mu_i| < 1\\))، فإن الحلول تضمحل أسياً نحو الصفر، وبالتالي يكون الحل الصفري مستقراً مقاربياً.",
      "Check whether all Floquet multipliers lie strictly inside the unit circle \\(|\\mu| < 1\\).",
      "تحقق مما إذا كانت جميع مضاعفات فلوكي تقع داخل دائرة الوحدة تماماً.")

    # 345: Logistic Equation with Harvesting
    q("KAUST-P2-345", "Dynamical Systems", "Medium",
      "Consider the population model with constant harvesting \\(\\dot{N} = N(1 - N) - h\\), where \\(h > 0\\). At what critical harvesting rate \\(h_c\\) does a saddle-node bifurcation occur?",
      "تأمل نموذج نمو عشيرة مع صيد بمعدل ثابت \\(\\dot{N} = N(1 - N) - h\\) حيث \\(h > 0\\). عند أي معدل صيد حرج \\(h_c\\) يحدث تفرع العقدة السرجية (saddle-node bifurcation)؟",
      ["\\(h_c = \\frac{1}{4}\\)", "\\(h_c = \\frac{1}{2}\\)", "\\(h_c = 1\\)", "\\(h_c = \\frac{1}{8}\\)"],
      0,
      "Equilibrium points satisfy \\(-N^2 + N - h = 0\\). The discriminant of this quadratic is \\(\\Delta = 1 - 4h\\). For \\(h < 1/4\\), there are two distinct equilibria (one stable, one unstable). At \\(h = 1/4\\), \\(\\Delta = 0\\), and the two equilibria collide at \\(N = 1/2\\). For \\(h > 1/4\\), \\(\\Delta < 0\\) and no real equilibria exist, leading to inevitable population extinction. Thus the saddle-node bifurcation occurs at \\(h_c = 1/4\\).",
      "نقاط الاتزان تحقق \\(N^2 - N + h = 0\\). المميز هو \\(\\Delta = 1 - 4h\\). عندما \\(h < 1/4\\) توجد نقطتا اتزان، وعند \\(h = 1/4\\) تلتقي النقطتان في نقطة شبه مستقرة، وعند \\(h > 1/4\\) لا توجد أي نقطة اتزان ويفنى المحصول. بالتالي يحدث تفرع العقدة السرجية عند \\(h_c = 1/4\\).",
      "Find the condition where the discriminant of the quadratic right-hand side is zero.",
      "أوجد شرط انعدام مميز كثيرة الحدود التربيعية في الطرف الأيمن.")

    # 346: Abel's Differential Equation
    q("KAUST-P2-346", "Differential Equations", "Hard",
      "Classify the first-order differential equation \\(y' = f_3(x)y^3 + f_2(x)y^2 + f_1(x)y + f_0(x)\\).",
      "صنف المعادلة التفاضلية من الرتبة الأولى \\(y' = f_3(x)y^3 + f_2(x)y^2 + f_1(x)y + f_0(x)\\).",
      ["Abel differential equation of the first kind",
       "Riccati differential equation",
       "Bernoulli differential equation",
       "Clairaut differential equation"],
      0,
      "An ODE of the form \\(y' = f_3(x)y^3 + f_2(x)y^2 + f_1(x)y + f_0(x)\\) with cubic nonlinearity in \\(y\\) is historically defined as an Abel differential equation of the first kind. If \\(f_3(x) = 0\\), it reduces to a Riccati equation.",
      "المعادلة التفاضلية من الصورة \\(y' = f_3 y^3 + f_2 y^2 + f_1 y + f_0\\) ذات اللاخطية التكعيبية في \\(y\\) تسمى تاريخياً معادلة آبل التفاضلية من النوع الأول. وفي حال كان \\(f_3 = 0\\) فإنها تختزل إلى معادلة ريكاتي.",
      "Recognize the cubic polynomial in \\(y\\) on the right-hand side.",
      "لاحظ وجود كثيرة حدود تكعيبية في \\(y\\) في الطرف الأيمن.")

    # 347: Exact Differential with Trigonometric Functions
    q("KAUST-P2-347", "Differential Equations", "Medium",
      "Solve \\((\\cos y + y \\cos x)dx + (\\sin x - x \\sin y)dy = 0\\) with \\(y(0) = \\pi/2\\).",
      "حل المعادلة \\((\\cos y + y \\cos x)dx + (\\sin x - x \\sin y)dy = 0\\) مع الشرط \\(y(0) = \\pi/2\\).",
      ["\\(x \\cos y + y \\sin x = 0\\)", "\\(x \\sin y + y \\cos x = \\pi/2\\)", "\\(\\cos(xy) = 1\\)", "\\(x \\cos y - y \\sin x = 0\\)"],
      0,
      "Let \\(M = \\cos y + y \\cos x\\) and \\(N = \\sin x - x \\sin y\\). Then \\(M_y = -\\sin y + \\cos x\\) and \\(N_x = \\cos x - \\sin y\\). Since \\(M_y = N_x\\), the equation is exact. Integrate \\(M\\) with respect to \\(x\\): \\(\\Psi(x, y) = x \\cos y + y \\sin x + g(y)\\). Differentiating with respect to \\(y\\): \\(\\Psi_y = -x \\sin y + \\sin x + g'(y) = N \\implies g'(y) = 0\\). Thus \\(x \\cos y + y \\sin x = C\\). At \\(x = 0, y = \\pi/2\\): \\(0 \\cos(\\pi/2) + (\\pi/2) \\sin(0) = 0 = C\\). Hence \\(x \\cos y + y \\sin x = 0\\).",
      "بما أن \\(M_y = N_x\\)، فالمعادلة تامة. بمكاملة \\(M\\) بالنسبة لـ \\(x\\) نجد دالة الجهد \\(\\Psi = x \\cos y + y \\sin x = C\\). بتطبيق الشرط الابتدائي نجد \\(C = 0\\). إذن الحل هو \\(x \\cos y + y \\sin x = 0\\).",
      "Check exactness and integrate \\(M\\) with respect to \\(x\\).",
      "تحقق من تمام المعادلة وكامل \\(M\\) بالنسبة لـ \\(x\\).")

    # 348: Linear System - Center vs Focus via Trace
    q("KAUST-P2-348", "Dynamical Systems", "Medium",
      "The linear planar system \\(\\dot{\\mathbf{x}} = \\begin{pmatrix} \\alpha & -5 \\\\ 2 & -1 \\end{pmatrix} \\mathbf{x}\\) has a center at the origin if and only if \\(\\alpha\\) equals what value?",
      "النظام الخطي المستوي \\(\\dot{\\mathbf{x}} = \\begin{pmatrix} \\alpha & -5 \\\\ 2 & -1 \\end{pmatrix} \\mathbf{x}\\) يمتلك مركزاً (center) عند نقطة الأصل إذا وفقط إذا كانت \\(\\alpha\\) تساوي أي قيمة؟",
      ["\\(\\alpha = 1\\)", "\\(\\alpha = -1\\)", "\\(\\alpha = 0\\)", "\\(\\alpha = 10\\)"],
      0,
      "A linear system has a center if and only if its eigenvalues are purely imaginary, which requires \\(\\text{tr}(A) = 0\\) and \\(\\det(A) > 0\\). The trace is \\(\\text{tr}(A) = \\alpha - 1\\). Setting \\(\\text{tr}(A) = 0 \\implies \\alpha = 1\\). At \\(\\alpha = 1\\), \\(\\det(A) = (1)(-1) - (-5)(2) = -1 + 10 = 9 > 0\\). Thus \\(\\alpha = 1\\) yields purely imaginary eigenvalues \\(\\lambda = \\pm 3i\\), which is a center.",
      "يكون للنظام الخطي مركز إذا وفقط إذا كانت القيم الذاتية تخيلية بحتة، وهو ما يتطلب أن يكون أثر المصفوفة صفراً ومحددها موجباً. الأثر هو \\(\\alpha - 1 = 0 \\implies \\alpha = 1\\). عند \\(\\alpha = 1\\) نجد المحدد \\(\\det = 9 > 0\\)، وتكون القيم الذاتية \\(\\pm 3i\\).",
      "A center requires zero trace and strictly positive determinant.",
      "يتطلب وجود المركز انعدام الأثر وأن يكون المحدد موجباً تماماً.")

    # 349: Damped Forced Oscillator Steady State
    q("KAUST-P2-349", "Differential Equations", "Medium",
      "Find the steady-state amplitude \\(X\\) of the driven oscillator \\(\\ddot{x} + 2\\dot{x} + 5x = 10\\cos(t)\\).",
      "أوجد سعة الحالة المستقرة \\(X\\) للمهتز القسري \\(\\ddot{x} + 2\\dot{x} + 5x = 10\\cos(t)\\).",
      ["\\(\\sqrt{5}\\)", "\\(2\\)", "\\(\\frac{5}{2}\\)", "\\(2\\sqrt{5}\\)"],
      0,
      "Represent the forcing as \\(10 e^{it}\\). Look for steady-state solution \\(x_p(t) = X_c e^{it}\\). Then \\(\\ddot{x}_p + 2\\dot{x}_p + 5x_p = (-1 + 2i + 5)X_c e^{it} = (4 + 2i)X_c e^{it}\\). Equating this to \\(10 e^{it}\\) gives complex amplitude \\(X_c = \\frac{10}{4 + 2i} = \\frac{10(4 - 2i)}{16 + 4} = \\frac{40 - 20i}{20} = 2 - i\\). The real physical amplitude is \\(X = |X_c| = |2 - i| = \\sqrt{2^2 + (-1)^2} = \\sqrt{5}\\).",
      "نستخدم التمثيل العقدي للقوة الخارجية \\(10 e^{it}\\). نفرض \\(x_p = X_c e^{it}\\). بالتعويض نجد \\((4 + 2i)X_c = 10\\)، ومنه \\(X_c = 10/(4+2i) = 2 - i\\). السعة الحقيقية هي القيمة المطلقة: \\(|X_c| = \\sqrt{2^2 + (-1)^2} = \\sqrt{5}\\).",
      "Use complex amplitudes: replace \\(\\cos(t)\\) by \\(e^{it}\\) and compute the modulus of \\(X_c\\).",
      "استخدم السعة العقدية واحسب مقياس العدد العقدي الناتج.")

    # 350: Wronskian of 3 Functions
    q("KAUST-P2-350", "Differential Equations", "Medium",
      "Compute the Wronskian \\(W(1, x, x^2)\\) at \\(x = 5\\).",
      "احسب قيمة الرونسكيان \\(W(1, x, x^2)\\) عند \\(x = 5\\).",
      ["\\(2\\)", "\\(0\\)", "\\(10\\)", "\\(25\\)"],
      0,
      "The Wronskian of \\(\\{1, x, x^2\\}\\) is given by the determinant \\(W(x) = \\det\\begin{pmatrix} 1 & x & x^2 \\\\ 0 & 1 & 2x \\\\ 0 & 0 & 2 \\end{pmatrix}\\). This is an upper triangular matrix! Its determinant is simply the product of the diagonal entries: \\(W(x) = (1)(1)(2) = 2\\). This holds for all \\(x\\), including \\(x = 5\\).",
      "الرونسكيان هو محدد المصفوفة التي صفوفها الدوال ومشتقاتها المتعاقبة: المصفوفة الناتجة مثلثية عليا قطرها \\((1, 1, 2)\\)، لذا محددها هو حاصل ضرب عناصر القطر ويساوي \\(2\\) لجميع قيم \\(x\\).",
      "Notice the matrix is upper triangular and compute the product of its diagonal elements.",
      "لاحظ أن المصفوفة مثلثية عليا واضرب عناصر القطر الرئيسي.")

    return questions

if __name__ == "__main__":
    qs = get_p2_part_b()
    print(f"Loaded {len(qs)} questions for Phase 2 Part B.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=301):
        expected_id = f"KAUST-P2-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 2 Part B questions successfully verified!")
