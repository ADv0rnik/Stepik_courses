"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности,
затем сумму второй пятерки, и т. д. Но последовательность не дается вам сразу целиком.
С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента,
потом следующие шесть, потом следующие два и т. д. Реализуйте класс Buffer,
который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.
Одним из требований к классу является то, что он не должен хранить в себе больше элементов,
чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку,
для которой была выведена сумма.
"""


class Buffer:
    def __init__(self):
        self.limit = 5
        self.current_part = list()

    def add(self, *args):
        for arg in args:
            self.current_part.append(arg)
            if len(self.current_part) == self.limit:
                print(sum(self.current_part))
                self.current_part.clear()
        return self.current_part

    def get_current_part(self):
        print(self.current_part)


buffer = Buffer()
buffer.add(1, 2, 3)
buffer.get_current_part()
buffer.add(4, 5, 6)
buffer.get_current_part()
buffer.add(7, 8, 9, 10)
buffer.get_current_part()
buffer.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buffer.get_current_part()
