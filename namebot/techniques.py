from __future__ import absolute_import
from __future__ import division

from random import choice
from string import ascii_uppercase
from collections import defaultdict
import re
import nltk

from . import settings as namebot_settings
from . import normalization


_prefixes = namebot_settings.PREFIXES
_suffixes = namebot_settings.SUFFIXES
_alphabet = namebot_settings.ALPHABET
_consonants = namebot_settings.CONSONANTS
_vowels = namebot_settings.VOWELS
_regexes = namebot_settings.regexes


class InsufficientWordsError(Exception):
    def __init__(self, msg):
        self.msg = msg


def domainify(words, tld='com'):
    _words = []
    if tld.startswith('.'):
        tld = tld.replace('.', '')
    for word in words:
        if word.endswith(tld) and tld != '':
            word = word.replace(tld, '.{}'.format(tld))
        _words.append(word)
    return _words


def spoonerism(words):
    """Convert a list of words formatted with the spoonerism
    linguistic technique.

    Args:
        words (list) - The list of words to operate on

    Returns:
        words (list) - The updated list of words

    >>> spoonerism(['foo', 'bar'])
    >>> ['boo', 'far']
    """
    "First: [f]oo [b]ar => boo far"
    new_words = []
    if len(words) < 2:
        raise InsufficientWordsError('Need more than one word to combine')
    for k, word in enumerate(words):
        try:
            new_words.append('{}{} {}{}'.format(
                words[k + 1][0],  # 2nd word, 1st letter
                word[1:],  # 1st word, 2nd letter to end
                word[0],  # 1st word, 1st letter
                words[k + 1][1:]))  # 2nd word, 2nd letter to end
        except IndexError:
            continue
    return new_words


def kniferism(words):
    """Convert a list of words formatted with the kniferism
    linguistic technique.

    Args:
        words (list) - The list of words to operate on

    Returns:
        words (list) - The updated list of words

    >>> kniferism(['foo', 'bar'])
    >>> ['fao', 'bor']
    """
    "Mid: f[o]o b[a]r => fao bor"
    if len(words) < 2:
        raise InsufficientWordsError('Need more than one word to combine')
    new_words = []
    for k, word in enumerate(words):
        try:
            middle_second = int(len(words[k + 1]) / 2)
            middle_first = int(len(word) / 2)
            new_words.append('{}{}{} {}{}{}'.format(
                word[:middle_first],
                words[k + 1][middle_second],
                word[middle_first + 1:],
                words[k + 1][:middle_second],
                word[middle_first],
                words[k + 1][middle_second + 1:]))
        except IndexError:
            continue
    return new_words


def forkerism(words):
    """Convert a list of words formatted with the forkerism
    linguistic technique.

    Args:
        words (list) - The list of words to operate on

    Returns:
        words (list) - The updated list of words

    >>> forkerism(['foo', 'bar'])
    >>> ['for', 'bao']
    """
    "Last: fo[o] ba[r] => for bao"
    if len(words) < 2:
        raise InsufficientWordsError('Need more than one word to combine')
    new_words = []
    for k, word in enumerate(words):
        try:
            s_word = words[k + 1]
            s_word_len = len(s_word)
            f_word_len = len(word)
            f_w_last_letter = word[f_word_len - 1]
            s_w_last_letter = words[k + 1][s_word_len - 1]
            new_words.append('{}{} {}{}'.format(
                word[:f_word_len - 1],  # 1st word, 1st letter to last - 1
                s_w_last_letter,  # 2nd word, last letter
                s_word[:s_word_len - 1],  # 2nd word, 1st letter to last - 1
                f_w_last_letter))  # 1st word, last letter
        except IndexError:
            continue
    return new_words


def reduplication_ablaut(words, count=1, random=True, vowel='e'):
    """
    http://phrases.org.uk/meanings/reduplication.html
    A technique to combine words and altering the vowels
    e.g ch[i]t-ch[a]t, d[i]lly, d[a]lly
    """
    if len(words) < 2:
        raise InsufficientWordsError('Need more than one word to combine')
    new_words = []
    substitution = choice(_vowels) if random else vowel
    for word in words:
        second = re.sub(r'a|e|i|o|u', substitution, word, count=count)
        # Only append if the first and second are different.
        if word != second:
            new_words.append('{} {}'.format(word, second))
    return new_words


def prefixify(words):
    """Apply a prefix technique to a set of words

    Args:
        words (list) - The list of words to operate on.

    Returns:
        new_arr (list): the updated *fixed words
    """
    new_arr = []
    for word in words:
        if not word:
            continue
        for prefix in _prefixes:
            first_prefix_no_vowel = re.search(_regexes['no_vowels'], word[0])
            second_prefix_no_vowel = re.search(_regexes['no_vowels'], prefix[0])
            if first_prefix_no_vowel or second_prefix_no_vowel:
                # if there's a vowel at the end of
                # prefix but not at the beginning
                # of the word (or vice versa)
                vowel_beginning = re.search(r'a|e|i|o|u', prefix[-1:])
                vowel_end = re.search(r'^a|e|i|o|u', word[:1])
                if vowel_beginning or vowel_end:
                    new_arr.append('{}{}'.format(prefix, word))
    return new_arr


def suffixify(words):
    """Apply a suffix technique to a set of words

    Args:
        words (list) - The list of words to operate on.
            (e.g -> chard + ard = chardard -> chard)

    Returns:
        new_arr (list): the updated *fixed words
    """
    new_arr = []
    for word in words:
        if not word:
            continue
        for suffix in _suffixes:
            prefix_start_vowel = re.search(_regexes['all_vowels'], word[0])
            suffix_start_vowel = re.search(_regexes['all_vowels'], suffix[0])
            if prefix_start_vowel or suffix_start_vowel:
                if suffix is 'ify':
                    if word[-1] is 'e':
                        if word[-2] is not 'i':
                            new_arr.append('{}{}'.format(word[:-2], suffix))
                        else:
                            new_arr.append('{}{}'.format(word[:-1], suffix))
                    new_arr.append(word + suffix)
                else:
                    new_arr.append(word + suffix)
    return new_arr


def duplifixify(words):
    """Apply a duplifix technique to a set of words (e.g: teeny weeny, etc...)

    Args:
        words (list) - The list of words to operate on.

    Returns:
        new_arr (list): the updated *fixed words
    """
    new_arr = []
    for word in words:
        if not word:
            continue
        for letter in _alphabet:
            # check if the first letter is NOT the same as the second letter,
            # or the combined word is not a duplicate of the first.
            duplicate_word = '{}{}'.format(letter, word[1:]) == word
            if word[0] is not letter and not duplicate_word:
                new_arr.append('{} {}{}'.format(word, letter, word[1:]))
    return new_arr


def disfixify(words):
    """Apply a disfix technique to a set of words

    TODO: implement

    Args:
        words (list) - The list of words to operate on.

    Returns:
        new_arr (list): the updated *fixed words
    """
    new_arr = []
    return new_arr


def infixify(words):
    """Apply a disfix technique to a set of words

    TODO: implement

    Args:
        words (list) - The list of words to operate on.

    Returns:
        new_arr (list): the updated *fixed words
    """
    new_arr = []
    return new_arr


def simulfixify(words, pairs=None, max=5):
    """Generates randomly simulfixed words.

    Args:
        words (list) - List of words to operate on.
        pairs (list, optional) - Simulfix pairs to use for each word.
                                 If not specified, these will be generated
                                 randomly as vowel + consonant strings.
        max (int, optional): The number of simulfix pairs to generate
                             (if pairs is not specified.)

    Returns:
        results (list) - The simulfix version of each word,
                         for each simulfix pair.
    """
    results = []
    if pairs is None:
        pairs = ['{}{}'.format(choice(_vowels), choice(_consonants))
                 for _ in range(max)]
    for word in words:
        for combo in pairs:
            mid = len(word) // 2
            _word = '{}{}{}'.format(word[0:mid], combo, word[mid:])
            results.append(_word)
    return results


def palindrome(word):
    return '{}{}'.format(word, word[::-1])


def palindromes(words):
    return [palindrome(word) for word in words]


def make_founder_product_name(founder1, founder2, product):
    """
    get the name of two people
    forming a company and combine it
    TODO: 1, 0, infinite
    """
    return '{} & {} {}'.format(
        founder1[0].upper(),
        founder2[0].upper(),
        product)


def make_name_alliteration(word_array, divider=' '):
    new_arr = []
    """
    java jacket
    singing sally
    earth engines
    ...etc

    1. Loop through a given array of words
    2. group by words with the same first letter
    3. combine them and return to new array

    """
    word_array = sorted(word_array)

    for word1 in word_array:
        for word2 in word_array:
            if word1[:1] is word2[:1] and word1 is not word2:
                new_arr.append(word1 + divider + word2)
    return new_arr


def make_name_abbreviation(words):
    """
    this function will make some kind of
    interesting company acronym
    eg: BASF, AT&T, A&W
    Returns a single string of the new word combined.
    """
    return ''.join([word[:1].upper() for word in words])


def make_vowel(words, vowel_type, vowel_index):
    """Primary for all Portmanteau generators, that creates
    the portmanteau based on :vowel_index, and :vowel_type.

    The algorithm works as following:

    It looks for the first occurrence of a specified vowel in the first word,
    then gets the matching occurrence (if any) of the second word,
    then determines which should be first or second position, based on
    the ratio of letters (for each word) divided by the position of the vowel
    in question (e.g. c[a]t (2/3) vs. cr[a]te (3/5)).

    The higher number is ordered first, and the two words are then fused
    together by the single matching vowel.
    """
    new_arr = []
    for i in words:
        for j in words:
            is_match_i = re.search(vowel_type, i)
            is_match_j = re.search(vowel_type, j)
            if i is not j and is_match_i and is_match_j:
                # get the indices and lengths to use in finding the ratio
                pos_i = i.index(vowel_index)
                len_i = len(i)
                pos_j = j.index(vowel_index)
                len_j = len(j)

                # If starting index is 0,
                # add 1 to it so we're not dividing by zero
                if pos_i is 0:
                    pos_i = 1
                if pos_j is 0:
                    pos_j = 1

                # Decide which word should be the
                # prefix and which should be suffix
                if round(pos_i / len_i) > round(pos_j / len_j):
                    p = i[0: pos_i + 1]
                    p2 = j[pos_j: len(j)]
                    if len(p) + len(p2) > 2:
                        if re.search(
                            _regexes['all_vowels'], p) or re.search(
                                _regexes['all_vowels'], p2):
                                    if p[-1] is p2[0]:
                                        new_arr.append(p[:-1] + p2)
                                    else:
                                        new_arr.append(p + p2)
    return new_arr


def make_portmanteau_default_vowel(words):
    """
    Make a portmanteau based on vowel
    matches (ala Brad+Angelina = Brangelina)
    Only matches for second to last letter
    in first word and matching vowel in second word.

    This defers to the make_vowel function for all the internal
    magic, but is a helper in that it provides all types of vowel
    combinations in one function.
    """
    new_arr = []
    vowel_a_re = re.compile(r'a{1}')
    vowel_e_re = re.compile(r'e{1}')
    vowel_i_re = re.compile(r'i{1}')
    vowel_o_re = re.compile(r'o{1}')
    vowel_u_re = re.compile(r'u{1}')

    new_arr += make_vowel(words, vowel_a_re, "a")
    new_arr += make_vowel(words, vowel_e_re, "e")
    new_arr += make_vowel(words, vowel_i_re, "i")
    new_arr += make_vowel(words, vowel_o_re, "o")
    new_arr += make_vowel(words, vowel_u_re, "u")
    return new_arr


def make_portmanteau_split(words):
    """
    nikon = [ni]pp[on] go[k]aku
    make words similar to nikon,
    which is comprised of Nippon + Gokaku.

    We get the first C+V in the first word,
    then last V+C in the first word,
    then all C in the second word.
    """
    new_arr = []
    for i in words:
        for j in words:
                if i is not j:
                    l1 = re.search(r'[^a|e|i|o|u{1}]+[a|e|i|o|u{1}]', i)
                    l2 = re.search(r'[a|e|i|o|u{1}]+[^a|e|i|o|u{1}]$', j)
                    if i and l1 and l2:
                        # Third letter used for
                        # consonant middle splits only
                        l3 = re.split(r'[a|e|i|o|u{1}]', i)
                        l1 = l1.group(0)
                        l2 = l2.group(0)
                        if l3 and len(l3) > 0:
                            for v in l3:
                                new_arr.append(l1 + v + l2)
                            else:
                                new_arr.append('{}{}{}'.format(l1, 't', l2))
                                new_arr.append('{}{}{}'.format(l1, 's', l2))
                                new_arr.append('{}{}{}'.format(l1, 'z', l2))
                                new_arr.append('{}{}{}'.format(l1, 'x', l2))
    return new_arr


def make_punctuator(words, replace):
    """Put some hyphens or dots, or a given punctutation via :replace
    in the word, but only around vowels ala "del.ic.ious"
    """
    def _replace(words, replace, replace_type='.'):
        return [word.replace(
            replace, replace + replace_type) for word in words]

    hyphens = _replace(words, replace, replace_type='-')
    periods = _replace(words, replace)
    return hyphens + periods


def make_punctuator_vowels(words):
    """Helper function that combines all
    possible combinations for vowels"""
    new_words = []
    new_words += make_punctuator(words, 'a')
    new_words += make_punctuator(words, 'e')
    new_words += make_punctuator(words, 'i')
    new_words += make_punctuator(words, 'o')
    new_words += make_punctuator(words, 'u')
    return new_words


def make_vowelify(words):
    """Chop off consonant ala nautica
    if second to last letter is a vowel.
    """
    new_arr = []
    for word in words:
        if re.search(_regexes['all_vowels'], word[:-2]):
            new_arr.append(word[:-1])
    return new_arr


def make_misspelling(words):
    """
    This is used as the primary "misspelling"
    technique, through a few different techniques
    that are all categorized as misspelling.

    Brute force all combinations,
    then use double metaphone to remove odd ones.
    """
    token_groups = (
        ('ics', 'ix'),
        ('ph', 'f'),
        ('kew', 'cue'),
        ('f', 'ph'),
        ('o', 'ough'),
        # these seem to have
        # sucked in practice
        ('o', 'off'),
        ('ow', 'o'),
        ('x', 'ecks'),
        ('za', 'xa'),
        ('xa', 'za'),
        ('ze', 'xe'),
        ('xe', 'ze'),
        ('zi', 'xi'),
        ('xi', 'zi'),
        ('zo', 'xo'),
        ('xo', 'zo'),
        ('zu', 'xu'),
        ('xu', 'zu'),
        # number based
        ('one', '1'),
        ('1', 'one'),
        ('two', '2'),
        ('2', 'two'),
        ('three', '3'),
        ('3', 'three'),
        ('four', '4'),
        ('4', 'four'),
        ('five', '5'),
        ('5', 'five'),
        ('six', '6'),
        ('6', 'six'),
        ('seven', '7'),
        ('7', 'seven'),
        ('eight', '8'),
        ('8', 'eight'),
        ('nine', '9'),
        ('9', 'nine'),
        ('ten', '10'),
        ('10', 'ten'),
        ('ecks', 'x'),
        ('spir', 'speer'),
        ('speer', 'spir'),
        ('x', 'ex'),
        ('on', 'awn'),
        ('ow', 'owoo'),
        ('awn', 'on'),
        ('awf', 'off'),
        ('s', 'z'),
        ('ce', 'ze'),
        ('ss', 'zz'),
        ('ku', 'koo'),
        ('trate', 'trait'),
        ('trait', 'trate'),
        ('ance', 'anz'),
        ('il', 'yll'),
        ('ice', 'ize'),
        ('chr', 'kr'),
        # These should only be at end of word!
        ('er', 'r'),
        ('lee', 'ly'),
    )
    new_arr = []
    for word in words:
        for tokens in token_groups:
            new_arr.append(word.replace(*tokens))
    return normalization.uniquify(new_arr)


def _pig_latinize(word, postfix='ay'):
    """Generates standard pig latin style,
    with customizeable postfix argument"""
    # Common postfixes: ['ay', 'yay', 'way']
    if not type(postfix) is str:
        raise TypeError('Must use a string for postfix.')

    piggified = None

    vowel_re = re.compile(r'(a|e|i|o|u)')
    first_letter = word[0:1]

    # clean up non letters
    word = word.replace(r'[^a-zA-Z]', '')

    if vowel_re.match(first_letter):
        piggified = word + 'way'
    else:
        piggified = ''.join([word[1: len(word)], first_letter, postfix])
    return piggified


def pig_latinize(words, postfix='ay'):
    return [_pig_latinize(word, postfix=postfix) for word in words]


def acronym_lastname(description, lastname):
    """Inspiration: ALFA Romeo"""
    desc = ''.join([word[0].upper() for word in normalization.remove_stop_words(
        description.split(' '))])
    return '{} {}'.format(desc, lastname)


def get_descriptors(words):
    """
    Use NLTK to first grab tokens by looping through words,
    then tag part-of-speech (in isolation)
    and provide a dictionary with a list of each type
    for later retrieval and usage
    """
    descriptors = defaultdict(list)
    tokens = nltk.word_tokenize(' '.join(words))
    parts = nltk.pos_tag(tokens)
    # Then, push the word into the matching type
    for part in parts:
        descriptors[part[1]].append(part[0])
    return descriptors


def _add_pos_subtypes(nouns, verbs):
    """Combine alternating verbs and nouns into a new list.

    Args:
        nouns (list) - List of nouns, noun phrases, etc...
        verbs (list) - List of verbs, verb phrases, etc...

    Returns:
        words (list) - The newly combined list
    """
    words = []
    try:
        for noun in nouns:
            for verb in verbs:
                words.append('{} {}'.format(noun, verb))
                words.append('{} {}'.format(verb, noun))
    except KeyError:
        pass
    return words


def _create_pos_subtypes(words):
    """Check the part-of-speech tags for a noun-phrase, and if it exists,
    add combinations with noun-phrase + verb-phrase, noun-phrase + verb,
    and noun-phrase + adverb, for each pos type that exists.

    Args:
        words (list) - List of verbs, verb phrases, etc...

    Returns:
        new_words (list) - The newly combined list
    """
    new_words = []
    types = words.keys()
    if 'NNP' in types:
        if 'VBP' in types:
            new_words += _add_pos_subtypes(words['NNP'], words['VBP'])
        if 'VB' in types:
            new_words += _add_pos_subtypes(words['NNP'], words['VB'])
        if 'RB' in types:
            new_words += _add_pos_subtypes(words['NNP'], words['RB'])
    return new_words


def make_descriptors(words):
    """Make descriptor names based from a verb + noun,
    or adjective + noun combination.
    Examples:
        -Pop Cap,
        -Big Fish,
        -Red Fin,
        -Cold Water (grill), etc...
    Combines VBP/VB/RB, with NN/NNS
    """
    return list(set(_create_pos_subtypes(words)))


def all_prefix_first_vowel(word, letters=list(ascii_uppercase)):
    """Finds the first vowel in a word and removes all letters before it,
    prefixing it with all consonants.

    Args:
        word (str) - the word to update
        letters (list) - the letters to use for prefixing.

    Returns:
        words (list) - All prefixed words

    """
    re_vowels = re.compile(r'[aeiouy]')
    matches = re.search(re_vowels, word)
    if matches is None:
        return [word]
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    first_match = matches.start(0)
    for letter in letters:
        if letter not in vowels:
            # If beginning letter is a vowel, don't offset the index
            if first_match == 0:
                words.append('{}{}'.format(letter, word))
            else:
                words.append('{}{}'.format(letter, word[first_match:]))
    return words


def recycle(words, func, times=2):
    """Runs a set of words applied to `func` and re-runs it
    `times` with the last output as the new input.
    `words` must be a list, and `func` must return a list."""
    if times > 0:
        return recycle(func(words), func, times - 1)
    return words


def super_scrub(data):
    """
    Runs words through a comprehensive
    list of filtering functions
    Expects a dictionary with key "words"
    """
    for technique in data['words']:
        data['words'][technique] = normalization.uniquify(
            normalization.remove_odd_sounding_words(
                normalization.clean_sort(
                    data['words'][technique])))
    return data


def generate_all_techniques(words):
    """
    Generates all techniques across the
    library in one place, and cleans them for use
    """
    data = {
        'words': {
            'alliterations': make_name_alliteration(words),
            'alliterations': make_name_alliteration(words),
            'portmanteau': make_portmanteau_default_vowel(words),
            'vowels': make_vowelify(words),
            'suffix': suffixify(words),
            'prefix': prefixify(words),
            'duplifix': duplifixify(words),
            'disfix': disfixify(words),
            'infix': infixify(words),
            'simulfix': simulfixify(words),
            'founder_product_name': make_founder_product_name(
                'Lindsey', 'Chris', 'Widgets'),
            'punctuator': make_punctuator_vowels(words),
            'name_abbreviation': make_name_abbreviation(words),
            'make_portmanteau_split': make_portmanteau_split(words),
            'forkerism': forkerism(words),
            'kniferism': kniferism(words),
            'spoonerism': spoonerism(words),
            'palindrome': palindromes(words),
            'reduplication_ablaut': reduplication_ablaut(words),
            'misspelling': make_misspelling(words),
            'descriptors': make_descriptors(
                get_descriptors(words))
        }
    }
    return super_scrub(data)
