from __future__ import absolute_import
from __future__ import division

from random import choice
import re
import string
import nltk

from pattern.en import split
from pattern.en import pluralize
from pattern.vector import words
from pattern.vector import stem
from pattern.vector import PORTER

from . import settings as namebot_settings
from . import normalization


def reduplication_ablaut(words):
    """
    http://phrases.org.uk/meanings/reduplication.html
    A technique to combine words and altering the vowels
    e.g ch[i]t-ch[a]t, d[i]lly, d[a]lly
    """

    new_words = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        print '%s %s ' % (word, re.sub(r'a|e|i|o|u', choice(vowels), word))
    return new_words


def affix_words(the_arr, affixType):
    """
    Do some type of affixing technique,
    such as prefixing or suffixing.

    MASTER LIST:

    TODO FINISH *-fixes from article

    prefixes = ["ac","ad","af","ag","al","ap","as","at","an","ab","abs","acer","acid","acri","acu","aer","aero","ag","agi","ig","act","agri","agro","alb","albo","ali","allo","alter","alt","am","ami","amor","ambi","ambul","ana","ano","andr","andro","ang","anim","ann","annu","enni","ante","anti","apo","ap","aph","aqu","arch","aster","astr","auc","aug","aut","aud","audi","aur","aus","aug","auc","aut","auto","bar","be","belli","bene","bi","bine","bibl","bibli","biblio","bio","brev","cap","cas","ceiv","cept","capt","cid","cip","calor","capit","carn","cat","cata","cath","caus","caut","cause","cuse","cus","ceas","ced","cede","ceed","cess","cent","centr","centri","chrom","chron","cide","cis","cise","cit","civ","clam","claim","clin","clud","clus","co","cog","col","coll","con","com","cor","cogn","gnos","contr","contra","cord","cor","cardi","corp","cort","cosm","cour","cur","curr","curs","crat","cracy","cre","cresc","cret","crease","crea","cred","cru","crit","cur","curs","cura","cycl","cyclo","de","dec","deca","dign","dei","div","dem","demo","dent","dont","derm","di","dy","dia","dic","dict","dit","dis","dif","doc","doct","domin","don","dorm","dox","en","em","end","epi","equi","duc","duct","dura","dynam","dys","ec","eco","ecto","ev","et","ex","exter","extra","extro","fa","fess","fac","fact","fec","fect","fic","fas","fea","fall","fals","femto","fer","fic","feign","fain","fit","feat","fid","fide","feder","fig","fila","fili","fin","fix","flex","flect","flict","flu","fluc","fluv","flux","fuse","for","fore","forc","fort","form","fract","frag","frai","fuge","gam","gastro","gen","geo","germ","gest","giga","gin","gloss","glot","glu","glo","gor","grad","gress","gree","graph","gram","graf","grat","grav","greg","hale","heal","helio","hema","hemo","her","here","hes","hex","ses","sex","homo","hum","hydr","hydra","hydro","hyper","hypn","ignis","im","in","il","ir","infra","inter","intra","intro","jac","ject","join","junct","jug","just","juven","labor","lau","lav","lot","lut","lect","leg","lig","levi","lex","leag","leg","liber","lide","liter","loc","loco","log","logo","ology","loqu","luc","lum","lun","lus","lust","lude","macr","magn","main","mal","man","manu","mand","mania","mar","mari","mer","matri","medi","mega","mem","ment","meso","meta","meter","metr","micro","migra","mill","kilo","milli","min","mis","mit","miss","mob","mov","mot","mon","mono","mor","mort","morph","multi","nano","nasc","nat","gnant","nai","nat","nasc","neo","neur","nom","nym","nomen","nomin","non","nov","nox","noc","numer","ob","oc","of","op","oct","oligo","omni","onym","oper","ortho","over","pac","pair","pare","pan","para","pat","pass","path","pater","patr","path","pathy","ped","pod","pedo","pel","puls","pend","pens","pond","per","peri","phage","phan","phas","phen","fan","phant","fant","phe","phil","phon","phot","photo","pico","pict","plac","plais","pli","ply","plore","plu","plur","plus","pneuma","pod","poli","poly","pon","pos","pound","pop","port","post","pot","pre","pur","prin","prim","prime","pro","proto","psych","punct","pute","quat","quad","quip","quir","quis","quer","re","reg","recti","retro","ri","ridi","risi","rog","roga","rupt","sacr","sanc","secr","salv","salu","sanct","sat","satis","sci","scio","scope","scrib","se","sect","sec","sed","sess","sid","semi","sen","scen","sent","sens","sept","sequ","secu","sue","serv","sign","signi","simil","simul","sist","sta","stit","soci","sol","solus","solv","solu","solut","somn","soph","spec","spect","spi","spic","sper","sphere","spir","stand","stant","stab","stat","stan","sti","sta","st","stead","strain","strict","string","stige","stru","struct","stroy","stry","sub","suc","suf","sup","sur","sus","sume","sump","super","supra","syn","sym","tact","tang","tag","tig","ting","tain","ten","tent","tin","tect","teg","tele","tem","tempo","ten","tin","tain","tend","tent","tens","tera","term","terr","terra","test","the","theo","therm","thet","tire","tom","tor","tors","tort","tox","tract","tra","trai","treat","trans","tri","trib","turbo","typ","ultima","umber","un","uni","vac","vade","vale","vali","valu","veh","vect","ven","vent","ver","veri","verb","verv","vert","vers","vi","vic","vicis","vict","vinc","vid","vis","viv","vita","vivi","voc","voke","vol","volcan","volv","volt","vol","vor","with","zo"]
    suffixes = ["age","able","ible","acy","cy","ade","al","ial","ical","an","ance","ence","ancy","ency","ent","ant","ent","ient","ar","ary","ard","art","ate","ation","cade","drome","ed","en","ence","ency","ier","er","or","erg","ery","es","ies","ess","est","iest","fold","ful","fy","ia","ian","an","iatry","ic","ics","ice","ify","ile","ing","ion","ish","ism","ist","ite","ity","ty","ive","ative","itive","ize","less","ly","ment","ness","or","ory","ous","eous","ose","ious","ship","ster","ure","ward","wise","y"]
    """

    prefixes = ["ac","ad","af","ag","al","ap","as","at","an","ab","abs", "acu","aer","aero","ag","agi","ig","act","alb", "ali","allo","alt","am","ami","amor","ambi","ambul","ana","ano","andr","andro","ang","anim","ann","annu","enni","ante","anti","apo","ap","aph","aqu","arch","aster","astr","auc","aug","aut","aud","audi","aur","aus","aug","auc","aut","auto","bar","be","bene","bi","bine","bibl","bio","brev","cap","cas","ceiv","cept","capt","cid","cip","carn","cat","cata","cath","caus","caut","cause","cuse","cus","ceas","ced","cede","ceed","cess","cent","chron","cide","cis","cise","cit","civ","clam","claim","clin","clud","clus","co","cog","col","coll","con","com","cor","cogn","gnos","contr", "cord","cor","cardi","corp","cort","cosm","cour","cur","curr","curs","crat","cracy","cre","cret","crea","cred","cru","crit","cur","curs","cura","cycl","cyclo","de","dec","deca","dign","dei","div","dem","demo","dent","dont","derm","di","dy","dia","dic","dict","dit","dis","dif","doc","doct","domin","don","dorm","dox","en","em","end","epi","equi","duc","duct","dura","dynam","dys","ec","eco","ecto","ev","et","ex","exter","fa","fess","fac","fact","fec","fect","fic","fas","fea","fall","fals","femto","fer","fic","feign","fain","fit","feat","fid","fide","feder","fig","fila","fili","fin","fix","flex","flu","fluc","fluv","flux","fuse","for","fore","forc","fort","form","fract","frag","frai","fuge","gam","geo","germ","gest","giga","gin","gloss","glot","glu","glo","gor","grad","gress","gree","graph","gram","graf","grat","grav","greg","hale","heal","helio","hema","hemo","her","here","hes","hex","ses","hum","hydra","hydro","hyper","im","in","il","ir","jac","ject","join","junct","jug","just","lau","lav","lot","lut","lect","leg","lig","levi","lex","leag","leg","liber","lide","liter","loc","loco","log","logo","ology","loqu","luc","lum","lun","lus","lust","lude","macr","magn","main","mal","man","manu","mand","mania","mar","mari","mer","matri","medi","mega","mem","ment","meso","meta","meter","metr","micro","migra","mill","kilo","milli","min","mis","mit","miss","mob","mov","mot","mon","mono","mor","mort","morph","multi","nano","nasc","nat","gnant","nai","nat","nasc","neo","neur","nom","nym","nomen","nomin","non","nov","nox","noc","numer","ob","oc","of","op","oct","oligo","omni","onym","oper","over","pac","pair","pare","pan","para","pat","pass","path","pater","patr","path","pathy","ped","pod","pedo","pel","puls","pend","pens","pond","per","peri","phage","phan","phas","phen","fan","phant","fant","phe","phil","phon","phot","photo","pico","pict","plac","plais","pli","ply","plore","plu","plur","plus","pneuma","pod","poli","poly","pon","pos","pound","pop","port","post","pot","pre","pur","prin","prim","prime","pro","proto","psych","punct","pute","quat","quad","quip","quir","quis","quer","re","reg","recti","retro","ri","ridi","risi","rog","roga","rupt","sacr","sanc","secr","salv","salu","sanct","sat","satis","sci","scio","scope","scrib","se","sect","sec","sed","sess","sid","semi","sen","scen","sent","sens","sept","sequ","secu","sue","serv","sign","signi","simil","simul","sist","sta","stit","soci","sol","solus","solv","solu","solut","somn","soph","spec","spect","spi","spic","sper","sphere","spir","stand","stant","stab","stat","stan","sti","sta","st","stead","strain","strict","string","stige","stru","struct","stroy","stry","sub","suc","suf","sup","sur","sus","sume","sump","super","supra","syn","sym","tact","tang","tag","tig","ting","tain","ten","tent","tin","tect","teg","tele","tem","tempo","ten","tin","tain","tend","tent","tens","tera","term","terr","terra","test","the","theo","therm","thet","tire","tom","tor","tors","tort","tox","tract","tra","trai","treat","trans","tri","trib","turbo","typ","ultima","umber","un","uni","vac","vade","vale","vali","valu","veh","vect","ven","vent","ver","veri","verb","verv","vert","vers","vi","vic","vicis","vict","vinc","vid","vis","viv","vita","vivi","voc","voke","vol","volcan","volv","volt","vol","vor","with","zo"]
    suffixes = ["age","able","ible","acy","cy","ade","al","ial","ical","an","ance","ence","ancy","ency","ent","ant","ent","ient","ar","ary","ard","art","ate","ation","cade","drome","ed","en","ence","ency","ier","er","or","erg","ery","es","ies","ess","est","iest","fold","ful","fy","ia","ian","an","iatry","ic","ics","ice","ify","ile","ing","ion","ish","ism","ist","ite","ity","ty","ive","ative","itive","ize","less","ly","ment","ness","or","ory","ous","eous","ose","ious","ship","ster","ure","ward","wise","y"]

    new_arr = []
    if len(the_arr):

        if affixType is 'prefix':
            for v in the_arr:
                for v1 in prefixes:
                    if v1 is not None:
                        if re.search(r'^/a|e|i|o|u', v[0]) or re.search(r'^/a|e|i|o|u', v1[0]):
                            """
                            if there's a vowel at the end of
                            prefix but not at the beginning
                            of the word (or vice versa)
                            """
                            if re.search(r'a|e|i|o|u', v1[-1:]) or re.search(r'^a|e|i|o|u', v[:1]):
                                new_arr.append(v1+v)

        elif affixType is 'suffix':
            for v in the_arr:
                for suffix in suffixes:
                    if suffix is not None:
                        if re.search(r'^/a|e|i|o|u', v[0]) or re.search(r'^/a|e|i|o|u', suffix[0]):
                            if suffix is "ify":
                                if v[-1] is "e":
                                    if v[-2] is not "i":
                                        new_arr.append(v[:-2]+suffix)
                                    else:
                                        new_arr.append(v[:-1]+suffix)
                                new_arr.append(v+suffix)
                            else:
                                new_arr.append(v+suffix)

        elif affixType is 'duplifix':
            """
            makes duplification
            (e.g: teeny weeny, etc...)
            """
            alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            for v in the_arr:
                for letter in alphabet:
                    # check if the first letter is
                    # NOT the same as the second letter in reduplication
                    if v[0] is not letter:
                        # check if the first word is
                        # NOT the same as the second word. (or letter)
                        if v is not letter+v[1:]:
                            if re.match('[aeiou]', v[1]):
                                if re.match('[^aeiou]', letter):
                                    new_arr.append(v+' '+letter+v[1:])
                            elif re.match('[^aeiou]', v[1]):
                                if re.match('[aeiou]', letter):
                                    new_arr.append(v+' '+letter+v[1:])

        elif affixType is "infix":
            pass

        elif affixType is "disfix":
            pass

    return new_arr


def make_founder_product_name(founder1, founder2, product):
    """
    get the name of two people
    forming a company and combine it

    """
    return founder1[0].upper() + ' & ' + founder2[0].upper() + ' ' + product


def make_name_obscured(the_arr):
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


def make_name_abbreviation(the_arr):
    """
    this function will make some kind of
    interesting company acronym
    eg: BASF, AT&T, A&W
    """
    new_arr = []
    for word in the_arr:
        new_arr.append(
            word[:1].upper() +
            word[:2].upper() +
            word[:3].upper() +
            word[:4].upper())
    return new_arr


def make_vowel(the_arr, vowel_type, vowel_index):
    new_arr = []
    for i in the_arr:
        for j in the_arr:
            if i is not j and re.search(vowel_type, i) and re.search(vowel_type, j):
                # get the indexes and lengths to use in finding the ratio
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
                if round(pos_i/len_i) > round(pos_j/len_j):
                    p = i[0: pos_i+1]
                    p2 = j[pos_j: len(j)]
                    len_p = len(p)
                    if len(p)+len(p2) > 2:
                        if re.search(namebot_settings.regex['all_vowels'], p) or re.search(namebot_settings.regex['all_vowels'], p2):
                            if p[-1] is p2[0]:
                                new_arr.append(p[:-1]+p2)
                            else:
                                new_arr.append(p+p2)
    return new_arr


def make_portmanteau_default_vowel(the_arr):
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

    make_vowel(the_arr, vowel_a_re, "a")
    make_vowel(the_arr, vowel_e_re, "e")
    make_vowel(the_arr, vowel_i_re, "i")
    make_vowel(the_arr, vowel_o_re, "o")
    make_vowel(the_arr, vowel_u_re, "u")
    return new_arr


def make_portmanteau_split(the_arr):
    """
    nikon = [ni]pp[on] go[k]aku
    make words similar to nikon,
    which is comprised of Nippon + Gokaku.

    We get the first C+V in the first word,
    then last V+C in the first word,
    then all C in the second word.
    """
    new_arr = []
    for i in the_arr:
        for j in the_arr:
                if i is not j:
                    l1 = re.search(r'[^aeiou{1}]+[aeiou{1}]', i)
                    l2 = re.search(r'[aeiou{1}]+[^aeiou{1}]$', j)
                    if i is not None and l1 and l2:

                        # third letter used for
                        # consonant middle splits only
                        l3 = re.split(r'[aeiou{1}]', i)
                        l1 = l1.group(0)
                        l2 = l2.group(0)

                        # l3 = uniquify(l3)
                        if len(l3) is not 0:
                            if l3 is not None:
                                for v in l3:
                                    new_arr.append(l1 + v + l2)
                            else:
                                new_arr.append(l1 + "t" + l2)
                                new_arr.append(l1 + "s" + l2)
                                new_arr.append(l1 + "z" + l2)
                                new_arr.append(l1 + "x" + l2)

    return new_arr


def make_punctuator(words):
    """
    put some random punctation like
    hyphens etc in there, only around vowels
    (ala del.ic.ious and others)
    """
    new_arr = []
    for word in words:
        if re.match(r'[aeiou]', word) and len(word) > 4:
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
    for word in words:
        if re.search(r'[aeiou]', word[:-2]):
            new_arr.append(word[:-1])
    return new_arr


def make_misspelling(the_arr):
    """
    This is used as the primary "misspelling"
    technique, through a few different techniques
    that are all categorized as misspelling.

    Brute force all combinations,
    then use double metaphone to remove odd ones.
    ...find a better way to do this TODO

    """

    new_arr = []
    for i in the_arr:
        new_arr.append(i.replace('ics', 'ix'))
        new_arr.append(i.replace('ph', 'f'))
        new_arr.append(i.replace('kew', 'cue'))
        new_arr.append(i.replace('f', 'ph'))
        new_arr.append(i.replace('o','ough'))

        # # these seem to have
        # # sucked in practice
        new_arr.append(i.replace('o','off'))
        new_arr.append(i.replace('ow', 'o'))
        new_arr.append(i.replace('x','ecks'))

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


def make_word_metaphor(the_arr):
    # TODO ADDME
    """
    Make a metaphor based
    on some words...?
    """
    new_arr = []
    return new_arr


def make_phrase(the_arr):
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
                new_words.append('%s %s' % (noun, verb))
                new_words.append('%s %s' % (verb, noun))
    except KeyError:
        pass

    try:
        for noun in words['NNS']:
            for verb in words['VB']:
                new_words.append('%s %s' % (noun, verb))
                new_words.append('%s %s' % (verb, noun))
    except KeyError:
        pass

    try:
        for noun in words['NNS']:
            for verb in words['VBP']:
                new_words.append('%s %s' % (noun, verb))
                new_words.append('%s %s' % (verb, noun))
    except KeyError:
        pass

    try:
        for noun in words['NN']:
            for verb in words['VB']:
                new_words.append('%s %s' % (noun, verb))
                new_words.append('%s %s' % (verb, noun))
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
        'words': {},
    }

    data['words']['alliterations'] = make_name_alliteration(words)
    data['words']['portmanteau'] = make_portmanteau_default_vowel(words)
    data['words']['vowels'] = make_vowelify(words)

    data['words']['suffix'] = affix_words(words, 'suffix')
    data['words']['prefix'] = affix_words(words, 'prefix')
    data['words']['duplifix'] = affix_words(words, 'duplifix')
    data['words']['disfix'] = affix_words(words, 'disfix')
    data['words']['infix'] = affix_words(words, 'infix')

    data['words']['found_product_name'] = make_founder_product_name(
        'Lindsey', 'Chris', 'Widgets')
    data['words']['cc_to_vc_swap'] = make_cc_to_vc_swap(words)
    data['words']['name_obscured'] = make_name_obscured(words)
    data['words']['punctuator'] = make_punctuator(words)
    data['words']['name_abbreviation'] = make_name_abbreviation(words)
    data['words']['make_portmanteau_split'] = make_portmanteau_split(words)
    data['words']['make_name_from_latin_root'] = make_name_from_latin_root(words)
    data['words']['make_word_metaphor'] = make_word_metaphor(words)
    data['words']['make_phrase'] = make_phrase(words)
    data['words']['reduplication_ablaut'] = reduplication_ablaut(words)
    data['words']['misspelling'] = make_misspelling(words)
    data['words']['descriptors'] = make_descriptors(
        get_descriptors(words))

    return super_scrub(data)
