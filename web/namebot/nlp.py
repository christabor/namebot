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
    results = {
        'words': {}
    }

    for word in words:
        synsets = wordnet.synsets(
            word.encode("utf-8"),
            pos=None)

        for synset in synsets:
            results['words']['synset_original'] = []
            results['words']['synset_original'].append(synset.lemma_names)
            if use_definitions:
                results['words']['synset_original'].append(
                    synset.definition.split())

            """
            More Specific *nyms (deep)
            """

            if synset.hyponyms():
                results['words']['hyponyms'] = []
                for v in synset.hyponyms():
                    results['words']['hyponyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['hyponyms'].append(
                            v.definition.split())

            if synset.instance_hyponyms():
                results['words']['instance_hyponyms'] = []
                for v in synset.instance_hyponyms():
                    results['words']['instance_hyponyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['instance_hyponyms'].append(
                            v.definition.split())

            if synset.member_meronyms():
                results['words']['member_meronyms'] = []
                for v in synset.member_meronyms():
                    results['words']['member_meronyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['member_meronyms'].append(
                            v.definition.split())

            if synset.substance_meronyms():
                results['words']['substance_meronyms'] = []
                for v in synset.substance_meronyms():
                    results['words']['substance_meronyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results['words'].append(
                            v.definition.split())

            if synset.part_meronyms():
                results['words']['part_meronyms'] = []
                for v in synset.part_meronyms():
                    results['words']['part_meronyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['part_meronyms'].append(
                            v.definition.split())

            if synset.substance_holonyms():
                results['words']['substance_holonyms'] = []
                for v in synset.substance_holonyms():
                    results['words']['substance_holonyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results['words']['substance_holonyms'].append(
                            v.definition.split())

            """
            More Generic *nyms (shallow)
            """

            if synset.member_holonyms():
                results['words']['causes'] = []
                for v in synset.member_holonyms():
                    results['words']['causes'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['causes'].append(
                            v.definition.split())

            if synset.part_holonyms():
                results['words']['part_holonyms'] = []
                for v in synset.part_holonyms():
                    results['words']['part_holonyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['part_holonyms'].append(
                            v.definition.split())

            if synset.instance_hypernyms():
                results['words']['instance_hypernyms'] = []
                for v in synset.instance_hypernyms():
                    results['words']['instance_hypernyms'].append(
                        v.lemma_names)
                    if use_definitions:
                        results['words']['instance_hypernyms'].append(
                            v.definition.split())

            if synset.hypernyms():
                results['words']['hypernyms'] = []
                for v in synset.hypernyms():
                    results['words']['hypernyms'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['hypernyms'].append(
                            v.definition.split())

            """
            Other types
            (need classification) TODO
            """

            if synset.topic_domains():
                results['words']['topic_domains'] = []
                for v in synset.topic_domains():
                    results['words']['topic_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['topic_domains'].append(
                            v.definition.split())

            if synset.region_domains():
                results['words']['region_domains'] = []
                for v in synset.region_domains():
                    results['words']['region_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['region_domains'].append(
                            v.definition.split())

            if synset.usage_domains():
                results['words']['usage_domains'] = []
                for v in synset.usage_domains():
                    results['words']['usage_domains'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['usage_domains'].append(
                            v.definition.split())

            if synset.attributes():
                results['words']['attributes'] = []
                for v in synset.attributes():
                    results['words']['attributes'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['attributes'].append(
                            v.definition.split())

            if synset.entailments():
                results['words']['entailments'] = []
                for v in synset.entailments():
                    results['words']['entailments'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['entailments'].append(
                            v.definition.split())

            if synset.causes():
                results['words']['causes'] = []
                for v in synset.causes():
                    results['words']['causes'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['causes'].append(
                            v.definition.split())

            if synset.also_sees():
                results['words']['also_sees'] = []
                for v in synset.also_sees():
                    results['words']['also_sees'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['also_sees'].append(
                            v.definition.split())

            if synset.verb_groups():
                results['words']['verb_groups'] = []
                for v in synset.verb_groups():
                    results['words']['verb_groups'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['verb_groups'].append(
                            v.definition.split())

            if synset.similar_tos():
                results['words']['similar_tos'] = []
                for v in synset.similar_tos():
                    results['words']['similar_tos'].append(v.lemma_names)
                    if use_definitions:
                        results['words']['similar_tos'].append(
                            v.definition.split())

    """
    1. get words back
    2. flatten nested array
    3. split up words
    4. filter, clean, stem, uniquify
    """

    for nlp_type in results['words']:
        results['words'][nlp_type] = sorted(
            normalization.uniquify(
                normalization.clean_sort(
                    normalization.remove_stop_words(
                        normalization.stem_words(
                            normalization.remove_bad_words(
                                list(itertools.chain(
                                    *results['words'][nlp_type]))))))))

    return results
