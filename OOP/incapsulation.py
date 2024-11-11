# """
# Инкапсуляция - принцип ООП, у которого есть 2 трактовки
# 1) сбор всех необходимых аттрибутов в одну "капсулу" (класс)
# 2) сокрытие данных (ограничение доступа к аттрибутам)
# """


# # Виды доступа к аттрибутам
# # 1) public - публичные аттрибуты
# # 2) protected (защищенные) - с одним underscore в начале
# # 3) private (приватный) - с двумя underscore в начале
"""
1) публичные аттрибуты/методы наследуются и их можно использовать где угодно
2) защищенные аттрибуты/методы наследуются, но работать с ними можно только внутри класса где аттрибут/метод был создан, и в его подклассах
3) приватные аттрибуты/методы не наследуются, и работать с ними принято только внутри класса, где аттрибут/метод был создан

"""
# class A:
#     attr1 = 'public'
#     _attr2 = 'protected'
#     __attr3 = 'private'

# obj = A()

# print(obj.attr1) # public
# print(obj._attr2) # protected
# # print(obj.__attr3) # AttributeError: 'A' object has no attribute '__attr3'. Did you mean: '_A__attr3'?
# print(obj._A__attr3) # private

# "obj.__dict__ - словарь с переменными объекта" 
# # print(A.__dict__) {'__module__': '__main__', 'attr1': 'public', '_attr2': 'protected', '_A__attr3': 'private', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

# class B:
#     x = 'hello'

#     def __init__(self):
#         self.y = 'world'

# obj1 = B()
# print(obj1.__dict__) # {'y': 'world'}


# "==========================================Getters/Setters===================================="
# # методы, с помощью которых можно получать/изменять значение аттрибута

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            raise Exception('Возраст не может быть меньше 0 или больше 100')
        
# obj2 = Person('Nikita', '10')
# print(obj2.name)
# # print(obj2._Person__age) # 10
# # print(obj2.get_age()) 10 Легальный способ
# obj2.set_age(20)
# print(obj2.get_age()) # 20
# obj2.set_age(1234123) Exception: Возраст не может быть меньше 0 или больше 100


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    # декоратор property делает из метода аттрибут
    @property
    def age(self):
        return self.__age
    
    # декоратор setter вызывается когда пишется obj.age = 'value'
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            raise Exception('возраст не может быть меньше 0 или больше 100')
        
obj = Person('nikita', 10)
print(obj.name)
print(obj.age)
obj.age = 55
print(obj.age)