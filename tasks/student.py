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
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __ne__(self, other):
        return self.average_score != other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other

    def __repr__(self):
        return "{} {} {} {}".format(self.surname, self.name, self.group, self.average_score)


stud_1 = Student("Хопкинс", "Энтони", 12, 8.3)
stud_2 = Student("Фостер", "Джоди", 10, 6.9)
stud_3 = Student("Пачино", "Аль", 11, 8.2)
stud_4 = Student("Томпсон", "Эмма", 9, 7.6)
stud_5 = Student("Хэнкс", "Том", 7, 9.1)

student_list = [stud_1, stud_2, stud_3, stud_4, stud_5]

print(sorted(student_list))

print(sorted(student_list, reverse=True))

for i in student_list:
    if i.average_score > 5:
        print(i)
