from ollama import generate

MODEL_NAME = "llama3:latest"

def ollama_generate(prompt):
    result = generate(model=MODEL_NAME, prompt=prompt)

    # 👇 ONLY AI TEXT RESPONSE
    return result['response']

def classify_query(user_input):
    prompt = f"""
    Classify this query into ONE category:
    sales / marketing / copywriting / analytics

    Query: {user_input}

    Only return one word.
    """

    result = generate(model=MODEL_NAME, prompt=prompt)
    return result['response'].strip().lower()
# ======================================================