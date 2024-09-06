class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str, __model:str, __color:str, __horsepower:int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__horsepower = __horsepower

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__horsepower}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.__color}\nВладелец: {self.owner}\n')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {self.new_color}\n')

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5



 # Изначальные свойства
#__COLOR_VARIANTS = ['yellow', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle1.print_info()

