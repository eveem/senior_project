import ast

for i in range(2, 41):
    file_name = str(i).zfill(4) + '.txt'
    f_output = open('./output/{}'.format(file_name))
    f_result = open('./result/{}'.format(file_name))

    for line in f_result:
        result_list = ast.literal_eval(line)
        break

    for line in f_output:
        ck = False
        x = open('./rank_result/' + file_name, 'w')
        for i, j in enumerate(result_list):
            if line == j:
                x.write(str(i) + '\n')
                ck = True
                break
        if ck == False:
            x.write('Not Found')
            x.write('\n')
            