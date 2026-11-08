"""Build & strictly validate data/olympiad.json: 1,080 Official-Scope Olympiad Math (Grades 7–12: Tier 1 Junior, Tier 2 Intermediate, Tier 3 Senior) 5-option MCQs with 100% SVGs."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from olympiad_common import (
    OLYMPIAD_FORBIDDEN_RE,
    OLYMPIAD_LEVELS,
    OLYMPIAD_TOPICS,
    load_other_olympiad_stems,
    norm_text,
)
from olympiad_t1_bank import build_tier1_bank
from olympiad_t2_bank import build_tier2_bank
from olympiad_t3_bank import build_tier3_bank


def main() -> None:
    other_stems = load_other_olympiad_stems()
    t1 = build_tier1_bank()
    t2 = build_tier2_bank()
    t3 = build_tier3_bank()
    assert len(t1) == 360, f"Expected 360 Tier 1 questions, got {len(t1)}"
    assert len(t2) == 360, f"Expected 360 Tier 2 questions, got {len(t2)}"
    assert len(t3) == 360, f"Expected 360 Tier 3 questions, got {len(t3)}"

    bank = t1 + t2 + t3
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
        assert q["track"] == "olympiad"
        assert q["level"] in OLYMPIAD_LEVELS, f"Invalid level in {qid}: {q['level']}"
        assert q["topic"] in OLYMPIAD_TOPICS, f"Invalid topic in {qid}: {q['topic']}"
        assert q["difficulty"] in ("Easy", "Medium", "Hard")
        assert q["type"] == "MCQ"
        assert isinstance(q["correct_index"], int) and 0 <= q["correct_index"] < 5

        stem = norm_text(q["content"]["en"]["question"])
        assert stem not in other_stems, f"Global stem collision with another track in {qid}: {stem[:80]}"
        assert stem not in seen_stems, f"Internal Olympiad duplicate stem in {qid}: {stem[:80]}"
        seen_stems.add(stem)

        if q["content"]["en"].get("diagram"):
            svg_count += 1

        for lang in ("en", "ar"):
            c = q["content"][lang]
            assert len(c["options"]) == 5, f"{qid} {lang} option count != 5"
            assert len({norm_text(o) for o in c["options"]}) == 5, f"{qid} {lang} duplicate options"
            assert "<svg" not in c["question"], f"Embedded SVG inside question text in {qid} {lang}"
            for field in (c["question"], *c["options"], c.get("hint", ""), c["explanation"]):
                assert "**" not in field, f"Raw markdown ** in {qid} {lang}: {field[:80]}"
                assert "\\\\(" not in field and "\\\\[" not in field, f"Double-escaped math in {qid} {lang}"
                assert field.count("\\(") == field.count("\\)"), f"Unbalanced inline math in {qid} {lang}"
                assert field.count("\\[") == field.count("\\]"), f"Unbalanced display math in {qid} {lang}"
                m_f = OLYMPIAD_FORBIDDEN_RE.search(field)
                assert not m_f, f"Forbidden out-of-scope term '{m_f.group(0)}' in {qid} {lang}"
            assert c.get("diagram"), f"Missing diagram in {qid} {lang}"
            ET.fromstring(c["diagram"])

        bp_counts[q["olympiad_blueprint"]] += 1
        level_counts[q["level"]] += 1
        diff_counts[q["difficulty"]] += 1
        topic_counts[q["topic"]] += 1

    assert len(bp_counts) == 72, f"Expected 72 distinct Olympiad blueprints, got {len(bp_counts)}"
    for bp, cnt in bp_counts.items():
        assert cnt == 15, f"Expected 15 Qs for blueprint {bp}, got {cnt}"
    assert svg_count == 1080, f"Expected 1080/1080 SVG diagrams across Olympiad, got {svg_count}"

    out_path = ROOT / "data" / "olympiad.json"
    out_path.write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"OK: Wrote {len(bank)} verified Olympiad questions | {len(bp_counts)} blueprints | "
        f"{svg_count} SVGs ({svg_count * 100 // len(bank)}%) | diffs={dict(diff_counts)} | "
        f"topics={dict(topic_counts)} | {out_path.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()
