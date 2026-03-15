# from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import SystemMessage, HumanMessage
from config.llm import llm
from utils.json_parser import parse_json


SYSTEM_PROMPT = """
You are a senior software architect.

Convert a website idea into structured architecture JSON.

Output format:

{
  "tech_stack": "",
  "pages": [],
  "components": [],
  "routing": {},
  "backend_required": true/false,
  "notes": ""
}
"""


def architecture_agent(state):

    prompt = state["user_prompt"]
    feedback = state.get("human_feedback")

    if feedback:
        user_input = f"""
User request:
{prompt}

Human feedback:
{feedback}

Regenerate architecture.
"""
    else:
        user_input = prompt

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ])

    architecture = parse_json(response.content)

    return {
        "architecture": architecture
    }