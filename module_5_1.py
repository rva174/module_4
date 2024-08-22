class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if (1 > new_floor > numbers_of_floor):
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

gk1 = House('ЖК Горский', 18)
gk2 = House("ЖК Домик в деревне", 2)
gk1.go_to(5)
#gk2.go_to(10)
print('"Такого этажа не существует"')