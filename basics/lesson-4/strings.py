
#! ========================================Строки================================================
#* Строки - неизменяемый, индексируемый, итерируемый тип данных, который предназначен для хранения текста, заключенного в одинарные или двойные кавычки

string1 = 'Строка с одинарными кавычками'
string2 = "Строка с двойными кавычками"
#* error_string = 'Неправильная строка"

string3 = "don't" #* Внутри двойных кавычек, все одинарные - просто символы
string4 = ' "ADA Courses" ' #* Внутри одинарных кавычек, все двойные - просто символы

string5 = '''
Многострочный текст
в одинарных кавычках
тут можно вставить "любые" 'кавычки'
'''

string6 = '''
Многострочный текст
в одинарных кавычках
тут можно вставить "любые" 'кавычки'
'''

string7 = 'hello' + ' ' + 'world' #* Конкатенация строк (склеивание)
print(string7)

string_hello = 'hello'
string_world = 'world'
print(string_hello + ' ' + string_world) #* тоже конкатенация

print(string_hello * 8) #* hellohellohellohellohellohellohellohello

#! ================================Экранизация строк=============================================
#* \n - перенос на новую строку
print('hello\nworld') #* hello
                      #* world

#* \t - табуляция
print('hello\tworld') #* hello    world

#* \' - отображение '
#* \" - отображение "
print('Dont\'t')

#! ================================Форматирование строк==========================================

product_title = 'iPhone 15'
price = 1000
#* print('Название: product_title, цена: price') #* Название переменных внутри строки, не считаются переменными, они считаются просто символами
#* print('Название: ', product_title, 'цена: ', price)

#* 1 способ (f-строка)
#* format1 = f'Название: {product_title}\nЦена: {price} '
#* print(format1)
"""
Название: iPhone 15
Цена: 1000
"""

#* 2 способ
format2 = 'Название: {}\nЦена: {}'
print(format2.format('iPhone 16', 1200))
print(format2.format('Молоко', 100))

#* 3 способ
format3 = 'Название: %s\nЦена: %s'
print(format3 % ('iPhone 16', 1200))

#! =====================================Методы строк=============================================

#* Методы - функции, которые относятся к определенному типу данных(классу), к ним мы обращаемся через точку

#*dir() - функция, которая позволяет посмотреть все методы класса
print(dir(str))

#* string.upper - переводит все символы строки в верхний регистр
print('hello'.upper()) #* HELLO

#* string.lower - переводит все символы строки в нижний регистр
print('HELLO'.lower()) #* hello

#* string.swapcase() - переводит регистр символов строки в противоположный
print('hELLo'.lower()) #* HellO

#* string.title() - делает первую букву каждого слова заглавной
print('hello world'.title())

#* string.capitalize() - делает первую букву первого слова заглавной
print('hello world'.capitalize())

#* string.count() - считает количество вхождений заданного элемента в строку
print('Hello world, this is ADA Courses'.count('l')) #* 3
print('Hello world, this is ADA Courses'.count('hello')) #* 1

#* string.startswith - метод, который проверяет начинается ли строка с заданного элемента
print('hello, World!'.startswith('h')) #* True
print('hello, World!'.startswith('hello')) #* True

#* string.endswith - метод, который проверяет заканчивается ли строка с заданного элемента
print('hello, World!'.endswith('hello')) #* False
print('hello, World!'.endswith('ld!')) #* True

#* string.islower() - метод, который проверяет находится ли вся строка в нижнем регистре
print('hello, world!'.islower()) #* True
print('hello, World!'.islower()) #* False

#* string.isupper() - метод, который проверяет находится ли вся строка в верхнем регистре
print('hello, world!'.isupper()) #* False
print('HELLO, WORLD!'.isupper()) #* TRUE

#* string.isdigit() - метод, который проверяет состоит ли вся строка в из чисел
print('1234'.isdigit()) #* True
print('1234k'.isdigit()) #* False

#* string.isalpha() - метод, который проверяет состоит ли вся строка в из букв
print('1234'.isalpha()) #* False
print('hello'.isalpha()) #* True

#* string.isallnum() - метод, которые проверяет состоит ли вся строка из букв и чисел
print('Hello1234'.isalnum()) #* True
print('Hello'.isalnum()) #* False
print('1234'.isalnum()) #* False

#* string.strip() - метод, который полностью удаляет все пробелы сначала и сконца строки, середину не трогает
string1 = '            hello world                 '
print(len(string1.strip())) #* 11
print(len(string1)) #* 40

#* string.rstrip() - метод, который полностью удаляет пробелы справа
print(len('hello                           '.rstrip())) #* 5
print(len('hello                           ')) #* 32


#* string.lstrip() - метод, который полностью удаляет пробелы слева
print(len('                  hello'.lstrip())) #* 5
print(len('                  hello')) #* 23

