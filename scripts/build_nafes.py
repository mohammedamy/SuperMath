"""Build & strictly validate data/nafes.json: 1,080 ETEC-Aligned Nafes KSA (Grades 3, 6, 9) 4-option (A–D) MCQs."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from nafes_common import (
    NAFES_FORBIDDEN_RE,
    NAFES_LEVELS,
    NAFES_TOPICS,
    load_other_track_stems,
    norm_text,
)
from nafes_g3_bank import build_grade3_bank
from nafes_g6_bank import build_grade6_bank
from nafes_g9_bank import build_grade9_bank


def main() -> None:
    other_stems = load_other_track_stems()
    g3 = build_grade3_bank()
    g6 = build_grade6_bank()
    g9 = build_grade9_bank()
    assert len(g3) == 360, f"Expected 360 Grade 3 questions, got {len(g3)}"
    assert len(g6) == 360, f"Expected 360 Grade 6 questions, got {len(g6)}"
    assert len(g9) == 360, f"Expected 360 Grade 9 questions, got {len(g9)}"

    bank = g3 + g6 + g9
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
        assert q["track"] == "nafes"
        assert q["level"] in NAFES_LEVELS, f"Invalid level in {qid}: {q['level']}"
        assert q["topic"] in NAFES_TOPICS, f"Invalid topic in {qid}: {q['topic']}"
        assert q["difficulty"] in ("Easy", "Medium", "Hard")
        assert q["type"] == "MCQ"
        assert isinstance(q["correct_index"], int) and 0 <= q["correct_index"] < 4

        stem = norm_text(q["content"]["en"]["question"])
        assert stem not in other_stems, f"Global stem collision with another track in {qid}: {stem[:80]}"
        assert stem not in seen_stems, f"Internal Nafes duplicate stem in {qid}: {stem[:80]}"
        seen_stems.add(stem)

        if q["content"]["en"].get("diagram"):
            svg_count += 1

        for lang in ("en", "ar"):
            c = q["content"][lang]
            assert len(c["options"]) == 4, f"{qid} {lang} option count != 4"
            assert len({norm_text(o) for o in c["options"]}) == 4, f"{qid} {lang} duplicate options"
            for field in (c["question"], *c["options"], c.get("hint", ""), c["explanation"]):
                assert "**" not in field, f"Raw markdown ** in {qid} {lang}: {field[:80]}"
                assert "\\\\(" not in field and "\\\\[" not in field, f"Double-escaped math in {qid} {lang}"
                assert field.count("\\(") == field.count("\\)"), f"Unbalanced inline math in {qid} {lang}"
                assert field.count("\\[") == field.count("\\]"), f"Unbalanced display math in {qid} {lang}"
                m_f = NAFES_FORBIDDEN_RE.search(field)
                assert not m_f, f"Forbidden out-of-scope term '{m_f.group(0)}' in {qid} {lang}"
            if c.get("diagram"):
                ET.fromstring(c["diagram"])

        bp_counts[q["nafes_blueprint"]] += 1
        level_counts[q["level"]] += 1
        diff_counts[q["difficulty"]] += 1
        topic_counts[q["topic"]] += 1

    assert len(bp_counts) == 72, f"Expected 72 distinct Nafes blueprints, got {len(bp_counts)}"
    for bp, cnt in bp_counts.items():
        assert cnt == 15, f"Expected 15 Qs for blueprint {bp}, got {cnt}"
    assert svg_count >= 900, f"Expected >= 900 SVG diagrams across Nafes, got {svg_count}"

    out_path = ROOT / "data" / "nafes.json"
    out_path.write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"OK: Wrote {len(bank)} verified Nafes questions | {len(bp_counts)} blueprints | "
        f"{svg_count} SVGs ({svg_count * 100 // len(bank)}%) | diffs={dict(diff_counts)} | "
        f"topics={dict(topic_counts)} | {out_path.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()

