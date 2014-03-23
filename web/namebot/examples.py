from __future__ import absolute_import

from . import nlp
from . import techniques
from . import metrics
from . import scoring


def example_synsets(words=None):
    if not words:
        return
    data = nlp.get_synsets(
        words=words,
        use_definitions=True)
    return data


def example_synset_categories():
    return nlp.print_all_synset_categories()


def example_techniques(words=None):
    return techniques.generate_all_techniques(words)


def example_scoring(words=None):
    test_scoring = scoring.NamebotScoring()
    return test_scoring.generate_all_scoring(words)


def example_metrics(filename=None, words=None):
    if not filename and not words:
        return None
    test = metrics.NameBotMetrics()
    if filename:
        allnames = test.open_file(filename)
    else:
        allnames = words
    results = {
        'names': allnames,
        'metrics': {
            'digits_freq': test.get_digits_frequency(allnames),
            'length': test.name_length(allnames),
            'vowel_beginning': test.name_starts_with_vowel(allnames),
            'vowel_count': test.name_vowel_count(allnames),
            'name_length': test.name_length(allnames),
            'name_spaces': test.get_name_spaces(allnames),
            'consonant_repeat_freq': test.get_consonant_repeat_frequency(allnames),
            'consonant_duplicate_repeat_freq': test.get_consonant_duplicate_repeat_frequency(allnames),
            'vowel_repeat_freq': test.get_vowel_repeat_frequency(allnames),
            'special_characters': test.get_special_chars(allnames),
            'search_results': test.get_search_results(allnames),
            'name_numbers': test.get_named_numbers(allnames),
            'adj_verb_noun': test.get_adjective_verb_or_noun(allnames),
            'first_letter_freq': test.get_first_letter_frequency(allnames),
            'word_types': test.get_word_types(allnames)
        }
    }
    return results


def generate_all_examples(filename=None, words=None):
    print '< ##=========##===========##=========## > '
    print '... -=|=- Running ALL the examples -=|=- ... '
    print '< ##=========##===========##=========## > '

    example_data = {
        'synsets': example_synsets(words=words),
        'metrics': example_metrics(filename=filename, words=words),
        'techniques': example_techniques(words=words),
        'scoring': example_scoring(words=words)
    }
    return example_data
