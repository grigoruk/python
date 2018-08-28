
import requests
url = 'https://stepik.org/media/attachments/course67/3.6.3/'
file = input()
with open(file, 'r') as fr:
    txt = fr.readline().strip()

while 'We' not in txt:
    if ('' not in txt):
        txt = url + txt
    f_get = requests.get(txt)
    print('url', f_get.url)
    if (f_get.status_code == 404):
        print('Not found 404')
        break
    txt = f_get.text.strip()

print(txt)