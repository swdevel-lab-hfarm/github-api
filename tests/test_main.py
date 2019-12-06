import unittest
from main import parse_allowed_repos
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        # note: this would be better done with tempfile
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        u, r = parse_allowed_repos(datafile="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(u)
        self.assertFalse(r)

    def test_empty_datafie(self):
        u, r = parse_allowed_repos(datafile=self.temporary_file)
        self.assertFalse(u)
        self.assertFalse(r)

    def tearDown(self):
        os.remove(self.temporary_file)

