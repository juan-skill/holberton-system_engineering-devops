#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """ retrieve the number of subscribers of a subreddit """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my-integration/1.2.3"}

    response = get(url=url, headers=headers)

    if response.status_code == 200:
        # print(response.json())

        response_json = response.json()
        data = response_json.get('data')
        subscribers = data.get("subscribers")

        return subscribers

    return 0
