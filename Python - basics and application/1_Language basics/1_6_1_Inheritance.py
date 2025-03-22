"""
1.6 Наследование классов
"""

d = {k[0]: (k[1] if len(k) > 1 else "object") for k in [input().split(' : ') for _ in range(int(input()))]}
i = int(input())
while i != 0:
    ancestor, child = input().split()
    if child in d and ancestor in d[child]:
        print("Yes")
    else:
        print("No")
    i -= 1
