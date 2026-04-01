from ollama import generate

MODEL_NAME = "llama3:latest"

def ollama_generate(prompt):
    result = generate(model=MODEL_NAME, prompt=prompt)

    # 👇 ONLY AI TEXT RESPONSE
    return result['response']