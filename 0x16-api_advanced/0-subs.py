#!/usr/bin/python3
"""how many subs"""
from requests import get


def number_of_subscribers(subreddit):
    """return number of subreddit subs"""
    subs = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), allow_redirects=False)
    if subs.status_code >= 300:
        return 0
    return subs.json().get('data').get('subscribers')
