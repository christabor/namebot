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


class ScoringLengthTestCase(unittest.TestCase):

    def test_score_length1(self):
        self.assertEqual(sc.score_length('a really long company name'), 1)

    def test_score_length2(self):
        self.assertEqual(sc.score_length('somewhat long name'), 2)

    def test_score_length3(self):
        self.assertEqual(sc.score_length('name'), 3)

    def test_score_length4(self):
        self.assertEqual(sc.score_length('western digital'), 4)

    def test_score_length5(self):
        self.assertEqual(sc.score_length('facebook'), 5)

    def test_score_length_empty(self):
        self.assertEqual(sc.score_length(''), 0)

    def test_score_length_none(self):
        self.assertEqual(sc.score_length(None), 0)


class ScoringPronounceabilityTestCase(unittest.TestCase):

    def test_score_pronounce_no_vowels(self):
        self.assertEqual(sc.score_pronounceability('vry bd wrd'), 0)

    def test_score_pronounce1(self):
        self.assertEqual(sc.score_pronounceability('ths vry bad wrd'), 1)

    def test_score_pronounce2(self):
        self.assertEqual(sc.score_pronounceability('bd word'), 2)

    def test_score_pronounce3(self):
        self.assertEqual(sc.score_pronounceability('CVS health'), 3)

    def test_score_pronounce4(self):
        self.assertEqual(sc.score_pronounceability('chevron'), 4)

    def test_score_pronounce5(self):
        self.assertEqual(sc.score_pronounceability('google'), 5)

    def test_score_pronounce_empty(self):
        self.assertEqual(sc.score_pronounceability(''), 0)

    def test_score_pronounce_none(self):
        self.assertEqual(sc.score_pronounceability(None), 0)


class ScoringSimplicityTestCase(unittest.TestCase):

    def test_score_simple1(self):
        self.assertEqual(sc.score_simplicity('a very poor name indeed'), 1)

    def test_score_simple2(self):
        self.assertEqual(sc.score_simplicity('not all that great'), 2)

    def test_score_simple3(self):
        self.assertEqual(sc.score_simplicity('not so perfect'), 3)

    def test_score_simple4(self):
        self.assertEqual(sc.score_simplicity('not perfect'), 4)

    def test_score_simple5(self):
        self.assertEqual(sc.score_simplicity('perfect'), 5)

    def test_score_simple_empty(self):
        self.assertEqual(sc.score_simplicity(''), 0)

    def test_score_simple_none(self):
        self.assertEqual(sc.score_simplicity(None), 0)


class ScoringOverallTestCase(unittest.TestCase):

    def test_score_overall_low(self):
        self.assertEqual(sc.score_name_overall('not vry grt n4m3'), 40.0)

    def test_score_overall_mid(self):
        self.assertEqual(sc.score_name_overall('CVS Health'), 80.0)

    def test_score_overall_high(self):
        self.assertEqual(sc.score_name_overall('google'), 100.0)

    def test_score_overall_empty(self):
        self.assertEqual(sc.score_simplicity(''), 0)

    def test_score_overall_none(self):
        self.assertEqual(sc.score_simplicity(None), 0)

    def test_scores_overall(self):
        self.assertIsInstance(sc.score_names_overall(
            ['google', 'microsoft', 'apple']), list)
