import pickle
from math import log10

with open('law_with_words.pickle', 'rb') as f:
    laws = pickle.load(f)

word_idf = {}

all_law_no = len(laws)

for law_dict in laws:
    for no_law in law_dict:
        words = law_dict[no_law]
    for word in words:
        if word in word_idf:
            word_idf[word] += 1
        else:
            word_idf[word] = 1

for word in word_idf:
    word_idf[word] = log10(all_law_no/word_idf[word])

print(word_idf)