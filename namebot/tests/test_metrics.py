import unittest
from namebot import metrics


class GetNamedNumbersTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_named_numbers_1_10(
            ['360 networks', 'Three Sixty networks'])
        self.assertEqual(res['data'], ['Three Sixty networks'])
        self.assertEqual(res['summary'], 'Of 2 words, 1 matched')


class NameLengthTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.name_length(['short', 'medium', 'veryveryverylong'])
        self.assertEqual(res['data'], [5, 6, 16])
        self.assertEqual(
            res['summary'], 'Of 3 words, the average length of names is...9.0')


class NameVowelCountTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.name_vowel_count(['neato'])
        self.assertEqual(res['data']['a'], 1)
        self.assertEqual(res['data']['e'], 1)
        self.assertEqual(res['data']['o'], 1)
        self.assertEqual(res['data']['i'], 0)


class NameStartsWithVowelTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.name_starts_with_vowel(['aardvark', 'apple', 'banana'])
        self.assertEqual(res['data'], None)
        self.assertEqual(
            res['summary'],
            'Of 3 words, 2 or 67.0% are vowels as the first letter.')

    def test_diff_percentage(self):
        words = ['aardvark', 'apple', 'banana', 'fruit', 'orange', 'grape']
        res = metrics.name_starts_with_vowel(words)
        self.assertEqual(res['data'], None)
        self.assertEqual(
            res['summary'],
            'Of 6 words, 3 or 50.0% are vowels as the first letter.')


class GetSearchResultsTestCase(unittest.TestCase):

    def test_basic(self):
        pass


class GetDigitsFrequencyTestCase(unittest.TestCase):

    def test_basic(self):
        msg = ('Of 3 words, 3 have numbers in them, with a'
               ' total of 5 numbers found.')
        res = metrics.get_digits_frequency(['7-11', '24/7Networks', '360corp'])
        self.assertEqual(res['data'], ['7', '11', '24', '7', '360'])
        self.assertEqual(res['summary'], msg)


class GetFirstLetterFrequencyTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_first_letter_frequency(['fjord', 'flower', 'apple'])
        self.assertEqual(res['data']['f'], 2)
        self.assertEqual(res['data']['a'], 1)


class GetSpecialCharsTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_special_chars(['de.li.c.ious', 'flip-to', 'bit.ly'])
        self.assertEqual(res['data'], ['.', '.', '.', '-', '.'])
        self.assertEqual(
            res['summary'],
            '5 occurrences of special characters were found in 3 words.')


class GetWordTypesTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_word_types(['apple', 'cat'])
        self.assertEqual(res['data'], [u'apple/NN', u'cat/NN'])


class GetNameSpacesTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_name_spaces(
            ['Itsy bitsy spider co', 'Nifty widgets, Inc'])
        self.assertEqual(res['data'][0]['spaces'], 4)
        self.assertEqual(res['data'][1]['spaces'], 3)


class GetConsonantRepeatFrequencyTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class GetConsonantDuplicateRepeatFrequencyTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_consonant_duplicate_repeat_frequency(
            ['cannon', 'fodder', 'grapple'])
        self.assertEqual(res['data'], 3)


class GetVowelRepeatFrequencyTestCase(unittest.TestCase):

    def test_basic(self):
        res = metrics.get_consonant_duplicate_repeat_frequency(
            ['food', 'beef', 'cheese'])
        self.assertEqual(res['data'], 3)


class GetAdjectiveVerbOrNounTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class GetKeywordRelevancyMapTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class CheckTrademarkRegistrationTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class CheckDomainSearchesTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class GetSearchResultCountTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass


class GetWordRankingTestCase(unittest.TestCase):
    # TODO

    def test_basic(self):
        pass
