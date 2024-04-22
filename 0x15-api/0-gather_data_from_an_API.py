#!/usr/bin/python3
"""
    A Script that, uses this REST API, for a given employee ID, returns
    information about his/her TODO list progress
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
    employee_name = req.get(user)

    employee_tasks = tasks.json()
    employee_name = employee_name.json()['name']

    completed_tasks = 0

    for task in employee_tasks:
        if task['completed']:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, completed_tasks, len(employee_tasks)))

    for task in employee_tasks:
        if task['completed']:
            print("\t " + task.get('title'))
