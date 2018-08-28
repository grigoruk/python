with open('dataset_3363_2.txt', 'r') as fr:
    s = fr.readline().strip()
new_s = ''
numbers = '1234567890'
i = 0
while i < len(s):
    cnt = ''
    correction = 1
    while (i + correction < len(s)) and (s[i + correction] in numbers):
        cnt += s[i + correction]
        correction += 1

    new_s += s[i] * int(cnt)
    i = i + correction

with open('dataset_3363_2_output.txt', 'w') as fw:
    fw.write(new_s)