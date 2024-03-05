#!/usr/bin/python3
"""how many subs"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """return number of subreddit subs"""
    header = {"User-Agent": "diet coke"}
    subs = get("https://www.reddit.com/r/{}/about.json".format(
        subreddit), headers=header).json()

    try:
        return subs.get("data").get("subscribers")
    except(Exception):
        return 0
