#!/usr/bin/python3
""" gathers data from API
"""

from requests import get
from sys import argv


def get_name_request(employe_id=None):
    """ gathers task data from employee """
    # print('employe_id: {}'.format(employe_id))

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employe_id)
    # print("url: {}".format(user_url))

    user_response = get(user_url)
    # print("response JSON representation: {}".format(user_response.json()))

    employee_name = user_response.json().get('name')
    # print('employee_name: {}'.format(employee_name))

    return employee_name


def get_task_request(employe_id=None):
    """ gathers task data from employee """
    # print('employe_id: {}'.format(employe_id))

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employe_id)
    # print("url: {}".format(todos_url))

    todos_response = get(todos_url)
    # print("response JSON representation: {}".format(todos_response.json()))

    return todos_response.json()


def count_data(employee_id=None, task_list=[]):
    """ Counts number of task """

    total_task = 0
    list_tasks = []
    for item in task_list:

        if item["userId"] == employee_id:
            total_task += 1

            if item["completed"]:
                list_tasks.append(item["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(list_tasks), total_task))

    for itask in list_tasks:
        print("\t {}".format(itask))


if __name__ == '__main__':

    name = get_name_request((int(argv[1])))
    tasks = get_task_request((int(argv[1])))

    count_data((int(argv[1])), tasks)
