#!/usr/bin/python3
"""
Get a list of all hot posts titles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], idx=0):
    """Return a list of all hot posts titles for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Ubuntu:testing (by /u/ku18m)'
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        timeout=10
        )
    if response.status_code != 200:
        return None
    response = response.json().get('data').get('children')
    if idx == len(response):
        return hot_list
    hot_list.append(response[idx].get('data').get('title'))
    return recurse(subreddit, hot_list, idx + 1)
