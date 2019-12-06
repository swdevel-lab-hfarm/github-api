import unittest
from main import parse_allowed_repos

class TestMain(unittest.TestCase):

    def test_no_datafile(self):
        u, r = parse_allowed_repos(datafile="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(u)
        self.assertFalse(r)
