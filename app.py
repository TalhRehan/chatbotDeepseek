from flask import Flask, request, jsonify, render_template
from langchain_ollama.llms import OllamaLLM
from langgraph.graph import StateGraph, START, END
from typing import List, Dict

app = Flask(__name__, template_folder="templates")

# Initialize Ollama LLM
llm = OllamaLLM(model="deepseek-r1", base_url="http://localhost:11434")

class State(Dict):
    messages: List[Dict[str, str]]

graph_builder = StateGraph(State)

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    state["messages"].append({"role": "assistant", "content": response})
    return {"messages": state["messages"]}

# Add nodes and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    state = {"messages": [{"role": "user", "content": user_input}]}
    for event in graph.stream(state):
        for value in event.values():
            return value["messages"][-1]["content"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = stream_graph_updates(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
