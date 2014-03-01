import fuzzy
# http://pypi.python.org/pypi/Fuzzy


class NamebotScoring:

    def score_dmetaphone(self, words):
        scores = []
        dmeta = fuzzy.DMetaphone()
        for word in words:
            scored = '%s: %s' % (word.lower(), dmeta(word))
            scores.append(scored)
        return scores

    def score_soundex(self, words):
        scores = []
        soundex = fuzzy.Soundex(4)
        for word in words:
            scored = '%s: %s' % (word.lower(), soundex(word))
            scores.append(scored)
        return scores

    def score_nysiis(self, words):
        scores = []
        for word in words:
            scored = '%s: %s' % (word.lower(), fuzzy.nysiis(word))
            scores.append(scored)
        return scores

    def generate_all_scoring(self, words):
        return {
            'scoring': {
                'dmetaphone': self.score_dmetaphone(words),
                'soundex': self.score_soundex(words),
                'nysiis': self.score_nysiis(words)
            },
        }
