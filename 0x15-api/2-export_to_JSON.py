#!/usr/bin/python3
""" Simple script to export data in the JSON format."""

from sys import argv
from requests import get
from json import dump


def export_to_json(eid=None):
    """export data in the JSON format"""

    url = "http://jsonplaceholder.typicode.com/users/{}".format(eid)
    response = get(url)
    response_json = response.json()
    username = response_json["username"]

    url = "http://jsonplaceholder.typicode.com/todos"
    response = get(url)
    response_json = response.json()

    list_tasks = []
    for task in response_json:
        if task["userId"] == int(eid):

            temp = {}
            temp["task"] = task["title"]
            temp["completed"] = task["completed"]
            temp["username"] = username

            list_tasks.append(temp)

    with open("{}.json".format(eid), 'w+') as file_obj:

        dump({eid: list_tasks}, file_obj)


if __name__ == "__main__":
    export_to_json(argv[1])
