from flask import Flask, request, jsonify

app = Flask(__name__)

#An easy in-memory data structure for To-Do List
todo_list = []

@app.route('/')
def home():
    return "Welcome to the To-Do List API!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_list)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if "task" in data:
        todo_list.append({"id": len(todo_list) + 1, "task": data["task"]})
        return jsonify({"message": "Task added!"}), 201
    return jsonify({"error": "Task is required"}), 400

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo_list
    todo_list = [task for task in todo_list if task["id"] != todo_id]
    return jsonify({"message": "Task deleted!"})

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5000)
