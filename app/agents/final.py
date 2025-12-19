def final_agent(state):
    print("[AGENT] Final agent running...")

    state["final"] = f"""
✈️ Travel Concierge Plan (Concise)

DESTINATION IDEAS
{state["inspiration"]}

ITINERARY (3 DAYS)
{state["plan"]}

FLIGHTS & STAY
{state["booking"]}
"""
    return state
