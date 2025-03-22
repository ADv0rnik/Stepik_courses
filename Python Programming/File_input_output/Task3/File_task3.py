"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
значения, разделённые пробелом, последней строкой в файл с ответом.

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""
import statistics

mean_lst = []
math_mark = []
phys_mark = []
rus_mark = []
count = 0

with open('in3.txt', 'r', encoding='utf-8') as inf:
    for line in inf.readlines():
        line = line.split(';')
        line.remove(line[0])
        for i, n in enumerate(line):
           line[i] = int(n)
        mean_lst.append(sum(line)/len(line))
        math_mark.append(line[0])
        phys_mark.append(line[1])
        rus_mark.append(line[2])
        count += 1
with open('out3.txt', 'w') as out_file:
    for i in mean_lst:
        out_file.write(str(i) + '\n')
    final_str = str(statistics.mean(map(float, math_mark))) + ' ' \
                + str(statistics.mean(map(float, phys_mark))) + ' ' \
                + str(statistics.mean(map(float, rus_mark)))
    out_file.write(final_str)