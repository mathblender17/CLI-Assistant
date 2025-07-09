import json
import re

def normalize_text(text):
    # Split into lines
    lines = text.splitlines()
    normalized = []
    in_code = False

    for line in lines:
        # Detect code block (you can adjust this rule)
        if line.strip().startswith("$") or line.strip().startswith("git") or line.startswith("    "):
            normalized.append("\n" + line.strip())
            in_code = True
        elif line.strip() == "":
            in_code = False
        elif in_code:
            normalized.append("\n" + line.strip())
        else:
            # Remove extra spaces and join normal text
            normalized.append(" " + line.strip())
            in_code = False

    # Join and collapse multiple spaces
    out = "".join(normalized)
    out = re.sub(r'\s+', ' ', out)
    # Restore line breaks before code blocks
    out = re.sub(r' ?(\n\$)', r'\1', out)
    return out.strip()

with open("qa_pairsII.json", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []
for qa in data:
    q = normalize_text(qa["question"])
    a = normalize_text(qa["answer"])
    cleaned.append({"question": q, "answer": a})

with open("qa_pairs_normalizedA.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)
