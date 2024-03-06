#!/usr/bin/python3
"""top ten"""
from requests import get


def top_ten(subreddit):
    """get top ten"""
    try:
        posts = get('https://www.reddit.com/r/{}/hot.json?count=10'.format(
            subreddit)).json().get('data').get('children')
        print('\n'.join([p.get('data').get('title')
                        for p in posts][:10]))
    except Exception:
        print("None")
