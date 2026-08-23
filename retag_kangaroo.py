#!/usr/bin/env python3
"""Retag existing 260 Middle School → Cadet (Grades 7-8), then inject Ecolier, Benjamin, Junior batches"""
import json
DATA_FILE = "data/kangaroo.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    qs = json.load(f)

# Retag all existing "Middle School" → "Cadet"
for q in qs:
    if q.get("level") == "Middle School":
        q["level"] = "Cadet"

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

phases = {}
for q in qs:
    lvl = q.get("level","?")
    phases[lvl] = phases.get(lvl,0)+1
print("Retagged. Counts:", phases)
print("Total:", len(qs))
