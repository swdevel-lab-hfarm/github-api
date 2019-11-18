import argparse
import csv
from github import get_events
default_datafile = 'data/allowed_repos.csv'

def parse_allowed_repos(datafile=default_datafile):
    usernames = set()
    repositories = set()
    with open(datafile) as repo_data:
        csv_reader = csv.reader(repo_data, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            usernames.add(row[0])
            repositories.add(row[1])
    return usernames, repositories


def parse_arguments(usernames, repositories):
    parser = argparse.ArgumentParser()
    parser.add_argument("reponame",
                        help="The name of the repository",
                        choices=repositories)
    parser.add_argument("-u", required=True,
                        help="The username of the github user/organization",
                        choices=usernames)
    parser.add_argument("-v", help="Be more verbose", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    usernames, repositories = parse_allowed_repos()
    args = parse_arguments(usernames, repositories)
    ev = get_events(args.u, args.reponame, args.v)
    print('Repository "{}" from user "{}" has {} events.'.format(args.reponame,
                                                                 args.u,
                                                                 ev))
