import sys
import json
import datetime
import os

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch
from transformers import BitsAndBytesConfig

def load_model():
    base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    adapter_path = "lora_adapter_2"

    print("⏳ Loading base model...")
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    # Use BitsAndBytesConfig for quantization``
    bnb_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=6.0,
    )

    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        quantization_config=bnb_config,
        device_map="auto"
    )
      # model = AutoModelForCausalLM.from_pretrained(
    #     base_model,
    #     device_map="auto",
    #     torch_dtype=torch.float16,
    #     load_in_8bit=True
    # )
    
    
    print("🔗 Loading LoRA adapter...")
    model = PeftModel.from_pretrained(model, adapter_path)

    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    input_text = f"<s>[INST] {prompt.strip()} [/INST]"
    #Dual bot GPU and CPU support
    # Use GPU if available, otherwise fallback to CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    

    # inputs = tokenizer(input_text, return_tensors="pt").to("cuda") --> only GPU

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
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

  