#!/usr/bin/python3
"""
    Queries the Reddit API and returns a list containing the 
    titles of all hot articles for a given subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns top ten post titles recursively"""
    global after

    agent = {'User-Agent': 'api_advanced-project'}
    api_URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    res = requests.get(api_URL, params=parameters, headers=agent,
                           allow_redirects=False)

    if res.status_code == 200:
        after_list = res.json().get("data").get("after")
        if after_list is not None:
            after = after_list
            recurse(subreddit, hot_list)
        titles = res.json().get("data").get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
