d = []
with open('dataset_3363_4.txt', 'r') as fr:
    line = fr.readline()
    while line:
#        print(line)
        #for FIO, s_math, s_fiz, s_rus in line.strip().split(';'):
        d.append(line.strip().split(';'))
        line = fr.readline()
print(d)
with open('dataset_3363_4_output.txt', 'w') as fw:
    sum_math, sum_fiz, sum_rus = 0, 0, 0
    for name, s_math, s_fiz, s_rus in d:
        s_math = int(s_math)
        s_rus = int(s_rus)
        s_fiz = int(s_fiz)
        #print((s_math + s_fiz + s_rus) / 3)
        fw.write(str((s_math + s_fiz + s_rus) / 3) + '\n')
        sum_fiz += s_fiz
        sum_math += s_math
        sum_rus += s_rus
    cnt = len(d)
    #print(sum_math/cnt, sum_fiz/cnt, sum_rus/cnt)
    fw.write(str(sum_math/cnt) + ' ' + str(sum_fiz/cnt) + ' ' + str(sum_rus/cnt))