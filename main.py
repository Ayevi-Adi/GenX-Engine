from graph.workflow import build_graph
import json


def main():

    graph = build_graph()

    prompt = input("Describe the website: ")

    result = graph.invoke({
        "user_prompt": prompt
    })

    print("\nFinal Approved Architecture:\n")
    print(json.dumps(result["architecture"], indent=2))


if __name__ == "__main__":
    main()