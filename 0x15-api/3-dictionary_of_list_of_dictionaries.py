#!/usr/bin/python3
"""Saves information about all users TODO list progress into json file."""
import json
import requests

if __name__ == "__main__":
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({user.get('id'): [
            {
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            } for task in requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    user.get('id'))).json()
        ] for user in users}, jsonfile)
