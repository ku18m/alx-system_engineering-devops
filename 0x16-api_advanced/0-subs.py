#!/usr/bin/python3
"""
Get number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers for a given subreddit"""
    if not subreddit or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Ubuntu:testing (by /u/ku18m)'
    }
    response = requests.get(
        url, headers=headers, allow_redirects=False, timeout=10)
    return response.json().get('data', {}).get('subscribers', 0)
