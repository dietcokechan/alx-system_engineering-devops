#!/usr/bin/python3
"""how many subs"""
from requests import get


def number_of_subscribers(subreddit):
    """return number of subreddit subs"""
    subs = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), allow_redirects=False).json()
    try:
        return subs.get('data').get('subscribers')
    except Exception:
        return 0
