"""Build & strictly validate data/kangaroo_mocks.json: 24 Official-Style Kangaroo Math (Grades 1–12)
Full Mock Exam Papers (4 per Division: 24 Qs / 96 pts for PreEcolier, Ecolier & Benjamin;
30 Qs / 120 pts for Cadet, Junior & Student; 75 min, 3/4/5-point scoring, 648 unique zero-overlap questions)."""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TIER_POINTS = {"Easy": 3, "Medium": 4, "Hard": 5}

DIVISION_SPECS = [
    {
        "level": "PreEcolier",
        "code": "PRE",
        "grades_en": "PreEcolier · Grades 1–2",
        "grades_ar": "بري إيكولير · الصفان 1–2",
        "q_count": 24,
        "tier_counts": {"Easy": 8, "Medium": 8, "Hard": 8},
        "max_points": 96,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba PreEcolier Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة بري إيكولير (الصفان 1–2)",
                "Balanced 24-question, 96-point Grades 1–2 simulation across skip-counting hops, toy balances, shape collages, wooden blocks, and clocks.",
                "محاكاة متوازنة من 24 سؤالاً (96 نقطة) للصفين الأول والثاني تشمل قفزات الأعداد، الموازين، الأشكال الهندسية، المكعبات، والساعات.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Tens & Ones, Bead Trains & Mirror Stamps",
                "اختبار كانجارو التجريبي الرسمي 2 — الآحاد والعشرات وقطار الخرز والأختام (الصفان 1–2)",
                "Highlights two-digit place-value blocks, fruit icon sums, repeating bead necklaces, mirror stamps, and marble bags.",
                "يركّز على قوالب الآحاد والعشرات، ألغاز الصور، أنماط الخرز، الأختام المنعكسة، وسحب الكرات الملونة.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Mini Pyramids, Paper Cuts & Coin Purses",
                "اختبار كانجارو التجريبي الرسمي 3 — الأهرامات الصغيرة وقص الأشرطة والنقود (الصفان 1–2)",
                "Focuses on mini brick pyramids, odd/even pairs, folded ribbon cuts, opposite die dots, and coin purse totals.",
                "يركّز على الأهرامات العددية المبسطة، الأزواج والفردي، قص الأشرطة المطوية، نقاط حجر النرد، وجمع النقود.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Little Kangaroo Gold Medal Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية لصغار الكنغر (الصفان 1–2)",
                "Complete 75-minute, 96-point PreEcolier dress rehearsal engineered for Grades 1–2 Mawhiba Kangaroo medalists.",
                "بروفة شاملة مدتها 75 دقيقة (24 سؤالاً — 96 نقطة) تحاكي معايير الميدالية الذهبية لمستوى بري إيكولير.",
            ),
        ],
    },
    {
        "level": "Ecolier",
        "code": "ECO",
        "grades_en": "Ecolier · Grades 3–4",
        "grades_ar": "إيكولير · الصفان 3–4",
        "q_count": 24,
        "tier_counts": {"Easy": 8, "Medium": 8, "Hard": 8},
        "max_points": 96,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba Ecolier Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة إيكولير (الصفان 3–4)",
                "Balanced 24-question, 96-point Kangaroo simulation across number pyramids, toy balances, staircase perimeters, cube stacks, and clocks.",
                "محاكاة متوازنة من 24 سؤالاً (96 نقطة) تشمل الأهرامات العددية، الموازين، المحيط المتدرج، المكعبات، والساعات.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Spatial Stamps, Ribbons & Logic",
                "اختبار كانجارو التجريبي الرسمي 2 — الأختام البصرية والأشرطة والمنطق (الصفان 3–4)",
                "Highlights transparent stamp rotations, opposite die faces, folded ribbon cuts, queue positions, and bar charts.",
                "يركّز على تدوير الأختام الشفافة، أوجه حجر النرد، قص الأشرطة المطوية، ترتيب الطوابير، والتمثيل بالأعمدة.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Number Jumps, Beads & Polyominoes",
                "اختبار كانجارو التجريبي الرسمي 3 — قفزات الكنغر والخرز والتبليط (الصفان 3–4)",
                "Focuses on skip-counting jumps, repeating bead necklaces, polyomino tilings, overlapping cards, and worst-case draws.",
                "يركّز على قفزات خط الأعداد، أنماط الخرز، تبليط البوليومينو، البطاقات المتداخلة، وسحب أسوأ الحالات.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Gold Medal Dress Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية الكاملة (الصفان 3–4)",
                "Complete 75-minute, 96-point Ecolier dress rehearsal calibrated to Mawhiba Kangaroo medal cutoffs.",
                "بروفة نهائية شاملة مدتها 75 دقيقة (96 نقطة) تحاكي معايير ميداليات كانجارو موهبة للصفين الثالث والرابع.",
            ),
        ],
    },
    {
        "level": "Benjamin",
        "code": "BEN",
        "grades_en": "Benjamin · Grades 5–6",
        "grades_ar": "بنجامين · الصفان 5–6",
        "q_count": 24,
        "tier_counts": {"Easy": 8, "Medium": 8, "Hard": 8},
        "max_points": 96,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba Benjamin Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة بنجامين (الصفان 5–6)",
                "Balanced 24-question, 96-point simulation spanning divisibility, visual fractions, painted cubes, Venn diagrams, and spinners.",
                "محاكاة متوازنة من 24 سؤالاً (96 نقطة) تشمل قابلية القسمة، الكسور البصرية، المكعبات المطلية، وأشكال فن.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Matchstick Digits, Nets & Gears",
                "اختبار كانجارو التجريبي الرسمي 2 — أرقام الثقاب والشبكات والتروس (الصفان 5–6)",
                "Features 7-segment matchstick digits, cube nets, interlocking gear trains, paper-folding angles, and travel maps.",
                "يتناول الأرقام الرقمية بأعواد الثقاب، شبكات المكعب، التروس المتشابكة، زوايا طي الورق، وخرائط الطرق.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Magic Squares, Overlaps & Necklaces",
                "اختبار كانجارو التجريبي الرسمي 3 — المربعات السحرية والتداخل والعقود (الصفان 5–6)",
                "Tests 3×3 magic squares, work-backwards machines, overlapping rectangle areas, pigeonhole logic, and bead symmetry.",
                "يختبر المربعات السحرية 3×3، آلات الحل العكسي، المستطيلات المتداخلة، مبدأ برج الحمام، وتماثل العقود.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Gold Medal Dress Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية الكاملة (الصفان 5–6)",
                "Full 75-minute, 96-point Benjamin dress rehearsal engineered for Grades 5–6 Kangaroo medalists.",
                "البروفة الختامية الكاملة (24 سؤالاً في 75 دقيقة — 96 نقطة) لمسابقة كانجارو موهبة للصفين الخامس والسادس.",
            ),
        ],
    },
    {
        "level": "Cadet",
        "code": "CAD",
        "grades_en": "Cadet · Grades 7–8",
        "grades_ar": "كاديت · الصفان 7–8",
        "q_count": 30,
        "tier_counts": {"Easy": 10, "Medium": 10, "Hard": 10},
        "max_points": 120,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba Cadet Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة كاديت (الصفان 7–8)",
                "Full 30-question, 120-point Cadet simulation across prime factors, ratios, parallel zigzags, rolling dice, and knights & liars.",
                "محاكاة رسمية كاملة من 30 سؤالاً (120 نقطة) تشمل العوامل الأولية، النسب، الخطوط المتعرجة، دحرجة النرد، والصادقين والكاذبين.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Harmonic Speed, Areas & Box Nets",
                "اختبار كانجارو التجريبي الرسمي 2 — السرعة التوافقية والمساحات وشبكات الصناديق (الصفان 7–8)",
                "Highlights round-trip harmonic speed, subdivided rectangle areas, ant-on-box shortest paths, and checkerboard parity.",
                "يركّز على السرعة المتوسطة التوافقية، مساحات المستطيلات المقسمة، أقصر مسار على الصندوق، وتكافؤ رقعة الشطرنج.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Power Cycles, Semicircles & Tournaments",
                "اختبار كانجارو التجريبي الرسمي 3 — دورات الآحاد وأنصاف الدوائر والبطولات (الصفان 7–8)",
                "Focuses on last-digit power cycles, telescoping fractions, circle-in-square areas, blocked street grids, and 3-set Venn counts.",
                "يركّز على خانة الآحاد للقوى، الكسور التلسكوبية، الدوائر داخل المربعات، مسارات الشبكات، وأشكال فن الثلاثية.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Gold Medal Dress Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية الكاملة (الصفان 7–8)",
                "Complete 75-minute, 120-point Cadet dress rehearsal calibrated to Grades 7–8 Kangaroo gold medal standards.",
                "بروفة شاملة مدتها 75 دقيقة (30 سؤالاً — 120 نقطة) تحاكي المستوى الذهبي لمسابقة كانجارو للصفين السابع والثامن.",
            ),
        ],
    },
    {
        "level": "Junior",
        "code": "JUN",
        "grades_en": "Junior · Grades 9–10",
        "grades_ar": "جونيور · الصفان 9–10",
        "q_count": 30,
        "tier_counts": {"Easy": 10, "Medium": 10, "Hard": 10},
        "max_points": 120,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba Junior Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة جونيور (الصفان 9–10)",
                "Full 30-question, 120-point Junior paper covering Simon's factoring, square identities, cyclic angles, Euler polyhedra, and invariants.",
                "اختبار رسمي كامل من 30 سؤالاً (120 نقطة) يغطي التحليل الديوفانتي، المتطابقات الهندسية، الزوايا المحيطية، ومتعددات الأوجه.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Vieta Symmetry, Chords & Stars-and-Bars",
                "اختبار كانجارو التجريبي الرسمي 2 — تماثل فييتا والأوتار والنجوم والفواصل (الصفان 9–10)",
                "Features divisor counting, Vieta root sums, intersecting chords, isosceles trapezoids, and Stars-and-Bars distributions.",
                "يتناول عدد القواسم، علاقات فييتا، تقاطع الأوتار، شبه المنحرف المتطابق الساقين، وتوزيعات النجوم والفواصل.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Trailing Zeros, Scaling & Geometric Probability",
                "اختبار كانجارو التجريبي الرسمي 3 — أصفار المضروب والتشابه والاحتمال الهندسي (الصفان 9–10)",
                "Tests factorial trailing zeros, reciprocal powers, similar-triangle area ratios, Manhattan diamonds, and geometric probability.",
                "يختبر أصفار المضروب، مجاميع المقلوبات، نسب مساحات المثلثات المتشابهة، معينات الإحداثيات، والاحتمال الهندسي.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Gold Medal Dress Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية الكاملة (الصفان 9–10)",
                "High-rigor 30-question, 75-minute, 120-point Junior dress rehearsal for Grades 9–10 Kangaroo champions.",
                "البروفة الختامية الكبرى (30 سؤالاً في 75 دقيقة — 120 نقطة) لأبطال مسابقة كانجارو موهبة للصفين التاسع والعاشر.",
            ),
        ],
    },
    {
        "level": "Student",
        "code": "STU",
        "grades_en": "Student · Grades 11–12",
        "grades_ar": "ستيودنت · الصفان 11–12",
        "q_count": 30,
        "tier_counts": {"Easy": 10, "Medium": 10, "Hard": 10},
        "max_points": 120,
        "duration_minutes": 75,
        "papers": [
            (
                "Official Kangaroo Mock Paper 1 — Mawhiba Student Simulation",
                "اختبار كانجارو التجريبي الرسمي 1 — محاكاة ستيودنت (الصفان 11–12)",
                "Full 30-question, 120-point senior simulation across Euler coprimes, cubic Vieta sums, Ceva ratios, inscribed spheres, and Catalan paths.",
                "محاكاة رسمية كاملة من 30 سؤالاً (120 نقطة) تشمل الأعداد الأولية نسبياً، علاقات فييتا التكعيبية، مبرهنة سيفا، الكرات المحاطة، ومسارات كاتالان.",
            ),
            (
                "Official Kangaroo Mock Paper 2 — Frobenius Coins, Tangential Quads & Bayes Trees",
                "اختبار كانجارو التجريبي الرسمي 2 — مسألة فروبينيوس والرباعيات المماسية والاحتمال الشرطي (الصفان 11–12)",
                "Highlights Frobenius postage bounds, polynomial remainder reconstruction, Pitot tangential quads, cone frustums, and Bayes urns.",
                "يركّز على مسألة الطوابع لفروبينيوس، بواقي كثيرات الحدود، الرباعيات المماسية لبيتو، المخاريط الناقصة، والاحتمال الشرطي.",
            ),
            (
                "Official Kangaroo Mock Paper 3 — Functional Equations, Radical Tangents & Expectation",
                "اختبار كانجارو التجريبي الرسمي 3 — المعادلات الدالية والدوائر المتماسة والتوقع الرياضي (الصفان 11–12)",
                "Focuses on involutive functional equations, AM-GM extremals, common external tangents, cube cross-sections, and linearity of expectation.",
                "يركّز على المعادلات الدالية، القيم القصوى بمتباينة الوسطين، المماسات المشتركة، مقاطع المكعب، وخطية التوقع الرياضي.",
            ),
            (
                "Official Kangaroo Mock Paper 4 — Senior Gold Medal Dress Rehearsal",
                "اختبار كانجارو التجريبي الرسمي 4 — البروفة الذهبية للمرحلة الثانوية (الصفان 11–12)",
                "Championship 30-question, 75-minute, 120-point Student dress rehearsal calibrated to Grades 11–12 Kangaroo gold medal cutoffs.",
                "البروفة النهائية الكبرى (30 سؤالاً في 75 دقيقة — 120 نقطة) لأبطال الصفين الحادي عشر والثاني عشر في كانجارو موهبة.",
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


def select_four_papers_for_division(spec: dict, div_lessons: list, fresh_by_les_diff: dict) -> list:
    """Assign 4 zero-overlap papers per Division (24 Qs for ECO/BEN, 30 Qs for CAD/JUN) with balanced (A)–(E) keys."""
    n_papers = 4
    les_ids = [l["id"] for l in div_lessons]
    tiers = spec["tier_counts"]
    rng = random.Random(20261104 + hash(spec["code"]) % 997)

    if spec["q_count"] == 24:
        # 6 lessons × 4 Qs = 24 Qs (8 Easy, 8 Medium, 8 Hard) covering all 24 blueprints!
        base_patterns = [
            ["Easy", "Easy", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Hard"],
            ["Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Hard", "Hard"],
        ]
    else:
        # 6 lessons × 5 Qs = 30 Qs (10 Easy, 10 Medium, 10 Hard) covering all 24 blueprints!
        base_patterns = [
            ["Easy", "Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Medium", "Hard"],
            ["Easy", "Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Easy", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Medium", "Hard", "Hard"],
            ["Easy", "Medium", "Medium", "Hard", "Hard"],
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
                        paper_bp_counts[q["kangaroo_blueprint"]],
                        tier_ans_counts[(diff, q["correct_index"])],
                        paper_ans_counts[q["correct_index"]],
                        global_bp_usage[q["kangaroo_blueprint"]],
                        0 if q["content"]["en"].get("diagram") else 1,
                        q["id"],
                    )
                )
                chosen = candidates[0]
                used_qids.add(chosen["id"])
                paper_bp_counts[chosen["kangaroo_blueprint"]] += 1
                paper_ans_counts[chosen["correct_index"]] += 1
                tier_ans_counts[(diff, chosen["correct_index"])] += 1
                global_bp_usage[chosen["kangaroo_blueprint"]] += 1
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
        distinct_bps = len({q["kangaroo_blueprint"] for _, q in ordered_qs})
        assert distinct_bps >= 20, f"Too few blueprints ({distinct_bps}) in {spec['code']} paper {p_idx + 1}"
        ans_seq = [q["correct_index"] for _, q in ordered_qs]
        assert max_consecutive_run(ans_seq) <= 2, f"Answer run > 2 in {spec['code']} paper {p_idx + 1}: {ans_seq}"

        en_title, ar_title, en_focus, ar_focus = spec["papers"][p_idx]
        e_cnt, m_cnt, h_cnt = tiers["Easy"], tiers["Medium"], tiers["Hard"]
        svg_cnt = sum(1 for _, q in ordered_qs if q["content"]["en"].get("diagram"))
        topic_counts = dict(Counter(q["topic"] for _, q in ordered_qs))
        max_pts = e_cnt * 3 + m_cnt * 4 + h_cnt * 5
        assert max_pts == spec["max_points"]

        papers_out.append({
            "id": f"KANG-MOCK-{spec['code']}-0{p_idx + 1}",
            "track": "kangaroo",
            "option_count": 5,
            "paper_num": p_idx + 1,
            "level": spec["level"],
            "track_code": spec["code"],
            "grades_en": spec["grades_en"],
            "grades_ar": spec["grades_ar"],
            "question_count": spec["q_count"],
            "duration_minutes": spec["duration_minutes"],
            "tier_points": TIER_POINTS,
            "points_correct": 4,
            "points_wrong": 0,
            "points_blank": 0,
            "max_points": max_pts,
            "svg_count": svg_cnt,
            "topic_counts": topic_counts,
            "sections": [
                {
                    "id": "A",
                    "difficulty": "Easy",
                    "points_each": 3,
                    "start_q": 1,
                    "end_q": e_cnt,
                    "en": f"Part A — 3-Point Problems (Questions 1–{e_cnt})",
                    "ar": f"الجزء الأول (A) — مسائل الـ 3 نقاط (الأسئلة 1–{e_cnt})",
                },
                {
                    "id": "B",
                    "difficulty": "Medium",
                    "points_each": 4,
                    "start_q": e_cnt + 1,
                    "end_q": e_cnt + m_cnt,
                    "en": f"Part B — 4-Point Problems (Questions {e_cnt + 1}–{e_cnt + m_cnt})",
                    "ar": f"الجزء الثاني (B) — مسائل الـ 4 نقاط (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})",
                },
                {
                    "id": "C",
                    "difficulty": "Hard",
                    "points_each": 5,
                    "start_q": e_cnt + m_cnt + 1,
                    "end_q": e_cnt + m_cnt + h_cnt,
                    "en": f"Part C — 5-Point Problems (Questions {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                    "ar": f"الجزء الثالث (C) — مسائل الـ 5 نقاط (الأسئلة {e_cnt + m_cnt + 1}–{e_cnt + m_cnt + h_cnt})",
                },
            ],
            "en": {"title": en_title, "focus": en_focus},
            "ar": {"title": ar_title, "focus": ar_focus},
            "question_ids": [q["id"] for _, q in ordered_qs],
            "question_lessons": {q["id"]: lid for lid, q in ordered_qs},
        })

    return papers_out


def main() -> None:
    bank = json.loads((ROOT / "data" / "kangaroo.json").read_text(encoding="utf-8"))
    lessons = json.loads((ROOT / "data" / "kangaroo_lessons.json").read_text(encoding="utf-8"))["lessons"]

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
        lid = bp_to_lesson.get(q["kangaroo_blueprint"])
        assert lid, f"Unmapped Kangaroo blueprint {q['kangaroo_blueprint']}"
        fresh_by_les_diff[(lid, q["difficulty"])].append(q)

    all_papers = []
    global_mock_qids: set[str] = set()
    for spec in DIVISION_SPECS:
        div_lessons = [l for l in lessons if l["level"] == spec["level"]]
        assert len(div_lessons) == 6
        papers = select_four_papers_for_division(spec, div_lessons, fresh_by_les_diff)
        for p in papers:
            for qid in p["question_ids"]:
                assert qid in bank_by_id
                assert qid not in reserved_ids, f"Overlap with Kangaroo lesson example/drill: {qid}"
                assert qid not in global_mock_qids, f"Duplicate question across Kangaroo mock papers: {qid}"
                global_mock_qids.add(qid)
        all_papers.extend(papers)

    out = {
        "academy_en": "Edugates International School",
        "academy_ar": "مدرسة بوابة المعرفة العالمية",
        "competition_en": "Kangaroo Math Competition (Mawhiba / KSF) — Official Simulation Series (Grades 1–12)",
        "competition_ar": "مسابقة كانجارو موهبة للرياضيات — سلسلة الاختبارات التجريبية الرسمية (الصفوف 1–12)",
        "default_paper": "A4",
        "option_count": 5,
        "scoring": {
            "part_a_easy": 3,
            "part_b_medium": 4,
            "part_c_hard": 5,
            "wrong": 0,
            "blank": 0,
            "calculator_allowed": False,
        },
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": all_papers,
    }

    out_path = ROOT / "data" / "kangaroo_mocks.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_svgs = sum(p["svg_count"] for p in all_papers)
    print(
        f"SUCCESS: Wrote {len(all_papers)} official Kangaroo mock papers ({len(global_mock_qids)} unique zero-overlap questions, "
        f"{total_svgs} SVG diagrams) to {out_path}"
    )


if __name__ == "__main__":
    main()

