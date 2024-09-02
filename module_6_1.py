#Съедобное, несъудобное
class Animal:
    alive = True        # живой,
    fed = False         # накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f"{self.name} съел {self.food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {self.food.name}")
            self.alive = False
class Plant:
    edible = False       # съедобность
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    def __init(self, foood):
        self.food = food

class Predator(Animal):
    def __init(self, food):
        self.food = food

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатика')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

