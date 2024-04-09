import requests
from collections import Counter
import re

def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles, 
    and prints a sorted count of given keywords (case-insensitive, delimited by spaces. 
    Javascript should count as javascript, but java should not).
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
            return count_words(subreddit, word_list, hot_list, after)
        else:
            # If the "after" value is None, count the occurrences of each word in the hot_list
            word_count = Counter(word.lower() for title in hot_list for word in re.findall(r'\\b{}\\b'.format('|'.join(word_list)), title, re.I))

            # Print the count of each word in descending order
            for word, count in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
                print(f"{word}: {count}")
    else:
        # If the subreddit is invalid, print nothing
        return None
