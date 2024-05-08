#!/usr/bin/python3

"""
    Prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the titles of the first
        10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    agent = {'User-agent': 'bhalut'}
    params = {'limit': 10}
    api_URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(api_URL, headers=agent, params=params)
    results = response.json()

    try:
        data = results.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
