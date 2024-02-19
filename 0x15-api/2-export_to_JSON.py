#!/usr/bin/python3
"""Saves information about his/her TODO list progress into json file."""
import json
import requests
from sys import argv

if __name__ == "__main__" and argv[1]:
    get = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    response = get.json()
    username = response.get('username')
    get = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    response = get.json()
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        json.dump({argv[1]: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            } for task in response]}, jsonfile)
