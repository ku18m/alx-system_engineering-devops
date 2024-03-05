#!/usr/bin/python3
"""
Get and print Top 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Get and print Top 10 hot posts for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Ubuntu:testing (by /u/ku18m)'
    }
    response = requests.get(
        url, headers=headers, allow_redirects=False, timeout=10)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get('data').get('children')[:10]:
        print(post.get('data').get('title'))
