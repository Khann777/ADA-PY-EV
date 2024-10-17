from functools import reduce
#? 1) напишите программу которая отбирает слова длина которых больше 7 из исходного списка
list1 = ['hello', 'hello world', 'count', 'ada courses', 'python', 'backend group']
list2 = list(filter(lambda x: len(x) > 7, list1))
# print(list2) # ['hello world', 'ada courses', 'backend group']

#? 2)  напишите программу которая считает количество четных и нечетных чисел в списке и выводит их количество в формате строки "четные: {колич'ество}, нечетные: {количество}"
list1 = list(range(1,101))
result = f'четные: {len(list(filter(lambda x: x % 2 == 0, list1)))}, нечетные: {len(list(filter(lambda x: x % 2 != 0, list1)))}'
# print(result) # четные: 50, нечетные: 50

#? 3) напишите программу которая находит самое длинное имя в списке
list_ = ['Никита', "Андрей", "Александр", "Иван", "Евгений"]
result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result) # Александр

#? 4) Напишите програму которая меняет число на 'fizz' если оно делится на 3, и на строку 'buzz' если не делится, в диапазоне чисел от 1 до 50 включительно
list1 = list(range(1,51))
list2 = list(map(lambda x: 'fizz' if x % 3 == 0 else 'buzz', list1))
# print(list2) # ['buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz', 'fizz', 'buzz', 'buzz']

#? 5) напишите программу которая находит минимальное значение у элемента в списке
import random
random_list = [random.randint(1, 100) for _ in range(25)]
result = reduce(lambda x, y: x if x < y else y, random_list)
# print(random_list)
# print('result: ', result)

def xyz(x, y, z):
    pass
