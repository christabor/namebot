from __future__ import division
import re
from pattern.en import parse
from pattern.web import sort, Bing

#from nltk.book import * # only for testing a book
# good use: lwords = [w for w in v if len(w) > 15]
# add w _as_ w (the key), in the obj, if some condition is met


"""
    Conventions used in this utility:
    1.  All functions return a dictionary,
        with key 'data' and/or 'summary':
        return {
            'data': data,
            'summary': summary or None
        }

"""


class NameBotMetricUtilities:
    def __init__(self):
        self.data = []
        self.word_length = 0

    def open_file(self, file_name):
        self.file_name = file_name
        items = []
        with open(file_name) as files:
            for newline in files:
                items.append(newline)
        self.total_words = len(items)
        return items

    def get_named_numbers(self, name_list):
        """
        Check for numbers spelled out
        e.g. One, Two, Three, Four
        """
        self.name_list = name_list
        matches = []
        numbers = re.compile(
            r'\AOne |Two |Three |Four |Five |Six |Seven |Eight |Nine |Ten ')
        for word in name_list:
            if re.findall(numbers, word):
                matches.append(word)

        summary = 'Of %s words %s matched' % (
            self.total_words, len(matches))
        return {
            'data': matches,
            'summary': summary
        }

    def name_length(self, name_list):
        self.name_list = name_list
        names_length = []
        for val in name_list:
            names_length.append(len(val))
        summary = (
            "Of %s words, the average length of company names is... %s " %
            (self.total_words, round(sum(names_length) / len(names_length))))
        return {
            'data': names_length,
            'summary': summary
        }

    def name_vowel_count(self, name_list):
        self.name_list = name_list
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

    def name_starts_with_vowel(self, name_list):
        self.name_list = name_list
        vowelcount = 0

        for name in name_list:
            if re.match(
                r'\A[aeiou]',
                name,
                    flags=re.IGNORECASE):
                        vowelcount += 1

        summary = 'Of %s words, %s or %s%s are vowels as the first letter.' % (
            len(name_list), vowelcount, len(name_list) % vowelcount, '%')
        return {
            'data': None,
            'summary': summary
        }

    def get_search_results(self, name_list):
        # TODO FIXME
        # values = []
        # self.name_list = name_list
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

        # summary = 'VAL: %s SEARCHES: %s %s' % (
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

    def get_digits_frequency(self, name_list):
        """
        Look for and count the
        digits in names, e.g. 7-11, 3M, etc...
        """
        self.name_list = name_list
        new_arr = []
        for name in name_list:
            if re.findall(r'[0-9]+', name):
                # content = str((name, len(name)))
                # new_arr.append(content)
                matches = re.findall(r'[0-9]+', name)
                new_arr.append(matches)
        return {
            'data': new_arr,
            'summary': None
        }

    def get_first_letter_frequency(self, name_list):
        """
        Add the frequency of first letters
        e.g. [C]at, [C]law, c = 2
        """
        self.name_list = name_list
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

    def get_special_chars(self, name_list):
        self.name_list = name_list
        new_arr = []
        charcount = 0
        for val in name_list:
            if re.findall(
                r'\&|\!|\@|\.',
                val,
                    flags=re.IGNORECASE):
                        charcount += 1

        summary = (
            'Special character for names: %s Special characters in list: %s' % (
                charcount,
                new_arr))
        return {
            'data': new_arr,
            'summary': summary
        }

    def get_word_types(self, name_list):
        self.name_list = name_list
        new_arr = []
        for val in name_list:
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
        return {
            'data': new_arr,
            'summary': None
        }

    def get_name_spaces(self, name_list):
        self.name_list = name_list
        num_arr = []
        for val in name_list:
            if re.match(r'', val):
                splits = val.split()
                num_arr.append(len(splits))
        return {
            'data': num_arr,
            'summary': None
        }

    def get_consonant_repeat_frequency(self, name_list):
        self.name_list = name_list
        count = 0
        for val in name_list:
            if re.match(r'[^aeiou]{6}', val):
                count += 1
        return {
            'data': count,
            'summary': None
        }

    def get_consonant_duplicate_repeat_frequency(self, name_list):
        self.name_list = name_list
        count = 0
        for name in name_list:
            if re.match(r'[^a]{3}[^e]{3}[^i]{3}[^o]{3}[^u]{3}', name):
                count += 1
        return {
            'data': count,
            'summary': None
        }

    def get_vowel_repeat_frequency(self, name_list):
        self.name_list = name_list
        count = 0
        for val in name_list:
            if re.match(r'[aeiou]{3}', val):
                count += 1
        return {
            'data': count,
            'summary': None
        }

    def get_adjective_verb_or_noun(self, name_list):
        self.name_list = name_list
        # TODO ADD
        return {
            'data': None,
            'summary': None
        }

    def get_keyword_relevancy_map(self, name_list, n_list, terms, sortcontext,
                                  enginetype='BING',
                                  license=None):
        """
        http://www.clips.ua.ac.be/pages/pattern-web#sort
        """
        results_list = []
        self.name_list = name_list
        results = sort(
            terms=[],
            context=sortcontext,  # Term used for sorting.
            service=enginetype,   # GOOGLE, YAHOO, BING, ...
            license=None,         # You should supply your own API license key
                                  # for the given service.
            strict=True,          # Wraps the query in quotes, i.e.'mac sweet'.
            reverse=True,         # Reverses term and context: 'sweet mac' <=>
                                  # 'mac sweet'.
            cached=True)

        for weight, term in results:
            results.append("%5.2f" % (weight * 100) + "%", term)

        return {
            'data': results_list,
            'summary': None
        }

    def check_trademark_registration(self, name_list):
        """
        search the USTM office and return
        the number of results, and
        what they are (if applicable)
        """
        self.name_list = name_list
        return {
            'data': None,
            'summary': None
        }

    def check_domain_searches(self, name_list):
        """
        check domains for each name...
        perhap hook into other domain
        name generators, sites..?
        """
        self.name_list = name_list
        return {
            'data': None,
            'summary': None
        }

    def get_search_result_count(self, name_list):
        """
        check google results and return
        a number of results (number)

        http://www.clips.ua.ac.be/pages/pattern-web#DOM
        """
        self.name_list = name_list
        return {
            'data': None,
            'summary': None
        }

    def get_word_ranking(self, name_list):
        """
        use google results and get a quality of
        ranking based on other metrics such as
        domain name availability,
        google results and others.
        """
        results = []
        self.name_list = name_list
        for name in name_list:
            results = self.get_search_result_count(name_list)
            domains = self.check_domain_searches(name_list)
            results.append(results / domains)
        return
        return {
            'data': results,
            'summary': None
        }
