
#! Задачи по классам:

#? 1) Нужно создать программу для банкомата, который принимает деньги и выдает деньги. Создайте класс Банкомат с методами: 

#? Чтобы банкомат принимал деньги
#? Чтобы банкомат выдавал деньги
#? Чтобы банкомат показывал остаток денег

class ATM:
    balance = 0
    def take_money(self, amount) -> int:
        self.balance += amount
    def give_money(self, amount) -> int:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception('Недостаточно средств на балансе')
    def show_money(self) -> None:
        print(self.balance)
    
obj = ATM()
# obj.take_money(1000)
# obj.show_money()
# obj.give_money(500)
# obj.show_money()

#? 2) Создайте класс Song с атрибутами author, title и year. Напишите методы showauthor, showtitle и show_year, которые возвращают строки с информацией о песне. Создайте объект этого класса и выведите информацию о песне, используя методы.

class Song:
    def __init__(self, author: str, title: str, year: str) -> None:
        self.author = author
        self.title = title
        self.year = year

    def show_author(self) -> str:
        return self.author

    def show_title(self) -> str:
        return self.title

    def show_year(self) -> str:
        return self.year
    
obj = Song('xcho', '6.3', '2024')
# print(obj.show_author())
# print(obj.show_title())
# print(obj.show_year())

#? 3) Создайте класс BankAccount с атрибутом экземпляра balance, инициализируемым нулем. Напишите методы withdraw и deposit, которые изменяют баланс и выводят его текущее значение. Создайте объект этого класса, пополните и снимите средства с баланса, и выведите баланс после каждой операции.

class BankAccount:
    balance = 0
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
            print(self.balance)
        else:
            raise Exception('Недостаточно средств на балансе')
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

obj = BankAccount()
# obj.deposit(1000)
# obj.withdraw(500)

#? 4) Создайте класс Taxi с атрибутами name, cost и cost_km. Напишите метод get_total_cost, который принимает расстояние в километрах и возвращает общую стоимость поездки. Создайте несколько объектов этого класса и выведите стоимость поездки для каждого из них.

class Taxi:
    name = 'ADA Taxi'
    cost = 100
    cost_km = 1

    def get_total_cost(self, distance: int) -> int:
        return (self.cost_km * distance) + self.cost

obj1 = Taxi()
obj2 = Taxi()
obj3 = Taxi()

# print(obj1.get_total_cost(10))
# print(obj2.get_total_cost(15))
# print(obj3.get_total_cost(20))


#? 5) Создайте класс Phone с атрибутами name, last_name и phone. Напишите метод get_info, который выводит информацию о контакте. Создайте объект этого класса и выведите информацию о контакте.

class Phone:
    name = 'Davlyat'
    last_name = 'Nurdinov'
    phone = '+996509079999'

    def get_info(self) -> str:
        return f'Контакт {self.name} {self.last_name} с номером - {self.phone}'
    
obj = Phone()
# print(obj.get_info())

#? 6) Создайте класс Salary с атрибутом класса percent (по умолчанию 8). Напишите метод __init, который инициализирует атрибуты экземпляра salary и experience. Напишите метод count_percent, который рассчитывает налог на зарплату за весь период работы. Создайте объект этого класса и выведите рассчитанный налог.

class Salary:
    percent = 8

    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience
    def count_percent(self) -> int:
        return (self.salary * self.percent) * self.experience / 100
    
obj = Salary(1200, 8)
# print(f'Налог на зарплату за весь период работы - {obj.count_percent()}')

#! Задачи по инкапсуляции

#? 1) Создайте класс A, который содержит три метода: public(), _protected() и private(), которые просто возвращают любую строку. Демонстрируйте, как получить доступ к каждому из методов через экземпляр класса A.

class A:
    def public(self):
        return 'public method'
    def _protected(self):
        return 'protected method'
    def __private(self):
        return 'private method'
    
obj = A()
# print(obj.public())
# print(obj._protected())
# print(obj._A__private())

#? 2) Создайте класс Car, который содержит приватное поле speed. Реализуйте методы(getter, setter) для установки и отображения значения этого поля. Создайте экземпляр класса и продемонстрируйте работу методов.

class Car:
    __speed = 0
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed

obj = Car()
# print(obj.get_speed())
obj.set_speed(100)
# print(obj.get_speed())

#? 3) Создайте класс Car, который содержит приватное поле speed. Используйте декораторы @property и @speed.setter для получения и установки значения этого поля. Создайте экземпляр класса и продемонстрируйте работу свойств.

class Car:
    __speed = 0
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def set_speed(self, amount):
        self.__speed = amount

obj1 = Car
obj1.speed = 100
# print(obj1.speed)

#? 4) Создайте класс Person, который содержит публичный атрибут name, защищённый атрибут _phone_number и приватный атрибут card_number. Создайте экземпляр класса и продемонстрируйте доступ к каждому из атрибутов.

class Person:
    name = 'Davlyat'
    _phone_number = '+996509079999'
    __card_number = '1234 5678 9012 3456'

a = Person
print(a.name)
print(a._phone_number)
print(a._Person__card_number)

#? 5) Создайте класс Game, который содержит приватное поле __level и публичное поле name. Реализуйте метод play, который увеличивает уровень при игре более 2 часов. Создайте метод для получения текущего уровня. Создайте экземпляр класса и продемонстрируйте работу методов.

class Game:
    __level = 0
    name = 'level'

    def play(self, playtime: int):
        for time in range(1, playtime + 1, 2):
            self.__level += 1
    
    def current_level(self):
        return self.__level
    
obj = Game()
print(obj.current_level())
obj.play(100)
print(obj.current_level())