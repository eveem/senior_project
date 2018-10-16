import pickle

with open('law_words_idf.pickle', 'rb') as f:
    laws_idf = pickle.load(f)

with open('law_words_tf.pickle', 'rb') as f:
    laws_tf = pickle.load(f)

laws_tfidf = []

for law_dict in laws_tf:
    for no_law in law_dict:
        temp = {}
        words = law_dict[no_law]
    for word in words:
        temp[word] = words[word] * laws_idf[word]
    temp_dict = {no_law: temp}
    laws_tfidf.append(temp_dict)

with open('law_words_tfidf.pickle', 'wb') as f:
    pickle.dump(laws_tfidf, f, pickle.HIGHEST_PROTOCOL)