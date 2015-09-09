import unittest
from namebot import strainer as strain


class FilterLengthTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.words = ['reallylongwordnojoke', 'reallylongword',
                     'foo', 'bar', 'baz', 'regular',
                     'words', 'are', 'good', 'for', 'you']

    def test_no_filter(self):
        """Basic sanity test - no filtering should be done."""
        strained = [word for word in self.words
                    if strain.filter_length(
                        word, min_length=0, max_length=99999)]
        self.assertEqual(len(self.words), len(strained))

    def test_min_length(self):
        """Tests filtering function for length"""
        strained = [word for word in self.words
                    if strain.filter_length(
                        word, min_length=4, max_length=999)]
        self.assertEqual(len(strained), 5)

    def test_max_length(self):
        """Tests filtering function for length"""
        strained = [word for word in self.words
                    if strain.filter_length(
                        word, min_length=0, max_length=3)]
        self.assertEqual(len(strained), 6)


class FilterStartsEndsWithTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = ['banana', 'baseball', 'brain',
                     'cat', 'phone', '', 'grape']

    def test_startswith(self):
        """Test if a word starts with a specific letter"""
        strained = [word for word in self.words
                    if strain.filter_startswith(word, beginning='b')]
        self.assertEqual(len(strained), 3)

    def test_endswith(self):
        """Test if a word ends with a specific letter"""
        strained = [word for word in self.words
                    if strain.filter_endswith(word, ending='e')]
        self.assertEqual(len(strained), 2)


class FilterVowelConsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = ['chrysanthemum', 'younker', 'overalcoholizing',
                     'refrigeration', 'bagpiped', 'ossianic', 'intermittence',
                     'huneker', 'cherty', 'sustainingly']

    def _getfunc(self, ratio):
        # Partially apply the argument for use with `filter`
        def func(word):
            return strain.filter_vowel_cons_ratio(word, ratio)
        return func

    def test_no_divbyzero_error(self):
        for n in range(1, 10):
            ratio = n * 0.1
            func = self._getfunc(ratio)
            res = filter(func, self.words)
        # Assert this was filtered, to some degre
        # (except 0.0, which is no filtering.)
        self.assertLess(len(res), len(self.words))
        self.assertIsInstance(res, list)

    def test_nofilter(self):
        func = self._getfunc(0.0)
        res = filter(func, self.words)
        self.assertEqual(len(res), len(self.words))
        self.assertIsInstance(res, list)


class FilterMetaphoneTestCase(unittest.TestCase):
    def test_bad_pronunciation(self):
        # TODO
        pass


class FilterSoundexTestCase(unittest.TestCase):
    def test_soundex(self):
        # TODO
        pass


class FilterNysiisTestCase(unittest.TestCase):
    def test_nysiis(self):
        # TODO
        pass
