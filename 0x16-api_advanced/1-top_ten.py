#!/usr/bin/pyhton3
""" queries the Reddit API
prints the titles of the first 10 hot posts listed
"""

import requests


def top_ten(subreddit):
    try:
        """method to print titles of the first 10
        hot posts after query"""
        url = f"https://www.reddit.com/r/{}/hot.json"
        req = requests.get(url, header={"user-Agents": "My ReddiBot"})
        data = req.json()
        titles = data["titles"]["hot post"]
        return titles
    except Exception as err:
        return None
