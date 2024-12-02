"""
SOLID - Это набор из пяти принципов, объектно ориентированного программирования, которые были созданы для написсания гибкого, поддерживаемого кода.
"""

"""
S(SRP - Single Responsibility Principle) - Приницп единой ответственности. У каждого класса должно быть только одно предназначение, класс должен выполнять только один задачу
"""

# before
class ExportCsv:
    def __init__(self, raw_data) -> None:
        self.data = self.prepare(raw_data)

    def prepare(self, raw_data):
        result = ''
        for data in raw_data:
            new_line = f"{data['name']}, {data['last_name']}\n"
            result += new_line
        return result
    
    def write(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data)

# after

class FormatData:
    def __init__(self, raw_data) -> None:
        self.raw_data = raw_data

    def prepare(self, raw_data):
        result = ''
        for data in raw_data:
            new_line = f"{data['name']}, {data['last_name']}\n"
            result += new_line
        return result
    

class FileWriter:
    def __init__(self, filename) -> None:
        self.filename = filename

    def write(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data)


"""
O (OCP - open-closed principle) - Принцип открытости-закрытости, класс должен быть открыт для расширения, но не для модификации
"""

# before
class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'default':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4

# after
class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'default':
            return self.price * 0.2
        

class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
    

class StaffDiscount(Discount):
    def get_discount(self):
        return super().get_discount() - 100
    
"""
L (LSP Liskov substitution priciple/Принцип подстановки Лисков) - объекты дочерних классов должны быть взаимозаменяемыми с объектами родительских классов
"""

# before 
class Bird:
    def fly(self):
        return 'i can fly'

class Ostrich(Bird):
    def fly(self):
        raise Exception('Страус летать не умеет')

bird1 = Bird()
bird2 = Ostrich()

def get_fly(bird_obj):
    return bird_obj.fly()

# print(get_fly(bird1))
# print(get_fly(bird2))

#* after
class Bird:
    def move(self):
        return 'i can fly'
    
class Sparrow(Bird):
    ...

class Ostrich(Bird):
    def move(self):
        return 'I can not fly, but I can run'
    
bird1 = Bird()
bird2 = Ostrich()
bird3 = Sparrow()

def get_move(bird_obj):
    return bird_obj.move()

# print(get_move(bird1))
# print(get_move(bird2))
# print(get_move(bird3))

"""
I - (ISP - Interface Segregation Principle) - Не заставляйте классы реализовывать интерфейсы которые им не нужны/которые они не используют
"""

#*before

class Worker:
    def eat(self):
        return 'Eating'
    def work(self):
        return 'Working'
    
class RoboWorker(Worker):
    def work(self):
        return 'working'

class HumanWorker(Worker):
    ...
    
class LazyWorker(Worker):
    def eat(self):
        return 'I don\'t like to work, but I love to eat'

robot1 = RoboWorker()
# print(robot1.work())
# print(robot1.eat())

#* after

class Workable:
    def work(self):
        return 'Working'

class Eatable:
    def eat(self):
        return 'Eating'
    
class RoboWorker(Workable):
    ...

class HumanWorker(Workable, Eatable):
    ...
    
class LazyWorker(Eatable):
    def eat(self):
        return 'I don\'t like to work, but I love to eat'
    
lazy_obj =LazyWorker()
# print(lazy_obj.eat())
# print(lazy_obj.work())


"""
D - (DIP - Dependency Inversion Principle/Принцип Инверсии Зависимостей)  - модули верхних уровней не должны зависеть от модулей нижних уровней, модули от абстракций, а не от конкретных реализаций
"""