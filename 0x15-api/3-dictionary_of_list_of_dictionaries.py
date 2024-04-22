#!/usr/bin/python3
"""
    A Script that, uses a REST API to return an employee's details,
    and exports their data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":

    baseUrl = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}users".format(baseUrl))
    users = users.json()

    todos = requests.get("{}todos".format(baseUrl))
    tasks = todos.json()

    all_tasks = {}

    for user in users:
        task_list = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_dict)
        all_tasks[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_tasks, f)
