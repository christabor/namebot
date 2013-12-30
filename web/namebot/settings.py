"""
=============================
NAMEBOT SETTINGS:
=============================

print conventions: use the name of
function you are printing and a colon
after the returned object,

"""

import re

MAX_LENGTH = 13
MIN_LENGTH = 4
SPACED_MAX_LENGTH = 22
TEST_DATA = [
    'chicken', 'flowers', 'computers',
    'anthropology', 'disaster', 'interest',
    'cats', 'burritos', 'communicate',
    'rebel', 'cried', 'more', 'devil', 'hour',
    'space', 'flame', 'rabbit', 'neat',
    'christmas', 'because', 'midnight',
    'sovereign', 'space', 'indeed', 'tiger']

regex = {
    'all_vowels': re.compile(r'a|e|i|o|u'),
    'vowels': re.compile(r'/[aeiou{1}]/'),
    'consonants': re.compile(r'/[qwrtypsdfghjklzxcvbnm{1}]/'),
}
