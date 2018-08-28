import requests
file = input()
with open(file, 'r') as fr:
    f_name_to_get = fr.readline().strip()

f_get = requests.get(f_name_to_get)
cnt = 0
print(f_get.text)
with open (f_get, 'r') as fr:
    while fr.readline():
        cnt += 1
print(cnt)