from langgraph.graph import StateGraph
from app.state import TravelState
from app.agents.inspiration import inspiration_agent
from app.agents.planning import planning_agent
from app.agents.booking import booking_agent
from app.agents.final import final_agent

def build_graph(llm):
    print("[GRAPH] Initializing StateGraph...")
    graph = StateGraph(TravelState)

    graph.add_node("inspiration", lambda s: inspiration_agent(s, llm))
    graph.add_node("planning", lambda s: planning_agent(s, llm))
    graph.add_node("booking", lambda s: booking_agent(s, llm))
    graph.add_node("final", final_agent)

    graph.set_entry_point("inspiration")
    graph.add_edge("inspiration", "planning")
    graph.add_edge("planning", "booking")
    graph.add_edge("booking", "final")

    compiled = graph.compile()
    print("[GRAPH] Graph compiled successfully")
    return compiled
