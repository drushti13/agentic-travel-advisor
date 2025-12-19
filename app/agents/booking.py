def booking_agent(state, llm):
    print("[AGENT] Booking agent running...")
    prompt = f"""
Give flight and stay info strictly for this destination.

Rules:
- No bold text
- No headings
- No notes
- No explanations
- Keep it short

Required format:

Flights & Stay
- Fly to: <2-3 major airports>
- Stay areas and prices:
  • Area name: price range per night
  • Area name: price range per night

Destination:
{state["user_input"]}
"""
    return {"booking": llm(prompt)}
