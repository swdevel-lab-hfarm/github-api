import argparse
from github import get_events
valid_usernames = ['swdevel-lab-hfarm', 'swdevel-lab-h-farm-2019']


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("reponame", 
                        help="The name of the repository")
    parser.add_argument("-u", required=True, 
                        help="The username of the github user/organization",
                        choices = valid_usernames)
    parser.add_argument("-v", help="Be more verbose", action="store_true")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    ev = get_events(args.u, args.reponame, args.v)
    print('Repository "{}" from user "{}" has {} events.'.format(args.reponame,
                                                                 args.u,
                                                                 ev))
