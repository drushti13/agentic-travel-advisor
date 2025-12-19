# Agentic Travel Advisor

## Description

Agentic Travel Advisor is a multi-agent travel planning application built using a graph-based agent architecture. The system leverages large language models to collaboratively generate travel inspiration, detailed itineraries, and booking guidance based on a user’s travel query.

The project demonstrates how multiple specialized agents can work together in a controlled execution flow using LangGraph, while optimizing for limited API quotas through concise prompts and optional caching.

## Features

- Multi-agent architecture with clear role separation
- Specialized agents for:
  - Travel inspiration
  - Itinerary planning
  - Booking recommendations
  - Final response aggregation
- Graph-based execution flow using LangGraph
- Integration with Google Gemini API
- Graceful handling of API quota limits
- Console-based user interaction
- Modular and extensible codebase

## Tech Stack

-Programming Language: Python 3.10+
-Large Language Model API: Google Gemini (via google-genai)
-Agent Orchestration: LangGraph
-State Management: TypedDict-based shared state
-Environment Management: python-dotenv
-Optional Caching: JSON-based local cache

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/agentic-travel-advisor.git
cd agentic-travel-advisor
```
Set up environment variables
Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```
Run the application
```bash
python -m app.main
```


