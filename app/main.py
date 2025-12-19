import os
from groq import Groq
from app.graph import build_graph
from app.state import TravelState


# -----------------------
# LLM SETUP (GROQ ONLY)
# -----------------------

def setup_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)
    print("[SETUP] Using Groq (llama-3.1-8b-instant)")

    def llm(prompt: str) -> str:
        print("[LLM] Sending prompt to Groq...")
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content

    return llm


# -----------------------
# MAIN
# -----------------------

def main():
    llm = setup_llm()

    print("[MAIN] Building agent graph...")
    app = build_graph(llm)

    user_input = input("\nAsk travel question: ")

    initial_state: TravelState = {
        "user_input": user_input,
        "inspiration": "",
        "plan": "",
        "booking": "",
        "final": "",
        "error": False,
    }

    print("\n[MAIN] Invoking graph...\n")
    result = app.invoke(initial_state)

    print("\n========== FINAL OUTPUT ==========\n")
    print(result["final"])


if __name__ == "__main__":
    main()
