
#! ====================================Exception===============================================
#* Исключения (ошибки) - объекты, которые прерывают работу кода, если они не обработаны

#* SyntaxError
#* Исключение, которое выходит когда в коде допущена синтаксическая ошибка
#* (
    #* SyntaxError: '(' was never closed
#* '
    #* SyntaxError: EOL while scanning string literal
#* a = 

#* NameError
#* Исключение, которые выходит когда мы обращаемся к несуществующей переменной
#* print(a)
#* NameError: name 'a' is not defined

#* IndexError
#* Исключение, которое выходит когда мы обращаемся к несуществующему индексу
#* list1 = [1,2,3,4,5]
#* print(list1[1000])
#* IndexError: list index out of range

#* KeyError
#* Исключение, которое выходит когда мы обращаемся по несуществующему ключу
dict1 = {1: 1, 2: 2}
#* print(dict1[1999])
#* KeyError: 1999

#* ValueError
#* Исключение, которое возникает, когда мы передаем в функцию некорректный для нее тип данных
#* int('sadasd')
#* ValueError: invalid literal for int() with base 10: 'sadasd'

#* Когда мы распаковываем итерируемый объект на несколько переменных и количество переменных не совпадает с количеством элементов в итерируемом объекте
#* a, b = [1]
#* ValueError: not enough values to unpack (expected 2, got 1)

#* IndentationError
#* Исключение, которое выходит мы неправильно используем отступы
    #* a = 5
#* IndentationError: unexpected indent
#* for i in range(5):
#* print(i)
#* IndentationError: expected an indented block

#* TypeError
#* Когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

#* for i in 123:
#*    ...
#* TypeError: 'int' object is not iterable
#* "5" + 5
#* TypeError: can only concatenate str (not "int") to str
#* 4 + '5'
#* TypeError: unsupported operand type(s) for +: 'int' and 'str'
#* [1,2,3]: 12}
#* TypeError: unhashable type: 'list'
#* input('Введи цифру', 1)
#* TypeError: input expected at most 1 argument, got 2

#* Exception
#* Исключение, которое создали, чтобы его вызывали

#! =================================Вызов исключений===========================================
#* raise NameError('Hello World')
#* NameError: Hello World

#! ==============================Обработка исключений==========================================
#*  Чтобы код не прекращал работу, мы можем использовать конструкцию try except и обрабатывать вызванное исключение

#* try:
#*     #* код который возможно выведет ошибку
#*     num = int(input('Введите число: '))
#* except ValueError: #* ошибка которая может возникнуть
#*     print('Вы ввели не число')
#* else:
#*     #* Код, который отработает только если ошибка не вышла
#*     print(num)
#* finally: 
#*     #* Код, который отработает в любом случае
#*     print("До свидания")

#* try: 
#*     raise ValueError('Error')
#* except (SyntaxError, NameError, ValueError):
#*     print('Вышла одна из указанных ошибок') 

#* try:
#*    raise TypeError('Type Error')
#* except Exception as error:
#*    print('Ошибка: ', type(error).__name__)

