from flask import Flask, request, jsonify, Response
from flask_cors import CORS   # <-- add this
from core.agent_manager import AgentManager
from core.langgraph_flow import run_langgraph


app = Flask(__name__)
CORS(app)  # <-- enable CORS for all routes

manager = AgentManager()

@app.route("/api/ask", methods=["POST"])
def ask_agent():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "Missing question"}), 400

    response = run_langgraph(question)

    return jsonify({"response": response})


@app.route("/api/stream", methods=["POST"])
def stream_agent():
    data = request.json
    question = data.get("question")

    if not question:
        return jsonify({"error": "Missing question"}), 400

    def generate_stream():
        from core.utils import ollama_stream

        for chunk in ollama_stream(question):
            yield chunk

    return Response(generate_stream(), content_type="text/plain")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
# =======================================================