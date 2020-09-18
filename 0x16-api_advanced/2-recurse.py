#!/usr/bin/python3
""" returns a list containing the titles of all hot
    articles for a given subreddit
"""

from requests import get


def recurse(subreddit, after=None, hot_list=[]):
    """ returns a list containing the titles of all hot
        articles for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {"User-Agent": "hola"}
    payload = {"after": after}
    response = get(url=url, headers=headers, params=payload)

    if response.status_code == 200:
        n_after = response.json().get('data').get('after')

        children = response.json().get('data').get('children')

        for data in children:
            hot_list.append(data.get('data').get('title'))

        if n_after:
            return recurse(subreddit, n_after, hot_list)

        else:
            return hot_list

    else:
        return None
