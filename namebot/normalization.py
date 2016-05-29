"""Helpers to normalize inputs and text."""

import re
import string
from collections import defaultdict

from nltk.corpus import stopwords

from pattern.vector import PORTER
from pattern.vector import stem

import settings as namebot_settings


def flatten(lst):
    """Flatten a list with arbitrary levels of nesting.

    CREDIT: http://stackoverflow.com/questions/10823877/
        what-is-the-fastest-way-to-flatten-arbitrarily-nested-lists-in-python
    Changes made include:
        1. Adding error handling,
        2. Renaming variables,
        3. Using `any` instead of `or`.
    See http://creativecommons.org/licenses/by-sa/3.0/ for specific details.

    Args:
        lst (list): The nested list.

    Returns:
        (generator): The new flattened list of words.
    """
    if not isinstance(lst, list):
        yield []
    for i in lst:
        if any([isinstance(i, list), isinstance(i, tuple)]):
            for j in flatten(i):
                yield j
        else:
            yield i


def remove_odd_sounding_words(words):
    """Remove random odd sounding word combinations via regular expressions.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with words cleaned.
    """
    odd_regexes = [
        re.compile(r'^a|e|i|o|u|y{3,6}'),
        # bk, ck, dk, gk, etc...
        re.compile(r'\b[^aeiouys]k|zt|ksd|kd|zhr'),
        re.compile(r'\bzt|ksd|kd|zhr')
    ]
    cleaned = []
    if words is None or len(words) == 0:
        return words
    # Loop through any number of
    # regexes and add only if no matches exist
    [cleaned.append(word) for word in words if not any(
        re.match(regex, word) for regex in odd_regexes)]
    return cleaned


def stem_words(words):
    """Stem words to their base linguistic stem to remove redundancy.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with words stemmed.
    """
    return [stem(word, stemmer=PORTER) for word in words]


def remove_stop_words(words):
    """Remove all stop words.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with stopwords removed.
    """
    # http://stackoverflow.com/questions/5486337/
    # how-to-remove-stop-words-using-nltk-or-python
    return [w for w in words if w.lower() not in stopwords.words('english')]


def remove_bad_words(words):
    """Remove naughty words that might come from wordnet synsets and lemmata.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with bad words removed.
    """
    bad_words = ["nigger", "wop",
                 "kike", "faggot",
                 "fuck", "pussy", "cunt"]
    return [word for word in words if word.lower() not in bad_words]


def filter_words(words):
    """Filter words by default min/max settings in the settings module.

    Args:
        words (list): The list of words

    Returns:
        list: The filtered words
    """
    new_arr = []
    for word in words:
        if not re.search(' ', word):
            lte = len(word) <= namebot_settings.MAX_LENGTH
            gte = len(word) >= namebot_settings.MIN_LENGTH
            if all([lte, gte]):
                new_arr.append(word)
        elif re.search(' ', word):
            split = re.split(' ', word)
            split_join = []
            for chunks in split:
                length = len(chunks)
                lte = length <= namebot_settings.SPACED_MAX_LENGTH
                gte = length >= namebot_settings.MIN_LENGTH
                if all([lte, gte]):
                    split_join.append(chunks)
            new_arr.append(
                ' '.join(split_join))
    return new_arr


def uniquify(words):
    """Remove duplicates from a list.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with duplicates removed.
    """
    return {}.fromkeys(words).keys() if words is not None else words


def clean_sort(words):
    """A function for cleaning and prepping words for techniques.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with words cleaned and sorted.
    """
    if isinstance(words, basestring):
        return words
    chars = '!"#$%\'()*+,._/:;<=>?@[\\]^`{|}~01234567890'
    if words is not None:
        try:
            words = [word.strip().lower().translate(
                string.maketrans('', ''),
                chars) for word in words if len(word) > 1]
        except TypeError:
            pass
    return words


def chop_duplicate_ends(word):
    """Remove duplicate letters on either end, if the are adjacent.

    Args:
        words (list): The list of words

    Returns:
        list: An updated word list with duplicate ends removed for each word.
    """
    if word[0] == word[1]:
        word = word[1:]
    if word[-2:-1] == word[-1:]:
        word = word[:-1]
    return word


def key_words_by_pos_tag(words):
    """Key words by the pos tag name, given when using pos_tag on a list.

    Args:
        words (list): The list of words, where each item is a 2-tuple.

    Returns:
        dict: An updated dictionary keyed by pos tag,
            with values as a list of matching pos matching words.
    """
    alltags = defaultdict(list)
    for word, pos in words:
        alltags[pos].append(word)
    return alltags
