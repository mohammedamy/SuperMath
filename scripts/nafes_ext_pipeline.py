"""Shared lesson-bank linking and official mock compilation helpers for Nafes Science & English."""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from audit_banks import norm


def attach_bank_ids_and_validate_lessons(
    lessons: list[dict], bank_path: Path, bp_key: str, out_path: Path
) -> None:
    """Select 6 bank_example_ids + 6 disjoint drill_ids per lesson, validate invariants, and write JSON."""
    bank = json.loads(bank_path.read_text("utf-8"))
    bank_stems = {norm(q["content"]["en"]["question"]) for q in bank}

    by_bp_diff: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for q in sorted(bank, key=lambda x: x["id"]):
        by_bp_diff[(q[bp_key], q["difficulty"])].append(q)

    global_used: set[str] = set()
    for les in lessons:
        bps = les["blueprints"]
        assert len(bps) == 4, f"Expected 4 blueprints on {les['id']}, got {len(bps)}"

        bank_ex_ids: list[str] = []
        drill_ids: list[str] = []

        # Pick 2 Easy, 2 Medium, 2 Hard for bank_example_ids, then 2E+2M+2H disjoint for drill_ids
        for diff in ("Easy", "Medium", "Hard"):
            cands: list[dict] = []
            max_len = max((len(by_bp_diff[(bp, diff)]) for bp in bps), default=0)
            for slot in range(max_len):
                for bp in bps:
                    bucket = by_bp_diff[(bp, diff)]
                    if slot < len(bucket):
                        q = bucket[slot]
                        if q["id"] not in global_used:
                            cands.append(q)
            assert len(cands) >= 4, f"{les['id']} ({bps}) has only {len(cands)} unused {diff} Qs"
            chosen_ex = cands[:2]
            chosen_dr = cands[2:4]
            for q in chosen_ex:
                bank_ex_ids.append(q["id"])
                global_used.add(q["id"])
            for q in chosen_dr:
                drill_ids.append(q["id"])
                global_used.add(q["id"])

        assert len(bank_ex_ids) == 6 and len(drill_ids) == 6
        assert set(bank_ex_ids).isdisjoint(drill_ids)
        les["bank_example_ids"] = bank_ex_ids
        les["drill_ids"] = drill_ids

        # Structural validation mirroring test-runtime.cjs
        for lang in ("en", "ar"):
            blk = les[lang]
            assert len(blk["concepts"]) >= 3, f"{les['id']} needs >=3 concepts"
            for ci, c in enumerate(blk["concepts"]):
                assert "<svg" in c.get("diagram", ""), f"{les['id']} concept {ci} missing SVG"
            assert len(blk["cheat_sheet"]) == 4, f"{les['id']} needs 4 cheat_sheet items"
            assert len(blk["examples"]) >= 4, f"{les['id']} needs >=4 worked examples"
            for ex in blk["examples"]:
                assert "<svg" in ex.get("diagram", ""), f"{les['id']} example {ex['id']} missing SVG"
                assert len(ex.get("options", [])) == 4, f"{les['id']} example {ex['id']} needs 4 options"
                if lang == "en":
                    assert norm(ex["question"]) not in bank_stems, (
                        f"{les['id']} example {ex['id']} collides with bank stem"
                    )
            def _chk(x):
                if isinstance(x, str):
                    assert "**" not in x, f"Raw ** in {les['id']}"
                    assert "\\\\(" not in x, f"Double-escaped \\\\( in {les['id']}"
                elif isinstance(x, list):
                    for item in x:
                        _chk(item)
                elif isinstance(x, dict):
                    for item in x.values():
                        _chk(item)
            _chk(blk)

    out_path.write_text(json.dumps({"lessons": lessons}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(lessons)} lessons ({len(global_used)} bank/drill IDs) -> {out_path}")


def _order_with_no_long_runs(qs: list[dict]) -> list[dict]:
    """Order Easy -> Medium -> Hard and guarantee no 3 consecutive identical correct_index values."""
    ordered: list[dict] = []
    for diff in ("Easy", "Medium", "Hard"):
        bucket = sorted((q for q in qs if q["difficulty"] == diff), key=lambda q: q["id"])
        while bucket:
            ban = (
                ordered[-1]["correct_index"]
                if len(ordered) >= 2 and ordered[-1]["correct_index"] == ordered[-2]["correct_index"]
                else None
            )
            counts = Counter(q["correct_index"] for q in bucket)
            cands = [i for i, q in enumerate(bucket) if q["correct_index"] != ban]
            if not cands:
                cands = list(range(len(bucket)))
            # Pick the eligible item whose answer index is most frequent remaining in this difficulty band
            picked_idx = max(cands, key=lambda i: (counts[bucket[i]["correct_index"]], -i))
            ordered.append(bucket.pop(picked_idx))

    # Repair any boundary/tail triple run within the same difficulty band (or anywhere if needed)
    for _ in range(len(ordered) * 2):
        bad = next(
            (i for i in range(len(ordered) - 2)
             if ordered[i]["correct_index"] == ordered[i + 1]["correct_index"] == ordered[i + 2]["correct_index"]),
            None,
        )
        if bad is None:
            break
        diff_i = ordered[bad + 2]["difficulty"]
        swapped = False
        for j in range(len(ordered)):
            if abs(j - (bad + 2)) <= 1 or ordered[j]["difficulty"] != diff_i:
                continue
            cand = list(ordered)
            cand[bad + 2], cand[j] = cand[j], cand[bad + 2]
            if not any(
                cand[k]["correct_index"] == cand[k + 1]["correct_index"] == cand[k + 2]["correct_index"]
                for k in range(len(cand) - 2)
            ):
                ordered = cand
                swapped = True
                break
        if not swapped:
            for j in range(len(ordered)):
                if abs(j - (bad + 1)) <= 1:
                    continue
                cand = list(ordered)
                cand[bad + 1], cand[j] = cand[j], cand[bad + 1]
                if not any(
                    cand[k]["correct_index"] == cand[k + 1]["correct_index"] == cand[k + 2]["correct_index"]
                    for k in range(len(cand) - 2)
                ):
                    ordered = cand
                    break
    return ordered


def build_ext_mocks(
    competition_name: str,
    track: str,
    bank_path: Path,
    lessons_path: Path,
    out_path: Path,
    bp_key: str,
    grade_specs: list[dict],
) -> None:
    """Compile balanced, zero-lesson-overlap official mock papers for Nafes Science or English."""
    bank = json.loads(bank_path.read_text("utf-8"))
    lessons = json.loads(lessons_path.read_text("utf-8"))["lessons"]

    bp_to_lesson: dict[str, str] = {}
    lesson_used: set[str] = set()
    for les in lessons:
        for bp in les["blueprints"]:
            bp_to_lesson[bp] = les["id"]
        lesson_used.update(les["bank_example_ids"])
        lesson_used.update(les["drill_ids"])

    mocks: list[dict] = []
    for spec in grade_specs:
        level = spec["level"]
        q_count = spec["question_count"]
        dur = spec["duration_minutes"]
        diff_targets: dict[str, int] = spec["diff_targets"]
        topics: list[str] = spec["topics"]
        assert sum(diff_targets.values()) == q_count

        pool = [
            q for q in sorted(bank, key=lambda x: x["id"])
            if q["level"] == level and q["id"] not in lesson_used
        ]
        # Build per-(topic, diff) round-robin queues across blueprints
        grade_used: set[str] = set()
        for p_idx, meta in enumerate(spec["papers_meta"], start=1):
            # Target topic counts for balanced paper across the 4 topics
            base_t, rem_t = divmod(q_count, len(topics))
            topic_quota = {
                t: base_t + (1 if ((i + p_idx - 1) % len(topics)) < rem_t else 0)
                for i, t in enumerate(topics)
            }
            diff_rem = dict(diff_targets)
            selected: list[dict] = []

            # Multi-pass selection: pair topics with needed difficulties while stepping across blueprints
            available = [q for q in pool if q["id"] not in grade_used]
            # Spread selection across offsets so each paper gets distinct blueprint slices
            by_bp: dict[str, list[dict]] = defaultdict(list)
            for q in available:
                by_bp[q[bp_key]].append(q)
            interleaved: list[dict] = []
            max_b = max((len(v) for v in by_bp.values()), default=0)
            bp_keys = sorted(by_bp.keys())
            for r in range(max_b):
                for bk in bp_keys:
                    if r < len(by_bp[bk]):
                        interleaved.append(by_bp[bk][r])

            for q in interleaved:
                t = q["topic"]
                d = q["difficulty"]
                if topic_quota.get(t, 0) > 0 and diff_rem.get(d, 0) > 0:
                    selected.append(q)
                    topic_quota[t] -= 1
                    diff_rem[d] -= 1
                    grade_used.add(q["id"])
                if len(selected) == q_count:
                    break

            # Fallback fill if exact (topic, diff) pairing left residual quota
            if len(selected) < q_count:
                for q in interleaved:
                    if q["id"] in grade_used:
                        continue
                    d = q["difficulty"]
                    if diff_rem.get(d, 0) > 0:
                        selected.append(q)
                        diff_rem[d] -= 1
                        grade_used.add(q["id"])
                    if len(selected) == q_count:
                        break

            assert len(selected) == q_count, f"{meta['id']} got {len(selected)}/{q_count} Qs"
            ordered = _order_with_no_long_runs(selected)

            for i in range(len(ordered) - 2):
                a, b, c = ordered[i]["correct_index"], ordered[i + 1]["correct_index"], ordered[i + 2]["correct_index"]
                assert not (a == b == c), f"Run of 3 identical answers in {meta['id']}"

            qids = [q["id"] for q in ordered]
            assert set(qids).isdisjoint(lesson_used), f"{meta['id']} overlaps lesson_used"
            svg_cnt = sum(1 for q in ordered if q["content"]["en"].get("diagram"))
            topic_counts = dict(Counter(q["topic"] for q in ordered))
            question_lessons = {
                q["id"]: bp_to_lesson[q[bp_key]]
                for q in ordered
                if q.get(bp_key) in bp_to_lesson
            }
            e_cnt = diff_targets["Easy"]
            m_cnt = diff_targets["Medium"]
            is_sci = track == "nafes_science"
            sections = [
                {
                    "id": "A",
                    "difficulty": "Easy",
                    "start_q": 1,
                    "end_q": e_cnt,
                    "en": (
                        f"Part A — Scientific Knowledge & Recall (Questions 1–{e_cnt})"
                        if is_sci
                        else f"Part A — Literal Comprehension & Core Usage (Questions 1–{e_cnt})"
                    ),
                    "ar": (
                        f"الجزء الأول (A) — المعرفة والاستدعاء العلمي (الأسئلة 1–{e_cnt})"
                        if is_sci
                        else f"الجزء الأول (A) — الفهم الحرفي والاستخدام الأساسي (الأسئلة 1–{e_cnt})"
                    ),
                },
                {
                    "id": "B",
                    "difficulty": "Medium",
                    "start_q": e_cnt + 1,
                    "end_q": e_cnt + m_cnt,
                    "en": (
                        f"Part B — Scientific Application & Inquiry (Questions {e_cnt + 1}–{e_cnt + m_cnt})"
                        if is_sci
                        else f"Part B — Context Clues & Sentence Structure (Questions {e_cnt + 1}–{e_cnt + m_cnt})"
                    ),
                    "ar": (
                        f"الجزء الثاني (B) — التطبيق والاستقصاء العلمي (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})"
                        if is_sci
                        else f"الجزء الثاني (B) — دلالات السياق وبنية الجملة (الأسئلة {e_cnt + 1}–{e_cnt + m_cnt})"
                    ),
                },
                {
                    "id": "C",
                    "difficulty": "Hard",
                    "start_q": e_cnt + m_cnt + 1,
                    "end_q": q_count,
                    "en": (
                        f"Part C — Scientific Reasoning & Analysis (Questions {e_cnt + m_cnt + 1}–{q_count})"
                        if is_sci
                        else f"Part C — Inference, Purpose & Textual Reasoning (Questions {e_cnt + m_cnt + 1}–{q_count})"
                    ),
                    "ar": (
                        f"الجزء الثالث (C) — الاستدلال العلمي وتحليل الأدلة (الأسئلة {e_cnt + m_cnt + 1}–{q_count})"
                        if is_sci
                        else f"الجزء الثالث (C) — الاستنتاج وتحليل الغرض والاستدلال النصي (الأسئلة {e_cnt + m_cnt + 1}–{q_count})"
                    ),
                },
            ]

            mocks.append({
                "id": meta["id"],
                "track": track,
                "level": level,
                "paper_num": p_idx,
                "duration_minutes": dur,
                "question_count": q_count,
                "option_count": 4,
                "points_correct": 1,
                "points_wrong": 0,
                "points_blank": 0,
                "max_points": q_count,
                "grades_en": spec["grades_en"],
                "grades_ar": spec["grades_ar"],
                "topic_counts": topic_counts,
                "sections": sections,
                "en": {"title": meta["title_en"], "focus": meta["subtitle_en"], "subtitle": meta["subtitle_en"]},
                "ar": {"title": meta["title_ar"], "focus": meta["subtitle_ar"], "subtitle": meta["subtitle_ar"]},
                "question_ids": qids,
                "question_lessons": question_lessons,
                "svg_count": svg_cnt,
            })

    payload = {
        "competition": competition_name,
        "blueprint_to_lesson": bp_to_lesson,
        "mocks": mocks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(mocks)} official mocks -> {out_path}")
