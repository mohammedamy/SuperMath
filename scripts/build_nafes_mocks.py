"""Build & strictly validate data/nafes_mocks.json: 12 Official ETEC-Style Nafes KSA (Grades 3, 6, 9)
Full Mock Exam Papers (4 per Grade: Grade 3 = 20 Qs / 45 min, Grade 6 = 25 Qs / 60 min, Grade 9 = 30 Qs / 75 min,
4-option A–D MCQs, 1 pt per question, 0 wrong penalty, 300 unique zero-overlap questions)."""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GRADE_SPECS = [
    {
        "level": "Grade 3",
        "code": "G3",
        "grades_en": "Grade 3 (Primary National Assessment)",
        "grades_ar": "الصف الثالث الابتدائي (اختبار نافس الوطني)",
        "q_count": 20,
        "tier_counts": {"Easy": 7, "Medium": 8, "Hard": 5},
        "duration_minutes": 45,
        "slot_patterns": [
            ["Easy", "Easy", "Medium", "Hard"],   # 4 Qs
            ["Easy", "Medium", "Medium", "Hard"], # 4 Qs
            ["Easy", "Easy", "Medium"],           # 3 Qs
            ["Easy", "Medium", "Hard"],           # 3 Qs
            ["Easy", "Medium", "Hard"],           # 3 Qs
            ["Medium", "Medium", "Hard"],         # 3 Qs -> Total: 7 Easy, 8 Medium, 5 Hard = 20 Qs
        ],
        "papers": [
            (
                "Official Nafes Mock Paper 1 — ETEC Grade 3 Full Benchmark",
                "اختبار نافس التجريبي الرسمي 1 — محاكاة شاملة للصف الثالث الابتدائي",
                "Balanced 20-question, 45-minute ETEC simulation across 4-digit place value, fractions, clocks, perimeters, and pictographs.",
                "محاكاة متوازنة من 20 سؤالاً (45 دقيقة) تشمل القيمة المنزلية، الكسور، الساعات، المحيط، والتمثيل بالرموز.",
            ),
            (
                "Official Nafes Mock Paper 2 — Numbers, Patterns & Everyday Measurement",
                "اختبار نافس التجريبي الرسمي 2 — الأعداد والأنماط والقياس اليومي (الصف 3)",
                "Highlights regrouping operations, multiplication/division arrays, input-output rules, Saudi Riyals, and metric units.",
                "يركّز على الجمع والطرح بإعادة التجميع، الضرب والقسمة، جداول المدخلات، النقود السعودية، ووحدات القياس.",
            ),
            (
                "Official Nafes Mock Paper 3 — Visual Fractions, Shapes & Data Charts",
                "اختبار نافس التجريبي الرسمي 3 — الكسور البصرية والأشكال والبيانات (الصف 3)",
                "Focuses on fraction strips, 2D polygons & 3D solids, lines of symmetry, bar charts, and spinner likelihood.",
                "يركّز على نماذج الكسور، المضلعات والمجسمات، محاور التماثل، التمثيل بالأعمدة، واحتمالات القرص الدوّار.",
            ),
            (
                "Official Nafes Mock Paper 4 — School Readiness Dress Rehearsal",
                "اختبار نافس التجريبي الرسمي 4 — البروفة الختامية لاختبار نافس (الصف 3)",
                "Complete 45-minute ETEC Grade 3 national assessment rehearsal calibrated to Knowing, Applying, and Reasoning.",
                "بروفة وطنية شاملة مدتها 45 دقيقة تحاكي مستويات المعرفة والتطبيق والاستدلال في اختبار نافس للصف الثالث.",
            ),
        ],
    },
    {
        "level": "Grade 6",
        "code": "G6",
        "grades_en": "Grade 6 (Upper Primary National Assessment)",
        "grades_ar": "الصف السادس الابتدائي (اختبار نافس الوطني)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "duration_minutes": 60,
        "slot_patterns": [
            ["Easy", "Easy", "Medium", "Medium", "Hard"], # 5 Qs
            ["Easy", "Easy", "Medium", "Hard"],           # 4 Qs
            ["Easy", "Easy", "Medium", "Hard"],           # 4 Qs
            ["Easy", "Medium", "Medium", "Hard"],         # 4 Qs
            ["Easy", "Medium", "Medium", "Hard"],         # 4 Qs
            ["Easy", "Medium", "Hard", "Hard"],           # 4 Qs -> Total: 9 Easy, 9 Medium, 7 Hard = 25 Qs
        ],
        "papers": [
            (
                "Official Nafes Mock Paper 1 — ETEC Grade 6 Full Benchmark",
                "اختبار نافس التجريبي الرسمي 1 — محاكاة شاملة للصف السادس الابتدائي",
                "Balanced 25-question, 60-minute ETEC simulation covering fractions, decimals, ratios, equations, angles, and averages.",
                "محاكاة متوازنة من 25 سؤالاً (60 دقيقة) تغطي الكسور، الكسور العشرية، النسب، المعادلات، الزوايا، والمتوسطات.",
            ),
            (
                "Official Nafes Mock Paper 2 — Ratios, Percentages & Algebraic Rules",
                "اختبار نافس التجريبي الرسمي 2 — النسب المئوية والتناسب والعبارات الجبرية (الصف 6)",
                "Highlights GCD/LCM cycles, unit rates, percentage discounts, order of operations, and function tables.",
                "يركّز على القاسم والمضاعف المشترك، معدل الوحدة، النسب المئوية، ترتيب العمليات، وجداول الدوال.",
            ),
            (
                "Official Nafes Mock Paper 3 — Area, Prism Volume, Angles & Charts",
                "اختبار نافس التجريبي الرسمي 3 — المساحة والحجم والزوايا والقطاعات الدائرية (الصف 6)",
                "Tests triangle/parallelogram area, rectangular prism volume, polygon angles, coordinates, and pie charts.",
                "يختبر مساحات المثلث ومتوازي الأضلاع، حجم المنشور، زوايا الأشكال، المستوى الإحداثي، والقطاعات الدائرية.",
            ),
            (
                "Official Nafes Mock Paper 4 — National Mastery Dress Rehearsal",
                "اختبار نافس التجريبي الرسمي 4 — البروفة الختامية لاختبار نافس (الصف 6)",
                "Complete 60-minute ETEC Grade 6 national assessment dress rehearsal across all four content domains.",
                "بروفة وطنية ختامية (25 سؤالاً في 60 دقيقة) تحاكي اختبار نافس الرسمي للصف السادس الابتدائي.",
            ),
        ],
    },
    {
        "level": "Grade 9",
        "code": "G9",
        "grades_en": "Grade 9 (Intermediate National Assessment)",
        "grades_ar": "الصف الثالث المتوسط (اختبار نافس الوطني)",
        "q_count": 30,
        "tier_counts": {"Easy": 10, "Medium": 11, "Hard": 9},
        "duration_minutes": 75,
        "slot_patterns": [
            ["Easy", "Easy", "Medium", "Medium", "Hard"], # 5 Qs
            ["Easy", "Easy", "Medium", "Medium", "Hard"], # 5 Qs
            ["Easy", "Easy", "Medium", "Medium", "Hard"], # 5 Qs
            ["Easy", "Easy", "Medium", "Hard", "Hard"],   # 5 Qs
            ["Easy", "Medium", "Medium", "Hard", "Hard"], # 5 Qs
            ["Easy", "Medium", "Medium", "Hard", "Hard"], # 5 Qs -> Total: 10 Easy, 11 Medium, 9 Hard = 30 Qs
        ],
        "papers": [
            (
                "Official Nafes Mock Paper 1 — ETEC Grade 9 Full Benchmark",
                "اختبار نافس التجريبي الرسمي 1 — محاكاة شاملة للصف الثالث المتوسط",
                "Full 30-question, 75-minute ETEC paper spanning surds, exponents, linear systems, quadratics, Pythagoras, and box plots.",
                "اختبار وطني شامل من 30 سؤالاً (75 دقيقة) يغطي الجذور، الأسس، الأنظمة الخطية، فيثاغورس، والصندوق وطرفيه.",
            ),
            (
                "Official Nafes Mock Paper 2 — Linear Functions, Factoring & Similarity",
                "اختبار نافس التجريبي الرسمي 2 — الدوال الخطية والتحليل والتشابه (الصف 9)",
                "Features compound percent change, slope-intercept lines, polynomial factoring, similar triangles, and histograms.",
                "يتناول التغير المئوي المركب، ميل المستقيم، تحليل كثيرات الحدود، تشابه المثلثات، والمدرجات التكرارية.",
            ),
            (
                "Official Nafes Mock Paper 3 — Exponents, Quadratics, 3D Solids & Probability",
                "اختبار نافس التجريبي الرسمي 3 — الأسس والتربيعيات والمجسمات والاحتمال المركب (الصف 9)",
                "Tests scientific notation, quadratic roots, distance/midpoint, cylinder/cone volumes, and compound probability.",
                "يختبر الصيغة العلمية، المعادلات التربيعية، المسافة ونقطة المنتصف، حجوم الأسطوانة والمخروط، والاحتمالات المركبة.",
            ),
            (
                "Official Nafes Mock Paper 4 — National Excellence Dress Rehearsal",
                "اختبار نافس التجريبي الرسمي 4 — البروفة الختامية لاختبار نافس (الصف 9)",
                "High-rigor 30-question, 75-minute ETEC Grade 9 dress rehearsal calibrated for national excellence.",
                "البروفة الختامية الشاملة (30 سؤالاً في 75 دقيقة) لاختبار نافس الوطني للصف الثالث المتوسط.",
            ),
        ],
    },
]


def max_consecutive_run(seq: list[int]) -> int:
    best = cur = 0
    prev = None
    for x in seq:
        if x == prev:
            cur += 1
        else:
            cur = 1
            prev = x
        best = max(best, cur)
    return best


def order_with_no_long_runs(items: list[dict], rng: random.Random) -> list[dict]:
    diff_rank = {"Easy": 0, "Medium": 1, "Hard": 2}
    for _ in range(300):
        grouped = defaultdict(list)
        for q in items:
            grouped[q["difficulty"]].append(q)
        ordered = []
        for diff in ("Easy", "Medium", "Hard"):
            arr = list(grouped[diff])
            rng.shuffle(arr)
            ordered.extend(arr)
        if max_consecutive_run([q["correct_index"] for q in ordered]) <= 2:
            return ordered
    # Greedy repair within same difficulty tier if needed
    ordered = sorted(items, key=lambda q: diff_rank[q["difficulty"]])
    for i in range(2, len(ordered)):
        if ordered[i]["correct_index"] == ordered[i - 1]["correct_index"] == ordered[i - 2]["correct_index"]:
            for j in range(i + 1, len(ordered)):
                if ordered[j]["difficulty"] == ordered[i]["difficulty"] and ordered[j]["correct_index"] != ordered[i]["correct_index"]:
                    ordered[i], ordered[j] = ordered[j], ordered[i]
                    break
    return ordered


def select_four_papers_for_grade(spec: dict, grade_lessons: list, fresh_by_les_diff: dict) -> list[dict]:
    les_ids = [l["id"] for l in grade_lessons]
    base_patterns = spec["slot_patterns"]
    rng = random.Random(20261104 + hash(spec["code"]) % 997)
    used_qids: set[str] = set()
    global_bp_usage: Counter[str] = Counter()
    papers_out = []

    for p_idx in range(4):
        rot = p_idx % len(les_ids)
        rotated_patterns = base_patterns[rot:] + base_patterns[:rot]
        selected: list[dict] = []
        key_counts: Counter[int] = Counter()

        for les_id, slots in zip(les_ids, rotated_patterns):
            used_bps_in_paper: set[str] = set()
            for diff in slots:
                cands = [q for q in fresh_by_les_diff[(les_id, diff)] if q["id"] not in used_qids]
                assert cands, f"Ran out of fresh {diff} Qs in {les_id} on paper {p_idx + 1}"
                cands.sort(
                    key=lambda q: (
                        1 if q["nafes_blueprint"] in used_bps_in_paper else 0,
                        global_bp_usage[q["nafes_blueprint"]],
                        key_counts[q["correct_index"]],
                        0 if q["content"]["en"].get("diagram") else 1,
                        q["id"],
                    )
                )
                chosen = cands[0]
                selected.append(chosen)
                used_qids.add(chosen["id"])
                used_bps_in_paper.add(chosen["nafes_blueprint"])
                global_bp_usage[chosen["nafes_blueprint"]] += 1
                key_counts[chosen["correct_index"]] += 1

        ordered = order_with_no_long_runs(selected, rng)
        assert len(ordered) == spec["q_count"]
        assert Counter(q["difficulty"] for q in ordered) == Counter(spec["tier_counts"])
        assert max_consecutive_run([q["correct_index"] for q in ordered]) <= 2, f"Run > 2 in {spec['code']}#{p_idx + 1}"

        t_en, t_ar, sub_en, sub_ar = spec["papers"][p_idx]
        papers_out.append(
            {
                "id": f"NAFS-MOCK-{spec['code']}-0{p_idx + 1}",
                "track": "nafes",
                "level": spec["level"],
                "paper_num": p_idx + 1,
                "duration_minutes": spec["duration_minutes"],
                "question_count": spec["q_count"],
                "option_count": 4,
                "points_correct": 1,
                "points_wrong": 0,
                "points_blank": 0,
                "max_points": spec["q_count"],
                "grades_en": spec["grades_en"],
                "grades_ar": spec["grades_ar"],
                "en": {"title": t_en, "subtitle": sub_en},
                "ar": {"title": t_ar, "subtitle": sub_ar},
                "question_ids": [q["id"] for q in ordered],
                "svg_count": sum(1 for q in ordered if q["content"]["en"].get("diagram")),
            }
        )
    return papers_out


def main() -> None:
    bank = json.loads((ROOT / "data" / "nafes.json").read_text(encoding="utf-8"))
    lessons = json.loads((ROOT / "data" / "nafes_lessons.json").read_text(encoding="utf-8"))["lessons"]

    lesson_used: set[str] = set()
    bp_to_lesson: dict[str, str] = {}
    for les in lessons:
        lesson_used.update(les["bank_example_ids"])
        lesson_used.update(les["drill_ids"])
        for bp in les["blueprints"]:
            bp_to_lesson[bp] = les["id"]

    fresh_by_les_diff = defaultdict(list)
    for q in bank:
        if q["id"] in lesson_used:
            continue
        lid = bp_to_lesson[q["nafes_blueprint"]]
        fresh_by_les_diff[(lid, q["difficulty"])].append(q)

    all_papers = []
    for spec in GRADE_SPECS:
        g_lessons = [l for l in lessons if l["level"] == spec["level"]]
        assert len(g_lessons) == 6
        all_papers.extend(select_four_papers_for_grade(spec, g_lessons, fresh_by_les_diff))

    assert len(all_papers) == 12
    all_qids = [qid for p in all_papers for qid in p["question_ids"]]
    assert len(all_qids) == len(set(all_qids)) == 300
    assert not (set(all_qids) & lesson_used)

    total_svgs = sum(p["svg_count"] for p in all_papers)
    doc = {
        "competition": "ETEC Nafes KSA National Assessment (Grades 3, 6 & 9)",
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": all_papers,
    }
    out = ROOT / "data" / "nafes_mocks.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"SUCCESS: Wrote {len(all_papers)} official Nafes mock papers "
        f"({len(all_qids)} unique zero-overlap questions, {total_svgs} SVG diagrams) to {out}"
    )


if __name__ == "__main__":
    main()

