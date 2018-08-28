def update_dictionary(d, key, value):
    double_key = 2 * key
    if key in d:
        d[key] += [value]
    elif double_key in d:
        d[double_key] += [value]
    else:
        d[double_key] = [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  # {2: [-1, -2, -3]}