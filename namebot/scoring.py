import fuzzy
import re

# http://pypi.python.org/pypi/Fuzzy


def score_dmetaphone(words):
    scores = []
    dmeta = fuzzy.DMetaphone()
    for word in words:
        scored = '{}: {}'.format(word.lower(), dmeta(word))
        scores.append(scored)
    return scores


def score_soundex(words):
    scores = []
    soundex = fuzzy.Soundex(4)
    for word in words:
        scored = '{}: {}'.format(word.lower(), soundex(word))
        scores.append(scored)
    return scores


def score_nysiis(words):
    scores = []
    for word in words:
        scored = '{}: {}'.format(word.lower(), fuzzy.nysiis(word))
        scores.append(scored)
    return scores


def score_length(word):
    """Return a score, 1-5, of the length of the word. Really long, or
    really short words get a lower score. There is no hard science, but popular
    opinion suggests that a word somewhere between 8-15 letters is optimal."""
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
    """Determine if a number is within the bounds of `start` and `end`."""
    return num >= start and num <= end


def score_pronounceability(word):

    """Gets the ratio of vowels to consonants, a very basic measurement.
    Half vowels and half consonants indicates a highly pronounceable word.
    For example, 0.5 / 0.5 = 1.0, so one is perfect, and lower is worse.

    The 1-5 scale translation:
    ---------------------------------------------------------------
    0.0   0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0
    ---------------------------------------------------------------
    0      1     2     3     4     5     4     3     2     1      5
    ---------------------------------------------------------------

    Args:
        word (string) - the name
    Returns:
        score (int) - the final pronounceability score
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
    print('w: {} v: {} c: {} r: {}'.format(word, vowels, consonants, ratio))
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
    """Determine how simple the word is. Simple is defined as the number of
    separate words. In this case, higher is better, indicating a better score.

    Args:
        word (string) - the name
    Returns:
        score (int) - the final simplicity score

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
    """Scores the name using separate scoring functions, then normalize to 100
    to give an overall intuitive score. The closer to 100%, the better.
    Args:
        word (string) - the name
    Returns:
        score (float) - the final name score
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
    Args:
        words (list) - the list of words.
    Returns:
        words (list) - a list of tuples, with the score and word.
    """
    new = []
    for k, word in enumerate(words):
        new.append((score_name_overall(word), word))
    return new


def generate_all_scoring(words):
    return {
        'dmetaphone': score_dmetaphone(words),
        'soundex': score_soundex(words),
        'nysiis': score_nysiis(words),
        'grade': score_names_overall(words)
    }
