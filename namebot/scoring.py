import fuzzy
# http://pypi.python.org/pypi/Fuzzy


def score_dmetaphone(words):
    scores = []
    dmeta = fuzzy.DMetaphone()
    for word in words:
        scored = '%s: %s' % (word.lower(), dmeta(word))
        scores.append(scored)
    return scores


def score_soundex(words):
    scores = []
    soundex = fuzzy.Soundex(4)
    for word in words:
        scored = '%s: %s' % (word.lower(), soundex(word))
        scores.append(scored)
    return scores


def score_nysiis(words):
    scores = []
    for word in words:
        scored = '%s: %s' % (word.lower(), fuzzy.nysiis(word))
        scores.append(scored)
    return scores


def generate_all_scoring(words):
    return {
        'scoring': {
            'dmetaphone': score_dmetaphone(words),
            'soundex': score_soundex(words),
            'nysiis': score_nysiis(words)
        },
    }
