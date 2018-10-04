import pickle
from math import log10

with open('law_with_words.pickle', 'rb') as f:
    laws = pickle.load(f)

words_idf = {}

all_law_no = len(laws)

for law_dict in laws:
    for no_law in law_dict:
        words = law_dict[no_law]
    for word in words:
        if word in words_idf:
            words_idf[word] += 1
        else:
            words_idf[word] = 1

for word in words_idf:
    words_idf[word] = log10(all_law_no/words_idf[word])

with open('law_words_idf.pickle', 'wb') as f:
    pickle.dump(words_idf, f, pickle.HIGHEST_PROTOCOL)