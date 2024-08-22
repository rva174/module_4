class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if (1 > new_floor > numbers_of_floors):
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

    def __str__(self):
        return f'Название: {self.name}, количество этажей:{self.numbers_of_floors}'

    def __len__(self):
        return self.numbers_of_floors

gk1 = House('ЖК Горский', 18)
gk2 = House("ЖК Домик в деревне", 2)

print(gk1)
print(gk2)
print(len(gk1))
print(len(gk2))



