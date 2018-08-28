n = int(input())
d = {}
for x in int(input()):
    if x not in d:
        d[x] = f(x)
    print(d[x])