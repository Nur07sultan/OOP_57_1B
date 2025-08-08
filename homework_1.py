class Person:
    # инициализатор
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

# создаём объекты класса
person_1 = Person("Нурсултан", "05.11.2007", "программист", False)
person_2 = Person("Асем", "12.04.2000", "дизайнер", True)
person_3 = Person("Эрмек", "30.09.1995", "инженер", True)

# печатаем атрибуты каждого экземпляра
print(person_1.name, person_1.birth_date, person_1.occupation, person_1.higher_education)
print(person_2.name, person_2.birth_date, person_2.occupation, person_2.higher_education)
print(person_3.name, person_3.birth_date, person_3.occupation, person_3.higher_education)

