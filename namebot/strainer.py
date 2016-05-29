"""Provides filtering functions for reducing large sets of generated words.

Recommended usage: filtered results using a list comprehension
of all filters 'anded' together.
e.g:

>>> filtered = [word for word in words if
            filter_length(word, max_length=7) and
            filter_startswith(word, beginning='c') and
            filter_startswith(word, beginning='c') and
            filter_endswith(word, ending='e') ...]
"""

from __future__ import absolute_import

import re

from . import scoring
from . import settings as namebot_settings


def filter_vowel_cons_ratio(word, ratio=0.5):
    """Return True if the ratio of vowels to consonants is > `ratio`.

    This can be used as an ad-hoc pronunciation filter.

    :param word (str): The word
    :param ratio (float, optional): The ratio
    :rtype: int
    """
    vowels = re.compile(r'[aeiouy]')
    consonants = re.compile(r'[^aeyiuo]')
    vmatch = re.findall(vowels, word.lower())
    cmatch = re.findall(consonants, word.lower())
    _ratio = float(len(vmatch)) / float(len(cmatch))
    return _ratio > ratio


def filter_length(word,
                  min_length=namebot_settings.MIN_LENGTH,
                  max_length=namebot_settings.MAX_LENGTH):
    """Filter based on min and max lengths.

    :param word (str): The word.
    :param min_length (int, optional): The minimum allowed length.
    :param max_length (int, optional): The maximum allowed length.
    :rtype: bool: The resulting check.
    """
    return len(word) >= min_length and len(word) <= max_length


def filter_startswith(word, beginning=None):
    """Filter a word starting with specified string.

    :param word (str): The word.
    :param beginning (str, optional): The beginning string to check.
    :rtype: bool: The resulting check.
    """
    return word.lower().startswith(beginning)


def filter_endswith(word, ending=None):
    """Filter words ending with a specified suffix.

    :param word (str): A word.
    :param ending (str, optional): The optional ending to check.
    :rtype bool: The resulting check.
    """
    return word.lower().endswith(ending)


def filter_tld(word, tld='.com'):
    """Check if a word ends with a TLD suffix (can be used to make a valid TLD).

    :param word (str): The wor.d
    :param tld (str, optional): The TLD to check against,
        with or without a dot.
    :rtype bool: The resulting check.
    """
    if tld.startswith('.'):
        tld = tld.replace('.', '')
    return filter_endswith(word, ending=tld)


def filter_dmetaphone(word, code=None):
    """Get double metaphone value, checking score.

    Where second key being None, an easy pronunciation is unlikely.

    :param word (str): The word.
    :param code (str, optional): The double metaphone pronunciation code.

    :rtype bool: The resulting check.
    """
    score = scoring.score_dmetaphone([word])[0]
    _, pronunciation, dmcode = score.split(':')
    if code is None:
        return True
    return pronunciation.lower() == code.lower()


def filter_soundex(word, code=None):
    """Get soundex value, checking result against a given code.

    :param word (str): The word.
    :param code (str, optional): The soundex pronunciation code.

    :rtype bool: The resulting check.
    """
    if code is None:
        return True
    retcode = scoring.score_soundex([word])[0].split(':')[1].strip().lower()
    return retcode == code.lower()


def filter_nysiis(word, code=None):
    """Get nysiis value, checking score.

    :param word (str): The word.
    :param code (str, optional): The nysiis pronunciation code.
    :rtype bool: The resulting check.
    """
    if code is None:
        return True
    retcode = scoring.score_nysiis([word])[0].split(':')[1].strip().lower()
    return retcode == code.lower()


def filter_consonant_ending(word):
    """Filter words that end in consonants.

    :param word (str): The word to filter.
    :rtype match (bool): An re.MatchObject or None.
    """
    cons = namebot_settings.regexes['consonant_ending']
    return re.search(cons, word[-1]) is not None


def filter_vowel_ending(word):
    """Filter words that end in vowels.

    :param word (str): The word to filter.
    :rtype match (bool): A re.MatchObject or None.
    """
    vowels = namebot_settings.regexes['vowel_ending']
    return re.match(vowels, word[-1]) is not None
