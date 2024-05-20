#!/usr/bin/python3
""" This script gathers data from a REST API for a given employee ID and
returns information about their TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = ("https://jsonplaceholder.typicode.com/users/{}"
                .format(employee_id))
    user_response = requests.get(user_url).json()
    employee_name = user_response.get("name")

    todos_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                 .format(employee_id))
    todos_response = requests.get(todos_url).json()

    total_tasks = len(todos_response)
    done_tasks = [task for task in todos_response if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
