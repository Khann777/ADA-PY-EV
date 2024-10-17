
#!  ===============================================Числа============================================
#* integer(int) - целые числа
#* num1 = 12
#* type() - функция, которая возвращает тип данных объекта
#* print(type(num1)) #* <class 'int'>

#* num_str = '10'
#* print(type(num_str)) #* <class 'str'>
#* num2 = int(num_str)
#* print(num2)
#* print(type(num2)) #* <class 'int'>


#* float - вещественные числа

#* float_number = 10.5
#* print(type(float_number)) #* <class 'float'>

#* float_str = '45.12'
#* new_float = float(float_str)
#* print(new_float)
#* print(type(new_float))

#* decimal - точное вещесвенное(дробное) число
#* Чтобы использовать decimal, нужно его импортировать

#* from decimal import Decimal
#* import decimal
#* decimal_num = Decimal('0.1')
#* float_num = 0.1
#* print(float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num + float_num) #* 0.9999999999999999

#* print(decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num + decimal_num) #* 1.0

#* binary(bin) - числа в двоичной системе исчесления

#* binary_num = bin(255)
#* print(binary_num) #* 0b11111111

#* hex - 16-ная система исчесления

#* hex_num = hex(255)
#* print(hex_num)

#!=====================================Операции над числами=========================================

5 + 7 #* Сложение
7 - 5 #* Вычитание
2 * 5 #* Умножение
4 / 2 #* 2.0 Деление (выводит с остатком)
4 // 2 #* 2 Целочисленное деление
5 % 2 #* 1 Остаток от деление
2 ** 3 #* 8 Возведение в степень
25 ** 0.5 #* 5 Нахождение квадратного корня числа

#* Модуль числа - перевод из отрицательного числа в положительное
#* abs() - находит модуль числа
negative_num = -1000
possitive_num = abs(negative_num)
print(negative_num) #* -1000
print(possitive_num) #* 1000
print(abs(-0.1)) #* 0.1
print(abs(10)) #* 10

#* round() - функция для округления числа
print(round(5.6)) #* 6 (Округление в большую сторону)
print(round(5.4)) #* 5 (Округление в меньшую сторону)
print(round(5.5)) #* 6 (Округлит до 6)
print(round(49.49)) #* 49 (Округление идет только по первой цифре после точки)

#* Можно указать количество цифр после запятой
print(round(10.0476, 2)) #* 10.05

#* sqrt() - функция, для нахождения квадратного корня числа (его нужно импортировать)

from math import sqrt

print(sqrt(25)) #* 5.0
print(25 ** 0.5) #* 5.0
print(sqrt(1000)) #* 31.622776601683793

#* pow():
#* 1) Возводит число в степень
#* 2) Находит остаток от деления на 3 число

print(pow(10, 2)) #* 100 (Запись аналогична: 10 ** 2)
print(pow(10,2,3)) #* 1 (Запись аналогична: 10 ** 2 % 3)

#* divmod() - функция, которая возвращает 2 числа, где 1 число - целая часть от деления, а второе - остаток от деления

print(divmod(5,2)) #* (2, 1)
 