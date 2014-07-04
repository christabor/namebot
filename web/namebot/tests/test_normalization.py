import unittest
from namebot import normalization as norm


class removeOddWordTestCase(unittest.TestCase):
    def test_remove_odd_sounding_words(self):
        """Test four nonsense inputs that should get
        captured by the regexes."""
        original = ['vvvrrrmmnt', 'aaaeee', 'flower', 'rabbit']
        original_count = len(original)
        updated = norm.remove_odd_sounding_words(original)
        new_count = len(updated)
        print updated
        self.assertEqual(new_count, original_count - 2)

    def test_no_remove_odd_sounding_words(self):
        """Test bad inputs should not get removed."""
        original = ['flower', 'rabbit']
        original_count = len(original)
        updated = norm.remove_odd_sounding_words(original)
        new_count = len(updated)
        self.assertEqual(new_count, original_count)

    def test_none_remove_odd_sounding_words(self):
        """Tests that no input is returned without looping"""
        original = None
        updated = norm.remove_odd_sounding_words(original)
        self.assertEqual(updated, original)

    def test_empty_remove_odd_sounding_words(self):
        """Tests that empty list is returned without looping"""
        original = []
        updated = norm.remove_odd_sounding_words(original)
        self.assertEqual(len(original), 0)
        self.assertEqual(original, updated)


class stemWordsTestCase(unittest.TestCase):
    def test_stem_words(self):
        """Tests stemmer is working"""
        words = ['running', 'jumping']
        stemmed = norm.stem_words(words)
        self.assertEqual(['run', 'jump'], stemmed)

    def test_no_stem_words(self):
        """Tests stemmer is not stemming root words"""
        words = ['run', 'jump']
        stemmed = norm.stem_words(words)
        self.assertEqual(words, stemmed)


class removeBadWordsTestCase(unittest.TestCase):
    def test_stem_words(self):
        """Tests bad words are getting filtered out."""
        bad_words = ['fuck', 'pussy', 'cunt']
        words = bad_words + ['cool', 'neat', 'rad']
        cleaned = norm.remove_bad_words(words)
        self.assertNotEqual(bad_words, cleaned)
        for bad_word in bad_words:
            self.assertFalse(bad_word in cleaned)


class removeStopWords(unittest.TestCase):
    def test_filter_long_words(self):
        """Test that no stop words were kept"""
        stop_words = ['the', 'is', 'are', 'am', 'but']
        filtered = norm.remove_stop_words(stop_words)
        self.assertEqual(len(filtered), 0)


class filterWordsTestCase(unittest.TestCase):
    def test_filter_long_words(self):
        """Tests that very long words are filtered out"""
        long_words = ['areallyverylongword', 'anextrareallyverylongword']
        words = long_words + ['normal', 'words']
        filtered = norm.filter_words(words)
        for long_word in long_words:
            self.assertFalse(long_word in filtered)


class uniquifyTestCase(unittest.TestCase):
    def test_uniquify(self):
        words = ['cool', 'neat', 'cool', 'cool', 'neat']
        updated = norm.uniquify(words)
        self.assertEqual(len(updated), 2)


class cleanSortTestCase(unittest.TestCase):
    def test_clean_sort(self):
        words = ['!@foobar!#', 'ba3z!@#33_', 'bam!333____#33']
        cleaned = norm.clean_sort(words)
        self.assertEqual(cleaned, ['foobar', 'baz', 'bam'])

    def test_clean_string(self):
        val = '!@foobar!#'
        cleaned = norm.clean_sort(val)
        self.assertEqual(cleaned, val)
