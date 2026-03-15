from typing import TypedDict, Optional, Dict


class GraphState(TypedDict):
    user_prompt: str
    architecture: Optional[Dict]
    human_feedback: Optional[str]
    approved: Optional[bool]