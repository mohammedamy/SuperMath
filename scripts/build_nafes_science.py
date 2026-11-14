"""Compile ETEC Nafes Science (Grades 6 & 9, 720 verified MCQs) into data/nafes_science.json."""
import json
import sys
from collections import Counter
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from audit_banks import norm
from nafes_science_g6_bank import build_g6_science_bank
from nafes_science_g9_bank import build_g9_science_bank


def build_nafes_science_bank() -> list[dict]:
    g6 = build_g6_science_bank()
    g9 = build_g9_science_bank()
    assert len(g6) == 360, f"Expected 360 G6 Science Qs, got {len(g6)}"
    assert len(g9) == 360, f"Expected 360 G9 Science Qs, got {len(g9)}"

    all_qs = g6 + g9
    assert len(all_qs) == 720

    ids = [q["id"] for q in all_qs]
    assert len(set(ids)) == 720, "Duplicate question IDs found in Nafes Science bank"

    stems = [norm(q["content"]["en"]["question"]) for q in all_qs]
    assert len(set(stems)) == 720, f"Expected 720 unique EN stems, got {len(set(stems))}"

    for q in all_qs:
        assert q["track"] == "nafes_science"
        assert q["level"] in ("Science · Grade 6", "Science · Grade 9")
        assert 0 <= q["correct_index"] < 4
        for lang in ("en", "ar"):
            blk = q["content"][lang]
            assert len(blk["options"]) == 4
            assert len({norm(o) for o in blk["options"]}) == 4, f"Duplicate {lang} options in {q['id']}"
            blob = " ".join([blk["question"], *blk["options"], blk.get("hint", ""), blk.get("explanation", "")])
            assert "**" not in blob, f"Raw ** in {q['id']}"
            assert "\\\\(" not in blob, f"Double-escaped \\\\( in {q['id']}"

    return all_qs


def main() -> None:
    all_qs = build_nafes_science_bank()
    out_path = ROOT / "data" / "nafes_science.json"
    out_path.write_text(json.dumps(all_qs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lv = Counter(q["level"] for q in all_qs)
    tp = Counter(q["topic"] for q in all_qs)
    df = Counter(q["difficulty"] for q in all_qs)
    print(f"Wrote {len(all_qs)} questions to {out_path}")
    print("  Levels:", dict(lv))
    print("  Topics:", dict(tp))
    print("  Difficulty:", dict(df))


if __name__ == "__main__":
    main()
