import json
import re

def normalize_whitespace(text):
    # Replace all sequences of whitespace (including newlines) with a single space
    return re.sub(r'\s+', ' ', text).strip()

with open("qa_pairsII.json", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []
for qa in data:
    q = normalize_whitespace(qa["question"])
    a = normalize_whitespace(qa["answer"])
    cleaned.append({"question": q, "answer": a})

with open("qa_pairs_normalizedB.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)
