from typing import TypedDict

class TravelState(TypedDict):
    user_input: str
    inspiration: str
    plan: str
    booking: str
    final: str
    error: bool
