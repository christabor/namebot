from nltk.corpus import stopwords
from pattern.vector import stem
from pattern.vector import PORTER
import re
import string

import settings as namebot_settings


def remove_odd_sounding_words(words):
    """
    after manipulating words through other techniques,
    remove random odd sounding word combinations
    via regular expressions
    """
    cleaned = []
    if words is None:
        return

    # Loop through any number of
    # regexes and add only if no matches exist
    [cleaned.append(word) for word in words
        if not any(
            re.match(regex, word) for regex in namebot_settings.regexes)]
    return cleaned


def stem_words(data):
    """
    Stem words to their base
    linguistic stem to remove redundancy
    """
    for val in data:
        val = stem(val, stemmer=PORTER)
    return data


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    # http://stackoverflow.com/questions/5486337/
            # how-to-remove-stop-words-using-nltk-or-python

    newdata = [w for w in data if w.lower() not in stop_words]
    # newdata = set(stopwords.words('english'))
    return newdata


def remove_bad_words(words):
    """
    remove naughty words that might
    come from wordnet synsets and lemmata
    """
    bad_words = ["nigger", "wop",
                 "kike", "faggot",
                 "fuck", "pussy", "cunt"]

    newdata = [word for word in words if word.lower() not in bad_words]
    return newdata


def filter_words(words):
    new_arr = []
    for word in words:
        if not re.search(' ', word):
            if len(word) <= namebot_settings.MAX_LENGTH and \
                    len(word) >= namebot_settings.MIN_LENGTH:
                        new_arr.append(word)

        elif re.search(' ', word):
            split = re.split(' ', word)
            split_join = []
            for chunks in split:
                length = len(chunks)
                if length <= namebot_settings.SPACED_MAX_LENGTH and \
                        length >= namebot_settings.MIN_LENGTH:
                            split_join.append(chunks)

            new_arr.append(
                ' '.join(split_join))
    return new_arr


def uniquify(words):
    """
    remove duplicates from a list
    """
    if words is not None:
        return {}.fromkeys(words).keys()
    else:
        return words


def clean_sort(words):
    """
    A function for cleaning string arrays
    and prepping them for word techniques
    """
    chars = '!"#$%\'()*+,./:;<=>?@[\\]^`{|}~01234567890'
    if words is not None:
        try:
            words = [word.strip().lower().translate(
                string.maketrans('', ''),
                chars) for word in words if len(word) > 1]
        except TypeError:
            pass
    return words


def combine_words(arr, custom):
    """
    a function to combine two words by
    an offset of 1
    (using array increment as offset)

    "custom" functions as a separator
    to use for different styles
    """
    new_arr = []
    try:
        for i in arr:
            for j in arr:
                if i is not j and j is not i:
                    if arr[i][-1] is not arr[j][-1]:
                        new_arr.append(i + custom + j)
                        new_arr.append(j + custom + i)

    except IndexError:
        pass

    return new_arr
