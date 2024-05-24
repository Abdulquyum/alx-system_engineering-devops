#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
emp_id = sys.argv[1]
emp_url = f"{url}/users/{emp_id}"

res = requests.get(emp_url)
emp_data = res.json()
emp_name = emp_data.get('name')

todo_url = f"{url}/todos?userId={emp_id}"
response = requests.get(todo_url)

todos = response.json()
total_todos = len(todos)
done_task = [todo for todo in todos if todo.get('completed')]
total_done = 0
for todo in todos:
    if todo.get('completed'):
        total_done += 1

print(f"Employee {emp_name} is done with tasks({total_done}/{total_todos}):")
for task in done_task:
    print(f"\t{task.get('title')}")
