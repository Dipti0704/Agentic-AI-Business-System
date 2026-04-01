from core.utils import ollama_generate, ollama_stream

# ===================== 🔥 NEW CODE =====================
chat_history = []
# ======================================================

class BaseAgent:
    def __init__(self, name, role_description, prompt_template_path):
        self.name = name
        self.role_description = role_description
        with open(prompt_template_path, "r", encoding="utf-8") as f:
            self.prompt_template = f.read()

    def generate_response(self, user_input):

        prompt = self.prompt_template.replace("{user_input}", user_input)
        return ollama_generate(prompt)
        # ======================================================

      

        # ======================================================

    def stream_response(self, user_input):
        prompt = self.prompt_template.replace("{user_input}", user_input)
        return ollama_stream(prompt)