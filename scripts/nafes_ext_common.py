"""Shared helpers, 4-option (A–D) MCQ builders, Study Academy lesson builders, and clean
XML-validated SVG generators for ETEC Nafes Science (Grades 6 & 9) and Nafes English (Grades 3, 6 & 9)."""
import random
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from kmc_common import (
    _format_prose_html,
    explain_ar,
    explain_en,
    fmt_val,
    m,
    norm_text,
)
from kmc_diagrams import BLUE, GREEN, GRID, MUTED, ORANGE, RED, SHADE, SHADE_ALT, STROKE, WATER, _esc as esc, wrap_svg
from nafes_common import (
    NAFES_FORBIDDEN_RE,
    dm,
    make_4_bilingual_options,
    make_4_math_options,
    nafes_concept,
)

ROOT = Path(__file__).resolve().parents[1]

NAFS_SCI_LEVELS = (
    "Science · Grade 6",
    "Science · Grade 9",
)
NAFS_SCI_TOPICS = (
    "Life Sciences",
    "Chemistry & Matter",
    "Physics: Forces & Energy",
    "Earth & Space Sciences",
)

NAFS_ENG_LEVELS = (
    "English · Grade 3",
    "English · Grade 6",
    "English · Grade 9",
)
NAFS_ENG_TOPICS = (
    "Reading Comprehension",
    "Text Analysis & Purpose",
    "Vocabulary & Context Clues",
    "Grammar & Sentence Structure",
)

PURPLE = "#7c3aed"
TEAL = "#0f766e"
TEAL_FILL = "#ccfbf1"
SLATE_BG = "#f8fafc"
LINE_GRID = "#e2e8f0"


def _ext_svg(w: int, h: int, body: str, title: str = "ETEC Nafes Visual Reference") -> str:
    return wrap_svg(body, w=w, h=h, disp_w=min(420, max(260, w)), title=title)


def wrap_passage_box(passage_html: str) -> str:
    """Wrap an English reading excerpt in a flat 1px container safe for both LTR & RTL cards."""
    return (
        '<div dir="ltr" class="mt-2 mb-2 px-3.5 py-2.5 rounded-lg border border-slate-200 dark:border-slate-700 '
        'bg-slate-50/70 dark:bg-slate-800/40 text-left text-sm leading-relaxed">'
        f"{passage_html}</div>"
    )


def make_ext_question(
    qid: str,
    track: str,
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
    assert track in ("nafes_science", "nafes_english"), f"Invalid track: {track}"
    if track == "nafes_science":
        assert level in NAFS_SCI_LEVELS, f"Invalid level: {level}"
        assert topic in NAFS_SCI_TOPICS, f"Invalid topic: {topic}"
        bp_key = "nafes_science_blueprint"
        scope = "etec_nafes_ksa_science_grades_6_9"
    else:
        assert level in NAFS_ENG_LEVELS, f"Invalid level: {level}"
        assert topic in NAFS_ENG_TOPICS, f"Invalid topic: {topic}"
        bp_key = "nafes_english_blueprint"
        scope = "etec_nafes_ksa_english_grades_3_6_9"

    assert difficulty in ("Easy", "Medium", "Hard"), f"Invalid difficulty: {difficulty}"
    assert len(opts_en) == 4 and len(opts_ar) == 4, f"4 options required: {qid}"
    assert 0 <= correct_idx < 4
    assert len({norm_text(o) for o in opts_en}) == 4, f"Dup EN options in {qid}: {opts_en}"
    assert len({norm_text(o) for o in opts_ar}) == 4, f"Dup AR options in {qid}: {opts_ar}"
    assert "\\\\(" not in q_en and "\\\\(" not in q_ar
    assert "<svg" not in q_en and "<svg" not in q_ar

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
        assert "**" not in blob, f"Raw markdown ** in {qid}"
        if track == "nafes_science":
            m_f = NAFES_FORBIDDEN_RE.search(blob)
            assert not m_f, f"Forbidden term '{m_f.group(0)}' in {qid}"

    return {
        "id": qid,
        "track": track,
        "level": level,
        "topic": topic,
        "type": "MCQ",
        "difficulty": difficulty,
        "correct_index": correct_idx,
        "correct_answer": str(correct_answer),
        bp_key: blueprint,
        "review": {
            "structural": "passed",
            "content": "programmatically_verified",
            "scope": scope,
        },
        "content": {
            "en": en_block,
            "ar": ar_block,
        },
    }


def make_science_math_q(
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
    opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, qid, suffix=suffix)
    return make_ext_question(
        qid=qid,
        track="nafes_science",
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


def make_science_concept_q(
    qid: str,
    level: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    option_pairs: list[tuple[str, str]],
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
    """option_pairs[0] is the correct (en, ar) pair; shuffled deterministically by qid."""
    opts_en, opts_ar, cidx, cans = make_4_bilingual_options(option_pairs, 0, qid)
    return make_ext_question(
        qid=qid,
        track="nafes_science",
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


def make_english_q(
    qid: str,
    level: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    options: list[str],
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
    """options[0] is the correct English answer option; kept in English in both EN & AR views."""
    assert len(options) == 4
    pairs = [(o, o) for o in options]
    opts_en, opts_ar, cidx, cans = make_4_bilingual_options(pairs, 0, qid)
    return make_ext_question(
        qid=qid,
        track="nafes_english",
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


def ext_worked_example(
    ex_id: str,
    title_en: str,
    title_ar: str,
    q_en: str,
    q_ar: str,
    idea_en: str,
    steps_en: list[str],
    check_en: str,
    idea_ar: str,
    steps_ar: list[str],
    check_ar: str,
    diagram_en: str,
    diagram_ar: str = None,
    correct_val=None,
    distractors: list = None,
    suffix: str = "",
    bilingual_pairs: list[tuple[str, str]] = None,
) -> dict:
    assert diagram_en and "<svg" in diagram_en, f"Worked example {ex_id} requires SVG"
    ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    if bilingual_pairs is not None:
        opts_en, opts_ar, cidx, cans = make_4_bilingual_options(bilingual_pairs, 0, ex_id)
    else:
        opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors or [], ex_id, suffix=suffix)

    clean_title_en = re.sub(r"^(?:Solved\s+)?Example\s*\d+\s*[:—\-–]\s*", "", title_en.strip(), flags=re.IGNORECASE)
    clean_title_ar = re.sub(r"^(?:ال)?مثال(?:\s+المحلول|\s+محلول)?\s*[\d٠-٩]+\s*[:—\-–]\s*", "", title_ar.strip())
    en_obj = {
        "title": _format_prose_html(clean_title_en),
        "question": _format_prose_html(q_en),
        "options": [_format_prose_html(o) for o in opts_en],
        "explanation": _format_prose_html(explain_en(idea_en, steps_en, check_en)),
        "diagram": diagram_en,
    }
    ar_obj = {
        "title": _format_prose_html(clean_title_ar),
        "question": _format_prose_html(q_ar),
        "options": [_format_prose_html(o) for o in opts_ar],
        "explanation": _format_prose_html(explain_ar(idea_ar, steps_ar, check_ar)),
        "diagram": diagram_ar if diagram_ar else diagram_en,
    }
    return {"id": ex_id, "correct_index": cidx, "correct_answer": str(cans), "en": en_obj, "ar": ar_obj}


def make_ext_lesson(
    lesson_id: str,
    track: str,
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
    cheat_sheet_en: list[tuple[str, str]],
    cheat_sheet_ar: list[tuple[str, str]],
    traps_en: list[str],
    traps_ar: list[str],
    examples: list[dict],
    blueprints: list[str],
) -> dict:
    assert len(concepts) >= 3
    assert len(examples) >= 4
    assert len(cheat_sheet_en) == 4 and len(cheat_sheet_ar) == 4
    clean_unit = re.sub(r"^(?:Lesson|درس)\s+", "", str(unit_num).strip(), flags=re.IGNORECASE)
    return {
        "id": lesson_id,
        "track": track,
        "level": level,
        "unit_num": clean_unit,
        "topic": topic,
        "blueprints": blueprints,
        "en": {
            "title": _format_prose_html(title_en),
            "summary": _format_prose_html(summary_en),
            "goals": [_format_prose_html(g) for g in goals_en],
            "concepts": [c["en"] for c in concepts],
            "cheat_sheet": [{"title": _format_prose_html(t), "formula": _format_prose_html(f)} for t, f in cheat_sheet_en],
            "traps": [_format_prose_html(t) for t in traps_en],
            "examples": [{"id": ex["id"], "correct_index": ex["correct_index"], **ex["en"]} for ex in examples],
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "summary": _format_prose_html(summary_ar),
            "goals": [_format_prose_html(g) for g in goals_ar],
            "concepts": [c["ar"] for c in concepts],
            "cheat_sheet": [{"title": _format_prose_html(t), "formula": _format_prose_html(f)} for t, f in cheat_sheet_ar],
            "traps": [_format_prose_html(t) for t in traps_ar],
            "examples": [{"id": ex["id"], "correct_index": ex["correct_index"], **ex["ar"]} for ex in examples],
        },
    }


# ==============================================================================
# Clean Science SVG Generators (font-size >= 11.5; banner headers = 14px)
# ==============================================================================

def svg_cell_diagram(cell_type: str = "plant", highlight: str = "Chloroplast", title: str = "Cell Structure") -> str:
    w, h = 360, 195
    parts = [
        f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.4"/>',
        f'<text x="180" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    if cell_type == "plant":
        parts.append(f'<rect x="65" y="46" width="160" height="122" rx="16" fill="#ecfdf5" stroke="{GREEN}" stroke-width="3"/>')
        parts.append(f'<rect x="74" y="54" width="142" height="106" rx="11" fill="#ffffff" stroke="{TEAL}" stroke-width="1.3" stroke-dasharray="4 3"/>')
        parts.append(f'<circle cx="112" cy="88" r="20" fill="{SHADE}" stroke="{PURPLE}" stroke-width="1.8"/>')
        parts.append(f'<ellipse cx="168" cy="118" rx="34" ry="22" fill="{WATER}" stroke="{BLUE}" stroke-width="1.6"/>')
        parts.append(f'<ellipse cx="108" cy="134" rx="18" ry="10" fill="#bbf7d0" stroke="{GREEN}" stroke-width="1.6"/>')
        labels = [
            (225, 62, "Cell Wall", 242, 66),
            (130, 84, "Nucleus", 242, 94),
            (200, 118, "Vacuole", 242, 122),
            (126, 136, "Chloroplast", 242, 150),
        ]
    else:
        parts.append(f'<ellipse cx="145" cy="108" rx="82" ry="56" fill="#eff6ff" stroke="{BLUE}" stroke-width="2.4"/>')
        parts.append(f'<circle cx="122" cy="102" r="22" fill="{SHADE}" stroke="{PURPLE}" stroke-width="1.8"/>')
        parts.append(f'<ellipse cx="176" cy="88" rx="18" ry="10" fill="{SHADE_ALT}" stroke="{ORANGE}" stroke-width="1.6"/>')
        parts.append(f'<circle cx="175" cy="132" r="10" fill="#e2e8f0" stroke="{MUTED}" stroke-width="1.4"/>')
        labels = [
            (215, 76, "Membrane", 242, 66),
            (142, 98, "Nucleus", 242, 94),
            (194, 88, "Mitochondria", 242, 122),
            (184, 134, "Cytoplasm", 242, 150),
        ]
    for sx, sy, lbl, tx, ty in labels:
        active = highlight.lower() in lbl.lower()
        col = RED if active else STROKE
        fw = "800" if active else "600"
        parts.append(f'<line x1="{sx}" y1="{sy}" x2="{tx-4}" y2="{ty-4}" stroke="{col}" stroke-width="1.3"/>')
        parts.append(f'<text x="{tx}" y="{ty}" font-size="12" font-weight="{fw}" fill="{col}">{esc(lbl)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_food_chain(steps: list[str], title: str = "Food Chain Flow") -> str:
    w, h = 380, 145
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="190" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    n = len(steps)
    bw = 74
    gap = (w - 40 - n * bw) / max(1, n - 1)
    fills = ["#dcfce7", "#dbeafe", "#fef3c7", "#fee2e2"]
    edges = [GREEN, BLUE, ORANGE, RED]
    for i, s in enumerate(steps):
        x = 20 + i * (bw + gap)
        parts.append(f'<rect x="{x:.1f}" y="52" width="{bw}" height="48" rx="9" fill="{fills[i % 4]}" stroke="{edges[i % 4]}" stroke-width="1.7"/>')
        parts.append(f'<text x="{x + bw/2:.1f}" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(s)}</text>')
        if i < n - 1:
            ax1 = x + bw + 3
            ax2 = x + bw + gap - 4
            parts.append(f'<line x1="{ax1:.1f}" y1="76" x2="{ax2:.1f}" y2="76" stroke="{STROKE}" stroke-width="1.8"/>')
            parts.append(f'<polygon points="{ax2:.1f},72 {ax2+5:.1f},76 {ax2:.1f},80" fill="{STROKE}"/>')
    parts.append(f'<text x="190" y="124" text-anchor="middle" font-size="11.5" font-weight="600" fill="{MUTED}">Producer → Consumers</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_energy_pyramid(tiers: list[tuple[str, str]], title: str = "Trophic Energy Pyramid") -> str:
    w, h = 360, 195
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    fills = ["#fee2e2", "#fef3c7", "#dbeafe", "#dcfce7"]
    edges = [RED, ORANGE, BLUE, GREEN]
    widths = [92, 152, 214, 280]
    y0 = 42
    th = 34
    for idx, ((name, energy), tw) in enumerate(zip(tiers, widths)):
        x = (w - tw) / 2
        y = y0 + idx * (th + 2)
        parts.append(f'<rect x="{x:.1f}" y="{y}" width="{tw}" height="{th}" rx="6" fill="{fills[idx % 4]}" stroke="{edges[idx % 4]}" stroke-width="1.5"/>')
        parts.append(f'<text x="{w/2:.1f}" y="{y+21}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(name)}: {esc(energy)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_punnett_square(p1: str, p2: str, cells: list[str], title: str = "Punnett Square") -> str:
    w, h = 290, 200
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="145" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    gx, gy, s = 92, 62, 54
    parts.append(f'<text x="{gx+27}" y="52" text-anchor="middle" font-size="13" font-weight="800" fill="{BLUE}">{esc(p1[0])}</text>')
    parts.append(f'<text x="{gx+81}" y="52" text-anchor="middle" font-size="13" font-weight="800" fill="{BLUE}">{esc(p1[1])}</text>')
    parts.append(f'<text x="{gx-18}" y="{gy+31}" text-anchor="middle" font-size="13" font-weight="800" fill="{GREEN}">{esc(p2[0])}</text>')
    parts.append(f'<text x="{gx-18}" y="{gy+85}" text-anchor="middle" font-size="13" font-weight="800" fill="{GREEN}">{esc(p2[1])}</text>')
    for idx, val in enumerate(cells):
        r, c = divmod(idx, 2)
        x = gx + c * s
        y = gy + r * s
        fc = "#dbeafe" if any(ch.isupper() for ch in val) else "#fef3c7"
        parts.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{fc}" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(f'<text x="{x+27}" y="{y+32}" text-anchor="middle" font-size="14" font-weight="800" fill="{STROKE}">{esc(val)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_states_of_matter(highlight: str = "Liquid", title: str = "States of Matter") -> str:
    w, h = 360, 155
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    states = [("Solid", 26, "#dbeafe", BLUE), ("Liquid", 138, "#ccfbf1", TEAL), ("Gas", 250, "#fef3c7", ORANGE)]
    for name, bx, fc, ec in states:
        is_hi = highlight.lower() == name.lower()
        sw = "2.5" if is_hi else "1.4"
        parts.append(f'<rect x="{bx}" y="44" width="84" height="72" rx="8" fill="#ffffff" stroke="{ec}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{bx+42}" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="{ec}">{name}</text>')
        if name == "Solid":
            for r in range(3):
                for c in range(3):
                    parts.append(f'<circle cx="{bx+22+c*20}" cy="{60+r*20}" r="6" fill="{fc}" stroke="{ec}" stroke-width="1.2"/>')
        elif name == "Liquid":
            pts = [(20, 96), (40, 100), (60, 96), (30, 80), (52, 82), (24, 65), (48, 66), (65, 76)]
            for px, py in pts:
                parts.append(f'<circle cx="{bx+px}" cy="{py}" r="5.5" fill="{fc}" stroke="{ec}" stroke-width="1.2"/>')
        else:
            pts = [(18, 58), (64, 62), (38, 78), (22, 98), (62, 96)]
            for px, py in pts:
                parts.append(f'<circle cx="{bx+px}" cy="{py}" r="5.5" fill="{fc}" stroke="{ec}" stroke-width="1.2"/>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_atom_bohr(symbol: str, p_cnt: int, n_cnt: int, shells: list[int], title: str = "Atomic Model") -> str:
    w, h = 340, 185
    cx, cy = 115, 102
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="170" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    radii = [34, 54, 72]
    for s_idx, e_cnt in enumerate(shells[:3]):
        r = radii[s_idx]
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="3 2"/>')
        import math
        for k in range(e_cnt):
            ang = 2 * math.pi * k / max(1, e_cnt)
            ex = cx + r * math.cos(ang)
            ey = cy + r * math.sin(ang)
            parts.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4.2" fill="{BLUE}" stroke="#ffffff" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="#fef3c7" stroke="{ORANGE}" stroke-width="2"/>')
    parts.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{esc(symbol)}</text>')
    # Info box on right
    parts.append(f'<rect x="210" y="54" width="112" height="96" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>')
    parts.append(f'<text x="266" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="{RED}">p+ = {p_cnt}</text>')
    parts.append(f'<text x="266" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">n0 = {n_cnt}</text>')
    parts.append(f'<text x="266" y="126" text-anchor="middle" font-size="12" font-weight="700" fill="{BLUE}">e- = {sum(shells)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_ph_scale(marker_ph: float, sample_label: str, title: str = "pH Scale") -> str:
    w, h = 370, 145
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="185" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    colors = [
        "#ef4444", "#f97316", "#f59e0b", "#eab308", "#a3e635",
        "#4ade80", "#34d399", "#22c55e", "#2dd4bf", "#38bdf8",
        "#60a5fa", "#818cf8", "#a78bfa", "#c084fc", "#9333ea"
    ]
    bx, bw = 24, 322
    sw = bw / 15.0
    for ph in range(15):
        x = bx + ph * sw
        parts.append(f'<rect x="{x:.1f}" y="68" width="{sw:.1f}" height="28" fill="{colors[ph]}" stroke="#ffffff" stroke-width="1"/>')
        if ph in (0, 3, 7, 10, 14):
            parts.append(f'<text x="{x + sw/2:.1f}" y="114" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{ph}</text>')
    mx = bx + (marker_ph + 0.5) * sw
    parts.append(f'<polygon points="{mx:.1f},64 {mx-6:.1f},52 {mx+6:.1f},52" fill="{STROKE}"/>')
    parts.append(f'<text x="{mx:.1f}" y="47" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(sample_label)} (pH {marker_ph:g})</text>')
    parts.append(f'<text x="58" y="129" text-anchor="middle" font-size="11.5" font-weight="700" fill="{RED}">Acidic</text>')
    parts.append(f'<text x="185" y="129" text-anchor="middle" font-size="11.5" font-weight="700" fill="{GREEN}">Neutral (7)</text>')
    parts.append(f'<text x="310" y="129" text-anchor="middle" font-size="11.5" font-weight="700" fill="{PURPLE}">Basic</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_force_block(left_f: int, right_f: int, mass_kg: int = None, title: str = "Force Diagram") -> str:
    w, h = 360, 155
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="30" y1="122" x2="330" y2="122" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="142" y="68" width="76" height="54" rx="8" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>',
    ]
    center_lbl = f"{mass_kg} kg" if mass_kg is not None else "Object"
    parts.append(f'<text x="180" y="100" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{esc(center_lbl)}</text>')
    if left_f > 0:
        parts.append(f'<line x1="142" y1="95" x2="62" y2="95" stroke="{RED}" stroke-width="3"/>')
        parts.append(f'<polygon points="62,89 50,95 62,101" fill="{RED}"/>')
        parts.append(f'<text x="95" y="80" text-anchor="middle" font-size="13" font-weight="800" fill="{RED}">{left_f} N</text>')
    if right_f > 0:
        parts.append(f'<line x1="218" y1="95" x2="298" y2="95" stroke="{GREEN}" stroke-width="3"/>')
        parts.append(f'<polygon points="298,89 310,95 298,101" fill="{GREEN}"/>')
        parts.append(f'<text x="265" y="80" text-anchor="middle" font-size="13" font-weight="800" fill="{GREEN}">{right_f} N</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_ohm_circuit(voltage_v: int, r_vals: list[int], mode: str = "series", title: str = "Electric Circuit") -> str:
    w, h = 360, 175
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    if mode == "series":
        parts.append(f'<rect x="65" y="54" width="230" height="86" rx="6" fill="none" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<rect x="44" y="84" width="44" height="26" rx="5" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="66" y="101" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{voltage_v} V</text>')
        xs = [125, 205] if len(r_vals) == 2 else [155]
        for idx, rv in enumerate(r_vals[:2]):
            rx = xs[idx]
            parts.append(f'<rect x="{rx}" y="42" width="58" height="24" rx="5" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.8"/>')
            parts.append(f'<text x="{rx+29}" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{rv} Ω</text>')
    else:
        parts.append(f'<rect x="65" y="52" width="230" height="96" rx="6" fill="none" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<line x1="65" y1="100" x2="295" y2="100" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<rect x="40" y="86" width="48" height="26" rx="5" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="64" y="103" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{voltage_v} V</text>')
        for idx, ry in enumerate((40, 88)):
            rv = r_vals[idx % len(r_vals)]
            parts.append(f'<rect x="155" y="{ry}" width="64" height="24" rx="5" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.8"/>')
            parts.append(f'<text x="187" y="{ry+16}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{rv} Ω</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_motion_graph(points: list[tuple[float, float]], y_label: str = "Speed (m/s)", x_label: str = "Time (s)", title: str = "Motion Graph") -> str:
    w, h = 360, 222
    ox, oy, gw, gh = 58, 168, 260, 104
    max_x = max(p[0] for p in points) or 1
    max_y = max(p[1] for p in points) or 1
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    for i in range(5):
        gy = oy - i * gh / 4
        parts.append(f'<line x1="{ox}" y1="{gy:.1f}" x2="{ox+gw}" y2="{gy:.1f}" stroke="{LINE_GRID}" stroke-width="1"/>')
        yv = max_y * i / 4
        parts.append(f'<text x="{ox-8}" y="{gy+4:.1f}" text-anchor="end" font-size="11.5" font-weight="600" fill="{MUTED}">{yv:g}</text>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+gw}" y2="{oy}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-gh}" stroke="{STROKE}" stroke-width="1.8"/>')
    coords = []
    for px, py in points:
        sx = ox + (px / max_x) * gw
        sy = oy - (py / max_y) * gh
        coords.append((sx, sy, px, py))
    poly = " ".join(f"{sx:.1f},{sy:.1f}" for sx, sy, _, _ in coords)
    parts.append(f'<polyline points="{poly}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>')
    for sx, sy, px, _ in coords:
        parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4.2" fill="{BLUE}" stroke="#ffffff" stroke-width="1.2"/>')
        parts.append(f'<text x="{sx:.1f}" y="{oy+16}" text-anchor="middle" font-size="11.5" font-weight="600" fill="{MUTED}">{px:g}</text>')
    parts.append(f'<text x="{ox+gw/2:.1f}" y="{h-14}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(x_label)}</text>')
    parts.append(f'<text x="{ox}" y="48" font-size="12" font-weight="700" fill="{STROKE}">{esc(y_label)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_wave_diagram(wavelength_m: float, amp_m: float, title: str = "Transverse Wave") -> str:
    w, h = 360, 175
    ox, mid_y = 32, 102
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="{ox}" y1="{mid_y}" x2="328" y2="{mid_y}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4 3"/>',
    ]
    import math
    pts = []
    for k in range(149):
        x = ox + k * 2
        y = mid_y - 34 * math.sin(2 * math.pi * (k * 2) / 140.0)
        pts.append(f"{x:.1f},{y:.1f}")
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>')
    # Crest-to-crest wavelength bar
    c1, c2 = ox + 35, ox + 175
    parts.append(f'<line x1="{c1}" y1="54" x2="{c2}" y2="54" stroke="{RED}" stroke-width="2"/>')
    parts.append(f'<text x="{(c1+c2)/2}" y="48" text-anchor="middle" font-size="12" font-weight="700" fill="{RED}">λ = {wavelength_m:g} m</text>')
    # Amplitude vertical arrow
    parts.append(f'<line x1="{c2}" y1="{mid_y}" x2="{c2}" y2="{mid_y-34}" stroke="{GREEN}" stroke-width="2"/>')
    parts.append(f'<text x="{c2+12}" y="{mid_y-14}" font-size="12" font-weight="700" fill="{GREEN}">A = {amp_m:g} m</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_earth_layers(highlight: str = "Mantle", title: str = "Earth Internal Layers") -> str:
    w, h = 360, 195
    cx, cy = 115, 110
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="{cx}" cy="{cy}" r="68" fill="#cbd5e1" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<circle cx="{cx}" cy="{cy}" r="58" fill="#fdba74" stroke="{ORANGE}" stroke-width="1.6"/>',
        f'<circle cx="{cx}" cy="{cy}" r="36" fill="#f87171" stroke="{RED}" stroke-width="1.6"/>',
        f'<circle cx="{cx}" cy="{cy}" r="18" fill="#fef08a" stroke="{ORANGE}" stroke-width="1.6"/>',
    ]
    rows = [("Crust", 63, 62), ("Mantle", 47, 92), ("Outer Core", 27, 122), ("Inner Core", 8, 152)]
    for lbl, r_off, ty in rows:
        is_hi = highlight.lower() in lbl.lower()
        col = RED if is_hi else STROKE
        fw = "800" if is_hi else "600"
        parts.append(f'<line x1="{cx+r_off}" y1="{cy}" x2="226" y2="{ty-4}" stroke="{col}" stroke-width="1.3"/>')
        parts.append(f'<text x="232" y="{ty}" font-size="12" font-weight="{fw}" fill="{col}">{lbl}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_moon_phases(phase_name: str = "Full Moon", title: str = "Sun · Earth · Moon") -> str:
    w, h = 360, 165
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="52" cy="96" r="24" fill="#fde047" stroke="{ORANGE}" stroke-width="2"/>',
        f'<text x="52" y="138" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">Sun</text>',
        f'<circle cx="220" cy="96" r="64" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="4 3"/>',
        f'<circle cx="220" cy="96" r="18" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>',
        f'<text x="220" y="128" text-anchor="middle" font-size="11.5" font-weight="700" fill="{BLUE}">Earth</text>',
    ]
    positions = [("New Moon", 156, 96, "#334155"), ("Full Moon", 284, 96, "#ffffff"), ("Quarter", 220, 42, "#cbd5e1")]
    for nm, mx, my, fc in positions:
        ring = RED if phase_name.lower() in nm.lower() else STROKE
        parts.append(f'<circle cx="{mx}" cy="{my}" r="11" fill="{fc}" stroke="{ring}" stroke-width="2"/>')
    parts.append(f'<text x="292" y="142" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(phase_name)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_plate_boundary(btype: str = "Convergent", title: str = "Tectonic Plate Boundary") -> str:
    w, h = 360, 155
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="34" y="68" width="136" height="44" rx="4" fill="#fed7aa" stroke="{ORANGE}" stroke-width="1.8"/>',
        f'<rect x="190" y="68" width="136" height="44" rx="4" fill="#bfdbfe" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<text x="102" y="95" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">Plate A</text>',
        f'<text x="258" y="95" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">Plate B</text>',
    ]
    if btype == "Convergent":
        parts.append(f'<line x1="78" y1="54" x2="146" y2="54" stroke="{RED}" stroke-width="2.5"/>')
        parts.append(f'<polygon points="146,48 158,54 146,60" fill="{RED}"/>')
        parts.append(f'<line x1="282" y1="54" x2="214" y2="54" stroke="{RED}" stroke-width="2.5"/>')
        parts.append(f'<polygon points="214,48 202,54 214,60" fill="{RED}"/>')
    elif btype == "Divergent":
        parts.append(f'<line x1="146" y1="54" x2="78" y2="54" stroke="{TEAL}" stroke-width="2.5"/>')
        parts.append(f'<polygon points="78,48 66,54 78,60" fill="{TEAL}"/>')
        parts.append(f'<line x1="214" y1="54" x2="282" y2="54" stroke="{TEAL}" stroke-width="2.5"/>')
        parts.append(f'<polygon points="282,48 294,54 282,60" fill="{TEAL}"/>')
    else:
        parts.append(f'<line x1="172" y1="48" x2="172" y2="112" stroke="{PURPLE}" stroke-width="2.5"/>')
        parts.append(f'<line x1="188" y1="112" x2="188" y2="48" stroke="{PURPLE}" stroke-width="2.5"/>')
    parts.append(f'<text x="180" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">Boundary: {esc(btype)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


# ==============================================================================
# Clean English Literacy & Grammar SVG Generators (font-size >= 11.5; headers 14)
# ==============================================================================

def svg_reading_card(title: str, rows: list[tuple[str, str]]) -> str:
    """Clean 2-column notice / schedule card (up to 4 short rows)."""
    h = 58 + len(rows) * 32
    w = 370
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="10" fill="#ffffff" stroke="{STROKE}" stroke-width="1.6"/>',
        f'<rect x="8" y="8" width="{w-16}" height="34" rx="10" fill="#eff6ff"/>',
        f'<line x1="8" y1="42" x2="{w-8}" y2="42" stroke="{STROKE}" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="30" text-anchor="middle" font-size="14" font-weight="800" fill="{BLUE}">{esc(title)}</text>',
    ]
    for i, (k, v) in enumerate(rows[:4]):
        y = 42 + i * 32
        if i > 0:
            parts.append(f'<line x1="16" y1="{y}" x2="{w-16}" y2="{y}" stroke="{LINE_GRID}" stroke-width="1"/>')
        parts.append(f'<text x="24" y="{y+21}" font-size="12" font-weight="700" fill="{STROKE}">{esc(k)}</text>')
        parts.append(f'<text x="{w-24}" y="{y+21}" text-anchor="end" font-size="12" font-weight="600" fill="{TEAL}">{esc(v)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_sequence_strip(steps: list[str], title: str = "Sequence of Events") -> str:
    w, h = 380, 145
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="190" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    bw = 96
    gap = (w - 36 - 3 * bw) / 2
    fills = ["#dbeafe", "#ccfbf1", "#fef3c7"]
    edges = [BLUE, TEAL, ORANGE]
    for i, st in enumerate(steps[:3]):
        x = 18 + i * (bw + gap)
        parts.append(f'<rect x="{x:.1f}" y="52" width="{bw}" height="56" rx="8" fill="{fills[i]}" stroke="{edges[i]}" stroke-width="1.6"/>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="70" text-anchor="middle" font-size="11.5" font-weight="800" fill="{edges[i]}">Step {i+1}</text>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(st)}</text>')
        if i < 2:
            ax1 = x + bw + 3
            ax2 = x + bw + gap - 4
            parts.append(f'<line x1="{ax1:.1f}" y1="80" x2="{ax2:.1f}" y2="80" stroke="{STROKE}" stroke-width="1.8"/>')
            parts.append(f'<polygon points="{ax2:.1f},76 {ax2+5:.1f},80 {ax2:.1f},84" fill="{STROKE}"/>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_idea_map(main_idea: str, details: list[str], title: str = "Main Idea Map") -> str:
    w, h = 370, 175
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="185" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="55" y="42" width="260" height="36" rx="8" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<text x="185" y="65" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(main_idea)}</text>',
    ]
    xs = [18, 134, 250]
    for i, det in enumerate(details[:3]):
        bx = xs[i]
        parts.append(f'<line x1="185" y1="78" x2="{bx+50}" y2="108" stroke="{MUTED}" stroke-width="1.5"/>')
        parts.append(f'<rect x="{bx}" y="108" width="102" height="44" rx="7" fill="#ffffff" stroke="{TEAL}" stroke-width="1.5"/>')
        parts.append(f'<text x="{bx+51}" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(det)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_word_morphology(prefix: str, root: str, suffix: str, meaning: str, title: str = "Word Parts") -> str:
    w, h = 360, 155
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    blocks = [
        ("Prefix", prefix or "—", 24, "#fee2e2", RED),
        ("Root", root, 134, "#dbeafe", BLUE),
        ("Suffix", suffix or "—", 244, "#dcfce7", GREEN),
    ]
    for kind, txt, bx, fc, ec in blocks:
        parts.append(f'<rect x="{bx}" y="48" width="92" height="54" rx="8" fill="{fc}" stroke="{ec}" stroke-width="1.7"/>')
        parts.append(f'<text x="{bx+46}" y="66" text-anchor="middle" font-size="11.5" font-weight="700" fill="{ec}">{kind}</text>')
        parts.append(f'<text x="{bx+46}" y="89" text-anchor="middle" font-size="14" font-weight="800" fill="{STROKE}">{esc(txt)}</text>')
    parts.append(f'<text x="180" y="129" text-anchor="middle" font-size="12.5" font-weight="700" fill="{STROKE}">Meaning: {esc(meaning)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def svg_tense_timeline(marker_label: str, pos_pct: float, span_pct: float = 0.0, title: str = "Tense Timeline") -> str:
    w, h = 360, 145
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="36" y1="88" x2="324" y2="88" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<line x1="180" y1="74" x2="180" y2="102" stroke="{TEAL}" stroke-width="2"/>',
        f'<text x="52" y="118" text-anchor="middle" font-size="12" font-weight="700" fill="{MUTED}">Past</text>',
        f'<text x="180" y="118" text-anchor="middle" font-size="12" font-weight="800" fill="{TEAL}">Now</text>',
        f'<text x="308" y="118" text-anchor="middle" font-size="12" font-weight="700" fill="{MUTED}">Future</text>',
    ]
    px = 36 + max(0.0, min(1.0, pos_pct)) * 288
    if span_pct > 0:
        sx = 36 + max(0.0, min(1.0, span_pct)) * 288
        parts.append(f'<line x1="{px:.1f}" y1="76" x2="{sx:.1f}" y2="76" stroke="{BLUE}" stroke-width="4"/>')
        parts.append(f'<text x="{(px+sx)/2:.1f}" y="62" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(marker_label)}</text>')
    else:
        parts.append(f'<circle cx="{px:.1f}" cy="88" r="7" fill="{RED}" stroke="#ffffff" stroke-width="1.5"/>')
        parts.append(f'<text x="{px:.1f}" y="66" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(marker_label)}</text>')
    return _ext_svg(w, h, "".join(parts), title)
