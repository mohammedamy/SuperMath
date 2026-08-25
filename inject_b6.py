#!/usr/bin/env python3
"""Batch 6 (Final) — Grade 6: 216-250, Grade 9: 201-250"""
import json
import os

DATA_FILE = "data/nafes.json"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "batch6.json")
    data_file_path = os.path.join(script_dir, DATA_FILE)
    
    with open(json_path, "r", encoding="utf-8") as f:
        new_questions = json.load(f)

    with open(data_file_path, "r", encoding="utf-8") as f:
        all_questions = json.load(f)
        
    existing_ids = {q["id"] for q in all_questions}
    to_add = [q for q in new_questions if q["id"] not in existing_ids]
    all_questions.extend(to_add)
    
    with open(data_file_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
        
    g3 = sum(1 for q in all_questions if q.get("level") == "Grade 3")
    g6 = sum(1 for q in all_questions if q.get("level") == "Grade 6")
    g9 = sum(1 for q in all_questions if q.get("level") == "Grade 9")
    print(f"Added {len(to_add)} questions. Grade 3: {g3} | Grade 6: {g6} | Grade 9: {g9} | Total: {len(all_questions)}")

if __name__ == "__main__":
    main()
