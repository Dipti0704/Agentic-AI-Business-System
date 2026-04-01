from core.agent_base import BaseAgent

class MarketingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Marketing Agent",
            role_description="Handles Meta Ads, Google Ads, Copywriting campaigns",
            prompt_template_path="prompts/marketing_prompt.txt"
        )