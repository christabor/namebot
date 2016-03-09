"""Provides filtering functions for reducing large sets of generated words.

Recommended usage: filtered results using a list comprehension
of all filters 'anded' together.
e.g:
filtered = [word for word in words if
            filter_length(word, max_length=7) and
            filter_startswith(word, beginning='c') and
            filter_startswith(word, beginning='c') and
            filter_endswith(word, ending='e') ...]
"""

import re
import scoring
import settings as namebot_settings


def filter_vowel_cons_ratio(word, ratio=0.5):
    """Return True if the ratio of vowels to consonants is > `ratio`.

    This can be used as an ad-hoc pronunciation filter.
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

    Args:
        word (str): The word.
        min_length (int, optional): The minimum allowed length.
        max_length (int, optional): The maximum allowed length.

    Returns:
        bool: The resulting check.
    """
    return len(word) >= min_length and len(word) <= max_length


def filter_startswith(word, beginning=None):
    """Filter a word starting with specified string.

    Args:
        word (str): The word.
        beginning (str, optional): The beginning string to check.

    Returns:
        bool: The resulting check.
    """
    return word.lower().startswith(beginning)


def filter_endswith(word, ending=None):
    """Filter words ending with a specified suffix.

    Args:
        word (str): A word.
        ending (str, optional): The optional ending to check.

    Returns:
        bool: The resulting check.
    """
    return word.lower().endswith(ending)


def filter_tld(word, tld='.com'):
    """Check if a word ends with a TLD suffix (can be used to make a valid TLD).

    Args:
        word (str): The wor.d
        tld (str, optional): The TLD to check against, with or without a dot.

    Returns:
        bool: The resulting check.
    """
    if tld.startswith('.'):
        tld = tld.replace('.', '')
    return filter_endswith(word, ending=tld)


def filter_dmetaphone(word, code=None):
    """Get double metaphone value, checking score.

    Where second key being None, an easy pronunciation is unlikely.

    Args:
        word (str): The word.
        code (str, optional): The double metaphone pronunciation code.

    Returns:
        bool: The resulting check.
    """
    score = scoring.score_dmetaphone([word])[0]
    _, pronunciation, dmcode = score.split(':')
    if code is None:
        return True
    return pronunciation.lower() == code.lower()


def filter_soundex(word, code=None):
    """Get soundex value, checking result against a given code.

    Args:
        word (str): The word.
        code (str, optional): The soundex pronunciation code.

    Returns:
        bool: The resulting check.
    """
    if code is None:
        return True
    retcode = scoring.score_soundex([word])[0].split(':')[1].strip().lower()
    return retcode == code.lower()


def filter_nysiis(word, code=None):
    """Get nysiis value, checking score.

    Args:
        word (str): The word.
        code (str, optional): The nysiis pronunciation code.

    Returns:
        bool: The resulting check.
    """
    if code is None:
        return True
    retcode = scoring.score_nysiis([word])[0].split(':')[1].strip().lower()
    return retcode == code.lower()
