from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simple in-memory storage
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todo = {
        "id": len(todos) + 1,
        "titre": data.get("titre"),
        "note": data.get("note"),
        "date": data.get("date", datetime.now().strftime("%Y-%m-%d"))
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Supprimé"}), 200

if __name__ == '__main__':
    # Bind to all interfaces for Docker/K8s
    app.run(host="0.0.0.0", port=5000)  # nosec B104
