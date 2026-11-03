"""Build & strictly validate data/nsmo.json: 1,350 Official-Scope NSMO / Mawhiba (Grades 7–10) 4-option MCQs."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from nsmo_common import NSMO_FORBIDDEN_RE, NSMO_LEVELS, NSMO_TOPICS, load_other_track_stems, norm_text
from nsmo_p1_bank import build_p1_bank
from nsmo_p2_bank import build_p2_bank
from nsmo_p3_bank import build_p3_bank


def main() -> None:
    other_stems = load_other_track_stems()
    p1 = build_p1_bank()
    p2 = build_p2_bank()
    p3 = build_p3_bank()
    assert len(p1) == 450, f"Expected 450 Phase 1 questions, got {len(p1)}"
    assert len(p2) == 450, f"Expected 450 Phase 2 questions, got {len(p2)}"
    assert len(p3) == 450, f"Expected 450 Phase 3 questions, got {len(p3)}"

    bank = p1 + p2 + p3
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
        assert q["track"] == "nsmo"
        assert q["level"] in NSMO_LEVELS, f"Invalid level in {qid}: {q['level']}"
        assert q["topic"] in NSMO_TOPICS, f"Invalid topic in {qid}: {q['topic']}"
        assert q["difficulty"] in ("Easy", "Medium", "Hard")
        assert q["type"] == "MCQ"
        assert isinstance(q["correct_index"], int) and 0 <= q["correct_index"] < 4

        stem = norm_text(q["content"]["en"]["question"])
        assert stem not in other_stems, f"Global stem collision with another track in {qid}: {stem[:80]}"
        assert stem not in seen_stems, f"Internal NSMO duplicate stem in {qid}: {stem[:80]}"
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
                m_f = NSMO_FORBIDDEN_RE.search(field)
                assert not m_f, f"Forbidden out-of-scope term '{m_f.group(0)}' in {qid} {lang}"
            if c.get("diagram"):
                ET.fromstring(c["diagram"])

        bp_counts[q["nsmo_blueprint"]] += 1
        level_counts[q["level"]] += 1
        diff_counts[q["difficulty"]] += 1
        topic_counts[q["topic"]] += 1

    assert len(bp_counts) == 90, f"Expected 90 distinct NSMO blueprints, got {len(bp_counts)}"
    assert svg_count >= 700, f"Expected >= 700 SVG diagrams across NSMO, got {svg_count}"

    out_path = ROOT / "data" / "nsmo.json"
    out_path.write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"OK: Wrote {len(bank)} verified NSMO questions | {len(bp_counts)} blueprints | "
        f"{svg_count} SVGs ({svg_count * 100 // len(bank)}%) | diffs={dict(diff_counts)} | "
        f"topics={dict(topic_counts)} | {out_path.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()

