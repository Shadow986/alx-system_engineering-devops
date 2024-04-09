#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the headers to include a custom User-Agent
    headers = {"User-Agent": "python:subredditscraper:v1 (by /u/username)"}

    # Send a GET request to the URL
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response status code is 200 (OK)
    if response.status_code == 200:
        # Return the number of subscribers
        return response.json()["data"]["subscribers"]
    else:
        # If the subreddit is invalid, return 0
        return 0

