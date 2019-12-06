import unittest
import github


class TestGithub(unittest.TestCase):

    def test_non_existing_repo(self):
        res = github.get_events("X", "Y")
        self.assertFalse(res)

    def test_empty_repo(self):
        res = github.get_events("", "")
        self.assertFalse(res)

    def test_mismatched_repo(self):
        res = github.get_events("swdevel-lab-hfarm", "birthdays")
        self.assertFalse(res)
