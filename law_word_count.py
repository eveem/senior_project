import pickle

with open('law_with_words.pickle', 'rb') as f:
    data = pickle.load(f)

n = []

for law_dict in data:
    for law_no in law_dict:
        new = {}
        for word in law_dict[law_no]:
            if word in new:
                new[word] += 1
            else:
                new[word] = 1
        new_d = {law_no: new}
        n.append(new_d)

with open('law_words_count.pickle', 'wb') as f:
    pickle.dump(n, f, pickle.HIGHEST_PROTOCOL)

print("Dump complete !!")