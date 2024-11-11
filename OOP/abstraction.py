"""
Абстракция - принцип ООП, в котором создается абстрактный класс(класс - пустышка),в котором задаются названия аттрибутов и методов для того, чтобы мы могли их переопределить в дочерних классах. 
У нас есть названия но нет логики
"""

from abc import ABC, abstractmethod

class AbstractAnimal(ABC):

    @abstractmethod
    def speak(self):
        print('voice')

    @abstractmethod
    def func(self):
        ...

# obj_ = AbstractAnimal() #*TypeError: Can't instantiate abstract class AbstractAnimal with abstract method speak
"""
Создавать объект от абстрактного класса нельзя
"""

class Dog(AbstractAnimal):
    def speak(self):
        print('Woof')
    
    def func(self):
        print('dsadasdqwdq')

obj1 = Dog() 
obj1.speak()
"""
Абстракция нужна для правильности полиморфизма
@abstractmethod - декоратор, который требует переопределения метода в дочернем классе
"""
from math import pi

class AbstractShape(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass

class Square(AbstractShape):
    def __init__(self, length) -> None:
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2
    
    def fact(self):
        return f'Я фигура {self.name}'
    
class Circle(AbstractShape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

obj = Circle(5)
print(obj.area()) #* 78.53981633974483