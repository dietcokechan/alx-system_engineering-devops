#!/usr/bin/python3
"""count it"""
from requests import get


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """count it"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "Diet Coke"
    }
    options = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = get(url, headers=header, params=options,
                            allow_redirects=False)
    try:
        words = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    words = words.get("data")
    after = words.get("after")
    count += words.get("dist")
    for i in words.get("children"):
        title = i.get("data").get("title").lower().split()
        for j in word_list:
            if j.lower() in title:
                n = len([t for t in title if t == j.lower()])
                if instances.get(j) is None:
                    instances[j] = n
                else:
                    instances[j] += n

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
