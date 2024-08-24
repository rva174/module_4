# Различие атрибутов класса и экземпляра
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(f'{args[0]}, {args[1]}')
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'"{self.name}" снесен, но он останется в истории')

gk1 = House("ЖК Горский", 10)
print(House.houses_history)
gk2 = House("ЖК Домик в деревне", 20)
print(House.houses_history)
gk3 = House("ЖК Матрёшки", 20)
print(House.houses_history)
del gk2
del gk3
print(House.houses_history)
