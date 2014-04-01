from __future__ import absolute_import
from __future__ import division

from random import choice
import re
import nltk

from . import settings as namebot_settings
from . import normalization


___prefixes___ = namebot_settings.PREFIXES
___suffixes___ = namebot_settings.SUFFIXES
___alphabet___ = namebot_settings.ALPHABET
___vowels___ = namebot_settings.VOWELS
___regexes___ = namebot_settings.regexes


def spoonerism(words):
    "First: [f]oo [b]ar => boo far"
    new_words = []
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
    "Mid: f[o]o b[a]r => fao bor"
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
    "Last: fo[o] ba[r] => for bao"
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


def reduplication_ablaut(words, count=1):
    """
    http://phrases.org.uk/meanings/reduplication.html
    A technique to combine words and altering the vowels
    e.g ch[i]t-ch[a]t, d[i]lly, d[a]lly
    """

    new_words = []
    for word in words:
        second = re.sub(
            r'a|e|i|o|u',
            choice(___vowels___),
            word,
            count=count)
        # Only append if the
        # first and second are different.
        if word != second:
            new_words.append('{} {}'.format(word, second))
    return new_words


def affix_words(words, affix_type):
    """
    Do some type of affixing technique,
    such as prefixing or suffixing.
    TODO FINISH *-fixes from article
    """
    new_arr = []
    if len(words):
        if affix_type is 'prefix':
            for v in words:
                for v1 in ___prefixes___:
                    if v1 is not None:
                        first_prefix_no_vowel = re.search(
                            ___regexes___['no_vowels'], v[0])
                        second_prefix_no_vowel = re.search(
                            ___regexes___['no_vowels'], v1[0])
                        if first_prefix_no_vowel or second_prefix_no_vowel:
                                    # if there's a vowel at the end of
                                    # prefix but not at the beginning
                                    # of the word (or vice versa)
                                    vowel_beginning = re.search(
                                        r'a|e|i|o|u', v1[-1:])
                                    vowel_end = re.search(
                                        r'^a|e|i|o|u', v[:1])
                                    if vowel_beginning or vowel_end:
                                        new_arr.append('{}{}'.format(v1, v))

        elif affix_type is 'suffix':
            for v in words:
                for suffix in ___suffixes___:
                    if suffix is not None:
                        prefix_start_vowel = re.search(
                            ___regexes___['all_vowels'], v[0])
                        suffix_start_vowel = re.search(
                            ___regexes___['all_vowels'], suffix[0])
                        if prefix_start_vowel or suffix_start_vowel:
                                if suffix is "ify":
                                    if v[-1] is "e":
                                        if v[-2] is not "i":
                                            new_arr.append('{}{}'.format(
                                                v[:-2], suffix))
                                        else:
                                            new_arr.append(
                                                '{}{}'.format(
                                                    v[:-1], suffix))
                                    new_arr.append(v + suffix)
                                else:
                                    new_arr.append(v + suffix)

        elif affix_type is 'duplifix':
            """
            makes duplification
            (e.g: teeny weeny, etc...)
            """
            for v in words:
                for letter in ___alphabet___:
                    vowel_first = re.match(
                        ___regexes___['all_vowels'], v[1])
                    no_vowel_letter = re.match(
                        ___regexes___['no_vowels'], letter)
                    no_vowel_first = re.match(
                        ___regexes___['no_vowels'], v[1])
                    vowel_letter = re.match(
                        ___regexes___['all_vowels'], letter)
                    # check if the first letter is
                    # NOT the same as the second letter in reduplication
                    if v[0] is not letter:
                        # check if the first word is
                        # NOT the same as the second word. (or letter)
                        if v is not letter + v[1:]:
                            if vowel_first:
                                if no_vowel_letter:
                                    new_arr.append('{} {}{}'.format(
                                        v, letter,
                                        v[1:]))
                            elif no_vowel_first:
                                if vowel_letter:
                                    new_arr.append('{} {}{}'.format(
                                        v, letter,
                                        v[1:]))
        elif affix_type is "infix":
            pass

        elif affix_type is "disfix":
            pass

    return new_arr


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


def make_name_obscured(words):
    """
    Takes a name and makes it obscure,
    ala Bebo, Ning, Bix, Jajah, Kiko.

    TODO ADDME
    """
    return


def make_cc_to_vc_swap(arr):
    """
    make name based on original word,
    but swap a CC with a V+C combo.
    if no double CC is found, skip it.

    origination: zappos -> zapatos

    examples:
        christopher -> christofaher
        christopher -> christokoer
        marshmallow -> margimallow

    TODO ADDME
    """
    return


def make_name_alliteration(word_array):
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
                new_arr.append(word1 + ' ' + word2)

    return new_arr


def make_name_abbreviation(words):
    """
    this function will make some kind of
    interesting company acronym
    eg: BASF, AT&T, A&W
    """
    new_arr = []
    for word in words:
        new_arr.append(
            word[:1].upper() +
            word[:2].upper() +
            word[:3].upper() +
            word[:4].upper())
    return new_arr


def make_vowel(words, vowel_type, vowel_index):
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

                # if starting index is 0,
                # add 1 to it so we're not dividing by zero
                if pos_i is 0:
                    pos_i = 1
                elif pos_j is 0:
                    pos_j = 1

                # decide which word should be the
                # prefix and which should be suffix
                if round(pos_i / len_i) > round(pos_j / len_j):
                    p = i[0: pos_i + 1]
                    p2 = j[pos_j: len(j)]
                    if len(p) + len(p2) > 2:
                        if re.search(
                            ___regexes___['all_vowels'], p) or re.search(
                                ___regexes___['all_vowels'], p2):
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
    in first word and matching vowel in second word

    TODO: More powerful, usable
    """
    new_arr = []
    vowel_a_re = re.compile(r'a{1}')
    vowel_e_re = re.compile(r'e{1}')
    vowel_i_re = re.compile(r'i{1}')
    vowel_o_re = re.compile(r'o{1}')
    vowel_u_re = re.compile(r'u{1}')

    make_vowel(words, vowel_a_re, "a")
    make_vowel(words, vowel_e_re, "e")
    make_vowel(words, vowel_i_re, "i")
    make_vowel(words, vowel_o_re, "o")
    make_vowel(words, vowel_u_re, "u")
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
                    l1 = re.search(r'[^aeiou{1}]+[aeiou{1}]', i)
                    l2 = re.search(r'[aeiou{1}]+[^aeiou{1}]$', j)
                    if i is not None and l1 and l2:
                        # third letter used for
                        # consonant middle splits only
                        l3 = re.split(r'[aeiou{1}]', i)
                        l1 = l1.group(0)
                        l2 = l2.group(0)
                        if len(l3) is not 0:
                            if l3 is not None:
                                for v in l3:
                                    new_arr.append(l1 + v + l2)
                            else:
                                new_arr.append('{}{}{}'.format(l1, 't', l2))
                                new_arr.append('{}{}{}'.format(l1, 's', l2))
                                new_arr.append('{}{}{}'.format(l1, 'z', l2))
                                new_arr.append('{}{}{}'.format(l1, 'x', l2))
    return new_arr


def make_punctuator(words):
    """
    put some random punctation like
    hyphens etc in there, only around vowels
    (ala del.ic.ious and others)
    """
    new_arr = []
    for word in words:
        vowels = re.compile(r'[aeiou]')
        if re.match(vowels, word) and len(word) > 4:
            spl = re.split(
                '([?=aeiou])',
                word,
                maxsplit=2)
            j1 = '-'.join(spl[1:])
            j2 = '.'.join(spl[1:])
            new_arr.append(j1)
            new_arr.append(j2)
    return new_arr


def make_vowelify(words):
    """
    chop off consonant ala nautica
    if second to last letter is a vowel.
    """
    new_arr = []
    vowels = re.compile(r'[aeiou]')
    for word in words:
        if re.search(vowels, word[:-2]):
            new_arr.append(word[:-1])
    return new_arr


def make_misspelling(words):
    """
    This is used as the primary "misspelling"
    technique, through a few different techniques
    that are all categorized as misspelling.

    Brute force all combinations,
    then use double metaphone to remove odd ones.
    ...find a better way to do this TODO

    """

    new_arr = []
    for i in words:
        new_arr.append(i.replace('ics', 'ix'))
        new_arr.append(i.replace('ph', 'f'))
        new_arr.append(i.replace('kew', 'cue'))
        new_arr.append(i.replace('f', 'ph'))
        new_arr.append(i.replace('o', 'ough'))

        # # these seem to have
        # # sucked in practice
        new_arr.append(i.replace('o', 'off'))
        new_arr.append(i.replace('ow', 'o'))
        new_arr.append(i.replace('x', 'ecks'))

        new_arr.append(i.replace('za', 'xa'))
        new_arr.append(i.replace('xa', 'za'))
        new_arr.append(i.replace('ze', 'xe'))
        new_arr.append(i.replace('xe', 'ze'))
        new_arr.append(i.replace('zi', 'xi'))
        new_arr.append(i.replace('xi', 'zi'))
        new_arr.append(i.replace('zo', 'xo'))
        new_arr.append(i.replace('xo', 'zo'))
        new_arr.append(i.replace('zu', 'xu'))
        new_arr.append(i.replace('xu', 'zu'))

        # number based
        new_arr.append(i.replace('one', '1'))
        new_arr.append(i.replace('1', 'one'))
        new_arr.append(i.replace('two', '2'))
        new_arr.append(i.replace('2', 'two'))
        new_arr.append(i.replace('three', '3'))
        new_arr.append(i.replace('3', 'three'))
        new_arr.append(i.replace('four', '4'))
        new_arr.append(i.replace('4', 'four'))
        new_arr.append(i.replace('five', '5'))
        new_arr.append(i.replace('5', 'five'))
        new_arr.append(i.replace('six', '6'))
        new_arr.append(i.replace('6', 'six'))
        new_arr.append(i.replace('seven', '7'))
        new_arr.append(i.replace('7', 'seven'))
        new_arr.append(i.replace('eight', '8'))
        new_arr.append(i.replace('8', 'eight'))
        new_arr.append(i.replace('nine', '9'))
        new_arr.append(i.replace('9', 'nine'))
        new_arr.append(i.replace('ten', '10'))
        new_arr.append(i.replace('10', 'ten'))

        new_arr.append(i.replace('ecks', 'x'))
        new_arr.append(i.replace('spir', 'speer'))
        new_arr.append(i.replace('speer', 'spir'))
        new_arr.append(i.replace('x', 'ex'))
        new_arr.append(i.replace('on', 'awn'))
        new_arr.append(i.replace('ow', 'owoo'))
        new_arr.append(i.replace('awn', 'on'))
        new_arr.append(i.replace('awf', 'off'))
        new_arr.append(i.replace('s', 'z'))
        new_arr.append(i.replace('ce', 'ze'))
        new_arr.append(i.replace('ss', 'zz'))
        new_arr.append(i.replace('ku', 'koo'))
        new_arr.append(i.replace('trate', 'trait'))
        new_arr.append(i.replace('trait', 'trate'))
        new_arr.append(i.replace('ance', 'anz'))
        new_arr.append(i.replace('il', 'yll'))
        new_arr.append(i.replace('ice', 'ize'))
        new_arr.append(i.replace('chr', 'kr'))

        # These should only be at end of word!
        new_arr.append(i.replace('er', 'r'))
        new_arr.append(i.replace('lee', 'ly'))
    return new_arr


def make_name_from_latin_root(name_list):
    # TODO ADDME
    """
    This will take a latin word that is returned
    from a seperate lookup function and tweak it
    for misspelling specifc to latin roots.
    """
    new_arr = []
    # for i, item in enumerate(name_list):
    #     print name_list[i]
    return new_arr


def make_word_metaphor(words):
    # TODO ADDME
    """
    Make a metaphor based
    on some words...?
    """
    new_arr = []
    return new_arr


def make_phrase(words):
    # TODO ADDME
    """
    WIP (e.g.
        simplyhired, second life,
        stumbleupon)
    """
    return


def get_descriptors(words):
    """
    Use NLTK to first grab tokens by looping through words,
    then tag part-of-speech (in isolation)
    and provide a dictionary with a list of each type
    for later retrieval and usage
    """

    descriptors = {}
    tokens = nltk.word_tokenize(' '.join(words))
    parts = nltk.pos_tag(tokens)

    # TODO ADD freq. measurement to metrics

    """
    populate with an empty array for each type
    so no KeyErrors will be thrown,
    and no knowledge of NLTK classification
    is required
    """
    for part in parts:
        descriptors[part[1]] = []

    # Then, push the word into the matching type
    for part in parts:
        descriptors[part[1]].append(part[0])

    return descriptors


def make_descriptors(words):
    """
    Make descriptor names based off of a
    verb or adjective and noun combination.
    Examples:
        -Pop Cap,
        -Big Fish,
        -Red Fin,
        -Cold Water (grill), etc...

    Combines VBP/VB, with NN/NNS

    ...could be optimized
    """
    new_words = []
    try:
        for noun in words['NN']:
            for verb in words['VBP']:
                new_words.append('{} {}'.format(noun, verb))
                new_words.append('{} {}'.format(verb, noun))
    except KeyError:
        pass
    try:
        for noun in words['NNS']:
            for verb in words['VB']:
                new_words.append('{} {}'.format(noun, verb))
                new_words.append('{} {}'.format(verb, noun))
    except KeyError:
        pass
    try:
        for noun in words['NNS']:
            for verb in words['VBP']:
                new_words.append('{} {}'.format(noun, verb))
                new_words.append('{} {}'.format(verb, noun))
    except KeyError:
        pass
    try:
        for noun in words['NN']:
            for verb in words['VB']:
                new_words.append('{} {}'.format(noun, verb))
                new_words.append('{} {}'.format(verb, noun))
    except KeyError:
        pass
    return new_words


def super_scrub(data):
    """
    Runs words through a comprehensive
    list of filtering functions

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
            'suffix': affix_words(words, 'suffix'),
            'prefix': affix_words(words, 'prefix'),
            'duplifix': affix_words(words, 'duplifix'),
            'disfix': affix_words(words, 'disfix'),
            'infix': affix_words(words, 'infix'),
            'founder_product_name': make_founder_product_name(
                'Lindsey', 'Chris', 'Widgets'),
            'cc_to_vc_swap': make_cc_to_vc_swap(words),
            'name_obscured': make_name_obscured(words),
            'punctuator': make_punctuator(words),
            'name_abbreviation': make_name_abbreviation(words),
            'make_portmanteau_split': make_portmanteau_split(words),
            'latin_root': make_name_from_latin_root(words),
            'make_word_metaphor': make_word_metaphor(words),
            'make_phrase': make_phrase(words),
            'forkerism': forkerism(words),
            'kniferism': kniferism(words),
            'spoonerism': spoonerism(words),
            'reduplication_ablaut': reduplication_ablaut(words),
            'misspelling': make_misspelling(words),
            'descriptors': make_descriptors(
                get_descriptors(words))
        }
    }
    return super_scrub(data)
