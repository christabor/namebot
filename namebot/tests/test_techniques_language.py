import unittest
from namebot import techniques_language as tl


class LatinLookupTestCase(unittest.TestCase):

    def test_lookup_empty(self):
        self.assertEqual(tl.lookup_latin_word(''), [])

    def test_lookup_none(self):
        self.assertEqual(tl.lookup_latin_word(None), [])

    def test_lookup_basic(self):
        self.assertEqual(tl.lookup_latin_word('cool'), [['tepesco']])

    def test_lookup_basic_multi_results(self):
        self.assertEqual(
            tl.lookup_latin_word('elevate'),
            [['extollo'], ['attollo'], ['tollo', 'sustuli', 'sublatum']])

    def test_lookup_multiple_words(self):
        self.assertEqual(
            tl.lookup_latin_words(['cool', 'no-word']), [[['tepesco']], []])

    def test_lookup_multiple_words_empty(self):
        self.assertEqual(tl.lookup_latin_words([]), [])

    def test_lookup_multiple_words_none(self):
        self.assertEqual(tl.lookup_latin_words(None), [])

    def test_lookup_multiple_words_nested_results(self):
        results = tl.lookup_latin_words(['cool'])
        for result in results:
            self.assertIsInstance(result, list)
