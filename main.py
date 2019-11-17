import argparse
from github import get_events

parser = argparse.ArgumentParser()
parser.add_argument("username", 
                    help="The username of the github user/organization")
parser.add_argument("reponame", 
                    help="The name of the repository")
parser.add_argument("-v", help="Be more verbose", action="store_true")
args = parser.parse_args()

ev = get_events(user, repo)
print('Repository "{}" from user "{}" has {} events.'.format(repo, user, ev))
