import csv
import json

input_file = 'QueryResults.csv'   # Your exported CSV file
output_file = 'qa_pairsI.json'

qa_list = []
with open(input_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        qa_list.append({
            "question": row["QuestionBody"],
            "answer": row["AnswerBody"]
        })

with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(qa_list, jsonfile, ensure_ascii=False, indent=2)
