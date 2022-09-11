"""
Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).
"""


def function(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return function(n-1, k) + function(n-1, k-1)


a, b = map(int, input().split())
print(function(a, b))
