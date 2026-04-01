from flask import Flask, request, jsonify
from flask_cors import CORS   # <-- add this
from core.agent_manager import AgentManager

app = Flask(__name__)
CORS(app)  # <-- enable CORS for all routes

manager = AgentManager()

@app.route("/api/ask", methods=["POST"])
def ask_agent():
    data = request.json
    category = data.get("agent")
    question = data.get("question")
    if not question:
        return jsonify({"error": "Missing question"}), 400

    response = manager.route_question(category, question)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)