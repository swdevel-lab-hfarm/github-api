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

    def test_correct_repo(self):
        res = github.get_events("swdevel-lab-h-farm-2019", "birthdays")
        self.assertTrue(res)



class TestAnalyser(unittest.TestCase):

    def testValid(self):
        event_list = [
            {'actor': {'login': 'u1'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u2'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u3'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u4'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u5'},
                'created_at': '2019-12-04T15:26:58Z'},
            ]
        oe, lm = github.analyse_events(event_list)
        self.assertEqual(oe, 1)
        self.assertEqual(lm, 1)

    def testEmpty(self):
        oe, lm = github.analyse_events([])
        self.assertFalse(oe)
        self.assertFalse(lm)

    def testEdge(self):
        event_list = [
            {'actor': {'login': 'u1'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u1'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'u1'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            ]
        oe, lm = github.analyse_events(event_list)
        self.assertEqual(oe, 0.5)
        self.assertEqual(lm, 1)

    def testCorner(self):
        event_list = [
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            {'actor': {'login': 'swdevel-lab-hfarm'},
                'created_at': '2019-12-04T15:26:58Z'},
            ]
        oe, lm = github.analyse_events(event_list)
        self.assertEqual(oe, 0)
        self.assertEqual(lm, 1)
