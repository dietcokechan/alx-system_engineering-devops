#!/usr/bin/python3
"""dictionary of list of dictionaries"""
import json
from requests import get
from sys import argv


def jsonWrite():
    """write to json"""
    data = get('https://jsonplaceholder.typicode.com/users').json()
    ids = [(dic.get('id'), dic.get('username')) for dic in data]
    dumped = {}
    for person in ids:
        data = get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                person[0])).json()
        olist = [{"task": line.get('title'), "completed":
                 line.get('completed'), "username":
                 person[1]} for line in data]
        dumped[person[0]] = olist
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dumped, f)


if __name__ == "__main__":
    jsonWrite()