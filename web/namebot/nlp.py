from __future__ import absolute_import
import itertools
from nltk.corpus import wordnet

from . import normalization

"""
def getRecursiveSynsets(word, base_case=4):

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
#   return getRecursiveSynsets(word, base_case=base+=1)
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
    """
    Prints all domains and
    categories for research purposes
    """
    categories = []
    for synset in list(wordnet.all_synsets('n')):
        categories.append(synset)
    return categories


def get_synsets(words=None, use_definitions=False):
    """This is a brute force method of getting as many related words
    to a given set as possible. You are expected to filter or remove any
    that are not relevant separately, if the resultant is too long.
    The scoring module provides tools to filter based on pronunciation,
    but you can write your own and extend the functionality."""
    results = {
        'words': {}
    }

    for word in words:
        synsets = wordnet.synsets(
            word.encode("utf-8"),
            pos=None)

        for synset in synsets:
            results['synset_original'] = []
            results['synset_original'].append(synset.lemma_names)
            if use_definitions:
                results['synset_original'].append(
                    synset.definition.split())

            """
            More Specific *nyms (deep)
            """

            if synset.hyponyms():
                results['hyponyms'] = []
                for v in synset.hyponyms():
                    results['hyponyms'].append(v.lemma_names)
                    if use_definitions:
                        results['hyponyms'].append(
                            v.definition.split())

            if synset.instance_hyponyms():
                results['instance_hyponyms'] = []
                for v in synset.instance_hyponyms():
                    results['instance_hyponyms'].append(v.lemma_names)
                    if use_definitions:
                        results['instance_hyponyms'].append(
                            v.definition.split())

            if synset.member_meronyms():
                results['member_meronyms'] = []
                for v in synset.member_meronyms():
                    results['member_meronyms'].append(v.lemma_names)
                    if use_definitions:
                        results['member_meronyms'].append(
                            v.definition.split())

            if synset.substance_meronyms():
                results['substance_meronyms'] = []
                for v in synset.substance_meronyms():
                    results['substance_meronyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results.append(
                            v.definition.split())

            if synset.part_meronyms():
                results['part_meronyms'] = []
                for v in synset.part_meronyms():
                    results['part_meronyms'].append(v.lemma_names)
                    if use_definitions:
                        results['part_meronyms'].append(
                            v.definition.split())

            if synset.substance_holonyms():
                results['substance_holonyms'] = []
                for v in synset.substance_holonyms():
                    results['substance_holonyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results['substance_holonyms'].append(
                            v.definition.split())

            """
            More Generic *nyms (shallow)
            """

            if synset.member_holonyms():
                results['causes'] = []
                for v in synset.member_holonyms():
                    results['causes'].append(v.lemma_names)
                    if use_definitions:
                        results['causes'].append(
                            v.definition.split())

            if synset.part_holonyms():
                results['part_holonyms'] = []
                for v in synset.part_holonyms():
                    results['part_holonyms'].append(v.lemma_names)
                    if use_definitions:
                        results['part_holonyms'].append(
                            v.definition.split())

            if synset.instance_hypernyms():
                results['instance_hypernyms'] = []
                for v in synset.instance_hypernyms():
                    results['instance_hypernyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results['instance_hypernyms'].append(
                            v.definition.split())

            if synset.hypernyms():
                results['hypernyms'] = []
                for v in synset.hypernyms():
                    results['hypernyms'].append(v.lemma_names)
                    if use_definitions:
                        results['hypernyms'].append(
                            v.definition.split())

            """
            Other types
            (need classification) TODO
            """

            if synset.topic_domains():
                results['topic_domains'] = []
                for v in synset.topic_domains():
                    results['topic_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['topic_domains'].append(
                            v.definition.split())

            if synset.region_domains():
                results['region_domains'] = []
                for v in synset.region_domains():
                    results['region_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['region_domains'].append(
                            v.definition.split())

            if synset.usage_domains():
                results['usage_domains'] = []
                for v in synset.usage_domains():
                    results['usage_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['usage_domains'].append(
                            v.definition.split())

            if synset.attributes():
                results['attributes'] = []
                for v in synset.attributes():
                    results['attributes'].append(v.lemma_names)
                    if use_definitions:
                        results['attributes'].append(
                            v.definition.split())

            if synset.entailments():
                results['entailments'] = []
                for v in synset.entailments():
                    results['entailments'].append(v.lemma_names)
                    if use_definitions:
                        results['entailments'].append(
                            v.definition.split())

            if synset.causes():
                results['causes'] = []
                for v in synset.causes():
                    results['causes'].append(v.lemma_names)
                    if use_definitions:
                        results['causes'].append(
                            v.definition.split())

            if synset.also_sees():
                results['also_sees'] = []
                for v in synset.also_sees():
                    results['also_sees'].append(v.lemma_names)
                    if use_definitions:
                        results['also_sees'].append(
                            v.definition.split())

            if synset.verb_groups():
                results['verb_groups'] = []
                for v in synset.verb_groups():
                    results['verb_groups'].append(v.lemma_names)
                    if use_definitions:
                        results['verb_groups'].append(
                            v.definition.split())

            if synset.similar_tos():
                results['similar_tos'] = []
                for v in synset.similar_tos():
                    results['similar_tos'].append(v.lemma_names)
                    if use_definitions:
                        results['similar_tos'].append(
                            v.definition.split())

    """
    1. get words back
    2. flatten nested array
    3. split up words
    4. filter, clean, stem, uniquify
    """

    for nlp_type in results:
        results[nlp_type] = sorted(
            normalization.uniquify(
                normalization.clean_sort(
                    normalization.remove_stop_words(
                        normalization.stem_words(
                            normalization.remove_bad_words(
                                list(itertools.chain(
                                    *results[nlp_type]))))))))

    return results
