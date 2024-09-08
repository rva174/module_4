#6.3 Мифическое наследование
class Horse:
    def __init__(self, x_distance=0, sound="Frrr"):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.dx:int = dx
        self.x_distance = self.x_distance + dx
        return int(self.x_distance)

class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.dy = dy
        self.y_distance = self.y_distance + dy
        return int(self.y_distance)

class Pegausus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        Pegausus = []

        return (self.x_distance, self.y_distance)

    def voise(self):
        print(self.sound)


p1 = Pegausus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voise()





