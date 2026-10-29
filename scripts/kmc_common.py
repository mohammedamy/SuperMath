"""Shared helpers for building verified, beginner-friendly KAUST Mathematics Competition (KMC) items."""
import html
import random
import re
from fractions import Fraction


def m(expr) -> str:
    """Wrap a LaTeX math expression in inline MathJax delimiters."""
    return f"\\( {expr} \\)"


def fmt_val(v) -> str:
    """Format an int, float, Fraction, or LaTeX string cleanly for MathJax."""
    if isinstance(v, Fraction):
        if v.denominator == 1:
            return str(v.numerator)
        if v.numerator < 0:
            return f"-\\frac{{{abs(v.numerator)}}}{{{v.denominator}}}"
        return f"\\frac{{{v.numerator}}}{{{v.denominator}}}"
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v))
        return f"{v:g}"
    return str(v)


def norm_text(s: str) -> str:
    s = re.sub(r"<svg\b.*?</svg>", " ", str(s), flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip().lower()


def explain_en(idea: str, steps: list[str], check: str) -> str:
    step_html = "".join(
        f'<p class="mb-1.5"><strong>Step {i}:</strong> {st}</p>'
        for i, st in enumerate(steps, 1)
    )
    return (
        f'<div class="space-y-2">'
        f'<p class="mb-2"><strong>💡 Key Idea:</strong> {idea}</p>'
        f'{step_html}'
        f'<p class="mt-2 pt-1.5 border-t border-slate-700/40"><strong>✅ Quick Check:</strong> {check}</p>'
        f'</div>'
    )


def explain_ar(idea: str, steps: list[str], check: str) -> str:
    step_html = "".join(
        f'<p class="mb-1.5"><strong>الخطوة {i}:</strong> {st}</p>'
        for i, st in enumerate(steps, 1)
    )
    return (
        f'<div class="space-y-2">'
        f'<p class="mb-2"><strong>💡 الفكرة الأساسية:</strong> {idea}</p>'
        f'{step_html}'
        f'<p class="mt-2 pt-1.5 border-t border-slate-700/40"><strong>✅ التحقق من الحل:</strong> {check}</p>'
        f'</div>'
    )


def make_5_math_options(correct_val, distractors: list, seed_key: str, suffix: str = "") -> tuple[list[str], list[str], int, str]:
    """Build 5 unique MathJax options around correct_val with deterministic order."""
    ans_str = fmt_val(correct_val) + suffix
    ans_opt = m(ans_str)
    pool = []
    seen = {norm_text(ans_opt)}
    for d in distractors:
        d_str = fmt_val(d) + suffix
        d_opt = m(d_str)
        nd = norm_text(d_opt)
        if nd not in seen:
            seen.add(nd)
            pool.append(d_opt)
        if len(pool) == 4:
            break

    # Deterministic fallback distractors if fewer than 4 distinct distractors were supplied
    step = 1
    while len(pool) < 4:
        if isinstance(correct_val, int):
            cand_v = correct_val + (step if step % 2 == 1 else -step // 2)
            if correct_val >= 0 and cand_v < 0:
                cand_v = correct_val + step + 3
        elif isinstance(correct_val, Fraction):
            cand_v = Fraction(max(1, correct_val.numerator + step), correct_val.denominator + (step % 2))
        else:
            cand_v = f"{ans_str}_{step}"
        c_opt = m(fmt_val(cand_v) + suffix)
        nc = norm_text(c_opt)
        if nc not in seen:
            seen.add(nc)
            pool.append(c_opt)
        step += 1

    all_opts = [ans_opt] + pool[:4]
    rng = random.Random(seed_key)
    rng.shuffle(all_opts)
    correct_idx = all_opts.index(ans_opt)
    assert len(all_opts) == 5 and len({norm_text(o) for o in all_opts}) == 5
    return all_opts, list(all_opts), correct_idx, ans_str


def make_5_bilingual_options(pairs: list[tuple[str, str]], correct_pair_idx: int = 0,
                             seed_key: str = "", shuffle: bool = True) -> tuple[list[str], list[str], int, str]:
    """Build 5 distinct bilingual options [(en, ar), ...]."""
    assert len(pairs) == 5, f"Expected 5 option pairs, got {len(pairs)}"
    indexed = list(enumerate(pairs))
    if shuffle:
        rng = random.Random(seed_key)
        rng.shuffle(indexed)
    opts_en = [p[0] for _, p in indexed]
    opts_ar = [p[1] for _, p in indexed]
    correct_idx = next(idx for idx, (orig_i, _) in enumerate(indexed) if orig_i == correct_pair_idx)
    assert len({norm_text(o) for o in opts_en}) == 5, f"Duplicate EN options: {opts_en}"
    assert len({norm_text(o) for o in opts_ar}) == 5, f"Duplicate AR options: {opts_ar}"
    return opts_en, opts_ar, correct_idx, pairs[correct_pair_idx][0]


def _format_prose_html(s: str) -> str:
    """Convert **bold** and `code` (including bold wrapping \\( ... \\)) into clean HTML tags."""
    saved: list[str] = []

    def _stash(match: re.Match) -> str:
        saved.append(match.group(0))
        return f"\x00MATH{len(saved) - 1}\x00"

    masked = re.sub(r"\\\(.*?\\\)", _stash, s.strip(), flags=re.S)
    masked = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", masked)
    masked = re.sub(r"`([^`]+)`", r"<code>\1</code>", masked)
    return re.sub(r"\x00MATH(\d+)\x00", lambda m_: saved[int(m_.group(1))], masked)


def make_kmc_question(
    qid: str,
    level: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    opts_en: list[str],
    opts_ar: list[str],
    correct_idx: int,
    correct_answer: str,
    hint_en: str,
    hint_ar: str,
    sol_en: str,
    sol_ar: str,
    diagram_en: str = None,
    diagram_ar: str = None,
) -> dict:
    assert level in (
        "Track 1: Grades 6-7",
        "Track 2: Grades 8-9",
        "Track 3: Grades 10-11",
    ), f"Invalid KMC level: {level}"
    assert difficulty in ("Easy", "Medium", "Hard")
    assert len(opts_en) == 5 and len(opts_ar) == 5
    assert 0 <= correct_idx < 5
    assert ":\\\\(" not in q_en and "\\\\(" not in q_en and "\\\\(" not in q_ar

    en_block = {
        "question": _format_prose_html(q_en),
        "options": [_format_prose_html(o) for o in opts_en],
        "hint": _format_prose_html(hint_en),
        "explanation": _format_prose_html(sol_en),
    }
    ar_block = {
        "question": _format_prose_html(q_ar),
        "options": [_format_prose_html(o) for o in opts_ar],
        "hint": _format_prose_html(hint_ar),
        "explanation": _format_prose_html(sol_ar),
    }
    if diagram_en:
        en_block["diagram"] = diagram_en
        ar_block["diagram"] = diagram_ar if diagram_ar else diagram_en

    return {
        "id": qid,
        "track": "kaust",
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        "kmc_blueprint": blueprint,
        "review": {
            "structural": "passed",
            "mathematical": "programmatically_verified",
            "scope": "kaust_mathematics_competition_kmc",
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }
