import deepcut
import pickle

file_path = '../text_legal_for_project/input/'

for i in range(2, 41):
# for i in range(2, 3):
    file_name = str(i).zfill(4) + '.txt'
    f = open(file_path + file_name, 'r')
    text = ''
    for line in f:
        text += line
    words = deepcut.tokenize(text)
    f.close()

    len_doc = len(words)

    with open('words_list.pickle', 'rb') as f:
        words_list = pickle.load(f)

    vector_text = [0 for i in range(0, len(words_list))]

    for word in words:
        if word in words_list:
            vector_text[words_list.index(word)] += 1
        
    for i in range(0, len(words_list)):
        vector_text[i] /= len_doc

    with open('law_vector.pickle', 'rb') as f:
        law_vector = pickle.load(f)

    sim = {}

    for no_law in law_vector:
        p = 0
        summ = 0
        for vc in law_vector[no_law]:
            summ += vc * vector_text[p]
            p += 1
        sim[no_law] = summ

    sim_sort = sorted(sim, key=lambda x: sim[x])

    x = open('./result/' + file_name, 'w+')
    x.write(str(sim_sort))
    x.close()
    print(sim_sort[-10:])

# text = "สอบสวน นางสาวบุญลอม  ปัดโรคา    ผู้กล่าวหา ให้การว่า ตามวันเวลาที่เกิดเหตุ ได้เลี้ยงหลานอยู่ที่บ้านพัก ต่อมาได้มีนายสุรชัย จินตนาการ สามีผู้เสียหายมาพูดว่า  ผู้ต้องหาได้พูดที่ตลาดว่า ผู้เสียหาย ไปให้เขาเย็ดทั่วบ้านทั่วเมืองซึ่งผู้เสียหายได้ยินแล้วเกิดความเสียหาย เสียชื่อเสียง จึงได้เดินทางมาแจ้งความร้องทุกข์ให้ดำเนินคดีกับผู้ต้องหาฐานหมิ่นประมาท"

# words = deepcut.tokenize(text)

# len_doc = len(words)

# with open('words_list.pickle', 'rb') as f:
#     words_list = pickle.load(f)

# vector_text = [0 for i in range(0, len(words_list))]

# for word in words:
#     if word in words_list:
#         vector_text[words_list.index(word)] += 1
    
# for i in range(0, len(words_list)):
#     vector_text[i] /= len_doc

# with open('law_vector.pickle', 'rb') as f:
#     law_vector = pickle.load(f)

# sim = {}

# for no_law in law_vector:
#     p = 0
#     summ = 0
#     for vc in law_vector[no_law]:
#         summ += vc * vector_text[p]
#         p += 1
#     sim[no_law] = summ

# sim_sort = sorted(sim, key=lambda x: sim[x])

# print(sim_sort[-10:])