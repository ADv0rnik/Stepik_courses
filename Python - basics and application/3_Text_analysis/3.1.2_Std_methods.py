"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
"""

def count_occurrences(seq, sub):
    count = 0
    start_ind = 0
    end_ind = len(sub)

    if sub not in seq:
        return count

    for i in range(len(seq)):
        if seq[start_ind:end_ind] == sub:
            count += 1
            start_ind += 1
            end_ind += 1
        else:
            start_ind += 1
            end_ind += 1
    return count


s, t = input(), input()
print(count_occurrences(s, t))
