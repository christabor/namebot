"""Metrics for measuring various aspects of words.

Conventions used in this utility:
1.  All functions return a dictionary,
    with key 'data' and/or 'summary':
    return {
        'data': data,
        'summary': summary or None
    }
"""

from __future__ import division
import re
from pattern.en import parse
from pattern.web import sort
from nltk import pos_tag


def prep_file(file_name):
    """Take a file, extracts items line-by-line, and returns a list of them.

    Args:
        file_name (str): The file name to open

    Returns:
        items (list): A list of items extracted from the file
    """
    items = []
    with open(file_name) as files:
        for newline in files:
            items.append(newline)
    return items


def get_named_numbers_1_10(words):
    """Return a summary of words spelled out (e.g. one, two).

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    matches = []
    numbers = re.compile(
        r'\Aone |two |three |four |five |six |seven |eight |nine |ten',
        re.IGNORECASE)
    for word in words:
        if re.findall(numbers, word):
            matches.append(word)
    return {
        'data': matches,
        'summary': 'Of {} words, {} matched'.format(len(words), len(matches))
    }


def name_length(words):
    """Check the length of each word and an average.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    names_length = []
    for val in words:
        names_length.append(len(val))
    summary = 'Of {} words, the average length of names is...{}'.format(
        len(words),
        round(sum(names_length) / len(names_length)))
    return {
        'data': names_length,
        'summary': summary
    }


def name_vowel_count(words):
    """Check the number of times vowels occurs, and total the results.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    num_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    try:
        for word in words:
            num_count['a'] += word.count('a')
            num_count['e'] += word.count('e')
            num_count['i'] += word.count('i')
            num_count['o'] += word.count('o')
            num_count['u'] += word.count('u')
    except AttributeError:
        pass
    finally:
        return {
            'data': num_count,
            'summary': None
        }


def name_starts_with_vowel(words):
    """Check the number of times a list of words starts with a vowel.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    vowelcount = 0
    vowels = re.compile(r'\A[aeiou]')
    for name in words:
        if re.match(vowels, name):
            vowelcount += 1
    summary = 'Of {} words, {} or {}% are vowels as the first letter.'.format(
        len(words), vowelcount,
        round(float(vowelcount) / len(words) * 100))
    return {
        'data': None,
        'summary': summary
    }


def get_digits_frequency(words):
    """Look for and count the digits in names, e.g. 7-11, 3M, etc...

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    new_words = []
    count = 0
    digits = re.compile(r'[0-9]+')
    for name in words:
        if re.findall(digits, name):
            count += 1
            matches = re.findall(digits, name)
            new_words += matches
    return {
        'data': new_words,
        'summary': ('Of {} words, {} have numbers in them, '
                    'with a total of {} numbers found.').format(
                        len(words), count, len(new_words))
    }


def get_first_letter_frequency(words):
    """Add the frequency of first letters e.g. [C]at, [C]law, c = 2.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    letters = {}
    # populate keys
    for name in words:
        letters[name[0]] = 0
    # add counts
    for name in words:
        letters[name[0]] += 1
    return {
        'data': letters,
        'summary': None
    }


def get_special_chars(words):
    """Find occurrences of special characters (non-alphabetical characters).

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    data = []
    chars = re.compile(r'[^a-z]', re.IGNORECASE)
    for word in words:
        if re.findall(chars, word):
            data += re.findall(chars, word)
    return {
        'data': data,
        'summary': ('{} occurrences of special characters were'
                    ' found in {} words.').format(len(data), len(words))
    }


def get_word_types(words):
    """Determine the occurrences of pos types.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    new_arr = []
    for val in words:
        try:
            val = parse(
                val,
                encoding='utf-8',
                tokenize=False,
                light=False,
                tags=True,
                chunks=False,
                relations=False,
                lemmata=False)
            new_arr.append(val)
        except IndexError:
            continue
    return {
        'data': new_arr,
        'summary': None
    }


def get_name_spaces(words):
    """Check number of spaces for a given set of words.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    results = [{'word': word, 'spaces': len(word.split(r' '))}
               for word in words]
    return {
        'data': results,
        'summary': None
    }


def get_consonant_repeat_frequency(words):
    """Check for repeating consonant frequency for a given set of words.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    count = 0
    cons = re.compile(r'[^a|e|i|o|u{6}]')
    for val in words:
        if re.match(cons, val):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_consonant_duplicate_repeat_frequency(words):
    """Check for duplicate repeating consonant frequency.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    count = 0
    cons_dup = re.compile(r'[^a|e|i|o|u]{1,}')
    for name in words:
        if re.match(cons_dup, name):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_vowel_repeat_frequency(words):
    """Check for repeating vowel frequency for a given set of words.

    Args:
        words (list): A list of words

    Returns:
        dict: The data and summary results.
    """
    count = 0
    cons_vowel = re.compile(r'[aeiou{3}]')
    for val in words:
        if re.match(cons_vowel, val):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_adjective_verb_or_noun(words):
    """Get the number of words that are classified as verbs or nouns.

    Args:
        words (TYPE): Description

    Returns:
        dict: The data and summary results.
    """
    total = len(words)
    data = {'verbs': 0, 'nouns': 0}
    verby = ['VBP', 'VB', 'RB', 'VBG']
    nouns = ['NN', 'NNP']
    for word, tag in pos_tag(words):
        if tag in nouns:
            data['nouns'] += 1
        elif tag in verby:
            data['verbs'] += 1
    remainder = total - (data['verbs'] + data['nouns'])
    return {
        'data': data,
        'summary': ('Of {0} words, {1} were nouns, {2} were verbs, '
                    'and {3} were everything else.').format(
                        total, data['nouns'], data['verbs'], remainder)
    }


def get_keyword_relevancy_map(words, n_list, terms, sortcontext,
                              enginetype='BING',
                              license=None):
    """http://www.clips.ua.ac.be/pages/pattern-web#sort."""
    results_list = []
    results = sort(
        terms=[],
        context=sortcontext,   # Term used for sorting.
        service=enginetype,    # GOOGLE, YAHOO, BING, ...
        license=None,          # You should supply your own API license key
        strict=True,           # Wraps query in quotes: 'mac sweet'.
        reverse=True,          # Reverse: 'sweet mac' <=> 'mac sweet'.
        cached=True)

    for weight, term in results:
        results.append("%5.2f" % (weight * 100) + "%", term)
    return {
        'data': results_list,
        'summary': None
    }


def categorize_word_type(words):
    """Get the common naming strategy 'category' of a name, based on precedence.

    Categories are derived from
    http://www.thenameinspector.com/10-name-types/,
    so it is important to note there is no agreed upon standard,
    meaning it is ultimately a little arbitrary.

    Since it is a bit challenging to actually determine its type,
    we give a weighting for each word based on a few known metrics.
    This can be updated in the future so that weightings are binary
    (e.g. 0.0 and 100.0), giving traditional False/True.

    Categories ====

    1. Real Words
     1a. Misspelled words
     1b. Foreign words
    2. Compounds
    3. Phrases
    4. Blends
    5. Tweaked
    6. Affixed
    7. Fake/obscure
    8. Puns
    9. People's names
    10. Initials and Acronyms

    Args:
        words (list): A list of words

    Returns:
        new_words (list) - A list of lists, with each word
                           and its distribution by word "type"
    """
    new_words = []

    def _get_distribution(word):
        # TODO:
        # misspelled, foreign, tweaked, affixed, fake_obscure,
        # initials_acronym, blend, puns, person, compound
        """Return the distribution for all categories, given a single word."""
        categories = {
            'real': 0,
            'misspelled': 0,
            'foreign': 0,
            'compound': 0,
            'phrase': 0,
            'blend': 0,
            'tweaked': 0,
            'affixed': 0,
            'fake_obscure': 0,
            'puns': 0,
            'person': 0,
            'initials_acronym': 0,
        }
        if len(word.split(' ')) == 1:
            # Real words are single
            categories['real'] = 50
        else:
            # Phrases are not
            categories['phrase'] = 50
        # If word cannot be tagged,
        # it's very likely fake_obscure
        if pos_tag([word])[0][1] == '-NONE-':
            categories['real'] = 0
            categories['fake_obscure'] = 75
        return categories

    for word in words:
        new_words.append([word, _get_distribution(word)])
    return new_words


def generate_all_metrics(filename=None, words=None):
    """Generate all metrics in this module in one place.

    Args:
        filename (str, optional): A filename to load words from.
        words (TYPE, optional): Words to use, if file is not specified.

    Returns:
        dict: All metrics results, keyed by name.
    """
    if not filename and not words:
        return None
    if filename:
        allnames = prep_file(filename)
    else:
        allnames = words
    return {
        'names': allnames,
        'metrics': {
            'digits_freq': get_digits_frequency(allnames),
            'length': name_length(allnames),
            'vowel_beginning': name_starts_with_vowel(allnames),
            'vowel_count': name_vowel_count(allnames),
            'name_length': name_length(allnames),
            'name_spaces': get_name_spaces(allnames),
            'consonant_repeat_freq': get_consonant_repeat_frequency(allnames),
            'consonant_dup_repeat_freq': get_consonant_duplicate_repeat_frequency(allnames),
            'vowel_repeat_freq': get_vowel_repeat_frequency(allnames),
            'special_characters': get_special_chars(allnames),
            'name_numbers': get_named_numbers_1_10(allnames),
            'adj_verb_noun': get_adjective_verb_or_noun(allnames),
            'first_letter_freq': get_first_letter_frequency(allnames),
            'word_types': get_word_types(allnames)
        }
    }
