import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set the headers to include a custom User-Agent
    headers = {"User-Agent": "python:subredditscraper:v1 (by /u/username)"}

    # Send a GET request to the URL
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response status code is 200 (OK)
    if response.status_code == 200:
        # Get the list of posts from the JSON data in the response
        posts = response.json()["data"]["children"]

        # Print the title of each post
        for post in posts:
            print(post["data"]["title"])
    else:
        # If the subreddit is invalid, print None
        print(None)
