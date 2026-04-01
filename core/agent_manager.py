from agents.sales_agent import SalesAgent
from agents.marketing_agent import MarketingAgent
from agents.copywriting_agent import CopywritingAgent
from agents.analytics_agent import AnalyticsAgent

class AgentManager:
    def __init__(self):
        self.agents = {
            "sales": SalesAgent(),
            "marketing": MarketingAgent(),
            "copywriting": CopywritingAgent(),
            "analytics": AnalyticsAgent(),
        }

    def route_question(self, category, question):
        if category not in self.agents:
            return "Only Sales, Marketing, Copywriting, or Analytics questions allowed."
        agent = self.agents[category]
        return agent.generate_response(question)