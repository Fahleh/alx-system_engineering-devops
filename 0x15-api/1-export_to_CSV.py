#!/usr/bin/python3
"""
    A Script that, uses a REST API to return an employee's details,
    and exports their data in the CSV format.
"""

import csv
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

    completed_tasks = 0

    for task in employee_tasks:
        if task['completed']:
            completed_tasks += 1

    CSV_file = emp_id + '.csv'

    with open(CSV_file, "w", newline='') as csvFile:
        write = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in employee_tasks:
            write.writerow([emp_id, employee,
                            t.get('completed'), t.get('title')])
