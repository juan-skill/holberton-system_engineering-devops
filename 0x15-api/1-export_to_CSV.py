#!/usr/bin/python3
""" Simple script export data in the CSV format."""

from sys import argv
from requests import get
import csv


def export_to_csv(eid=None):
    """Use REST API, for a given employee ID,
    returns information about his/her TODO list progress
    Args:1
        employee_id: id for each employee
    """
    url = "http://jsonplaceholder.typicode.com/users/{}".format(eid)
    response = get(url)
    response_json = response.json()

    username = response_json["username"]

    url2 = "http://jsonplaceholder.typicode.com/todos"
    response = get(url2)
    response_json = response.json()

    all_tasks = []
    for task in response_json:

        if task["userId"] == int(eid):
            temp = []
            temp.extend(
                (eid,
                 username,
                 task["completed"],
                 task["title"])
            )
            all_tasks.append(temp)

    file = "{}.csv".format(eid)
    with open(file, 'w+') as obj_file:

        write_obj = csv.writer(
            obj_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        write_obj.writerows(all_tasks)


if __name__ == "__main__":
    export_to_csv(argv[1])
