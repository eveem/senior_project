import deepcut
import pickle

# f = open('criminal_code.html', 'r')
f = open('cleaning_law_list.txt', 'r')

law_list = []
prev_line = []

for line in f:
    d = {}
    new_line = line.replace("'", '')
    new_line = new_line.replace("[", '')
    new_line = new_line.replace("]", '')
    new_line = new_line.replace(",", '')
    new_line = new_line.replace('\n', '')
    new_line = new_line.split(' ')
    text_inline = ''.join(new_line[2:])
    d[new_line[1]] = deepcut.tokenize(text_inline)
    print(d[new_line[1]])
    law_list.append(d)
    # print(new_line)
#     new_line = line.replace('<', '')
#     new_line = new_line.replace('>', '')
#     new_line = new_line.replace('/', '')
#     new_line = new_line.replace('p', '')
#     new_line = new_line.replace('b', '')
#     new_line = new_line.replace('r', '')
#     new_line = new_line.replace('\xa0', '')
#     new_line = new_line.replace('\n', '')
#     space_split = new_line.split(' ')
#     law_list.append(space_split)

# print(len(law_list))
# prev_law = law_list[0]
# fin_law = []

# for law in law_list[1:]:
#     if law[0] != 'มาตรา':
#         prev_law += law
#     else:
#         fin_law.append(prev_law)
#         prev_law = law

# fin_law = fin_law[1:]
# dict_format = []

# for law in fin_law:
#     all_words = []
#     for text in law[2:]:
#         all_words += deepcut.tokenize(text)
#     dict_format.append({law[1]: all_words})

with open('law_with_words.pickle', 'wb') as f:
    pickle.dump(law_list, f, pickle.HIGHEST_PROTOCOL)

print("Dump complete !!")