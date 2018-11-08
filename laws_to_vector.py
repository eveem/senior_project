import pickle

with open('law_words_idf.pickle', 'rb') as f:
    data = pickle.load(f)

new_data = sorted(data, key=lambda x: data[x])

new_dict = {}
word_list = []

for i in new_data:
    if data[i] > 1:
        new_dict[i] = data[i]
        word_list.append(i)

with open('law_words_tfidf.pickle', 'rb') as f:
    laws = pickle.load(f)

laws_vector = {}

for law_dict in laws:
    x = [0 for i in range(0, len(word_list))]
    for no_law in law_dict:
        words = law_dict[no_law]
    for word in words:
        if word in word_list:
            x[word_list.index(word)] = words[word]
    laws_vector[no_law] = x

for i in laws_vector:
    print(i, len(laws_vector[i]))
    break

print(len(word_list))

with open('law_vector.pickle', 'wb') as f:
    pickle.dump(laws_vector, f, pickle.HIGHEST_PROTOCOL)

with open('words_list.pickle', 'wb') as f:
    pickle.dump(word_list, f, pickle.HIGHEST_PROTOCOL)
