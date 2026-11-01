"""Build & strictly validate data/kaust_lessons.json: 18 KAUST (KMC) study lessons covering 100% of blueprints."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_kaust_kmc import FORBIDDEN_RE
from kmc_lessons_t1 import build_t1_lessons
from kmc_lessons_t2 import build_t2_lessons
from kmc_lessons_t3 import build_t3_lessons


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


def main():
    qs = json.loads((ROOT / "data/kaust.json").read_text())
    by_bp = defaultdict(list)
    bp_level = {}
    for q in qs:
        by_bp[q["kmc_blueprint"]].append(q)
        bp_level[q["kmc_blueprint"]] = q["level"]

    lessons = build_t1_lessons() + build_t2_lessons() + build_t3_lessons()
    assert len(lessons) == 18, len(lessons)

    seen = []
    total_bespoke = 0
    total_bank = 0
    for les in lessons:
        bps = les["blueprints"]
        for bp in bps:
            assert bp in by_bp, f"unknown blueprint {bp}"
            assert bp_level[bp] == les["level"], f"{bp} level mismatch"
            seen.append(bp)

        # Pick 5 distinct-blueprint bank examples, prioritizing diagrammed items & varied difficulties
        target_k = min(5, len(bps))
        # Sort blueprints so diagrammed blueprints get represented, while preserving spread across the lesson
        indices = [round(i * (len(bps) - 1) / (target_k - 1)) for i in range(target_k)] if target_k > 1 else [0]
        picked_bps = []
        for idx in indices:
            if bps[idx] not in picked_bps:
                picked_bps.append(bps[idx])
        for bp in bps:
            if len(picked_bps) >= target_k:
                break
            if bp not in picked_bps:
                picked_bps.append(bp)

        diff_pref = ["Easy", "Medium", "Medium", "Hard", "Medium"]
        bank_ids = []
        for rank_i, bp in enumerate(picked_bps):
            cand = sorted(by_bp[bp], key=lambda item: (
                0 if ("diagram" in item["content"]["en"]) else 1,
                0 if item["difficulty"] == diff_pref[rank_i % len(diff_pref)] else 1,
                item["id"],
            ))
            bank_ids.append(cand[0]["id"])
        assert len(set(bank_ids)) == target_k
        les["bank_example_ids"] = bank_ids
        total_bespoke += len(les["en"]["examples"])
        total_bank += len(bank_ids)

        for s in strings(les):
            assert "**" not in s, (les["id"], s[:80])
            assert "\\\\(" not in s and "\\\\[" not in s, (les["id"], s[:80])
            assert s.count("\\(") == s.count("\\)"), (les["id"], "unbalanced inline math", s[:80])
            assert s.count("\\[") == s.count("\\]"), (les["id"], "unbalanced display math", s[:80])
            m_forb = FORBIDDEN_RE.search(s)
            assert not m_forb, (les["id"], m_forb.group(0), s[:100])
            if s.lstrip().startswith("<svg"):
                ET.fromstring(s)

    assert len(seen) == len(set(seen)), "blueprint used twice"
    assert set(seen) == set(by_bp), f"missing: {set(by_bp) - set(seen)}"

    out = ROOT / "data/kaust_lessons.json"
    out.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, separators=(",", ":")))
    print(
        f"OK: {len(lessons)} lessons | {len(seen)} blueprints (100%) | "
        f"{total_bespoke} bespoke + {total_bank} curated bank = {total_bespoke + total_bank} solved examples | "
        f"{out.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()
