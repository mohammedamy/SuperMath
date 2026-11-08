"""Build & strictly validate data/olympiad_mocks.json: 12 Official Olympiad Screening Mock Exam Papers
(4 per Tier across Grades 7–12: 25 5-option MCQs, 90 min, +6 / 0 / 0 scoring = 150 max points, 300 unique zero-overlap questions)."""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TIER_SPECS = [
    {
        "level": "Tier 1: Junior Olympiad (Grades 7-8)",
        "code": "T1",
        "grades_en": "Tier 1 · Junior Olympiad (Grades 7–8)",
        "grades_ar": "المستوى 1 · أولمبياد الناشئين (الصفان 7–8)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "max_points": 150,
        "duration_minutes": 90,
        "papers": [
            (
                "Official Junior Olympiad Mock 1 — JBMO & AMC 8 Screening Simulation",
                "اختبار الأولمبياد التجريبي الرسمي 1 — محاكاة تصفيات الناشئين (الصفان 7–8)",
                "Balanced 25-question, 150-point Junior Olympiad paper spanning divisor counts, telescoping sums, AM-GM bounds, cyclic angles, and parity tilings.",
                "محاكاة أولمبية متوازنة من 25 سؤالاً (150 نقطة) تشمل القواسم، المجاميع التلسكوبية، متباينة الوسطين، الزوايا المحيطية، وتكافؤ التبليط.",
            ),
            (
                "Official Junior Olympiad Mock 2 — Simon's Trick, Incircles & Pigeonhole",
                "اختبار الأولمبياد التجريبي الرسمي 2 — التحليل الديوفانتي والدائرة الداخلة وبرج الحمام (الصفان 7–8)",
                "Highlights Diophantine factoring, Sophie Germain identities, incircle tangent lengths, Heron shortest reflections, and Dirichlet boxes.",
                "يركّز على التحليل الديوفانتي، متطابقة صوفي جيرمان، مماسات الدائرة الداخلة، أقصر مسار بالانعكاس، ومبدأ برج الحمام.",
            ),
            (
                "Official Junior Olympiad Mock 3 — Modular Cycles, Pick's Theorem & Bijections",
                "اختبار الأولمبياد التجريبي الرسمي 3 — البواقي الدورية ومبرهنة بيك والتقابلات (الصفان 7–8)",
                "Focuses on modular remainders, nested radicals, discrete smoothing, lattice polygon areas, and Stars-and-Bars bijections.",
                "يركّز على الحساب المعياري، الجذور المتداخلة، التحسين المتقطع، مساحات المضلعات الشبكية، وتقابلات النجوم والفواصل.",
            ),
            (
                "Official Junior Olympiad Mock 4 — Junior Gold Medal Dress Rehearsal",
                "اختبار الأولمبياد التجريبي الرسمي 4 — البروفة الذهبية لأولمبياد الناشئين (الصفان 7–8)",
                "Full 90-minute, 150-point championship rehearsal calibrated to Grades 7–8 regional and junior international Olympiad cutoffs.",
                "البروفة الختامية الشاملة (25 سؤالاً في 90 دقيقة — 150 نقطة) لمعايير التأهل والميداليات في أولمبياد الناشئين.",
            ),
        ],
    },
    {
        "level": "Tier 2: Intermediate Olympiad (Grades 9-10)",
        "code": "T2",
        "grades_en": "Tier 2 · Intermediate Olympiad (Grades 9–10)",
        "grades_ar": "المستوى 2 · الأولمبياد المتوسط (الصفان 9–10)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "max_points": 150,
        "duration_minutes": 90,
        "papers": [
            (
                "Official Intermediate Olympiad Mock 1 — AMC 10 & BMO1 Screening Simulation",
                "اختبار الأولمبياد التجريبي الرسمي 1 — محاكاة تصفيات المستوى المتوسط (الصفان 9–10)",
                "Balanced 25-question, 150-point paper across Euler totient, Newton power sums, Titu's Lemma, radical axes, and Catalan paths.",
                "اختبار أولمبي متوازن من 25 سؤالاً (150 نقطة) يغطي دالة أويلر، مجاميع نيوتن، متباينة تيتو، المحور الأساسي، ومسارات كاتالان.",
            ),
            (
                "Official Intermediate Olympiad Mock 2 — CRT, Ptolemy & Ceva-Menelaus",
                "اختبار الأولمبياد التجريبي الرسمي 2 — البواقي الصينية وبطليموس وسيفا ومينيلاوس (الصفان 9–10)",
                "Features simultaneous congruences, polynomial remainder interpolation, Nesbitt cyclic sums, Ptolemy cyclic quads, and tree degrees.",
                "يتناول مبرهنة البواقي الصينية، استيفاء كثيرات الحدود، المجاميع الدورية، رباعيات بطليموس الدائرية، ودرجات الأشجار.",
            ),
            (
                "Official Intermediate Olympiad Mock 3 — Legendre p-Adic, Euler Line & Monovariants",
                "اختبار الأولمبياد التجريبي الرسمي 3 — صيغة ليجاندر وخط أويلر وشبه اللامتغيرات (الصفان 9–10)",
                "Tests factorial p-adic valuations, functional involutions, rearrangement bounds, Nine-Point Circle geometry, and impartial games.",
                "يختبر الأسس الأولية للمضروب، المعادلات الدالية، متباينة إعادة الترتيب، دائرة النقاط التسع، والألعاب الاستراتيجية.",
            ),
            (
                "Official Intermediate Olympiad Mock 4 — Intermediate Gold Medal Dress Rehearsal",
                "اختبار الأولمبياد التجريبي الرسمي 4 — البروفة الذهبية للأولمبياد المتوسط (الصفان 9–10)",
                "High-rigor 90-minute, 150-point dress rehearsal calibrated to AMC 10 / Arab Olympiad / BMO1 distinction cutoffs.",
                "البروفة النهائية الكبرى (25 سؤالاً في 90 دقيقة — 150 نقطة) لأبطال الصفين التاسع والعاشر في الأولمبياد الرياضي.",
            ),
        ],
    },
    {
        "level": "Tier 3: Senior Olympiad (Grades 11-12)",
        "code": "T3",
        "grades_en": "Tier 3 · Senior Olympiad (Grades 11–12)",
        "grades_ar": "المستوى 3 · الأولمبياد المتقدم IMO/BMO (الصفان 11–12)",
        "q_count": 25,
        "tier_counts": {"Easy": 9, "Medium": 9, "Hard": 7},
        "max_points": 150,
        "duration_minutes": 90,
        "papers": [
            (
                "Official Senior Olympiad Mock 1 — AMC 12, AIME & IMO Shortlist Screening",
                "اختبار الأولمبياد التجريبي الرسمي 1 — محاكاة الأولمبياد المتقدم والـ IMO (الصفان 11–12)",
                "Full 25-question, 150-point senior paper spanning Lifting the Exponent (LTE), roots-of-unity filters, Schur/Hölder bounds, Chicken-Feet Lemma, and Turán graphs.",
                "اختبار أولمبي متقدم من 25 سؤالاً (150 نقطة) يشمل رفع الأس (LTE)، جذور الوحدة، متباينتي شور وهولدر، لمّة الحافز، ومبرهنة توران.",
            ),
            (
                "Official Senior Olympiad Mock 2 — Multiplicative Orders, Spiral Similarity & Burnside",
                "اختبار الأولمبياد التجريبي الرسمي 2 — الرتب الضربية والتشابه الحلزوني ولمّة بيرنسايد (الصفان 11–12)",
                "Highlights primitive-root orders, IMO functional equations, algebraic tangent-line bounds, inversion/spiral similarity, and Burnside symmetries.",
                "يركّز على الرتب الضربية، المعادلات الدالية الأولمبية، طريقة خط المماس الجبرية، التشابه الحلزوني والانعكاس الدائري، وتماثلات بيرنسايد.",
            ),
            (
                "Official Senior Olympiad Mock 3 — Vieta Jumping, Projective Hexagons & Probabilistic Method",
                "اختبار الأولمبياد التجريبي الرسمي 3 — قفز فييتا والهندسة الإسقاطية والطريقة الاحتمالية (الصفان 11–12)",
                "Focuses on Vieta jumping descent, cyclotomic polynomials, Miquel/Simson configurations, disphenoid 3D tetrahedra, and expectation bounds.",
                "يركّز على قفز فييتا، كثيرات الحدود الدويرية، نقاط ميكيل ومستقيم سيمسون، رباعيات الأوجه الفضائية، والطريقة الاحتمالية.",
            ),
            (
                "Official Senior Olympiad Mock 4 — National Team Selection Dress Rehearsal",
                "اختبار الأولمبياد التجريبي الرسمي 4 — البروفة النهائية لمنتخب الأولمبياد الدولي (الصفان 11–12)",
                "Championship 90-minute, 150-point senior Olympiad dress rehearsal engineered for national team screening and IMO shortlist preparation.",
                "البروفة الختامية الكبرى (25 سؤالاً في 90 دقيقة — 150 نقطة) لإعداد وتصفية مرشحي المنتخب الوطني للأولمبياد الدولي للرياضيات.",
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


def select_four_papers_for_tier(spec: dict, tier_lessons: list, fresh_by_les_diff: dict) -> list:
    """Assign 4 zero-overlap 25-question papers per Tier (9 Easy, 9 Medium, 7 Hard) with balanced (A)–(E) keys."""
    n_papers = 4
    les_ids = [l["id"] for l in tier_lessons]
    tiers = spec["tier_counts"]
    rng = random.Random(20261106 + hash(spec["code"]) % 997)

    # 6 lessons summing to 9 Easy + 9 Medium + 7 Hard = 25 Qs per paper:
    # 3 lessons of 4 Qs + 2 lessons of 4 Qs + 1 lesson of 5 Qs -> wait: 5*4 + 5 = 25!
    base_patterns = [
        ["Easy", "Easy", "Medium", "Medium", "Hard"],  # 5
        ["Easy", "Easy", "Medium", "Hard"],            # 4
        ["Easy", "Easy", "Medium", "Hard"],            # 4
        ["Easy", "Medium", "Medium", "Hard"],          # 4
        ["Easy", "Medium", "Medium", "Hard"],          # 4
        ["Easy", "Medium", "Hard", "Hard"],            # 4 -> sum: Easy=9, Medium=9, Hard=7 = 25!
    ]

    used_qids: set[str] = set()
    global_bp_usage: Counter[str] = Counter()
    papers_out = []

    for p_idx in range(n_papers):
        rot = p_idx % len(les_ids)
        rotated_patterns = base_patterns[rot:] + base_patterns[:rot]

        paper_qs = []
        paper_bp_counts: Counter[str] = Counter()
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
                    if q["id"] not in used_qids
                ]
                assert candidates, f"Ran out of candidates for {lid} {diff} in paper {p_idx + 1}"

                candidates.sort(
                    key=lambda q: (
                        paper_bp_counts[q["olympiad_blueprint"]],
                        tier_ans_counts[(diff, q["correct_index"])],
                        paper_ans_counts[q["correct_index"]],
                        global_bp_usage[q["olympiad_blueprint"]],
                        0 if q["content"]["en"].get("diagram") else 1,
                        q["id"],
                    )
                )
                chosen = candidates[0]
                used_qids.add(chosen["id"])
                paper_bp_counts[chosen["olympiad_blueprint"]] += 1
                paper_ans_counts[chosen["correct_index"]] += 1
                tier_ans_counts[(diff, chosen["correct_index"])] += 1
                global_bp_usage[chosen["olympiad_blueprint"]] += 1
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
        distinct_bps = len({q["olympiad_blueprint"] for _, q in ordered_qs})
        assert distinct_bps >= 20, f"Too few blueprints ({distinct_bps}) in {spec['code']} paper {p_idx + 1}"
        ans_seq = [q["correct_index"] for _, q in ordered_qs]
        assert max_consecutive_run(ans_seq) <= 2, f"Answer run > 2 in {spec['code']} paper {p_idx + 1}: {ans_seq}"

        en_title, ar_title, en_focus, ar_focus = spec["papers"][p_idx]
        e_cnt, m_cnt, h_cnt = tiers["Easy"], tiers["Medium"], tiers["Hard"]
        svg_cnt = sum(1 for _, q in ordered_qs if q["content"]["en"].get("diagram"))
        topic_counts = dict(Counter(q["topic"] for _, q in ordered_qs))
        max_pts = spec["q_count"] * 6
        assert max_pts == spec["max_points"]

        papers_out.append({
            "id": f"OLYM-MOCK-{spec['code']}-0{p_idx + 1}",
            "track": "olympiad",
            "option_count": 5,
            "paper_num": p_idx + 1,
            "level": spec["level"],
            "track_code": spec["code"],
            "grades_en": spec["grades_en"],
            "grades_ar": spec["grades_ar"],
            "question_count": spec["q_count"],
            "duration_minutes": spec["duration_minutes"],
            "tier_points": None,
            "points_correct": 6,
            "points_wrong": 0,
            "points_blank": 0,
            "max_points": max_pts,
            "svg_count": svg_cnt,
            "topic_counts": topic_counts,
            "sections": [
                {
                    "id": "A",
                    "difficulty": "Easy",
                    "points_each": 6,
                    "start_q": 1,
                    "end_q": e_cnt,
                    "en": f"Part A — Olympiad Foundations & Speed (Questions 1–{e_cnt})",
                    "ar": f"الجزء الأول (A) — الأساسيات الأولمبية والسرعة (الأسئلة 1–{e_cnt})",
                },
                {
                    "id": "B",
                    "difficulty": "Medium",
                    "points_each": 6,
                    "start_q": e_cnt + 1,
                    "end_q": e_cnt + m_cnt,
                    "en": f"Part B — Structural Lemmas & Multi-Step Synthesis (Questions {e_cnt + 1}–{e_cnt + m_cnt})",
                    "ar": f"الجزء الثاني (B) — اللمّات البنيوية والتركيب متعدد الخطوات (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})",
                },
                {
                    "id": "C",
                    "difficulty": "Hard",
                    "points_each": 6,
                    "start_q": e_cnt + m_cnt + 1,
                    "end_q": e_cnt + m_cnt + h_cnt,
                    "en": f"Part C — National & International Olympiad Qualifier (Questions {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                    "ar": f"الجزء الثالث (C) — تحدي التصفيات الوطنية والدولية (الأسئلة {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                },
            ],
            "en": {"title": en_title, "focus": en_focus},
            "ar": {"title": ar_title, "focus": ar_focus},
            "question_ids": [q["id"] for _, q in ordered_qs],
            "question_lessons": {q["id"]: lid for lid, q in ordered_qs},
        })

    return papers_out


def main() -> None:
    bank = json.loads((ROOT / "data" / "olympiad.json").read_text(encoding="utf-8"))
    lessons = json.loads((ROOT / "data" / "olympiad_lessons.json").read_text(encoding="utf-8"))["lessons"]

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
        lid = bp_to_lesson.get(q["olympiad_blueprint"])
        assert lid, f"Unmapped Olympiad blueprint {q['olympiad_blueprint']}"
        fresh_by_les_diff[(lid, q["difficulty"])].append(q)

    all_papers = []
    global_mock_qids: set[str] = set()
    for spec in TIER_SPECS:
        tier_lessons = [l for l in lessons if l["level"] == spec["level"]]
        assert len(tier_lessons) == 6
        papers = select_four_papers_for_tier(spec, tier_lessons, fresh_by_les_diff)
        for p in papers:
            for qid in p["question_ids"]:
                assert qid in bank_by_id
                assert qid not in reserved_ids, f"Overlap with Olympiad lesson example/drill: {qid}"
                assert qid not in global_mock_qids, f"Duplicate question across Olympiad mock papers: {qid}"
                global_mock_qids.add(qid)
        all_papers.extend(papers)

    out = {
        "academy_en": "Edugates International School",
        "academy_ar": "مدرسة بوابة المعرفة العالمية",
        "competition_en": "Mathematical Olympiad (IMO / BMO / AMC) — Official Screening Series (Grades 7–12)",
        "competition_ar": "الأولمبياد الرياضي (الدولي والإقليمي) — سلسلة اختبارات التصفيات الرسمية (الصفوف 7–12)",
        "default_paper": "A4",
        "option_count": 5,
        "scoring": {
            "correct": 6,
            "wrong": 0,
            "blank": 0,
            "calculator_allowed": False,
        },
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": all_papers,
    }

    out_path = ROOT / "data" / "olympiad_mocks.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_svgs = sum(p["svg_count"] for p in all_papers)
    print(
        f"SUCCESS: Wrote {len(all_papers)} official Olympiad mock papers ({len(global_mock_qids)} unique zero-overlap questions, "
        f"{total_svgs} SVG diagrams) to {out_path}"
    )


if __name__ == "__main__":
    main()
