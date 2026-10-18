#!/usr/bin/env python3
"""
Build and verify all 200 Phase 2 questions (KAUST-P2-251 to KAUST-P2-450).
"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kaust_p2_part_a import get_p2_part_a
from kaust_p2_part_b import get_p2_part_b
from kaust_p2_part_c import get_p2_part_c
from kaust_p2_part_d import get_p2_part_d

def build_phase_2():
    part_a = get_p2_part_a()
    part_b = get_p2_part_b()
    part_c = get_p2_part_c()
    part_d = get_p2_part_d()

    all_p2 = part_a + part_b + part_c + part_d
    print(f"Loaded: Part A={len(part_a)}, Part B={len(part_b)}, Part C={len(part_c)}, Part D={len(part_d)}")
    print(f"Total Phase 2 questions: {len(all_p2)}")

    assert len(all_p2) == 200, f"Expected 200 questions, got {len(all_p2)}"

    seen_ids = set()
    for i, q in enumerate(all_p2, start=251):
        expected_id = f"KAUST-P2-{i}"
        assert q["id"] == expected_id, f"ID mismatch: expected {expected_id}, got {q['id']}"
        assert q["id"] not in seen_ids, f"Duplicate ID: {q['id']}"
        seen_ids.add(q["id"])

        assert q["track"] == "kaust"
        assert q["level"] == "Phase 2: Advanced Analysis"
        assert q["type"] == "MCQ"
        assert q["difficulty"] in ["Easy", "Medium", "Hard"]

        content = q["content"]
        assert "en" in content and "ar" in content
        for lang in ["en", "ar"]:
            c = content[lang]
            assert "question" in c and len(c["question"].strip()) > 10
            assert "options" in c and len(c["options"]) == 4
            assert "explanation" in c and len(c["explanation"].strip()) > 10
            assert "hint" in c and len(c["hint"].strip()) > 5
            # Options must be non-empty strings
            for opt in c["options"]:
                assert isinstance(opt, str) and len(opt.strip()) > 0
            # No duplicate options
            assert len(set(c["options"])) == 4, f"Duplicate options in {q['id']} ({lang})"

        assert isinstance(q["correct_index"], int)
        assert 0 <= q["correct_index"] <= 3

    print("SUCCESS: Generated and validated all 200 Phase 2 questions (KAUST-P2-251 to KAUST-P2-450).")
    return all_p2

if __name__ == "__main__":
    build_phase_2()
