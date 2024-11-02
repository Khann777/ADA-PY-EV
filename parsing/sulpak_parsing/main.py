import requests
from bs4 import BeautifulSoup as BS
import json
from multiprocessing import Pool
from time import time

URL = 'https://www.sulpak.kg/f/'
def get_html(category: str, page: int = 1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(f'{URL}{category}', params={'page': page}, headers=headers)
    if response.status_code == 200:
        return response.text
    raise Exception('Произошла ошибка!')

def get_cards(html: str):
    soup = BS(html, 'lxml')
    return soup.find_all('div', class_='product__item product__item-js tile-container')

def parse_cards(cards: list) -> list:
    data = []
    try:
        for card in cards:
            data.append({
                'title': card.get('data-name'),
                'price': card.get('data-price'),
                'brand': card.get('data-brand'),
                'in_stock': card.find('div', class_='product__item-showcase').text if card.find('div', class_='product__item-showcase') else 'Нет в наличии',
                'product_link': 'https://www.sulpak.kg' + card.find('div', class_='product__item-name').find('a').get('href')
            })
        return data
    except Exception as e:
        print(f"Что-то пошло не так {e}")
        return []

def get_last_page(category: str) -> int:
    html = get_html(category)
    soup = BS(html, 'lxml')
    last_page = soup.find('div', class_='pagination').get('data-pagescount')
    return int(last_page)

def save_to_json(data: list, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def benchmark(func):
    def wrapper(*a,**k):
        start = time()
        func(*a,**k)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функции: {total_time} секунд')
    return wrapper

@benchmark
def main(category: str) -> None:
    data = []
    last_page = get_last_page(category)
    
    for page in range(1,last_page + 1):
        html = get_html(category, page)
        cards = get_cards(html)
        data.extend(parse_cards(cards))
    
    save_to_json(data, f'{category}.json')


# Функция для работы с каждой страницей
def process_page(args):
    category, page = args
    html = get_html(category, page)
    cards = get_cards(html)
    return parse_cards(cards)

@benchmark
def fast_main(category: str) -> None:
    last_page = get_last_page(category)
    
    # Создаем список аргументов для каждой страницы
    pages = [(category, page) for page in range(1, last_page + 1)]
    
    # Создаем пул процессов и запускаем их
    with Pool(processes=8) as pool:
        results = pool.map(process_page, pages)
    
    # Объединяем все результаты в один список
    data = [item for sublist in results for item in sublist]
    save_to_json(data, f'{category}.json')

# if __name__ == '__main__':
#     fast_main('holodilniki') # Время выполнения функции: 1.8776378631591797 секунд


main('holodilniki') # Время выполнения функции: 4.47379207611084 секунд
