import os
from google import genai
from app.graph import build_graph
from app.state import TravelState

def setup_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")

    client = genai.Client(api_key=api_key)

    print("[SETUP] Detecting available Gemini models...")
    model = "models/gemini-2.5-flash"
    print(f"[SETUP] Using model: {model}")

    def llm(prompt: str) -> str:
        print("[LLM] Sending prompt to Gemini...")
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        return response.text

    return llm


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
