"""Techniques for various languages."""

from __future__ import absolute_import
from __future__ import division
from .latin_words import words as lwords


def lookup_latin_word(word):
    """Search the latin word list for any matches for the given `word`.

    Args:
        word (str) - The word to search for
    Returns:
        results (list) - A nested list with each matching definition(s) group.
    """
    results = []
    if not word:
        return results
    for lword, keywords in lwords.iteritems():
        if word in keywords:
            results.append(lword.split(','))
    return results


def lookup_latin_words(words):
    """Look up the matching latin definitions for a list of words.

    Args:
        words (list): A list of words.

    Returns:
        results (list): The updated list.
    """
    results = []
    if not words:
        return results
    for word in words:
        results.append(lookup_latin_word(word))
    return results
