from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

# Prompts for evaluation
prompts = [
    "How do I create and switch to a new Git branch?",
    "How to compress a directory into a .tar.gz file?",
    "How do I activate a virtual environment in Python?",
    "Find all .txt files inside a directory recursively.",
    "How do I remove a remote Git repository?"
]

base_model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
adapter_path = "lora_adapter_2"

# Load tokenizer
print(" Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(base_model_id)

# Load base model
print(" Loading base model...")
base_model = AutoModelForCausalLM.from_pretrained(base_model_id).to("cpu")

# Load fine-tuned model with LoRA adapter
print(" Attaching LoRA adapter...")
finetuned_model = AutoModelForCausalLM.from_pretrained(base_model_id).to("cpu")
finetuned_model = PeftModel.from_pretrained(finetuned_model, adapter_path)

# Inference function
def generate(model, prompt, max_new_tokens=150):
    input_text = f"<s>[INST] {prompt.strip()} [/INST]"
    inputs = tokenizer(input_text, return_tensors="pt").to("cpu")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_p=0.95,
        temperature=0.7
    )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("[/INST]")[-1].strip()

# Run comparison
print("\n Comparing Base vs. Fine-Tuned Model...\n")

for i, prompt in enumerate(prompts, 1):
    print(f" Prompt {i}: {prompt}\n")

    print(" Base Model Output:")
    base_output = generate(base_model, prompt)
    print(base_output, "\n")

    print(" Fine-Tuned Model Output:")
    tuned_output = generate(finetuned_model, prompt)
    print(tuned_output, "\n")

    print("" + "-"*70 + "\n")
