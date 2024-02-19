#!/usr/bin/python3
"""Saves information about his/her TODO list progress into csv file."""
import csv
import requests
from sys import argv

if __name__ == "__main__" and argv[1]:
    get = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    response = get.json()
    name = response.get('username')
    get = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    response = get.json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [argv[1], name, task.get('completed'), task.get('title')]
            )
            for task in response]
