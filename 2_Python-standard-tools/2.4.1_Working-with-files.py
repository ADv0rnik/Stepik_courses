"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке

"""
lines = []
with open('dataset_24465_4 (1).txt', 'r') as file:
    for i in file.readlines():
         lines.append(i.strip("\n"))

lines.reverse()

with open('text_1.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line + "\n")