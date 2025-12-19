def planning_agent(state, llm):
    print("[AGENT] Planning agent running...")

    prompt = f"""
Create a simple 3-day itinerary.
Rules:
- Use exactly this format
- Include times: 10am, 4pm, 8pm
- Keep place names short
- No extra descriptions

Format:
Day 1
10am:
4pm:
8pm:

Day 2
10am:
4pm:
8pm:

Day 3
10am:
4pm:
8pm:

Destination context:
{state['user_input']}
"""

    return {"plan": llm(prompt)}
