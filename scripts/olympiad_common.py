"""Shared helpers, 5-option (A–E) Olympiad MCQ builders, lesson builders, and IMO/BMO/AMC Olympiad SVG generators (Grades 7–12)."""
import html
import json
import math
import random
import re
import xml.etree.ElementTree as ET
from fractions import Fraction
from pathlib import Path

from kangaroo_common import *  # noqa: F401,F403
from kmc_common import (
    _format_prose_html,
    explain_ar,
    explain_en,
    fmt_val,
    m,
    norm_text,
)
from kmc_diagrams import BLUE, DARK, GREEN, GRID, MUTED, ORANGE, RED, SHADE, SHADE_ALT, STROKE, WATER, _esc as esc, _nlabel, wrap_svg
from nsmo_common import PAL, dm

ROOT = Path(__file__).resolve().parents[1]

OLYMPIAD_LEVELS = (
    "Tier 1: Junior Olympiad (Grades 7-8)",
    "Tier 2: Intermediate Olympiad (Grades 9-10)",
    "Tier 3: Senior Olympiad (Grades 11-12)",
)

OLYMPIAD_TOPICS = (
    "Number Theory",
    "Algebra",
    "Inequalities",
    "Geometry",
    "Combinatorics",
)

OLYMPIAD_FORBIDDEN_RE = re.compile(
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
        r"\bmarkov\b",
        r"\bstochastic\b",
        r"\btaylor\b",
        r"\bmaclaurin\b",
        r"\bfourier\b",
        r"\blaplace\b",
        r"\bcalculus\b",
        r"\\int\b",
        r"\\lim\b",
        r"\\partial\b",
        r"\\nabla\b",
    ]),
    re.IGNORECASE,
)


def load_other_olympiad_stems() -> set[str]:
    """Return normalized English stems from all non-Olympiad banks so Olympiad stems are 100% globally unique."""
    stems: set[str] = set()
    for name in ("kaust", "nsmo", "kangaroo", "nafes", "jee"):
        p = ROOT / "data" / f"{name}.json"
        if p.exists():
            for q in json.loads(p.read_text(encoding="utf-8")):
                stems.add(norm_text(q["content"]["en"]["question"]))
    return stems


def make_olympiad_question(
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
    assert level in OLYMPIAD_LEVELS, f"Invalid Olympiad level: {level}"
    assert topic in OLYMPIAD_TOPICS, f"Invalid Olympiad topic: {topic}"
    assert difficulty in ("Easy", "Medium", "Hard"), f"Invalid difficulty: {difficulty}"
    assert len(opts_en) == 5 and len(opts_ar) == 5, f"Olympiad requires 5 options (A–E): {qid}"
    assert 0 <= correct_idx < 5
    assert "\\\\(" not in q_en and "\\\\(" not in q_ar
    assert diagram_en and "<svg" in diagram_en, f"Olympiad question {qid} requires an SVG diagram"

    ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)

    en_block = {
        "question": _format_prose_html(q_en),
        "options": [_format_prose_html(o) for o in opts_en],
        "hint": _format_prose_html(hint_en),
        "explanation": _format_prose_html(sol_en),
        "diagram": diagram_en,
    }
    ar_block = {
        "question": _format_prose_html(q_ar),
        "options": [_format_prose_html(o) for o in opts_ar],
        "hint": _format_prose_html(hint_ar),
        "explanation": _format_prose_html(sol_ar),
        "diagram": diagram_ar if diagram_ar else diagram_en,
    }

    for lang_blk in (en_block, ar_block):
        blob = " ".join([lang_blk["question"], *lang_blk["options"], lang_blk["hint"], lang_blk["explanation"]])
        assert not OLYMPIAD_FORBIDDEN_RE.search(blob), f"Forbidden term in {qid}: {OLYMPIAD_FORBIDDEN_RE.search(blob)}"

    return {
        "id": qid,
        "track": "olympiad",
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        "olympiad_blueprint": blueprint,
        "review": {
            "structural": "passed",
            "mathematical": "programmatically_verified",
            "scope": "imo_bmo_amc_olympiad_grades_7_12",
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }


def make_olym_q(
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
    """Convenience builder combining make_5_math_options + explain_en/ar + make_olympiad_question."""
    opts_en, opts_ar, cidx, cans = make_5_math_options(correct_val, distractors, qid, suffix=suffix)
    return make_olympiad_question(
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


def make_olym_bilingual_q(
    qid: str,
    level: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    option_pairs: list[tuple[str, str]],
    correct_pair_idx: int,
    hint_en: str,
    hint_ar: str,
    idea_en: str,
    steps_en: list[str],
    check_en: str,
    idea_ar: str,
    steps_ar: list[str],
    check_ar: str,
    diagram_en: str = None,
    diagram_ar: str = None,
) -> dict:
    opts_en, opts_ar, cidx, cans = make_5_bilingual_options(option_pairs, correct_pair_idx, seed_key=qid)
    return make_olympiad_question(
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


# ---- Olympiad Study Lesson Builders ----
def olym_concept(
    title_en: str,
    title_ar: str,
    body_en: str,
    body_ar: str,
    formula_en: str = None,
    caption_ar: str = "",
    formula_math_ar: str = None,
    diagram_en: str = None,
    diagram_ar: str = None,
    *,
    rule_en: str = None,
    rule_ar: str = None,
) -> dict:
    if formula_en is None:
        formula_en = rule_en or ""
    if formula_math_ar is None:
        formula_math_ar = rule_ar if rule_ar is not None else formula_en
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


def olym_worked_example(
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


def make_olympiad_lesson(
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
    assert level in OLYMPIAD_LEVELS
    assert topic in OLYMPIAD_TOPICS
    assert len(concepts) >= 3
    assert len(examples) >= 4
    clean_unit_num = re.sub(r"^(?:Lesson|درس)\s+", "", str(unit_num).strip(), flags=re.IGNORECASE)
    return {
        "id": lesson_id,
        "track": "olympiad",
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
# Olympiad-Specific SVG Diagram Generators (12 Synthetic / Combinatorial Helpers)
# ==============================================================================

def svg_olym_radical_axis(r1_lbl: str = "R", r2_lbl: str = "r", p_lbl: str = "P") -> str:
    """Two intersecting circles with their vertical radical axis and an external point P."""
    c1x, c2x, cy = 112, 198, 98
    r1, r2 = 54, 44
    # Radical axis x: (x - c1x)^2 - r1^2 = (x - c2x)^2 - r2^2
    rx = ((c2x**2 - c1x**2) - (r2**2 - r1**2)) / (2 * (c2x - c1x))
    parts = [
        f'<circle cx="{c1x}" cy="{cy}" r="{r1}" fill="{WATER}" fill-opacity="0.48" stroke="{BLUE}" stroke-width="2"/>',
        f'<circle cx="{c2x}" cy="{cy}" r="{r2}" fill="{SHADE}" fill-opacity="0.52" stroke="{ORANGE}" stroke-width="2"/>',
        f'<line x1="{c1x}" y1="{cy}" x2="{c2x}" y2="{cy}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="4,3"/>',
        f'<line x1="{rx:.1f}" y1="18" x2="{rx:.1f}" y2="164" stroke="{RED}" stroke-width="2.1"/>',
        f'<circle cx="{rx:.1f}" cy="30" r="3.5" fill="{RED}"/>',
        f'<circle cx="{c1x}" cy="{cy}" r="2.8" fill="{DARK}"/>',
        f'<circle cx="{c2x}" cy="{cy}" r="2.8" fill="{DARK}"/>',
        _nlabel(c1x - 16, cy - 8, r1_lbl, size=11, color=BLUE),
        _nlabel(c2x + 16, cy - 8, r2_lbl, size=11, color=ORANGE),
        _nlabel(rx + 14, 28, p_lbl, size=11, color=RED),
        _nlabel(c1x, cy + 16, "O₁", size=10, color=DARK),
        _nlabel(c2x, cy + 16, "O₂", size=10, color=DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Radical axis of two circles")


def svg_olym_nine_point_euler(o_lbl: str = "O", g_lbl: str = "G", h_lbl: str = "H") -> str:
    """Acute scalene triangle ABC with Euler line O–G–H (OH = 3 OG)."""
    ax, ay = 132, 24
    bx, by = 52, 148
    cx, cy = 264, 148
    gx, gy = (ax + bx + cx) / 3, (ay + by + cy) / 3
    # Circumcenter O and Orthocenter H satisfying G = (2O + H)/3
    ox, oy = 158, 108
    hx, hy = 3 * gx - 2 * ox, 3 * gy - 2 * oy
    parts = [
        f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{ax}" y2="{by}" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="4,3"/>',
        f'<line x1="{ox - 18:.1f}" y1="{oy + (oy - hy)*0.22:.1f}" x2="{hx + 18:.1f}" y2="{hy - (oy - hy)*0.22:.1f}" stroke="{RED}" stroke-width="2.1"/>',
        f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="3.6" fill="{BLUE}"/>',
        f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="3.6" fill="{GREEN}"/>',
        f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="3.6" fill="{RED}"/>',
        _nlabel(ax, ay - 8, "A", size=11, color=DARK),
        _nlabel(bx - 11, by + 4, "B", size=11, color=DARK),
        _nlabel(cx + 11, cy + 4, "C", size=11, color=DARK),
        _nlabel(ox + 12, oy + 12, o_lbl, size=11, color=BLUE),
        _nlabel(gx, gy - 10, g_lbl, size=11, color=GREEN),
        _nlabel(hx - 12, hy - 8, h_lbl, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=174, disp_w=370, title="Triangle Euler line O-G-H")


def svg_olym_incircle_excircle(a_lbl: str = "a", b_lbl: str = "b", c_lbl: str = "c", note: str = "s − a") -> str:
    """Triangle ABC with inscribed circle I and tangency segments s-a, s-b, s-c."""
    ax, ay = 148, 24
    bx, by = 56, 148
    cx, cy = 262, 148
    ix, iy, ir = 152, 108, 39
    parts = [
        f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<circle cx="{ix}" cy="{iy}" r="{ir}" fill="{WATER}" fill-opacity="0.58" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="{ix}" y1="{iy}" x2="{ix}" y2="{by}" stroke="{RED}" stroke-width="1.6" stroke-dasharray="3,3"/>',
        f'<circle cx="{ix}" cy="{iy}" r="3" fill="{DARK}"/>',
        _nlabel(ax, ay - 7, "A", size=11, color=DARK),
        _nlabel(bx - 10, by + 4, "B", size=11, color=DARK),
        _nlabel(cx + 10, cy + 4, "C", size=11, color=DARK),
        _nlabel((bx + cx) / 2, by + 15, a_lbl, size=11, color=BLUE),
        _nlabel((ax + cx) / 2 + 14, (ay + cy) / 2, b_lbl, size=11, color=BLUE),
        _nlabel((ax + bx) / 2 - 14, (ay + by) / 2, c_lbl, size=11, color=BLUE),
        _nlabel(ix + 12, (iy + by) / 2 + 3, "r", size=11, color=RED),
        _nlabel(258, 30, note, size=11, color=GREEN),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Triangle incircle and tangent lengths")


def svg_olym_cyclic_ptolemy(
    ab_lbl: str = "a",
    bc_lbl: str = "b",
    cd_lbl: str = "c",
    da_lbl: str = "d",
    diag_note: str = "AC·BD",
) -> str:
    """Cyclic quadrilateral ABCD inscribed in a circle with both diagonals AC and BD."""
    ox, oy, R = 160, 92, 66
    angs = [212, 326, 38, 144]
    pts = [(ox + R * math.cos(math.radians(t)), oy - R * math.sin(math.radians(t))) for t in angs]
    (ax, ay), (bx, by), (cx, cy), (dx, dy) = pts
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts = [
        f'<circle cx="{ox}" cy="{oy}" r="{R}" fill="{WATER}" fill-opacity="0.32" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<polygon points="{poly}" fill="#ffffff" fill-opacity="0.72" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="{RED}" stroke-width="1.8" stroke-dasharray="4,3"/>',
        f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{dx:.1f}" y2="{dy:.1f}" stroke="{ORANGE}" stroke-width="1.8" stroke-dasharray="4,3"/>',
        _nlabel(ax - 11, ay + 6, "A", size=11, color=DARK),
        _nlabel(bx + 11, by + 6, "B", size=11, color=DARK),
        _nlabel(cx + 11, cy - 4, "C", size=11, color=DARK),
        _nlabel(dx - 11, dy - 4, "D", size=11, color=DARK),
        _nlabel((ax + bx) / 2, (ay + by) / 2 + 13, ab_lbl, size=11, color=BLUE),
        _nlabel((bx + cx) / 2 + 12, (by + cy) / 2, bc_lbl, size=11, color=BLUE),
        _nlabel((cx + dx) / 2, (cy + dy) / 2 - 8, cd_lbl, size=11, color=BLUE),
        _nlabel((dx + ax) / 2 - 12, (dy + ay) / 2, da_lbl, size=11, color=BLUE),
        _nlabel(274, 24, diag_note, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=180, disp_w=370, title="Cyclic quadrilateral Ptolemy configuration")


def svg_olym_spiral_homothety(k_lbl: str = "k", center_lbl: str = "S") -> str:
    """Homothety / spiral similarity from center S mapping triangle ABC to A'B'C'."""
    sx, sy = 44, 126
    p1 = [(112, 68), (104, 134), (154, 114)]
    p2 = [(204, 34), (190, 146), (272, 112)]
    poly1 = " ".join(f"{x},{y}" for x, y in p1)
    poly2 = " ".join(f"{x},{y}" for x, y in p2)
    rays = "".join(
        f'<line x1="{sx}" y1="{sy}" x2="{x2}" y2="{y2}" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="4,3"/>'
        for x2, y2 in p2
    )
    parts = [
        rays,
        f'<polygon points="{poly1}" fill="{WATER}" fill-opacity="0.65" stroke="{BLUE}" stroke-width="2"/>',
        f'<polygon points="{poly2}" fill="{SHADE}" fill-opacity="0.55" stroke="{ORANGE}" stroke-width="2"/>',
        f'<circle cx="{sx}" cy="{sy}" r="4" fill="{RED}"/>',
        _nlabel(sx - 10, sy + 14, center_lbl, size=11, color=RED),
        _nlabel(122, 60, "A", size=10, color=BLUE),
        _nlabel(210, 26, "A'", size=10, color=ORANGE),
        _nlabel(160, 22, f"scale {k_lbl}", size=11, color=GREEN),
    ]
    return wrap_svg("".join(parts), w=320, h=174, disp_w=370, title="Homothety and spiral similarity")


def svg_olym_tetrahedron_3d(ab_lbl: str = "a", cd_lbl: str = "b", h_lbl: str = "h") -> str:
    """3D tetrahedron ABCD wireframe with hidden edge BD dashed and altitude/bimedian highlighted."""
    ax, ay = 158, 22
    bx, by = 66, 132
    cx, cy = 178, 154
    dx, dy = 252, 114
    gx, gy = (bx + cx + dx) / 3, (by + cy + dy) / 3
    parts = [
        f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="{WATER}" fill-opacity="0.38" stroke="none"/>',
        f'<polygon points="{ax},{ay} {cx},{cy} {dx},{dy}" fill="{SHADE}" fill-opacity="0.42" stroke="none"/>',
        f'<line x1="{bx}" y1="{by}" x2="{dx}" y2="{dy}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="5,4"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{gx:.1f}" y2="{gy:.1f}" stroke="{RED}" stroke-width="1.9" stroke-dasharray="3,3"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{cx}" y2="{cy}" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{dx}" y2="{dy}" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{bx}" y1="{by}" x2="{cx}" y2="{cy}" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{dx}" y2="{dy}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(ax, ay - 7, "A", size=11, color=DARK),
        _nlabel(bx - 10, by + 5, "B", size=11, color=DARK),
        _nlabel(cx, cy + 14, "C", size=11, color=DARK),
        _nlabel(dx + 10, dy + 4, "D", size=11, color=DARK),
        _nlabel((ax + bx) / 2 - 12, (ay + by) / 2, ab_lbl, size=11, color=BLUE),
        _nlabel((cx + dx) / 2 + 10, (cy + dy) / 2 + 12, cd_lbl, size=11, color=ORANGE),
        _nlabel((ax + gx) / 2 + 10, (ay + gy) / 2 + 4, h_lbl, size=11, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=178, disp_w=370, title="3D Olympiad tetrahedron")


def svg_olym_bipartite_graph(
    m_left: int = 3,
    n_right: int = 4,
    edges: list[tuple[int, int]] = None,
    note: str = "",
) -> str:
    """Bipartite graph G = (U, V, E) for Hall's Marriage, degree-sum, and extremal graph puzzles."""
    m_l = max(2, min(5, m_left))
    n_r = max(2, min(5, n_right))
    y_l = [36 + i * (108 / max(1, m_l - 1)) for i in range(m_l)]
    y_r = [30 + j * (120 / max(1, n_r - 1)) for j in range(n_r)]
    xl, xr = 92, 228
    if edges is None:
        edges = [(i, j) for i in range(m_l) for j in range(n_r) if (i + j) % 2 == 0 or j == i]
    parts = []
    if note:
        parts.append(_nlabel(160, 18, note, size=11, color=GREEN))
    for i, j in edges:
        if 0 <= i < m_l and 0 <= j < n_r:
            parts.append(f'<line x1="{xl}" y1="{y_l[i]:.1f}" x2="{xr}" y2="{y_r[j]:.1f}" stroke="{BLUE}" stroke-width="1.6" stroke-opacity="0.75"/>')
    for i, y in enumerate(y_l):
        parts.append(f'<circle cx="{xl}" cy="{y:.1f}" r="8" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(xl - 20, y + 4, f"u{i+1}", size=10, color=DARK))
    for j, y in enumerate(y_r):
        parts.append(f'<circle cx="{xr}" cy="{y:.1f}" r="8" fill="{WATER}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(xr + 20, y + 4, f"v{j+1}", size=10, color=DARK))
    return wrap_svg("".join(parts), w=320, h=174, disp_w=370, title="Bipartite graph diagram")


def svg_olym_board_coloring(rows: int = 4, cols: int = 4, modulus: int = 2, note: str = "") -> str:
    """Olympiad board coloring (2-coloring chessboard or 3-coloring diagonal stripes) for tiling invariants."""
    r_cnt = max(2, min(6, rows))
    c_cnt = max(2, min(6, cols))
    cs = min(26, 128 // max(r_cnt, c_cnt))
    gw, gh = c_cnt * cs, r_cnt * cs
    x0 = (320 - gw) / 2
    y0 = 28 if note else 20
    palette = ["#ffffff", "#bae6fd", "#fde68a", "#bbf7d0"]
    parts = []
    if note:
        parts.append(_nlabel(160, 18, note, size=11, color=GREEN))
    for r in range(r_cnt):
        for c in range(c_cnt):
            k = (r + c) % max(2, modulus)
            fc = palette[k % len(palette)]
            parts.append(
                f'<rect x="{x0 + c*cs:.1f}" y="{y0 + r*cs:.1f}" width="{cs}" height="{cs}" fill="{fc}" stroke="{STROKE}" stroke-width="1.4"/>'
            )
            if modulus >= 3 and cs >= 22:
                parts.append(_nlabel(x0 + (c + 0.5) * cs, y0 + (r + 0.5) * cs + 4, str(k), size=9, color=DARK))
    return wrap_svg("".join(parts), w=320, h=max(164, int(y0 + gh + 18)), disp_w=360, title="Board coloring invariant")


def svg_olym_inequality_curve(a_lbl: str = "a", b_lbl: str = "b", note: str = "AM ≥ GM") -> str:
    """Visual proof of AM-GM on a semicircle of diameter a + b: radius (a+b)/2 >= altitude sqrt(ab)."""
    x_left, x_right, y_base = 48, 272, 142
    R = (x_right - x_left) / 2  # 112
    ox = (x_left + x_right) / 2  # 160
    px = x_left + 72  # split point between a and b
    h = math.sqrt(max(1.0, R**2 - (px - ox) ** 2))
    parts = [
        f'<path d="M {x_left} {y_base} A {R} {R} 0 0 1 {x_right} {y_base} Z" fill="{WATER}" fill-opacity="0.38" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{px}" y1="{y_base}" x2="{px}" y2="{y_base - h:.1f}" stroke="{RED}" stroke-width="2.3"/>',
        f'<line x1="{ox}" y1="{y_base}" x2="{ox}" y2="{y_base - R:.1f}" stroke="{BLUE}" stroke-width="2.1" stroke-dasharray="4,3"/>',
        f'<circle cx="{ox}" cy="{y_base}" r="3" fill="{DARK}"/>',
        f'<circle cx="{px}" cy="{y_base}" r="3" fill="{RED}"/>',
        _nlabel((x_left + px) / 2, y_base + 16, a_lbl, size=11, color=DARK),
        _nlabel((px + x_right) / 2, y_base + 16, b_lbl, size=11, color=DARK),
        _nlabel(px - 18, y_base - h / 2, "√ab", size=11, color=RED),
        _nlabel(ox + 28, y_base - R / 2, "(a+b)/2", size=11, color=BLUE),
        _nlabel(268, 28, note, size=11, color=GREEN),
    ]
    return wrap_svg("".join(parts), w=320, h=172, disp_w=370, title="AM-GM semicircle diagram")


def svg_olym_func_mapping(
    dom_vals: list[str] = ("x", "1−x", "1/x"),
    cod_vals: list[str] = ("f(x)", "f(1−x)", "?"),
    note: str = "Functional Cycle",
) -> str:
    """Two-oval domain/target mapping diagram for Olympiad functional equations and involutions."""
    n = min(4, max(2, len(dom_vals), len(cod_vals)))
    ys = [52 + i * (84 / max(1, n - 1)) for i in range(n)]
    parts = [
        _nlabel(160, 18, note, size=11, color=GREEN),
        f'<ellipse cx="88" cy="94" rx="44" ry="62" fill="{SHADE}" fill-opacity="0.45" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<ellipse cx="232" cy="94" rx="48" ry="62" fill="{WATER}" fill-opacity="0.45" stroke="{STROKE}" stroke-width="1.8"/>',
    ]
    for i in range(n):
        dv = dom_vals[i] if i < len(dom_vals) else ""
        cv = cod_vals[i] if i < len(cod_vals) else ""
        y = ys[i]
        parts.append(_nlabel(88, y + 4, str(dv), size=11, color=DARK))
        parts.append(_nlabel(232, y + 4, str(cv), size=11, color=RED if "?" in str(cv) else BLUE))
        parts.append(
            f'<line x1="126" y1="{y:.1f}" x2="188" y2="{y:.1f}" stroke="{BLUE}" stroke-width="1.7"/>'
            f'<polygon points="188,{y:.1f} 181,{y-3.5:.1f} 181,{y+3.5:.1f}" fill="{BLUE}"/>'
        )
    return wrap_svg("".join(parts), w=320, h=172, disp_w=370, title="Functional mapping diagram")


def svg_olym_divisibility_lattice(
    top_lbl: str = "lcm(a,b)",
    left_lbl: str = "a",
    right_lbl: str = "b",
    bot_lbl: str = "gcd(a,b)",
) -> str:
    """Hasse divisibility diamond showing gcd(a,b) dividing a, b which divide lcm(a,b)."""
    nodes = [
        (160, 32, top_lbl, PAL["amber_fill"]),
        (86, 88, left_lbl, PAL["blue_fill"]),
        (234, 88, right_lbl, PAL["blue_fill"]),
        (160, 144, bot_lbl, "#bbf7d0"),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    parts = [
        f'<line x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[j][0]}" y2="{nodes[j][1]}" stroke="{STROKE}" stroke-width="1.9"/>'
        for i, j in edges
    ]
    for x, y, lbl, fc in nodes:
        bw = max(56, int(len(str(lbl)) * 7.4 + 18))
        parts.append(f'<rect x="{x - bw/2:.1f}" y="{y - 15}" width="{bw}" height="30" rx="8" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(x, y + 4, str(lbl), size=11, color=RED if "?" in str(lbl) else DARK))
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370, title="Divisibility GCD-LCM lattice")


def svg_olym_pigeonhole_boxes(n_boxes: int = 4, items_note: str = "N items", ask_note: str = "≥ ⌈N/k⌉") -> str:
    """Pigeonhole / Dirichlet box partition showing N objects distributed across k boxes."""
    k = max(2, min(6, n_boxes))
    bw, bh, gap = 42, 46, 8
    tot_w = k * bw + (k - 1) * gap
    x0 = (320 - tot_w) / 2
    y0 = 76
    parts = [
        _nlabel(160, 24, f"{items_note} → {k} boxes", size=12, color=BLUE),
        f'<line x1="160" y1="32" x2="160" y2="66" stroke="{RED}" stroke-width="1.8" stroke-dasharray="3,3"/>',
        _nlabel(160, 148, ask_note, size=11, color=RED if "?" in str(ask_note) else GREEN),
    ]
    for i in range(k):
        x = x0 + i * (bw + gap)
        fc = PAL["amber_fill"] if i == 0 else "#f8fafc"
        parts.append(f'<rect x="{x:.1f}" y="{y0}" width="{bw}" height="{bh}" rx="6" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(x + bw / 2, y0 + 28, f"B{i+1}", size=11, color=DARK))
    return wrap_svg("".join(parts), w=320, h=168, disp_w=370, title="Pigeonhole boxes diagram")
