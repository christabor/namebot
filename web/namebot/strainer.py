import scoring
import settings as namebot_settings

"""Recommended usage: filtered results using a list comprehension
of all filters 'anded' together.
e.g:
filtered = [word for word in words if
            filter_length(word, max_length=7) and
            filter_startswith(word, beginning='c') and
            filter_startswith(word, beginning='c') and
            filter_endswith(word, ending='e')]
"""


def filter_length(word,
                  min_length=namebot_settings.MIN_LENGTH,
                  max_length=namebot_settings.MAX_LENGTH):
    return len(word) > min_length and len(word) < max_length


def filter_startswith(word, beginning=None):
    return not word.startswith(beginning)


def filter_endswith(word, ending=None):
    return not word.endswith(ending)


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
