"""Build & strictly validate data/nsmo_lessons.json: 18 NSMO / Mawhiba (Grades 7–10) study lessons covering
100% of all 90 blueprints, 54/54 concept SVGs, 180 solved examples, and 108 disjoint printable practice drills."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from nsmo_common import NSMO_FORBIDDEN_RE
from nsmo_lessons_p1 import build_p1_lessons
from nsmo_lessons_p2 import build_p2_lessons
from nsmo_lessons_p3 import build_p3_lessons
from study_academy_enhancements import apply_lesson_enhancements


def iter_strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from iter_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from iter_strings(v)


def main() -> None:
    qs = json.loads((ROOT / "data" / "nsmo.json").read_text(encoding="utf-8"))
    by_bp = defaultdict(list)
    bp_level = {}
    for q in qs:
        by_bp[q["nsmo_blueprint"]].append(q)
        bp_level[q["nsmo_blueprint"]] = q["level"]

    lessons = build_p1_lessons() + build_p2_lessons() + build_p3_lessons()
    assert len(lessons) == 18, f"Expected 18 NSMO lessons, got {len(lessons)}"
    apply_lesson_enhancements(lessons)

    mock_path = ROOT / "data" / "nsmo_mocks.json"
    mock_used_ids: set[str] = set()
    if mock_path.exists():
        for m in json.loads(mock_path.read_text(encoding="utf-8")).get("mocks", []):
            mock_used_ids.update(m.get("question_ids", []))

    seen_bps: list[str] = []
    total_bespoke = 0
    total_bank = 0
    total_drills = 0
    total_concept_svgs = 0

    for les in lessons:
        lid = les["id"]
        bps = list(les["blueprints"])
        assert len(bps) == 5, f"Expected 5 blueprints in {lid}, got {len(bps)}"
        for bp in bps:
            assert bp in by_bp, f"Unknown NSMO blueprint {bp} in {lid}"
            assert bp_level[bp] == les["level"], f"Level mismatch on {bp} in {lid}"
            seen_bps.append(bp)

        assert len(les["en"]["concepts"]) == 3 and len(les["ar"]["concepts"]) == 3, lid
        for c_idx in range(3):
            diag_en = les["en"]["concepts"][c_idx].get("diagram", "")
            diag_ar = les["ar"]["concepts"][c_idx].get("diagram", "")
            assert diag_en and "<svg" in diag_en, f"Missing concept SVG in {lid}#{c_idx}"
            ET.fromstring(diag_en)
            ET.fromstring(diag_ar)
            total_concept_svgs += 1

        # 1. Pick 6 curated bank worked examples covering all 5 blueprints + 1 extra (preferring SVG diagrams)
        slot_bps = bps + [bps[0]]
        diff_pref = ["Easy", "Medium", "Medium", "Hard", "Easy", "Hard"]
        bank_ids: list[str] = []
        used_ids: set[str] = set(mock_used_ids)
        for rank_i, bp in enumerate(slot_bps):
            cand = sorted(
                [q for q in by_bp[bp] if q["id"] not in used_ids],
                key=lambda item: (
                    0 if item["content"]["en"].get("diagram") else 1,
                    0 if item["difficulty"] == diff_pref[rank_i] else 1,
                    item["id"],
                ),
            )
            chosen = cand[0]
            bank_ids.append(chosen["id"])
            used_ids.add(chosen["id"])
        assert len(set(bank_ids)) == 6
        les["bank_example_ids"] = bank_ids

        # 2. Pick 6 strictly disjoint graduated Practice Drills (2 Easy, 2 Medium, 2 Hard) covering all 5 blueprints!
        used_drill_bps: set[str] = set()
        pool = [q for bp in bps for q in by_bp[bp] if q["id"] not in used_ids]
        picked_drills = []
        for target_diff in ("Hard", "Hard", "Medium", "Medium", "Easy", "Easy"):
            cands = sorted(
                [q for q in pool if q["id"] not in used_ids],
                key=lambda q: (
                    0 if q["nsmo_blueprint"] not in used_drill_bps else 1,
                    0 if q["difficulty"] == target_diff else 1,
                    0 if q["content"]["en"].get("diagram") else 1,
                    q["id"],
                ),
            )
            chosen = cands[0]
            picked_drills.append(chosen)
            used_ids.add(chosen["id"])
            used_drill_bps.add(chosen["nsmo_blueprint"])

        diff_rank = {"Easy": 0, "Medium": 1, "Hard": 2}
        picked_drills.sort(key=lambda q: (diff_rank.get(q["difficulty"], 1), q["id"]))
        drill_ids = [q["id"] for q in picked_drills]
        assert len(set(drill_ids)) == 6 and len(used_drill_bps) == 5, f"Drill coverage issue in {lid}"
        assert not (set(drill_ids) & set(bank_ids)), f"Overlap in {lid}"
        les["drill_ids"] = drill_ids

        total_bespoke += len(les["en"]["examples"])
        total_bank += len(bank_ids)
        total_drills += len(drill_ids)

        for ex in les["en"]["examples"] + les["ar"]["examples"]:
            assert len(ex["options"]) == 4, f"Expected 4 options in worked example {ex['id']}"

        for s in iter_strings(les):
            assert "**" not in s, (lid, s[:80])
            assert "\\\\(" not in s and "\\\\[" not in s, (lid, s[:80])
            assert s.count("\\(") == s.count("\\)"), (lid, "unbalanced inline math", s[:80])
            assert s.count("\\[") == s.count("\\]"), (lid, "unbalanced display math", s[:80])
            m_forb = NSMO_FORBIDDEN_RE.search(s)
            assert not m_forb, (lid, m_forb.group(0), s[:100])
            if s.lstrip().startswith("<svg"):
                ET.fromstring(s)

    assert len(seen_bps) == len(set(seen_bps)) == 90, f"Blueprint mapping count: {len(seen_bps)}"
    assert set(seen_bps) == set(by_bp), f"Unmapped blueprints: {set(by_bp) - set(seen_bps)}"
    assert total_concept_svgs == 54, f"Expected 54/54 concept SVGs, got {total_concept_svgs}"

    out = ROOT / "data" / "nsmo_lessons.json"
    out.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"OK: {len(lessons)} NSMO lessons | {len(seen_bps)} blueprints (100%) | {total_concept_svgs}/54 concept SVGs | "
        f"{total_bespoke} bespoke + {total_bank} bank = {total_bespoke + total_bank} solved examples | "
        f"{total_drills} practice drills | {out.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()

