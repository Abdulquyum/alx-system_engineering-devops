#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers
'''


import requests


def number_of_subscribers(subreddit):
    """ method to query the Reddit API
    and returns the number of subscribers
    if none return 0 """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        req = requests.get(url, headers={"User-Agent": "MyRedditBot"})
        data = req.json()
        subscribers = data["data"]["subscribers"]
        return subcribers
    except Exception as err:
        return 0
