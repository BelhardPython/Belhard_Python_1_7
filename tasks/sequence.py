"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""


import random


class RandSequence:
    n: int
    sequence = []

    def __init__(self, n):
        self.n = n
        sequen = [random_element for element in range(n) for random_element in [random.randint(-n, n)]]
        self.sequence = sequen

    def generate(self, n=None):
        if n is None:
            n = self.n
            sequen = [random_element for element in range(n) for random_element in [random.randint(-n, n)]]
            self.sequence = sequen

    def print_seq(self):
        for element in self.sequence:
            print(element)
        return
