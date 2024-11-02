"=======================================Модули и пакеты==================================="
# любой файл с расширением .py - модуль

# пакет - набор модулей (обязательно должен быть файл __init__.py)
"=======================================Работа с файлами=================================="
# open - функция, которая открывает файл в определенном режиме
"режимы:"
"""
r - read (открываем файл только для чтения, методы для записи работать не будут)
w - write (открываем файл только для записи, при каждом запуске файл очищается и записываются новые данные)
a - append (открываем файл для дозаписи, новые данные записываются в конец и не стриаются как в случае с режимом "w")
x - Создает новый файл, но если такой файл уже существует то выйдет ошибка
b - binary (файл в бинарном виде)
"""

"==========================================Read=============================================="
file = open('test.txt', 'r')
# print(file) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# print(dir(file))

# writable - метод, который возвращает True если в файл можно что-то записать, и False - если файл только для чтения 
# print(file.writable()) # False

# readable() - метод который так-же возвращает булевые значения (True/False), но проверяет, можно ли считать файл
# print(file.readable()) # True

# read() - метод который считывает весь файл, и возвращает тип данных str (если режим выбран "w", то этот метод будет недоступен
print(file.read())
print(file.read()) # '' - возвращается пустота, потому что каретка находится в конце

# метод seek() переносит каретку на указанную позицию, 0 - самое начало
file.seek(0)
print(file.read(5)) # hello
file.seek(0)
# print(file.read(7))

# readlines() - метод, который считывает весь файл и возвращает список со строками
print(file.readlines()) # ['hello\n', 'ada\n', 'courses']

# readline() - считывает одну строку и возвращает тип данных str

file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
# close() - метод который позволяет закрыть файл, и сделать его недоступным для работы, если не закрыть врчную через close(), то файл будет постоянно открыт
file.close()
"=======================================Write===================================="
# file.read() # ValueError: I/O operation on closed file.
"""
в режиме w если указанного файла не существует, то он создается автоматически, если же файл существует, то он стирает все, и записывает новые данные

write() - метод который принимает строку, и записывает ее в файл

writelines() - метод, который принимает список из строк, и записывает в файл

"""
file2 = open('test2.txt', 'w')
file2.write('hello\n')
file2.write('world\n')

file2.writelines(['hello\n', 'my\n', 'name\n', 'is\n', 'nikita'])
file2.close()
"===================================Append===================================="
file3 = open('test3.txt', 'a')
print(file3.readable()) # False
file3.write('Lections EVENING')

file3.writelines(['Nikita\n'])
"========================================Контекстный менеджер========================"
# конструкция with ... as ...

with open('test3.txt', 'r') as file4:
    print(file4.read())

# file4.read()
# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.
with open('test.txt', 'r') as file:
    content = file.read()

if 'w' in content:
    print('Да')
else:
    print('Нет')


# 4) Создайте текстовый файл python.txt и запишите в него текст #1 из github: Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и 
#   выведите на экран все полученные слова.
text = """
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
"""

with open('task4.txt', 'w') as file:
    file.write(text)

with open('task4.txt', 'r') as file:
    content = file.read()

o_words = [word for word in content.split() if 'o' in word]
print(o_words)

# 5)  Возьмите текст №2(GitHub), запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.

text2 = """
.detacilpmoc naht retteb si xelpmoC
.xelpmoc naht retteb si elpmiS
.ticilpmi naht retteb si ticilpxE
.ylgu naht retteb si lufituaeB
"""


with open('task5.txt', 'w') as file:
    file.write(text2)

with open('task5.txt', 'r') as file:
    content = file.read()
    reversed_content = content[::-1]
    print(reversed_content)

# 6) Создайте файл и запишите туда текст №3(github). В каждой строчке есть цифры, которые вместе дадут число. Посчитайте сумму всех чисел.

text3 = """
123
aaa456
fxdya 5 0 0
"""

with open('task6.txt', 'w') as file:
    file.write(text3)

total_sum = 0
with open('task6.txt', 'r') as file:
    for i in file.read():
        if i.isdigit():
            total_sum += int(i)
    print(total_sum)
    