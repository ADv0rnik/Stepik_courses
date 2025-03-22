'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти
слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''
import random

n = int(input())
lst = [input().lower() for i in range(n)]
m = int(input())
lst1 = [input().lower() for k in range(m)]
errors = []

for q in lst1:
    temp = q.split()
    _ = [errors.append(x) for x in temp if x not in lst and x not in errors]
random.shuffle(errors)
print('\n'.join(errors))