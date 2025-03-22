'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''

import requests

url_pattern = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('in.txt') as input:
    url = input.read().strip()
while True:
    t = requests.get(url)
    if 'We' in str(t.text.strip()):
        break
    url = url_pattern + str(t.text.strip())
    #print(url)

print('Checking complete!')
with open('out.txt', 'w') as output:
    output.write(t.text.strip())
