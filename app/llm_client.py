import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"

def generate_from_local_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 1.0,
            "top_p": 0.95,
            "num_predict": 80,
            "repeat_penalty": 1.1
        }
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()

    response_text = data.get("response", "").strip()
    thinking = data.get("thinking", "")

    if response_text:
        return response_text
    elif thinking:
        return thinking
    else:
        return "No response generated"