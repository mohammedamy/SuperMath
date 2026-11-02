"""Build & strictly validate data/kaust_mocks.json: 15 Official-Style KAUST Mathematics Competition (KMC)
Full Mock Exam Papers (5 per Track across Grades 6-7, 8-9, and 10-11; 390 distinct zero-overlap questions)."""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TRACK_SPECS = [
    {
        "level": "Track 1: Grades 6-7",
        "code": "T1",
        "grades_en": "Grades 6–7 (Junior Division)",
        "grades_ar": "الصفوف 6–7 (المسار التأسيسي)",
        "q_count": 24,
        "per_lesson": 4,
        "tier_counts": {"Easy": 8, "Medium": 8, "Hard": 8},
        "duration_minutes": 120,
        "papers": [
            (
                "Official KMC Mock Paper 1 — Junior Elimination Simulation",
                "الاختبار التجريبي الرسمي 1 — محاكاة التصفيات الأولى (الصفوف 6–7)",
                "Balanced full-syllabus simulation across arithmetic shortcuts, LCM cycles, visual geometry, and parity.",
                "محاكاة شاملة ومتوازنة تغطي اختصارات الحساب، المضاعف المشترك الأصغر، الهندسة البصرية، والزوجية والفردية.",
            ),
            (
                "Official KMC Mock Paper 2 — Visual & Number Sense Challenge",
                "الاختبار التجريبي الرسمي 2 — تحدي الحس العددي والبصري (الصفوف 6–7)",
                "Emphasizes grid fractions, clock & fold angles, function machines, and counting without overcounting.",
                "يركّز على شبكات الكسور، زوايا الساعة وطي الورق، آلات الدوال، ومبادئ العد دون تكرار.",
            ),
            (
                "Official KMC Mock Paper 3 — Multi-Step Logic & Patterns",
                "الاختبار التجريبي الرسمي 3 — الأنماط والاستدلال المتدرج (الصفوف 6–7)",
                "Focuses on age-gap invariants, train/chase timelines, dot growth patterns, and 3D cube stacks.",
                "يركّز على ثبات فرق العمر، مسائل اللحاق والالتقاء، أنماط النقاط المتنامية، ومجسمات المكعبات.",
            ),
            (
                "Official KMC Mock Paper 4 — Pre-Qualifier Speed & Accuracy",
                "الاختبار التجريبي الرسمي 4 — دقة وسرعة ما قبل التأهل (الصفوف 6–7)",
                "Sharpens trap-avoidance on remainders, Venn clubs, magic squares, and composite rectilinear areas.",
                "يصقل مهارة تجنّب المصائد الحسابية في البواقي، مخططات فن، المربعات السحرية، والمساحات المركّبة.",
            ),
            (
                "Official KMC Mock Paper 5 — Championship Dress Rehearsal",
                "الاختبار التجريبي الرسمي 5 — البروفة الختامية للمسابقة (الصفوف 6–7)",
                "Final exam-day rehearsal calibrating pacing and smart blank-vs-guess strategy across 24 KMC problems.",
                "البروفة النهائية ليوم الاختبار لضبط توزيع الوقت واستراتيجية الترك الذكي عبر 24 مسألة تنافسية.",
            ),
        ],
    },
    {
        "level": "Track 2: Grades 8-9",
        "code": "T2",
        "grades_en": "Grades 8–9 (Intermediate Division)",
        "grades_ar": "الصفوف 8–9 (المسار المتوسط)",
        "q_count": 24,
        "per_lesson": 4,
        "tier_counts": {"Easy": 8, "Medium": 8, "Hard": 8},
        "duration_minutes": 120,
        "papers": [
            (
                "Official KMC Mock Paper 1 — Intermediate Elimination Simulation",
                "الاختبار التجريبي الرسمي 1 — محاكاة التصفيات الأولى (الصفوف 8–9)",
                "Full intermediate simulation spanning prime factorizations, algebraic identities, circle geometry, and grid paths.",
                "محاكاة متكاملة تشمل التحليل الأولي، المتطابقات الجبرية، هندسة الدائرة، ومسارات الشبكات.",
            ),
            (
                "Official KMC Mock Paper 2 — Algebraic Factoring & Modular Cycles",
                "الاختبار التجريبي الرسمي 2 — التحليل الجبري والدورات المعيارية (الصفوف 8–9)",
                "Highlights telescoping products, Simon's factoring, trailing zeros, and harmonic round-trip speeds.",
                "يركّز على الجداءات التلسكوبية، إتمام المستطيل، الأصفار الطرفية، والسرعة المتوسطة ذهاباً وإياباً.",
            ),
            (
                "Official KMC Mock Paper 3 — Euclidean Geometry & Rate Systems",
                "الاختبار التجريبي الرسمي 3 — الهندسة الإقليدية ومعدلات العمل (الصفوف 8–9)",
                "Tests Thales semicircles, trapezoid Pythagoras, inlet-leak tanks, and tournament point invariants.",
                "يختبر زوايا نصف الدائرة (طاليس)، شبه المنحرف المتطابق الساقين، خزانات التدفق والتسريب، ونقاط الدوريات.",
            ),
            (
                "Official KMC Mock Paper 4 — Combinatorial Reasoning & Number Theory",
                "الاختبار التجريبي الرسمي 4 — التركيبات ونظرية الأعداد (الصفوف 8–9)",
                "Balances 3-set inclusion-exclusion, palindrome divisibility, counterfeit weighings, and probability transfers.",
                "يوازن بين مبدأ الشمول والإقصاء، قابلية قسمة الأعداد المتناظرة، أوزان العملات، واحتمالات النقل.",
            ),
            (
                "Official KMC Mock Paper 5 — Championship Dress Rehearsal",
                "الاختبار التجريبي الرسمي 5 — البروفة الختامية للمسابقة (الصفوف 8–9)",
                "Complete 2-hour dress rehearsal calibrated to official Grades 8–9 KMC elimination difficulty.",
                "بروفة كاملة لمدة ساعتين تحاكي بدقة مستوى وتدرج اختبار التصفيات الرسمي للصفين 8 و9.",
            ),
        ],
    },
    {
        "level": "Track 3: Grades 10-11",
        "code": "T3",
        "grades_en": "Grades 10–11 (Senior Division)",
        "grades_ar": "الصفوف 10–11 (المسار المتقدم)",
        "q_count": 30,
        "per_lesson": 5,
        "tier_counts": {"Easy": 10, "Medium": 10, "Hard": 10},
        "duration_minutes": 120,
        "papers": [
            (
                "Official KMC Mock Paper 1 — Senior Elimination Simulation",
                "الاختبار التجريبي الرسمي 1 — محاكاة التصفيات الأولى (الصفوف 10–11)",
                "Full 30-question senior paper covering Legendre's formula, Vieta's roots, Power of a Point, and Stars & Bars.",
                "اختبار كامل من 30 سؤالاً يغطي صيغة ليجاندر، علاقات فييتا، قوة النقطة، وطريقة النجوم والفواصل.",
            ),
            (
                "Official KMC Mock Paper 2 — Olympiad Algebra & Floor Sums",
                "الاختبار التجريبي الرسمي 2 — الجبر الأولمبي ومجاميع الجزء الصحيح (الصفوف 10–11)",
                "Features nested radicals, functional involutions, Hermite floor sums, and parabola chord geometry.",
                "يتناول الجذور المتداخلة، المعادلات الدالية، مجاميع الجزء الصحيح، وهندسة أوتار القطع المكافئ.",
            ),
            (
                "Official KMC Mock Paper 3 — Circle Theorems, Inradii & 3D Cross-Sections",
                "الاختبار التجريبي الرسمي 3 — نظريات الدائرة والمقاطع الهندسية (الصفوف 10–11)",
                "Deep practice on secant-tangent theorems, angle bisector ratios, right-triangle inradii, and inscribed solids.",
                "تدريب معمّق على القواطع والمماسات، منصف الزاوية، نصف قطر الدائرة الداخلة، والمجسمات المحاطة.",
            ),
            (
                "Official KMC Mock Paper 4 — Diophantine Equations & Combinatorics",
                "الاختبار التجريبي الرسمي 4 — المعادلات الديوفانتية والتركيبات (الصفوف 10–11)",
                "Combines Frobenius coin bounds, divisor-square structure, circular seating, and geometric probability.",
                "يجمع بين معضلة العملات لفروبينيوس، قواسم المربعات والمكعبات، الجلوس الدائري، والاحتمال الهندسي.",
            ),
            (
                "Official KMC Mock Paper 5 — Championship Dress Rehearsal",
                "الاختبار التجريبي الرسمي 5 — البروفة الختامية للمسابقة (الصفوف 10–11)",
                "High-intensity 30-question, 120-minute final rehearsal engineered for KMC Final Round qualification.",
                "البروفة النهائية المكثفة (30 سؤالاً في 120 دقيقة) المصممة للتأهل إلى المرحلة النهائية في كاوست.",
            ),
        ],
    },
]


def select_five_papers_for_track(spec: dict, track_lessons: list, fresh_by_les_diff: dict) -> list:
    """Assign 5 zero-overlap papers for a track with:
    - Exact per-lesson quota (4 Qs/lesson for T1/T2 = 24; 5 Qs/lesson for T3 = 30)
    - Exact tier counts (8/8/8 for T1/T2; 10/10/10 for T3)
    - 100% distinct kmc_blueprint within every paper
    - Zero question ID overlap across all 5 papers and lessons/drills
    """
    n_papers = 5
    les_ids = [l["id"] for l in track_lessons]
    per_les = spec["per_lesson"]
    tiers = spec["tier_counts"]

    # Deterministic balanced tier matrix shape: papers (5) x lessons (6) -> list of difficulties of length per_les
    # Check available counts per (les_id, diff) so we never exceed a lesson's Hard/Easy supply across 5 papers.
    rng = random.Random(20261102 + hash(spec["code"]) % 997)

    # Build difficulty slots per paper (each lesson gets `per_les` items; sum across 6 lessons = Easy/Medium/Hard quota)
    # For T1/T2 (24 Qs, 4 per lesson, 8E/8M/8H): in each paper, 2 lessons get (2E,1M,1H), 2 get (1E,2M,1H), 2 get (1E,1M,2H)!
    # Rotating by paper index `p` means across 5 papers EVERY lesson needs at most 7E, 7M, 7H (and minimum available is 10H, 21E, 27M!).
    # For T3 (30 Qs, 5 per lesson, 10E/10M/10H): in each paper, 2 lessons get (2E,2M,1H), 2 get (2E,1M,2H), 2 get (1E,2M,2H)!
    # Across 5 papers EVERY T3 lesson needs at most 9E, 9M, 9H (and minimum available is 19H, 25E, 42M!).
    if per_les == 4:
        base_patterns = [
            ["Easy", "Easy", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Hard"],
            ["Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Hard", "Hard"],
        ]
    else:
        base_patterns = [
            ["Easy", "Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Medium", "Hard", "Hard"],
        ]

    used_qids = set()
    global_bp_usage = Counter()
    papers_out = []

    for p_idx in range(n_papers):
        # Rotate patterns across lessons so every lesson gets balanced difficulty across the 5 papers
        rot = p_idx % len(les_ids)
        rotated_patterns = base_patterns[rot:] + base_patterns[:rot]

        paper_qs = []
        paper_bps = set()
        paper_ans_counts = Counter()

        # Assign Hard -> Easy -> Medium within each lesson (most blueprint-constrained first)
        for l_idx, lid in enumerate(les_ids):
            slots = sorted(
                rotated_patterns[l_idx],
                key=lambda d: {"Hard": 0, "Easy": 1, "Medium": 2}[d],
            )
            for diff in slots:
                candidates = [
                    q for q in fresh_by_les_diff[(lid, diff)]
                    if q["id"] not in used_qids and q["kmc_blueprint"] not in paper_bps
                ]
                if not candidates:
                    # Fallback relaxing blueprint uniqueness within lesson only if mathematically forced
                    candidates = [q for q in fresh_by_les_diff[(lid, diff)] if q["id"] not in used_qids]
                assert candidates, f"Ran out of candidates for {lid} {diff} in paper {p_idx + 1}"

                # Prefer unused blueprints, balanced A-E answer letters, least global blueprint reuse, and SVG diagrams
                candidates.sort(
                    key=lambda q: (
                        q["kmc_blueprint"] in paper_bps,
                        paper_ans_counts[q["correct_index"]],
                        global_bp_usage[q["kmc_blueprint"]],
                        0 if q["content"]["en"].get("diagram") else 1,
                        q["id"],
                    )
                )
                chosen = candidates[0]
                used_qids.add(chosen["id"])
                paper_bps.add(chosen["kmc_blueprint"])
                paper_ans_counts[chosen["correct_index"]] += 1
                global_bp_usage[chosen["kmc_blueprint"]] += 1
                paper_qs.append((lid, chosen))

        # Order questions strictly by Part A (Easy) -> Part B (Medium) -> Part C (Hard),
        # interleaving lessons/topics AND avoiding consecutive identical answer letters (max_run <= 2)!
        ordered_qs = []
        for tier_name in ("Easy", "Medium", "Hard"):
            tier_items = [(lid, q) for lid, q in paper_qs if q["difficulty"] == tier_name]
            rng.shuffle(tier_items)
            arranged = []
            rem = list(tier_items)
            while rem:
                prev_seq = ordered_qs + arranged
                prev_lid = prev_seq[-1][0] if prev_seq else None
                prev_ans = prev_seq[-1][1]["correct_index"] if prev_seq else None
                rem.sort(
                    key=lambda item: (
                        1 if item[1]["correct_index"] == prev_ans else 0,
                        1 if item[0] == prev_lid else 0,
                    )
                )
                arranged.append(rem.pop(0))
            ordered_qs.extend(arranged)

        assert len(ordered_qs) == spec["q_count"]
        diff_check = Counter(q["difficulty"] for _, q in ordered_qs)
        assert diff_check == Counter(tiers), f"Tier mismatch: {diff_check} != {tiers}"
        assert len({q["kmc_blueprint"] for _, q in ordered_qs}) == spec["q_count"], (
            f"Duplicate blueprint inside {spec['code']} paper {p_idx + 1}"
        )

        en_title, ar_title, en_focus, ar_focus = spec["papers"][p_idx]
        e_cnt = tiers["Easy"]
        m_cnt = tiers["Medium"]
        h_cnt = tiers["Hard"]
        svg_cnt = sum(1 for _, q in ordered_qs if q["content"]["en"].get("diagram"))
        topic_counts = dict(Counter(q["topic"] for _, q in ordered_qs))

        papers_out.append({
            "id": f"KMC-MOCK-{spec['code']}-0{p_idx + 1}",
            "paper_num": p_idx + 1,
            "level": spec["level"],
            "track_code": spec["code"],
            "grades_en": spec["grades_en"],
            "grades_ar": spec["grades_ar"],
            "question_count": spec["q_count"],
            "duration_minutes": spec["duration_minutes"],
            "points_correct": 4,
            "points_wrong": -1,
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
                    "en": f"Part A — Core Reasoning & Speed (Questions 1–{e_cnt})",
                    "ar": f"الجزء الأول (A) — التفكير الأساسي والسرعة (الأسئلة 1–{e_cnt})",
                },
                {
                    "id": "B",
                    "difficulty": "Medium",
                    "start_q": e_cnt + 1,
                    "end_q": e_cnt + m_cnt,
                    "en": f"Part B — Multi-Step Contest Problems (Questions {e_cnt + 1}–{e_cnt + m_cnt})",
                    "ar": f"الجزء الثاني (B) — المسائل التنافسية متعددة الخطوات (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})",
                },
                {
                    "id": "C",
                    "difficulty": "Hard",
                    "start_q": e_cnt + m_cnt + 1,
                    "end_q": e_cnt + m_cnt + h_cnt,
                    "en": f"Part C — Olympiad Elimination Challenge (Questions {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                    "ar": f"الجزء الثالث (C) — تحدي التصفيات الأولمبية (الأسئلة {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                },
            ],
            "en": {
                "title": en_title,
                "focus": en_focus,
            },
            "ar": {
                "title": ar_title,
                "focus": ar_focus,
            },
            "question_ids": [q["id"] for _, q in ordered_qs],
            "question_lessons": {q["id"]: lid for lid, q in ordered_qs},
        })

    return papers_out


def main() -> None:
    bank = json.loads((ROOT / "data" / "kaust.json").read_text(encoding="utf-8"))
    lessons_doc = json.loads((ROOT / "data" / "kaust_lessons.json").read_text(encoding="utf-8"))
    lessons = lessons_doc["lessons"]

    # Exclude all 216 questions already featured as worked examples or end-of-lesson drills
    reserved_ids = set()
    bp_to_lesson = {}
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
        lid = bp_to_lesson.get(q["kmc_blueprint"])
        assert lid, f"Unmapped blueprint {q['kmc_blueprint']}"
        fresh_by_les_diff[(lid, q["difficulty"])].append(q)

    all_papers = []
    global_mock_qids = set()
    for spec in TRACK_SPECS:
        track_lessons = [l for l in lessons if l["level"] == spec["level"]]
        assert len(track_lessons) == 6
        papers = select_five_papers_for_track(spec, track_lessons, fresh_by_les_diff)
        for p in papers:
            for qid in p["question_ids"]:
                assert qid in bank_by_id
                assert qid not in reserved_ids, f"Overlap with lesson example/drill: {qid}"
                assert qid not in global_mock_qids, f"Duplicate question across mock papers: {qid}"
                global_mock_qids.add(qid)
        all_papers.extend(papers)

    out = {
        "academy_en": "Edugates International School",
        "academy_ar": "مدرسة بوابة المعرفة العالمية",
        "competition_en": "KAUST Mathematics Competition (KMC) — First Round Simulation Series",
        "competition_ar": "مسابقة كاوست للرياضيات (KMC) — سلسلة اختبارات المحاكاة الرسمية للتصفيات",
        "default_paper": "A4",
        "scoring": {
            "correct": 4,
            "wrong": -1,
            "blank": 0,
            "calculator_allowed": False,
        },
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": all_papers,
    }

    out_path = ROOT / "data" / "kaust_mocks.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_svgs = sum(p["svg_count"] for p in all_papers)
    print(
        f"SUCCESS: Wrote {len(all_papers)} official KMC mock papers ({len(global_mock_qids)} unique zero-overlap questions, "
        f"{total_svgs} SVG diagrams) to {out_path}"
    )
    for p in all_papers:
        print(
            f"  {p['id']} ({p['level']}): {p['question_count']} Qs | {p['duration_minutes']} min | "
            f"Max {p['max_points']} pts | {p['svg_count']} SVGs | topics={p['topic_counts']}"
        )


if __name__ == "__main__":
    main()
