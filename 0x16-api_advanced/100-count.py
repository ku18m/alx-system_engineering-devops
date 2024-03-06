#!/usr/bin/python3
"""
Get a list of all hot posts titles for a given subreddit
"""
import requests


def count_words(subreddit, word_list, idx=0, word_count={}):
    """
    Count words of given list in all hot posts titles for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return
    if word_list is None or type(word_list) is not list:
        return
    word_list = [word.lower() for word in word_list]
    word_list = sorted(list(set(word_list)))
    if word_count == {}:
        word_count = {word: 0 for word in word_list}
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
        return
    response = response.json().get('data').get('children')
    if idx == len(response):
        for key, value in word_count.items():
            print('{}: {}'.format(key, value))
        return
    title = response[idx].get('data').get('title').split()
    print(title)
    for word in word_list:
        if word.lower() in [word.lower() for word in title]:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return count_words(subreddit, word_list, idx + 1, word_count)
