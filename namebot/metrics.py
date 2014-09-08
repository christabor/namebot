from __future__ import division
import re
from pattern.en import parse
from pattern.web import sort


"""
    Conventions used in this utility:
    1.  All functions return a dictionary,
        with key 'data' and/or 'summary':
        return {
            'data': data,
            'summary': summary or None
        }

"""


def prep_file(file_name=None):
    if file_name is None:
        return
    file_name = file_name
    items = []
    with open(file_name) as files:
        for newline in files:
            items.append(newline)
    return items


def get_named_numbers(name_list):
    """
    Check for numbers spelled out
    e.g. One, Two, Three, Four
    """
    matches = []
    numbers = re.compile(
        r'\AOne |Two |Three |Four |Five |Six |Seven |Eight |Nine |Ten ')
    for word in name_list:
        if re.findall(numbers, word):
            matches.append(word)
    summary = 'Of {} words {} matched'.format(
        len(name_list), len(matches))
    return {
        'data': matches,
        'summary': summary
    }


def name_length(name_list):
    names_length = []
    for val in name_list:
        names_length.append(len(val))
    summary = 'Of {} words, the average length of names is...{}'.format(
        len(name_list),
        round(sum(names_length) / len(names_length)))
    return {
        'data': names_length,
        'summary': summary
    }


def name_vowel_count(name_list):
    num_count = {}
    num_count['a'] = 0
    num_count['e'] = 0
    num_count['i'] = 0
    num_count['o'] = 0
    num_count['u'] = 0

    try:
        for word in name_list:
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


def name_starts_with_vowel(name_list):
    vowelcount = 0
    vowels = re.compile(r'\A[aeiou]')
    for name in name_list:
        if re.match(vowels, name):
            vowelcount += 1
    summary = 'Of {} words, {} or {}% are vowels as the first letter.'.format(
        len(name_list),
        vowelcount,
        vowelcount % len(name_list))
    return {
        'data': None,
        'summary': summary
    }


def get_search_results(name_list):
    # TODO FIXME
    # values = []
    #
    # for name in name_list:
    #     engine = Bing(
    #         license=None)
    #     searches = engine.search(
    #         name,
    #         type='SEARCH',
    #         start=1,
    #         count=10000,
    #         sort='RELEVANCY',
    #         size=None,
    #         cached=False,)
    #     values.append(name, len(searches))

    # summary = 'VAL: {} SEARCHES: {} {}'.format(
    #     name,
    #     len(searches),
    #     searches)
    # return {
    #     'data': values,
    #     'summary': summary
    # }
    return {
        'data': None,
        'summary': None
    }


def get_digits_frequency(name_list):
    """
    Look for and count the
    digits in names, e.g. 7-11, 3M, etc...
    """
    new_arr = []
    digits = re.compile(r'[0-9]+')
    for name in name_list:
        if re.findall(digits, name):
            matches = re.findall(digits, name)
            new_arr.append(matches)
    return {
        'data': new_arr,
        'summary': None
    }


def get_first_letter_frequency(name_list):
    """
    Add the frequency of first letters
    e.g. [C]at, [C]law, c = 2
    """
    letters = {}
    # populate keys
    for name in name_list:
        letters[name[0]] = 0

    # add counts
    for name in name_list:
        letters[name[0]] += 1

    return {
        'data': letters,
        'summary': None
    }


def get_special_chars(words):
    data = []
    words_matched = 0
    chars = re.compile(r'[^a-z]', re.IGNORECASE)
    for word in words:
        if re.findall(chars, word):
            data += re.findall(chars, word)
            words_matched += 1
    summary = '{} special characters were found in {} words.'.format(
        len(data),
        words_matched)
    return {
        'data': data,
        'summary': summary
    }


def get_word_types(name_list):
    new_arr = []
    for val in name_list:
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


def get_name_spaces(name_list):
    num_arr = []
    spaces = r'\s'
    for val in name_list:
        if re.match(spaces, val):
            splits = val.split()
            num_arr.append(len(splits))
    return {
        'data': num_arr,
        'summary': None
    }


def get_consonant_repeat_frequency(name_list):
    count = 0
    cons = re.compile(r'[^aeiou]{6}')
    for val in name_list:
        if re.match(cons, val):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_consonant_duplicate_repeat_frequency(name_list):
    count = 0
    cons_dup = re.compile(r'[^a]{3}[^e]{3}[^i]{3}[^o]{3}[^u]{3}')
    for name in name_list:
        if re.match(cons_dup, name):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_vowel_repeat_frequency(name_list):
    count = 0
    cons_vowel = re.compile(r'[aeiou]{3}')
    for val in name_list:
        if re.match(cons_vowel, val):
            count += 1
    return {
        'data': count,
        'summary': None
    }


def get_adjective_verb_or_noun(name_list):
    # TODO ADD
    return {
        'data': None,
        'summary': None
    }


def get_keyword_relevancy_map(name_list, n_list, terms, sortcontext,
                              enginetype='BING',
                              license=None):
    """
    http://www.clips.ua.ac.be/pages/pattern-web#sort
    """
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


def check_trademark_registration(name_list):
    """
    search the USTM office and return
    the number of results, and
    what they are (if applicable)
    """
    return {
        'data': None,
        'summary': None
    }


def check_domain_searches(name_list):
    """
    check domains for each name...
    perhap hook into other domain
    name generators, sites..?
    """
    return {
        'data': None,
        'summary': None
    }


def get_search_result_count(name_list):
    """
    check google results and return
    a number of results (number)

    http://www.clips.ua.ac.be/pages/pattern-web#DOM
    """
    return {
        'data': None,
        'summary': None
    }


def get_word_ranking(name_list):
    """
    use google results and get a quality of
    ranking based on other metrics such as
    domain name availability,
    google results and others.
    """
    results = []
    for name in name_list:
        results = get_search_result_count(name_list)
        domains = check_domain_searches(name_list)
        results.append(results / domains)
    return
    return {
        'data': results,
        'summary': None
    }


def generate_all_metrics(filename=None, words=None):
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
            'search_results': get_search_results(allnames),
            'name_numbers': get_named_numbers(allnames),
            'adj_verb_noun': get_adjective_verb_or_noun(allnames),
            'first_letter_freq': get_first_letter_frequency(allnames),
            'word_types': get_word_types(allnames)
        }
    }
