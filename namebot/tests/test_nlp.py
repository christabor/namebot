import unittest
from namebot import nlp


class NLPTestCase(unittest.TestCase):

    def test_create_synset_basic(self):
        res = nlp.get_synsets(words=['potato'])
        self.assertIsInstance(res, dict)
        for synset, vals in res.iteritems():
            self.assertIsInstance(vals, dict)
            self.assertIsNotNone(synset)
            self.assertIsNotNone(vals)
