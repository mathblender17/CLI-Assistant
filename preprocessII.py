import json
from bs4 import BeautifulSoup
import html

input_file = "qa_pairsI.json"      # Your original JSON file
output_file = "qa_PairsII.json" # Output for fine-tuning

def clean_html(text):
    # Remove HTML tags, decode HTML entities, preserve code formatting
    soup = BeautifulSoup(text, "html.parser")
    # Convert <pre><code>...</code></pre> to just the code (preserving line breaks)
    for code in soup.find_all("code"):
        code.replace_with("\n" + code.get_text() + "\n")
    # Get text, preserving line breaks
    cleaned = soup.get_text(separator="\n")
    # Decode HTML entities
    cleaned = html.unescape(cleaned)
    # Remove excessive blank lines
    cleaned = "\n".join(line.rstrip() for line in cleaned.splitlines() if line.strip())
    return cleaned.strip()

with open(input_file, encoding="utf-8") as f:
    data = json.load(f)

cleaned_data = []
for item in data:
    question = clean_html(item["question"])
    answer = clean_html(item["answer"])
    cleaned_data.append({"question": question, "answer": answer})

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print(f"Cleaned {len(cleaned_data)} Q&A pairs and saved to {output_file}")
