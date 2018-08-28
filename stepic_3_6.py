import requests
file = input()
with open(file, 'r') as fr:
    f_name_to_get = fr.readline().strip()

f_get = requests.get(f_name_to_get)
cnt = len(f_get.text.splitlines())
print(cnt)
