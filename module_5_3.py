# Перегрузка операторов
class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.numbers_of_floors}'

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors = self.numbers_of_floors + value
            return self
        else:
            print('Ошибка: value не целое число')
    def __iadd__(self, value):
        if isinstance(self, House):
            self.numbers_of_floors += value
            return self
        else:
            print('Ошибка: self не указывает на объект типа House')
    def __radd__(other, House):
        if isinstance(value, int):
            other.numbers_of_floors += value
            return other
        else:
            print('Ошибка: other не указывает на объект типа House')




    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors
    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors
    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors
    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors
    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

gk1 = House('ЖК Горский', 10)
gk2 = House("ЖК Домик в деревне", 20)
print(gk1)
print(gk2)
print(gk1 == gk2)       #__eq__ (==)
gk1 = gk1 + 10
print(gk1)             #__add__
print(gk1 == gk2)       #__eq__ (==)
gk1 += 10
print(gk1)             #__iadd__
gk2 += 10
print(gk2)             #__radd__
print(gk1 > gk2)      #__gt__(>)
print(gk1 >= gk2)      #__ge__(>=)
print(gk1 < gk2)      #__lt__ (<)
print(gk1 <= gk2)     #__le__ (<=)
print(gk1 != gk2)      #__ne__ (!=)

