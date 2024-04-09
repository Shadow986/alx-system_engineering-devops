import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the headers to include a custom User-Agent
    headers = {"User-Agent": "python:subredditscraper:v1 (by /u/username)"}

    # Set the parameters to include the "after" parameter for pagination
    params = {"after": after}

    # Send a GET request to the URL
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the response status code is 200 (OK)
    if response.status_code == 200:
        # Get the list of posts from the JSON data in the response
        posts = response.json()["data"]["children"]

        # Add the title of each post to the hot_list
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Get the "after" value for pagination
        after = response.json()["data"]["after"]

        # If the "after" value is not None, call the function recursively with the "after" value
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            # If the "after" value is None, return the hot_list
            return hot_list
    else:
        # If the subreddit is invalid, return None
        return None
