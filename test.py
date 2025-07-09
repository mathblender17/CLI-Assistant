from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model).to("cpu")

def ask(prompt):
    input_text = f"<s>[INST] {prompt.strip()} [/INST]"
    inputs = tokenizer(input_text, return_tensors="pt").to("cpu")
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        top_p=0.95,
        temperature=0.7
    )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("[/INST]")[-1].strip()

# Example
prompt = "How do I create and switch to a new Git branch?"
print(ask(prompt))
