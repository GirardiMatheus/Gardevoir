from flask import Flask, request, jsonify
from models.tasks import Tasks

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Tasks(id=task_id_control, title=data["title"], description=data.get("description", ""))
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "New task successfully created", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = []
  for task in tasks:
    task_list.append(task.to_dict())
  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }
  return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())

  return jsonify({"message": "Could not find the task"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break

  if task is None:
      return jsonify({"message": "Could not find the task"}), 404

  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  
  return jsonify({"message": "Task successfully updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break

  if task is None:
      return jsonify({"message": "Could not find the task"}), 404

  tasks.remove(task)
  return jsonify({"message": "Task successfully deleted"})

if __name__ == "__main__":
  app.run(debug=True)
