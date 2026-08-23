import json
import os
import time
from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPENROUTER_API_KEY")
)

# Define the target paths
DATA_DIR = "data"
GRADES = {
    "Grade 3": "Basic arithmetic, simple geometry, logical reasoning, patterns. 4-option MCQs. Language must be simple.",
    "Grade 6": "Fractions, decimals, percentages, basic algebra, data analysis, 2D geometry. 4-option MCQs.",
    "Grade 9": "Algebra, linear equations, geometry (triangles, circles), probability. 4-option MCQs. Advanced logical thinking."
}

QUESTIONS_PER_BATCH = 20
TOTAL_PER_GRADE = 250

def generate_batch(grade_level, description, existing_count):
    prompt = f"""
    Generate a batch of {QUESTIONS_PER_BATCH} highly challenging and unique math questions for the Nafes KSA track.
    Target Audience/Level: {grade_level}
    Characteristics: {description}
    
    Requirements:
    1. Provide the content in both English and Arabic.
    2. ABSOLUTELY STRICT LATEX RULE: Every single number, variable, formula, and equation MUST be wrapped in LaTeX delimiters. Use \\( x^2 \\) for inline math, and $$ \\sum x $$ for block math. Do NOT write "2x + 3" as plain text. It MUST be "\\( 2x + 3 \\)". Even isolated numbers like "5" must be "\\( 5 \\)".
    3. The Arabic translation must be grammatically correct and use standard Arabic mathematical terminology (specifically for the Saudi curriculum).
    4. For MCQs, provide exactly 4 options.
    5. The 'id' should follow the format NAFES-{grade_level[-1]}-{(existing_count+1):03d} onwards.
    
    CRITICAL VISUAL REQUIREMENT:
    To match the real papers flavor, AT LEAST 8 questions in this batch MUST include high-quality visual elements within the `question` text (both English and Arabic). 
    - Use HTML `<table>` for data tables (add Tailwind classes like `w-full text-center border-collapse border border-slate-700`).
    - Use inline `<svg>` for geometry diagrams, charts, and graphs. Ensure SVGs are responsive (e.g. `viewBox="0 0 200 200" class="w-full max-w-xs mx-auto bg-white rounded-lg p-2"`), use standard stroke/fill colors, and are completely valid XML without markdown code blocks.
    Do NOT just provide text. You must actively generate tables and SVG shapes representing triangles, circles, coordinate planes, or bar charts directly inside the JSON string where appropriate.
    
    CRITICAL REQUIREMENT:
    All generated questions MUST closely mimic the ACTUAL PAST PAPERS of the Nafes competition for {grade_level}.
    Match the exact style, rigor, formatting, tone, and typical mathematical depth found in the real exams.
    
    OUTPUT FORMAT:
    You must output ONLY a valid JSON object containing a single key "questions" whose value is an array of the {QUESTIONS_PER_BATCH} question objects.
    
    Each question object must strictly follow this exact schema:
    {{
        "id": "NAFES-{grade_level[-1]}-001",
        "track": "nafes",
        "level": "{grade_level}",
        "topic": "Topic Name",
        "type": "MCQ", 
        "difficulty": "hard",
        "content": {{
            "en": {{
                "question": "English question text",
                "options": ["A", "B", "C", "D"], 
                "hint": "English hint",
                "explanation": "English explanation"
            }},
            "ar": {{
                "question": "Arabic question text",
                "options": ["A", "B", "C", "D"], 
                "hint": "Arabic hint",
                "explanation": "Arabic explanation"
            }}
        }},
        "correct_index": "0" 
    }}
    """
    
    print(f"Generating batch for Nafes {grade_level} (Questions {existing_count+1} to {existing_count+QUESTIONS_PER_BATCH})...", flush=True)
    
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.7
    )
    
    content = response.choices[0].message.content
    return json.loads(content)["questions"]

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    file_path = os.path.join(DATA_DIR, "nafes.json")
    
    questions = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                old_questions = json.load(f)
                # Keep only questions that match exactly "Grade 3", "Grade 6", or "Grade 9" 
                # (to discard the old mixed ones that had "Grades 3, 6, 9")
                questions = [q for q in old_questions if q.get("level") in GRADES.keys()]
            except:
                questions = []
                
    for grade_level, description in GRADES.items():
        grade_questions = [q for q in questions if q.get("level") == grade_level]
        current_count = len(grade_questions)
        
        print(f"[Nafes {grade_level}] Currently has {current_count} questions.", flush=True)
        
        while current_count < TOTAL_PER_GRADE:
            try:
                new_batch = generate_batch(grade_level, description, current_count)
                for q in new_batch:
                    q["level"] = grade_level
                    
                grade_questions.extend(new_batch)
                questions.extend(new_batch)
                current_count = len(grade_questions)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(questions, f, ensure_ascii=False, indent=2)
                
                print(f"[Nafes {grade_level}] Successfully added batch. Total now: {current_count}/{TOTAL_PER_GRADE}", flush=True)
                time.sleep(1)
            except Exception as e:
                print(f"Error generating batch: {e}", flush=True)
                time.sleep(5)
                
    print(f"Reached target! Pushing to GitHub...", flush=True)
    os.system(f"git add {file_path} && git commit -m 'Auto-push Nafes updated (750 questions total)' && git push origin main")

if __name__ == "__main__":
    print("Starting Nafes Grade-Specific Generation...", flush=True)
    main()
    print("Finished generating Nafes database!", flush=True)
