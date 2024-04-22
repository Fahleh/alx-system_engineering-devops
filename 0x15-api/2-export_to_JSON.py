#!/usr/bin/python3
"""
    A sript that, uses a REST API, to return an employee's details
    and exports their data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    baseUrl = 'https://jsonplaceholder.typicode.com/'

    req = requests.Session()

    emp_id = argv[1]
    todo = '{}users/{}/todos'.format(baseUrl, emp_id)
    user = '{}users/{}'.format(baseUrl, emp_id)

    tasks = req.get(todo)
    user_name = req.get(user)

    employee_tasks = tasks.json()
    employee = user_name.json()['username']

    completed_tasks = []
    user_obj = {}

    for task in employee_tasks:
        completed_tasks.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee,
            })
    user_obj[emp_id] = completed_tasks

    file_JSON = emp_id + ".json"
    with open(file_JSON, 'w') as fd:
        json.dump(user_obj, fd)
