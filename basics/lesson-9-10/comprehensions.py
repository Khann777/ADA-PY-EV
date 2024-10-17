
#! =====================================Comprehensions=========================================
#* Генератор, с помощью которого мы можем создавать последовательности используя цикл for в одну строку

#* Структура
#* Результат for элемент in последовательность
#* i for i in list1
#* результат for элемент in последовательность if фильтр - фильтр
#* i for i in list1 if i % 2 == 0
#* тело1 if условие else тело2 for элемент in последовательность -- условие
#*  'четное' if i % 2 == 0 else 'нечетное' for i in range(1,11)

comprehension = (i for i in range(1, 6))
print(comprehension) #* <generator object <genexpr> at 0x10235a5f0>
#* Генератор - итерируемый объект, который не хранит в себе полностью всю последовательность данных, а создает их когда требуется

#* print(next(comprehension))
#* print(next(comprehension))

#* next() - функция, которая запрашивает у генератора текущий элемент, и генератор создает следующий элемент

#! ============================================================================================

list_comprehension = list((i**2 for i in range(1, 11)))
#* print(list_comprehension) #* [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_comprehension2 = [i**2 for i in range(1,11)]
#* print(list_comprehension2) #* [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#? Создайте список состоящий из нечетных чисел от 1 до 50
list_comprehension3 = [i for i in range(1,51) if i % 2 != 0]
#* print(list_comprehension3) #* [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

list1 = []
for i in range(1, 51):
    if i % 2 != 0:
        list1.append(i)
#* print(list1)

#? Создайте список состоящий из 5 строк 'hello' используя comprehension
list_hello = ['hello' for i in range(5)]
#* print(list_hello) #* ['hello', 'hello', 'hello', 'hello', 'hello']

list2 = []
for _ in range(5):
    list2.append('hello')
#* print(list2)

#? Создайте список состоящий из чисел от 1 до 10, но вместо чисел написать четное или нечетное
list_odd = ['четное' if i % 2 == 0 else 'нечетное' for i in range(1,11)]
#* print(list_odd) #* ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное']

list3 = []
for i in range(1,11):
    if i % 2 == 0:
        list3.append('четное')
    else: 
        list3.append('нечетное')
#* print(list3) #* ['нечетное', 'четноsе', 'нечетное', 'четноsе', 'нечетное', 'четноsе', 'нечетное', 'четноsе', 'нечетное', 'четноsе']

#? Создайте список из существующего списка, оставив только строки
list1 = [1, 2, 3, 4, 5, 'hello', 'world', 'ada', 'courses']

list2 = [i for i in list1 if type(i) == str]
#* print(list2) #* ['hello', 'world', 'ada', 'courses']

list3 = []
for i in list1:
    if type(i) == str:
        list3.append(i)
#* print(list3) #* ['hello', 'world', 'ada', 'courses']

#! ==================================Dict Comprehensions=======================================
dict_ = dict((i, i ** 2) for i in range(1,11))
#* print(dict_) #* {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

dict_ = {i: i ** 2 for i in range(1, 11)}
#* print(dict_) #* {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#? Дан словарь, создайте его копию при помощи comprehension
dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_ = {key: value for key,value in dict1.items()}
#* print(dict_) #* {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_ = {}
for key, value in dict1.items():
    dict_[key] = value
#* print(dict_) #* {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

#? Дан словарь, поменяйте ключи со значениями используя comprehension
dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict2 = {value: key for key, value in dict1.items()}
#* print(dict2) #* {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict3 = {}
for key, value in dict1.items():
    dict3[value] = key
#* print(dict2) #* {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

#? Дан словарь, где значение - списки с числами, создайте словарь, где значениями буду суммы этих чисел
dict1 = {"a": [1,2,3,4], "b": [10,15,16,17], "c": [1,2,54]}

dict_ = {key: sum(value) for key, value in dict1.items()}
#* print(dict_) #* {'a': 10, 'b': 58, 'c': 57}

dict3 = {}
for key, value in dict1.items():
    dict3[key] = sum(value)
#* print(dict3) #* {'a': 10, 'b': 58, 'c': 57}


#! ===================================Вложенные Comprehension=================================
#? Создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа
#? {1: {1}, 2: {1, 2} 3: {1, 2, 3}, 4: {1, 2, 3, 4}, 5: {1, 2, 3, 4, 5}}

dict1 = {}
for i in range(1, 6):
    key = i
    value = [j for j in range(1, i+1)]
    dict1[key] = value
#* print(dict_) #* {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

dict2 = {i: [j for j in range(1, i+1)] for i in range(1, 6)}
#* print(dict2) #* {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

dict3 = {i: list(range(1, i+1)) for i in range(1,6)}
#* print(dict3) #* {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

#? Создать список, состоящий из 10 списков, в каждом из которых строка 'hello world' повтораяется по 5 раз
#? [['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
#? ['hello world', 'hello world', 'hello world', 'hello world', 'hello world']]

list1 = []
for i in range(10):
    inner_list = []
    for j in range(5):
        inner_list.append('hello world')
    list1.append(inner_list)
#* print(list1)

list2 = [['hello world' for j in range(5)] for i in range(10)]
#* print(list2)

list3 = [['hello world'] * 5] * 10
#* print(list3)

#? Создайте список, состоящий ищ 10 списков, в которых будут числа от 1 до 5
list2 = [[i for i in range(1, 6)] for j in range(10)]
#* print(list2) #* [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

list3 = []
for i in range(10):
    inner_list = []
    for j in range(1, 6):
        inner_list.append(j)
    list3.append(inner_list)
#* print(list3) #* [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

list4 = [list(range(1, 6))] * 10
#* print(list4) #* [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

#? Создайте словарь, где ключами буду числа от 1 до 5, а значениями будут словари, в которых ключами будут числа от 1 до этого числа, а значениями будут списки от 1 до этого числа

{
    1: {
        1: [1]
    },
    2: {
        1: [1],
        2: [1, 2]
    },
    3: {
        1: [1],
        2: [1, 2],
        3: [1, 2, 3]
    },
    4: {
        1: [1],
        2: [1, 2],
        3: [1, 2, 3],
        4: [1, 2, 3, 4]
    },
    5: {
        1: [1],
        2: [1, 2],
        3: [1, 2, 3],
        4: [1, 2, 3, 4],
        5: [1, 2, 3, 4, 5]
    }
}

dict1 = {i: {j: [h for h in range(1, j+1)] for j in range(1, i+1)} for i in range(1, 6)}
#* print(dict1)

{
    1: {
        1: [1]
        },
    2: {
        1: [1], 
        2: [1, 2]
        },
    3: {
        1: [1], 
        2: [1, 2], 
        3: [1, 2, 3]}, 
    4: {
        1: [1], 
        2: [1, 2], 
        3: [1, 2, 3], 
        4: [1, 2, 3, 4]}, 
    5: {
        1: [1], 
        2: [1, 2], 
        3: [1, 2, 3], 
        4: [1, 2, 3, 4], 
        5: [1, 2, 3, 4, 5]}
}

dict2 = {}
for i in range(1,6):
    inner_dict = {}
    for j in range(1, i+1):
        list_ = []
        for k in range(1, j+1):
            list_.append(k)
        inner_dict[j] = list_
    dict2[i] = inner_dict
#* print(dict2)

#? Дан словарь:
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
#? Создайте dict2:
#? - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
#? - значением должно быть количество повторений символов i в этом ключе

dict2 = {}
for key, value in dict1.items():
    count = 0
    new_key = key
    for i in key:
        if i == 'i':
            new_key = key.replace('i', '')
            count = count + 1
        value = count
    dict2[new_key] = value

#* print(dict2) #* {'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mnvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}

dict3 = {i.replace('i', ''): i.count('i') for i in dict1.keys()}
#* print(dict3) #* {'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mnvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}


#? Используя приведенный словарь dict_, создайте список из id, 
#? которые хранятся под ключом comments. Берите только те комментарии, 
#? количество которых больше 3

dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

list_ = []
for i in dict_.values():
    comments = i.get('comments')
    if len(comments) > 3:
        id = [comment['id'] for comment in comments]
        list_.extend(id)
#* print(list_) #* [1, 2, 3, 4, 5, 6]
