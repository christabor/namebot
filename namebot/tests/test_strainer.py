import unittest
from namebot.namebot  import strainer as strain


class FilterLengthTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.words = ['reallylongwordnojoke', 'reallylongword',
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
    def setUpClass(self):
        self.words = ['banana', 'baseball', 'brain',
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
