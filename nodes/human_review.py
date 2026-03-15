import json


def human_review(state):

    print("\nGenerated Architecture:\n")
    print(json.dumps(state["architecture"], indent=2))

    decision = input("\nApprove architecture? (y/n): ")

    if decision.lower() == "y":
        return {
            "approved": True
        }

    feedback = input("Enter feedback: ")

    return {
        "approved": False,
        "human_feedback": feedback
    }