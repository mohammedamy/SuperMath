#!/usr/bin/env python3
"""
Inject 200 high-quality questions into each level of KAUST track (600 questions total).
- Phase 1: Foundation Research (250 existing -> 450 total, adding KAUST-P1-251 to KAUST-P1-450)
- Phase 2: Advanced Analysis (250 existing -> 450 total, adding KAUST-P2-251 to KAUST-P2-450)
- Phase 3: Elite Research (250 existing -> 450 total, adding KAUST-P3-251 to KAUST-P3-450)

Total in data/kaust.json: 750 -> 1350 questions.
Total across all tracks: 4250 -> 4850 questions.
"""

import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from build_kaust_p1 import generate_phase1
from build_kaust_p2 import build_phase_2
from build_kaust_p3 import build_phase_3

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    kaust_file = os.path.join(root, 'data', 'kaust.json')

    print(f"Loading existing KAUST bank from {kaust_file}...")
    with open(kaust_file, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    print(f"Existing KAUST question count: {len(existing)}")

    # Build new batches
    print("Generating Phase 1 (200 questions)...")
    p1 = generate_phase1()
    assert len(p1) == 200, f"Expected 200 Phase 1 questions, got {len(p1)}"

    print("Generating Phase 2 (200 questions)...")
    p2 = build_phase_2()
    assert len(p2) == 200, f"Expected 200 Phase 2 questions, got {len(p2)}"

    print("Generating Phase 3 (200 questions)...")
    p3 = build_phase_3()
    assert len(p3) == 200, f"Expected 200 Phase 3 questions, got {len(p3)}"

    all_new = p1 + p2 + p3
    assert len(all_new) == 600, f"Expected 600 new questions, got {len(all_new)}"

    # Validate all new questions
    seen_ids = set(q['id'] for q in existing)
    for q in all_new:
        qid = q['id']
        assert qid not in seen_ids, f"Collision on ID {qid}"
        seen_ids.add(qid)
        assert q['track'] == 'kaust'
        assert q['type'] == 'MCQ'
        assert 0 <= q['correct_index'] <= 3
        for lang in ['en', 'ar']:
            c = q['content'][lang]
            assert len(c['options']) == 4, f"Option count != 4 in {qid} ({lang})"
            assert len(set(c['options'])) == 4, f"Duplicate options in {qid} ({lang})"
            assert len(c['question'].strip()) > 10
            assert len(c['explanation'].strip()) > 10
            assert len(c['hint'].strip()) > 5

    # Combine existing + new
    combined = existing + all_new
    print(f"Combined KAUST total questions: {len(combined)}")
    assert len(combined) == 1350, f"Expected 1350 questions, got {len(combined)}"

    # Check breakdown per level
    levels = {}
    for q in combined:
        lvl = q.get('level')
        levels[lvl] = levels.get(lvl, 0) + 1

    print("\nKAUST Level Breakdown:")
    for lvl, count in sorted(levels.items()):
        print(f"  - {lvl}: {count} questions")
        assert count == 450, f"Expected 450 questions for level '{lvl}', got {count}"

    # Write back to data/kaust.json
    print(f"\nWriting updated bank to {kaust_file}...")
    with open(kaust_file, 'w', encoding='utf-8') as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
    print("SUCCESS: data/kaust.json updated successfully!")

if __name__ == '__main__':
    main()
