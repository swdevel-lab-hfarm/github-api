from github import get_events
import sys

if len(sys.argv) == 3:
    user = sys.argv[1]
    repo = sys.argv[2]
else:
    print("Please run the program like: python3 main.py username reponame")
    exit()

ev = get_events(user, repo)
print('Repository "{}" from user "{}" has {} events.'.format(repo, user, ev))
