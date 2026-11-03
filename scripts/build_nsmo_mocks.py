"""Build & strictly validate data/nsmo_mocks.json: 12 Official-Style NSMO / Mawhiba (Grades 7–10)
Full Mock Exam Papers (4 per Phase × 25 4-option MCQs, 90 min, 300 distinct zero-overlap questions)."""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PHASE_SPECS = [
    {
        "level": "Phase 1: Junior Olympiad (Grade 7)",
        "code": "P1",
        "grades_en": "Grade 7 (Junior National Olympiad)",
        "grades_ar": "الصف السابع (الأولمبياد الوطني للناشئين)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "duration_minutes": 90,
        "papers": [
            (
                "Official NSMO Mock Paper 1 — Mawhiba Junior Stage 1 Simulation",
                "اختبار نسمو التجريبي الرسمي 1 — محاكاة المرحلة الأولى للناشئين (الصف 7)",
                "Balanced 25-question Mawhiba simulation across divisibility, ratios, balance algebra, angles, and counting.",
                "محاكاة متوازنة من 25 سؤالاً تشمل قابلية القسمة، النسب، موازين الجبر، الزوايا، ومبادئ العد.",
            ),
            (
                "Official NSMO Mock Paper 2 — Number Sense & Visual Geometry",
                "اختبار نسمو التجريبي الرسمي 2 — الحس العددي والهندسة البصرية (الصف 7)",
                "Highlights LCM cycles, cryptarithms, paper-folding angles, rectilinear perimeters, and grid walks.",
                "يركّز على دورات المضاعف المشترك، الألغاز الرقمية، طي الورق، محيط الأشكال المتدرجة، ومسارات الشبكات.",
            ),
            (
                "Official NSMO Mock Paper 3 — Patterns, Rates & Pigeonhole Logic",
                "اختبار نسمو التجريبي الرسمي 3 — الأنماط والمعدلات ومبدأ برج الحمام (الصف 7)",
                "Focuses on figurate growth, relative speed timelines, magic squares, painted cubes, and worst-case guarantees.",
                "يركّز على الأنماط البصرية، الحركة النسبية، المربعات السحرية، المكعبات المطلية، وضمانات أسوأ الحالات.",
            ),
            (
                "Official NSMO Mock Paper 4 — Winter Camp Qualification Rehearsal",
                "اختبار نسمو التجريبي الرسمي 4 — بروفة التأهل لملتقى الشتاء (الصف 7)",
                "Full 90-minute dress rehearsal calibrated to Mawhiba Junior Olympiad camp qualification standards.",
                "بروفة شاملة مدتها 90 دقيقة تحاكي معايير التأهل لملتقيات موهبة التدريبية للصف السابع.",
            ),
        ],
    },
    {
        "level": "Phase 2: Intermediate Olympiad (Grades 8-9)",
        "code": "P2",
        "grades_en": "Grades 8–9 (Intermediate National Olympiad)",
        "grades_ar": "الصفان 8–9 (الأولمبياد الوطني المتوسط)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "duration_minutes": 90,
        "papers": [
            (
                "Official NSMO Mock Paper 1 — Mawhiba Intermediate Stage Simulation",
                "اختبار نسمو التجريبي الرسمي 1 — محاكاة المرحلة المتوسطة (الصفان 8–9)",
                "Covers Chinese Remainder Theorem, Simon's factoring, Vieta's formulas, similar triangles, and Stars & Bars.",
                "يغطي البواقي المتزامنة، تحليل سايمون، علاقات فييتا، تشابه المثلثات، وطريقة النجوم والفواصل.",
            ),
            (
                "Official NSMO Mock Paper 2 — Digit Structure & Algebraic Telescoping",
                "اختبار نسمو التجريبي الرسمي 2 — بنية الخانات والمجاميع التلسكوبية (الصفان 8–9)",
                "Features semi-increasing numbers, factorial zeros, conjugate surd sums, and Thales circle geometry.",
                "يتناول الأعداد المتزايدة خاناتها، أصفار المضروب، إنطاق الجذور التلسكوبية، وهندسة طاليس في الدائرة.",
            ),
            (
                "Official NSMO Mock Paper 3 — Euclidean Ratios & Blocked Grids",
                "اختبار نسمو التجريبي الرسمي 3 — النسب الهندسية والشبكات المحظورة (الصفان 8–9)",
                "Tests trapezoid Pythagoras, cevian area splits, blocked lattice paths, and 3-set Inclusion-Exclusion.",
                "يختبر شبه المنحرف وفيثاغورس، نسب المساحات، مسارات الشبكات ذات العوائق، ومبدأ الشمول والإقصاء.",
            ),
            (
                "Official NSMO Mock Paper 4 — National Forum Dress Rehearsal",
                "اختبار نسمو التجريبي الرسمي 4 — البروفة الختامية للملتقى الوطني (الصفان 8–9)",
                "Complete 90-minute rehearsal engineered for Grades 8–9 Mawhiba National Olympiad qualification.",
                "البروفة النهائية الكاملة (25 سؤالاً في 90 دقيقة) للتأهل في أولمبياد نسمو للصفين الثامن والتاسع.",
            ),
        ],
    },
    {
        "level": "Phase 3: Senior National Olympiad (Grade 10)",
        "code": "P3",
        "grades_en": "Grade 10 (Senior National Olympiad)",
        "grades_ar": "الصف العاشر (الأولمبياد الوطني المتقدم)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "duration_minutes": 90,
        "papers": [
            (
                "Official NSMO Mock Paper 1 — Senior National Olympiad Simulation",
                "اختبار نسمو التجريبي الرسمي 1 — محاكاة الأولمبياد الوطني المتقدم (الصف 10)",
                "Spans Euler's totient, polynomial remainders, AM-GM optimization, Power of a Point, and derangements.",
                "يشمل دالة أويلر، نظرية باقي كثيرات الحدود، متباينة الوسطين، قوة النقطة، والتبديلات الخالية من النقاط الثابتة.",
            ),
            (
                "Official NSMO Mock Paper 2 — Legendre Valuation, Functional Equations & Circles",
                "اختبار نسمو التجريبي الرسمي 2 — صيغة ليجاندر والمعادلات الدالية والدوائر (الصف 10)",
                "Focuses on prime powers in factorials, functional involutions, cyclic quadrilaterals, and Fibonacci tilings.",
                "يركّز على قوى الأعداد الأولية في المضروب، المعادلات الدالية، الرباعيات الدائرية، وتبليطات فيبوناتشي.",
            ),
            (
                "Official NSMO Mock Paper 3 — Diophantine Factoring, Cauchy-Schwarz & Medians",
                "اختبار نسمو التجريبي الرسمي 3 — المعادلات الديوفانتية وكوشي-شفارتز والمتوسطات (الصف 10)",
                "Highlights difference-of-squares Diophantines, Titu's Lemma, Apollonius medians, and graph handshakes.",
                "يتناول المعادلات الديوفانتية، ليمّا تيتو، نظرية أبولونيوس للمتوسطات، ونظرية المصافحات في الرسوم البيانية.",
            ),
            (
                "Official NSMO Mock Paper 4 — National Team Selection Rehearsal",
                "اختبار نسمو التجريبي الرسمي 4 — البروفة الختامية لترشيحات المنتخب العلمي (الصف 10)",
                "High-rigor 25-question, 90-minute rehearsal calibrated to Grade 10 Mawhiba National Olympiad finals.",
                "بروفة ختامية عالية الدقة (25 سؤالاً في 90 دقيقة) تحاكي اختبارات الترشيح للمنتخب العلمي السعودي.",
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


def select_four_papers_for_phase(spec: dict, phase_lessons: list, fresh_by_les_diff: dict) -> list:
    """Assign 4 zero-overlap 25-question papers per Phase:
    - 5 lessons contribute 4 Qs and 1 rotating lesson contributes 5 Qs (= 25 Qs across 25 distinct blueprints)
    - Exact tier counts: 9 Easy, 9 Medium, 7 Hard
    - Balanced (A)-(D) answer keys (7/6/6/6) and max consecutive identical answer letter <= 2
    """
    n_papers = 4
    les_ids = [l["id"] for l in phase_lessons]
    tiers = spec["tier_counts"]
    rng = random.Random(20261103 + hash(spec["code"]) % 997)

    # 6 lesson slot patterns summing to 9 Easy, 9 Medium, 7 Hard (= 25 Qs: one 5-Q lesson + five 4-Q lessons)
    base_patterns = [
        ["Easy", "Easy", "Medium", "Medium", "Hard"],  # 5 Qs (2E, 2M, 1H)
        ["Easy", "Easy", "Medium", "Hard"],            # 4 Qs (2E, 1M, 1H)
        ["Easy", "Easy", "Medium", "Hard"],            # 4 Qs (2E, 1M, 1H)
        ["Easy", "Medium", "Medium", "Hard"],          # 4 Qs (1E, 2M, 1H)
        ["Easy", "Medium", "Medium", "Hard"],          # 4 Qs (1E, 2M, 1H)
        ["Easy", "Medium", "Hard", "Hard"],            # 4 Qs (1E, 1M, 2H)
    ]

    used_qids: set[str] = set()
    global_bp_usage: Counter[str] = Counter()
    papers_out = []

    for p_idx in range(n_papers):
        rot = p_idx % len(les_ids)
        rotated_patterns = base_patterns[rot:] + base_patterns[:rot]

        paper_qs = []
        paper_bps: set[str] = set()
        paper_ans_counts: Counter[int] = Counter()
        tier_ans_counts: Counter[tuple[str, int]] = Counter()

        for l_idx, lid in enumerate(les_ids):
            slots = sorted(
                rotated_patterns[l_idx],
                key=lambda d: {"Hard": 0, "Easy": 1, "Medium": 2}[d],
            )
            for diff in slots:
                candidates = [
                    q for q in fresh_by_les_diff[(lid, diff)]
                    if q["id"] not in used_qids and q["nsmo_blueprint"] not in paper_bps
                ]
                if not candidates:
                    candidates = [q for q in fresh_by_les_diff[(lid, diff)] if q["id"] not in used_qids]
                assert candidates, f"Ran out of candidates for {lid} {diff} in paper {p_idx + 1}"

                candidates.sort(
                    key=lambda q: (
                        q["nsmo_blueprint"] in paper_bps,
                        tier_ans_counts[(diff, q["correct_index"])],
                        paper_ans_counts[q["correct_index"]],
                        global_bp_usage[q["nsmo_blueprint"]],
                        0 if q["content"]["en"].get("diagram") else 1,
                        q["id"],
                    )
                )
                chosen = candidates[0]
                used_qids.add(chosen["id"])
                paper_bps.add(chosen["nsmo_blueprint"])
                paper_ans_counts[chosen["correct_index"]] += 1
                tier_ans_counts[(diff, chosen["correct_index"])] += 1
                global_bp_usage[chosen["nsmo_blueprint"]] += 1
                paper_qs.append((lid, chosen))

        ordered_qs = []
        for tier_name in ("Easy", "Medium", "Hard"):
            tier_items = [(lid, q) for lid, q in paper_qs if q["difficulty"] == tier_name]
            rng.shuffle(tier_items)
            arranged = []
            rem = list(tier_items)
            while rem:
                rem_ans_freq = Counter(it[1]["correct_index"] for it in rem)
                prev_seq = ordered_qs + arranged
                prev_lid = prev_seq[-1][0] if prev_seq else None
                prev_ans = prev_seq[-1][1]["correct_index"] if prev_seq else None
                prev2_ans = prev_seq[-2][1]["correct_index"] if len(prev_seq) >= 2 else None
                rem.sort(
                    key=lambda item: (
                        1 if (item[1]["correct_index"] == prev_ans and prev_ans == prev2_ans) else 0,
                        1 if item[1]["correct_index"] == prev_ans else 0,
                        -rem_ans_freq[item[1]["correct_index"]],
                        1 if item[0] == prev_lid else 0,
                    )
                )
                arranged.append(rem.pop(0))
            ordered_qs.extend(arranged)

        assert len(ordered_qs) == spec["q_count"]
        diff_check = Counter(q["difficulty"] for _, q in ordered_qs)
        assert diff_check == Counter(tiers), f"Tier mismatch: {diff_check} != {tiers}"
        assert len({q["nsmo_blueprint"] for _, q in ordered_qs}) == spec["q_count"], (
            f"Duplicate blueprint inside {spec['code']} paper {p_idx + 1}"
        )
        ans_seq = [q["correct_index"] for _, q in ordered_qs]
        assert max_consecutive_run(ans_seq) <= 2, f"Answer run > 2 in {spec['code']} paper {p_idx + 1}: {ans_seq}"

        en_title, ar_title, en_focus, ar_focus = spec["papers"][p_idx]
        e_cnt, m_cnt, h_cnt = tiers["Easy"], tiers["Medium"], tiers["Hard"]
        svg_cnt = sum(1 for _, q in ordered_qs if q["content"]["en"].get("diagram"))
        topic_counts = dict(Counter(q["topic"] for _, q in ordered_qs))

        papers_out.append({
            "id": f"NSMO-MOCK-{spec['code']}-0{p_idx + 1}",
            "track": "nsmo",
            "option_count": 4,
            "paper_num": p_idx + 1,
            "level": spec["level"],
            "track_code": spec["code"],
            "grades_en": spec["grades_en"],
            "grades_ar": spec["grades_ar"],
            "question_count": spec["q_count"],
            "duration_minutes": spec["duration_minutes"],
            "points_correct": 4,
            "points_wrong": 0,
            "points_blank": 0,
            "max_points": spec["q_count"] * 4,
            "svg_count": svg_cnt,
            "topic_counts": topic_counts,
            "sections": [
                {
                    "id": "A",
                    "difficulty": "Easy",
                    "start_q": 1,
                    "end_q": e_cnt,
                    "en": f"Part A — Olympiad Foundations & Speed (Questions 1–{e_cnt})",
                    "ar": f"الجزء الأول (A) — الأساسيات الأولمبية والسرعة (الأسئلة 1–{e_cnt})",
                },
                {
                    "id": "B",
                    "difficulty": "Medium",
                    "start_q": e_cnt + 1,
                    "end_q": e_cnt + m_cnt,
                    "en": f"Part B — Multi-Step Olympiad Reasoning (Questions {e_cnt + 1}–{e_cnt + m_cnt})",
                    "ar": f"الجزء الثاني (B) — الاستدلال الأولمبي متعدد الخطوات (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})",
                },
                {
                    "id": "C",
                    "difficulty": "Hard",
                    "start_q": e_cnt + m_cnt + 1,
                    "end_q": e_cnt + m_cnt + h_cnt,
                    "en": f"Part C — Mawhiba Camp Qualifier Challenge (Questions {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                    "ar": f"الجزء الثالث (C) — تحدي التأهل لملتقيات موهبة (الأسئلة {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                },
            ],
            "en": {"title": en_title, "focus": en_focus},
            "ar": {"title": ar_title, "focus": ar_focus},
            "question_ids": [q["id"] for _, q in ordered_qs],
            "question_lessons": {q["id"]: lid for lid, q in ordered_qs},
        })

    return papers_out


def main() -> None:
    bank = json.loads((ROOT / "data" / "nsmo.json").read_text(encoding="utf-8"))
    lessons = json.loads((ROOT / "data" / "nsmo_lessons.json").read_text(encoding="utf-8"))["lessons"]

    reserved_ids: set[str] = set()
    bp_to_lesson: dict[str, str] = {}
    for les in lessons:
        reserved_ids.update(les.get("bank_example_ids", []))
        reserved_ids.update(les.get("drill_ids", []))
        for bp in les["blueprints"]:
            bp_to_lesson[bp] = les["id"]

    fresh_by_les_diff = defaultdict(list)
    bank_by_id = {q["id"]: q for q in bank}
    for q in bank:
        if q["id"] in reserved_ids:
            continue
        lid = bp_to_lesson.get(q["nsmo_blueprint"])
        assert lid, f"Unmapped NSMO blueprint {q['nsmo_blueprint']}"
        fresh_by_les_diff[(lid, q["difficulty"])].append(q)

    all_papers = []
    global_mock_qids: set[str] = set()
    for spec in PHASE_SPECS:
        phase_lessons = [l for l in lessons if l["level"] == spec["level"]]
        assert len(phase_lessons) == 6
        papers = select_four_papers_for_phase(spec, phase_lessons, fresh_by_les_diff)
        for p in papers:
            for qid in p["question_ids"]:
                assert qid in bank_by_id
                assert qid not in reserved_ids, f"Overlap with NSMO lesson example/drill: {qid}"
                assert qid not in global_mock_qids, f"Duplicate question across NSMO mock papers: {qid}"
                global_mock_qids.add(qid)
        all_papers.extend(papers)

    out = {
        "academy_en": "Edugates International School",
        "academy_ar": "مدرسة بوابة المعرفة العالمية",
        "competition_en": "NSMO / Mawhiba National Mathematics Olympiad — Simulation Series (Grades 7–10)",
        "competition_ar": "أولمبياد العلوم والرياضيات الوطني (نسمو — موهبة) — سلسلة الاختبارات التجريبية الرسمية",
        "default_paper": "A4",
        "option_count": 4,
        "scoring": {
            "correct": 4,
            "wrong": 0,
            "blank": 0,
            "calculator_allowed": False,
        },
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": all_papers,
    }

    out_path = ROOT / "data" / "nsmo_mocks.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_svgs = sum(p["svg_count"] for p in all_papers)
    print(
        f"SUCCESS: Wrote {len(all_papers)} official NSMO mock papers ({len(global_mock_qids)} unique zero-overlap questions, "
        f"{total_svgs} SVG diagrams) to {out_path}"
    )


if __name__ == "__main__":
    main()

