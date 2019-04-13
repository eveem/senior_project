from wordcut import Wordcut
import pickle

file = open('./final_process/text_no_space.pickle','rb')
object_file = pickle.load(file)
file.close()

with open('./final_process/dict.txt', encoding='UTF-8') as dict_file:
    word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
    wordcut = Wordcut(word_list)

freq_words = {}

for text in object_file:
    words = wordcut.tokenize(text)
    for word in words:
        if len(word) > 1:
            if word in freq_words:
                freq_words[word] += 1
            else:
                freq_words[word] = 1

print(len(freq_words))
