#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


BASE_URL = 'https://www.reddit.com'
"""The base API URL."""


def number_of_subscribers(subreddit):
    """
        Retrieves the number of subscribers in a given subreddit.
    """
    call_header = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    response = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=call_header,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
