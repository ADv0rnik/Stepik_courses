'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc

Sample Output 2:
badc
dcba
'''

n = list(input())
m = list(input())
txt = input()
code = input()

d = dict(zip(n, m))

def transform_text(txt, dic):
    frm = ''.join([str(i) for i in dic.keys()])
    to = ''.join([str(i) for i in dic.values()])
    table =txt.maketrans(frm, to)
    return txt.translate(table)

def reverse_transform_text(txt1, dic1):
    frm = ''.join([str(i) for i in dic1.values()])
    to = ''.join([str(i) for i in dic1.keys()])
    table =txt1.maketrans(frm, to)
    return txt1.translate(table)
print(transform_text(txt,d))
print(reverse_transform_text(code,d))