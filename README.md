# 🧠 CLI Assistant — TinyLlama + LoRA for Command-Line Help

This project builds a lightweight command-line assistant fine-tuned on CLI Q&A (Linux, Git, Python environments) using the TinyLlama-1.1B-Chat model enhanced with LoRA adapters for efficient training and inference.

---

## 🚀 Features

- ✅ TinyLlama-based assistant with fast 8-bit inference
- 🔁 LoRA-fine-tuning on CLI Q&A JSONL dataset
- 📊 Evaluation with BLEU, ROUGE-L, and plan quality (0–2)
- ⚙️ Works on both CPU (local) and GPU (Colab)
- 🧪 Dynamic + Static evaluation pipeline

---

## 📦 Requirements

Install dependencies (locally):

```bash
pip install -r requirements.txt
```

## Project Structure
cli-assistant/
├── agent.py                   # Run assistant locally (CPU)
├── agent_colab.ipynb         # GPU/Colab version with BLEU/ROUGE eval
├── cli_qa.jsonl              # Prompt-answer dataset
├── compare_base_vs_finetuned.py # Static evaluation script
├── model_comparison_results.csv  # Output of evaluation
├── lora_adapter/             # Fine-tuned LoRA weights (upload in Colab)
├── requirements.txt
└── README.md


## Setup & Inference
### Local (CPU)
```bash
python agent.py "How to activate a virtual environment in Python?"
```
### Colab (GPU)
Open agent_colab.ipynb, upload:

cli_qa.jsonl to /content/

lora_adapter/ folder to /content/

Then run all cells to test and evaluate.



### Example
```bash
$ python agent.py "Find all .txt files recursively"
Response: find . -type f -name "*.txt"
```
## Future Scope
Add multi-turn interaction

Deploy as web or shell chatbot

Integrate execution with sandboxed shell

