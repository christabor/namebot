import unittest
from namebot import techniques


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
