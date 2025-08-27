import os
import re
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# 這裡替換成你的 Hugging Face 模型名稱
STAGE1_MODEL = "your-hf-username/t5-stage1"
STAGE2_MODEL = "your-hf-username/t5-stage2"

MODEL_DIR = os.path.join(os.path.dirname(__file__), "../../models")
STAGE1_PATH = os.path.join(MODEL_DIR, "t5_stage1_trained")
STAGE2_PATH = os.path.join(MODEL_DIR, "t5_stage2_trained_local")

os.makedirs(STAGE1_PATH, exist_ok=True)
os.makedirs(STAGE2_PATH, exist_ok=True)

device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

def load_model(model_name, local_path):
    if not os.listdir(local_path):
        print(f"Downloading model to {local_path} ...")
        model = T5ForConditionalGeneration.from_pretrained(model_name, cache_dir=local_path)
        tokenizer = T5Tokenizer.from_pretrained(model_name, cache_dir=local_path)
    else:
        tokenizer = T5Tokenizer.from_pretrained(local_path)
        model = T5ForConditionalGeneration.from_pretrained(local_path)
    model.to(device)
    return model, tokenizer

model1, tokenizer1 = load_model(STAGE1_MODEL, STAGE1_PATH)
model2, tokenizer2 = load_model(STAGE2_MODEL, STAGE2_PATH)

def predict(text, model, tokenizer, max_length=64):
    inputs = tokenizer(text, return_tensors="pt").to(device)
    outputs = model.generate(inputs["input_ids"], max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def summarize_review(text):
    stage1_output = predict(text, model1, tokenizer1)
    stage2_output = predict(stage1_output, model2, tokenizer2)

    pros_match = re.search(r'pros\s*:\s*(.*?)(?:cons\s*:|$)', stage2_output, flags=re.IGNORECASE | re.DOTALL)
    cons_match = re.search(r'cons\s*:\s*(.*)', stage2_output, flags=re.IGNORECASE | re.DOTALL)

    pros_text = pros_match.group(1).strip() if pros_match else ""
    cons_text = cons_match.group(1).strip() if cons_match else ""

    pros_text = pros_text.capitalize()
    cons_text = cons_text.capitalize()

    result = ""
    if pros_text:
        result += "Pros:\n" + "\n".join(["- " + s.strip() for s in re.split(r'\. |\n', pros_text) if s.strip()]) + "\n\n"
    if cons_text:
        result += "Cons:\n" + "\n".join(["- " + s.strip() for s in re.split(r'\. |\n', cons_text) if s.strip()])
    return result
