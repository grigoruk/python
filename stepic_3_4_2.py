d = {}
with open('dataset_3363_3.txt', 'r') as fr:
    line = fr.readline()
    while line:
        print(line)
        for i in line.strip().lower().split():
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        line = fr.readline()
print(d)
s = ''
cnt = 0
for k,v in d.items():
    if (v > cnt):
        s = k
        cnt = v
    elif (v == cnt) and ((k < s) or ( s == '')):
        s = k
        cnt = v
print(s, cnt)