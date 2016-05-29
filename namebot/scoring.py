"""Provides various scoring methods for word strength."""

import re

import fuzzy

dmeta = fuzzy.DMetaphone()
soundex = fuzzy.Soundex(4)


def score_dmetaphone(words):
    """Score words using the double metaphone algorithm.

    :param words (list): the list of words.
    :rtype scores (list): the scored words
    """
    scores = []
    for word in words:
        res, output = dmeta(word)
        scores.append('{0}:{1}:{2}'.format(word, res, output))
    return scores


def score_soundex(words):
    """Score words using the soundex algorithm.

    :param words (list): the list of words.
    :rtype scores (list): the scored words
    """
    return ['{}: {}'.format(w.lower(), soundex(w)) for w in words]


def score_nysiis(words):
    """Score words using the nysiis algorithm.

    :param words (list): the list of words.
    :rtype scores (list): the scored words
    """
    return ['{}: {}'.format(w.lower(), fuzzy.nysiis(w)) for w in words]


def score_length(word):
    """Return a score, 1-5, of the length of the word.

    Really long, or really short words get a lower score.
    There is no hard science, but popular opinion suggests
    that a word somewhere between 8-15 letters is optimal.

    :param word (str): The word to score.
    :rtype score (int): The resulting score.
    """
    if not word or len(word) == 0:
        return 0
    _len = len(word)
    # 20+
    if _len > 20:
        return 1
    # 15-20
    elif _len > 15 and _len <= 20:
        return 2
    # 1-4
    elif _len <= 4:
        return 3
    # 10-15
    elif _len >= 10 and _len <= 15:
        return 4
    # 5-10
    elif _len > 4 and _len < 10:
        return 5


def bounded(num, start, end):
    """Determine if a number is within the bounds of `start` and `end`.

    :param num (int): An integer.
    :param start (int): A start minimum.
    :param end (int): An end maximum.
    :rtype is_bounded (bool): Whether number is bounded by start and end.
    """
    return num >= start and num <= end


def score_pronounceability(word):
    """Get the ratio of vowels to consonants, a very basic measurement.

    Half vowels and half consonants indicates a highly pronounceable word.
    For example, 0.5 / 0.5 = 1.0, so one is perfect, and lower is worse.

    The 1-5 scale translation:

    0.0   0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0
    0      1     2     3     4     5     4     3     2     1      5

    :param word (string): The name
    :rtype (int): The final pronounceability score
    """
    if not word or len(word) == 0:
        return 0
    word = re.sub(r'[^a-zA-Z0-9]', '', word)
    re_vowels = re.compile(r'[a|e|i|o|u]')
    re_cons = re.compile(r'[^a|e|i|o|u]')
    vowels = float(len(re.findall(re_vowels, word)))
    consonants = float(len(re.findall(re_cons, word)))
    if vowels is 0.0 or consonants is 0.0:
        return 0
    if vowels < consonants:
        ratio = vowels / consonants
    else:
        ratio = consonants / vowels
    if ratio == 0.0:
        return 0
    if ratio == 1.0:
        return 5
    if bounded(ratio, 0.0, 0.1) or bounded(ratio, 0.9, 1.0):
        return 1
    if bounded(ratio, 0.1, 0.2) or bounded(ratio, 0.8, 0.9):
        return 2
    if bounded(ratio, 0.2, 0.3) or bounded(ratio, 0.7, 0.8):
        return 3
    if bounded(ratio, 0.3, 0.4) or bounded(ratio, 0.6, 0.7):
        return 4
    if bounded(ratio, 0.4, 0.5) or bounded(ratio, 0.5, 0.6):
        return 5
    return 0


def score_simplicity(word):
    """Determine how simple the word is.

    Simple is defined as the number of separate words.
    In this case, higher is better, indicating a better score.

    :param word (string): the name
    :rtype score (int): the final simplicity score

    >>> score_simplicity('the cat in the hat')
    >>> 1
    >>> score_simplicity('facebook')
    >>> 5
    """
    if not word or len(word) == 0:
        return 0
    word_count = len(re.split(r'[^a-z]', word))
    if word_count == 1:
        return 5
    if word_count < 3:
        return 4
    if word_count < 4:
        return 3
    if word_count < 5:
        return 2
    # After 4+ words, the name has a very poor score.
    return 1


def score_name_overall(word):
    """Score the name using separate scoring functions, then normalize to 100.

    This method gives an overall intuitive score.
    The closer to 100%, the better.

    :param word (string): the name
    :rtype score (float): the final name score
    """
    length = score_length(word)
    pronounceability = score_pronounceability(word)
    simplicity = score_simplicity(word)
    _scores = sum([length, pronounceability, simplicity])
    score = round(_scores * 10)
    # cut off at 100%
    if score > 100:
        return 100
    return score


def score_names_overall(words):
    """Score all names.

    :param words (list): the list of words.
    :rtype words (list): a list of tuples, with the score and word.
    """
    return [(score_name_overall(w), w) for w in words]


def generate_all_scoring(words):
    """Return all scoring methods for a set of words.

    :param words (list): the list of words.
    :rtype words (dict): the scores, keyed by scoring name.
    """
    return {
        'dmetaphone': score_dmetaphone(words),
        'soundex': score_soundex(words),
        'nysiis': score_nysiis(words),
        'grade': score_names_overall(words)
    }
