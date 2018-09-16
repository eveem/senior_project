import pickle

with open('law_with_words.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)