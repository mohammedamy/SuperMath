"""Compile 12 Official ETEC Nafes English Timed Mock Papers (Grades 3, 6 & 9) -> data/nafes_english_mocks.json."""
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from nafes_ext_common import NAFS_ENG_TOPICS
from nafes_ext_pipeline import build_ext_mocks


GRADE_SPECS = [
    {
        "level": "English · Grade 3",
        "question_count": 20,
        "duration_minutes": 45,
        "diff_targets": {"Easy": 7, "Medium": 7, "Hard": 6},
        "topics": list(NAFS_ENG_TOPICS),
        "grades_en": "Grade 3 (Primary National English · CEFR A1)",
        "grades_ar": "الصف الثالث الابتدائي (نافس اللغة الإنجليزية · مستوى A1)",
        "papers_meta": [
            {
                "id": "NAFS-ENG-MOCK-G3-01",
                "title_en": "Official Nafes English Mock 1 — Grade 3 National Simulation",
                "subtitle_en": "Balanced 20-question, 45-minute CEFR A1 simulation spanning Reading, Signs, Sight Words, and Core Grammar.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 1 — محاكاة الصف الثالث الابتدائي",
                "subtitle_ar": "محاكاة متوازنة من 20 سؤالاً (45 دقيقة) للقراءة واللافتات والمفردات والقواعد الأساسية.",
            },
            {
                "id": "NAFS-ENG-MOCK-G3-02",
                "title_en": "Official Nafes English Mock 2 — Grade 3 Stories & Signs Focus",
                "subtitle_en": "20 fresh Grade 3 questions (45 min) on short notices, picture sequences, context clues, and plurals.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 2 — القصص والإعلانات (ثالث ابتدائي)",
                "subtitle_ar": "20 سؤالاً جديداً (45 دقيقة) في فهم الإعلانات وتسلسل الأحداث وسياق المفردات والجمع.",
            },
            {
                "id": "NAFS-ENG-MOCK-G3-03",
                "title_en": "Official Nafes English Mock 3 — Grade 3 Comprehension & Clarity",
                "subtitle_en": "20 unseen Grade 3 items (45 min) testing pronoun clues, speaker intent, opposites, and present forms.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 3 — الفهم والوضوح اللغوي (ثالث ابتدائي)",
                "subtitle_ar": "20 سؤالاً غير مكرر (45 دقيقة) في مرجعية الضمائر وقصد المتحدث والأضداد والمضارع.",
            },
            {
                "id": "NAFS-ENG-MOCK-G3-04",
                "title_en": "Official Nafes English Mock 4 — Grade 3 Final Benchmark",
                "subtitle_en": "Capstone 20-question, 45-minute ETEC Grade 3 English assessment matching full blueprint balance.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 4 — الاختبار الختامي الشامل (ثالث)",
                "subtitle_ar": "نموذج محاكاة ختامي من 20 سؤالاً (45 دقيقة) يغطي كامل مواصفات نافس للغة الإنجليزية.",
            },
        ],
    },
    {
        "level": "English · Grade 6",
        "question_count": 25,
        "duration_minutes": 60,
        "diff_targets": {"Easy": 9, "Medium": 9, "Hard": 7},
        "topics": list(NAFS_ENG_TOPICS),
        "grades_en": "Grade 6 (Upper Primary National English · CEFR A2)",
        "grades_ar": "الصف السادس الابتدائي (نافس اللغة الإنجليزية · مستوى A2)",
        "papers_meta": [
            {
                "id": "NAFS-ENG-MOCK-G6-01",
                "title_en": "Official Nafes English Mock 1 — Grade 6 National Simulation",
                "subtitle_en": "Balanced 25-question, 60-minute CEFR A2 simulation covering Informational Texts, Inference, Morphology, and Syntax.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 1 — محاكاة الصف السادس الابتدائي",
                "subtitle_ar": "محاكاة من 25 سؤالاً (60 دقيقة) لنصوص المعلومات والاستنتاج وبنية الكلمة والنحو.",
            },
            {
                "id": "NAFS-ENG-MOCK-G6-02",
                "title_en": "Official Nafes English Mock 2 — Grade 6 Purpose & Schedules Focus",
                "subtitle_en": "25 fresh Grade 6 questions (60 min) integrating schedules, author purpose, prefixes/suffixes, and modals.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 2 — الجداول وغرض الكاتب (سادس)",
                "subtitle_ar": "25 سؤالاً جديداً (60 دقيقة) في قراءة الجداول وغرض الكاتب والسوابق والأفعال الناقصة.",
            },
            {
                "id": "NAFS-ENG-MOCK-G6-03",
                "title_en": "Official Nafes English Mock 3 — Grade 6 Critical Reading",
                "subtitle_en": "25 unseen Grade 6 items (60 min) assessing cause-effect, fact vs. opinion, collocations, and comparatives.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 3 — القراءة الناقدة والسياق (سادس)",
                "subtitle_ar": "25 سؤالاً غير مكرر (60 دقيقة) في السبب والنتيجة والحقيقة والرأي والمقارنة.",
            },
            {
                "id": "NAFS-ENG-MOCK-G6-04",
                "title_en": "Official Nafes English Mock 4 — Grade 6 Final Benchmark",
                "subtitle_en": "Capstone 25-question, 60-minute ETEC Grade 6 English benchmark exam.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 4 — الاختبار الختامي الشامل (سادس)",
                "subtitle_ar": "نموذج محاكاة ختامي من 25 سؤالاً (60 دقيقة) وفق مواصفات نافس للغة الإنجليزية.",
            },
        ],
    },
    {
        "level": "English · Grade 9",
        "question_count": 30,
        "duration_minutes": 75,
        "diff_targets": {"Easy": 10, "Medium": 11, "Hard": 9},
        "topics": list(NAFS_ENG_TOPICS),
        "grades_en": "Grade 9 (Intermediate National English · CEFR B1)",
        "grades_ar": "الصف الثالث المتوسط (نافس اللغة الإنجليزية · مستوى B1)",
        "papers_meta": [
            {
                "id": "NAFS-ENG-MOCK-G9-01",
                "title_en": "Official Nafes English Mock 1 — Grade 9 National Simulation",
                "subtitle_en": "Balanced 30-question, 75-minute CEFR B1 simulation spanning Academic Passages, Rhetoric, Lexis, and Clauses.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 1 — محاكاة الصف الثالث المتوسط",
                "subtitle_ar": "محاكاة من 30 سؤالاً (75 دقيقة) في النصوص الأكاديمية والبلاغة والمفردات والتراكيب.",
            },
            {
                "id": "NAFS-ENG-MOCK-G9-02",
                "title_en": "Official Nafes English Mock 2 — Grade 9 Discourse & Argument",
                "subtitle_en": "30 fresh Grade 9 questions (75 min) testing synthesis, tone/claim evidence, academic roots, and conditionals.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 2 — تحليل الخطاب والحجج (ثالث متوسط)",
                "subtitle_ar": "30 سؤالاً جديداً (75 دقيقة) في تركيب المعلومات والنبرة والجذور والجمل الشرطية.",
            },
            {
                "id": "NAFS-ENG-MOCK-G9-03",
                "title_en": "Official Nafes English Mock 3 — Grade 9 Analytical Mastery",
                "subtitle_en": "30 unseen Grade 9 items (75 min) covering passive voice, relative clauses, idioms, and paired data texts.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 3 — الإتقان التحليلي (ثالث متوسط)",
                "subtitle_ar": "30 سؤالاً غير مكرر (75 دقيقة) في المبني للمجهول وجمل الوصل والتعابير والبيانات.",
            },
            {
                "id": "NAFS-ENG-MOCK-G9-04",
                "title_en": "Official Nafes English Mock 4 — Grade 9 Final Benchmark",
                "subtitle_en": "Capstone 30-question, 75-minute ETEC Grade 9 English official readiness exam.",
                "title_ar": "اختبار نافس إنجليزي التجريبي 4 — الاختبار الختامي الشامل (ثالث متوسط)",
                "subtitle_ar": "نموذج محاكاة ختامي من 30 سؤالاً (75 دقيقة) لقياس الجاهزية الكاملة لاختبار نافس.",
            },
        ],
    },
]


def main() -> None:
    build_ext_mocks(
        competition_name="ETEC Nafes KSA National English Assessment (Grades 3, 6 & 9)",
        track="nafes_english",
        bank_path=ROOT / "data" / "nafes_english.json",
        lessons_path=ROOT / "data" / "nafes_english_lessons.json",
        out_path=ROOT / "data" / "nafes_english_mocks.json",
        bp_key="nafes_english_blueprint",
        grade_specs=GRADE_SPECS,
    )


if __name__ == "__main__":
    main()
