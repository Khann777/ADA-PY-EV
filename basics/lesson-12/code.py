
#? 8) Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключения ValueError и ZeroDivisionError, выводя сообщение "".

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError) as err:
#     print(type(err).__name__, '- Произошла ошибка!')

#? 9) Напишите код, который принимает сумму денег от пользователя и выбрасывает исключение ValueError с сообщением "Сумма не может быть отрицательной!", если сумма меньше 0. Обработайте это исключение и выведите сообщение ошибки. Если исключение не возникло, выведите сумму.

# try: 
#     num1 = float(input('Введите первое число: '))
#     if num1 < 0:
#         raise ValueError()
# except:
#     print('Введите корректное число!')
# else:
#     print("Сумма: ", num1)

#? 10) Напишите код, который пытается сложить строку и число. Обработайте исключение TypeError, выводя сообщение "Unsupported option"

# num1 = 1
# str1 = 'str1'
# try:
#     print(num1 + str1)
#     raise TypeError
# except:
#     print("Unsupported option")

#? 11) Напишите код, который пытается расширить список, который не был создан. Обработайте исключение NameError, и выведите сообщение 'list does not exist'.

# try:
#     list1.extend(1)
#     raise NameError
# except:
#     print('List does not exist')

#? 12) Напишите код, который перебирает элементы списка, превышая его длину. Обработайте исключение IndexError, не выполняя никаких действий при возникновении ошибки.

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# try:
#     for i in range(0, len(list1) + 1):
#         print(list1[i])
# except IndexError:
#     print('Index out of range!')

#? Напишите код, который проверяет длину хранилища и выбрасывает исключение ValueError, если длина больше 10. Также выбрасывайте исключение ValueError, если какой-либо вложенный список внутри хранилища имеет длину больше 3.

# warehouse = [
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     ['1', '2', '3'],
#     [1, 2, 3, 4 , 5, 6],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]

# if len(warehouse) > 10:
#     raise ValueError('Длина больше 10')
# else:
#     for i in warehouse:
#         if len(i) > 3:
#             raise ValueError('Длина больше 3')
#         for j in i:
#             if len(j) > 3:
#                 raise ValueError('Длина больше 3 опять')

#? Напишите код, который уменьшает значение переменной в цикле while. Обработайте исключение KeyboardInterrupt, выводя сообщение "Nope".

# a = 10
# try:
#     while True:
#         a -= 1
#         print(f"Текущее значение: {a}")
# except KeyboardInterrupt:
#     print('Nope')

#?  Напишите код, который принимает строку, разделяет её на элементы и пытается преобразовать каждый элемент в целое число, добавляя его в список. Если элемент не является числом, выбрасывайте исключение ValueError с сообщением "Данный элемент не является числом!".

# try:
#     str1 = input('Введите строку: ')
#     list1 = []
#     for i in str1:
#         if type(i) != int:
#             list1.append(int(i))
#         else:
#             raise ValueError
#     print(list1)
# except ValueError:
#     print('Данный элемент не является числом!')

