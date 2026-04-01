from agents.sales_agent import SalesAgent
from agents.marketing_agent import MarketingAgent
from agents.copywriting_agent import CopywritingAgent
from agents.analytics_agent import AnalyticsAgent
from core.utils import classify_query


class AgentManager:
    def __init__(self):
        self.agents = {
            "sales": SalesAgent(),
            "marketing": MarketingAgent(),
            "copywriting": CopywritingAgent(),
            "analytics": AnalyticsAgent(),
        }

    def route_question(self, category, question):

        if not category:
            category = classify_query(question)

        print(f"[LOG] Selected Agent: {category}")
        # ======================================================

        if category not in self.agents:
            return "Only Sales, Marketing, Copywriting, or Analytics questions allowed."

        agent = self.agents[category]
        return agent.generate_response(question)