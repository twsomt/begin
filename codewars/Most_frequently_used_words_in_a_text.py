import re
from collections import Counter

def top_3_words(text):
    words = re.findall("[a-z']+", text.lower())
    return [el[0] for el in Counter(words).most_common(3) if re.search('[a-z]', el[0])]

print(top_3_words('a a a  b  c c  d d d d  e e e e e'))  # ["e", "d", "a"]
print(top_3_words('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e'))  # ["e", "ddd", "aa"]
print(top_3_words("  //wont won't won't "))  # "won't", "wont"



