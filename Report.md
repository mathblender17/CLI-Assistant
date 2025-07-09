# 🧠 CLI Assistant with TinyLlama & LoRA – Project Report

## 📌 Overview

This project develops a lightweight command-line assistant capable of understanding and answering Linux/Git/CLI-related queries. The core of the assistant is based on the `TinyLlama-1.1B-Chat` language model, fine-tuned using LoRA (Low-Rank Adaptation) on a custom CLI Q&A dataset. The assistant can simulate shell commands, answer natural language prompts, and demonstrate command-line workflows safely and effectively.

---

## 🗃️ Dataset

- **Format**: JSONL file with `{"question": "...", "answer": "..."}` pairs
- **Size**: 150 samples, curated manually
- **Domain**: Git, bash scripting, shell basics, environment setup
- **Goal**: Teach the LLM to answer CLI questions concisely and safely

---

## 🛠️ Model & Fine-Tuning

- **Base Model**: [`TinyLlama/TinyLlama-1.1B-Chat-v1.0`](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- **Method**: Parameter-efficient fine-tuning with LoRA using the `peft` library
- **Training Platform**: Google Colab (CPU + GPU)
- **Inference Support**: CPU (local) and GPU (Colab) via `agent.py` and `agent_colab.ipynb`
- **LoRA Output**: Saved to `lora_adapter/` directory

---

## 🧪 Evaluation Strategy

We performed two types of evaluations:

### 1. Static Evaluation (`eval_static.md`)
- Compared base model vs fine-tuned outputs on 5 standard prompts
- Assessed **Plan Quality** (0–2) and human alignment
- Fine-tuned model showed stronger contextual structure but varied performance

### 2. Dynamic Evaluation (`eval_dynamic.md`)
- Ran live agent queries via `agent.py`
- Included 2 edge-case prompts for robustness
- Dry-run shell preview for command safety

---

## 📊 Results Summary

| Metric         | Base Model | Fine-Tuned Model |
|----------------|------------|------------------|
| Plan Quality (avg) | 1.4        | 0.6–2.0            |
| BLEU (avg)     | ~0.38      | ↑ Improved         |
| ROUGE-L (avg)  | ~0.45      | ↑ Improved         |

- **Key Strength**: Fine-tuned model gives structured, step-by-step guidance
- **Key Weakness**: Inconsistent decoding in edge prompts without retries

---

## 💡 Challenges Faced

- Installing and running quantized (8-bit) TinyLlama with GPU inference
- LoRA adapter mismatch errors due to versioning
- Handling `.to(device)` errors with 8-bit models
- Ensuring consistent decoding with truncated outputs

---

## ✅ Final Takeaways

- LoRA is highly effective for lightweight, domain-specific fine-tuning
- TinyLlama is a great base for edge-deployable assistants
- Structured prompting and consistent evaluation pipelines are critical
- A minimal dataset (~150 samples) can already shape useful behavior

---

## 🏁 Project Status

✅ Training complete  
✅ Inference stable (CPU/GPU)  
✅ Evaluation documented  
✅ Logs tracked in `logs/trace.jsonl`

---

## 🔮 Future Scope

- Expand dataset to 500–1000 entries
- Handle multi-turn CLI interactions
- Integrate command validation or execution (sandboxed)
- Add UI/CLI front-end wrapper

---

## 👨‍💻 Built With

- `transformers` (Hugging Face)
- `peft`, `accelerate`, `bitsandbytes`
- Python 3.11
- Google Colab + VS Code

---

*Project by: Meghraj | Date: June 2025*
