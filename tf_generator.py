import pickle

with open('law_with_words.pickle', 'rb') as f:
    laws = pickle.load(f)

with open('law_words_count.pickle', 'rb') as f:
    laws_f = pickle.load(f)

laws_len = {}
for law_dict in laws:
    for no_law in law_dict:
        words = law_dict[no_law]
    laws_len[no_law] = len(words)

tf_score = []

for law in laws_f:
    for no_law in law:
        temp_tf = {}
        for word in law[no_law]:
            temp_tf[word] = law[no_law][word]/laws_len[no_law]
        temp_dict = {no_law: temp_tf}
        tf_score.append(temp_dict)

with open('law_words_tf.pickle', 'wb') as f:
    pickle.dump(tf_score, f, pickle.HIGHEST_PROTOCOL)