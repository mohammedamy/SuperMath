"""Build & strictly validate data/kaust_lessons.json: 18 KAUST (KMC) study lessons covering 100% of blueprints,
100% concept diagram coverage, 185 solved examples, and 108 graduated end-of-lesson printable practice drills."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_kaust_kmc import FORBIDDEN_RE
from kmc_diagrams import svg_number_strip, svg_subdivided_apex_triangle, svg_subdivided_rect_2x2
import kmc_diagrams_extra as D
from kmc_lessons_t1 import build_t1_lessons
from kmc_lessons_t2 import build_t2_lessons
from kmc_lessons_t3 import build_t3_lessons

# 54 expanded KMC blueprints (3 per lesson across all 18 lessons)
EXTRA_LESSON_BLUEPRINTS = {
    "KMC-L1-01": ["g67-visual-fraction-grid", "g67-bundle-promo-discount", "g67-two-jar-transfer"],
    "KMC-L1-02": ["g67-digital-clock-palindromes", "g67-venn-two-clubs", "g67-missing-digit-div-346"],
    "KMC-L1-03": ["g67-dot-array-growth", "g67-function-machine-2step", "g67-additive-number-pyramid"],
    "KMC-L1-04": ["g67-fencepost-tree-spacing", "g67-opposite-meet-trains", "g67-heads-legs-two-values"],
    "KMC-L1-05": ["g67-folded-paper-angle", "g67-clock-hands-angle", "g67-glued-cube-stack-area"],
    "KMC-L1-06": ["g67-magic-square-3x3", "g67-shortest-street-grid", "g67-pie-chart-sectors"],
    "KMC-L2-01": ["kmc_g89_factor_tree_square_cube", "kmc_g89_venn_three_sets", "kmc_g89_simultaneous_remainders"],
    "KMC-L2-02": ["kmc_g89_binary_switch_panel", "kmc_g89_palindrome_divisibility", "kmc_g89_digital_root_invariant"],
    "KMC-L2-03": ["kmc_g89_geometric_square_identity", "kmc_g89_telescoping_fraction_prod", "kmc_g89_linear_floor_equation"],
    "KMC-L2-04": ["kmc_g89_harmonic_round_trip_speed", "kmc_g89_inlet_outlet_pipe_tank", "kmc_g89_league_table_points"],
    "KMC-L2-05": ["kmc_g89_thales_semicircle_angles", "kmc_g89_isosceles_trapezoid_pythag", "kmc_g89_sector_arc_annulus"],
    "KMC-L2-06": ["kmc_g89_blocked_grid_paths", "kmc_g89_counterfeit_coin_weighings", "kmc_g89_two_box_transfer_prob"],
    "KMC-L3-01": ["kmc_g1011_legendre_prime_factorial", "kmc_g1011_divisors_of_square_cube", "kmc_g1011_frobenius_coin_stamp"],
    "KMC-L3-02": ["kmc_g1011_hermite_paired_floor_sum", "kmc_g1011_base_b_representation", "kmc_g1011_constrained_sum_prod_extremum"],
    "KMC-L3-03": ["kmc_g1011_parabola_chord_vertex", "kmc_g1011_exp_quadratic_substitution", "kmc_g1011_reciprocal_cube_power"],
    "KMC-L3-04": ["kmc_g1011_functional_involution_system", "kmc_g1011_manhattan_diamond_area", "kmc_g1011_nested_radical_denest"],
    "KMC-L3-05": ["kmc_g1011_power_of_point_secant_tangent", "kmc_g1011_angle_bisector_ratio", "kmc_g1011_right_triangle_inradius"],
    "KMC-L3-06": ["kmc_g1011_stars_and_bars_solutions", "kmc_g1011_circular_seating_derangement", "kmc_g1011_geometric_interval_prob"],
}

# Custom concept diagrams so 100% of all 54 concepts across all 18 lessons have crisp past-paper visuals
EXTRA_CONCEPT_DIAGRAMS = {
    ("KMC-L1-01", 0): D.svg_fraction_grid(5, 3, 5, 4),
    ("KMC-L1-01", 1): D.svg_two_jars("3 : 2", 0.55, "3 : 4", 0.78, "+2 parts"),
    ("KMC-L1-02", 0): D.svg_digital_clock("12:21", "LCM cycles & clock palindromes"),
    ("KMC-L1-02", 1): D.svg_venn_2("÷ A", "÷ B", "A only", "lcm(A,B)", "B only"),
    ("KMC-L1-04", 0): D.svg_function_machine("?", "× 3", "+ 5", "29"),
    ("KMC-L1-04", 1): D.svg_number_pyramid("A+2B+C", "A+B", "B+C", "A", "B", "C"),
    ("KMC-L1-04", 2): D.svg_motion_timeline("Fast v₁", "Slow v₂", "Gap G", "v₁", "v₂", meet=False),
    ("KMC-L1-06", 0): svg_subdivided_apex_triangle(3, 2),
    ("KMC-L2-01", 0): D.svg_factor_tree("72", "2³ = 8", "9", "3", "3"),
    ("KMC-L2-01", 2): D.svg_venn_3("A", "B", "C", {"a": "A", "b": "B", "c": "C", "ab": "", "bc": "", "ac": "", "abc": "∩"}),
    ("KMC-L2-02", 0): D.svg_function_machine("7¹=7", "×7 → 9", "×7 → 3", "1"),
    ("KMC-L2-02", 1): D.svg_factor_tree("10 = 2×5", "2ᵃ", "5ᵇ", "5", "2"),
    ("KMC-L2-02", 2): D.svg_binary_bulbs((1, 0, 1, 1, 0)),
    ("KMC-L2-03", 0): D.svg_area_identity_square("a", "b"),
    ("KMC-L2-03", 2): svg_number_strip(["1", "+ 2", "+ 4", "+ 8", "= 2⁴ − 1"]),
    ("KMC-L2-04", 0): svg_number_strip(["m − 2d", "m − d", "m", "m + d", "m + 2d"]),
    ("KMC-L2-04", 1): D.svg_pipe_tank("+1 / t₁", "−1 / t₂"),
    ("KMC-L2-04", 2): D.svg_motion_timeline("A", "B", "d", "v₁ →", "← v₂", meet=True),
    ("KMC-L2-06", 1): D.svg_street_grid(4, 3, (2, 1)),
    ("KMC-L3-01", 0): D.svg_factor_tree("n!", "2²ᵃ", "p²ᵇ", "pᵇ", "pᵇ"),
    ("KMC-L3-01", 1): D.svg_area_identity_square("p", "q"),
    ("KMC-L3-02", 0): svg_number_strip(["1..3 → 1", "4..8 → 2", "9..15 → 3"]),
    ("KMC-L3-02", 1): D.svg_dot_pattern("L"),
    ("KMC-L3-03", 0): D.svg_parabola_roots("r₁", "r₂", "V"),
    ("KMC-L3-03", 1): D.svg_area_identity_square("a", "b"),
    ("KMC-L3-03", 2): D.svg_function_machine("a⁻ⁿ", "1 / aⁿ", "(p/q)⁻¹", "q / p"),
    ("KMC-L3-04", 0): svg_number_strip(["√2 − √1", "+ √3 − √2", "+ ···", "= √n − 1"]),
    ("KMC-L3-04", 1): D.svg_coord_diamond("R"),
}

# Custom diagrams for Core Worked Examples in lessons that previously had 0 worked-example SVGs
EXTRA_EXAMPLE_DIAGRAMS = {
    "L14-E4": D.svg_motion_timeline("Yasser", "Salim", "720 m", "200 m/m", "80 m/m", meet=False),
    "L22-E2": svg_number_strip(["1..9 (9d)", "10..54 (90d)", "55 → 5"]),
    "L23-E2": svg_subdivided_rect_2x2("xy", "x", "y", "1"),
    "L24-E1": D.svg_function_machine("30 units", "A: 2/min", "B: 3/min", "5/min"),
    "L31-E2": D.svg_factor_tree("10!", "2⁸·3⁴·5²", "7¹", "k = 7", "□²"),
    "L33-E1": D.svg_parabola_roots("r₁", "r₂", "Δ₁ = 13"),
    "L34-E4": svg_number_strip(["−3", "−2", "−1", "0", "1", "2"]),
}


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
    total_drills = 0
    total_concept_svgs = 0

    for les in lessons:
        lid = les["id"]
        orig_bps = list(les["blueprints"])
        extra_bps = EXTRA_LESSON_BLUEPRINTS.get(lid, [])
        # Append extra blueprints that exist in data/kaust.json
        bps = orig_bps + [bp for bp in extra_bps if bp in by_bp and bp not in orig_bps]
        les["blueprints"] = bps

        # Attach extra concept SVGs so every single concept card in all 18 lessons has a diagram
        for c_idx in range(len(les["en"]["concepts"])):
            if not les["en"]["concepts"][c_idx].get("diagram"):
                svg = EXTRA_CONCEPT_DIAGRAMS.get((lid, c_idx))
                if svg:
                    ET.fromstring(svg)
                    les["en"]["concepts"][c_idx]["diagram"] = svg
                    les["ar"]["concepts"][c_idx]["diagram"] = svg
            if les["en"]["concepts"][c_idx].get("diagram"):
                total_concept_svgs += 1

        # Attach extra worked-example SVGs so every lesson also has illustrated core worked examples
        for e_idx, ex_en in enumerate(les["en"]["examples"]):
            if not ex_en.get("diagram") and ex_en["id"] in EXTRA_EXAMPLE_DIAGRAMS:
                svg = EXTRA_EXAMPLE_DIAGRAMS[ex_en["id"]]
                ET.fromstring(svg)
                les["en"]["examples"][e_idx]["diagram"] = svg
                les["ar"]["examples"][e_idx]["diagram"] = svg

        for bp in bps:
            assert bp in by_bp, f"unknown blueprint {bp}"
            assert bp_level[bp] == les["level"], f"{bp} level mismatch"
            seen.append(bp)

        # 1. Pick 6 distinct-blueprint curated worked bank examples (4 from orig + 2 from extra when present)
        target_k = min(6, len(bps))
        picked_bps = []
        if extra_bps and all(bp in by_bp for bp in extra_bps):
            orig_k = 4
            indices = [round(i * (len(orig_bps) - 1) / (orig_k - 1)) for i in range(orig_k)]
            for idx in indices:
                if orig_bps[idx] not in picked_bps:
                    picked_bps.append(orig_bps[idx])
            for bp in orig_bps:
                if len(picked_bps) >= orig_k:
                    break
                if bp not in picked_bps:
                    picked_bps.append(bp)
            picked_bps.extend(extra_bps[:2])
        else:
            indices = [round(i * (len(bps) - 1) / (target_k - 1)) for i in range(target_k)]
            for idx in indices:
                if bps[idx] not in picked_bps:
                    picked_bps.append(bps[idx])
            for bp in bps:
                if len(picked_bps) >= target_k:
                    break
                if bp not in picked_bps:
                    picked_bps.append(bp)

        diff_pref = ["Easy", "Medium", "Medium", "Hard", "Easy", "Medium"]
        bank_ids = []
        for rank_i, bp in enumerate(picked_bps[:target_k]):
            cand = sorted(
                by_bp[bp],
                key=lambda item: (
                    0 if ("diagram" in item["content"]["en"]) else 1,
                    0 if item["difficulty"] == diff_pref[rank_i % len(diff_pref)] else 1,
                    item["id"],
                ),
            )
            bank_ids.append(cand[0]["id"])
        assert len(set(bank_ids)) == target_k
        les["bank_example_ids"] = bank_ids

        # 2. Pick 6 strictly disjoint graduated Practice Drills (2 Easy, 2 Medium, 2 Hard) across 6 distinct blueprints!
        # Assign Hard slots first (most constrained), then sort Easy -> Medium -> Hard for student progression.
        used_ids = set(bank_ids)
        used_drill_bps = set()
        pool = [q for bp in bps for q in by_bp[bp] if q["id"] not in used_ids]
        picked_drills = []
        for target_diff in ("Hard", "Hard", "Medium", "Medium", "Easy", "Easy"):
            cands = sorted(
                [q for q in pool if q["id"] not in used_ids],
                key=lambda q: (
                    0 if q["kmc_blueprint"] not in used_drill_bps else 1,
                    0 if q["difficulty"] == target_diff else 1,
                    0 if ("diagram" in q["content"]["en"]) else 1,
                    0 if q["kmc_blueprint"] not in picked_bps else 1,
                    q["id"],
                ),
            )
            chosen = cands[0]
            picked_drills.append(chosen)
            used_ids.add(chosen["id"])
            used_drill_bps.add(chosen["kmc_blueprint"])
        diff_rank = {"Easy": 0, "Medium": 1, "Hard": 2}
        picked_drills.sort(key=lambda q: (diff_rank.get(q["difficulty"], 1), q["id"]))
        drill_ids = [q["id"] for q in picked_drills]
        assert len(set(drill_ids)) == 6 and len(used_drill_bps) == 6, f"Non-distinct drill blueprints in {lid}"
        assert not (set(drill_ids) & set(bank_ids)), f"Overlap in {lid}"
        les["drill_ids"] = drill_ids

        total_bespoke += len(les["en"]["examples"])
        total_bank += len(bank_ids)
        total_drills += len(drill_ids)

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
    assert total_concept_svgs == 54, f"Expected 54/54 concept SVGs, got {total_concept_svgs}"

    out = ROOT / "data/kaust_lessons.json"
    out.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, separators=(",", ":")))
    print(
        f"OK: {len(lessons)} lessons | {len(seen)} blueprints (100%) | {total_concept_svgs}/54 concept SVGs | "
        f"{total_bespoke} bespoke + {total_bank} bank = {total_bespoke + total_bank} solved examples | "
        f"{total_drills} practice drills | {out.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()
