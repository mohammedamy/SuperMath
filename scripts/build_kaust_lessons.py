"""Build & strictly validate data/kaust_lessons.json: 18 KAUST (KMC) study lessons covering 100% of blueprints,
100% concept diagram coverage, 185 solved examples, and 108 graduated end-of-lesson printable practice drills."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_kaust_kmc import FORBIDDEN_RE
from kmc_diagrams import svg_number_strip, svg_subdivided_apex_triangle, svg_subdivided_rect_2x2
from ar_svg_localizer import localize_svg_to_ar
import kmc_diagrams_extra as D
from kmc_lesson_helpers import _polish_html
from kmc_lessons_enhancements import LESSON_ENHANCEMENTS
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
    ("KMC-L1-01", 1): (
        D.svg_two_jars("3 : 2", 0.55, "3 : 4", 0.78, "+2 parts"),
        D.svg_two_jars("3 : 2", 0.55, "3 : 4", 0.78, "+2 أجزاء"),
    ),
    ("KMC-L1-02", 0): (
        D.svg_digital_clock("12:21", "12:21 ⇄ 12:21"),
        D.svg_digital_clock("12:21", "دورات م.م.أ وتناظر الساعة"),
    ),
    ("KMC-L1-02", 1): (
        D.svg_venn_2("÷ A", "÷ B", "A", "lcm(A,B)", "B"),
        D.svg_venn_2("÷ A", "÷ B", "A فقط", "lcm(A,B)", "B فقط"),
    ),
    ("KMC-L1-04", 0): D.svg_function_machine("?", "× 3", "+ 5", "29"),
    ("KMC-L1-04", 1): D.svg_number_pyramid("A+2B+C", "A+B", "B+C", "A", "B", "C"),
    ("KMC-L1-04", 2): (
        D.svg_motion_timeline("Fast v₁", "Slow v₂", "Gap G", "v₁", "v₂", meet=False),
        D.svg_motion_timeline("سريع v₁", "بطيء v₂", "الفارق G", "v₁", "v₂", meet=False),
    ),
    ("KMC-L1-06", 0): svg_subdivided_apex_triangle(3, 2),
    ("KMC-L2-01", 0): D.svg_factor_tree("72", "2³ = 8", "9", "3", "3"),
    ("KMC-L2-01", 2): D.svg_venn_3("A", "B", "C", {"a": "A", "b": "B", "c": "C", "ab": "", "bc": "", "ac": "", "abc": "∩"}),
    ("KMC-L2-02", 0): D.svg_function_machine("7¹=7", "×7 → 9", "×7 → 3", "1"),
    ("KMC-L2-02", 1): D.svg_factor_tree("10 = 2×5", "2ᵃ", "5ᵇ", "5", "2"),
    ("KMC-L2-02", 2): (
        D.svg_binary_bulbs((1, 0, 1, 1, 0), lang="en"),
        D.svg_binary_bulbs((1, 0, 1, 1, 0), lang="ar"),
    ),
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

# Custom diagrams for ALL 45 Core Worked Examples across all 18 lessons (77/77 = 100% bespoke worked example SVGs)
EXTRA_EXAMPLE_DIAGRAMS = {
    "L11-E1": (
        D.svg_tape_bar_split([(0.25, "1/4"), (0.50, "2/3 rem"), (0.25, "35")], "N = ?"),
        D.svg_tape_bar_split([(0.25, "1/4"), (0.50, "2/3 الباقي"), (0.25, "35")], "الكل = ؟"),
    ),
    "L11-E2": (
        D.svg_two_jars("3 : 4", 0.55, "1 : 2", 0.78, "+10 blue"),
        D.svg_two_jars("3 : 4", 0.55, "1 : 2", 0.78, "+10 أزرق"),
    ),
    "L11-E4": (
        D.svg_algebra_flow([("Mistake", "N × 0.5 = 18"), ("Number", "N = ?"), ("Correct", "N ÷ 0.5 = ?")], ["÷0.5", "÷0.5"]),
        D.svg_algebra_flow([("الخطأ", "N × 0.5 = 18"), ("العدد", "N = ؟"), ("الصحيح", "N ÷ 0.5 = ؟")], ["÷0.5", "÷0.5"]),
    ),
    "L12-E1": (
        D.svg_venn_2("÷ 4", "÷ 6", "?", "÷ 12", "?", "1..60"),
        D.svg_venn_2("÷ 4", "÷ 6", "؟", "÷ 12", "؟", "1..60"),
    ),
    "L12-E3": (
        D.svg_digit_cards(["?", "?"], "d₁ × d₂ = 72", "d₁ + d₂ = ?"),
        D.svg_digit_cards(["؟", "؟"], "d₁ × d₂ = 72", "d₁ + d₂ = ؟"),
    ),
    "L12-E4": (
        D.svg_cycle_ring(["12 s", "18 s", "30 s"], "8:00:00 → ?", "lcm = ?"),
        D.svg_cycle_ring(["12 ث", "18 ث", "30 ث"], "8:00:00 ← ؟", "م.م.أ = ؟"),
    ),
    "L14-E1": (
        D.svg_score_table(["Person", "Now", "+t yrs"], [["Father", "42", "42 + t"], ["Son", "10", "10 + t"]], "42 + t = 3(10 + t)"),
        D.svg_score_table(["الشخص", "الآن", "+t سنة"], [["الأب", "42", "42 + t"], ["الابن", "10", "10 + t"]], "42 + t = 3(10 + t)"),
    ),
    "L14-E2": (
        D.svg_pigeonhole_bins([("A + B", "23"), ("B + C", "29"), ("A + C", "26")], "B = ?"),
        D.svg_pigeonhole_bins([("A + B", "23"), ("B + C", "29"), ("A + C", "26")], "سلة B = ؟"),
    ),
    "L14-E3": (
        D.svg_number_line_sign_chart([("A", True), ("B", True), ("C", True), ("D", True)], ["", "?", "?", "?", ""], "AC = 45, AD = 72, BD = 53"),
        D.svg_number_line_sign_chart([("A", True), ("B", True), ("C", True), ("D", True)], ["", "؟", "؟", "؟", ""], "AC = 45, AD = 72, BD = 53"),
    ),
    "L14-E4": (
        D.svg_motion_timeline("Yasser", "Salim", "720 m", "200 m/min", "80 m/min", meet=False),
        D.svg_motion_timeline("ياسر", "سالم", "720 م", "200 م/د", "80 م/د", meet=False),
    ),
    "L16-E2": D.svg_grid_dimensions(3, 2, "3", "2", mode="subrect"),
    "L21-E2": (
        D.svg_divisor_rainbow("77 − 5 = 72 (d > 5)", ["1..5", "6", "...", "36", "72"], "d | 72, d > 5"),
        D.svg_divisor_rainbow("77 − 5 = 72 (d > 5)", ["1..5", "6", "...", "36", "72"], "قواسم 72 الأكبر من 5"),
    ),
    "L21-E3": (
        D.svg_algebra_flow([("gcd = 6", "a = 6x, b = 6y"), ("lcm = 180", "x · y = 30"), ("Min", "a + b = ?")], ["→", "min"]),
        D.svg_algebra_flow([("ق.م.أ = 6", "a = 6x, b = 6y"), ("م.م.أ = 180", "x · y = 30"), ("الأصغر", "a + b = ؟")], ["←", "أصغر"]),
    ),
    "L21-E4": D.svg_factor_tree("720", "2⁴ = 16", "45", "3²", "5¹"),
    "L22-E1": (
        D.svg_digit_cards(["9", "9", "...", "9", "5", "2"], "10²⁵ − 48", "Sum = ?"),
        D.svg_digit_cards(["9", "9", "...", "9", "5", "2"], "10²⁵ − 48", "مجموع الأرقام = ؟"),
    ),
    "L22-E2": svg_number_strip(["1..9 (9)", "10..54 (90)", "55 → 5"]),
    "L22-E3": (
        D.svg_cycle_ring(["3", "9", "7", "1"], "3²⁰²⁵ + 7²⁰²⁶", "mod 10"),
        D.svg_cycle_ring(["3", "9", "7", "1"], "3²⁰²⁵ + 7²⁰²⁶", "دورة الآحاد = 4"),
    ),
    "L22-E4": (
        D.svg_factorial_padic_bars("25³ × 16² × 15²", [("2ᵃ", 1.0, "2⁸"), ("5ᵇ", 1.0, "5⁸"), ("10ᵏ", 1.0, "10^?")]),
        D.svg_factorial_padic_bars("25³ × 16² × 15²", [("2ᵃ", 1.0, "2⁸"), ("5ᵇ", 1.0, "5⁸"), ("10ᵏ", 1.0, "10^؟")]),
    ),
    "L23-E1": D.svg_area_identity_square("x", "1/x"),
    "L23-E2": svg_subdivided_rect_2x2("xy", "x", "y", "1"),
    "L23-E3": D.svg_number_line_sign_chart([("3", True), ("√13", True), ("4", True)], ["", "−", "+", ""], "√9 < √13 < √16"),
    "L23-E4": D.svg_gnomon_diff_squares("503", "497", "(503² − 497²) ÷ 60"),
    "L24-E1": (
        D.svg_function_machine("30", "A: 2/min", "B: 3/min", "5/min"),
        D.svg_function_machine("30", "A: 2/د", "B: 3/د", "5/د"),
    ),
    "L24-E2": (
        D.svg_score_table(["Type", "Count", "Pts"], [["Correct", "c = ?", "+4"], ["Wrong", "22 − c", "−1"], ["Blank", "3", "0"]], "Total = 68"),
        D.svg_score_table(["النوع", "العدد", "النقاط"], [["صحيحة", "c = ؟", "+4"], ["خاطئة", "22 − c", "−1"], ["فارغة", "3", "0"]], "المجموع = 68"),
    ),
    "L24-E3": D.svg_telescoping_chain(["a₄ = 19", "+ 7d", "a₁₁ = 54", "+ 4d", "a₁₅ = ?"], "→", slash_middle=False),
    "L24-E4": (
        D.svg_telescoping_chain(["m−3", "...", "m", "...", "m+3 = ?"], "+", "7m = 161", slash_middle=False),
        D.svg_telescoping_chain(["m−3", "...", "m", "...", "m+3 = ؟"], "+", "7m = 161", slash_middle=False),
    ),
    "L26-E3": (
        D.svg_pigeonhole_bins([("Red", "10"), ("Blue", "8"), ("Green", "6"), ("Yellow", "3")], "Guarantee 5 = ?"),
        D.svg_pigeonhole_bins([("أحمر", "10"), ("أزرق", "8"), ("أخضر", "6"), ("أصفر", "3")], "لضمان 5 متماثلة = ؟"),
    ),
    "L31-E1": (
        D.svg_statement_cards([("p + q = 99", "2 + q = 99"), ("p × q", "2 × q = ?")], "p, q primes"),
        D.svg_statement_cards([("p + q = 99", "2 + q = 99"), ("p × q", "2 × q = ؟")], "p, q أوليان"),
    ),
    "L31-E2": D.svg_factor_tree("10!", "2⁸·3⁴·5²", "7¹", "k = 7", "□²"),
    "L31-E3": D.svg_gnomon_diff_squares("p", "q", "p² − q² = (p−q)(p+q) = 21"),
    "L31-E4": (
        D.svg_algebra_flow([("gcd(n,60)=12", "n = 12k"), ("Coprime", "gcd(k,5) = 1"), ("n > 50", "n = ?")], ["→", "min"]),
        D.svg_algebra_flow([("gcd(n,60)=12", "n = 12k"), ("أوليان نسبيًا", "gcd(k,5) = 1"), ("n > 50", "n = ؟")], ["←", "أصغر"]),
    ),
    "L31-E5": D.svg_telescoping_chain(["1²", "2²", "...", "9²", "10²"], "+", "mod 9 = ?", slash_middle=False),
    "L32-E1": D.svg_telescoping_chain(["1..3 → 1", "4..8 → 2", "9..15 → 3", "16..24 → 4"], "+", "⌊√k⌋", slash_middle=False),
    "L32-E2": D.svg_telescoping_chain(["1 (×1)", "2 (×2)", "3 (×3)", "...", "k (×k)"], "·", "k(k+1)/2 ≥ 100", slash_middle=False),
    "L33-E1": D.svg_parabola_roots("r₁", "r₂", "Δ₁ = 13"),
    "L33-E2": (
        D.svg_algebra_flow([("Given", "a+b = 5, ab = 3"), ("Identity", "(a+b)³ − 3ab(a+b)"), ("Target", "a³ + b³ = ?")], ["→", "="]),
        D.svg_algebra_flow([("المعطى", "a+b = 5, ab = 3"), ("المتطابقة", "(a+b)³ − 3ab(a+b)"), ("المطلوب", "a³ + b³ = ؟")], ["←", "="]),
    ),
    "L33-E3": svg_subdivided_rect_2x2("xy", "x", "y", "1"),
    "L33-E4": D.svg_algebra_flow([("2⁻¹ + 3⁻¹", "5 / 6"), ("(5/6)⁻¹", "6 / 5"), ("× 10", "10(6/5 + 1) = ?")], ["⁻¹", "+1"]),
    "L34-E1": D.svg_telescoping_chain(["√2 − √1", "√3 − √2", "...", "√100 − √99"], "+", "√100 − √1 = ?"),
    "L34-E2": D.svg_symmetry_curve("odd_shift", "f(−x) + f(x) = 14", "(−4, 19)", "(4, ?)"),
    "L34-E3": (
        D.svg_algebra_flow([("√(2x+7) = x−4", "x − 4 ≥ 0"), ("Square", "(x−4)² = 2x+7"), ("Check", "x ≥ 4 → ?")], ["≥0", "( )²"]),
        D.svg_algebra_flow([("√(2x+7) = x−4", "x − 4 ≥ 0"), ("تربيع", "(x−4)² = 2x+7"), ("تحقق", "x ≥ 4 ← ؟")], ["≥0", "( )²"]),
    ),
    "L34-E4": svg_number_strip(["−3", "−2", "−1", "0", "1", "2"]),
    "L35-E5": (
        D.svg_algebra_flow([("s", "A₁ = 6s²"), ("3s", "A₂ = 6(3s)²"), ("Δ%", "+? %")], ["×3", "×9"]),
        D.svg_algebra_flow([("s", "A₁ = 6s²"), ("3s", "A₂ = 6(3s)²"), ("الزيادة", "+؟ %")], ["×3", "×9"]),
    ),
    "L36-E3": D.svg_graph_chord_polygon(6, "C(6,3) − C(4,1) = ?", bad_edge=True),
    "L36-E4": (
        D.svg_pigeonhole_bins([("Green", "4"), ("Gold", "2")], "P(same) = ?"),
        D.svg_pigeonhole_bins([("أخضر", "4"), ("ذهبي", "2")], "احتمال التماثل = ؟"),
    ),
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
    mocks_path = ROOT / "data/kaust_mocks.json"
    mock_used_ids = set()
    if mocks_path.exists():
        mocks_doc = json.loads(mocks_path.read_text())
        mock_used_ids = {qid for m in mocks_doc.get("mocks", []) for qid in m.get("question_ids", [])}

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

        # Apply LESSON_ENHANCEMENTS (5th goal, 4th concept card, 4 traps, cheat-sheet, 6 bespoke examples)
        enh = LESSON_ENHANCEMENTS.get(lid)
        assert enh is not None, f"Missing LESSON_ENHANCEMENTS for {lid}"
        for g_en, g_ar in enh.get("extra_goals", []):
            les["en"]["goals"].append(_polish_html(g_en))
            les["ar"]["goals"].append(_polish_html(g_ar))
        if enh.get("extra_concept"):
            les["en"]["concepts"].append(enh["extra_concept"]["en"])
            les["ar"]["concepts"].append(enh["extra_concept"]["ar"])
        for t_en, t_ar in enh.get("extra_traps", []):
            les["en"]["traps"].append(_polish_html(t_en))
            les["ar"]["traps"].append(_polish_html(t_ar))
        if enh.get("cheat_sheet"):
            les["en"]["cheat_sheet"] = [c["en"] for c in enh["cheat_sheet"]]
            les["ar"]["cheat_sheet"] = [c["ar"] for c in enh["cheat_sheet"]]
        for ex in enh.get("extra_examples", []):
            les["en"]["examples"].append({"id": ex["id"], "correct_index": ex["correct_index"], **ex["en"]})
            les["ar"]["examples"].append({"id": ex["id"], "correct_index": ex["correct_index"], **ex["ar"]})

        # Attach extra concept SVGs so every single concept card in all 18 lessons has a diagram (72/72 = 100%)
        for c_idx in range(len(les["en"]["concepts"])):
            if not les["en"]["concepts"][c_idx].get("diagram"):
                svg_entry = EXTRA_CONCEPT_DIAGRAMS.get((lid, c_idx))
                if svg_entry:
                    svg_en, svg_ar = svg_entry if isinstance(svg_entry, tuple) else (svg_entry, svg_entry)
                    ET.fromstring(svg_en)
                    ET.fromstring(svg_ar)
                    les["en"]["concepts"][c_idx]["diagram"] = svg_en
                    les["ar"]["concepts"][c_idx]["diagram"] = svg_ar
            if les["en"]["concepts"][c_idx].get("diagram"):
                total_concept_svgs += 1

        # Attach extra worked-example SVGs so every single bespoke worked example has a diagram (108/108 = 100%)
        for e_idx, ex_en in enumerate(les["en"]["examples"]):
            if not ex_en.get("diagram") and ex_en["id"] in EXTRA_EXAMPLE_DIAGRAMS:
                svg_entry = EXTRA_EXAMPLE_DIAGRAMS[ex_en["id"]]
                svg_en, svg_ar = svg_entry if isinstance(svg_entry, tuple) else (svg_entry, svg_entry)
                ET.fromstring(svg_en)
                ET.fromstring(svg_ar)
                les["en"]["examples"][e_idx]["diagram"] = svg_en
                les["ar"]["examples"][e_idx]["diagram"] = svg_ar
            les["ar"]["examples"][e_idx]["diagram"] = localize_svg_to_ar(les["ar"]["examples"][e_idx]["diagram"])
            assert les["en"]["examples"][e_idx].get("diagram") and les["ar"]["examples"][e_idx].get("diagram"), (
                f"Missing diagram on bespoke example {ex_en['id']}"
            )
        assert len(les["en"]["concepts"]) == 4 and len(les["ar"]["concepts"]) == 4, f"Expected 4 concepts in {lid}"
        assert len(les["en"]["examples"]) == 6 and len(les["ar"]["examples"]) == 6, f"Expected 6 bespoke examples in {lid}"
        assert len(les["en"]["traps"]) == 4 and len(les["ar"]["traps"]) == 4, f"Expected 4 traps in {lid}"
        assert len(les["en"]["cheat_sheet"]) == 4 and len(les["ar"]["cheat_sheet"]) == 4, f"Expected 4 cheat_sheet items in {lid}"

        for bp in bps:
            assert bp in by_bp, f"unknown blueprint {bp}"
            assert bp_level[bp] == les["level"], f"{bp} level mismatch"
            seen.append(bp)

        # 1. Pick 8 distinct-blueprint curated worked bank examples (5 from orig + 3 from extra, zero mock overlap)
        target_k = min(8, len(bps))
        picked_bps = []
        if extra_bps and all(bp in by_bp for bp in extra_bps):
            orig_k = min(5, len(orig_bps))
            indices = [round(i * (len(orig_bps) - 1) / max(1, orig_k - 1)) for i in range(orig_k)]
            for idx in indices:
                if orig_bps[idx] not in picked_bps:
                    picked_bps.append(orig_bps[idx])
            for bp in orig_bps:
                if len(picked_bps) >= orig_k:
                    break
                if bp not in picked_bps:
                    picked_bps.append(bp)
            for bp in extra_bps:
                if len(picked_bps) < target_k and bp not in picked_bps:
                    picked_bps.append(bp)
        for bp in bps:
            if len(picked_bps) >= target_k:
                break
            if bp not in picked_bps:
                picked_bps.append(bp)

        diff_pref = ["Easy", "Medium", "Medium", "Hard", "Easy", "Medium", "Hard", "Medium"]
        bank_ids = []
        for rank_i, bp in enumerate(picked_bps[:target_k]):
            non_mock_bp = [item for item in by_bp[bp] if item["id"] not in mock_used_ids]
            cand = sorted(
                non_mock_bp,
                key=lambda item: (
                    0 if ("diagram" in item["content"]["en"]) else 1,
                    0 if item["difficulty"] == diff_pref[rank_i % len(diff_pref)] else 1,
                    item["id"],
                ),
            )
            bank_ids.append(cand[0]["id"])
        assert len(set(bank_ids)) == 8, f"Expected 8 distinct bank examples in {lid}"
        les["bank_example_ids"] = bank_ids

        # 2. Pick 9 strictly disjoint graduated Practice Drills (3 Easy, 3 Medium, 3 Hard) maximizing blueprint diversity!
        used_ids = set(bank_ids) | mock_used_ids
        used_drill_bps = Counter()
        pool = [q for bp in bps for q in by_bp[bp] if q["id"] not in used_ids]
        picked_drills = []
        for target_diff in ("Hard", "Hard", "Hard", "Medium", "Medium", "Medium", "Easy", "Easy", "Easy"):
            cands = sorted(
                [q for q in pool if q["id"] not in used_ids],
                key=lambda q: (
                    used_drill_bps[q["kmc_blueprint"]],
                    0 if q["difficulty"] == target_diff else 1,
                    0 if q["kmc_blueprint"] not in picked_bps else 1,
                    0 if ("diagram" in q["content"]["en"]) else 1,
                    q["id"],
                ),
            )
            chosen = cands[0]
            picked_drills.append(chosen)
            used_ids.add(chosen["id"])
            used_drill_bps[chosen["kmc_blueprint"]] += 1
        diff_rank = {"Easy": 0, "Medium": 1, "Hard": 2}
        picked_drills.sort(key=lambda q: (diff_rank.get(q["difficulty"], 1), q["id"]))
        drill_ids = [q["id"] for q in picked_drills]
        assert len(set(drill_ids)) == 9 and len(used_drill_bps) >= min(8, len(bps)), f"Drill blueprint diversity low in {lid}"
        assert not (set(drill_ids) & set(bank_ids)), f"Overlap in {lid}"
        assert not (set(drill_ids) & mock_used_ids), f"Mock overlap in {lid}"
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
    assert total_concept_svgs == 72, f"Expected 72/72 concept SVGs, got {total_concept_svgs}"
    assert total_bespoke == 108, f"Expected 108 bespoke worked examples, got {total_bespoke}"
    assert total_bank == 144, f"Expected 144 bank worked examples, got {total_bank}"
    assert total_drills == 162, f"Expected 162 practice drills, got {total_drills}"

    out = ROOT / "data/kaust_lessons.json"
    out.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, separators=(",", ":")))
    print(
        f"OK: {len(lessons)} lessons | {len(seen)} blueprints (100%) | {total_concept_svgs}/72 concept SVGs | "
        f"{total_bespoke} bespoke + {total_bank} bank = {total_bespoke + total_bank} solved examples | "
        f"{total_drills} practice drills | {out.stat().st_size // 1024} KB"
    )


if __name__ == "__main__":
    main()
