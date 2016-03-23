"""All example generation for demos, etc..."""

from __future__ import absolute_import

from . import metrics
from . import nlp
from . import scoring
from . import techniques


def generate_all_examples(filename=None, words=None):
    """Generate examples using all functions available.

    Args:
        filename (str, optional): A file name.
        words (list, optional): A list of words.

    Returns:
        dict: All generated examples
    """
    return {
        'synset_categories': nlp.print_all_synset_categories(),
        'synsets': nlp.get_synsets(words, use_definitions=True),
        'metrics': metrics.generate_all_metrics(
            filename=filename,
            words=words),
        'techniques': techniques.generate_all_techniques(words),
        'scoring': scoring.generate_all_scoring(words)
    }
