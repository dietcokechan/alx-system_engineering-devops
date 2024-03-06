#!/usr/bin/python3
"""top ten"""
from requests import get


def top_ten(subreddit):
    """get top ten"""
    header = {'User-Agent': 'Diet Coke'}
    try:
        posts = get('https://www.reddit.com/r/{}/hot.json?count=10'
                    .format(subreddit),
                    allow_redirects=False,
                    headers=header).json().get('data').get('children')
        print('\n'.join([p.get('data').get('title')
                        for p in posts]))
    except Exception:
        print("None")
