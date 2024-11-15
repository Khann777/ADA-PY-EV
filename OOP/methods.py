"""
В классах есть множество разных методов, мы знакомы с самыми распространенными, методы которые работают с конкретным экземпляром класса.
Но, так-же в разработке часто используются такие методы как:
1. classmethods
2. staticmethods
"""

class User:
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        return f'hello {self.name}'

obj = User('Davlyat')
# print(obj.greet())

#* classmethods - методы, которые работают не с объектом а с самим классом, и создаются при помощи декоратора @classmethod, класс методы всегда первым аргументом принимают cls(ссылка на класс)

class User:
    default_role = 'user'

    def __init__(self, name, role=None) -> None:
        self.name = name
        self.role = role or User.default_role

    @classmethod
    def create_admin(cls, name) -> None: #* это метод класса, который создает объект с фиксированной ролью админа
        return cls(name, role='admin')
    
user = User('Alice')
print(user.name, user.role)

admin = User.create_admin('Nik')
print(admin.name, admin.role)

import json

class Order:
    def __init__(self, order_id, items) -> None:
        self.order_id = order_id
        self.items = items
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(order_id=data['order_id'], items=data['items'])

json_data = '{"order_id":1, "items": ["apple", "banana"]}'
order = Order.from_json(json_data)
print(order.order_id, order.items)

#? staticmethod - независимые функции внутри класса
#? Это методы которые не принимают никаких ссылок в аргументы, и они не зависят ни от объекта ни от класса, зачастую применяются для каких-либо операций

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
print(MathUtils.add(5,5))
print(MathUtils.multiply(5,5))

class Product:
    tax_rate = 0.2 #! Налог 20%
    product_list = []

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    @staticmethod
    def calculate_tax(price):
        return price + (price * Product.tax_rate)
    
iphone_object = Product('iPhone 11', 1000)
price_with_tax = Product.calculate_tax(iphone_object.price)
print(price_with_tax)

class Validator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return 'Valid' if '@' in email and '.' in email[email.index("@"):] else 'Invalid'
    
print(Validator.is_valid_email('dasd@dasd.da'))

class User:
    def __init__(self, username, role) -> None:
        self.username = username
        self.role = role

    @classmethod
    def create_guest(cls, username):
        return cls(username, 'guest')

    def __str__(self):
        return f'{self.role} - {self.username}'

user = User('davlyat', 'user')
print(user)

guest = User.create_guest('anonym')
print(guest)