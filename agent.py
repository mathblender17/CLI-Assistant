#CPU only version of the agent script
import sys
import json
import datetime
import os


import warnings
warnings.filterwarnings("ignore", message=".*Found missing adapter keys.*")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

def load_model():
    base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    adapter_path = "lora_adapter_2"

    print("⏳ Loading base model...")
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model)

    print("🔗 Loading LoRA adapter...")
    model = PeftModel.from_pretrained(model, adapter_path)

    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    input_text = f"<s>[INST] {prompt.strip()} [/INST]"
    inputs = tokenizer(input_text, return_tensors="pt")  # No .to("cuda")

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        top_p=0.95,
        temperature=0.7
    )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("[/INST]")[-1].strip()

def dry_run_shell_command(response):
    first_line = response.strip().split('\n')[0]
    if first_line.startswith("`") and first_line.endswith("`"):
        cmd = first_line.strip("`")
        print(f"\n💻 Dry Run: echo {cmd}\n")
    elif first_line.startswith("$"):
        cmd = first_line[1:].strip()
        print(f"\n💻 Dry Run: echo {cmd}\n")
    else:
        print("\nℹ️ No shell command detected in the first line.\n")

def log_interaction(prompt, response):
    os.makedirs("logs", exist_ok=True)
    entry = {
        "timestamp": str(datetime.datetime.now()),
        "instruction": prompt,
        "response": response
    }
    with open("logs/trace.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py \"Your CLI question here\"")
        sys.exit(1)

    user_input = sys.argv[1]

    model, tokenizer = load_model()
    print("🤖 Generating response...")
    response = generate_response(model, tokenizer, user_input)

    print("\n🧠 Response:\n")
    print(response)

    dry_run_shell_command(response)
    log_interaction(user_input, response)
