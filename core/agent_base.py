from core.utils import ollama_generate

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

        chat_history.append({"user": user_input})

        context = "\n".join(
            [f"User: {c['user']}" for c in chat_history[-5:] if "user" in c]
        )
        # ======================================================

        prompt = self.prompt_template.replace("{user_input}", context)

        response = ollama_generate(prompt)

        chat_history.append({"ai": response})
        # ======================================================

        return response