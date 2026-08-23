#!/usr/bin/env python3
"""Retag existing 253 NSMO questions to 'Phase 2: Intermediate Olympiad (Grades 8-9)'"""
import json

DATA_FILE = "data/nsmo.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    qs = json.load(f)

for q in qs:
    if q.get("level") == "Grades 7-10 (Mawhiba)":
        q["level"] = "Phase 2: Intermediate Olympiad (Grades 8-9)"

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

from collections import Counter
counts = Counter(q.get("level") for q in qs)
print("Retagged NSMO questions:", dict(counts))
