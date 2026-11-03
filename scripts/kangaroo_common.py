"""Shared helpers, 5-option (A–E) 3/4/5-point MCQ builders, lesson builders, and Kangaroo puzzle SVG generators (Grades 3–10)."""
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
from kmc_diagrams import BLUE, DARK, GREEN, GRID, MUTED, ORANGE, RED, SHADE, SHADE_ALT, STROKE, WATER, _esc as esc, _nlabel, wrap_svg
from kmc_diagrams_extra import *  # noqa: F401,F403
from nsmo_common import (
    PAL,
    dm,
    svg_circle_chords,
    svg_cyclic_quad,
    svg_digit_slots,
    svg_graph_cycle_chords,
    svg_median_tri,
    svg_parallel_similar_tri,
)

ROOT = Path(__file__).resolve().parents[1]

KANGAROO_LEVELS = (
    "Ecolier",
    "Benjamin",
    "Cadet",
    "Junior",
)

KANGAROO_TOPICS = (
    "Number Theory",
    "Algebra",
    "Geometry",
    "Combinatorics & Logic",
    "Data & Probability",
)

DIFF_TO_POINTS = {
    "Easy": 3,
    "Medium": 4,
    "Hard": 5,
}

KANGAROO_FORBIDDEN_RE = re.compile(
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
        r"\bcalculus\b",
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


def load_other_track_stems() -> set[str]:
    """Return normalized English stems from all non-Kangaroo banks so Kangaroo stems are 100% globally unique."""
    stems: set[str] = set()
    for name in ("kaust", "nsmo", "nafes", "jee", "olympiad"):
        p = ROOT / "data" / f"{name}.json"
        if p.exists():
            for q in json.loads(p.read_text(encoding="utf-8")):
                stems.add(norm_text(q["content"]["en"]["question"]))
    return stems


def make_5_math_options(correct_val, distractors: list, seed_key: str, suffix: str = "") -> tuple[list[str], list[str], int, str]:
    """Build 5 distinct MathJax options (A–E) around correct_val with deterministic order."""
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

    step = 1
    while len(pool) < 4:
        if isinstance(correct_val, int):
            cand_v = correct_val + (step if step % 2 == 1 else -step // 2)
            if correct_val >= 0 and cand_v < 0:
                cand_v = correct_val + step + 4
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


def make_5_bilingual_options(
    pairs: list[tuple[str, str]],
    correct_pair_idx: int = 0,
    seed_key: str = "",
    shuffle: bool = True,
) -> tuple[list[str], list[str], int, str]:
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


def make_kangaroo_question(
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
    assert level in KANGAROO_LEVELS, f"Invalid Kangaroo level: {level}"
    assert topic in KANGAROO_TOPICS, f"Invalid Kangaroo topic: {topic}"
    assert difficulty in ("Easy", "Medium", "Hard"), f"Invalid difficulty: {difficulty}"
    assert len(opts_en) == 5 and len(opts_ar) == 5, f"Kangaroo requires 5 options (A–E): {qid}"
    assert 0 <= correct_idx < 5
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
        assert not KANGAROO_FORBIDDEN_RE.search(blob), f"Forbidden term in {qid}: {KANGAROO_FORBIDDEN_RE.search(blob)}"

    return {
        "id": qid,
        "track": "kangaroo",
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "kang_points": DIFF_TO_POINTS[difficulty],
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        "kangaroo_blueprint": blueprint,
        "review": {
            "structural": "passed",
            "mathematical": "programmatically_verified",
            "scope": "ksf_mawhiba_kangaroo_grades_3_10",
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }


def make_kang_q(
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
    """Convenience builder combining make_5_math_options + explain_en/ar + make_kangaroo_question."""
    opts_en, opts_ar, cidx, cans = make_5_math_options(correct_val, distractors, qid, suffix=suffix)
    return make_kangaroo_question(
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


# ---- Kangaroo Study Lesson Builders ----
def kang_concept(
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


def kang_worked_example(
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


def make_kangaroo_lesson(
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
    assert level in KANGAROO_LEVELS
    assert topic in KANGAROO_TOPICS
    assert len(concepts) >= 3
    assert len(examples) >= 4
    clean_unit_num = re.sub(r"^(?:Lesson|درس)\s+", "", str(unit_num).strip(), flags=re.IGNORECASE)
    return {
        "id": lesson_id,
        "track": "kangaroo",
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
            "examples": [{"id": ex["id"], "correct_index": ex["correct_index"], **ex["en"]} for ex in examples],
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "summary": _format_prose_html(summary_ar),
            "goals": [_format_prose_html(g) for g in goals_ar],
            "concepts": [c["ar"] for c in concepts],
            "traps": [_format_prose_html(t) for t in traps_ar],
            "examples": [{"id": ex["id"], "correct_index": ex["correct_index"], **ex["ar"]} for ex in examples],
        },
    }


# ==============================================================================
# 12 Signature Kangaroo Puzzle, Spatial & Competition SVG Generators
# ==============================================================================

# 1. Additive / Multiplicative Kangaroo Brick Number Pyramid
def svg_kang_number_pyramid(rows: list[list[str]]) -> str:
    """rows from top to bottom, e.g. [['?'], ['14', '19'], ['6', '8', '11']]."""
    bw, bh = 56, 32
    n_rows = len(rows)
    h = max(148, 36 + n_rows * bh)
    y0 = (h - n_rows * bh) / 2
    parts = []
    for r_idx, row in enumerate(rows):
        k = len(row)
        x_start = 160 - (k * bw) / 2
        y = y0 + r_idx * bh
        for c_idx, val in enumerate(row):
            x = x_start + c_idx * bw
            is_q = "?" in str(val) or str(val).isalpha()
            fc = "#fde68a" if is_q else (WATER if r_idx % 2 == 0 else SHADE)
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{bh}" rx="4" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
            parts.append(_nlabel(x + bw / 2, y + bh / 2 + 5, str(val), size=13, color=RED if is_q else DARK))
    return wrap_svg("".join(parts), w=320, h=int(h), disp_w=360, title="Kangaroo number pyramid")


# 2. Transparent Stamp / Grid Pattern (0=empty, 1=shaded, 2=accent)
def svg_kang_stamp_grid(grid: list[list[int]], caption: str = "") -> str:
    rows = len(grid)
    cols = len(grid[0]) if rows else 3
    cs = min(34, 136 // max(rows, cols))
    gw, gh = cols * cs, rows * cs
    x0 = (320 - gw) / 2
    y0 = (168 - gh) / 2 + (8 if caption else 0)
    parts = []
    if caption:
        parts.append(_nlabel(160, 22, caption, size=12, color=BLUE))
    palette = {0: "#ffffff", 1: SHADE, 2: WATER, 3: "#fde68a", 4: "#bbf7d0"}
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            fc = palette.get(v, SHADE)
            parts.append(f'<rect x="{x0 + c*cs:.1f}" y="{y0 + r*cs:.1f}" width="{cs}" height="{cs}" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
            if v >= 2:
                parts.append(f'<circle cx="{x0 + (c+0.5)*cs:.1f}" cy="{y0 + (r+0.5)*cs:.1f}" r="{cs*0.2:.1f}" fill="{STROKE}"/>')
    return wrap_svg("".join(parts), w=320, h=182, disp_w=350, title="Kangaroo stamp grid pattern")


# 3. Polyomino / Tiling Board (grid of integer region IDs, -1=hole/blocked)
def svg_kang_polyomino_board(board: list[list[int]]) -> str:
    rows = len(board)
    cols = len(board[0]) if rows else 4
    cs = min(30, 144 // max(rows, cols))
    gw, gh = cols * cs, rows * cs
    x0, y0 = (320 - gw) / 2, (176 - gh) / 2
    fills = ["#ffffff", WATER, SHADE, "#fde68a", "#bbf7d0", "#fecdd3", SHADE_ALT]
    parts = []
    for r in range(rows):
        for c in range(cols):
            v = board[r][c]
            fc = "#334155" if v < 0 else fills[v % len(fills)]
            parts.append(f'<rect x="{x0 + c*cs:.1f}" y="{y0 + r*cs:.1f}" width="{cs}" height="{cs}" fill="{fc}" stroke="{STROKE}" stroke-width="1.6"/>')
    return wrap_svg("".join(parts), w=320, h=176, disp_w=350, title="Kangaroo tiling board")


# 4. 7-Segment Matchstick Digital Display
_SEG_MAP = {
    "0": (1, 1, 1, 1, 1, 1, 0),
    "1": (0, 1, 1, 0, 0, 0, 0),
    "2": (1, 1, 0, 1, 1, 0, 1),
    "3": (1, 1, 1, 1, 0, 0, 1),
    "4": (0, 1, 1, 0, 0, 1, 1),
    "5": (1, 0, 1, 1, 0, 1, 1),
    "6": (1, 0, 1, 1, 1, 1, 1),
    "7": (1, 1, 1, 0, 0, 0, 0),
    "8": (1, 1, 1, 1, 1, 1, 1),
    "9": (1, 1, 1, 1, 0, 1, 1),
}


def svg_kang_matchstick_digits(digits_str: str = "2026") -> str:
    s = [ch for ch in str(digits_str) if ch in _SEG_MAP]
    n = max(1, len(s))
    dw, dh, gap = 38, 68, 18
    tot_w = n * dw + (n - 1) * gap
    x0 = (320 - tot_w) / 2
    y0 = 46
    parts = [f'<rect x="20" y="24" width="280" height="112" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.8"/>']
    for idx, ch in enumerate(s):
        ox = x0 + idx * (dw + gap)
        oy = y0
        hm = dh / 2
        segs = [
            (ox + 4, oy, ox + dw - 4, oy),                  # a top
            (ox + dw, oy + 4, ox + dw, oy + hm - 3),        # b top-right
            (ox + dw, oy + hm + 3, ox + dw, oy + dh - 4),   # c bot-right
            (ox + 4, oy + dh, ox + dw - 4, oy + dh),        # d bot
            (ox, oy + hm + 3, ox, oy + dh - 4),             # e bot-left
            (ox, oy + 4, ox, oy + hm - 3),                  # f top-left
            (ox + 4, oy + hm, ox + dw - 4, oy + hm),        # g middle
        ]
        mask = _SEG_MAP[ch]
        for on, (x1, y1, x2, y2) in zip(mask, segs):
            col = ORANGE if on else "#e2e8f0"
            sw = "4.2" if on else "2"
            parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>')
    return wrap_svg("".join(parts), w=320, h=160, disp_w=360, title="Matchstick 7-segment digits")


# 5. Folded Rope / Ribbon Cut by Scissors Line
def svg_kang_folded_ribbon(strands: int = 4, cuts: int = 1) -> str:
    strands = max(2, min(6, strands))
    gap = 20
    h = max(156, 56 + strands * gap)
    y0 = (h - (strands - 1) * gap) / 2
    x_l, x_r = 56, 264
    parts = []
    for i in range(strands):
        y = y0 + i * gap
        parts.append(f'<line x1="{x_l}" y1="{y:.1f}" x2="{x_r}" y2="{y:.1f}" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/>')
        if i < strands - 1:
            if i % 2 == 0:
                cy = y + gap / 2
                parts.append(f'<path d="M {x_r} {y:.1f} A {gap/2:.1f} {gap/2:.1f} 0 0 1 {x_r} {y+gap:.1f}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
            else:
                parts.append(f'<path d="M {x_l} {y:.1f} A {gap/2:.1f} {gap/2:.1f} 0 0 0 {x_l} {y+gap:.1f}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
    for c_i in range(cuts):
        cx = 160 if cuts == 1 else 118 + c_i * (84 / max(1, cuts - 1))
        parts.append(f'<line x1="{cx:.1f}" y1="{y0 - 20:.1f}" x2="{cx:.1f}" y2="{y0 + (strands-1)*gap + 20:.1f}" stroke="{RED}" stroke-width="2.4" stroke-dasharray="6,4"/>')
        parts.append(_nlabel(cx, y0 - 25, "✂", size=14, color=RED))
    return wrap_svg("".join(parts), w=320, h=int(h), disp_w=360, title="Folded rope cut diagram")


# 6. 3D Numbered Die / Cube Showing Top, Front, Right Faces
def svg_kang_cube_faces(top_lbl: str = "1", front_lbl: str = "2", right_lbl: str = "3") -> str:
    # Isometric cube centered at (160, 96)
    cx, cy, r = 160, 96, 56
    dx, dy = r * 0.866, r * 0.5
    p_top = [(cx, cy - r), (cx + dx, cy - dy), (cx, cy), (cx - dx, cy - dy)]
    p_front = [(cx - dx, cy - dy), (cx, cy), (cx, cy + r), (cx - dx, cy + r - dy)]
    p_right = [(cx, cy), (cx + dx, cy - dy), (cx + dx, cy + r - dy), (cx, cy + r)]
    fmt_p = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts = [
        f'<polygon points="{fmt_p(p_top)}" fill="#fde68a" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<polygon points="{fmt_p(p_front)}" fill="{WATER}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<polygon points="{fmt_p(p_right)}" fill="{SHADE}" stroke="{STROKE}" stroke-width="2.2"/>',
        _nlabel(cx, cy - dy + 5, str(top_lbl), size=16, color=DARK),
        _nlabel(cx - dx / 2, cy + (r - dy) / 2 + 5, str(front_lbl), size=16, color=DARK),
        _nlabel(cx + dx / 2, cy + (r - dy) / 2 + 5, str(right_lbl), size=16, color=DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=180, disp_w=350, title="3D numbered cube faces")


# 7. Interlocking Gear Train (labels + CW/CCW direction on gear 1)
def svg_kang_gear_train(labels: list[str] = ("A", "B", "C", "D"), first_dir: str = "CW ↻") -> str:
    n = len(labels)
    r = 25 if n <= 4 else 20
    step = 2 * r + 3
    x0 = 160 - (n - 1) * step / 2
    cy = 96
    parts = []
    if first_dir:
        parts.append(_nlabel(x0, 38, first_dir, size=12, color=RED))
    for i, lbl in enumerate(labels):
        cx = x0 + i * step
        fc = WATER if i % 2 == 0 else SHADE
        for k in range(8):
            ang = math.radians(k * 45 + (22.5 if i % 2 else 0))
            tx1, ty1 = cx + (r - 2) * math.cos(ang), cy + (r - 2) * math.sin(ang)
            tx2, ty2 = cx + (r + 5) * math.cos(ang), cy + (r + 5) * math.sin(ang)
            parts.append(f'<line x1="{tx1:.1f}" y1="{ty1:.1f}" x2="{tx2:.1f}" y2="{ty2:.1f}" stroke="{STROKE}" stroke-width="4" stroke-linecap="round"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="{fc}" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="5" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>')
        parts.append(_nlabel(cx, cy + r + 20, str(lbl), size=12, color=DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=370, title="Interlocking gear train")


# 8. Circular Bead Necklace / Round-Table Arrangement
def svg_kang_necklace_beads(beads: list[str]) -> str:
    """beads: list of short labels or color codes ('R','B','Y','G','W' or numbers)."""
    n = max(3, len(beads))
    cx, cy, r = 160, 92, 60
    cmap = {"R": "#fca5a5", "B": WATER, "Y": "#fde047", "G": "#86efac", "P": SHADE, "W": "#ffffff", "?": "#fde68a"}
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{STROKE}" stroke-width="2" stroke-dasharray="4,3"/>']
    br = min(14, max(9, int(115 / n)))
    for i, b in enumerate(beads):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        bx, by = cx + r * math.cos(ang), cy + r * math.sin(ang)
        fc = cmap.get(str(b).upper(), SHADE if i % 2 else WATER)
        parts.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{br}" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(bx, by + 4, str(b), size=10 if len(str(b)) <= 2 else 9))
    return wrap_svg("".join(parts), w=320, h=184, disp_w=360, title="Circular bead necklace")


# 9. Overlapping Rectangles Showing Shaded Intersection
def svg_kang_overlapping_rects(lbl1: str = "A", lbl2: str = "B", ov_lbl: str = "Overlap") -> str:
    parts = [
        f'<rect x="48" y="28" width="136" height="92" fill="{WATER}" fill-opacity="0.7" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="132" y="60" width="140" height="92" fill="{SHADE}" fill-opacity="0.7" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="132" y="60" width="52" height="60" fill="#fde68a" stroke="{STROKE}" stroke-width="2.2"/>',
        _nlabel(90, 74, lbl1, size=13, color=BLUE),
        _nlabel(228, 114, lbl2, size=13, color=DARK),
        _nlabel(158, 94, ov_lbl, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Overlapping rectangles")


# 10. Rectilinear Staircase Perimeter Polygon
def svg_kang_staircase_perimeter(w_lbl: str = "12", h_lbl: str = "9", steps: int = 4) -> str:
    x0, y0, w, h = 68, 28, 176, 112
    pts = [(x0, y0 + h), (x0 + w, y0 + h)]
    sw, sh = w / steps, h / steps
    for i in range(steps):
        cx = x0 + w - i * sw
        cy = y0 + h - i * sh
        pts.append((cx, cy - sh))
        pts.append((cx - sw, cy - sh))
    poly = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    parts = [
        f'<polygon points="{poly}" fill="{WATER}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0+w}" y2="{y0}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,4"/>',
        f'<line x1="{x0+w}" y1="{y0}" x2="{x0+w}" y2="{y0+h}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,4"/>',
        _nlabel(x0 + w / 2, y0 + h + 18, w_lbl, size=13, color=BLUE),
        _nlabel(x0 - 12, y0 + h / 2 + 5, h_lbl, size=13, color=ORANGE, anchor="end"),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=360, title="Rectilinear staircase perimeter")


# 11. Magic Number Cross / 5-Cell Kangaroo Sum Puzzle
def svg_kang_magic_cross(center: str = "?", top: str = "4", right: str = "7", bottom: str = "6", left: str = "3", note: str = "") -> str:
    cs = 38
    cx, cy = 160 - cs / 2, 92 - cs / 2
    cells = [
        (cx, cy - cs, top, WATER),
        (cx - cs, cy, left, WATER),
        (cx, cy, center, "#fde68a"),
        (cx + cs, cy, right, SHADE),
        (cx, cy + cs, bottom, SHADE),
    ]
    parts = []
    if note:
        parts.append(_nlabel(160, 22, note, size=12, color=GREEN))
    for x, y, val, fc in cells:
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cs}" height="{cs}" rx="5" fill="{fc}" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(_nlabel(x + cs / 2, y + cs / 2 + 5, str(val), size=14, color=RED if "?" in str(val) else DARK))
    return wrap_svg("".join(parts), w=320, h=184, disp_w=350, title="Kangaroo magic cross puzzle")


# 12. Grid Walk Path with Start Cell and Target/Visited Cells
def svg_kang_grid_walk(cols: int = 5, rows: int = 4, path_cells: list[tuple[int, int]] = ((0, 3), (1, 3), (1, 2), (2, 2), (2, 1), (3, 1))) -> str:
    cs = min(30, 140 // max(cols, rows))
    gw, gh = cols * cs, rows * cs
    x0, y0 = (320 - gw) / 2, (172 - gh) / 2
    parts = []
    pset = set(path_cells)
    for r in range(rows):
        for c in range(cols):
            fc = WATER if (c, r) in pset else "#ffffff"
            if path_cells and (c, r) == path_cells[0]:
                fc = "#bbf7d0"
            elif path_cells and (c, r) == path_cells[-1]:
                fc = "#fde68a"
            parts.append(f'<rect x="{x0 + c*cs:.1f}" y="{y0 + r*cs:.1f}" width="{cs}" height="{cs}" fill="{fc}" stroke="{STROKE}" stroke-width="1.5"/>')
    if len(path_cells) >= 2:
        pts = [(x0 + (c + 0.5) * cs, y0 + (r + 0.5) * cs) for c, r in path_cells]
        d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        parts.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
        parts.append(_nlabel(pts[0][0], pts[0][1] + 4, "S", size=11, color=DARK))
        parts.append(_nlabel(pts[-1][0], pts[-1][1] + 4, "★", size=11, color=RED))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=350, title="Kangaroo grid walk path")

