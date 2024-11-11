"""
Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная

"Один интерфейс - много реализаций"
"""

class Dog:
    def speak(self):
        print('Woof-woof')

class Cat:
    def speak(self):
        print('Meow-meow')

class Frog:
    def speak(self):
        print('Kwa-Kwa')

objects = [Frog(), Cat(), Dog()]

for obj in objects:
    obj.speak()

#* __add__ (+) - Метод полиморф
# print(5 + 5)
# print('hello' + 'hello')
# print('5' + '5')
# print([1,2,3,4] + [5,6,7])
# a = [1,2,3,4,5]
# b = [4,4,4,4]
# print(a.__add__(b))


#* len() (__len__) - Метод полиморф
print(len('hello'))
# print(len([1,2,3]))
# print(len({1:1,2:2}))
# print('abc'.__len__())

from math import pi

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return f'Я фигура в двумерной плоскости: {self.name}'
    

class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2
    
    def fact(self):
        return super().fact() + '\nУ квадрата все стороны равны и углы равны 90 градусам!'
    

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)
    

class Triangle(Shape):
    def __init__(self, base, height) -> None:
        super().__init__('Трeугольник')
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


obj1 = Square(8)
obj2 = Circle(3)
obj3 = Triangle(5, 7)

print(obj1.area())
print(obj1.fact())
print()
print(obj2.area())
print(obj2.fact())
print()
print(obj3.area())
print(obj3.fact())