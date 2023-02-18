from flask import Flask, jsonify, request, abort
import csv

app = Flask(__name__)

# Sample tasks for testing
tasks = [
    {"id": 1, "title": "do coding", "description": "finish the project", "done": False},
    {"id": 2, "title": "have food", "description": "have healthy food", "done": False}
]

with open('tasks.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['id'] = int(row['id'])
        row['done'] = row['done'] == 'True'
        tasks.append(row)

# Save data to CSV file
def save_tasks():
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'title', 'description', 'done'])
        writer.writeheader()
        for task in tasks:
            task['done'] = str(task['done'])
            writer.writerow(task)
# for Getting all tasks details
@app.route('/api/todo', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Getting a single task by id
@app.route('/api/todo/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    return jsonify({'task': task[0]})

# Create a new task
@app.route('/api/todo', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'The title of the task is required'})
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Update an existing task
@app.route('/api/todo/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    if not request.json:
        return jsonify({'error': 'No data provided to update the task'})
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# Mark a task as complete
@app.route('/api/todo/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    task[0]['done'] = True
    return jsonify({'task': task[0]})

# Mark a task as incomplete
@app.route('/api/todo/<int:task_id>/incomplete', methods=['PUT'])
def incomplete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    task[0]['done'] = False
    return jsonify({'task': task[0]})

# Delete a task by using id
@app.route('/api/todo/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
