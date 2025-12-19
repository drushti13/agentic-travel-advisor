def planning_agent(state, llm):
    print("[AGENT] Planning agent running...")

    prompt = f"""
Create a 3-day itinerary based on:
{state["inspiration"]}
"""

    try:
        state["plan"] = llm(prompt)
    except Exception:
        state["plan"] = "__ERROR__: Gemini API quota exceeded."
        state["error"] = True

    return state
