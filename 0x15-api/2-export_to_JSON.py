#!/usr/bin/python3
"""export to json"""
import json
from requests import get
from sys import argv


def jsonWrite(user):
    """write to json"""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    olist = []
    for line in data:
        olist.append({"task": line.get('title'), "completed":
                        line.get('completed'), "username": name})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: olist}, f)


if __name__ == "__main__":
    jsonWrite(int(argv[1]))
