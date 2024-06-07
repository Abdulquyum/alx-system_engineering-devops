#!/usr/bin/python3
''' queries the Reddit API
prints the titles of the first 10 hot posts listed '''


import requests


def top_ten(subreddit):
    ''' method to print titles of the first 10
    hot posts after query '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
            else:
                print("None")
    except Exception:
        print("None")
