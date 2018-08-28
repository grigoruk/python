d = {}
for i in input().split():
    i = i.lower()
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k, v in d.items():
    print(k, v)