import lxml
from bs4 import BeautifulSoup as BS
import csv
import requests
from multiprocessing import Pool
from time import time

URL = 'https://www.kivano.kg/mobilnye-telefony'

def get_html(url: str, page: int = 1) -> str:
    response = requests.get(url, params={'page': page})
    if response.status_code == 200:
        return response.text
    raise Exception('Произошла ошибка!')


def get_data(html: str) -> list:
    soup = BS(html, 'lxml')
    return soup.find_all('div', class_='item product_listbox oh')


def parse_data(smartphones: list) -> list:

    for smartphone in smartphones:
        try:
            title = smartphone.find('div', class_='listbox_img pull-left').find('a').find('img').get('alt')

            image = smartphone.find('div', class_='listbox_img pull-left').find('a').find('img').get('src')
            image = f'https://kivano.kg{image}'

            price = smartphone.find('div', class_='pull-right rel').find('div', class_='motive_box pull-right').find('div', class_='listbox_price text-center').find('strong').text

            link = smartphone.find('div', class_='pull-right rel').find('div', class_='product_text pull-left').find('div', class_='listbox_title oh').find('a').get('href')
        except Exception as e:
            print(f"Что-то пошло не так {e}")
            return []
        
        data = {
            'title': title,
            'image': image,
            'price': price,
            'link': f'https://kivano.kg{link}'
        }

        write_csv(data)

def get_last_page(url: str) -> int:
    html = get_html(url)
    soup = BS(html, 'lxml')
    last_page = soup.find('div', class_='pager-wrap').find('ul', class_='pagination pagination-sm').find('li', class_='last').find('a').text
    return int(last_page)

def write_csv(data):
    with open('smartphones.csv', 'a') as csv_file:
        names = ('title', 'price', 'image', 'link')
        writer = csv.DictWriter(csv_file, delimiter='|' ,fieldnames=names)
        writer.writerow(data)

def benchmark(func):
    def wrapper(*a,**k):
        start = time()
        func(*a,**k)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функции: {total_time} секунд')
    return wrapper

# Функция для работы с каждой страницей
def process_page(args):
    url, page = args
    html = get_html(url, page)
    cards = get_data(html)
    return parse_data(cards)

@benchmark
def fast_main(url: str) -> None:
    last_page = get_last_page(url)
    
    # Создаем список аргументов для каждой страницы
    pages = [(url, page) for page in range(1, last_page + 1)]
    
    # Создаем пул процессов и запускаем их
    with Pool(processes=8) as pool:
        pool.map(process_page, pages)

if __name__ == '__main__':
    fast_main(URL) 
