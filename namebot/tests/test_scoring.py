import unittest
from namebot import scoring as sc


class ScoringTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.words = ['cat', 'dog', 'rabbit', 'giraffe', 'potato']

    def test_score_dmetaphone_basic(self):
        self.assertIsInstance(sc.score_dmetaphone(self.words), list)

    def test_score_nysiis_basic(self):
        self.assertIsInstance(sc.score_nysiis(self.words), list)

    def test_score_soundex_basic(self):
        # TODO
        pass

    def test_generate_all_scoring_basic(self):
        # TODO
        pass
