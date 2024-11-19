
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


#! Задания по Абстракции:
from abc import ABC, abstractmethod

#? 1) Создайте абстрактный класс Transport с методами start() и stop(). Затем создайте классы Car и Bicycle, которые реализуют эти методы.
#? Задача: В Car добавьте метод, имитирующий запуск двигателя, а в Bicycle — метод для проверки состояния цепи.

class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Transport):
    def start(self):
        return f'Двигатель запущен'
    def stop(self):
        return f'Двигатель заглушен'
    
class Bicycle(Transport):
    def start(self):
        return f'Состояние цепи отличное'
    def stop(self):
        return f'Велосипед поставлен на подножку'
    
obj = Car()
# print(obj.start())
# print(obj.stop())
obj = Bicycle()
# print(obj.start())
# print(obj.stop())

#? 2) Создайте абстрактный класс ElectronicDevice с методом turn_on(). Реализуйте классы Phone и Laptop, которые наследуют этот класс и добавьте в каждый из них метод turn_off().

class ElectronicDevice(ABC):
    @abstractmethod
    def turn_on(self):
        return 'Устройство включено!'

class Phone(ElectronicDevice):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return 'Устройство выключено!'

class Laptop(ElectronicDevice):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return 'Устройство выключено!'
    
obj = Phone()
# print(obj.turn_on())
# print(obj.turn_off())
obj = Laptop()
# print(obj.turn_on())
# print(obj.turn_off())

#? 3) Создайте абстрактный класс Person с методом get_info(), который возвращает информацию о человеке. Создайте классы Student и Teacher, которые расширяют Person. Реализуйте get_info() так, чтобы он возвращал информацию в зависимости от роли (студент или преподаватель).

class Person(ABC):
    @abstractmethod
    def get_info(self):
        pass

class Student(Person):
    def get_info(self):
        return 'Я - студент'
class Teacher(Person):
    def get_info(self):
        return 'Я - учитель'

obj = Student()
# print(obj.get_info())
obj = Teacher()
# print(obj.get_info())

#? 4) Создайте интерфейс PaymentMethod с методом process_payment(amount). Реализуйте классы CreditCard и PayPal, которые используют этот интерфейс и выводят сообщение о платеже с разными способами оплаты.

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount, name):
        return f'Оплата {amount}$ через - {name}'
    
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return super().process_payment(amount, 'Кредитная карта')
    
class Paypal(PaymentMethod):
    def process_payment(self, amount):
        return super().process_payment(amount, 'PayPal')
    
obj = CreditCard()
# print(obj.process_payment(500))
obj = Paypal()
# print(obj.process_payment(500))

#? 5) Создайте абстрактный класс Document с методами open(), save(), и close(). Реализуйте два класса — WordDocument и PDFDocument, которые определяют уникальные действия для каждого метода.

class Document(ABC):
    @abstractmethod
    def open(self):
        ...
    
    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def close(self):
        ...

class WordDocument(Document):
    def open(self):
        return 'Открытие Word документа'
    def save(self):
        return 'Сохранение Word документа'
    def close(self):
        return 'Закрытие Word документа'
class PDFDocument(Document):
    def open(self):
        return 'Открытие PDF документа'
    def save(self):
        return 'Сохранение PDF документа'
    def close(self):
        return 'Закрытие PDF документа'

# obj = WordDocument()
# print(obj.open())
# print(obj.save())
# print(obj.close())
# obj = PDFDocument()
# print(obj.open())
# print(obj.save())
# print(obj.close())

#? 6) Создайте абстрактный класс UIComponent с методами draw() и resize(). Реализуйте классы Button, TextField и CheckBox, которые наследуют UIComponent и определяют специфическое поведение для этих методов.

class UIComponent(ABC):
    @abstractmethod
    def draw(self):
        ...
    def resize(self):
        ...

class Button(UIComponent):
    def draw(self):
        return 'Рисование кнопки'
    def resize(self):
        return 'Изменение размера кнопки'
class TextField(UIComponent):
    def draw(self):
        return 'Рисование TextField'
    def resize(self):
        return 'Изменение размера TextField'
class CheckBox(UIComponent):
    def draw(self):
        return 'Рисование Checkbox'
    def resize(self):
        return 'Изменение размера Checkbox'
    
obj = Button()
print(obj.draw())
print(obj.resize())
obj = TextField()
print(obj.draw())
print(obj.resize())
obj = CheckBox()
print(obj.draw())
print(obj.resize())

#? 7) Создайте абстрактный класс User с методами login() и logout(). Реализуйте классы Admin и Guest, которые расширяют User. В классе Admin добавьте метод manage_users(), а в Guest — view_content(). Напишите программу, которая управляет входом и выходом пользователей и предоставляет доступ к уникальным методам каждого пользователя в зависимости от его типа.

class User(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class Admin(User):
    def login(self):
        return 'Вы вошли как админ'
    def logout(self):
        return 'Вы вышли из аккаунта админа'
    def manage_users(self, count):
        return f'В сети {count} пользователей'

class Guest(User):
    def login(self):
        return 'Для входа вам нужно зарегистрироваться'
    def logout(self):
        return 'До свидания'
    def view_content(self):
        return 'Что бы смотреть контент вам нужно зарегистрироваться!'
    
# obj = Admin()
# print(obj.login())
# print(obj.logout())
# print(obj.manage_users(10))
# obj = Guest()
# print(obj.login())
# print(obj.logout())
# print(obj.view_content())

#? 8) Создайте абстрактный класс Product с методами get_price() и get_name(). Реализуйте классы Electronics, Clothing и Food, которые представляют товары из разных категорий и добавляют особенности, характерные для каждой из них, например, warranty() для Electronics и size() для Clothing. Реализуйте корзину покупок, которая принимает объекты Product, и выведите итоговую сумму всех товаров в корзине.

class Product(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def get_price(self):
        return self.price
    
    @abstractmethod
    def get_name(self):
        return self.name
    
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if not isinstance(product, Product):
            return 'Добавьте продукт'
        self.items.append(product)

    def total_price(self):
        return sum(item.get_price() for item in self.items)
    
cart = Cart()

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty_time = warranty

    def get_price(self):
        return super().get_price()
    
    def get_name(self):
        return super().get_name()
    
    def warranty(self):
        return f'Срок гарантии - {self.warranty_time} лет'

obj = Electronics('phone', 10000, 10)
print(obj.warranty())
cart.add_product(obj)

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size
    def get_price(self):
        return super().get_price()
    def get_name(self):
        return super().get_name()
    def size(self):
        return f'Размер одежды - {self._size}'

obj = Clothing('футболка', 1000, 'S')
print(obj.size())
cart.add_product(obj)

class Food(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self._weight = weight

    def get_price(self):
        return super().get_price()
    
    def get_name(self):
        return super().get_name()
    
    def weight(self):
        return f'Вес еды - {self._weight} грамм'

obj = Food('burger', 100, 250)
print(obj.weight())
cart.add_product(obj)
print(cart.total_price())



#! задачи по Ассоциации:

#? 1) Создайте два класса: Address с аттрибутами street, city, country и Person с аттрибутом address, который хранит объект от класса Address. Адрес является неотъемлемой частью человека, и при удалении объекта Person адрес также удаляется. 

class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    
    def __str__(self):
        return f'street - {self.street}, city - {self.city}, country - {self.country}'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = Address('Razzakova', 'Bishkek', 'Kyrgyzstan')

obj = Person('Davlyat', 23)
# print(obj.address)

#? 2) Создайте два класса: School с аттрибутом students (список) и методом add_student() для добавления ученика и методом show_students() для отображения всех студентов. Класс Student имеет аттрибут school, указывающий на объект School. Школа существует независимо от учеников, и один ученик может учиться в разных школах.

class School:
    students = []
    def __init__(self, name):
        self.name = name

    def add_student(self, name):
        self.students.append(name)
    
    def show_student(self):
        print(f"Ученики в {self.name}:")
        for student in self.students:
            print(f"- {student}")

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def __str__(self):
        return f'Студент - {self.name} учится в - {self.school}'
    
# school = School('Oxford')
# student = Student('Davlyat', school)
# print(student)
# print(school.students)
# school.add_student('Davlyat')
# school.add_student('Nikita')
# school.show_student()

#? 3) Создайте два класса: Mouse с аттрибутом model и Computer с аттрибутом mouse, который может содержать объект Mouse. В классе Computer реализуйте метод check_mouse(), проверяющий подключение мыши. Мышь может быть подключена или отключена, и компьютер может работать без неё.

class Mouse:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, mouse = None):
        self.mouse = mouse

    def check_mouse(self):
        if not self.mouse == None:
            return f'Мышка - {self.mouse.model} подключена'
        else:
            return "Мышка не подключена"

mouse = Mouse('logitech')
comp = Computer(mouse)
# print(comp.check_mouse())
comp = Computer()
# print(comp.check_mouse())


#? 4) Создайте два класса: Room с аттрибутом name и House с аттрибутом rooms (список) и методами add_room() для добавления комнаты и count_rooms() для подсчета количества комнат. Комнаты — неотъемлемая часть дома, и при удалении дома все комнаты также удаляются.

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room.name)

    def count_rooms(self):
        return f'Комнат в доме - {len(self.rooms)}'
    
room1 = Room('Kitchen')
room2 = Room('Toilet')
room3 = Room('Room')
house = House()
house.add_room(room1)
house.add_room(room2)
house.add_room(room3)
# print(house.count_rooms())

#? 5) Создайте два класса: Engine и Car, где у Car будет обязательный аттрибут engine. В классе Car реализуйте метод start(), который проверяет наличие двигателя перед запуском. Автомобиль не может существовать без двигателя

class Engine:
    def __init__(self, engine_num):
        self.engine_num = engine_num
        pass
    def __str__(self):
        return self.engine_num

class Car:
    def __init__(self):
        self.engine = Engine('2JZ')
    def start(self):
        if not self.engine == None:
            return 'Автомобиль запущен c двигателем - {self.engine}'
        
obj = Car()
# print(obj.start())