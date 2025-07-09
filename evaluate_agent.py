import subprocess
import csv
import os

# Prompts to test
prompts = [
    "I accidentally committed the wrong files to Git but haven't pushed the commit to the server yet. How do I undo those commits from the local repository?",
    "How do I properly delete the remotes/origin/bugfix branch both locally and remotely?",
    "What are the differences between git pull and git fetch?",
    "How can I rename a local branch which has not yet been pushed to a remote repository?",
    "I mistakenly added files to Git using the command: git add myfile.txt I have not yet run git commit. How do I undo this so that these changes will not be included in the commit?",
    "I did a git rebase but now my history looks weird and I’m not sure what happened. How do I go back to the previous state?",
    "I did a git pull and now I have a merge conflict, but I also staged the wrong changes. How do I cancel everything and just go back?"
]

# Output CSV path
csv_output = "agent_responses.csv"

# Ensure logs/trace.jsonl is clean
if os.path.exists("logs/trace.jsonl"):
    os.remove("logs/trace.jsonl")

# Evaluate all prompts
print("🔍 Running agent.py on all prompts...")
for prompt in prompts:
    cmd = ["python", "agent.py", prompt]
    subprocess.run(cmd)

# Read logs
print("📥 Reading logs and writing CSV...")
with open("logs/trace.jsonl", "r") as f:
    lines = f.readlines()

# Parse and write CSV
with open(csv_output, "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Prompt", "Response"])  # CSV header

    for line in lines:
        entry = eval(line.strip())
        writer.writerow([entry["instruction"], entry["response"]])

print(f"✅ Done! Results saved in: {csv_output}")
