
#! ===========================================ООП==============================================
#* ООП - Объектно Ориентированное Программирование - Парадигма (стиль написания кода)
#* Классы принято именовать при помощи CamelCase

class Person:
    #* Переменные внутри класса - аттрибуты
    brain = 1 #* Аттрибут класса
    body = 1 #* Аттрибут класса
    legs = 2 #* Аттрибут класса
    arms = 2 #* Аттрибут класса

    #* Функции внутри класса - методы
    def __init__(self, name, last_name, age) -> None:
        #* __init__ - метод, который будет добавлять в объект те аттрибуты, которые отличаются у разных объектов
        #* self - ссылка на объект, который только что создался
        self.name = name
        self.last_name = last_name
        self.age = age

    def walk(self):
        # print(f'{self.name} ходит...')
        return f'{self.name} ходит...'

    def happy_b_day(self):
        self.age += 1
        return f'У пользователя {self.name} день рождения, исполнилось {self.age} лет.'

nikita = Person('Nikita', 'Grebnev', 18)
print(nikita) #* <__main__.Person object at 0x1031d1010>
print(nikita.age) #* 18
print(nikita.name) #* Nikita
nikita.walk() #* Nikita ходит...
print(nikita.walk()) #* Nikita ходит...
print(nikita.happy_b_day())
print(nikita.happy_b_day())
print(nikita.happy_b_day())
print(nikita.happy_b_day())

tima = Person('Tima', 21, 'Zhoroev')
print(tima) #* <__main__.Person object at 0x1044725d0>
print(tima.age) #* 21
print(tima.name) #* Tima
print(tima.last_name) #* Zhoroev

nikita.hello = 'hello'

print(nikita.hello) #* hello
# print(tima.hello) #* AttributeError: 'Person' object has no attribute 'hello'

#! ======================================Объекты класса========================================

"""
Объект, Экземпляр, Instance (инстанс) - синонимы, которые обозначают объект, созданный по шаблону класса
"""

#! =====================================Аттрибуты и методы=====================================

"""
Аттрибуты - переменные
Методы - функции
"""

#! ============================================================================================

class A:
    var1 = 'Аттрибут(переменная) класса'

    def __init__(self) -> None:
        self.var2 = 'Аттрибут(переменная) объекта'
    
    def __str__(self) -> str:
        return 'Объект от класса А'
    
obj1 = A()

print(nikita)
print(obj1)

print(dir(A)) #* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'var1']

print(dir(obj1)) #* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']


class Calculator:
    def add(self, num1, num2) -> int:
        return num1 + num2
    def minus(self, num1, num2) -> int:
        return num1 - num2
    def multiply(self, num1, num2) -> int:
        return num1 * num2
    def divide(self, num1, num2) -> int:
        return num1 / num2
    def reminder(self, num1, num2) -> int:
        return num1 % num2
    def powerof(self, num1, num2) -> int:
        return num1 ** num2
    def sqrt(self, num1) -> int:
        return num1 ** 0.5
    def percent(self, total_sum, percent) -> int:
        return (total_sum * percent) / 100
    def super_method(self, string) -> int:
        return eval(string)

calc = Calculator()
print(calc.add(15,10)) #* 25
print(calc.powerof(5,2)) #* 25
print(calc.sqrt(625)) #* 25.0
print(calc.percent(100, 25)) #* 25.0
print(calc.super_method('(10-5)*7 - 10')) #* 25

