"""Build data/kaust_lessons.json: 18 KAUST (KMC) study lessons with 100% blueprint coverage."""
import json
import re
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
        by_bp[q["kmc_blueprint"]].append(q["id"])
        bp_level[q["kmc_blueprint"]] = q["level"]

    lessons = build_t1_lessons() + build_t2_lessons() + build_t3_lessons()
    assert len(lessons) == 18, len(lessons)
    seen = []
    for les in lessons:
        for bp in les["blueprints"]:
            assert bp in by_bp, f"unknown blueprint {bp}"
            assert bp_level[bp] == les["level"], f"{bp} level mismatch"
            seen.append(bp)
        # curated bank examples: first question of 4 spread-out blueprints
        bps = les["blueprints"]
        step = max(1, len(bps) // 4)
        picks = [bps[i] for i in range(0, len(bps), step)][:4]
        les["bank_example_ids"] = [sorted(by_bp[b])[len(by_bp[b]) // 2] for b in picks]
        assert len(set(les["bank_example_ids"])) == 4
        for s in strings(les):
            assert "**" not in s, (les["id"], s[:80])
            assert not FORBIDDEN_RE.search(s), (les["id"], FORBIDDEN_RE.search(s).group(0))
            if s.lstrip().startswith("<svg"):
                ET.fromstring(s)
    assert len(seen) == len(set(seen)), "blueprint used twice"
    assert set(seen) == set(by_bp), f"missing: {set(by_bp) - set(seen)}"
    out = ROOT / "data/kaust_lessons.json"
    out.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, separators=(",", ":")))
    print(f"OK: {len(lessons)} lessons, {len(seen)} blueprints, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
