def inspiration_agent(state, llm):
    print("[AGENT] Inspiration agent running...")

    prompt = f"""
Suggest 3 concise travel ideas (bullets only) for:
{state["user_input"]}
"""

    try:
        text = llm(prompt)
        state["inspiration"] = text
    except Exception as e:
        state["inspiration"] = "__ERROR__: Gemini API quota exceeded."
        state["error"] = True

    return state
