"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: int

    def __init__(self, name, surname, group, average_score):
        self.name = name
        self.surname = surname
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        if not isinstance(other, int):
            raise TypeError("Операнд average_score должен иметь тип int")
        return(self.average_score == other.average_score)

    def __ne__(self, other):
            if not isinstance(other, int):
                raise TypeError("Операнд average_score должен иметь тип int")
            return (self.average_score != other.average_score)

    def __lt__(self, other):
            if not isinstance(other, int):
                raise TypeError("Операнд average_score должен иметь тип int")
            return (self.average_score < other.average_score)

    def __le__(self, other):
            if not isinstance(other, int):
                raise TypeError("Операнд average_score должен иметь тип int")
            return (self.average_score <= other.average_score)

    def __gt__(self, other):
            if not isinstance(other, int):
                raise TypeError("Операнд average_score должен иметь тип int")
            return (self.average_score > other.average_score)

    def __ge__(self, other):
            if not isinstance(other, int):
                raise TypeError("Операнд average_score должен иметь тип int")
            return (self.average_score >= other.average_score)

    def __str__(self):
        return (f"Name: {self.name}, Surname: {self.surname}, Group: {self.group}, Average_score: {self.average_score}")


a = Student("Anna", "Tretyakova", 3, 8)
b = Student("Elena", "Evlash", 3, 7)
c = Student("Timur", "Kudaynazarov", 4, 9)
d = Student("Olga", "Naduyalova", 4, 6)
e = Student("Irina", "Novik", 5, 3)

list_1 = [a, b, c, d, e]
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if(list_1[j].average_score < list_1[i].average_score):
            x = list_1[i]
            list_1[i] = list_1[j]
            list_1[j] = x

for i in list_1:
    print(i.__str__())


list_1 = [a, b, c, d, e]
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if(list_1[j].average_score > list_1[i].average_score):
            x = list_1[i]
            list_1[i] = list_1[j]
            list_1[j] = x

for i in list_1:
    print(i.__str__())


list_1 = [a, b, c, d, e]
list_2 = []
for i in range(len(list_1)):
        if list_1[i].average_score > 5:
            list_2.append(list_1[i])
for j in list_2:
    print(j.__str__())
