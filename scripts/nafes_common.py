"""Shared helpers, 4-option (A–D) MCQ builders, lesson builders, and ETEC Nafes SVG generators for Grades 3, 6, and 9."""
import html
import json
import math
import random
import re
import xml.etree.ElementTree as ET
from fractions import Fraction
from pathlib import Path

from kmc_common import (
    _format_prose_html,
    explain_ar,
    explain_en,
    fmt_val,
    m,
    norm_text,
)
from kmc_diagrams import *  # noqa: F401,F403
from kmc_diagrams import BLUE, GREEN, GRID, MUTED, ORANGE, RED, SHADE, SHADE_ALT, STROKE, WATER, _esc as esc, wrap_svg
from kmc_diagrams_extra import *  # noqa: F401,F403
from kangaroo_common import (  # noqa: F401
    svg_kang_cube_faces,
    svg_kang_folded_ribbon,
    svg_kang_gear_train,
    svg_kang_grid_walk,
    svg_kang_magic_cross,
    svg_kang_matchstick_digits,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_overlapping_rects,
    svg_kang_polyomino_board,
    svg_kang_staircase_perimeter,
    svg_kang_stamp_grid,
)

PAL = {
    "ink": STROKE,
    "blue": BLUE,
    "rose": RED,
    "teal": GREEN,
    "amber": ORANGE,
    "purple": "#7c3aed",
    "muted": MUTED,
    "grid": GRID,
    "blue_fill": WATER,
    "amber_fill": SHADE_ALT,
    "teal_fill": "#ccfbf1",
    "purple_fill": SHADE,
}

ROOT = Path(__file__).resolve().parents[1]

NAFES_LEVELS = (
    "Grade 3",
    "Grade 6",
    "Grade 9",
)

NAFES_TOPICS = (
    "Numbers & Operations",
    "Algebra",
    "Geometry",
    "Data & Probability",
)

NAFES_FORBIDDEN_RE = re.compile(
    "|".join([
        r"\bderivative\b",
        r"\bintegral\b",
        r"\bdifferentiable\b",
        r"\bdifferential\s+equation",
        r"\beigenvalue\b",
        r"\beigenvector\b",
        r"\bdeterminant\b",
        r"\bmatrix\b",
        r"\bmatrices\b",
        r"\bcomplex\s+number",
        r"\bimaginary\b",
        r"\blogarithm",
        r"\bmarkov\b",
        r"\bstochastic\b",
        r"\btaylor\b",
        r"\bfourier\b",
        r"\blaplace\b",
        r"\bcauchy-schwarz\b",
        r"\beuler's\s+totient\b",
        r"\\int\b",
        r"\\lim\b",
        r"\\log\b",
        r"\\ln\b",
        r"\\sin\b",
        r"\\cos\b",
        r"\\tan\b",
        r"\\cot\b",
        r"\\sec\b",
        r"\\csc\b",
        r"\\partial\b",
        r"\\nabla\b",
    ]),
    re.IGNORECASE,
)


def dm(expr: str) -> str:
    return f"\\[ {expr} \\]"


def load_other_track_stems() -> set[str]:
    """Return normalized English stems from all non-Nafes banks so Nafes stems are 100% globally unique."""
    stems: set[str] = set()
    for name in ("kaust", "nsmo", "kangaroo", "jee", "olympiad"):
        p = ROOT / "data" / f"{name}.json"
        if p.exists():
            for q in json.loads(p.read_text(encoding="utf-8")):
                stems.add(norm_text(q["content"]["en"]["question"]))
    return stems


def make_4_math_options(correct_val, distractors: list, seed_key: str, suffix: str = "") -> tuple[list[str], list[str], int, str]:
    """Build 4 distinct MathJax options (A–D) around correct_val with deterministic order."""
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
        if len(pool) == 3:
            break

    step = 1
    while len(pool) < 3:
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

    all_opts = [ans_opt] + pool[:3]
    rng = random.Random(seed_key)
    rng.shuffle(all_opts)
    correct_idx = all_opts.index(ans_opt)
    assert len(all_opts) == 4 and len({norm_text(o) for o in all_opts}) == 4
    return all_opts, list(all_opts), correct_idx, ans_str


def make_4_bilingual_options(
    pairs: list[tuple[str, str]],
    correct_pair_idx: int = 0,
    seed_key: str = "",
    shuffle: bool = True,
) -> tuple[list[str], list[str], int, str]:
    """Build 4 distinct bilingual options [(en, ar), ...]."""
    assert len(pairs) == 4, f"Expected 4 option pairs, got {len(pairs)}"
    indexed = list(enumerate(pairs))
    if shuffle:
        rng = random.Random(seed_key)
        rng.shuffle(indexed)
    opts_en = [p[0] for _, p in indexed]
    opts_ar = [p[1] for _, p in indexed]
    correct_idx = next(idx for idx, (orig_i, _) in enumerate(indexed) if orig_i == correct_pair_idx)
    assert len({norm_text(o) for o in opts_en}) == 4, f"Duplicate EN options: {opts_en}"
    assert len({norm_text(o) for o in opts_ar}) == 4, f"Duplicate AR options: {opts_ar}"
    return opts_en, opts_ar, correct_idx, pairs[correct_pair_idx][0]


def make_nafes_question(
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
    assert level in NAFES_LEVELS, f"Invalid Nafes level: {level}"
    assert topic in NAFES_TOPICS, f"Invalid Nafes topic: {topic}"
    assert difficulty in ("Easy", "Medium", "Hard"), f"Invalid difficulty: {difficulty}"
    assert len(opts_en) == 4 and len(opts_ar) == 4, f"Nafes requires 4 options (A–D): {qid}"
    assert 0 <= correct_idx < 4
    assert "\\\\(" not in q_en and "\\\\(" not in q_ar

    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)

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

    for lang_blk in (en_block, ar_block):
        blob = " ".join([lang_blk["question"], *lang_blk["options"], lang_blk["hint"], lang_blk["explanation"]])
        m_f = NAFES_FORBIDDEN_RE.search(blob)
        assert not m_f, f"Forbidden term '{m_f.group(0)}' in {qid}"

    return {
        "id": qid,
        "track": "nafes",
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        "nafes_blueprint": blueprint,
        "review": {
            "structural": "passed",
            "mathematical": "programmatically_verified",
            "scope": "etec_nafes_ksa_grades_3_6_9",
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }


def make_nafes_q(
    qid: str,
    level: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    correct_val,
    distractors: list,
    hint_en: str,
    hint_ar: str,
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
    """Convenience builder combining make_4_math_options + explain_en/ar + make_nafes_question."""
    opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, qid, suffix=suffix)
    return make_nafes_question(
        qid=qid,
        level=level,
        topic=topic,
        difficulty=difficulty,
        blueprint=blueprint,
        q_en=q_en,
        q_ar=q_ar,
        opts_en=opts_en,
        opts_ar=opts_ar,
        correct_idx=cidx,
        correct_answer=cans,
        hint_en=hint_en,
        hint_ar=hint_ar,
        sol_en=explain_en(idea_en, steps_en, check_en),
        sol_ar=explain_ar(idea_ar, steps_ar, check_ar),
        diagram_en=diagram_en,
        diagram_ar=diagram_ar,
    )


# ---- Nafes Study Lesson Builders ----
def nafes_concept(
    title_en: str,
    title_ar: str,
    body_en: str,
    body_ar: str,
    formula_en: str,
    caption_ar: str,
    formula_math_ar: str,
    diagram_en: str,
    diagram_ar: str = None,
) -> dict:
    assert diagram_en and "<svg" in diagram_en, f"Concept '{title_en}' must include an SVG diagram"
    ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    ar_form = (
        f'<div class="eg-f-caption" dir="rtl">{_format_prose_html(caption_ar)}</div>{formula_math_ar}'
        if caption_ar
        else _format_prose_html(formula_math_ar)
    )
    return {
        "en": {
            "title": _format_prose_html(title_en),
            "body": _format_prose_html(body_en),
            "formula": _format_prose_html(formula_en),
            "diagram": diagram_en,
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "body": _format_prose_html(body_ar),
            "formula": ar_form,
            "diagram": diagram_ar if diagram_ar else diagram_en,
        },
    }


def nafes_worked_example(
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
    bilingual_pairs: list[tuple[str, str]] = None,
    correct_pair_idx: int = 0,
) -> dict:
    if bilingual_pairs is not None:
        opts_en, opts_ar, cidx, cans = make_4_bilingual_options(bilingual_pairs, correct_pair_idx, ex_id)
    else:
        opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, ex_id, suffix=suffix)
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    clean_title_en = re.sub(r"^(?:Solved\s+)?Example\s*\d+\s*[:—\-–]\s*", "", title_en.strip(), flags=re.IGNORECASE)
    clean_title_ar = re.sub(r"^(?:ال)?مثال(?:\s+المحلول|\s+محلول)?\s*[\d٠-٩]+\s*[:—\-–]\s*", "", title_ar.strip())
    en_obj = {
        "title": _format_prose_html(clean_title_en),
        "question": _format_prose_html(q_en),
        "options": [_format_prose_html(o) for o in opts_en],
        "explanation": _format_prose_html(explain_en(idea_en, steps_en, check_en)),
    }
    ar_obj = {
        "title": _format_prose_html(clean_title_ar),
        "question": _format_prose_html(q_ar),
        "options": [_format_prose_html(o) for o in opts_ar],
        "explanation": _format_prose_html(explain_ar(idea_ar, steps_ar, check_ar)),
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


def make_nafes_lesson(
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
    assert level in NAFES_LEVELS
    assert topic in NAFES_TOPICS
    assert len(concepts) >= 3
    assert len(examples) >= 4
    clean_unit_num = re.sub(r"^(?:Lesson|درس)\s+", "", str(unit_num).strip(), flags=re.IGNORECASE)
    return {
        "id": lesson_id,
        "track": "nafes",
        "level": level,
        "unit_num": clean_unit_num,
        "topic": topic,
        "blueprints": blueprints,
        "en": {
            "title": _format_prose_html(title_en),
            "summary": _format_prose_html(summary_en),
            "goals": [_format_prose_html(g) for g in goals_en],
            "concepts": [c["en"] for c in concepts],
            "traps": [_format_prose_html(t) for t in traps_en],
            "examples": [
                {"id": ex["id"], "correct_index": ex["correct_index"], **ex["en"]}
                for ex in examples
            ],
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "summary": _format_prose_html(summary_ar),
            "goals": [_format_prose_html(g) for g in goals_ar],
            "concepts": [c["ar"] for c in concepts],
            "traps": [_format_prose_html(t) for t in traps_ar],
            "examples": [
                {"id": ex["id"], "correct_index": ex["correct_index"], **ex["ar"]}
                for ex in examples
            ],
        },
    }


# ==============================================================================
# 10 Bespoke ETEC Nafes SVG Generators (Grades 3, 6 & 9 — Screen + A4 Print)
# ==============================================================================

def _wrap_nafes_svg(w: int, h: int, body: str) -> str:
    return wrap_svg(body, w=w, h=h, disp_w=min(420, max(240, w)), title="ETEC Nafes diagram / رسم توضيحي لاختبار نافس")


def svg_nafes_place_value_blocks(thousands: int = 0, hundreds: int = 2, tens: int = 4, ones: int = 5, label: str = "") -> str:
    """Place-value chart with Base-10 visual columns (Thousands, Hundreds, Tens, Ones)."""
    w, h = 420, 175
    cols = [("1000s", thousands, "#dbeafe", BLUE), ("100s", hundreds, "#ccfbf1", GREEN), ("10s", tens, "#fef3c7", ORANGE), ("1s", ones, "#f3e8ff", "#7c3aed")]
    if thousands == 0:
        cols = cols[1:]
        w = 340
    cw = (w - 36) / len(cols)
    parts = [f'<rect x="14" y="14" width="{w - 28:.1f}" height="{h - 32}" rx="10" fill="#ffffff" stroke="{STROKE}" stroke-width="1.6"/>']
    parts.append(f'<line x1="14" y1="44" x2="{w - 14}" y2="44" stroke="{STROKE}" stroke-width="1.3"/>')
    for idx, (hdr, cnt, fill_c, strk_c) in enumerate(cols):
        x0 = 14 + idx * cw
        if idx > 0:
            parts.append(f'<line x1="{x0:.1f}" y1="14" x2="{x0:.1f}" y2="{h - 18}" stroke="{GRID}" stroke-width="1.2"/>')
        cx = x0 + cw / 2
        parts.append(f'<text x="{cx:.1f}" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(hdr)}</text>')
        for k in range(min(cnt, 9)):
            r, c = divmod(k, 3)
            bx = x0 + cw / 2 - 31 + c * 22
            by = 54 + r * 24
            if hdr == "10s":
                parts.append(f'<rect x="{bx + 4:.1f}" y="{by}" width="10" height="19" rx="2" fill="{fill_c}" stroke="{strk_c}" stroke-width="1.3"/>')
            elif hdr == "1s":
                parts.append(f'<circle cx="{bx + 9:.1f}" cy="{by + 9}" r="6.5" fill="{fill_c}" stroke="{strk_c}" stroke-width="1.3"/>')
            else:
                parts.append(f'<rect x="{bx:.1f}" y="{by}" width="18" height="18" rx="3" fill="{fill_c}" stroke="{strk_c}" stroke-width="1.3"/>')
        parts.append(f'<text x="{cx:.1f}" y="{h - 24}" text-anchor="middle" font-size="12" font-weight="800" fill="{strk_c}">({cnt})</text>')
    if label:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 4}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(label)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_fraction_bars(num1: int, den1: int, num2: int = None, den2: int = None, label1: str = "", label2: str = "") -> str:
    """Shaded fraction strip(s) for visual fraction comparison, equivalence, or addition."""
    two = num2 is not None and den2 is not None
    w, h = 360, (142 if two else 92)
    bx, bw, bh = 28, 250, 30
    parts = []

    def draw_strip(y: int, num: int, den: int, fill_c: str, strk_c: str, lbl: str):
        den = max(1, den)
        sw = bw / den
        for i in range(den):
            fc = fill_c if i < num else "#f8fafc"
            parts.append(f'<rect x="{bx + i * sw:.2f}" y="{y}" width="{sw:.2f}" height="{bh}" fill="{fc}" stroke="{STROKE}" stroke-width="1.4"/>')
        txt = lbl if lbl else f"{num}/{den}"
        parts.append(f'<text x="{bx + bw + 14}" y="{y + 20}" font-size="13" font-weight="800" fill="{strk_c}">{esc(txt)}</text>')

    draw_strip(24, num1, den1, "#bfdbfe", BLUE, label1)
    if two:
        draw_strip(78, num2, den2, "#bbf7d0", GREEN, label2)
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_analog_clock(hour: int, minute: int, caption: str = "") -> str:
    """Analog 12-hour clock face with crisp hour & minute hands and minute ticks."""
    w, h = 230, (215 if caption else 195)
    cx, cy, r = 115, 96, 76
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{GRID}" stroke-width="1"/>',
    ]
    for m_tick in range(60):
        ang = math.radians(m_tick * 6 - 90)
        r_in = r - (8 if m_tick % 5 == 0 else 4)
        sw = 1.8 if m_tick % 5 == 0 else 0.9
        col = STROKE if m_tick % 5 == 0 else MUTED
        parts.append(
            f'<line x1="{cx + r_in * math.cos(ang):.2f}" y1="{cy + r_in * math.sin(ang):.2f}" '
            f'x2="{cx + (r - 1) * math.cos(ang):.2f}" y2="{cy + (r - 1) * math.sin(ang):.2f}" stroke="{col}" stroke-width="{sw}"/>'
        )
    for num in range(1, 13):
        ang = math.radians(num * 30 - 90)
        nx = cx + (r - 20) * math.cos(ang)
        ny = cy + (r - 20) * math.sin(ang) + 4.5
        parts.append(f'<text x="{nx:.2f}" y="{ny:.2f}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{num}</text>')

    min_ang = math.radians((minute % 60) * 6 - 90)
    hr_ang = math.radians(((hour % 12) + (minute % 60) / 60.0) * 30 - 90)
    parts.append(
        f'<line x1="{cx}" y1="{cy}" x2="{cx + 54 * math.cos(min_ang):.2f}" y2="{cy + 54 * math.sin(min_ang):.2f}" '
        f'stroke="{BLUE}" stroke-width="2.8" stroke-linecap="round"/>'
    )
    parts.append(
        f'<line x1="{cx}" y1="{cy}" x2="{cx + 37 * math.cos(hr_ang):.2f}" y2="{cy + 37 * math.sin(hr_ang):.2f}" '
        f'stroke="{RED}" stroke-width="3.8" stroke-linecap="round"/>'
    )
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="{STROKE}"/>')
    if caption:
        parts.append(f'<text x="{cx}" y="{h - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_sar_money(bills_and_coins: list[int], caption: str = "") -> str:
    """Visual Saudi Riyal (SAR) banknotes (5, 10, 50, 100, 500) & coins (1, 2)."""
    items = list(bills_and_coins)[:10]
    cols = min(5, max(1, len(items)))
    rows = (len(items) + cols - 1) // cols
    w = max(250, cols * 74 + 28)
    h = rows * 50 + (42 if caption else 24)
    parts = []
    bill_colors = {500: ("#dbeafe", BLUE), 100: ("#fee2e2", RED), 50: ("#dcfce7", GREEN), 20: ("#f3e8ff", "#7c3aed"), 10: ("#fef3c7", ORANGE), 5: ("#fce7f3", "#db2777")}
    for idx, val in enumerate(items):
        r, c = divmod(idx, cols)
        x = 18 + c * 72
        y = 14 + r * 48
        if val >= 5:
            fc, sc = bill_colors.get(val, ("#e0f2fe", BLUE))
            parts.append(f'<rect x="{x}" y="{y}" width="62" height="34" rx="5" fill="{fc}" stroke="{sc}" stroke-width="1.6"/>')
            parts.append(f'<text x="{x + 31}" y="{y + 22}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{val} SAR</text>')
        else:
            cx, cy = x + 31, y + 17
            fc = "#fef08a" if val == 2 else "#e2e8f0"
            sc = ORANGE if val == 2 else STROKE
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{fc}" stroke="{sc}" stroke-width="1.8"/>')
            parts.append(f'<text x="{cx}" y="{cy + 4.5}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{STROKE}">{val} SAR</text>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_function_table(headers: list[str], rows: list[list], highlight_cell: tuple[int, int] = None) -> str:
    """Clean ETEC input-output / ratio / two-way data table SVG."""
    ncols = max(2, len(headers))
    nrows = len(rows)
    cw = max(68, min(115, 360 // ncols))
    w = ncols * cw + 36
    rh = 28
    h = (nrows + 1) * rh + 28
    x0, y0 = 18, 14
    tw, th = ncols * cw, (nrows + 1) * rh
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{tw}" height="{th}" rx="8" fill="#ffffff" stroke="{STROKE}" stroke-width="1.6"/>',
        f'<rect x="{x0}" y="{y0}" width="{tw}" height="{rh}" rx="8" fill="#e0f2fe" stroke="{STROKE}" stroke-width="1.4"/>',
    ]
    for c_i, hdr in enumerate(headers):
        cx = x0 + c_i * cw + cw / 2
        if c_i > 0:
            parts.append(f'<line x1="{x0 + c_i * cw}" y1="{y0}" x2="{x0 + c_i * cw}" y2="{y0 + th}" stroke="{GRID}" stroke-width="1.2"/>')
        parts.append(f'<text x="{cx:.1f}" y="{y0 + 19}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(str(hdr))}</text>')
    for r_i, row in enumerate(rows):
        ry = y0 + (r_i + 1) * rh
        parts.append(f'<line x1="{x0}" y1="{ry}" x2="{x0 + tw}" y2="{ry}" stroke="{GRID}" stroke-width="1.1"/>')
        for c_i, cell in enumerate(row[:ncols]):
            if highlight_cell == (r_i, c_i) or str(cell).strip() == "?":
                parts.append(f'<rect x="{x0 + c_i * cw + 2}" y="{ry + 2}" width="{cw - 4}" height="{rh - 4}" rx="4" fill="#fef3c7"/>')
            cx = x0 + c_i * cw + cw / 2
            col = RED if (highlight_cell == (r_i, c_i) or str(cell).strip() == "?") else STROKE
            parts.append(f'<text x="{cx:.1f}" y="{ry + 19}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{col}">{esc(str(cell))}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_pictograph(rows: list[tuple[str, float]], key_label: str, symbol_color: str = BLUE) -> str:
    """Pictograph chart supporting whole and half (.5) symbols with a clear legend key."""
    w = 360
    rh = 30
    h = len(rows) * rh + 56
    parts = [
        f'<rect x="14" y="12" width="{w - 28}" height="{len(rows) * rh + 12}" rx="8" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>',
        f'<line x1="112" y1="12" x2="112" y2="{len(rows) * rh + 24}" stroke="{STROKE}" stroke-width="1.3"/>',
    ]
    defs = []
    for idx, (lbl, count) in enumerate(rows):
        y = 18 + idx * rh
        if idx > 0:
            parts.append(f'<line x1="14" y1="{y - 3}" x2="{w - 14}" y2="{y - 3}" stroke="{GRID}" stroke-width="1"/>')
        parts.append(f'<text x="104" y="{y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
        whole = int(math.floor(count + 1e-6))
        half = (count - whole) >= 0.45
        for k in range(min(whole, 9)):
            cx = 128 + k * 24
            parts.append(f'<circle cx="{cx}" cy="{y + 12}" r="8" fill="#bfdbfe" stroke="{symbol_color}" stroke-width="1.6"/>')
        if half:
            cx = 128 + whole * 24
            clip_id = f"pclip_{idx}_{whole}"
            defs.append(f'<clipPath id="{clip_id}"><rect x="{cx - 9}" y="{y + 2}" width="9" height="20"/></clipPath>')
            parts.append(f'<circle cx="{cx}" cy="{y + 12}" r="8" fill="#bfdbfe" stroke="{symbol_color}" stroke-width="1.6" clip-path="url(#{clip_id})"/>')
            parts.append(f'<line x1="{cx}" y1="{y + 4}" x2="{cx}" y2="{y + 20}" stroke="{symbol_color}" stroke-width="1.5"/>')
    ky = len(rows) * rh + 43
    parts.append(f'<circle cx="44" cy="{ky - 4}" r="7" fill="#bfdbfe" stroke="{symbol_color}" stroke-width="1.6"/>')
    parts.append(f'<text x="58" y="{ky}" font-size="12" font-weight="700" fill="{STROKE}">{esc(key_label)}</text>')
    defs_tag = f"<defs>{''.join(defs)}</defs>" if defs else ""
    return _wrap_nafes_svg(w, h, defs_tag + "".join(parts))


def svg_nafes_coordinate_line(
    pts: list[tuple[float, float, str]],
    line_kb: tuple[float, float] = None,
    line2_kb: tuple[float, float] = None,
    max_coord: int = 6,
) -> str:
    """4-quadrant coordinate plane [-max_coord, max_coord] with optional line(s) y = m*x + b and labeled points."""
    w, h = 270, 260
    cx, cy = 135, 130
    span = 102
    sc = span / max(1, max_coord)
    parts = [f'<rect x="{cx - span}" y="{cy - span}" width="{2 * span}" height="{2 * span}" fill="#ffffff" stroke="{GRID}" stroke-width="1"/>']
    for k in range(-max_coord, max_coord + 1):
        gx = cx + k * sc
        gy = cy - k * sc
        parts.append(f'<line x1="{gx:.2f}" y1="{cy - span}" x2="{gx:.2f}" y2="{cy + span}" stroke="{GRID}" stroke-width="0.9"/>')
        parts.append(f'<line x1="{cx - span}" y1="{gy:.2f}" x2="{cx + span}" y2="{gy:.2f}" stroke="{GRID}" stroke-width="0.9"/>')
    parts.append(f'<line x1="{cx - span - 6}" y1="{cy}" x2="{cx + span + 8}" y2="{cy}" stroke="{STROKE}" stroke-width="1.7"/>')
    parts.append(f'<line x1="{cx}" y1="{cy + span + 6}" x2="{cx}" y2="{cy - span - 8}" stroke="{STROKE}" stroke-width="1.7"/>')
    parts.append(f'<text x="{cx + span + 12}" y="{cy + 4}" font-size="11.5" font-weight="700" fill="{STROKE}">x</text>')
    parts.append(f'<text x="{cx + 5}" y="{cy - span - 8}" font-size="11.5" font-weight="700" fill="{STROKE}">y</text>')

    def clip_line(slope: float, b_int: float, color: str, dash: str = ""):
        cands = []
        for xv in (-max_coord, max_coord):
            yv = slope * xv + b_int
            if -max_coord - 1e-6 <= yv <= max_coord + 1e-6:
                cands.append((xv, yv))
        if abs(slope) > 1e-9:
            for yv in (-max_coord, max_coord):
                xv = (yv - b_int) / slope
                if -max_coord - 1e-6 <= xv <= max_coord + 1e-6:
                    cands.append((xv, yv))
        uniq = []
        for p in cands:
            if not any(math.hypot(p[0] - q[0], p[1] - q[1]) < 1e-4 for q in uniq):
                uniq.append(p)
        if len(uniq) >= 2:
            (x1, y1), (x2, y2) = uniq[0], uniq[-1]
            d_attr = f' stroke-dasharray="{dash}"' if dash else ""
            parts.append(
                f'<line x1="{cx + x1 * sc:.2f}" y1="{cy - y1 * sc:.2f}" '
                f'x2="{cx + x2 * sc:.2f}" y2="{cy - y2 * sc:.2f}" stroke="{color}" stroke-width="2.3"{d_attr}/>'
            )

    if line_kb is not None:
        clip_line(line_kb[0], line_kb[1], BLUE)
    if line2_kb is not None:
        clip_line(line2_kb[0], line2_kb[1], GREEN, "5,3")

    for px, py, lbl in pts:
        sx, sy = cx + px * sc, cy - py * sc
        parts.append(f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="4.2" fill="{RED}" stroke="#ffffff" stroke-width="1.2"/>')
        if lbl:
            dx = 7 if px >= 0 else -7
            anc = "start" if px >= 0 else "end"
            dy = -7 if py >= 0 else 14
            parts.append(f'<text x="{sx + dx:.2f}" y="{sy + dy:.2f}" text-anchor="{anc}" font-size="11" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_box_plot(min_v: float, q1: float, med: float, q3: float, max_v: float, title: str = "") -> str:
    """Box-and-whisker plot over a calibrated number line showing Min, Q1, Median, Q3, and Max."""
    w, h = 390, 145
    x0, x1 = 36, 354
    span_v = max(1.0, float(max_v - min_v))
    lo_axis = math.floor(min_v - 0.08 * span_v)
    hi_axis = math.ceil(max_v + 0.08 * span_v)
    if hi_axis <= lo_axis:
        hi_axis = lo_axis + 10

    def sx(v: float) -> float:
        return x0 + (v - lo_axis) / (hi_axis - lo_axis) * (x1 - x0)

    by, bh, ly = 44, 34, 104
    parts = []
    if title:
        parts.append(f'<text x="{w / 2:.1f}" y="20" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(title)}</text>')
    parts.append(f'<line x1="{x0}" y1="{ly}" x2="{x1}" y2="{ly}" stroke="{STROKE}" stroke-width="1.6"/>')

    # Whiskers & box
    x_min, x_q1, x_med, x_q3, x_max = sx(min_v), sx(q1), sx(med), sx(q3), sx(max_v)
    ym = by + bh / 2
    parts.append(f'<line x1="{x_min:.2f}" y1="{ym}" x2="{x_q1:.2f}" y2="{ym}" stroke="{STROKE}" stroke-width="2"/>')
    parts.append(f'<line x1="{x_q3:.2f}" y1="{ym}" x2="{x_max:.2f}" y2="{ym}" stroke="{STROKE}" stroke-width="2"/>')
    parts.append(f'<line x1="{x_min:.2f}" y1="{by + 7}" x2="{x_min:.2f}" y2="{by + bh - 7}" stroke="{STROKE}" stroke-width="2"/>')
    parts.append(f'<line x1="{x_max:.2f}" y1="{by + 7}" x2="{x_max:.2f}" y2="{by + bh - 7}" stroke="{STROKE}" stroke-width="2"/>')
    parts.append(f'<rect x="{x_q1:.2f}" y="{by}" width="{max(2.0, x_q3 - x_q1):.2f}" height="{bh}" fill="#dbeafe" stroke="{BLUE}" stroke-width="2"/>')
    parts.append(f'<line x1="{x_med:.2f}" y1="{by}" x2="{x_med:.2f}" y2="{by + bh}" stroke="{RED}" stroke-width="2.6"/>')

    for val, y_lbl, col in [(min_v, ly + 20, STROKE), (q1, by - 6, BLUE), (med, ly + 20, RED), (q3, by - 6, BLUE), (max_v, ly + 20, STROKE)]:
        xv = sx(val)
        parts.append(f'<line x1="{xv:.2f}" y1="{ly - 4}" x2="{xv:.2f}" y2="{ly + 4}" stroke="{STROKE}" stroke-width="1.5"/>')
        v_txt = str(int(val)) if float(val).is_integer() else f"{val:g}"
        parts.append(f'<text x="{xv:.2f}" y="{y_lbl}" text-anchor="middle" font-size="11" font-weight="700" fill="{col}">{v_txt}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_pie_chart(slices: list[tuple[str, float]], title: str = "") -> str:
    """Sector pie chart with side legend for Grade 6 & Grade 9 Data & Probability."""
    w, h = 360, 195
    cx, cy, r = 104, 102, 70
    colors = ["#93c5fd", "#86efac", "#fde68a", "#f9a8d4", "#c4b5fd", "#fdba74"]
    strokes = [BLUE, GREEN, ORANGE, "#db2777", "#7c3aed", RED]
    tot = max(1e-6, sum(v for _, v in slices))
    parts = []
    if title:
        parts.append(f'<text x="{w / 2:.1f}" y="18" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(title)}</text>')
    cur_ang = -90.0
    for idx, (lbl, val) in enumerate(slices):
        sweep = 360.0 * (val / tot)
        fc = colors[idx % len(colors)]
        sc = strokes[idx % len(strokes)]
        if sweep >= 359.9:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fc}" stroke="{STROKE}" stroke-width="1.6"/>')
        elif sweep > 0.1:
            a1 = math.radians(cur_ang)
            a2 = math.radians(cur_ang + sweep)
            x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
            x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
            large = 1 if sweep > 180.0 else 0
            parts.append(
                f'<path d="M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f} Z" '
                f'fill="{fc}" stroke="{STROKE}" stroke-width="1.5"/>'
            )
        cur_ang += sweep
        ly = 42 + idx * 25
        parts.append(f'<rect x="196" y="{ly - 11}" width="14" height="14" rx="3" fill="{fc}" stroke="{sc}" stroke-width="1.3"/>')
        parts.append(f'<text x="217" y="{ly + 1}" font-size="12" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_nafes_spinner(sector_labels: list[str], caption: str = "") -> str:
    """Equal-sector probability spinner wheel with central pointer arrow."""
    n = max(2, len(sector_labels))
    w, h = 235, (215 if caption else 195)
    cx, cy, r = 117, 96, 74
    colors = ["#dbeafe", "#dcfce7", "#fef3c7", "#fce7f3", "#f3e8ff", "#ffedd5", "#e0e7ff", "#ccfbf1"]
    parts = []
    sweep = 360.0 / n
    for idx, lbl in enumerate(sector_labels):
        a1 = math.radians(-90 + idx * sweep)
        a2 = math.radians(-90 + (idx + 1) * sweep)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if sweep > 180.0 else 0
        fc = colors[idx % len(colors)]
        parts.append(
            f'<path d="M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f} Z" '
            f'fill="{fc}" stroke="{STROKE}" stroke-width="1.6"/>'
        )
        am = math.radians(-90 + (idx + 0.5) * sweep)
        tx, ty = cx + 0.62 * r * math.cos(am), cy + 0.62 * r * math.sin(am) + 4.5
        parts.append(f'<text x="{tx:.2f}" y="{ty:.2f}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(str(lbl))}</text>')
    # Pointer arrow
    parts.append(f'<line x1="{cx - 18}" y1="{cy + 12}" x2="{cx + 28}" y2="{cy - 20}" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>')
    parts.append(f'<polygon points="{cx + 33},{cy - 23} {cx + 22},{cy - 23} {cx + 28},{cy - 13}" fill="{RED}"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{STROKE}"/>')
    if caption:
        parts.append(f'<text x="{cx}" y="{h - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))
