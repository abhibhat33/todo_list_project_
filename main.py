import json
import urllib.request
from urllib.parse import urlencode

url = "http://127.0.0.1:5000/api/todo"

# List all tasks
with urllib.request.urlopen(url) as response:
    tasks = json.loads(response.read().decode())
    print(tasks)

# Create a new task
new_task = {"title": "Do laundry", "description": "Wash clothes"}
data = urlencode(new_task).encode('utf-8')
req = urllib.request.Request(url + "/create", data=data, method='POST')
with urllib.request.urlopen(req) as response:
    task = json.loads(response.read().decode())
    print(task)

# List all tasks again to see the new task
with urllib.request.urlopen(url) as response:
    tasks = json.loads(response.read().decode())
    print(tasks)
