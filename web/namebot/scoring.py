import fuzzy
# http://pypi.python.org/pypi/Fuzzy


#TODO MAKE CLASS BASED
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
    data = {
        'scoring': {},
    }
    data['scoring']['dmetaphone'] = score_dmetaphone(words)
    data['scoring']['soundex'] = score_soundex(words)
    data['scoring']['nysiis'] = score_nysiis(words)
    return data
