"""NLP module tests."""

import unittest

from namebot import nlp


class NLPTestCase(unittest.TestCase):

    def test_create_synset_basic(self):
        res = nlp.get_synsets(['potato'])
        self.assertIsInstance(res, dict)
        for synset, vals in res.iteritems():
            self.assertIsInstance(vals, dict)
            self.assertIsNotNone(synset)
            self.assertIsNotNone(vals)

    def test_get_synsets_definitions(self):
        res = nlp.get_synsets_definitions(['potato'])
        self.assertIsInstance(res, list)
        self.assertGreater(len(res), 0)

    def test_get_verb_lemmas(self):
        res = nlp.get_verb_lemmas(['flying', 'crying', 'dying'])
        self.assertGreater(len(res), 0)
        for word in res:
            self.assertIsInstance(word, unicode)

    def test_get_verb_lemmas_noverbs(self):
        res = nlp.get_verb_lemmas(['cat', 'dog', 'parrot'])
        self.assertEqual(len(res), 0)


class GetSynsetWordsTestCase(unittest.TestCase):

    def test_get_words_basic(self):
        res = nlp._get_synset_words('cat')
        self.assertIsInstance(res, list)
