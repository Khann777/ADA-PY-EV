"""
Напишите мини-проект “Калькулятор”. Для этого, вам
необходимо вспомнить стандартный ввод и вывод данных, тип
данных Числа и операции над числами. Также вам потребуется
помощь условных операторов и циклов.
Требования:
1. Ваш калькулятор должен запрашивать последовательно
первое число, затем второе число. Затем калькулятор должен
запросить операцию, которую он произведет с числами (сложение,
вычитание, умножение, деление, остаток от деления, возведение в
степень, целочисленное деление)
2. Далее калькулятор выдает вам ответ.
3. Если пользователь вводит несуществующую операцию,
калькулятор выводит сообщение: “Данной операции нет в системе”
3. После того, как действие над числами было проведено, и ответ вернулся. Работа калькулятора не должна быть окончена. В терминале должно выйти собщение "Хотите продолжить?", если ответ "yes", то калькулятор снова должен запросить 2 числа и операцию над ними. Если ответ "no", то работа калькулятора должна быть завершена, и должно выйти сообщение "До свидания!".

Пример:
Ввод:
Введите первое число: 3
Введите второе число: 7
Выберите операцию из следующих +-*/%// : *
Вывод:
Ответ: 21
Ввод:
Хотите продолжить(yes/no)?: yes
Введите первое число: 5
Введите второе число: 5
Выберите операцию из следующих +-*/%// : +
Вывод:
Ответ: 10
Хотите продолжить(yes/no)?: no
Вывод: До свидания!
Пример:
Ввод:
Введите первое число: 3
Введите второе число: 7
Выберите операцию из следующих +-*/%// : =
Вывод:
Ответ: Данной операции нет в системе
"""

from .decorators import time_decorator

def plus(num1, num2):
    result = num1 + num2
    return result
def minus(num1, num2):
    result = num1 - num2
    return result
def multiply(num1, num2):
    result = num1 * num2
    return result
def divide(num1, num2):
    result = num1 / num2
    return result
def reminder(num1, num2):
    result = num1 % num2
    return result
def exponentiation(num1, num2):
    result = num1 ** num2
    return result
def int_division(num1, num2):
    result = num1 // num2
    return result

@time_decorator
def calculator(num1, num2, operation):
    if operation == 1:
        print('Сложение')
        result = plus(num1, num2)
    if operation == 2:
        print('Вычитание')
        result = minus(num1, num2)
    if operation == 3:
        print('Умножение')
        result = multiply(num1, num2)
    if operation == 4:
        print('Деление')
        result = divide(num1, num2)
    if operation == 5:
        print('Остаток от деления')
        result = reminder(num1, num2)
    if operation == 6:
        print('Возведение в степень')
        result = exponentiation(num1, num2)
    if operation == 7:
        print('Целочисленное деление')
        result = int_division(num1, num2)
    print('Результат: ', result)

print("Добро пожаловать в калькулятор.\nВам нужно сначала ввести первое число, затем второе, после номер операции.")
try:
    while True:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        print('Операции:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - остаток от деления\n6 - возведение встепень\n7 - целочисленное деление\n0 - остановить калькулятор')
        operation = int(input('Введите номер операции: '))
        if operation == 0:
            break
        elif operation > 7:
            print('Данной операции не существует. Выберите операцию из существующих')
        else:
            calculator(num1, num2, operation)
            answer = input('Хотите продолжить? ')
            if answer.lower() != 'yes' or answer.lower() != 'да':
                print('До свидания!')
                break
except (KeyboardInterrupt, ValueError, ZeroDivisionError) as err:
    print(type(err).__name__, '- Ошибка')