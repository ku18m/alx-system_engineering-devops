#!/usr/bin/python3
# returns information about his/her TODO list progress.
import requests
from sys import argv

if __name__ == "__main__" and argv[1]:
    get = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    response = get.json()
    name = response.get('name')
    get = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    response = get.json()
    total = len(response)
    done = [task for task in response if task.get('completed') is True]
    print(
        'Employee {} is done with tasks({}/{}):'.format(
            name, len(done), total))
    [print('\t {}'.format(task.get('title'))) for task in done]
