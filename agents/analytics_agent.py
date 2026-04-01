from core.agent_base import BaseAgent

class AnalyticsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analytics Agent",
            role_description="Generates campaign analytics, reports, and actionable insights",
            prompt_template_path="prompts/analytics_prompt.txt"
        )