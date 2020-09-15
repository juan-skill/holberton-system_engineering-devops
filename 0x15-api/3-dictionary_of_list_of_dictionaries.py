#!/usr/bin/python3
""" script to export data in the JSON format """


from json import dump
from requests import get


def export_data_in_the_json():
    """script to export data in the JSON format"""

    url = "http://jsonplaceholder.typicode.com/users"
    response = get(url)
    users = response.json()

    my_big_dic = {}

    for iuser in users:

        eid = iuser["id"]
        username = iuser["username"]

        url = "http://jsonplaceholder.typicode.com/todos"
        response = get("{}?userId={}".format(url, eid))
        tasks = response.json()

        list_tasks = []
        for itask in tasks:

            temp = {}
            temp["task"] = itask["title"]
            temp["completed"] = itask["completed"]
            temp["username"] = username
            list_tasks.append(temp)

        my_big_dic[eid] = list_tasks

    file = "todo_all_employees.json"
    with open(file, 'w+') as file_obj:

        dump(my_big_dic, file_obj)


if __name__ == "__main__":
    export_data_in_the_json()
