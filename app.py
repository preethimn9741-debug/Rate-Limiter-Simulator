from flask import Flask, request, jsonify
from database import (
    init_db, get_tasks, add_task, update_task, delete_task
)

app = Flask(__name__)
init_db()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Task Manager API Running"})

@app.route("/tasks", methods=["GET"])
def fetch_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    if not request.is_json:
        return {"error": "JSON required"}, 415

    data = request.get_json()
    if "title" not in data or not data["title"]:
        return {"error": "Invalid task title"}, 400

    add_task(data["title"])
    return {"message": "Task added"}, 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def toggle_task(task_id):
    if not request.is_json:
        return {"error": "JSON required"}, 415

    data = request.get_json()
    if "completed" not in data or not isinstance(data["completed"], bool):
        return {"error": "completed must be boolean"}, 400

    try:
        update_task(task_id, data["completed"])
    except ValueError as e:
        return {"error": str(e)}, 400

    return {"message": "Task updated"}, 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return {"message": "Task deleted"}, 200


if __name__ == "__main__":
    app.run(debug=True)
