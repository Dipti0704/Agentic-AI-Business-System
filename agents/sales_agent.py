from core.agent_base import BaseAgent

class SalesAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Sales Agent",
            role_description="Handles customer sales queries, pitches, and follow-ups",
            prompt_template_path="prompts/sales_prompt.txt"
        )