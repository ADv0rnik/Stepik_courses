"""
Реализуйте структуру данных, представляющую собой расширенную структуру стек.
"""

class ExtendedStack(list):
    def sum(self):
       self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())

def test(lst: ExtendedStack):
    lst.sum()
    assert lst.pop() == 11

l = ExtendedStack([1, 2, 3, 4, 5, 6])
test(l)
