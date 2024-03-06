#!/usr/bin/python3
"""count it"""
from requests import get

hotposts = []
after = None


def count_all(hotposts, word_list):
    dic = {word.lower(): 0 for word in word_list}
    for post in hotposts:
        words = post.split(' ')
        for word in words:
            if dic.get(word) is not None:
                dic[word] += 1

    for i in sorted(dic, key=dic.get, reverse=True):
        if dic.get(i):
            for j in word_list:
                if i == j.lower():
                    print("{}: {}".format(j, dic[i]))


def count_words(subreddit, word_list):
    global hotposts
    global after
    """count it"""
    head = {'User-Agent': 'Diet Coke'}
    if after:
        count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=head,
            allow_redirects=False).json().get('data')
    else:
        count = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=head,
            allow_redirects=False).json().get('data')
    hotposts += [dic.get('data').get('title').lower()
                for dic in count.get('children')]
    after = count.get('after')
    if after:
        return count_words(subreddit, word_list)
    return count_all(hotposts, word_list)
