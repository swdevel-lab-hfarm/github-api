from github import get_events

user = 'swdevel-lab-hfarm'
repo = 'example'

ev = get_events(user, repo)
print(ev)
