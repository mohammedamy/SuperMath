"""Shared helpers for building bilingual, beginner-friendly KAUST (KMC) Study Lessons."""
import xml.etree.ElementTree as ET
from kmc_common import m, explain_en, explain_ar, _format_prose_html, make_5_math_options, make_5_bilingual_options


def dm(expr: str) -> str:
    """Wrap a display-math formula cleanly in \\[ ... \\]."""
    return f"\\[ {expr} \\]"


def concept(title_en: str, title_ar: str, body_en: str, body_ar: str,
            formula_en: str = "", formula_ar: str = "",
            diagram_en: str = None, diagram_ar: str = None) -> dict:
    if diagram_en:
        ET.fromstring(diagram_en)
    if diagram_ar:
        ET.fromstring(diagram_ar)
    out = {
        "en": {
            "title": _format_prose_html(title_en),
            "body": _format_prose_html(body_en),
            "formula": _format_prose_html(formula_en) if formula_en else "",
        },
        "ar": {
            "title": _format_prose_html(title_ar),
            "body": _format_prose_html(body_ar),
            "formula": _format_prose_html(formula_ar or formula_en) if (formula_ar or formula_en) else "",
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

