import requests
import json
from collections import defaultdict
import datetime

github_URL = "https://api.github.com/repos/%s/%s/events"


def get_modification_day(date_string):
    dt = datetime.datetime.strptime(date_string[:10], "%Y-%m-%d")
    now = datetime.datetime.now()
    return (now-dt).days


def analyse_events(event_list):
    """ returns the percentage of events in the last month,
        and the percentage of events from students. """
    events_author = defaultdict(int)
    events_time = []
    for event in event_list:
        events_author[event['actor']['login']] += 1
        events_time.append(get_modification_day(event['created_at']))
    non_owner_events = 0
    tot_events = 0
    for author, ev_number in events_author.items():
        tot_events += ev_number
        if author not in ["swdevel-lab-h-farm-2019", "swdevel-lab-hfarm"]:
            non_owner_events += ev_number
    last_month_events = 0
    for w in events_time:
        if w < 30:
            last_month_events += 1
    if tot_events:
        return non_owner_events/tot_events, last_month_events/tot_events
    else:
        return 0, 0


def get_events(user, repo, verbose=False):
    url = github_URL % (user, repo)
    if verbose:
        print("Trying to fetch the data from the API")
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        if verbose:
            print("Successfully fetched data")
        list_of_events = json.loads(r.text)
        oe, lme = analyse_events(list_of_events)
        if oe > 0.5:
            print("More than half of the events were from students")
        if lme > 0.5:
            print("More than half of the events were in the last month")
        return len(list_of_events)
    print("Could not find the given repository: {}".format(url))
    return 0
