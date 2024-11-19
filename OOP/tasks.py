
#! Задачи по наследованию и полиморфизму

#? 1) Создайте класс Phone, который наследует класс Device.
#? Должны быть атрибуты brand, model, pixel.

class Device:
    def __init__(self):
        pass


class Phone(Device):
    def __init__(self, brand, model, pixel):
        super().__init__()
        self.brand = brand
        self.model = model
        self.pixel = pixel

    def __str__(self):
        return f"Phone - Brand: {self.brand}, Model: {self.model}, Pixel: {self.pixel})"

obj = Phone('iPhone', '16 Pro Max', '12432')
# print(obj)


#? 2) Создайте класс Car с атрибутами max_speed и weight. Создайте метод, который посчитает время прохождения 100 метров. Формула для нахождения max_speed / 100 * 3.14. Создайте два экземпляра.

class Car:
    def __init__(self, max_speed, weight):
        self.max_speed = max_speed
        self.weight = weight

    def time(self):
        return self.max_speed / 100 * 3.14
    
obj1 = Car(240, 3000)
obj2 = Car(200, 3000)

# print(obj1.time())
# print(obj2.time())


#? 3) Создайте класс Person с атрибутами name, age. Создайте метод eat, который принимает обязательный аргумент food, данный метод выводит сообщение 'Я кушаю {food}'. Определить класс Reader, хранящий информацию о читателе библиотеки. Атрибуты: номер читательского билета, телефон. Создайте два метода take_book, return_book, которые принимают аргумент book_name. take_book выводит сообщение '{name} взял {book_name}.
#? return_book выводит сообщение '{name} вернул {book_name}.
#? Переопределите метод eat в Person, так чтобы он выводил сообщение:
#? 'Я {name} и я не кушаю {food}, а предпочитаю книги' 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        self.food = food
        return f'Я кушаю {self.food}'
    

class Reader(Person):
    def __init__(self, ticket, phone):
        super().__init__('Davlyat', '23')
        self.ticket = ticket
        self.phone = phone

    def take_book(self, book_name):
        self.book_name = book_name
        return f'{self.name} взял {self.book_name}'

    def return_book(self, book_name):
        self.book_name = book_name
        return f'{self.name} вернул {self.book_name}'
    
    def eat(self, food):
        self.food = food
        return f'Я {self.name} и я не кушаю {self.food}, а предпочитаю книги'

        
# obj = Reader('123', '+996509079999')
# print(obj.take_book('Harry Potter'))
# print(obj.return_book('Harry Potter'))
# print(obj.eat('Burger'))


#? 4) Создать класс Student, Aspirant. Student содержит атрибуты name, group, average_mark(средняя оценка). Создайте метод get_scholarship, который посчитает стипендию за счёт средней оценки. Если средняя оценка равна 5 то метод возвращает 2000 сом, иначе 1500 сом. Класс Aspirant должен наследовать класс Student. В Aspirant переопределите метод get_scholarship, так чтоб если оценка 5 то возвращает 3000 сом, иначе 2500 сом. 

class Student:
    def __init__(self, name, group, average_mark):
        self.name = name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return 2000
        else: 
            return 1500        
class Aspirant(Student):
    def __init__(self, name, group, average_mark):
        super().__init__(name, group, average_mark)

    def get_scholarship(self):
        if self.average_mark == 5:
            return 3000
        else:
            return 2500
obj = Student('Davlyat', 'surgeant', 4)
# print(obj.get_scholarship())
obj = Aspirant('Davlyat', 'Surgeant', 5)
# print(obj.get_scholarship())

#? 5) Создайте базовый класс Money у которого есть два аттрибута экземпляра класса (country, symbol) и классы Dollar и Euro, которые наследуются от Money, у этих классов должен быть аттрибут rate, в котором будет храниться курс валют. Эти классы должны иметь метод exchange, который конвертирует сумму в сомы и возвращает строку с результатом 
#? "$ {amount} равен {som} сомам".
#? "€ {amount} равен {som} сомам"

class Money:
    def __init__(self, country, symbol):
        self.country = country
        self.symbol = symbol

class Dollar(Money):
    __rate = 86.5
    def exchange(self, amount):
        som = amount * self.__rate
        return f"$ {amount} равен {som} сомам"

class Euro(Money):
    __rate = 91.5
    def exchange(self, amount):
        som = amount * self.__rate
        return f"€ {amount} равен {som} сомам"
    
obj = Dollar('USA', '$')
print(obj.exchange(500))
obj = Euro("Europe", '€')
print(obj.exchange(500))