#!/usr/bin/env python3
"""
KAUST Phase 3 Questions Part C: 351 to 400
Elite Research: Stochastic Processes, Markov Chains & Measure-Theoretic Probability:
Discrete and continuous-time Markov chains, Stationary distributions,
Absorbing chains, Poisson processes, Renewal theory, Martingales,
Optional Stopping Theorem, Brownian motion, Itô's Lemma, SDEs, Fokker-Planck.
Authentic lineages: MIT 18.445 / 6.262, Stanford STATS 217, Cambridge Tripos Part II, Harvard Stat 210.
"""

def get_p3_part_c():
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

    # 351: 2-State Markov Chain Stationary Distribution with SVG
    svg_markov2 = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='-20 -20 180 80' width='100%' height='100%' style='background:#0d1117;'>
  <!-- State 0 -->
  <circle cx='25' cy='20' r='18' fill='#161b22' stroke='#58a6ff' stroke-width='2'/>
  <text x='20' y='25' fill='#58a6ff' font-size='12' font-family='sans-serif' font-weight='bold'>0</text>
  <!-- State 1 -->
  <circle cx='115' cy='20' r='18' fill='#161b22' stroke='#f0883e' stroke-width='2'/>
  <text x='110' y='25' fill='#f0883e' font-size='12' font-family='sans-serif' font-weight='bold'>1</text>
  <!-- Arrow 0 -> 1 -->
  <path d='M 38,10 Q 70,-8 102,10' fill='none' stroke='#8b949e' stroke-width='1.5'/>
  <polygon points='98,10 106,12 101,6' fill='#8b949e'/>
  <text x='65' y='-2' fill='#8b949e' font-size='10' font-family='sans-serif'>α = 0.2</text>
  <!-- Arrow 1 -> 0 -->
  <path d='M 102,30 Q 70,48 38,30' fill='none' stroke='#8b949e' stroke-width='1.5'/>
  <polygon points='42,30 34,28 39,34' fill='#8b949e'/>
  <text x='65' y='48' fill='#8b949e' font-size='10' font-family='sans-serif'>β = 0.3</text>
</svg>"""
    q("KAUST-P3-351", "Markov Chains", "Medium",
      "A two-state Markov chain has transition matrix \\(P = \\begin{pmatrix} 0.8 & 0.2 \\\\ 0.3 & 0.7 \\end{pmatrix}\\). What is the stationary distribution \\(\\boldsymbol{\\pi} = (\\pi_0, \\pi_1)\\)?",
      "سلسلة ماركوف ذات حالتين لها مصفوفة انتقال \\(P = \\begin{pmatrix} 0.8 & 0.2 \\\\ 0.3 & 0.7 \\end{pmatrix}\\). ما هو التوزيع المستقر \\(\\boldsymbol{\\pi} = (\\pi_0, \\pi_1)\\)؟",
      ["\\(\\boldsymbol{\\pi} = (0.6, 0.4)\\)", "\\(\\boldsymbol{\\pi} = (0.5, 0.5)\\)", "\\(\\boldsymbol{\\pi} = (0.4, 0.6)\\)", "\\(\\boldsymbol{\\pi} = (0.7, 0.3)\\)"],
      0,
      "The stationary distribution satisfies \\(\\boldsymbol{\\pi} P = \\boldsymbol{\\pi}\\) and \\(\\pi_0 + \\pi_1 = 1\\). In general for a 2-state chain with transition probabilities \\(0 \\to 1\\) as \\(\\alpha = 0.2\\) and \\(1 \\to 0\\) as \\(\\beta = 0.3\\), detailed balance gives \\(\\pi_0 \\alpha = \\pi_1 \\beta \\implies 0.2 \\pi_0 = 0.3 \\pi_1 \\implies \\pi_1 = \\frac{2}{3} \\pi_0\\). Using \\(\\pi_0 + \\pi_1 = 1\\): \\(\\pi_0 + \\frac{2}{3}\\pi_0 = \\frac{5}{3}\\pi_0 = 1 \\implies \\pi_0 = \\frac{3}{5} = 0.6\\), and \\(\\pi_1 = 0.4\\). Thus \\(\\boldsymbol{\\pi} = (0.6, 0.4)\\).",
      "يحقق التوزيع المستقر معادلة التوازن التفصيلي: \\(\\pi_0 \\alpha = \\pi_1 \\beta\\)، أي \\(0.2 \\pi_0 = 0.3 \\pi_1\\)، ومنه \\(\\pi_1 = \\frac{2}{3} \\pi_0\\). وبما أن \\(\\pi_0 + \\pi_1 = 1\\)، نجد \\(\\frac{5}{3}\\pi_0 = 1 \\implies \\pi_0 = 0.6\\) و \\(\\pi_1 = 0.4\\).",
      "Use detailed balance \\(\\pi_0 P_{01} = \\pi_1 P_{10}\\).",
      "استخدم معادلة التوازن التفصيلي بين الحالتين.",
      diagram=svg_markov2)

    # 352: Itô's Lemma on Standard Function
    q("KAUST-P3-352", "Stochastic Calculus", "Hard",
      "Let \\(W_t\\) be a standard 1D Brownian motion. Using Itô's formula, what is the stochastic differential \\(d(W_t^3)\\)?",
      "ليكن \\(W_t\\) حركة براونية قياسية أحادية البعد. باستخدام صيغة إيتو، ما هو التفاضل العشوائي \\(d(W_t^3)\\)؟",
      ["\\(d(W_t^3) = 3 W_t^2 dW_t + 3 W_t dt\\)",
       "\\(d(W_t^3) = 3 W_t^2 dW_t\\)",
       "\\(d(W_t^3) = 3 W_t^2 dW_t + \\frac{3}{2} W_t dt\\)",
       "\\(d(W_t^3) = 3 W_t^2 dW_t + 6 W_t dt\\)"],
      0,
      "Itô's formula for \\(f(W_t)\\) is \\(df(W_t) = f'(W_t) dW_t + \\frac{1}{2} f''(W_t) dt\\). For \\(f(x) = x^3\\): \\(f'(x) = 3x^2\\) and \\(f''(x) = 6x\\). Substituting these derivatives: \\(d(W_t^3) = 3W_t^2 dW_t + \\frac{1}{2}(6W_t) dt = 3W_t^2 dW_t + 3W_t dt\\). The extra \\(3W_t dt\\) term is the Itô correction arising from the non-zero quadratic variation \\((dW_t)^2 = dt\\).",
      "تنص صيغة إيتو للدالة \\(f(x) = x^3\\) على \\(df = f'(W_t) dW_t + \\frac{1}{2}f''(W_t) dt\\). المشتق الأول هو \\(3x^2\\) والمشتق الثاني هو \\(6x\\). بالتعويض: \\(d(W_t^3) = 3W_t^2 dW_t + \\frac{1}{2}(6W_t)dt = 3W_t^2 dW_t + 3W_t dt\\).",
      "Remember the second-order Taylor term with \\((dW_t)^2 = dt\\).",
      "تذكر حد تايلور من الدرجة الثانية واستبدال \\((dW_t)^2\\) بـ \\(dt\\).")

    # 353: Optional Stopping Theorem - Gambler's Ruin
    q("KAUST-P3-353", "Martingales", "Hard",
      "A gambler starts with \\$k\\) and plays a fair game (win \\$1\\) with probability \\(1/2\\), lose \\$1\\) with probability \\(1/2\\)). The game stops when the gambler reaches \\$N\\) or \\$0\\). Using the Optional Stopping Theorem on the martingale \\(M_n = X_n\\), what is the probability of reaching \\$N\\) before going broke?",
      "يبدأ مقامر برصيد \\$k\\) ويلعب لعبة عادلة (يربح \\$1\\) باحتمال \\(1/2\\) أو يخسر \\$1\\) باحتمال \\(1/2\\)). تتوقف اللعبة عند بلوغ \\$N\\) أو الإفلاس عند 0. باستخدام نظرية الإيقاف الاختياري، ما هو احتمال الوصول إلى \\$N\\) قبل الإفلاس؟",
      ["\\(\\frac{k}{N}\\)", "\\(\\frac{k}{N-k}\\)", "\\(\\frac{1}{2}\\)", "\\(\\left(\\frac{1}{2}\\right)^{N-k}\\)"],
      0,
      "The fortune \\(X_n\\) is a martingale since the game is fair: \\(\\mathbb{E}[X_{n+1} \\mid X_n] = X_n\\). The stopping time \\(T = \\min\\{n : X_n = 0 \\text{ or } X_n = N\\}\\) is almost surely finite and \\(X_{n \\wedge T}\\) is bounded in \\([0, N]\\). By the Optional Stopping Theorem: \\(\\mathbb{E}[X_T] = X_0 = k\\). But \\(X_T\\) can only take values \\(N\\) (with probability \\(p\\)) or \\(0\\) (with probability \\(1-p\\)). Thus \\(\\mathbb{E}[X_T] = p N + (1-p) 0 = p N\\). Equating gives \\(p N = k \\implies p = \\frac{k}{N}\\).",
      "رصيد المقامر يشكل مارتينغال لأن اللعبة عادلة: \\(\\mathbb{E}[X_n] = k\\). عند زمن التوقف \\(T\\)، لا يأخذ الرصيد سوى القيمة \\(N\\) باحتمال \\(p\\) أو 0 باحتمال \\(1-p\\). حسب نظرية الإيقاف الاختياري: \\(\\mathbb{E}[X_T] = pN = X_0 = k\\)، ومنه مباشرة \\(p = k/N\\).",
      "Apply \\(\\mathbb{E}[X_T] = X_0\\) where \\(X_T \\in \\{0, N\\}\\).",
      "طبق \\(\\mathbb{E}[X_T] = X_0\\) حيث لا يأخذ المتغير عند التوقف سوى القيمتين 0 أو \\(N\\).")

    # 354: Quadratic Variation of Brownian Motion
    q("KAUST-P3-354", "Stochastic Calculus", "Medium",
      "For a standard Brownian motion \\(W_t\\) on \\([0, T]\\), let \\(\\Pi_n = \\{0 = t_0 < t_1 < \\dots < t_n = T\\}\\) be a partition with mesh size \\(|\\Pi_n| \\to 0\\). In what sense and to what value does the quadratic variation \\(\\sum_{i=0}^{n-1} (W_{t_{i+1}} - W_{t_i})^2\\) converge?",
      "لحركة براونية قياسية \\(W_t\\) على \\([0, T]\\)، بأي مفهوم وإلى أي قيمة يتقارب التغير التربيعي \\(\\sum (W_{t_{i+1}} - W_{t_i})^2\\) مع تناهي قطر التجزئة للصفر؟",
      ["Converges in \\(L^2\\) (and in probability) to \\(T\\)",
       "Converges to 0",
       "Diverges to \\(\\infty\\)",
       "Converges to \\(W_T^2\\)"],
      0,
      "Let \\(\\Delta W_i = W_{t_{i+1}} - W_{t_i}\\). Then \\(\\mathbb{E}[(\\Delta W_i)^2] = \\Delta t_i\\), so \\(\\mathbb{E}\\left[\\sum (\\Delta W_i)^2\\right] = \\sum \\Delta t_i = T\\). The variance is \\(\\text{Var}\\left(\\sum (\\Delta W_i)^2\\right) = \\sum \\text{Var}((\\Delta W_i)^2) = \\sum 2 (\\Delta t_i)^2 \\le 2 |\\Pi_n| \\sum \\Delta t_i = 2 |\\Pi_n| T \\to 0\\) as \\(|\\Pi_n| \\to 0\\). By Chebyshev's inequality, \\(\\sum (\\Delta W_i)^2 \\xrightarrow{L^2} T\\). This non-zero deterministic quadratic variation \\([W, W]_T = T\\) is the foundation of Itô calculus.",
      "التوقع الرياضي لمجموع مربعات الزيادات هو \\(\\sum \\Delta t_i = T\\). والتباين يؤول للصفر لأن \\(\\text{Var} = 2\\sum (\\Delta t_i)^2 \\le 2|\\Pi_n|T \\to 0\\). بالتالي يتقارب التغير التربيعي في فضاء \\(L^2\\) وفي الاحتمال إلى القيمة الحتمية \\(T\\).",
      "Compute the expectation and show the variance vanishes as mesh size shrinks.",
      "احسب التوقع وأثبت أن التباين يؤول للصفر مع تناهي قطر التجزئة.")

    # 355: Geometric Brownian Motion Exact Solution
    q("KAUST-P3-355", "Stochastic Calculus", "Hard",
      "Solve the stochastic differential equation for Geometric Brownian Motion: \\(dS_t = \\mu S_t dt + \\sigma S_t dW_t\\) with \\(S_0 > 0\\).",
      "حل المعادلة التفاضلية العشوائية للحركة البراونية الهندسية: \\(dS_t = \\mu S_t dt + \\sigma S_t dW_t\\) مع \\(S_0 > 0\\).",
      ["\\(S_t = S_0 \\exp\\left(\\left(\\mu - \\frac{1}{2}\\sigma^2\\right)t + \\sigma W_t\\right)\\)",
       "\\(S_t = S_0 \\exp(\\mu t + \\sigma W_t)\\)",
       "\\(S_t = S_0 \\exp\\left(\\left(\\mu + \\frac{1}{2}\\sigma^2\\right)t + \\sigma W_t\\right)\\)",
       "\\(S_t = S_0 (1 + \\mu t + \\sigma W_t)\\)"],
      0,
      "Apply Itô's formula to \\(f(S) = \\ln S\\). Here \\(f'(S) = 1/S\\) and \\(f''(S) = -1/S^2\\). Then: \\(d(\\ln S_t) = \\frac{1}{S_t} dS_t + \\frac{1}{2}\\left(-\\frac{1}{S_t^2}\\right)(dS_t)^2 = \\frac{1}{S_t}(\\mu S_t dt + \\sigma S_t dW_t) - \\frac{1}{2S_t^2}(\\sigma^2 S_t^2 dt) = \\mu dt + \\sigma dW_t - \\frac{1}{2}\\sigma^2 dt = \\left(\\mu - \\frac{1}{2}\\sigma^2\\right)dt + \\sigma dW_t\\). Integrating from \\(0\\) to \\(t\\): \\(\\ln(S_t / S_0) = \\left(\\mu - \\frac{1}{2}\\sigma^2\\right)t + \\sigma W_t\\). Exponentiating yields \\(S_t = S_0 \\exp\\left(\\left(\\mu - \\frac{1}{2}\\sigma^2\\right)t + \\sigma W_t\\right)\\).",
      "بتطبيق صيغة إيتو على \\(\\ln S_t\\) مع \\(f' = 1/S\\) و \\(f'' = -1/S^2\\): نجد \\(d(\\ln S_t) = (\\mu - \\frac{1}{2}\\sigma^2)dt + \\sigma dW_t\\). بالمكاملة المباشرة وأخذ الأس نحصل على الحل الكلاسيكي للحركة البراونية الهندسية.",
      "Apply Itô's formula to \\(f(S) = \\ln(S)\\) to find \\(d(\\ln S_t)\\).",
      "طبق صيغة إيتو على لوغاريتم السعر \\(\\ln(S)\\).")

    # 356: Absorbing Markov Chains - Fundamental Matrix
    q("KAUST-P3-356", "Markov Chains", "Hard",
      "An absorbing Markov chain in canonical form has transition matrix \\(P = \\begin{pmatrix} Q & R \\\\ 0 & I \\end{pmatrix}\\), where \\(Q\\) corresponds to transitions among transient states. The fundamental matrix is \\(N = (I - Q)^{-1}\\). What does the entry \\(N_{ij}\\) represent?",
      "سلسلة ماركوف الماصة في صورتها القياسية لها مصفوفة انتقال \\(P = \\begin{pmatrix} Q & R \\\\ 0 & I \\end{pmatrix}\\). المصفوفة الأساسية هي \\(N = (I - Q)^{-1}\\). ماذا يمثل العنصر \\(N_{ij}\\)؟",
      ["The expected number of visits to transient state \\(j\\) starting from transient state \\(i\\) before absorption",
       "The probability of being absorbed into state \\(j\\)",
       "The variance of the time until absorption",
       "The rate of transition from \\(i\\) to \\(j\\)"],
      0,
      "The matrix power \\(Q^k_{ij}\\) gives the probability of being in transient state \\(j\\) after \\(k\\) steps starting from \\(i\\). The total number of visits to state \\(j\\) is \\(V_{ij} = \\sum_{k=0}^\\infty \\mathbb{I}_{\\{X_k = j\\}}\\). By linearity of expectation: \\(\\mathbb{E}[V_{ij}] = \\sum_{k=0}^\\infty Q^k_{ij} = (\\sum_{k=0}^\\infty Q^k)_{ij}\\). Since \\(Q^k \\to 0\\) as \\(k \\to \\infty\\), the geometric series sums to \\((I - Q)^{-1} = N\\). Thus \\(N_{ij}\\) is the expected number of visits to state \\(j\\) before absorption.",
      "تمثل \\(Q^k_{ij}\\) احتمال التواجد في الحالة العابرة \\(j\\) بعد \\(k\\) خطوة. مجموع المتسلسلة الهندسية \\(\\sum_{k=0}^\\infty Q^k = (I - Q)^{-1} = N\\) يعطي القيمة المتوقعة للعدد الكلي للزيارات للحالة العابرة \\(j\\) انطلاقاً من \\(i\\) قبل الوقوع في إحدى الحالات الماصة.",
      "Sum the geometric series of transition powers \\(\\sum_{k=0}^\\infty Q^k\\).",
      "اجمع المتسلسلة الهندسية لقوى مصفوفة الحالات العابرة.")

    # 357: Poisson Process Inter-arrival and Waiting Times
    q("KAUST-P3-357", "Poisson Processes", "Medium",
      "For a Poisson process \\(N(t)\\) with rate \\(\\lambda > 0\\), what is the probability distribution of the waiting time \\(S_n\\) until the \\(n\\)-th arrival?",
      "لعملية بواسون \\(N(t)\\) بمعدل \\(\\lambda > 0\\)، ما هو التوزيع الاحتمالي لزمن الانتظار \\(S_n\\) حتى وصول الحدث رقم \\(n\\)؟",
      ["\\(\\text{Gamma}(n, \\lambda)\\) (Erlang distribution)",
       "\\(\\text{Exponential}(n\\lambda)\\)",
       "\\(\\text{Poisson}(n\\lambda)\\)",
       "\\(\\text{Normal}(n/\\lambda, n/\\lambda^2)\\)"],
      0,
      "The arrival time of the \\(n\\)-th event is the sum of \\(n\\) independent inter-arrival times: \\(S_n = T_1 + T_2 + \\dots + T_n\\), where each \\(T_i \\sim \\text{Exponential}(\\lambda)\\). The sum of \\(n\\) independent exponential random variables with rate \\(\\lambda\\) follows the Gamma (or Erlang) distribution with shape parameter \\(n\\) and rate \\(\\lambda\\), having density \\(f_{S_n}(t) = \\frac{\\lambda^n t^{n-1} e^{-\\lambda t}}{(n-1)!}\\) for \\(t > 0\\).",
      "زمن وصول الحدث رقم \\(n\\) هو مجموع \\(n\\) من أزمنة الوصول البينية المستقلة والمتطابقة والتي يتبع كل منها توزيعاً أسياً بمعدل \\(\\lambda\\). مجموع \\(n\\) متغيرات أسية يتبع توزيع غاما (أو توزيع إيرلانغ) بالمعالم \\((n, \\lambda)\\) وكثافته \\(\\frac{\\lambda^n t^{n-1} e^{-\\lambda t}}{(n-1)!}\\).",
      "The sum of \\(n\\) i.i.d. Exponential(\\(\\lambda\\)) random variables is an Erlang / Gamma distribution.",
      "مجموع \\(n\\) متغيرات عشوائية أسية مستقلة هو توزيع غاما (إيرلانغ).")

    # 358: Continuous-Time Markov Chain (CTMC) Stationary Distribution
    q("KAUST-P3-358", "Markov Chains", "Hard",
      "For an irreducible continuous-time Markov chain with generator matrix \\(Q\\), what equation defines the stationary probability distribution \\(\\boldsymbol{\\pi}\\)?",
      "لسلسلة ماركوف متصلة الزمن غير قابلة للاختزال ذات مصفوفة توليد \\(Q\\)، ما هي المعادلة التي تحدد التوزيع الاحتمالي المستقر \\(\\boldsymbol{\\pi}\\)؟",
      ["\\(\\boldsymbol{\\pi} Q = \\mathbf{0}\\) with \\(\\sum_i \\pi_i = 1\\)",
       "\\(\\boldsymbol{\\pi} Q = \\boldsymbol{\\pi}\\) with \\(\\sum_i \\pi_i = 1\\)",
       "\\(Q \\boldsymbol{\\pi} = \\mathbf{0}\\)",
       "\\(\\det(Q) = 0\\)"],
      0,
      "The Kolmogorov forward equations for transition probabilities are \\(\\frac{d}{dt} P(t) = P(t) Q\\). At equilibrium (steady-state), the state probabilities \\(\\boldsymbol{\\pi}(t)\\) do not change over time, so \\(\\frac{d\\boldsymbol{\\pi}}{dt} = \\mathbf{0}\\). Substituting gives \\(\\boldsymbol{\\pi} Q = \\mathbf{0}\\), along with the normalization \\(\\sum_i \\pi_i = 1\\). This reflects global balance: for each state, the total transition rate in equals the total transition rate out.",
      "معادلات كولموغوروف الأمامية تعطي \\(\\frac{d\\boldsymbol{\\pi}}{dt} = \\boldsymbol{\\pi} Q\\). في الحالة المستقرة تتوقف الاحتمالات عن التغير مع الزمن، أي \\(\\frac{d\\boldsymbol{\\pi}}{dt} = \\mathbf{0}\\). ينتج عن ذلك \\(\\boldsymbol{\\pi} Q = \\mathbf{0}\\) مع شرط المعايرة \\(\\sum \\pi_i = 1\\).",
      "Set the time derivative \\(\\frac{d\\boldsymbol{\\pi}}{dt} = \\boldsymbol{\\pi} Q\\) to zero.",
      "ساوِ المشتقة الزمنية للاحتمالات بالصفر عند الاتزان.")

    # 359: M/M/1 Queue Stationary Distribution
    q("KAUST-P3-359", "Queueing Theory", "Medium",
      "An M/M/1 queue has arrival rate \\(\\lambda\\) and service rate \\(\\mu\\), with traffic intensity \\(\\rho = \\lambda / \\mu < 1\\). What is the stationary probability \\(\\pi_n\\) that there are \\(n\\) customers in the system?",
      "نظام صفوف انتظار M/M/1 له معدل وصول \\(\\lambda\\) ومعدل خدمة \\(\\mu\\) مع شدة حركة \\(\\rho = \\lambda/\\mu < 1\\). ما هو الاحتمال المستقر \\(\\pi_n\\) لوجود \\(n\\) زبون في النظام؟",
      ["\\(\\pi_n = (1 - \\rho) \\rho^n\\) for \\(n = 0, 1, 2, \\dots\\)",
       "\\(\\pi_n = \\rho^n\\)",
       "\\(\\pi_n = \\frac{\\rho^n}{n!} e^{-\\rho}\\)",
       "\\(\\pi_n = (1 - \\rho) \\frac{\\rho^n}{n!}\\)"],
      0,
      "The birth-death balance equations for the M/M/1 queue are \\(\\lambda \\pi_n = \\mu \\pi_{n+1} \\implies \\pi_{n+1} = \\rho \\pi_n\\). By induction, \\(\\pi_n = \\rho^n \\pi_0\\). Using normalization: \\(\\sum_{n=0}^\\infty \\pi_n = \\pi_0 \\sum_{n=0}^\\infty \\rho^n = \\frac{\\pi_0}{1 - \\rho} = 1 \\implies \\pi_0 = 1 - \\rho\\). Therefore, \\(\\pi_n = (1 - \\rho) \\rho^n\\), which is a Geometric distribution on \\(\\{0, 1, 2, \\dots\\}\\).",
      "معادلات التوازن لمسألة الولادة والموت في صف M/M/1 هي \\(\\lambda \\pi_n = \\mu \\pi_{n+1}\\)، ومنها \\(\\pi_n = \\rho^n \\pi_0\\). بمجموع المتسلسلة الهندسية نجد \\(\\pi_0 = 1 - \\rho\\). وبالتالي فإن \\(\\pi_n = (1-\\rho)\\rho^n\\)، وهو التوزيع الهندسي.",
      "Use the balance relation \\(\\pi_{n+1} = \\rho \\pi_n\\) and sum the geometric series.",
      "استخدم علاقة التوازن التكرارية واجمع المتسلسلة الهندسية.")

    # 360: M/M/1 Expected Number of Customers
    q("KAUST-P3-360", "Queueing Theory", "Medium",
      "For the same M/M/1 queue with \\(\\rho = \\lambda/\\mu < 1\\), what is the expected total number of customers \\(L\\) in the system in steady state?",
      "لنفس نظام M/M/1 السابق مع \\(\\rho < 1\\)، ما هو العدد المتوقع للزبائن \\(L\\) في النظام عند الاستقرار؟",
      ["\\(L = \\frac{\\rho}{1 - \\rho}\\)",
       "\\(L = \\frac{1}{1 - \\rho}\\)",
       "\\(L = \\frac{\\rho^2}{1 - \\rho}\\)",
       "\\(L = \\rho\\)"],
      0,
      "Using \\(\\pi_n = (1 - \\rho)\\rho^n\\), compute the mean of the geometric distribution: \\(L = \\sum_{n=0}^\\infty n \\pi_n = (1 - \\rho) \\sum_{n=1}^\\infty n \\rho^n = (1 - \\rho) \\rho \\sum_{n=1}^\\infty n \\rho^{n-1} = (1 - \\rho) \\rho \\frac{1}{(1 - \\rho)^2} = \\frac{\\rho}{1 - \\rho}\\). Notice that as \\(\\rho \\to 1\\), the queue length explodes to infinity.",
      "بحساب القيمة المتوقعة للتوزيع الهندسي: \\(L = \\sum n (1-\\rho)\\rho^n = (1-\\rho)\\rho \\frac{d}{d\\rho}\\sum \\rho^n = \\frac{\\rho}{1-\\rho}\\). نلاحظ أنه عندما يقترب معامل التشغيل من 1، ينفجر طول الصف إلى اللانهاية.",
      "Compute the expectation \\(\\sum_{n=0}^\\infty n (1-\\rho)\\rho^n\\).",
      "احسب توقع التوزيع الهندسي باستخدام تفاضل المتسلسلة الهندسية.")

    # 361 to 400: Generate remaining 40 questions for Part C
    # 361: Ornstein-Uhlenbeck Process
    q("KAUST-P3-361", "Stochastic Calculus", "Hard",
      "The Ornstein-Uhlenbeck process satisfies the mean-reverting SDE \\(dX_t = -\\theta X_t dt + \\sigma dW_t\\) with \\(X_0 = x_0\\) and \\(\\theta, \\sigma > 0\\). What is the long-term variance \\(\\lim_{t\\to\\infty} \\text{Var}(X_t)\\)?",
      "تحقق عملية أورنشتاين-أولنبيك المعادلة التفاضلية العشوائية ذات الارتداد للمتوسط \\(dX_t = -\\theta X_t dt + \\sigma dW_t\\). ما هو التباين طويل الأمد \\(\\lim_{t\\to\\infty} \\text{Var}(X_t)\\)؟",
      ["\\(\\frac{\\sigma^2}{2\\theta}\\)", "\\(\\frac{\\sigma^2}{\\theta}\\)", "\\(\\frac{\\sigma}{\\sqrt{2\\theta}}\\)", "\\(\\frac{\\sigma^2}{4\\theta^2}\\)"],
      0,
      "Multiply by the integrating factor \\(e^{\\theta t}\\): \\(d(e^{\\theta t} X_t) = e^{\\theta t} dX_t + \\theta e^{\\theta t} X_t dt = \\sigma e^{\\theta t} dW_t\\). Integrating: \\(X_t = x_0 e^{-\\theta t} + \\sigma \\int_0^t e^{-\\theta(t-s)} dW_s\\). The expectation is \\(\\mathbb{E}[X_t] = x_0 e^{-\\theta t} \\to 0\\). By Itô's isometry: \\(\\text{Var}(X_t) = \\sigma^2 \\int_0^t e^{-2\\theta(t-s)} ds = \\sigma^2 \\left[\\frac{e^{-2\\theta(t-s)}}{2\\theta}\\right]_0^t = \\frac{\\sigma^2}{2\\theta}(1 - e^{-2\\theta t})\\). As \\(t \\to \\infty\\), \\(\\text{Var}(X_t) \\to \\frac{\\sigma^2}{2\\theta}\\).",
      "باستخدام عامل المكاملة \\(e^{\\theta t}\\) والتكامل العشوائي نجد \\(X_t = x_0 e^{-\\theta t} + \\sigma \\int_0^t e^{-\\theta(t-s)} dW_s\\). بحساب التباين باستخدام متساوي قياس إيتو: \\(\\text{Var} = \\sigma^2 \\int_0^t e^{-2\\theta(t-s)} ds = \\frac{\\sigma^2}{2\\theta}(1 - e^{-2\\theta t})\\). عند \\(t \\to \\infty\\) يؤول التباين إلى \\(\\frac{\\sigma^2}{2\\theta}\\).",
      "Apply Itô's isometry to the stochastic integral \\(\\int_0^t e^{-\\theta(t-s)} dW_s\\).",
      "طبق متساوي قياس إيتو على التكامل العشوائي واحسب تكامل مربع الدالة الأسية.")

    # 362: Fokker-Planck Equation
    q("KAUST-P3-362", "Stochastic Calculus", "Hard",
      "For a stochastic process satisfying the Itô SDE \\(dX_t = b(X_t) dt + \\sigma(X_t) dW_t\\), the probability density function \\(p(x, t)\\) evolves according to which Fokker-Planck (Kolmogorov forward) PDE?",
      "لعملية عشوائية تحقق معادلة إيتو \\(dX_t = b(X_t)dt + \\sigma(X_t)dW_t\\)، كيف تتطور دالة كثافة الاحتمال \\(p(x, t)\\) وفق معادلة فوكر-بلانك؟",
      ["\\(\\frac{\\partial p}{\\partial t} = -\\frac{\\partial}{\\partial x}[b(x) p] + \\frac{1}{2}\\frac{\\partial^2}{\\partial x^2}[\\sigma^2(x) p]\\)",
       "\\(\\frac{\\partial p}{\\partial t} = b(x) \\frac{\\partial p}{\\partial x} + \\frac{1}{2}\\sigma^2(x) \\frac{\\partial^2 p}{\\partial x^2}\\)",
       "\\(\\frac{\\partial p}{\\partial t} = -b(x) p + \\sigma(x) \\frac{\\partial p}{\\partial x}\\)",
       "\\(\\frac{\\partial p}{\\partial t} = \\frac{\\partial^2}{\\partial x^2}[b(x) p] - \\frac{\\partial}{\\partial x}[\\sigma(x) p]\\)"],
      0,
      "By applying Itô's lemma to a smooth test function \\(f(X_t)\\) and taking expectations: \\(\\frac{d}{dt}\\mathbb{E}[f(X_t)] = \\mathbb{E}[b(X_t) f'(X_t) + \\frac{1}{2}\\sigma^2(X_t) f''(X_t)]\\). Expressing the expectations in terms of the density \\(p(x, t)\\) and integrating by parts yields: \\(\\int f \\frac{\\partial p}{\\partial t} dx = \\int f \\left(-\\frac{\\partial}{\\partial x}[b(x)p] + \\frac{1}{2}\\frac{\\partial^2}{\\partial x^2}[\\sigma^2(x)p]\\right) dx\\). Since this holds for all test functions \\(f\\), we obtain the Fokker-Planck equation.",
      "بتطبيق صيغة إيتو على دالة اختبارية وحساب التوقع ثم التكامل بالتجزئة لنقل المشتقات من دالة الاختبار إلى دالة الكثافة \\(p(x, t)\\)، نصل مباشرة إلى معادلة فوكر-بلانك: \\(\\frac{\\partial p}{\\partial t} = -\\frac{\\partial}{\\partial x}[b(x)p] + \\frac{1}{2}\\frac{\\partial^2}{\\partial x^2}[\\sigma^2(x)p]\\).",
      "Integrate by parts to move spatial derivatives from the test function onto the density.",
      "كامل بالتجزئة لنقل المشتقات المكانية من دالة الاختبار إلى دالة الكثافة.")

    # 363: Doob's Optional Stopping Theorem Conditions
    q("KAUST-P3-363", "Martingales", "Hard",
      "Which of the following is NOT a sufficient condition for the Optional Stopping Theorem to hold (i.e., \\(\\mathbb{E}[M_T] = \\mathbb{E}[M_0]\\)) for a stopping time \\(T\\) and martingale \\(M_n\\)?",
      "أي مما يلي ليس شرطاً كافياً لضمان صحة نظرية الإيقاف الاختياري لدووب (\\(\\mathbb{E}[M_T] = \\mathbb{E}[M_0]\\)) لمارتينغال \\(M_n\\) وزمن توقف \\(T\\)؟",
      ["\\(T\\) is finite with probability 1 (\\(\\mathbb{P}(T < \\infty) = 1\\)) with no other boundedness conditions",
       "\\(T\\) is a bounded stopping time (\\(T \\le K\\) almost surely)",
       "\\(M_n\\) is uniformly bounded and \\(T < \\infty\\) almost surely",
       "\\(\\mathbb{E}[T] < \\infty\\) and \\(|M_{n+1} - M_n| \\le c < \\infty\\) almost surely"],
      0,
      "Merely knowing that \\(T < \\infty\\) almost surely is NOT sufficient for the Optional Stopping Theorem. A famous counterexample is the doubling strategy in a fair coin toss: the stopping time \\(T\\) (time of first win) is finite with probability 1, but \\(M_T = 1\\) with probability 1, while \\(M_0 = 0\\), so \\(1 = \\mathbb{E}[M_T] \\neq \\mathbb{E}[M_0] = 0\\). The theorem requires integrability conditions like boundedness of \\(T\\), uniform boundedness of \\(M\\), or bounded increments with finite expected stopping time.",
      "مجرد كون زمن التوقف منتهياً باحتمال 1 لا يكفي لصحة نظرية الإيقاف الاختياري. وخير مثال مضاد هو استراتيجية المضاعفة في رمي العملة، حيث زمن التوقف منتهٍ حتماً، ولكن \\(M_T = 1\\) دائماً بينما \\(M_0 = 0\\). تتطلب النظرية شروط محدودية إضافية.",
      "Consider the classic Martingale doubling betting strategy where \\(\\mathbb{E}[M_T] = 1 \\neq 0\\).",
      "تذكر استراتيجية المقامرة بالمضاعفة التي تفشل فيها مساواة التوقع.")

    # 364: Doob's Maximal Inequality
    q("KAUST-P3-364", "Martingales", "Hard",
      "Let \\(M_n\\) be a non-negative submartingale. Doob's maximal inequality bounds the maximum value \\(M_n^* = \\max_{0 \\le k \\le n} M_k\\). For any \\(\\lambda > 0\\):",
      "لتكن \\(M_n\\) شبه مارتينغال غير سالب. يحدد حصر دووب الأعظمي احتمال تجاوز القيمة العظمى \\(M_n^*\\) لحاجز \\(\\lambda > 0\\) بـ:",
      ["\\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le \\frac{\\mathbb{E}[M_n]}{\\lambda}\\)",
       "\\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le \\frac{\\mathbb{E}[M_0]}{\\lambda}\\)",
       "\\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le \\frac{\\text{Var}(M_n)}{\\lambda^2}\\)",
       "\\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le e^{-\\lambda}\\)"],
      0,
      "Doob's first submartingale inequality states that for a non-negative submartingale \\(M_k\\) and any \\(\\lambda > 0\\), \\(\\lambda \\mathbb{P}(\\max_{0 \\le k \\le n} M_k \\ge \\lambda) \\le \\mathbb{E}[M_n \\mathbb{I}_{\\{M_n^* \\ge \\lambda\\}}] \\le \\mathbb{E}[M_n]\\). Dividing by \\(\\lambda\\) gives \\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le \\frac{\\mathbb{E}[M_n]}{\\lambda}\\). This powerful inequality extends Markov's inequality from the final value \\(M_n\\) to the running maximum over the entire trajectory.",
      "تنص متباينة دووب لشبه المارتينغال غير السالب على أن \\(\\lambda \\mathbb{P}(M_n^* \\ge \\lambda) \\le \\mathbb{E}[M_n]\\). بالقسمة على \\(\\lambda\\) نحصل على \\(\\mathbb{P}(M_n^* \\ge \\lambda) \\le \\frac{\\mathbb{E}[M_n]}{\\lambda}\\)، وهي تعميم قوي لمتباينة ماركوف ليشمل القيمة العظمى للمسار بأكمله.",
      "This is an extension of Markov's inequality to the entire running maximum.",
      "هذه المتباينة هي امتداد لمتباينة ماركوف على القيمة العظمى الجارية.")

    # 365: Transition Probability Matrix Powers Limit
    q("KAUST-P3-365", "Markov Chains", "Medium",
      "For an irreducible, aperiodic finite Markov chain with transition matrix \\(P\\) and unique stationary distribution \\(\\boldsymbol{\\pi} = (\\pi_1, \\dots, \\pi_m)\\), what is \\(\\lim_{n \\to \\infty} P^n\\)?",
      "لسلسلة ماركوف منتهية وغير قابلة للاختزال ولا دورية ذات مصفوفة انتقال \\(P\\) وتوزيع مستقر \\(\\boldsymbol{\\pi}\\)، ما هي نهاية قوى المصفوفة \\(\\lim_{n \\to \\infty} P^n\\)؟",
      ["A matrix where every row is identical and equal to \\(\\boldsymbol{\\pi}\\)",
       "The identity matrix \\(I\\)",
       "The zero matrix",
       "A diagonal matrix containing \\(\\boldsymbol{\\pi}\\)"],
      0,
      "By the Fundamental Limit Theorem for Markov chains, if a finite chain is irreducible and aperiodic, the state distribution converges to \\(\\boldsymbol{\\pi}\\) regardless of the starting state. Concretely, \\(\\lim_{n\\to\\infty} P^n_{ij} = \\pi_j\\) for all \\(i\\). Therefore, every row of the limiting matrix \\(\\lim_{n\\to\\infty} P^n\\) converges to the exact same row vector \\(\\boldsymbol{\\pi} = (\\pi_1, \\pi_2, \\dots, \\pi_m)\\).",
      "حسب مبرهنة النهاية الأساسية لسلاسل ماركوف، فإن \\(\\lim_{n\\to\\infty} P^n_{ij} = \\pi_j\\) لجميع الصفوف \\(i\\). بالتالي، فإن جميع صفوف مصفوفة النهاية تتطابق وتساوي متجهة السطر للتوزيع المستقر \\(\\boldsymbol{\\pi}\\).",
      "Every row converges to the stationary distribution vector.",
      "كل صف في مصفوفة النهاية يتقارب إلى متجه التوزيع المستقر.")

    # 366: Period of a Markov Chain State
    q("KAUST-P3-366", "Markov Chains", "Medium",
      "The period \\(d(i)\\) of a state \\(i\\) in a Markov chain is defined as \\(d(i) = \\gcd\\{n \\ge 1 : P^n_{ii} > 0\\}\\). If a state has \\(P_{ii} > 0\\), what is its period?",
      "يُعرّف دور الحالة \\(i\\) في سلسلة ماركوف بـ \\(d(i) = \\gcd\\{n \\ge 1 : P^n_{ii} > 0\\}\\). إذا كان للحالة احتمال بقاء ذاتي موجباً \\(P_{ii} > 0\\)، فما هو دورها؟",
      ["\\(d(i) = 1\\) (aperiodic)",
       "\\(d(i) = 2\\)",
       "\\(d(i) = 0\\)",
       "\\(d(i) = \\infty\\)"],
      0,
      "If \\(P_{ii} > 0\\), then \\(n = 1\\) is in the return set \\(\\{n \\ge 1 : P^n_{ii} > 0\\}\\). Since the greatest common divisor of any set of positive integers containing \\(1\\) is \\(1\\) (\\(\\gcd(1, k, \\dots) = 1\\)), the period must be \\(d(i) = 1\\). Any state with a self-loop is automatically aperiodic.",
      "إذا كان \\(P_{ii} > 0\\)، فإن العدد 1 ينتمي لمجموعة أزمنة العودة الممكنة. وبما أن القاسم المشترك الأكبر لأي مجموعة تحوي العدد 1 هو 1 حتماً، فإن دور الحالة هو 1، وتسمى الحالة لا دورية (aperiodic).",
      "The greatest common divisor of any set containing 1 is 1.",
      "القاسم المشترك الأكبر لأي مجموعة تحوي العدد 1 هو 1 دائماً.")

    # 367: Poisson Thinning (Splitting)
    q("KAUST-P3-367", "Poisson Processes", "Medium",
      "Events arrive according to a Poisson process with rate \\(\\lambda\\). Each arriving event is independently classified as Type 1 with probability \\(p\\) and Type 2 with probability \\(1 - p\\). What is the joint distribution of the number of Type 1 events \\(N_1(t)\\) and Type 2 events \\(N_2(t)\\) by time \\(t\\)?",
      "تصل الأحداث وفق عملية بواسون بمعدل \\(\\lambda\\). يُصنف كل حدث باستقلال كنوع 1 باحتمال \\(p\\) أو كنوع 2 باحتمال \\(1-p\\). ما هو التوزيع المشترك لـ \\(N_1(t)\\) و \\(N_2(t)\\)؟",
      ["\\(N_1(t)\\) and \\(N_2(t)\\) are completely independent Poisson processes with rates \\(\\lambda p\\) and \\(\\lambda(1-p)\\)",
       "They are negatively correlated with \\(\\text{Cov}(N_1, N_2) = -\\lambda t\\)",
       "They form a multinomial distribution and are dependent",
       "\\(N_1(t)\\) is Poisson but \\(N_2(t)\\) is Binomial"],
      0,
      "By the Poisson Thinning Theorem, splitting a Poisson process of rate \\(\\lambda\\) by independent Bernoulli trials with parameter \\(p\\) decomposes it into two strictly INDEPENDENT Poisson processes: \\(N_1(t) \\sim \\text{Poisson}(\\lambda p t)\\) and \\(N_2(t) \\sim \\text{Poisson}(\\lambda(1-p)t)\\). The remarkable fact that \\(N_1(t)\\) and \\(N_2(t)\\) are statistically independent is a unique property of the Poisson process.",
      "تنص نظرية ترقيق بواسون (Poisson Thinning) على أن تقسيم عملية بواسون بمحاولات برنولي المستقلة يفككها إلى عمليتي بواسون مستقلتين إحصائياً تماماً بمعدلي \\(\\lambda p\\) و \\(\\lambda(1-p)\\).",
      "Independent thinning of a Poisson process creates two independent Poisson processes.",
      "التصنيف المستقل لأحداث عملية بواسون ينتج عمليتي بواسون مستقلتين تماماً.")

    # 368: Itô Integral Expectation and Martingale Property
    q("KAUST-P3-368", "Stochastic Calculus", "Hard",
      "Let \\(f(t)\\) be an adapted square-integrable process (\\(\\mathbb{E}[\\int_0^T f(t)^2 dt] < \\infty\\)). What are the expectation and martingale properties of the Itô integral \\(I_t = \\int_0^t f(s) dW_s\\)?",
      "ليكن \\(f(t)\\) مساراً عشوائياً متكيفاً وقابلاً للتكامل التربيعي. ما هو التوقع الرياضي وخاصية المارتينغال للتكامل العشوائي لإيتو \\(I_t = \\int_0^t f(s) dW_s\\)؟",
      ["\\(\\mathbb{E}[I_t] = 0\\) for all \\(t\\), and \\(I_t\\) is a continuous martingale",
       "\\(\\mathbb{E}[I_t] = t\\), and \\(I_t\\) is a submartingale",
       "\\(\\mathbb{E}[I_t] = \\int_0^t \\mathbb{E}[f(s)] ds\\)",
       "\\(I_t\\) is not a martingale"],
      0,
      "A fundamental property of the Itô stochastic integral is that it has zero mean: \\(\\mathbb{E}\\left[\\int_0^t f(s) dW_s\\right] = 0\\) for all \\(t \\ge 0\\). Furthermore, for \\(s < t\\), \\(\\mathbb{E}\\left[\\int_0^t f(u) dW_u \\,\\middle|\\, \\mathcal{F}_s\\right] = \\int_0^s f(u) dW_u + \\mathbb{E}\\left[\\int_s^t f(u) dW_u \\,\\middle|\\, \\mathcal{F}_s\\right] = I_s + 0 = I_s\\). Thus the Itô integral \\(I_t\\) is always a martingale.",
      "من الخواص الجوهرية لتكامل إيتو العشوائي أن توقعه الرياضي صفر دائماً: \\(\\mathbb{E}[I_t] = 0\\). كما أنه يحقق شرط المارتينغال: التوقع الشرطي لـ \\(I_t\\) بالنظر إلى تاريخ العملية حتى \\(s\\) يساوي \\(I_s\\). بالتالي فإن تكامل إيتو هو مارتينغال مستمر.",
      "The expectation of any Itô stochastic integral with respect to Brownian motion is zero.",
      "توقع أي تكامل عشوائي لإيتو بالنسبة للحركة البراونية يساوي صفراً دوماً.")

    # 369: Itô's Isometry
    q("KAUST-P3-369", "Stochastic Calculus", "Hard",
      "Itô's isometry relates the variance of an Itô integral to the norm of the integrand. What is the explicit identity?",
      "تربط متطابقة إيتو القياسية تباين تكامل إيتو بمعيار الدالة المكاملة. ما هي المتطابقة الصريحة؟",
      ["\\(\\mathbb{E}\\left[\\left(\\int_0^T f(t) dW_t\\right)^2\\right] = \\mathbb{E}\\left[\\int_0^T f(t)^2 dt\\right]\\)",
       "\\(\\mathbb{E}\\left[\\left(\\int_0^T f(t) dW_t\\right)^2\\right] = \\left(\\mathbb{E}\\left[\\int_0^T f(t) dt\\right]\\right)^2\\)",
       "\\(\\mathbb{E}\\left[\\left(\\int_0^T f(t) dW_t\\right)^2\\right] = T \\mathbb{E}[f(T)^2]\\)",
       "\\(\\mathbb{E}\\left[\\left(\\int_0^T f(t) dW_t\\right)^2\\right] = 0\\)"],
      0,
      "Itô's Isometry states that for any adapted process \\(f \\in L^2(\\Omega \\times [0, T])\\), \\(\\mathbb{E}\\left[\\left(\\int_0^T f(t) dW_t\\right)^2\\right] = \\mathbb{E}\\left[\\int_0^T f(t)^2 dt\\right]\\). This establishes an isometric embedding from the space \\(L^2([0, T])\\) of integrands into the Hilbert space \\(L^2(\\Omega)\\) of random variables, allowing the stochastic integral to be defined by continuous extension from simple step processes.",
      "تنص متطابقة إيتو متساوية القياس على أن القيمة المتوقعة لمربع التكامل العشوائي تساوي القيمة المتوقعة لتكامل مربع الدالة بالنسبة للزمن المعتاد. هذه المتطابقة تنشئ تماكلاً متساوي القياس يتيح تعريف التكامل العشوائي لجميع الدوال في \\(L^2\\).",
      "Square of stochastic integral matches the integral of the square with \\(dt\\).",
      "مربع التكامل العشوائي يطابق تكامل المربع بالنسبة لـ \\(dt\\).")

    # 370: Little's Law in Queueing Systems
    q("KAUST-P3-370", "Queueing Theory", "Medium",
      "Little's Law is a universal theorem in queueing theory relating the average number of customers \\(L\\) in a stationary queueing system to the arrival rate \\(\\lambda\\) and the average time \\(W\\) a customer spends in the system. The relation is:",
      "قانون ليتل هو نظرية شاملة في نظرية صفوف الانتظار تربط متوسط عدد الزبائن \\(L\\) بمعدل الوصول \\(\\lambda\\) ومتوسط زمن بقاء الزبون \\(W\\). العلاقة هي:",
      ["\\(L = \\lambda W\\)", "\\(L = \\frac{W}{\\lambda}\\)", "\\(L = \\frac{\\lambda}{W}\\)", "\\(L = \\lambda^2 W\\)"],
      0,
      "Little's Law states \\(L = \\lambda W\\). Remarkably, this relation holds with immense generality: it does not depend on the arrival process distribution (does not need to be Poisson), does not depend on the service time distribution (can be arbitrary), and does not depend on the queue discipline (FIFO, LIFO, priority). It holds for any stable system where customers do not vanish.",
      "ينص قانون ليتل على أن \\(L = \\lambda W\\). وتتميز هذه العلاقة بعمومية هائلة: فهي تتحقق لأي توزيع للوصول أو الخدمة وأي ترتيب لخدمة الزبائن، بشرط استقرار النظام وعدم ضياع الزبائن.",
      "The average queue length equals arrival rate times average residence time.",
      "متوسط طول الصف يساوي معدل الوصول مضروباً في متوسط زمن الإقامة.")

    # 371 to 400: Continuing Part C
    # 371: Renewal Reward Theorem
    q("KAUST-P3-371", "Renewal Theory", "Hard",
      "In renewal reward theory, let \\(X_n\\) be i.i.d. inter-renewal times with \\(\\mathbb{E}[X] = \\mu < \\infty\\), and \\(R_n\\) be the reward earned in cycle \\(n\\) with \\(\\mathbb{E}[R] < \\infty\\). What is the long-run expected rate of reward \\(\\lim_{t \\to \\infty} \\frac{R(t)}{t}\\)?",
      "في نظرية التجديد مع العوائد، إذا كان متوسط زمن دورة التجديد \\(\\mathbb{E}[X] = \\mu\\) ومتوسط العائد في الدورة \\(\\mathbb{E}[R]\\)، فما هو معدل العائد المتوقع على المدى الطويل؟",
      ["\\(\\frac{\\mathbb{E}[R]}{\\mathbb{E}[X]}\\) (almost surely)",
       "\\(\\mathbb{E}[R] \\times \\mathbb{E}[X]\\)",
       "\\(\\frac{\\mathbb{E}[X]}{\\mathbb{E}[R]}\\)",
       "\\(\\frac{\\text{Var}(R)}{\\text{Var}(X)}\\)"],
      0,
      "The Renewal Reward Theorem states that \\(\\lim_{t\\to\\infty} \\frac{R(t)}{t} = \\frac{\\mathbb{E}[R_1]}{\\mathbb{E}[X_1]}\\) almost surely. That is, the long-run average rate of reward is simply the expected reward per cycle divided by the expected length of a cycle.",
      "تنص نظرية التجديد مع العوائد على أن معدل العائد التراكمي على المدى الطويل يتقارب شبه مؤكداً إلى نسبة العائد المتوقع في الدورة الواحدة مقسوماً على متوسط طول الدورة: \\(\\frac{\\mathbb{E}[R]}{\\mathbb{E}[X]}\\).",
      "Expected reward per cycle divided by expected duration of a cycle.",
      "اقسم العائد المتوقع في الدورة على متوسط مدة الدورة.")

    # 372: Hitting Time of Brownian Motion
    q("KAUST-P3-372", "Stochastic Calculus", "Hard",
      "Let \\(W_t\\) be a standard Brownian motion with \\(W_0 = 0\\), and let \\(T_a = \\inf\\{t > 0 : W_t = a\\}\\) with \\(a > 0\\) be the first passage time to level \\(a\\). What is the probability density function \\(f_{T_a}(t)\\) for \\(t > 0\\)?",
      "لتكن \\(W_t\\) حركة براونية قياسية. ليكن \\(T_a\\) زمن الوصول الأول للمستوى \\(a > 0\\). ما هي دالة كثافة الاحتمال \\(f_{T_a}(t)\\) لـ \\(t > 0\\)؟",
      ["\\(f_{T_a}(t) = \\frac{a}{\\sqrt{2\\pi t^3}} \\exp\\left(-\\frac{a^2}{2t}\\right)\\) (Lévy distribution)",
       "\\(f_{T_a}(t) = \\frac{1}{\\sqrt{2\\pi t}} \\exp\\left(-\\frac{a^2}{2t}\\right)\\)",
       "\\(f_{T_a}(t) = \\frac{a^2}{2\\pi t^2} \\exp\\left(-\\frac{a}{2t}\\right)\\)",
       "\\(f_{T_a}(t) = \\frac{1}{a} \\exp(-t/a)\\)"],
      0,
      "By the reflection principle: \\(\\mathbb{P}(T_a \\le t) = 2\\mathbb{P}(W_t \\ge a) = 2 \\int_a^\\infty \\frac{1}{\\sqrt{2\\pi t}} e^{-x^2 / (2t)} dx = \\frac{2}{\\sqrt{2\\pi}} \\int_{a/\\sqrt{t}}^\\infty e^{-u^2 / 2} du\\). Differentiating with respect to \\(t\\) using Leibniz's rule: \\(f_{T_a}(t) = \\frac{d}{dt}\\mathbb{P}(T_a \\le t) = -\\frac{2}{\\sqrt{2\\pi}} e^{-a^2/(2t)} \\left(-\\frac{a}{2 t^{3/2}}\\right) = \\frac{a}{\\sqrt{2\\pi t^3}} e^{-a^2 / (2t)}\\). This is the Lévy distribution, an example of a heavy-tailed distribution with infinite mean \\(\\mathbb{E}[T_a] = \\infty\\).",
      "بمبدأ الانعكاس للحركة البراونية: \\(\\mathbb{P}(T_a \\le t) = 2\\mathbb{P}(W_t \\ge a)\\). باشتقاق دالة التوزيع التراكمي بالنسبة للزمن \\(t\\) نصل مباشرة إلى كثافة ليفي: \\(f_{T_a}(t) = \\frac{a}{\\sqrt{2\\pi t^3}} \\exp(-a^2/(2t))\\). متوسط هذا الزمن لا نهائي.",
      "Use the reflection principle \\(\\mathbb{P}(T_a \\le t) = 2\\mathbb{P}(W_t \\ge a)\\) and differentiate with respect to \\(t\\).",
      "استخدم مبدأ الانعكاس وفاضل دالة التوزيع بالنسبة للزمن.")

    # 373: Girsanov's Theorem
    q("KAUST-P3-373", "Stochastic Calculus", "Hard",
      "Girsanov's theorem is fundamental in mathematical finance for changing from the physical measure \\(\\mathbb{P}\\) to the risk-neutral measure \\(\\mathbb{Q}\\). What does it state about a Brownian motion with drift \\(X_t = W_t + \\theta t\\)?",
      "تعتبر نظرية غيرسانوف جوهرية في الرياضيات المالية لتغيير القياس الاحتمالي إلى القياس المحايد للمخاطر. ماذا تنص بخصوص حركة براونية بانجراف \\(X_t = W_t + \\theta t\\)؟",
      ["Under an equivalent probability measure \\(\\mathbb{Q}\\) defined by the Radon-Nikodym derivative \\(\\frac{d\\mathbb{Q}}{d\\mathbb{P}} = e^{-\\theta W_T - \\frac{1}{2}\\theta^2 T}\\), \\(X_t\\) is a driftless standard Brownian motion",
       "\\(X_t\\) can never be transformed into a standard Brownian motion",
       "The variance of \\(X_t\\) changes from \\(t\\) to \\(\\theta^2 t\\)",
       "The drift \\(\\theta\\) is multiplied by 2"],
      0,
      "Girsanov's theorem asserts that adding a drift to a Brownian motion does not change the class of equivalent probability measures. By weighting paths with the Cameron-Martin-Girsanov density martingale \\(Z_t = \\exp\\left(-\\int_0^t \\theta_s dW_s - \\frac{1}{2}\\int_0^t \\theta_s^2 ds\\right)\\), the shifted process \\(\\tilde{W}_t = W_t + \\int_0^t \\theta_s ds\\) becomes a standard Brownian motion with zero drift under the new measure \\(\\mathbb{Q}\\).",
      "تنص مبرهنة غيرسانوف على أن إضافة انجراف للحركة البراونية لا يغير فئة القياسات المكافئة. باستخدام مشتق رادون-نيكوديم الأسّي، تتحول العملية ذات الانجراف إلى حركة براونية قياسية خالصة بدون انجراف تحت القياس الجديد \\(\\mathbb{Q}\\).",
      "The Radon-Nikodym derivative uses the exponential martingale \\(e^{-\\theta W_t - \\frac{1}{2}\\theta^2 t}\\).",
      "يستخدم مشتق رادون-نيكوديم المارتينغال الأسي لحذف حد الانجراف.")

    # 374: Reversible Markov Chains (Detailed Balance)
    q("KAUST-P3-374", "Markov Chains", "Medium",
      "A discrete-time Markov chain with transition matrix \\(P\\) is time-reversible with respect to distribution \\(\\boldsymbol{\\pi}\\) if and only if which condition holds for all states \\(i, j\\)?",
      "تكون سلسلة ماركوف عكوسة زمنياً بالنسبة للتوزيع \\(\\boldsymbol{\\pi}\\) إذا وفقط إذا تحقق أي شرط لجميع الحالات \\(i, j\\)؟",
      ["\\(\\pi_i P_{ij} = \\pi_j P_{ji}\\) (Detailed Balance)",
       "\\(\\sum_i \\pi_i P_{ij} = \\pi_j\\) (Global Balance)",
       "\\(P_{ij} = P_{ji}\\) (Symmetric transition matrix)",
       "\\(P^2 = P\\)"],
      0,
      "A Markov chain is time-reversible if running the chain forward in time is statistically indistinguishable from running it backward in time. The necessary and sufficient condition is the detailed balance equation \\(\\pi_i P_{ij} = \\pi_j P_{ji}\\) for all \\(i, j\\). Summing over \\(i\\) automatically yields the global balance equation \\(\\sum_i \\pi_i P_{ij} = \\pi_j \\sum_i P_{ji} = \\pi_j(1) = \\pi_j\\), meaning any distribution satisfying detailed balance is automatically stationary.",
      "تكون السلسلة عكوسة زمنياً إذا كان سريانها في الزمن للأمام مطابقاً إحصائياً لسريانها للخلف، والشرط اللازم والكافي هو معادلة التوازن التفصيلي \\(\\pi_i P_{ij} = \\pi_j P_{ji}\\). وبجمع المعادلة بالنسبة لـ \\(i\\) نجد أنها تحقق تلقائياً شرط التوزيع المستقر.",
      "Probability flow from \\(i\\) to \\(j\\) must equal probability flow from \\(j\\) to \\(i\\).",
      "تدفق الاحتمال من \\(i\\) إلى \\(j\\) يجب أن يطابق تدفق الاحتمال المعاكس.")

    # 375: Martingale Convergence Theorem
    q("KAUST-P3-375", "Martingales", "Hard",
      "Doob's Forward Convergence Theorem states that if \\(M_n\\) is a submartingale that is bounded in \\(L^1\\) (\\(\\sup_n \\mathbb{E}[|M_n|] < \\infty\\)), then:",
      "تنص مبرهنة دووب للتقارب على أنه إذا كان \\(M_n\\) شبه مارتينغال محدوداً في \\(L^1\\)، فإن:",
      ["\\(M_n\\) converges almost surely to a finite random variable \\(M_\\infty\\) with \\(\\mathbb{E}[|M_\\infty|] < \\infty\\)",
       "\\(M_n\\) converges to 0 almost surely",
       "\\(M_n\\) converges in \\(L^2\\)",
       "\\(M_n\\) is a constant sequence"],
      0,
      "Doob's Martingale Convergence Theorem proves that any \\(L^1\\)-bounded submartingale (or martingale) converges almost surely: \\(M_n \\xrightarrow{a.s.} M_\\infty\\), where \\(M_\\infty\\) is a finite random variable. The proof is based on Doob's upcrossing inequality, which bounds the expected number of upcrossings of any interval \\([a, b]\\), proving that oscillations must cease almost surely.",
      "تثبت نظرية دووب لتقارب المارتينغال أن أي شبه مارتينغال محدود في \\(L^1\\) يتقارب شبه مؤكداً إلى متغير عشوائي منتهٍ \\(M_\\infty\\). يستند البرهان إلى متباينة دووب للعبور الصاعد التي تبين أن التذبذبات تتوقف باحتمال 1.",
      "The proof relies on Doob's upcrossing inequality.",
      "يعتمد البرهان على متباينة دووب للعبور الصاعد.")

    # 376: Random Walk Recurrence in Different Dimensions (Polya's Theorem)
    q("KAUST-P3-376", "Random Walks", "Hard",
      "Pólya's 1921 theorem on simple symmetric random walks on the integer lattice \\(\\mathbb{Z}^d\\) states that the random walk is recurrent in which dimensions?",
      "تنص نظرية بوليا لعام 1921 على أن المشي العشوائي البسيط المتماثل على الشبكة \\(\\mathbb{Z}^d\\) يكون عائداً (recurrent) في أي أبعاد؟",
      ["\\(d = 1\\) and \\(d = 2\\) only (transient for all \\(d \\ge 3\\))",
       "\\(d = 1\\) only",
       "All dimensions \\(d \\ge 1\\)",
       "\\(d = 3\\) only"],
      0,
      "Pólya proved that a random walk on \\(\\mathbb{Z}^d\\) returns to the origin with probability 1 if and only if \\(d = 1\\) or \\(d = 2\\). In \\(d = 3\\), the probability of return is only \\(\\approx 0.3405 < 1\\), making it transient. As Shizuo Kakutani famously summarized: 'A drunk man will find his way home, but a drunk bird will get lost forever.' The proof evaluates the integral \\(\\int_{[-\\pi, \\pi]^d} \\frac{d\\mathbf{k}}{1 - \\phi(\\mathbf{k})}\\), which converges (transient) if and only if \\(d \\ge 3\\).",
      "أثبت بوليا أن المشي العشوائي يعود إلى نقطة البداية باحتمال 1 فقط في البعدين الأول والثاني \\(d = 1, 2\\). بينما في ثلاثة أبعاد وما فوق يكون عابراً (transient)، واحتمال العودة في 3D هو حوالي 0.34 فقط. يستند البرهان إلى تكامل تحويل فورييه لدالة الخطوة.",
      "Remember Kakutani's quote: drunk man (2D) returns, drunk bird (3D) gets lost.",
      "تذكر مقولة كاكوتاني الشهيرة: السائر الثمل في بعدين يعود حتماً، أما الطائر الثمل في ثلاثة أبعاد فيضيع للأبد.")

    # 377: Generator Matrix Rows Sum to Zero
    q("KAUST-P3-377", "Markov Chains", "Medium",
      "For any continuous-time Markov chain transition rate matrix (infinitesimal generator) \\(Q\\), what must the row sums \\(\\sum_j Q_{ij}\\) equal for every state \\(i\\)?",
      "لأي مصفوفة معدلات انتقال (المولد المتناهي في الصغر) \\(Q\\) لسلسلة ماركوف متصلة، ماذا يجب أن يساوي مجموع عناصر كل صف \\(\\sum_j Q_{ij}\\)؟",
      ["\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(\\lambda_i\\)"],
      0,
      "The diagonal entries of \\(Q\\) are defined as \\(Q_{ii} = -q_i = -\\sum_{j \\neq i} Q_{ij}\\), where \\(q_i\\) is the total rate of leaving state \\(i\\). Therefore, \\(\\sum_j Q_{ij} = Q_{ii} + \\sum_{j \\neq i} Q_{ij} = -q_i + q_i = 0\\). This zero row sum property guarantees that the transition probability matrix \\(P(t) = e^{Qt}\\) preserves total probability: \\(\\sum_j P_{ij}(t) = 1\\).",
      "تُعرّف العناصر القطرية بـ \\(Q_{ii} = -\\sum_{j \\neq i} Q_{ij}\\)، حيث تمثل القيمة السالبة للمعدل الكلي لمغادرة الحالة. وبالتالي فإن مجموع عناصر أي صف هو \\(Q_{ii} + \\sum_{j \\neq i} Q_{ij} = 0\\)، مما يضمن أن \\(\\sum_j P_{ij}(t) = 1\\).",
      "The diagonal entry is minus the sum of all off-diagonal entries in the row.",
      "العنصر القطري يساوي سالب مجموع العناصر خارج القطر في نفس الصف.")

    # 378: Black-Scholes Formula Drift Elimination via Martingale
    q("KAUST-P3-378", "Financial PDEs", "Hard",
      "In the risk-neutral pricing framework, the discounted stock price \\(e^{-rt} S_t\\) must be which type of process under the risk-neutral measure \\(\\mathbb{Q}\\)?",
      "في إطار التسعير المحايد للمخاطر، ما نوع العملية التي يجب أن يمثلها سعر السهم المخصوم \\(e^{-rt} S_t\\) تحت القياس \\(\\mathbb{Q}\\)؟",
      ["A martingale", "A submartingale", "A stationary Gaussian process", "A Poisson process"],
      0,
      "The First Fundamental Theorem of Asset Pricing states that a market model is free of arbitrage if and only if there exists an equivalent martingale measure \\(\\mathbb{Q}\\) under which the discounted asset price \\(\\tilde{S}_t = e^{-rt} S_t\\) is a martingale: \\(\\mathbb{E}^\\mathbb{Q}[e^{-rt} S_t \\mid \\mathcal{F}_s] = e^{-rs} S_s\\). This forces the drift of \\(S_t\\) under \\(\\mathbb{Q}\\) to be exactly the risk-free rate \\(r\\).",
      "تنص النظرية الأساسية الأولى لتسعير الأصول على أن السوق خالٍ من المراجحة (arbitrage) إذا وفقط إذا وجد قياس مكافئ \\(\\mathbb{Q}\\) يكون عنده السعر المخصوم \\(e^{-rt} S_t\\) مارتينغالاً. وهذا يفرض أن يكون معدل الانجراف مساوياً تماماً لسعر الفائدة الخالي من المخاطر \\(r\\).",
      "Arbitrage-free pricing requires discounted prices to be martingales.",
      "التسعير الخالي من المراجحة يشترط أن تكون الأسعار المخصومة مارتينغالات.")

    # 379: Poisson Process Superposition
    q("KAUST-P3-379", "Poisson Processes", "Medium",
      "If \\(N_1(t)\\) and \\(N_2(t)\\) are independent Poisson processes with rates \\(\\lambda_1\\) and \\(\\lambda_2\\), what is the distribution of the merged process \\(N(t) = N_1(t) + N_2(t)\\)?",
      "إذا كانت \\(N_1(t)\\) و \\(N_2(t)\\) عمليتي بواسون مستقلتين بمعدلي \\(\\lambda_1\\) و \\(\\lambda_2\\)، فما هو توزيع العملية المدمجة \\(N(t) = N_1(t) + N_2(t)\\)؟",
      ["A Poisson process with rate \\(\\lambda_1 + \\lambda_2\\)",
       "A Poisson process with rate \\(\\lambda_1 \\lambda_2\\)",
       "A renewal process that is no longer Poisson",
       "A Gaussian process"],
      0,
      "By the superposition property of Poisson processes, merging two independent Poisson processes with rates \\(\\lambda_1\\) and \\(\\lambda_2\\) produces a single Poisson process whose rate is the sum of the rates: \\(\\lambda = \\lambda_1 + \\lambda_2\\). The inter-arrival times are independent and exponentially distributed with parameter \\(\\lambda_1 + \\lambda_2\\).",
      "خاصية التراكب لعمليات بواسون تضمن أن دمج عمليتي بواسون مستقلتين ينتج عملية بواسون جديدة معدلها هو مجموع المعدلين \\(\\lambda_1 + \\lambda_2\\).",
      "Rates add directly when independent Poisson streams merge.",
      "تُجمع المعدلات مباشرة عند دمج تدفقات بواسون المستقلة.")

    # 380: Ehrenfest Urn Model Stationary Distribution
    q("KAUST-P3-380", "Markov Chains", "Hard",
      "In the Ehrenfest urn model for gas diffusion, \\(N\\) molecules are distributed between two urns. At each step, a molecule is chosen uniformly at random and moved to the other urn. Let \\(X_n\\) be the number of molecules in Urn 1. What is the stationary distribution of \\(X_n\\)?",
      "في نموذج إهرنفست لانتشار الغاز، يتوزع \\(N\\) جزيء بين إناءين. في كل خطوة، يُختار جزيء عشوائياً بانتظام ويُنقل للإناء الآخر. ما هو التوزيع المستقر لعدد الجزيئات في الإناء الأول؟",
      ["\\(\\text{Binomial}\\left(N, \\frac{1}{2}\\right)\\), so \\(\\pi_k = \\binom{N}{k}\\left(\\frac{1}{2}\\right)^N\\)",
       "\\(\\text{Uniform}\\left(\\{0, 1, \\dots, N\\}\\right)\\), so \\(\\pi_k = \\frac{1}{N+1}\\)",
       "\\(\\text{Poisson}(N/2)\\)",
       "\\(\\pi_k = \\frac{1}{2}\\) for \\(k = 0, N\\) and 0 elsewhere"],
      0,
      "The transition probabilities are \\(P_{k, k+1} = \\frac{N-k}{N}\\) and \\(P_{k, k-1} = \\frac{k}{N}\\). Checking the detailed balance equation \\(\\pi_k P_{k, k+1} = \\pi_{k+1} P_{k+1, k}\\): \\(\\pi_k \\frac{N-k}{N} = \\pi_{k+1} \\frac{k+1}{N} \\implies \\pi_{k+1} = \\frac{N-k}{k+1}\\pi_k\\). This is the exact recurrence relation for the binomial coefficients \\(\\binom{N}{k}\\). Normalizing gives the Binomial distribution \\(\\pi_k = \\binom{N}{k}(1/2)^N\\). In thermal equilibrium, each particle is independently in Urn 1 with probability 1/2.",
      "معادلة التوازن التفصيلي تعطي \\(\\pi_{k+1} = \\frac{N-k}{k+1}\\pi_k\\)، وهي تماماً العلاقة التكرارية لمعاملات ذات الحدين. بالمعايرة ينتج توزيع ذو الحدين \\(\\text{Binomial}(N, 1/2)\\). في الاتزان الحراري، يكون لكل جزيء احتمال متساوٍ \\(1/2\\) للتواجد في أي من الإناءين.",
      "Use detailed balance \\(\\pi_k P_{k, k+1} = \\pi_{k+1} P_{k+1, k}\\).",
      "استخدم معادلة التوازن التفصيلي لربط \\(\\pi_{k+1}\\) بـ \\(\\pi_k\\).")

    # 381 to 400: Completing questions 381-400
    # 381: Tanaka's Formula and Local Time
    q("KAUST-P3-381", "Stochastic Calculus", "Hard",
      "Tanaka's formula extends Itô's lemma to the non-differentiable absolute value function \\(|W_t|\\). What is the explicit formula for \\(|W_t|\\)?",
      "تمدد صيغة تاناكا توطئة إيتو إلى دالة القيمة المطلقة غير القابلة للاشتقاق \\(|W_t|\\). ما هي الصيغة الصريحة لـ \\(|W_t|\\)؟",
      ["\\(|W_t| = \\int_0^t \\text{sgn}(W_s) dW_s + L_t^0\\), where \\(L_t^0\\) is the Brownian local time at 0",
       "\\(|W_t| = \\int_0^t \\text{sgn}(W_s) dW_s\\)",
       "\\(|W_t| = W_t + t\\)",
       "\\(|W_t| = \\int_0^t |W_s| ds\\)"],
      0,
      "Because \\(f(x) = |x|\\) has weak derivative \\(f'(x) = \\text{sgn}(x)\\) and second derivative in the sense of distributions \\(f''(x) = 2\\delta(x)\\), the formal Itô expansion gives \\(d|W_t| = \\text{sgn}(W_t) dW_t + \\frac{1}{2}(2\\delta(W_t))dt = \\text{sgn}(W_t) dW_t + dL_t^0\\). Integrating yields Tanaka's formula: \\(|W_t| = \\int_0^t \\text{sgn}(W_s) dW_s + L_t^0\\), where \\(L_t^0 = \\lim_{\\epsilon \\to 0} \\frac{1}{2\\epsilon}\\int_0^t \\mathbb{I}_{\\{|W_s| < \\epsilon\\}} ds\\) is the local time spent by the Brownian motion at the origin.",
      "بما أن المشتق الثاني للقيمة المطلقة بمفهوم التوزيعات هو \\(2\\delta(x)\\)، فإن صيغة إيتو تعطي \\(d|W_t| = \\text{sgn}(W_t)dW_t + dL_t^0\\). بالمكاملة نحصل على صيغة تاناكا، حيث \\(L_t^0\\) هو الزمن المحلي لبراون عند الصفر والذي يقيس كثافة مكوث المسار عند نقطة الأصل.",
      "The second derivative of \\(|x|\\) is \\(2\\delta(x)\\), which produces local time.",
      "المشتق الثاني لدالة القيمة المطلقة هو ضعف دالة ديراك، مما يولد الزمن المحلي.")

    # 382: Markov Chain Mixing Time
    q("KAUST-P3-382", "Markov Chains", "Hard",
      "For an ergodic finite Markov chain, the total variation mixing time \\(t_{\\text{mix}}(\\epsilon)\\) is closely bounded by the spectral gap \\(\\gamma = 1 - \\lambda_2\\), where \\(\\lambda_2\\) is the second largest eigenvalue of \\(P\\). How does the mixing time scale with the spectral gap \\(\\gamma\\)?",
      "لسلسلة ماركوف منتهية، يرتبط زمن الخلط بالتباين الكلي بفجوة الطيف \\(\\gamma = 1 - \\lambda_2\\). كيف يتناسب زمن الخلط مع فجوة الطيف \\(\\gamma\\)؟",
      ["\\(t_{\\text{mix}} \\sim O\\left(\\frac{1}{\\gamma}\\right)\\) (inversely proportional to the spectral gap)",
       "\\(t_{\\text{mix}} \\sim O(\\gamma)\\)",
       "\\(t_{\\text{mix}} \\sim O(e^\\gamma)\\)",
       "\\(t_{\\text{mix}}\\) is independent of \\(\\gamma\\)"],
      0,
      "The rate of convergence of \\(P^t\\) to the stationary distribution \\(\\boldsymbol{\\pi}\\) is governed by the second largest eigenvalue modulus \\(|\\lambda_2|^t = (1 - \\gamma)^t \\approx e^{-\\gamma t}\\). For the total variation distance to fall below \\(\\epsilon\\), we require \\(e^{-\\gamma t} \\le \\epsilon \\implies t \\ge \\frac{1}{\\gamma}\\ln(1/\\epsilon)\\). Hence, the relaxation time is \\(t_{\\text{rel}} = 1/\\gamma\\), and the mixing time is proportional to \\(1/\\gamma\\). A larger spectral gap implies much faster mixing.",
      "معدل تقارب السلسلة نحو التوزيع المستقر تحدده القيمة الذاتية الثانية: \\(|\\lambda_2|^t = (1-\\gamma)^t \\approx e^{-\\gamma t}\\). لكي تصبح المسافة أقل من \\(\\epsilon\\)، نحتاج \\(t \\sim \\frac{1}{\\gamma}\\ln(1/\\epsilon)\\). إذن زمن الخلط يتناسب عكساً مع فجوة الطيف \\(1/\\gamma\\).",
      "Convergence goes as \\((1-\\gamma)^t \\approx e^{-\\gamma t}\\).",
      "التقارب الأسي يتم بمعدل \\(e^{-\\gamma t}\\).")

    # 383: Wald's Identity for Stopping Times
    q("KAUST-P3-383", "Martingales", "Medium",
      "Wald's First Identity states that if \\(X_1, X_2, \\dots\\) are i.i.d. random variables with finite expectation \\(\\mathbb{E}[X] = \\mu\\), and \\(T\\) is a stopping time with \\(\\mathbb{E}[T] < \\infty\\), then the sum \\(S_T = \\sum_{i=1}^T X_i\\) satisfies:",
      "تنص متطابقة فالد الأولى على أنه إذا كانت \\(X_i\\) متغيرات عشوائية مستقلة ومتطابقة التوزيع وكان \\(T\\) زمن توقف بمتوسط منتهٍ، فإن المجموع \\(S_T\\) يحقق:",
      ["\\(\\mathbb{E}[S_T] = \\mu \\mathbb{E}[T]\\)",
       "\\(\\mathbb{E}[S_T] = \\mu + \\mathbb{E}[T]\\)",
       "\\(\\mathbb{E}[S_T] = \\mu^2 \\mathbb{E}[T]\\)",
       "\\(\\mathbb{E}[S_T] = \\frac{\\mu}{\\mathbb{E}[T]}\\)"],
      0,
      "Wald's Identity is proven by noting that \\(M_n = S_n - n\\mu\\) is a martingale with \\(M_0 = 0\\). Applying the Optional Stopping Theorem to \\(M_n\\) gives \\(\\mathbb{E}[M_T] = \\mathbb{E}[S_T - T\\mu] = 0 \\implies \\mathbb{E}[S_T] = \\mu \\mathbb{E}[T]\\).",
      "تُثبت متطابقة فالد بملاحظة أن العملية \\(M_n = S_n - n\\mu\\) هي مارتينغال مع \\(M_0 = 0\\). بتطبيق نظرية الإيقاف الاختياري نجد \\(\\mathbb{E}[S_T - T\\mu] = 0\\)، ومنه \\(\\mathbb{E}[S_T] = \\mu \\mathbb{E}[T]\\).",
      "Apply the optional stopping theorem to the martingale \\(S_n - n\\mu\\).",
      "طبق نظرية الإيقاف الاختياري على المارتينغال \\(S_n - n\\mu\\).")

    # 384: Wald's Second Identity
    q("KAUST-P3-384", "Martingales", "Hard",
      "Under the same conditions with \\(\\mathbb{E}[X_i] = 0\\) and \\(\\text{Var}(X_i) = \\sigma^2 < \\infty\\), Wald's Second Identity asserts that:",
      "تحت نفس الشروط السابقة مع \\(\\mathbb{E}[X_i] = 0\\) وتباين \\(\\sigma^2\\)، تنص متطابقة فالد الثانية على أن:",
      ["\\(\\mathbb{E}[S_T^2] = \\sigma^2 \\mathbb{E}[T]\\)",
       "\\(\\mathbb{E}[S_T^2] = \\sigma \\mathbb{E}[T]\\)",
       "\\(\\mathbb{E}[S_T^2] = \\sigma^2 (\\mathbb{E}[T])^2\\)",
       "\\(\\mathbb{E}[S_T^2] = 0\\)"],
      0,
      "When \\(\\mathbb{E}[X_i] = 0\\), the process \\(M_n = S_n^2 - n\\sigma^2\\) is a martingale with \\(M_0 = 0\\). Applying the Optional Stopping Theorem yields \\(\\mathbb{E}[S_T^2 - T\\sigma^2] = 0 \\implies \\mathbb{E}[S_T^2] = \\sigma^2 \\mathbb{E}[T]\\).",
      "عندما يكون المتوسط صفراً، فإن العملية \\(M_n = S_n^2 - n\\sigma^2\\) تشكل مارتينغالاً. بتطبيق نظرية الإيقاف الاختياري نجد \\(\\mathbb{E}[S_T^2 - T\\sigma^2] = 0\\)، ومنه \\(\\mathbb{E}[S_T^2] = \\sigma^2 \\mathbb{E}[T]\\).",
      "Consider the martingale \\(S_n^2 - n\\sigma^2\\).",
      "تأمل المارتينغال التربيعي \\(S_n^2 - n\\sigma^2\\).")

    # 385: Cameron-Martin Theorem
    q("KAUST-P3-385", "Stochastic Calculus", "Hard",
      "The Cameron-Martin theorem states that shifting a Wiener measure on \\(C([0, 1])\\) by a deterministic function \\(h(t)\\) produces an equivalent measure (mutually absolutely continuous) if and only if \\(h\\) belongs to which space?",
      "تنص نظرية كاميرون-مارتن على أن إزاحة قياس فينر بدالة حتمية \\(h(t)\\) ينتج قياساً مكافئاً إذا وفقط إذا كانت \\(h\\) تنتمي إلى أي فضاء؟",
      ["The Cameron-Martin space \\(H^1([0, 1]) = \\{h : h(0)=0, h' \\in L^2([0, 1])\\}\\)",
       "The space of continuous functions \\(C([0, 1])\\)",
       "The Lebesgue space \\(L^2([0, 1])\\)",
       "The space of bounded variation functions"],
      0,
      "The Cameron-Martin theorem states that the translated measure \\(\\mu_h(A) = \\mu(A - h)\\) is absolutely continuous with respect to the Wiener measure \\(\\mu\\) if and only if \\(h\\) is absolutely continuous with \\(h(0) = 0\\) and square-integrable derivative \\(h' \\in L^2([0, 1])\\) (finite Dirichlet energy \\(\\int_0^1 (h')^2 dt < \\infty\\)). For any \\(h\\) outside this space, the shifted measure is mutually singular (orthogonal) to the Wiener measure.",
      "تنص نظرية كاميرون-مارتن على أن القياس المزاح يكون مكافئاً لقياس فينر إذا وفقط إذا كانت الدالة \\(h\\) تنتمي لفضاء كاميرون-مارتن، أي دالة متصلة مطلقاً مع \\(h(0) = 0\\) ومشتقها ينتمي لـ \\(L^2\\). لأي دالة خارج هذا الفضاء، يكون القياسان منفصلين تماماً (متعامدين).",
      "The function must be in the Sobolev space \\(H^1\\) with finite energy \\(\\int (h')^2 dt < \\infty\\).",
      "يجب أن تمتلك الدالة طاقة مشتقة منتهية في فضاء سوبوليف \\(H^1\\).")

    # 386: Renewal Function Asymptotics (Elementary Renewal Theorem)
    q("KAUST-P3-386", "Renewal Theory", "Medium",
      "The Elementary Renewal Theorem states that for a renewal process with i.i.d. inter-arrival times having mean \\(\\mu < \\infty\\), the expected number of renewals \\(m(t) = \\mathbb{E}[N(t)]\\) satisfies:",
      "تنص النظرية الابتدائية للتجديد على أن متوسط عدد التجديدات \\(m(t) = \\mathbb{E}[N(t)]\\) يحقق:",
      ["\\(\\lim_{t \\to \\infty} \\frac{m(t)}{t} = \\frac{1}{\\mu}\\)",
       "\\(\\lim_{t \\to \\infty} \\frac{m(t)}{t} = \\mu\\)",
       "\\(\\lim_{t \\to \\infty} m(t) = \\mu\\)",
       "\\(\\lim_{t \\to \\infty} \\frac{m(t)}{t^2} = \\frac{1}{2\\mu}\\)"],
      0,
      "The Elementary Renewal Theorem establishes that as \\(t \\to \\infty\\), \\(\\frac{m(t)}{t} \\to \\frac{1}{\\mu}\\). Intuitively, if events occur on average every \\(\\mu\\) units of time, the long-term rate of events per unit time must be \\(1/\\mu\\). Blackwell's renewal theorem further strengthens this to \\(\\lim_{t\\to\\infty} [m(t + h) - m(t)] = h/\\mu\\).",
      "تثبت النظرية الابتدائية للتجديد أن \\(\\lim_{t\\to\\infty} \\frac{m(t)}{t} = \\frac{1}{\\mu}\\). هندسياً، إذا كان متوسط الزمن بين الأحداث هو \\(\\mu\\)، فإن المعدل طويل الأمد لعدد الأحداث في وحدة الزمن هو مقلوب المتوسط \\(1/\\mu\\).",
      "The rate of events per unit time is the reciprocal of the mean inter-arrival time.",
      "معدل الأحداث في وحدة الزمن هو مقلوب متوسط زمن الوصول البيني.")

    # 387: Blackwell's Renewal Theorem
    q("KAUST-P3-387", "Renewal Theory", "Hard",
      "For a non-lattice renewal process with mean inter-arrival time \\(\\mu\\), Blackwell's renewal theorem states that for any fixed \\(h > 0\\):",
      "لعملية تجديد غير شبكية بمتوسط زمن بيني \\(\\mu\\)، تنص نظرية بلاكويل للتجديد على أنه لأي \\(h > 0\\) ثابت:",
      ["\\(\\lim_{t \\to \\infty} [m(t + h) - m(t)] = \\frac{h}{\\mu}\\)",
       "\\(\\lim_{t \\to \\infty} [m(t + h) - m(t)] = 0\\)",
       "\\(\\lim_{t \\to \\infty} [m(t + h) - m(t)] = h \\mu\\)",
       "\\(\\lim_{t \\to \\infty} [m(t + h) - m(t)] = \\infty\\)"],
      0,
      "Blackwell's renewal theorem states that for any non-lattice distribution with mean \\(\\mu\\), \\(\\lim_{t\\to\\infty} [m(t+h) - m(t)] = \\frac{h}{\\mu}\\). This shows that far into the future, the renewal process becomes locally stationary with constant intensity \\(1/\\mu\\) in any time window of fixed length \\(h\\).",
      "تنص نظرية بلاكويل للتجديد على أن متوسط عدد الأحداث في أي فترة زمنية طولها \\(h\\) يتقارب عندما \\(t \\to \\infty\\) إلى \\(h/\\mu\\). هذا يوضح أن عملية التجديد تصبح مستقرة موضعياً على المدى البعيد.",
      "In a window of length \\(h\\), the expected number of events approaches \\(h/\\mu\\).",
      "في فترة طولها \\(h\\)، يقترب عدد الأحداث المتوقع من \\(h/\\mu\\).")

    # 388: Birth-Death Process Stationary Condition
    q("KAUST-P3-388", "Markov Chains", "Hard",
      "For a continuous-time birth-death process on \\(\\{0, 1, 2, \\dots\\}\\) with birth rates \\(\\lambda_n\\) and death rates \\(\\mu_n > 0\\), what is the necessary and sufficient condition for a stationary distribution to exist?",
      "لعملية ولادة وموت متصلة الزمن مع معدلات ولادة \\(\\lambda_n\\) ومعدلات موت \\(\\mu_n > 0\\)، ما هو الشرط اللازم والكافي لوجود توزيع مستقر؟",
      ["\\(\\sum_{n=1}^\\infty \\frac{\\lambda_0 \\lambda_1 \\dots \\lambda_{n-1}}{\\mu_1 \\mu_2 \\dots \\mu_n} < \\infty\\)",
       "\\(\\lambda_n < \\mu_n\\) for all \\(n\\)",
       "\\(\\sum_{n=1}^\\infty \\frac{\\mu_n}{\\lambda_n} < \\infty\\)",
       "\\(\\lim_{n\\to\\infty} \\lambda_n = 0\\)"],
      0,
      "By the detailed balance equations: \\(\\lambda_{n-1}\\pi_{n-1} = \\mu_n \\pi_n \\implies \\pi_n = \\frac{\\lambda_0 \\dots \\lambda_{n-1}}{\\mu_1 \\dots \\mu_n} \\pi_0\\). For the probabilities to sum to 1, we require \\(\\sum_{n=0}^\\infty \\pi_n = \\pi_0 \\left(1 + \\sum_{n=1}^\\infty \\prod_{i=1}^n \\frac{\\lambda_{i-1}}{\\mu_i}\\right) = 1\\). Thus a stationary distribution exists if and only if the series \\(S = \\sum_{n=1}^\\infty \\frac{\\lambda_0 \\dots \\lambda_{n-1}}{\\mu_1 \\dots \\mu_n} < \\infty\\), giving \\(\\pi_0 = \\frac{1}{1 + S} > 0\\).",
      "من معادلات التوازن التفصيلي نجد أن كل احتمال يكتب بدلالة \\(\\pi_0\\) كـ \\(\\pi_n = \\pi_0 \\prod_{i=1}^n \\frac{\\lambda_{i-1}}{\\mu_i}\\). لكي يكون المجموع قابلاً للمعايرة (يساوي 1)، يجب أن تكون المتسلسلة متقاربة: \\(\\sum_{n=1}^\\infty \\prod \\frac{\\lambda_{i-1}}{\\mu_i} < \\infty\\).",
      "Check the convergence of the series expressing \\(\\sum \\pi_n\\) in terms of \\(\\pi_0\\).",
      "افحص تقارب متسلسلة التوازن التفصيلي المعبرة عن الاحتمالات.")

    # 389: Pure Birth (Yule-Furry) Process
    q("KAUST-P3-389", "Markov Chains", "Medium",
      "In a pure birth Yule-Furry process where each individual splits into two at rate \\(\\lambda\\) (so \\(\\lambda_n = n\\lambda\\)) starting with \\(X(0) = 1\\), what is the probability distribution of population size \\(X(t)\\)?",
      "في عملية يول-فوري للولادة الخالصة حيث \\(\\lambda_n = n\\lambda\\) بدءاً من فرد واحد \\(X(0) = 1\\)، ما هو التوزيع الاحتمالي لحجم العشيرة \\(X(t)\\)؟",
      ["\\(\\text{Geometric}(p)\\) with \\(p = e^{-\\lambda t}\\) on \\(\\{1, 2, 3, \\dots\\}\\)",
       "\\(\\text{Poisson}(\\lambda t)\\)",
       "\\(\\text{Binomial}(n, e^{-\\lambda t})\\)",
       "\\(\\text{Exponential}(\\lambda t)\\)"],
      0,
      "The differential-difference equations for the Yule process are \\(P_n'(t) = (n-1)\\lambda P_{n-1}(t) - n\\lambda P_n(t)\\) with \\(P_1(0) = 1\\). Solving via probability generating functions yields \\(P_n(t) = e^{-\\lambda t}(1 - e^{-\\lambda t})^{n-1}\\) for \\(n \\ge 1\\). This is a Geometric distribution with parameter \\(p = e^{-\\lambda t}\\) on \\(\\{1, 2, \\dots\\}\\), with mean \\(\\mathbb{E}[X(t)] = e^{\\lambda t}\\).",
      "المعادلات التفاضلية لعملية يول تعطي بالحل التكراري أو بالدوال المولدة: \\(P_n(t) = e^{-\\lambda t}(1 - e^{-\\lambda t})^{n-1}\\) لـ \\(n \\ge 1\\). هذا هو التوزيع الهندسي بمعلمة النجاح \\(p = e^{-\\lambda t}\\)، ومتوسط حجم العشيرة ينمو أسياً: \\(\\mathbb{E}[X(t)] = e^{\\lambda t}\\).",
      "Solve the linear differential system for \\(P_n(t)\\) or use generating functions.",
      "حل النظام التفاضلي أو استخدم الدالة المولدة للاحتمالات.")

    # 390: Geometric Brownian Motion Martingale Property
    q("KAUST-P3-390", "Stochastic Calculus", "Hard",
      "For what value of parameter \\(\\alpha\\) is the process \\(M_t = \\exp(\\sigma W_t - \\alpha t)\\) a martingale with respect to the Brownian filtration?",
      "لأي قيمة للمعلمة \\(\\alpha\\) تكون العملية \\(M_t = \\exp(\\sigma W_t - \\alpha t)\\) مارتينغالاً بالنسبة لمرشح الحركة البراونية؟",
      ["\\(\\alpha = \\frac{1}{2}\\sigma^2\\)", "\\(\\alpha = \\sigma^2\\)", "\\(\\alpha = 0\\)", "\\(\\alpha = \\frac{1}{4}\\sigma^2\\)"],
      0,
      "Apply Itô's formula to \\(f(W_t, t) = e^{\\sigma W_t - \\alpha t}\\): \\(dM_t = (-\\alpha M_t) dt + \\sigma M_t dW_t + \\frac{1}{2}\\sigma^2 M_t dt = M_t\\left(\\frac{1}{2}\\sigma^2 - \\alpha\\right)dt + \\sigma M_t dW_t\\). For \\(M_t\\) to be a martingale, the \\(dt\\) drift term must vanish identically: \\(\\frac{1}{2}\\sigma^2 - \\alpha = 0 \\implies \\alpha = \\frac{1}{2}\\sigma^2\\). The resulting process \\(M_t = e^{\\sigma W_t - \\frac{1}{2}\\sigma^2 t}\\) is the famous Doléans-Dade exponential martingale.",
      "بتطبيق صيغة إيتو على \\(M_t\\): \\(dM_t = M_t(\\frac{1}{2}\\sigma^2 - \\alpha)dt + \\sigma M_t dW_t\\). لكي تكون العملية مارتينغالاً، يجب أن ينعدم حد الانجراف \\(dt\\)، أي \\(\\frac{1}{2}\\sigma^2 - \\alpha = 0\\)، ومنه \\(\\alpha = \\frac{1}{2}\\sigma^2\\). هذا هو مارتينغال دوليان-داد الأسي.",
      "Require the \\(dt\\) coefficient in Itô's expansion to be zero.",
      "اشترط انعدام معامل \\(dt\\) في تفاضل إيتو.")

    # 391: Stationary Distribution for Random Walk on a Graph
    q("KAUST-P3-391", "Markov Chains", "Medium",
      "A simple random walk on an undirected connected graph \\(G = (V, E)\\) moves from vertex \\(u\\) to any neighbor with probability \\(1/\\deg(u)\\). What is the stationary probability \\(\\pi_u\\) of vertex \\(u\\)?",
      "مشية عشوائية بسيطة على رسم بياني غير موجه ومتصل \\(G = (V, E)\\) تنتقل من الرأس \\(u\\) إلى أي جار باحتمال \\(1/\\deg(u)\\). ما هو الاحتمال المستقر \\(\\pi_u\\) للرأس \\(u\\)؟",
      ["\\(\\pi_u = \\frac{\\deg(u)}{2|E|}\\)",
       "\\(\\pi_u = \\frac{1}{|V|}\\)",
       "\\(\\pi_u = \\frac{\\deg(u)}{|V|}\\)",
       "\\(\\pi_u = \\frac{1}{\\deg(u)}\\)"],
      0,
      "Test detailed balance with \\(\\pi_u = c \\deg(u)\\): \\(\\pi_u P_{uv} = (c \\deg(u))\\frac{1}{\\deg(u)} = c\\) for every edge \\((u, v) \\in E\\). Symmetrically, \\(\\pi_v P_{vu} = (c \\deg(v))\\frac{1}{\\deg(v)} = c\\). Thus \\(\\pi_u P_{uv} = \\pi_v P_{vu}\\) holds for all edges, so the walk is reversible. Normalizing: \\(\\sum_{u \\in V} \\pi_u = c \\sum_{u \\in V} \\deg(u) = c (2|E|) = 1 \\implies c = \\frac{1}{2|E|}\\). Thus \\(\\pi_u = \\frac{\\deg(u)}{2|E|}\\).",
      "باختبار التوازن التفصيلي بفرض \\(\\pi_u = c \\deg(u)\\): نجد أن \\(\\pi_u P_{uv} = c\\) و \\(\\pi_v P_{vu} = c\\)، فالتوازن التفصيلي محقق لكل حافة. وبالمعايرة مع استخدام مبرهنة المصافحة \\(\\sum \\deg(u) = 2|E|\\)، نجد \\(c = 1/(2|E|)\\)، إذن \\(\\pi_u = \\frac{\\deg(u)}{2|E|}\\).",
      "Use the handshaking lemma \\(\\sum_{u \\in V} \\deg(u) = 2|E|\\).",
      "استخدم مبرهنة المصافحة لمجموع درجات رؤوس الرسم البياني.")

    # 392: Stratonovich vs Itô Integral
    q("KAUST-P3-392", "Stochastic Calculus", "Hard",
      "What is the relationship between the Stratonovich integral \\(\\int_0^T W_t \\circ dW_t\\) and the Itô integral \\(\\int_0^T W_t dW_t\\)?",
      "ما هي العلاقة بين تكامل ستراتونوفيتش \\(\\int W_t \\circ dW_t\\) وتكامل إيتو \\(\\int W_t dW_t\\)؟",
      ["\\(\\int_0^T W_t \\circ dW_t = \\int_0^T W_t dW_t + \\frac{1}{2}T\\)",
       "\\(\\int_0^T W_t \\circ dW_t = \\int_0^T W_t dW_t - \\frac{1}{2}T\\)",
       "\\(\\int_0^T W_t \\circ dW_t = \\int_0^T W_t dW_t\\)",
       "\\(\\int_0^T W_t \\circ dW_t = 2\\int_0^T W_t dW_t\\)"],
      0,
      "The Stratonovich integral evaluates the integrand at the midpoint of each interval: \\(W_{(t_i + t_{i+1})/2}\\). By Taylor expansion, \\(W_{(t_i + t_{i+1})/2} = W_{t_i} + \\frac{1}{2}\\Delta W_i + \\dots\\). Multiplying by \\(\\Delta W_i\\): \\(W_{(t_i + t_{i+1})/2}\\Delta W_i = W_{t_i}\\Delta W_i + \\frac{1}{2}(\\Delta W_i)^2\\). Summing yields \\(\\int_0^T W_t \\circ dW_t = \\int_0^T W_t dW_t + \\frac{1}{2}[W, W]_T = \\int_0^T W_t dW_t + \\frac{1}{2}T\\). Note that the Stratonovich integral obeys standard ordinary calculus chain rules: \\(\\int_0^T W_t \\circ dW_t = \\frac{1}{2}W_T^2\\).",
      "يقيم تكامل ستراتونوفيتش الدالة عند نقطة المنتصف لكل فترة تجزئة. بنشر تايلور يظهر حد تصحيح إضافي يساوي نصف التغير التربيعي: \\(\\frac{1}{2}[W, W]_T = \\frac{1}{2}T\\). بالتالي فإن تكامل ستراتونوفيتش يساوي تكامل إيتو زائد \\(T/2\\)، وهو يتبع قواعد التفاضل والتكامل العادية: \\(\\int W \\circ dW = \\frac{1}{2}W_T^2\\).",
      "The midpoint evaluation adds a term equal to \\(\\frac{1}{2}\\) times the quadratic variation \\(T\\).",
      "التقييم عند نقطة المنتصف يضيف نصف التغير التربيعي \\(T/2\\).")

    # 393: Ehrenfest Urn Time Reversibility
    q("KAUST-P3-393", "Markov Chains", "Medium",
      "In statistical mechanics, the Ehrenfest urn model demonstrated that a microscopic time-reversible Markov chain can exhibit macroscopic irreversible behavior (entropy increase). What resolves this apparent paradox?",
      "في الميكانيكا الإحصائية، بين نموذج إهرنفست كيف يمكن لسلسلة ماركوف عكوسة مجهرياً أن تبدي سلوكاً غير عكوس عيانياً (ازدياد الإنتروبيا). ما الذي يحل هذا التناقض الظاهري؟",
      ["The Poincaré recurrence time from an empty urn is astronomically large (\\(2^N\\) steps), making recurrence physically unobservable for large \\(N\\)",
       "The Ehrenfest model is actually not time-reversible",
       "Entropy does not increase in the Ehrenfest model",
       "The chain is absorbing"],
      0,
      "The Ehrenfest chain is mathematically time-reversible and recurrent: starting with all \\(N\\) particles in Urn 1, the system is mathematically guaranteed to return to this state with probability 1. However, by Kac's lemma, the expected return time to state \\(0\\) is \\(1/\\pi_0 = 2^N\\) steps. For macroscopic \\(N \\sim 10^{23}\\), \\(2^{10^{23}}\\) vastly exceeds the age of the universe, resolving Boltzmann's paradox.",
      "السلسلة عكوسة رياضياً وعائدة باحتمال 1، لكن حسب توطئة كاك، متوسط زمن العودة إلى الحالة الابتدائية هو \\(1/\\pi_0 = 2^N\\) خطوة. عندما يكون \\(N\\) كبيراً (من رتبة أفوغادرو)، يصبح زمن العودة فلكياً ويتجاوز عمر الكون، مما يفسر الاتجاه العياني غير العكوس نحو الاتزان.",
      "Consider the expected return time \\(1/\\pi_0 = 2^N\\).",
      "تأمل زمن العودة المتوقع \\(1/\\pi_0 = 2^N\\).")

    # 394: Feynman-Kac Formula
    q("KAUST-P3-394", "Stochastic Calculus", "Hard",
      "The Feynman-Kac formula establishes a profound link between PDEs and stochastic processes. It states that the solution to the parabolic PDE \\(u_t + \\mu(x) u_x + \\frac{1}{2}\\sigma^2(x) u_{xx} - V(x) u = 0\\) with terminal condition \\(u(x, T) = g(x)\\) is represented as:",
      "تنشئ صيغة فاينمان-كاك رابطاً عميقاً بين المعادلات التفاضلية الجزئية والعمليات العشوائية. تنص على أن حل المعادلة المكافئة مع الشرط النهائي \\(u(x, T) = g(x)\\) يُمثل بـ:",
      ["\\(u(x, t) = \\mathbb{E}\\left[\\exp\\left(-\\int_t^T V(X_s) ds\\right) g(X_T) \\,\\middle|\\, X_t = x\\right]\\)",
       "\\(u(x, t) = \\mathbb{E}[g(X_T) \\mid X_t = x]\\)",
       "\\(u(x, t) = g(x) e^{-V(x)(T-t)}\\)",
       "\\(u(x, t) = \\int_t^T \\mathbb{E}[V(X_s)] ds\\)"],
      0,
      "By applying Itô's lemma to the process \\(Y_s = \\exp\\left(-\\int_t^s V(X_u) du\\right) u(X_s, s)\\) where \\(dX_s = \\mu(X_s) ds + \\sigma(X_s) dW_s\\), the drift of \\(Y_s\\) is zero precisely because \\(u\\) satisfies the PDE. Thus \\(Y_s\\) is a martingale. Equating \\(Y_t = u(x, t)\\) with \\(\\mathbb{E}[Y_T \\mid X_t = x]\\) yields the Feynman-Kac representation formula.",
      "بتطبيق صيغة إيتو على الدالة المخصومة \\(Y_s = e^{-\\int V du} u(X_s, s)\\)، ينعدم حد الانجراف تماماً بفضل تحقيق \\(u\\) للمعادلة التفاضلية الجزئية، فتصبح العملية مارتينغالاً. بمساواة القيمة عند \\(t\\) بتوقع القيمة النهائية عند \\(T\\) نحصل على صيغة فاينمان-كاك.",
      "Discounting by the potential \\(V(x)\\) appears as an exponential factor \\(\\exp(-\\int V ds)\\) inside the expectation.",
      "يظهر التخصيم بجهد \\(V(x)\\) كمعامل أسي داخل التوقع الرياضي.")

    # 395: Renewal Equation
    q("KAUST-P3-395", "Renewal Theory", "Hard",
      "The renewal function \\(m(t) = \\mathbb{E}[N(t)]\\) for inter-arrival distribution \\(F(t)\\) satisfies which fundamental renewal integral equation?",
      "تحقق دالة التجديد \\(m(t) = \\mathbb{E}[N(t)]\\) لدالة التوزيع البيني \\(F(t)\\) أي معادلة تكاملية أساسية للتجديد؟",
      ["\\(m(t) = F(t) + \\int_0^t m(t - s) dF(s)\\)",
       "\\(m(t) = \\int_0^t F(s) ds\\)",
       "\\(m(t) = F(t) + m(t)^2\\)",
       "\\(m(t) = \\int_0^t e^{-s} m(s) ds\\)"],
      0,
      "Condition on the time \\(S_1 = s\\) of the first renewal: if \\(s > t\\), no renewal has occurred by time \\(t\\) (0 renewals). If \\(s \\le t\\), exactly 1 renewal has occurred, and by the renewal property, the process restarts from that point, yielding an expected \\(m(t - s)\\) additional renewals. Integrating over all possible values of \\(s\\): \\(m(t) = \\int_0^t (1 + m(t - s)) dF(s) = \\int_0^t dF(s) + \\int_0^t m(t - s) dF(s) = F(t) + (m * F)(t)\\).",
      "بالتكييف على زمن التجديد الأول \\(S_1 = s\\): إذا كان \\(s \\le t\\) فقد وقع تجديد واحد وتستأنف العملية من جديد لتعطي متوسط \\(m(t-s)\\) تجديداً إضافياً. بالمكاملة على جميع الأزمنة نجد معادلة التجديد التكاملية: \\(m(t) = F(t) + \\int_0^t m(t-s) dF(s)\\).",
      "Condition on the time of the very first renewal event.",
      "كيف الاحتمال على زمن وقوع أول حدث تجديد.")

    # 396: Martingale Property of Brownian Motion Squared minus Time
    q("KAUST-P3-396", "Martingales", "Medium",
      "For a standard Brownian motion \\(W_t\\), which of the following is a martingale?",
      "لحركة براونية قياسية \\(W_t\\)، أي من العمليات التالية تمثل مارتينغالاً؟",
      ["\\(M_t = W_t^2 - t\\)", "\\(M_t = W_t^2\\)", "\\(M_t = W_t^2 + t\\)", "\\(M_t = W_t^3 - t\\)"],
      0,
      "For \\(s < t\\): \\(\\mathbb{E}[W_t^2 - t \\mid \\mathcal{F}_s] = \\mathbb{E}[(W_s + (W_t - W_s))^2 - t \\mid \\mathcal{F}_s] = \\mathbb{E}[W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2 - t \\mid \\mathcal{F}_s]\\). Since increments are independent and have zero mean: \\(W_s^2 + 0 + (t - s) - t = W_s^2 - s\\). Thus \\(\\mathbb{E}[W_t^2 - t \\mid \\mathcal{F}_s] = W_s^2 - s\\), proving that \\(W_t^2 - t\\) is a martingale.",
      "بحساب التوقع الشرطي لـ \\(W_t^2 - t\\) بالاستفادة من استقلال الزيادات وتوقعها الصفري وتباينها \\(t - s\\): نجد \\(W_s^2 + (t - s) - t = W_s^2 - s\\). هذا يثبت أن العملية \\(W_t^2 - t\\) هي مارتينغال.",
      "Expand \\(W_t = W_s + (W_t - W_s)\\) and use \\(\\mathbb{E}[(W_t - W_s)^2] = t - s\\).",
      "فك \\(W_t\\) إلى \\(W_s + (W_t - W_s)\\) واستخدم خاصية تباين الزيادات.")

    # 397: Continuous-Time Poisson Generator
    q("KAUST-P3-397", "Poisson Processes", "Medium",
      "A Poisson process \\(N(t)\\) with rate \\(\\lambda\\) viewed as a continuous-time Markov chain on \\(\\{0, 1, 2, \\dots\\}\\) has what non-zero transition rates in its generator matrix \\(Q\\)?",
      "عملية بواسون بمعدل \\(\\lambda\\) إذا نُظر إليها كسلسلة ماركوف متصلة الزمن، فما هي معدلات الانتقال غير الصفرية في مصفوفة التوليد \\(Q\\)؟",
      ["\\(Q_{i, i+1} = \\lambda\\) and \\(Q_{ii} = -\\lambda\\) for all \\(i \\ge 0\\)",
       "\\(Q_{i, i+1} = i\\lambda\\) and \\(Q_{ii} = -i\\lambda\\)",
       "\\(Q_{i, i-1} = \\lambda\\) and \\(Q_{ii} = -\\lambda\\)",
       "\\(Q_{ij} = \\lambda\\) for all \\(j > i\\)"],
      0,
      "In a Poisson process, transitions only occur from state \\(i\\) to state \\(i + 1\\) (pure birth with constant rate), with rate \\(Q_{i, i+1} = \\lambda\\). Since the total rate of leaving state \\(i\\) is \\(\\lambda\\), the diagonal entry must be \\(Q_{ii} = -\\lambda\\). All other entries are zero.",
      "في عملية بواسون، الانتقال الوحيد الممكن هو زيادة بمقدار 1 بمعدل ثابت \\(\\lambda\\)، إذن \\(Q_{i, i+1} = \\lambda\\). ولكي يكون مجموع عناصر الصف صفراً، فإن العنصر القطري هو \\(Q_{ii} = -\\lambda\\).",
      "The rate of jumping from state \\(i\\) to \\(i+1\\) is constant \\(\\lambda\\).",
      "معدل القفز من الحالة \\(i\\) إلى \\(i+1\\) هو الثابت \\(\\lambda\\).")

    # 398: Gambler's Ruin with Unfair Coin
    q("KAUST-P3-398", "Martingales", "Hard",
      "In the Gambler's Ruin problem with starting wealth \\(k\\), target \\(N\\), and win probability \\(p \\neq 1/2\\) (where \\(q = 1 - p\\)), what is the probability of reaching \\(N\\) before going broke?",
      "في مسألة خراب المقامر برصيد ابتدائي \\(k\\) وهدف \\(N\\) واحتمال فوز \\(p \\neq 1/2\\)، ما هو احتمال الوصول إلى \\(N\\) قبل الإفلاس؟",
      ["\\(\\frac{1 - (q/p)^k}{1 - (q/p)^N}\\)",
       "\\(\\frac{k}{N}\\)",
       "\\(\\left(\\frac{p}{q}\\right)^{N-k}\\)",
       "\\(\\frac{(p/q)^k - 1}{(p/q)^N + 1}\\)"],
      0,
      "For \\(p \\neq 1/2\\), the process \\(M_n = (q/p)^{X_n}\\) is a martingale because \\(\\mathbb{E}[(q/p)^{X_{n+1}} \\mid X_n] = p(q/p)^{X_n + 1} + q(q/p)^{X_n - 1} = (q/p)^{X_n}[p(q/p) + q(p/q)] = (q/p)^{X_n}[q + p] = (q/p)^{X_n}\\). Applying the Optional Stopping Theorem: \\(\\mathbb{E}[M_T] = M_0 = (q/p)^k\\). Since \\(X_T\\) is either \\(N\\) (probability \\(P\\)) or \\(0\\) (probability \\(1-P\\)): \\(P (q/p)^N + (1 - P)(q/p)^0 = (q/p)^k \\implies P((q/p)^N - 1) = (q/p)^k - 1 \\implies P = \\frac{1 - (q/p)^k}{1 - (q/p)^N}\\).",
      "عندما \\(p \\neq 1/2\\)، تشكل العملية \\(M_n = (q/p)^{X_n}\\) مارتينغالاً. بتطبيق نظرية الإيقاف الاختياري نجد \\(P(q/p)^N + (1-P) = (q/p)^k\\). بحل المعادلة بالنسبة لـ \\(P\\) نحصل على \\(P = \\frac{1 - (q/p)^k}{1 - (q/p)^N}\\).",
      "Use the exponential martingale \\(M_n = (q/p)^{X_n}\\).",
      "استخدم المارتينغال الأسي \\(M_n = (q/p)^{X_n}\\).")

    # 399: Detailed Balance and Stationary Distribution Calculation
    q("KAUST-P3-399", "Markov Chains", "Medium",
      "A 3-state birth-death chain on \\(\\{0, 1, 2\\}\\) has forward probabilities \\(P_{01} = 1, P_{12} = 1/3\\) and backward probabilities \\(P_{10} = 2/3, P_{21} = 1\\). What is the stationary probability \\(\\pi_0\\)?",
      "سلسلة ولادة وموت ثلاثية الحالات لها احتمالات انتقال أمامية \\(P_{01} = 1, P_{12} = 1/3\\) وخلفية \\(P_{10} = 2/3, P_{21} = 1\\). ما هو الاحتمال المستقر \\(\\pi_0\\)؟",
      ["\\(\\frac{2}{5}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{1}{2}\\)"],
      0,
      "Use detailed balance: 1) \\(\\pi_0 P_{01} = \\pi_1 P_{10} \\implies \\pi_0 (1) = \\pi_1 (2/3) \\implies \\pi_1 = \\frac{3}{2}\\pi_0\\). 2) \\(\\pi_1 P_{12} = \\pi_2 P_{21} \\implies \\left(\\frac{3}{2}\\pi_0\\right)\\left(\\frac{1}{3}\\right) = \\pi_2 (1) \\implies \\pi_2 = \\frac{1}{2}\\pi_0\\). Sum of probabilities: \\(\\pi_0 + \\pi_1 + \\pi_2 = \\pi_0\\left(1 + \\frac{3}{2} + \\frac{1}{2}\\right) = \\pi_0(3) = 1 \\implies \\pi_0 = \\frac{1}{3}\\)... wait! Let's check the sum: \\(1 + 3/2 + 1/2 = 3\\). If sum is 3, \\(\\pi_0 = 1/3\\)! Option A is 2/5, Option B is 1/3. Let's make Option A the correct answer by adjusting options or numbers: if \\(\\pi_0 = 2/5\\), then \\(1 + \\dots = 5/2\\). If \\(P_{10} = 1/2\\), \\(\\pi_1 = 2\\pi_0\\). Let's set corr_idx = 1 (1/3) or adjust to corr_idx = 0.",
      "بالتوازن التفصيلي: \\(\\pi_1 = \\frac{3}{2}\\pi_0\\) و \\(\\pi_2 = \\frac{1}{2}\\pi_0\\). مجموع الاحتمالات: \\(\\pi_0(1 + 3/2 + 1/2) = 3\\pi_0 = 1\\)، ومنه \\(\\pi_0 = 1/3\\).",
      "Apply detailed balance \\(\\pi_0 P_{01} = \\pi_1 P_{10}\\) and \\(\\pi_1 P_{12} = \\pi_2 P_{21}\\).",
      "طبق التوازن التفصيلي بين الحالات المتجاورة.")

    # Let's fix 399 with corr_idx = 0 cleanly:
    questions.pop()
    q("KAUST-P3-399", "Markov Chains", "Medium",
      "A 3-state birth-death chain on \\(\\{0, 1, 2\\}\\) has forward probabilities \\(P_{01} = 1, P_{12} = 1/3\\) and backward probabilities \\(P_{10} = 2/3, P_{21} = 1\\). What is the stationary probability \\(\\pi_0\\)?",
      "سلسلة ولادة وموت ثلاثية الحالات لها احتمالات انتقال أمامية \\(P_{01} = 1, P_{12} = 1/3\\) وخلفية \\(P_{10} = 2/3, P_{21} = 1\\). ما هو الاحتمال المستقر \\(\\pi_0\\)؟",
      ["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)"],
      0,
      "Use detailed balance: 1) \\(\\pi_0 P_{01} = \\pi_1 P_{10} \\implies \\pi_0 (1) = \\pi_1 (2/3) \\implies \\pi_1 = \\frac{3}{2}\\pi_0\\). 2) \\(\\pi_1 P_{12} = \\pi_2 P_{21} \\implies \\left(\\frac{3}{2}\\pi_0\\right)\\left(\\frac{1}{3}\\right) = \\pi_2 (1) \\implies \\pi_2 = \\frac{1}{2}\\pi_0\\). Sum of probabilities: \\(\\pi_0 + \\pi_1 + \\pi_2 = \\pi_0\\left(1 + \\frac{3}{2} + \\frac{1}{2}\\right) = 3\\pi_0 = 1 \\implies \\pi_0 = \\frac{1}{3}\\).",
      "بالتوازن التفصيلي: \\(\\pi_1 = \\frac{3}{2}\\pi_0\\) و \\(\\pi_2 = \\frac{1}{2}\\pi_0\\). مجموع الاحتمالات: \\(\\pi_0(1 + 3/2 + 1/2) = 3\\pi_0 = 1\\)، ومنه \\(\\pi_0 = 1/3\\).",
      "Apply detailed balance \\(\\pi_0 P_{01} = \\pi_1 P_{10}\\) and \\(\\pi_1 P_{12} = \\pi_2 P_{21}\\).",
      "طبق التوازن التفصيلي بين الحالات المتجاورة واجمع الاحتمالات.")

    # 400: Ergodic Theorem for Markov Chains
    q("KAUST-P3-400", "Markov Chains", "Hard",
      "The Ergodic Theorem for an irreducible positive-recurrent Markov chain asserts that for any bounded function \\(f\\), the long-run time average \\(\\lim_{n\\to\\infty} \\frac{1}{n}\\sum_{k=0}^{n-1} f(X_k)\\) converges almost surely to which ensemble average?",
      "تنص النظرية الإرغودية لسلسلة ماركوف غير قابلة للاختزال وموجبة العودية على أن المتوسط الزمني طويل الأمد يتقارب شبه مؤكداً إلى أي متوسط إحصائي؟",
      ["\\(\\sum_i \\pi_i f(i) = \\mathbb{E}_\\pi[f(X)]\\)",
       "\\(f(X_0)\\)",
       "\\(\\max_i f(i)\\)",
       "\\(0\\)"],
      0,
      "The Ergodic Theorem (Birkhoff-von Neumann) for Markov chains establishes that the long-term time average along a single trajectory equals the spatial ensemble average with respect to the unique stationary distribution \\(\\boldsymbol{\\pi}\\): \\(\\lim_{n\\to\\infty} \\frac{1}{n}\\sum_{k=0}^{n-1} f(X_k) = \\sum_i \\pi_i f(i) = \\mathbb{E}_\\pi[f]\\) almost surely, completely independent of the starting state \\(X_0\\). Time average equals space average.",
      "تثبت النظرية الإرغودية لسلاسل ماركوف أن المتوسط الزمني على مسار مفرد يطابق تماماً المتوسط الإحصائي المكاني بالنسبة للتوزيع المستقر: \\(\\lim_{n\\to\\infty} \\frac{1}{n}\\sum f(X_k) = \\sum \\pi_i f(i)\\) شبه مؤكداً، دون أي اعتماد على الحالة الابتدائية.",
      "Time average equals ensemble average with respect to the stationary distribution.",
      "المتوسط الزمني يطابق المتوسط الإحصائي بالنسبة للتوزيع المستقر.")

    return questions

if __name__ == "__main__":
    qs = get_p3_part_c()
    print(f"Loaded {len(qs)} questions for Phase 3 Part C.")
    assert len(qs) == 50, f"Expected 50 questions, got {len(qs)}"
    for i, q in enumerate(qs, start=351):
        expected_id = f"KAUST-P3-{i}"
        assert q["id"] == expected_id, f"Expected {expected_id}, got {q['id']}"
        assert len(q["content"]["en"]["options"]) == 4
        assert len(q["content"]["ar"]["options"]) == 4
        assert 0 <= q["correct_index"] <= 3
        # Check no duplicate options
        assert len(set(q["content"]["en"]["options"])) == 4, f"Duplicate option in {q['id']}"
    print("All 50 Phase 3 Part C questions successfully verified!")
