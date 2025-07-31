import re
from collections import Counter

def is_pangram(sentence):
    
    return len(dict(Counter(re.findall("[a-z]", sentence.casefold())))) == 26
