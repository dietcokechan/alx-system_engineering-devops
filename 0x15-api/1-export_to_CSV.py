#!/usr/bin/python3
"""export to csv"""
import csv
from requests import get
from sys import argv


def cvsWrite(user):
    """write to csv"""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    employ_data = open('{}.csv'.format(user), 'w')
    csvw = csv.writer(employ_data, quoting=csv.QUOTE_ALL)
    for line in data:
        lined = [line.get('userId'), name,
                 line.get('completed'), line.get('title')]
        csvw.writerow(lined)
    employ_data.close()


if __name__ == "__main__":
    cvsWrite(argv[1])
