import re
import scoring
import settings as namebot_settings

"""Recommended usage: filtered results using a list comprehension
of all filters 'anded' together.
e.g:
filtered = [word for word in words if
            filter_length(word, max_length=7) and
            filter_startswith(word, beginning='c') and
            filter_startswith(word, beginning='c') and
            filter_endswith(word, ending='e') ...]
"""


def filter_vowel_cons_ratio(word, ratio=0.5):
    """Return True if the ratio of vowels to consonants is > `ratio`.
    This can be used as an ad-hoc pronunciation filter."""
    vowels = re.compile(r'[aeiouy]')
    consonants = re.compile(r'[^aeyiuo]')
    vmatch = re.findall(vowels, word.lower())
    cmatch = re.findall(consonants, word.lower())
    _ratio = float(len(vmatch)) / float(len(cmatch))
    return _ratio > ratio


def filter_length(word,
                  min_length=namebot_settings.MIN_LENGTH,
                  max_length=namebot_settings.MAX_LENGTH):
    return len(word) >= min_length and len(word) <= max_length


def filter_startswith(word, beginning=None):
    return word.lower().startswith(beginning)


def filter_endswith(word, ending=None):
    return word.lower().endswith(ending)


def filter_metaphone(word):
    """Get the metaphone value, and if the second key is None
    pronunciation is unlikely."""
    score = scoring.score_dmetaphone(word)
    return score[1] is not None


def filter_soundex(word):
    # TODO
    # res = nameScoring.score_soundex(word)
    pass


def filter_nysiis(word):
    # TODO
    # res = nameScoring.score_nysiis(word)
    pass
