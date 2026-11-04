"""Shared helpers, 4-option (A–D) MCQ builders, lesson builders, and Mawhiba SVG generators for NSMO (Grades 7–10)."""
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

NSMO_LEVELS = (
    "Phase 1: Junior Olympiad (Grade 7)",
    "Phase 2: Intermediate Olympiad (Grades 8-9)",
    "Phase 3: Senior National Olympiad (Grade 10)",
)

NSMO_TOPICS = (
    "Number Theory",
    "Algebra",
    "Geometry",
    "Combinatorics & Logic",
    "Data & Probability",
)

NSMO_FORBIDDEN_RE = re.compile(
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
    """Return normalized English stems from all non-NSMO banks so NSMO stems are 100% globally unique."""
    stems: set[str] = set()
    for name in ("kaust", "kangaroo", "nafes", "jee", "olympiad"):
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


def make_nsmo_question(
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
    assert level in NSMO_LEVELS, f"Invalid NSMO level: {level}"
    assert topic in NSMO_TOPICS, f"Invalid NSMO topic: {topic}"
    assert difficulty in ("Easy", "Medium", "Hard"), f"Invalid difficulty: {difficulty}"
    assert len(opts_en) == 4 and len(opts_ar) == 4, f"NSMO requires 4 options: {qid}"
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
        assert not NSMO_FORBIDDEN_RE.search(blob), f"Forbidden term in {qid}: {NSMO_FORBIDDEN_RE.search(blob)}"

    return {
        "id": qid,
        "track": "nsmo",
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        "nsmo_blueprint": blueprint,
        "review": {
            "structural": "passed",
            "mathematical": "programmatically_verified",
            "scope": "mawhiba_nsmo_grades_7_10",
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }


# ---- NSMO Study Lesson Builders ----
def nsmo_concept(
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


def nsmo_worked_example(
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
    opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, ex_id, suffix=suffix)
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    en_obj = {
        "title": _format_prose_html(title_en),
        "question": _format_prose_html(q_en),
        "options": [_format_prose_html(o) for o in opts_en],
        "explanation": _format_prose_html(explain_en(idea_en, steps_en, check_en)),
    }
    ar_obj = {
        "title": _format_prose_html(title_ar),
        "question": _format_prose_html(q_ar),
        "options": [_format_prose_html(o) for o in opts_ar],
        "explanation": _format_prose_html(explain_ar(idea_ar, steps_ar, check_ar)),
    }
    if diagram_en:
        en_obj["diagram"] = diagram_en
        ar_block_diag = diagram_ar if diagram_ar else diagram_en
        ar_obj["diagram"] = ar_block_diag
    return {
        "id": ex_id,
        "correct_index": cidx,
        "correct_answer": str(cans),
        "en": en_obj,
        "ar": ar_obj,
    }


def make_nsmo_lesson(
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
    assert level in NSMO_LEVELS
    assert len(concepts) >= 3
    assert len(examples) >= 4
    return {
        "id": lesson_id,
        "track": "nsmo",
        "level": level,
        "unit_num": unit_num,
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


# ---- 6 Signature Mawhiba / NSMO Vector Diagram Generators ----
def svg_parallel_similar_tri(ad_lbl: str = "AD", db_lbl: str = "DB", de_lbl: str = "DE", bc_lbl: str = "BC") -> str:
    """Triangle ABC with DE || BC cutting AB at D and AC at E."""
    ax, ay = 155, 22
    bx, by = 52, 162
    cx, cy = 268, 162
    t = 0.45
    dx, dy = ax + t * (bx - ax), ay + t * (by - ay)
    ex, ey = ax + t * (cx - ax), ay + t * (cy - ay)
    body = f"""
    <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="{PAL['blue_fill']}" fill-opacity="0.32" stroke="{PAL['ink']}" stroke-width="2.2"/>
    <polygon points="{ax},{ay} {dx:.1f},{dy:.1f} {ex:.1f},{ey:.1f}" fill="{PAL['amber_fill']}" fill-opacity="0.65" stroke="{PAL['ink']}" stroke-width="2"/>
    <line x1="{dx:.1f}" y1="{dy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{PAL['blue']}" stroke-width="2.5"/>
    <circle cx="{ax}" cy="{ay}" r="3.2" fill="{PAL['ink']}"/>
    <circle cx="{bx}" cy="{by}" r="3.2" fill="{PAL['ink']}"/>
    <circle cx="{cx}" cy="{cy}" r="3.2" fill="{PAL['ink']}"/>
    <circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.2" fill="{PAL['blue']}"/>
    <circle cx="{ex:.1f}" cy="{ey:.1f}" r="3.2" fill="{PAL['blue']}"/>
    <text x="{ax}" y="{ay - 6}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">A</text>
    <text x="{bx - 11}" y="{by + 4}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">B</text>
    <text x="{cx + 11}" y="{cy + 4}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">C</text>
    <text x="{dx - 12:.1f}" y="{dy + 2:.1f}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['blue']}">D</text>
    <text x="{ex + 12:.1f}" y="{ey + 2:.1f}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['blue']}">E</text>
    <text x="{(ax + dx)/2 - 16:.1f}" y="{(ay + dy)/2:.1f}" text-anchor="end" font-size="11.5" font-weight="700" fill="{PAL['amber']}">{esc(ad_lbl)}</text>
    <text x="{(dx + bx)/2 - 14:.1f}" y="{(dy + by)/2 + 4:.1f}" text-anchor="end" font-size="11.5" font-weight="700" fill="{PAL['ink']}">{esc(db_lbl)}</text>
    <text x="{(dx + ex)/2:.1f}" y="{dy - 6:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{PAL['blue']}">{esc(de_lbl)}</text>
    <text x="{(bx + cx)/2:.1f}" y="{by + 16}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{PAL['ink']}">{esc(bc_lbl)}</text>
    """
    return wrap_svg(body, 320, 186, 390, "Similar triangles DE parallel to BC")


def svg_cyclic_quad(ang_a_lbl: str = "α", ang_c_lbl: str = "180°−α") -> str:
    """Cyclic quadrilateral ABCD inscribed in a circle showing opposite supplementary angles."""
    cx, cy, r = 160, 94, 70
    angs = [math.radians(a) for a in (-130, -35, 42, 148)]
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in angs]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    names = ["A", "B", "C", "D"]
    offsets = [(-11, -7), (11, -7), (12, 11), (-12, 11)]
    v_svg = "".join(
        f'<circle cx="{pts[i][0]:.1f}" cy="{pts[i][1]:.1f}" r="3.4" fill="{PAL["ink"]}"/>'
        f'<text x="{pts[i][0] + offsets[i][0]:.1f}" y="{pts[i][1] + offsets[i][1]:.1f}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL["ink"]}">{names[i]}</text>'
        for i in range(4)
    )
    body = f"""
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAL['teal_fill']}" fill-opacity="0.35" stroke="{PAL['teal']}" stroke-width="2.2"/>
    <polygon points="{poly}" fill="{PAL['purple_fill']}" fill-opacity="0.55" stroke="{PAL['ink']}" stroke-width="2.1"/>
    {v_svg}
    <text x="{pts[0][0] + 18:.1f}" y="{pts[0][1] + 18:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{PAL['rose']}">{esc(ang_a_lbl)}</text>
    <text x="{pts[2][0] - 22:.1f}" y="{pts[2][1] - 8:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{PAL['blue']}">{esc(ang_c_lbl)}</text>
    """
    return wrap_svg(body, 320, 188, 390, "Cyclic quadrilateral inscribed in circle")


def svg_circle_chords(ae_lbl: str = "AE", eb_lbl: str = "EB", ce_lbl: str = "CE", ed_lbl: str = "ED") -> str:
    """Intersecting chords AB and CD at interior point E (AE·EB = CE·ED)."""
    cx, cy, r = 160, 94, 70
    angs = [math.radians(a) for a in (-145, 22, -55, 132)]
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in angs]
    # Intersection of p0-p1 and p2-p3
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = pts
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
    body = f"""
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAL['blue_fill']}" fill-opacity="0.3" stroke="{PAL['ink']}" stroke-width="2.1"/>
    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{PAL['blue']}" stroke-width="2.3"/>
    <line x1="{x3:.1f}" y1="{y3:.1f}" x2="{x4:.1f}" y2="{y4:.1f}" stroke="{PAL['rose']}" stroke-width="2.3"/>
    <circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{PAL['amber']}"/>
    <text x="{px + 9:.1f}" y="{py + 14:.1f}" font-size="11.5" font-weight="800" fill="{PAL['ink']}">E</text>
    <text x="{(x1 + px)/2 - 4:.1f}" y="{(y1 + py)/2 - 5:.1f}" text-anchor="middle" font-size="11" font-weight="800" fill="{PAL['blue']}">{esc(ae_lbl)}</text>
    <text x="{(x2 + px)/2 + 4:.1f}" y="{(y2 + py)/2 - 6:.1f}" text-anchor="middle" font-size="11" font-weight="800" fill="{PAL['blue']}">{esc(eb_lbl)}</text>
    <text x="{(x3 + px)/2 + 12:.1f}" y="{(y3 + py)/2:.1f}" text-anchor="start" font-size="11" font-weight="800" fill="{PAL['rose']}">{esc(ce_lbl)}</text>
    <text x="{(x4 + px)/2 - 10:.1f}" y="{(y4 + py)/2 + 4:.1f}" text-anchor="end" font-size="11" font-weight="800" fill="{PAL['rose']}">{esc(ed_lbl)}</text>
    """
    return wrap_svg(body, 320, 188, 390, "Intersecting chords inside a circle")


def svg_median_tri(ab_lbl: str = "c", ac_lbl: str = "b", bc_lbl: str = "a", m_lbl: str = "mₐ") -> str:
    """Triangle ABC with median AM to midpoint M of BC (Apollonius / centroid 2:1)."""
    ax, ay = 172, 24
    bx, by = 48, 160
    cx, cy = 272, 160
    mx, my = (bx + cx) / 2, by
    gx, gy = (ax + 2 * mx) / 3, (ay + 2 * my) / 3
    body = f"""
    <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="{PAL['teal_fill']}" fill-opacity="0.4" stroke="{PAL['ink']}" stroke-width="2.2"/>
    <line x1="{ax}" y1="{ay}" x2="{mx:.1f}" y2="{my:.1f}" stroke="{PAL['purple']}" stroke-width="2.4" stroke-dasharray="5,3"/>
    <circle cx="{mx:.1f}" cy="{my:.1f}" r="3.4" fill="{PAL['purple']}"/>
    <circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.6" fill="{PAL['rose']}"/>
    <text x="{ax}" y="{ay - 6}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">A</text>
    <text x="{bx - 10}" y="{by + 4}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">B</text>
    <text x="{cx + 10}" y="{cy + 4}" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL['ink']}">C</text>
    <text x="{mx:.1f}" y="{my + 16:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{PAL['purple']}">M ({esc(bc_lbl)})</text>
    <text x="{gx + 12:.1f}" y="{gy + 3:.1f}" font-size="11" font-weight="800" fill="{PAL['rose']}">G</text>
    <text x="{(ax + bx)/2 - 12:.1f}" y="{(ay + by)/2:.1f}" text-anchor="end" font-size="11.5" font-weight="700" fill="{PAL['ink']}">{esc(ab_lbl)}</text>
    <text x="{(ax + cx)/2 + 12:.1f}" y="{(ay + cy)/2:.1f}" text-anchor="start" font-size="11.5" font-weight="700" fill="{PAL['ink']}">{esc(ac_lbl)}</text>
    <text x="{(ax + mx)/2 - 8:.1f}" y="{(ay + my)/2 - 6:.1f}" text-anchor="end" font-size="11.5" font-weight="800" fill="{PAL['purple']}">{esc(m_lbl)}</text>
    """
    return wrap_svg(body, 320, 186, 390, "Triangle median and centroid")


def svg_digit_slots(slot_labels: list[str], top_note: str = "") -> str:
    """Combinatorial digit/seat boxes showing choices per position."""
    n = len(slot_labels)
    max_chars = max((len(str(lbl)) for lbl in slot_labels), default=1)
    bw = max(46, int(max_chars * 7.8 + 16))
    bh, gap = 44, 10
    total_w = n * bw + max(0, n - 1) * gap
    vw = max(320, total_w + 32)
    x0 = (vw - total_w) / 2
    y0 = 62
    boxes = []
    for i, lbl in enumerate(slot_labels):
        x = x0 + i * (bw + gap)
        boxes.append(
            f'<rect x="{x:.1f}" y="{y0}" width="{bw}" height="{bh}" rx="8" fill="{PAL["amber_fill"] if i==0 else PAL["blue_fill"]}" stroke="{PAL["ink"]}" stroke-width="2"/>'
            f'<text x="{x + bw/2:.1f}" y="{y0 + 27}" text-anchor="middle" font-size="13" font-weight="800" fill="{PAL["ink"]}">{esc(lbl)}</text>'
            f'<text x="{x + bw/2:.1f}" y="{y0 + bh + 16}" text-anchor="middle" font-size="10" font-weight="700" fill="{PAL["muted"]}">#{i+1}</text>'
        )
    note = f'<text x="{vw/2:.1f}" y="38" text-anchor="middle" font-size="12" font-weight="800" fill="{PAL["teal"]}">{esc(top_note)}</text>' if top_note else ""
    return wrap_svg(note + "".join(boxes), vw, 142, max(390, vw + 40), "Digit slots counting diagram")


def svg_graph_cycle_chords(n: int = 6, full_kn: bool = True) -> str:
    """Graph vertices around a circle showing handshakes / complete graph K_n or cycle."""
    cx, cy, r = 160, 92, 66
    pts = [(cx + r * math.cos(2 * math.pi * i / n - math.pi / 2), cy + r * math.sin(2 * math.pi * i / n - math.pi / 2)) for i in range(n)]
    lines = []
    for i in range(n):
        for j in range(i + 1, n):
            if full_kn or j == i + 1 or (i == 0 and j == n - 1):
                col = PAL["blue"] if (j == i + 1 or (i == 0 and j == n - 1)) else PAL["grid"]
                sw = "2" if col == PAL["blue"] else "1.4"
                lines.append(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{col}" stroke-width="{sw}"/>')
    nodes = [
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{PAL["teal_fill"]}" stroke="{PAL["ink"]}" stroke-width="2"/>'
        f'<text x="{x:.1f}" y="{y + 3.5:.1f}" text-anchor="middle" font-size="9.5" font-weight="800" fill="{PAL["ink"]}">{i+1}</text>'
        for i, (x, y) in enumerate(pts)
    ]
    return wrap_svg("".join(lines + nodes), 320, 184, 380, "Graph vertices and edges")
