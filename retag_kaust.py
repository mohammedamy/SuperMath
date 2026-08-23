#!/usr/bin/env python3
"""Retag existing 260 KAUST questions to 'Phase 2: Advanced Analysis'"""
import json

DATA_FILE = "data/kaust.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    qs = json.load(f)

for q in qs:
    if q.get("level") == "High School (Gifted)":
        q["level"] = "Phase 2: Advanced Analysis"

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

from collections import Counter
counts = Counter(q.get("level") for q in qs)
print("Retagged KAUST questions:", dict(counts))
