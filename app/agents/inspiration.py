def inspiration_agent(state, llm):
    print("[AGENT] Inspiration agent running...")

    prompt = f"""
Give exactly 3 destination ideas for this trip.
Rules:
- Short bullet points only
- No explanations
- No formatting symbols
Trip:
{state['user_input']}
"""

    response = llm(prompt)

    return {
        "inspiration": response.strip()
    }
