"""Master builder & strict scope/quality verifier for data/kaust.json (KAUST Mathematics Competition — KMC)."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import kmc_t1_algebra
import kmc_t1_comb_data
import kmc_t1_geometry
import kmc_t1_numbers
import kmc_t2_algebra
import kmc_t2_comb_data
import kmc_t2_geometry
import kmc_t2_number_theory
import kmc_t3_algebra
import kmc_t3_comb_prob
import kmc_t3_geometry
import kmc_t3_number_theory
from kmc_common import norm_text

FORBIDDEN_PATTERNS = [
    r"\bderivative\b",
    r"\bintegral\b",
    r"\bdifferentiable\b",
    r"\beigenvalue\b",
    r"\beigenvector\b",
    r"\bdeterminant\b",
    r"\bmatrix\b",
    r"\bmatrices\b",
    r"\bcomplex\s+number",
    r"\bimaginary\b",
    r"\blogarithm",
    r"\bmarkov\b",
    r"\bstochastic\b",
    r"\btaylor\b",
    r"\bfourier\b",
    r"\blaplace\b",
    r"\\int\b",
    r"\\lim\b",
    r"\\log\b",
    r"\\ln\b",
    r"\\sin\b",
    r"\\cos\b",
    r"\\tan\b",
    r"\\cot\b",
    r"\\sec\b",
    r"\\csc\b",
    r"\\partial\b",
    r"\\nabla\b",
]
FORBIDDEN_RE = re.compile("|".join(FORBIDDEN_PATTERNS), re.IGNORECASE)


def build() -> None:
    t1_items = (
        kmc_t1_numbers.generate_t1_numbers()
        + kmc_t1_algebra.generate_t1_algebra()
        + kmc_t1_geometry.generate_t1_geometry()
        + kmc_t1_comb_data.generate_t1_comb_data()
    )
    t2_items = (
        kmc_t2_number_theory.generate()
        + kmc_t2_algebra.generate_t2_algebra()
        + kmc_t2_geometry.generate()
        + kmc_t2_comb_data.generate()
    )
    t3_items = (
        kmc_t3_number_theory.generate()
        + kmc_t3_algebra.generate()
        + kmc_t3_geometry.generate()
        + kmc_t3_comb_prob.generate()
    )

    assert len(t1_items) == 450, f"Track 1 count = {len(t1_items)}"
    assert len(t2_items) == 450, f"Track 2 count = {len(t2_items)}"
    assert len(t3_items) == 450, f"Track 3 count = {len(t3_items)}"

    for i, q in enumerate(t1_items, 1):
        assert q["level"] == "Track 1: Grades 6-7"
        q["id"] = f"KAUST-G67-{i:03d}"
    for i, q in enumerate(t2_items, 1):
        assert q["level"] == "Track 2: Grades 8-9"
        q["id"] = f"KAUST-G89-{i:03d}"
    for i, q in enumerate(t3_items, 1):
        assert q["level"] == "Track 3: Grades 10-11"
        q["id"] = f"KAUST-G1011-{i:03d}"

    all_kaust = t1_items + t2_items + t3_items
    assert len(all_kaust) == 1350

    # Load all other 5 banks to guarantee zero cross-bank collisions
    other_en = {}
    other_ar = {}
    for other_name in ("kangaroo", "nafes", "nsmo", "jee", "olympiad"):
        rows = json.loads((ROOT / "data" / f"{other_name}.json").read_text(encoding="utf-8"))
        for r in rows:
            other_en[norm_text(r["content"]["en"]["question"])] = f"{other_name}:{r['id']}"
            other_ar[norm_text(r["content"]["ar"]["question"])] = f"{other_name}:{r['id']}"

    seen_en = {}
    seen_ar = {}
    svg_count = 0

    for q in all_kaust:
        qid = q["id"]
        en = q["content"]["en"]
        ar = q["content"]["ar"]

        # 1. Check 5 distinct options & structured explanations
        assert len(en["options"]) == 5 and len(ar["options"]) == 5, qid
        assert len({norm_text(o) for o in en["options"]}) == 5, f"Duplicate EN opts in {qid}"
        assert len({norm_text(o) for o in ar["options"]}) == 5, f"Duplicate AR opts in {qid}"
        assert 0 <= q["correct_index"] < 5, qid
        assert "Key Idea:" in en["explanation"] and "Step 1:" in en["explanation"] and "Quick Check:" in en["explanation"], qid
        assert "الفكرة الأساسية:" in ar["explanation"] and "الخطوة 1:" in ar["explanation"] and "التحقق من الحل:" in ar["explanation"], qid

        # 2. Check strict KMC syllabus scope (zero forbidden advanced topics)
        blob = " ".join([
            en["question"], " ".join(en["options"]), en["hint"], en["explanation"],
            ar["question"], " ".join(ar["options"]), ar["hint"], ar["explanation"],
        ])
        m_forb = FORBIDDEN_RE.search(blob)
        assert not m_forb, f"Forbidden out-of-scope term {m_forb.group(0)!r} in {qid}"
        assert "\\\\(" not in blob and ":\\(" not in blob, f"Malformed MathJax delimiter in {qid}"

        # 3. Check SVG XML validity when diagram is present
        if "diagram" in en or "diagram" in ar:
            assert "diagram" in en and "diagram" in ar, f"Asymmetric diagram presence in {qid}"
            ET.fromstring(en["diagram"])
            ET.fromstring(ar["diagram"])
            svg_count += 1

        # 4. Check stem uniqueness (internal + cross-bank)
        # Note: if a diagram encodes problem numbers (e.g. number triangle / bar chart / cryptarithm),
        # include normalized text inside SVG <text> nodes so distinct visual problems are distinguished,
        # while STILL asserting pure stem uniqueness or stem+diagram uniqueness!
        nen = norm_text(en["question"])
        nar = norm_text(ar["question"])
        assert nen not in seen_en, f"Duplicate EN stem between {seen_en[nen]} and {qid}: {en['question'][:90]}"
        assert nar not in seen_ar, f"Duplicate AR stem between {seen_ar[nar]} and {qid}: {ar['question'][:90]}"
        assert nen not in other_en, f"Cross-bank EN collision between {other_en[nen]} and {qid}"
        assert nar not in other_ar, f"Cross-bank AR collision between {other_ar[nar]} and {qid}"
        seen_en[nen] = qid
        seen_ar[nar] = qid

    out_path = ROOT / "data" / "kaust.json"
    out_path.write_text(json.dumps(all_kaust, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"SUCCESS: Wrote {len(all_kaust)} verified KMC questions to {out_path}")
    print("By Track :", dict(Counter(q["level"] for q in all_kaust)))
    print("By Topic :", dict(Counter(q["topic"] for q in all_kaust)))
    print("By Diff  :", dict(Counter(q["difficulty"] for q in all_kaust)))
    print(f"SVG Diagrams: {svg_count} / {len(all_kaust)} questions ({svg_count * 100 / len(all_kaust):.1f}%)")


if __name__ == "__main__":
    build()
