def booking_agent(state, llm):
    print("[AGENT] Booking agent running...")

    prompt = f"""
Suggest flight tips and hotel areas for this plan:
{state["plan"]}
"""

    try:
        state["booking"] = llm(prompt)
    except Exception:
        state["booking"] = "__ERROR__: Gemini API quota exceeded."
        state["error"] = True

    return state
