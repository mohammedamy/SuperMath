"""Compile 8 Official ETEC Nafes Science Timed Mock Papers (Grades 6 & 9) -> data/nafes_science_mocks.json."""
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from nafes_ext_common import NAFS_SCI_TOPICS
from nafes_ext_pipeline import build_ext_mocks


GRADE_SPECS = [
    {
        "level": "Science · Grade 6",
        "question_count": 25,
        "duration_minutes": 60,
        "diff_targets": {"Easy": 9, "Medium": 9, "Hard": 7},
        "topics": list(NAFS_SCI_TOPICS),
        "grades_en": "Grade 6 (Upper Primary National Science)",
        "grades_ar": "الصف السادس الابتدائي (اختبار نافس الوطني للعلوم)",
        "papers_meta": [
            {
                "id": "NAFS-SCI-MOCK-G6-01",
                "title_en": "Official Nafes Science Mock 1 — Grade 6 National Simulation",
                "subtitle_en": "Balanced 25-question, 60-minute Grade 6 simulation spanning Cells, Matter, Forces, and Earth Systems.",
                "title_ar": "اختبار نافس علوم التجريبي 1 — محاكاة الصف السادس الابتدائي",
                "subtitle_ar": "محاكاة متوازنة من 25 سؤالاً (60 دقيقة) في الخلايا والمادة والقوى والأرض والفضاء.",
            },
            {
                "id": "NAFS-SCI-MOCK-G6-02",
                "title_en": "Official Nafes Science Mock 2 — Grade 6 Inquiry & Energy Focus",
                "subtitle_en": "25 fresh Grade 6 questions (60 min) testing Ecosystems, Mixtures, Electrical Circuits, and Weather.",
                "title_ar": "اختبار نافس علوم التجريبي 2 — الاستقصاء العلمي والطاقة (سادس)",
                "subtitle_ar": "25 سؤالاً جديداً (60 دقيقة) تغطي الأنظمة البيئية والمخاليط والدوائر الكهربائية والطقس.",
            },
            {
                "id": "NAFS-SCI-MOCK-G6-03",
                "title_en": "Official Nafes Science Mock 3 — Grade 6 Scientific Reasoning",
                "subtitle_en": "25 unseen Grade 6 items (60 min) emphasizing data tables, experimental controls, and physical models.",
                "title_ar": "اختبار نافس علوم التجريبي 3 — الاستدلال العلمي والبيانات (سادس)",
                "subtitle_ar": "25 سؤالاً غير مكرر (60 دقيقة) تركز على الجداول وضوابط التجربة والنماذج الفيزيائية.",
            },
            {
                "id": "NAFS-SCI-MOCK-G6-04",
                "title_en": "Official Nafes Science Mock 4 — Grade 6 Final Benchmark",
                "subtitle_en": "Capstone 25-question, 60-minute ETEC Nafes Science simulation across Knowing, Applying, and Reasoning.",
                "title_ar": "اختبار نافس علوم التجريبي 4 — الاختبار الختامي الشامل (سادس)",
                "subtitle_ar": "نموذج محاكاة ختامي من 25 سؤالاً (60 دقيقة) عبر مهارات المعرفة والتطبيق والاستدلال.",
            },
        ],
    },
    {
        "level": "Science · Grade 9",
        "question_count": 30,
        "duration_minutes": 75,
        "diff_targets": {"Easy": 10, "Medium": 11, "Hard": 9},
        "topics": list(NAFS_SCI_TOPICS),
        "grades_en": "Grade 9 (Intermediate National Science)",
        "grades_ar": "الصف الثالث المتوسط (اختبار نافس الوطني للعلوم)",
        "papers_meta": [
            {
                "id": "NAFS-SCI-MOCK-G9-01",
                "title_en": "Official Nafes Science Mock 1 — Grade 9 National Simulation",
                "subtitle_en": "Balanced 30-question, 75-minute Grade 9 ETEC simulation across Genetics, Reactions, Mechanics, and Plates.",
                "title_ar": "اختبار نافس علوم التجريبي 1 — محاكاة الصف الثالث المتوسط",
                "subtitle_ar": "محاكاة رسمية من 30 سؤالاً (75 دقيقة) في الوراثة والتفاعلات والميكانيكا والصفائح الأرضية.",
            },
            {
                "id": "NAFS-SCI-MOCK-G9-02",
                "title_en": "Official Nafes Science Mock 2 — Grade 9 Quantitative Science",
                "subtitle_en": "30 fresh Grade 9 questions (75 min) testing Stoichiometry, Ohm's Law, Energy Conservation, and Waves.",
                "title_ar": "اختبار نافس علوم التجريبي 2 — العلوم الكمية والقوانين (ثالث متوسط)",
                "subtitle_ar": "30 سؤالاً جديداً (75 دقيقة) في الحسابات الكيميائية وقانون أوم وحفظ الطاقة والموجات.",
            },
            {
                "id": "NAFS-SCI-MOCK-G9-03",
                "title_en": "Official Nafes Science Mock 3 — Grade 9 Lab & Systems Analysis",
                "subtitle_en": "30 unseen Grade 9 items (75 min) assessing pH curves, motion graphs, homeostasis, and planetary cycles.",
                "title_ar": "اختبار نافس علوم التجريبي 3 — تحليل التجارب والأنظمة (ثالث متوسط)",
                "subtitle_ar": "30 سؤالاً غير مكرر (75 دقيقة) في منحنيات الحموضة والرسوم البيانية والاتزان الداخلي.",
            },
            {
                "id": "NAFS-SCI-MOCK-G9-04",
                "title_en": "Official Nafes Science Mock 4 — Grade 9 Final Benchmark",
                "subtitle_en": "Capstone 30-question, 75-minute ETEC Nafes Science simulation with full STEM reasoning balance.",
                "title_ar": "اختبار نافس علوم التجريبي 4 — الاختبار الختامي الشامل (ثالث متوسط)",
                "subtitle_ar": "نموذج محاكاة ختامي من 30 سؤالاً (75 دقيقة) يغطي كامل مواصفات نافس للعلوم.",
            },
        ],
    },
]


def main() -> None:
    build_ext_mocks(
        competition_name="ETEC Nafes KSA National Science Assessment (Grades 6 & 9)",
        track="nafes_science",
        bank_path=ROOT / "data" / "nafes_science.json",
        lessons_path=ROOT / "data" / "nafes_science_lessons.json",
        out_path=ROOT / "data" / "nafes_science_mocks.json",
        bp_key="nafes_science_blueprint",
        grade_specs=GRADE_SPECS,
    )


if __name__ == "__main__":
    main()
