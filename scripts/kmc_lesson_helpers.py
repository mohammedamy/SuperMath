"""Shared helpers for building bilingual, beginner-friendly KAUST (KMC) Study Lessons."""
import re
import xml.etree.ElementTree as ET
from kmc_common import m, explain_en, explain_ar, _format_prose_html, make_5_math_options, make_5_bilingual_options


def dm(expr: str) -> str:
    """Wrap a display-math formula cleanly in \\[ ... \\]."""
    return f"\\[ {expr} \\]"


# Clean Arabic formula-box overrides (Arabic caption + universal symbolic math) keyed by English formula substring
_AR_FORMULA_MAP = [
    ("Final Fraction Left", "الكسر المتبقي النهائي:", dm("F = (1 - f_1) \\times (1 - f_2)")),
    ("Added Amount", "قيمة الحصة الواحدة:", dm("u = \\frac{\\Delta Q}{\\Delta n}")),
    ("M_{\\text{total}}", "معامل التغير المئوي المحصّل:", dm("M = \\left(1 \\pm \\frac{p_1}{100}\\right)\\left(1 \\pm \\frac{p_2}{100}\\right)")),
    ("Align cycles", "تلاقي الدورات (م.م.أ) والتقسيم المتساوي (ق.م.أ):", dm("\\operatorname{lcm}(a, b) \\quad \\mid \\quad \\gcd(a, b)")),
    ("N(A \\text{ or } B)", "مبدأ التضمين والإقصاء:", dm("N(A \\cup B) = \\left\\lfloor\\frac{N}{A}\\right\\rfloor + \\left\\lfloor\\frac{N}{B}\\right\\rfloor - \\left\\lfloor\\frac{N}{\\operatorname{lcm}(A,B)}\\right\\rfloor")),
    ("Squares: ", "عدد أعواد الثقاب لـ \\( n \\) أشكال متجاورة:", dm("S_{\\square}(n) = 3n + 1, \\qquad S_{\\triangle}(n) = 2n + 1")),
    ("2\\bigcirc = 3\\square", "التعويض المتسلسل في الموازين:", dm("2\\bigcirc = 3\\square,\\; \\square = 2\\triangle \\implies 2\\bigcirc = 6\\triangle \\implies 1\\bigcirc = 3\\triangle")),
    ("Age Difference", "فرق العمر ثابت لا يتغير بمرور السنين:", dm("D = A_1 - A_2 = \\text{const}")),
    ("catch-up", "زمن اللحاق = المسافة الفاصلة مقسومةً على فرق السرعتين:", dm("t = \\frac{G}{v_1 - v_2}")),
    ("eighth of square", "مساحة المثلث المحاط وثُمن المربع:", dm("A_{\\triangle} = \\frac{1}{2} L W, \\qquad \\frac{1}{8} = 12.5\\%")),
    ("staircase", "محيط الشكل المدرّج وزاوية الخط المتعرج:", dm("P = 2(W + H), \\qquad \\theta = \\alpha + \\beta")),
    ("Apex Triangles", "عدد الأزواج وعدد المثلثات الممتدة من الرأس:", dm("\\binom{n}{2} = \\frac{n(n-1)}{2}, \\qquad N_{\\triangle} = \\frac{m(m+1)}{2}")),
    ("Combined Mean", "المتوسط الحسابي المرجّح لمجموعتين:", dm("\\bar{x} = \\frac{N_1 \\bar{x}_1 + N_2 \\bar{x}_2}{N_1 + N_2}")),
    ("\\text{with } d > r", "شرط المقسوم عليه مع الباقي:", dm("A = qd + r \\iff d \\mid (A - r), \\quad d > r")),
    ("2nd in ", "دورة رقم الآحاد لقوى 7 (طولها 4):", dm("2026 = 4(506) + 2 \\implies (7, 9, 3, 1) \\longrightarrow 9")),
    ("nines", "الطرح من قوى العشرة ومجموع الأرقام:", dm("10^{20} - 37 = \\underbrace{99\\dots9}_{18}63 \\implies S = 18(9) + 6 + 3 = 171")),
    ("digits up to ", "عدد الخانات التراكمي حتى 99:", dm("9 \\times 1 + 90 \\times 2 = 189")),
    ("consecutive", "الفرق في المتتابعة الحسابية ومجموع الحدود المتتالية:", dm("a_m - a_n = (m - n)d, \\qquad S_k = k \\cdot m")),
    ("t_{\\text{together}}", "زمن إنجاز العمل المشترك:", dm("t = \\frac{1}{\\frac{1}{t_1} + \\frac{1}{t_2}} = \\frac{t_1 t_2}{t_1 + t_2}")),
    ("Points Lost from Max", "النقاط المفقودة عن الدرجة الكاملة:", dm("L = (p + q)W + pB")),
    ("Base angles ", "زوايا القاعدة في مثلث متطابق الضلعين رأسه \\( 30^\\circ \\):", dm("\\frac{180^\\circ - 30^\\circ}{2} = 75^\\circ")),
    ("A_{\\text{ov}}", "فرق المنطقتين غير المتداخلتين يساوي فرق الشكلين الأصليين:", dm("(A_1 - A_0) - (A_2 - A_0) = A_1 - A_2")),
    ("Guarantee ", "مبدأ برج الحمام (أسوأ الحالات + 1):", dm("N = m(k - 1) + 1")),
    ("Median position", "رتبة الوسيط (فردي) وعدد نواتج حجري نرد:", dm("\\frac{N + 1}{2}, \\qquad |\\Omega| = 6 \\times 6 = 36")),
    ("odd exponent in ", "شرط المربع الكامل (جميع الأسس الأولية زوجية):", dm("\\frac{n!}{k} = m^2 \\iff v_p\\!\\left(\\frac{n!}{k}\\right) \\equiv 0 \\pmod{2}")),
    ("2m + 1 \\text{ terms}", "ثبات \\( \\lfloor\\sqrt{n}\\rfloor \\) على \\( 2m + 1 \\) عدداً متتالياً:", dm("\\lfloor \\sqrt{n} \\rfloor = m \\quad \\left(m^2 \\le n \\le (m+1)^2 - 1\\right)")),
    ("term equals ", "تحديد قيمة الحد ذي الرتبة \\( N \\) بالأعداد المثلثية:", dm("T_{k-1} < N \\le T_k \\implies a_N = k")),
    ("g_{\\text{odd}}", "تماثل دالة فردية مضافاً إليها ثابت \\( k \\):", dm("g(-x) = -g(x),\\; f(x) = g(x) + k \\implies f(a) + f(-a) = 2k")),
    ("lies between ", "أصغر مجموع مسافتين يتحقق على كامل القطعة الواصلة بين النقطتين:", dm("|x - a| + |x - b| = |a - b| \\iff \\min(a,b) \\le x \\le \\max(a,b)")),
    ("r_{\\text{cyl}}^2", "المكعب داخل أسطوانة وشبه المنحرف القائم حول نصف دائرة:", dm("r_1^2 = \\frac{a^2}{2}, \\qquad r_2 = \\sqrt{ab}, \\qquad A = (a + b)\\sqrt{ab}")),
    ("Interior Diagonal Intersections", "تقاطعات الأقطار الداخلية ومعاملات تكبير المساحة والحجم:", dm("\\binom{n}{4}, \\qquad \\frac{A_2}{A_1} = k^2, \\qquad \\frac{V_2}{V_1} = k^3")),
    ("\\text{Step }", "ركن الحلزون المرجعي وعدد النقاط الصحيحة في المعين:", dm("2k(2k+1) \\longrightarrow (-k, -k), \\qquad \\#\\{|x| + |y| \\le R\\} = 2R^2 + 2R + 1")),
    ("Valid Committees", "التوافيق والعدّ بطرح الحالات الممنوعة:", dm("\\binom{n}{k} = \\frac{n!}{k!(n-k)!}, \\qquad \\binom{n}{k} - \\binom{n - 2}{k - 2}")),
    ("P(A \\text{ then } B)", "قاعدة ضرب الاحتمالات المتتابعة:", dm("P(A \\cap B) = P(A) \\times P(B \\mid A)")),
]


def _polish_html(s: str) -> str:
    """Format markdown bold/code, convert newlines to <br>, and glue trailing punctuation to inline math."""
    out = _format_prose_html(s)
    out = out.replace("\n", "<br>")
    # Prevent orphan punctuation (! . , ? ; : ، ؟) wrapping alone onto a new line right after short \( ... \)
    out = re.sub(
        r"(\\\([^<>]{1,42}?\\\))([.,!?;:،؟]+)",
        r'<span class="eg-mkeep">\1\2</span>',
        out,
    )
    return out


def _localize_formula_ar(formula_en: str, formula_ar: str) -> str:
    if formula_ar:
        return _polish_html(formula_ar)
    if not formula_en:
        return ""
    for needle, caption_ar, clean_math in _AR_FORMULA_MAP:
        if needle in formula_en:
            return f'<div class="eg-f-caption" dir="rtl">{_polish_html(caption_ar)}</div>{clean_math}'
    return _polish_html(formula_en)


def concept(title_en: str, title_ar: str, body_en: str, body_ar: str,
            formula_en: str = "", formula_ar: str = "",
            diagram_en: str = None, diagram_ar: str = None) -> dict:
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    out = {
        "en": {
            "title": _polish_html(title_en),
            "body": _polish_html(body_en),
            "formula": _polish_html(formula_en) if formula_en else "",
        },
        "ar": {
            "title": _polish_html(title_ar),
            "body": _polish_html(body_ar),
            "formula": _localize_formula_ar(formula_en, formula_ar),
        },
    }
    if diagram_en:
        out["en"]["diagram"] = diagram_en
        out["ar"]["diagram"] = diagram_ar if diagram_ar else diagram_en
    return out


def worked_math_example(
    ex_id: str,
    title_en: str,
    title_ar: str,
    q_en: str,
    q_ar: str,
    correct_val,
    distractors: list,
    idea_en: str,
    steps_en: list[str],
    check_en: str,
    idea_ar: str,
    steps_ar: list[str],
    check_ar: str,
    suffix: str = "",
    diagram_en: str = None,
    diagram_ar: str = None,
) -> dict:
    opts_en, opts_ar, cidx, cans = make_5_math_options(correct_val, distractors, ex_id, suffix=suffix)
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    en_obj = {
        "title": _polish_html(title_en),
        "question": _polish_html(q_en),
        "options": [_polish_html(o) for o in opts_en],
        "explanation": _polish_html(explain_en(idea_en, steps_en, check_en)),
    }
    ar_obj = {
        "title": _polish_html(title_ar),
        "question": _polish_html(q_ar),
        "options": [_polish_html(o) for o in opts_ar],
        "explanation": _polish_html(explain_ar(idea_ar, steps_ar, check_ar)),
    }
    if diagram_en:
        en_obj["diagram"] = diagram_en
        ar_obj["diagram"] = diagram_ar if diagram_ar else diagram_en
    return {
        "id": ex_id,
        "correct_index": cidx,
        "correct_answer": str(cans),
        "en": en_obj,
        "ar": ar_obj,
    }


def worked_bilingual_example(
    ex_id: str,
    title_en: str,
    title_ar: str,
    q_en: str,
    q_ar: str,
    pairs: list[tuple[str, str]],
    idea_en: str,
    steps_en: list[str],
    check_en: str,
    idea_ar: str,
    steps_ar: list[str],
    check_ar: str,
    diagram_en: str = None,
    diagram_ar: str = None,
) -> dict:
    opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, 0, ex_id, shuffle=True)
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    en_obj = {
        "title": _polish_html(title_en),
        "question": _polish_html(q_en),
        "options": [_polish_html(o) for o in opts_en],
        "explanation": _polish_html(explain_en(idea_en, steps_en, check_en)),
    }
    ar_obj = {
        "title": _polish_html(title_ar),
        "question": _polish_html(q_ar),
        "options": [_polish_html(o) for o in opts_ar],
        "explanation": _polish_html(explain_ar(idea_ar, steps_ar, check_ar)),
    }
    if diagram_en:
        en_obj["diagram"] = diagram_en
        ar_obj["diagram"] = diagram_ar if diagram_ar else diagram_en
    return {
        "id": ex_id,
        "correct_index": cidx,
        "correct_answer": str(cans),
        "en": en_obj,
        "ar": ar_obj,
    }


def make_lesson(
    lesson_id: str,
    level: str,
    unit_num: str,
    topic: str,
    title_en: str,
    title_ar: str,
    summary_en: str,
    summary_ar: str,
    goals_en: list[str],
    goals_ar: list[str],
    concepts: list[dict],
    traps_en: list[str],
    traps_ar: list[str],
    examples: list[dict],
    blueprints: list[str],
) -> dict:
    assert level in ("Track 1: Grades 6-7", "Track 2: Grades 8-9", "Track 3: Grades 10-11")
    assert len(concepts) >= 3
    assert len(examples) >= 4
    return {
        "id": lesson_id,
        "track": "kaust",
        "level": level,
        "unit_num": unit_num,
        "topic": topic,
        "blueprints": blueprints,
        "en": {
            "title": _polish_html(title_en),
            "summary": _polish_html(summary_en),
            "goals": [_polish_html(g) for g in goals_en],
            "concepts": [c["en"] for c in concepts],
            "traps": [_polish_html(t) for t in traps_en],
            "examples": [
                {"id": ex["id"], "correct_index": ex["correct_index"], **ex["en"]}
                for ex in examples
            ],
        },
        "ar": {
            "title": _polish_html(title_ar),
            "summary": _polish_html(summary_ar),
            "goals": [_polish_html(g) for g in goals_ar],
            "concepts": [c["ar"] for c in concepts],
            "traps": [_polish_html(t) for t in traps_ar],
            "examples": [
                {"id": ex["id"], "correct_index": ex["correct_index"], **ex["ar"]}
                for ex in examples
            ],
        },
    }
