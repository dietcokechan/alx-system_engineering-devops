#!/usr/bin/python3
"""recurse it"""
from requests import get


def recurse(subreddit, hotposts=[], after=None):
    """recurse it"""
    try:
        if after:
            posts = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after)).json().get('data')
        else:
            posts = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit)).json().get('data')

        hotposts += [d.get('data').get('title') for d in posts.get('children')]
        if posts.get('after'):
            return recurse(subreddit, hotposts, after=posts.get('after'))
        return hotposts
    except Exception:
        return None
