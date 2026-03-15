from langgraph.graph import StateGraph, END
from state.graph_state import GraphState
from agents.architecture_agent import architecture_agent
from nodes.human_review import human_review


def router(state):

    if state["approved"]:
        return "approved"

    return "regenerate"


def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("architecture_agent", architecture_agent)
    workflow.add_node("human_review", human_review)

    workflow.set_entry_point("architecture_agent")

    workflow.add_edge("architecture_agent", "human_review")

    workflow.add_conditional_edges(
        "human_review",
        router,
        {
            "approved": END,
            "regenerate": "architecture_agent"
        }
    )

    return workflow.compile()