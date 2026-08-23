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
TRACKS = {
    "kangaroo": {"level": "Middle School", "description": "Logical puzzles, spatial reasoning, visual geometry, 4-5 option MCQs."},
    "nafes": {"level": "Grades 3, 6, 9", "description": "Standard Saudi curriculum (algebra, geometry, data analysis). 4-option MCQs."},
    "jee": {"level": "High School (Grade 12)", "description": "Advanced calculus, complex numbers, coordinate geometry. Highly rigorous."},
    "olympiad": {"level": "High School", "description": "Number theory, combinatorics, functional equations. Rigorous mathematical proofs (FRQ)."},
    "kaust": {"level": "High School (Gifted)", "description": "Applied math, logical deduction, discrete mathematics. Mix of MCQ and short FRQ."},
    "nsmo": {"level": "Grades 7-10 (Mawhiba)", "description": "Integrated science and math, advanced algebra, scientific reasoning. Mix of MCQ and FRQ."}
}

QUESTIONS_PER_BATCH = 20
TOTAL_WANTED = 250

def generate_batch(track_id, existing_count):
    track_info = TRACKS[track_id]
    prompt = f"""
    Generate a batch of {QUESTIONS_PER_BATCH} highly challenging and unique math questions for the '{track_id}' track.
    Target Audience/Level: {track_info['level']}
    Characteristics: {track_info['description']}
    
    Requirements:
    1. Provide the content in both English and Arabic.
    2. ABSOLUTELY STRICT LATEX RULE: Every single number, variable, formula, and equation MUST be wrapped in LaTeX delimiters. Use \\( x^2 \\) for inline math, and $$ \\sum x $$ for block math. Do NOT write "2x + 3" as plain text. It MUST be "\\( 2x + 3 \\)". Even isolated numbers like "5" must be "\\( 5 \\)".
    3. The Arabic translation must be grammatically correct and use standard Arabic mathematical terminology.
    4. For MCQs, provide 4 to 5 options. For FRQs, leave the options array empty and put the final answer in `correct_index`.
    5. The 'id' should follow the format {track_id.upper()}-{(existing_count+1):03d} onwards.
    
    CRITICAL VISUAL REQUIREMENT:
    To match the real papers flavor, AT LEAST 8 questions in this batch MUST include high-quality visual elements within the `question` text (both English and Arabic). 
    - Use HTML `<table>` for data tables (add Tailwind classes like `w-full text-center border-collapse border border-slate-700`).
    - Use inline `<svg>` for geometry diagrams, charts, and graphs. Ensure SVGs are responsive (e.g. `viewBox="0 0 200 200" class="w-full max-w-xs mx-auto bg-white rounded-lg p-2"`), use standard stroke/fill colors, and are completely valid XML without markdown code blocks.
    Do NOT just provide text. You must actively generate tables and SVG shapes representing triangles, circles, coordinate planes, or bar charts directly inside the JSON string where appropriate.
    
    CRITICAL REQUIREMENT:
    All generated questions MUST closely mimic the ACTUAL PAST PAPERS of the {track_id} competition.
    Match the exact style, rigor, formatting, tone, and typical mathematical depth found in the real exams.
    
    OUTPUT FORMAT:
    You must output ONLY a valid JSON object containing a single key "questions" whose value is an array of the {QUESTIONS_PER_BATCH} question objects.
    
    Each question object must strictly follow this exact schema:
    {{
        "id": "KAUST-001",
        "track": "{track_id}",
        "level": "{track_info['level']}",
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
    
    print(f"Generating batch for {track_id} (Questions {existing_count+1} to {existing_count+QUESTIONS_PER_BATCH})...", flush=True)
    
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
        
    for track_id in TRACKS.keys():
        file_path = os.path.join(DATA_DIR, f"{track_id}.json")
        
        # Load existing
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    questions = json.load(f)
                except json.JSONDecodeError:
                    questions = []
        else:
            questions = []
            
        current_count = len(questions)
        print(f"[{track_id}] Currently has {current_count} questions.", flush=True)
        
        # Only process tracks that aren't finished
        if current_count >= TOTAL_WANTED:
             continue

        # Generate until we reach the target
        while current_count < TOTAL_WANTED:
            try:
                new_batch = generate_batch(track_id, current_count)
                questions.extend(new_batch)
                current_count = len(questions)
                
                # Save progress
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(questions, f, ensure_ascii=False, indent=2)
                
                print(f"[{track_id}] Successfully added batch. Total now: {current_count}/{TOTAL_WANTED}", flush=True)
                
                # Sleep to avoid rate limits
                time.sleep(1)
                
            except Exception as e:
                print(f"Error generating batch for {track_id}: {e}", flush=True)
                print("Retrying in 5 seconds...", flush=True)
                time.sleep(5)
        
        # Track finished, push to git
        if current_count >= TOTAL_WANTED:
            print(f"[{track_id}] Reached target! Pushing to GitHub...", flush=True)
            os.system(f"git add {file_path} && git commit -m 'Auto-push {track_id} track (100 questions)' && git push origin main")

if __name__ == "__main__":
    print("Starting the Math Database Generation Protocol...", flush=True)
    main()
    print("Finished generating database!", flush=True)
