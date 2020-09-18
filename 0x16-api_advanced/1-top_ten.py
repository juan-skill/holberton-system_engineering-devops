#!/usr/bin/python3
""" prints the titles of the first 10 hot posts
    listed for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
        listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "hola-tu"}
    payload = {"limit": 10}

    response = get(url=url, headers=headers, params=payload)

    if response.status_code == 200:

        response_json = response.json()

        data = response_json.get("data")
        children = data.get("children")

        if children:
            for data in children:
                data2 = data.get("data")
                title = data2.get("title")
                print(title)
    else:
        print(None)
