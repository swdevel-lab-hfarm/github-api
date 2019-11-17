import requests
import json

github_URL = "https://api.github.com/repos/%s/%s/events"


def get_events(user, repo):
    url = github_URL % (user, repo)
    r = requests.get(url)
    list_of_events = len(json.loads(r.text))
    return list_of_events
