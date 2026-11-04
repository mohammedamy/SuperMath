"""Build & strictly validate data/kangaroo.json: 2,160 Official-Scope Kangaroo Math (Grades 1–12: PreEcolier, Ecolier, Benjamin, Cadet, Junior, Student) 5-option MCQs."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from kangaroo_common import (
    DIFF_TO_POINTS,
    KANGAROO_FORBIDDEN_RE,
    KANGAROO_LEVELS,
    KANGAROO_TOPICS,
    load_other_track_stems,
    norm_text,
)
from kangaroo_ben_bank import build_benjamin_bank
from kangaroo_cad_bank import build_cadet_bank
from kangaroo_eco_bank import build_ecolier_bank
from kangaroo_jun_bank import build_junior_bank
from kangaroo_pre_bank import build_preecolier_bank
from kangaroo_stu_bank import build_student_bank


def main() -> None:
    other_stems = load_other_track_stems()
    pre = build_preecolier_bank()
    eco = build_ecolier_bank()
    ben = build_benjamin_bank()
    cad = build_cadet_bank()
    jun = build_junior_bank()
    stu = build_student_bank()
    assert len(pre) == 360, f"Expected 360 PreEcolier questions, got {len(pre)}"
    assert len(eco) == 360, f"Expected 360 Ecolier questions, got {len(eco)}"
    assert len(ben) == 360, f"Expected 360 Benjamin questions, got {len(ben)}"
    assert len(cad) == 360, f"Expected 360 Cadet questions, got {len(cad)}"
    assert len(jun) == 360, f"Expected 360 Junior questions, got {len(jun)}"
    assert len(stu) == 360, f"Expected 360 Student questions, got {len(stu)}"

    bank = pre + eco + ben + cad + jun + stu
    seen_ids: set[str] = set()
    seen_stems: set[str] = set()
    svg_count = 0
    bp_counts: Counter[str] = Counter()
    level_counts: Counter[str] = Counter()
    diff_counts: Counter[str] = Counter()
    topic_counts: Counter[str] = Counter()

    for q in bank:
        qid = q["id"]
        assert qid not in seen_ids, f"Duplicate ID: {qid}"
        seen_ids.add(qid)
        assert q["track"] == "kangaroo"
        assert q["level"] in KANGAROO_LEVELS, f"Invalid level in {qid}: {q['level']}"
        assert q["topic"] in KANGAROO_TOPICS, f"Invalid topic in {qid}: {q['topic']}"
        assert q["difficulty"] in ("Easy", "Medium", "Hard")
        assert q.get("kang_points") == DIFF_TO_POINTS[q["difficulty"]], f"Points mismatch in {qid}"
        assert q["type"] == "MCQ"
        assert isinstance(q["correct_index"], int) and 0 <= q["correct_index"] < 5

        stem = norm_text(q["content"]["en"]["question"])
        assert stem not in other_stems, f"Global stem collision with another track in {qid}: {stem[:80]}"
        assert stem not in seen_stems, f"Internal Kangaroo duplicate stem in {qid}: {stem[:80]}"
        seen_stems.add(stem)

        if q["content"]["en"].get("diagram"):
            svg_count += 1

        for lang in ("en", "ar"):
            c = q["content"][lang]
            assert len(c["options"]) == 5, f"{qid} {lang} option count != 5"
            assert len({norm_text(o) for o in c["options"]}) == 5, f"{qid} {lang} duplicate options"
            for field in (c["question"], *c["options"], c.get("hint", ""), c["explanation"]):
                assert "**" not in field, f"Raw markdown ** in {qid} {lang}: {field[:80]}"
                assert "\\\\(" not in field and "\\\\[" not in field, f"Double-escaped math in {qid} {lang}"
                assert field.count("\\(") == field.count("\\)"), f"Unbalanced inline math in {qid} {lang}"
                assert field.count("\\[") == field.count("\\]"), f"Unbalanced display math in {qid} {lang}"
                m_f = KANGAROO_FORBIDDEN_RE.search(field)
                assert not m_f, f"Forbidden out-of-scope term '{m_f.group(0)}' in {qid} {lang}"
            if c.get("diagram"):
                ET.fromstring(c["diagram"])

        bp_counts[q["kangaroo_blueprint"]] += 1
        level_counts[q["level"]] += 1
        diff_counts[q["difficulty"]] += 1
        topic_counts[q["topic"]] += 1

    assert len(bp_counts) == 144, f"Expected 144 distinct Kangaroo blueprints, got {len(bp_counts)}"
    for bp, cnt in bp_counts.items():
        assert cnt == 15, f"Expected 15 Qs for blueprint {bp}, got {cnt}"
    assert svg_count == 2160, f"Expected 2160/2160 SVG diagrams across Kangaroo, got {svg_count}"

    out_path = ROOT / "data" / "kangaroo.json"
    out_path.write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"OK: Wrote {len(bank)} verified Kangaroo questions | {len(bp_counts)} blueprints | "
        f"{svg_count} SVGs ({svg_count * 100 // len(bank)}%) | diffs={dict(diff_counts)} | "
        f"topics={dict(topic_counts)} | {out_path.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()

