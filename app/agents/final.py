def final_agent(state):
    print("[AGENT] Final agent running...")
    return {
        "final": f"""
Travel Plan

Destination Ideas
{state["inspiration"]}

3-Day Itinerary
{state["plan"]}

Flights & Stay
{state["booking"]}
"""
    }
