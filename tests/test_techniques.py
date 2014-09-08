import unittest
from namebot import techniques


class SpoonerismTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.spoonerism(['flim', 'boom', 'dang', 'dune']),
            ['blim foom', 'doom bang', 'dang dune'])

    def test_single_word(self):
        with self.assertRaises(techniques.InsufficientWordsError):
            self.assertEqual(techniques.spoonerism(['foo']))


class KniferismTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.kniferism(['flim', 'boom', 'dang', 'dune']),
            ['flom boim', 'bonm daog', 'dang dune'])

    def test_single_word(self):
        with self.assertRaises(techniques.InsufficientWordsError):
            self.assertEqual(techniques.kniferism(['foo']))


class ForkerismTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.forkerism(['flim', 'boom', 'dang', 'dune']),
            ['flim boom', 'boog danm', 'dane dung'])

    def test_single_word(self):
        with self.assertRaises(techniques.InsufficientWordsError):
            self.assertEqual(techniques.forkerism(['foo']))


class ReduplicationAblautTestCase(unittest.TestCase):

    def test_vowel_a(self):
        self.assertEqual(techniques.reduplication_ablaut(
            ['cat', 'dog'], random=False, vowel='a'), ['dog dag'])

    def test_vowel_e(self):
        self.assertEqual(techniques.reduplication_ablaut(
            ['cat', 'dog'], random=False, vowel='e'),
            ['cat cet', 'dog deg'])

    def test_vowel_i(self):
        self.assertEqual(techniques.reduplication_ablaut(
            ['cat', 'dog'], random=False, vowel='i'),
            ['cat cit', 'dog dig'])

    def test_vowel_o(self):
        self.assertEqual(techniques.reduplication_ablaut(
            ['cat', 'dog'], random=False, vowel='o'), ['cat cot'])

    def test_vowel_u(self):
        self.assertEqual(techniques.reduplication_ablaut(
            ['cat', 'dog'], random=False, vowel='u'),
            ['cat cut', 'dog dug'])


class AffixWordsTestCase(unittest.TestCase):

    def setUp(self):
        self.words = ['shop']

    def test_prefix(self):
        res = techniques.affix_words(self.words, 'prefix')
        self.assertEqual(res[:3], ['ennishop', 'epishop', 'equishop'])

    def test_suffix(self):
        res = techniques.affix_words(self.words, 'suffix')
        self.assertEqual(res[:3], ['shopage', 'shopable', 'shopible'])

    def test_duplifix(self):
        res = techniques.affix_words(self.words, 'duplifix')
        print res, '< ------- RES'
        self.assertEqual(res[:3], [])

    def test_infix(self):
        # TODO
        pass

    def test_disfix(self):
        # TODO
        pass


class MakeFounderProductNameTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.make_founder_product_name(
                'Foo', 'Bar', 'Goods'), 'F & B Goods')

    def test_simple_lowercase(self):
        self.assertNotEqual(
            techniques.make_founder_product_name(
                'Foo', 'Bar', 'Goods'), 'foo bar & co goods')


class MakeNameObscuredTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class MakeCCtoVCSwapTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class MakeNameAlliterationTestCase(unittest.TestCase):

    def test_simple(self):
        original = ['jamba', 'juice', 'dancing', 'tornado',
                    'disco', 'wicked', 'tomato']
        updated = ['dancing disco', 'disco dancing', 'jamba juice',
                   'juice jamba', 'tomato tornado', 'tornado tomato']
        self.assertEqual(
            techniques.make_name_alliteration(original), updated)


class MakeNameAbbreviationTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.make_name_abbreviation(
                ['Badische', 'Anilin', 'Soda', 'Fabrik']), 'BASF')


class MakeVowelTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass

    def test_no_substring(self):
        """Checks for values that aren't found in the regex list."""
        pass


class MakePortmanteauDefaultVowelTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.make_portmanteau_default_vowel(
                ['sweet', 'potato', 'nifty', 'gadget', 'widgets']),
            ['potadget', 'gadgeet', 'widgeet'])


class MakemakePortmanteauSplitTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class MakePunctuatorTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        self.assertEqual(
            techniques.make_punctuator(['delicious'], 'i'),
            ['deli-ci-ous', 'deli.ci.ous'])


class MakeVowelifyTestCase(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            techniques.make_vowelify(
                ['nautical', 'monster']), ['nautica', 'monste'])


class MakemisspellingTestCase(unittest.TestCase):
    # TODO
    def setUp(self):
        self.words = ['shop', 'effects']

    def test_simple(self):
        self.assertEqual(
            techniques.make_misspelling(self.words)[:6],
            ['shop', 'zhop', 'shoffp', 'ephphects', 'effects', 'shoughp'])


class MakeNameFromLatinRootTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class PigLatinTestCase(unittest.TestCase):

    def test_simple(self):
        """Basic test."""
        self.assertEqual(
            techniques.pig_latinize('rad'), 'adray')

    def test_custom_postfix_value(self):
        """Basic test."""
        self.assertEqual(
            techniques.pig_latinize('rad', postfix='ey'), 'adrey')

    def test_bad_postfix_value(self):
        """Basic test."""
        with self.assertRaises(TypeError):
            techniques.pig_latinize('rad', postfix=1223)


class MakeWordMetaphorTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class MakePhraseTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class GetDescriptorsTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class MakeDescriptorsTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass


class SuperScrubTestCase(unittest.TestCase):
    # TODO

    def test_simple(self):
        pass
