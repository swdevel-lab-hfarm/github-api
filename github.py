import requests
import json

github_URL = "https://api.github.com/repos/%s/%s/events"

def get_events(user, repo, verbose=False):
    url = github_URL % (user, repo)
    if verbose:
        print("Trying to fetch the data from the API")
    r = requests.get(url)
    if verbose:
        print("Successfully fetched data")
    list_of_events = len(json.loads(r.text))
    return list_of_events