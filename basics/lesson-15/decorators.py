
#! ==========================================Decorators======================================== 
# Функция высшего порядка - функция, которая принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию, возвращает функцию

# Декораторы - функция высшего порядка, которая нужна чтобы расширять функционал функции, не изменяя её функционал (функция-обёртка)

# как пишутся декораторы

def time_decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print(f'start: {datetime.now()}')
        func(*args, **kwargs)
        print(f'finish: {datetime.now()}')
    return wrapper

@time_decorator
def hello():
    print('hello')
# hello()

def func_total_time(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime('%d.%m.%Y %H:%M')
        print(f'Функция запущена: {correct_format}')
        func(*args, **kwargs)
    return wrapper

@func_total_time
def iterate_list(list_):
    for i in list_:
        print(i)

# iterate_list([1,2,3,4,5,6,7,8,9,0])

def iter_decorator(num):
    def inner_decorator(func):
        def wrapper(*a, **k):
            for i in range(num):
                func(*a, **k)
        return wrapper
    return inner_decorator

@iter_decorator(100)
def hello():
    print('Hello')

# hello()

from time import time
import requests

def benchmark(func):
    def wrapper(*a,**k):
        start = time()
        func(*a,**k)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функции: {total_time} секунд')
    return wrapper

@benchmark
def iter_range():
    count = 0
    for i in range(1, 1000001):
        count += i
    print(count)
# iter_range()

@benchmark
def fetch_webpage():
    webpage = requests.get('http://youtube.com/')
fetch_webpage()