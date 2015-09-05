from __future__ import absolute_import
import itertools
from nltk.corpus import wordnet

from . import normalization

"""
def get_recursive_synsets(word, base_case=4):

TODO ADDME

perhaps this can have a threshold argument
that determines how recursively down the
*nym should go within a given synset,
and have a default that is crafted over practice

will obtain a synset, grab that synsets
value and continue recursively until a
base case is reached, defaulting to depth 4

# base = 0
# if not base_case >= base:
#   return get_recursive_synsets(word, base_case=base+=1)
    # stem and remove punctuation, if any

E.G:
for k in new_array:
t = synset.hyponyms()
for sub_t in t:
#print "sub sub hyponyms", sub_t.hyponyms()
x = sub_t.hyponyms()
for sub_sub_t in x:
y = sub_sub_t.hyponyms()
for sub_sub_sub_t in y:
print "sub sub sub sub hyponyms",sub_sub_sub_t.hyponyms()

"""


def print_all_synset_categories():
    # Prints all domains and
    # categories for research purposes
    categories = []
    for synset in list(wordnet.all_synsets('n')):
        categories.append(synset)
    return categories


def _get_lemma_names(sub_synset, use_definitions=False):
    results = []
    if sub_synset():
        for v in sub_synset():
            results += v.lemma_names()
            if use_definitions:
                results.append(v.definition.split())
    return results


def get_hyponyms(synset, use_definitions=False):
    return _get_lemma_names(synset.hyponyms, use_definitions=use_definitions)


def get_inst_hyponyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.instance_hyponyms, use_definitions=use_definitions)


def get_member_meronyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.member_meronyms, use_definitions=use_definitions)


def get_substance_meronyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.substance_meronyms, use_definitions=use_definitions)


def get_part_meronyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.part_meronyms, use_definitions=use_definitions)


def get_substance_holoynms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.substance_holonyms, use_definitions=use_definitions)


def get_topic_domains(synset, use_definitions=False):
    return _get_lemma_names(
        synset.topic_domains, use_definitions=use_definitions)


def get_region_domains(synset, use_definitions=False):
    return _get_lemma_names(
        synset.region_domains, use_definitions=use_definitions)


def get_usage_domains(synset, use_definitions=False):
    return _get_lemma_names(
        synset.usage_domains, use_definitions=use_definitions)


def get_attributes(synset, use_definitions=False):
    return _get_lemma_names(
        synset.attributes, use_definitions=use_definitions)


def get_entailments(synset, use_definitions=False):
    return _get_lemma_names(
        synset.entailments, use_definitions=use_definitions)


def get_causes(synset, use_definitions=False):
    if synset.causes():
        return _get_lemma_names(
            synset.causes, use_definitions=use_definitions)


def get_also_sees(synset, use_definitions=False):
    return _get_lemma_names(
        synset.also_sees, use_definitions=use_definitions)


def get_verb_groups(synset, use_definitions=False):
    return _get_lemma_names(
        synset.verb_groups, use_definitions=use_definitions)


def get_similartos(synset, use_definitions=False):
    return _get_lemma_names(
        synset.similar_tos, use_definitions=use_definitions)


def get_member_holoynms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.member_holonyms, use_definitions=use_definitions)


def get_part_holoynms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.part_holonyms, use_definitions=use_definitions)


def get_instance_hypernyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.instance_hypernyms, use_definitions=use_definitions)


def get_hypernyms(synset, use_definitions=False):
    return _get_lemma_names(
        synset.hypernyms, use_definitions=use_definitions)


def get_word_synsets(word):
    synset = wordnet.synsets(word.encode("utf-8"), pos=None)
    return synset


def get_synsets(words=[], use_definitions=False, clean=False):
    """This is a brute force method of getting as many related words
    to a given set as possible. You are expected to filter or remove any
    that are not relevant separately, if the resultant set is too long.
    The scoring module provides tools to filter based on pronunciation,
    but you can write your own and extend the functionality."""
    results = {}

    for word in words:
        synsets = get_word_synsets(word)

        key = {'synset_original': []}

        for synset in synsets:
            key['synset_original'].append(synset.lemma_names())

            # More Specific *nyms (deep)
            key['hyponyms'] = get_hyponyms(synset)
            key['instance_hyponyms'] = get_inst_hyponyms(synset)
            key['member_meronyms'] = get_member_meronyms(synset)
            key['substance_meronyms'] = get_substance_meronyms(synset)
            key['part_meronyms'] = get_part_meronyms(synset)
            key['substance_holonyms'] = get_substance_holoynms(synset)

            # More Generic *nyms (shallow)
            key['member_holonyms'] = get_member_holoynms(synset)
            key['part_holonyms'] = get_part_holoynms(synset)
            key['instance_hypernyms'] = get_instance_hypernyms(synset)
            key['hypernyms'] = get_hypernyms(synset)

            # Other types
            # (need classification) TODO

            key['topic_domains'] = get_topic_domains(synset)
            key['region_domains'] = get_region_domains(synset)
            key['usage_domains'] = get_usage_domains(synset)
            key['attributes'] = get_attributes(synset)
            key['entailments'] = get_entailments(synset)
            key['causes'] = get_causes(synset)
            key['also_sees'] = get_also_sees(synset)
            key['verb_groups'] = get_verb_groups(synset)
            key['similar_tos'] = get_similartos(synset)

        results[word] = key

    # 1. get words back
    # 2. flatten nested array
    # 3. split up words
    # 4. filter, clean, stem, uniquify

    for nlp_type in results:
        if clean:
            results[nlp_type] = sorted(
                normalization.uniquify(
                    normalization.clean_sort(
                        normalization.remove_stop_words(
                            normalization.stem_words(
                                normalization.remove_bad_words(
                                    list(itertools.chain(
                                        *results[nlp_type]))))))))

    return results
