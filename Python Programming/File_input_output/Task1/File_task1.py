'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст. Запишите полученный текст в файл и прикрепите его, как ответ
на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''

num = list('0123456789')
i = 0
x = ''
final_string = ''

with open('in.txt') as inf:
    s = inf.readline().strip()
a = s[i]
i += 1

while i < len(s):
    while s[i] in num:
        x += s[i]
        i += 1
        if i > (len(s) - 1):
            break
    final_string += (a * int(x))
    x = ''
    if i > (len(s) - 1):
        break
    a = s[i]
    i += 1

with open('out.txt','w') as outf:
    outf.write(final_string)

