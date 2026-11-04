"""Shared helpers, 5-option (A–E) 3/4/5-point MCQ builders, lesson builders, and Kangaroo puzzle SVG generators (Grades 1–12)."""
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
    "PreEcolier",
    "Ecolier",
    "Benjamin",
    "Cadet",
    "Junior",
    "Student",
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
            "scope": "ksf_mawhiba_kangaroo_grades_1_12",
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



# ==============================================================================
# PreEcolier (Grades 1–2) Visual Picture-Puzzle SVG Generators
# ==============================================================================

def svg_pre_tens_ones_blocks(tens: int = 3, ones: int = 4, badge_lbl: str = "?") -> str:
    """Base-10 rods (stacks of 10) and unit cubes for Grades 1–2 two-digit place-value puzzles."""
    tens = max(0, min(9, int(tens)))
    ones = max(0, min(9, int(ones)))
    parts = [f'<rect x="14" y="14" width="292" height="146" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>']
    rx0 = 28
    for t in range(tens):
        rx = rx0 + t * 18
        for k in range(10):
            ry = 128 - (k + 1) * 9
            parts.append(f'<rect x="{rx}" y="{ry}" width="13" height="9" fill="{WATER}" stroke="{STROKE}" stroke-width="1.1"/>')
    if tens > 0:
        parts.append(_nlabel(rx0 + (tens * 18 - 5) / 2, 148, f"{tens} Tens", size=11, color=BLUE))
    ox0 = max(172, rx0 + tens * 18 + 14)
    for u in range(ones):
        col = u % 3
        row = u // 3
        ux = ox0 + col * 18
        uy = 114 - row * 18
        parts.append(f'<rect x="{ux}" y="{uy}" width="14" height="14" rx="2" fill="#fde68a" stroke="{STROKE}" stroke-width="1.3"/>')
    if ones > 0:
        parts.append(_nlabel(ox0 + 24, 148, f"{ones} Ones", size=11, color=ORANGE))
    bw = max(54, 16 + len(str(badge_lbl)) * 9)
    bx = 294 - bw
    parts.append(f'<rect x="{bx:.1f}" y="24" width="{bw:.1f}" height="32" rx="8" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(_nlabel(bx + bw / 2, 45, str(badge_lbl), size=13, color=RED if "?" in str(badge_lbl) else DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Tens and ones blocks")


def _draw_pre_icon(kind: str, cx: float, cy: float, r: float = 13) -> str:
    k = kind.lower()
    if k in ("star", "★"):
        pts = []
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            rad = r if i % 2 == 0 else r * 0.45
            pts.append(f"{cx + rad * math.cos(ang):.1f},{cy + rad * math.sin(ang):.1f}")
        return f'<polygon points="{" ".join(pts)}" fill="#facc15" stroke="{STROKE}" stroke-width="1.5"/>'
    if k in ("heart", "♥"):
        return f'<circle cx="{cx - r*0.32:.1f}" cy="{cy - r*0.18:.1f}" r="{r*0.48:.1f}" fill="#fb7185" stroke="{STROKE}" stroke-width="1.3"/><circle cx="{cx + r*0.32:.1f}" cy="{cy - r*0.18:.1f}" r="{r*0.48:.1f}" fill="#fb7185" stroke="{STROKE}" stroke-width="1.3"/><polygon points="{cx - r*0.76:.1f},{cy - r*0.02:.1f} {cx + r*0.76:.1f},{cy - r*0.02:.1f} {cx:.1f},{cy + r*0.85:.1f}" fill="#fb7185" stroke="{STROKE}" stroke-width="1.3"/>'
    if k in ("diamond", "◆"):
        return f'<polygon points="{cx:.1f},{cy-r:.1f} {cx+r*0.85:.1f},{cy:.1f} {cx:.1f},{cy+r:.1f} {cx-r*0.85:.1f},{cy:.1f}" fill="{WATER}" stroke="{STROKE}" stroke-width="1.6"/>'
    if k in ("square", "■"):
        return f'<rect x="{cx-r*0.8:.1f}" y="{cy-r*0.8:.1f}" width="{r*1.6:.1f}" height="{r*1.6:.1f}" rx="3" fill="#86efac" stroke="{STROKE}" stroke-width="1.6"/>'
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*0.85:.1f}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.6"/>'


def svg_pre_icon_addition(eq1_icons: list[str], eq1_rhs: str, eq2_icons: list[str], eq2_rhs: str = "?") -> str:
    """Two-row visual icon equation board for Grades 1–2 picture-addition puzzles."""
    parts = [f'<rect x="16" y="16" width="288" height="140" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.8"/>']
    for row_i, (icons, rhs) in enumerate(((eq1_icons, eq1_rhs), (eq2_icons, eq2_rhs))):
        cy = 56 + row_i * 60
        n = max(1, len(icons))
        step = min(52, 168 // max(1, n))
        x0 = 42
        for idx, ic in enumerate(icons):
            cx = x0 + idx * step
            parts.append(_draw_pre_icon(ic, cx, cy, 13))
            if idx < n - 1:
                parts.append(_nlabel(cx + step / 2, cy + 5, "+", size=14, color=DARK))
        eq_x = x0 + (n - 1) * step + 28
        parts.append(_nlabel(eq_x, cy + 5, "=", size=15, color=DARK))
        bw = max(48, 16 + len(str(rhs)) * 9)
        bx = min(288 - bw, eq_x + 18)
        fc = "#fde68a" if "?" in str(rhs) else "#ffffff"
        parts.append(f'<rect x="{bx:.1f}" y="{cy - 16:.1f}" width="{bw:.1f}" height="32" rx="7" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        parts.append(_nlabel(bx + bw / 2, cy + 5, str(rhs), size=14, color=RED if "?" in str(rhs) else DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Picture icon addition puzzle")


def svg_pre_paired_items(total: int = 9, caption: str = "") -> str:
    """Visual pairs of colorful tokens/mittens to show even/odd pairing and leftovers for Grades 1–2."""
    total = max(2, min(19, int(total)))
    pairs = total // 2
    rem = total % 2
    cols = pairs + rem
    step = min(38, 260 // max(1, cols))
    x0 = 160 - (cols - 1) * step / 2
    parts = [f'<rect x="16" y="16" width="288" height="140" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>']
    if caption:
        parts.append(_nlabel(160, 36, caption, size=12, color=BLUE))
    y_top, y_bot = (68, 108) if caption else (62, 104)
    for p in range(pairs):
        cx = x0 + p * step
        parts.append(f'<rect x="{cx - 13:.1f}" y="{y_top - 15}" width="26" height="62" rx="10" fill="#e0f2fe" stroke="{BLUE}" stroke-width="1.2" stroke-dasharray="3,2"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{y_top}" r="9" fill="{WATER}" stroke="{STROKE}" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{y_bot}" r="9" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.5"/>')
    if rem:
        cx = x0 + pairs * step
        parts.append(f'<circle cx="{cx:.1f}" cy="{(y_top + y_bot)/2:.1f}" r="10" fill="#fde68a" stroke="{RED}" stroke-width="2"/>')
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Paired items even-odd diagram")


def svg_pre_die_dots(top_dots: int = 1, front_dots: int = 2, right_dots: int = 3) -> str:
    """Isometric 3D die showing pip dots (1..6) on the top, front-left, and front-right faces."""
    cx, cy, r = 160, 96, 58
    dx, dy = r * 0.866, r * 0.5
    p_top = [(cx, cy - r), (cx + dx, cy - dy), (cx, cy), (cx - dx, cy - dy)]
    p_front = [(cx - dx, cy - dy), (cx, cy), (cx, cy + r), (cx - dx, cy + r - dy)]
    p_right = [(cx, cy), (cx + dx, cy - dy), (cx + dx, cy + r - dy), (cx, cy + r)]
    fmt_p = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts = [
        f'<polygon points="{fmt_p(p_top)}" fill="#fef9c3" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<polygon points="{fmt_p(p_front)}" fill="{WATER}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<polygon points="{fmt_p(p_right)}" fill="{SHADE}" stroke="{STROKE}" stroke-width="2.2"/>',
    ]
    pip_uv = {
        1: [(0.5, 0.5)],
        2: [(0.28, 0.28), (0.72, 0.72)],
        3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
        4: [(0.28, 0.28), (0.72, 0.28), (0.28, 0.72), (0.72, 0.72)],
        5: [(0.26, 0.26), (0.74, 0.26), (0.5, 0.5), (0.26, 0.74), (0.74, 0.74)],
        6: [(0.28, 0.24), (0.72, 0.24), (0.28, 0.5), (0.72, 0.5), (0.28, 0.76), (0.72, 0.76)],
    }

    def bilerp(quad, u, v):
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = quad
        x = (1 - u) * (1 - v) * x0 + u * (1 - v) * x1 + u * v * x2 + (1 - u) * v * x3
        y = (1 - u) * (1 - v) * y0 + u * (1 - v) * y1 + u * v * y2 + (1 - u) * v * y3
        return x, y

    for quad, cnt in ((p_top, top_dots), (p_front, front_dots), (p_right, right_dots)):
        if cnt in pip_uv:
            for u, v in pip_uv[cnt]:
                px, py = bilerp(quad, u, v)
                parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.1" fill="{DARK}"/>')
        else:
            px, py = bilerp(quad, 0.5, 0.5)
            parts.append(_nlabel(px, py + 5, "?", size=16, color=RED))
    return wrap_svg("".join(parts), w=320, h=180, disp_w=350, title="3D die with pip dots")


def svg_pre_coin_purse(coins: list[str], tag_lbl: str = "Price: ?") -> str:
    """Visual coins (1, 2, 5, 10) arranged beside a price tag for Grades 1–2 money puzzles."""
    n = max(1, len(coins))
    parts = [f'<rect x="14" y="16" width="292" height="140" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>']
    bw = max(92, 22 + len(str(tag_lbl)) * 7.5)
    bx = 160 - bw / 2
    parts.append(f'<rect x="{bx:.1f}" y="24" width="{bw:.1f}" height="28" rx="7" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.6"/>')
    parts.append(_nlabel(160, 43, str(tag_lbl), size=12, color=RED if "?" in str(tag_lbl) else DARK))
    cols = min(6, n)
    step = min(44, 252 // cols)
    for idx, c in enumerate(coins[:12]):
        r_i = idx // cols
        c_i = idx % cols
        row_cnt = min(cols, len(coins[:12]) - r_i * cols)
        x0 = 160 - (row_cnt - 1) * step / 2
        cx = x0 + c_i * step
        cy = 84 + r_i * 40 if len(coins) > cols else 102
        fc = "#fde047" if str(c) in ("5", "10") else WATER
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="16" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(cx, cy + 5, str(c), size=12, color=DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Coin purse puzzle")


def svg_pre_queue_line(shown_slots: int = 7, star_idx: int = 3, front_lbl: str = "Front", back_lbl: str = "Back") -> str:
    """Row of children/badges highlighting one starred child's spot from Front and Back."""
    n = max(3, min(11, int(shown_slots)))
    step = min(32, 240 // n)
    x0 = 160 - (n - 1) * step / 2
    parts = [
        f'<line x1="{x0 - 12:.1f}" y1="112" x2="{x0 + (n-1)*step + 12:.1f}" y2="112" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4,3"/>',
        _nlabel(x0, 36, front_lbl, size=11, color=BLUE),
        _nlabel(x0 + (n - 1) * step, 36, back_lbl, size=11, color=ORANGE),
    ]
    for i in range(n):
        cx = x0 + i * step
        is_star = (i == star_idx)
        fc = "#fde68a" if is_star else WATER
        parts.append(f'<circle cx="{cx:.1f}" cy="74" r="9" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        parts.append(f'<rect x="{cx - 8:.1f}" y="85" width="16" height="24" rx="5" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        if is_star:
            parts.append(_nlabel(cx, 78, "★", size=10, color=RED))
            parts.append(_nlabel(cx, 134, "★", size=12, color=RED))
    return wrap_svg("".join(parts), w=320, h=164, disp_w=360, title="Queue position diagram")


def svg_pre_marble_bag(counts: list[tuple[str, int]], top_lbl: str = "Blindfold Pick") -> str:
    """Pouch showing color groups of marbles (e.g. [('R', 4), ('B', 3), ('G', 2)]) for worst-case picks."""
    cmap = {"R": "#fca5a5", "B": WATER, "Y": "#fde047", "G": "#86efac", "P": SHADE, "W": "#ffffff"}
    parts = [
        f'<rect x="28" y="38" width="264" height="118" rx="22" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(160, 26, top_lbl, size=12, color=BLUE),
    ]
    k = max(1, len(counts))
    col_w = 240 / k
    for idx, (col_code, cnt) in enumerate(counts):
        cx = 40 + (idx + 0.5) * col_w
        fc = cmap.get(col_code[0].upper(), SHADE)
        shown = min(6, max(1, int(cnt)))
        for m_i in range(shown):
            mx = cx + ((m_i % 3) - 1) * 16
            my = 74 + (m_i // 3) * 18
            parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="7" fill="{fc}" stroke="{STROKE}" stroke-width="1.4"/>')
        parts.append(_nlabel(cx, 138, f"{col_code}: {cnt}", size=11, color=DARK))
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Marble bag puzzle")


def svg_pre_shape_collage(tri_count: int = 3, sq_count: int = 2, cir_count: int = 2) -> str:
    """Scattered non-overlapping triangles, squares, and circles on a card for Grades 1–2 shape/corner counting."""
    anchors = [
        (58, 56), (126, 52), (196, 58), (262, 54),
        (68, 118), (138, 122), (208, 116), (266, 120),
        (96, 86), (168, 88), (234, 88),
    ]
    shapes = (["T"] * tri_count + ["S"] * sq_count + ["C"] * cir_count)[:len(anchors)]
    parts = [f'<rect x="18" y="18" width="284" height="138" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>']
    for (cx, cy), kind in zip(anchors, shapes):
        if kind == "T":
            parts.append(f'<polygon points="{cx},{cy-16} {cx+16},{cy+13} {cx-16},{cy+13}" fill="#fde68a" stroke="{STROKE}" stroke-width="1.8"/>')
        elif kind == "S":
            parts.append(f'<rect x="{cx-14}" y="{cy-14}" width="28" height="28" fill="{WATER}" stroke="{STROKE}" stroke-width="1.8"/>')
        else:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="#bbf7d0" stroke="{STROKE}" stroke-width="1.8"/>')
    return wrap_svg("".join(parts), w=320, h=172, disp_w=360, title="Geometric shape collage")


# ==============================================================================
# Student Division (Grades 11–12) Competition SVG Generators
# ==============================================================================

def svg_stu_ceva_triangle(af_lbl: str = "2", fb_lbl: str = "3", bd_lbl: str = "4", dc_lbl: str = "?", ce_lbl: str = "3", ea_lbl: str = "2") -> str:
    """Triangle ABC with concurrent cevians AD, BE, CF meeting at interior point P."""
    ax, ay = 156, 22
    bx, by = 46, 150
    cx, cy = 274, 150
    dx, dy = (bx + cx) / 2 + 8, 150
    ex, ey = (ax + cx) / 2 + 6, (ay + cy) / 2 + 6
    fx, fy = (ax + bx) / 2 - 4, (ay + by) / 2 + 4
    # Intersection of AD and BE
    denom = (ax - dx) * (by - ey) - (ay - dy) * (bx - ex)
    px = ((ax * dy - ay * dx) * (bx - ex) - (ax - dx) * (bx * ey - by * ex)) / denom
    py = ((ax * dy - ay * dx) * (by - ey) - (ay - dy) * (bx * ey - by * ex)) / denom
    fx2_d = (cx - px) * (by - ay) - (cy - py) * (bx - ax)
    if abs(fx2_d) > 1e-6:
        fx = ((cx * py - cy * px) * (bx - ax) - (cx - px) * (bx * ay - by * ax)) / fx2_d
        fy = ((cx * py - cy * px) * (by - ay) - (cy - py) * (bx * ay - by * ax)) / fx2_d
    parts = [
        f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{dx:.1f}" y2="{dy:.1f}" stroke="{BLUE}" stroke-width="1.7"/>',
        f'<line x1="{bx}" y1="{by}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{ORANGE}" stroke-width="1.7"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{fx:.1f}" y2="{fy:.1f}" stroke="{GREEN}" stroke-width="1.7"/>',
        f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{RED}"/>',
        _nlabel(ax, ay - 6, "A", size=12, color=DARK),
        _nlabel(bx - 12, by + 4, "B", size=12, color=DARK),
        _nlabel(cx + 12, cy + 4, "C", size=12, color=DARK),
        _nlabel(dx, dy + 15, "D", size=11, color=BLUE),
        _nlabel(ex + 12, ey, "E", size=11, color=ORANGE),
        _nlabel(fx - 12, fy, "F", size=11, color=GREEN),
        _nlabel((ax + fx) / 2 - 12, (ay + fy) / 2, af_lbl, size=11, color=RED if "?" in str(af_lbl) else BLUE),
        _nlabel((fx + bx) / 2 - 12, (fy + by) / 2, fb_lbl, size=11, color=RED if "?" in str(fb_lbl) else BLUE),
        _nlabel((bx + dx) / 2, by + 15, bd_lbl, size=11, color=RED if "?" in str(bd_lbl) else DARK),
        _nlabel((dx + cx) / 2, cy + 15, dc_lbl, size=11, color=RED if "?" in str(dc_lbl) else DARK),
        _nlabel((cx + ex) / 2 + 13, (cy + ey) / 2, ce_lbl, size=11, color=RED if "?" in str(ce_lbl) else ORANGE),
        _nlabel((ex + ax) / 2 + 13, (ey + ay) / 2, ea_lbl, size=11, color=RED if "?" in str(ea_lbl) else ORANGE),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Ceva concurrent cevians triangle")


def svg_stu_tangent_circles(r1_lbl: str = "9", r2_lbl: str = "4", d_lbl: str = "AB = ?") -> str:
    """Two externally tangent circles resting on a horizontal common external tangent line AB."""
    y_line = 144
    r1, r2 = 46, 26
    x1 = 112
    dx = 2 * math.sqrt(r1 * r2)
    x2 = x1 + dx
    c1y, c2y = y_line - r1, y_line - r2
    parts = [
        f'<line x1="36" y1="{y_line}" x2="284" y2="{y_line}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<circle cx="{x1:.1f}" cy="{c1y:.1f}" r="{r1}" fill="{WATER}" fill-opacity="0.55" stroke="{STROKE}" stroke-width="2"/>',
        f'<circle cx="{x2:.1f}" cy="{c2y:.1f}" r="{r2}" fill="{SHADE}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{x1:.1f}" y1="{c1y:.1f}" x2="{x1:.1f}" y2="{y_line}" stroke="{BLUE}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        f'<line x1="{x2:.1f}" y1="{c2y:.1f}" x2="{x2:.1f}" y2="{y_line}" stroke="{ORANGE}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        f'<line x1="{x1:.1f}" y1="{c1y:.1f}" x2="{x2:.1f}" y2="{c2y:.1f}" stroke="{RED}" stroke-width="1.8"/>',
        _nlabel(x1 - 14, (c1y + y_line) / 2 + 4, r1_lbl, size=11, color=BLUE),
        _nlabel(x2 + 14, (c2y + y_line) / 2 + 4, r2_lbl, size=11, color=ORANGE),
        _nlabel(x1, y_line + 16, "A", size=11, color=DARK),
        _nlabel(x2, y_line + 16, "B", size=11, color=DARK),
        _nlabel((x1 + x2) / 2, y_line + 18, d_lbl, size=12, color=RED if "?" in str(d_lbl) else DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=174, disp_w=370, title="Externally tangent circles and common tangent")


def svg_stu_tangential_quad(top_lbl: str = "a", right_lbl: str = "b", bot_lbl: str = "c", left_lbl: str = "d", r_lbl: str = "r") -> str:
    """Tangential quadrilateral circumscribed around an inscribed circle (Pitot's Theorem a + c = b + d)."""
    cx, cy, r = 160, 92, 46
    # Isosceles-like tangential trapezoid/quad around circle (cx, cy, r)
    pts = [(114, 46), (206, 46), (236, 138), (84, 138)]
    poly = " ".join(f"{x},{y}" for x, y in pts)
    parts = [
        f'<polygon points="{poly}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WATER}" fill-opacity="0.55" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy + r}" stroke="{RED}" stroke-width="1.7" stroke-dasharray="4,3"/>',
        f'<circle cx="{cx}" cy="{cy}" r="3" fill="{DARK}"/>',
        _nlabel(cx, 36, top_lbl, size=12, color=RED if "?" in str(top_lbl) else BLUE),
        _nlabel(cx, 156, bot_lbl, size=12, color=RED if "?" in str(bot_lbl) else BLUE),
        _nlabel(76, 96, left_lbl, size=12, color=RED if "?" in str(left_lbl) else ORANGE, anchor="end"),
        _nlabel(244, 96, right_lbl, size=12, color=RED if "?" in str(right_lbl) else ORANGE, anchor="start"),
        _nlabel(cx + 12, cy + r / 2 + 4, r_lbl, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=174, disp_w=360, title="Tangential quadrilateral with incircle")


def svg_stu_sphere_in_cylinder(r_lbl: str = "R", h_lbl: str = "2R") -> str:
    """Sphere inscribed inside a right circular cylinder (Archimedes 2:3 ratio)."""
    cx, cy, r = 152, 92, 52
    ry = 14
    parts = [
        f'<rect x="{cx - r}" y="{cy - r}" width="{2*r}" height="{2*r}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<ellipse cx="{cx}" cy="{cy - r}" rx="{r}" ry="{ry}" fill="#e2e8f0" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<ellipse cx="{cx}" cy="{cy + r}" rx="{r}" ry="{ry}" fill="none" stroke="{STROKE}" stroke-width="1.8" stroke-dasharray="4,3"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WATER}" fill-opacity="0.6" stroke="{BLUE}" stroke-width="2.1"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{ry}" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4,3"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{RED}" stroke-width="1.8"/>',
        _nlabel(cx + r / 2, cy - 6, r_lbl, size=12, color=RED),
        f'<line x1="{cx + r + 20}" y1="{cy - r}" x2="{cx + r + 20}" y2="{cy + r}" stroke="{ORANGE}" stroke-width="1.8"/>',
        _nlabel(cx + r + 28, cy + 4, h_lbl, size=12, color=ORANGE, anchor="start"),
    ]
    return wrap_svg("".join(parts), w=320, h=180, disp_w=360, title="Sphere inscribed in cylinder")


def svg_stu_cone_frustum(H_lbl: str = "H", h_lbl: str = "h", R_lbl: str = "R") -> str:
    """Right circular cone sliced by a horizontal plane showing similar upper cone and lower frustum."""
    ax, ay = 148, 22
    by = 146
    R = 64
    sy = 84
    r_mid = R * (sy - ay) / (by - ay)
    parts = [
        f'<polygon points="{ax},{ay} {ax - R},{by} {ax + R},{by}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{ax - r_mid:.1f},{sy} {ax + r_mid:.1f},{sy} {ax + R},{by} {ax - R},{by}" fill="{WATER}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<ellipse cx="{ax}" cy="{by}" rx="{R}" ry="13" fill="{WATER}" fill-opacity="0.75" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<ellipse cx="{ax}" cy="{sy}" rx="{r_mid:.1f}" ry="8" fill="#bae6fd" stroke="{BLUE}" stroke-width="1.6"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{by}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,3"/>',
        f'<line x1="{ax}" y1="{by}" x2="{ax + R}" y2="{by}" stroke="{RED}" stroke-width="1.7"/>',
        _nlabel(ax + R / 2, by - 4, R_lbl, size=11, color=RED),
        _nlabel(ax - R - 18, (ay + by) / 2, H_lbl, size=12, color=DARK),
        _nlabel(ax + r_mid + 24, (ay + sy) / 2 + 4, h_lbl, size=12, color=BLUE),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=360, title="Cone and frustum scaling diagram")


def svg_stu_cube_corner_cut(a_lbl: str = "a", b_lbl: str = "b", c_lbl: str = "c") -> str:
    """3D cube with a shaded corner tetrahedron cut along three edges meeting at the top-front-right vertex."""
    # Front square + oblique depth
    x0, y0, s = 76, 54, 96
    dx, dy = 42, -30
    # Top-right-front corner is V = (x0+s, y0)
    vx, vy = x0 + s, y0
    p_left = (vx - 44, vy)
    p_down = (vx, vy + 46)
    p_back = (vx + dx * 0.55, vy + dy * 0.55)
    parts = [
        f'<polygon points="{x0},{y0} {x0+dx},{y0+dy} {x0+s+dx},{y0+dy} {x0+s},{y0}" fill="#f1f5f9" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<polygon points="{x0+s},{y0} {x0+s+dx},{y0+dy} {x0+s+dx},{y0+s+dy} {x0+s},{y0+s}" fill="#e2e8f0" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{p_left[0]:.1f},{p_left[1]:.1f} {p_down[0]:.1f},{p_down[1]:.1f} {p_back[0]:.1f},{p_back[1]:.1f}" fill="#fde68a" fill-opacity="0.88" stroke="{RED}" stroke-width="2.1"/>',
        _nlabel((vx + p_left[0]) / 2, vy - 7, a_lbl, size=11, color=BLUE),
        _nlabel(vx - 12, (vy + p_down[1]) / 2 + 4, b_lbl, size=11, color=ORANGE),
        _nlabel(p_back[0] + 12, p_back[1] + 2, c_lbl, size=11, color=GREEN),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=360, title="Cube corner tetrahedron cut")


def svg_stu_mirror_bounce(w_lbl: str = "12", h_lbl: str = "8", path_lbl: str = "?") -> str:
    """Rectangle billiard/mirror wall reflection showing shortest path A -> P -> B via reflected point A'."""
    x0, y0, w, h = 52, 26, 196, 92
    ax, ay = x0 + 28, y0 + 34
    bx, by = x0 + w - 24, y0 + 52
    ay_ref = y0 + h + (y0 + h - ay)
    # Intersection P with bottom wall y = y0 + h
    t = ((y0 + h) - ay_ref) / (by - ay_ref)
    px = ax + t * (bx - ax)
    py = y0 + h
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{ay_ref:.1f}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,3"/>',
        f'<line x1="{ax}" y1="{ay_ref:.1f}" x2="{px:.1f}" y2="{py}" stroke="{ORANGE}" stroke-width="1.6" stroke-dasharray="5,3"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{px:.1f}" y2="{py}" stroke="{RED}" stroke-width="2.3"/>',
        f'<line x1="{px:.1f}" y1="{py}" x2="{bx}" y2="{by}" stroke="{RED}" stroke-width="2.3"/>',
        f'<circle cx="{ax}" cy="{ay}" r="4" fill="{BLUE}"/>',
        f'<circle cx="{bx}" cy="{by}" r="4" fill="{GREEN}"/>',
        f'<circle cx="{ax}" cy="{ay_ref:.1f}" r="3.5" fill="{ORANGE}"/>',
        _nlabel(ax, ay - 9, "A", size=11, color=BLUE),
        _nlabel(bx, by - 9, "B", size=11, color=GREEN),
        _nlabel(ax + 16, ay_ref + 4, "A'", size=11, color=ORANGE),
        _nlabel(px, py - 8, "P", size=11, color=RED),
        _nlabel(x0 + w / 2, y0 - 7, w_lbl, size=11, color=DARK),
        _nlabel(x0 + w + 14, y0 + h / 2 + 4, h_lbl, size=11, color=DARK, anchor="start"),
        _nlabel(208, 156, path_lbl, size=11, color=RED if "?" in str(path_lbl) else DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Mirror reflection shortest bounce")


def svg_stu_meeting_square(L_lbl: str = "60", t_lbl: str = "15") -> str:
    """Geometric probability square [0, L] x [0, L] with shaded meeting band |x - y| <= t."""
    x0, y0, s = 88, 22, 132
    d = 36
    band = f"{x0},{y0+s} {x0+d},{y0+s} {x0+s},{y0+d} {x0+s},{y0+s-s} {x0+s},{y0} {x0+s-d},{y0} {x0},{y0+s-d}"
    # Careful exact vertices in SVG coords (origin bottom-left = (x0, y0+s), top-right = (x0+s, y0)):
    # Math (0,0)->(x0, y0+s), (t,0)->(x0+d, y0+s), (L, L-t)->(x0+s, y0+d), (L,L)->(x0+s, y0), (L-t, L)->(x0+s-d, y0), (0, t)->(x0, y0+s-d)
    band_pts = f"{x0},{y0+s} {x0+d},{y0+s} {x0+s},{y0+d} {x0+s},{y0} {x0+s-d},{y0} {x0},{y0+s-d}"
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{band_pts}" fill="{WATER}" fill-opacity="0.75" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<line x1="{x0}" y1="{y0+s}" x2="{x0+s}" y2="{y0}" stroke="{RED}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        _nlabel(x0 - 8, y0 + s + 12, "0", size=11, color=DARK),
        _nlabel(x0 + d, y0 + s + 15, t_lbl, size=11, color=BLUE),
        _nlabel(x0 + s, y0 + s + 15, L_lbl, size=11, color=DARK),
        _nlabel(x0 - 14, y0 + s - d + 4, t_lbl, size=11, color=BLUE),
        _nlabel(x0 - 14, y0 + 5, L_lbl, size=11, color=DARK),
        _nlabel(x0 + s / 2, y0 + s / 2 + 4, "|x−y|≤" + str(t_lbl), size=11, color=DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=178, disp_w=360, title="Geometric probability meeting square")


def svg_stu_dyck_grid(n: int = 4, path_steps: str = "RRUURURU") -> str:
    """Catalan / ballot lattice n x n grid staying on or below the main diagonal y = x."""
    n = max(2, min(6, int(n)))
    cs = min(28, 128 // n)
    s = n * cs
    x0, y0 = (320 - s) / 2, (168 - s) / 2
    parts = []
    for i in range(n + 1):
        parts.append(f'<line x1="{x0}" y1="{y0 + i*cs:.1f}" x2="{x0 + s:.1f}" y2="{y0 + i*cs:.1f}" stroke="{GRID}" stroke-width="1.3"/>')
        parts.append(f'<line x1="{x0 + i*cs:.1f}" y1="{y0}" x2="{x0 + i*cs:.1f}" y2="{y0 + s:.1f}" stroke="{GRID}" stroke-width="1.3"/>')
    parts.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{s:.1f}" height="{s:.1f}" fill="none" stroke="{STROKE}" stroke-width="1.9"/>')
    parts.append(f'<line x1="{x0:.1f}" y1="{y0 + s:.1f}" x2="{x0 + s:.1f}" y2="{y0:.1f}" stroke="{BLUE}" stroke-width="1.8" stroke-dasharray="5,3"/>')
    cx, cy = 0, 0
    pts = [(x0, y0 + s)]
    for ch in path_steps.upper():
        if ch == "R" and cx < n:
            cx += 1
        elif ch == "U" and cy < n:
            cy += 1
        pts.append((x0 + cx * cs, y0 + s - cy * cs))
    if len(pts) >= 2:
        d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        parts.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append(f'<circle cx="{x0:.1f}" cy="{y0 + s:.1f}" r="4" fill="{GREEN}"/>')
    parts.append(f'<circle cx="{x0 + s:.1f}" cy="{y0:.1f}" r="4" fill="{ORANGE}"/>')
    return wrap_svg("".join(parts), w=320, h=172, disp_w=350, title="Catalan ballot lattice grid")


def svg_stu_probability_tree(p1_lbl: str = "1/2", p2_lbl: str = "1/2", q1_lbl: str = "3/5", q2_lbl: str = "1/4", top_box: str = "Box A", bot_box: str = "Box B") -> str:
    """Two-stage conditional probability / Bayes tree diagram with dynamic box widths."""
    bw = max(58, 16 + max(len(str(top_box)), len(str(bot_box))) * 7.2)
    parts = [
        f'<circle cx="34" cy="88" r="7" fill="{DARK}"/>',
        f'<line x1="41" y1="88" x2="112" y2="48" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="41" y1="88" x2="112" y2="128" stroke="{ORANGE}" stroke-width="2"/>',
        _nlabel(72, 58, p1_lbl, size=11, color=BLUE),
        _nlabel(72, 126, p2_lbl, size=11, color=ORANGE),
        f'<rect x="112" y="32" width="{bw:.1f}" height="30" rx="7" fill="{WATER}" stroke="{STROKE}" stroke-width="1.8"/>',
        _nlabel(112 + bw / 2, 51, top_box, size=11, color=DARK),
        f'<rect x="112" y="112" width="{bw:.1f}" height="30" rx="7" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        _nlabel(112 + bw / 2, 131, bot_box, size=11, color=DARK),
        f'<line x1="{112 + bw:.1f}" y1="47" x2="254" y2="34" stroke="{GREEN}" stroke-width="2"/>',
        f'<line x1="{112 + bw:.1f}" y1="127" x2="254" y2="114" stroke="{GREEN}" stroke-width="2"/>',
        _nlabel((112 + bw + 254) / 2, 32, q1_lbl, size=11, color=RED if "?" in str(q1_lbl) else GREEN),
        _nlabel((112 + bw + 254) / 2, 112, q2_lbl, size=11, color=RED if "?" in str(q2_lbl) else GREEN),
        f'<rect x="254" y="20" width="52" height="26" rx="6" fill="#fde68a" stroke="{STROKE}" stroke-width="1.6"/>',
        _nlabel(280, 37, "Win", size=11, color=DARK),
        f'<rect x="254" y="100" width="52" height="26" rx="6" fill="#fde68a" stroke="{STROKE}" stroke-width="1.6"/>',
        _nlabel(280, 117, "Win", size=11, color=DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=168, disp_w=370, title="Two-stage conditional probability tree")
