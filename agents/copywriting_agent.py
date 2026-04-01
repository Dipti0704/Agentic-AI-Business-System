from core.agent_base import BaseAgent

class CopywritingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Copywriting Agent",
            role_description="Generates high-converting copywriting content for ads, emails, posts",
            prompt_template_path="prompts/copywriting_prompt.txt"
        )