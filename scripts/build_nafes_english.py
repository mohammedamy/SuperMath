"""Compile ETEC Nafes English (Grades 3, 6 & 9, 1,080 verified MCQs) into data/nafes_english.json."""
import json
import sys
from collections import Counter
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from audit_banks import norm
from nafes_english_g3_bank import build_g3_english_bank
from nafes_english_g6_bank import build_g6_english_bank
from nafes_english_g9_bank import build_g9_english_bank


def build_nafes_english_bank() -> list[dict]:
    g3 = build_g3_english_bank()
    g6 = build_g6_english_bank()
    g9 = build_g9_english_bank()
    assert len(g3) == 360, f"Expected 360 G3 English Qs, got {len(g3)}"
    assert len(g6) == 360, f"Expected 360 G6 English Qs, got {len(g6)}"
    assert len(g9) == 360, f"Expected 360 G9 English Qs, got {len(g9)}"

    all_qs = g3 + g6 + g9
    assert len(all_qs) == 1080

    ids = [q["id"] for q in all_qs]
    assert len(set(ids)) == 1080, "Duplicate question IDs found in Nafes English bank"

    stems = [norm(q["content"]["en"]["question"]) for q in all_qs]
    assert len(set(stems)) == 1080, f"Expected 1080 unique EN stems, got {len(set(stems))}"

    for q in all_qs:
        assert q["track"] == "nafes_english"
        assert q["level"] in ("English · Grade 3", "English · Grade 6", "English · Grade 9")
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
    all_qs = build_nafes_english_bank()
    out_path = ROOT / "data" / "nafes_english.json"
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
