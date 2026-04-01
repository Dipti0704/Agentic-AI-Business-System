from langgraph.graph import StateGraph
from core.agent_manager import AgentManager
from core.utils import classify_query

manager = AgentManager()

# ===================== STATE =====================
# state = {
#   "input": str,
#   "agent": str,
#   "output": str
# }

# ===================== STEP 1: CLASSIFIER =====================
def classify_node(state):
    user_input = state["input"]

    agent = classify_query(user_input)

    print(f"[LangGraph] Classified as: {agent}")

    state["agent"] = agent
    return state


# ===================== STEP 2: PRIMARY AGENT =====================
def agent_node(state):
    agent_name = state["agent"]
    user_input = state["input"]

    agent = manager.agents.get(agent_name)

    if not agent:
        state["output"] = "Invalid agent type"
        return state

    result = agent.generate_response(user_input)

    state["output"] = result
    return state


# ===================== STEP 3: OPTIONAL REFINEMENT =====================
def refinement_node(state):
    """
    Example:
    Marketing → Copywriting refinement
    """
    agent_name = state["agent"]

    # 🔥 ONLY apply refinement for marketing
    if agent_name == "marketing":
        copy_agent = manager.agents["copywriting"]

        refined = copy_agent.generate_response(state["output"])

        state["output"] = refined

    return state


# ===================== BUILD GRAPH =====================
def build_graph():
    graph = StateGraph(dict)

    graph.add_node("classifier", classify_node)
    graph.add_node("agent", agent_node)
    graph.add_node("refiner", refinement_node)

    graph.set_entry_point("classifier")

    graph.add_edge("classifier", "agent")
    graph.add_edge("agent", "refiner")

    return graph.compile()


# ===================== RUN FUNCTION =====================
app_graph = build_graph()

def run_langgraph(input_text):
    result = app_graph.invoke({"input": input_text})
    return result["output"]