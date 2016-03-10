"""Settings and configuration for namebot modules."""

import re

MAX_LENGTH = 13
MIN_LENGTH = 4
SPACED_MAX_LENGTH = 22
VOWELS = list('aeiou')
CONSONANTS = list('qwrtypsdfghjklzxcvbnm')
# Two-letter vowel+consonant prefixes
VC_TL_PREFIXES = ['ac', 'ad', 'af', 'ag', 'al', 'ap', 'as', 'at', 'an', 'ab',
                  'ag', 'ig', 'am', 'ap', 'be', 'bi', 'co', 'de', 'di', 'dy',
                  'en', 'em', 'ec', 'ev', 'et', 'ex', 'fa', 'im', 'in', 'il',
                  'ir', 'ob', 'oc', 'of', 'op', 're', 'ri', 'se', 'st', 'un',
                  'vi', 'zo']
# Greather than two-letter vowel+consonant prefixes.
VC_GT_TL_PREFIXES = ['abs', 'acer', 'acid', 'acri', 'acu', 'aer', 'aero', 'agi', 'act', 'agri', 'agro', 'alb', 'albo', 'ali', 'allo', 'alter', 'alt', 'ami', 'amor', 'ambi', 'ambul', 'ana', 'ano', 'andr', 'andro', 'ang', 'anim', 'ann', 'annu', 'enni', 'ante', 'anti', 'apo', 'aph', 'aqu', 'arch', 'aster', 'astr', 'auc', 'aug', 'aut', 'aud', 'audi', 'aur', 'aus', 'aug', 'auc', 'aut', 'auto', 'bar', 'belli', 'bene', 'bine', 'bibl', 'bibli', 'biblio', 'bio', 'brev', 'cap', 'cas', 'ceiv', 'cept', 'capt', 'cid', 'cip', 'calor', 'capit', 'carn', 'cat', 'cata', 'cath', 'caus', 'caut', 'cause', 'cuse', 'cus', 'ceas', 'ced', 'cede', 'ceed', 'cess', 'cent', 'centr', 'centri', 'chrom', 'chron', 'cide', 'cis', 'cise', 'cit', 'civ', 'clam', 'claim', 'clin', 'clud', 'clus', 'cog', 'col', 'coll', 'con', 'com', 'cor', 'cogn', 'gnos', 'contr', 'contra', 'cord', 'cor', 'cardi', 'corp', 'cort', 'cosm', 'cour', 'cur', 'curr', 'curs', 'crat', 'cracy', 'cre', 'cresc', 'cret', 'crease', 'crea', 'cred', 'cru', 'crit', 'cur', 'curs', 'cura', 'cycl', 'cyclo', 'dec', 'deca', 'dign', 'dei', 'div', 'dem', 'demo', 'dent', 'dont', 'derm', 'dia', 'dic', 'dict', 'dit', 'dis', 'dif', 'doc', 'doct', 'domin', 'don', 'dorm', 'dox', 'end', 'epi', 'equi', 'duc', 'duct', 'dura', 'dynam', 'dys', 'eco', 'ecto', 'exter', 'extra', 'extro', 'fess', 'fac', 'fact', 'fec', 'fect', 'fic', 'fas', 'fea', 'fall', 'fals', 'femto', 'fer', 'fic', 'feign', 'fain', 'fit', 'feat', 'fid', 'fide', 'feder', 'fig', 'fila', 'fili', 'fin', 'fix', 'flex', 'flect', 'flict', 'flu', 'fluc', 'fluv', 'flux', 'fuse', 'for', 'fore', 'forc', 'fort', 'form', 'fract', 'frag', 'frai', 'fuge', 'gam', 'gastro', 'gen', 'geo', 'germ', 'gest', 'giga', 'gin', 'gloss', 'glot', 'glu', 'glo', 'gor', 'grad', 'gress', 'gree', 'graph', 'gram', 'graf', 'grat', 'grav', 'greg', 'hale', 'heal', 'helio', 'hema', 'hemo', 'her', 'here', 'hes', 'hex', 'ses', 'sex', 'homo', 'hum', 'hydr', 'hydra', 'hydro', 'hyper', 'hypn', 'ignis', 'infra', 'inter', 'intra', 'intro', 'jac', 'ject', 'join', 'junct', 'jug', 'just', 'juven', 'labor', 'lau', 'lav', 'lot', 'lut', 'lect', 'leg', 'lig', 'levi', 'lex', 'leag', 'leg', 'liber', 'lide', 'liter', 'loc', 'loco', 'log', 'logo', 'ology', 'loqu', 'luc', 'lum', 'lun', 'lus', 'lust', 'lude', 'macr', 'magn', 'main', 'mal', 'man', 'manu', 'mand', 'mania', 'mar', 'mari', 'mer', 'matri', 'medi', 'mega', 'mem', 'ment', 'meso', 'meta', 'meter', 'metr', 'micro', 'migra', 'mill', 'kilo', 'milli', 'min', 'mis', 'mit', 'miss', 'mob', 'mov', 'mot', 'mon', 'mono', 'mor', 'mort', 'morph', 'multi', 'nano', 'nasc', 'nat', 'gnant', 'nai', 'nat', 'nasc', 'neo', 'neur', 'nom', 'nym', 'nomen', 'nomin', 'non', 'nov', 'nox', 'noc', 'numer', 'oct', 'oligo', 'omni', 'onym', 'oper', 'ortho', 'over', 'pac', 'pair', 'pare', 'pan', 'para', 'pat', 'pass', 'path', 'pater', 'patr', 'path', 'pathy', 'ped', 'pod', 'pedo', 'pel', 'puls', 'pend', 'pens', 'pond', 'per', 'peri', 'phage', 'phan', 'phas', 'phen', 'fan', 'phant', 'fant', 'phe', 'phil', 'phon', 'phot', 'photo', 'pico', 'pict', 'plac', 'plais', 'pli', 'ply', 'plore', 'plu', 'plur', 'plus', 'pneuma', 'pod', 'poli', 'poly', 'pon', 'pos', 'pound', 'pop', 'port', 'post', 'pot', 'pre', 'pur', 'prin', 'prim', 'prime', 'pro', 'proto', 'psych', 'punct', 'pute', 'quat', 'quad', 'quip', 'quir', 'quis', 'quer', 'reg', 'recti', 'retro', 'ridi', 'risi', 'rog', 'roga', 'rupt', 'sacr', 'sanc', 'secr', 'salv', 'salu', 'sanct', 'sat', 'satis', 'sci', 'scio', 'scope', 'scrib', 'sect', 'sec', 'sed', 'sess', 'sid', 'semi', 'sen', 'scen', 'sent', 'sens', 'sept', 'sequ', 'secu', 'sue', 'serv', 'sign', 'signi', 'simil', 'simul', 'sist', 'sta', 'stit', 'soci', 'sol', 'solus', 'solv', 'solu', 'solut', 'somn', 'soph', 'spec', 'spect', 'spi', 'spic', 'sper', 'sphere', 'spir', 'stand', 'stant', 'stab', 'stat', 'stan', 'sti', 'sta', 'stead', 'strain', 'strict', 'string', 'stige', 'stru', 'struct', 'stroy', 'stry', 'sub', 'suc', 'suf', 'sup', 'sur', 'sus', 'sume', 'sump', 'super', 'supra', 'syn', 'sym', 'tact', 'tang', 'tag', 'tig', 'ting', 'tain', 'ten', 'tent', 'tin', 'tect', 'teg', 'tele', 'tem', 'tempo', 'ten', 'tin', 'tain', 'tend', 'tent', 'tens', 'tera', 'term', 'terr', 'terra', 'test', 'the', 'theo', 'therm', 'thet', 'tire', 'tom', 'tor', 'tors', 'tort', 'tox', 'tract', 'tra', 'trai', 'treat', 'trans', 'tri', 'trib', 'turbo', 'typ', 'ultima', 'umber', 'uni', 'vac', 'vade', 'vale', 'vali', 'valu', 'veh', 'vect', 'ven', 'vent', 'ver', 'veri', 'verb', 'verv', 'vert', 'vers', 'vic', 'vicis', 'vict', 'vinc', 'vid', 'vis', 'viv', 'vita', 'vivi', 'voc', 'voke', 'vol', 'volcan', 'volv', 'volt', 'vol', 'vor', 'with']
PREFIXES = VC_TL_PREFIXES + VC_GT_TL_PREFIXES
# Consonant+vowel pairs (e.g. ma me mi mo mu, ...)
CV_TL_PAIRS = ['{}{}'.format(c, v) for c in CONSONANTS for v in VOWELS]
SUFFIXES = ['age', 'able', 'ible', 'acy', 'cy', 'ade', 'al', 'ial', 'ical',
            'an', 'ance', 'ence', 'ancy', 'ency', 'ent', 'ant', 'ent', 'ient',
            'ar', 'ary', 'ard', 'art', 'ate', 'ation', 'cade', 'drome', 'ed',
            'en', 'ence', 'ency', 'ier', 'er', 'or', 'erg', 'ery', 'es', 'ies',
            'ess', 'est', 'iest', 'fold', 'ful', 'fy', 'ia', 'ian', 'an',
            'iatry', 'ic', 'ics', 'ice', 'ify', 'ile', 'ing', 'ion', 'ish',
            'ism', 'ist', 'ite', 'ity', 'ty', 'ive', 'ative', 'itive', 'ize',
            'less', 'ly', 'ment', 'ness', 'or', 'ory', 'ous', 'eous', 'ose',
            'ious', 'ship', 'ster', 'ure', 'ward', 'wise', 'y']
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
regexes = {
    'no_vowels': re.compile(r'^/a|e|i|o|u', re.IGNORECASE),
    'all_vowels': re.compile(r'a|e|i|o|u', re.IGNORECASE),
    'vowels': re.compile(r'[a-zA-Z][a|e|i|o|u]', re.IGNORECASE),
    'consonants': re.compile(r'[a-zA-Z][^a|e|i|o|u]', re.IGNORECASE),
}
