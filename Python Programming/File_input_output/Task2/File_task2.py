"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
"""

d = {}
inf = open('in1.txt', 'r')
lst = inf.read().lower().split()
inf.close()
for word in lst:
    if word not in d:
        d[word] = 1
    elif word in d:
        d[word] += 1
maximum = 0
for key, value in d.items():
    k = d.get(key)
    if k > maximum:
        maximum = k
with open('out1.txt', 'w') as outf:
    most_popular = max(d, key = d.get) + ' ' + str(maximum)
    outf.write(most_popular)

